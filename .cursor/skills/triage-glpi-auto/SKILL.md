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

Este orquestador **recibe** los tickets a analizar (no los busca en GLPI): por cada ejecución llega un payload ya preparado por n8n con `{ticket_id, texto_limpio, adjuntos}`. La búsqueda de tickets nuevos y la limpieza de HTML/imágenes ya las hizo n8n antes de disparar este Automation. **El proyecto del solicitante no viene en el payload** — este mismo Automation lo resuelve en el Paso 2, consultando GLPI directamente.

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
- Las skills `openbravo-triage-tecnico` y `openbravo-soporte-sidesoft` (viven en `.cursor/skills/` del repo orquestador junto a esta)

**⚠️ Optimización de costo — NO leer todavía los archivos de `conocimiento_comun/modulos/` ni `casos_de_uso_openbravo_erp.md` en este paso.** Son archivos grandes (varios miles de líneas cada uno); cargarlos todos en cada corrida es el mayor gasto de tokens del flujo. Se leen selectivamente, uno a la vez, recién en el Paso 4.3/5 cuando ya se identificó el módulo probable — ver nota ahí.

---

## Paso 2 — Resolver el proyecto del solicitante y el cliente/repo para cada ticket

El payload de entrada solo trae `{ticket_id, texto_limpio, adjuntos}` — el proyecto **no** viene incluido, lo resuelve este mismo paso.

1. Resolver el proyecto del solicitante vía MCP-DB (alias `glpi`). El proyecto GLPI no se vincula al ticket — se vincula al **solicitante**, vía el campo plugin `glpi_plugin_fields_userproyectorelacionadousers`:

```sql
SELECT COALESCE(pr.name, '') AS proyecto
FROM glpi_tickets t
LEFT JOIN glpi_tickets_users tu ON tu.tickets_id = t.id AND tu.type = 1
LEFT JOIN glpi_plugin_fields_userproyectorelacionadousers up
  ON up.items_id = tu.users_id
LEFT JOIN glpi_projects pr
  ON pr.id = REPLACE(REPLACE(REPLACE(up.projects_id_proyectorelacionadouserfield, '"', ''), '[', ''), ']', '')
WHERE t.id = {ticket_id};
```

Si el solicitante puede tener más de un proyecto asignado en el campo plugin (multi-selección), avisar para cambiar el `REPLACE` por una comparación tipo `FIND_IN_SET` — tal como está, asume un solo valor por campo.

Si la consulta no devuelve proyecto (`proyecto` vacío): registrar en el log `estado_procesamiento = 'proyecto_no_registrado'` y no procesar más este ticket en esta corrida.

2. Buscar el proyecto obtenido como clave exacta en `registro_clientes/clientes.json` (Paso 0).
   - **No existe esa clave** → el proyecto no está habilitado en el registro. Registrar en el log `estado_procesamiento = 'proyecto_no_registrado'` y no procesar más este ticket en esta corrida.
   - **Existe** → obtener `{owner, repo}` de esa entrada y continuar al Paso 3.

---

## Paso 3 — Leer el contexto específico del cliente (sin clonar)

Usando `{owner, repo}` resuelto en el Paso 2, invocar la herramienta MCP de GitHub (`get_file_contents` o la que exponga el MCP configurado) para leer directamente, vía API, sin descargar el repo completo:

- `config_agent_support/cliente.json` (reglas propias del cliente, si difieren del estándar: SLA, umbrales, etc.)
- Archivos de customización/documentación relevantes de ese repo (ej. `customizaciones/*.md`) que ayuden al diagnóstico

**Nota:** `graphify-out/` (el grafo de código) vive en el repo del CLIENTE (ej. `Unnoparts-Agente-Soporte`), no en el orquestador — es específico del código de cada instalación de Openbravo. Por eso los comandos `graphify query/path/explain` del Paso 5 solo tienen sentido una vez que el agente está operando en el contexto del cliente correcto (ya resuelto en el Paso 2).

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

