# Openbravo Sidesoft — Activos Fijos

> Registro, depreciación, traslado, baja, revalorización, impuestos, presupuesto, secuencia, reportes y customizaciones de activos fijos.

**Paquetes incluidos (17):**
- `com.sidesoft.ecuador.asset.allocation` — Asset Allocation
- `com.sidesoft.ecuador.asset.changetranslation` — Change Translation Assets Field
- `com.sidesoft.ecuador.asset.move` — Asset Move
- `com.sidesoft.ecuador.asset.subcategory.level` — Sidesoft Asset Subcategory Level
- `ec.com.sidesoft.asset.dimensions` — Asset Dimensions
- `ec.com.sidesoft.asset.revaluation` — Sidesoft Assets Revaluation
- `ec.com.sidesoft.asset.transfer` — Sidesoft Asset Transfer
- `ec.com.sidesoft.assets.budget` — Assets Budget
- `ec.com.sidesoft.assets.changes` — Sidesoft Assets Changes
- `ec.com.sidesoft.assets.customizations` — Assets Customizations
- `ec.com.sidesoft.assets.reports` — Sidesoft Assets Reports
- `ec.com.sidesoft.assets.sequence` — Sidesoft Assets Automatic Sequence
- `ec.com.sidesoft.assets.taxes` — Sidesoft Assets Taxes
- `ec.com.sidesoft.control.assets` — Sidesoft Control Assets
- `ec.com.sidesoft.derecognize.asset` — Asset Derecognize
- `ec.com.sidesoft.ecuador.asset.purchase.info` — Sidesoft Asset Purchase Information
- `ec.com.sidesoft.hidefield.assets` — Hide Fields Asset


---
## Asset Allocation
**Package:** `com.sidesoft.ecuador.asset.allocation`

# Module overview — Asset Allocation

## Functional

El módulo de Asignación de Activos se centra en gestionar la distribución y control de equipos y recursos en una organización. Los actores principales incluyen los administradores, el personal de soporte y los usuarios del negocio encargados de la gestión de activos. Este módulo permite la creación, modificación y seguimiento de activos, asegurando que se asignen correctamente a los departamentos pertinentes, facilitando su uso eficiente. Depende del núcleo del ERP para funcionar correctamente, ya que usa sus tablas y funciones base.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/ecuador/asset/allocation` |
| Web | `web/com.sidesoft.ecuador.asset.allocation/` |

### Declared dependencies

- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSAL`

