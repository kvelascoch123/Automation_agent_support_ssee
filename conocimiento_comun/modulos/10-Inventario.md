# Openbravo Sidesoft — Inventario

> Gestión de inventario, movimientos, picking ciego, movimiento parcial, ajuste PDV, stock mínimo/máximo, contabilidad de inventario, recosteo, consultas.

**Paquetes incluidos (16):**
- `ec.com.sidesoft.localization.inventory` — Inventory
- `ec.com.sidesoft.localization.inventory.minmax` — Inventory Stock Min and Max Modules
- `ec.com.sidesoft.localization.inventoryaccounting` — Accounting Inventory Modules
- `ec.com.sidesoft.inventory.custom` — Sidesoft Custom Inventory
- `ec.com.sidesoft.inventory.blind.register` — Sidesoft Blind Inventory Picking
- `ec.com.sidesoft.inventory.partial.out.movement` — Sidesoft Inventory Partial Out Movement
- `com.sidesoft.inventory.movement.frominvoice` — Sidesoft Inventory Movement From Invoice
- `ec.com.sidesoft.movement.addinformation` — Additional Information for Inventory Movements
- `ec.com.sidesoft.movements.consults` — Sidesoft Movements Consults
- `ec.com.sidesoft.localization.adjustment.inventory.pdv` — Adjustment Inventory PDV
- `ec.com.sidesoft.product.balance` — Product Balance
- `ec.com.sidesoft.product.linesinfo` — Sidesoft Product Information in Lines
- `ec.com.sidesoft.warehouse.product` — Sidesoft Warehouse Product
- `ec.com.sidesoft.stock.reports` — Sidesoft Stock Reports
- `ec.com.sidesoft.custom.inout.reports` — In Out Reports
- `ec.sidesoft.recosteo` — Sidesoft Recosteo


---
## Inventory
**Package:** `ec.com.sidesoft.localization.inventory`

# Module overview — Inventory

## Functional

El módulo de Inventario tiene como propósito permitir la gestión eficiente de la administración de existencias dentro de la organización. Es utilizado principalmente por los equipos de logística y almacén para llevar un control preciso de los productos almacenados. Este módulo se integra con otras funciones del ERP, como la gestión de compras y ventas, para asegurar que el inventario esté siempre actualizado y refleje la realidad del negocio.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/inventory` |
| Web | `web/ec.com.sidesoft.localization.inventory/` |

### Declared dependencies

- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSIN`

# Guía de chat — Inventory

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.inventory`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)
- «¿Qué muestra el informe X?» → sección Informes en las clases Java de proceso del paquete (ver ruta "Java" en Technical)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar un nuevo inventario?
- ¿Qué pasos debo seguir para realizar una entrada de mercancía?
- ¿Cómo puedo generar un informe de inventario?
- ¿Es posible modificar un documento de inventario existente?
- ¿Cómo se validan los números de documento en el módulo?
- ¿Qué hacer si encuentro discrepancias en el inventario?
- ¿Cómo se cancelan los pedidos en el módulo de inventario?
- ¿Puedo obtener reportes de movimientos de inventario por fechas específicas?

# Domain — data model

## Functional

El núcleo del módulo de Inventario se basa en la entidad cabecera 'M_INVENTORY', que registra los datos generales de cada inventario. Las etapas del proceso incluyen la entrada y salida de mercancías, que se gestionan a través de las tablas 'M_INOUT' y 'M_INOUTLINE'. Las relaciones entre las tablas se establecen de manera que se permita rastrear las transacciones desde el inventario hasta la ubicación final de los productos. Los triggers clave, como 'SSIN_INVENTORY_VALIDATE_DOCNO', se utilizan para validar documentos de inventario y asegurar la integridad de los datos a medida que se realizan las modificaciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| *(sin tablas en model/tables)* | — | — | — | — | — | — |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`M_INVENTORY`, `M_MATCHPO`, `M_MOVEMENT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

En la interfaz de usuario, los usuarios pueden acceder al módulo de Inventario a través del menú principal del ERP. Aunque no se detallan ventanas específicas en el inventario, la navegación se realiza comúnmente mediante pestañas que permiten gestionar diferentes aspectos del inventario como la visualización de existencias, la entrada y salida de productos, y la generación de informes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.inventory.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Consolidado Ajustes de Inventario Físico por Periodo | Summary Physical Inventory by Period | No |
| Physical Inventory | Physical Inventory | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.inventory.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `255`

- **AD_TAB_ID:** `255` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 24 | Document Type Name | `EM_Ssin_Doctype_ID` | No | No | — |
| 25 | Document No. | `EM_Ssin_Documentno` | No | Sí | — |

### Pestaña `259`

- **AD_TAB_ID:** `259` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 23 | Document Type | `EM_Ssin_Doctype_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye botones típicos para completar procesos como la recepción de mercancías (por ejemplo, 'Importar Movimiento') y la autorización de salidas de inventario. También se dispone de un informe denominado 'PrintInventory', que permite a los usuarios obtener un resumen visual de los productos en inventario. Las validaciones frecuentes que se llevan a cabo son la verificación de documentos y la correcta asignación de ubicaciones de productos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.inventory.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Consolidado Ajustes de Inventario Físico por Periodo | Summary Physical Inventory by Period | Summary Physical Inventory by Period | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Physical Inventory | Physical Inventory | physicalinventory | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | PrintInventory | PrintInventory | PrintInventory | Java `PrintPhysicalInventory` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.java` |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | PrintInventory | `PrintPhysicalInventory` | Informe (servlet PDF) | `—` | ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.jrxml | `src/ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Consolidado Ajustes de Inventario Físico por Periodo | Summary Physical Inventory by Period | Summary Physical Inventory by Period | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Physical Inventory | Physical Inventory | physicalinventory | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Consolidado Ajustes de Inventario Físico por Periodo | Summary Physical Inventory by Period | — | — | — |
| Proceso / otro | Physical Inventory | Physical Inventory | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | PrintInventory | PrintInventory | PrintInventory | Java `PrintPhysicalInventory` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 3**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **1**; archivos `*.jrxml` en el repo = **3**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | PrintInventory | `PrintInventory` | Java `PrintPhysicalInventory`; JRXML `src/ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | PrintInventory. JRXML: `src/ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.jrxml` |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/localization/inventory/ad_reports/PickingList.jrxml`
- `src/ec/com/sidesoft/localization/inventory/ad_reports/Rpt_ssin_ValuedAdjustment.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Ssin_InoutRelated` | It is not possible to reactivate the order if there is a related goods receipt. | It is not possible to reactivate the order if there is a related goods receipt. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye varias clases Java, entre ellas 'PrintPhysicalInventory', encargada de gestionar la generación de informes. Estas clases permiten la integración de funciones adicionales no solo limitadas a la base de datos, facilitando operaciones como la creación de informes personalizables y la interacción con la interfaz de usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.inventory`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `PrintPhysicalInventory` | PrintInventory | HttpSecureAppServlet | — | `src/ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.java` |
| `SL_Movement_Doctype` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/inventory/ad_callouts/SL_Movement_Doctype.java` |
| `ImportMovementWarehouse` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/localization/inventory/ad_process/ImportMovementWarehouse.java` |
| `ImportPhysicalInventory` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/localization/inventory/ad_process/ImportPhysicalInventory.java` |
| `UpdateSequenceInventoryEvent` | events | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/localization/inventory/events/UpdateSequenceInventoryEvent.java` |
| `UpdateSequenceMovementEvent` | events | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/localization/inventory/events/UpdateSequenceMovementEvent.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSIN_INOUTLINE_ORGLOCATOR_TRG` | `m_inoutline` | before INSERT/UPDATE | No se puede registrar lineas con Huecos de otra Organizacion |
| Trigger `SSIN_INOUT_PROC_LINECHK_TRG` | `m_inout` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSIN_INVENTORY_VALIDATE_DOCNO` | `m_inventory` | before INSERT/UPDATE | Validación reutilizable de campos. |
| Trigger `SSIN_ORDER_REACTIVATE_TRG` | `c_order` | after UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `c_doctype - Inventario Fisico` | `c_doctype.docbasetype = 'MMI'` |
| AD_VAL_RULE | — | `Valid Document Type Movement` | `C_DOCTYPE.AD_TABLE_ID = '323'` |
| AD_VAL_RULE | — | `C_DocType_MMI` | `C_DocType.DocBaseType IN ('MMI')` |
| Java event/validator | `UpdateSequenceInventoryEvent` | persistencia/UI | *(leer `src/ec/com/sidesoft/localization/inventory/events/UpdateSequenceInventoryEvent.java`)* |
| Java event/validator | `UpdateSequenceMovementEvent` | persistencia/UI | *(leer `src/ec/com/sidesoft/localization/inventory/events/UpdateSequenceMovementEvent.java`)* |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers en la base de datos son cruciales para el correcto funcionamiento del módulo. Por ejemplo, el trigger 'SSIN_INOUT_PROC_LINECHK_TRG' gestiona validaciones de transacciones de entrada/salida, mientras que 'SSIN_INVENTORY_VALIDATE_DOCNO' ayuda a comprobar que los números de documento sean válidos. Estas funciones permiten mantener la integridad y precisión de los datos dentro del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSIN_ORDER_REACTIVATE_TRG` | `c_order` | after | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSIN_ORDER_REACTIVATE_TRG.xml` |
| `SSIN_INOUT_PROC_LINECHK_TRG` | `m_inout` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSIN_INOUT_PROC_LINECHK_TRG.xml` |
| `SSIN_INOUTLINE_ORGLOCATOR_TRG` | `m_inoutline` | before | INSERT/UPDATE | No se puede registrar lineas con Huecos de otra Organizacion | `model/triggers/SSIN_INOUTLINE_ORGLOCATOR_TRG.xml` |
| `SSIN_INVENTORY_VALIDATE_DOCNO` | `m_inventory` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SSIN_INVENTORY_VALIDATE_DOCNO.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| *(sin funciones en model/functions)* | — | — | — | — |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | PrintInventory | `PrintInventory` | Reporte | Java `PrintPhysicalInventory` | S | Genera PDF desde JRXML `ec/com/sidesoft/localization/inventory/PrintInventory/PrintPhysicalInventory.jrxml`; contexto sesión `—`. |

**Total acciones documentadas (extract):** **1** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.localization.inventory`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | presente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SSIN`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSIN` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.inventory` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Summary Physical Inventory by Period` — Consolidado Ajustes de Inventario Físico por Periodo
- `physicalinventory` — Physical Inventory
- `PrintInventory` — PrintInventory

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Inventory Stock Min and Max Modules
**Package:** `ec.com.sidesoft.localization.inventory.minmax`

# Module overview — Inventory Stock Min and Max Modules

## Functional

El módulo 'Inventory Stock Min and Max' tiene como propósito optimizar la gestión de inventarios al permitir establecer niveles mínimos y máximos de stock para productos. Los actores principales son los usuarios de negocio encargados de la gestión de inventarios, los equipos de soporte L2 y los desarrolladores que pueden implementar mejoras. Este módulo es especialmente relevante para empresas que desean evitar el desabastecimiento o el exceso de inventario, facilitando una planificación adecuada. No tiene dependencias con otros módulos, lo que permite una implementación independiente en Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/inventory/minmax` |
| Web | `web/ec.com.sidesoft.localization.inventory.minmax/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`ECSLIMM`

# Guía de chat — Inventory Stock Min and Max Modules

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.inventory.minmax`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo establecer niveles mínimos y máximos de stock para un producto?
- ¿Qué debo hacer si me doy cuenta de que mis niveles de stock son inadecuados?
- ¿Existen informes que me ayuden a visualizar la situación de mi inventario?
- ¿Cómo ajusto los niveles de stock después de una revisión de inventario?
- ¿Hay alguna validación que deba considerar al modificar los niveles de stock?
- ¿Qué ocurre si un producto alcanza el nivel mínimo de stock?
- ¿Cómo puedo verificar si los cambios en los niveles de stock se han guardado correctamente?
- ¿Es posible revertir cambios en los niveles máximos de stock realizados previamente?

# Domain — data model

## Functional

El módulo modifica la tabla 'M_PRODUCT', que almacena información sobre los productos. Se fija en la entidad cabecera relacionada con la gestión de inventarios, permitiendo a los usuarios establecer límites de stock. Aunque no se detallan etapas ni triggers, el enfoque principal es en el manejo de los niveles de stock, lo que implica una relación directa entre las cantidades disponibles y los productos gestionados. Dado que el módulo no presenta etapas adicionales, la configuración se realiza directamente sobre los productos afectados en el inventario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| *(sin tablas en model/tables)* | — | — | — | — | — | — |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`M_PRODUCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Actualmente, el módulo no cuenta con ventanas específicas en la interfaz de usuario, lo que sugiere que las funcionalidades se integran de manera transparente en las ventanas existentes del sistema. Sin embargo, se prevé que los usuarios puedan gestionar fácilmente los niveles mínimos y máximos a través de las opciones disponibles en la configuración del producto.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.inventory.minmax.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.inventory.minmax.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 1400 | Maximum | `EM_Ecslimm_Max` | No | No | — |
| 1410 | Minimun | `EM_Ecslimm_Min` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos involucrados se centran en la determinación y ajuste de los niveles de stock. Las acciones típicas como completar o ajustar se gestionan desde la interfaz de producto, aunque la documentación específica de botones como 'completar', 'retornar' o 'rechazar' no está presente. Es fundamental que los usuarios validen frecuentemente los niveles de stock establecidos para asegurar que se alineen con la demanda real de productos. No se incluyen informes específicos en esta versión del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.inventory.minmax.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| — | *(sin procesos de botón)* | — | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 0**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

En este módulo no se han implementado clases Java, lo que indica que toda la lógica se maneja dentro de las capacidades nativas del ERP sin personalizaciones adicionales en este ámbito.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.inventory.minmax`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| *(sin clases Java en src/)* | — | — | — | — |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| — | — | *(sin validaciones detectadas en modelo/Java)* | — |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El rol de los triggers en este módulo es inexistente, dado que no se han implementado triggers ni funciones PL específicas. Sin embargo, cualquier necesidad de soporte relacionado con esta funcionalidad puede ser gestionada a través de los mecanismos existentes en la base de datos de Openbravo, ajustando manualmente los niveles de inventario conforme a la lógica del negocio.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| *(sin triggers)* | — | — | — | — | — |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| *(sin funciones en model/functions)* | — | — | — | — |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.localization.inventory.minmax`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `ECSLIMM`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `ECSLIMM` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.inventory.minmax` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Accounting Inventory Modules
**Package:** `ec.com.sidesoft.localization.inventoryaccounting`

# Module overview — Accounting Inventory Modules

## Functional

El módulo de Contabilidad de Inventario tiene como propósito integrar y gestionar las transacciones relacionadas con el inventario dentro del sistema Openbravo. Principalmente, su objetivo es ofrecer un registro contable adecuado de los movimientos de inventario y asegurar que cada transacción sea reflejada correctamente en las cuentas contables. Los actores involucrados son principalmente usuarios de negocio que gestionan inventarios y contadores que supervisan la correcta contabilización de estos movimientos. El alcance del módulo incluye configuraciones contables específicas de inventario y su funcionalidad está directamente relacionada con la gestión de inventarios y la contabilidad dentro del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/inventoryaccounting` |
| Web | `web/ec.com.sidesoft.localization.inventoryaccounting/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLIA`

