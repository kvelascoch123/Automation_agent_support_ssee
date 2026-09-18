---
name: triage-glpi-auto
description: Agente orquestador de triage automático de tickets GLPI (multi-cliente). Lee tickets Nuevos, resuelve a qué cliente/repo pertenece el solicitante vía registro_clientes/clientes.json, lee el contexto específico de ese cliente vía MCP GitHub (sin clonar), aplica el motor común de análisis de 9 pasos (openbravo-functional-ticket-analysis), que incorpora nativamente el chequeo de suficiencia de contexto (5 mínimos funcionales), el mapa dominio→módulos, el índice de conocimiento estático por módulo y el vocabulario de causa raíz, evalúa acertividad, aplica preguntas de aclaración cuando el contexto es insuficiente, y publica followups en GLPI. Maneja además dos casos que cortan el flujo de análisis: solicitudes de Capacitación (comentario público CX, estado Planificado, asignado a kvelasco, campo Fuente de solicitud = Capacitación) y Proyecto no registrado (marcador [TRIAGE-PROYECTO-NO-REGISTRADO], estado Planificado, asignado a bruno díaz). Antes de cerrar cualquier diagnóstico, aplica un módulo obligatorio de investigación de causa raíz en profundidad (trazabilidad de flujo completo hasta el componente técnico exacto —jrxml/SQL/trigger/función/clase Java—, generación y descarte de hipótesis alternativas —incluyendo cualquier ticket relacionado o precedente histórico, que se trata como hipótesis a validar contra datos concretos de este ticket, nunca como conclusión automática—, verificación del alcance real del patrón de datos, y verificación de consistencia cuando la corrección toca un valor de configuración replicado en varios campos/registros similares) en vez de detenerse en la primera causa aparente o en el primer archivo/precedente parecido. Detecta corridas concurrentes/duplicadas antes de publicar nada y garantiza, por corrida, exactamente un análisis de 9 pasos y una única respuesta sugerida al usuario (nunca una "segunda opinión" ni un comentario de corrección aparte).
---

# Agente Orquestador de Triage GLPI — ejecución automática (cron)

Este proceso corre sin intervención humana en cada ejecución programada.
No requiere frase disparadora ni confirmación — se ejecuta completo de inicio a fin cada vez que el Automation corre.

Este Automation está vinculado a UN SOLO repo (el **orquestador**) — nunca a los repos de cliente. Los repos de cliente se leen dinámicamente vía MCP de GitHub, según el proyecto del solicitante de cada ticket.