# Guía de chat — Asset Allocation

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.ecuador.asset.allocation`).

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
- «¿Qué es la tabla ssal_appl_active?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo aprobar un nuevo activo asignado a mi departamento?
- ¿Cuáles son los pasos para devolver un activo que ya no se necesita?
- ¿Cómo puedo generar un informe sobre los activos que tengo a cargo?
- ¿Qué debo hacer si un activo está dañado o necesita mantenimiento?
- ¿Cómo se registra un nuevo activo en el sistema?
- ¿Es posible transferir un activo a otro departamento?
- ¿Cómo puedo consultar la historia de un activo específico?
- ¿Hay alguna validación que deba tener en cuenta al asignar actuados?

# Domain — data model

## Functional

El modelo de datos está centrado en la entidad cabecera de 'Activo', de la cual derivan otras tablas de soporte. Las etapas clave incluyen la creación de activos, la aprobación de asignaciones y la devolución de activos. Relaciones importantes se encuentran entre las tablas de activos y los detalles de activos, así como entre los activos y los departamentos asignados. El trigger clave es 'SSAL_CUSTODIO_TRG', que ejecuta una rutina PL/pgSQL para gestionar la lógica de negocio al insertar o actualizar registros en la tabla 'A_ASSET'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssal_active_main` |
| `ssal_appl_active` |
| `ssal_asset_com` |
| `ssal_asset_mov` |
| `ssal_asset_return` |
| `ssal_asset_returnline` |
| `ssal_asset_tranfer` |
| `ssal_building` |
| `ssal_department` |
| `ssal_mark` |
| `ssal_model` |
| `ssal_series` |
| `ssal_state` |
| `ssal_state_asset` |
| `ssal_unit` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssal_active_main` | ssal_active_main | — | — | a_asset_id→a_asset; a_asset_cod_id→a_asset; a_asset_description_id→a_asset; a_asset_upc_id→a_asset; a_asset_group_id→a_asset_group (+13) | Detalle enlazado a a_asset. | PK `ssal_active_main_key`; Cols: m_product_id, c_doctype_id, c_costcenter_id, user1_id, user2_id; `SSAL_ACT_MAIN_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSAL_ACT_MAIN_PROCE_CHK`: PROCESSED IN ('Y', 'N') |
| `ssal_appl_active` | ssal_appl_active | — | — | ssal_active_main_id→ssal_active_main; a_asset_id→a_asset; a_asset_cod_id→a_asset; a_asset_description_id→a_asset; a_asset_upc_id→a_asset (+14) | Detalle enlazado a a_asset, ssal_active_main. | PK `ssal_appl_active_key`; Cols: m_product_id, c_doctype_id, c_costcenter_id, user1_id, user2_id; `SSAL_APPL_ACTIVE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSAL_APPL_ACTIVE_PROCE_CHK`: PROCESSED IN ('Y', 'N') |
| `ssal_asset_com` | ssal_asset_com | — | — | a_asset_id→a_asset; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a a_asset, ad_client, ad_org. | PK `ssal_asset_com_key`; Cols: a_asset_id, name, description, peso, volume; `SSAL_ASSET_COM_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_asset_mov` | — | — | — | a_asset_id→a_asset; ad_client_id→ad_client; ad_org_id→ad_org; ssal_appl_active_id→ssal_appl_active; c_bpartner_id→c_bpartner (+9) | Detalle enlazado a a_asset, ad_client, ad_org. | PK `ssal_asset_mov_key`; Cols: m_product_id, c_doctype_id, c_costcenter_id, user1_id, user2_id; `SSAL_ASSET_MOV_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_asset_return` | ssal_asset_return | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ssal_asset_app_id→ssal_appl_active; c_bpartner_id→c_bpartner; c_doctype_id→c_doctype (+2) | Detalle enlazado a ad_client, ad_org, ssal_appl_active. | PK `ssal_asset_return_key`; Cols: c_bpartner_id, m_product_id, ssal_state, date_mov, load_assets; `SSAL_ASSET_RET_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_asset_returnline` | ssal_asset_returnline | — | — | ssal_appl_active_id→ssal_appl_active; ssal_building_id→ssal_building; ad_client_id→ad_client; c_costcenter_id→c_costcenter; ssal_department_id→ssal_department (+5) | Detalle enlazado a ad_client, ssal_appl_active, ssal_building. | PK `ssal_asset_returnline_key`; Cols: ssal_asset_return_id, ssal_appl_active_id, tranfer, ssal_building_id, ssal_unit_id; `SSAL_ASSET_RETL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_asset_tranfer` | — | — | — | a_asset_id→a_asset; a_asset_group_id→a_asset_group; ad_client_id→ad_client; ad_org_id→ad_org; ssal_appl_active_id→ssal_appl_active (+9) | Detalle enlazado a a_asset, a_asset_group, ad_client. | PK `ssal_asset_tranfer_key`; Cols: m_product_id, c_bpartner_id, c_doctype_id, ssal_state_id, a_asset_id; `SSAL_ASSET_TRAN_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_building` | ssal_building | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssal_building_key`; Cols: value, name, description, direction; `SSAL_BUILDING_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_department` | ssal_department | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssal_department_key`; Cols: value, name, description; `SSAL_DEPARTMENT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_mark` | ssal_mark | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssal_mark_key`; Cols: value, name, description; `SSAL_MARK_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_model` | ssal_model | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssal_model_key`; Cols: value, name, description; `SSAL_MODEL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_series` | ssal_series | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssal_series_key`; Cols: value, name, description; `SSAL_SERIES_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_state` | ssal_state | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssal_state_key`; Cols: value, name, description; `SSAL_STATE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_state_asset` | ssal_state_asset | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssal_state_asset_key`; Cols: value, name, description; `SSAL_STATE_ASSET_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssal_unit` | ssal_unit | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssal_unit_key`; Cols: value, name, description; `SSAL_UNIT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssal_active_main` |
| `ssal_appl_active` |
| `ssal_asset_com` |
| `ssal_asset_return` |
| `ssal_asset_returnline` |
| `ssal_building` |
| `ssal_department` |
| `ssal_mark` |
| `ssal_model` |
| `ssal_series` |
| `ssal_state` |
| `ssal_state_asset` |
| `ssal_unit` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`A_ASSET`, `SSATR_ASSET_DETAIL`, `SSATR_ASSET_TRANSFER`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de diversas ventanas que permiten acceder a diferentes funciones, como la 'Aprobación de activo' y 'Devolución de activo'. Cada ventana contiene pestañas que detallan características específicas, permitiendo a los usuarios gestionar los activos mediante formularios y listas con información relevante.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.ecuador.asset.allocation.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Aprobación de activo | Approval of Active |
| Building | Building |
| Características de activo | Characteristics of Assets |
| Department Asset | Department Asset |
| Devolución de activo | Return Active |
| Fixed Assets Request OLD | Fixed Assets Request OLD |
| Marca | Mark |
| Modelo | Model |
| Series | Series |
| Solicitud de Activo | Fixed Assets Request |
| State Asset | State Asset |
| State Request | State Request |
| Unit | Unit |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Aprobación de activo | Approval of Active | No |
| Características de activo | Characteristics of Assets | No |
| Configuración | Setup | Sí |
| Departamento | Department Asset | No |
| Devolución de activo | Return Active | No |
| Edificio | Building | No |
| Informe de activos fijos | Report of Assets Fixed | No |
| Marca | Mark | No |
| Modelo | Model | No |
| Reporte Activos por custodio | Assets by Custodian | No |
| Reporte Asignación de activos | Report Asset Allocation | No |
| Reporte Bajas de activos | Report Asset Low | No |
| Reporte Componentes de activos | Report Asset Components | No |
| Reporte Estado de activos | Assets Status | No |
| Reporte general de activos | Report General Active | No |
| Reporte Movimiento de activos | Report Asset Movements | No |
| Reporte Solicitud de activos | Report Asset Request | No |
| Reporte Verificación física de activos | Report Asset Physical Verification | No |
| Solicitud de Activo | Fixed Assets Request | No |
| State Asset | State Asset | No |
| Transacciones | Transactions | Sí |
| Unidad | Unit | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.ecuador.asset.allocation.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Aprobación de activo

- **AD_WINDOW_ID:** `A39DA45460AD41D18FBE99FE70173690`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Approval of Active | `8784C55BFE1D4C8993EEE2F8146FFE56` | 0 |
| 20 | Lines | `E9FC518A39C64655BADA0C0F4830D834` | 1 |

### Ventana: Building

- **AD_WINDOW_ID:** `638A493D753A4C1C91F2188B6A340021`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Building | `84636920D2CA45E9BF9F0FE9463C63F8` | 0 |

### Ventana: Características de activo

- **AD_WINDOW_ID:** `46C41886EF63481F80BD345D36151BB1`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Characteristics of Assets | `539` | 0 |
| 20 | Movement | `E9FC518A39C64655BADA0C0F4830D834` | 1 |
| 30 | Components | `8B0AD20831DD4F4085BC07E6E190CC91` | 1 |

### Ventana: Department Asset

- **AD_WINDOW_ID:** `17D55132BA2F4D88A4EAD5D4AA477946`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Department Asset | `7FEA19BE574E42E4875C0CD6ED49E369` | 0 |

### Ventana: Devolución de activo

- **AD_WINDOW_ID:** `1BCE01C581F848AC8710B8DFC2C8B9B2`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Return Active | `4468ADC751174A7C81B316057A8EC7E5` | 0 |
| 20 | Asssets | `A224E335DB004C8382546006C8BFD474` | 1 |

### Ventana: Fixed Assets Request OLD

- **AD_WINDOW_ID:** `8850B801A49941B98A4A391408AA5E84`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Fixed Assets Request OLD | `E9FC518A39C64655BADA0C0F4830D834` | 0 |

### Ventana: Marca

- **AD_WINDOW_ID:** `894DBF87C0514F04BDA352F654681084`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Mark | `7A553017602F4669BC90AFF32F1F1298` | 0 |

### Ventana: Modelo

- **AD_WINDOW_ID:** `EB0E9BBC53B44E53973331D5341AF730`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Model | `6CB591849918405C80DB4F2EB1453317` | 0 |

### Ventana: Series

- **AD_WINDOW_ID:** `151F497D62D9457F86DDB86B7F6E65CF`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Series | `0723B1FA680A4F51BC1E696801386B7E` | 0 |

### Ventana: Solicitud de Activo

- **AD_WINDOW_ID:** `5117C70DACDF4EADA8EB43916139BC77`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Fixed Assets Request | `8784C55BFE1D4C8993EEE2F8146FFE56` | 0 |

### Ventana: State Asset

- **AD_WINDOW_ID:** `CBA0B366839446B4B8DC8C7273123012`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | State Asset | `0C64B67D8102441AB877D42BCA344CAA` | 0 |

### Ventana: State Request

- **AD_WINDOW_ID:** `4332BAFFD5A246EAB162FFD8AA52BB28`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | State Request | `ED7157A5B8E44A44858593DDF00C9D9C` | 0 |

### Ventana: Unit

- **AD_WINDOW_ID:** `C8BBA317C3B948D3A5B04DFA1C0D42A8`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Unit | `7C0EEF00E0004B23BC3DAE0959AB05BF` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Return Active (ventana: Devolución de activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 35 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 35 | Document No. | `Documentno` | No | Sí | — |
| 150 | Date_Mov | `Date_Mov` | No | No | — |
| 160 | Procesado | `Load_Assets` | No | Sí | — |
| 165 | Ending Date | `Enddate` | No | No | — |
| 170 | Custodian | `C_Custodian_ID` | No | No | — |
| 190 | LoadActive2 | `Load_Active` | No | No | — |
| 540 | Description | `Description` | No | No | — |
| 550 | Create Lines Return Asset | `Generatelines` | No | No | — |

### State Asset (ventana: State Asset)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### State Request (ventana: State Request)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Components (ventana: Características de activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 50 | Asset | `A_Asset_ID` | No | Sí | — |
| 60 | Commercial Name | `Name` | No | No | — |
| 70 | Description | `Description` | No | No | — |
| 80 | Peso | `Peso` | No | No | — |
| 90 | Volume | `Volume` | No | No | — |

### Series (ventana: Series)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Department Asset (ventana: Department Asset)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Pestaña `6D56D425862540AAAF3442B038FE06E2`

- **AD_TAB_ID:** `6D56D425862540AAAF3442B038FE06E2` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 120 | Edifice | `EM_Ssal_Building_ID` | No | No | 8484DE4BC0CD49C99E8D7FA4A7CF1E81 |
| 130 | Unit | `EM_Ssal_Unit_ID` | No | No | 8484DE4BC0CD49C99E8D7FA4A7CF1E81 |
| 140 | Department | `EM_Ssal_Department_ID` | No | No | 8484DE4BC0CD49C99E8D7FA4A7CF1E81 |
| 150 | Building destination | `EM_Ssal_Building_Dest_ID` | No | No | 8484DE4BC0CD49C99E8D7FA4A7CF1E81 |
| 160 | Destination unit | `EM_Ssal_Unit_Dest_ID` | No | No | 8484DE4BC0CD49C99E8D7FA4A7CF1E81 |
| 170 | Destination department | `EM_Ssal_Department_Dest_ID` | No | No | 8484DE4BC0CD49C99E8D7FA4A7CF1E81 |

### Unit (ventana: Unit)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Commercial Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Pestaña `7D8FA15C61074FC58F97668E2873DC4E`

- **AD_TAB_ID:** `7D8FA15C61074FC58F97668E2873DC4E` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Edifice | `EM_Ssal_Building_ID` | No | Sí | — |
| 110 | Unit | `EM_Ssal_Unit_ID` | No | Sí | — |
| 120 | Department | `EM_Ssal_Department_ID` | No | Sí | — |

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 50 | Document Type | `EM_Ssal_C_Doctype_ID` | No | No | — |
| 90 | Código de Barras | `EM_Ssal_Bar_Code` | No | No | — |
| 520 | Edifice | `EM_Ssal_Building_ID` | No | No | — |
| 530 | Unit | `EM_Ssal_Unit_ID` | No | No | — |
| 540 | Department | `EM_Ssal_Department_ID` | No | No | — |

### Lines (ventana: Aprobación de activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 110 | Quantity | `Quantity` | No | No | — |
| 395 | Description Mov | `Description_Mov` | No | No | 929BB97A32E94530ADBC2780A8E0DA31 |
| 397 | UPC/EAN | `A_Asset_Upc_ID` | No | Sí | — |
| 399 | Description Active | `A_Asset_Description_ID` | No | Sí | — |
| 400 | Asset Category | `A_Asset_Group_ID` | No | No | 929BB97A32E94530ADBC2780A8E0DA31 |
| 410 | Asset | `A_Asset_ID` | No | No | 929BB97A32E94530ADBC2780A8E0DA31 |
| 420 | Código Activo | `A_Asset_Cod_ID` | No | Sí | 929BB97A32E94530ADBC2780A8E0DA31 |

### Asssets (ventana: Devolución de activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | Sí | — |
| 40 | UPC/EAN | `A_Asset_Upc_ID` | No | Sí | — |
| 42 | Description Active | `A_Asset_Description_ID` | No | Sí | — |
| 44 | Asset Category | `A_Asset_Group_ID` | No | Sí | — |
| 46 | Active | `Ssal_Appl_Active_ID` | No | Sí | — |
| 48 | Código Activo | `A_Asset_Cod_ID` | No | Sí | — |
| 50 | Tranfer | `Tranfer` | No | No | — |
| 60 | Edifice | `Ssal_Building_ID` | No | Sí | — |
| 70 | Unit | `Ssal_Unit_ID` | No | Sí | — |
| 80 | Department | `Ssal_Department_ID` | No | Sí | — |
| 90 | Cost Center | `C_Costcenter_ID` | No | Sí | — |
| 100 | 1st Dimension | `User1_ID` | No | Sí | — |
| 110 | 2nd Dimension | `User2_ID` | No | Sí | — |

### Fixed Assets Request (ventana: Solicitud de Activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 80 | Document Type | `C_Doctype_ID` | No | No | — |
| 85 | Document No. | `Documentno` | No | Sí | — |
| 90 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 100 | Date Request | `Date_Application` | No | No | — |
| 105 | Quantity | `Quantity` | No | No | — |
| 110 | Justification | `Justification` | No | No | — |
| 115 | Product | `M_Product_ID` | No | No | — |
| 150 | Description | `Description` | No | No | — |
| 200 | State | `State` | No | Sí | — |
| 280 | Process Request | `Process_Request` | No | No | — |
| 400 | Edifice | `Ssal_Building_ID` | No | No | 47BC13601657479785E4B5D632B167D6 |
| 410 | Unit | `Ssal_Unit_ID` | No | No | 47BC13601657479785E4B5D632B167D6 |
| 420 | Department | `Ssal_Department_ID` | No | No | 47BC13601657479785E4B5D632B167D6 |
| 500 | Cost Center | `C_Costcenter_ID` | No | No | 8D71261F17854B44A75D9C894F751091 |
| 510 | 1st Dimension | `User1_ID` | No | No | 8D71261F17854B44A75D9C894F751091 |
| 520 | 2nd Dimension | `User2_ID` | No | No | 8D71261F17854B44A75D9C894F751091 |

### Approval of Active (ventana: Aprobación de activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 60 | Document Type | `C_Doctype_ID` | No | Sí | — |
| 90 | Document No. | `Documentno` | No | Sí | — |
| 100 | Date Request | `Date_Application` | No | Sí | — |
| 100 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 105 | Product | `M_Product_ID` | No | Sí | — |
| 110 | Quantity | `Quantity` | No | Sí | — |
| 150 | Justification | `Justification` | No | Sí | — |
| 190 | Approved Resquest | `Approved` | No | No | — |
| 250 | Processed | `Processed` | No | Sí | — |
| 270 | Date Transaction | `Date_Transaction` | No | Sí | — |
| 350 | State | `State` | No | Sí | — |
| 351 | Custodian | `C_Custodian_ID` | No | No | C90B234F855D4874B6727A1D6E974E5A |
| 352 | Starting Date | `Startdate` | No | No | C90B234F855D4874B6727A1D6E974E5A |
| 353 | Ending Date | `Enddate` | No | No | C90B234F855D4874B6727A1D6E974E5A |
| 500 | Cost Center | `C_Costcenter_ID` | No | No | 8D71261F17854B44A75D9C894F751091 |
| 510 | 2nd Dimension | `User2_ID` | No | No | 8D71261F17854B44A75D9C894F751091 |
| 510 | 1st Dimension | `User1_ID` | No | No | 8D71261F17854B44A75D9C894F751091 |

### Model (ventana: Modelo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Mark (ventana: Marca)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Building (ventana: Building)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Dirección | `Direction` | No | No | — |

### Characteristics of Assets (ventana: Características de activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Search Key | `—` | No | No | — |
| 30 | Name | `—` | No | No | — |
| 40 | Asset Category | `—` | No | No | — |
| 50 | Document Type | `EM_Ssal_C_Doctype_ID` | No | Sí | — |
| 55 | Document No. | `—` | No | Sí | — |
| 63 | Description | `—` | No | No | — |
| 65 | Buque | `EM_Ssal_Isvessel` | No | No | — |
| 69 | Currency | `—` | No | No | — |
| 70 | Product | `—` | No | No | — |
| 80 | Summary Level | `—` | No | No | — |
| 85 | Static | `—` | No | No | — |
| 88 | State Asset | `EM_Ssal_State_Asset_ID` | No | No | — |
| 90 | Marca | `EM_Ssal_Mark_ID` | No | No | — |
| 100 | Serie | `EM_Ssal_Series` | No | No | — |
| 100 | Modelo | `EM_Ssal_Model_ID` | No | No | — |
| 140 | Usable Life - Years | `—` | No | Sí | — |
| 160 | Purchase Date | `—` | No | No | — |
| 170 | Cancellation Date | `—` | No | No | — |
| 200 | Project | `—` | No | No | — |
| 220 | Depreciation Amt. | `—` | No | Sí | — |
| 230 | Previously Depreciated Amt. | `—` | No | Sí | — |
| 310 | Asset Value | `—` | No | Sí | — |
| 320 | Residual Asset Value | `—` | No | Sí | — |
| 330 | Isavailable | `EM_Ssal_Isavailable` | No | Sí | — |
| 390 | Código de Barras | `EM_Ssal_Bar_Code` | No | No | — |
| 400 | Calculate Type | `—` | No | Sí | 111D1BFF30CC475F93AD4F406225566D |
| 410 | Amortize | `—` | No | Sí | 111D1BFF30CC475F93AD4F406225566D |
| 420 | Usable Life - Months | `—` | No | Sí | 111D1BFF30CC475F93AD4F406225566D |
| 520 | Custodio | `EM_Ssal_Custodio_ID` | No | No | — |
| 540 | Low reason | `EM_Ssal_Lowreason` | No | No | 3C3A75AFB6CA4DA6A75DD961988D0AAE |
| 550 | Low Date | `EM_Ssal_Lowdate` | No | No | 3C3A75AFB6CA4DA6A75DD961988D0AAE |
| 560 | Process Low Asset | `EM_Ssal_Lowprocess` | No | No | — |
| 570 | Low Status | `EM_Ssal_Lowstatus` | No | Sí | 3C3A75AFB6CA4DA6A75DD961988D0AAE |

### Movement (ventana: Características de activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | Sí | — |
| 30 | Product | `M_Product_ID` | No | Sí | — |
| 40 | Document Type | `C_Doctype_ID` | No | Sí | — |
| 80 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 90 | Date Request | `Date_Application` | No | Sí | — |
| 150 | Document No. | `Documentno` | No | Sí | — |
| 170 | Processed | `Processed` | No | Sí | — |
| 190 | Edifice | `Ssal_Building_ID` | No | Sí | — |
| 200 | Unit | `Ssal_Unit_ID` | No | Sí | — |
| 210 | Description Mov | `Description_Mov` | No | No | — |
| 210 | Department | `Ssal_Department_ID` | No | Sí | — |
| 230 | State | `State` | No | Sí | — |
| 240 | Asset | `A_Asset_ID` | No | Sí | — |
| 250 | Asset Category | `A_Asset_Group_ID` | No | Sí | — |
| 260 | Date Transaction | `Date_Transaction` | No | Sí | — |
| 261 | Custodian | `C_Custodian_ID` | No | Sí | C90B234F855D4874B6727A1D6E974E5A |
| 261 | C_Previous_Custodian_ID | `C_Previous_Custodian_ID` | No | Sí | C90B234F855D4874B6727A1D6E974E5A |
| 262 | Starting Date | `Startdate` | No | Sí | C90B234F855D4874B6727A1D6E974E5A |
| 263 | Ending Date | `Enddate` | No | Sí | C90B234F855D4874B6727A1D6E974E5A |
| 300 | Motive Return | `Motive_Return` | No | Sí | 039AB4AB73CF41C1B3FF2A1E8164633A |
| 310 | Date Asset Return | `Date_Return` | No | Sí | 039AB4AB73CF41C1B3FF2A1E8164633A |
| 320 | Doctype Return | `C_Doctype_Id_Return` | No | Sí | 039AB4AB73CF41C1B3FF2A1E8164633A |
| 330 | Documentno Return | `Documentno_Return` | No | Sí | 039AB4AB73CF41C1B3FF2A1E8164633A |
| 340 | IS_Return | `IS_Return` | No | No | 039AB4AB73CF41C1B3FF2A1E8164633A |
| 500 | Cost Center | `C_Costcenter_ID` | No | Sí | 8D71261F17854B44A75D9C894F751091 |
| 510 | 1st Dimension | `User1_ID` | No | Sí | 8D71261F17854B44A75D9C894F751091 |
| 520 | 2nd Dimension | `User2_ID` | No | Sí | 8D71261F17854B44A75D9C894F751091 |

### Fixed Assets Request OLD (ventana: Fixed Assets Request OLD)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 80 | Document Type | `C_Doctype_ID` | No | No | — |
| 85 | Document No. | `Documentno` | No | Sí | — |
| 90 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 100 | Date Request | `Date_Application` | No | No | — |
| 105 | Quantity | `Quantity` | No | No | — |
| 110 | Justification | `Justification` | No | No | — |
| 115 | Product | `M_Product_ID` | No | No | — |
| 150 | Description | `Description` | No | No | — |
| 200 | State | `State` | No | Sí | — |
| 280 | Process Request | `Process_Request` | No | No | — |
| 400 | Edifice | `Ssal_Building_ID` | No | No | 47BC13601657479785E4B5D632B167D6 |
| 410 | Unit | `Ssal_Unit_ID` | No | No | 47BC13601657479785E4B5D632B167D6 |
| 420 | Department | `Ssal_Department_ID` | No | No | 47BC13601657479785E4B5D632B167D6 |
| 500 | Cost Center | `C_Costcenter_ID` | No | No | 8D71261F17854B44A75D9C894F751091 |
| 510 | 1st Dimension | `User1_ID` | No | No | 8D71261F17854B44A75D9C894F751091 |
| 520 | 2nd Dimension | `User2_ID` | No | No | 8D71261F17854B44A75D9C894F751091 |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos típicos incluyen la aprobación y devolución de activos, con botones que permiten a los usuarios completar o rechazar transacciones. Frecuentemente se utilizan informes como el 'Informe de activos fijos' y el 'Print Delivery Asset', que permiten a los usuarios realizar seguimiento y documentación de los activos gestionados. Las validaciones comunes se ejecutan en función de botones, asegurando la integridad de los datos gestionados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.ecuador.asset.allocation.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | LoadActive2 | LoadActive2 | LoadActive2 | `ssal_transfer_assets` | ERROR=No existe Tipo de Documento configurado para la tabla Ssal_Appl_Active; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA REGISTRO ACTIVO | — |
| Botón (PL/pgSQL) | Proceso de baja activos | Process Low Asset | Process Low Asset | `ssal_low_equipment` | ERROR=EL ACTIVO NO SE HA DEPRECIADO COMPLETAMENTE; ERROR=CAMPO FECHA DE INICIO AMORTIZACION ES OBLIGATORIO; ERROR=CAMPO FECHA DE BAJA ES OBLIGATORIO; ERROR=FECHA DE BAJA DEBE SER MAYOR A LA FECHA DE DEPRECIACION | — |
| Botón (PL/pgSQL) | Retorno de activos | Create Lines Return Asset | Create Lines Return Asset | `ssal_generatelines_return` | raise exception '%','funcion2 '||V_BPARTNER_ID||' '||v_Client_ID||' '|| v_Org_ID||' '||v_User_ID; | — |
| Informe (servlet) | Aprobar Solicitud | Approved Resquest | ApprovedResquest | Java `Approved_state` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `Ssal_Appl_Active_ID` | `src/com/sidesoft/ecuador/asset/allocation/ad_process/Approved_state.java` |
| Informe (servlet) | Load Active | Load Active | LoadActive | Java `ReturnAssetsStore` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `Ssal_Asset_Return_ID` | `src/com/sidesoft/ecuador/asset/allocation/ad_process/ReturnAssetsStore.java` |
| Informe (servlet) | Procesar solicitud | Process Request | ChangeState | Java `change_state` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `Ssal_Active_Main_ID` | `src/com/sidesoft/ecuador/asset/allocation/ad_process/change_state.java` |
| Proceso / otro | Reporte Activos por custodio | Assets by Custodian | Assets by Custodian | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Asignación de activos | Report Asset Allocation | Report Asset Allocation | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Bajas de activos | Report Asset Low | Report Asset Low | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Componentes de activos | Report Asset Components | Report Asset Components | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Estado de activos | Assets Status | Assets Status | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte general de activos | Report General Active | Report General Active | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Movimiento de activos | Report Asset Movements | Report Asset Movements | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Solicitud de activos | Report Asset Request | Report Asset Request | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Verificación física de activos | Report Asset Physical Verification | Report Asset Physical Verification | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Informe de activos fijos | Report of Assets Fixed | Report of Assets Fixed | *(OBUIAPP / manual)* | Report of Assets Fixed | — |
| Reporte | Print Delivery Asset | Print Delivery Asset | Print Delivery Asset | Java `DeliveryAsset` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.jrxml`; contexto sesión `—`. | `src/com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.java` |
| Reporte | Print Report Act Receipt | Print Report Act Receipt | Print Report Act Receipt | Java `ActReception` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.jrxml`; contexto sesión `—`. | `src/com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.java` |
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
| Informe (servlet) | Aprobar Solicitud | `Approved_state` | Proceso Java (toolbar/background) | `Ssal_Appl_Active_ID` | — | `src/com/sidesoft/ecuador/asset/allocation/ad_process/Approved_state.java` |
| Informe (servlet) | Load Active | `ReturnAssetsStore` | Proceso Java (toolbar/background) | `Ssal_Asset_Return_ID` | — | `src/com/sidesoft/ecuador/asset/allocation/ad_process/ReturnAssetsStore.java` |
| Informe (servlet) | Procesar solicitud | `change_state` | Proceso Java (toolbar/background) | `Ssal_Active_Main_ID` | — | `src/com/sidesoft/ecuador/asset/allocation/ad_process/change_state.java` |
| Reporte | Print Delivery Asset | `DeliveryAsset` | Informe (servlet PDF) | `—` | com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.jrxml | `src/com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.java` |
| Reporte | Print Report Act Receipt | `ActReception` | Informe (servlet PDF) | `—` | com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.jrxml | `src/com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | LoadActive2 | LoadActive2 | LoadActive2 | `ssal_transfer_assets` | ERROR=No existe Tipo de Documento configurado para la tabla Ssal_Appl_Active; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA REGISTRO ACTIVO | — |
| Botón (PL/pgSQL) | Proceso de baja activos | Process Low Asset | Process Low Asset | `ssal_low_equipment` | ERROR=EL ACTIVO NO SE HA DEPRECIADO COMPLETAMENTE; ERROR=CAMPO FECHA DE INICIO AMORTIZACION ES OBLIGATORIO; ERROR=CAMPO FECHA DE BAJA ES OBLIGATORIO; ERROR=FECHA DE BAJA DEBE SER MAYOR A LA FECHA DE DEPRECIACION | — |
| Botón (PL/pgSQL) | Retorno de activos | Create Lines Return Asset | Create Lines Return Asset | `ssal_generatelines_return` | raise exception '%','funcion2 '||V_BPARTNER_ID||' '||v_Client_ID||' '|| v_Org_ID||' '||v_User_ID; | — |
| Informe (servlet) | Aprobar Solicitud | Approved Resquest | ApprovedResquest | Java `Approved_state` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `Ssal_Appl_Active_ID` | `src/com/sidesoft/ecuador/asset/allocation/ad_process/Approved_state.java` |
| Informe (servlet) | Load Active | Load Active | LoadActive | Java `ReturnAssetsStore` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `Ssal_Asset_Return_ID` | `src/com/sidesoft/ecuador/asset/allocation/ad_process/ReturnAssetsStore.java` |
| Informe (servlet) | Procesar solicitud | Process Request | ChangeState | Java `change_state` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `Ssal_Active_Main_ID` | `src/com/sidesoft/ecuador/asset/allocation/ad_process/change_state.java` |
| Proceso / otro | Reporte Activos por custodio | Assets by Custodian | Assets by Custodian | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Asignación de activos | Report Asset Allocation | Report Asset Allocation | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Bajas de activos | Report Asset Low | Report Asset Low | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Componentes de activos | Report Asset Components | Report Asset Components | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Estado de activos | Assets Status | Assets Status | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte general de activos | Report General Active | Report General Active | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Movimiento de activos | Report Asset Movements | Report Asset Movements | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Solicitud de activos | Report Asset Request | Report Asset Request | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Verificación física de activos | Report Asset Physical Verification | Report Asset Physical Verification | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | LoadActive2 | LoadActive2 | PL `ssal_transfer_assets` | ERROR=No existe Tipo de Documento configurado para la tabla Ssal_Appl_Active; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA REGISTRO ACTIVO | ERROR=No existe Tipo de Documento configurado para la tabla Ssal_Appl_Active; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA REGISTRO ACTIVO |
| Botón (PL/pgSQL) | Proceso de baja activos | Process Low Asset | PL `ssal_low_equipment` | ERROR=EL ACTIVO NO SE HA DEPRECIADO COMPLETAMENTE; ERROR=CAMPO FECHA DE INICIO AMORTIZACION ES OBLIGATORIO; ERROR=CAMPO FECHA DE BAJA ES OBLIGATORIO; ERROR=FECHA DE BAJA DEBE SER MAYOR A LA FECHA DE DEPRECIACION | ERROR=EL ACTIVO NO SE HA DEPRECIADO COMPLETAMENTE; ERROR=CAMPO FECHA DE INICIO AMORTIZACION ES OBLIGATORIO; ERROR=CAMPO FECHA DE BAJA ES OBLIGATORIO; ERROR=FECHA DE BAJA DEBE SER MAYOR A LA FECHA DE DEPRECIACION |
| Botón (PL/pgSQL) | Retorno de activos | Create Lines Return Asset | PL `ssal_generatelines_return` | raise exception '%','funcion2 '||V_BPARTNER_ID||' '||v_Client_ID||' '|| v_Org_ID||' '||v_User_ID; | raise exception '%','funcion2 '||V_BPARTNER_ID||' '||v_Client_ID||' '|| v_Org_ID||' '||v_User_ID; |
| Informe (servlet) | Aprobar Solicitud | Approved Resquest | Java `Approved_state` | Proceso Openbravo registro `Ssal_Appl_Active_ID` | Proceso Openbravo registro `Ssal_Appl_Active_ID` |
| Informe (servlet) | Load Active | Load Active | Java `ReturnAssetsStore` | Proceso Openbravo registro `Ssal_Asset_Return_ID` | Proceso Openbravo registro `Ssal_Asset_Return_ID` |
| Informe (servlet) | Procesar solicitud | Process Request | Java `change_state` | Proceso Openbravo registro `Ssal_Active_Main_ID` | Proceso Openbravo registro `Ssal_Active_Main_ID` |
| Proceso / otro | Reporte Activos por custodio | Assets by Custodian | — | — | — |
| Proceso / otro | Reporte Asignación de activos | Report Asset Allocation | — | — | — |
| Proceso / otro | Reporte Bajas de activos | Report Asset Low | — | — | — |
| Proceso / otro | Reporte Componentes de activos | Report Asset Components | — | — | — |
| Proceso / otro | Reporte Estado de activos | Assets Status | — | — | — |
| Proceso / otro | Reporte general de activos | Report General Active | — | — | — |
| Proceso / otro | Reporte Movimiento de activos | Report Asset Movements | — | — | — |
| Proceso / otro | Reporte Solicitud de activos | Report Asset Request | — | — | — |
| Proceso / otro | Reporte Verificación física de activos | Report Asset Physical Verification | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Informe de activos fijos | Report of Assets Fixed | Report of Assets Fixed | *(OBUIAPP / manual)* | Report of Assets Fixed | — |
| Reporte | Print Delivery Asset | Print Delivery Asset | Print Delivery Asset | Java `DeliveryAsset` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.jrxml`; contexto sesión `—`. | `src/com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.java` |
| Reporte | Print Report Act Receipt | Print Report Act Receipt | Print Report Act Receipt | Java `ActReception` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.jrxml`; contexto sesión `—`. | `src/com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 13**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **3**; archivos `*.jrxml` en el repo = **13**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Informe de activos fijos | `Report of Assets Fixed` | — | *(ver AD_PROCESS_PARA / servlet)* | Report of Assets Fixed |
| 2 | Print Delivery Asset | `Print Delivery Asset` | Java `DeliveryAsset`; JRXML `src/com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | Print Delivery Asset. JRXML: `src/com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.jrxml` |
| 3 | Print Report Act Receipt | `Print Report Act Receipt` | Java `ActReception`; JRXML `src/com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.jrxml`, `src/com/sidesoft/ecuador/asset/allocation/ReportActReception/Rpt_ActReceipt.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | Print Report Act Receipt. JRXML: `src/com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.jrxml` |

### Plantillas sin proceso en diccionario

- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/ReportAssetAllocation.jrxml`
- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/ReportAssetComponents.jrxml`
- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/ReportAssetMovements.jrxml`
- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/ReportAssetRequest.jrxml`
- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/ReportGeneralActive.jrxml`
- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/ReportLowAsset.jrxml`
- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/Rpt_AssetPhysicalVerification.jrxml`
- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/Rpt_AssetState.jrxml`
- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/Rpt_AssetbyCustodian.jrxml`
- `src/com/sidesoft/ecuador/asset/allocation/ad_reports/Rpt_AssetsFixed.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Ssal_Error_Approved` | This asset is assigned to other custodian | This asset is assigned to other custodian | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssal_Title_Approved_Error` | Failed to approve the Active | Failed to approve the Active | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye varias clases Java que son responsables de la generación de informes y la gestión de la interfaz de usuario, como 'DeliveryAsset' y 'ActReception', que permiten la creación de reportes a partir de los datos almacenados en la base de datos del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.ecuador.asset.allocation`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ActReception` | ReportActReception | HttpSecureAppServlet | — | `src/com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.java` |
| `DeliveryAsset` | ReportDeliveryAsset | HttpSecureAppServlet | — | `src/com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.java` |
| `Add_taxid` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/ecuador/asset/allocation/ad_callouts/Add_taxid.java` |
| `SS_Asset` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/ecuador/asset/allocation/ad_callouts/SS_Asset.java` |
| `SearchIdentifierProductAsset` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/ecuador/asset/allocation/ad_callouts/SearchIdentifierProductAsset.java` |
| `UpdateNumber` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/ecuador/asset/allocation/ad_callouts/UpdateNumber.java` |
| `UpdateNumberRequest` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/ecuador/asset/allocation/ad_callouts/UpdateNumberRequest.java` |
| `Approved_state` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/ecuador/asset/allocation/ad_process/Approved_state.java` |
| `ReturnAssetsStore` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/ecuador/asset/allocation/ad_process/ReturnAssetsStore.java` |
| `change_state` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/ecuador/asset/allocation/ad_process/change_state.java` |
| `UpdateNumberRequestEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/ecuador/asset/allocation/event/UpdateNumberRequestEvent.java` |
| `UpdateSequenceNumberEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/ecuador/asset/allocation/event/UpdateSequenceNumberEvent.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSAL_CUSTODIO_TRG` | `a_asset` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `filetr fixed` | `Ssal_Appl_Active.C_Bpartner_ID = @C_Bpartner_ID@ AND  Ssal_Appl_Active.IS_Return='N'` |
| AD_VAL_RULE | — | `filter doct type return` | `C_Doctype.DocBaseType = 'SSAL_RETURN'` |
| AD_VAL_RULE | — | `filter cod assets` | `A_Asset.A_Asset_ID = @A_Asset_ID@` |
| AD_VAL_RULE | — | `filter asset return` | `—` |
| AD_VAL_RULE | — | `filter fixed assets request` | `C_Doctype.DocBaseType = 'SSAL_FIXED'` |
| AD_VAL_RULE | — | `filter for category return` | `Ssal_Appl_Active.Ssal_Appl_Active_ID = @Ssal_Appl_Active_ID@` |
| AD_VAL_RULE | — | `filetr fixed lines` | `Ssal_Appl_Active.C_Bpartner_ID in (select C_Bpartner_ID from ssal_asset_return where ssal_asset_return_id = @ssal_asset_` |
| AD_VAL_RULE | — | `Ssal_Custodian_Validate_Isemployee` | `C_Bpartner.isemployee='Y'` |
| AD_VAL_RULE | — | `validation assets` | `c_doctype.AD_TABLE_ID IN (

SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(tablename) = UPPER('A_Asset'))` |
| AD_VAL_RULE | — | `Logged User` | `ad_user.ad_user_id =@#ad_user_id@` |
| AD_VAL_RULE | — | `filter category asset` | `A_Asset.A_Asset_Group_ID = @A_Asset_Group_ID@` |
| AD_VAL_RULE | — | `Valdation for return Assets` | `C_Doctype.C_Doctype_ID = 'C64CEB6196B74809BE7BE4A9B3E3C2C3'` |
| Java event/validator | `UpdateNumberRequestEvent` | persistencia/UI | *(leer `src/com/sidesoft/ecuador/asset/allocation/event/UpdateNumberRequestEvent.java`)* |
| Java event/validator | `UpdateSequenceNumberEvent` | persistencia/UI | *(leer `src/com/sidesoft/ecuador/asset/allocation/event/UpdateSequenceNumberEvent.java`)* |
| Función PL `ssal_generatelines_return` | — | invocación proceso | raise exception '%','funcion2 '||V_BPARTNER_ID||' '||v_Client_ID||' '|| v_Org_ID||' '||v_User_ID; |
| Función PL `ssal_low_equipment` | — | invocación proceso | ERROR=EL ACTIVO NO SE HA DEPRECIADO COMPLETAMENTE; ERROR=CAMPO FECHA DE INICIO AMORTIZACION ES OBLIGATORIO; ERROR=CAMPO FECHA DE BAJA ES OBLIGATORIO |
| Función PL `ssal_transfer_assets` | — | invocación proceso | ERROR=No existe Tipo de Documento configurado para la tabla Ssal_Appl_Active; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA REGISTRO ACTIVO |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL son esenciales para el soporte del módulo, ya que permiten la validación automática y la integración de procesos en la base de datos. Con solo un trigger, se asegura que las reglas de negocio se apliquen de forma correcta durante las operaciones de inserción y actualización en la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSAL_CUSTODIO_TRG` | `a_asset` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSAL_CUSTODIO_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssal_generatelines_return` | Retorno de activos | raise exception '%','funcion2 '||V_BPARTNER_ID||' '||v_Client_ID||' '|| v_Org_ID||' '||v_User_ID; | raise exception '%','funcion2 '||V_BPARTNER_ID||' '||v_Client_ID||' '|| v_Org_ID||' '||v_User_ID; | `model/functions/SSAL_GENERATELINES_RETURN.xml` |
| `ssal_low_equipment` | Proceso de baja activos | ERROR=EL ACTIVO NO SE HA DEPRECIADO COMPLETAMENTE; ERROR=CAMPO FECHA DE INICIO AMORTIZACION ES OBLIGATORIO; ERROR=CAMPO FECHA DE BAJA ES OBLIGATORIO; ERROR=FECHA DE BAJA DEBE SER MAYOR A LA FECHA DE DEPRECIACION | ERROR=EL ACTIVO NO SE HA DEPRECIADO COMPLETAMENTE; ERROR=CAMPO FECHA DE INICIO AMORTIZACION ES OBLIGATORIO; ERROR=CAMPO FECHA DE BAJA ES OBLIGATORIO; ERROR=FECHA DE BAJA DEBE SER MAYOR A LA FECHA DE DEPRECIACION | `model/functions/SSAL_LOW_EQUIPMENT.xml` |
| `ssal_transfer_assets` | LoadActive2 | ERROR=No existe Tipo de Documento configurado para la tabla Ssal_Appl_Active; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA REGISTRO ACTIVO | ERROR=No existe Tipo de Documento configurado para la tabla Ssal_Appl_Active; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA REGISTRO ACTIVO | `model/functions/SSAL_TRANSFER_ASSETS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LoadActive2 | `LoadActive2` | Botón (PL/pgSQL) | PL `ssal_transfer_assets` | N | ERROR=No existe Tipo de Documento configurado para la tabla Ssal_Appl_Active; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA REGISTRO ACTIVO |
| 2 | Proceso de baja activos | `Process Low Asset` | Botón (PL/pgSQL) | PL `ssal_low_equipment` | N | ERROR=EL ACTIVO NO SE HA DEPRECIADO COMPLETAMENTE; ERROR=CAMPO FECHA DE INICIO AMORTIZACION ES OBLIGATORIO; ERROR=CAMPO FECHA DE BAJA ES OBLIGATORIO; ERROR=FECHA DE BAJA DEBE SER M |
| 3 | Retorno de activos | `Create Lines Return Asset` | Botón (PL/pgSQL) | PL `ssal_generatelines_return` | N | raise exception '%','funcion2 '||V_BPARTNER_ID||' '||v_Client_ID||' '|| v_Org_ID||' '||v_User_ID; |
| 4 | Aprobar Solicitud | `ApprovedResquest` | Informe (servlet) | Java `Approved_state` | N | Proceso Openbravo registro `Ssal_Appl_Active_ID` |
| 5 | Load Active | `LoadActive` | Informe (servlet) | Java `ReturnAssetsStore` | N | Proceso Openbravo registro `Ssal_Asset_Return_ID` |
| 6 | Procesar solicitud | `ChangeState` | Informe (servlet) | Java `change_state` | N | Proceso Openbravo registro `Ssal_Active_Main_ID` |
| 7 | Informe de activos fijos | `Report of Assets Fixed` | Reporte | — | S | Report of Assets Fixed |
| 8 | Print Delivery Asset | `Print Delivery Asset` | Reporte | Java `DeliveryAsset` | S | Genera PDF desde JRXML `com/sidesoft/ecuador/asset/allocation/ReportDeliveryAsset/DeliveryAsset.jrxml`; contexto sesión `—`. |
| 9 | Print Report Act Receipt | `Print Report Act Receipt` | Reporte | Java `ActReception` | S | Genera PDF desde JRXML `com/sidesoft/ecuador/asset/allocation/ReportActReception/ActReception.jrxml`; contexto sesión `—`. |

**Total acciones documentadas (extract):** **9** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `com.sidesoft.ecuador.asset.allocation`.

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

# Glosario — prefijo `SSAL`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSAL` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.ecuador.asset.allocation` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `LoadActive2` — LoadActive2
- `Process Low Asset` — Proceso de baja activos
- `Create Lines Return Asset` — Retorno de activos
- `ApprovedResquest` — Aprobar Solicitud
- `LoadActive` — Load Active
- `ChangeState` — Procesar solicitud
- `Assets by Custodian` — Reporte Activos por custodio
- `Report Asset Allocation` — Reporte Asignación de activos
- `Report Asset Low` — Reporte Bajas de activos
- `Report Asset Components` — Reporte Componentes de activos
- `Assets Status` — Reporte Estado de activos
- `Report General Active` — Reporte general de activos
- `Report Asset Movements` — Reporte Movimiento de activos
- `Report Asset Request` — Reporte Solicitud de activos
- `Report Asset Physical Verification` — Reporte Verificación física de activos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Change Translation Assets Field
**Package:** `com.sidesoft.ecuador.asset.changetranslation`

# Module overview — Change Translation Assets Field

## Functional

El módulo 'Change Translation Assets Field' permite a los usuarios realizar modificaciones en los campos de traducción de los activos registrados en el sistema Openbravo. Está diseñado para usuarios de negocios que necesitan personalizar la información de activos, así como para el soporte técnico que gestiona y mantiene las configuraciones necesarias. Este módulo no posee dependencias externas y su implementación es autocontenida dentro del ecosistema de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/ecuador/asset/changetranslation` |
| Web | `web/com.sidesoft.ecuador.asset.changetranslation/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SEACT`

# Guía de chat — Change Translation Assets Field

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.ecuador.asset.changetranslation`).

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
- «¿Qué es la tabla seact_asset_setup?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo cambiar la traducción de un activo?
- ¿Qué pasos debo seguir para configurar un nuevo campo de traducción?
- ¿Qué impacto tiene utilizar el módulo en la integridad de los datos de los activos?
- ¿Existen restricciones al modificar activos existentes?
- ¿Puedo revertir un cambio realizado en la traducción de un activo?
- ¿Cómo obtengo asistencia si encuentro errores al usar el módulo?
- ¿Qué sucede si no se activa el trigger después de realizar cambios?
- ¿Hay algún límite en la cantidad de activos que puedo modificar a la vez?

# Domain — data model

## Functional

El modelo de datos está centrado en la tabla 'seact_asset_setup', que actúa como la entidad cabecera donde se almacenan múltiples configuraciones relacionadas con los activos. Al utilizar este módulo, un registro de activo puede ser modificado para actualizar su traducción, lo que implica una relación directa con el trigger 'SEACT_ASSET_SETUP_TRG'. Este trigger asegura que las actualizaciones en la tabla de activos se reflejen adecuadamente en el sistema, ejecutando una rutina PL/pgSQL para mantener la integridad de los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `seact_asset_setup` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `seact_asset_setup` | seact_asset_setup | `SEACT_ASSET_SETUP_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype | Detalle enlazado a ad_client, ad_org, c_doctype. Validado por trigger(s): SEACT_ASSET_SETUP_TRG. | PK `seact_asset_setup_key`; Cols: c_doctype_id, depreciation; `SEACT_ASSET_SETUP_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `seact_asset_setup` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`A_ASSET`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación por el módulo se realiza a través de la ventana de 'Configuración activos'. Desde esta interfaz, los usuarios pueden acceder a los campos que pueden ser editados, permitiéndoles ajustar la información de traducción de los activos. La interfaz es intuitiva y permite un acceso rápido a las funcionalidades requeridas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.ecuador.asset.changetranslation.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuración activos | Asset Setup |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración activos | Asset Setup | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.ecuador.asset.changetranslation.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuración activos

- **AD_WINDOW_ID:** `019552C6AFC14DD89A9F3E40DBC3BBC6`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Asset Setup | `81C6D74B7F574DAAB67E5B033041D27B` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 560 | Low reason | `—` | No | No | — |
| 570 | Low Date | `—` | No | No | — |
| 580 | Low Status | `—` | No | No | — |
| 590 | State Asset | `—` | No | No | — |
| — | SEACT Reactivate | `em_seact_abreactivate` | No | No | — |
| — | SEACT Process | `em_seact_abprocess` | No | No | — |

### Asset Setup (ventana: Configuración activos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | C_Doctype_ID | `C_Doctype_ID` | No | No | — |
| 40 | Depreciation | `Depreciation` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dentro del módulo, los botones típicos incluyen 'Completar' y 'Retornar', que permiten finalizar la edición de un activo o volver a la vista anterior. No se contemplan procesos de reporte, pero sí se realizan validaciones frecuentes al guardar cambios, asegurando que los datos introducidos cumplan con los estándares definidos en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.ecuador.asset.changetranslation.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Procesar | SEACT Process | em_seact_abprocess | `em_seact_abprocess` | Process | — |
| Botón (PL/pgSQL) | Reactivar | SEACT Reactivate | em_seact_abreactivate | `em_seact_abreactivate` | Reactivate | — |
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
| Botón (PL/pgSQL) | Procesar | SEACT Process | em_seact_abprocess | `em_seact_abprocess` | Process | — |
| Botón (PL/pgSQL) | Reactivar | SEACT Reactivate | em_seact_abreactivate | `em_seact_abreactivate` | Reactivate | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Procesar | SEACT Process | PL `em_seact_abprocess` | Process | — |
| Botón (PL/pgSQL) | Reactivar | SEACT Reactivate | PL `em_seact_abreactivate` | Reactivate | — |
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
| `SEACT_AnotherActiveConfiguration` | There is another active configuration | There is another active configuration | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SEACT_DoctypeNotDefined` | A document type must be configured for Asset Depreciation | A document type must be configured for Asset Depreciation | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo 'Change Translation Assets Field' no contiene clases Java, lo que implica que toda la lógica se manipula a través de sus funcionalidades PL/pgSQL y triggers asociados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.ecuador.asset.changetranslation`.

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
| Trigger `SEACT_ASSET_SETUP_TRG` | `seact_asset_setup` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL son elementos clave para el soporte del módulo, facilitando la ejecución lógica necesaria para las modificaciones de la tabla 'seact_asset_setup'. El trigger 'SEACT_ASSET_SETUP_TRG' se activa para asegurar que las actualizaciones en el inventario de activos se manejen correctamente, manteniendo la coherencia de los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SEACT_ASSET_SETUP_TRG` | `seact_asset_setup` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SEACT_ASSET_SETUP_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `seact_abprocess` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SEACT_ABPROCESS.xml` |
| `seact_abreactivate` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SEACT_ABREACTIVATE.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Procesar | `em_seact_abprocess` | Botón (PL/pgSQL) | PL `em_seact_abprocess` | N | Process |
| 2 | Reactivar | `em_seact_abreactivate` | Botón (PL/pgSQL) | PL `em_seact_abreactivate` | N | Reactivate |

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

Módulo: `com.sidesoft.ecuador.asset.changetranslation`.

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

# Glosario — prefijo `SEACT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SEACT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.ecuador.asset.changetranslation` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `em_seact_abprocess` — Procesar
- `em_seact_abreactivate` — Reactivar

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Asset Move
**Package:** `com.sidesoft.ecuador.asset.move`

# Module overview — Asset Move

## Functional

El módulo 'Asset Move' tiene como propósito gestionar la baja y enajenación de activos fijos dentro de un sistema ERP. Este funcionalidad es esencial para los departamentos de contabilidad y finanzas, donde los activos deben ser dados de baja de manera adecuada y registrada la información de su enajenación. Los actores principales incluyen a los contadores, administradores de activos y usuarios del área financeira. Este módulo depende de la compatibilidad con la 'Core' y la '2.50 to 3.00 Compatibility Skin'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/ecuador/asset/move` |
| Web | `web/com.sidesoft.ecuador.asset.move/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSAM`

# Guía de chat — Asset Move

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.ecuador.asset.move`).

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
- «¿Qué es la tabla ssam_alienate?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo dar de baja un activo fijo?
- ¿Qué pasos debo seguir para registrar una enajenación?
- ¿Qué tipo de motivo de enajenación está permitido?
- ¿Cómo se valida un activo antes de su enajenación?
- ¿Puedo revertir una baja de activo una vez registrada?
- ¿Dónde puedo consultar la contabilidad de un activo enajenado?
- ¿Qué información debo proporcionar al registrar un motivo de enajenación?
- ¿Cómo afecta la baja de un activo a mis estados financieros?

# Domain — data model

## Functional

La entidad cabecera para este módulo es 'ssam_alienate', que recoge todas las transacciones relativas a la baja de activos. Este módulo sigue un flujo de procesos que abarca desde la creación de un registro de baja hasta su validación y contabilización. Las tablas principales incluyen 'A_ASSET', que contiene los datos de los activos, y 'C_INVOICELINE', relevante para las lineas de facturación asociadas. Triggers como 'SSAM_POST_ALIENATE_TRG' y 'SSAM_VALIDATE_ASSET_TRG' aseguran la integridad y validación de datos durante el proceso de enajenación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssam_alienate` |
| `ssam_alienateline` |
| `ssam_reason_alienate` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssam_alienate` | ssam_alienate | `SSAM_POST_ALIENATE_TRG` | `SSAM_ALIENATE_DOCNO_UN` (documentno) | a_assetend_id→a_asset; a_assetstart_id→a_asset; c_doctype_id→c_doctype; ad_org_id→ad_org; c_bpartner_id→c_bpartner (+2) | Detalle enlazado a a_asset, c_doctype. Validado por trigger(s): SSAM_POST_ALIENATE_TRG. | PK `ssam_alienate_key`; Cols: documentno, processed, description, posted, processing; `SSAM_ALIENATE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssam_alienateline` | ssam_alienateline | `SSAM_POST_ALIENATETLINE_TRG` | — | ssam_alienate_id→ssam_alienate; a_asset_id→a_asset; ad_client_id→ad_client; a_asset_group_id→a_asset_group; ad_org_id→ad_org (+1) | Detalle enlazado a a_asset, ad_client, ssam_alienate. Validado por trigger(s): SSAM_POST_ALIENATETLINE_TRG. | PK `ssam_alie_line_key`; Cols: line, status, alienatedate, ssam_alienate_id, a_asset_id; `SSAM_ALIE_LINE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssam_reason_alienate` | ssam_reason_alienate | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssam_rea_alienate_key`; Cols: reason, description, typereason, use_transit_account; `SSAM_REAALI_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssam_alienate` |
| `ssam_alienateline` |
| `ssam_reason_alienate` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`A_AMORTIZATIONLINE`, `A_ASSET`, `A_ASSET_ACCT`, `A_ASSET_GROUP_ACCT`, `C_ELEMENTVALUE`, `C_INVOICELINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de dos ventanas principales: 'Baja / Enajenación de activos fijos' y 'Motivos de Enajenación'. Estas ventanas permiten a los usuarios acceder a las funcionalidades necesarias para registrar y gestionar la baja de activos fijos de manera efectiva.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.ecuador.asset.move.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Baja / Enajenación de activos fijos | Alienate Assets |
| Motivos de Enajenación | Reasons Alienate |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Baja / Enajenación de activos fijos | Alienate Assets | No |
| Certificado de entrega / recepción de activos | Certificate of Asset Delivery/Receipt | No |
| Depreciación de Activos | Depreciation Assets | No |
| Enajenación por Motivo | Alienate by Reason | No |
| Informe de Activos Fijos Relacionados | Related Fixed Assets | No |
| Motivos de Enajenación | Reasons Alienate | No |
| Reporte Activos con facturas en espera | Asset Waiting Invoice | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.ecuador.asset.move.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Baja / Enajenación de activos fijos

- **AD_WINDOW_ID:** `4D8410A8736C4C62AACEDE8507B0517C`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Alienate Assets | `FC1F2D243F8D4FD1B5562F9B37CECB12` | 0 |
| 20 | Line | `89DA68C2352A4F869D99807DB6B4C458` | 1 |

### Ventana: Motivos de Enajenación

- **AD_WINDOW_ID:** `A0C5A79612104C6686E913F535F50EBC`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Reason Alienate | `8F669AEB282F4899867B7228E7DABF5F` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `132`

- **AD_TAB_ID:** `132` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 117 | Fixed Asset | `EM_Ssam_Asset` | No | No | — |

### Pestaña `270`

- **AD_TAB_ID:** `270` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 69 | Is Asset | `EM_Ssam_Asset` | No | No | — |
| 70 | Asset / Alienate | `EM_Ssam_Assetalienate` | No | No | — |
| 71 | Asset | `EM_Ssam_A_Asset_ID` | No | No | — |
| 72 | Asset Alienate | `EM_Ssam_Alienate_ID` | No | No | — |
| 73 | Asset Alienate Line | `EM_Ssam_Alienateline_ID` | No | No | — |

### Reason Alienate (ventana: Motivos de Enajenación)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Reason | `Reason` | No | No | — |
| 40 | Type Reason Alienate | `Typereason` | No | No | — |
| 50 | Description Alienate | `Description` | No | No | — |
| 60 | USE_Transit_Account | `USE_Transit_Account` | No | No | — |

### Pestaña `800077`

- **AD_TAB_ID:** `800077` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 60 | Type of change | `EM_Ssam_Typeofchange` | No | Sí | — |
| 2050 | Asset Group | `EM_Ssam_A_Asset_Group_ID` | No | No | — |

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 35 | Status | `EM_Ssam_Status` | No | Sí | — |
| 55 | Asset Type | `EM_Ssam_Assettype` | No | No | — |
| 61 | Additional description | `EM_Ssam_Add_Description` | No | No | — |
| 255 | Condition | `EM_Ssam_Condition` | No | No | — |
| 260 | Correspondent | `EM_Ssam_C_Bpartner_ID` | No | No | — |
| 270 | Identificador | `EM_Ssam_Taxid` | No | Sí | — |
| 280 | Net Worth | `EM_Ssam_Net_Worth` | No | Sí | — |
| 290 | Model | `EM_Ssam_Model` | No | No | — |
| 300 | Serie | `EM_Ssam_Serie` | No | No | — |
| 301 | Brand | `EM_Ssam_Brand` | No | No | — |
| 330 | Replacement Value | `EM_Ssam_Replacement_Value` | No | No | — |
| 350 | Alienate Line | `EM_Ssam_Alienateline_ID` | No | Sí | — |
| 445 | Value In Books | `EM_Ssam_Value_In_Books` | No | No | 54712E7EFB254D9CB6137B6AAEE76927 |
| 450 | Change of value | `EM_Ssam_Changeofvalue` | No | No | — |
| 530 | Type of change | `EM_Ssam_Typeofchange` | No | No | 54712E7EFB254D9CB6137B6AAEE76927 |
| 540 | Observations | `EM_Ssam_Observations` | No | No | 54712E7EFB254D9CB6137B6AAEE76927 |
| 550 | Reference | `EM_Ssam_Reference` | No | No | — |

### Pestaña `800190`

- **AD_TAB_ID:** `800190` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 70 | Sales of Asset | `EM_Ssam_Sales_Acct` | No | No | — |
| 80 | Historic Cost | `EM_Ssam_Historiccost_Acct` | No | No | — |
| 90 | Alienate Result | `EM_Ssam_Resultalienate_Acct` | No | No | — |

### Pestaña `800204`

- **AD_TAB_ID:** `800204` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 80 | Sales of Asset | `EM_Ssam_Sales_Acct` | No | No | — |
| 90 | Historic Cost | `EM_Ssam_Historiccost_Acct` | No | No | — |
| 100 | Alienate Result | `EM_Ssam_Resultalienate_Acct` | No | No | — |

### Alienate Assets (ventana: Baja / Enajenación de activos fijos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Process Alienate | `Processed` | No | No | — |
| 50 | Description Alienate | `Description` | No | No | — |
| 60 | Posted | `Posted` | No | No | — |
| 80 | Document No. | `Documentno` | No | No | — |
| 100 | Type Reason Alienate | `Typereason` | No | No | — |
| 110 | Reason Alienate | `Ssam_Reason_Alienate_ID` | No | No | — |
| 120 | Create Lines Alienate | `Createline` | No | No | — |
| 130 | Document Date | `Datedoc` | No | No | — |
| 140 | Start Asset | `A_Assetstart_ID` | No | No | — |
| 150 | End Asset | `A_Assetend_ID` | No | No | — |
| 160 | Beneficiary | `C_Bpartner_ID` | No | No | — |

### Pestaña `C2E8978199C34A94A105EE7282EB5E84`

- **AD_TAB_ID:** `C2E8978199C34A94A105EE7282EB5E84` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 105 | Replacement Value | `EM_Ssam_Replacement_Value` | No | Sí | — |

### Line (ventana: Baja / Enajenación de activos fijos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | Sí | — |
| 30 | Line No. | `Line` | No | Sí | — |
| 40 | Complete Alienate | `Status` | No | Sí | — |
| 50 | Alienate Date | `Alienatedate` | No | Sí | — |
| 70 | Asset | `A_Asset_ID` | No | Sí | — |
| 80 | Asset Group | `A_Asset_Group_ID` | No | Sí | — |
| 90 | Depreciation End Date | `Amortizationenddate` | No | Sí | — |
| 100 | Depreciation Start Date | `Amortizationstartdate` | No | Sí | — |
| 110 | Amortization Type | `Amortizationtype` | No | Sí | — |
| 120 | Calculate Type | `Amortizationcalctype` | No | Sí | — |
| 130 | Cancellation Date | `Datecancelled` | No | Sí | — |
| 140 | Purchase Date | `Datepurchased` | No | Sí | — |
| 150 | Asset Value | `Assetvalueamt` | No | Sí | — |
| 160 | Amortization Value | `Amortizationvalue` | No | Sí | — |
| 170 | Net Value | `Netvalue` | No | Sí | — |
| 180 | Description Alienate | `Description` | No | Sí | — |
| 190 | Invoice | `C_Invoice_ID` | No | Sí | — |
| 200 | Replacement Value | `Replacement_Value` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Entre los procesos disponibles, los botones típicos que los usuarios pueden encontrar son: completar, retornar o rechazar un registro de baja de activos. Aunque no se incluyen informes específicos dentro del módulo, las validaciones frecuentes garantizan que se cumplan las restricciones de negocio, como la verificación del activo y sus cuentas contables asociadas antes de confirmar la enajenación. Estos procesos son cruciales para mantener una contabilidad precisa y actualizada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.ecuador.asset.move.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Depreciación de Activos | Depreciation Assets | Depreciation Assets | Java `ProcessBatchDepreciationAssets` (AD_MODEL_OBJECT `P`) | Proceso Openbravo ver `doExecute` en fuente | `src/com/sidesoft/ecuador/asset/move/ad_process/ProcessBatchDepreciationAssets.java` |
| Botón (PL/pgSQL) | Crear lineas de enajenación | Create Lines Alienate | Create Lines Alienate | `ssam_create_alienate` | ACTUALIZA EL ESTADO DE LA ENAJEACION A DESPROCESADO; ACTUALIZA EL ESTADO DE LA ENAJEACION A PROCESADO; v_Message := '@sspr_RowsInsertedwarning@: ' || v_n_insertions; | — |
| Botón (PL/pgSQL) | Procesar enajenación | Process Alienate | Process Alienate | `ssam_process_alienate` | No existe configración en el campo Tipo de Activo:; El activo es un bien de control y no debe tener datos de Amortización”:; Existes Amortizaciones contabilizadas futuras a la fecha de Enajenación:; Existes Amortizacion… | — |
| Informe (servlet) | Generar plan de depreciación | Generate Amortizacion Plan Asset Move | Generate Amortizacion Plan Asset Move | Java `AssetLinearDepreciationMethodProcess` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `A_Asset_ID` | `src/com/sidesoft/ecuador/asset/move/amortization/AssetLinearDepreciationMethodProcess.java` |
| Proceso / otro | Certificado de entrega / recepción de activos | Certificate of Asset Delivery/Receipt | Certificate of Asset Delivery/Receipt | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Enajenación por Motivo | Alienate by Reason | Alienate by Reason | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Informe de Activos Fijos Relacionados | Related Fixed Assets | Related Fixed Assets | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Activos con facturas en espera | Asset Waiting Invoice | Asset Waiting Invoice | *(OBUIAPP / manual)* | Asset Waiting Invoice | — |
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
| Botón (Java) | Depreciación de Activos | `ProcessBatchDepreciationAssets` | Proceso Java (toolbar/background) | `—` | — | `src/com/sidesoft/ecuador/asset/move/ad_process/ProcessBatchDepreciationAssets.java` |
| Informe (servlet) | Generar plan de depreciación | `AssetLinearDepreciationMethodProcess` | Proceso Java (toolbar/background) | `A_Asset_ID` | — | `src/com/sidesoft/ecuador/asset/move/amortization/AssetLinearDepreciationMethodProcess.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Depreciación de Activos | Depreciation Assets | Depreciation Assets | Java `ProcessBatchDepreciationAssets` (AD_MODEL_OBJECT `P`) | Proceso Openbravo ver `doExecute` en fuente | `src/com/sidesoft/ecuador/asset/move/ad_process/ProcessBatchDepreciationAssets.java` |
| Botón (PL/pgSQL) | Crear lineas de enajenación | Create Lines Alienate | Create Lines Alienate | `ssam_create_alienate` | ACTUALIZA EL ESTADO DE LA ENAJEACION A DESPROCESADO; ACTUALIZA EL ESTADO DE LA ENAJEACION A PROCESADO; v_Message := '@sspr_RowsInsertedwarning@: ' || v_n_insertions; | — |
| Botón (PL/pgSQL) | Procesar enajenación | Process Alienate | Process Alienate | `ssam_process_alienate` | No existe configración en el campo Tipo de Activo:; El activo es un bien de control y no debe tener datos de Amortización”:; Existes Amortizaciones contabilizadas futuras a la fecha de Enajenación:; Existes Amortizacion… | — |
| Informe (servlet) | Generar plan de depreciación | Generate Amortizacion Plan Asset Move | Generate Amortizacion Plan Asset Move | Java `AssetLinearDepreciationMethodProcess` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `A_Asset_ID` | `src/com/sidesoft/ecuador/asset/move/amortization/AssetLinearDepreciationMethodProcess.java` |
| Proceso / otro | Certificado de entrega / recepción de activos | Certificate of Asset Delivery/Receipt | Certificate of Asset Delivery/Receipt | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Enajenación por Motivo | Alienate by Reason | Alienate by Reason | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Informe de Activos Fijos Relacionados | Related Fixed Assets | Related Fixed Assets | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Activos con facturas en espera | Asset Waiting Invoice | Asset Waiting Invoice | *(OBUIAPP / manual)* | Asset Waiting Invoice | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Depreciación de Activos | Depreciation Assets | Java `ProcessBatchDepreciationAssets` | Proceso Openbravo ver `doExecute` en fuente | Proceso Openbravo ver `doExecute` en fuente |
| Botón (PL/pgSQL) | Crear lineas de enajenación | Create Lines Alienate | PL `ssam_create_alienate` | ACTUALIZA EL ESTADO DE LA ENAJEACION A DESPROCESADO; ACTUALIZA EL ESTADO DE LA ENAJEACION A PROCESADO; v_Message := '@sspr_RowsInsertedwarning@: ' || v_n_insertions; | ACTUALIZA EL ESTADO DE LA ENAJEACION A DESPROCESADO; ACTUALIZA EL ESTADO DE LA ENAJEACION A PROCESADO; v_Message := '@sspr_RowsInsertedwarning@: ' || v_n_insertions; |
| Botón (PL/pgSQL) | Procesar enajenación | Process Alienate | PL `ssam_process_alienate` | No existe configración en el campo Tipo de Activo:; El activo es un bien de control y no debe tener datos de Amortización”:; Existes Amortizaciones contabilizadas futuras a la fecha de Enajenación:; Existes Amortizacion… | No existe configración en el campo Tipo de Activo:; El activo es un bien de control y no debe tener datos de Amortización”:; Existes Amortizaciones contabilizadas futuras a la fecha de Enajenación:; Existes Amortizaciones anteriores sin contabilizar:; EJECUTA VALIDACIONES EN LA LÍNEAS DE ACTIVOS; VALIDA QUE EXISTA CONFIGURACION EN EL CAMPO TIPO DE ACTIVO |
| Informe (servlet) | Generar plan de depreciación | Generate Amortizacion Plan Asset Move | Java `AssetLinearDepreciationMethodProcess` | Proceso Openbravo registro `A_Asset_ID` | Proceso Openbravo registro `A_Asset_ID` |
| Proceso / otro | Certificado de entrega / recepción de activos | Certificate of Asset Delivery/Receipt | — | — | — |
| Proceso / otro | Enajenación por Motivo | Alienate by Reason | — | — | — |
| Proceso / otro | Informe de Activos Fijos Relacionados | Related Fixed Assets | — | — | — |
| Proceso / otro | Reporte Activos con facturas en espera | Asset Waiting Invoice | — | Asset Waiting Invoice | — |
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
**Total de reportes del módulo: 4**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **4**.

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
| `SSAM_PARENT_NULL` | The asset does not have a parent asset to apply the impairment. | The asset does not have a parent asset to apply the impairment. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSAM_TYPEOFCHANGE_NULL` | The field 'Type of change' can not be null if the field 'Change of value' is marked | The field 'Type of change' can not be null if the field 'Change of value' is marked | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSAM_PARENT_WITH_SON` | The asset has children with lines. | The asset has children with lines. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `ssam_assetalienated` | Asset is Alienated | Asset is Alienated | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSAM_ERROR_QUERY_CHILD` | Failed to get information on child assets. | Failed to get information on child assets. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo también incorpora lógica Java en las clases 'DocAlienate' y 'DocLine_Alienate', que gestionan la contabilización de la enajenación de activos y sus detalles, garantizando que se sigan los procedimientos adecuados durante el flujo de procesos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.ecuador.asset.move`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `DocAlienate` | accounting | AcctServer | — | `src/com/sidesoft/ecuador/asset/move/accounting/DocAlienate.java` |
| `DocLine_Alienate` | accounting | DocLine | — | `src/com/sidesoft/ecuador/asset/move/accounting/DocLine_Alienate.java` |
| `Add_taxid` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/ecuador/asset/move/ad_callouts/Add_taxid.java` |
| `ssam_UpdateFieldDocumentType` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/ecuador/asset/move/ad_callouts/ssam_UpdateFieldDocumentType.java` |
| `ProcessBatchDepreciationAssets` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/ecuador/asset/move/ad_process/ProcessBatchDepreciationAssets.java` |
| `AssetLinearDepreciationMethodProcess` | amortization | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/ecuador/asset/move/amortization/AssetLinearDepreciationMethodProcess.java` |
| `ValidateAssetEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/ecuador/asset/move/event/ValidateAssetEvent.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSAM_AMORTIZ_DOC_SEQ_TRG` | `a_amortization` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSAM_FACT_ACCT_ASSET_TRG` | `fact_acct` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSAM_POST_ALIENATETLINE_TRG` | `ssam_alienateline` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSAM_POST_ALIENATE_TRG` | `ssam_alienate` | before INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSAM_VALIDATE_ASSET_TRG` | `c_invoiceline` | before INSERT/UPDATE | Validación reutilizable de campos. |
| AD_VAL_RULE | — | `FIlter Assset Alienate` | `(a_asset.em_ssam_alienated = 'N' or a_asset.em_ssam_alienated is null)` |
| AD_VAL_RULE | — | `FIlter Assset Waiting Invoice` | `a_asset.em_ssam_status in ('W','L')` |
| AD_VAL_RULE | — | `FIlter Alienate Waiting Invoice` | `ssam_alienate.ssam_alienate_id In (select ssam_alienate_id
			from ssam_alienateline a
			left join a_asset b on b.a_ass` |
| AD_VAL_RULE | — | `Son Assets` | `A_ASSET.A_ASSET_ID IN (SELECT AT.A_ASSET_ID  FROM A_ASSET AT
WHERE ssam_get_record_parent(1,AT.A_ASSET_ID) <>'0' )` |
| AD_VAL_RULE | — | `Filter Alienate line head` | `ssam_alienateline.ssam_alienate_id = @EM_Ssam_Alienate_ID@` |
| AD_VAL_RULE | — | `Parent Assets` | `A_ASSET.A_ASSET_ID IN (SELECT ssam_get_record_parent(1,AT.A_ASSET_ID)    FROM A_ASSET AT
WHERE ssam_get_record_parent(1,` |
| AD_VAL_RULE | — | `Filter Asset Employee` | `c_bpartner.isemployee = 'Y'` |
| AD_VAL_RULE | — | `Filter Type Reason Alienate` | `Ssam_Reason_Alienate.Typereason = @Typereason@` |
| AD_VAL_RULE | — | `Logged User` | `ad_user.ad_user_id =@#ad_user_id@` |
| AD_VAL_RULE | — | `Document Type Alienate` | `C_Doctype.docbasetype = 'SSAM_ALT'` |
| Java event/validator | `ValidateAssetEvent` | persistencia/UI | *(leer `src/com/sidesoft/ecuador/asset/move/event/ValidateAssetEvent.java`)* |
| Función PL `ssam_amortization_process` | — | invocación proceso | Check the header belongs to a organization where transactions are posible and ready to use; Check the document does not have elements of different business unit or legal entities.; Check the period control is opened (only if it is legal entity with accounting) |
| Función PL `ssam_asset_post` | — | invocación proceso | v_Message VARCHAR(255); --OBTG:VARCHAR2--; Validando que exista un tipo de documento configurado; we calculate the already completed number of cycles |
| Función PL `ssam_create_alienate` | — | invocación proceso | ACTUALIZA EL ESTADO DE LA ENAJEACION A DESPROCESADO; ACTUALIZA EL ESTADO DE LA ENAJEACION A PROCESADO; v_Message := '@sspr_RowsInsertedwarning@: ' || v_n_insertions; |
| Función PL `ssam_process_alienate` | — | invocación proceso | No existe configración en el campo Tipo de Activo:; El activo es un bien de control y no debe tener datos de Amortización”:; Existes Amortizaciones contabilizadas futuras a la fecha de Enajenación: |
| Función PL `ssam_status_asset` | — | invocación proceso | Actualiza enajenacion a con el id de la factura; Actualiza enajenacion con el id de la factura |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers desempeñan un papel fundamental en este módulo, ya que ejecutan rutinas PL/pgSQL que se encargan de gestionar eventos como la contabilización de activos y la validación de datos. Las funciones PL asociadas a este módulo permiten realizar tareas específicas cuando se interactúa con la base de datos, facilitando el soporte y la integridad de la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSAM_AMORTIZ_DOC_SEQ_TRG` | `a_amortization` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSAM_AMORTIZ_DOC_SEQ_TRG.xml` |
| `SSAM_VALIDATE_ASSET_TRG` | `c_invoiceline` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SSAM_VALIDATE_ASSET_TRG.xml` |
| `SSAM_FACT_ACCT_ASSET_TRG` | `fact_acct` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSAM_FACT_ACCT_ASSET_TRG.xml` |
| `SSAM_POST_ALIENATE_TRG` | `ssam_alienate` | before | INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSAM_POST_ALIENATE_TRG.xml` |
| `SSAM_POST_ALIENATETLINE_TRG` | `ssam_alienateline` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSAM_POST_ALIENATETLINE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssam_amortization_process` | — | Check the header belongs to a organization where transactions are posible and ready to use; Check the document does not have elements of different business unit or legal entities.; Check the period control is opened (on… | Check the header belongs to a organization where transactions are posible and ready to use; Check the document does not have elements of different business unit or legal entities.; Check the period control is opened (only if it is legal entity with accounting); RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | `model/functions/SSAM_AMORTIZATION_PROCESS.xml` |
| `ssam_asset_group_acct_copy` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSAM_ASSET_GROUP_ACCT_COPY.xml` |
| `ssam_asset_post` | — | v_Message VARCHAR(255); --OBTG:VARCHAR2--; Validando que exista un tipo de documento configurado; we calculate the already completed number of cycles; we get the standard precision for the selected currency | v_Message VARCHAR(255); --OBTG:VARCHAR2--; Validando que exista un tipo de documento configurado; we calculate the already completed number of cycles; we get the standard precision for the selected currency; v_PercentageGeneral:=((v_AMORTIZATIONVALUEAMT-v_DEPRECIATEDPREVIOUSAMT-v_depreciatedPlan) *100/v_AMORTIZATIONVALUEAMT) /(v_USELIFEYEARS-v_DepreciatedLines) ;; v_PercentageGeneral := 100 / v_USELIFEYEARS; | `model/functions/SSAM_ASSET_POST.xml` |
| `ssam_create_alienate` | Crear lineas de enajenación | ACTUALIZA EL ESTADO DE LA ENAJEACION A DESPROCESADO; ACTUALIZA EL ESTADO DE LA ENAJEACION A PROCESADO; v_Message := '@sspr_RowsInsertedwarning@: ' || v_n_insertions; | ACTUALIZA EL ESTADO DE LA ENAJEACION A DESPROCESADO; ACTUALIZA EL ESTADO DE LA ENAJEACION A PROCESADO; v_Message := '@sspr_RowsInsertedwarning@: ' || v_n_insertions; | `model/functions/SSAM_CREATE_ALIENATE.xml` |
| `ssam_delete_amortization_lines` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSAM_DELETE_AMORTIZATION_LINES.xml` |
| `ssam_get_record_parent` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSAM_GET_RECORD_PARENT.xml` |
| `ssam_process_alienate` | Procesar enajenación | No existe configración en el campo Tipo de Activo:; El activo es un bien de control y no debe tener datos de Amortización”:; Existes Amortizaciones contabilizadas futuras a la fecha de Enajenación:; Existes Amortizacion… | No existe configración en el campo Tipo de Activo:; El activo es un bien de control y no debe tener datos de Amortización”:; Existes Amortizaciones contabilizadas futuras a la fecha de Enajenación:; Existes Amortizaciones anteriores sin contabilizar:; EJECUTA VALIDACIONES EN LA LÍNEAS DE ACTIVOS; VALIDA QUE EXISTA CONFIGURACION EN EL CAMPO TIPO DE ACTIVO | `model/functions/SSAM_PROCESS_ALIENATE.xml` |
| `ssam_status_asset` | — | Actualiza enajenacion a con el id de la factura; Actualiza enajenacion con el id de la factura | Actualiza enajenacion a con el id de la factura; Actualiza enajenacion con el id de la factura | `model/functions/SSAM_STATUS_ASSET.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Depreciación de Activos | `Depreciation Assets` | Botón (Java) | Java `ProcessBatchDepreciationAssets` | N | Proceso Openbravo ver `doExecute` en fuente |
| 2 | Crear lineas de enajenación | `Create Lines Alienate` | Botón (PL/pgSQL) | PL `ssam_create_alienate` | N | ACTUALIZA EL ESTADO DE LA ENAJEACION A DESPROCESADO; ACTUALIZA EL ESTADO DE LA ENAJEACION A PROCESADO; v_Message := '@sspr_RowsInsertedwarning@: ' || v_n_insertions; |
| 3 | Procesar enajenación | `Process Alienate` | Botón (PL/pgSQL) | PL `ssam_process_alienate` | N | No existe configración en el campo Tipo de Activo:; El activo es un bien de control y no debe tener datos de Amortización”:; Existes Amortizaciones contabilizadas futuras a la fech |
| 4 | Generar plan de depreciación | `Generate Amortizacion Plan Asset Move` | Informe (servlet) | Java `AssetLinearDepreciationMethodProcess` | N | Proceso Openbravo registro `A_Asset_ID` |

**Total acciones documentadas (extract):** **4** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `com.sidesoft.ecuador.asset.move`.

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

# Glosario — prefijo `SSAM`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSAM` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.ecuador.asset.move` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Depreciation Assets` — Depreciación de Activos
- `Create Lines Alienate` — Crear lineas de enajenación
- `Process Alienate` — Procesar enajenación
- `Generate Amortizacion Plan Asset Move` — Generar plan de depreciación
- `Certificate of Asset Delivery/Receipt` — Certificado de entrega / recepción de activos
- `Alienate by Reason` — Enajenación por Motivo
- `Related Fixed Assets` — Informe de Activos Fijos Relacionados
- `Asset Waiting Invoice` — Reporte Activos con facturas en espera

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Asset Subcategory Level
**Package:** `com.sidesoft.ecuador.asset.subcategory.level`

# Module overview — Sidesoft Asset Subcategory Level

## Functional

El módulo Sidesoft Asset Subcategory Level tiene como propósito la gestión de las subcategorías dentro de la categoría de activos, permitiendo una mayor organización y clasificación de los mismos. Los actores principales son los usuarios del ERP que gestionan activos y los administradores de la base de datos. El alcance del módulo incluye la creación, modificación y visualización de subcategorías, facilitando el seguimiento de los activos. No tiene dependencias adicionales más allá de la compatibilidad con la interfaz de usuario de versiones de Openbravo de 2.50 a 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/ecuador/asset/subcategory/level` |
| Web | `web/com.sidesoft.ecuador.asset.subcategory.level/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSASL`

# Guía de chat — Sidesoft Asset Subcategory Level

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.ecuador.asset.subcategory.level`).

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
- «¿Qué es la tabla ssasl_subcategory?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo añadir una nueva subcategoría para un activo?
- ¿Dónde puedo ver todas las subcategorías disponibles?
- ¿Qué sucede si ingreso datos incorrectos al crear una subcategoría?
- ¿Es posible eliminar una subcategoría de activos una vez creada?
- ¿Cómo se relacionan las subcategorías con los activos existentes?
- ¿Puedo modificar una subcategoría después de haberla creado?
- ¿Existen informes específicos para visualizar las subcategorías de activos?
- ¿Qué debo hacer si tengo problemas para guardar los cambios en las subcategorías?

# Domain — data model

## Functional

La entidad cabecera principal es la tabla 'ssasl_subcategory', que almacena la información relevante de las subcategorías de activos. Este módulo modifica las tablas 'A_ASSET' y 'A_ASSET_GROUP', permitiendo que la información de las subcategorías esté relacionada con los activos y sus agrupaciones. Aunque no hay etapas definidas ni triggers en este módulo, la relación entre subcategorías y activos se establece a través de claves foráneas que aseguran la integridad de los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssasl_subcategory` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssasl_subcategory` | SSASL_Subcategory | — | — | a_asset_group_id→a_asset_group; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a a_asset_group, ad_client, ad_org. | PK `ssasl_subcategory_key`; Cols: code, name, description, a_asset_group_id; `SSASL_ACT_MAIN_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SSASL_Subcategory` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`A_ASSET`, `A_ASSET_GROUP`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Este módulo no presenta ventanas específicas en la UI, pero se prevé que la gestión de subcategorías se integre en la ventana de activos existente. Los usuarios podrán acceder a las subcategorías directamente desde la interfaz de activos, donde podrán visualizar, crear y modificar estas entradas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.ecuador.asset.subcategory.level.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.ecuador.asset.subcategory.level.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Subcategory

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Code | `Code` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |

### Pestaña `452`

- **AD_TAB_ID:** `452` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 55 | EM_Ssasl_Amortizationperctg | `EM_Ssasl_Amortizationperctg` | No | No | — |

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 45 | Subcategory | `EM_Ssasl_Subcategory_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que no se han definido procesos específicos dentro del módulo, tampoco existen botones o informes asociados. Sin embargo, las validaciones frecuentes incluirían la verificación de la integridad de las subcategorías al ser creadas o modificadas, asegurando que los datos sean consistentes con las categorías de activos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.ecuador.asset.subcategory.level.es_ES/referencedata/translation/`.

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

El módulo no incluye componentes en Java, por lo que no hay clases Java asociadas que influyan en su funcionalidad.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.ecuador.asset.subcategory.level`.

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
| AD_VAL_RULE | — | `SSASL_ValidateSubcategory` | `ssasl_subcategory.ssasl_subcategory_id in ( 
select ssasl_subcategory_id 
from  ssasl_subcategory  
where a_asset_group_` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

En este módulo, aunque no hay triggers ni funciones PL, la estructura de base de datos asegurará que los datos se mantengan coherentes al modificarse las tablas relacionadas. La administración y soporte en la base de datos se realizarán minimizando las alteraciones de la integridad de los datos mediante la utilización de claves foráneas.

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

Módulo: `com.sidesoft.ecuador.asset.subcategory.level`.

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

# Glosario — prefijo `SSASL`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSASL` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.ecuador.asset.subcategory.level` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Asset Dimensions
**Package:** `ec.com.sidesoft.asset.dimensions`

# Module overview — Asset Dimensions

## Functional

El módulo 'Asset Dimensions' permite implementar y gestionar dimensiones de activos dentro del sistema ERP Openbravo. Este módulo es esencial para los usuarios de negocio que desean tener un control más granular sobre sus activos, así como para el soporte de nivel 2 y desarrolladores que requieran integrar o personalizar la funcionalidad relacionada con activos. Su alcance incluye la modificación de tablas relevantes y la activación de triggers que ayudan en el manejo de datos de amortización. La principal dependencia de este módulo es el núcleo del sistema (Core).

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/asset/dimensions` |
| Web | `web/ec.com.sidesoft.asset.dimensions/` |

### Declared dependencies

- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSAD`

# Guía de chat — Asset Dimensions

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.asset.dimensions`).

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

- ¿Cómo puedo modificar las dimensiones de un activo?
- ¿Qué pasos seguir para verificar la amortización de mis activos?
- ¿Dónde encuentro los registros de amortización de un activo específico?
- ¿Qué sucede si edito un activo mientras tengo una amortización activa?
- ¿Cómo puedo generar un informe sobre los activos y sus dimensiones?
- ¿Hay forma de revertir cambios en las dimensiones de un activo?
- ¿Qué validaciones se realizan al actualizar las dimensiones de un activo?
- ¿Cómo afecta el trigger de amortización a la información de mis activos?

# Domain — data model

## Functional

La entidad cabecera para este módulo está vinculada a la tabla 'A_ASSET', donde se gestionan los activos. Aunque no tiene etapas explícitas definidas en el inventario, el funcionamiento interno puede implicar etapas de creación y modificación de activos. La relación entre las dimensiones y los activos se establece a través de modificaciones en la tabla mencionada y es gestionada por el trigger clave 'SSAD_A_AMORTIZATIONLINE_TRG', que se activa al realizar cambios en los registros de la tabla 'a_amortizationline'. Este trigger permite que las lógicas de negocio asociadas a las amortizaciones se implementen de manera efectiva.

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

`A_ASSET`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo carece de ventanas o UI específicas disponibles en el inventario actual, lo que sugiere que las interacciones pueden ser a través de ajustes directos en tablas o mediante scripts SQL. La navegación en el sistema podría implicar trabajar con las vistas de datos existentes para los activos, aunque no se detallan particularidades visuales.

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

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 410 | Cost Center | `C_Costcenter_ID` | No | No | 800000 |
| 420 | 1st Dimension | `User1_ID` | No | No | 800000 |
| 430 | 2nd Dimension | `User2_ID` | No | No | 800000 |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Aunque el módulo no cuenta con procesos definidos que incluyan botones o informes, se puede suponer que algunos procesos típicos implicarían la validación de datos de activos y la comprobación de las dimensiones asociadas. Los usuarios podrían requerir informes sobre el estado de los activos o las amortizaciones, que deben ser manejados cuidadosamente para evitar inconsistencias en los datos al realizar modificaciones.

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

No se han definido clases Java específicas para este módulo, lo que sugiere que la funcionalidad está completamente implementada en las capas de base de datos y lógica de negocio a través de triggers y otras herramientas del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.asset.dimensions`.

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
| Trigger `SSAD_A_AMORTIZATIONLINE_TRG` | `a_amortizationline` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El uso de triggers es crucial en este módulo para mantener la integridad de los datos y asegurar que las operaciones sobre activos y sus dimensiones se realicen correctamente. El trigger 'SSAD_A_AMORTIZATIONLINE_TRG' es un ejemplo de cómo se utiliza PL/pgSQL para implementar lógica de negocio que se activa automáticamente en respuesta a cambios en el sistema, proporcionando un soporte efectivo en la gestión de los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSAD_A_AMORTIZATIONLINE_TRG` | `a_amortizationline` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSAD_A_AMORTIZATIONLINE_TRG.xml` |
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

Módulo: `ec.com.sidesoft.asset.dimensions`.

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

# Glosario — prefijo `SSAD`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSAD` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.asset.dimensions` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Assets Revaluation
**Package:** `ec.com.sidesoft.asset.revaluation`

# Module overview — Sidesoft Assets Revaluation

## Functional

El módulo Sidesoft Assets Revaluation permite la revaluación de activos en un entorno empresarial utilizando el ERP Openbravo. Este proceso es relevante para contables y gerentes de activos que necesitan ajustar el valor de los activos debido a variaciones en el mercado o de acuerdo con políticas internas. Los actores principales son los usuarios de negocio que ejecutan el proceso y el soporte técnico que garantiza su correcto funcionamiento. El alcance del módulo incluye la integración con otros módulos relacionados con activos y la generación de informes específicos. Las dependencias del módulo aseguran la compatibilidad y funcionalidad adecuada dentro del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/asset/revaluation` |
| Web | `web/ec.com.sidesoft.asset.revaluation/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Asset Dimensions
- Asset Move
- Change Translation Assets Field
- Core
- Hide Fields Asset
- Sidesoft Asset Subcategory Level

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSARV`

# Guía de chat — Sidesoft Assets Revaluation

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.asset.revaluation`).

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
- «¿Qué es la tabla ssarv_value_change?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo inicio el proceso de revaluación de activos?
- ¿Qué informes puedo generar después de revaluar mis activos?
- ¿Qué datos necesito para completar una revaluación?
- ¿Cómo puedo ver el historial de revaluación de un activo específico?
- ¿Puedo deshacer una revaluación realizada por error?
- ¿Qué hacer si un activo no aparece en la lista para revaluar?
- ¿Cómo se calculan los nuevos valores de los activos?
- ¿Qué dependencias debo tener en cuenta para usar este módulo?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la tabla de cabecera 'ssarv_value_change', que captura los cambios de valor de los activos. Esta tabla está relacionada con la entidad de activos 'A_ASSET', permitiendo un vínculo directo entre los cambios de revaluación y los activos mismos. Aunque no hay triggers definidos, el módulo se apoya en funciones y clases Java que gestionan la lógica del proceso de revaluación, garantizando que los datos se actualicen correctamente en función de las modificaciones realizadas por los usuarios.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssarv_value_change` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssarv_value_change` | ssarv_value_change | — | — | a_asset_id→a_asset; ad_client_id→ad_client; hv_c_taxcategory_id→c_taxcategory; nv_c_taxcategory_id→c_taxcategory; ad_org_id→ad_org | Detalle enlazado a a_asset, ad_client, c_taxcategory. | PK `ssarv_vc_key`; Cols: hv_datepurchased, hv_amortizationtype, hv_amortizationcalctype, hv_amortizationstartdate, hv_amortizationenddate; `SSARV_VC_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssarv_value_change` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`A_ASSET`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo de revaluación de activos no incluye ventanas específicas en la interfaz de usuario, ya que se basa en un proceso que se invoca mediante un botón para iniciar la revaluación y generar informes. La navegación se realiza a través de funciones integradas en el sistema que permiten a los usuarios acceder y ejecutar el proceso de revaluación sin necesidad de una interfaz dedicada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.asset.revaluation.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.asset.revaluation.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Value Change

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 110 | Purchase Date | `HV_Datepurchased` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 120 | Depreciation Type | `HV_Amortizationtype` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 130 | Calculate Type | `HV_Amortizationcalctype` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 140 | Depreciation Start Date | `HV_Amortizationstartdate` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 150 | Depreciation End Date | `HV_Amortizationenddate` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 160 | Depreciate | `HV_Assetschedule` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 170 | Usable Life - Months | `HV_Uselifemonths` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 180 | Asset Value | `HV_Assetvalueamt` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 190 | Residual Asset Value | `HV_Residualassetvalueamt` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 200 | Depreciation Amt. | `HV_Amortizationvalueamt` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 210 | Previously Depreciated Amt. | `HV_Depreciatedpreviousamt` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 220 | Net Worth | `HV_Net_Worth` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 230 | Value In Books | `HV_Value_In_Books` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 240 | Tax Group | `HV_C_Taxcategory_ID` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 250 | Tax | `HV_Taxamt` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 260 | Total Purchase Amount | `HV_Totalpurchaseamt` | No | No | B1F4F952FE034306B49B89979F309F20 |
| 310 | Value Change Date | `NV_Changedate` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 320 | Description | `NV_Description` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 330 | Purchase Date | `NV_Datepurchased` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 340 | Depreciation Type | `NV_Amortizationtype` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 350 | Calculate Type | `NV_Amortizationcalctype` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 360 | Depreciation Start Date | `NV_Amortizationstartdate` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 370 | Depreciation End Date | `NV_Amortizationenddate` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 380 | Depreciate | `NV_Assetschedule` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 390 | Usable Life - Months | `NV_Uselifemonths` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 400 | Asset Value | `NV_Assetvalueamt` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 410 | Residual Asset Value | `NV_Residualassetvalueamt` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 420 | Depreciation Amt. | `NV_Amortizationvalueamt` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 430 | Tax Group | `NV_C_Taxcategory_ID` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 440 | Tax | `NV_Taxamt` | No | No | 7949DDD07EFE47C58E3114A342907330 |
| 450 | Total Purchase Amount | `NV_Totalpurchaseamt` | No | No | 7949DDD07EFE47C58E3114A342907330 |

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| — | Create Depreciation Plan | `EM_Ssarv_Depreciation_Plan` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso de revaluación de activos se activa mediante un botón, lo que inicia la lógica para calcular y registrar cambios de valor. Además, está disponible un informe titulado 'Reporte de Revalorización de Activos', que permite a los usuarios generar un documento que detalla los cambios en los valores de los activos revaluados. Las validaciones frecuentes incluyen la verificación de que todos los campos requeridos estén completos antes de proceder con la revaluación y las validaciones de integridad de datos que aseguran que los valores sean consistentes y correctos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.asset.revaluation.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Crear Plan de Depreciación | Create Depreciation Plan | Create Depreciation Plan | Java `AssetRevaluation` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `A_Asset_ID` | `src/ec/com/sidesoft/asset/revaluation/ad_process/AssetRevaluation.java` |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Reporte de Revalorización de Activos | Asset Revaluation Report | Asset Revaluation Report | Java `AssetRevaluationReport` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/asset/revaluation/ad_reports/AssetRevaluationReport.jrxml`; contexto sesión `800027|Ssarv_Value_Change_ID`. | `src/ec/com/sidesoft/asset/revaluation/ad_process/AssetRevaluationReport.java` |
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
| Botón (Java) | Crear Plan de Depreciación | `AssetRevaluation` | Proceso Java (toolbar/background) | `A_Asset_ID` | — | `src/ec/com/sidesoft/asset/revaluation/ad_process/AssetRevaluation.java` |
| Reporte | Reporte de Revalorización de Activos | `AssetRevaluationReport` | Informe (servlet PDF) | `800027|Ssarv_Value_Change_ID` | ec/com/sidesoft/asset/revaluation/ad_reports/AssetRevaluationReport.jrxml | `src/ec/com/sidesoft/asset/revaluation/ad_process/AssetRevaluationReport.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Crear Plan de Depreciación | Create Depreciation Plan | Create Depreciation Plan | Java `AssetRevaluation` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `A_Asset_ID` | `src/ec/com/sidesoft/asset/revaluation/ad_process/AssetRevaluation.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Crear Plan de Depreciación | Create Depreciation Plan | Java `AssetRevaluation` | Proceso Openbravo registro `A_Asset_ID` | Proceso Openbravo registro `A_Asset_ID` |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Reporte de Revalorización de Activos | Asset Revaluation Report | Asset Revaluation Report | Java `AssetRevaluationReport` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/asset/revaluation/ad_reports/AssetRevaluationReport.jrxml`; contexto sesión `800027|Ssarv_Value_Change_ID`. | `src/ec/com/sidesoft/asset/revaluation/ad_process/AssetRevaluationReport.java` |
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
| 1 | Reporte de Revalorización de Activos | `Asset Revaluation Report` | Java `AssetRevaluationReport`; JRXML `ec/com/sidesoft/asset/revaluation/ad_reports/AssetRevaluationReport.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | Asset Revaluation Report. Contexto sesión: `800027|Ssarv_Value_Change_ID`. Plantilla: ec/com/sidesoft/asset/revaluation/ad_reports/AssetRevaluationReport.jrxml |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/asset/revaluation/ad_reports/AssetRevaluationReport.jrxml`
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

El módulo cuenta con dos clases Java que gestionan la lógica de revaluación y la generación del informe correspondiente. La clase 'AssetRevaluation' se encarga de realizar el procesamiento de la revaluación, mientras que 'AssetRevaluationReport' gestiona la creación y exportación del informe en formato PDF, asegurando que toda la funcionalidad necesaria esté disponible para los usuarios.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.asset.revaluation`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `AssetRevaluation` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/asset/revaluation/ad_process/AssetRevaluation.java` |
| `AssetRevaluationReport` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/asset/revaluation/ad_process/AssetRevaluationReport.java` |
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

El módulo no incluye triggers específicos, lo que significa que la manipulación de datos se realiza a través de las clases Java y las funciones de procesamiento del módulo. Las funciones PL son inexistentes, pues las operaciones se gestionan completamente desde el código Java, garantizando un control adecuado y eficiente sobre el flujo de datos durante el proceso de revaluación.

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
| 1 | Crear Plan de Depreciación | `Create Depreciation Plan` | Botón (Java) | Java `AssetRevaluation` | N | Proceso Openbravo registro `A_Asset_ID` |
| 2 | Reporte de Revalorización de Activos | `Asset Revaluation Report` | Reporte | Java `AssetRevaluationReport` | S | Genera PDF desde JRXML `ec/com/sidesoft/asset/revaluation/ad_reports/AssetRevaluationReport.jrxml`; contexto sesión `800027|Ssarv_Value_Change_ID`. |

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

Módulo: `ec.com.sidesoft.asset.revaluation`.

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

# Glosario — prefijo `SSARV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSARV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.asset.revaluation` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Create Depreciation Plan` — Crear Plan de Depreciación
- `Asset Revaluation Report` — Reporte de Revalorización de Activos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Asset Transfer
**Package:** `ec.com.sidesoft.asset.transfer`

# Module overview — Sidesoft Asset Transfer

## Functional

El módulo 'Sidesoft Asset Transfer' está diseñado para gestionar la transferencia de activos dentro de una organización. Los principales actores que interactúan con este módulo son usuarios de negocio, personal de soporte y desarrolladores. Este módulo garantiza que los activos se transfieran de manera adecuada y registra toda la información relevante desde el origen hasta el destino. La funcionalidad del módulo depende de otros módulos como 'com.sidesoft.ecuador.asset.allocation' y 'com.sidesoft.ecuador.asset.subcategory.level'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/asset/transfer` |
| Web | `web/ec.com.sidesoft.asset.transfer/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSATR`

# Guía de chat — Sidesoft Asset Transfer

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.asset.transfer`).

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
- «¿Qué es la tabla ssatr_asset_transfer?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar una nueva transferencia de activo?
- ¿Qué campos son obligatorios para completar una transferencia?
- ¿Cómo puedo revisar las transferencias anteriores?
- ¿Qué debo hacer si un campo requerido no se completa correctamente?
- ¿Puedo revertir una transferencia una vez que se ha realizado?
- ¿Cómo se generan los informes de las transferencias?
- ¿Hay alguna validación que deba tener en cuenta al transferir activos?
- ¿Cómo se gestionan los errores en el proceso de transferencia de activos?