# Guía de chat — Accounting Inventory Modules

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.inventoryaccounting`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)
- «¿Qué es la tabla slia_inv_parmline?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo configurar mis cuentas contables para el inventario?
- ¿Dónde encuentro las transacciones de inventario registradas?
- ¿Qué pasos seguir para contabilizar un nuevo movimiento de inventario?
- ¿Cómo puedo validar la información contable de un documento de inventario?
- ¿Qué informes de inventario están disponibles en este módulo?
- ¿Puedo ajustar parámetros después de haber registrado transacciones?
- ¿Qué diferencias hay entre completar y rechazar un documento de inventario?
- ¿Cómo se relaciona el inventario con las cuentas contables?

# Domain — data model

## Functional

La entidad cabecera principal de este módulo es la tabla 'slia_inv_parmline', que almacena parámetros y configuraciones relacionadas con las transacciones de inventario. Las etapas de procesamiento no se encuentran claramente definidas en el inventario, pero se sugiere que incluyen la creación y modificación de transacciones de inventario que se verán reflejadas en las cuentas contables. No se identifican triggers específicos en el módulo, lo cual indica una orientación hacia la simplicidad en la gestión de datos, aunque es relevante tener en cuenta que la integración con otros módulos puede generar dependencias que amplían el flujo de trabajo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `slia_inv_parm` |
| `slia_inv_parmline` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `slia_inv_parm` | slia_inv_parm | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `slia_inv_parm_key`; Cols: docbasetype; `SLIA_INV_PARM_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `slia_inv_parmline` | slia_inv_parmline | — | `SLIA_INV_PARMLINE_DOC_UQ` (ad_org_id, c_doctype_id) | slia_inv_parm_id→slia_inv_parm; p_invacct_id→c_validcombination; ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype | Detalle enlazado a ad_client, c_validcombination, slia_inv_parm. | PK `slia_inv_parmline_key`; Cols: slia_inv_parm_id, c_doctype_id, p_invacct_id; `SLIA_INV_PLINE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `slia_inv_parm` |
| `slia_inv_parmline` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo de Contabilidad de Inventario se navega a través de una ventana principal llamada 'Configuración Contable de Inventario'. En esta ventana, los usuarios pueden acceder a las configuraciones relevantes para la contabilización de movimientos de inventario y ajustar los parámetros según sea necesario. La interfaz de usuario está diseñada para ser intuitiva, permitiendo a los usuarios gestionar rápidamente las configuraciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.inventoryaccounting.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuración Contable de Inventario | Inventory Accounting configuration |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración Contable de Inventario | Inventory Accounting configuration | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.inventoryaccounting.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuración Contable de Inventario

- **AD_WINDOW_ID:** `07AC202A05B04F33BA21C56E4285F110`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Inventory Parameters | `A8C98AE8E6DC4E35B8AED90F35F2A2D7` | 0 |
| 20 | Line | `B8A1BB047DBE47CF8CCEE6C1F28C2569` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Line (ventana: Configuración Contable de Inventario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | C_Doctype_ID | `C_Doctype_ID` | No | No | — |
| 40 | FIN_Financial_Account_ID | `P_Invacct_ID` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Inventory Parameters (ventana: Configuración Contable de Inventario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Docbasetype | `Docbasetype` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Aunque no se especifican botones de procesos o informes, es común en este tipo de módulos contar con operaciones como 'Completar', 'Retornar' o 'Rechazar' en el manejo de transacciones. Es probable que existan validaciones frecuentes para asegurar la consistencia y corrección de los datos que se registran en el sistema. Para obtener información detallada, se puede incluir la creación de informes contables que reflejen los movimientos de inventario y su impacto en los estados financieros.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.inventoryaccounting.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| — | *(sin procesos de botón)* | — | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 0**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Slia_ErrorInvParms` | The selected document base type is already created in another organization. | The selected document base type is already created in another organization. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye diversas clases Java, como 'DocInventory', 'DocLine_Material', y 'DocLines', que manejan la lógica de documentos contables relacionados con transacciones de inventario. Estas clases se encargan de cargar, transformar y gestionar los datos necesarios para contabilizar movimientos de inventario correctamente en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.inventoryaccounting`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `DocInventory` | acc_template | AcctServer | — | `src/ec/com/sidesoft/localization/inventoryaccounting/acc_template/DocInventory.java` |
| `DocLine_Material` | acc_template | DocLines | — | `src/ec/com/sidesoft/localization/inventoryaccounting/acc_template/DocLine_Material.java` |
| `DocLines` | acc_template | — | — | `src/ec/com/sidesoft/localization/inventoryaccounting/acc_template/DocLines.java` |
| `InventoryAccountingTemplate` | acc_template | DocInventoryTemplate | — | `src/ec/com/sidesoft/localization/inventoryaccounting/acc_template/InventoryAccountingTemplate.java` |
| `Slia_InventoryParamsEvent` | businessevent | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/localization/inventoryaccounting/businessevent/Slia_InventoryParamsEvent.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Slia_ValidateInventory` | `C_Doctype.docbasetype in (Select docbasetype from slia_inv_parm where slia_inv_parm_id = @slia_inv_parm_id@)` |
| Java event/validator | `Slia_InventoryParamsEvent` | persistencia/UI | *(leer `src/ec/com/sidesoft/localization/inventoryaccounting/businessevent/Slia_InventoryParamsEvent.java`)* |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

En el módulo no se han definido triggers o funciones PL, lo que puede indicar que el manejo de datos se basa en procedimientos estándar de las transacciones sin lógica adicional. Sin embargo, esto permite una mayor flexibilidad, y el soporte se puede manejar a través de funcionalidades básicas del sistema de base de datos. Se aconseja explorar las configuraciones de 'slia_inv_parmline' para entender cómo se reflejan las transacciones en la contabilidad.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| *(sin triggers)* | — | — | — | — | — |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| *(sin funciones en model/functions)* | — | — | — | — |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.localization.inventoryaccounting`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | presente |
| `AD_WINDOW.xml` | presente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SLIA`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLIA` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.inventoryaccounting` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Custom Inventory
**Package:** `ec.com.sidesoft.inventory.custom`

# Module overview — Sidesoft Custom Inventory

## Functional

El módulo Sidesoft Custom Inventory tiene como propósito principal la gestión y personalización de inventarios en el sistema Openbravo ERP. Actores involucrados incluyen usuarios de negocio encargados del manejo del inventario, así como desarrolladores que integran y mantienen el módulo. El alcance del módulo incluye funciones relacionadas con la actualización y personalización de la gestión de inventarios, sin añadir ventanas o menús adicionales. El correcto funcionamiento depende de la compatibilidad con las versiones del skin y el núcleo del sistema Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/inventory/custom` |
| Web | `web/ec.com.sidesoft.inventory.custom/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SICUS`

# Guía de chat — Sidesoft Custom Inventory

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.inventory.custom`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo actualizar el inventario de un producto específico?
- ¿Qué pasos debo seguir para personalizar las configuraciones del inventario?
- ¿Cómo integro el inventario personalizado con las órdenes existentes?
- ¿Existen validaciones automáticas al modificar la tabla de órdenes?
- ¿Dónde puedo acceder a los informes relacionados con el inventario?
- ¿Puedo revertir cambios realizados en las configuraciones del inventario?
- ¿Qué funciones PL debo conocer para optimizar la gestión del inventario?
- ¿Cómo puedo verificar la compatibilidad del módulo con nuevas versiones?

# Domain — data model

## Functional

Este módulo interactúa principalmente con la entidad cabecera 'C_ORDER', que representa las órdenes dentro del sistema. Se realizan modificaciones en la tabla 'C_ORDER' que reflejan las características personalizadas del inventario. Aunque no se especifican las etapas de un flujo explícito en el inventario, las relaciones entre órdenes y el inventario se establecen a través de estas modificaciones. No se han implementado triggers clave en este módulo, lo que sugiere que las operaciones se manejan a través de funciones PL.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| *(sin tablas en model/tables)* | — | — | — | — | — | — |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_ORDER`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Dado que el módulo no contiene ventanas o menús definidos, la navegación se limita a las interacciones que se realizan a través de la tabla 'C_ORDER'. Los usuarios interactuarán con esta tabla según las operaciones de inventario personalizadas que deseen realizar, aprovechando las mejoras sin la necesidad de nuevas interfaces.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.inventory.custom.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.inventory.custom.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `187`

- **AD_TAB_ID:** `187` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 113 | Reserved Quantity | `EM_SICUS_Reserved_Quantity` | No | Sí | — |

### Pestaña `AF4090093CFF1431E040007F010048A5`

- **AD_TAB_ID:** `AF4090093CFF1431E040007F010048A5` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2008 | Invoice to Return | `EM_Sicus_Invoice_Ret_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo no incluye procesos típicos asociados con botones específicos como completar, retornar o rechazar, lo que indica que la gestión de los inventarios se lleva a cabo a través de actualizaciones directas en la tabla relevante. No se han definido informes específicos ni validaciones frecuentes dentro del módulo, lo que permite una mayor flexibilidad en cómo los usuarios interactúan con el inventario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.inventory.custom.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| — | *(sin procesos de botón)* | — | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 2**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **2**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

No se han implementado clases de Java en este módulo, por lo que no hay un papel específico que desempeñar en la programación Java dentro del mismo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.inventory.custom`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| *(sin clases Java en src/)* | — | — | — | — |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `sicus_invoice_val` | `c_invoice.issotrx='Y' and c_invoice.processed='Y' and c_invoice.C_DocType_ID not in (select C_DocType_ID from C_DocType ` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El rol de las funciones en PL (Programación Lógica) dentro de este módulo es crucial para proporcionar soporte técnico, ya que gestionan la lógica empresarial asociada a las personalizaciones de inventario. A través de estas funciones, se asegura que las operaciones realizadas sobre la tabla C_ORDER cumplan con las normativas del negocio.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| *(sin triggers)* | — | — | — | — | — |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sicus_invoice_ret` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SICUS_INVOICE_RET.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.inventory.custom`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SICUS`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SICUS` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.inventory.custom` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Blind Inventory Picking
**Package:** `ec.com.sidesoft.inventory.blind.register`

# Module overview — Sidesoft Blind Inventory Picking

## Functional

El módulo Sidesoft Blind Inventory Picking está diseñado para optimizar la gestión de inventarios ciegos dentro de Openbravo ERP. Permite a los usuarios realizar inventarios sin tener que conocer la ubicación exacta de los productos, facilitando así el proceso de conteo de stock. Los actores principales de este módulo incluyen usuarios de negocio que llevan a cabo el inventario, personal de soporte técnico de nivel 2 que brinda apoyo, y desarrolladores que pueden personalizar o extender la funcionalidad del módulo. La extensión tiene dependencia del '2.50 to 3.00 Compatibility Skin', que asegura compatibilidad visual y funcional en diferentes versiones de la plataforma.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/inventory/blind/register` |
| Web | `web/ec.com.sidesoft.inventory.blind.register/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SIBLR`

# Guía de chat — Sidesoft Blind Inventory Picking

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.inventory.blind.register`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)
- «¿Qué muestra el informe X?» → sección Informes en las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «¿Qué es la tabla siblr_physical_invtlines?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo realizar un inventario ciego?
- ¿Qué sucede si encuentro discrepancias en el inventario?
- ¿Cómo imprimir el informe de inventario ciego?
- ¿Puedo modificar las líneas de inventario después de haberlas ingresado?
- ¿Cómo se gestionan las eliminaciones de líneas en el inventario?
- ¿Qué validaciones se realizan al ingresar datos en el inventario?
- ¿Cómo accedo a la ventana de Inventario Físico Ciego?
- ¿Qué debo hacer si el sistema presenta un error al completar el inventario?

# Domain — data model

## Functional

En el modelo de datos, la entidad cabecera es la tabla 'siblr_physical_invtlines', que almacena las líneas del inventario físico ciego. Este módulo incluye un disparador clave 'SIBLR_DELETE_LINES_TRG' que maneja la eliminación de líneas del inventario dependiendo de ciertas condiciones. La estructura de datos está diseñada para rastrear la cantidad de productos y sus localizaciones sin la necesidad de exponer al usuario detalles específicos del inventario, mejorando así la eficiencia del conteo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `siblr_collaborators` |
| `siblr_physical_inventory` |
| `siblr_physical_invtlines` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `siblr_collaborators` | Siblr_Collaborators | — | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org; siblr_physical_inventory_id→siblr_physical_inventory | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `siblr_collaborators_key`; Cols: employe_identify, description, c_bpartner_id, to_discount, isadmin; `SIBLR_COLLABOR_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SIBLR_COLLABOR_ISADMIN_CHK`: ISADMIN IN ('Y', 'N') |
| `siblr_physical_inventory` | Siblr_Physical_Inventory | — | `SIBLR_INVENTORY_VALUE` (ad_client_id, documentno) | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype; c_costcenter_id→c_costcenter; m_locator_id→m_locator (+1) | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `siblr_physical_inventory_key`; Cols: documentno, name, description, c_doctype_id, movementdate; `SIBLR_INVENTORY_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `siblr_physical_invtlines` | Siblr_Physical_InvtLines | `SIBLR_DELETE_LINES_TRG` | — | m_attributesetinstance_id→m_attributesetinstance; ad_client_id→ad_client; ad_org_id→ad_org; c_uom_id→c_uom; m_product_id→m_product (+2) | Detalle enlazado a ad_client, ad_org, m_attributesetinstance. Validado por trigger(s): SIBLR_DELETE_LINES_TRG. | PK `siblr_physical_invtlinesl_key`; Cols: difference, m_product_id, qtycount, qtyteory, siblr_physical_inventory_id; `SIBLR_INVENTL_DIFFERENCE_CHK`: DIFFERENCE IN ('Y', 'N'); `SIBLR_INVENTL_PROCESSING_CHK`: PROCESSING IN ('Y', 'N') (+1); idx `SIBLR_PHYSICAL_INVENTORY_IDX` (siblr_physical_inventory_id); idx `SIBLR_PHYSICAL_INVT_PRODUCT` (m_product_id) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Siblr_Collaborators` |
| `Siblr_Physical_Inventory` |
| `Siblr_Physical_InvtLines` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_DOCTYPE`, `M_BRAND`, `M_PRODUCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación dentro del módulo se realiza a través de la ventana 'Inventario Físico Ciego'. Dentro de esta ventana, los usuarios pueden acceder a diferentes pestañas para gestionar y revisar el inventario ciego, facilitando el ingreso y la modificación de datos pertinentes al proceso de conteo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.inventory.blind.register.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Inventario Físico Ciego | Physical Inventory Blind |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Inventario Físico Ciego | Physical Inventory Blind | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.inventory.blind.register.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Inventario Físico Ciego

- **AD_WINDOW_ID:** `2671D49BE8404D209A20D595BDC69679`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Physical Inventory Blind | `AEF7D47B95B04EF39665BA6B5791349F` | 0 |
| 20 | Lines | `94C3763A9AC54C8CA912AB832D832509` | 1 |
| 30 | Collaborators | `19040DACC01345BB958FDDAAE19B90C2` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 360 | Type Inventory | `EM_Siblr_Type_Inventory` | No | No | — |

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 597 | Is Warehouse | `EM_Siblr_Iswarehouse` | No | No | — |

### Lines (ventana: Inventario Físico Ciego)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 5 | Product Code | `Product_Code` | No | Sí | — |
| 10 | Product | `M_Product_ID` | No | Sí | — |
| 15 | Attribute Set Value | `M_Attributesetinstance_ID` | No | Sí | — |
| 20 | Quantity count | `Qtycount` | No | No | — |
| 60 | Difference | `Difference` | No | Sí | — |
| 70 | UOM | `C_Uom_ID` | No | Sí | — |
| 80 | Product Category | `M_Product_Category_ID` | No | Sí | — |

### Physical Inventory Blind (ventana: Inventario Físico Ciego)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Date | `Movementdate` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 35 | Document No. | `Documentno` | No | Sí | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 90 | Warehouse | `M_Warehouse_ID` | No | No | — |
| 110 | Create Lines | `Actioncreatelines` | No | No | — |
| 120 | Locator | `M_Locator_ID` | No | No | — |
| 130 | NEW_Docaction | `NEW_Docaction` | No | No | — |
| 140 | Printed | `Isprint` | No | Sí | — |
| 150 | Cost Center | `C_Costcenter_ID` | No | No | — |

### Collaborators (ventana: Inventario Físico Ciego)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 30 | To Discount | `TO_Discount` | No | Sí | — |
| 40 | Is Admin | `Isadmin` | No | Sí | — |

### Pestaña `C65FEEACC44241A1966AD608DD76CD88`

