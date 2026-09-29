---
name: triage-glpi-auto
description: Agente orquestador de triage automático de tickets GLPI (multi-cliente, sin supervisión humana). Recibe de n8n un ticket Nuevo o con respuesta nueva del solicitante, resuelve el cliente/repo del solicitante con registro_clientes/clientes.json, descarta primero los casos que cortan el flujo (duplicado, Capacitación, espera, Proyecto no registrado), lee el código del cliente (desplegado en su BD Openbravo, solo lectura, y en su repo vía MCP GitHub), contrasta con soluciones y validaciones de tickets previos del mismo cliente y con playbooks, ejecuta el motor de 9 pasos (openbravo-functional-ticket-analysis) con investigación obligatoria de causa raíz, arma el bloque de evidencia y aplica el gate de publicación, calcula el score de acertividad, publica los comentarios en GLPI, registra Score agente y Aplica IA, asigna al responsable según perfil, similitud y carga, y deja registro en sidesoft_triage_glpi_log.
---

# Agente Orquestador de Triage GLPI — ejecución automática

**Versión de la skill:** `triage-2026-09-29.4` (se registra en el log junto a la versión del motor).

Corre sin intervención humana y sin pedir confirmación. Está vinculado al **repo orquestador**; los repos de código de cada cliente se leen dinámicamente vía **MCP GitHub**.

**Entrada:** payload de n8n `{ticket_id, texto_limpio, adjuntos}`. n8n ya buscó el ticket y limpió HTML e imágenes. El proyecto y el asunto **no** vienen en el payload: se consultan en GLPI.

**Requisito del disparador (n8n):** además de tickets en Nuevo (`status = 1`), n8n debe entregar tickets en `status` 2, 3 o 4 que tengan un followup del solicitante posterior al último comentario de `bot.glpi`, o una solución del bot rechazada (`glpi_itilsolutions.status = 4`). Sin esto, las ramas 4.2 y 4.2-bis nunca se ejecutan.