# Domain — data model

## Functional

El modelo de datos se centra en la tabla principal 'ssatr_asset_transfer', que actúa como entidad cabecera en el registro de transferencias de activos. Esta tabla está relacionada con la tabla 'ssatr_asset_detail', que proporciona detalles adicionales sobre cada transferencia. A lo largo del proceso de transferencia, se verifican automáticamente diversos campos, como 'Custodio' y 'Transferir a', a través de triggers que aseguran la integridad de la información y que los valores obligatorios estén correctamente proporcionados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssatr_asset_detail` |
| `ssatr_asset_transfer` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssatr_asset_detail` | ssatr_asset_detail | `SSATR_ASSET_DETAIL_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; a_asset_id→a_asset; a_asset_group_id→a_asset_group; ssasl_subcategory_id→ssasl_subcategory (+1) | Detalle enlazado a a_asset, ad_client, ad_org. Validado por trigger(s): SSATR_ASSET_DETAIL_TRG. | PK `ssatr_asset_det_transfer_key`; Cols: ssatr_asset_transfer_id, a_asset_id, code, name, a_asset_group_id; `SSATR_ASSETDET_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `ssatr_asset_transfer` | ssatr_asset_transfer | `SSATR_FIELDS_VALIDATE_TRG` | — | custodian_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org; a_asset_group_id→a_asset_group; c_doctype_id→c_doctype (+2) | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SSATR_FIELDS_VALIDATE_TRG. | PK `ssatr_asset_tr_transfer_key`; Cols: transaction_type, c_doctype_id, documentno, docstatus, datetransfer; `SSATR_ASSET_TR_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssatr_asset_detail` |
| `ssatr_asset_transfer` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de la ventana 'Transferencia de activos', donde los usuarios pueden acceder a las funciones de registro y gestión de las transferencias. La interfaz de usuario permite a los empleados ingresar los datos necesarios, consultar transferencias previas y ejecutar informes relacionados con las transferencias de activos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.asset.transfer.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Transferencia de activos | Asset transfer |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Transferencia de activos | Asset transfer | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.asset.transfer.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Transferencia de activos