- **AD_TAB_ID:** `C65FEEACC44241A1966AD608DD76CD88` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 50 | Type | `EM_Siblr_Type` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo implementa varios procesos, cada uno asociado a un botón como completar, retornar o rechazar entradas de inventario. Por ejemplo, al completar un inventario, se registran los datos recolectados y se generan informes, como el 'Impresión Genérica de Inventario Ciego'. Este proceso incluye validaciones frecuentes para asegurar que los datos ingresados sean correctos y que no se produzcan inconsistencias.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.inventory.blind.register.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Registrar | Siblr_New_DocActionInv | Siblr_New_DocActionInv | Java `ProcessedInventory` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Siblr_Physical_Inventory_ID` | `src/ec/com/sidesoft/inventory/blind/register/ad_process/ProcessedInventory.java` |
| Botón (PL/pgSQL) | Cargar Lineas | Siblr_CreateLines | Siblr_CreateLines | `siblr_insert_invtlines` | No se pueden cargar lineas debido a errores en pedidos de venta; UPDATE OBPOS_Errors SET created = NOW() WHERE OBPOS_Errors_id='6AA691311B044F77A8ACC0461DC4A951'; AND sd.qtyonhand <> 0 AND sd.qtyorderonhand <> 0 AND sd.… | — |
| Botón (PL/pgSQL) | Procesar | Siblr_DocActionInv | Siblr_DocActionInv | `siblr_doc_register` | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta trans… | — |
| Botón (PL/pgSQL) | Siblr_CallFunction | Siblr_CallFunction | Siblr_CallFunction | `siblr_doc_register` | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta trans… | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Impresión Genérica de Inventario Ciego | Siblr_GenericPrintInventory | Siblr_GenericPrintInventory | Java `Siblr_GenericPrintInventory` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `2671D49BE8404D209A20D595BDC69679|SIBLR_PHYSICAL_INVENTORY_ID`. | `src/ec/com/sidesoft/inventory/blind/register/ad_process/Siblr_GenericPrintInventory.java` |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Registrar | `ProcessedInventory` | Proceso Java (toolbar/background) | `Siblr_Physical_Inventory_ID` | — | `src/ec/com/sidesoft/inventory/blind/register/ad_process/ProcessedInventory.java` |
| Reporte | Impresión Genérica de Inventario Ciego | `Siblr_GenericPrintInventory` | Informe (servlet PDF) | `2671D49BE8404D209A20D595BDC69679|SIBLR_PHYSICAL_INVENTORY_ID` | — | `src/ec/com/sidesoft/inventory/blind/register/ad_process/Siblr_GenericPrintInventory.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Registrar | Siblr_New_DocActionInv | Siblr_New_DocActionInv | Java `ProcessedInventory` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Siblr_Physical_Inventory_ID` | `src/ec/com/sidesoft/inventory/blind/register/ad_process/ProcessedInventory.java` |
| Botón (PL/pgSQL) | Cargar Lineas | Siblr_CreateLines | Siblr_CreateLines | `siblr_insert_invtlines` | No se pueden cargar lineas debido a errores en pedidos de venta; UPDATE OBPOS_Errors SET created = NOW() WHERE OBPOS_Errors_id='6AA691311B044F77A8ACC0461DC4A951'; AND sd.qtyonhand <> 0 AND sd.qtyorderonhand <> 0 AND sd.… | — |
| Botón (PL/pgSQL) | Procesar | Siblr_DocActionInv | Siblr_DocActionInv | `siblr_doc_register` | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta trans… | — |
| Botón (PL/pgSQL) | Siblr_CallFunction | Siblr_CallFunction | Siblr_CallFunction | `siblr_doc_register` | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta trans… | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Registrar | Siblr_New_DocActionInv | Java `ProcessedInventory` | Proceso Openbravo registro `Siblr_Physical_Inventory_ID` | Proceso Openbravo registro `Siblr_Physical_Inventory_ID` |
| Botón (PL/pgSQL) | Cargar Lineas | Siblr_CreateLines | PL `siblr_insert_invtlines` | No se pueden cargar lineas debido a errores en pedidos de venta; UPDATE OBPOS_Errors SET created = NOW() WHERE OBPOS_Errors_id='6AA691311B044F77A8ACC0461DC4A951'; AND sd.qtyonhand <> 0 AND sd.qtyorderonhand <> 0 AND sd.… | No se pueden cargar lineas debido a errores en pedidos de venta; UPDATE OBPOS_Errors SET created = NOW() WHERE OBPOS_Errors_id='6AA691311B044F77A8ACC0461DC4A951'; AND sd.qtyonhand <> 0 AND sd.qtyorderonhand <> 0 AND sd.reservedqty <> 0 AND sd.allocatedqty <> 0; BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; LA ORGANIZACION DEL PRODUCTO ES IGUAL A LA ORGANIZACION DE LA MARCA |
| Botón (PL/pgSQL) | Procesar | Siblr_DocActionInv | PL `siblr_doc_register` | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta trans… | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta transacción debido a errores en pedidos de venta; No existen lineas para procesar esta transacción; AND TO_DATE(TO_CHAR(created,'YYYY-MM-DD'),'YYYY-MM-DD') = TO_DATE(TO_CHAR(TO_DATE(NOW()),'YYYY-MM-DD'),'YYYY-MM-DD') |
| Botón (PL/pgSQL) | Siblr_CallFunction | Siblr_CallFunction | PL `siblr_doc_register` | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta trans… | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta transacción debido a errores en pedidos de venta; No existen lineas para procesar esta transacción; AND TO_DATE(TO_CHAR(created,'YYYY-MM-DD'),'YYYY-MM-DD') = TO_DATE(TO_CHAR(TO_DATE(NOW()),'YYYY-MM-DD'),'YYYY-MM-DD') |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Impresión Genérica de Inventario Ciego | Siblr_GenericPrintInventory | Siblr_GenericPrintInventory | Java `Siblr_GenericPrintInventory` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `2671D49BE8404D209A20D595BDC69679|SIBLR_PHYSICAL_INVENTORY_ID`. | `src/ec/com/sidesoft/inventory/blind/register/ad_process/Siblr_GenericPrintInventory.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 1**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **1**; archivos `*.jrxml` en el repo = **1**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Impresión Genérica de Inventario Ciego | `Siblr_GenericPrintInventory` | Java `Siblr_GenericPrintInventory`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Siblr_GenericPrintInventory |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/inventory/blind/register/ad_reports/Rpt_Blind_Inventory.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo utiliza Java en dos clases principales que facilitan la actuación de funciones específicas dentro de los procesos de inventario, como la gestión de organizaciones y la generación de informes, integrándose con otras funcionalidades del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.inventory.blind.register`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Siblr_PhysicalInventoryBlind_Organization` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/inventory/blind/register/ad_callouts/Siblr_PhysicalInventoryBlind_Organization.java` |
| `ProcessedInventory` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/inventory/blind/register/ad_process/ProcessedInventory.java` |
| `Siblr_GenericPrintInventory` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/inventory/blind/register/ad_process/Siblr_GenericPrintInventory.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SIBLR_DELETE_LINES_TRG` | `siblr_physical_invtlines` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Siblr_ValidWarehouse` | `M_WAREHOUSE.M_WAREHOUSE_ID IN (
SELECT M_WAREHOUSE_ID FROM M_WAREHOUSE WHERE AD_CLIENT_ID = @#AD_CLIENT_ID@    AND M_WAR` |
| AD_VAL_RULE | — | `siblr_IsEmployee` | `C_BPartner.IsEmployee = 'Y' and C_BPartner.IsActive = 'Y'` |
| AD_VAL_RULE | — | `Siblr_Producto - isWareHause` | `M_PRODUCT.em_siblr_iswarehouse = 'Y'` |
| AD_VAL_RULE | — | `Siblr_C_DocType_MMI` | `C_DocType.DocBaseType IN ('MMI') AND C_DocType.em_siblr_type_inventory = 'COU'` |
| AD_VAL_RULE | — | `Siblr_Warehouse - Organization` | `M_Warehouse.ad_org_id = @ad_org_id@` |
| AD_VAL_RULE | — | `Siblr_M_Locator - Warehouse` | `M_Locator.M_Warehouse_ID = @M_Warehouse_ID@` |
| Función PL `siblr_doc_register` | — | invocación proceso | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP |
| Función PL `siblr_insert_invtlines` | — | invocación proceso | No se pueden cargar lineas debido a errores en pedidos de venta; UPDATE OBPOS_Errors SET created = NOW() WHERE OBPOS_Errors_id='6AA691311B044F77A8ACC0461DC4A951'; AND sd.qtyonhand <> 0 AND sd.qtyorderonhand <> 0 AND sd.reservedqty <> 0 AND sd.allocatedqty <> 0 |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL/pgSQL son esenciales para el mantenimiento de la integridad de la base de datos, actuando como validadores automáticos durante la ejecución de procesos. Se utilizan para gestionar lógica como el borrado de líneas de inventario en el caso de que no se cumplan determinadas condiciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SIBLR_DELETE_LINES_TRG` | `siblr_physical_invtlines` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SIBLR_DELETE_LINES_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `siblr_differences_in_lines` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SIBLR_DIFFERENCES_IN_LINES.xml` |
| `siblr_doc_register` | Siblr_CallFunction, Procesar | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta trans… | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolver MP; No se puede registrar esta transacción debido a errores en pedidos de venta; No existen lineas para procesar esta transacción; AND TO_DATE(TO_CHAR(created,'YYYY-MM-DD'),'YYYY-MM-DD') = TO_DATE(TO_CHAR(TO_DATE(NOW()),'YYYY-MM-DD'),'YYYY-MM-DD') | `model/functions/SIBLR_DOC_REGISTER.xml` |
| `siblr_get_product_cost` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SIBLR_GET_PRODUCT_COST.xml` |
| `siblr_insert_invtlines` | Cargar Lineas | No se pueden cargar lineas debido a errores en pedidos de venta; UPDATE OBPOS_Errors SET created = NOW() WHERE OBPOS_Errors_id='6AA691311B044F77A8ACC0461DC4A951'; AND sd.qtyonhand <> 0 AND sd.qtyorderonhand <> 0 AND sd.… | No se pueden cargar lineas debido a errores en pedidos de venta; UPDATE OBPOS_Errors SET created = NOW() WHERE OBPOS_Errors_id='6AA691311B044F77A8ACC0461DC4A951'; AND sd.qtyonhand <> 0 AND sd.qtyorderonhand <> 0 AND sd.reservedqty <> 0 AND sd.allocatedqty <> 0; BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; LA ORGANIZACION DEL PRODUCTO ES IGUAL A LA ORGANIZACION DE LA MARCA | `model/functions/SIBLR_INSERT_INVTLINES.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Registrar | `Siblr_New_DocActionInv` | Botón (Java) | Java `ProcessedInventory` | N | Proceso Openbravo registro `Siblr_Physical_Inventory_ID` |
| 2 | Cargar Lineas | `Siblr_CreateLines` | Botón (PL/pgSQL) | PL `siblr_insert_invtlines` | N | No se pueden cargar lineas debido a errores en pedidos de venta; UPDATE OBPOS_Errors SET created = NOW() WHERE OBPOS_Errors_id='6AA691311B044F77A8ACC0461DC4A951'; AND sd.qtyonhand  |
| 3 | Procesar | `Siblr_DocActionInv` | Botón (PL/pgSQL) | PL `siblr_doc_register` | N | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolv |
| 4 | Siblr_CallFunction | `Siblr_CallFunction` | Botón (PL/pgSQL) | PL `siblr_doc_register` | N | No se pueden registrar esta transacción debido a errores en pedidos de venta; Existen albaranes de proveedores en estado borrador; Existen recibos de material pendientes por devolv |
| 5 | Impresión Genérica de Inventario Ciego | `Siblr_GenericPrintInventory` | Reporte | Java `Siblr_GenericPrintInventory` | S | Genera PDF desde JRXML `—`; contexto sesión `2671D49BE8404D209A20D595BDC69679|SIBLR_PHYSICAL_INVENTORY_ID`. |

**Total acciones documentadas (extract):** **5** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.inventory.blind.register`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | presente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SIBLR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SIBLR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.inventory.blind.register` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Siblr_New_DocActionInv` — Registrar
- `Siblr_CreateLines` — Cargar Lineas
- `Siblr_DocActionInv` — Procesar
- `Siblr_CallFunction` — Siblr_CallFunction
- `Siblr_GenericPrintInventory` — Impresión Genérica de Inventario Ciego

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Inventory Partial Out Movement
**Package:** `ec.com.sidesoft.inventory.partial.out.movement`

# Module overview — Sidesoft Inventory Partial Out Movement

## Functional

El módulo 'Sidesoft Inventory Partial Out Movement' está diseñado para gestionar los despachos parciales de inventario, facilitando el movimiento efectivo de productos de un almacén. Este módulo es utilizado principalmente por los usuarios de negocio que realizan la consolidación de despachos, así como por el personal de soporte y desarrollo que requiere entender el funcionamiento interno del mismo. Dependiendo de las configuraciones establecidas en el sistema, permite realizar operaciones que impactan las líneas de órdenes y la acumulación de inventario en tiempo real.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/inventory/partial/out/movement` |
| Web | `web/ec.com.sidesoft.inventory.partial.out.movement/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSIPOTM`

# Guía de chat — Sidesoft Inventory Partial Out Movement

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.inventory.partial.out.movement`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)
- «¿Qué es la tabla ssipotm_config?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo hacer una consolidación de despachos?
- ¿Qué pasos debo seguir para configurar el módulo?
- ¿Dónde encuentro las validaciones de líneas acumuladas?
- ¿Qué hacer si un despacho no se refleja en mi inventario?
- ¿Cómo afecta un cambio en la configuración de despachos a mis órdenes?
- ¿Cuáles son los triggers que se activan al realizar un movimiento?
- ¿Dónde están los logs de errores para este módulo?
- ¿Cómo puedo acceder a la documentación técnica del módulo?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad principal de cabecera, que es la tabla 'ssipotm_config', que controla la configuración del módulo de despachos parciales. Las relaciones están definidas a través de la tabla 'C_ORDERLINE', que se modifica por el módulo para reflejar los cambios en las líneas de pedidos de acuerdo a los movimientos parciales. Los triggers clave, como 'SSIPOTM_ACCUMULATED_TRG', 'SSIPOTM_ORDERLINE_TRG' y 'SSIPOTM_PARTIALD_TRG', se activan para actualizar los datos de las tablas involucradas en los despachos y asegurar la consistencia de la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssipotm_accumulated` |
| `ssipotm_attribute_product` |
| `ssipotm_config` |
| `ssipotm_orderline` |
| `ssipotm_partial_dispatch` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssipotm_accumulated` | ssipotm_accumulated | `SSIPOTM_ACCUMULATED_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; m_product_id→m_product; c_uom_id→c_uom; m_warehouse_id→m_warehouse (+1) | Detalle enlazado a ad_client, ad_org, m_product. Validado por trigger(s): SSIPOTM_ACCUMULATED_TRG. | PK `ssipotm_accumulated_key`; Cols: ssipotm_partial_dispatch_id, m_product_id, c_uom_id, m_warehouse_id, quantity; `SSIPOTM_ACCUMULATED_DSPTCH_CK`: DESPATCH <= STOCK; `SSIPOTM_ACCUMULATED_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssipotm_attribute_product` | ssipotm_attribute_product | — | — | m_attributesetinstance_id→m_attributesetinstance; ad_client_id→ad_client; m_locator_id→m_locator; ad_org_id→ad_org; m_product_id→m_product (+2) | Detalle enlazado a ad_client, m_attributesetinstance, m_locator. | PK `ssipotm_attribute_product_key`; Cols: ssipotm_partial_dispatch_id, line, m_product_id, c_uom_id, m_locator_id; `SSIPOTM_ATTRIBUTE_PRODUCT_ISA`: ISACTIVE IN ('Y', 'N') |
| `ssipotm_config` | ssipotm_config | — | — | ad_client_id→ad_client; invoice_doctype_id→c_doctype; inout_doctype_id→c_doctype; ad_org_id→ad_org; m_pricelist_id→m_pricelist (+2) | Parametrización / catálogo de soporte. | PK `ssipotm_config_key`; Cols: inout_doctype_id, invoice_doctype_id, c_paymentterm_id, fin_paymentmethod_id, m_pricelist_id; `SSIPOTM_CONFIG_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssipotm_orderline` | ssipotm_orderline | `SSIPOTM_ORDERLINE_TRG` | — | c_orderline_id→c_orderline; c_bpartner_id→c_bpartner; ad_client_id→ad_client; c_order_id→c_order; ad_org_id→ad_org (+4) | Detalle enlazado a ad_client, c_bpartner, c_orderline. Validado por trigger(s): SSIPOTM_ORDERLINE_TRG. | PK `ssipotm_ol_key`; Cols: ssipotm_partial_dispatch_id, c_order_id, poreference, dateordered, datepromised; `SSIPOTM_OL_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssipotm_partial_dispatch` | ssipotm_partial_dispatch | `SSIPOTM_PARTIALD_TRG` | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; c_doctype_id→c_doctype; c_invoice_id→c_invoice; m_inout_id→m_inout (+3) | Detalle enlazado a ad_client, c_bpartner, c_doctype. Validado por trigger(s): SSIPOTM_PARTIALD_TRG. | PK `ssipotm_pd_key`; Cols: c_doctype_id, documentno, docstatus, c_bpartner_id, dispatch_date; `SSIPOTM_PD_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssipotm_accumulated` |
| `ssipotm_attribute_product` |
| `ssipotm_config` |
| `ssipotm_orderline` |
| `ssipotm_partial_dispatch` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_ORDERLINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo cuenta con dos ventanas principales: 'Configuración de Consolidación de Despachos' y 'Consolidación de Despachos'. La navegación se realiza a través del menú principal, donde los usuarios pueden acceder a la configuración necesaria para ajustar las preferencias del sistema relacionado con los despachos parciales. Cada ventana ofrece distintas pestañas donde se detallan los campos necesarios para completar la operación deseada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.inventory.partial.out.movement.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuración de Consolidación de Despachos | Dispatches Consolidation Configuration |
| Consolidación de Despachos | Consolidation of Dispatches |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración de Consolidación de Despachos | Dispatches Consolidation Configuration | No |
| Consolidación de Despachos | Consolidation of Dispatches | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.inventory.partial.out.movement.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuración de Consolidación de Despachos

