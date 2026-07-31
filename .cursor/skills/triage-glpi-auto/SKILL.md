---
name: triage-glpi-auto
description: Triage automático de tickets GLPI (Sidesoft) para ejecución programada sin supervisión humana. Filtra tickets Nuevos por el proyecto GLPI configurado en .cursor/config/cliente.json (vía el proyecto asignado al solicitante), invoca el motor de análisis funcional de 9 pasos (openbravo-functional-ticket-analysis), evalúa acertividad de la respuesta, aplica preguntas de aclaración cuando el contexto es insuficiente, y publica followups en GLPI.
---

# Agente de Triage GLPI — ejecución automática (cron)

Este proceso corre sin intervención humana en cada ejecución programada.
No requiere frase disparadora ni confirmación — se ejecuta completo de inicio a fin cada vez que el Automation corre.

MCP-DB (alias `glpi`) se usa para leer y escribir directamente sobre la base de datos.

**Esta skill SIEMPRE invoca `openbravo-functional-ticket-analysis` como motor principal de diagnóstico** — no se activa por frase disparadora en este contexto automático, se ejecuta directo como parte del Paso 3 de este flujo.

## Alcance de prueba (mientras no se indique lo contrario)

- Solo procesar tickets con ID **9477 , 9478, 5388**.
- Cualquier otro ticket_id: ignorarlo por completo, no clasificar, no escribir nada.
- Nunca modificar el **estado (status)** del ticket — restricción dura, no cambia nunca.

---

## Paso 0 — Leer el config del repo/cliente

Antes de consultar GLPI, leer `config_agent_support/cliente.json` en la raíz del repo:

```json
{
  "cliente": "Unnoparts",
  "proyecto_glpi_nombre": "UNNOPARTS",
  "mcp_alias": "glpi"
}
```

El valor `proyecto_glpi_nombre` se usa como filtro en el Paso 1. Cada repo/cliente tiene su propio `cliente.json` dentro de `config_agent_support/` con su nombre de proyecto — esto es lo que permite reutilizar la misma skill en distintos repos sin tocar el SQL.

## Paso 1 — Leer el ticket y su historial de followups

Vía MCP-DB (herramienta de consulta expuesta por el MCP `glpi`):

**Importante:** el proyecto GLPI no se vincula al ticket — se vincula al **solicitante**, vía el campo plugin `glpi_plugin_fields_userproyectorelacionadousers`. Por eso el filtro de proyecto se hace a través del join con el solicitante (`tu.users_id`), no con el ticket directamente. Esto también resuelve el caso de varios solicitantes distintos dentro del mismo proyecto: cualquiera de ellos que tenga el proyecto asignado en su perfil, queda incluido automáticamente.

```sql
SELECT
  t.id AS ticket_id, t.name AS titulo, t.content AS descripcion_html,
  u.name AS solicitante, tu.users_id AS solicitante_id,
  COALESCE(c.name,'Sin categoría') AS categoria,
  t.date AS fecha_apertura,
  CASE t.status WHEN 1 THEN 'Nuevo' ELSE 'Otro' END AS estado,
  COALESCE(pr.name,'') AS proyecto
FROM glpi_tickets t
LEFT JOIN glpi_tickets_users tu ON tu.tickets_id = t.id AND tu.type = 1
LEFT JOIN glpi_users u ON u.id = tu.users_id
LEFT JOIN glpi_itilcategories c ON c.id = t.itilcategories_id
-- Proyecto relacionado al SOLICITANTE (no al ticket)
LEFT JOIN glpi_plugin_fields_userproyectorelacionadousers up
  ON up.items_id = tu.users_id
LEFT JOIN glpi_projects pr
  ON pr.id = REPLACE(REPLACE(REPLACE(up.projects_id_proyectorelacionadouserfield, '"', ''), '[', ''), ']', '')
WHERE pr.name = '{proyecto_glpi_nombre}'   -- viene de config_agent_support/cliente.json
  AND t.status = 1
  AND t.id IN (9477, 9478, 5388);  -- whitelist de prueba, temporal — quitar esta línea cuando se libere a producción
```

Si un solicitante puede tener **más de un proyecto asignado** en el campo plugin (multi-selección), avisar para cambiar el `REPLACE` por una comparación tipo `FIND_IN_SET` — tal como está, asume un solo valor por campo.

```sql
SELECT id, users_id, content, is_private, date_creation
FROM glpi_itilfollowups
WHERE items_id IN (9477, 9478, 5388) AND itemtype = 'Ticket'
ORDER BY date_creation ASC;
```

Limpiar el HTML de `descripcion_html` y de cada `content` (quitar tags, decodificar entidades) antes de analizar.