- **AD_WINDOW_ID:** `D3340A4CA0F449EEA0B52EF85D30A5CA`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `F2E1D613BF5E4886BF570511A1E9C227` | 0 |
| 20 | Assets | `62A294E4D12A497C9410C4C4A639FC2A` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Header (ventana: Transferencia de activos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Transaction type | `Transaction_Type` | No | No | — |
| 40 | Document Type | `C_Doctype_ID` | No | No | — |
| 50 | Document No. | `Documentno` | No | No | — |
| 70 | Date | `Datetransfer` | No | No | — |
| 80 | Asset Category | `A_Asset_Group_ID` | No | No | — |
| 90 | Subcategory | `Ssasl_Subcategory_ID` | No | No | — |
| 100 | Custodian_ID | `Custodian_ID` | No | No | — |
| 110 | Trasfer to | `Trasferto_ID` | No | No | — |
| 115 | Description | `Description` | No | No | — |
| 180 | Asset | `A_Asset_ID` | No | No | — |
| 190 | Active | `Isactive` | No | No | — |
| 200 | Document Status | `Docstatus` | No | Sí | — |
| 220 | LoadAssets | `Loadassets` | No | No | — |
| 230 | Process | `Process` | No | No | — |
| 240 | Select All | `Select_All` | No | No | — |

### Assets (ventana: Transferencia de activos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 40 | Transfer | `Transfer` | No | No | — |
| 50 | Asset | `A_Asset_ID` | No | Sí | — |
| 60 | Code | `Code` | No | Sí | — |
| 70 | Name | `Name` | No | Sí | — |
| 80 | Asset Group | `A_Asset_Group_ID` | No | Sí | — |
| 90 | Subcategory | `Ssasl_Subcategory_ID` | No | Sí | — |
| 130 | Custodian_ID | `Custodian_ID` | No | Sí | — |
| 140 | Asset transfer | `Ssatr_Asset_Transfer_ID` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Las funciones principales del módulo incluyen botones para completar, retornar o rechazar transacciones de transferencia. Al finalizar una transferencia, se genera un informe titulado 'Proceso de Impresion - Transferencia de activos', que proporciona un registro visual del proceso realizado. Además, se aplican validaciones frecuentes para asegurar que no se completen transferencias con información incompleta o errónea.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.asset.transfer.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar activos | LoadAssets | LoadAssets | `ssatr_load_assets` | No se encontraron activos con las características especificadas (Grupo - Subcategoría - Custodio - Edificio - Unidad - Departamento). | — |
| Botón (PL/pgSQL) | Procesar | Process | Ssatr_Process | `ssatr_process_transfer` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Seleccionar todo | Select All | ssatr_select_all_assets | `ssatr_select_all_assets` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Proceso de Impresion - Transferencia de activos | PRINT GENERIC - ASSET TRANSFER | PRINT GENERIC - ASSET TRANSFER | Java `AssetTransferReport` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `D3340A4CA0F449EEA0B52EF85D30A5CA|ssatr_asset_transfer_id`. | `src/ec/com/sidesoft/asset/transfer/ad_report/AssetTransferReport.java` |
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
| Reporte | Proceso de Impresion - Transferencia de activos | `AssetTransferReport` | Informe (servlet PDF) | `D3340A4CA0F449EEA0B52EF85D30A5CA|ssatr_asset_transfer_id` | — | `src/ec/com/sidesoft/asset/transfer/ad_report/AssetTransferReport.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar activos | LoadAssets | LoadAssets | `ssatr_load_assets` | No se encontraron activos con las características especificadas (Grupo - Subcategoría - Custodio - Edificio - Unidad - Departamento). | — |
| Botón (PL/pgSQL) | Procesar | Process | Ssatr_Process | `ssatr_process_transfer` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Seleccionar todo | Select All | ssatr_select_all_assets | `ssatr_select_all_assets` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar activos | LoadAssets | PL `ssatr_load_assets` | No se encontraron activos con las características especificadas (Grupo - Subcategoría - Custodio - Edificio - Unidad - Departamento). | No se encontraron activos con las características especificadas (Grupo - Subcategoría - Custodio - Edificio - Unidad - Departamento). |
| Botón (PL/pgSQL) | Procesar | Process | PL `ssatr_process_transfer` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Seleccionar todo | Select All | PL `ssatr_select_all_assets` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Proceso de Impresion - Transferencia de activos | PRINT GENERIC - ASSET TRANSFER | PRINT GENERIC - ASSET TRANSFER | Java `AssetTransferReport` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `D3340A4CA0F449EEA0B52EF85D30A5CA|ssatr_asset_transfer_id`. | `src/ec/com/sidesoft/asset/transfer/ad_report/AssetTransferReport.java` |
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
| 1 | Proceso de Impresion - Transferencia de activos | `PRINT GENERIC - ASSET TRANSFER` | Java `AssetTransferReport`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | PRINT GENERIC - ASSET TRANSFER. Contexto sesión: `D3340A4CA0F449EEA0B52EF85D30A5CA|ssatr_asset_transfer_id`. Plantilla: — |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/asset/transfer/ad_report/AssetTransfer.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `SSATR_DocumentProcessed` | Document processed error | Document processed error | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSATR_NoLineSelected` | No asset selected to transfer | No asset selected to transfer | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo contiene clases Java como 'AssetTransferReport' que facilitan la generación de informes a partir de los datos de la transferencia de activos. Esta clase se encarga de procesar las solicitudes y generar un informe PDF que puede ser utilizado para documentar las transferencias realizadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.asset.transfer`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `AssetTransferReport` | ad_report | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/asset/transfer/ad_report/AssetTransferReport.java` |
| `UpdateSequenceTransfer` | event | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/asset/transfer/event/UpdateSequenceTransfer.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSATR_ASSET_DETAIL_TRG` | `ssatr_asset_detail` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSATR_FIELDS_VALIDATE_TRG` | `ssatr_asset_transfer` | before INSERT/UPDATE | Los campos "Custodio" y "Transferir a" son obligatorios.; Los campos de ubicación son obligatorios si su origen o destino correspondiente no es nulo.<br>(Edificio - Edificio destino) (Unidad - Unidad destino) (Departame… |
| AD_VAL_RULE | — | `Doctype table` | `C_DocType.AD_Table_ID='F2E1D613BF5E4886BF570511A1E9C227' AND AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.AD_Org_ID, @#AD_Clie` |
| AD_VAL_RULE | — | `SSATR_Asset_Transfer` | `A_ASSET.A_ASSET_ID IN (
SELECT AT.A_ASSET_ID FROM A_ASSET AT
WHERE 
 (AT.a_asset_group_id=@a_asset_group_id@ OR @a_asset` |
| Función PL `ssatr_load_assets` | — | invocación proceso | No se encontraron activos con las características especificadas (Grupo - Subcategoría - Custodio - Edificio - Unidad - Departamento). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers desempeñan un papel crucial en este módulo. Por ejemplo, el trigger 'SSATR_ASSET_DETAIL_TRG' asegura que la lógica del módulo se aplique correctamente cuando se realizan cambios en la transferencia. Las funciones PL asociadas permiten la ejecución de lógica específica cuando se guardan las transferencias, garantizando que todos los campos requeridos sean validados adecuadamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSATR_ASSET_DETAIL_TRG` | `ssatr_asset_detail` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSATR_ASSET_DETAIL_TRG.xml` |
| `SSATR_FIELDS_VALIDATE_TRG` | `ssatr_asset_transfer` | before | INSERT/UPDATE | Los campos "Custodio" y "Transferir a" son obligatorios.; Los campos de ubicación son obligatorios si su origen o destino correspondiente no es nulo.<br>(Edificio - Edificio destino) (Unidad - Unidad destino) (Departame… | `model/triggers/SSATR_FIELDS_VALIDATE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssatr_load_assets` | Cargar activos | No se encontraron activos con las características especificadas (Grupo - Subcategoría - Custodio - Edificio - Unidad - Departamento). | No se encontraron activos con las características especificadas (Grupo - Subcategoría - Custodio - Edificio - Unidad - Departamento). | `model/functions/SSATR_LOAD_ASSETS.xml` |
| `ssatr_process_transfer` | Procesar | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSATR_PROCESS_TRANSFER.xml` |
| `ssatr_select_all_assets` | Seleccionar todo | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSATR_SELECT_ALL_ASSETS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cargar activos | `LoadAssets` | Botón (PL/pgSQL) | PL `ssatr_load_assets` | N | No se encontraron activos con las características especificadas (Grupo - Subcategoría - Custodio - Edificio - Unidad - Departamento). |
| 2 | Procesar | `Ssatr_Process` | Botón (PL/pgSQL) | PL `ssatr_process_transfer` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 3 | Seleccionar todo | `ssatr_select_all_assets` | Botón (PL/pgSQL) | PL `ssatr_select_all_assets` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 4 | Proceso de Impresion - Transferencia de activos | `PRINT GENERIC - ASSET TRANSFER` | Reporte | Java `AssetTransferReport` | S | Genera PDF desde JRXML `—`; contexto sesión `D3340A4CA0F449EEA0B52EF85D30A5CA|ssatr_asset_transfer_id`. |

**Total acciones documentadas (extract):** **4** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `ec.com.sidesoft.asset.transfer`.

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

# Glosario — prefijo `SSATR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSATR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.asset.transfer` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `LoadAssets` — Cargar activos
- `Ssatr_Process` — Procesar
- `ssatr_select_all_assets` — Seleccionar todo
- `PRINT GENERIC - ASSET TRANSFER` — Proceso de Impresion - Transferencia de activos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Assets Budget
**Package:** `ec.com.sidesoft.assets.budget`

# Module overview — Assets Budget

## Functional

El módulo 'Assets Budget' está diseñado para gestionar la planificación y el control del presupuesto asignado a activos en las organizaciones. Su propósito es proporcionar a los usuarios un sistema que permita una visibilidad clara sobre el uso del presupuesto para los activos, facilitando así una mejor toma de decisiones financieras. Los principales actores involucrados son los gerentes financieros, responsables de activos y contadores. Este módulo se integra con otros módulos de Openbravo, aunque actualmente no tiene dependencias específicas documentadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/assets/budget` |
| Web | `web/ec.com.sidesoft.assets.budget/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSABGT`

# Guía de chat — Assets Budget

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.assets.budget`).

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

- ¿Cómo puedo acceder al módulo de presupuesto de activos?
- ¿Qué tablas son utilizadas en el módulo de presupuesto de activos?
- ¿Dónde se registran los cambios en el presupuesto de activos?
- ¿Cómo puedo verificar el estado del presupuesto de activos?
- ¿Existen informes disponibles para el seguimiento del presupuesto de activos?
- ¿Qué validaciones se realizan al ingresar datos en el módulo?
- ¿Qué sucede si el presupuesto asignado se excede?
- ¿Cómo se relaciona este módulo con otros en Openbravo?

# Domain — data model

## Functional

El modelo de datos del módulo 'Assets Budget' incluye una entidad cabecera que es la tabla 'A_AMORTIZATION', la cual es crítica para el manejo de la amortización de activos. La relación principal se establece en cómo esta tabla interactúa con otras entidades relacionadas en el sistema, permitiendo así un flujo adecuado de información entre módulos. Aunque no se han especificado triggers, es esencial considerar que las modificaciones en la tabla de amortización pueden requerir validaciones y controles para asegurar la integridad de los datos.

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

`A_AMORTIZATION`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo actualmente no cuenta con ventanas ni interfaces de usuario específicas, por lo que la interacción se haría a través de configuraciones predeterminadas del ERP. La navegación y manipulación de datos deben llevarse a cabo utilizando las funcionalidades estándar de Openbravo para la gestión de activos y presupuestos, lo que implica un uso intensivo de llamadas a las APIs disponibles.

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

### Pestaña `800076`

- **AD_TAB_ID:** `800076` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 15 | Transaction Document | `C_Doctype_ID` | No | No | — |
| 16 | Document No. | `DocumentNo` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que el módulo no incluye procesos específicos documentados, se entiende que las funcionalidades básicas están integradas dentro de los procesos estándar de gestión de activos. Los usuarios típicamente se enfrentarán a botones generales de completar, retornar o rechazar en situaciones estándar de flujo de trabajo. Las validaciones más frecuentes podrían incluir la verificación del presupuesto disponible antes de ejecutar operaciones que afectan la amortización de activos.

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

No se reportan clases Java específicas para el módulo 'Assets Budget', indicando que su funcionalidad se basa en las integraciones y operaciones estándar proporcionadas por la plataforma Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.assets.budget`.

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
| AD_VAL_RULE | — | `Document Type Amortization` | `C_DocType.DocBaseType = 'SSABGT_AM' AND (AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.AD_Org_ID, @#AD_Client_ID@) <> '-1' OR C` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL en el contexto de este módulo son esenciales para la gestión de la integridad de los datos, aunque actualmente no se reportan triggers específicos asociados. Esto puede implicar que, en el futuro, se tendrá que considerar la implementación de procedimientos para manejar eventos de datos y automatizaciones necesarias para el cálculo y seguimiento del presupuesto de activos.

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

Módulo: `ec.com.sidesoft.assets.budget`.

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

# Glosario — prefijo `SSABGT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSABGT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.assets.budget` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Assets Changes
**Package:** `ec.com.sidesoft.assets.changes`

# Module overview — Sidesoft Assets Changes

## Functional

El módulo Sidesoft Assets Changes permite gestionar los cambios en los activos, facilitando modificaciones y actualizaciones de información relacionada. Los actores principales incluyen usuarios de negocio que requieren adaptaciones en la gestión de activos y equipos de soporte técnico que garantizan el correcto funcionamiento del ERP. Este módulo es esencial para mejorar la administración de activos y asegurar que la información esté siempre actualizada y precisa, con dependencias directas del skin de compatibilidad de versiones del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/assets/changes` |
| Web | `web/ec.com.sidesoft.assets.changes/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSACH`

# Guía de chat — Sidesoft Assets Changes

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.assets.changes`).

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
- «¿Qué es la tabla ssach_modify_line?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo modificar un activo existente?
- ¿Qué informes están disponibles para visualizar cambios en activos?
- ¿Qué sucede si no puedo completar un cambio de activo?
- ¿Los cambios se registran automáticamente en el sistema?
- ¿Cómo acceder a la ventana de 'Modificar activo'?
- ¿Qué validaciones se aplican al ingresar datos de un activo?
- ¿Cómo imprimir un informe de activo modificado?
- ¿Qué debo hacer si un activo no aparece en la lista?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la entidad cabecera relacionada con los cambios de activos, concretamente `ssach_modify_line` que contiene registros de modificaciones. Este modelo permite gestionar las etapas del proceso de cambios en los activos, asegurando la correcta trazabilidad de las acciones realizadas. Las relaciones entre tablas se ven reflejadas en los triggers que permiten mantener la integridad de los datos, como por ejemplo, `SSACH_LOAD_ASSET_STATUS` y `SSACH_LOAD_VALUE_ASSET`, que se activan durante los procesos de modificación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssach_assets_changes` |
| `ssach_modify_asset` |
| `ssach_modify_line` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssach_assets_changes` | ssach_assets_changes | — | — | ad_client_id→ad_client; ad_column_id→ad_column; ad_field_id→ad_field; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_column, ad_field. | PK `ssach_assets_changes_key`; Cols: ad_column_id, ad_field_id; `SSACH_ASSETS_CHANGES_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssach_modify_asset` | ssach_modify_asset | — | — | a_asset_id→a_asset; ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype | Detalle enlazado a a_asset, ad_client, ad_org. | PK `ssach_modify_asset_key`; Cols: c_doctype_id, documentno, description, a_asset_id, name; `SSACH_MODIFY_ASSET_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssach_modify_line` | ssach_modify_line | `SSACH_LOAD_ASSET_STATUS`; `SSACH_LOAD_VALUE_ASSET` | — | ssach_assets_changes_id→ssach_assets_changes; ssach_modify_asset_id→ssach_modify_asset; ssach_modify_asset_id→ssach_modify_asset; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ssach_assets_changes, ssach_modify_asset. Validado por trigger(s): SSACH_LOAD_ASSET_STATUS, SSACH_LOAD_VALUE_ASSET. | PK `ssach_modify_line_key`; Cols: is_modify, previous_record, actual_record, name_field, ssach_modify_asset_id; `SSACH_MODIFY_LINE_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssach_assets_changes` |
| `ssach_modify_asset` |
| `ssach_modify_line` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de dos ventanas principales: 'Cambios Activo' y 'Modificar activo', donde los usuarios pueden acceder a las funcionalidades necesarias para realizar cambios en activos existentes. La interfaz es intuitiva, permitiendo a los usuarios seleccionar activos y aplicar modificaciones de manera efectiva.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.assets.changes.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Cambios Activo | Assets Changes |
| Modificar activo | Modify Asset |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Cambios Activo | Assets Changes | No |
| Modificar activo | Modify Asset | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.assets.changes.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Cambios Activo

- **AD_WINDOW_ID:** `26FDBBA99BCF4EEA9FB3792E2DB88885`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `D9B82A3FFF6B4B8B91CC35A48D97A2E4` | 0 |

### Ventana: Modificar activo

- **AD_WINDOW_ID:** `03F4F8A399C040CB9ED7F7B96306A7AB`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `98FB4CED424D43DA859F45CCA08297C9` | 0 |
| 20 | Lines | `DCFDB82837374B569DF4A274E1DAABB7` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Lines (ventana: Modificar activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | IS_Modify | `IS_Modify` | No | No | — |
| 30 | Previous_Record | `Previous_Record` | No | Sí | — |
| 40 | Actual_Record | `Actual_Record` | No | No | — |
| 50 | Name_Field | `Name_Field` | No | Sí | — |
| 70 | Active | `Isactive` | No | No | — |

### Header (ventana: Modificar activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 30 | Document No. | `DocumentNo` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Asset | `A_Asset_ID` | No | No | — |
| 60 | Name | `Name` | No | Sí | — |
| 70 | Active | `Isactive` | No | No | — |
| 90 | Load_Fields | `Load_Fields` | No | No | — |
| 100 | load_changes | `Process` | No | No | — |

### Header (ventana: Cambios Activo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Field | `AD_Field_ID` | No | No | — |
| 30 | Column | `AD_Column_ID` | No | No | — |
| 40 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dentro del módulo, los procesos típicos incluyen botones como 'Completar' y 'Retornar', utilizados para finalizar o cancelar cambios en activos, respectivamente. Los informes generados, como 'Imprimir Activo Modificado', permiten visualizar los resultados de las modificaciones realizadas. Las validaciones frecuentes suelen incluir comprobaciones de existencia de activos y la validez de los datos introducidos para asegurar la calidad de la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.assets.changes.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar campos | Load_Fields | Load_Fields | Java `LoadField` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssach_Modify_Asset_ID` | `src/com/sidesoft/assets/changes/ad_process/LoadField.java` |
| Botón (Java) | Procesar | load_changes | load_changes | Java `ProcessAssetChanges` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssach_Modify_Asset_ID` | `src/com/sidesoft/assets/changes/ad_process/ProcessAssetChanges.java` |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Imprimir Activo Modificado | PrintAssetModify | PrintAssetModify | Java `AssetModifyReport` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/assets/changes/ad_Reports/Rpt_AssetModify.jrxml`; contexto sesión `—`. | `src/com/sidesoft/assets/changes/ad_process/AssetModifyReport.java` |
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
| Botón (Java) | Cargar campos | `LoadField` | Proceso Java (toolbar/background) | `Ssach_Modify_Asset_ID` | — | `src/com/sidesoft/assets/changes/ad_process/LoadField.java` |
| Botón (Java) | Procesar | `ProcessAssetChanges` | Proceso Java (toolbar/background) | `Ssach_Modify_Asset_ID` | — | `src/com/sidesoft/assets/changes/ad_process/ProcessAssetChanges.java` |
| Reporte | Imprimir Activo Modificado | `AssetModifyReport` | Informe (servlet PDF) | `—` | com/sidesoft/assets/changes/ad_Reports/Rpt_AssetModify.jrxml | `src/com/sidesoft/assets/changes/ad_process/AssetModifyReport.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar campos | Load_Fields | Load_Fields | Java `LoadField` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssach_Modify_Asset_ID` | `src/com/sidesoft/assets/changes/ad_process/LoadField.java` |
| Botón (Java) | Procesar | load_changes | load_changes | Java `ProcessAssetChanges` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssach_Modify_Asset_ID` | `src/com/sidesoft/assets/changes/ad_process/ProcessAssetChanges.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar campos | Load_Fields | Java `LoadField` | Proceso Openbravo registro `Ssach_Modify_Asset_ID` | Proceso Openbravo registro `Ssach_Modify_Asset_ID` |
| Botón (Java) | Procesar | load_changes | Java `ProcessAssetChanges` | Proceso Openbravo registro `Ssach_Modify_Asset_ID` | Proceso Openbravo registro `Ssach_Modify_Asset_ID` |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Imprimir Activo Modificado | PrintAssetModify | PrintAssetModify | Java `AssetModifyReport` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/assets/changes/ad_Reports/Rpt_AssetModify.jrxml`; contexto sesión `—`. | `src/com/sidesoft/assets/changes/ad_process/AssetModifyReport.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 2**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **1**; archivos `*.jrxml` en el repo = **2**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Imprimir Activo Modificado | `PrintAssetModify` | Java `AssetModifyReport`; JRXML `com/sidesoft/assets/changes/ad_Reports/Rpt_AssetModify.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | PrintAssetModify. JRXML: `com/sidesoft/assets/changes/ad_Reports/Rpt_AssetModify.jrxml` |

### Plantillas sin proceso en diccionario

- `src/com/sidesoft/assets/changes/ad_Reports/Rpt_AssetModify.jrxml`
- `src/com/sidesoft/assets/changes/ad_Reports/Rpt_AssetModify_subreport.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `ssach_error_process` | Error | Error | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `ssach_load_field` | Line | Line | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `ssach_no_line` | No line present | No line present | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye varias clases Java, entre las que destacan aquellas encargadas de la identificación de activos y la actualización de numeraciones de documentos, que permiten gestionar la lógica de negocio de manera estructurada y escalable, facilitando la implementación de nuevas funcionalidades en el futuro.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.assets.changes`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `AssetsIdentify` | com | SimpleCallout | — | `src/com/sidesoft/assets/changes/ad_callouts/AssetsIdentify.java` |
| `UpdateDocNumber` | com | SimpleCallout | — | `src/com/sidesoft/assets/changes/ad_callouts/UpdateDocNumber.java` |
| `AssetModifyReport` | com | HttpSecureAppServlet | Proceso / informe Java | `src/com/sidesoft/assets/changes/ad_process/AssetModifyReport.java` |
| `LoadField` | com | DalBaseProcess | — | `src/com/sidesoft/assets/changes/ad_process/LoadField.java` |
| `ProcessAssetChanges` | com | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/assets/changes/ad_process/ProcessAssetChanges.java` |
| `UpdateSequence` | com | EntityPersistenceEventObserver | — | `src/com/sidesoft/assets/changes/event/UpdateSequence.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSACH_LOAD_ASSET_STATUS` | `ssach_modify_line` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSACH_LOAD_VALUE_ASSET` | `ssach_modify_line` | after INSERT | SELECT a_asset_id INTO V_ASSET_ID FROM a_asset WHERE a_asset_id=V_ASSET_ID; New.actual_record |
| AD_VAL_RULE | — | `Assest Colums Table exist` | `AD_Column.AD_Column_ID=(Select AD_Column_ID FROM AD_Field where AD_Field_ID=@AD_Field_ID@)` |
| AD_VAL_RULE | — | `Validation Asset Modify` | `c_doctype.AD_TABLE_ID IN (

SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(tablename) = UPPER('ssach_modify_asset'))` |
| AD_VAL_RULE | — | `Asset Fields Exist` | `ad_field.ad_field_id not in (select ad_field_id from ssach_assets_changes) AND (ad_field.showinrelation='Y' OR ad_field.` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers juegan un rol crítico al automatizar procesos y mantener la integridad de los datos dentro de las operaciones del módulo. Las funciones PL para soporte son limitadas, pero los triggers establecidos garantizan un flujo adecuado de información entre la base de datos y la aplicación, permitiendo que se realicen operaciones en tiempo real.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSACH_LOAD_ASSET_STATUS` | `ssach_modify_line` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSACH_LOAD_ASSET_STATUS.xml` |
| `SSACH_LOAD_VALUE_ASSET` | `ssach_modify_line` | after | INSERT | SELECT a_asset_id INTO V_ASSET_ID FROM a_asset WHERE a_asset_id=V_ASSET_ID; New.actual_record | `model/triggers/SSACH_LOAD_VALUE_ASSET.xml` |
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
| 1 | Cargar campos | `Load_Fields` | Botón (Java) | Java `LoadField` | N | Proceso Openbravo registro `Ssach_Modify_Asset_ID` |
| 2 | Procesar | `load_changes` | Botón (Java) | Java `ProcessAssetChanges` | N | Proceso Openbravo registro `Ssach_Modify_Asset_ID` |
| 3 | Imprimir Activo Modificado | `PrintAssetModify` | Reporte | Java `AssetModifyReport` | S | Genera PDF desde JRXML `com/sidesoft/assets/changes/ad_Reports/Rpt_AssetModify.jrxml`; contexto sesión `—`. |

**Total acciones documentadas (extract):** **3** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `ec.com.sidesoft.assets.changes`.

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

# Glosario — prefijo `SSACH`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSACH` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.assets.changes` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Load_Fields` — Cargar campos
- `load_changes` — Procesar
- `PrintAssetModify` — Imprimir Activo Modificado

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Assets Customizations
**Package:** `ec.com.sidesoft.assets.customizations`

# Module overview — Assets Customizations

## Functional

El módulo 'Assets Customizations' está diseñado para personalizar el manejo de activos en Openbravo, facilitando la gestión de facturas asociadas y mejorando la experiencia del usuario en el proceso de gestión de activos. Está dirigido principalmente a usuarios de negocio que manejan activos, así como a equipo de soporte técnico de nivel 2 que necesita entender la funcionalidad y el flujo del módulo. Su alcance engloba la modificación de tablas críticas como A_ASSET, C_DOCTYPE y C_INVOICELINE para adaptarse a requerimientos específicos. Tiene como dependencia la compatibilidad con '2.50 to 3.00 Compatibility Skin'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/assets/customizations` |
| Web | `web/ec.com.sidesoft.assets.customizations/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSAC`

# Guía de chat — Assets Customizations

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.assets.customizations`).

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

- ¿Cómo puedo personalizar la gestión de activos en Openbravo?
- ¿Qué tablas se ven afectadas al manejar activos en este módulo?
- ¿Qué validaciones se aplican al crear un nuevo activo?
- ¿Cómo afecta el trigger 'SSAC_CREATEASSET_TRG' en el manejo de activos?
- ¿Cuál es el flujo típico para gestionar una factura relacionada con un activo?
- ¿Qué dependencia debo considerar al actualizar el módulo?
- ¿Puedo modificar la lógica del trigger para adaptarlo a mis necesidades?
- ¿Dónde encuentro documentación sobre las tablas afectadas por el módulo?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad cabecera 'A_ASSET', que representa los activos individuales dentro del sistema. Las relaciones con las tablas C_DOCTYPE y C_INVOICELINE son esenciales para la gestión de documentos y líneas de factura asociadas a los activos, permitiendo un flujo de información efectivo entre ellos. El módulo incluye un trigger clave denominado 'SSAC_CREATEASSET_TRG', el cual se activa tras la creación de un nuevo activo, asegurando que se realicen las acciones necesarias en el sistema, como actualizaciones o validaciones relevantes para el proceso de manejo de activos.

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

`A_ASSET`, `C_DOCTYPE`, `C_INVOICELINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no cuenta con ventanas específicas, lo que sugiere que las personalizaciones se integran directamente en las existentes en Openbravo. Los usuarios pueden navegar a través del módulo utilizando las opciones generales del ERP, accediendo a las funcionalidades vinculadas a la gestión de activos mediante las ventanas predefinidas del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.assets.customizations.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.assets.customizations.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 296 | Asset Purchase | `EM_Ssac_Isassetpurchase` | No | No | — |

### Pestaña `291`

- **AD_TAB_ID:** `291` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 79 | Asset Type | `EM_Ssac_Assettype` | No | No | — |
| 79 | Asset Group | `EM_Ssac_Asset_Group_ID` | No | No | — |

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 210 | Invoice | `EM_Ssac_Invoice_ID` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que no se especifican botones o procesos típicos adicionales en el inventario, se infiere que la interacción principal del usuario se realiza mediante operaciones en las ventanas existentes del ERP, donde pueden completar o retornar documentos relacionados con los activos. Las validaciones frecuentes se basan en el aseguramiento de la integridad de datos al modificar las tablas de activos y facturas, refiriéndose a las configuraciones establecidas en el trigger y las funciones PL del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.assets.customizations.es_ES/referencedata/translation/`.

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

El módulo no incluye clases Java, lo que sugiere que su funcionalidad se basa completamente en configuraciones de base de datos y lógica de triggers PL, sin la necesidad de personalizaciones a nivel de código en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.assets.customizations`.

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
| Trigger `SSAC_CREATEASSET_TRG` | `a_asset` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Función PL `ssac_createasset` | — | invocación proceso | No se encontro tipo de documento por defecto para la tabla A_Asset |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL desempeñan un papel crucial en el soporte técnico, ya que garantizan que las operaciones sobre las tablas de activos y facturas se realicen con las reglas de negocio definidas. El trigger 'SSAC_CREATEASSET_TRG' es responsable de ejecutar la lógica necesaria al crear nuevos activos, asegurando que cualquier validación o actualización requerida se lleve a cabo sin problemas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSAC_CREATEASSET_TRG` | `a_asset` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSAC_CREATEASSET_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssac_createasset` | — | No se encontro tipo de documento por defecto para la tabla A_Asset | No se encontro tipo de documento por defecto para la tabla A_Asset | `model/functions/SSAC_CREATEASSET.xml` |
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

Módulo: `ec.com.sidesoft.assets.customizations`.

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

# Glosario — prefijo `SSAC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSAC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.assets.customizations` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Assets Reports
**Package:** `ec.com.sidesoft.assets.reports`

# Module overview — Sidesoft Assets Reports

## Functional

El módulo Sidesoft Assets Reports está diseñado para gestionar y presentar información acerca de los activos dentro de una organización. Los actores principales incluyen usuarios de negocio que requieren reportes detallados de los activos, así como el equipo de soporte y desarrolladores que mantienen y optimizan la funcionalidad del módulo. Este módulo asegura que los usuarios puedan acceder a reportes necesarios para la toma de decisiones y el análisis de activos. Tiene como dependencia principal el Core de Openbravo, asegurando su integración y funcionalidad dentro del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/assets/reports` |
| Web | `web/ec.com.sidesoft.assets.reports/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSAR`

# Guía de chat — Sidesoft Assets Reports

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.assets.reports`).

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

- ¿Cómo puedo generar un informe detallado de los activos?
- ¿Qué pasos debo seguir para imprimir un activo específico?
- ¿Puedo revisar el historial de un activo anteriormente reportado?
- ¿Qué tipos de filtros puedo aplicar a los reportes de activos?
- ¿Hay algún reporte que me muestre los activos dados de baja?
- ¿Qué datos necesito para imprimir el informe 'Proceso de impresión - Baja de activos'?
- ¿Es posible personalizar los campos que aparecen en los reportes?
- ¿Cómo puedo acceder al módulo de Sidesoft Assets Reports desde el menú principal?

# Domain — data model

## Functional

La entidad cabecera de este módulo se centra en los activos, gestionados a través de informes que permiten visualizar su estado, historial y operación. Aunque no hay tablas físicas dedicadas en este módulo, se modifican propiedades de la tabla A_ASSET para integrar nuevos campos y reportes. Las relaciones se establecen en torno a los activos y sus categorías, y los triggers y funciones necesarias están implementadas para facilitar la generación de informes y la automatización de procesos. Sin embargo, actualmente no se han registrado triggers específicos ni funciones PL dentro del módulo.

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

`A_ASSET`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación en el módulo Sidesoft Assets Reports se realiza mediante un menú en la interfaz de usuario que permite acceder directamente a los reportes y funciones disponibles. Aunque no se han definido ventanas específicas en el inventario, los usuarios interactúan con las opciones del menú para generar los reportes deseados de activos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.assets.reports.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Activos por custodio | Custodian assets | No |
| Bienes Valorados | Valued Assets | No |
| Depreciación del periodo | Depreciation for the period | No |
| Histórico de activos | Asset history | No |
| Histórico de activos detallado | Detailed Historical Asset Report | No |
| Reporte Historial Depreciación de Activos | Asset Depreciation History Report | No |
| Saldos por mes | Balances per month | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.assets.reports.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 303 | Color | `EM_Ssar_Color` | No | No | — |
| 304 | Measurements | `EM_Ssar_Measurements` | No | No | — |
| 305 | Other attributes | `EM_Ssar_Other_Attributes` | No | No | — |
| 306 | Warranty date | `EM_Ssar_Warranty_Date` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dentro de los procesos del módulo, los usuarios encuentran botones típicos como completar, retornar y rechazar, utilizados para gestionar los diferentes reportes de activos. Se dispone de tres reportes principales: el 'Histórico de activos detallado', 'Imprimir Activo' y 'Proceso de impresión - Baja de activos', que son esenciales para la gestión de activos. Las validaciones frecuentes aseguran que los datos presentados en los informes sean precisos y relevantes, permitiendo una adecuada toma de decisiones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.assets.reports.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Activos por custodio | Custodian assets | Custodian assets | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Bienes Valorados | Valued Assets | Valued Assets | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Depreciación del periodo | Depreciation for the period | Depreciation for the period | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Histórico de activos | Asset history | Asset history | *(OBUIAPP / manual)* | Asset history | — |
| Proceso / otro | Reporte Historial Depreciación de Activos | Asset Depreciation History Report | Asset Depreciation History Report | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Saldos por mes | Balances per month | Balances per month | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Histórico de activos detallado | Detailed Historical Asset Report | Detailed Historical Asset Report | *(OBUIAPP / manual)* | — | — |
| Reporte | Imprimir Activo | Print Asset | PrintAsset | Java `AssetReport` (AD_MODEL_OBJECT `S`) | Servlet de informe `AssetReport` (fuente no en `src/` del módulo). | — |
| Reporte | Proceso de impresion - Baja de activos | PRINT GENERIC - ALIENATE ASSETS | PRINT GENERIC - ALIENATE ASSETS | Java `AssetWriteOff` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `4D8410A8736C4C62AACEDE8507B0517C|ssam_alienate_id`. | `src/ec/com/sidesoft/assets/reports/ad_Reports/AssetWriteOff.java` |
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
| Reporte | Imprimir Activo | `AssetReport` | Informe (servlet) | `—` | — | `—` |
| Reporte | Proceso de impresion - Baja de activos | `AssetWriteOff` | Informe (servlet PDF) | `4D8410A8736C4C62AACEDE8507B0517C|ssam_alienate_id` | — | `src/ec/com/sidesoft/assets/reports/ad_Reports/AssetWriteOff.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Activos por custodio | Custodian assets | Custodian assets | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Bienes Valorados | Valued Assets | Valued Assets | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Depreciación del periodo | Depreciation for the period | Depreciation for the period | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Histórico de activos | Asset history | Asset history | *(OBUIAPP / manual)* | Asset history | — |
| Proceso / otro | Reporte Historial Depreciación de Activos | Asset Depreciation History Report | Asset Depreciation History Report | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Saldos por mes | Balances per month | Balances per month | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Activos por custodio | Custodian assets | — | — | — |
| Proceso / otro | Bienes Valorados | Valued Assets | — | — | — |
| Proceso / otro | Depreciación del periodo | Depreciation for the period | — | — | — |
| Proceso / otro | Histórico de activos | Asset history | — | Asset history | — |
| Proceso / otro | Reporte Historial Depreciación de Activos | Asset Depreciation History Report | — | — | — |
| Proceso / otro | Saldos por mes | Balances per month | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Histórico de activos detallado | Detailed Historical Asset Report | Detailed Historical Asset Report | *(OBUIAPP / manual)* | — | — |
| Reporte | Imprimir Activo | Print Asset | PrintAsset | Java `AssetReport` (AD_MODEL_OBJECT `S`) | Servlet de informe `AssetReport` (fuente no en `src/` del módulo). | — |
| Reporte | Proceso de impresion - Baja de activos | PRINT GENERIC - ALIENATE ASSETS | PRINT GENERIC - ALIENATE ASSETS | Java `AssetWriteOff` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `4D8410A8736C4C62AACEDE8507B0517C|ssam_alienate_id`. | `src/ec/com/sidesoft/assets/reports/ad_Reports/AssetWriteOff.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 8**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **3**; archivos `*.jrxml` en el repo = **8**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Histórico de activos detallado | `Detailed Historical Asset Report` | — | *(ver AD_PROCESS_PARA / servlet)* | Detailed Historical Asset Report |
| 2 | Imprimir Activo | `PrintAsset` | Java `AssetReport`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Print Asset |
| 3 | Proceso de impresion - Baja de activos | `PRINT GENERIC - ALIENATE ASSETS` | Java `AssetWriteOff`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | PRINT GENERIC - ALIENATE ASSETS |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/assets/reports/ad_Reports/AssetDepreciationHistoryReport.jrxml`
- `src/ec/com/sidesoft/assets/reports/ad_Reports/AssetHistory.jrxml`
- `src/ec/com/sidesoft/assets/reports/ad_Reports/AssetWriteOff.jrxml`
- `src/ec/com/sidesoft/assets/reports/ad_Reports/BalancesPerMonth.jrxml`
- `src/ec/com/sidesoft/assets/reports/ad_Reports/CustodianAssets.jrxml`
- `src/ec/com/sidesoft/assets/reports/ad_Reports/DepreciationPeriod.jrxml`
- `src/ec/com/sidesoft/assets/reports/ad_Reports/RptDetailedAssetHistory.jrxml`
- `src/ec/com/sidesoft/assets/reports/ad_Reports/ValuedAssets.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Ssar_Label_AssetHistory_AssetHistory` | Asset History | Asset History | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye varias clases Java, como AssetWriteOff y las clases de expresión de filtro, que ayudan a realizar operaciones específicas y gestionar la lógica detrás de la generación de informes. Estas clases manejan la interacción con los datos y permiten que los reportes se generen de manera efectiva y dinámica según las necesidades de los usuarios.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.assets.reports`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `AssetWriteOff` | ad_Reports | HttpSecureAppServlet | — | `src/ec/com/sidesoft/assets/reports/ad_Reports/AssetWriteOff.java` |
| `AssetFilterExpression` | filterexpression | FilterExpression | — | `src/ec/com/sidesoft/assets/reports/filterexpression/AssetFilterExpression.java` |
| `CustodianFilterExpression` | filterexpression | FilterExpression | — | `src/ec/com/sidesoft/assets/reports/filterexpression/CustodianFilterExpression.java` |
| `SubCategoryFilterExpression` | filterexpression | FilterExpression | — | `src/ec/com/sidesoft/assets/reports/filterexpression/SubCategoryFilterExpression.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Is employee` | `C_BPartner.IsEmployee = 'Y'` |
| AD_VAL_RULE | — | `User Log Assets` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Assets Org` | `AD_ORG.AD_ORG_ID = @#AD_ORG_ID@` |
| AD_VAL_RULE | — | `Assets rule` | `(A_Asset.EM_Ssam_Assettype=@EM_Ssam_Assettype@ OR @EM_Ssam_Assettype@ is null)  AND 
(A_Asset.EM_Ssal_Custodio_ID=@C_BPa` |
| AD_VAL_RULE | — | `Assets Custodian` | `C_BPartner.IsEmployee = 'Y' AND C_BPartner.C_BPartner_ID IN ( Select EM_Ssal_Custodio_ID  
FROM A_Asset WHERE 
(A_Asset.` |
| AD_VAL_RULE | — | `Assets Subgroup` | `ssasl_subcategory.ssasl_subcategory_id in ( 
select ssasl_subcategory_id 
from  ssasl_subcategory  
where a_asset_group_` |
| AD_VAL_RULE | — | `Assets Group` | `A_Asset_Group.A_Asset_Group_ID in ( SELECT A_Asset_Group_ID FROM A_Asset WHERE EM_Ssam_Assettype=@EM_Ssam_Assettype@)` |
| AD_VAL_RULE | — | `SSAR_ValidateSubcategory` | `ssasl_subcategory.ssasl_subcategory_id in ( 
select ssasl_subcategory_id 
from  ssasl_subcategory  
where a_asset_group_` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Aunque el módulo no presenta triggers ni funciones PL registradas, el rol de estos elementos en otros módulos y en la estructura de Openbravo es crítico para el soporte. Sin embargo, se espera que en este caso, funciones Java implementadas tienen un rol más prominente en el procesamiento de datos y generación de informes.

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
| 1 | Histórico de activos detallado | `Detailed Historical Asset Report` | Reporte | — | S | — |
| 2 | Imprimir Activo | `PrintAsset` | Reporte | Java `AssetReport` | S | Servlet de informe `AssetReport` (fuente no en `src/` del módulo). |
| 3 | Proceso de impresion - Baja de activos | `PRINT GENERIC - ALIENATE ASSETS` | Reporte | Java `AssetWriteOff` | S | Genera PDF desde JRXML `—`; contexto sesión `4D8410A8736C4C62AACEDE8507B0517C|ssam_alienate_id`. |

**Total acciones documentadas (extract):** **3** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `ec.com.sidesoft.assets.reports`.

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

# Glosario — prefijo `SSAR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSAR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.assets.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Custodian assets` — Activos por custodio
- `Valued Assets` — Bienes Valorados
- `Depreciation for the period` — Depreciación del periodo
- `Asset history` — Histórico de activos
- `Asset Depreciation History Report` — Reporte Historial Depreciación de Activos
- `Balances per month` — Saldos por mes
- `Detailed Historical Asset Report` — Histórico de activos detallado
- `PrintAsset` — Imprimir Activo
- `PRINT GENERIC - ALIENATE ASSETS` — Proceso de impresion - Baja de activos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Assets Automatic Sequence
**Package:** `ec.com.sidesoft.assets.sequence`

# Module overview — Sidesoft Assets Automatic Sequence

## Functional

El módulo 'Sidesoft Assets Automatic Sequence' tiene como propósito gestionar las secuencias automáticas para activos en la plataforma Openbravo. Está diseñado para ser utilizado por usuarios de negocio que requieran una gestión eficiente de los activos, así como por el equipo de soporte técnico y desarrolladores que busquen personalizar o extender las funcionalidades del sistema. El alcance del módulo abarca la creación y seguimiento de secuencias automáticas vinculadas a categorías de activos y subcategorías. Depende de la compatibilidad con la skin 2.50 a 3.00, lo que optimiza su implementación y uso en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/assets/sequence` |
| Web | `web/ec.com.sidesoft.assets.sequence/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSASEQ`

# Guía de chat — Sidesoft Assets Automatic Sequence

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.assets.sequence`).

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

- ¿Cómo puedo crear una nueva secuencia automática para un activo?
- ¿Dónde puedo ver las secuencias actuales asignadas a mis activos?
- ¿Qué debo hacer si el valor de la secuencia no se está actualizando correctamente?
- ¿Cómo se relacionan las subcategorías de activos con las secuencias automáticas?
- ¿Hay alguna forma de personalizar las secuencias para diferentes tipos de activos?
- ¿Cómo puedo revisar el historial de cambios de secuencias en el módulo?
- ¿Qué dependencias debo considerar al implementar este módulo en mi entorno?
- ¿Cómo se puede verificar si el módulo está instalado y funcionando correctamente?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la entidad 'A_ASSET_GROUP' y la subcategoría 'SSASL_SUBCATEGORY'. Estas tablas son fundamentales para organizar y clasificar los activos dentro del sistema. Se ha implementado un trigger, 'SSASEQ_VALUE_SEQUENCE_TRG', que se activa en la tabla 'a_asset' y tiene el objetivo de automatizar la gestión del valor de la secuencia. Este trigger permite mantener la integridad de los datos y asegurar la correcta ejecución de las secuencias automáticas, siendo crucial para el funcionamiento del módulo.

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

`A_ASSET_GROUP`, `SSASL_SUBCATEGORY`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no presenta ventanas específicas para la navegación en la interfaz de usuario, lo que sugiere una integración directa con las funcionalidades del sistema. Los usuarios interactuarán con las operaciones relacionadas en las pantallas donde se gestionen los activos, sin ventanas adicionales específicas dentro del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.assets.sequence.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.assets.sequence.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `16779DFE22FE470090FC951574FBBCBA`

- **AD_TAB_ID:** `16779DFE22FE470090FC951574FBBCBA` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 45 | EM_Ssaseq_Sequence_Prefix | `EM_Ssaseq_Sequence_Prefix` | No | No | — |
| 75 | EM_Ssaseq_Current_Value | `EM_Ssaseq_Current_Value` | No | No | — |
| 85 | EM_Ssaseq_Sequence_Prefix_Pe | `EM_Ssaseq_Sequence_Prefix_Pe` | No | No | — |
| 95 | EM_Ssaseq_Current_Value_Pe | `EM_Ssaseq_Current_Value_Pe` | No | No | — |

### Pestaña `452`

- **AD_TAB_ID:** `452` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 160 | EM_Ssaseq_Sequence_Prefix | `EM_Ssaseq_Sequence_Prefix` | No | No | — |
| 170 | EM_Ssaseq_Seq_Prefix_Pe | `EM_Ssaseq_Seq_Prefix_Pe` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Aunque no se han definido botones de procesamiento típicos dentro del módulo, su funcionamiento está en gran medida regido por el trigger mencionado, que se activa automáticamente durante los eventos de gestión de activos. Las validaciones frecuentes incluyen asegurar que las categorías y subcategorías de activos tengan secuencias apropiadas, siendo esencial para la correcta administración del inventario de activos. Dado que no hay informes definidos, se espera que el estado y gestión de las secuencias se maneje a través de las vistas estándar del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.assets.sequence.es_ES/referencedata/translation/`.

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

El módulo incluye una clase Java, 'Sequence_Current', que extiende la funcionalidad del sistema al permitir la automatización de la asignación de valores secuenciales a los activos a través de callouts. Esta clase gestiona la recuperación de datos y la lógica necesaria para actualizar las secuencias según las categorías y subcategorías de activos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.assets.sequence`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Sequence_Current` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/assets/sequence/ad_callouts/Sequence_Current.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSASEQ_VALUE_SEQUENCE_TRG` | `a_asset` | after INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers desempeñan un rol fundamental en la base de datos, siendo responsables de las actualizaciones automáticas y la integridad de las secuencias de activos. Aunque el módulo no cuenta con funciones PL específicas, el trigger implementado en 'a_asset' es esencial para asegurar que los valores de secuencia se asignen correctamente en el momento adecuado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSASEQ_VALUE_SEQUENCE_TRG` | `a_asset` | after | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSASEQ_VALUE_SEQUENCE_TRG.xml` |
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

Módulo: `ec.com.sidesoft.assets.sequence`.

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

# Glosario — prefijo `SSASEQ`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSASEQ` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.assets.sequence` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Assets Taxes
**Package:** `ec.com.sidesoft.assets.taxes`

# Module overview — Sidesoft Assets Taxes

## Functional

El módulo Sidesoft Assets Taxes tiene como propósito la gestión de impuestos relacionados con activos en el sistema Openbravo ERP. Este módulo permite a los usuarios de negocio procesar y calcular impuestos en función de las categorías fiscales asociadas a los activos. Los actores principales incluyen administradores de activos y contadores que deben asegurarse de que los impuestos se calculen correctamente conforme a la legislación vigente. El alcance del módulo se limita a la integración de impuestos específicos para la administración de activos, dependiendo de su relación con otros módulos como Sidesoft Assets Reports y el Core de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/assets/taxes` |
| Web | `web/ec.com.sidesoft.assets.taxes/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Sidesoft Assets Reports

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSATAX`

# Guía de chat — Sidesoft Assets Taxes

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.assets.taxes`).

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