Primero, traer el historial de followups del ticket vía MCP-DB (alias `glpi`):

```sql
SELECT id, users_id, content, is_private, date_creation
FROM glpi_itilfollowups
WHERE items_id = {ticket_id} AND itemtype = 'Ticket'
ORDER BY date_creation ASC;
```

Si existe la tabla `sidesoft_triage_glpi_log`, revisar también el último registro por `ticket_id` para saber en qué punto del flujo quedó ese ticket en una corrida anterior.

Con ese historial, evaluar en este orden:

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

**Lectura de conocimiento:**

1. Identifica el módulo/concepto probable con la tabla de pistas de `openbravo-triage-tecnico`.
2. Consulta `graphify-out/` del repo del cliente. Es un paso obligatorio, pero acotado a lo que el grafo realmente puede responder — ver *Qué esperar de graphify* abajo.
3. Lee el código fuente real del cliente vía MCP de GitHub. Para incidencias cuya causa está en la lógica de base de datos, este es el paso que resuelve, no el grafo.

Si algo de esto no se ejecuta, declararlo como omitido en la sección 9 del análisis. **Nunca escribir que se revisó una fuente que no se abrió en esta corrida**, ni apoyarse en la conclusión de una corrida anterior para afirmar evidencia en la actual.

### Qué esperar de graphify (medido sobre el repo de Unnoparts, 2026-08-12)

`graphify-out/` tiene cuatro archivos y **no se leen vía MCP** — se bajan a `/tmp` con `curl` usando el `download_url` del listado de directorio y se procesan en local:

| Archivo | Realidad | Uso |
|---|---|---|
| `graph.json` | puntero **Git LFS a 224 MB** | inaccesible en la práctica, la lectura devuelve solo el puntero |
| `manifest.json` | 2,5 MB, solo ruta + `mtime` + hashes | **el único con valor operativo**: inventario de qué archivos están indexados |
| `.graphify_analysis.json` | 12,4 MB: `communities`, `cohesion`, `gods`, `surprises` | clusters de nodos sin aristas consultables, valor marginal |
| `.graphify_root` | 31 bytes | ninguno |

**Limitante estructural: graphify indexa cero archivos `.xml`.** Como toda la lógica PL/SQL de Openbravo vive en `src-db/database/model/functions/*.xml`, el grafo **no puede ver** triggers ni funciones de base de datos, que son la causa raíz de la mayoría de las incidencias de soporte.

Uso recomendado, barato y con retorno real: filtrar las claves de `manifest.json` por el nombre del módulo sospechoso para saber qué clases Java existen ahí. Eso orienta la lectura de código y a veces destapa una clase relevante que no aparecía en el listado de directorio. Todo lo demás del grafo se puede omitir sin pérdida, dejándolo anotado en la sección 9.

**Procedimiento exacto** — cuesta segundos, no hay razón para saltárselo:

```bash
mkdir -p /tmp/gfy
# el download_url sale del listado de directorio de graphify-out/
curl -sSL -o /tmp/gfy/manifest.json "<download_url de manifest.json>"
python3 -c "
import json,sys
m=json.load(open('/tmp/gfy/manifest.json'))
mod=sys.argv[1]
print('entradas totales:',len(m))
for p in sorted(k for k in m if mod in k): print(' ',p)
" ec.com.sidesoft.pre.cancellations
```

La salida (número de entradas + lista de archivos indexados del módulo) es el **dato probatorio** que exige el registro de evidencia del Paso 5-A.

---

### Paso 5-A — Orden de fuentes, precedencia de la memoria y registro de evidencia

Existe para impedir un fallo concreto ya ocurrido: la memoria del Automation traía la nota *"graphify no aporta nada utilizable"*, se tomó esa conclusión pasada como hecho presente, se omitió un paso obligatorio y **se afirmó en un comentario publicado que sí se había revisado**. La memoria terminó pesando más que la propia skill porque nada decía cuál manda.

#### 1. Regla de precedencia (no admite excepción)