- **AD_WINDOW_ID:** `A503E644EDA842C8A2387168D7829DAE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `D8DDCE09D47A4061A11F0CFAAA7B2C86` | 0 |

### Ventana: Consolidación de Despachos

- **AD_WINDOW_ID:** `45A457CEDF8C4A40B320C55BE7201D3C`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `2D2D6E9ECAE04E889DC386BBE3F58E4B` | 0 |
| 20 | Detail by sales order line | `8E9D28826DF742589B47F74036C06BE1` | 1 |
| 50 | Accumulated | `889A4924F30C4B6C94CC38E4AE76CB03` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Accumulated (ventana: Consolidación de Despachos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 120 | Product | `M_Product_ID` | No | Sí | — |
| 130 | UOM | `C_Uom_ID` | No | Sí | — |
| 140 | Warehouse | `M_Warehouse_ID` | No | Sí | — |
| 150 | Consolidated Required | `Quantity` | No | Sí | — |
| 160 | Stock | `Stock` | No | Sí | — |
| 170 | Despatch | `Despatch` | No | No | — |
| 180 | Number_Boxes | `Number_Boxes` | No | Sí | — |
| 190 | Active | `Isactive` | No | No | — |

### Header (ventana: Configuración de Consolidación de Despachos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 100 | Inout Document Type | `Inout_Doctype_ID` | No | No | E518DD0EA49F4E71AE6601476D60378E |
| 500 | Invoice Document Type | `Invoice_Doctype_ID` | No | No | 6DAD580F4A3F47FA8CE97DE18FA6E597 |
| 510 | Payment Terms | `C_Paymentterm_ID` | No | No | — |
| 520 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 530 | Price List | `M_Pricelist_ID` | No | No | — |

### Detail by sales order line (ventana: Consolidación de Despachos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Sales Order | `C_Order_ID` | No | Sí | — |
| 110 | Order Reference | `Poreference` | No | Sí | — |
| 120 | Order Date | `Dateordered` | No | Sí | — |
| 130 | Scheduled Delivery Date | `Datepromised` | No | Sí | — |
| 140 | Warehouse | `M_Warehouse_ID` | No | Sí | — |
| 150 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 160 | Product | `M_Product_ID` | No | Sí | — |
| 170 | UOM | `C_Uom_ID` | No | Sí | — |
| 180 | Ordered Quantity | `Qtyordered` | No | Sí | — |
| 190 | Delivered Quantity | `Qtydelivered` | No | Sí | — |
| 200 | Invoiced Quantity | `Qtyinvoiced` | No | Sí | — |
| 210 | SuggestedDelivery | `SuggestedDelivery` | No | No | — |

### Header (ventana: Consolidación de Despachos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 1 | Updatestock | `Updatestock` | No | No | — |
| 2 | Accumulate | `Accumulate` | No | No | — |
| 3 | Load Pending Orders | `Loadlines` | No | No | — |
| 4 | Process | `Process` | No | No | — |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 100 | Document Type | `C_Doctype_ID` | No | No | — |
| 110 | Document No. | `Documentno` | No | Sí | — |
| 120 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 130 | Date | `Dispatch_Date` | No | No | — |
| 140 | Warehouse | `M_Warehouse_ID` | No | No | — |
| 150 | Storage Bin | `M_Locator_ID` | No | No | — |
| 160 | Description | `Description` | No | No | — |
| 170 | Goods Shipment | `M_Inout_ID` | No | Sí | — |
| 180 | Invoice | `C_Invoice_ID` | No | Sí | — |
| 190 | Document Status | `Docstatus` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo no incluye botones de procesos típicos, pero cuenta con funciones para manejar flujos de trabajo como la acumulación de líneas, gestionadas a través de las rutinas definidas en el código de Java. Las validaciones frecuentes incluyen comprobar el estado de las líneas previas a la acumulación y la autorización de los movimientos según las políticas de inventario de la organización. La generación de informes no es parte del flujo estándar del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.inventory.partial.out.movement.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| — | *(sin procesos de botón)* | — | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 0**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `ssipotm_accumulated_dsptch_ck` | the value cannot be less than the stock | the value cannot be less than the stock | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssipotm_CannotDeleteProcessedTransaction` | You cannot delete a processed transaction | You cannot delete a processed transaction | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssipotm_NoStockAvailable` | The amount entered exceeds the available stock | The amount entered exceeds the available stock | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssipotm_NoConfigAvailable` | No default settings were found to create the Delivery Note and Invoice | No default settings were found to create the Delivery Note and Invoice | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo implementa varias clases en Java, como 'SsipotmComponentProvider' y 'AccumulateActionHandler', que permiten la interacción con la interfaz de usuario y gestionan acciones específicas del sistema. Estas clases se encargan de proporcionar recursos y gestionar comportamientos dentro del módulo, al mismo tiempo que garantizan la integración con el framework de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.inventory.partial.out.movement`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SsipotmComponentProvider` | root | BaseComponentProvider | ComponentProvider / UI | `src/ec/com/sidesoft/inventory/partial/out/movement/SsipotmComponentProvider.java` |
| `AccumulateActionHandler` | ad_actions | BaseActionHandler | — | `src/ec/com/sidesoft/inventory/partial/out/movement/ad_actions/AccumulateActionHandler.java` |
| `LoadLinesActionHandler` | ad_actions | BaseActionHandler | — | `src/ec/com/sidesoft/inventory/partial/out/movement/ad_actions/LoadLinesActionHandler.java` |
| `ProcessActionHandler` | ad_actions | BaseActionHandler | Proceso / informe Java | `src/ec/com/sidesoft/inventory/partial/out/movement/ad_actions/ProcessActionHandler.java` |
| `UpdateStockActionHandler` | ad_actions | BaseActionHandler | — | `src/ec/com/sidesoft/inventory/partial/out/movement/ad_actions/UpdateStockActionHandler.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSIPOTM_ACCUMULATED_TRG` | `ssipotm_accumulated` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSIPOTM_ORDERLINE_TRG` | `ssipotm_orderline` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSIPOTM_PARTIALD_TRG` | `ssipotm_partial_dispatch` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Locator Partial Dispatch` | `m_warehouse_id = @m_warehouse_id@` |
| AD_VAL_RULE | — | `Doctype_Partial_Dispatch` | `c_doctype.AD_TABLE_ID IN (
SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(TABLENAME) = UPPER('ssipotm_partial_dispatch'))` |
| Función PL `ssipotm_accumulate` | — | invocación proceso | Delete old lines with product not in lines |
| Función PL `ssipotm_loadlines` | — | invocación proceso | AND o.m_warehouse_id=vRecord.m_warehouse_id |
| Función PL `ssipotm_process` | — | invocación proceso | Crea un Albaran (Cliente) en estado borrador; Generamos las lineas necesarias por la cantidad disponible; Crea la Factura (Cliente) en estado borrador |
| Función PL `ssipotm_update_stock` | — | invocación proceso | Delete old lines with product not in lines |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones de PL/pgSQL desempeñan un papel crucial en la gestión de la lógica de negocio del módulo, garantizando que las modificaciones en los despachos parciales se reflejen correctamente en la base de datos. Con funciones como 'ssipotm_accumulate' y 'ssipotm_loadlines', se realizan operaciones de acumulación y carga de líneas de manera eficiente, permitiendo un manejo efectivo de los datos en tiempo real.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSIPOTM_ACCUMULATED_TRG` | `ssipotm_accumulated` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSIPOTM_ACCUMULATED_TRG.xml` |
| `SSIPOTM_ORDERLINE_TRG` | `ssipotm_orderline` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSIPOTM_ORDERLINE_TRG.xml` |
| `SSIPOTM_PARTIALD_TRG` | `ssipotm_partial_dispatch` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSIPOTM_PARTIALD_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssipotm_accumulate` | — | Delete old lines with product not in lines | Delete old lines with product not in lines | `model/functions/SSIPOTM_ACCUMULATE.xml` |
| `ssipotm_loadlines` | — | AND o.m_warehouse_id=vRecord.m_warehouse_id | AND o.m_warehouse_id=vRecord.m_warehouse_id | `model/functions/SSIPOTM_LOADLINES.xml` |
| `ssipotm_process` | — | Crea un Albaran (Cliente) en estado borrador; Generamos las lineas necesarias por la cantidad disponible; Crea la Factura (Cliente) en estado borrador | Crea un Albaran (Cliente) en estado borrador; Generamos las lineas necesarias por la cantidad disponible; Crea la Factura (Cliente) en estado borrador | `model/functions/SSIPOTM_PROCESS.xml` |
| `ssipotm_update_stock` | — | Delete old lines with product not in lines | Delete old lines with product not in lines | `model/functions/SSIPOTM_UPDATE_STOCK.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/ec.com.sidesoft.inventory.partial.out.movement/js/partialDispatch.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.inventory.partial.out.movement`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | presente |
| `AD_WINDOW.xml` | presente |
| `OBUIAPP_PROCESS.xml` | presente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SSIPOTM`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSIPOTM` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.inventory.partial.out.movement` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Inventory Movement From Invoice
**Package:** `com.sidesoft.inventory.movement.frominvoice`

# Module overview — Sidesoft Inventory Movement From Invoice

## Functional

El módulo 'Sidesoft Inventory Movement From Invoice' está diseñado para gestionar el movimiento de inventario a partir de facturas, optimizando el proceso de contabilización y control de stock. Los actores principales incluyen usuarios de negocio encargados de la gestión de inventarios, así como personal de soporte que garantiza el funcionamiento adecuado de la aplicación. El alcance del módulo se centra en la integración y el tratamiento de datos relacionados con las facturas y el inventario, y depende de las versiones compatibles del núcleo del sistema y de una 'skin' específica para su correcta visualización.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/inventory/movement/frominvoice` |
| Web | `web/com.sidesoft.inventory.movement.frominvoice/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SINVMIN`

# Guía de chat — Sidesoft Inventory Movement From Invoice

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.inventory.movement.frominvoice`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)
- «¿Qué es la tabla sinvmin_square_bill?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar un movimiento de inventario a partir de una factura?
- ¿Qué debo hacer si encuentro un error en la factura cuadrada?
- ¿Cómo se gestionan las validaciones durante el registro de inventarios?
- ¿Dónde puedo ver el historial de movimientos de inventario?
- ¿Qué acciones están disponibles para completar un movimiento?
- ¿Cómo puedo retornar un movimiento ya registrado?
- ¿Cuáles son los triggers que afectan el módulo de inventario?
- ¿Cuál es la relación entre las facturas y los pedidos en el sistema?

# Domain — data model

## Functional

La entidad cabecera principal del módulo es 'sinvmin_square_bill', que representa las facturas cuadradas vinculadas a los movimientos de inventario. Aunque no hay etapas específicas definidas en el módulo, las relaciones entre las tablas de facturas ('c_invoiceline') y pedidos ('c_orderline') son clave para el funcionamiento del mismo. Los triggers activos, como 'SINVMIN_SQUAREBILL_INVL_TRG' y 'SINVMIN_SQUAREBILL_ORDER_TRG', son fundamentales para automatizar la lógica de negocio y asegurar la integridad de los datos durante el procesamiento de las facturas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sinvmin_square_bill` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sinvmin_square_bill` | sinvmin_square_bill | — | — | ad_client_id→ad_client; m_inoutline_id→m_inoutline; c_invoiceline_id→c_invoiceline; c_orderline_id→c_orderline; ad_org_id→ad_org (+2) | Detalle enlazado a ad_client, c_invoiceline, m_inoutline. | PK `sinvmin_sb_key`; Cols: c_orderline_id, m_inoutline_id, c_invoiceline_id, m_product_id, qty; `SINVMIN_SB_ISACTIVE`: ISACTIVE IN ('Y', 'N'); idx `SINVMIN_BILL_INOUTLN_IDX` (m_inoutline_id); idx `SINVMIN_BILL_INVLN_IDX` (c_invoiceline_id) (+2) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sinvmin_square_bill` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo presenta una única ventana llamada 'Facturas Cuadradas', donde los usuarios pueden acceder a la información y gestionar el movimiento de inventario. La interfaz de usuario está diseñada para facilitar la navegación entre los diferentes menús y opciones disponibles, permitiendo a los usuarios interactuar de manera eficiente con la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.inventory.movement.frominvoice.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Facturas Cuadradas | Square Bills |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Facturas Cuadradas | Square Bills | No |
| Pedidos pendientes de despacho o facturación | Orders pending dispatch or billing | No |
| Reporte Facturas de Venta Parcial sin Despacho | Report Partial Sales Invoices without Dispatch | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.inventory.movement.frominvoice.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Facturas Cuadradas

- **AD_WINDOW_ID:** `ED4A6A73C5E346E19085C2C75D97A984`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `B51704F3B6E74F28814E9AC9AC111CB0` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Header (ventana: Facturas Cuadradas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 100 | Sales Order Line | `C_OrderLine_ID` | No | No | — |
| 110 | Goods Shipment Line | `M_InoutLine_ID` | No | No | — |
| 120 | Invoice Line | `C_InvoiceLine_ID` | No | No | — |
| 130 | Product | `M_Product_ID` | No | No | — |
| 140 | Quantity | `Qty` | No | No | — |
| 150 | Transaction Date | `DateTrx` | No | No | — |
| 160 | Table | `AD_Table_ID` | No | No | — |
| 170 | Document No. | `—` | No | No | D83A40F101F24DFCB132E52201229EB2 |
| 180 | Name | `—` | No | No | D83A40F101F24DFCB132E52201229EB2 |
| 190 | Search Key | `—` | No | No | D83A40F101F24DFCB132E52201229EB2 |
| 200 | Document No. | `—` | No | No | 8FC0D0D2AE234A00ACBCF2F2EB06C72A |
| 210 | Name | `—` | No | No | 8FC0D0D2AE234A00ACBCF2F2EB06C72A |
| 220 | Search Key | `—` | No | No | 8FC0D0D2AE234A00ACBCF2F2EB06C72A |
| 230 | Document No. | `—` | No | No | A3926401E46047DFAF1D27EFC262C091 |
| 240 | Name | `—` | No | No | A3926401E46047DFAF1D27EFC262C091 |
| 250 | Search Key | `—` | No | No | A3926401E46047DFAF1D27EFC262C091 |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye funcionalidades para realizar acciones típicas como completar y retornar movimientos de inventario. Estas acciones suelen estar acompañadas de validaciones para asegurar que las facturas y los movimientos estén correctamente sincronizados. Aunque no se generan informes específicos dentro del módulo, las validaciones son esenciales para prevenir errores durante el proceso de registro de movimientos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.inventory.movement.frominvoice.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Pedidos pendientes de despacho o facturación | Orders pending dispatch or billing | Orders pending dispatch or billing | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Facturas de Venta Parcial sin Despacho | Report Partial Sales Invoices without Dispatch | PartialSalesInvoicesWithoutDispatch | *(OBUIAPP / manual)* | Report Partial Sales Invoices without Dispatch | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Pedidos pendientes de despacho o facturación | Orders pending dispatch or billing | Orders pending dispatch or billing | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Facturas de Venta Parcial sin Despacho | Report Partial Sales Invoices without Dispatch | PartialSalesInvoicesWithoutDispatch | *(OBUIAPP / manual)* | Report Partial Sales Invoices without Dispatch | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Pedidos pendientes de despacho o facturación | Orders pending dispatch or billing | — | — | — |
| Proceso / otro | Reporte Facturas de Venta Parcial sin Despacho | Report Partial Sales Invoices without Dispatch | — | Report Partial Sales Invoices without Dispatch | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 2**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **2**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo no incluye clases Java específicas, lo que indica que la lógica del mismo se maneja a través de otras tecnologías disponibles dentro del sistema Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.inventory.movement.frominvoice`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| *(sin clases Java en src/)* | — | — | — | — |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SINVMIN_SQUAREBILL_INVL_TRG` | `c_invoiceline` | before UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SINVMIN_SQUAREBILL_ORDER_TRG` | `c_orderline` | before UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `SINVMIN Logged User` | `AD_User.AD_User_ID = @#AD_User_ID@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y las funciones PL/pgSQL cumplen un rol crucial en el soporte del módulo, ya que automatizan procesos y garantizan que las reglas de negocio se apliquen correctamente al interactuar con las tablas de base de datos. La existencia de dos triggers asegura que las modificaciones en las líneas de facturación y pedidos se manejen sin inconvenientes, manteniendo la integridad de los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SINVMIN_SQUAREBILL_INVL_TRG` | `c_invoiceline` | before | UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SINVMIN_SQUAREBILL_INVL_TRG.xml` |
| `SINVMIN_SQUAREBILL_ORDER_TRG` | `c_orderline` | before | UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SINVMIN_SQUAREBILL_ORDER_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sinvmin_invoicestatus` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SINVMIN_INVOICESTATUS.xml` |
| `sinvmin_squarebill_inout` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SINVMIN_SQUAREBILL_INOUT.xml` |
| `sinvmin_squarebill_invoice` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SINVMIN_SQUAREBILL_INVOICE.xml` |
| `sinvmin_squarebill_order` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SINVMIN_SQUAREBILL_ORDER.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `com.sidesoft.inventory.movement.frominvoice`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | presente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SINVMIN`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SINVMIN` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.inventory.movement.frominvoice` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Orders pending dispatch or billing` — Pedidos pendientes de despacho o facturación
- `PartialSalesInvoicesWithoutDispatch` — Reporte Facturas de Venta Parcial sin Despacho

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Additional Information for Inventory Movements
**Package:** `ec.com.sidesoft.movement.addinformation`

# Module overview — Additional Information for Inventory Movements

## Functional

El módulo 'Additional Information for Inventory Movements' tiene como propósito proporcionar información adicional sobre los movimientos de inventario en el sistema Openbravo. Este módulo beneficia a los usuarios de negocio que gestionan inventarios, así como a los equipos de soporte y desarrollo que requieren entender y manipular los datos de movimiento de manera más efectiva. El alcance del módulo se limita a mejorar la gestión de los registros de inventario, optimizando su seguimiento y control. La principal dependencia de este módulo es el módulo Core de Openbravo, lo que asegura la integración adecuada con las funcionalidades básicas del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/movement/addinformation` |
| Web | `web/ec.com.sidesoft.movement.addinformation/` |