- ¿Cómo puedo calcular el impuesto de un activo específico?
- ¿Qué criterios se utilizan para categorizar los activos en el sistema?
- ¿Dónde puedo encontrar el reporte de impuestos aplicables a mis activos?
- ¿Qué debo hacer si la tasa de impuesto en el sistema parece incorrecta?
- ¿Hay algún límite sobre qué activos pueden ser gravados con impuestos?
- ¿Cómo se actualizan las tasas de impuesto en el módulo?
- ¿Existen validaciones automáticas al ingresar datos sobre un activo?
- ¿Cómo puedo acceder a la configuración del módulo de impuestos de activos?

# Domain — data model

## Functional

La entidad principal del módulo es la cabecera relacionada con los activos, particularmente la tabla 'A_ASSET', que ha sido modificada para incorporar campos adicionales relacionados con los impuestos. Este modelo se estructura en torno a la identificación de categorías fiscales y su correspondiente tasa impositiva. La relación entre activo y categoría fiscal se establece a través de clases en la base de datos, donde una categoría puede tener múltiples tasas aplicables, facilitando así el cálculo de impuestos en diferentes contextos. Aunque no se han definido triggers específicos en el módulo, su implementación puede ser considerada en futuras actualizaciones.

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

`A_ASSET`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de la interfaz de usuario de Openbravo, donde se debe acceder a la sección asignada para la gestión de activos. A pesar de que no se listan ventanas específicas en el inventario, los usuarios pueden esperar una experiencia coherente y alineada con la navegación estándar de Openbravo, lo que les permitirá seleccionar activos y realizar operaciones relacionadas con los impuestos de manera intuitiva.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.assets.taxes.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.assets.taxes.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 232 | Tax Group | `em_ssatax_c_taxcategory_id` | No | No | — |
| 234 | Tax | `em_ssatax_taxamt` | No | Sí | — |
| 236 | Total Purchase Amount | `em_ssatax_totalpurchaseamt` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos típicos dentro del módulo incluyen la capacidad de calcular y aplicar impuestos sobre el valor de los activos. Los principales botones que los usuarios pueden encontrar durante sus tareas incluirán opciones como completar, retornar o rechazar procesos relacionados con la gestión de impuestos. Aunque no se especifican informes en el inventario, es importante considerar la generación de reportes para el cumplimiento fiscal que probablemente se implementen a través de módulos relacionados. Las validaciones frecuentes incluirán la comprobación de que las tasas de impuestos aplicables sean válidas y coherentes con las categorías fiscales seleccionadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.assets.taxes.es_ES/referencedata/translation/`.

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
| `SSATAX_NoTaxGroup` | You must select a tax group | You must select a tax group | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye una clase Java llamada SSATAX_TaxCategory, que se encarga de realizar cálculos de impuestos de acuerdo con las categorías fiscales seleccionadas. Esta clase utiliza la lógica de negocios para determinar automáticamente el monto del impuesto y el total a pagar en función del valor del activo, asegurando así que los cálculos se realicen de manera eficiente y precisa.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.assets.taxes`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SSATAX_TaxCategory` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/assets/taxes/ad_callouts/SSATAX_TaxCategory.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Tipo de Retención VAT` | `em_sswh_withholdingtype='VA'` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

