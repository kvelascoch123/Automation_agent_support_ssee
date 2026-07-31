---
name: triage-glpi-auto
description: Agente orquestador de triage automático de tickets GLPI (multi-cliente). Lee tickets Nuevos, resuelve a qué cliente/repo pertenece el solicitante vía registro_clientes/clientes.json, lee el contexto específico de ese cliente vía MCP GitHub (sin clonar), aplica las metodologías de openbravo-triage-tecnico (5 mínimos funcionales, pistas de módulo) y openbravo-soporte-sidesoft (taxonomía de clasificación) junto con el motor común de análisis de 9 pasos (openbravo-functional-ticket-analysis), evalúa acertividad, aplica preguntas de aclaración cuando el contexto es insuficiente, y publica followups en GLPI.
---

# Agente Orquestador de Triage GLPI — ejecución automática (cron)

Este proceso corre sin intervención humana en cada ejecución programada.
No requiere frase disparadora ni confirmación — se ejecuta completo de inicio a fin cada vez que el Automation corre.

Este Automation está vinculado a UN SOLO repo (el **orquestador**) — nunca a los repos de cliente. Los repos de cliente se leen dinámicamente vía MCP de GitHub, según el proyecto del solicitante de cada ticket.

MCP-DB (alias `glpi`) se usa para leer y escribir sobre la base de datos GLPI (compartida por todos los clientes).
MCP de GitHub (`get_file_contents` o equivalente) se usa para leer archivos de los repos de cliente sin clonarlos.

**Esta skill SIEMPRE invoca `openbravo-functional-ticket-analysis` como motor principal de diagnóstico** — no se activa por frase disparadora en este contexto automático, se ejecuta directo como parte del Paso 5 de este flujo.

## Alcance de prueba (mientras no se indique lo contrario)

- Solo procesar tickets con ID **9477, 9478 y 5388**.
- Cualquier otro ticket_id: ignorarlo por completo, no clasificar, no escribir nada.
- Nunca modificar el **estado (status)** del ticket — restricción dura, no cambia nunca.

---

## Paso 0 — Leer el registro de clientes (repo orquestador)

Leer `registro_clientes/clientes.json` en la raíz del repo orquestador (lectura local, es el propio home repo del Automation, no requiere MCP de GitHub):

```json
{
  "UNNOPARTS": {
    "owner": "tuorg",
    "repo": "Unnoparts-Agente-Soporte",
    "openbravo_db_alias": null
  },
  "SAN FELIPE": {
    "owner": "tuorg",
    "repo": "SanFelipe-Agente-Soporte",
    "openbravo_db_alias": null
  },
  "ACTUARIA": {
    "owner": "tuorg",
    "repo": "Actuaria-Agente-Soporte",
    "openbravo_db_alias": null
  }
}
```

`openbravo_db_alias` identifica la BD de Openbravo (PostgreSQL) de ese cliente para verificaciones contables — se deja en `null` hasta que se configure el MCP de Postgres correspondiente (ver Paso 3-B). Mientras esté en `null`, el análisis procede solo con conocimiento estático, sin verificación en BD real.

Este registro es la única fuente de verdad de qué proyectos GLPI están habilitados y a qué repo corresponde cada uno. Agregar un cliente nuevo = una entrada nueva aquí — no requiere tocar esta skill.

También leer, del propio repo orquestador (conocimiento común, aplica a todos los clientes):
- `conocimiento_comun/casos_de_uso_openbravo_erp.md`
- `conocimiento_comun/modulos/01-Facturacion-Electronica.md` … `15-Plataforma-Configuracion.md` (detalle por módulo, ya cargados)
- Las skills `openbravo-triage-tecnico` y `openbravo-soporte-sidesoft` (viven en `.cursor/skills/` del repo orquestador junto a esta)

---

## Paso 1 — Leer tickets nuevos con el proyecto de su solicitante

Vía MCP-DB (alias `glpi`).