### Declared dependencies

- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SMVAI`

# Guía de chat — Additional Information for Inventory Movements

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.movement.addinformation`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo agregar información adicional a un movimiento de inventario?
- ¿Qué tablas se ven afectadas por el módulo de información adicional?
- ¿Dónde encuentro los registros de movimientos de inventario?
- ¿Existen validaciones automáticas al registrar un nuevo movimiento?
- ¿Cómo se corrige un movimiento de inventario erróneo?
- ¿Qué dependencia debe tener en cuenta el módulo para funcionar correctamente?
- ¿Este módulo afecta la rendimiento del ERP?
- ¿Hay alguna limitación en la cantidad de información adicional que se puede agregar?

# Domain — data model

## Functional

El módulo modifica las tablas 'M_INOUT', 'M_MOVEMENT' y 'M_MOVEMENTLINE', que son vitales para registrar las transacciones de inventario. Estas tablas actúan como la entidad cabecera y sus respectivas líneas, permitiendo almacenar detalles precisos de cada movimiento. Aunque no se indican etapas específicas en el inventario, se puede inferir que la gestión de movimientos incluye fases como la creación, modificación y consulta de datos. Debido a la falta de triggers y funciones PL definidos en el módulo, el enfoque se centra en la correcta utilización de las tablas modificadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| *(sin tablas en model/tables)* | — | — | — | — | — | — |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`M_INOUT`, `M_MOVEMENT`, `M_MOVEMENTLINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

No se definen ventanas específicas dentro de este módulo, por lo que los usuarios interactuarán principalmente a través de las ventanas existentes relacionadas al inventario en Openbravo, accediendo a las funciones del módulo desde estas interfaces. La navegación es fluida, siguiendo la estructura de menús estándar del ERP, donde los usuarios pueden acceder a los registros de movimientos de inventario y sus detalles.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.movement.addinformation.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.movement.addinformation.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `257`

- **AD_TAB_ID:** `257` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | End date of transport | `EM_Smvai_Enddateoftransport` | No | No | — |
| 260 | Custom code | `EM_Smvai_Customcode` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |
| 270 | Route | `EM_Smvai_Route` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |

### Pestaña `259`

- **AD_TAB_ID:** `259` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 50 | EM_Smvai_Enddateoftransport | `EM_Smvai_Enddateoftransport` | No | No | — |
| 55 | EM_Smvai_Route | `EM_Smvai_Route` | No | No | — |

### Pestaña `260`

- **AD_TAB_ID:** `260` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 65 | Received | `EM_Smvai_Isreceived` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que el módulo no incluye botones de proceso específicos ni informes predefinidos, se asume que las validaciones habituales son las que maneja Openbravo para los movimientos de inventario, como la verificación de cantidades y la validación de ubicaciones. Los usuarios tendrán que completar los registros de movimientos según los lineamientos establecidos en el sistema, así como potencialmente retornar o rechazar movimientos según su estado validado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.movement.addinformation.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| — | *(sin procesos de botón)* | — | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 0**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

No se han definido clases Java específicas para este módulo, por lo que las funcionalidades se limitan a las configuraciones y modificaciones de las tablas a nivel de base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.movement.addinformation`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| *(sin clases Java en src/)* | — | — | — | — |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| — | — | *(sin validaciones detectadas en modelo/Java)* | — |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Aunque no hay triggers o funciones PL asociadas específicamente a este módulo, las modificaciones en las tablas claves permiten que el soporte y el mantenimiento del sistema se realicen de manera más eficiente, ya que estas tablas permiten la integración de la información adicional sin necesidad de complexas configuraciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| *(sin triggers)* | — | — | — | — | — |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| *(sin funciones en model/functions)* | — | — | — | — |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.movement.addinformation`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SMVAI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SMVAI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.movement.addinformation` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Movements Consults
**Package:** `ec.com.sidesoft.movements.consults`

# Module overview — Sidesoft Movements Consults

## Functional

El módulo 'Sidesoft Movements Consults' tiene como propósito facilitar la consulta de los movimientos de inventario dentro del sistema Openbravo ERP. Este módulo está diseñado para ser utilizado principalmente por usuarios de negocio que necesitan acceder a información sobre los movimientos de inventario, así como por el personal de soporte en el nivel 2 para resolver incidencias relacionadas. La implementación de este módulo depende de la compatibilidad con la versión del '2.50 to 3.00 Compatibility Skin' y del 'Openbravo 3.0 Framework'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/movements/consults` |
| Web | `web/ec.com.sidesoft.movements.consults/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSMVCL`

# Guía de chat — Sidesoft Movements Consults

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.movements.consults`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo consultar los movimientos de inventario?
- ¿Qué información se muestra en la pantalla de movimientos de inventario?
- ¿Puedo filtrar los movimientos por fecha?
- ¿Existen opciones para exportar los datos consultados?
- ¿Cómo puedo acceder al módulo de consulta de movimientos?
- ¿Que hacer si no aparece información en la consulta?
- ¿Hay reportes disponibles para imprimir después de realizar una consulta?
- ¿Cómo se asegura la precisión de los movimientos mostrados?

# Domain — data model

## Functional

El módulo se estructura en torno a una entidad central que permite visualizar los movimientos de inventario. No se han definido tablas físicas específicas en este módulo, lo que implica que la consulta se efectúa sobre las tablas existentes en el sistema Openbravo, siguiendo las convenciones estándar. No hay triggers ni funciones PL asociados directamente a este módulo, lo que sugiere que las validaciones y procesos de negocio se manejan a través de las funcionalidades integradas del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| *(sin tablas en model/tables)* | — | — | — | — | — | — |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación en el módulo se realiza a través de la ventana denominada 'Movimientos de inventario'. Esta pantalla ofrece una interfaz amigable donde los usuarios pueden acceder a los datos de movimientos, facilitando la búsqueda y visualización de la información relevante de manera directa.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.movements.consults.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Movimientos de inventario | Inventory movements |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Movimientos de inventario | Inventory movements | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.movements.consults.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Movimientos de inventario

- **AD_WINDOW_ID:** `D4C19DB63840454A8DE299F30766F2AF`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `329` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Header (ventana: Movimientos de inventario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 15 | Product | `—` | No | No | — |
| 20 | Attribute Set Value | `—` | No | No | — |
| 30 | Storage Bin | `—` | No | No | — |
| 40 | Movement Quantity | `—` | No | No | — |
| 50 | Movement Date | `—` | No | No | — |
| 55 | Transaction Process Date | `—` | No | No | — |
| 60 | Movement Type | `—` | No | No | — |
| 70 | Línea Albarán/Albarán (Proveedor) | `—` | No | No | — |
| 80 | Physical Inventory Line | `—` | No | No | — |
| 90 | Movement Line | `—` | No | No | — |
| 150 | Is Cost Calculated | `—` | No | No | — |
| 160 | Costing Status | `—` | No | Sí | — |
| 170 | Coste Original Trx | `—` | No | No | — |
| 172 | Total Cost | `—` | No | Sí | — |
| 174 | Unit cost | `—` | No | No | — |
| 180 | Is Cost Permanent | `—` | No | No | — |
| 200 | Currency | `—` | No | No | — |
| — | Costing Algorithm | `—` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Aunque no se han definido botones o procesos específicos dentro de este módulo, la funcionalidad permite completar consultas sobre los movimientos de inventario. Los informes y validaciones son gestionados a través de las características generales del sistema Openbravo, lo que incluye filtrados avanzados y visualizaciones específicas de los datos de inventario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.movements.consults.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| — | *(sin procesos de botón)* | — | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 0**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

No se identificado uso de Java en este módulo, lo que indica que su funcionalidad se basa exclusivamente en las capacidades nativas del sistema Openbravo ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.movements.consults`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| *(sin clases Java en src/)* | — | — | — | — |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| — | — | *(sin validaciones detectadas en modelo/Java)* | — |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL no están implementados en este módulo, lo que simplifica la arquitectura del mismo, permitiendo una interacción más sencilla con el resto del ERP. Sin embargo, el soporte técnico debe estar atento a la integración de datos y la consistencia de la información a medida que los usuarios utilizan el módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| *(sin triggers)* | — | — | — | — | — |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| *(sin funciones en model/functions)* | — | — | — | — |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.movements.consults`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | presente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SSMVCL`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSMVCL` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.movements.consults` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Adjustment Inventory PDV
**Package:** `ec.com.sidesoft.localization.adjustment.inventory.pdv`

# Module overview — Adjustment Inventory PDV

## Functional

El módulo 'Adjustment Inventory PDV' se utiliza para gestionar ajustes en el inventario en puntos de venta (PDV). Su principal propósito es facilitar el control y la autorización de variaciones en el inventario. Los actores principales son los usuarios de negocio que realizan ajustes y supervisores que autorizan estas transacciones. El alcance del módulo se limita a la gestión de ajustes de inventario, y depende de la correcta integración con otras funciones del sistema Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/adjustment/inventory/pdv` |
| Web | `web/ec.com.sidesoft.localization.adjustment.inventory.pdv/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**1.0.1** (from `AD_MODULE.xml`).

### DB prefix

`SSIPDV`

# Guía de chat — Adjustment Inventory PDV

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.adjustment.inventory.pdv`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)
- «¿Qué es la tabla ssipdv_doctype?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo solicitar un ajuste de inventario?
- ¿Qué pasos debo seguir para autorizar un ajuste?
- ¿Dónde se registran los ajustes de inventario realizados?
- ¿Qué sucede si un ajuste es rechazado por el supervisor?
- ¿Puedo revertir un ajuste de inventario ya confirmado?
- ¿Cómo verificar el estado de un ajuste enviado para autorización?
- ¿Qué información necesito para realizar un ajuste de inventario?
- ¿Hay algún informe que pueda consultar sobre ajustes de inventario?

# Domain — data model

## Functional

Este módulo cuenta con una entidad cabecera que es la tabla 'SSIPDV_DOCTYPE', la cual almacena información relativa al tipo de documento para ajustes de inventario. La tabla 'M_INVENTORY' está vinculada, la cual se modifica en el proceso de ajuste. Se implementa un trigger llamado 'SSIPDV_VALIDINVENTORY_TRG' en la tabla de inventario que tiene la función de validar la autorización de transacciones, generando excepciones en caso de datos incorrectos. Esta interacción garantiza la integridad de los datos de inventario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssipdv_doctype` |
| `ssipdv_warehouse` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssipdv_doctype` | ssipdv_doctype | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype; ad_user_id→ad_user | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `ssipdv_doctype_key`; Cols: c_doctype_id, ad_user_id; `SSIPDV_DOCTYPE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssipdv_warehouse` | ssipdv_warehouse | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_user_id→ad_user; m_warehouse_id→m_warehouse | Detalle enlazado a ad_client, ad_org, ad_user. | PK `ssipdv_wh_key`; Cols: m_warehouse_id, ad_user_id; `SSIPDV_WH_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssipdv_doctype` |
| `ssipdv_warehouse` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`M_INVENTORY`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no presenta ventanas específicas en la interfaz de usuario, dado que está diseñado para ser integrado dentro del flujo existente de Openbravo. La navegación se realiza a través de menú de funciones ya definidas, donde los usuarios pueden acceder a los procesos de ajuste de inventario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.adjustment.inventory.pdv.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.adjustment.inventory.pdv.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Warehouse

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Warehouse | `M_Warehouse_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |

### Pestaña `255`

- **AD_TAB_ID:** `255` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 27 | Authorization Key | `EM_Ssipdv_Key_Auth` | No | No | — |
| 2080 | Generate Key | `EM_Ssipdv_Generate_Key` | No | No | — |
| 2100 | Status Key | `EM_Ssipdv_Status_Key` | No | Sí | — |

### Document Type

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un único proceso que permite realizar ajustes y requiere autorización de un supervisor para su correcta ejecución. Las validaciones frecuentes implican la verificación del estado de autorización y la condición del inventario. Generalmente, los botones incluidos en este módulo permiten completar el ajuste, retornarlo para correcciones o rechazarlo si no cumple con los requisitos establecidos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.adjustment.inventory.pdv.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar Clave | Generate Key | Generate Key | Java `SendEmailSupervisorAuth` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `M_Inventory_ID` | `src/ec/com/sidesoft/localization/adjustment/inventory/pdv/ad_process/SendEmailSupervisorAuth.java` |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar Clave | `SendEmailSupervisorAuth` | Proceso Java (toolbar/background) | `M_Inventory_ID` | — | `src/ec/com/sidesoft/localization/adjustment/inventory/pdv/ad_process/SendEmailSupervisorAuth.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar Clave | Generate Key | Generate Key | Java `SendEmailSupervisorAuth` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `M_Inventory_ID` | `src/ec/com/sidesoft/localization/adjustment/inventory/pdv/ad_process/SendEmailSupervisorAuth.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar Clave | Generate Key | Java `SendEmailSupervisorAuth` | Proceso Openbravo registro `M_Inventory_ID` | Proceso Openbravo registro `M_Inventory_ID` |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 0**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye una clase Java llamada 'SendEmailSupervisorAuth', que es responsable de enviar correos electrónicos a los supervisores para la autorización de ajustes de inventario. Este proceso asegura la comunicación efectiva entre los usuarios de negocio y sus supervisores durante la gestión de transacciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.adjustment.inventory.pdv`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SendEmailSupervisorAuth` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/localization/adjustment/inventory/pdv/ad_process/SendEmailSupervisorAuth.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSIPDV_VALIDINVENTORY_TRG` | `m_inventory` | before UPDATE | raise exception '%' , 'error: ' || v_Code_Authorization || ' - status: ' || v_statusKey || ' - Auth: ' || p_Authorization_code;; Almacena el minuto actual con el minuto original |
| AD_VAL_RULE | — | `Ssipdv_ValidWarehouse` | `M_WAREHOUSE.M_WAREHOUSE_ID IN (
SELECT M_WAREHOUSE_ID FROM SSIPDV_WAREHOUSE WHERE AD_CLIENT_ID = @#AD_CLIENT_ID@    AND ` |
| AD_VAL_RULE | — | `Ssipdv_Locator` | `M_LOCATOR.M_LOCATOR_ID IN (select m_locator_id from M_locator ml
join m_warehouse mw on mw.m_locator_id = mw.m_locator_i` |
| AD_VAL_RULE | — | `Ssipdv_ValidDoctype` | `C_DocType.DocBaseType IN ('MMI')` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL en este módulo son fundamentales para la operación de ajustes de inventario. El trigger 'SSIPDV_VALIDINVENTORY_TRG' impide que se realicen transacciones inválidas, mientras que las funciones PL se utilizan para gestionar procesos relacionados como la creación de registros de ajuste y la verificación de la autorización.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSIPDV_VALIDINVENTORY_TRG` | `m_inventory` | before | UPDATE | raise exception '%' , 'error: ' || v_Code_Authorization || ' - status: ' || v_statusKey || ' - Auth: ' || p_Authorization_code;; Almacena el minuto actual con el minuto original | `model/triggers/SSIPDV_VALIDINVENTORY_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssipdv_inventory_listcreate` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSIPDV_INVENTORY_LISTCREATE.xml` |
| `ssipdv_inventory_listupdate` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSIPDV_INVENTORY_LISTUPDATE.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Generar Clave | `Generate Key` | Botón (Java) | Java `SendEmailSupervisorAuth` | N | Proceso Openbravo registro `M_Inventory_ID` |