En el contexto de la base de datos, aunque no se han definido triggers o funciones PL dentro del módulo, la estructura de las tablas modificadas permite una interpretación óptima de los datos. Los desarrolladores pueden implementar futuras funciones que faciliten el soporte y mantenimiento del módulo, aprovechando las tablas modificadas para incorporar lógicas de negocio específicas.

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

Módulo: `ec.com.sidesoft.assets.taxes`.

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

# Glosario — prefijo `SSATAX`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSATAX` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.assets.taxes` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Control Assets
**Package:** `ec.com.sidesoft.control.assets`

# Module overview — Sidesoft Control Assets

## Functional

El módulo Sidesoft Control Assets está diseñado para la gestión y control de activos dentro de una organización. Su propósito principal es permitir a los usuarios un seguimiento efectivo de los bienes, a través de procesos que integran tanto aspectos técnicos como de gestión de negocio. Los actores involucrados son usuarios de negocio que realizan el seguimiento de activos, personal de soporte de nivel 2 encargado de resolver incidencias, y desarrolladores que mantienen y mejoran el sistema. Este módulo es compatible con el núcleo de Openbravo y depende de la compatibilidad entre versiones, específicamente entre 2.50 y 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/control/assets` |
| Web | `web/ec.com.sidesoft.control.assets/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SCRTLA`

# Guía de chat — Sidesoft Control Assets

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.control.assets`).

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