Si existe la tabla `sidesoft_triage_glpi_log`, revisar el último registro por `ticket_id` para saber en qué punto del flujo quedó ese ticket (ver Paso 2).

---

## Paso 2 — Determinar en qué punto del flujo está el ticket

Evaluar en este orden:

### 2.1 — ¿Ya se enviaron preguntas de aclaración antes?
Buscar entre los followups un comentario público que inicie con el marcador `[TRIAGE-ACLARACION]`.

- **No existe ese marcador** → ir a 2.3 (evaluación de suficiencia de contexto, primera pasada).
- **Existe** → ir a 2.2.

### 2.2 — ¿El solicitante ya respondió después de esas preguntas?
Buscar followups con `date_creation` posterior al comentario `[TRIAGE-ACLARACION]` y `users_id` distinto de 148 (`bot.glpi`), es decir, del solicitante u otro usuario real.

- **No hay respuesta posterior** → el ticket sigue esperando al cliente. **Registrar en el log `estado_procesamiento = 'esperando_respuesta_cliente'` y terminar sin publicar ningún comentario nuevo.** No repetir preguntas ya enviadas.
- **Sí hay respuesta posterior** → tomar ese contenido como **"respuesta de aclaración"**, combinarlo con la descripción original del ticket como contexto ampliado, y continuar directo al **Paso 3** (saltar 2.3, el contexto ya se dio por bueno una vez que el cliente respondió).

### 2.3 — Evaluar si el contexto es suficiente (primera pasada, sin preguntas previas)
Aplicar el **Paso 0 / 0B** de la skill `openbravo-functional-ticket-analysis` (normalización) sobre la descripción del ticket. Contar cuántos de estos campos quedan en "No indicado":

- Resultado esperado
- Resultado actual / mensaje de error
- Pasos para reproducir
- Documentos/datos clave

- **3 o más en "No indicado"** → contexto insuficiente → ir a **Paso 2.4 (preguntas de aclaración)**.
- **2 o menos** → contexto suficiente → ir directo al **Paso 3**.

### 2.4 — Generar preguntas de aclaración (máximo 8, técnico-funcionales)
- Redactar entre 3 y 8 preguntas concretas, orientadas a cerrar exactamente los campos que quedaron ambiguos (no preguntas genéricas tipo "¿puede dar más detalles?").
- Publicar **un único comentario público**, iniciando con el marcador literal `[TRIAGE-ACLARACION]` (puede quedar visible, no es necesario ocultarlo), listando las preguntas en formato numerado, tono profesional, sin tecnicismos internos.
- **No aplicar ningún otro comentario en esta corrida** (ni el de primer contacto, ni el de SLA, ni el análisis de 9 pasos, ni el score). Este ticket se retoma solo cuando el cliente responda (ver 2.2).
- Registrar en `sidesoft_triage_glpi_log`: `estado_procesamiento = 'preguntas_enviadas'`.
- Terminar el procesamiento de este ticket en esta corrida.

---

## Paso 3 — Ejecutar el análisis funcional completo (motor: `openbravo-functional-ticket-analysis`)

Invocar el flujo completo de 9 pasos de esa skill, usando como entrada:
- La descripción original del ticket, y
- Si se venía del camino 2.2, también la respuesta de aclaración del cliente, combinada en el mismo contexto de análisis.

Producto esperado: el documento completo de 9 secciones (Clasificación, Entendimiento, Diagnóstico técnico, Causa raíz, Plan de solución, Escalamiento, **Respuesta sugerida al usuario final — §7**, Prevención, Datos faltantes), siguiendo el subtipo que corresponda (Incidencia o Viabilidad) tal como esa skill lo define.

---

## Paso 4 — Publicar los comentarios (sin confirmación — ejecución automática)

Ejecutar en este orden. `users_id = 148` = usuario `bot.glpi`.

### 4.1 — Comentario público: primer contacto (formato sin cambios)
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_primer_contacto}', 0, 0, NOW(), NOW(), 1);
```

### 4.2 — Comentario privado: SLA / criticidad (formato sin cambios)
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_sla_html}', 1, 0, NOW(), NOW(), 1);
```