> **La memoria nunca cancela un paso obligatorio. Solo puede cambiar cómo de barato se ejecuta, nunca si se ejecuta.**

La memoria es una caché de conclusiones pasadas, no una fuente de evidencia del caso actual. Una nota de memoria puede decir *qué esperar* y *cómo leerlo barato*. No puede autorizar a no mirar. Si una nota de memoria, leída literalmente, llevaría a saltarse una fuente obligatoria, esa nota está mal escrita: hay que ejecutar el paso igual y reescribir la nota (ver punto 4).

#### 2. Orden obligatorio: primero la fuente, después la memoria

1. **Abrir la fuente primaria** de esta corrida — `graphify-out/` según el procedimiento de arriba, y el código del cliente.
2. **Recién entonces leer la memoria**, para interpretar lo que se acaba de ver, ahorrar exploración y contrastar con corridas anteriores.
3. Si la memoria **contradice** lo observado ahora, gana lo observado ahora. Corregir la memoria en la misma corrida, indicando qué decía, qué se midió y cuándo.

La memoria se consulta *después* justamente para que no pueda sesgar la decisión de mirar o no mirar.

#### 3. Registro de evidencia (obligatorio en la sección 9 del análisis)

Toda fuente obligatoria aparece en esta tabla. Es el mecanismo de control: `LEÍDO` **solo es válido si la tercera columna trae un dato concreto obtenido en esta corrida**. Sin dato, el estado es `OMITIDO`, no `LEÍDO`.

| Fuente | Estado | Dato probatorio de esta corrida |
|---|---|---|
| `graphify-out/manifest.json` | LEÍDO / OMITIDO | nº de entradas y archivos indexados del módulo |
| Código fuente del módulo | LEÍDO / OMITIDO | archivos y funciones concretas abiertas |
| BD del ERP (Paso 3-B) | LEÍDO / NO DISPONIBLE | resultado del SELECT, o el motivo |
| Contexto del cliente (Paso 3) | LEÍDO / OMITIDO | archivo y contenido relevante |

No sirve como dato probatorio: una cita de la memoria, una conclusión de una corrida anterior, ni una descripción genérica del archivo. Sirve un número, un nombre de archivo o un fragmento que solo se puede conocer habiéndolo abierto ahora.

#### 4. Higiene de la memoria

- Redactar toda nota sobre una fuente como **expectativa con procedencia**, nunca como veredicto ni prohibición. Mal: *"graphify no sirve"*. Bien: *"verificado el 2026-08-12: `graph.json` es un puntero LFS de 224 MB y el índice no incluye `.xml`, así que para causas en PL/SQL no aporta - usar `manifest.json` para listar el Java del módulo, cuesta segundos"*.
- Toda nota lleva **fecha de verificación y el comando o consulta** que la produjo. Una nota sin procedencia se trata como no verificada.
- Escribir en la memoria **qué esperar y a qué costo**, para acelerar el paso. Nunca *si hay que darlo* — eso lo decide la skill.
- Al corregir una nota equivocada, dejar constancia de qué decía antes. Los errores silenciosamente sobreescritos se repiten.

#### 5. Excepciones

Una omisión es legítima solo si es **explícita, justificada y auditable**: estado `OMITIDO` en la tabla, motivo en la sección 9, y reflejo en `respuesta_modelo_raw` del log del Paso 7. Lo que no es aceptable es la omisión silenciosa ni la que se apoya en la memoria como coartada. Si la misma fuente aparece `OMITIDO` en corridas sucesivas, eso es señal de que el procedimiento de lectura es demasiado caro y hay que arreglarlo en la skill, no normalizar el salto.

---

Invocar el flujo completo de 9 pasos de esa skill (vive en el repo orquestador, es común a todos los clientes), usando como entrada:
- La descripción original del ticket,
- Si se venía del camino 4.2, también la respuesta de aclaración del cliente,
- El contexto específico del cliente leído en el Paso 3,
- El resultado de la verificación en BD contable del Paso 3-B, si aplicó.