- ¿Cómo puedo añadir un nuevo activo en el sistema?
- ¿Qué pasos debo seguir para actualizar la información de un activo existente?
- ¿Cómo se manejan los informes relacionados con los activos?
- ¿Qué debo hacer si un activo está dañado o no se puede localizar?
- ¿Cómo verificar el historial de cambios en la gestión de activos?
- ¿Puedo asignar un activo a un departamento específico?
- ¿Cómo se garantiza la seguridad de la información sobre los activos?
- ¿Qué acciones puedo tomar si encuentro un error en los registros de activos?

# Domain — data model

## Functional

El modelo de datos del módulo incluye entidades clave como C_DOCTYPE y M_PRODUCT, que son esenciales en la gestión documental de los activos. Aunque no se definen tablas físicas adicionales, la integración con estas entidades permite un control integral de los productos o activos del sistema. Actualmente, no hay triggers específicos, lo que implica que las validaciones y la lógica de negocio se manejan a través de otros mecanismos del ERP, dependiendo de los cambios en las tablas modificadas.

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

`C_DOCTYPE`, `M_PRODUCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no incluye ventanas específicas en su interfaz de usuario, lo que sugiere que la navegación se realiza de manera más directa a través de un menú único asociado al módulo. Los usuarios deberán familiarizarse con el acceso a las funcionalidades dado que la estructura de ventanas no se despliega de manera visualmente fragmentada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.control.assets.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Reporte Bienes de Control | Control Assets Report | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.control.assets.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 360 | Control Assets | `EM_Scrtla_Control_Assets` | No | No | — |

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 1400 | Control Assets | `EM_Scrtla_Control_Assets` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo cuenta con un único proceso que permite ejecutar ciertas operativas, asumiendo que el usuario puede completar, retornar o rechazar entradas relacionadas con los activos. Las validaciones frecuentes se enfocan en asegurar la integridad de los datos y la correcta asignación de activos a las categorías definidas. Dado que no se han definido informes específicos, los usuarios deberán confiar en los reportes generales disponibles en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.control.assets.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Bienes de Control | Control Assets Report | Control Assets Report | *(OBUIAPP / manual)* | Control Assets Report | — |
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
| Proceso / otro | Reporte Bienes de Control | Control Assets Report | Control Assets Report | *(OBUIAPP / manual)* | Control Assets Report | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Bienes de Control | Control Assets Report | — | Control Assets Report | — |
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
**Total de reportes del módulo: 1**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **1**.

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

No se han definido clases Java específicas para el módulo, lo que indica que su funcionalidad está diseñada para operar dentro del marco proporcionado por Openbravo sin dependencias de programación adicional.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.control.assets`.

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