### 4.3 — Comentario privado NUEVO: detalle completo de los 9 pasos
Contenido: el documento completo generado en el Paso 3 (las 9 secciones tal cual las produce `openbravo-functional-ticket-analysis`), en HTML legible (títulos, listas). Audiencia: consultor/soporte técnico — sí puede incluir SQL, IDs, nombres de módulo.
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_analisis_9_pasos_html}', 1, 0, NOW(), NOW(), 1);
```

### 4.4 — Comentario privado NUEVO: score de acertividad (0–100)
Evaluar **exclusivamente la sección §7** (Respuesta sugerida al usuario final) del análisis del Paso 3, y asignar un puntaje 0–100 según estos criterios:

| Rango | Criterio |
|---|---|
| 90–100 | Veredicto/diagnóstico con evidencia directa de módulo o código confirmado (`docs_customization/knowledge` o código citado), sin datos faltantes, procedimiento accionable completo |
| 70–89 | Diagnóstico con buena evidencia pero con 1 supuesto razonable no confirmado en código, o falta 1 dato menor |
| 40–69 | Diagnóstico plausible pero con confianza Media/Baja declarada en el Paso 1/1B, o basado solo en comportamiento core sin confirmar personalización del proyecto |
| 0–39 | Datos insuficientes pese a haber pasado el filtro de contexto, múltiples hipótesis sin evidencia, o sección 9 (Datos faltantes) con elementos críticos pendientes |

Contenido del comentario: el puntaje, una frase justificando el rango, y qué elemento —si lo hay— bajaría o subiría la confianza.

```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_score_acertividad}', 1, 0, NOW(), NOW(), 1);
```

### 4.5 — Comentario público NUEVO (condicional): solo si score > 70
Si el score del paso 4.4 es **mayor a 70**, publicar un comentario público adicional con la sección §7 del análisis, reformateada: lenguaje simple, profesional, sin SQL/IDs/nombres de módulo, en HTML limpio para visualización en GLPI (misma plantilla de tono que ya usa `openbravo-functional-ticket-analysis` en su §7).

```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_publico_respuesta_formateada}', 0, 0, NOW(), NOW(), 1);
```

Si el score es **70 o menor, no publicar este comentario** — el ticket queda con 1 comentario público (primer contacto) y 3 privados (SLA, análisis, score) hasta revisión humana.

### 4.6 — Actualizar campos del ticket — nunca incluir `status`
```sql
UPDATE glpi_tickets
SET itilcategories_id = COALESCE({categoria_id_o_null}, itilcategories_id),
    impact = {impact_id}, priority = {priority_id}, date_mod = NOW()
WHERE id = {ticket_id};
```

**Nota sobre notificación al solicitante**: el INSERT directo en `glpi_itilfollowups` no dispara el correo de notificación de GLPI. Pendiente de confirmar si la API REST está habilitada para ese caso.

---

## Paso 5 — Registrar en el histórico

Insertar UNA fila por ticket procesado en esta corrida (o intento de procesamiento, aunque haya terminado temprano en 2.2 o 2.4):

```sql
INSERT INTO sidesoft_triage_glpi_log
  (ticket_id, estado_procesamiento, nivel_sla, criticidad, area_funcional,
   categoria_glpi, impacto, prioridad,
   followup_publico_id, followup_privado_id,
   followup_analisis_id, followup_score_id, followup_publico_solucion_id,
   score_acertividad, campos_ticket_actualizados,
   respuesta_modelo_raw, resultado, detalle_error)
VALUES
  ({ticket_id}, '{estado_procesamiento}', '{nivel_sla}', '{criticidad}', '{area_funcional}',
   '{categoria_glpi}', '{impacto}', '{prioridad}',
   {followup_publico_id_o_null}, {followup_privado_id_o_null},
   {followup_analisis_id_o_null}, {followup_score_id_o_null}, {followup_publico_solucion_id_o_null},
   {score_acertividad_o_null}, {1_o_0},
   '{json_de_la_clasificacion_completa}', '{ok_o_error}', {detalle_error_o_null});
```

Valores posibles de `estado_procesamiento`: `preguntas_enviadas`, `esperando_respuesta_cliente`, `ok_alta_confianza` (score > 70), `ok_baja_confianza` (score ≤ 70), `error`.

---

## Reglas críticas (aplican siempre, sin excepción)

- Nunca procesar tickets fuera del whitelist (9477, 9478,5388).
- Nunca modificar `status`.
- Nunca inventar nombres de técnicos ni datos que no vengan en el ticket.
- Nunca asignar SLA 1 sin bloqueo total confirmado explícitamente en la descripción.
- Nunca repetir preguntas de aclaración ya enviadas mientras no haya respuesta nueva del solicitante.
- Nunca publicar el comentario público de solución (4.5) si el score de acertividad es 70 o menor.
- Siempre registrar el resultado en `sidesoft_triage_glpi_log`, incluso si el ticket terminó en preguntas o en espera.

---

## Cambio de esquema requerido en `sidesoft_triage_glpi_log`

```sql
ALTER TABLE sidesoft_triage_glpi_log
  ADD COLUMN followup_analisis_id INT NULL,
  ADD COLUMN followup_score_id INT NULL,
  ADD COLUMN followup_publico_solucion_id INT NULL,
  ADD COLUMN score_acertividad INT NULL;
```