**Importante:** el proyecto GLPI no se vincula al ticket — se vincula al **solicitante**, vía el campo plugin `glpi_plugin_fields_userproyectorelacionadousers`. El filtro de proyecto se hace a través del join con el solicitante (`tu.users_id`), no con el ticket directamente. Esto también cubre el caso de varios solicitantes distintos dentro del mismo proyecto: cualquiera de ellos que tenga el proyecto asignado en su perfil queda incluido automáticamente.

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
WHERE t.status = 1
  AND pr.name IS NOT NULL
  AND t.id IN (9477, 9478, 5388);  -- whitelist de prueba, temporal — quitar esta línea cuando se libere a producción
```

Si un solicitante puede tener **más de un proyecto asignado** en el campo plugin (multi-selección), avisar para cambiar el `REPLACE` por una comparación tipo `FIND_IN_SET` — tal como está, asume un solo valor por campo.

Para cada ticket obtenido, traer también su historial de followups:
```sql
SELECT id, users_id, content, is_private, date_creation
FROM glpi_itilfollowups
WHERE items_id = {ticket_id} AND itemtype = 'Ticket'
ORDER BY date_creation ASC;
```

Limpiar el HTML de `descripcion_html` y de cada `content` (quitar tags, decodificar entidades) antes de analizar.

Si existe la tabla `sidesoft_triage_glpi_log`, revisar el último registro por `ticket_id` para saber en qué punto del flujo quedó ese ticket (ver Paso 4).

---

## Paso 2 — Resolver cliente y repo para cada ticket

Por cada ticket obtenido en el Paso 1:

1. Tomar el valor de la columna `proyecto`.
2. Buscarlo como clave exacta en `registro_clientes/clientes.json` (Paso 0).
   - **No existe esa clave** → el proyecto no está habilitado en el registro. Registrar en el log `estado_procesamiento = 'proyecto_no_registrado'` y no procesar más este ticket en esta corrida.
   - **Existe** → obtener `{owner, repo}` de esa entrada y continuar al Paso 3.

---

## Paso 3 — Leer el contexto específico del cliente (sin clonar)

Usando `{owner, repo}` resuelto en el Paso 2, invocar la herramienta MCP de GitHub (`get_file_contents` o la que exponga el MCP configurado) para leer directamente, vía API, sin descargar el repo completo:

- `config_agent_support/cliente.json` (reglas propias del cliente, si difieren del estándar: SLA, umbrales, etc.)
- Archivos de customización/documentación relevantes de ese repo (ej. `customizaciones/*.md`) que ayuden al diagnóstico

Si alguno de estos archivos no existe en ese repo, continuar el análisis solo con el conocimiento común (las skills del repo orquestador) y anotarlo en el comentario privado de análisis del Paso 6.

---

## Paso 3-B — Verificación contable en BD de Openbravo (solo si aplica, y solo lectura)

Si la clasificación del ticket (aplicando la taxonomía de `openbravo-soporte-sidesoft`) resulta **CONTABLE**, y el cliente tiene `openbravo_db_alias` distinto de `null` en el registro:

1. Usar el MCP de PostgreSQL correspondiente para consultar, con `SELECT` filtrado y `LIMIT`, las tablas necesarias (`Fact_Acct`, `C_Invoice`, `C_Payment`, etc.) siguiendo las reglas SQL de `openbravo-soporte-sidesoft`.
2. Usar el resultado real para confirmar o descartar la hipótesis de causa raíz antes de redactar el análisis del Paso 5.
3. Si `openbravo_db_alias` es `null` (MCP aún no configurado para ese cliente), continuar sin esta verificación y anotarlo explícitamente en el comentario privado: *"Diagnóstico basado solo en conocimiento estático — verificación en BD contable no disponible para este cliente."*

**Regla dura**: esta consulta es SIEMPRE de solo lectura. Ningún `INSERT`/`UPDATE`/`DELETE`/`DDL` se ejecuta contra la BD de Openbravo del cliente en modo automático — ver Paso 6-B para cómo se maneja una corrección sugerida.

---

## Paso 4 — Determinar en qué punto del flujo está el ticket

Evaluar en este orden, usando el historial de followups leído en el Paso 1:

### 4.1 — ¿Ya se enviaron preguntas de aclaración antes?
Buscar entre los followups un comentario (privado) que inicie con el marcador `[TRIAGE-ACLARACION]`.

- **No existe ese marcador** → ir a 4.3 (evaluación de suficiencia de contexto, primera pasada).
- **Existe** → ir a 4.2.

### 4.2 — ¿El solicitante ya respondió después de esas preguntas?
Buscar followups con `date_creation` posterior al comentario `[TRIAGE-ACLARACION]` y `users_id` distinto de 148 (`bot.glpi`), es decir, del solicitante u otro usuario real.

- **No hay respuesta posterior** → el ticket sigue esperando al cliente. Registrar en el log `estado_procesamiento = 'esperando_respuesta_cliente'` y terminar sin publicar ningún comentario nuevo. No repetir preguntas ya enviadas.
- **Sí hay respuesta posterior** → tomar ese contenido como **"respuesta de aclaración"**, combinarlo con la descripción original del ticket como contexto ampliado, y continuar directo al **Paso 5** (saltar 4.3, el contexto ya se dio por bueno una vez que el cliente respondió).

### 4.3 — Evaluar si el contexto es suficiente (primera pasada, sin preguntas previas)
Aplicar los **5 mínimos funcionales** de `openbravo-triage-tecnico` sobre la descripción del ticket:

1. Módulo y documento
2. Acción exacta
3. Síntoma literal
4. Resultado esperado vs. obtenido
5. Alcance y entorno

- **Faltan 2 o más** → contexto insuficiente → ir a **4.4 (preguntas de aclaración)**.
- **Faltan 0 o 1** → contexto suficiente → ir directo al **Paso 5**, señalando igual el dato faltante en el comentario privado.

### 4.4 — Generar preguntas de aclaración (máximo 8, técnico-funcionales)
- Usar la **tabla de pistas palabra-clave → módulo** de `openbravo-triage-tecnico` para identificar el módulo probable y orientar las preguntas a cerrar exactamente los mínimos ausentes (no preguntas genéricas tipo "¿puede dar más detalles?").
- Redactar entre 3 y 8 preguntas concretas.
- Publicar **un único comentario PRIVADO** (`is_private = 1`), iniciando con el marcador literal `[TRIAGE-ACLARACION]`, listando las preguntas en formato numerado.
- Las "preguntas que el técnico puede verificar él mismo" y las "sospechas iniciales" (definidas en `openbravo-triage-tecnico`) se incluyen en el mismo comentario privado.
- **No aplicar ningún otro comentario en esta corrida.**
- Registrar en `sidesoft_triage_glpi_log`: `estado_procesamiento = 'preguntas_enviadas'`.
- Terminar el procesamiento de este ticket en esta corrida.

> **⚠️ Limitación conocida al pasar este comentario a privado**: el solicitante NO puede ver comentarios privados en GLPI, por lo tanto nunca verá estas preguntas ni podrá responderlas dentro del ticket. El Paso 4.2 (detectar respuesta del cliente) dejará de poder cumplirse por esta vía — el ticket quedará indefinidamente en `esperando_respuesta_cliente` a menos que se defina otro canal para hacerle llegar las preguntas (correo, WhatsApp, o que un humano las traslade manualmente). Pendiente de resolver.

---

## Paso 5 — Ejecutar el análisis funcional completo (motor: `openbravo-functional-ticket-analysis`)

Invocar el flujo completo de 9 pasos de esa skill (vive en el repo orquestador, es común a todos los clientes), usando como entrada:
- La descripción original del ticket,
- Si se venía del camino 4.2, también la respuesta de aclaración del cliente,
- El contexto específico del cliente leído en el Paso 3,
- El resultado de la verificación en BD contable del Paso 3-B, si aplicó.

**Enriquecimiento con las skills complementarias:**
- En la sección de **Clasificación** (Paso 1 del motor de 9 pasos), agregar también la categoría de `openbravo-soporte-sidesoft`: FUNCIONAL / TÉCNICO / CONFIGURACIÓN / CONTABLE / CAPACITACIÓN.
- En la sección de **Causa raíz**, usar el vocabulario de 5 categorías de `openbravo-triage-tecnico`: configuración faltante, estado del documento, restricción de negocio del sistema, dato del cliente erróneo, o bug real (último recurso).
- Citar por nombre de archivo cualquier caso de uso de `casos_de_uso_openbravo_erp.md` que aplique.

Producto esperado: el documento completo de 9 secciones (Clasificación, Entendimiento, Diagnóstico técnico, Causa raíz, Plan de solución, Escalamiento, **Respuesta sugerida al usuario final — §7**, Prevención, Datos faltantes), siguiendo el subtipo que corresponda (Incidencia o Viabilidad) tal como esa skill lo define.

---

## Paso 6 — Publicar los comentarios, TODOS PRIVADOS (sin confirmación — ejecución automática)

Ejecutar en este orden, vía MCP-DB (`glpi`). `users_id = 148` = usuario `bot.glpi`. **Todos los comentarios de este flujo se publican con `is_private = 1` — ninguno es visible para el solicitante/cliente en GLPI.**

### 6.1 — Comentario privado: primer contacto
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_primer_contacto}', 1, 0, NOW(), NOW(), 1);
```

### 6.2 — Comentario privado: SLA / criticidad
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_sla_html}', 1, 0, NOW(), NOW(), 1);
```

### 6.3 — Comentario privado: detalle completo de los 9 pasos
Contenido: el documento completo generado en el Paso 5, en HTML legible. Audiencia: consultor/soporte técnico — puede incluir SQL, IDs, nombres de módulo.
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_analisis_9_pasos_html}', 1, 0, NOW(), NOW(), 1);
```

### 6.4 — Comentario privado: score de acertividad (0–100)
Evaluar **exclusivamente la sección §7** del análisis del Paso 5, y asignar un puntaje 0–100:

| Rango | Criterio |
|---|---|
| 90–100 | Veredicto con evidencia directa de módulo/código confirmado, sin datos faltantes, procedimiento accionable completo |
| 70–89 | Buena evidencia pero con 1 supuesto razonable no confirmado, o falta 1 dato menor |
| 40–69 | Diagnóstico plausible pero con confianza Media/Baja declarada, o basado solo en comportamiento core sin confirmar personalización del proyecto |
| 0–39 | Datos insuficientes pese a pasar el filtro de contexto, múltiples hipótesis sin evidencia, o Datos faltantes con elementos críticos pendientes |

```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_score_acertividad}', 1, 0, NOW(), NOW(), 1);
```

### 6.5 — Comentario privado (condicional): solo si score > 70
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_publico_respuesta_formateada}', 1, 0, NOW(), NOW(), 1);
```
Si el score es 70 o menor, no publicar este comentario.

### 6.6 — Actualizar campos del ticket — nunca incluir `status`
```sql
UPDATE glpi_tickets
SET itilcategories_id = COALESCE({categoria_id_o_null}, itilcategories_id),
    impact = {impact_id}, priority = {priority_id}, date_mod = NOW()
WHERE id = {ticket_id};
```

**Nota sobre notificación al solicitante**: el INSERT directo en `glpi_itilfollowups` no dispara el correo de notificación de GLPI. Pendiente de confirmar si la API REST está habilitada para ese caso.

### 6-B — Si el análisis produjo un script SQL correctivo sobre el ERP del cliente
Siguiendo la regla dura de `openbravo-triage-tecnico` para modo automático: cualquier `INSERT`/`UPDATE`/`DELETE`/`DDL` sugerido contra tablas del ERP del cliente (`Fact_Acct`, `C_Invoice`, etc.) va **como texto dentro del comentario privado del Paso 6.3** (detalle de los 9 pasos), nunca como acción ejecutada. Encabezar ese bloque con:

```
⚠️ Script sugerido — requiere revisión y ejecución manual de un técnico.
No fue ejecutado automáticamente.
```

Este flujo automático **solo ejecuta escritura** sobre las tablas propias de GLPI (`glpi_itilfollowups`, `sidesoft_triage_glpi_log`) — nunca sobre la base de datos de producción del ERP del cliente.

---

## Paso 7 — Registrar en el histórico

```sql
INSERT INTO sidesoft_triage_glpi_log
  (ticket_id, proyecto_glpi, repo_cliente, estado_procesamiento, nivel_sla, criticidad, area_funcional,
   categoria_glpi, impacto, prioridad,
   followup_publico_id, followup_privado_id,
   followup_analisis_id, followup_score_id, followup_publico_solucion_id,
   score_acertividad, campos_ticket_actualizados,
   respuesta_modelo_raw, resultado, detalle_error)
VALUES
  ({ticket_id}, '{proyecto}', '{owner}/{repo}', '{estado_procesamiento}', '{nivel_sla}', '{criticidad}', '{area_funcional}',
   '{categoria_glpi}', '{impacto}', '{prioridad}',
   {followup_publico_id_o_null}, {followup_privado_id_o_null},
   {followup_analisis_id_o_null}, {followup_score_id_o_null}, {followup_publico_solucion_id_o_null},
   {score_acertividad_o_null}, {1_o_0},
   '{json_de_la_clasificacion_completa}', '{ok_o_error}', {detalle_error_o_null});
```

Valores posibles de `estado_procesamiento`: `proyecto_no_registrado`, `preguntas_enviadas`, `esperando_respuesta_cliente`, `ok_alta_confianza` (score > 70), `ok_baja_confianza` (score ≤ 70), `error`.

---

## Reglas críticas (aplican siempre, sin excepción)

- Nunca procesar tickets fuera del whitelist (9477, 9478, 5388).
- Nunca modificar `status`.
- Nunca inventar nombres de técnicos ni datos que no vengan en el ticket.
- Nunca asignar SLA 1 sin bloqueo total confirmado explícitamente en la descripción.
- Nunca repetir preguntas de aclaración ya enviadas mientras no haya respuesta nueva del solicitante.
- Nunca publicar el comentario de solución (6.5) si el score de acertividad es 70 o menor.
- Todos los comentarios publicados por este flujo son privados (`is_private = 1`) — ninguno llega al solicitante dentro de GLPI.
- Nunca clonar un repo de cliente — siempre leer vía MCP de GitHub, archivo por archivo.
- Nunca procesar un ticket cuyo proyecto no esté en `registro_clientes/clientes.json`.
- Nunca ejecutar (solo sugerir como texto) cualquier `INSERT`/`UPDATE`/`DELETE`/`DDL` sobre la BD de producción del ERP de un cliente — regla dura heredada de `openbravo-triage-tecnico` en modo automático.
- Toda consulta a la BD de Openbravo del cliente (Paso 3-B) es siempre `SELECT`, con filtros y `LIMIT` en tablas de alto volumen.
- Siempre registrar el resultado en `sidesoft_triage_glpi_log`, incluso si el ticket terminó en preguntas, en espera, o sin proyecto registrado.

---

## Cambio de esquema requerido en `sidesoft_triage_glpi_log`

```sql
ALTER TABLE sidesoft_triage_glpi_log
  ADD COLUMN proyecto_glpi VARCHAR(255) NULL,
  ADD COLUMN repo_cliente VARCHAR(255) NULL,
  ADD COLUMN followup_analisis_id INT NULL,
  ADD COLUMN followup_score_id INT NULL,
  ADD COLUMN followup_publico_solucion_id INT NULL,
  ADD COLUMN score_acertividad INT NULL;
```