Aunque no existen triggers o funciones PL específicas vinculadas al módulo, la integridad de datos y la lógica de procesos se mantiene a través de modificaciones en tablas esenciales del sistema. Esto refuerza la importancia de la gestión de datos confiables para el correcto funcionamiento del módulo dentro de Openbravo.

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

Módulo: `ec.com.sidesoft.control.assets`.

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

# Glosario — prefijo `SCRTLA`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SCRTLA` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.control.assets` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Control Assets Report` — Reporte Bienes de Control

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Asset Derecognize
**Package:** `ec.com.sidesoft.derecognize.asset`

# Module overview — Asset Derecognize

## Functional

El módulo 'Asset Derecognize' permite a los usuarios gestionar la baja de activos en el sistema Openbravo. Está diseñado para ser utilizado por empleados responsables del control de activos, así como por el equipo de soporte L2 que necesita comprender la lógica del módulo. Su alcance incluye la identificación y procesamiento de activos que ya no son necesarios para la organización. Este módulo depende del '2.50 to 3.00 Compatibility Skin' para su correcta visualización y funcionamiento en el entorno del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/derecognize/asset` |
| Web | `web/ec.com.sidesoft.derecognize.asset/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SDA`

# Guía de chat — Asset Derecognize

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.derecognize.asset`).

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

- ¿Cómo puedo dar de baja un activo?
- ¿Qué información necesito para registrar la baja de un activo?
- ¿Puedo revertir la baja de un activo una vez procesada?
- ¿Cómo se actualiza la información del activo antes de darlo de baja?
- ¿Qué sucede con el historial del activo después de la baja?
- ¿Existen restricciones para dar de baja ciertos activos?
- ¿Cómo se notifica la baja de un activo al equipo contable?
- ¿Hay algún informe que se genere después de dar de baja un activo?

# Domain — data model

## Functional

La entidad cabecera del módulo está relacionada con la tabla 'A_ASSET', la cual almacena información sobre los activos de la organización. Las etapas del proceso de baja de activos no están explícitamente definidas en este inventario, pero se puede inferir que el flujo sigue un proceso de identificación y marcado para baja. El módulo no cuenta con triggers específicos, lo que sugiere que la lógica en torno a la baja de activos se maneja a través de la función PL vinculada, la cual se activa mediante un botón en la interfaz del usuario.

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

`A_ASSET`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Este módulo no especifica ventanas en su diseño, por lo que la interacción se realiza posiblemente a través de formularios diseñados para operar con la entidad 'A_ASSET'. Los usuarios navegarían a través del módulo utilizando el menú principal del ERP, accediendo a opciones relacionadas con la baja de activos según las configuraciones establecidas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.derecognize.asset.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.derecognize.asset.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 480 | Derecognition Asset | `EM_Sda_Derecognition` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso central del módulo 'Asset Derecognize' se ejecuta a través de un botón de acción que permite a los usuarios completar la baja de activos. No se mencionan informes asociados a este proceso, lo que podría indicar un enfoque directo en la acción de baja sin necesidad de generación de reportes adicionales. Las validaciones habituales podrían incluir la verificación de que el activo está en condiciones de ser dado de baja y que se cumplen los requisitos legales y contables pertinentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.derecognize.asset.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Ejecutar Baja de Activos. | Derecognition Asset | sda_derecognition_asset | `sda_derecognition_asset` | Desvincular linea de amortizacion en el Activo | — |
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
| Botón (PL/pgSQL) | Ejecutar Baja de Activos. | Derecognition Asset | sda_derecognition_asset | `sda_derecognition_asset` | Desvincular linea de amortizacion en el Activo | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Ejecutar Baja de Activos. | Derecognition Asset | PL `sda_derecognition_asset` | Desvincular linea de amortizacion en el Activo | Desvincular linea de amortizacion en el Activo |
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

El módulo 'Asset Derecognize' no incluye implementación de clases en Java, lo que significa que toda la lógica se gestiona a través de procesos PL sin necesidad de extender funcionalidades mediante código Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.derecognize.asset`.

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
| Función PL `sda_derecognition_asset` | — | invocación proceso | Desvincular linea de amortizacion en el Activo |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El módulo cuenta con una función PL que se vincula directamente al proceso de baja de activos, lo que permite realizar la lógica de negocio necesaria en la base de datos. A pesar de no tener triggers, esta función es clave para garantizar que las actualizaciones se realicen correctamente en la tabla 'A_ASSET', asegurando la integridad de los datos.

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
| `sda_derecognition_asset` | Ejecutar Baja de Activos. | Desvincular linea de amortizacion en el Activo | Desvincular linea de amortizacion en el Activo | `model/functions/SDA_DERECOGNITION_ASSET.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ejecutar Baja de Activos. | `sda_derecognition_asset` | Botón (PL/pgSQL) | PL `sda_derecognition_asset` | N | Desvincular linea de amortizacion en el Activo |

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

Módulo: `ec.com.sidesoft.derecognize.asset`.

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

# Glosario — prefijo `SDA`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SDA` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.derecognize.asset` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `sda_derecognition_asset` — Ejecutar Baja de Activos.

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Asset Purchase Information
**Package:** `ec.com.sidesoft.ecuador.asset.purchase.info`

# Module overview — Sidesoft Asset Purchase Information

## Functional

El módulo Sidesoft Asset Purchase Information está diseñado para gestionar la información relacionada con la compra de activos en Ecuador. Actores clave incluyen personal de contabilidad, administración y compras, quienes utilizan la información para registrar, gestionar y reportar las adquisiciones de activos. El alcance del módulo se limita a la gestión de tipos de documentos y tipos de transacción. Dependencias notables incluyen la compatibilidad con la skin de versiones 2.50 a 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/ecuador/asset/purchase/info` |
| Web | `web/ec.com.sidesoft.ecuador.asset.purchase.info/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSAPI`

# Guía de chat — Sidesoft Asset Purchase Information

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.ecuador.asset.purchase.info`).

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
- «¿Qué es la tabla ssapi_documenttype?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo creo un nuevo tipo de documento?
- ¿Cuál es la diferencia entre los tipos de transacción?
- ¿Puedo editar un tipo de documento existente?
- ¿Qué campos son obligatorios al registrar un nuevo tipo de transacción?
- ¿Cómo puedo eliminar un tipo de documento?
- ¿Es posible generar un informe de los tipos de documentos usados?
- ¿Dónde encuentro la información de los activos adquiridos?
- ¿Qué debo hacer si veo un error en el registro de un tipo de documento?

# Domain — data model

## Functional

El modelo de datos gira en torno a dos entidades principales: los tipos de documentos y los tipos de transacción. La entidad cabecera es 'ssapi_documenttype', enfocándose en definir cómo se clasifican las transacciones de compra de activos. Aunque no se definen etapas complejas en este módulo, hay relaciones directas entre los tipos de documentos y las entradas asociadas a adquisiciones de activos. A pesar de que no se especifican triggers, es fundamental adaptar las tablas según las necesidades de reporte y validación en procesos de negocio.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssapi_documenttype` |
| `ssapi_trasactiontype` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssapi_documenttype` | SSAPI_Documenttype | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssapi_documenttype_key`; Cols: code, name, description; `SSAPI_ACT_MAIN_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssapi_trasactiontype` | SSAPI_Trasactiontype | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssapi_trasactiontype_key`; Cols: code, name, description; `SSAPI_ACT_MAIN_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SSAPI_Documenttype` |
| `SSAPI_Trasactiontype` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`A_ASSET`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo cuenta con dos ventanas accesibles desde el menú principal: 'Tipo de Documento' y 'Tipo de Transacción'. Los usuarios pueden navegar por estas ventanas para agregar, modificar o eliminar registros relacionados con la gestión de activos, permitiendo una clara organización de la documentación necesaria para cada compra.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.ecuador.asset.purchase.info.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Tipo de Documento | Document Type |
| Tipo de Transacción | Transaction Type |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Tipo de Documento | Document Type | No |
| Tipo de Transacción | Transaction Type | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.ecuador.asset.purchase.info.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Tipo de Documento

- **AD_WINDOW_ID:** `6363993DFB8140E6820F42F132E09121`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Document Type | `CB3104783F3C41E5ADB6173F142163BF` | 0 |

### Ventana: Tipo de Transacción

- **AD_WINDOW_ID:** `98194DA878A04B4AB824D6B224B42273`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Transaction Type | `4F43FE941987454FB87A0E6E3D2EEF52` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Document Type (ventana: Tipo de Documento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Code | `Code` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |

### Pestaña `800078`

- **AD_TAB_ID:** `800078` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 480 | Transaction Type | `EM_Ssapi_Trasactiontype_ID` | No | No | 01BBAC7D88AA4D0ABDF3F93E713CC234 |
| 490 | Document Type | `EM_Ssapi_Documenttype_ID` | No | No | 01BBAC7D88AA4D0ABDF3F93E713CC234 |
| 500 | Invoice | `EM_Ssapi_Invoice_ID` | No | No | — |
| 500 | Invoice No | `EM_Ssapi_Invoiceno` | No | No | 01BBAC7D88AA4D0ABDF3F93E713CC234 |
| 510 | Provider | `EM_Ssapi_Bpartner_ID` | No | No | — |
| 510 | Provider | `EM_Ssapi_Provider` | No | No | 01BBAC7D88AA4D0ABDF3F93E713CC234 |

### Transaction Type (ventana: Tipo de Transacción)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Code | `Code` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo no cuenta con botones de proceso típicos como completar o rechazar. En su lugar, se enfoca en la gestión de información a través de las interfaces de usuario. Aunque no hay informes predefinidos, los usuarios pueden realizar consultas específicas sobre los tipos de documentos y transacciones para desarrollar informes personalizados según las necesidades del negocio. Las validaciones frecuentes podrían incluir chequeos de coherencia en la información de tipos de documentos y su aplicación en transacciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.ecuador.asset.purchase.info.es_ES/referencedata/translation/`.

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

El módulo no cuenta con clases Java asociadas, lo que sugiere que la funcionalidad del módulo se centra principalmente en la interfaz de usuario y en la gestión de base de datos, sin lógica de negocio adicional implementada en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.ecuador.asset.purchase.info`.

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

No se cuentan con triggers ni funciones PL en este módulo, lo que indica que las validaciones y control de datos podría ser manejado directamente a través de las interfaces de usuario o mediante procesos de negocio. Sin embargo, es importante considerar cómo los datos se integran con otras tablas dentro del sistema, especialmente con la tabla 'A_ASSET', que ha sido modificada para reflejar nuevas necesidades.

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

Módulo: `ec.com.sidesoft.ecuador.asset.purchase.info`.

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

# Glosario — prefijo `SSAPI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSAPI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.ecuador.asset.purchase.info` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Hide Fields Asset
**Package:** `ec.com.sidesoft.hidefield.assets`

# Module overview — Hide Fields Asset

## Functional

El módulo 'Hide Fields Asset' tiene como propósito principal la gestión de la visibilidad de los campos en el activo del ERP Openbravo. Este módulo está diseñado para usuarios de negocio que desean personalizar su experiencia de usuario al ocultar campos que no son relevantes para ciertas funciones o roles. Los actores principales son los administradores del sistema que configuran las opciones de visibilidad de campos y los usuarios finales que interactúan con la interfaz del ERP. Su implementación depende de la compatibilidad con la '2.50 to 3.00 Compatibility Skin'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/hidefield/assets` |
| Web | `web/ec.com.sidesoft.hidefield.assets/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSHF`

# Guía de chat — Hide Fields Asset

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.hidefield.assets`).

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

- ¿Cómo puedo ocultar un campo en mi vista actual?
- ¿Este módulo es compatible con mi versión de Openbravo?
- ¿Qué permisos necesito para ocultar campos en el sistema?
- ¿Puedo reactivar un campo que he ocultado anteriormente?
- ¿Hay algún impacto en la funcionalidad al ocultar campos?
- ¿Dónde encuentro la configuración para la ocultación de campos?
- ¿Puedo personalizar la visibilidad de campos por usuario?
- ¿Este módulo afecta a los informes asociados a los campos ocultos?

# Domain — data model

## Functional

Este módulo no cuenta con una entidad cabecera ni relaciones complejas, ya que su funcionalidad se basa en la personalización de la interfaz sin modificar la estructura de la base de datos. No hay etapas definidas, ya que se centra en la ocultación de campos específicos en diferentes contextos. Dado que no se han definido triggers o funciones PL, el enfoque del módulo está orientado hacia la personalización visual y la mejora de la usabilidad.

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

No se han especificado ventanas en el módulo, lo que sugiere que la configuración se realiza a través de herramientas de personalización del sistema en lugar de mediante una interfaz de usuario dedicada. Los usuarios pueden acceder a la funcionalidad de ocultación de campos a través de las configuraciones generales del sistema y opciones de personalización específicas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.hidefield.assets.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.hidefield.assets.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo 'Hide Fields Asset' no incluye botones o procesos típicos como completar, retornar o rechazar debido a su naturaleza de personalización de interfaz. Sin embargo, se esperan validaciones relacionadas con los permisos y roles de usuario al ocultar campos. No se proporcionan informes específicos, dado que no se registran procesos asociados a la funcionalidad del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.hidefield.assets.es_ES/referencedata/translation/`.

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

No hay clases Java específicas asociadas al módulo, lo que indica que su funcionalidad se implementa principalmente a través de configuraciones dentro del ERP sin necesidad de lógica adicional en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.hidefield.assets`.

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

No se han implementado triggers ni funciones PL en este módulo, lo que implica que no hay un rol específico de estos elementos en el soporte cotidiano. El mantenimiento y soporte del módulo se basan en configuraciones de personalización a nivel de interfaz sin interacciones directas en la base de datos.

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

Módulo: `ec.com.sidesoft.hidefield.assets`.

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

# Glosario — prefijo `SSHF`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSHF` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.hidefield.assets` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