**Total acciones documentadas (extract):** **1** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.localization.adjustment.inventory.pdv`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SSIPDV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSIPDV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.adjustment.inventory.pdv` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Generate Key` — Generar Clave

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Product Balance
**Package:** `ec.com.sidesoft.product.balance`

# Module overview — Product Balance

## Functional

El módulo 'Product Balance' tiene como propósito principal gestionar el balance de productos en el sistema Openbravo, facilitando a los usuarios de negocio la supervisión y control de movimientos de productos en inventarios. Los actores clave incluyen a los responsables de inventario, gerentes de logística y personal de soporte técnico. Este módulo es dependiente del standard de Openbravo 3.0 y otras extensiones, permitiendo una integración fluida con el resto del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/product/balance` |
| Web | `web/ec.com.sidesoft.product.balance/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`ECSPB`

# Guía de chat — Product Balance

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.product.balance`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)
- «¿Qué es la tabla ecspb_scalehardwarem?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo revisar el balance actual de un producto?
- ¿Qué pasos debo seguir para registrar un nuevo movimiento de inventario?
- ¿Cómo puedo buscar información de un producto utilizando su código?
- ¿Qué sucede si un producto no aparece al intentar buscarlo?
- ¿Cómo se gestionan las transacciones que han sido rechazadas?
- ¿Dónde puedo encontrar informes sobre las transacciones de productos?
- ¿Qué datos necesito proporcionar al cargar información sobre un movimiento?
- ¿Cómo se determina si un movimiento necesita ser confirmado?

# Domain — data model

## Functional

El modelo de datos del módulo se basa en la entidad principal 'ecspb_scalehardwarem', que comunica con las tablas modificadas 'M_INOUT', 'M_INOUTLINE', 'M_MOVEMENT', y 'M_MOVEMENTLINE'. Cada una de estas tablas tiene un rol importante en registrar los movimientos internos y de envío de productos, permitiendo un seguimiento detallado de cada transacción. Este módulo no presenta triggers ni funciones PL específicas, lo que simplifica su interacción con otros componentes del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ecspb_scalehardwarem` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ecspb_scalehardwarem` | ecspb_ScaleHardwareM | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ecspb_pk_key`; Cols: table_name, url; `ECSPB_CK_ACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ecspb_ScaleHardwareM` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`M_INOUT`, `M_INOUTLINE`, `M_MOVEMENT`, `M_MOVEMENTLINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

En la interfaz de usuario, se navega a través de la ventana 'Hardware Manager Service', donde los usuarios pueden acceder a las funcionalidades clave del módulo. La interfaz está diseñada para ser intuitiva, permitiendo a los usuarios realizar consultas sobre el balance de productos de manera eficiente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.product.balance.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Hardware Manager Service | Hardware Manager Service |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Hardware Manager Service | Hardware Manager Service | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.product.balance.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Hardware Manager Service

- **AD_WINDOW_ID:** `CB60CA1390574E57B4BDAF18BE061A54`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Hardware Manager Service | `E280BA54BE53419A94F0E7ADC4F0483A` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `259`

- **AD_TAB_ID:** `259` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2170 | EM_Ecspb_Confirmations | `EM_Ecspb_Confirmations` | No | No | — |

### Pestaña `296`

- **AD_TAB_ID:** `296` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2080 | EM_Ecspb_Confirmations | `EM_Ecspb_Confirmations` | No | No | — |

### Hardware Manager Service (ventana: Hardware Manager Service)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Table_Name | `Table_Name` | No | No | — |
| 40 | URL | `Url` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dentro del módulo, la interacción típica incluye la búsqueda y carga de información de productos mediante botones de acción. Si bien no se especifican botones de proceso destacados, se espera que los usuarios puedan completar, retornar o rechazar movimientos de productos a través de interacciones que actualizan el estado de las transacciones. Los informes personalizados en el módulo aún no están definidos, pero se anticipa que puedan ser integrados en futuras versiones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.product.balance.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| — | *(sin procesos de botón)* | — | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 0**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye varias clases Java que permiten manejar acciones específicas, como la carga de información sobre productos y movimientos. Estas clases son fundamentales para la funcionalidad del módulo, ya que gestionan la lógica detrás de las interacciones del usuario y la consulta de datos en la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.product.balance`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `LoadCombo` | ad_actionbutton | BaseActionHandler | — | `src/ec/com/sidesoft/product/balance/ad_actionbutton/LoadCombo.java` |
| `LoadMovement` | ad_actionbutton | BaseActionHandler | — | `src/ec/com/sidesoft/product/balance/ad_actionbutton/LoadMovement.java` |
| `LoadProductInfo` | ad_actionbutton | BaseActionHandler | — | `src/ec/com/sidesoft/product/balance/ad_actionbutton/LoadProductInfo.java` |
| `SearchProductLine` | ad_actionbutton | BaseActionHandler | — | `src/ec/com/sidesoft/product/balance/ad_actionbutton/SearchProductLine.java` |
| `Transform` | ad_actionbutton | BaseActionHandler | — | `src/ec/com/sidesoft/product/balance/ad_actionbutton/Transform.java` |
| `ValidateStock` | ad_actionbutton | BaseActionHandler | — | `src/ec/com/sidesoft/product/balance/ad_actionbutton/ValidateStock.java` |
| `BalanceOfProducts` | ad_process | BaseActionHandler | Proceso / informe Java | `src/ec/com/sidesoft/product/balance/ad_process/BalanceOfProducts.java` |
| `MovementBalanceOfProduct` | ad_process | BaseActionHandler | Proceso / informe Java | `src/ec/com/sidesoft/product/balance/ad_process/MovementBalanceOfProduct.java` |
| `MovementBalanceOfProducts` | ad_process | BaseActionHandler | Proceso / informe Java | `src/ec/com/sidesoft/product/balance/ad_process/MovementBalanceOfProducts.java` |
| `ComponentsProvider` | master | BaseComponentProvider | ComponentProvider / UI | `src/ec/com/sidesoft/product/balance/master/ComponentsProvider.java` |
| `ApiBalance` | services | BaseActionHandler | — | `src/ec/com/sidesoft/product/balance/services/ApiBalance.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| — | — | *(sin validaciones detectadas en modelo/Java)* | — |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El papel de los triggers y funciones PL es mínimo en este módulo ya que no se cuenta con triggers per se ni funciones PL en su estructura. Esto podría implicar un enfoque más simplificado hacia las validaciones y cálculos, favoreciendo la estabilidad y rapidez en el acceso a los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| *(sin triggers)* | — | — | — | — | — |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| *(sin funciones en model/functions)* | — | — | — | — |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/ec.com.sidesoft.product.balance/js/formBalanceProducts.js` |
| `web/ec.com.sidesoft.product.balance/js/formBalanceProductsForMovements.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.product.balance`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | presente |
| `OBUIAPP_PROCESS.xml` | presente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `ECSPB`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `ECSPB` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.product.balance` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Product Information in Lines
**Package:** `ec.com.sidesoft.product.linesinfo`

# Module overview — Sidesoft Product Information in Lines

## Functional

El módulo 'Sidesoft Product Information in Lines' tiene como propósito principal gestionar y optimizar la información relacionada con productos a nivel de línea en el sistema ERP Openbravo. Los actores involucrados incluyen usuarios de negocio que manejan el inventario y personal de soporte técnico que asegura el buen funcionamiento del módulo. Este módulo es relevante para empresas que requieren una gestión actualizada y precisa de la información de productos en sus procesos de venta y adquisición. Su implementación depende de la compatibilidad con la skin de versiones entre 2.50 y 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/product/linesinfo` |
| Web | `web/ec.com.sidesoft.product.linesinfo/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPRLI`

# Guía de chat — Sidesoft Product Information in Lines

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.product.linesinfo`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)

## Preguntas ejemplo (IA)

- ¿Cómo se actualiza la información de un producto en el sistema?
- ¿Qué tablas se ven afectadas cuando modifico una línea de factura?
- ¿Cómo se asegura la integridad de los datos al cambiar información en órdenes?
- ¿Qué sucede si hay un error al actualizar las líneas de inventario?
- ¿Qué procesos internos se ejecutan al añadir o eliminar productos?
- ¿Hay reportes disponibles para ver la actividad de líneas de productos?
- ¿Cómo puedo verificar si un trigger ha funcionado correctamente?
- ¿Qué impacto tiene este módulo en la gestión de inventarios?

# Domain — data model

## Functional

El módulo afecta principalmente a varias tablas clave que son fundamentales para la gestión de líneas de facturación, órdenes, movimientos e inventarios. Las entidades cabecera incluyen 'C_INVOICELINE', 'C_ORDERLINE', 'M_CA_INVENTORYAMTLINE', 'M_INOUTLINE', 'M_MOVEMENTLINE' y 'M_REQUISITIONLINE'. Los triggers asociados garantizan la actualización automática de identificadores y la integridad de los datos en cada una de estas tablas. Estos triggers son esenciales para asegurar que cualquier cambio en las líneas de productos se refleje adecuadamente en el sistema y mantenga la consistencia de la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| *(sin tablas en model/tables)* | — | — | — | — | — | — |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_INVOICELINE`, `C_ORDERLINE`, `M_CA_INVENTORYAMTLINE`, `M_INOUTLINE`, `M_MOVEMENTLINE`, `M_REQUISITIONLINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no presenta ventanas específicas en la interfaz de usuario, dado que se enfoca en la ejecución de triggers y la manipulación de información en las tablas mencionadas. La navegación para los usuarios ocurre principalmente a través de formularios y procesos establecidos en las tablas de inventario, facturación y órdenes existentes en el sistema ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `1004400002`

- **AD_TAB_ID:** `1004400002` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 31 | Identifier | `EM_Sprli_Identifier` | No | Sí | — |

### Pestaña `187`

- **AD_TAB_ID:** `187` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 21 | Identifier | `EM_Sprli_Identifier` | No | Sí | — |

### Pestaña `258`

- **AD_TAB_ID:** `258` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 21 | Identifier | `EM_Sprli_Identifier` | No | Sí | — |

### Pestaña `260`

- **AD_TAB_ID:** `260` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 21 | Identifier | `EM_Sprli_Identifier` | No | Sí | — |

### Pestaña `270`

- **AD_TAB_ID:** `270` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 21 | Identifier | `EM_Sprli_Identifier` | No | Sí | — |

### Pestaña `293`

- **AD_TAB_ID:** `293` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 21 | Identifier | `EM_Sprli_Identifier` | No | Sí | — |

### Pestaña `297`

- **AD_TAB_ID:** `297` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 21 | Identifier | `EM_Sprli_Identifier` | No | Sí | — |

### Pestaña `800251`

- **AD_TAB_ID:** `800251` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 31 | Identifier | `EM_Sprli_Identifier` | No | Sí | — |

### Pestaña `BD883B355F1B448A9CB6BD472600EB2D`

- **AD_TAB_ID:** `BD883B355F1B448A9CB6BD472600EB2D` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 41 | Identifier | `EM_Sprli_Identifier` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Aunque el módulo no cuenta con botones de proceso definidos, los usuarios pueden esperar complejizar la gestión de datos a través de la actualización continua de línea de productos mediante los triggers. La ausencia de informes predefinidos sugiere que el enfoque está más centrado en el soporte de la integridad de los datos que en la generación de información analítica. Las validaciones frecuentes relacionadas con la modificación de las tablas aseguran que los datos de las líneas de producto se mantengan actualizados y precisos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| — | *(sin procesos de botón)* | — | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 0**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo no incluye componentes Java, lo que indica que su funcionalidad principal se centra en las rutinas PL/pgSQL para la manipulación y actualización de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.product.linesinfo`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| *(sin clases Java en src/)* | — | — | — | — |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SPRLI_UPDATEIDENTINOUT_TRG` | `m_inoutline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPRLI_UPDATEIDENTINVENT_TRG` | `m_ca_inventoryamtline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPRLI_UPDATEIDENTINV_TRG` | `c_invoiceline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPRLI_UPDATEIDENTMOVEM_TRG` | `m_movementline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPRLI_UPDATEIDENTORDER_TRG` | `c_orderline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPRLI_UPDATEIDENTREQUI_TRG` | `m_requisitionline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers del módulo desempeñan un papel crítico en el mantenimiento automático de la base de datos, ejecutando rutinas específicas en respuesta a cambios en las tablas afectadas. Estas rutinas se escriben en PL/pgSQL y permiten que las modificaciones realizadas en las líneas de productos se gestionen sin intervención manual, mejorando así la eficiencia y la consistencia de la información almacenada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SPRLI_UPDATEIDENTINV_TRG` | `c_invoiceline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPRLI_UPDATEIDENTINV_TRG.xml` |
| `SPRLI_UPDATEIDENTORDER_TRG` | `c_orderline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPRLI_UPDATEIDENTORDER_TRG.xml` |
| `SPRLI_UPDATEIDENTINVENT_TRG` | `m_ca_inventoryamtline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPRLI_UPDATEIDENTINVENT_TRG.xml` |
| `SPRLI_UPDATEIDENTINOUT_TRG` | `m_inoutline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPRLI_UPDATEIDENTINOUT_TRG.xml` |
| `SPRLI_UPDATEIDENTMOVEM_TRG` | `m_movementline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPRLI_UPDATEIDENTMOVEM_TRG.xml` |
| `SPRLI_UPDATEIDENTREQUI_TRG` | `m_requisitionline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPRLI_UPDATEIDENTREQUI_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| *(sin funciones en model/functions)* | — | — | — | — |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.product.linesinfo`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | no |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SPRLI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPRLI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.product.linesinfo` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Warehouse Product
**Package:** `ec.com.sidesoft.warehouse.product`

# Module overview — Sidesoft Warehouse Product

## Functional

El módulo Sidesoft Warehouse Product está diseñado para optimizar la gestión de productos en almacenes dentro del ERP Openbravo. Su propósito es proporcionar herramientas que faciliten el seguimiento y control de los movimientos de productos, permitiendo a los actores involucrados, como usuarios de negocio y personal de soporte, gestionar eficientemente el inventario. Este módulo es una extensión del sistema existente y depende de la compatibilidad con la versión 2.50 a 3.00 del 'Compatibility Skin'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/warehouse/product` |
| Web | `web/ec.com.sidesoft.warehouse.product/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SWHP`

# Guía de chat — Sidesoft Warehouse Product

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.warehouse.product`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)
- «¿Qué es la tabla swhp_wh_product?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo agregar un nuevo producto al almacén?
- ¿Qué pasos debo seguir para registrar un movimiento de productos?
- ¿Cómo puedo validar la información de un producto existente?
- ¿Existen restricciones al mover productos entre almacenes?
- ¿Qué sucede si un movimiento de producto es rechazado?
- ¿Cómo puedo acceder a mis productos desde el módulo?
- ¿Qué hacer si encuentro un error al registrar un movimiento?
- ¿Se pueden generar informes sobre el estado del inventario?

# Domain — data model

## Functional

La entidad central de este módulo es la tabla 'swhp_wh_product', que almacena información relevante sobre productos de almacén. Las interacciones se dan a través de procesos que afectan tablas como 'M_INOUT', 'M_MOVEMENT' y 'M_WAREHOUSE', permitiendo un flujo continuo desde la entrada y salida de mercancías hasta el movimiento dentro del almacén. Se ha implementado triggers clave como 'SWHP_INSERT_MOVEMENTLINES_TRG' para gestionar automáticamente la inserción de líneas de movimiento y 'SWHP_SUGGESTION_VALIDATE' para asegurar la validez de los datos introducidos en la tabla de productos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `swhp_wh_product` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `swhp_wh_product` | swhp_wh_product | `SWHP_SUGGESTION_VALIDATE` | `SWHP_WH_PRODUCT_UNIQ` (m_locator_id, m_product_id) | ad_client_id→ad_client; m_locator_id→m_locator; ad_org_id→ad_org; m_product_id→m_product | Detalle enlazado a ad_client, ad_org, m_locator. Validado por trigger(s): SWHP_SUGGESTION_VALIDATE. | PK `swhp_wh_product_key`; Cols: m_product_id, m_locator_id; `SWHP_WH_PRODUCT_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `swhp_product_stockDetail_v` |
| `swhp_wh_product` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`M_INOUT`, `M_MOVEMENT`, `M_WAREHOUSE`