**Enriquecimiento con las skills complementarias — 3 campos distintos, no se fusionan:**
- **Tipo de caso** (clasificación nativa del motor, Paso 3 de `openbravo-functional-ticket-analysis`): Operativo / Configuración / Integración / Bug / Infraestructura. Este es el campo principal que determina el manejo general del ticket.
- **Causa raíz** (vocabulario de `openbravo-triage-tecnico`, dentro de la sección de Diagnóstico/Causa raíz del motor): configuración faltante, estado del documento, restricción de negocio del sistema, dato del cliente erróneo, o bug real (último recurso). Es un campo aparte y más granular que el Tipo de caso — no lo reemplaza ni se combina en el mismo valor.
- **Categoría de audiencia/formato** (taxonomía de `openbravo-soporte-sidesoft`): FUNCIONAL / TÉCNICO / CONFIGURACIÓN / CONTABLE / CAPACITACIÓN. Determina el formato de la respuesta (ver Paso 3 de esa skill), no el diagnóstico en sí.
- Citar por nombre de archivo cualquier caso de uso de `casos_de_uso_openbravo_erp.md` que aplique.

**Reglas específicas de la sección §7 (respuesta al usuario final) — alineadas con `openbravo-functional-ticket-analysis.mdc`:**
- §7 **nunca** debe incluir: SQL, sentencias UPDATE, scripts de corrección, referencias a tablas, columnas, código fuente, ni IDs técnicos. Eso va exclusivamente en las secciones 5-6 (uso del consultor/técnico) o en el comentario privado 6.3 de este flujo.
- §7 debe incluir, cuando aplique: (1) diagnóstico en términos de negocio — qué documento/flujo se usó mal; (2) por qué está mal — naturaleza del movimiento, tipo de documento, impacto en conciliación/contabilidad; (3) qué debieron hacer — el flujo correcto en Openbravo; (4) solución operativa numerada, típicamente en el patrón revertir → recrear correctamente → conciliar/validar.
- Si el caso es operativo (no bug de sistema): la solución principal va completa en §7. El SQL o escalamiento a desarrollo, si existe, va solo en las secciones 5-6 para el consultor — nunca en §7 ni en el comentario de solución 6.3.
- Si además hay un bug de sistema real: §7 sigue siendo el flujo correcto para el usuario; el detalle técnico del bug y su escalamiento van en 5-6 / comentario privado.

Producto esperado: el documento completo de 9 secciones (Clasificación, Entendimiento, Diagnóstico técnico, Causa raíz, Plan de solución, Escalamiento, **Respuesta sugerida al usuario final — §7**, Prevención, Datos faltantes), siguiendo el subtipo que corresponda (Incidencia o Viabilidad) tal como esa skill lo define.

---

## Paso 6 — Publicar los comentarios, TODOS PRIVADOS (sin confirmación — ejecución automática)

Ejecutar en este orden, vía MCP-DB (`glpi`). `users_id = 148` = usuario `bot.glpi`. **Todos los comentarios de este flujo se publican con `is_private = 1` — ninguno es visible para el solicitante/cliente en GLPI.**

**Cambio: ya no se publica comentario de "primer contacto".** El flujo pasa directo del análisis al comentario de SLA+Score. Quedan 3 comentarios en total (antes eran 5).

### 6.1 — Comentario privado: SLA/criticidad + score de acertividad (fusionado)
Un solo `INSERT` que combina ambos contenidos — nivel SLA, criticidad, área funcional, tiempo estimado, **y** el score de acertividad de la §7 con su justificación, todo en el mismo comentario.

Evaluar el score exclusivamente sobre la sección §7 del análisis del Paso 5, con estos rangos:

| Rango | Criterio |
|---|---|
| 90–100 | Veredicto con evidencia directa de módulo/código confirmado, sin datos faltantes, procedimiento accionable completo |
| 70–89 | Buena evidencia pero con 1 supuesto razonable no confirmado, o falta 1 dato menor |
| 40–69 | Diagnóstico plausible pero con confianza Media/Baja declarada, o basado solo en comportamiento core sin confirmar personalización del proyecto |
| 0–39 | Datos insuficientes pese a pasar el filtro de contexto, múltiples hipótesis sin evidencia, o Datos faltantes con elementos críticos pendientes |

```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_sla_y_score_html}', 1, 0, NOW(), NOW(), 1);
```

`{comentario_sla_y_score_html}` incluye, en un solo bloque: Nivel SLA · Criticidad · Área funcional · Tiempo estimado de revisión inicial · Score de acertividad (0-100) · Justificación del rango.

### 6.2 — Comentario privado: detalle completo de los 9 pasos
Contenido: el documento completo generado en el Paso 5, en HTML legible. Audiencia: consultor/soporte técnico — puede incluir SQL, IDs, nombres de módulo. Si el `adjuntos` recibido en el payload no es `sin adjuntos`, agregar al final una nota: "Ticket con adjuntos no analizados automáticamente: {lista de nombres} — revisar manualmente en GLPI."

**Obligatorio: dividir este comentario en dos followups.** El documento completo de 9 secciones supera el límite de escritura del MCP (ver *Límite de tamaño* abajo) y se pierde entero si se inserta como un solo bloque. Publicar:
- `[TRIAGE-ANALISIS-9PASOS] Parte 1 de 2` — secciones 1 a 3 (Clasificación, Entendimiento, Diagnóstico técnico).
- `[TRIAGE-ANALISIS-9PASOS] Parte 2 de 2` — secciones 4 a 6 y 8 a 9, más la nota de adjuntos.

En el log del Paso 7, `followup_analisis_id` lleva el id de la Parte 1, y ambos ids se detallan en `respuesta_modelo_raw`.
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_analisis_9_pasos_html}', 1, 0, NOW(), NOW(), 1);
```

### 6.3 — Comentario privado (condicional): solo si score > 70
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_publico_respuesta_formateada}', 1, 0, NOW(), NOW(), 1);
```
Si el score es 70 o menor, no publicar este comentario.

### 6.4 — Actualizar campos del ticket — nunca incluir `status`
```sql
UPDATE glpi_tickets
SET itilcategories_id = COALESCE({categoria_id_o_null}, itilcategories_id),
    impact = {impact_id}, priority = {priority_id}, date_mod = NOW()
WHERE id = {ticket_id};
```

**Nota sobre notificación al solicitante**: el INSERT directo en `glpi_itilfollowups` no dispara el correo de notificación de GLPI. Pendiente de confirmar si la API REST está habilitada para ese caso.

### 6-A — Límite de tamaño y verificación obligatoria de cada INSERT

El MCP-DB **descarta en silencio** un `INSERT` cuyo `content` supere aproximadamente **3,2 KB**: la herramienta responde `Insert successful ... Last insert ID: N`, el contador de auto-incremento avanza, y la fila nunca queda en la tabla. Confirmado el 2026-08-12 comparando `SELECT MAX(id) FROM glpi_itilfollowups` contra los ids que el log daba por insertados. No es concurrencia entre corridas ni latencia de réplica.

Por eso, para **cada** `INSERT` de este flujo (`glpi_itilfollowups` y `sidesoft_triage_glpi_log`):

1. Mantener el `content` por debajo de ~3,2 KB — dividir en varios followups si hace falta (ver 6.2).
2. Insertar.
3. Verificar con un `SELECT` por el id devuelto, **en una llamada aparte** — un `SELECT` en el mismo lote puede dar falso negativo por latencia.
4. Si vuelve vacío, repetir el `SELECT` una vez más antes de concluir que se perdió.
5. Si sigue vacío, reintentar el `INSERT` una sola vez.
6. Registrar en el log únicamente ids que hayan pasado por un `SELECT` positivo. Nunca encadenar el INSERT del log con un id sin verificar.