**Herramientas:**
- **MCP-DB `sidesoft-db`** (https://mcp-db.sidesoftcorp.com), parámetro `database`:
  - `glpi` → lectura y escritura en GLPI (único alias con escritura).
  - `{openbravo_db_alias}` del cliente → **solo lectura** (`pg_query`, `pg_describe_table`, `pg_list_databases`; nunca `pg_execute`).
- **MCP GitHub** (`get_file_contents`, búsqueda de código) → lectura del repo de código del cliente, sin clonar.
- **Motor:** `openbravo-functional-ticket-analysis` se invoca siempre en el Paso 5.

**Usuarios GLPI:**

| Usuario | ID | Rol en el flujo |
|---|---|---|
| bot.glpi | 148 | Autor de todo lo que publica el flujo |
| DCAZA | 117 | Técnico |
| NRIVADENEIRA | 118 | Técnico |
| sconsultor | 154 | Consultor |
| kquingaluisa | 183 | Consultor |
| kvelasco | 63 | Coordinador (asignación por defecto y capacitación) |
| bruno díaz | `{ID_BRUNODIAZ}` | Proyecto no registrado (2-A). **Mientras el id siga como marcador, asignar a kvelasco (63).** |

**Principio rector:** cada conclusión se apoya en evidencia obtenida en esta corrida (código del cliente, BD, ticket, soluciones previas verificadas). Lo no confirmado se declara como pendiente y baja el score; nunca se inventa un dato, ventana, causa o nombre de persona para dar una solución.

**Orden de ejecución:** Paso 0 → Paso 2 (resolver proyecto y 2-A) → **Paso 4** → 2-B y 2-C → Paso 3 → Paso 5 → Paso 6 → Paso 7. El Paso 4 (punto del flujo) va antes de la recolección de evidencia para descartar duplicados, capacitaciones y tickets en espera sin gastar consultas ni lecturas de código. La numeración se conserva por trazabilidad con el log y el motor.

---

## Paso 0 — Registro de clientes

Leer localmente `registro_clientes/clientes.json` (repo orquestador, sin MCP GitHub):

```json
{
  "ACTUARIA CONSULTORES S.A": { "owner": "Sidesoftpreprod", "repo": "ActuariaCodigoCompleto", "openbravo_db_alias": "actuaria" }
}
```

- **`owner`/`repo`:** repo de código del cliente. El `owner` debe ser el real de la URL de GitHub; un owner mal cargado da 404 a nivel de repositorio, indistinguible de falta de permisos.
- **`openbravo_db_alias`:** alias exacto del Panel MCP (https://mcp-db.sidesoftcorp.com/admin/databases). Si es `null`, el análisis procede sin BD real y, con ancla clase A, aplica el tope de score (6.1).

Es la única fuente de verdad de los proyectos habilitados. Agregar un cliente = una entrada nueva.

**Costo:** no leer todavía `conocimiento_comun/modulos/` ni `casos_de_uso_openbravo_erp.md`. Se leen selectivamente, un archivo y solo las secciones necesarias, cuando el módulo ya está identificado (Paso 5).

## Paso 2 — Resolver proyecto y cliente

El proyecto se vincula al **solicitante** (campo plugin), no al ticket:

```sql
SELECT pr.id AS proyecto_id, COALESCE(pr.name, '') AS proyecto
FROM glpi_tickets t
LEFT JOIN glpi_tickets_users tu ON tu.tickets_id = t.id AND tu.type = 1
LEFT JOIN glpi_plugin_fields_userproyectorelacionadousers up ON up.items_id = tu.users_id
LEFT JOIN glpi_projects pr ON pr.id = REPLACE(REPLACE(REPLACE(up.projects_id_proyectorelacionadouserfield, '"', ''), '[', ''), ']', '')
WHERE t.id = {ticket_id};
```

(Asume un solo proyecto por solicitante; si el campo trae varios, avisar para cambiar el `REPLACE` por `FIND_IN_SET`.)

- Proyecto vacío, o sin clave exacta en `clientes.json` → `estado_procesamiento = 'proyecto_no_registrado'`, aplicar 2-A y terminar el ticket.
- Existe → tomar `owner`, `repo`, `openbravo_db_alias` y continuar.

### Paso 2-A — Proyecto no registrado

1. Followup privado (`is_private = 1`) iniciando con `[TRIAGE-PROYECTO-NO-REGISTRADO]`: el proyecto del solicitante no está habilitado en el flujo automático y queda para revisión manual.
2. `UPDATE glpi_tickets SET status = 3, date_mod = NOW() WHERE id = {ticket_id};` y asignar a **bruno díaz** con el patrón de asignación de 6.4 (si su id sigue como marcador, a kvelasco 63).
3. No ejecutar el resto del flujo.

### Paso 2-B — Acceso al repo y raíz del código

1. Listar la raíz del repo del cliente con MCP GitHub (`get_file_contents`, path vacío).
   - **404 a nivel de repositorio** → `REPO_INACCESIBLE` en la evidencia (nunca `OMITIDO`) + followup privado `[TRIAGE-REPO-INACCESIBLE]` (el `owner`/`repo` de `clientes.json` es inválido o sin permisos). Continuar sin repo; la lectura de código desplegado en BD (3-C) y la comparación por introspección de BD siguen siendo obligatorias.
2. **Detectar dónde arranca el código Openbravo** (dato de esta corrida, no de configuración): si `src-db`, `src-core` o `modules` están en la raíz → raíz. Si no, revisar las carpetas de primer nivel: si **exactamente una** contiene esas carpetas → esa es la raíz (ej. `actuaria/`). Cero o varias candidatas → `ESTRUCTURA_NO_DETECTADA` + followup privado listando las candidatas; continuar sin repo. Nunca suponer la raíz sin haberla detectado.

(Si el Paso 4 corta el flujo, el 2-B no se ejecuta: se hace después del Paso 4, antes del Paso 3.)

### Paso 2-C — Contexto fijo de la corrida

`contexto_cliente = {proyecto_id, proyecto, owner, repo, raiz_codigo, openbravo_db_alias, modulo_ticket}`. `modulo_ticket` se lee de `glpi_plugin_fields_ticketmoduloausars` (`datacenters_id_moduloausarfield`) del ticket actual; puede estar vacío. Todo paso posterior lee de aquí; nadie vuelve a leer ni reinterpretar `clientes.json`.

---

## Paso 4 — Punto del flujo del ticket (se ejecuta antes del Paso 3)

Traer el historial (vía `glpi`):

```sql
SELECT id, users_id, content, is_private, date_creation FROM glpi_itilfollowups
WHERE items_id = {ticket_id} AND itemtype = 'Ticket' ORDER BY date_creation;
SELECT id, users_id, content, is_private, actiontime, date_creation FROM glpi_tickettasks
WHERE tickets_id = {ticket_id} ORDER BY date_creation;
SELECT id, users_id, status, date_creation FROM glpi_itilsolutions
WHERE itemtype = 'Ticket' AND items_id = {ticket_id} ORDER BY date_creation;
SELECT name, content, status FROM glpi_tickets WHERE id = {ticket_id};
```

Revisar también el último registro de `sidesoft_triage_glpi_log` del ticket. Evaluar en este orden:

### 4.-1 — Corrida duplicada
Si `bot.glpi` publicó en los **últimos 15 minutos** un `[TRIAGE-SLA-SCORE]`, un `[TRIAGE-ANALISIS-9PASOS]`, una Solución al Caso (encabezado `SOLUCIÓN AL CASO`, o tarea `ANÁLISIS INICIAL`, o tag legado `[TRIAGE-RESPUESTA-SUGERIDA]`) o unas `PREGUNTAS DE ACLARACIÓN`, sin respuesta nueva del solicitante después → no publicar nada, registrar `duplicado_abortado` con el id del comentario existente y terminar. (La causa de fondo de las corridas concurrentes está en el disparador de n8n; este paso solo contiene el síntoma.)

### 4.0 — Caso Capacitación
Solo si el bot aún no actuó en el ticket. Si el asunto o la descripción contienen (sin distinguir mayúsculas ni tildes) `capacitac`, `entrenamiento` o `training`:
1. Followup **público** (`is_private = 0`), tono cercano: se evaluará la capacitación solicitada y se confirmará la fecha.
2. `UPDATE glpi_tickets SET status = 3, date_mod = NOW() WHERE id = {ticket_id};` y asignar a **kvelasco (63)** con el patrón de 6.4.
3. Actualizar el campo plugin **Fuente de solicitud** a **Capacitación** (verificar antes con `pg_describe_table` el nombre real de la tabla/columna plugin y el id del valor; si no hay fila, `INSERT`).
4. Log `capacitacion` y terminar.

### 4.1 — ¿Ya se enviaron preguntas de aclaración?
Buscar un followup de `bot.glpi` con el encabezado visible `PREGUNTAS DE ACLARACIÓN` (o el tag legado `[TRIAGE-ACLARACION]`). No existe → 4.2-bis. Existe → 4.2.

### 4.2 — ¿El solicitante respondió?
Followups posteriores a esas preguntas con `users_id <> 148`:
- **No** → log `esperando_respuesta_cliente`, sin publicar nada ni repetir preguntas. Terminar.
- **Sí** → combinar esa respuesta con la descripción original e ir a 2-B → Paso 3 → Paso 5 (sin 4.3).

### 4.2-bis — Reanálisis tras un análisis o solución previa
Aplica si existe un `[TRIAGE-ANALISIS-9PASOS]` previo del bot y, después de él, hay un followup del solicitante (`users_id <> 148`) o una solución del bot rechazada (`glpi_itilsolutions.status = 4`):
- Es un **reanálisis**: entrada del motor = descripción original + todo lo nuevo del solicitante + el análisis previo del bot, que pasa a ser **hipótesis a falsear** (regla 5A.7 del motor), nunca conclusión heredada. Si el solicitante dice que la solución no funcionó, la causa anterior se reevalúa desde cero y la tabla de hipótesis debe mostrar por qué se mantiene o se descarta.
- Se publica un nuevo juego completo (6.1, 6.2 y canal 6.3) cuya primera línea indica `Reanálisis N — motivo: {respuesta del solicitante o solución rechazada}`.
- **Máximo 2 reanálisis por ticket.** Al tercero: followup privado `[TRIAGE-REANALISIS-LIMITE]`, asignar a kvelasco (63), log `error` con detalle `limite_reanalisis` y terminar.
- Si no se cumple la condición → 4.3.

### 4.3 — Suficiencia de contexto
Aplicar el Paso 0-A del motor (5 mínimos), intentando antes cubrir con la BD los mínimos que tengan un identificador consultable. Faltan 2 o más → 4.4. Faltan 0 o 1 → 2-B → Paso 3 → Paso 5, señalando el faltante.

### 4.4 — Preguntas de aclaración (públicas)
- Identificar el módulo probable (mapa 5B del motor) y redactar **3 a 8 preguntas** concretas que cierren exactamente los mínimos ausentes (nada genérico tipo "¿puede dar más detalles?"). Si una pregunta necesita un dato que el usuario ve en pantalla, decir en qué ventana buscarlo.
- Publicar **un único followup público** (`is_private = 0`), dirigido al solicitante, que inicie con el encabezado visible `<b>PREGUNTAS DE ACLARACIÓN</b>`, con las preguntas numeradas, en lenguaje claro: sin SQL, IDs internos, nombres de tablas ni marcadores `[TRIAGE-*]`.
- Ningún otro comentario en esta corrida. Log `preguntas_enviadas`, estado y asignación según 6.4 Caso B. Terminar.

---

## Paso 3-A — Datos accionables de `Detalles Adicionales:`

Si `texto_limpio` trae `Detalles Adicionales:` (texto extraído de imágenes por un modelo de visión), tomar de cada `Imagen N:` **solo** valores que identifiquen filas: nº de documento/factura/pedido/NC/comprobante, montos, fechas, tercero (nombre, CI/RUC), tipo de documento, organización. Descartar etiquetas sin valor, campos vacíos o en cero (salvo que el ticket trate de eso) y texto decorativo. Si la imagen muestra un mensaje de error, conservarlo literal: es candidato a ancla (motor Paso 1.5).
- **Viable** (al menos un identificador único, o tercero + fecha + monto) → usarlos como filtros literales del Paso 3-B.
- **No viable** y la descripción tampoco trae identificador → anotar "Imagen adjunta sin datos suficientes para acotar una verificación en BD" y no consultar sin `WHERE`.
- Registrar qué identificadores se usaron (evidencia).

## Paso 3-B — Verificación en la BD Openbravo del cliente (solo lectura)

Aplica si `openbravo_db_alias` no es `null` y hay identificador usable. **No se limita a descuadres contables.** Disparadores: descuadre o asiento; ancla clase A del motor; documento con inconsistencia de montos, estados, líneas, plan de pagos o `em_*`; hipótesis de maestro/configuración que exige comparar valores vivos.

1. `database` = `openbravo_db_alias` exacto (alias lógico, nunca adivinado).
2. `pg_describe_table` antes de consultar tablas que no se conozcan.
3. `pg_query` con `SELECT` filtrado y `LIMIT`, usando los identificadores del 3-A (búsqueda dirigida, no exploratoria).
4. **Ancla clase A:** ejecutar la auditoría de `ad_pinstance` y la comparación contra hermanos exitosos del motor (Paso 1.5) **antes** de explicar estados o flujo. Prohibido cerrar con "genere albarán/factura" o "Proformado es esperado" sin explicar el `errormsg`. Si coexisten A y un estado tipo Proformado, manda A.
5. Un campo relacional en `null` que en filas pares sí está poblado (ej. `c_bpartner_id` en `fin_payment_scheduledetail`) es **candidato técnico de causa raíz**, no dato de contexto; si requiere corrección de datos, aplica 6-B.
6. Si `pg_query` falla, usar `pg_list_databases`, registrar la incidencia y seguir sin esta verificación. Si el alias es `null`: anotar "Diagnóstico basado solo en conocimiento estático — verificación en BD del ERP no disponible"; con ancla A, `ad_pinstance` queda `NO DISPONIBLE` y aplica el tope de 6.1.

## Paso 3-C — Código desplegado y diccionario en la BD del cliente

Con `openbravo_db_alias` disponible, el motor ejecuta sus Pasos 5A.0 y 5C por BD: funciones y triggers **desplegados** (`pg_get_functiondef`, `pg_trigger`), mensajes (`ad_message_trl`), y ventana, pestaña, campo y **ruta de menú completa** en el idioma del sistema (tablas `_trl`). Reglas del orquestador:
- Lo desplegado en BD manda sobre el repo para PL/SQL y diccionario; si difieren, `REPO_DESACTUALIZADO` en la evidencia.
- Con `REPO_INACCESIBLE` o `ESTRUCTURA_NO_DETECTADA`, este paso es la fuente principal de código (solo queda sin cubrir Java y reportes, lo que se declara en §9).
- Toda ventana o campo citado en §7 debe salir de aquí o, sin BD, del XML del repo; si no, se declara no confirmado.

## Paso 3-D — Soluciones y validaciones de tickets anteriores del mismo cliente

Objetivo: aprovechar cómo se resolvieron casos parecidos del **mismo proyecto** y dónde se equivocó antes el bot, sin adoptarlos a ciegas.

1. Elegir 2–4 términos distintivos del ticket (tipo de documento, mensaje literal, ventana, proceso) y buscar candidatos por título, contenido y módulo:

```sql
SELECT DISTINCT t.id, t.name, t.solvedate
FROM glpi_tickets t
JOIN glpi_tickets_users tu ON tu.tickets_id = t.id AND tu.type = 1
JOIN glpi_plugin_fields_userproyectorelacionadousers up ON up.items_id = tu.users_id
LEFT JOIN glpi_plugin_fields_ticketmoduloausars m ON m.items_id = t.id AND m.itemtype = 'Ticket'
WHERE REPLACE(REPLACE(REPLACE(up.projects_id_proyectorelacionadouserfield, '"', ''), '[', ''), ']', '') = '{proyecto_id}'
  AND t.id <> {ticket_id} AND t.is_deleted = 0 AND t.status IN (5, 6)
  AND t.date >= NOW() - INTERVAL 12 MONTH
  AND (t.name LIKE '%{termino1}%' OR t.name LIKE '%{termino2}%' OR t.content LIKE '%{termino1}%'
       OR t.content LIKE '%{mensaje_literal_corto}%' OR m.datacenters_id_moduloausarfield = '{modulo_ticket}')
ORDER BY t.id DESC LIMIT 8;
```
(Omitir las condiciones cuyo valor esté vacío.)

2. Para los 3 más pertinentes (por título y módulo), leer **solo** lo escrito por personas (excluir `users_id = 148`: los análisis del bot no son soluciones validadas), con `LEFT(content, 1500)`: la solución (`glpi_itilsolutions`, con su `status`) y las tareas/followups de técnicos.
3. **Validación humana de la IA** en esos tickets:

```sql
SELECT f.items_id, f.iaacertofield, f.plugin_fields_motivofalloiafielddropdowns_id AS motivo_id,
       d.name AS motivo, LEFT(f.observacionvalidacioniafield, 800) AS observacion
FROM glpi_plugin_fields_ticketticketsformfields f
LEFT JOIN glpi_plugin_fields_motivofalloiafielddropdowns d ON d.id = f.plugin_fields_motivofalloiafielddropdowns_id
WHERE f.itemtype = 'Ticket' AND f.items_id IN ({ids_candidatos});
```
   (Verificar antes con `pg_describe_table` los nombres reales si la consulta falla.) Convención: **IA acerto = Sí** es acierto validado. **IA acerto = No** solo cuenta como validación si **Motivo fallo IA** está lleno; sin motivo se trata como "sin validar". Si un ticket similar tiene fallo validado, su motivo y observación son una **advertencia explícita** para este análisis (qué no repetir: ej. ventana incorrecta, alcance incompleto) y se citan en §9.
4. **Evaluar efectividad** de cada referencia:
   - *Efectiva:* solución aceptada (`glpi_itilsolutions.status = 3`), o ticket cerrado con confirmación del usuario, sin un ticket posterior del mismo solicitante por el mismo problema.
   - *No efectiva:* solución rechazada (`status = 4`), reapertura o reincidencia.
   - *Sin evidencia:* ninguna de las anteriores.
5. **Aplicabilidad:** una referencia efectiva es una **hipótesis**, no la conclusión (regla 5A.7 del motor). Verificar en código/BD un dato concreto de este ticket que su mecanismo exija (mismo tipo de documento, mismo mensaje, misma condición de datos). Solo si se confirma se usa como base de la solución; si no, se descarta explícitamente.
6. Registrar en §9 y en el log (`tickets_referencia`): `#id — efectiva/no efectiva/sin evidencia — aplicable/no aplicable — dato verificado — validación IA (acierto/fallo: motivo/sin validar)`. En §7 se describe la solución en lenguaje de negocio, sin nombres de técnicos ni números de ticket de otros solicitantes.

## Paso 3-E — Playbooks de casos recurrentes

Leer `conocimiento_comun/playbooks/README.md` (índice corto de disparadores). Si el ticket coincide con un disparador, leer **solo** ese playbook y seguir su lista de investigación: qué verificar, qué evidencia exige y qué forma tiene la solución. El playbook **ordena la investigación, no la reemplaza**: toda causa sigue exigiendo confirmación en código/BD de este caso. Registrar el playbook usado en el log (`playbook`) y en §9. Si ninguno aplica, continuar sin él.

---

## Paso 5 — Análisis funcional completo (motor `openbravo-functional-ticket-analysis`)

Entrada del motor: descripción original, respuesta de aclaración (si viene de 4.2), datos del reanálisis (si viene de 4.2-bis), `contexto_cliente`, resultado del Paso 3-B (incluida la auditoría `ad_pinstance` si el ancla es A), código desplegado y nombres de UI del 3-C, referencias verificadas y advertencias de validación del Paso 3-D y playbook del 3-E.

**Orden obligatorio:** motor Paso 1.5 (ancla) primero. Luego:
1. Identificar el módulo con el mapa 5B del motor y, si ayuda, leer el archivo de `conocimiento_comun/modulos/` correspondiente (solo secciones necesarias; su tabla "Technical" da las rutas de código).
2. **Leer el código real del cliente** (motor Paso 5A): desplegado en BD (5A.0) y repo vía MCP GitHub usando `raiz_codigo`. No se usa graphify ni `graphify-out/` ni ningún JSON asociado, y no se busca código Openbravo en el repo orquestador.
3. Rastrear el componente exacto (motor 5A.6); si no se confirma → `COMPONENTE_NO_CONFIRMADO`.
4. Ticket con varios problemas independientes → sub-casos según el motor; cada uno con su evidencia.

Nunca escribir que se revisó una fuente que no se abrió en esta corrida, ni apoyarse en una conclusión de una corrida anterior como evidencia actual.

### 5-EVIDENCIA — Precedencia de la memoria y registro

**La memoria del Automation nunca cancela un paso obligatorio; solo puede abaratarlo.** Orden: abrir primero la fuente de esta corrida, luego leer la memoria para interpretar; si la contradice, gana lo observado y la memoria se corrige en la misma corrida (qué decía, qué se midió, cuándo). Toda nota de memoria se redacta como expectativa con fecha y comando que la produjo, nunca como prohibición.

Tabla obligatoria en §9 — `LEÍDO` solo vale con un dato concreto obtenido en esta corrida; sin dato es `OMITIDO`:

| Fuente | Estado | Dato probatorio |
|---|---|---|
| Código fuente del módulo (repo del cliente) | LEÍDO / OMITIDO / REPO_INACCESIBLE / ESTRUCTURA_NO_DETECTADA / COMPONENTE_NO_CONFIRMADO | archivos y funciones abiertos, o el eslabón no confirmado |
| Código desplegado en BD (3-C) | LEÍDO / NO DISPONIBLE — y IGUAL / REPO_DESACTUALIZADO / SOLO BD | funciones/triggers leídos y resultado de la comparación con el repo |
| Ruta de menú y etiquetas de UI (3-C / motor 5C) | CONFIRMADA (BD) / CONFIRMADA (repo) / NO CONFIRMADA / NO APLICA | ruta completa y campo, o motivo |
| `Detalles Adicionales:` (3-A) | LEÍDO / SIN IMÁGENES | identificadores usados o motivo de no viable |
| BD del ERP (3-B) | LEÍDO / NO DISPONIBLE | resultado del SELECT o motivo; `null` anómalos detectados |
| `ad_pinstance` (3-B.4) | AUDITADO / NO APLICA / OMITIDO / NO DISPONIBLE | process, result, errormsg, fecha. `NO APLICA` solo si el ancla no es A. `OMITIDO` con ancla A bloquea score ≥ 90 |
| Ancla del síntoma | A / B / C / D / E | clase + fragmento literal |
| Mecanismo reproducido (motor 2.9) | CONFIRMADO / NO CONFIRMADO / NO APLICA | condición concreta, documentos KO vs OK comparados y valor simulado vs observado |
| Cadena causal (motor 2.10) | TERMINAL ALCANZADA / CAUSA_TERMINAL_NO_ALCANZADA | niveles con su evidencia, o nivel donde se detuvo y qué faltó |
| Dato que distingue (motor 2.11) | NOMBRADO / NO APLICA / OMITIDO | ventana y valor que difiere del caso OK, o motivo de no aplica |
| Tickets previos del cliente (3-D) | VERIFICADO / SIN CANDIDATOS / NO APLICABLE | ids, efectividad, dato verificado y validación IA |
| Playbook (3-E) | APLICADO / NO APLICA | nombre del playbook |
| Comparación contra pares (5-B.1) | COMPARADO / SIN PARES | registros y resultado, o motivo |
| Alcance real e impacto del cambio (5-B.5 / motor 2.8) | MEDIDO / NO APLICA | número obtenido y consulta, o motivo |

`OMITIDO` (archivo puntual inexistente en un repo accesible), `REPO_INACCESIBLE` (repo entero 404), `ESTRUCTURA_NO_DETECTADA` (repo accesible sin raíz de código clara), `COMPONENTE_NO_CONFIRMADO` (archivo existente no confirmado como responsable) y `REPO_DESACTUALIZADO` (repo difiere de lo desplegado) no son intercambiables. Una omisión solo es legítima si es explícita, justificada y queda en `respuesta_modelo_raw`.

### 5-B — Profundización de causa raíz (obligatoria antes de cerrar)

Se aplica **durante** el motor y **antes de publicar**; todo hallazgo se incorpora al mismo documento (§3, §4, §5, §8, §9) y a la única §7. Nunca un comentario de corrección posterior.

1. **No cerrar en la primera causa plausible:** preguntarse qué otra cosa produciría el mismo síntoma y evaluarla antes de fijar la causa. Aplica también a "no hay error"/"comportamiento esperado": la consistencia interna de un registro no prueba que esté bien configurado frente a sus pares. La comparación contra pares (motor Paso 2.7 y 7-bis) es **siempre obligatoria** en este flujo (hay BD disponible), cubriendo tantos escenarios comparables como sea razonable, y su profundidad se refleja en el score. Con ancla A, primero la auditoría `ad_pinstance`; la comparación de maestros va después y nunca la sustituye. Si datos ausentes en una ventana podrían venir de una integración externa, evaluar esa sincronización como hipótesis, verificándola en código/BD (ej. usuario creador, proceso o servicio que genera esos registros), antes de concluir "falta de registro manual". Si el síntoma es "antes funcionaba", buscar cambios recientes en maestros y código (motor Paso 2.7). Con **ancla E** (resultado incorrecto sin error) o cualquier causa de cálculo o de generación de registros, es obligatoria la reproducción del mecanismo del motor (Paso 2.9): leer la lógica del proceso, comparar el documento que falla contra los que funcionan (incluidos los que el propio ticket o el análisis mencionan) y simular el cálculo hasta reproducir el valor incorrecto. **Después, siempre, el descenso del motor (Paso 2.10):** la condición encontrada se toma como nuevo síntoma, se identifica y simula el paso anterior que la produjo (con `created`/`createdby`, `ad_pinstance` y el código que inserta o modifica esas filas), y se repite hasta una causa que el usuario puede corregir. En toda incidencia con un caso comparable que sí funciona, es obligatorio el Paso 2.11 del motor: leer las entradas reales del proceso en el caso malo y en el bueno, y nombrar el registro o valor que los distingue. El botón o la línea de código que muestra el síntoma no es la causa terminal si solo falla cuando esa entrada es distinta. Quedarse en el proceso que el usuario ya señaló, o en "use otro documento", es un análisis incompleto.
2. **Trazabilidad:** Usuario → origen del dato → proceso funcional → backend (función/trigger/servicio) → BD → registro → resultado. Identificar el eslabón roto y distinguir error visible, error técnico y causa raíz. Señalar cuando el flujo pasa por un módulo custom en vez del estándar. El eslabón backend se llena solo con el componente confirmado (motor 5A.6), preferentemente en su versión desplegada.
3. **Tabla de hipótesis y descarte** (en §9, respaldo de §4): Hipótesis | Campo (columna exacta o N/A) | Evidencia | Cómo se validó | Resultado | Estado. Reglas anti-colapso, de agrupación de `EM_*` no relacionadas y de precedentes: las del motor (Paso 4 y 5A.7).
4. **Cuatro niveles de causa** en §4 (plantilla nativa del motor).
5. **Alcance real** (si la causa es un patrón de datos/proceso o un gap de un módulo compartido): consulta que cuente cuántos registros del cliente comparten la condición; registrar el número. Mayor a 1 → patrón sistémico en §4 y §8, y fases en §5. Si es específico de un registro, declarar "no aplica" con el motivo. **Configuración replicada** (fórmula que agrupa conceptos, parámetro por sucursal): identificar todos los campos/registros hermanos, listar en §5 **cada** uno a actualizar y señalar si unos ya tienen el patrón y otros no.
6. **Workaround vs solución definitiva** por separado en §5, con los riesgos del workaround.
7. **Impacto y fases** antes de sugerir corrección de datos o de configuración: procesos afectados (POS, ventas, reportes, contabilidad, integraciones) y número medido (motor Paso 2.8). Volumen alto → **Fase 1 puntual** (registros del ticket, con transacción y respaldo) y **Fase 2 masiva** (por lotes, marcada "no ejecutar sin revisión"), cada una con su número de registros.
8. **Validación de la solución** en §5: qué volver a consultar (ej. repetir la consulta de alcance) y qué caso borde revisar.
9. **Verificación para el usuario en §7:** la solución incluye cómo comprobar que quedó resuelto y qué responder si no funciona (plantilla del motor). Sin esto, el análisis no pasa el gate (5-C).
10. **Hallazgo distinto del síntoma:** la §7 debe comunicar la causa encontrada (condición concreta de datos, configuración o lógica que no estaba en el texto del ticket) y la corrección de esa causa. Repetir lo que el usuario reportó y ofrecer solo un workaround no es un análisis y no pasa el gate (5-C).

**Campos del motor, sin fusionar:** *Tipo de caso* (Operativo / Configuración / Integración / Bug / Infraestructura) y *Causa raíz* (vocabulario de §4, declarado una sola vez). Citar por nombre cualquier caso de `casos_de_uso_openbravo_erp.md` que aplique.

**§7:** se rige por las plantillas y reglas de §7 del motor (sin SQL, tablas, columnas ni IDs; ruta de menú completa y etiqueta del campo confirmadas o declaradas en §9; valor actual y valor nuevo exacto; camino operativo estándar antes que script; dónde se configura la regla; Complementarias e Informativas en "Otras opciones a considerar"; bloque "Solución a aplicar o verificar"; "Cómo verificar que quedó resuelto" y "Si después de aplicarlo el problema continúa"). En un caso operativo la solución completa va en §7; SQL y escalamiento solo en §5–6. Si 5-B separó workaround y definitiva, §7 refleja ambos en lenguaje operativo. Cambio de un valor de configuración de interfaz: §7 indica ruta, campo y el valor final exacto en lenguaje llano, con el script en 6-B.

**Producto:** documento de 9 secciones (Clasificación, Entendimiento, Diagnóstico técnico, Causa raíz, Plan de solución, Escalamiento, **§7 Respuesta sugerida**, Prevención, Datos faltantes/Evidencia), subtipo Incidencia o Viabilidad.

### 5-C — Bloque de evidencia y gate de publicación

Antes de publicar, armar el bloque de evidencia (JSON compacto, sin punto y coma) con lo que el documento **realmente** contiene:

```json
{"version_skill":"triage-2026-09-29.4/motor-2026-09-29.4","subtipo":"Incidencia","tipo_caso":"Configuracion","subcasos":1,
 "ancla":"C","ad_pinstance":"NO APLICA","codigo":"LEIDO","repo_vs_bd":"IGUAL","componente_confirmado":true,"componente_fuente":"BD",
 "causa_en_maestro":true,"comparacion_pares":"COMPARADO","cierre_comportamiento_esperado":false,
 "mecanismo_confirmado":true,"dato_distingue":"NOMBRADO","hallazgo_distinto_al_sintoma":true,"niveles_causa":3,"causa_terminal":true,"s7_explica_causa":true,
 "accion_en_pantalla":true,"ruta_menu_confirmada":true,"requiere_cambio_datos":false,"script_incluido":false,
 "verificacion_en_s7":true,"secciones_completas":true,"score_propuesto":92,"score_final":92,
 "gate_resultado":"aprobado","gate_reglas":[]}
```

Valores: `tipo_caso` ∈ Operativo/Configuracion/Integracion/Bug/Infraestructura/Viabilidad · `codigo` = estado de la fila de código de 5-EVIDENCIA · `repo_vs_bd` ∈ IGUAL/REPO_DESACTUALIZADO/SOLO_BD/SOLO_REPO/NO_APLICA · `componente_fuente` ∈ BD/REPO/AMBOS/NO_APLICA · `comparacion_pares` ∈ COMPARADO/SIN PARES/PENDIENTE · `mecanismo_confirmado` = el motor reprodujo o demostró la condición que produce el síntoma (Paso 2.9 o auditoría 1.5) · `hallazgo_distinto_al_sintoma` = la §7 contiene al menos una condición concreta (dato, configuración o lógica) que **no** aparece en el texto del ticket · `niveles_causa` = número de niveles de la cadena causal (motor 2.10) · `causa_terminal` = se llegó a un registro, parámetro o acción que el usuario puede corregir, o a un defecto que ocurre también con las mismas entradas que un caso OK. Nombrar solo el botón o el proceso que el usuario ya señaló no pone `causa_terminal` en true · `dato_distingue` ∈ NOMBRADO/NO_APLICA/OMITIDO (motor 2.11). NOMBRADO exige la ventana y el valor que difiere del caso OK · `s7_explica_causa` = la §7 contiene "Qué identificamos" y "Por qué ocurre" con esa causa, no con el síntoma repetido.

**Gate (se aplica en orden, el score final es el menor tope alcanzado):**

| Regla | Condición | Efecto |
|---|---|---|
| G1 | `ancla = A` y `ad_pinstance` ≠ AUDITADO | score máx. 70 |
| G2 | (`causa_en_maestro` o `cierre_comportamiento_esperado`) y `comparacion_pares` ≠ COMPARADO | score máx. 70 |
| G3 | `componente_confirmado = false` y `tipo_caso` ∈ Bug/Integracion | score máx. 70 |
| G4 | `repo_vs_bd = REPO_DESACTUALIZADO` y `componente_fuente = REPO` | score máx. 70 |
| G5 | `accion_en_pantalla` y `ruta_menu_confirmada = false` | score máx. 84 |
| G6 | score ≥ 90 sin (`tipo_caso` ∈ Operativo/Configuracion/Viabilidad, `requiere_cambio_datos = false` y `verificacion_en_s7 = true`) | score máx. 89 |
| G7 | `requiere_cambio_datos` y `script_incluido = false` | **bloqueado**: completar el script antes de publicar |
| G8 | `secciones_completas = false` o `verificacion_en_s7 = false` | **bloqueado**: regenerar |
| G9 | `mecanismo_confirmado = false` y `tipo_caso` ≠ Viabilidad | score máx. 70 (no se publica tarea ni solución al usuario) |
| G10 | `hallazgo_distinto_al_sintoma = false` | **bloqueado**: rehacer la §7 con el mecanismo, o, si no se confirmó, con lo revisado, lo descartado y lo pendiente |
| G11 | `mecanismo_confirmado = true` y `causa_terminal = false` | **bloqueado** una vez: volver al motor Paso 2.10 y bajar un nivel más (paso anterior + simulación). Si tras ese intento la evidencia sigue agotada, score máx. 84 con el nivel faltante declarado en §9 y en "Por qué ocurre" |
| G12 | `s7_explica_causa = false` | **bloqueado**: la §7 (y por tanto el canal 6.3) debe incluir "Qué identificamos" y "Por qué ocurre" |
| G13 | hay un caso OK comparable y `dato_distingue` ≠ NOMBRADO, o la §7 solo nombra el proceso que el usuario ya señaló | **bloqueado** una vez: ejecutar el motor Paso 2.11 y rehacer la §7 con el registro o valor que distingue al caso |

- Un bloqueo se resuelve completando el documento **una vez**; si sigue bloqueado, se publica con score máx. 70 y `gate_resultado = bloqueado`.
- Cualquier tope aplicado → `gate_resultado = degradado` y las reglas en `gate_reglas`. Sin topes → `aprobado`.
- La justificación del score en 6.1 cita las reglas del gate aplicadas.
- El bloque va al log (`evidencia_json`), no a GLPI.

---

## Paso 6 — Publicar (sin confirmación)

Vía `glpi`, autor `users_id = 148`. Todo comentario es **privado** (`is_private = 1`) salvo tres excepciones públicas dirigidas al solicitante: el comentario de Capacitación (4.0), las **Preguntas de aclaración** (4.4) y la **tarea `ANÁLISIS INICIAL`** (6.3, score 81–89). No se publica comentario de "primer contacto".

### 6.1 — `[TRIAGE-SLA-SCORE]` (privado)
Un solo comentario con: Nivel SLA · Criticidad · Área funcional · Tiempo estimado de revisión inicial · Score de acertividad (0–100) · Justificación del rango (incluidas las reglas del gate 5-C aplicadas) · **Asignación** (usuario, perfil y motivo con los números de 6.4). En reanálisis, primera línea `Reanálisis N`.

**Niveles SLA** (única fuente; valores exactos para GLPI y log):

| nivel_sla | Criticidad | Criterio | Revisión inicial | Categoría GLPI (id) | Impacto | Prioridad |
|---|---|---|---|---|---|---|
| `SLA 1` | `Crítica` | Bloqueo total, sin forma de continuar ni manualmente | 2 h hábiles | SLA Nivel 1 (2) | 5 | 6 |
| `SLA 2` | `Alta` | Proceso importante afectado, con workaround parcial | 4 h hábiles | SLA Nivel 2 (3) | 4 | 5 |
| `SLA 3` | `Media` | Requerimiento funcional, duda de uso, error no bloqueante | 8 h hábiles | SLA Nivel 3 (4) | 3 | 4 |
| `SLA 4` | `Baja` | Mejora o consulta general | 24 h hábiles | (no reasignar) | 2 | 3 |

SLA 1 solo con bloqueo total explícito en la descripción; tono urgente con workaround = máximo SLA 2; ambiguo = SLA 3 (decirlo). Solo el árbol "SLA Nivel 1/2/3" (ids 2, 3, 4), nunca el de Infraestructura (6, 7, 8).

**Score de acertividad** — se evalúa sobre la §7 y responde *¿quién cierra el caso y con qué medio?*:

| Rango | Criterio |
|---|---|
| **90–100** | Autoservicio: el usuario o consultor lo resuelve completo con configuración o pasos en el sistema, sin técnico ni desarrollo pendiente, con mecanismo confirmado, ruta de menú confirmada y verificación incluida. |
| **81–89** | Intervención manual/técnica puntual que **sí cierra** el caso hoy (corregir datos, anclar/anular registros, método alterno), aunque quede desarrollo preventivo, **con el mecanismo confirmado** (se sabe qué condición lo causa). 85–89 sin cabos sueltos; 81–84 con puntos por confirmar o coordinar. Un workaround sin mecanismo no califica para este rango. |
| **71–80** | Lo pedido no se puede cumplir hoy de ninguna forma; depende de un desarrollo del proveedor (el workaround solo mitiga). |
| **41–70** | Diagnóstico plausible con confianza Media/Baja, o basado en core sin confirmar la personalización. |
| **0–40** | Datos insuficientes, múltiples hipótesis sin evidencia o faltantes críticos. |

Topes: solución real = capacitación/coordinación no formalizada → máximo **49**. Ancla A con `ad_pinstance` `OMITIDO`/`NO DISPONIBLE`, o `AUDITADO` con `result = 0` alineado al síntoma pero §7 cerrada como "comportamiento esperado" sin explicarlo → máximo **70** (prohibido ≥ 90). Además, los topes del gate 5-C. Con sub-casos, el score es el del sub-caso de menor score. La evidencia no fija el rango por sí sola, pero sin evidencia firme del tipo de intervención el score baja a 41–70.

### 6.2 — `[TRIAGE-ANALISIS-9PASOS]` (privado)
El documento completo en HTML para consultor/técnico (puede incluir SQL, IDs, módulos). Si `adjuntos` ≠ `sin adjuntos`, cerrar con: "Ticket con adjuntos no analizados automáticamente: {lista} — revisar manualmente en GLPI."
- **Control de calidad** antes de publicar: el gate 5-C sin bloqueos, 9 secciones completas y coherentes, **§7 siempre incluida** aunque el score sea bajo. Si no pasa, regenerar una vez. Nunca publicar una versión parcial y luego una corregida.
- **Dividir** por el límite de 6-A: `Parte 1 de 2` (§1–3) y `Parte 2 de 2` (§4–9 + nota de adjuntos). Si la Parte 2 supera ~3,2 KB: `1 de 3` (§1–3), `2 de 3` (§4–6, incluye script), `3 de 3` (§7–9). Si aun así una parte supera el límite, seguir dividiendo por sección (`1 de N`), nunca recortar contenido.
- Cambio de datos en BD → el **script sugerido** (6-B) va en §5/§6, con `SELECT` de localización + escritura acotada o plantilla con placeholders. Si el usuario puede hacerlo por interfaz, §7 da ruta y pasos; el script queda como respaldo.

### 6.3 — Canal adicional según score
Copia la **§7 completa** (que ya está en 6.2), en su mismo orden: saludo con la causa en una oración, **Qué identificamos**, **Por qué ocurre**, **Solución a aplicar o verificar**, "Mientras se aplica la corrección" si existe, **Cómo verificar que quedó resuelto**, **Si después de aplicarlo el problema continúa**, "Otras opciones a considerar" si existe e **Importante**. Nunca se publica solo la parte de pasos: el cliente debe entender qué está pasando y por qué. `TRIAGE-RESPUESTA-SUGERIDA` es solo el nombre interno: **nunca** se escribe en el contenido; el contenido inicia con el encabezado visible del rango.

| Score | Canal | Visibilidad | Encabezado visible |
|---|---|---|---|
| 90–100 | Solución del ticket (`glpi_itilsolutions`) | según GLPI | `SOLUCIÓN AL CASO` |
| 81–89 | Tarea (`glpi_tickettasks`), `actiontime = 600`, `state = 2`, `users_id_tech = 148` | **Pública** | `ANÁLISIS INICIAL` |
| 71–80 | Followup | Privado | `SOLUCIÓN AL CASO` |
| 0–70 | No se publica canal adicional | — | — |

```sql
-- 90–100
INSERT INTO glpi_itilsolutions (itemtype, items_id, solutiontypes_id, content, date_creation, date_mod, users_id, status)
VALUES ('Ticket', {ticket_id}, 0, '{respuesta_html}', NOW(), NOW(), 148, 1);
-- 81–89
INSERT INTO glpi_tickettasks (tickets_id, taskcategories_id, date, users_id, users_id_editor, content, is_private, actiontime, state, users_id_tech, groups_id_tech, date_creation, date_mod, timeline_position)
VALUES ({ticket_id}, 0, NOW(), 148, 148, '{respuesta_html}', 0, 600, 2, 148, 0, NOW(), NOW(), 1);
```
Followups (6.1, 6.2, 71–80, aclaración, capacitación):
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{contenido_html}', {0_o_1}, 0, NOW(), NOW(), 1);
```
En 81–89 el contenido es la §7 en lenguaje claro, sin SQL, IDs internos, marcadores ni hipótesis descartadas. Empieza por la **causa identificada** (nunca por el síntoma que el usuario ya reportó) y conserva "Cómo verificar que quedó resuelto" y "Si después de aplicarlo el problema continúa".

### 6.4 — Estado, campos y asignación

| Caso | Condición | status | Asignado |
|---|---|---|---|
| A | Solución publicada (score 90–100) | 5 Resuelto | según selección |
| A-1 | Análisis publicado con score 0–89 | 3 Planificado | según selección |
| B | `preguntas_enviadas` | 4 En espera | consultor según selección |
| — | Capacitación (4.0) | 3 | kvelasco (63) |
| — | Proyecto no registrado (2-A) | 3 | bruno díaz (o kvelasco mientras su id sea marcador) |
| — | `esperando_respuesta_cliente`, `duplicado_abortado`, `error` | sin cambio | sin cambio |

**Un ticket con análisis publicado nunca queda en Nuevo** (n8n busca `status = 1` y lo reprocesaría indefinidamente). En A y A-1:
```sql
UPDATE glpi_tickets SET itilcategories_id = COALESCE({categoria_id_o_null}, itilcategories_id),
  impact = {impact}, priority = {priority}, status = {status}, date_mod = NOW() WHERE id = {ticket_id};
```

**Selección del responsable** (casos A, A-1 y B):
1. **Perfil del caso:**
   - **Técnico** (DCAZA, NRIVADENEIRA): lo que falta es 100 % técnico — corrección de código/compilación, script de datos a ejecutar, fallo de proceso/BD con componente confirmado, integración o servicio.
   - **Consultor** (sconsultor, kquingaluisa): revisión contable, de flujos o de configuración funcional; orientación de uso; o un análisis previo para confirmar si luego se necesita un técnico (hipótesis sin confirmar, score ≤ 70, preguntas de aclaración).
   - **Indeterminado**, o que por su naturaleza debe decidir el coordinador → **kvelasco (63)**, y fin.
2. Para los dos candidatos del perfil:
```sql
-- Carga actual (En curso, Planificado, En espera)
SELECT tu.users_id, COUNT(*) AS carga FROM glpi_tickets_users tu JOIN glpi_tickets t ON t.id = tu.tickets_id
WHERE tu.type = 2 AND tu.users_id IN ({id1}, {id2}) AND t.status IN (2, 3, 4) AND t.is_deleted = 0 GROUP BY tu.users_id;
-- Experiencia en tickets similares resueltos (mismo módulo del ticket o referencias del 3-D, últimos 6 meses)
SELECT tu.users_id, COUNT(*) AS similares FROM glpi_tickets_users tu JOIN glpi_tickets t ON t.id = tu.tickets_id
LEFT JOIN glpi_plugin_fields_ticketmoduloausars m ON m.items_id = t.id AND m.itemtype = 'Ticket'
WHERE tu.type = 2 AND tu.users_id IN ({id1}, {id2}) AND t.status IN (5, 6) AND t.date >= NOW() - INTERVAL 6 MONTH
  AND (m.datacenters_id_moduloausarfield = '{modulo_ticket}' OR t.id IN ({ids_referencia_3D}))
GROUP BY tu.users_id;
```
   (`{modulo_ticket}` sale de `contexto_cliente`; si está vacío, usar solo las referencias del 3-D.)
3. **Regla:** elegir quien tenga más `similares`; si la diferencia es ≤ 2 (o ambos 0), elegir al de menor `carga`; si el elegido tiene más de 5 tickets abiertos por encima del otro, elegir al otro. Registrar los números en 6.1 y el usuario en el log (`tecnico_asignado`).
4. Asignar (sin duplicar):
```sql
-- si no existe fila type=2:
INSERT INTO glpi_tickets_users (tickets_id, users_id, type) VALUES ({ticket_id}, {id_elegido}, 2);
-- si existe:
UPDATE glpi_tickets_users SET users_id = {id_elegido} WHERE tickets_id = {ticket_id} AND type = 2;
```

**Nota:** el INSERT directo no dispara las notificaciones por correo de GLPI.

### 6-C — Campos "Score agente" y "Aplica IA"
Siempre que el agente realice el análisis y determine el score (análisis de 9 pasos publicado, estados `ok_*`), escribir **ambos** campos plugin del ticket (contenedor `ticketsformfield`, id 11), aunque ya tuvieran un valor:
- **Score agente** (`scoreagentefield`): el número entero del score final aplicado en 6.1 (después del gate), sin decimales ni texto (ej. `85`).
- **Aplica IA** (`plugin_fields_aplicaiafielddropdowns_id`, desplegable): score **≥ 80** → **Si (id 1)**. Score **< 80** → **No (id 3)**. El id 2 no existe y `0` es vacío.

```sql
-- si existe fila del contenedor para el ticket:
UPDATE glpi_plugin_fields_ticketticketsformfields
SET scoreagentefield = '{score}', plugin_fields_aplicaiafielddropdowns_id = {1_si_score_mayor_igual_80_o_3}
WHERE items_id = {ticket_id} AND itemtype = 'Ticket';
-- si no existe:
INSERT INTO glpi_plugin_fields_ticketticketsformfields
  (items_id, itemtype, plugin_fields_containers_id, entities_id, scoreagentefield, plugin_fields_aplicaiafielddropdowns_id)
VALUES ({ticket_id}, 'Ticket', 11, {entities_id_del_ticket}, '{score}', {1_si_score_mayor_igual_80_o_3});
```
Verificar con `SELECT` aparte que ambos valores quedaron guardados (6-A). No se escriben en capacitación, proyecto no registrado, preguntas, espera, duplicado ni error (no hay score).

**Campos de validación humana (nunca los escribe el bot):** **IA acerto** (`iaacertofield`), **Motivo fallo IA** (`plugin_fields_motivofalloiafielddropdowns_id`) y **Observacion validacion IA** (`observacionvalidacioniafield`) los llena el técnico o consultor al resolver. El `UPDATE` de este paso solo toca `scoreagentefield` y `plugin_fields_aplicaiafielddropdowns_id`; un `INSERT` nuevo no incluye esas columnas. En un reanálisis, el bot no limpia ni modifica una validación ya registrada. El bot solo los **lee** (Paso 3-D).

### 6-A — Límite de tamaño y verificación de cada escritura
El MCP-DB **descarta en silencio** un `INSERT` cuyo `content` supere ~**3,2 KB** (responde "Insert successful", avanza el autoincremento y la fila no existe; confirmado el 2026-08-12). Para **cada** escritura:
1. `content` por debajo de ~3,2 KB (dividir si hace falta).
2. Escribir.
3. Verificar con `SELECT` por id **en una llamada aparte**; si vuelve vacío, repetir el `SELECT` una vez; si sigue vacío, reintentar la escritura una sola vez.
4. Registrar en el log solo ids verificados. No confiar en ids de corridas anteriores: si un id registrado es mayor que el `MAX(id)` actual de la tabla, nunca existió.

**Caracteres prohibidos** en todo string enviado al MCP: punto y coma, literal o dentro de entidades HTML (`&mdash;`, `&gt;`). Usar guiones y palabras. Etiquetas seguras: `<br>`, `<b>`, `<table>`, `<tr>`, `<td>`, `<th>`.

**Scripts sugeridos dentro de un comentario:** como el punto y coma está prohibido, cada sentencia se escribe **sin terminador** y se separa de la siguiente con una línea `-- fin de sentencia`. El encabezado del script agrega: "Agregar el punto y coma al final de cada sentencia antes de ejecutar." Evitar `<` y `>` dentro del script (GLPI puede interpretarlos como etiquetas HTML y sus entidades llevan punto y coma): reescribir la condición con `BETWEEN`, `NOT IN`, `IS DISTINCT FROM`, `NOT (a = b)` o `GREATEST`/`LEAST`.

### 6-A-bis — Tablas en comentarios técnicos (6.1, 6.2)
GLPI no aplica estilo a las tablas y `style` con varias declaraciones usa punto y coma (prohibido). Usar **atributos HTML legados**:
- `<table border="1" cellpadding="4" cellspacing="0" width="100%">` siempre.
- `<th bgcolor="#e8e8e8" align="left">`.
- Estado: Confirmada `#e6f4ea`, Descartada `#fbeaea`, Complementaria `#fff6e0`, Informativa `#e8f0fb`.
- Matriz de maestros: fila del caso con el nombre en `<b>`, toda celda que se aparta del patrón mayoritario con `bgcolor="#fbeaea"` (todas las atípicas, no solo el caso), fila final "Patrón mayoritario de la columna" con `bgcolor="#f0f0f0"` e `<i>`.
- Máximo 4–5 columnas, celdas cortas, sin listas ni párrafos dentro de `<td>`. Si no entra, priorizar las columnas que sustentan la conclusión y conservar el formato. Las `EM_*` no relacionadas van en una sola fila agrupada (motor Paso 4). Nunca tablas como texto separado por `|`. Nunca en §7/6.3.

### 6-B — Qué escribe este flujo
**Solo escribe en GLPI:**
- `glpi_itilfollowups`: comentarios (6.1, 6.2, 71–80, aclaración, capacitación, proyecto no registrado, repo inaccesible, estructura no detectada, límite de reanálisis).
- `glpi_tickettasks`: `ANÁLISIS INICIAL` (81–89).
- `glpi_itilsolutions`: `SOLUCIÓN AL CASO` (90–100).
- `glpi_tickets`: categoría, impacto, prioridad y `status` (6.4, 2-A, 4.0).
- `glpi_tickets_users`: asignación `type = 2` (6.4).
- `glpi_plugin_fields_ticketticketsformfields`: solo `scoreagentefield` y `plugin_fields_aplicaiafielddropdowns_id` (6-C).
- Tabla plugin **Fuente de solicitud** (solo Capacitación, 4.0).
- `sidesoft_triage_glpi_log` (Paso 7).

**Nunca escribe en la BD del ERP del cliente.** Cualquier `INSERT`/`UPDATE`/`DELETE`/DDL sobre Openbravo va como texto en §5/§6 del 6.2, con el encabezado:
```
⚠️ Script sugerido — requiere revisión y ejecución manual de un técnico.
No fue ejecutado automáticamente. Agregar el punto y coma al final de cada sentencia antes de ejecutar.
```
Obligatorio adjuntarlo cuando la solución (o una hipótesis que, confirmada, exige corrección) implica cambiar filas; sin BD disponible, plantilla con placeholders y la condición "ejecutar solo tras confirmar el SELECT". Dato roto a nivel técnico (ej. fila no editable en pantalla) → script, no rodeo de UI. Con Fase 1 y Fase 2 (5-B.7): bloques separados (`Fase 1 — corrección puntual` / `Fase 2 — corrección masiva, no ejecutar sin revisión`) con el número de registros afectados.

---

## Paso 7 — Registrar en el histórico

```sql
INSERT INTO sidesoft_triage_glpi_log
  (ticket_id, proyecto_glpi, repo_cliente, estado_procesamiento, nivel_sla, criticidad, area_funcional,
   categoria_glpi, impacto, prioridad, followup_score_id, followup_analisis_id, followup_publico_solucion_id,
   score_acertividad, campos_ticket_actualizados, tecnico_asignado, tickets_referencia, playbook,
   version_skill, tipo_caso, gate_resultado, evidencia_json,
   respuesta_modelo_raw, resultado, detalle_error)
VALUES
  ({ticket_id}, '{proyecto}', '{owner}/{repo}', '{estado}', '{nivel_sla}', '{criticidad}', '{area_funcional}',
   '{categoria_glpi}', '{impacto}', '{prioridad}', {id_sla_score_o_null}, {id_parte1_o_null}, {id_canal_6_3_o_null},
   {score_final_o_null}, {1_o_0}, '{usuario_asignado_o_null}', '{ids_3D_o_null}', '{playbook_o_null}',
   '{version_skill}', '{tipo_caso_o_null}', '{gate_resultado_o_null}', '{evidencia_json_o_null}',
   '{json_clasificacion}', '{ok_o_error}', {detalle_error_o_null});
```

- Si las columnas `version_skill`, `tipo_caso`, `gate_resultado` o `evidencia_json` aún no existen en la tabla (verificar con `pg_describe_table`), omitirlas del `INSERT` y guardar esos valores dentro de `respuesta_modelo_raw`.
- `followup_publico_solucion_id` lleva el id del canal 6.3 (solución, tarea o followup); con tarea, `respuesta_modelo_raw` indica `"canal_respuesta": "tarea"`. Todos los ids de las partes del análisis van en `respuesta_modelo_raw`, junto con `"reanalisis": N` cuando aplique.
- **`estado_procesamiento` (valores exactos):** `ok_alta_confianza` (análisis publicado, score **81–100**), `ok_baja_confianza` (análisis publicado, score **0–80**), `preguntas_enviadas`, `esperando_respuesta_cliente`, `capacitacion`, `proyecto_no_registrado`, `duplicado_abortado`, `error`.
- `nivel_sla` y `criticidad`: solo los valores de la tabla de 6.1.
- Registrar siempre, también en preguntas, espera, duplicado, no registrado o error (con los ids que sí se generaron).

---

## Reglas críticas (checklist final antes de publicar)

1. Nada inventado: técnicos, ventanas, columnas, causas y datos salen del ticket, el código o la BD de esta corrida; lo no confirmado va a §9 y baja el score.
2. Paso 4 antes que el Paso 3: duplicados, capacitación y espera se resuelven sin gastar consultas.
3. Ancla A → `ad_pinstance` auditado antes de cualquier explicación de flujo (si no, tope 70).
4. Comparación contra pares hecha (maestros hermanos si la causa es un flag), con todas las `EM_*` enumeradas por BD, las relacionadas comparadas una a una y decidida contra el patrón mayoritario.
5. Componente confirmado (o `COMPONENTE_NO_CONFIRMADO`), en su versión desplegada cuando hay BD; precedentes, tickets previos, reanálisis y playbooks verificados con un dato de este caso; fallos de IA validados en tickets similares considerados.
6. Alcance e impacto del cambio medidos cuando hay flujo compartido o cambio de configuración; volumen alto → Fase 1 / Fase 2; workaround y definitiva separados.
7. Script sugerido presente si hay que cambiar datos, sin punto y coma y con separadores; nada ejecutado sobre el ERP.
8. §7 con ruta de menú completa, etiqueta del campo, valor exacto, cómo verificar y qué hacer si no funciona.
9. §7 empieza por la causa identificada y corrige esa causa: nunca repite como hallazgo el síntoma del ticket ni ofrece un workaround como única solución. Con ancla E o causa de cálculo, mecanismo reproducido contra un caso OK o score máx. 70. Si existe un caso comparable, el dato que distingue está nombrado (motor 2.11) en la §7. Después, descenso hasta la causa terminal (motor 2.10). El canal público 6.3 lleva la §7 completa, incluidos "Qué identificamos" y "Por qué ocurre".
10. Gate 5-C aplicado; 9 secciones completas con §7; canal 6.3 según el rango del score final; `status` según 6.4 (nunca queda en Nuevo tras publicar el análisis); Score agente y Aplica IA escritos (6-C); campos de validación humana intactos.
11. Un solo `[TRIAGE-SLA-SCORE]`, `[TRIAGE-ANALISIS-9PASOS]` y Solución al Caso por ticket sin respuesta nueva del solicitante, sin comentarios de corrección posteriores. **Excepción:** si un análisis publicado omitió la §7 o el script obligatorio, un único followup privado `[TRIAGE-ANALISIS-9PASOS] Completar secciones faltantes` solo con lo omitido.
12. Cada escritura verificada por `SELECT` aparte, bajo ~3,2 KB, sin punto y coma, con tablas en atributos HTML legados.
13. Log registrado con valores exactos de estado, SLA y criticidad, versión de skill, tipo de caso, resultado del gate y bloque de evidencia.