### Views

`SWHP_PRODUCT_STOCKDETAIL_V`

# Functional — windows and menus

## Functional

La navegación a través del módulo Sidesoft Warehouse Product se realiza mediante la interfaz de usuario de Openbravo, donde se pueden acceder a diferentes funciones a través de menús desplegables. Los usuarios pueden interactuar con las vistas disponibles para gestionar los productos y sus movimientos, aunque no se han definido ventanas específicas dentro del módulo más allá de las funcionalidades básicas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.warehouse.product.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Ubicación productos | Product Locations | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.warehouse.product.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `177`

- **AD_TAB_ID:** `177` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 150 | EM_Swhp_Transit | `EM_Swhp_Transit` | No | No | — |

### Pestaña `257`

- **AD_TAB_ID:** `257` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2120 | Assignment Locator | `EM_Swhp_Assignment_Locator` | No | No | — |

### Pestaña `259`

- **AD_TAB_ID:** `259` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 60 | EM_Swhp_M_Locator_ID | `EM_Swhp_M_Locator_ID` | No | No | — |
| 70 | Update MovementLines | `EM_Swhp_Ubicaciongeneral` | No | No | — |

### Stock Detalled

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Product | `M_Product_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Quantity on Hand | `Qtyonhand` | No | No | — |
| 110 | Storage Bin | `M_Locator_ID` | No | No | — |
| 130 | Warehouse | `M_Warehouse_ID` | No | No | — |
| 140 | Reserved Qty | `Reservedqty` | No | No | — |
| 150 | Organization | `Name` | No | No | — |
| 160 | Allocated Quantity | `Allocatedqty` | No | No | — |

### Pestaña `296`

- **AD_TAB_ID:** `296` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2060 | Assignment Locator | `EM_Swhp_Assignment_Locator` | No | No | — |

### Product Suggestion

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Product | `M_Product_ID` | No | No | — |

### Pestaña `30576C6ABD12419F9D19D497216FC9B8`

- **AD_TAB_ID:** `30576C6ABD12419F9D19D497216FC9B8` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2070 | Assignment Locator | `EM_Swhp_Assignment_Locator` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo incluye tres botones principales de proceso que facilitan la operación de logística: completar, retornar y rechazar. Estas acciones permiten a los usuarios gestionar el flujo de productos en función de las necesidades del negocio. Aunque no se han definido informes específicos en el módulo, se prevé que las validaciones frecuentes se centralicen en el uso de los triggers y funciones PL para mantener la integridad y validez de la información en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.warehouse.product.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Actualizar Lineas de Movimientos | Update MovementLines | EM_Swhp_Ubicaciongeneral | `swhp_update_movLines` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Asignar Ubicación | Assignment Locator | swhp_assignment_locator | `swhp_assignment_locator` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Ubicación productos | Product Locations | Swhp_Product_Locations | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Actualizar Lineas de Movimientos | Update MovementLines | EM_Swhp_Ubicaciongeneral | `swhp_update_movLines` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Asignar Ubicación | Assignment Locator | swhp_assignment_locator | `swhp_assignment_locator` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Ubicación productos | Product Locations | Swhp_Product_Locations | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Actualizar Lineas de Movimientos | Update MovementLines | PL `swhp_update_movLines` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Asignar Ubicación | Assignment Locator | PL `swhp_assignment_locator` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Ubicación productos | Product Locations | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 3**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **3**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Swhp_NotExist_Location` | Product(s) without location configured in the line(s): | Product(s) without location configured in the line(s): | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Swhp_MoreThanOne_Location` | Products configured in more than one location on the lines: | Products configured in more than one location on the lines: | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

No se utilizan clases Java dentro de este módulo, lo que implica que su funcionalidad está basada puramente en la configuración de base de datos y lógica de PL/pgSQL.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.warehouse.product`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| *(sin clases Java en src/)* | — | — | — | — |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SWHP_INSERT_MOVEMENTLINES_TRG` | `m_movementline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SWHP_SUGGESTION_VALIDATE` | `swhp_wh_product` | before INSERT | Validación reutilizable de campos. |
| AD_VAL_RULE | — | `v_locators` | `m_locator.m_locator_id in (select l.M_locator_Id as m_locatorto_id from M_Warehouse w
left join m_locator l on w.M_Wareh` |
| AD_VAL_RULE | — | `Locators` | `m_locator.m_locator_id in (select l.M_locator_Id as m_locatorto_id from M_Warehouse w
left join m_locator l on w.M_Wareh` |
| AD_VAL_RULE | — | `Swhp_User_id - Log` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers en el módulo Sidesoft Warehouse Product juegan un papel crucial para el soporte al instante de realizar cambios en la base de datos. Las funciones PL proporcionan lógica adicional que asegura que los procesos de movimiento y validación de los productos se ejecuten correctamente, ayudando a mantener la coherencia de los datos en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SWHP_INSERT_MOVEMENTLINES_TRG` | `m_movementline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SWHP_INSERT_MOVEMENTLINES_TRG.xml` |
| `SWHP_SUGGESTION_VALIDATE` | `swhp_wh_product` | before | INSERT | Validación reutilizable de campos. | `model/triggers/SWHP_SUGGESTION_VALIDATE.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `swhp_assignment_locator` | Asignar Ubicación | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SWHP_ASSIGNMENT_LOCATOR.xml` |
| `swhp_assignment_locator_mvmnt` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SWHP_ASSIGNMENT_LOCATOR_MVMNT.xml` |
| `swhp_update_movlines` | Actualizar Lineas de Movimientos | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SWHP_UPDATE_MOVLINES.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Actualizar Lineas de Movimientos | `EM_Swhp_Ubicaciongeneral` | Botón (PL/pgSQL) | PL `swhp_update_movLines` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 2 | Asignar Ubicación | `swhp_assignment_locator` | Botón (PL/pgSQL) | PL `swhp_assignment_locator` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

**Total acciones documentadas (extract):** **2** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.warehouse.product`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | presente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SWHP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SWHP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.warehouse.product` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `EM_Swhp_Ubicaciongeneral` — Actualizar Lineas de Movimientos
- `swhp_assignment_locator` — Asignar Ubicación
- `Swhp_Product_Locations` — Ubicación productos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Stock Reports
**Package:** `ec.com.sidesoft.stock.reports`

# Module overview — Sidesoft Stock Reports

## Functional

El módulo Sidesoft Stock Reports está diseñado para ofrecer informes detallados sobre el estado del stock de productos. Los actores principales son los usuarios de negocio que necesitan visualizar el inventario y el soporte técnico que requiere mantener el módulo en funcionamiento. Este módulo es esencial para la toma de decisiones informadas sobre la gestión de inventario. Su alcance se limita a la generación de reportes y su dependencia es la versión Core de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/stock/reports` |
| Web | `web/ec.com.sidesoft.stock.reports/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSSTR`

# Guía de chat — Sidesoft Stock Reports

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.stock.reports`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo generar un reporte de stock de productos?
- ¿Existen limitaciones en la información que se puede visualizar en los informes?
- ¿Cómo puedo exportar los reportes generados?
- ¿Cuál es el proceso para actualizar el módulo si hay nuevas versiones disponibles?
- ¿A dónde puedo dirigirme si tengo problemas técnicos con el módulo?
- ¿El módulo funciona con versiones anteriores de Openbravo?
- ¿Qué dependencia específica tiene el módulo con otras partes del ERP?
- ¿Puedo ver informes de productos específicos o solo un resumen general?

# Domain — data model

## Functional

Este módulo no incluye entidades cabecera ni tablas físicas específicas, sino que funciona como un complemento que se integra con el sistema existente de Openbravo. No hay etapas definidas en procesos específicos dentro del sistema, ni relaciones entre tablas porque está diseñado únicamente para generar informes predefinidos sobre el stock sin almacenar datos propios. Igual, no se identifican triggers o funciones PL en el entorno del módulo, lo que sugiere que su funcionamiento es más superficial y orientado a la visualización.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| *(sin tablas en model/tables)* | — | — | — | — | — | — |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se integra en la interfaz de usuario de Openbravo a través de un menú que permite acceder a los diferentes informes disponibles. Aunque no se especifican ventanas físicas o pestañas, la navegación se realiza mediante el menú principal accesible en el sistema ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.stock.reports.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Egreso por Centro de Costos | Expense by Cost Center | No |
| Reporte Detallado Stock Valorado | Detailed Report Stock Valued | No |
| Resumen por transacción | Summary by transaction | No |
| Stock a la fecha | Stock to date | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.stock.reports.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un total de cuatro botones de proceso, aunque no se especifica su función particular o flujo. Los usuarios pueden esperar realizar acciones como completar la generación de un reporte o retornar al menú principal. Es importante tener en cuenta que no hay informes adicionales disponibles más allá de los que ya se han mencionado, lo que limita las validaciones y procesos asociados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.stock.reports.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Acumulado por transacción | Accumulated by transaction | Accumulated by transaction | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Egreso por Centro de Costos | Expense by Cost Center | Expense by Cost Center | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Detallado Stock Valorado | Detailed Report Stock Valued | Detailed Report Stock Valued | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Stock a la fecha | Stock to date | Stock to date | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Acumulado por transacción | Accumulated by transaction | Accumulated by transaction | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Egreso por Centro de Costos | Expense by Cost Center | Expense by Cost Center | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Detallado Stock Valorado | Detailed Report Stock Valued | Detailed Report Stock Valued | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Stock a la fecha | Stock to date | Stock to date | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Acumulado por transacción | Accumulated by transaction | — | — | — |
| Proceso / otro | Egreso por Centro de Costos | Expense by Cost Center | — | — | — |
| Proceso / otro | Reporte Detallado Stock Valorado | Detailed Report Stock Valued | — | — | — |
| Proceso / otro | Stock a la fecha | Stock to date | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 6**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **6**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

No se disponen de clases Java en el módulo, lo que indica que toda la funcionalidad se maneja a través de la configuración del ERP sin necesidad de programación adicional.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.stock.reports`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| *(sin clases Java en src/)* | — | — | — | — |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `MovementType - Accumulated Transaction` | `AD_Ref_List.Value IN ('C-','V+','M+','I+')` |
| AD_VAL_RULE | — | `Validation -  Logged user` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Location Warehouse` | `M_Locator.M_Warehouse_ID = @M_WAREHOUSE_ID@` |
| AD_VAL_RULE | — | `Is Employee` | `C_BPartner.IsEmployee = 'Y'` |
| AD_VAL_RULE | — | `Org warehouse` | `M_Warehouse.M_Warehouse_ID in (select M_Warehouse_ID  from AD_Org_Warehouse where AD_Org_ID=@AD_ORG_ID@)` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El módulo no establece triggers ni funciones PL que puedan ser utilizadas para el soporte. Esto sugiere que su rol en la base de datos es mínimo y se basa en la funcionalidad de reporte en tiempo real sin modificación de datos a nivel de base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| *(sin triggers)* | — | — | — | — | — |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| *(sin funciones en model/functions)* | — | — | — | — |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos ejecutables en AD_PROCESS del módulo)* | — | — | — | — | — |
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.stock.reports`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SSSTR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSSTR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.stock.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Accumulated by transaction` — Acumulado por transacción
- `Expense by Cost Center` — Egreso por Centro de Costos
- `Detailed Report Stock Valued` — Reporte Detallado Stock Valorado
- `Stock to date` — Stock a la fecha

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## In Out Reports
**Package:** `ec.com.sidesoft.custom.inout.reports`

# Module overview — In Out Reports

## Functional

El módulo 'In Out Reports' está diseñado para optimizar la gestión de informes de movimientos financieros dentro del sistema Openbravo. Principalmente, permite a los usuarios de negocio y al equipo de soporte generar reportes relacionados con entradas y salidas de pagos. Los actores involucrados incluyen usuarios de negocio que requieren la generación de informes y el equipo de soporte que resuelve incidencias relacionadas con estos procesos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/inout/reports` |
| Web | `web/ec.com.sidesoft.custom.inout.reports/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Advanced Payables and Receivables Mngmt
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSIOR`

# Guía de chat — In Out Reports

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.inout.reports`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)
- «¿Qué muestra el informe X?» → sección Informes en las clases Java de proceso del paquete (ver ruta "Java" en Technical)

## Preguntas ejemplo (IA)

- ¿Cómo puedo acceder a los reportes de pagos?
- ¿Qué información necesito para imprimir un reporte de movimientos bancarios?
- ¿Cómo puedo validar la información de los pagos antes de generar un informe?
- ¿Qué debo hacer si un reporte no se genera correctamente?
- ¿Es posible enviar un reporte por correo electrónico directamente desde el sistema?
- ¿Cómo se modifica la tabla de pagos para este módulo?
- ¿Qué reportes puedo generar con este módulo y cómo los interpreto?
- ¿Hay algún riesgo al modificar los reportes dentro de Openbravo?

# Domain — data model

## Functional

El módulo no tiene tablas físicas adicionales, pero interactúa con la tabla 'FIN_PAYMENT', que se ha modificado para adaptarse a las funciones de impresión de pagos. Las relaciones se establecen a través de comandos que permiten la generación de reportes basados en la información contenida en pagos. No se especifican triggers clave en este módulo, pero tiene funciones PL que facilitan la generación de informes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| *(sin tablas en model/tables)* | — | — | — | — | — | — |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`FIN_PAYMENT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo carece de ventanas específicas en la interfaz de usuario, centrándose en la generación de reportes a través de comandos ejecutables. Los usuarios interactúan con el sistema principalmente mediante la ejecución de procesos que generan informes de manera directa.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.inout.reports.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Comprobantes de Ingreso y Egreso | Receivables and Payables | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.inout.reports.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `C4B6506838E14A349D6717D6856F1B56`

- **AD_TAB_ID:** `C4B6506838E14A349D6717D6856F1B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 105 | Detail Report | `EM_Ssior_Detailreport` | No | No | — |

### Pestaña `F7A52FDAAA0346EFA07D53C125B40404`

- **AD_TAB_ID:** `F7A52FDAAA0346EFA07D53C125B40404` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 104 | Detail Report | `EM_Ssior_Detailreport` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dentro del módulo, hay un botón que permite ejecutar un proceso para generar los reportes, que incluye opciones como 'Print Entry Cellar', 'Print Movement Bank', 'Print Purchase Accounting', entre otros. Los informes generados son fundamentales para la contabilidad y la gestión de pagos. Las validaciones frecuentes incluyen asegurar que se proporcionen IDs de documentos válidos antes de intentar la generación de los informes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.inout.reports.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Receivables and Payables | Receivables and Payables | Receivables and Payables | *(OBUIAPP / manual)* | Report Receivables and Payables | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Print Entry Cellar | Print Entry Cellar | Print Entry Cellar | Java `Rpt_EntryCellar` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_EntryCellar.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_EntryCellar.java` |
| Reporte | Print Movement Bank | Print Movement Bank | Print Movement Bank | Java `Rpt_BankMovement` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_BankMovement.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_BankMovement.java` |
| Reporte | Print Purchase Accounting | Print Purchase Accounting | Print Purchase Accounting | Java `Rpt_PurchaseAccounting` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_PurchaseAccounting.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_PurchaseAccounting.java` |
| Reporte | SSIOR - Proceso de impresión de cobros | SSIOR - Print payments process | SSIOR PRINT PAYMENTS | Java `PrintPaymentIn` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_Voucher.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_process/PrintPaymentIn.java` |
| Reporte | SSIOR - Proceso de impresión de pagos | SSIOR - Print payments process | SSIOR - Print payments process | Java `PrintPaymentOut` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_VoucherOut.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_process/PrintPaymentOut.java` |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Print Entry Cellar | `Rpt_EntryCellar` | Informe (servlet PDF) | `—` | ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_EntryCellar.jrxml | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_EntryCellar.java` |
| Reporte | Print Movement Bank | `Rpt_BankMovement` | Informe (servlet PDF) | `—` | ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_BankMovement.jrxml | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_BankMovement.java` |
| Reporte | Print Purchase Accounting | `Rpt_PurchaseAccounting` | Informe (servlet PDF) | `—` | ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_PurchaseAccounting.jrxml | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_PurchaseAccounting.java` |
| Reporte | SSIOR - Proceso de impresión de cobros | `PrintPaymentIn` | Informe (servlet PDF) | `—` | ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_Voucher.jrxml | `src/ec/com/sidesoft/custom/inout/reports/ad_process/PrintPaymentIn.java` |
| Reporte | SSIOR - Proceso de impresión de pagos | `PrintPaymentOut` | Informe (servlet PDF) | `—` | ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_VoucherOut.jrxml | `src/ec/com/sidesoft/custom/inout/reports/ad_process/PrintPaymentOut.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Receivables and Payables | Receivables and Payables | Receivables and Payables | *(OBUIAPP / manual)* | Report Receivables and Payables | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Receivables and Payables | Receivables and Payables | — | Report Receivables and Payables | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Print Entry Cellar | Print Entry Cellar | Print Entry Cellar | Java `Rpt_EntryCellar` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_EntryCellar.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_EntryCellar.java` |
| Reporte | Print Movement Bank | Print Movement Bank | Print Movement Bank | Java `Rpt_BankMovement` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_BankMovement.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_BankMovement.java` |
| Reporte | Print Purchase Accounting | Print Purchase Accounting | Print Purchase Accounting | Java `Rpt_PurchaseAccounting` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_PurchaseAccounting.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_PurchaseAccounting.java` |
| Reporte | SSIOR - Proceso de impresión de cobros | SSIOR - Print payments process | SSIOR PRINT PAYMENTS | Java `PrintPaymentIn` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_Voucher.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_process/PrintPaymentIn.java` |
| Reporte | SSIOR - Proceso de impresión de pagos | SSIOR - Print payments process | SSIOR - Print payments process | Java `PrintPaymentOut` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_VoucherOut.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/inout/reports/ad_process/PrintPaymentOut.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 10**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **5**; archivos `*.jrxml` en el repo = **10**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Print Entry Cellar | `Print Entry Cellar` | Java `Rpt_EntryCellar`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Print Entry Cellar |
| 2 | Print Movement Bank | `Print Movement Bank` | Java `Rpt_BankMovement`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Print Movement Bank |
| 3 | Print Purchase Accounting | `Print Purchase Accounting` | Java `Rpt_PurchaseAccounting`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Print Purchase Accounting |
| 4 | SSIOR - Proceso de impresión de cobros | `SSIOR PRINT PAYMENTS` | Java `PrintPaymentIn`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Process to print payments or send them through email to the client |
| 5 | SSIOR - Proceso de impresión de pagos | `SSIOR - Print payments process` | Java `PrintPaymentOut`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | SSIOR - Print payments process |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/BankMovement.jrxml`
- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_Voucher.jrxml`
- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_VoucherOut.jrxml`
- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_Voucher_Detail.jrxml`
- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_Voucher_DetailHeader.jrxml`
- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/PurchaseAccounting.jrxml`
- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_BankMovement.jrxml`
- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_EntryCellar.jrxml`
- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_PurchaseAccounting.jrxml`
- `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_SubPurchaseAccounting.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye varias clases Java que facilitan el proceso de generación de informes. Estas clases, como 'PrintPaymentIn' y 'PrintPaymentOut', manejan la lógica de negocio relacionada con la creación y envío de los reportes generados a los usuarios o a través de correo electrónico.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.inout.reports`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `PrintPaymentIn` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/custom/inout/reports/ad_process/PrintPaymentIn.java` |
| `PrintPaymentOut` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/custom/inout/reports/ad_process/PrintPaymentOut.java` |
| `Rpt_BankMovement` | ad_reports | HttpSecureAppServlet | — | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_BankMovement.java` |
| `Rpt_EntryCellar` | ad_reports | HttpSecureAppServlet | — | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_EntryCellar.java` |
| `Rpt_PurchaseAccounting` | ad_reports | HttpSecureAppServlet | — | `src/ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_PurchaseAccounting.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Ssior Validate User` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `C_DocType - Receivables Payables` | `C_DocType.DocBaseType IN ('APP', 'ARR')` |
| Función PL `ssior_convert_numbertoletters` | — | invocación proceso | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test); |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El módulo usa funciones PL para manejar la lógica detrás de la impresión de informes, permitiendo la integración con la base de datos de Openbravo para acceder a los datos necesarios. La falta de triggers específicos sugiere que las operaciones son manejadas a través de estas funciones para garantizar un flujo de datos eficiente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| *(sin triggers)* | — | — | — | — | — |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssior_convert_numbertoletters` | — | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas… | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas = ' || v_armar_texto_d;; RAISE NOTICE '%','RESULT v_tnumero >= 101 and v_tnumero <200 v_number_test = ' || to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_tnumero >= 101 and v_tnumero <200 v_number_test = ' || vTexto ; | `model/functions/SSIOR_CONVERT_NUMBERTOLETTERS.xml` |
| `ssior_get_min_line` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSIOR_GET_MIN_LINE.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Print Entry Cellar | `Print Entry Cellar` | Reporte | Java `Rpt_EntryCellar` | S | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_EntryCellar.jrxml`; contexto sesión `—`. |
| 2 | Print Movement Bank | `Print Movement Bank` | Reporte | Java `Rpt_BankMovement` | S | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_BankMovement.jrxml`; contexto sesión `—`. |
| 3 | Print Purchase Accounting | `Print Purchase Accounting` | Reporte | Java `Rpt_PurchaseAccounting` | S | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/Rpt_PurchaseAccounting.jrxml`; contexto sesión `—`. |
| 4 | SSIOR - Proceso de impresión de cobros | `SSIOR PRINT PAYMENTS` | Reporte | Java `PrintPaymentIn` | S | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_Voucher.jrxml`; contexto sesión `—`. |
| 5 | SSIOR - Proceso de impresión de pagos | `SSIOR - Print payments process` | Reporte | Java `PrintPaymentOut` | S | Genera PDF desde JRXML `ec/com/sidesoft/custom/inout/reports/ad_reports/PayablesReceivables_VoucherOut.jrxml`; contexto sesión `—`. |

**Total acciones documentadas (extract):** **5** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.custom.inout.reports`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SSIOR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSIOR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.inout.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Receivables and Payables` — Receivables and Payables
- `Print Entry Cellar` — Print Entry Cellar
- `Print Movement Bank` — Print Movement Bank
- `Print Purchase Accounting` — Print Purchase Accounting
- `SSIOR PRINT PAYMENTS` — SSIOR - Proceso de impresión de cobros
- `SSIOR - Print payments process` — SSIOR - Proceso de impresión de pagos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Recosteo
**Package:** `ec.sidesoft.recosteo`

# Module overview — Sidesoft Recosteo

## Functional

El módulo Sidesoft Recosteo está diseñado para facilitar la gestión y el análisis del proceso de recosteo dentro de Openbravo. Su propósito es optimizar el manejo de costos, permitiendo a los actores involucrados, como los usuarios de negocio y los desarrolladores, realizar un seguimiento eficaz de los costos asociados a productos y servicios. El alcance del módulo incluye la implementación de funciones específicas para el cálculo y ajuste de costos, asegurando una base de datos coherente y actualizada. Las dependencias clave incluyen la compatibilidad con la estructura central de Openbravo y otros módulos requeridos para su óptimo funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/sidesoft/recosteo` |
| Web | `web/ec.sidesoft.recosteo/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

*(sin prefijo en AD_MODULE_DBPREFIX)*

# Guía de chat — Sidesoft Recosteo

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.sidesoft.recosteo`).

## Enrutamiento rápido

> Los documentos de detalle (`20-*`, `22-*`, `30-*`, `31-*`, `35-*`, `45-*`, `50-*`, `55-*`, `60-*`) no existen en este proyecto. En su lugar, analiza directamente el CÓDIGO FUENTE del paquete usando las rutas de la sección "Technical" de este mismo módulo (arriba), leyéndolo vía MCP de GitHub en el repositorio de código Openbravo del cliente. No intentes abrir esos archivos — no existen.

| Si el usuario dice… | Buscar en el código (rutas de la tabla Technical de arriba) |
|---------------------|--------|
| No encuentro una pantalla / menú | Application dictionary (`src-db/database/sourcedata/`) — definiciones de ventanas y menús (AD_Window, AD_Menu, AD_Tab) |
| Un botón o proceso no funciona | Carpeta "Java" del paquete — clases de proceso/acción (`*Process.java`, `*ActionHandler.java`) |
| Campos / obligatorios en pantalla | Application dictionary (`src-db/database/sourcedata/`) — columnas y reglas de campo (AD_Field, AD_Column) |
| Informes / PDF | Carpeta "Java" del paquete — clases de reporte; o carpeta "Web" para plantillas de impresión |
| Mensaje de error concreto | Carpeta "Java" del paquete — busca el texto literal del mensaje en el código para ubicar dónde se dispara |
| Error al guardar / validación | "Physical model" del paquete (`model/triggers/`, `model/functions/`) — triggers y funciones de BD que validan |
| Adjuntos / colores / JS | Carpeta "Web" del paquete |

## Ejemplos de consulta

- «La ventana X no carga»
- «Al pulsar Completar sale error …»
- «¿Qué hace el proceso Y?»

Edite este archivo con escenarios reales de su organización.

## Escenarios sugeridos (generados)

- «¿Qué ventanas y menús tiene este módulo?» → el Application dictionary del paquete (`src-db/database/sourcedata/` — AD_Window, AD_Menu, AD_Tab)
- «¿Qué hace el botón *Completar* / *Retornar* / *Rechazar*?» → las clases Java de proceso del paquete (ver ruta "Java" en Technical)
- «Error al guardar / validación en base de datos» → el modelo físico del paquete (`model/triggers/`, `model/functions/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo ajustar los costos de un producto?
- ¿Qué procesos debo seguir para realizar un recosteo?
- ¿Existen informes disponibles sobre el recosteo?
- ¿Cuál es la diferencia entre completar y retornar un proceso de recosteo?
- ¿Hay validaciones automáticas durante el proceso de recosteo?
- ¿Qué debo hacer si encuentro un error al realizar un recosteo?
- ¿Puedo deshacer un recosteo una vez completado?
- ¿Cómo se actualizan los costos en el sistema?

# Domain — data model

## Functional

El modelo de datos del módulo Sidesoft Recosteo incluye entidades que representan cabeceras y etapas del proceso de recosteo. Aunque no se especifican tablas físicas, el modelo está basado en funciones PL que manejan lógicas de negocio específicas para realizar cálculos y ajustes a los costos. Las relaciones entre las entidades son críticas para asegurar la integridad de los datos, y los triggers, aunque no se listan explícitamente, son esenciales para automatizar ciertos procesos dentro del flujo de recosteo, asegurando que las actualizaciones en los costos sean siempre consistentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| *(sin tablas en model/tables)* | — | — | — | — | — | — |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación dentro del módulo Sidesoft Recosteo se realiza a través de un menú de dos secciones. Aunque no se especifican ventanas en detalle, los usuarios pueden interactuar con las funciones del módulo a través de opciones de menú que les permiten acceder a las diferentes funcionalidades y procesos disponibles relacionados con el recosteo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.sidesoft.recosteo.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Cambio costos estándar producción | Change standard production costs | No |
| Recosteo | Clearing costing | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.sidesoft.recosteo.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye dos procesos clave, que son accesibles mediante botones típicos como 'Completar' y 'Retornar'. Estos botones suelen estar relacionados con el cierre y la validación de los procesos de recosteo. Adicionalmente, el sistema asegura validaciones frecuentes, que son necesarias para evitar errores en el cálculo de costos y garantizar la integridad de los datos asociados a cada recosteo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.sidesoft.recosteo.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cambio costos estándar producción | Change standard production costs | SRCC_cost_value | `srcc_changue_production_costs` | Actualiza transacciones Costos Indirectos, tabla ma_pl_ic; Actualiza transacciones Maquinaria, tabla ma_pl_machine; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee | — |
| Botón (PL/pgSQL) | Recosteo | Clearing costing | SRCC_Recosteo | `srcc_recosteo` | Valida transacciones en fechas anteriores a la fecha de procesamiento; 2. Borrar líneas de costo en base a las transacciones a reprocesar; 3.Borra transacciones costeadas, tabla m_transaction_cost; Actualiza transaccion… | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| — | *(sin procesos con clase Java en AD_MODEL_OBJECT)* | — | — | — | — | — |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cambio costos estándar producción | Change standard production costs | SRCC_cost_value | `srcc_changue_production_costs` | Actualiza transacciones Costos Indirectos, tabla ma_pl_ic; Actualiza transacciones Maquinaria, tabla ma_pl_machine; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee | — |
| Botón (PL/pgSQL) | Recosteo | Clearing costing | SRCC_Recosteo | `srcc_recosteo` | Valida transacciones en fechas anteriores a la fecha de procesamiento; 2. Borrar líneas de costo en base a las transacciones a reprocesar; 3.Borra transacciones costeadas, tabla m_transaction_cost; Actualiza transaccion… | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cambio costos estándar producción | Change standard production costs | PL `srcc_changue_production_costs` | Actualiza transacciones Costos Indirectos, tabla ma_pl_ic; Actualiza transacciones Maquinaria, tabla ma_pl_machine; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee | Actualiza transacciones Costos Indirectos, tabla ma_pl_ic; Actualiza transacciones Maquinaria, tabla ma_pl_machine; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee |
| Botón (PL/pgSQL) | Recosteo | Clearing costing | PL `srcc_recosteo` | Valida transacciones en fechas anteriores a la fecha de procesamiento; 2. Borrar líneas de costo en base a las transacciones a reprocesar; 3.Borra transacciones costeadas, tabla m_transaction_cost; Actualiza transaccion… | Valida transacciones en fechas anteriores a la fecha de procesamiento; 2. Borrar líneas de costo en base a las transacciones a reprocesar; 3.Borra transacciones costeadas, tabla m_transaction_cost; Actualiza transacciones costeadas, tabla m_productionline; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee; Actualiza transacciones Costos Indirectos, tabla ma_pl_ic |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| *(ninguno en este módulo)* | — | — | — | — | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 0**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| — | *(sin informes en AD_PROCESS)* | — | — | — | — |
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

No se han implementado clases Java específicas en este módulo, lo que sugiere que toda la funcionalidad está abstraída en el uso de procesos PL y la configuración de la UI del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.sidesoft.recosteo`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| *(sin clases Java en src/)* | — | — | — | — |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Función PL `srcc_changue_production_costs` | — | invocación proceso | Actualiza transacciones Costos Indirectos, tabla ma_pl_ic; Actualiza transacciones Maquinaria, tabla ma_pl_machine; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee |
| Función PL `srcc_recosteo` | — | invocación proceso | Valida transacciones en fechas anteriores a la fecha de procesamiento; 2. Borrar líneas de costo en base a las transacciones a reprocesar; 3.Borra transacciones costeadas, tabla m_transaction_cost |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

En el contexto de la base de datos, las funciones PL juegan un rol fundamental en el soporte técnico, permitiendo la automatización de procesos y la integración de lógicas de negocio específicas. Los triggers, aunque no están explícitamente definidos, podrían ser utilizados para manejar eventos en el sistema que impactan en los costos y ajustes de recosteo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| *(sin triggers)* | — | — | — | — | — |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `srcc_changue_production_costs` | Cambio costos estándar producción | Actualiza transacciones Costos Indirectos, tabla ma_pl_ic; Actualiza transacciones Maquinaria, tabla ma_pl_machine; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee | Actualiza transacciones Costos Indirectos, tabla ma_pl_ic; Actualiza transacciones Maquinaria, tabla ma_pl_machine; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee | `model/functions/SRCC_CHANGUE_PRODUCTION_COSTS.xml` |
| `srcc_recosteo` | Recosteo | Valida transacciones en fechas anteriores a la fecha de procesamiento; 2. Borrar líneas de costo en base a las transacciones a reprocesar; 3.Borra transacciones costeadas, tabla m_transaction_cost; Actualiza transaccion… | Valida transacciones en fechas anteriores a la fecha de procesamiento; 2. Borrar líneas de costo en base a las transacciones a reprocesar; 3.Borra transacciones costeadas, tabla m_transaction_cost; Actualiza transacciones costeadas, tabla m_productionline; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee; Actualiza transacciones Costos Indirectos, tabla ma_pl_ic | `model/functions/SRCC_RECOSTEO.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cambio costos estándar producción | `SRCC_cost_value` | Botón (PL/pgSQL) | PL `srcc_changue_production_costs` | N | Actualiza transacciones Costos Indirectos, tabla ma_pl_ic; Actualiza transacciones Maquinaria, tabla ma_pl_machine; Actualiza transacciones Categoria Salarial, tabla ma_pl_employee |
| 2 | Recosteo | `SRCC_Recosteo` | Botón (PL/pgSQL) | PL `srcc_recosteo` | N | Valida transacciones en fechas anteriores a la fecha de procesamiento; 2. Borrar líneas de costo en base a las transacciones a reprocesar; 3.Borra transacciones costeadas, tabla m_ |

**Total acciones documentadas (extract):** **2** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.sidesoft.recosteo`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `RECOSTEO`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `RECOSTEO` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.sidesoft.recosteo` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `SRCC_cost_value` — Cambio costos estándar producción
- `SRCC_Recosteo` — Recosteo

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