Al inicio de cada corrida, no confiar en los ids de followup de un registro anterior de `sidesoft_triage_glpi_log`: releer siempre el historial real del ticket (Paso 4). Chequeo rápido: si un id registrado es mayor que el `MAX(id)` actual de la tabla, esa fila nunca existió.

**Caracteres a evitar en cualquier string enviado por el MCP**: el punto y coma, tanto literal como dentro de entidades HTML (`&mdash;`, `&gt;`). Usar guiones y palabras. Las etiquetas `<br>` y `<b>` sí son seguras.

### 6-B — Si el análisis produjo un script SQL correctivo sobre el ERP del cliente
Siguiendo la regla dura de `openbravo-triage-tecnico` para modo automático: cualquier `INSERT`/`UPDATE`/`DELETE`/`DDL` sugerido contra tablas del ERP del cliente (`Fact_Acct`, `C_Invoice`, etc.) va **como texto dentro del comentario privado del Paso 6.2** (detalle de los 9 pasos), nunca como acción ejecutada. Encabezar ese bloque con:

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
   followup_sla_score_id,
   followup_analisis_id, followup_publico_solucion_id,
   score_acertividad, campos_ticket_actualizados,
   respuesta_modelo_raw, resultado, detalle_error)
VALUES
  ({ticket_id}, '{proyecto}', '{owner}/{repo}', '{estado_procesamiento}', '{nivel_sla}', '{criticidad}', '{area_funcional}',
   '{categoria_glpi}', '{impacto}', '{prioridad}',
   {followup_sla_score_id_o_null},
   {followup_analisis_id_o_null}, {followup_publico_solucion_id_o_null},
   {score_acertividad_o_null}, {1_o_0},
   '{json_de_la_clasificacion_completa}', '{ok_o_error}', {detalle_error_o_null});
```

Valores posibles de `estado_procesamiento`: `proyecto_no_registrado`, `preguntas_enviadas`, `esperando_respuesta_cliente`, `ok_alta_confianza` (score > 70), `ok_baja_confianza` (score ≤ 70), `error`.

---

## Reglas críticas (aplican siempre, sin excepción)

- Nunca modificar `status`.
- Nunca inventar nombres de técnicos ni datos que no vengan en el ticket.
- Nunca asignar SLA 1 sin bloqueo total confirmado explícitamente en la descripción.
- Nunca repetir preguntas de aclaración ya enviadas mientras no haya respuesta nueva del solicitante.
- Nunca publicar el comentario de solución (6.3) si el score de acertividad es 70 o menor.
- Todos los comentarios publicados por este flujo son privados (`is_private = 1`) — ninguno llega al solicitante dentro de GLPI.
- Nunca clonar un repo de cliente — siempre leer vía MCP de GitHub, archivo por archivo.
- Nunca procesar un ticket cuyo proyecto no esté en `registro_clientes/clientes.json`.
- Nunca ejecutar (solo sugerir como texto) cualquier `INSERT`/`UPDATE`/`DELETE`/`DDL` sobre la BD de producción del ERP de un cliente — regla dura heredada de `openbravo-triage-tecnico` en modo automático.
- Toda consulta a la BD de Openbravo del cliente (Paso 3-B) es siempre `SELECT`, con filtros y `LIMIT` en tablas de alto volumen.
- Siempre registrar el resultado en `sidesoft_triage_glpi_log`, incluso si el ticket terminó en preguntas, en espera, o sin proyecto registrado.
- Nunca dar por buena la respuesta `Insert successful` del MCP-DB: todo id se confirma con un `SELECT` posterior, en una llamada aparte (Paso 6-A).
- La memoria del Automation nunca cancela un paso obligatorio: solo abarata su ejecución (Paso 5-A). Ante contradicción entre la memoria y lo observado en esta corrida, gana lo observado, y la memoria se corrige en el momento.
- Nunca declarar una fuente como revisada sin un dato probatorio obtenido en esta corrida. Sin dato, la fuente va como `OMITIDO` en el registro de evidencia de la sección 9.