MCP-DB (servidor `sidesoft-db`, https://mcp-db.sidesoftcorp.com) se usa para dos cosas distintas, ambas vía el mismo servidor pero con `database` (alias) diferente:
- `database = "glpi"` → leer y escribir sobre la base de datos GLPI (compartida por todos los clientes, único alias con permiso de escritura de este flujo).
- `database = {openbravo_db_alias del cliente}` → consultar, siempre de solo lectura (`pg_query`/`pg_describe_table`, nunca `pg_execute`), la base Openbravo del cliente resuelto en el Paso 2 (proceso, datos y contabilidad — ver Paso 3-B).

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
    "base_path": null,
    "config_dir": null,
    "openbravo_db_alias": null
  },
  "ACTUARIA CONSULTORES S.A": {
    "owner": "Sidesoftpreprod",
    "repo": "ActuariaCodigoCompleto",
    "base_path": "actuaria",
    "config_dir": "registro_clientes/actuaria",
    "openbravo_db_alias": "actuaria"
  }
}
```

Cada entrada resuelve tres cosas distintas, que **nunca se derivan unas de otras** — hay que leerlas todas de acá, explícitamente, y no asumir ninguna por default:

- **`owner` / `repo`**: el **repo de código** del cliente — donde vive el código fuente real de Openbravo (`src-db`, `src-core`, `modules`, etc.) y `graphify-out/`. Es lo que usan el Paso 3-C y el Paso 5. **Tiene que ser el owner real de GitHub** (el que aparece en la URL del repo) — un owner mal cargado acá (ej. `"actuaria"` en vez de `"Sidesoftpreprod"`) produce 404 a nivel de repositorio completo, indistinguible a simple vista de un problema de permisos, y es el primer punto a revisar cuando algo da `REPO_INACCESIBLE` (Paso 2-B).
- **`base_path`** (opcional, string o `null`): la carpeta dentro de ese repo donde arranca el código, si no está en la raíz. Con Actuaria, todo el árbol de Openbravo está anidado bajo `actuaria/`, no en la raíz del repo. Si el repo trae el código directo en la raíz, dejarlo en `null` y el Paso 2-B lo detecta solo.
- **`config_dir`** (opcional, string o `null`): ruta **dentro del propio repo orquestador**, relativa a su raíz, donde vive la configuración específica de ese cliente — `cliente.json` (reglas propias), `integraciones.json` (desarrollos externos, ver Paso 3-C), `customizaciones/*.md`. Es una subcarpeta de `registro_clientes/` (ej. `registro_clientes/actuaria/`), **no un repo aparte**: se lee local, igual que `clientes.json`, sin MCP de GitHub y sin el riesgo de un owner/repo mal cargado en un tercer repositorio. Si es `null`, el Paso 3 no busca esos archivos en ningún lado y lo registra como "sin `config_dir` configurado" — estado legítimo, no error.

`openbravo_db_alias` identifica la BD de Openbravo (PostgreSQL) de ese cliente para verificaciones de proceso, datos y contabilidad — es el valor de la columna "ALIAS MCP" del Panel MCP (https://mcp-db.sidesoftcorp.com/admin/databases), no un nombre inventado. El servidor MCP-DB ya está activo para todos los alias ahí listados; lo único pendiente por cliente es completar este campo en `clientes.json` con el alias exacto (ver Paso 3-B para cómo se usa). Mientras esté en `null`, el análisis procede solo con conocimiento estático, sin verificación en BD real; si el ticket trae ancla clase A (error de proceso/BD), eso fuerza tope de score (Paso 6.1).

Este registro es la única fuente de verdad de qué proyectos GLPI están habilitados y a qué repo, `base_path` y `config_dir` corresponde cada uno. Agregar un cliente nuevo = una entrada nueva aquí (y su carpeta `registro_clientes/<cliente>/` si aplica) — no requiere tocar esta skill.

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
   - **No existe esa clave** → el proyecto no está habilitado en el registro. Registrar en el log `estado_procesamiento = 'proyecto_no_registrado'`, aplicar el Paso 2-A, y no procesar más este ticket en esta corrida.
   - **Existe** → obtener `{owner, repo}` de esa entrada y continuar al Paso 3.

Si el propio Paso 2, punto 1, ya terminó sin proyecto (consulta vacía), aplica el mismo tratamiento: registrar `estado_procesamiento = 'proyecto_no_registrado'` y aplicar el Paso 2-A.

---

## Paso 2-A — Acciones cuando el proyecto no está registrado (Caso Proyecto no registrado)

Cuando el Paso 2 termina con `estado_procesamiento = 'proyecto_no_registrado'` (proyecto no resuelto para el solicitante, o resuelto pero sin entrada en `clientes.json`):

1. Publicar un comentario privado (`is_private = 1`) iniciando con el marcador literal `[TRIAGE-PROYECTO-NO-REGISTRADO]`, indicando que el proyecto del solicitante no está registrado/habilitado en el flujo automático y que el ticket queda para revisión manual.
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '[TRIAGE-PROYECTO-NO-REGISTRADO] {detalle}', 1, 0, NOW(), NOW(), 1);
```

2. Actualizar el estado del ticket a **En curso (planificado)** (`status = 3`) y asignar el técnico al usuario **bruno díaz**:
```sql
UPDATE glpi_tickets SET status = 3, date_mod = NOW() WHERE id = {ticket_id};
```
La asignación vive en `glpi_tickets_users` (`type = 2`), mismo patrón de verificación que el resto del flujo:
```sql
-- si no existe fila type=2 para este ticket:
INSERT INTO glpi_tickets_users (tickets_id, users_id, type)
VALUES ({ticket_id}, {ID_BRUNODIAZ}, 2);
-- si ya existe, actualizarla en vez de insertar:
UPDATE glpi_tickets_users SET users_id = {ID_BRUNODIAZ} WHERE tickets_id = {ticket_id} AND type = 2;
```

3. No ejecutar el resto del flujo (Paso 3 en adelante) para este ticket en esta corrida — ya quedó registrado y asignado para revisión manual.

**Nota:** `{ID_BRUNODIAZ}` debe reemplazarse por el ID numérico real del usuario bruno díaz en GLPI (mismo procedimiento que `{ID_KVELASCO}`, ver Nota del Paso 6.4), antes de usar esta skill en producción.

---

## Paso 2-B — Verificar acceso al repo de código y determinar el `base_path`

Existe para impedir dos fallos concretos ya ocurridos, distintos entre sí aunque ambos se vean como "no encontré el archivo":

1. Para el cliente ACTUARIA, el repo de código (`Sidesoftpreprod/ActuariaCodigoCompleto`) **sí existe y es accesible**, pero todo el árbol real de Openbravo (`src-db`, `src-core`, `modules`, `graphify-out`) está anidado bajo una carpeta `actuaria/`, no en la raíz. La skill asumía raíz por defecto, así que cada lectura fallaba con 404 aunque el repo estuviera perfectamente accesible.
2. Independiente de eso, un repo puede directamente no ser accesible (404 a nivel de repositorio, no de archivo) — típicamente porque `clientes.json` tiene el `owner`/`repo` mal cargado, o porque el token/App de GitHub del MCP no tiene ese repo privado habilitado.

Ambos casos se ven igual si no se los distingue explícitamente — este paso separa uno de otro **antes** de que el Paso 3-C o el Paso 5 intenten leer nada.

### 1. Verificar acceso al repo
Hacer una llamada liviana al MCP de GitHub contra `{owner, repo}` (repo de código) resuelto en el Paso 2 — listar la raíz del repo (`get_file_contents` con path vacío).

- **Si devuelve 404 a nivel de repositorio** (no de un archivo puntual): registrar `REPO_INACCESIBLE` en la sección 9 (nunca `OMITIDO`), publicar un comentario privado adicional con el marcador `[TRIAGE-REPO-INACCESIBLE]` señalando que `registro_clientes/clientes.json` tiene un `{owner, repo}` inválido o sin permisos para este cliente y necesita corrección manual, y continuar el análisis solo con conocimiento estático. **No seguir al punto 2** — sin acceso al repo no hay nada que detectar.
- **Si responde con el listado de la raíz**: continuar al punto 2.

### 2. Determinar el `base_path` (dónde arranca el código Openbravo real)

- **Si `clientes.json` ya trae `base_path` cargado** para este cliente (ej. `"actuaria"` para ACTUARIA): usarlo directo, sin detectar nada. Ir al punto 3.
- **Si `base_path` es `null` o no está**, auto-detectar con el listado de la raíz ya obtenido en el punto 1:
  a. Revisar si alguna carpeta típica de un repo de Openbravo (`src-db`, `src-core`, `modules`, `graphify-out`) aparece **directamente en la raíz**. Si aparece al menos una → el código está en la raíz, `base_path = ""` para esta corrida.
  b. Si ninguna aparece en la raíz, listar las carpetas de primer nivel una por una y revisar si **exactamente una** de ellas contiene, un nivel más abajo, alguna de esas mismas carpetas típicas (como `actuaria/` en este caso, que contiene `src-db`, `src-core`, `modules`, `graphify-out`). Si hay exactamente una candidata → usarla como `base_path` para esta corrida.
  c. **Si hay cero candidatas, o hay más de una** (ambigüedad — no se puede decidir solo): no asumir ninguna. Registrar `ESTRUCTURA_NO_DETECTADA` en la sección 9, publicar comentario privado señalando la ambigüedad encontrada (listar las carpetas candidatas, si las hubo), y continuar sin graphify/código para esta corrida — mismo tratamiento de fondo que `OMITIDO`, pero con motivo explícito y distinguible.
  d. Cuando la auto-detección sí resuelve un `base_path` (casos a o b), anotarlo en el comentario privado de análisis como sugerencia para cargarlo en `clientes.json` y ahorrarse la detección en corridas futuras de ese mismo cliente.

### 3. Usar el `base_path` resuelto
Todas las lecturas del Paso 3-C y del Paso 5 (graphify, código fuente) se hacen prefijando `{base_path}/` a la ruta que pedían antes (ej. `{base_path}/graphify-out/manifest.json`, `{base_path}/src-db/...`). Si `base_path` quedó en `""`, es exactamente el comportamiento que la skill ya tenía (rutas desde la raíz).

---

## Paso 2-C — Fijar el contexto resuelto del cliente para toda la corrida

Con el Paso 2 (proyecto → cliente) y el Paso 2-B (acceso + `base_path`) ya resueltos, consolidar todo en un único bloque antes de seguir — cada paso siguiente **lee de acá**, no vuelve a derivar nada por su cuenta:

```
contexto_cliente = {
  proyecto:            {proyecto resuelto en el Paso 2},
  owner, repo:         {repo de código, Paso 2 / clientes.json},
  base_path:           {resuelto en el Paso 2-B — "" si el código está en la raíz},
  openbravo_db_alias:  {de clientes.json, o null},
  config_dir:          {de clientes.json, o null — carpeta local en el repo orquestador}
}
```

Este bloque es lo que efectivamente viaja al resto del flujo (Paso 3 usa `config_dir`; Paso 3-B usa `openbravo_db_alias`; Paso 3-C y Paso 5 usan `owner`/`repo`/`base_path`). Ningún paso posterior vuelve a leer `clientes.json` desde cero ni reinterpreta el proyecto — todos consumen este mismo objeto ya resuelto, para evitar que una corrida use un dato de un cliente y otra un dato de otro por error de contexto entre pasos.

---

## Paso 3 — Leer la configuración específica del cliente

`cliente.json`, `integraciones.json` y `customizaciones/*.md` viven **en el propio repo orquestador**, bajo `config_dir` (ej. `registro_clientes/actuaria/`) — no en el repo de código del cliente. Es una lectura local, igual que `clientes.json` en el Paso 0, sin MCP de GitHub:

- **Si `contexto_cliente.config_dir` está definido**: leer de ahí, localmente:
  - `{config_dir}/cliente.json` (reglas propias del cliente, si difieren del estándar: SLA, umbrales, etc.)
  - `{config_dir}/integraciones.json` — registro de integraciones/desarrollos externos del cliente que escriben datos directamente en Openbravo (ver Paso 3-C).
  - Archivos de customización/documentación relevantes (ej. `{config_dir}/customizaciones/*.md`) que ayuden al diagnóstico.
- **Si `config_dir` es `null` o no está**: no intentar leer estos archivos en ningún lado. Registrar en la sección 9 "sin `config_dir` configurado" — es un estado legítimo, no un error ni un intento fallido — y continuar el análisis solo con el conocimiento común (las skills del repo orquestador).

**Nota:** `graphify-out/` y el código fuente **sí** viven en el repo de código (`contexto_cliente.owner`/`repo`, con `base_path`) — es específico de cada instalación de Openbravo, y es un repo distinto del orquestador. No mezclar las rutas de uno con las del otro.

Si alguno de los archivos de este paso no existe bajo `config_dir` (pero la carpeta sí), continuar el análisis solo con el conocimiento común y anotarlo en el comentario privado de análisis del Paso 6 — eso sigue siendo `OMITIDO` normal.

---

## Paso 3-C — Verificar si el módulo/ventana afectada tiene una integración externa registrada

Existe para impedir un fallo concreto ya ocurrido: un ticket reportaba que no había comprobantes de retención de un mes cargados en Openbravo, y el análisis concluyó que el proceso era manual y faltaba registrarlo a mano — sin detectar que un desarrollo externo (servicio que recibe datos de un tercero, ej. Taxo, y crea esos comprobantes automáticamente) es la vía normal por la que esos registros aparecen. La causa raíz real a investigar era la sincronización de ese servicio, no la falta de carga manual.

1. Con `{config_dir}/integraciones.json` leído en el Paso 3 (si existe), buscar si alguna integración registrada escribe sobre el mismo módulo/ventana/tipo de documento que reporta el ticket (ej. "Comprobante de Retención" / tipo de documento "RETENCIONES CLIENTES").
2. **Si hay match** (existe una integración registrada para esa ventana/documento): la causa raíz candidata pasa a incluir, como hipótesis principal a validar, una falla o atraso en esa sincronización — no solo "falta de registro manual". El diagnóstico del Paso 5 y la §7 (respuesta al usuario) deben pedir explícitamente verificar el estado de esa integración (último envío recibido, errores del servicio, si el tercero efectivamente envió los datos del período en cuestión) como parte de la solución, antes o junto con la opción de registrar el comprobante a mano.
3. **Si no hay match, o `integraciones.json` no existe (o no hay `config_dir` configurado para este cliente)**: continuar el análisis solo con las hipótesis habituales (proceso manual, configuración, etc.) y anotarlo explícitamente en el comentario privado del Paso 6 — nunca asumir en silencio que no hay integración solo porque no se encontró el archivo; declararlo `SIN REGISTRO`.
4. Este chequeo es una **fuente de evidencia obligatoria** — ver la tabla del Paso 5-EVIDENCIA. No sirve como evidencia "no encontré integraciones" sin haber intentado leer `integraciones.json` (o el archivo equivalente) primero.

**Nota:** el nombre y la ubicación exacta de este archivo por cliente (`integraciones.json` u otro) hay que confirmarlos contra la estructura real de cada repo — mismo tipo de verificación pendiente que `{ID_KVELASCO}` en el Paso 6.4. Mientras no exista ese archivo para un cliente dado, el punto 3 aplica (`SIN REGISTRO`) y conviene proponerle al cliente documentar ahí sus integraciones conocidas (nombre, ventana/tabla que alimenta, tipo de documento, cómo verificar su estado).

---

## Paso 3-A — Extraer datos accionables de `Detalles Adicionales:` (si el ticket tenía imágenes)

`texto_limpio` puede traer, al final, una sección `Detalles Adicionales:` con el texto que un modelo de visión (Abacus, vía n8n) extrajo de cada imagen del ticket — pantallazos de pantallas del ERP, facturas, comprobantes, etc. Esa sección viene tal cual la devolvió el modelo: mezcla campos útiles con ruido (etiquetas de UI, campos vacíos, texto decorativo). Este paso decide qué de eso sirve como **filtro concreto** para la verificación en BD del Paso 3-B, y qué se descarta.

1. **Si `texto_limpio` no trae `Detalles Adicionales:`**, no hay nada que extraer aquí — ir directo al Paso 3-B con los datos que ya traiga la descripción original del ticket (si el usuario escribió un número de documento a mano, por ejemplo).

2. **Si trae `Detalles Adicionales:`**, de cada bloque `Imagen N:` extraer únicamente los campos con valor real que sirvan como identificador o filtro de una fila en BD:
   - Números de documento: Nº documento, Nº de factura, Nº de pedido, Nº de nota de crédito/débito, número de comprobante.
   - Montos: total cobrado, total pendiente, total mora, importe, saldo.
   - Fechas: fecha de pago, fecha de vencimiento, fecha de emisión.
   - Identificadores de tercero/cliente: nombre o CI/NIF del cliente, razón social.
   - Tipo de documento y organización/sucursal, cuando ayuden a acotar la tabla o el `WHERE`.

   **Descartar** (no pasa al Paso 3-B): etiquetas de campo sin valor, campos marcados por el propio modelo como vacíos o en cero salvo que el ticket trate justamente de por qué algo está en cero, texto puramente decorativo (logos, headers de sección, nombres de columnas de una tabla sin sus valores), y cualquier dato que no identifique una fila concreta (colores resaltados, formato visual, etc. — esos van al análisis funcional del Paso 5, no a un filtro SQL).

3. **Decidir viabilidad del análisis en BD** con el resultado de la extracción:
   - **Viable** — se logró al menos un identificador concreto y único (número de documento/factura/pedido, o la combinación tercero + fecha + monto). Pasar estos valores como filtros literales al `WHERE` de las consultas del Paso 3-B, en vez de hacer `SELECT` exploratorios sin acotar.
   - **No viable** — `Detalles Adicionales:` solo trae campos genéricos, vacíos, o ninguno de los anteriores. Continuar el Paso 3-B igual si la descripción original (no la imagen) ya trae un identificador propio; si tampoco lo trae, anotar en el comentario privado: *"Imagen adjunta sin datos suficientes para acotar una verificación en BD — se revisó solo con conocimiento estático."* y no ejecutar `pg_query` a ciegas sin `WHERE`.

4. Dejar registro de qué identificadores se usaron (o por qué no se usó ninguno) — es el dato probatorio que exige el registro de evidencia del Paso 5-EVIDENCIA cuando la fuente sea "BD del ERP".

---

## Paso 3-B — Verificación en BD de Openbravo (proceso, datos y contabilidad; solo lectura)

Si el cliente tiene `openbravo_db_alias` distinto de `null` en el registro, y el ticket trae al menos un identificador usable (Paso 3-A o descripción), consultar la BD del cliente. **No limitar este paso a descuadres contables**: aplica siempre que haya documento/proceso con síntoma verificable en datos.

**Disparadores (cualquiera basta):**
- Descuadre, asiento o cuenta contable (criterio en `openbravo-functional-ticket-analysis`, Paso 3).
- **Ancla clase A** del Paso 1.5 del motor: error SQL/constraint/`ERROR=` / fallo al Completar, Registrar, Procesar, Contabilizar o Generar.
- Documento concreto con inconsistencia de montos, estados, líneas, plan de pagos, o campos `em_*` sospechosos.
- Hipótesis de dato maestro/configuración que exige comparar valores vivos (Paso 5-B / motor Paso 2 punto 7).

1. Usar la herramienta MCP-DB (servidor `sidesoft-db`, https://mcp-db.sidesoftcorp.com) para consultar la base del cliente. El parámetro `database` de estas herramientas debe recibir EXACTAMENTE el valor de `openbravo_db_alias` del cliente resuelto en el Paso 2 — es un alias lógico, no el host ni credenciales reales; ese mapeo lo resuelve el servidor MCP-DB, no esta skill.
2. Antes de consultar tablas que no se conozcan de memoria, usar `pg_describe_table` (parámetros: `database` = alias del cliente, `table` = nombre de tabla) para confirmar el esquema real en vez de asumirlo.
3. Usar `pg_query` (parámetros: `database` = alias del cliente, `query` = SQL) para todas las consultas — nunca `pg_execute` contra un alias de cliente (ver Regla dura abajo). Consultar con `SELECT` filtrado y `LIMIT` las tablas necesarias (`C_Order`, `C_Invoice`, `Fact_Acct`, `C_Payment`, tablas satélite `em_*`, etc.), siguiendo la disciplina SQL de `openbravo-functional-ticket-analysis`. **Si el Paso 3-A extrajo identificadores concretos, usarlos como filtro `WHERE`** — búsqueda dirigida, no exploración genérica.
3-A. **Auditoría de fallo de proceso (obligatoria si ancla clase A)** — ejecutar **antes** de explicar estados generales, reglas de facturación/entrega o "comportamiento esperado":
   1. Resolver `record_id` del documento (`c_order_id`, `c_invoice_id`, etc.) por `documentno` u otro ID del ticket.
   2. Consultar:
      ```sql
      SELECT p.ad_pinstance_id, p.ad_process_id, pr.value AS process_value, pr.name AS process_name,
             p.result, p.errormsg, p.created, p.ad_user_id
      FROM ad_pinstance p
      LEFT JOIN ad_process pr ON pr.ad_process_id = p.ad_process_id
      WHERE p.record_id = '{record_id}'
      ORDER BY p.created DESC
      LIMIT 25;
      ```
   3. Si hay `result = 0` (o equivalente) y `errormsg` alineado al síntoma: la causa candidata es el **fallo de ese proceso**. Queda **prohibido** cerrar solo con "genere albarán / factura" o "Proformado es esperado" sin haber explicado y seguido ese `errormsg`.
   4. Comparar el documento del caso contra 2–5 **hermanos exitosos** de la misma familia (mismo doctype/org/flujo): campos `em_*` que el proceso o sus EP tocan, filas hijas esperadas (líneas, schedules, tablas satélite), y maestros referenciados **en la misma combinación** que usa el documento (producto en tarifa activa, oferta con filas hijas, etc.).
   5. Desambiguar homónimos del error (motor Paso 1.5 punto 2): p.ej. columna numérica `pricelist` ≠ `m_pricelist_id` (Tarifa).
4. Usar el resultado real para confirmar o descartar la hipótesis de causa raíz antes de redactar el análisis del Paso 5.
4-B. **Si alguna fila devuelta trae en `null` un campo que estructuralmente debería estar poblado** para que el documento/transacción opere con normalidad (ej. `c_bpartner_id` en `fin_payment_scheduledetail`; o campos de extensión que un EP/proceso espera no-nulos — comparar contra otras filas del mismo tipo que sí los traen poblados), no tratar eso solo como dato de contexto. Es evidencia de una posible **inconsistencia técnica en la fila**, y debe registrarse explícitamente como candidato de causa raíz — cruzarlo contra el vocabulario de causa raíz de `openbravo-functional-ticket-analysis` antes de descartarlo. Si corresponde una corrección a nivel de datos, aplicar el Paso 6-B (script de corrección sugerido, solo texto) — el diagnóstico no puede cerrarse únicamente con un rodeo funcional para el usuario final cuando la BD ya mostró el dato roto.
5. Si `pg_query` falla contra el alias configurado (conexión caída, alias inexistente), usar `pg_list_databases` para confirmar qué alias están disponibles en esta corrida, registrar la incidencia en el log, y continuar sin esta verificación.
6. Si `openbravo_db_alias` es `null` (cliente sin base Openbravo asociada), continuar sin esta verificación y anotarlo explícitamente en el comentario privado: *"Diagnóstico basado solo en conocimiento estático — verificación en BD del ERP no disponible para este cliente."* Si además la ancla era clase A, la fila de evidencia de `ad_pinstance` queda `NO DISPONIBLE` y aplica el tope de score del Paso 6.1.

**Regla dura**: esta consulta es SIEMPRE de solo lectura, siempre vía `pg_query`. `pg_execute` (lectura/escritura) está reservado exclusivamente para el alias interno `glpi`; nunca se usa contra el alias de un cliente. Ningún `INSERT`/`UPDATE`/`DELETE`/`DDL` se ejecuta contra la BD de Openbravo del cliente en modo automático — ver Paso 6-B para cómo se maneja una corrección sugerida.

**Regla dura — prioridad del ancla:** si coexisten un error de proceso/BD (clase A) y un estado de negocio tipo Proformado / "falta albarán", **manda la clase A**. La comparación de doctype/hermanos maestros (Paso 5-B) sigue siendo obligatoria, pero **después** de la auditoría 3-A, y no puede usarse sola para cerrar como "no hay error" mientras `ad_pinstance` muestre fallos alineados al síntoma.

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

### 4.-1 — Detectar corrida concurrente o duplicada (verificar antes que cualquier otro caso)

Revisar si en el historial recién leído ya existe un comentario `[TRIAGE-SLA-SCORE]`, `[TRIAGE-ANALISIS-9PASOS]` o `[TRIAGE-RESPUESTA-SUGERIDA]` publicado por `bot.glpi` en los **últimos 15 minutos**, sin que exista entre ese comentario y este momento una respuesta nueva del solicitante.

- **Existe** → esta corrida es una ejecución concurrente/duplicada del mismo ticket (ej. n8n disparó el Automation dos veces para el mismo evento, o una corrida quedó reintentando). No publicar ningún comentario nuevo, no repetir el análisis ni la respuesta sugerida. Registrar en `sidesoft_triage_glpi_log`: `estado_procesamiento = 'duplicado_abortado'`, referenciando el id del comentario ya existente, y terminar el procesamiento de este ticket en esta corrida.
- **No existe** → continuar normalmente a 4.0.

Este chequeo existe para impedir un fallo concreto ya ocurrido: en el ticket 9827, dos corridas concurrentes publicaron cada una su propio `[TRIAGE-SLA-SCORE]`/`[TRIAGE-ANALISIS-9PASOS]`/`[TRIAGE-RESPUESTA-SUGERIDA]` con ids de análisis consecutivos (13767-13769), duplicando por completo la salida del flujo para el mismo ticket. Si el mismo proyecto sigue mostrando corridas concurrentes de forma recurrente pese a este chequeo, la causa de fondo está en el disparador de n8n (falta de idempotencia al encolar el Automation para un mismo ticket), no en este paso — este chequeo solo contiene el síntoma dentro del Automation, no lo resuelve en la fuente.

### 4.0 — Detectar caso Capacitación (corta el flujo, no entra a 4.1 en adelante)

Antes de evaluar suficiencia de contexto o disparar el motor de análisis, revisar si el ticket es una **solicitud de capacitación** y no una incidencia/consulta funcional.

Traer el asunto del ticket vía MCP-DB (alias `glpi`) — el payload de entrada no trae el asunto, solo `texto_limpio`:
```sql
SELECT name, content FROM glpi_tickets WHERE id = {ticket_id};
```

Se considera **Caso Capacitación** si el asunto (`name`) o la descripción (`content` / `texto_limpio`) contienen, sin distinguir mayúsculas ni tildes, alguna de estas raíces: `capacitac` (cubre capacitación/capacitacion/capacitaciones), `entrenamiento`, `training`.

**Si aplica**, no ejecutar 4.1 en adelante ni el Paso 5 (motor de 9 pasos) para este ticket. En su lugar:

1. Publicar un único comentario, **esta vez público** (`is_private = 0` — única excepción de este flujo a la regla de "todo comentario es privado", justamente porque este mensaje es para el solicitante), en tono cercano/CX, indicando que se evaluará la capacitación solicitada y que se confirmará el día:
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_cx_capacitacion_html}', 0, 0, NOW(), NOW(), 1);
```
`{comentario_cx_capacitacion_html}` — ejemplo de tono: *"Gracias por tu solicitud. Vamos a evaluar la capacitación solicitada y te confirmaremos la fecha en la que se realizará."*

2. Actualizar el estado del ticket a **En curso (planificado)** (`status = 3`) y asignar el técnico al usuario **kvelasco**:
```sql
UPDATE glpi_tickets SET status = 3, date_mod = NOW() WHERE id = {ticket_id};
```
La asignación vive en `glpi_tickets_users` (`type = 2`), mismo patrón de verificación que el resto del flujo (ver Paso 6.4):
```sql
-- si no existe fila type=2 para este ticket:
INSERT INTO glpi_tickets_users (tickets_id, users_id, type)
VALUES ({ticket_id}, {ID_KVELASCO}, 2);
-- si ya existe, actualizarla en vez de insertar:
UPDATE glpi_tickets_users SET users_id = {ID_KVELASCO} WHERE tickets_id = {ticket_id} AND type = 2;
```

3. Actualizar el campo plugin **"Fuente de solicitud"** al valor **"Capacitación"**:
```sql
-- ⚠️ Verificar con pg_describe_table (alias glpi) el nombre real de la tabla/columna plugin de
-- "Fuente de solicitud" y el id del valor "Capacitación" en su tabla de dropdown asociada,
-- antes de usar esta skill en producción — igual que {ID_KVELASCO} (ver Nota del Paso 6.4).
UPDATE {tabla_plugin_fuente_solicitud}
SET {columna_fuente_solicitud} = {ID_VALOR_CAPACITACION}
WHERE items_id = {ticket_id};
-- si no existe fila para este ticket en esa tabla plugin, hacer INSERT en su lugar.
```

4. Registrar en `sidesoft_triage_glpi_log`: `estado_procesamiento = 'capacitacion'`.
5. Terminar el procesamiento de este ticket en esta corrida — no continuar a 4.1, Paso 5 ni Paso 6.

**Si no aplica**, continuar en 4.1.

### 4.1 — ¿Ya se enviaron preguntas de aclaración antes?
Buscar entre los followups un comentario (privado) que inicie con el marcador `[TRIAGE-ACLARACION]`.

- **No existe ese marcador** → ir a 4.3 (evaluación de suficiencia de contexto, primera pasada).
- **Existe** → ir a 4.2.

### 4.2 — ¿El solicitante ya respondió después de esas preguntas?
Buscar followups con `date_creation` posterior al comentario `[TRIAGE-ACLARACION]` y `users_id` distinto de 148 (`bot.glpi`), es decir, del solicitante u otro usuario real.

- **No hay respuesta posterior** → el ticket sigue esperando al cliente. Registrar en el log `estado_procesamiento = 'esperando_respuesta_cliente'` y terminar sin publicar ningún comentario nuevo. No repetir preguntas ya enviadas.
- **Sí hay respuesta posterior** → tomar ese contenido como **"respuesta de aclaración"**, combinarlo con la descripción original del ticket como contexto ampliado, y continuar directo al **Paso 5** (saltar 4.3, el contexto ya se dio por bueno una vez que el cliente respondió).

### 4.3 — Evaluar si el contexto es suficiente (primera pasada, sin preguntas previas)
Aplicar el **Paso 0-A (5 mínimos funcionales)** de `openbravo-functional-ticket-analysis` sobre la descripción del ticket — es la misma evaluación, no un chequeo aparte del orquestador:

- **Faltan 2 o más** → contexto insuficiente → ir a **4.4 (preguntas de aclaración)**.
- **Faltan 0 o 1** → contexto suficiente → ir directo al **Paso 5**, señalando igual el dato faltante en el comentario privado.

### 4.4 — Generar preguntas de aclaración (máximo 8, técnico-funcionales)
- Usar el **mapa dominio→módulos** de `openbravo-functional-ticket-analysis` (Paso 5B) para identificar el módulo probable y orientar las preguntas a cerrar exactamente los mínimos ausentes del Paso 0-A (no preguntas genéricas tipo "¿puede dar más detalles?").
- Redactar entre 3 y 8 preguntas concretas, dirigidas al solicitante.
- Publicar **un único comentario PRIVADO** (`is_private = 1`), iniciando con el marcador literal `[TRIAGE-ACLARACION]`, listando las preguntas en formato numerado.
- Cualquier hipótesis de causa que ya se intuya con el contexto parcial disponible se documenta en la tabla de hipótesis del motor (Paso 4 de `openbravo-functional-ticket-analysis`) cuando el ticket vuelva a analizarse con la respuesta del cliente — no en este comentario, que es solo para el solicitante.
- **No aplicar ningún otro comentario en esta corrida.**
- Registrar en `sidesoft_triage_glpi_log`: `estado_procesamiento = 'preguntas_enviadas'`.
- Terminar el procesamiento de este ticket en esta corrida.

> **⚠️ Limitación conocida al pasar este comentario a privado**: el solicitante NO puede ver comentarios privados en GLPI, por lo tanto nunca verá estas preguntas ni podrá responderlas dentro del ticket. El Paso 4.2 (detectar respuesta del cliente) dejará de poder cumplirse por esta vía — el ticket quedará indefinidamente en `esperando_respuesta_cliente` a menos que se defina otro canal para hacerle llegar las preguntas (correo, WhatsApp, o que un humano las traslade manualmente). Pendiente de resolver.

---

## Paso 5 — Ejecutar el análisis funcional completo (motor: `openbravo-functional-ticket-analysis`)

**Orden obligatorio con el motor:** aplicar primero el **Paso 1.5** (ancla A/B/C/D). Si es clase A, el resultado del Paso 3-B punto 3-A (`ad_pinstance`) es entrada obligatoria del diagnóstico — no opcional ni solo "si es contable".

**Lectura de conocimiento:**

1. Identifica el módulo/concepto probable con el mapa dominio→módulos de `openbravo-functional-ticket-analysis` (Paso 5B) y, si el proyecto lo tiene cargado, el índice de conocimiento estático por módulo (Paso 5B-bis de esa misma skill).
2. Consulta `graphify-out/` del repo del cliente. Es un paso obligatorio, pero acotado a lo que el grafo realmente puede responder — ver *Qué esperar de graphify* abajo.
3. Lee el código fuente real del cliente vía MCP de GitHub. Para incidencias cuya causa está en la lógica de base de datos, este es el paso que resuelve, no el grafo.

Si algo de esto no se ejecuta, declararlo como omitido en la sección 9 del análisis. **Nunca escribir que se revisó una fuente que no se abrió en esta corrida**, ni apoyarse en la conclusión de una corrida anterior para afirmar evidencia en la actual.

#### 3-bis. Rastreo obligatorio del componente exacto (no sustituir por un archivo "parecido")

Existe para impedir un fallo concreto ya ocurrido: ante un documento impreso con datos incorrectos, `graphify-out/manifest.json` no resolvió la ruta (404) y, en vez de rastrear el proceso real, el análisis tomó como base un `.jrxml` de un módulo distinto (Sales Order) solo porque estaba disponible y "parecía" relacionado, sin confirmar que fuera el archivo que efectivamente genera ese documento. La causa raíz resultante quedó construida sobre un componente no verificado.

Cuando graphify no resuelve el archivo por nombre, **simular el proceso real en vez de suponer un componente similar**: reconstruir la cadena completa hasta identificar con certeza el artefacto responsable —

```
Ventana/proceso/botón que el usuario dispara
  → definición del reporte o proceso (AD_Process, AD_ReportView, o el proceso/reporte configurado en la ventana)
  → plantilla de impresión exacta (jrxml) o consulta/función que arma el documento
  → función(es) PL/pgSQL, trigger(s) o clase(s) Java involucradas
```

- Cada eslabón se confirma leyendo el código o la configuración real (Application Dictionary, referencias cruzadas en el propio repo, o el resultado de `manifest.json` filtrado por módulo) — nunca se asume por similitud de nombre o de módulo.
- Si no se logra confirmar el eslabón siguiente con las fuentes disponibles en esta corrida, no se continúa el diagnóstico sobre un archivo "candidato" sin confirmar: se declara el estado `COMPONENTE_NO_CONFIRMADO` en la sección 9 (ver tabla de evidencia del Paso 5-EVIDENCIA) y la sección 4 (Causa raíz) no puede marcarse como "Confirmada" apoyada en ese archivo — como máximo queda como hipótesis a confirmar por un técnico.
- Este mismo rastreo aplica a cualquier incidencia cuya causa esté en un proceso, trigger, función o reporte del sistema — no es exclusivo de documentos impresos.

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

La salida (número de entradas + lista de archivos indexados del módulo) es el **dato probatorio** que exige el registro de evidencia del Paso 5-EVIDENCIA.

---

### Paso 5-EVIDENCIA — Orden de fuentes, precedencia de la memoria y registro de evidencia

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
| `graphify-out/manifest.json` | LEÍDO / OMITIDO / REPO_INACCESIBLE / ESTRUCTURA_NO_DETECTADA | nº de entradas y archivos indexados del módulo, o el resultado del Paso 2-B si el repo no respondió o no se pudo determinar el `base_path` |
| Código fuente del módulo | LEÍDO / OMITIDO / REPO_INACCESIBLE / ESTRUCTURA_NO_DETECTADA / COMPONENTE_NO_CONFIRMADO | archivos y funciones concretas abiertas, o el resultado del Paso 2-B si el repo no respondió o no se pudo determinar el `base_path`, o la cadena de rastreo del punto 3-bis y en qué eslabón no se pudo confirmar el siguiente |
| `Detalles Adicionales:` de imágenes (Paso 3-A) | LEÍDO / SIN IMÁGENES | identificador(es) extraído(s) usado(s) como filtro, o motivo de no viable |
| BD del ERP (Paso 3-B) | LEÍDO / NO DISPONIBLE | resultado del SELECT, o el motivo — incluir si se detectó algún `null` anómalo en campo relacional (4-B) |
| Auditoría de fallo de proceso / `ad_pinstance` (Paso 3-B, 3-A) | AUDITADO / NO APLICA / OMITIDO / NO DISPONIBLE | si ancla clase A: process_value, result, errormsg y created de los intentos fallidos (o el motivo de no poder auditar). `NO APLICA` solo si el ancla no es clase A. `OMITIDO` con ancla clase A **bloquea** score ≥ 90 y cierre "comportamiento esperado" |
| Ancla del síntoma (motor Paso 1.5) | A / B / C / D | clase elegida + fragmento literal del error o síntoma usado como ancla |
| Contexto del cliente (Paso 3) | LEÍDO / OMITIDO / SIN CONFIG_DIR CONFIGURADO | archivo y contenido relevante, o que `config_dir` es `null` en `clientes.json` |
| Integraciones registradas del cliente (Paso 3-C) | LEÍDO / SIN REGISTRO | nombre de la integración que aplica al módulo/ventana afectada, o motivo de que no aplica ninguna |
| Comparación contra pares/registros similares (Paso 5-B, punto 1) | COMPARADO / SIN PARES | qué registros/configuraciones comparables se revisaron y qué diferencias o coincidencias se encontraron, o el motivo por el que no existe un conjunto comparable |
| Alcance real del patrón (Paso 5-B, punto 5) | MEDIDO / NO APLICA | número obtenido por la consulta de dimensionamiento y la consulta usada, o el motivo por el que no aplica (causa raíz sin flujo/módulo compartido con otros registros) |

**`OMITIDO` vs `REPO_INACCESIBLE` vs `ESTRUCTURA_NO_DETECTADA` vs `COMPONENTE_NO_CONFIRMADO`**: no son intercambiables. `OMITIDO` es para un archivo puntual que legítimamente no existe en un repo válido y accesible. `REPO_INACCESIBLE` (Paso 2-B, punto 1) es para cuando el repo de código entero no respondió — problema de configuración en `clientes.json` (owner/repo o permisos). `ESTRUCTURA_NO_DETECTADA` (Paso 2-B, punto 2) es para cuando el repo sí es accesible pero la auto-detección de `base_path` dio cero o múltiples candidatas — no se pudo determinar dónde arranca el código, y hace falta cargar `base_path` a mano en `clientes.json`. `COMPONENTE_NO_CONFIRMADO` (punto 3-bis) es distinto de los tres anteriores: el repo es accesible y el archivo que se leyó existe, pero no se confirmó que sea el componente que realmente genera el proceso/documento del ticket — es una falla de identificación, no de acceso. Los cuatro apuntan a causas y soluciones distintas — no colapsarlos en uno solo.

No sirve como dato probatorio: una cita de la memoria, una conclusión de una corrida anterior, ni una descripción genérica del archivo. Sirve un número, un nombre de archivo o un fragmento que solo se puede conocer habiéndolo abierto ahora.

#### 4. Higiene de la memoria

- Redactar toda nota sobre una fuente como **expectativa con procedencia**, nunca como veredicto ni prohibición. Mal: *"graphify no sirve"*. Bien: *"verificado el 2026-08-12: `graph.json` es un puntero LFS de 224 MB y el índice no incluye `.xml`, así que para causas en PL/SQL no aporta - usar `manifest.json` para listar el Java del módulo, cuesta segundos"*.
- Toda nota lleva **fecha de verificación y el comando o consulta** que la produjo. Una nota sin procedencia se trata como no verificada.
- Escribir en la memoria **qué esperar y a qué costo**, para acelerar el paso. Nunca *si hay que darlo* — eso lo decide la skill.
- Al corregir una nota equivocada, dejar constancia de qué decía antes. Los errores silenciosamente sobreescritos se repiten.

#### 5. Excepciones

Una omisión es legítima solo si es **explícita, justificada y auditable**: estado `OMITIDO` en la tabla, motivo en la sección 9, y reflejo en `respuesta_modelo_raw` del log del Paso 7. Lo que no es aceptable es la omisión silenciosa ni la que se apoya en la memoria como coartada. Si la misma fuente aparece `OMITIDO` en corridas sucesivas, eso es señal de que el procedimiento de lectura es demasiado caro y hay que arreglarlo en la skill, no normalizar el salto.

---

### Paso 5-B — Profundización de causa raíz (RCA obligatorio antes de cerrar el diagnóstico)

Existe para impedir un fallo concreto ya detectado por fuera del flujo automático: en el ticket 9741 (combos `BAJA-COM-AD`, San Felipe) el motor de 9 pasos llegó a una causa raíz correcta y bien evidenciada (`qtyreserved` residual por cierre de pedidos POS/autoventa sin liberar la reserva), pero la cerró como un caso puntual del producto reportado. Un análisis manual posterior, sobre un pedido distinto (`SF02-PVT-10101428`) con el mismo síntoma, profundizó un nivel más — identificó el mecanismo exacto (el módulo custom Sidesoft Dispatch Mobile completa el albarán vía funciones PL/pgSQL propias, sin pasar por el flujo estándar que sincroniza `qtyreserved`/`m_inoutline_id`) y, al correr una consulta de alcance, encontró **62.299 líneas afectadas en todo el cliente**, no un caso aislado. La causa raíz ya estaba bien identificada por el motor; lo que faltó fue el siguiente nivel de profundidad y la verificación de alcance. Este paso formaliza ese nivel adicional como obligatorio, no opcional, para todo ticket que llegue al Paso 5.

Este paso **no reemplaza** el motor de 9 pasos ni cambia su estructura de salida — es una disciplina de investigación que se aplica *durante* la ejecución del motor, **antes de publicar nada**, y cuyo resultado alimenta directamente las secciones 3 (Diagnóstico técnico), 4 (Causa raíz), 5 (Plan de solución), 8 (Prevención) y 9 (Datos faltantes / Evidencia) del documento final, y por lo tanto también la única §7 que se publicará. Cualquier hallazgo de este paso que profundice o corrija la causa raíz encontrada en una primera pasada se incorpora al documento **antes** del Paso 6 — nunca se publica como un comentario adicional aparte (ej. un `[TRIAGE-CORRECCION]` posterior al `[TRIAGE-ANALISIS-9PASOS]` y a la `[TRIAGE-RESPUESTA-SUGERIDA]` ya publicados). Un ticket termina, por corrida, con exactamente un análisis de 9 pasos y exactamente una respuesta sugerida — nunca una "versión corregida" publicada después de la primera.

#### 1. Principio — no cerrar en la primera causa plausible
Encontrar una explicación que encaja con el síntoma no es lo mismo que haber encontrado la causa raíz. Antes de dar por cerrado el diagnóstico, preguntarse explícitamente: *¿qué otra cosa podría producir exactamente el mismo síntoma?* Si existe al menos una hipótesis alternativa razonable con los datos ya disponibles (código, BD, `graphify-out/`, `integraciones.json`), evaluarla antes de fijar la causa raíz — no después, no como nota al margen.

**Este principio aplica también cuando la conclusión es "no hay error" o "es el comportamiento esperado/normal".** Existe para impedir un fallo concreto ya ocurrido: ante un bloqueo al registrar un pedido, el motor confirmó que el registro y su estado eran *internamente consistentes* (el mismo tipo de documento se comporta igual en otros pedidos del día) y cerró el caso como "malinterpretación del estado, no un error" — sin comparar esa configuración contra sus **pares** (los demás tipos de documento de la misma familia). Un análisis posterior, comparando ese tipo de documento contra todos sus hermanos, encontró que era el único con un flag de configuración distinto al resto — la causa real. Consistencia interna (esto siempre pasa así para este registro/tipo) no es lo mismo que corrección (este registro/tipo está configurado igual que sus pares) — la primera nunca es evidencia suficiente para la segunda.

**Prioridad sobre este principio — ancla clase A (`openbravo-functional-ticket-analysis` Paso 1.5):** si el ticket muestra un error literal de proceso/BD al Completar/Registrar/Procesar, **no** se puede cerrar como "comportamiento esperado" ni como guía de flujo posterior (Proformado → albarán → factura) solo con la comparación de doctype/hermanos maestros. Primero Paso 3-B punto 3-A (`ad_pinstance` + hermanos transaccionales exitosos + desambiguación de homónimos). La comparación de maestros sigue siendo obligatoria **después**, como verificación adicional, nunca como sustituto de la auditoría del proceso fallido.

**Comparación obligatoria contra pares/registros similares — no condicionada a que ya se haya detectado un problema.** El procedimiento completo (cómo distinguir comparación transaccional vs. comparación contra registros maestros hermanos, enumeración exhaustiva de columnas `EM_*` por código + esquema vivo, y la regla de "no detenerse en el primer campo coherente") **vive en `openbravo-functional-ticket-analysis`, Paso 2 punto 7 y punto 7-bis** — no se repite aquí para evitar que ambas copias diverjan con el tiempo. Este motor siempre corre con `pg_query`/MCP-DB disponible dentro de `triage-glpi-auto`, así que esa comparación nunca es opcional en este flujo automático.

Esto se hace siempre, cubriendo tantos escenarios comparables como sea razonable con las fuentes disponibles en esta corrida, independientemente de si la comparación termina confirmando una anomalía o confirmando que todo está en línea — es un paso de verificación, no una reacción a una sospecha ya formada. El resultado (qué pares se revisaron — transaccionales o de configuración — y qué diferencias o coincidencias se encontraron) es evidencia obligatoria de la sección 9 (ver fila correspondiente en la tabla del punto 3) y su ausencia o profundidad debe reflejarse en la justificación del score de acertividad (Paso 6.1) — un diagnóstico que comparó registros transaccionales entre sí, sin comparar la configuración contra sus hermanos, no puede justificar el mismo nivel de confianza que uno que sí llegó al nivel de configuración.

#### 2. Trazabilidad de flujo obligatoria
Reconstruir la cadena completa hasta el punto donde se origina el problema, no solo hasta donde se manifiesta:

```
Usuario → Interfaz/origen del dato → Proceso funcional → Backend (función/trigger/servicio) → Base de datos → Registro → Resultado
```

Identificar explícitamente **en qué eslabón se rompe la cadena**, y distinguir tres cosas que suelen confundirse en un mismo párrafo:
- **Error visible**: lo que el usuario ve (ej. el mensaje de guardado fallido).
- **Error técnico**: la condición inmediata que lo dispara (ej. el trigger que lee una reserva residual).
- **Causa raíz**: por qué esa condición existe (ej. un flujo de despacho que nunca liberó la reserva).

Cuando el flujo pasa por un módulo custom (prefijo propio, ej. `SSDPM`) en vez del flujo estándar de Openbravo, señalarlo explícitamente — es habitualmente el punto donde una sincronización esperada por el core deja de cumplirse.

Cuando el eslabón "Backend (función/trigger/servicio)" de esta cadena involucra código o una plantilla de impresión, este eslabón se llena únicamente con el resultado del rastreo obligatorio del punto 3-bis (Paso 5) — nunca con un archivo similar no confirmado como responsable.

#### 3. Tabla de hipótesis y descarte
Cuando exista más de una causa plausible para el mismo síntoma, documentar el descarte con esta estructura (va en la sección 9 del documento, como respaldo de la sección 4):

| Hipótesis | Campo evaluado (nombre exacto de columna, si aplica) | Evidencia | Cómo se validó | Resultado | Estado |
|---|---|---|---|---|---|
| {hipótesis 1} | {`nombre_columna` o "N/A" si no es una hipótesis de configuración} | {fuente/dato} | {consulta o revisión aplicada} | {resultado obtenido} | Confirmada / Descartada |
| {hipótesis 2} | {`nombre_columna`} | {fuente/dato} | {consulta o revisión aplicada} | {resultado obtenido} | Confirmada / Descartada |

**Regla anti-colapso y validación de ticket relacionado:** mismas reglas de `openbravo-functional-ticket-analysis` — Paso 4 ("Regla de esta tabla", una fila por columna `EM_*` candidata, la hipótesis general solo se descarta cuando todas fueron probadas) y Paso 5A punto 7 (un ticket/precedente histórico es una hipótesis a falsear con un dato concreto de este ticket, nunca una conclusión por defecto). No se repiten aquí — ver esa skill para el criterio exacto de cuándo marcar Confirmada/Descartada.

#### 4. Cuatro niveles de causa raíz (obligatorios en la sección 4 del documento)
Esta estructura ya está incorporada de forma nativa en la plantilla de la sección 4 de `openbravo-functional-ticket-analysis` (formato Incidencia) — no es una capa aparte que el orquestador agregue por fuera del motor. Se documenta aquí solo para que quede explícito que la sección 4 del documento publicado nunca queda completa con un solo nivel de explicación. Debe distinguir:
1. **Síntoma** — qué reporta o percibe el usuario.
2. **Causa inmediata** — qué dispara el error o comportamiento (trigger, validación, condición puntual).
3. **Causa raíz** — por qué existe esa condición (qué proceso/flujo la generó).
4. **Causa estructural** — por qué el sistema permitió que esa condición llegara a producirse sin corregirse sola (ej. una sincronización que el flujo estándar hace pero el módulo custom no replica).

#### 5. Verificación de alcance real — obligatoria cuando la causa raíz es un patrón de datos, de proceso, o un valor de configuración replicado
Si la causa raíz identificada es una **condición de datos o un gap de un flujo/módulo** (no un error de configuración puntual de un solo registro), **no dar por buena la conclusión de "caso aislado" sin antes medirlo**:

1. Formular una consulta de diagnóstico (vía `pg_query`, Paso 3-B) que cuente o liste cuántos otros registros del cliente comparten exactamente la misma condición estructural que produjo el síntoma (mismo patrón de campos NULL/residuales, mismo módulo de origen, mismo tipo de documento).
2. Correr esa consulta contra la BD del cliente y registrar el número real obtenido — este resultado es evidencia obligatoria de la sección 9, con el mismo criterio del Paso 5-EVIDENCIA (un número obtenido en esta corrida, no una estimación).
3. Si el número es significativamente mayor a 1, la sección 4 (Causa raíz) y la sección 8 (Prevención) del documento deben reflejar que se trata de un **patrón sistémico**, no de un caso puntual, y la sección 5 (Plan de solución) debe seguir el punto 7 de abajo (fases de corrección).
4. Si no hay indicios de que la condición pueda repetirse (ej. error de configuración específico de un solo maestro, sin relación con un flujo o módulo compartido), se puede omitir este chequeo — dejar registrado explícitamente el motivo ("no aplica: causa raíz específica de este registro, sin flujo/módulo compartido con otros documentos") en vez de omitirlo en silencio.

**Caso particular — la solicitud implica modificar un valor de configuración que sigue un patrón replicado en varios campos o registros similares** (ej. una fórmula que agrupa conceptos y debe incluir uno nuevo, un parámetro que se repite por sucursal/organización, una regla de validación configurada en varias ventanas): el mismo principio de "no cerrar en el primer caso" aplica, pero el alcance se mide por **inspección de los campos/registros hermanos**, no por conteo de filas de un patrón de datos roto:

1. Identificar, por BD o por código, todos los campos/registros que agrupan el mismo tipo de elemento que la solicitud pide modificar (ej. todas las fórmulas de Nómina que suman bonos del mismo tipo que el concepto en cuestión, no solo la primera que se detecte).
2. Listar en la sección 5 (Plan de solución) **cada** campo/registro que debe actualizarse para que el cambio quede consistente — no solo el que motivó el ticket.
3. Si se detecta que algunos campos hermanos ya incluyen el patrón correcto y otros no, señalarlo explícitamente — es evidencia de que el gap es sistémico (aplica también el punto 3 de arriba) y no un olvido puntual.

#### 6. Workaround vs. solución definitiva — nunca presentar uno como el otro
Esta distinción ya tiene su propio apartado (5-B) en la plantilla de sección 5 de `openbravo-functional-ticket-analysis` (formato Incidencia) — se resume aquí el criterio, no un requisito adicional fuera de esa plantilla. Cuando exista una forma de mitigar el síntoma mientras se corrige la causa raíz de fondo, la sección 5 (Plan de solución) debe declarar ambas por separado y explícitamente etiquetadas:
- **Solución temporal / workaround**: qué se puede hacer ya para reducir o eliminar el impacto inmediato (ej. desactivar la venta sin tocar `isactive`).
- **Solución definitiva**: qué debe corregirse de fondo — a nivel de datos (Paso 6-B) y/o a nivel de desarrollo (reportar el gap en el módulo/función responsable).
- **Riesgos del workaround**: qué queda sin resolver o qué puede seguir generando el mismo síntoma mientras no se aplique la solución definitiva.

#### 7. Análisis de impacto y fases de ejecución — obligatorio antes de sugerir cualquier corrección de datos
Antes de que el Paso 6-B redacte el script correctivo sugerido, evaluar:
- Qué otros procesos podrían verse afectados por la corrección (POS, ventas, reportes, contabilidad, integraciones registradas del cliente — cruzar con el Paso 3-C).
- Si el volumen medido en el punto 5 es alto, **la corrección no se sugiere como un único script masivo por defecto**. Separar en fases, siguiendo el mismo patrón usado en el análisis de San Felipe:
  - **Fase 1 — puntual**: corrección acotada al/los registro(s) del ticket actual, con transacción y respaldo, lista para ejecutar por un técnico.
  - **Fase 2 — masiva**: corrección del resto de registros con el mismo patrón, explícitamente marcada como *no lista para correr sin revisión* cuando liberar el volumen completo de una vez pueda producir un efecto secundario súbito (ej. disponibilidad de stock, cambios en reportes) — requiere ejecución paginada/por lotes y validación intermedia.
- Este análisis de impacto y fases va en la sección 5 (Plan de solución) del documento; el script en sí sigue las reglas del Paso 6-B (solo texto, nunca ejecutado automáticamente).

#### 8. Validación de la solución
La sección 5 (Plan de solución) debe indicar además cómo se comprobaría que la corrección funcionó: qué volver a consultar (ej. repetir la query de alcance del punto 5 y confirmar que el conteo baja a 0 para el/los registro(s) corregidos), y qué caso borde adicional conviene revisar (otro documento con el mismo patrón, otra organización/bodega, otro estado del documento).

---

Invocar el flujo completo de 9 pasos de esa skill (vive en el repo orquestador, es común a todos los clientes), usando como entrada:
- La descripción original del ticket,
- Si se venía del camino 4.2, también la respuesta de aclaración del cliente,
- El contexto específico del cliente leído en el Paso 3,
- El resultado de la verificación en BD del Paso 3-B, si aplicó — **incluyendo** la auditoría `ad_pinstance` (3-A) cuando el ancla fue clase A.

**Campos nativos del motor — 2 campos distintos, no se fusionan:**
- **Tipo de caso** (clasificación nativa del motor, Paso 3 de `openbravo-functional-ticket-analysis`): Operativo / Configuración / Integración / Bug / Infraestructura. Este es el campo principal que determina el manejo general del ticket.
- **Causa raíz** (vocabulario nativo de la sección 4 del motor, subordinado a sus cuatro niveles — síntoma / causa inmediata / causa raíz / causa estructural): configuración faltante, estado del documento, restricción de negocio del sistema, dato del cliente erróneo, o bug real (último recurso). Es un campo aparte y más granular que el Tipo de caso — no lo reemplaza ni se combina en el mismo valor, y se declara una sola vez en el nivel donde realmente corresponde, nunca repetido en más de uno.
- Citar por nombre de archivo cualquier caso de uso de `casos_de_uso_openbravo_erp.md` que aplique (ver Paso 5B-bis del motor).

**Reglas específicas de la sección §7 (respuesta al usuario final) — alineadas con `openbravo-functional-ticket-analysis.mdc`:**
- §7 **nunca** debe incluir: SQL, sentencias UPDATE, scripts de corrección, referencias a tablas, columnas, código fuente, ni IDs técnicos. Eso va exclusivamente en las secciones 5-6 (uso del consultor/técnico) o en el comentario privado 6.3 de este flujo.
- §7 debe incluir, cuando aplique: (1) diagnóstico en términos de negocio — qué documento/flujo se usó mal; (2) por qué está mal — naturaleza del movimiento, tipo de documento, impacto en conciliación/contabilidad; (3) qué debieron hacer — el flujo correcto en Openbravo; (4) solución operativa numerada, típicamente en el patrón revertir → recrear correctamente → conciliar/validar.
- Si el Paso 5-B distinguió workaround y solución definitiva, §7 refleja ambas para el usuario final en lenguaje operativo (qué hacer ya / qué queda pendiente de que un técnico corrija de fondo) — sin perder la regla de no incluir SQL, tablas ni IDs técnicos.
- Si el caso es operativo (no bug de sistema): la solución principal va completa en §7. El SQL o escalamiento a desarrollo, si existe, va solo en las secciones 5-6 para el consultor — nunca en §7 ni en el comentario de solución 6.3.
- Si además hay un bug de sistema real: §7 sigue siendo el flujo correcto para el usuario; el detalle técnico del bug y su escalamiento van en 5-6 / comentario privado.
- **Cuando la solución operativa (punto 4) implique ejecutar una acción en el sistema**, §7 debe indicar el **nombre exacto de la ventana** donde se hace, tal como aparece en el ERP (ej. "Gestión de Almacén → Transacciones → Ajuste de Inventario Físico"), junto con los datos concretos a ingresar (producto, cantidad, tipo de movimiento, almacén). Ese nombre se obtiene del código/documentación del cliente (Paso 3, `graphify-out/`, conocimiento común del módulo) — nunca se inventa ni se generaliza a "consulte con su consultor". Si no se puede confirmar la ventana exacta con las fuentes disponibles en esta corrida, declararlo explícitamente en la sección 9 en vez de omitir el paso.
- **Cuando exista un camino operativo estándar en el sistema** para corregir el dato afectado (ej. un ajuste de inventario Alta/Baja desde la ventana estándar) y no solo mediante script SQL, §7 debe priorizar y detallar ese camino operativo como la vía principal — el script sugerido del Paso 6-B queda como respaldo técnico en las secciones 5-6, no como la única opción ofrecida.
- **Cuando la causa raíz sea una regla de negocio controlada por un campo de configuración** (una regla de facturación, un flag de un tipo de documento, un parámetro de módulo) — **incluso cuando el veredicto sea "comportamiento esperado, no un error"** — no basta con nombrar la regla ("la facturación es Después de entregado"). Hay que resolver y citar **dónde se configura** esa regla (ventana/pestaña/campo exactos, o tabla/columna si no tiene ventana propia) en la sección 4/5, y ofrecerlo en §7 como paso opcional ("si prefieren que esto funcione distinto, el ajuste se hace en...") para que el cliente sepa qué tocar si decide cambiar la política, sin tener que abrir otro ticket para preguntarlo.
- **Antes de recomendar en la sección 5/6 el cambio de un campo/parámetro como solución de fondo o como ajuste opcional**: confirmar que el nombre exacto de columna propuesto es **el mismo** que quedó "Confirmada" en la tabla de hipótesis del Paso 5-B punto 3 — no un campo de nombre o dominio parecido. Distintos módulos de personalización pueden definir su propio campo con semántica similar sobre la misma tabla (ej. varias columnas `EM_*` de "regla de facturación" de prefijos distintos, cada una gobernando un comportamiento independiente salvo que el código confirme lo contrario). Si el campo que resolvería el ajuste de negocio que pide el usuario no es el mismo que la causa raíz confirmada, decir ambos por separado en §7 — nunca ofrecer el campo equivocado como si fuera "el" ajuste.
- **Toda afirmación en §7 de tipo "alineado con [otro tipo de documento/registro]" o "es el comportamiento esperado"** debe corresponder a una hipótesis de tipo "registro maestro anómalo" marcada **Descartada** en la tabla de hipótesis (Paso 5-B, punto 3) con **todas** sus columnas `EM_*` candidatas probadas — nunca a la comparación de una sola columna cuando la enumeración (punto 1, incluyendo 1-ter) identificó más candidatas sin probar todavía.
- **Todo campo de configuración evaluado en el Paso 5-B punto 3 que quedó Descartado como causa pero gobierna un comportamiento automático del mismo flujo del ticket** (ej. Completar Albarán / Completar Factura en el tipo de documento del caso) se marca **Informativa** (estado definido en `openbravo-functional-ticket-analysis`, Paso 4) y **debe aparecer en §7** dentro de "Otras opciones a considerar", como un punto más que el usuario debe validar: qué hace en lenguaje llano, cómo está hoy, dónde se cambia, y **explícitamente que no corrige este caso puntual** (nunca presentarlo como si resolviera el síntoma). Descartar un campo como causa no autoriza a omitirlo de la respuesta. Las filas Complementarias (resolverían el caso por otra vía) siguen siendo obligatorias en §7 y se distinguen de las Informativas en el texto.
- **Cuando la solicitud pide cambiar un valor de configuración que vive en un campo de interfaz** (ej. la fórmula de un concepto, un parámetro, un texto de validación) y no es una corrección de datos rotos: no basta con describir la acción en términos genéricos ("agregar X a la fórmula", "incluir el concepto junto a los demás"). El análisis debe (1) consultar por BD el valor/fórmula actual del campo (Paso 3-B), (2) construir el valor nuevo exacto siguiendo el mismo patrón que ya usan los campos/registros hermanos identificados en el punto 5 de arriba, (3) dejar ese script de actualización listo en el Paso 6-B (mismo formato: texto sugerido, nunca ejecutado automáticamente), y (4) en §7 indicar, en lenguaje llano y sin SQL ni nombres de tabla, el campo/ventana exacto y el valor final que debe quedar ahí — de modo que quien aplique el cambio (por script o manualmente desde la interfaz) sepa con certeza qué poner, sin tener que deducirlo.
- El bloque de acciones a ejecutar dentro de §7 se titula siempre **"Solución a aplicar o verificar"** (nunca "Qué hacer ya" / "Qué hacer ahora") — mantener este título de forma consistente en todos los tickets.

Producto esperado: el documento completo de 9 secciones (Clasificación, Entendimiento, Diagnóstico técnico, Causa raíz, Plan de solución, Escalamiento, **Respuesta sugerida al usuario final — §7**, Prevención, Datos faltantes), siguiendo el subtipo que corresponda (Incidencia o Viabilidad) tal como esa skill lo define.

---

## Paso 6 — Publicar los comentarios, TODOS PRIVADOS (sin confirmación — ejecución automática)

Ejecutar en este orden, vía MCP-DB (`glpi`). `users_id = 148` = usuario `bot.glpi`. **Todos los comentarios de este flujo se publican con `is_private = 1` — ninguno es visible para el solicitante/cliente en GLPI**, salvo el comentario CX del Caso Capacitación (Paso 4.0), que se publica con `is_private = 0` por diseño.

**Cambio: ya no se publica comentario de "primer contacto".** El flujo pasa directo del análisis al comentario de SLA+Score. Quedan 3 comentarios en total (antes eran 5).

### 6.1 — Comentario privado: SLA/criticidad + score de acertividad (fusionado)
Un solo `INSERT` que combina ambos contenidos — nivel SLA, criticidad, área funcional, tiempo estimado, **y** el score de acertividad de la §7 con su justificación, todo en el mismo comentario.

Evaluar el score exclusivamente sobre la sección §7 del análisis del Paso 5. El eje del score **no es qué tan bien redactada o evidenciada está la respuesta** — es **qué tipo de intervención se necesita para que el caso puntual reportado quede efectivamente cerrado**. La pregunta que decide el rango: *¿quién cierra el caso, y con qué medio?*

| Rango | Criterio |
|---|---|
| 90–100 | **Autoservicio**: el usuario o consultor resuelve el caso completo con configuración o pasos ejecutables directamente en el sistema — no requiere que un técnico corrija datos, ni desarrollo pendiente, ni siquiera para prevenir que se repita. |
| 80–89 | **Intervención manual/funcional o técnica puntual que SÍ cierra el caso actual**: un consultor o técnico corrige datos, ancla/anula registros, o determina el valor correcto mediante un método alterno (ej. cálculo manual, otra fuente de verdad) — el caso puntual queda resuelto hoy, aunque quede pendiente un desarrollo para que no se repita en el futuro. Dentro de este rango, un caso ya resuelto sin cabos sueltos va hacia 85-89; uno resuelto pero con más de un punto todavía por confirmar o coordinar va hacia 80-84. |
| 71–80 | **Demanda no cubierta por el sistema, ni con esfuerzo manual**: lo que el usuario pidió no se puede cumplir hoy de ninguna forma — cualquier workaround disponible solo evita o mitiga el síntoma, no satisface lo solicitado. Depende enteramente de que el proveedor entregue el desarrollo. |
| 40–70 | Diagnóstico plausible pero con confianza Media/Baja declarada, o basado solo en comportamiento core sin confirmar personalización del proyecto — evidencia insuficiente para clasificar con certeza en cualquiera de los rangos anteriores. |
| 0–39 | Datos insuficientes pese a pasar el filtro de contexto, múltiples hipótesis sin evidencia, o Datos faltantes con elementos críticos pendientes. |

**Excepción — casos de capacitación no formalizados**: si §7 concluye que la solución real es que el usuario reciba capacitación o coordinación (y el ticket no disparó el Caso Capacitación del Paso 4.0 por no contener las palabras clave), aplicar como máximo **49** — depende de gestión coordinada con el cliente, no de una corrección de sistema.

**Excepción — ancla clase A sin auditoría de proceso (o con auditoría que contradice el cierre):** si el ticket trae error SQL/constraint/`ERROR=` / fallo al Completar-Registrar-Procesar (motor Paso 1.5 clase A) y en la tabla de evidencia la fila `ad_pinstance` está `OMITIDO` o `NO DISPONIBLE`, **o** está `AUDITADO` con `result=0` alineado al síntoma pero §7 cierra solo como "comportamiento esperado" / flujo posterior (Proformado, generar albarán, etc.) sin explicar ese fallo: aplicar como máximo **70**. Queda **prohibido** score ≥ 90 (autoservicio / Resuelto automático) en esos casos. Si la auditoría sí se hizo y la causa raíz explica el `errormsg` con evidencia, el score sigue la tabla normal.

**Nota de calibración**: la evidencia (Paso 5-EVIDENCIA) sigue siendo obligatoria y sigue registrándose en la sección 9, pero ya no determina el rango por sí sola — determina si la clasificación del tipo de intervención (autoservicio / manual-técnica-puntual / desarrollo pendiente) es confiable. Un diagnóstico con evidencia débil no debe declararse "autoservicio" (90-100) ni "cierra el caso hoy" (80-89) solo porque suena plausible: si no hay evidencia firme de en cuál de los tres tipos cae, el score baja al rango 40-70 en vez de forzarlo hacia arriba.

```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_sla_y_score_html}', 1, 0, NOW(), NOW(), 1);
```

`{comentario_sla_y_score_html}` incluye, en un solo bloque: Nivel SLA · Criticidad · Área funcional · Tiempo estimado de revisión inicial · Score de acertividad (0-100) · Justificación del rango.

### 6.2 — Comentario privado: detalle completo de los 9 pasos
Contenido: el documento completo generado en el Paso 5, en HTML legible. Audiencia: consultor/soporte técnico — puede incluir SQL, IDs, nombres de módulo. Si el `adjuntos` recibido en el payload no es `sin adjuntos`, agregar al final una nota: "Ticket con adjuntos no analizados automáticamente: {lista de nombres} — revisar manualmente en GLPI."

**Control de calidad antes de publicar (obligatorio):** verificar que el documento tenga las **9 secciones completas** (1 Clasificación, 2 Entendimiento, 3 Diagnóstico técnico, 4 Causa raíz, 5 Plan de solución, 6 Escalamiento/script, **7 Respuesta sugerida al usuario final**, 8 Prevención, 9 Datos faltantes/Evidencia), con contenido coherente y sin puntos a medio redactar o inconsistentes entre sí. **La §7 nunca se omite del análisis de 9 pasos**, aunque el score sea bajo y no se publique después `[TRIAGE-RESPUESTA-SUGERIDA]` ni solución — ver regla dura abajo. Si no pasa este control, **regenerar el análisis una vez** antes de publicar nada. Nunca publicar una primera versión parcial/confusa y luego, en la misma corrida, publicar una segunda versión corregida como si fuera un comentario aparte — se publica una sola vez, cuando el documento ya pasó este control.

**Obligatorio: dividir este comentario en dos (o tres) followups.** El documento completo de 9 secciones supera el límite de escritura del MCP (ver *Límite de tamaño* abajo) y se pierde entero si se inserta como un solo bloque. Publicar:
- `[TRIAGE-ANALISIS-9PASOS] Parte 1 de 2` — secciones 1 a 3 (Clasificación, Entendimiento, Diagnóstico técnico).
- `[TRIAGE-ANALISIS-9PASOS] Parte 2 de 2` — secciones **4 a 9** (Causa raíz, Plan, Escalamiento/script, **§7 Respuesta al usuario**, Prevención, Evidencia), más la nota de adjuntos.

Si la Parte 2 supera ~3,2 KB con las secciones 4–9 incluidas, dividir en tres followups (nunca sacrificando la §7):
- Parte 1 de 3 — secciones 1 a 3
- Parte 2 de 3 — secciones 4 a 6 (incluye el script correctivo si aplica)
- Parte 3 de 3 — secciones **7**, 8 y 9

**Regla dura — §7 vs triage de respuesta/solución (no confundir):**
- La **§7 vive siempre dentro de `[TRIAGE-ANALISIS-9PASOS]`** (Parte 2 o Parte 3). Score bajo **no** autoriza saltarse el punto 7 del análisis.
- Lo único que se salta con score bajo es **republicar ese mismo contenido** como comentario aparte `[TRIAGE-RESPUESTA-SUGERIDA]` o como solución en `glpi_itilsolutions` (Paso 6.3). Es decir: el análisis siempre trae las 9 secciones; el triage de respuesta/solución es un canal adicional condicionado al score.

**Regla dura — corrección de datos o acción por interfaz (siempre en el análisis):**
- Si el caso requiere un **cambio a nivel de base de datos** (dato roto, PSD, flag, fórmula, reasignación, etc.): el **script SQL correctivo sugerido** (solo texto, nunca ejecutado) debe ir en las secciones **5 y/o 6** del `[TRIAGE-ANALISIS-9PASOS]`, con el encabezado del Paso 6-B. No basta con decir "hay que corregir el dato" sin adjuntar el script plantilla (aunque falten IDs por BD cerrada: dejar el `SELECT` de localización + el `UPDATE`/`INSERT` con placeholders y la condición de ejecución).
- Si el usuario **puede resolverlo por la interfaz** del ERP: la **§7** (y, cuando el score lo permita, el triage de respuesta/solución 6.3) debe indicar la **ventana/ruta exacta** y los pasos operativos. Si además existe un script de respaldo técnico, el script queda en §5/§6 y la vía UI es la principal en §7.

En el log del Paso 7, `followup_analisis_id` lleva el id de la Parte 1, y todos los ids de partes se detallan en `respuesta_modelo_raw`.
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_analisis_9_pasos_html}', 1, 0, NOW(), NOW(), 1);
```

### 6.3 — Comentario condicional según score de acertividad

Evaluar el score de acertividad (calculado en 6.1, sobre la §7 del análisis del Paso 5) para decidir **si se publica un canal adicional** de respuesta/solución. La §7 **ya debe estar** dentro del `[TRIAGE-ANALISIS-9PASOS]` del Paso 6.2 — este paso solo decide si se **copia** ese contenido (o un extracto operativo) a solución/respuesta sugerida.

- **Score >= 90**: el contenido `[TRIAGE-RESPUESTA-SUGERIDA]` se aplica como **solución del ticket** (tabla `glpi_itilsolutions`), no como followup. El cambio de `status` a Resuelto y la asignación a kvelasco se aplican en el Paso 6.4, Caso A.
```sql
INSERT INTO glpi_itilsolutions (itemtype, items_id, solutiontypes_id, content, date_creation, date_mod, users_id, status)
VALUES ('Ticket', {ticket_id}, 0, '{comentario_publico_respuesta_formateada}', NOW(), NOW(), 148, 1);
```
**Nota:** verificar contra el esquema real de GLPI (`pg_describe_table`/equivalente) los nombres de columna de `glpi_itilsolutions` antes de usar esta skill en producción — igual que `{ID_KVELASCO}`, no confirmado en esta corrección.

- **Score > 80 y < 90**: publicar el mismo contenido como followup privado (`is_private = 1`) con marcador `[TRIAGE-RESPUESTA-SUGERIDA]`. Además, el cambio de `status` a Planificado y la asignación a kvelasco se aplican en el Paso 6.4, Caso A-1.
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_publico_respuesta_formateada}', 1, 0, NOW(), NOW(), 1);
```

- **Score > 70 y <= 80**: publicar el mismo contenido como followup privado (`is_private = 1`) con marcador `[TRIAGE-RESPUESTA-SUGERIDA]`. El `status` (Planificado) y la asignación a kvelasco se aplican igual en el Paso 6.4, Caso A-1 — un análisis ya publicado nunca deja el ticket en Nuevo.
```sql
INSERT INTO glpi_itilfollowups (itemtype, items_id, date, users_id, users_id_editor, content, is_private, requesttypes_id, date_creation, date_mod, timeline_position)
VALUES ('Ticket', {ticket_id}, NOW(), 148, 148, '{comentario_publico_respuesta_formateada}', 1, 0, NOW(), NOW(), 1);
```

- **Score <= 70**: **no** publicar `[TRIAGE-RESPUESTA-SUGERIDA]` ni solución en `glpi_itilsolutions`. **Sí** debe haberse publicado la §7 completa dentro de `[TRIAGE-ANALISIS-9PASOS]` (6.2). Esto no implica dejar el ticket sin gestionar: el `[TRIAGE-SLA-SCORE]` y el análisis de 9 pasos (con §7 incluida) ya se publicaron, así que el `status` (Planificado) y la asignación a kvelasco se aplican igual en el Paso 6.4, Caso A-1, para que un técnico tome el caso y el ticket no vuelva a la cola de Nuevos.

### 6.4 — Actualizar el estado del ticket (excepciones puntuales a "nunca modificar status")

Por regla general este flujo no toca `status`. Las excepciones son las siguientes, según cómo terminó el ticket en esta corrida (A, A-1 y B cubren todo ticket que llega hasta publicar análisis o preguntas):

**Caso A — Se aplicó el comentario como solución del ticket (6.3, score >= 90):** dejar el ticket en Resuelto (status = 5), asignado al técnico kvelasco.
```sql
UPDATE glpi_tickets
SET itilcategories_id = COALESCE({categoria_id_o_null}, itilcategories_id),
    impact = {impact_id}, priority = {priority_id}, status = 5, date_mod = NOW()
WHERE id = {ticket_id};
```
La asignación de técnico vive en `glpi_tickets_users` (`type = 2` = asignado), no en `glpi_tickets`. Antes de insertar, verificar con un `SELECT` si ya existe una fila `type = 2` para este `tickets_id` (para no duplicar en corridas repetidas de un mismo ticket):
```sql
-- si no existe fila type=2 para este ticket:
INSERT INTO glpi_tickets_users (tickets_id, users_id, type)
VALUES ({ticket_id}, {ID_KVELASCO}, 2);
-- si ya existe, actualizarla en vez de insertar:
UPDATE glpi_tickets_users SET users_id = {ID_KVELASCO} WHERE tickets_id = {ticket_id} AND type = 2;
```

**Caso A-1 — Análisis de 9 pasos publicado con score de acertividad menor a 90 (cualquier valor, incluido <= 70 sin respuesta sugerida publicada — `ok_baja_confianza` y `ok_alta_confianza` con score < 90):** dejar el ticket en En curso (planificado) (status = 3), asignado al técnico kvelasco.

Existe para impedir un fallo concreto ya ocurrido (ticket 9938): el análisis de 9 pasos se publicó completo pero, al no alcanzar el score para publicar respuesta sugerida ni solución, el ticket quedó en Nuevo y sin técnico. Como el cron de n8n busca `status = 1`, un ticket que queda en Nuevo se vuelve a tomar y el motor completo se re-ejecuta indefinidamente (el Paso 4.-1 solo cubre una ventana de 15 minutos). Un ticket con análisis ya publicado nunca debe quedar en Nuevo: pasa a Planificado y a un técnico, tenga o no respuesta sugerida.
```sql
UPDATE glpi_tickets
SET itilcategories_id = COALESCE({categoria_id_o_null}, itilcategories_id),
    impact = {impact_id}, priority = {priority_id}, status = 3, date_mod = NOW()
WHERE id = {ticket_id};
```
La asignación de técnico vive en `glpi_tickets_users` (`type = 2` = asignado), no en `glpi_tickets`. Antes de insertar, verificar con un `SELECT` si ya existe una fila `type = 2` para este `tickets_id` (para no duplicar en corridas repetidas de un mismo ticket):
```sql
-- si no existe fila type=2 para este ticket:
INSERT INTO glpi_tickets_users (tickets_id, users_id, type)
VALUES ({ticket_id}, {ID_KVELASCO}, 2);
-- si ya existe, actualizarla en vez de insertar:
UPDATE glpi_tickets_users SET users_id = {ID_KVELASCO} WHERE tickets_id = {ticket_id} AND type = 2;
```

**Caso B — El ticket quedó con triage de preguntas (`estado_procesamiento = 'preguntas_enviadas'`):** dejar el ticket en En espera (status = 4), asignado al técnico kvelasco.
```sql
UPDATE glpi_tickets SET status = 4, date_mod = NOW() WHERE id = {ticket_id};
```
La asignación de técnico vive en `glpi_tickets_users` (`type = 2` = asignado), no en `glpi_tickets`. Antes de insertar, verificar con un `SELECT` si ya existe una fila `type = 2` para este `tickets_id` (para no duplicar en corridas repetidas de un mismo ticket):
```sql
-- si no existe fila type=2 para este ticket:
INSERT INTO glpi_tickets_users (tickets_id, users_id, type)
VALUES ({ticket_id}, {ID_KVELASCO}, 2);
-- si ya existe, actualizarla en vez de insertar:
UPDATE glpi_tickets_users SET users_id = {ID_KVELASCO} WHERE tickets_id = {ticket_id} AND type = 2;
```

**Cualquier otro caso** (`proyecto_no_registrado` — que ya se movió a Planificado en el Paso 2-A —, `esperando_respuesta_cliente` — que ya quedó En espera por el Caso B de una corrida anterior —, `error`): no tocar `status` ni la asignación — sigue aplicando la regla original. `error` se deja sin cambio de `status` a propósito, para permitir el reintento (no se publicó análisis).
```sql
UPDATE glpi_tickets
SET itilcategories_id = COALESCE({categoria_id_o_null}, itilcategories_id),
    impact = {impact_id}, priority = {priority_id}, date_mod = NOW()
WHERE id = {ticket_id};
```

**Nota:** `{ID_KVELASCO}` debe reemplazarse por el ID numérico real del usuario kvelasco en GLPI (Configuración > Usuarios > abrir el usuario > ver `id=XXX` en la URL) antes de usar esta skill en producción.

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

**Caracteres a evitar en cualquier string enviado por el MCP**: el punto y coma, tanto literal como dentro de entidades HTML (`&mdash;`, `&gt;`). Usar guiones y palabras. Las etiquetas `<br>`, `<b>`, `<table>`, `<tr>`, `<td>` y `<th>` sí son seguras.

### 6-A-bis — Formato de tablas comparativas dentro de los comentarios (mejora de diseño, no cambia el análisis)

Esta sección solo mejora cómo se ve una comparación ya exigida por el análisis (Paso 5-B, puntos 1, 3 y 5) — no agrega ni quita ningún requisito de contenido.

**Problema detectado (2026-09-18, ticket 9934):** las tablas se publicaban como `<table><tr><th>...` sin ningún atributo de estilo. GLPI no aplica un CSS de tabla por defecto a los comentarios, así que el resultado se ve sin bordes, sin sombreado de encabezado y sin alineación clara — exactamente el problema reportado. La causa no era el contenido del análisis (la matriz ya traía los datos correctos), era la falta de estilo en el HTML.

**Restricción dura que condiciona la solución:** el punto y coma está prohibido en cualquier string enviado al MCP (ver "Caracteres a evitar" arriba) — y un atributo `style="border:1px solid #999;padding:4px 8px"` con más de una declaración CSS usa punto y coma entre declaraciones, así que **queda descartado**, aunque sea la forma "moderna" de estilar HTML. La solución es usar **atributos HTML legacy** (`border`, `cellpadding`, `cellspacing`, `bgcolor`, `align`, `width`) en vez de `style` con varias declaraciones — todo navegador y el visor de GLPI los siguen renderizando igual, y ninguno usa punto y coma:

```html
<table border="1" cellpadding="4" cellspacing="0" width="100%">
<tr>
<th bgcolor="#e8e8e8" align="left">Hipótesis</th>
<th bgcolor="#e8e8e8" align="left">Campo</th>
<th bgcolor="#e8e8e8" align="left">Resultado</th>
<th bgcolor="#e8e8e8" align="left">Estado</th>
</tr>
<tr>
<td>H1 ...</td>
<td>nombre_columna</td>
<td>...</td>
<td bgcolor="#e6f4ea"><b>Confirmada</b></td>
</tr>
<tr>
<td>H2 ...</td>
<td>otro_campo</td>
<td>...</td>
<td bgcolor="#fbeaea">Descartada</td>
</tr>
</table>
```

Reglas de estilo, siempre las mismas (no reinventar el formato por comentario, para que todos los tickets se vean igual):
- `<table border="1" cellpadding="4" cellspacing="0" width="100%">` — siempre estos cuatro atributos, en ese orden, en toda tabla comparativa. `border="1"` es lo único que garantiza líneas visibles entre celdas sin usar `style`.
- Encabezado (`<th>`): siempre `bgcolor="#e8e8e8" align="left"` — gris claro, alineado a la izquierda (nunca centrado: dificulta el escaneo vertical de nombres de campo/columna largos).
- Celda con Estado **Confirmada**: `bgcolor="#e6f4ea"` (verde muy claro) — resalta de un vistazo cuál hipótesis quedó activa.
- Celda con Estado **Descartada**: `bgcolor="#fbeaea"` (rojo muy claro), opcional si ayuda a distinguir rápido; con **Complementaria**: `bgcolor="#fff6e0"` (ámbar muy claro), con **Informativa**: `bgcolor="#e8f0fb"` (azul muy claro).
- Un solo atributo por propiedad (`bgcolor`, `align`, `border`, `cellpadding`, `cellspacing`, `width`) — nunca combinarlos dentro de un `style` con más de una declaración, por la restricción del punto y coma.

**Para la matriz de registro maestro × campos `EM_*`** (Paso 5-B punto 1, matriz completa de `openbravo-functional-ticket-analysis` Paso 4): mismos atributos de tabla, y además:
- La fila del **registro del caso** lleva su primera celda (nombre del registro) envuelta en `<b>...</b>`, para ubicarla de un vistazo entre los hermanos.
- **Toda celda cuyo valor se aparte del "Patrón mayoritario de la columna"** (la fila obligatoria de esa matriz) lleva `bgcolor="#fbeaea"` — así el ojo detecta la columna y las filas atípicas sin leer cada celda una por una. Esto incluye **todas** las filas atípicas, no solo la del caso: si dos registros comparten el valor minoritario (ej. C1 y C9), ambas celdas se resaltan igual — el resaltado no implica "es el caso", implica "se aparta de la mayoría".
- La fila final "Patrón mayoritario de la columna" lleva `bgcolor="#f0f0f0"` y el texto envuelto en `<i>...</i>` para distinguirla de las filas de registros reales.

Mismo patrón para la tabla de alcance (Paso 5-B, punto 5): encabezados cortos, una fila por elemento comparado, celdas con el valor concreto (no la descripción larga de por qué importa; eso va en el texto alrededor de la tabla).

Reglas para que la tabla no rompa el límite de tamaño (6-A):
- Máximo 4-5 columnas, encabezados y celdas cortos (palabras o valores, no oraciones). Los atributos `bgcolor`/`align` consumen algo de espacio adicional — si una matriz tiene muchas filas y columnas y no entra en el presupuesto de 6-A, priorizar mantener el formato (bordes + resaltado) sobre agregar más columnas; es mejor una tabla pequeña legible que una grande sin formato.
- Sin etiquetas anidadas dentro de una celda salvo `<b>`/`<i>` puntual — nada de listas ni párrafos dentro de `<td>`.
- Si la tabla completa no entra en el followup disponible (ver 6.2, división en Parte 1/Parte 2), priorizar las columnas que sustentan la conclusión (ej. Hipótesis/Resultado/Estado, o Registro maestro/Campo comparado/Valor) y mover el detalle narrativo extendido a texto plano alrededor, en vez de omitir filas de la comparación o quitar el formato.

Este formato aplica a los comentarios técnicos (6.1, 6.2) — nunca a §7/6.3, que sigue sin SQL, columnas ni IDs técnicos (ver reglas de §7 en el Paso 5-B); si una comparación es relevante para el usuario final en términos de negocio, se resume ahí en lenguaje llano, sin nombres de campo ni una tabla técnica.

### 6-B — Si el análisis produjo un script SQL correctivo sobre el ERP del cliente
Siguiendo la disciplina SQL de `openbravo-functional-ticket-analysis` (Paso 3) para modo automático: cualquier `INSERT`/`UPDATE`/`DELETE`/`DDL` sugerido contra tablas del ERP del cliente (`Fact_Acct`, `C_Invoice`, etc.) va **como texto dentro del comentario privado del Paso 6.2** (detalle de los 9 pasos, secciones 5 y/o 6), nunca como acción ejecutada. Encabezar ese bloque con:

```
⚠️ Script sugerido — requiere revisión y ejecución manual de un técnico.
No fue ejecutado automáticamente.
```

**Obligatorio cuando hay cambio de dato:** si la solución (o una hipótesis que, de confirmarse, exige corrección) implica modificar filas en BD, el análisis de 9 pasos **debe adjuntar el script** (o plantilla con `SELECT` de localización + sentencia de escritura acotada). No se acepta cerrar el plan solo con "un técnico debe corregir el PSD/campo X" sin el SQL sugerido. Si la BD del cliente no estuvo disponible en la corrida, igual se publica la plantilla con placeholders y la condición "ejecutar solo tras confirmar el SELECT".

**Si el cambio lo puede hacer el usuario por interfaz:** no sustituir el script por la UI cuando el dato esté roto a nivel técnico (ej. PSD con BP null no editable en pantalla). En cambio, si la vía correcta es operativa/configuración editable: priorizar esa vía en la **§7** (ventana + pasos) y, si aplica, dejar el script solo como respaldo en §5/§6.

Este flujo automático **solo ejecuta escritura** sobre las tablas propias de GLPI (`glpi_itilfollowups`, `sidesoft_triage_glpi_log`) — nunca sobre la base de datos de producción del ERP del cliente.

Si el Paso 5-B, punto 7, determinó que la corrección tiene una Fase 1 (puntual) y una Fase 2 (masiva), publicar ambas por separado dentro del mismo bloque, cada una con su propio encabezado (`Fase 1 — corrección puntual` / `Fase 2 — corrección masiva, no ejecutar sin revisión`) y el número de registros afectados obtenido en el Paso 5-B, punto 5. Nunca fusionar ambas fases en un único script sin distinguirlas — el volumen alto de la Fase 2 es justamente lo que exige revisión y ejecución por lotes, no ejecución directa.

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

Valores posibles de `estado_procesamiento`: `capacitacion`, `proyecto_no_registrado`, `preguntas_enviadas`, `esperando_respuesta_cliente`, `ok_alta_confianza` (score >= 80), `ok_baja_confianza` (score < 80), `error`.

---

## Reglas críticas (aplican siempre, sin excepción)

- Nunca modificar `status`, salvo las excepciones puntuales ya definidas en esta skill: Caso Capacitación (Paso 4.0 → En curso (planificado) + asignado a kvelasco), Caso Proyecto no registrado (Paso 2-A → En curso (planificado) + asignado a bruno díaz), score >= 90 (Paso 6.4 Caso A → Resuelto + asignado a kvelasco), todo análisis de 9 pasos publicado con score < 90, incluido score <= 70 sin respuesta sugerida (Paso 6.4 Caso A-1 → En curso (planificado) + asignado a kvelasco), y triage de preguntas (Paso 6.4 Caso B → En espera + asignado a kvelasco). Fuera de esos casos, `status` no se toca. **Nunca dejar en Nuevo (status = 1) un ticket cuyo análisis de 9 pasos ya se publicó** — el cron de n8n lo reprocesaría en bucle.
- Nunca inventar nombres de técnicos ni datos que no vengan en el ticket.
- Nunca asignar SLA 1 sin bloqueo total confirmado explícitamente en la descripción.
- Nunca repetir preguntas de aclaración ya enviadas mientras no haya respuesta nueva del solicitante.
- Nunca aplicar el comentario `[TRIAGE-RESPUESTA-SUGERIDA]` como solución del ticket (6.3) si el score de acertividad es menor a 90. Nunca publicar el comentario de respuesta como followup (6.3) si el score es 70 o menor.
- Nunca omitir la **sección 7** del `[TRIAGE-ANALISIS-9PASOS]` porque el score sea bajo o porque no se vaya a publicar triage de respuesta/solución — el score solo condiciona el canal 6.3, no la completitud del análisis.
- Nunca cerrar un plan que exija cambio de datos en el ERP sin **adjuntar el script SQL sugerido** (o plantilla con placeholders) en las secciones 5/6 del análisis. Si el usuario puede hacerlo por interfaz, la §7 (y el triage de respuesta/solución cuando aplique) debe indicar ventana y pasos — no solo "corregir en el sistema".
- Todos los comentarios publicados por este flujo son privados (`is_private = 1`), con una única excepción: el comentario CX del Caso Capacitación (Paso 4.0), que se publica público (`is_private = 0`) porque va dirigido al solicitante. Fuera de ese caso, ninguno llega al solicitante dentro de GLPI.
- Nunca clonar un repo de cliente — siempre leer vía MCP de GitHub, archivo por archivo.
- Nunca procesar un ticket cuyo proyecto no esté en `registro_clientes/clientes.json`.
- Nunca ejecutar (solo sugerir como texto) cualquier `INSERT`/`UPDATE`/`DELETE`/`DDL` sobre la BD de producción del ERP de un cliente — misma disciplina SQL de `openbravo-functional-ticket-analysis` (Paso 3), aplicada en modo automático.
- Toda consulta a la BD de Openbravo del cliente (Paso 3-B) es siempre `SELECT` vía `pg_query`/`pg_describe_table` de MCP-DB, con `database` = `openbravo_db_alias` exacto del cliente (nunca un alias adivinado o distinto al registrado en `clientes.json`), con filtros y `LIMIT` en tablas de alto volumen. `pg_execute` nunca se usa contra el alias de un cliente.
- Siempre registrar el resultado en `sidesoft_triage_glpi_log`, incluso si el ticket terminó en preguntas, en espera, o sin proyecto registrado.
- Nunca dar por buena la respuesta `Insert successful` del MCP-DB: todo id se confirma con un `SELECT` posterior, en una llamada aparte (Paso 6-A).
- Nunca usar `Detalles Adicionales:` de una imagen tal cual, sin pasar por el filtrado del Paso 3-A, como valor literal de un `WHERE` — solo los campos identificados como identificador/monto/fecha concretos, nunca ruido de etiquetas o texto decorativo.
- La memoria del Automation nunca cancela un paso obligatorio: solo abarata su ejecución (Paso 5-EVIDENCIA). Ante contradicción entre la memoria y lo observado en esta corrida, gana lo observado, y la memoria se corrige en el momento.
- Nunca declarar una causa raíz de "falta de registro/proceso manual" para datos ausentes en una ventana/tabla sin antes revisar (Paso 3-C) si existe una integración externa registrada del cliente que normalmente alimenta esa misma ventana — si existe, la sincronización de esa integración es una hipótesis de causa raíz que debe evaluarse y reflejarse en la §7, no descartarse por defecto.
- Nunca marcar `OMITIDO` cuando el repo de código del cliente entero no respondió (404) — ese caso es `REPO_INACCESIBLE` (Paso 2-B, punto 1) y exige el comentario `[TRIAGE-REPO-INACCESIBLE]` alertando el problema de configuración en `clientes.json`. `OMITIDO` es solo para un archivo puntual ausente en un repo accesible.
- Nunca asumir `base_path = ""` (raíz) sin haber pasado por la detección del Paso 2-B — si la auto-detección da cero o múltiples candidatas, el estado es `ESTRUCTURA_NO_DETECTADA`, no una suposición silenciosa de dónde está el código.
- Nunca releer o reinterpretar `clientes.json` en un paso posterior al Paso 2-C — todo paso desde el 3 en adelante consume el `contexto_cliente` ya consolidado, para que un mismo ticket no termine mezclando datos resueltos de forma distinta en pasos distintos.
- Al cargar o corregir una entrada de `clientes.json`, el `owner` tiene que copiarse literal de la URL real del repo en GitHub (`github.com/{owner}/{repo}`), nunca inventarse o abreviarse — un owner mal cargado produce `REPO_INACCESIBLE` indistinguible de un problema de permisos.
- Nunca buscar `cliente.json`, `integraciones.json` o `customizaciones/*.md` en el repo de código del cliente — viven en el repo orquestador, bajo `config_dir` (Paso 3). Si `config_dir` es `null`, no intentar leerlos en ningún lado; registrar "sin `config_dir` configurado", no `OMITIDO`.
- Nunca cerrar el diagnóstico solo con una explicación funcional/de proceso cuando la BD del ERP (Paso 3-B) mostró un valor `null` anómalo en un campo relacional que debería estar poblado — eso es candidato de causa raíz técnica (4-B) y, si aplica corrección de datos, debe acompañarse del script sugerido del Paso 6-B, no reemplazarlo por un rodeo funcional para el usuario final.
- Nunca cerrar como "comportamiento esperado", "el documento ya está registrado" o "genere albarán/factura" cuando el ancla del ticket es un fallo de proceso/BD (motor Paso 1.5 clase A) sin haber corrido la auditoría de `ad_pinstance` (Paso 3-B, 3-A) o cuando esa auditoría muestra `result=0` alineado al síntoma y §7 no lo explica — en esos casos el score máximo es 70 (Paso 6.1).
- Nunca equivaler un label de UI ("Tarifa", "Completar") con la columna o proceso del error SQL sin desambiguar homónimos (motor Paso 1.5 punto 2) y verificar ambos en BD.
- Nunca limitar el Paso 3-B a tickets contables: con documento identificable y síntoma de proceso/datos, la verificación en BD (incluida `ad_pinstance` si aplica) es obligatoria.
- Nunca declarar una fuente como revisada sin un dato probatorio obtenido en esta corrida. Sin dato, la fuente va como `OMITIDO` en el registro de evidencia de la sección 9.
- Nunca cerrar una causa raíz de origen técnico o de datos como caso aislado sin haber corrido la consulta de alcance real del Paso 5-B (punto 5) cuando exista un flujo o módulo compartido que pueda repetir la misma condición en otros registros del cliente.
- Nunca fijar la causa raíz de un ticket habiendo evaluado una sola hipótesis, si con los datos ya leídos en esta corrida existía al menos una hipótesis alternativa razonable — esa evaluación de descarte (Paso 5-B, punto 3) queda registrada en la sección 9, no solo en el razonamiento interno.
- Nunca presentar un workaround como si fuera la corrección definitiva del problema — ambos van declarados por separado en la sección 5 del análisis (Paso 5-B, punto 6).
- Nunca sugerir un único script correctivo masivo cuando la consulta de alcance del Paso 5-B muestre un volumen alto de registros afectados — la corrección se separa en Fase 1 (puntual, lista para ejecutar) y Fase 2 (masiva, por lotes, no lista para correr sin revisión), según el Paso 5-B punto 7 y el Paso 6-B.
- Nunca publicar un segundo `[TRIAGE-SLA-SCORE]`, un segundo `[TRIAGE-ANALISIS-9PASOS]` o un segundo `[TRIAGE-RESPUESTA-SUGERIDA]` para el mismo ticket en la misma corrida o en corridas concurrentes sin una respuesta nueva del solicitante entre ambos — eso lo controla el Paso 4.-1. Si ya existe uno reciente sin respuesta nueva del cliente, esta corrida se aborta (`duplicado_abortado`), no se publica una "segunda opinión".
- Nunca publicar un comentario de corrección/profundización técnica (tipo `[TRIAGE-CORRECCION]`) por separado, después de ya haber publicado el análisis de 9 pasos y la respuesta sugerida. Toda profundización de causa raíz del Paso 5-B se incorpora al mismo documento y a la misma respuesta **antes** de publicar (Paso 6) — nunca como un comentario adicional posterior.
- Nunca publicar el análisis de 9 pasos (6.2) si no pasó el control de calidad de esa sección (9 secciones completas — **incluida la §7** — y coherentes entre sí) — regenerar una vez antes de publicar, en vez de publicar una versión confusa o incompleta. **Excepción de remediación:** si un análisis ya publicado omitió la §7 o el script obligatorio por error de una corrida anterior, se permite **un único** followup privado `[TRIAGE-ANALISIS-9PASOS] Completar secciones faltantes` con solo lo omitido (no un segundo análisis completo ni un `[TRIAGE-CORRECCION]` de causa raíz).
- Nunca dejar la sección de acciones de §7 sin el nombre exacto de la ventana del sistema cuando la solución implique una acción operativa en el ERP — si no se puede confirmar con las fuentes de esta corrida, declararlo explícitamente en la sección 9 en vez de omitir la instrucción o generalizarla.
- Nunca adoptar un ticket relacionado o precedente histórico (propio o detectado por el motor) como causa raíz de este ticket sin haberlo falseado contra un dato concreto de este ticket (Paso 5-B, punto 3) — la similitud de síntoma o de módulo nunca es evidencia suficiente por sí sola. Si no se confirma, o si el análisis propio sostiene una causa distinta, declararlo explícitamente sin relación en las secciones 1 y 4, nunca dejarlo implícito como la solución.
- Nunca fijar la causa raíz sobre un archivo de código (jrxml, función, trigger, clase Java) que no se haya confirmado, mediante el rastreo del Paso 5 punto 3-bis, como el componente real responsable del proceso/documento del ticket — un archivo "similar" o del mismo módulo no confirmado se registra como `COMPONENTE_NO_CONFIRMADO`, no como base de un diagnóstico cerrado.
- Nunca describir en términos genéricos una solución que requiere cambiar un valor de configuración de interfaz (fórmula, parámetro, texto de validación) pudiendo consultarlo por BD — debe incluir el script de actualización sugerido (Paso 6-B) con el valor nuevo exacto, y §7 debe indicar ese mismo valor en lenguaje llano para quien vaya a aplicarlo desde la interfaz.
- Nunca dar por resuelto un cambio de configuración replicado (ej. una fórmula que agrupa conceptos) revisando un solo campo/registro — identificar y listar todos los campos/registros hermanos que deben quedar consistentes (Paso 5-B, punto 5, caso particular de configuración) antes de cerrar la sección 5.
- Nunca cerrar un diagnóstico —incluida la conclusión de que "no hay error" o "es el comportamiento esperado"— apoyándose solo en que el registro es consistente con su propio historial, sin haberlo comparado antes contra sus pares/registros similares (Paso 5-B, punto 1). Consistencia interna (esto siempre pasa así para este registro) no es evidencia de corrección frente a sus pares — esa comparación se hace siempre antes de cerrar, cubriendo tantos escenarios comparables como sea razonable, no solo cuando ya se sospecha un problema de configuración, y su resultado queda registrado en la sección 9 y refleja el score de acertividad (Paso 6.1). Cuando la causa candidata sea un flag/parámetro de un registro maestro (tipo de documento, concepto, parámetro de módulo), comparar transacciones que comparten esa misma configuración **no cumple** esta regla — la comparación debe ser contra los registros maestros hermanos de la misma familia.
- Nunca limitar la enumeración de columnas `EM_*` candidatas (Paso 5-B, punto 1, 1-bis) a lo que el repo/`graphify-out/` pueda mostrar — `pg_describe_table` sobre la tabla maestra en cuestión (punto 1-ter) es una fuente independiente y obligatoria, no un respaldo opcional, y es la **única** fuente válida cuando el repo esté `REPO_INACCESIBLE` o `ESTRUCTURA_NO_DETECTADA` para esta corrida. No cerrar la comparación de pares citando solo el estado del repo en la sección 9 sin haber corrido esta introspección primero.
- Nunca descartar la hipótesis general de "registro maestro anómalo" (Paso 5-B, punto 3) tras probar una sola columna `EM_*` que resultó alineada con los hermanos, cuando la enumeración del punto 1 identificó otras columnas candidatas sobre la misma tabla sin probar — cada columna candidata es su propia fila en la tabla de hipótesis; la hipótesis general solo se descarta cuando todas quedaron probadas.
- Nunca omitir de §7 un campo de configuración marcado Informativa o Complementaria en la tabla de hipótesis (Paso 5-B, punto 3) solo porque fue descartado como causa raíz o porque no resolvería el síntoma — los campos Informativos se informan como punto a validar (aclarando que no corrigen este caso puntual) y los Complementarios como alternativa de solución. Callar un campo relacionado por haberlo descartado como causa deja al usuario sin poder validar esa configuración.
- Nunca recomendar en la sección 5/6 o en §7 el cambio de un campo/parámetro distinto, por nombre, al que quedó "Confirmada" en la tabla de hipótesis del Paso 5-B punto 3 — un campo de nombre o dominio parecido, de otro módulo de personalización, puede ser independiente y no resolver el síntoma reportado.
- Nunca presentar una tabla de hipótesis, comparación contra pares, o alcance (Paso 5-B, puntos 1/3/5) como texto corrido separado por `|` en los comentarios técnicos (6.1, 6.2) — usar la tabla HTML con atributos legacy (`border`, `cellpadding`, `bgcolor`, `align`) del Paso 6-A-bis, dentro del límite de tamaño de cada followup.
- Nunca usar un atributo `style` con más de una declaración CSS (separadas por punto y coma) en las tablas de comentarios (Paso 6-A-bis) — viola la restricción dura del punto y coma en strings enviados al MCP (arriba, Paso 6-A). Usar siempre los atributos HTML legacy (`border`, `cellpadding`, `cellspacing`, `bgcolor`, `align`, `width`), que no requieren punto y coma.
- Nunca marcar una fila de la tabla de hipótesis como "Descartada — alineado con [registro X]" sin haber construido antes la matriz completa con su fila "Patrón mayoritario de la columna" (`openbravo-functional-ticket-analysis`, Paso 4) — coincidir con un hermano que también es minoritario no es evidencia de normalidad, es evidencia de una anomalía compartida.
- Nunca cerrar una causa raíz atribuida a una regla de negocio/configuración —aunque el veredicto sea "comportamiento esperado"— nombrando solo la regla sin decir dónde se configura (ventana/campo o tabla/columna). El cliente puede querer cambiar esa política, y sin esa referencia tendría que abrir otro ticket solo para preguntar dónde ajustarla.
