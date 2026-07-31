# Openbravo Sidesoft — Producción

> Gestión de producción, lista de materiales (LDM), lotes, información adicional de producción.

**Paquetes incluidos (4):**
- `ec.com.sidesoft.production` — Sidesoft Production Management
- `ec.com.sidesoft.production.additional.information` — Additional Information for Production
- `ec.com.sidesoft.localization.production.lotautogen` — Sidesoft Localization Production Lote
- `ec.com.sidesoft.ldm.report` — Sidesoft Production LDM Reports


---
## Sidesoft Production Management
**Package:** `ec.com.sidesoft.production`

# Module overview — Sidesoft Production Management

## Functional

El módulo Sidesoft Production Management está diseñado para gestionar las actividades relacionadas con la producción en las organizaciones. Permite a los usuarios gestionar planes de producción, órdenes de mantenimiento, costos indirectos y consumo interno, entre otros aspectos. Los actores principales incluyen usuarios de negocio responsables de la planificación y ejecución de la producción, así como desarrolladores y personal de soporte que trabajan en la configuración y adaptación del módulo. El alcance involucra múltiples aspectos del proceso productivo, desde la planificación hasta el mantenimiento de máquinas, y requiere dependencias como '2.50 to 3.00 Compatibility Skin' para su correcto funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/production` |
| Web | `web/ec.com.sidesoft.production/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**0.0.1** (from `AD_MODULE.xml`).

### DB prefix

`SSPROD`

# Guía de chat — Sidesoft Production Management

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.production`).

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
- «¿Qué es la tabla ssprod_prod_att?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo ver el informe de requisitos de trabajo diario?
- ¿Qué pasos debo seguir para crear una nueva orden de mantenimiento?
- ¿Cómo puedo asignar un costo indirecto a un producto?
- ¿Dónde se reportan los consumos internos de materiales?
- ¿Qué debo hacer si quiero cambiar la categoría de una máquina?
- ¿Cómo se generan los informes de costos de producción?
- ¿Qué procesos se realizan antes de finalizar un plan de producción?
- ¿Cómo puedo verificar el estado de una orden de trabajo pendiente?

# Domain — data model

## Functional

La entidad cabecera del módulo está relacionada principalmente con el plan de producción (M_PRODUCTIONPLAN) y comprende varias etapas que abarcan la planificación y ejecución de la producción. Las relaciones entre las tablas como MA_MACHINE, MA_PROCESSPLAN_VERSION y M_PRODUCTION permiten una integración fluida de los datos en estos procesos. Existen triggers clave como SSPROD_COSTCENTERUSE_TRG y SSPROD_DATECONTROL_TRG que aseguran la consistencia de los datos al realizar operaciones críticas en las tablas respectivas, lo cual es esencial para mantener la integridad de la información a lo largo de los distintos procesos del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssprod_prod_att` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssprod_prod_att` | ssprod_prod_att | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssprod_prod_att_key`; Cols: product, attibuteinstance, p_instance |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssprod_prod_att` |
| `ssprod_product_lot_v` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`MA_MACHINE`, `MA_PROCESSPLAN_VERSION`, `M_PRODUCTIONPLAN`

### Views

`SSPROD_PRODUCT_LOT_V`

# Functional — windows and menus

## Functional

Los usuarios pueden navegar por el módulo Sidesoft Production Management a través de diversas ventanas accesibles desde el menú principal. Algunas de las ventanas disponibles incluyen 'Activity', 'Indirect Cost', 'Internal Consumption', 'Machine', y 'Maintenance Order', cada una diseñada para gestionar aspectos específicos de la producción. La interfaz permite a los usuarios realizar actividades de manera intuitiva al seleccionar la ventana correspondiente y acceder a los datos relacionados con cada función.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Activity | Activity |
| Indirect Cost | Indirect Cost |
| Internal Consumption | Internal Consumption |
| Machine | Machine |
| Machine Category | Machine Category |
| Maintenance Order | Maintenance Order |
| Maintenance Plan | Maintenance Plan |
| Maintenance Task | Maintenance Task |
| Manufacturing Cost Center | Manufacturing Cost Center |
| Periodic Quality Control | Periodic Quality Control |
| Periodic Quality Control Data | Periodic Quality Control Data |
| Process Plan | Process Plan |
| Production Run | Production Run |
| Products View for Attributes | Products View for Attributes |
| Quality Control Point | Quality Control Point |
| Quality Control Report | Quality Control Report |
| Section | Section |
| test | test |
| Test | Test |
| Toolset | Toolset |
| Work Center | Work Center |
| Work Effort | Work Effort |
| Work Incidence | Work Incidence |
| Work Requirement | Work Requirement |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Activity | Activity | No |
| Analysis Tools | Analysis Tools | Sí |
| Calculate Standard Costs | Calculate Standard Costs | No |
| Compliance with the Production Projection | Compliance with the Production Projection | No |
| Create Production Costs | Create Production Costs | No |
| Daily Work Requirements Report | Daily Work Requirements Report | No |
| Indirect Cost | Indirect Cost | No |
| Insert Maintenances | Insert Maintenances | No |
| Internal Consumption | Internal Consumption | No |
| Machine | Machine | No |
| Machine Category | Machine Category | No |
| Maintenance Order | Maintenance Order | No |
| Maintenance Plan | Maintenance Plan | No |
| Maintenance Task | Maintenance Task | No |
| Manufacturing Cost Center | Manufacturing Cost Center | No |
| Materials List Valued | Materials List Valued | No |
| Pending Work Requirement | Pending Work Requirement | No |
| Periodic Quality Control | Periodic Quality Control | No |
| Periodic Quality Control Data | Periodic Quality Control Data | No |
| Process Plan | Process Plan | No |
| Production Cost Report | Production Cost Report | No |
| Production Management | Production Management | Sí |
| Production Run | Production Run | No |
| Production Run Status Report | Production Run Status Report | No |
| Products View for Attributes | Products View for Attributes | No |
| Quality Control Point | Quality Control Point | No |
| Quality Control Report | Quality Control Report | No |
| Report Efficiency by standard time | Report Efficiency by standard time | No |
| Report Evolution of costs by product | Report Evolution of costs by product | No |
| Report Manufacturing Order Registration by Areas | Report Manufacturing Order Registration by Areas | No |
| Report Production Incident | Report Production Incident | No |
| Report Productive process losses | Report Productive process losses | No |
| Report Used machine capacity | Report Used machine capacity | No |
| Section | Section | No |
| Setup | Setup | Sí |
| Standard Costs Report | Standard Costs Report | No |
| Toolset | Toolset | No |
| Transactions | Transactions | Sí |
| Work Center | Work Center | No |
| Work Effort | Work Effort | No |
| Work Incidence | Work Incidence | No |
| Work Requirement | Work Requirement | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

<!-- knowledge-extract:window_specs -->
### Ventana: Activity

- **AD_WINDOW_ID:** `82E1016A33314A76A4790DD95D3C49BA`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Activity | `800072` | 0 |
| 20 | Toolset | `800081` | 1 |

### Ventana: Indirect Cost

- **AD_WINDOW_ID:** `387DCD1EB9F54B8491C749CC1EA2A38A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Indirect Cost | `800190` | 0 |
| 20 | Value | `800191` | 1 |

### Ventana: Internal Consumption

- **AD_WINDOW_ID:** `C5FAE6AAFF89405ABAB9AA1478A11634`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Header | `800168` | 0 |
| 10 | Lines | `800169` | 1 |
| 20 | Accounting | `270` | 1 |

### Ventana: Machine

- **AD_WINDOW_ID:** `4B493627A2A0439A8264647810FECABB`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Machine | `800069` | 0 |
| 10 | Maintenance | `800159` | 1 |
| 20 | Periodicity | `800160` | 2 |
| 5 | Cost | `800200` | 1 |

### Ventana: Machine Category

- **AD_WINDOW_ID:** `68F051F966EE46ECBB3AC7406C4B0513`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Machine Category | `800157` | 0 |
| 10 | Maintenance | `800159` | 1 |
| 20 | Periodicity | `800160` | 2 |

### Ventana: Maintenance Order

- **AD_WINDOW_ID:** `E052C86CC62E42C19CE097A03E178558`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Order | `800163` | 0 |
| 10 | Worker | `800164` | 1 |
| 20 | Task | `800161` | 1 |

### Ventana: Maintenance Plan

- **AD_WINDOW_ID:** `D648B7980B5143C59A7FC760D3617615`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Maintenance | `800161` | 0 |

### Ventana: Maintenance Task

- **AD_WINDOW_ID:** `01EB770BAFF84E738D699E836755E94B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Maintenance Task | `800158` | 0 |

### Ventana: Manufacturing Cost Center

- **AD_WINDOW_ID:** `6EDC152D663141FBA7A013A38742CD28`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Cost Center | `800123` | 0 |
| 10 | Version | `800197` | 1 |
| 20 | Employee | `800189` | 2 |
| 25 | Machine | `800199` | 2 |
| 30 | Indirect Cost | `800192` | 2 |

### Ventana: Periodic Quality Control

- **AD_WINDOW_ID:** `DBF297CD33F248F288358AE71B6E8AD1`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Test | `800139` | 0 |
| 10 | Check Point | `800140` | 1 |

### Ventana: Periodic Quality Control Data

- **AD_WINDOW_ID:** `426444AF6E7940938A27FE7E36CA84A9`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Test | `800141` | 0 |
| 10 | Result | `800142` | 1 |

### Ventana: Process Plan

- **AD_WINDOW_ID:** `21976EDEA3934A61884D0B1B681A3776`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Process Plan | `800095` | 0 |
| 20 | Version | `800125` | 1 |
| 40 | Operation | `800096` | 2 |
| 50 | I/O Products | `800097` | 3 |
| 55 | Copy From Attribute | `FF80818132144FDB01321456E8AC000E` | 4 |
| 70 | Employee | `800206` | 3 |
| 80 | Machine | `800207` | 3 |
| 90 | Indirect Cost | `800208` | 3 |

### Ventana: Production Run

- **AD_WINDOW_ID:** `359556B79F7A41069A987D4DDD00EB33`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Production Run | `385` | 0 |
| 20 | Incidence | `800103` | 1 |
| 30 | Toolset | `800105` | 1 |
| 40 | Product | `326` | 1 |
| 50 | Salary Category / Employee | `800201` | 1 |
| 60 | Indirect Cost | `800202` | 1 |
| 70 | Machine | `800203` | 1 |
| 80 | Outsourced | `800195` | 1 |

### Ventana: Products View for Attributes

- **AD_WINDOW_ID:** `E2830096CA7E42C79DEBCC2B0C7ED4E4`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Products View for Attributes | `5AB447857C184DF4845F84413138853C` | 0 |

### Ventana: Quality Control Point

- **AD_WINDOW_ID:** `6C0AF024993F4DFC9D997CA39F58BB52`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Check Point Set | `800131` | 0 |
| 10 | Check Point | `800132` | 1 |
| 20 | Shift | `800152` | 1 |

### Ventana: Quality Control Report

- **AD_WINDOW_ID:** `B997A55D42144D0495AE707E49A593A4`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Date and Shift | `800138` | 0 |
| 20 | Check Point Set | `800133` | 1 |
| 30 | Time | `800134` | 2 |
| 40 | Values | `800135` | 3 |

### Ventana: Section

- **AD_WINDOW_ID:** `31FF1D1C24F149399F685CD11F4EE653`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Section | `800067` | 0 |

### Ventana: test

- **AD_WINDOW_ID:** `2F1F33922CBF413D978C83F11A66F906`

### Ventana: Test

- **AD_WINDOW_ID:** `D0338D07018640069425663FDF174488`

### Ventana: Toolset

- **AD_WINDOW_ID:** `D41ACC4A805B4445BFBCDAA4974E3666`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Toolset Type | `800079` | 0 |
| 20 | Toolset | `800080` | 1 |

### Ventana: Work Center

- **AD_WINDOW_ID:** `0108727346834FFF80BBE96B1C1D1D35`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Work Center | `800070` | 0 |
| 20 | Machine Station | `800071` | 1 |
| 30 | Activity | `800072` | 1 |
| 40 | Toolset | `800081` | 2 |

### Ventana: Work Effort

- **AD_WINDOW_ID:** `0D49D788605449178F19CBB42B5335EA`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Work Effort | `325` | 0 |
| 20 | Employee | `800102` | 1 |
| 30 | Incidence | `800103` | 1 |
| 40 | Global Use | `800143` | 1 |
| 50 | Production Run | `385` | 1 |
| 60 | Toolset | `800105` | 2 |
| 70 | Product | `326` | 2 |
| 72 | Salary Category / Employee | `800201` | 2 |
| 74 | Indirect Cost | `800202` | 2 |
| 78 | Machine | `800203` | 2 |
| 80 | Outsourced | `800195` | 2 |

### Ventana: Work Incidence

- **AD_WINDOW_ID:** `FA5A5BC0F50246569B9CED7256356B25`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 0 | Work Incidence | `800092` | 0 |

### Ventana: Work Requirement

- **AD_WINDOW_ID:** `C6FF17AB1F6E41499D21CD2F37389F48`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `800098` | 0 |
| 20 | Operation | `800099` | 1 |
| 30 | Product | `800100` | 2 |

## Campos añadidos por el módulo (AD_FIELD)

### Cost Center (ventana: Manufacturing Cost Center)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Search Key | `—` | No | No | — |
| 30 | Name | `—` | No | No | — |
| 40 | Active | `—` | No | No | — |
| 50 | Calculated | `—` | No | No | — |
| 60 | By Default | `—` | No | No | — |
| 70 | Cost | `—` | No | No | — |

### Machine (ventana: Production Run)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Machine | `—` | No | No | — |
| 20 | Usage Coefficient | `—` | No | No | — |

### Accounting (ventana: Internal Consumption)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `—` | No | Sí | — |
| 60 | General Ledger | `—` | No | Sí | — |
| 70 | Currency | `—` | No | Sí | — |
| 80 | Period | `—` | No | Sí | — |
| 90 | Accounting Date | `—` | No | Sí | — |
| 100 | Account | `—` | No | Sí | — |
| 130 | Debit | `—` | No | Sí | — |
| 140 | Credit | `—` | No | Sí | — |
| 150 | Description | `—` | No | No | — |
| 160 | Business Partner | `—` | No | Sí | 800000 |
| 170 | Product | `—` | No | Sí | 800000 |
| 180 | Project | `—` | No | Sí | 800000 |
| 190 | Cost Center | `—` | No | Sí | 800000 |
| 200 | Asset | `—` | No | Sí | 800000 |
| 210 | 1st Dimension | `—` | No | Sí | 800000 |
| 220 | 2nd Dimension | `—` | No | Sí | 800000 |

### Outsourced (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Invoice Line | `—` | No | No | — |
| 20 | Cost | `—` | No | No | — |

### Date and Shift (ventana: Quality Control Report)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Measurement Date | `—` | No | No | — |
| 30 | Shift | `—` | No | No | — |
| 40 | User/Contact | `—` | No | No | — |
| 50 | Comments | `—` | No | No | — |
| 60 | Explode Measure Shift | `—` | No | No | — |
| 70 | Edit CCP Measured Values | `—` | No | No | — |

### Maintenance (ventana: Maintenance Plan)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Maintenance Type | `—` | No | No | — |
| 30 | Maintenance | `—` | No | No | — |
| 40 | Maintenance Task | `—` | No | No | — |
| 50 | Planned Date | `—` | No | No | — |
| 60 | Shift | `—` | No | No | — |
| 70 | Machine Category | `—` | No | No | — |
| 80 | Machine | `—` | No | No | — |
| 90 | Description | `—` | No | No | — |
| 100 | Confirmation | `—` | No | No | — |
| 110 | Maintenance Order | `—` | No | No | — |
| 120 | Result | `—` | No | No | — |
| 130 | Time Used | `—` | No | No | — |
| 140 | Comments | `—` | No | No | — |
| 150 | Internal Consumption | `—` | No | No | — |
| 160 | Active | `—` | No | No | — |

### Indirect Cost (ventana: Indirect Cost)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Name | `—` | No | No | — |
| 30 | Description | `—` | No | No | — |
| 40 | Cost Type | `—` | No | No | — |
| 50 | Active | `—` | No | No | — |

### Section (ventana: Section)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Name | `—` | No | No | — |
| 30 | Description | `—` | No | No | — |
| 40 | Active | `—` | No | No | — |

### Incidence (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Incidence | `—` | No | No | — |
| 20 | Starting Time | `—` | No | No | — |
| 30 | Ending Time | `—` | No | No | — |
| 40 | Description | `—` | No | No | — |
| 50 | Production Plan | `—` | No | Sí | — |

### Product (ventana: Production Run)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `—` | No | No | — |
| 20 | Product | `—` | No | No | — |
| 30 | Attribute Set Value | `—` | No | No | — |
| 40 | Production Type | `—` | No | No | — |
| 50 | Quantity | `—` | No | No | — |
| 60 | UOM | `—` | No | No | — |
| 70 | Rejected Quantity | `—` | No | No | — |
| 80 | Storage Bin | `—` | No | No | — |
| 90 | Order Quantity | `—` | No | No | — |
| 100 | Order UOM | `—` | No | No | — |
| 110 | Division Group Quantity | `—` | No | Sí | — |

### Result (ventana: Periodic Quality Control Data)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `—` | No | No | — |
| 30 | Periodic Quality Control Case | `—` | No | Sí | — |
| 40 | Active | `—` | No | No | — |
| 50 | Periodic Quality Control Test | `—` | No | No | — |
| 60 | Test Date | `—` | No | No | — |
| 70 | Test Result | `—` | No | No | — |

### Machine (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Machine | `—` | No | No | — |
| 20 | Usage Coefficient | `—` | No | No | — |

### Check Point (ventana: Quality Control Point)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Sequence Number | `—` | No | No | — |
| 20 | Name | `—` | No | No | — |
| 30 | Number of Measurements | `—` | No | No | — |
| 40 | Value Type | `—` | No | No | — |
| 50 | Critical | `—` | No | No | — |
| 60 | Active | `—` | No | No | — |
| 70 | Description | `—` | No | No | — |

### Value (ventana: Indirect Cost)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Starting Date | `—` | No | No | — |
| 20 | Ending Date | `—` | No | No | — |
| 30 | Cost UOM | `—` | No | No | — |
| 40 | Cost | `—` | No | No | — |
| 50 | Total | `—` | No | No | — |
| 60 | Calculate Indirect Cost | `—` | No | No | — |
| 70 | Calculated | `—` | No | No | — |

### Lines (ventana: Internal Consumption)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `—` | No | No | — |
| 20 | Product | `—` | No | No | — |
| 30 | Attribute Set Value | `—` | No | No | — |
| 40 | Movement Quantity | `—` | No | No | — |
| 50 | UOM | `—` | No | Sí | — |
| 60 | Storage Bin | `—` | No | No | — |
| 70 | Order Quantity | `—` | No | No | — |
| 80 | Order UOM | `—` | No | No | — |
| 90 | Voided Internal Consumption Line | `—` | No | Sí | — |

### Machine (ventana: Manufacturing Cost Center)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Machine | `—` | No | No | — |
| 20 | Usage Coefficient | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |

### Production Run (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `—` | No | No | — |
| 20 | WR Phase | `—` | No | No | — |
| 22 | Starting Time | `—` | No | No | — |
| 24 | Ending Time | `—` | No | No | — |
| 30 | Cost Center Version | `—` | No | No | — |
| 40 | Required Quantity | `—` | No | Sí | — |
| 50 | Completed Quantity | `—` | No | No | — |
| 54 | Process Unit | `—` | No | No | — |
| 58 | Conversion Rate | `—` | No | Sí | — |
| 80 | Rejected Quantity | `—` | No | No | — |
| 100 | Cost Center Use | `—` | No | No | — |
| 110 | Create Standards New | `—` | No | No | — |
| 120 | Outsourced | `—` | No | No | — |
| 160 | Close Phase | `—` | No | No | — |
| 270 | Movement Date | `—` | No | No | — |
| 280 | Environmental conditions | `EM_Ssprod_Env_Conditions` | No | No | — |

### Salary Category / Employee (ventana: Production Run)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Salary Category | `—` | No | No | — |
| 20 | Business Partner | `—` | No | No | — |
| 30 | Quantity | `—` | No | No | — |
| 40 | Estimated Cost | `—` | No | No | — |
| 50 | Run Time | `—` | No | No | — |

### Maintenance Task (ventana: Maintenance Task)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Name | `—` | No | No | — |
| 30 | Description | `—` | No | No | — |
| 40 | Active | `—` | No | No | — |

### Maintenance (ventana: Machine Category)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Name | `—` | No | No | — |
| 20 | Maintenance Type | `—` | No | No | — |
| 30 | Description | `—` | No | No | — |
| 40 | Maintenance Task | `—` | No | No | — |
| 50 | Planned Time (Hours) | `—` | No | No | — |
| 60 | Insert in Machines | `—` | No | No | — |

### Indirect Cost (ventana: Manufacturing Cost Center)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Indirect Cost | `—` | No | No | — |
| 20 | Active | `—` | No | No | — |

### Global Use (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Product | `—` | No | No | — |
| 20 | Attribute Set Value | `—` | No | No | — |
| 30 | Movement Quantity | `—` | No | No | — |
| 40 | UOM | `—` | No | No | — |
| 50 | Storage Bin | `—` | No | No | — |
| 60 | Order Quantity | `—` | No | No | — |
| 70 | Order UOM | `—` | No | No | — |

### Machine (ventana: Process Plan)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Machine | `—` | No | No | — |
| 20 | Estimated Cost | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |

### Maintenance (ventana: Machine)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Name | `—` | No | No | — |
| 20 | Maintenance Type | `—` | No | No | — |
| 30 | Description | `—` | No | No | — |
| 40 | Maintenance Task | `—` | No | No | — |
| 50 | Planned Time (Hours) | `—` | No | No | — |
| 60 | Active | `—` | No | No | — |

### Version (ventana: Manufacturing Cost Center)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Document No. | `—` | No | No | — |
| 20 | Valid From Date | `—` | No | No | — |
| 30 | Cost | `—` | No | No | — |
| 40 | Cost UOM | `—` | No | No | — |
| 50 | Active | `—` | No | No | — |

### Toolset (ventana: Toolset)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Active | `—` | No | No | — |
| 20 | Search Key | `—` | No | No | — |
| 30 | Storage Bin | `—` | No | No | — |
| 40 | Discarded | `—` | No | No | — |
| 50 | Utilization | `—` | No | Sí | — |

### Toolset (ventana: Work Center)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Toolset Type | `—` | No | No | — |
| 20 | Utilization Coefficient | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |

### Shift (ventana: Quality Control Point)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Shift | `—` | No | No | — |
| 20 | Starting Time | `—` | No | No | — |
| 30 | Ending Time | `—` | No | No | — |
| 40 | Active | `—` | No | No | — |

### Values (ventana: Quality Control Report)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Sequence Number | `—` | No | No | — |
| 20 | Measurement Time | `—` | No | Sí | — |
| 30 | Critical Control Point | `—` | No | No | — |
| 40 | Value Type | `—` | No | No | — |
| 50 | Text | `—` | No | No | — |
| 60 | Value | `—` | No | No | — |
| 70 | Check | `—` | No | No | — |

### Activity (ventana: Activity)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Search Key | `—` | No | No | — |
| 30 | Name | `—` | No | No | — |
| 40 | Cost Center | `—` | No | No | — |
| 50 | Work Center | `—` | No | No | — |
| 60 | Description | `—` | No | No | — |
| 70 | Active | `—` | No | No | — |

### Test (ventana: Periodic Quality Control Data)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Name | `—` | No | No | — |
| 50 | Periodic Quality Control | `—` | No | No | — |
| 60 | Starting Date | `—` | No | No | — |
| 70 | Ending Date | `—` | No | No | — |
| 80 | Product | `—` | No | No | — |
| 90 | Attribute Set Value | `—` | No | No | — |
| 100 | Run Periodic Control | `—` | No | No | — |
| — | Client | `—` | No | No | — |

### Work Incidence (ventana: Work Incidence)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Name | `—` | No | No | — |
| 30 | Work Incidence Downtime | `—` | No | No | — |
| 40 | Description | `—` | No | No | — |

### Incidence (ventana: Production Run)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Incidence | `—` | No | No | — |
| 20 | Starting Time | `—` | No | No | — |
| 30 | Ending Time | `—` | No | No | — |
| 40 | Description | `—` | No | No | — |

### Check Point Set (ventana: Quality Control Point)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Sequence Number | `—` | No | No | — |
| 30 | Name | `—` | No | No | — |
| 40 | Frequency | `—` | No | No | — |
| 50 | Active | `—` | No | No | — |
| 50 | Description | `—` | No | No | — |

### Salary Category / Employee (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Salary Category | `—` | No | No | — |
| 20 | Business Partner | `—` | No | No | — |
| 30 | Quantity | `—` | No | No | — |
| 40 | Estimated Cost | `—` | No | No | — |
| 50 | Run Time | `—` | No | No | — |

### Operation (ventana: Process Plan)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Sequence Number | `—` | No | No | — |
| 20 | Search Key | `—` | No | No | — |
| 30 | Name | `—` | No | No | — |
| 40 | Activity | `—` | No | No | — |
| 45 | Estimated Time | `—` | No | No | — |
| 50 | Cost Center Use Time | `—` | No | No | — |
| 60 | Preparation Time | `—` | No | No | — |
| 70 | Description | `—` | No | No | — |
| 80 | Multiplier | `—` | No | No | — |
| 90 | Empty Cells are Zero | `—` | No | No | — |
| 100 | Global Use | `—` | No | No | — |
| 110 | Outsourced | `—` | No | No | — |
| 120 | Outsourcing Cost | `—` | No | No | — |
| 130 | Default | `—` | No | No | — |
| 140 | Active | `—` | No | No | — |
| 160 | Create Standards | `—` | No | No | — |

### Toolset (ventana: Production Run)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Toolset | `—` | No | No | — |
| 20 | Toolset Uses | `—` | No | No | — |

### Periodicity (ventana: Machine Category)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Active | `—` | No | No | — |
| 20 | Periodicity Type | `—` | No | No | — |
| 30 | Shift | `—` | No | No | — |
| 40 | Day of the Month | `—` | No | No | — |
| 50 | Weekday | `—` | No | No | — |
| 50 | Starting Day | `—` | No | No | — |
| 70 | Exclude Weekends | `—` | No | No | — |

### Order (ventana: Maintenance Order)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Document No. | `—` | No | No | — |
| 30 | Maintenance Order Date | `—` | No | No | — |
| 40 | Shift | `—` | No | No | — |
| 50 | Create from Maintenance Part | `—` | No | No | — |
| 60 | Active | `—` | No | No | — |

### Indirect Cost (ventana: Process Plan)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Indirect Cost | `—` | No | No | — |
| 20 | Estimated Cost | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |

### Machine Category (ventana: Machine Category)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Name | `—` | No | No | — |
| 30 | Description | `—` | No | No | — |
| 40 | Active | `—` | No | No | — |

### Header (ventana: Internal Consumption)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Movement Date | `—` | No | No | — |
| 30 | Name | `—` | No | No | — |
| 40 | Process Internal Consumption | `—` | No | No | — |
| 60 | Project | `—` | No | No | 800000 |
| 110 | Cost Center | `—` | No | No | 800000 |
| — | Posted | `—` | No | No | — |

### Test (ventana: Periodic Quality Control)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Name | `—` | No | No | — |
| 30 | Description | `—` | No | No | — |
| 40 | Active | `—` | No | No | — |

### Time (ventana: Quality Control Report)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Measurement Hour | `—` | No | No | — |
| 20 | Measurement Set | `—` | No | Sí | — |
| 30 | Input Time Measurement | `—` | No | No | — |

### Machine (ventana: Machine)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Search Key | `—` | No | No | — |
| 30 | Name | `—` | No | No | — |
| 40 | Machine Category | `—` | No | No | — |
| 50 | Purchase Year | `—` | No | No | — |
| 60 | Lifespan (years) | `—` | No | No | — |
| 70 | Active | `—` | No | No | — |
| 80 | Machine Capacity | `EM_Ssprod_Machine_Capacity` | No | No | — |

### Cost (ventana: Machine)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Valid From Date | `—` | No | No | — |
| 20 | Purchase Amount | `—` | No | No | — |
| 30 | Cost | `—` | No | No | — |
| 40 | Cost UOM | `—` | No | No | — |
| 50 | Toolset Amount | `—` | No | No | — |
| 60 | Amortization (years) | `—` | No | No | — |
| 70 | Value/Year | `—` | No | No | — |
| 80 | Work Days/Year | `—` | No | No | — |
| 90 | Work Hours/Day | `—` | No | No | — |
| 100 | Days/Year | `—` | No | No | — |
| 110 | UOM Annual Cost | `—` | No | No | — |

### Work Center (ventana: Work Center)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Search Key | `—` | No | No | — |
| 30 | Name | `—` | No | No | — |
| 40 | Section | `—` | No | No | — |
| 50 | Active | `—` | No | No | — |

### Employee (ventana: Manufacturing Cost Center)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Salary Category | `—` | No | No | — |
| 20 | Quantity | `—` | No | No | — |
| 30 | Cost UOM | `—` | No | Sí | — |
| 40 | Active | `—` | No | No | — |
| 50 | Split | `—` | No | No | — |

### Process Plan (ventana: Process Plan)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Search Key | `—` | No | No | — |
| 30 | Name | `—` | No | No | — |
| 40 | Description | `—` | No | No | — |
| 50 | Process Unit | `—` | No | No | — |
| 60 | Conversion Rate | `—` | No | No | — |
| 70 | Include Operations when inserting | `—` | No | No | — |
| 80 | Active | `—` | No | No | — |
| 90 | Copy Version | `—` | No | No | — |

### Periodicity (ventana: Machine)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Periodicity Type | `—` | No | No | — |
| 20 | Shift | `—` | No | No | — |
| 30 | Day of the Month | `—` | No | No | — |
| 40 | Starting Day | `—` | No | No | — |
| 50 | Weekday | `—` | No | No | — |
| 60 | Exclude Weekends | `—` | No | No | — |

### Toolset (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Toolset | `—` | No | No | — |
| 20 | Toolset Uses | `—` | No | No | — |

### Products View for Attributes (ventana: Products View for Attributes)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Product | `M_Product_ID` | No | No | — |
| 40 | Storage Bin | `M_Locator_ID` | No | No | — |
| 50 | Attribute Set Value | `M_Attributesetinstance_ID` | No | No | — |
| 70 | Expiration Date | `Guaranteedate` | No | No | — |
| 90 | Stock | `Stock` | No | No | — |
| 130 | UOM | `C_Uom_ID` | No | No | — |

### Outsourced (ventana: Production Run)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Invoice Line | `—` | No | No | — |
| 20 | Cost | `—` | No | No | — |

### Product (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `—` | No | No | — |
| 20 | Product | `—` | No | No | — |
| 30 | Attribute Set Value | `—` | No | No | — |
| 40 | Production Type | `—` | No | No | — |
| 50 | Movement Quantity | `—` | No | No | — |
| 60 | UOM | `—` | No | No | — |
| 70 | Rejected Quantity | `—` | No | No | — |
| 80 | Storage Bin | `—` | No | No | — |
| 90 | Order Quantity | `—` | No | No | — |
| 100 | Order UOM | `—` | No | No | — |
| 110 | Division Group Quantity | `—` | No | No | — |

### Copy From Attribute (ventana: Process Plan)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 40 | Sequence Product | `—` | No | Sí | — |
| 50 | Product Attribute | `—` | No | No | — |
| 60 | Is special attribute | `—` | No | No | — |
| 70 | Special Attribute | `—` | No | No | — |
| 80 | Product From | `—` | No | No | — |
| 90 | Attribute use | `—` | No | No | — |
| 100 | Copy special into normal attribute | `—` | No | No | — |

### Task (ventana: Maintenance Order)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Time Used | `—` | No | No | — |
| 20 | Internal Consumption | `—` | No | No | — |
| 30 | Result | `—` | No | No | — |
| 40 | Maintenance | `—` | No | Sí | — |
| 50 | Planned Date | `—` | No | Sí | — |
| 60 | Shift | `—` | No | Sí | — |
| 70 | Maintenance Type | `—` | No | Sí | — |
| 80 | Machine | `—` | No | Sí | — |
| 90 | Machine Category | `—` | No | Sí | — |
| 100 | Maintenance Task | `—` | No | Sí | — |
| 110 | Confirmation | `—` | No | Sí | — |
| 120 | Description | `—` | No | Sí | — |
| 130 | Comments | `—` | No | No | — |
| 140 | Active | `—` | No | No | — |

### Employee (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Business Partner | `—` | No | No | — |

### Operation (ventana: Work Requirement)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Sequence Number | `—` | No | No | — |
| 20 | MA Sequence | `—` | No | No | — |
| 30 | Activity | `—` | No | No | — |
| 32 | Starting Date | `—` | No | No | — |
| 34 | Ending Date | `—` | No | No | — |
| 36 | Estimated Time | `—` | No | No | — |
| 38 | Run Time | `—` | No | Sí | — |
| 40 | Quantity | `—` | No | No | — |
| 50 | Completed Quantity | `—` | No | Sí | — |
| 60 | Cost Center Use Time | `—` | No | No | — |
| 70 | Description | `—` | No | No | — |
| 80 | Empty Cells are Zero | `—` | No | No | — |
| 90 | Global Use | `—` | No | No | — |
| 100 | Close Phase | `—` | No | No | — |
| 110 | Outsourced | `—` | No | No | — |
| 120 | Preparation Time | `—` | No | No | — |
| 130 | Create Standards | `—` | No | No | — |

### Version (ventana: Process Plan)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Document No. | `—` | No | No | — |
| 20 | Starting Date | `—` | No | No | — |
| 30 | Ending Date | `—` | No | No | — |
| 40 | Active | `—` | No | No | — |
| 50 | Estimated Time | `—` | No | Sí | — |
| 60 | Print Cost | `EM_Ssprod_Printcost` | No | No | — |

### Product (ventana: Work Requirement)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Product | `—` | No | No | — |
| 20 | Production Type | `—` | No | No | — |
| 30 | Movement Quantity | `—` | No | No | — |
| 40 | UOM | `—` | No | Sí | — |
| 50 | Component Cost | `—` | No | No | — |
| 60 | Order Quantity | `—` | No | No | — |
| 70 | Order UOM | `—` | No | No | — |
| 90 | Warehouse Rule | `—` | No | No | — |

### Toolset (ventana: Activity)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Toolset Type | `—` | No | No | — |
| 20 | Utilization Coefficient | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |

### Indirect Cost (ventana: Production Run)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Indirect Cost | `—` | No | No | — |

### Production Run (ventana: Production Run)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 7 | Movement Date | `—` | No | No | — |
| 10 | Line No. | `—` | No | No | — |
| 20 | WR Phase | `—` | No | No | — |
| 22 | Starting Time | `—` | No | No | — |
| 24 | Ending Time | `—` | No | No | — |
| 30 | Cost Center Version | `—` | No | No | — |
| 40 | Required Quantity | `—` | No | Sí | — |
| 50 | Production Quantity | `—` | No | No | — |
| 54 | Process Unit | `—` | No | Sí | — |
| 58 | Conversion Rate | `—` | No | Sí | — |
| 60 | Process Quantity | `—` | No | No | — |
| 80 | Rejected Quantity | `—` | No | No | — |
| 100 | Cost Center Use | `—` | No | No | — |
| 110 | Create Standards New | `—` | No | No | — |
| 120 | Outsourced | `—` | No | No | — |
| 160 | Close Phase | `—` | No | No | — |
| 170 | Validate Work Effort | `—` | No | No | — |

### Toolset Type (ventana: Toolset)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Name | `—` | No | No | — |
| 30 | Lifespan (years) | `—` | No | No | — |
| 40 | Description | `—` | No | No | — |
| 50 | Active | `—` | No | No | — |

### Work Effort (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Movement Date | `—` | No | No | — |
| 30 | Starting Time | `—` | No | No | — |
| 40 | Ending Time | `—` | No | No | — |
| 50 | Document No. | `—` | No | No | — |
| 60 | Validate Work Effort | `—` | No | No | — |
| 80 | Posted | `—` | No | No | — |

### Worker (ventana: Maintenance Order)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Business Partner | `—` | No | No | — |
| 20 | Active | `—` | No | No | — |

### Header (ventana: Work Requirement)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 15 | Document Type | `—` | No | No | — |
| 20 | Document No. | `—` | No | No | — |
| 30 | Process Plan | `—` | No | No | — |
| 40 | Quantity | `—` | No | Sí | — |
| 50 | WR Creation Date | `—` | No | No | — |
| 60 | Starting Date | `—` | No | No | — |
| 70 | Ending Date | `—` | No | No | — |
| 80 | Conversion Rate | `—` | No | Sí | — |
| 90 | Process Quantity | `—` | No | No | — |
| 100 | Include Operations when inserting | `—` | No | No | — |
| 110 | Process Unit | `—` | No | Sí | — |
| 115 | Estimated Time | `—` | No | Sí | — |
| 116 | Run Time | `—` | No | Sí | — |
| 130 | Process Work Requirement | `—` | No | No | — |
| 140 | Close Work Requirement | `—` | No | No | — |
| 150 | Create Work Effort | `—` | No | No | — |
| 160 | Closed | `—` | No | No | — |

### Check Point Set (ventana: Quality Control Report)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Sequence Number | `—` | No | No | — |
| 20 | Measurement Shift | `—` | No | Sí | — |
| 30 | Quality Control Point Set | `—` | No | No | — |

### Employee (ventana: Process Plan)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Salary Category | `—` | No | No | — |
| 20 | Estimated Cost | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |

### Activity (ventana: Work Center)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Search Key | `—` | No | No | — |
| 20 | Name | `—` | No | No | — |
| 30 | Description | `—` | No | No | — |

### Indirect Cost (ventana: Work Effort)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Indirect Cost | `—` | No | No | — |

### Machine Station (ventana: Work Center)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Machine | `—` | No | No | — |
| 20 | Active | `—` | No | No | — |

### Check Point (ventana: Periodic Quality Control)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Name | `—` | No | No | — |
| 20 | Waiting Period (Days) | `—` | No | No | — |
| 30 | Description | `—` | No | No | — |
| 40 | Active | `—` | No | No | — |

### I/O Products (ventana: Process Plan)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 5 | Line No. | `—` | No | No | — |
| 10 | Product | `—` | No | No | — |
| 20 | Production Type | `—` | No | No | — |
| 30 | Quantity | `—` | No | No | — |
| 40 | UOM | `—` | No | Sí | — |
| 50 | Component Cost | `—` | No | No | — |
| 60 | Decrease | `—` | No | No | — |
| 70 | Rejected | `—` | No | No | — |
| 80 | Order Quantity | `—` | No | No | — |
| 90 | Order UOM | `—` | No | No | — |
| 110 | Active | `—` | No | No | — |
| 120 | Division Group Quantity | `—` | No | No | — |
| 130 | Create Product Copy | `—` | No | No | — |
| 140 | Warehouse Rule | `—` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo cuenta con varios botones de proceso que incluyen acciones típicas como completar, retornar o rechazar actividades en el flujo de trabajo. Se generan informes relevantes que apoyan la toma de decisiones, entre ellos el 'Daily Work Requirements Report' y el 'Production Cost Report', que ofrecen visibilidad sobre las necesidades de trabajo y los costos de producción. Además, se implementan validaciones frecuentes como la correcta asignación de costes y fechas para asegurar que los datos ingresados cumplen con los requisitos del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Create Standards New | Create Standards New | CreateStandardsProcessNEW | Java `CreateStandards` (AD_MODEL_OBJECT `P`) | Clase `CreateStandards` extiende `—`. | `src/ec/com/sidesoft/production/ad_actionButton/CreateStandards.java` |
| Botón (PL/pgSQL) | Calculate Standard Costs | Calculate Standard Costs | MA_StandardCost | `Ma_Standard_Cost` | Calculates the standard cost of manufactured products. | — |
| Botón (PL/pgSQL) | Create Production Costs | Create Production Costs | MA_Production_Cost_Generate | `MA_Production_Cost_Generate` | Create Production Costs | — |
| Botón (PL/pgSQL) | Create Standards NewSql | Create Standards NewSql | Ssprod_ProductionRun_Standard | `ssprod_productionrun_standard` | ORDER BY MS.PRIORITY, t.m_product_id asc, mattsi.guaranteedate asc ;; It's taken the toolset with higher number of uses; Get StdPrecision of Uom of Product to be used in Production Line.; Insert production plan for used… | — |
| Botón (PL/pgSQL) | Generate Work_Requirement Prod | Generate Work_Requirement Prod | ssprod_workrequirement | `ssprod_workrequirement` | Validar que el tipo de documento tenga secuencia asignada | — |
| Botón (PL/pgSQL) | Insert Maintenances | Insert Maintenances | MA_Maint_All | `MA_Maint_All` | Insert Maintenances | — |
| Proceso / otro | Compliance with the Production Projection | Compliance with the Production Projection | Ssprod_CompliancewithProduction | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Materials List Valued | Materials List Valued | Ssprod_Materials_List_Valued | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Efficiency by standard time | Report Efficiency by standard time | Report Efficiency by standard time | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Evolution of costs by product | Report Evolution of costs by product | Report Evolution of costs by product | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Manufacturing Order Registration by Areas | Report Manufacturing Order Registration by Areas | Report Manufacturing Order Registration | *(OBUIAPP / manual)* | Report Manufacturing Order Registration by Areas | — |
| Proceso / otro | Report Production Incident | Report Production Incident | Report Production Incident | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Productive process losses | Report Productive process losses | Report Productive process losses | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Used machine capacity | Report Used machine capacity | Report Used machine capacity | *(OBUIAPP / manual)* | Report Used machine capacity | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Daily Work Requirements Report | Daily Work Requirements Report | RV_ReportWorkRequirementDaily | Java `ReportWorkRequirementDaily` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `org/openbravo/erpCommon/ad_reports/ReportWorkRequirementDailyEdit.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementDaily.java` |
| Reporte | Generic Print Part Of Work | Generic Print Part Of Work | Generic Print Part Of Work | Java `Ssprod_GenericPrintPartOfWork` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `0D49D788605449178F19CBB42B5335EA|M_PRODUCTION_ID`. | `src/ec/com/sidesoft/production/ad_process/Ssprod_GenericPrintPartOfWork.java` |
| Reporte | Pending Work Requirement | Pending Work Requirement | ReportWorkRequirementJR | Java `ReportWorkRequirementJR` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementJR.java` |
| Reporte | Production Cost Report | Production Cost Report | RV_ReportProductionCost | Java `ReportProductionCost` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionCost.java` |
| Reporte | Production Run Status Report | Production Run Status Report | ReportProductionRunJR | Java `ReportProductionRunJR` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `org/openbravo/erpCommon/ad_reports/ReportProductionRun.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionRunJR.java` |
| Reporte | Standard Costs Report | Standard Costs Report | ReportStandardCostJR | Java `ReportStandardCostJR` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportStandardCostJR.java` |
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
| Botón (Java) | Create Standards New | `CreateStandards` | Java (otro) | `—` | — | `src/ec/com/sidesoft/production/ad_actionButton/CreateStandards.java` |
| Reporte | Daily Work Requirements Report | `ReportWorkRequirementDaily` | Informe (servlet PDF) | `—` | org/openbravo/erpCommon/ad_reports/ReportWorkRequirementDailyEdit.jrxml | `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementDaily.java` |
| Reporte | Generic Print Part Of Work | `Ssprod_GenericPrintPartOfWork` | Informe (servlet PDF) | `0D49D788605449178F19CBB42B5335EA|M_PRODUCTION_ID` | — | `src/ec/com/sidesoft/production/ad_process/Ssprod_GenericPrintPartOfWork.java` |
| Reporte | Pending Work Requirement | `ReportWorkRequirementJR` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementJR.java` |
| Reporte | Production Cost Report | `ReportProductionCost` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionCost.java` |
| Reporte | Production Run Status Report | `ReportProductionRunJR` | Informe (servlet PDF) | `—` | org/openbravo/erpCommon/ad_reports/ReportProductionRun.jrxml | `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionRunJR.java` |
| Reporte | Standard Costs Report | `ReportStandardCostJR` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/production/ad_reports/reports/ReportStandardCostJR.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Create Standards New | Create Standards New | CreateStandardsProcessNEW | Java `CreateStandards` (AD_MODEL_OBJECT `P`) | Clase `CreateStandards` extiende `—`. | `src/ec/com/sidesoft/production/ad_actionButton/CreateStandards.java` |
| Botón (PL/pgSQL) | Calculate Standard Costs | Calculate Standard Costs | MA_StandardCost | `Ma_Standard_Cost` | Calculates the standard cost of manufactured products. | — |
| Botón (PL/pgSQL) | Create Production Costs | Create Production Costs | MA_Production_Cost_Generate | `MA_Production_Cost_Generate` | Create Production Costs | — |
| Botón (PL/pgSQL) | Create Standards NewSql | Create Standards NewSql | Ssprod_ProductionRun_Standard | `ssprod_productionrun_standard` | ORDER BY MS.PRIORITY, t.m_product_id asc, mattsi.guaranteedate asc ;; It's taken the toolset with higher number of uses; Get StdPrecision of Uom of Product to be used in Production Line.; Insert production plan for used… | — |
| Botón (PL/pgSQL) | Generate Work_Requirement Prod | Generate Work_Requirement Prod | ssprod_workrequirement | `ssprod_workrequirement` | Validar que el tipo de documento tenga secuencia asignada | — |
| Botón (PL/pgSQL) | Insert Maintenances | Insert Maintenances | MA_Maint_All | `MA_Maint_All` | Insert Maintenances | — |
| Proceso / otro | Compliance with the Production Projection | Compliance with the Production Projection | Ssprod_CompliancewithProduction | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Materials List Valued | Materials List Valued | Ssprod_Materials_List_Valued | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Efficiency by standard time | Report Efficiency by standard time | Report Efficiency by standard time | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Evolution of costs by product | Report Evolution of costs by product | Report Evolution of costs by product | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Manufacturing Order Registration by Areas | Report Manufacturing Order Registration by Areas | Report Manufacturing Order Registration | *(OBUIAPP / manual)* | Report Manufacturing Order Registration by Areas | — |
| Proceso / otro | Report Production Incident | Report Production Incident | Report Production Incident | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Productive process losses | Report Productive process losses | Report Productive process losses | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Used machine capacity | Report Used machine capacity | Report Used machine capacity | *(OBUIAPP / manual)* | Report Used machine capacity | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Create Standards New | Create Standards New | Java `CreateStandards` | Clase `CreateStandards` extiende `—`. | Clase `CreateStandards` extiende `—`. |
| Botón (PL/pgSQL) | Calculate Standard Costs | Calculate Standard Costs | PL `Ma_Standard_Cost` | Calculates the standard cost of manufactured products. | — |
| Botón (PL/pgSQL) | Create Production Costs | Create Production Costs | PL `MA_Production_Cost_Generate` | Create Production Costs | — |
| Botón (PL/pgSQL) | Create Standards NewSql | Create Standards NewSql | PL `ssprod_productionrun_standard` | ORDER BY MS.PRIORITY, t.m_product_id asc, mattsi.guaranteedate asc ;; It's taken the toolset with higher number of uses; Get StdPrecision of Uom of Product to be used in Production Line.; Insert production plan for used… | ORDER BY MS.PRIORITY, t.m_product_id asc, mattsi.guaranteedate asc ;; It's taken the toolset with higher number of uses; Get StdPrecision of Uom of Product to be used in Production Line.; Insert production plan for used products P-; Get StdPrecision for Uom of product to be used in Production Line; Get Locator with negative Stock that belongs to the same Warehosue |
| Botón (PL/pgSQL) | Generate Work_Requirement Prod | Generate Work_Requirement Prod | PL `ssprod_workrequirement` | Validar que el tipo de documento tenga secuencia asignada | Validar que el tipo de documento tenga secuencia asignada |
| Botón (PL/pgSQL) | Insert Maintenances | Insert Maintenances | PL `MA_Maint_All` | Insert Maintenances | — |
| Proceso / otro | Compliance with the Production Projection | Compliance with the Production Projection | — | — | — |
| Proceso / otro | Materials List Valued | Materials List Valued | — | — | — |
| Proceso / otro | Report Efficiency by standard time | Report Efficiency by standard time | — | — | — |
| Proceso / otro | Report Evolution of costs by product | Report Evolution of costs by product | — | — | — |
| Proceso / otro | Report Manufacturing Order Registration by Areas | Report Manufacturing Order Registration by Areas | — | Report Manufacturing Order Registration by Areas | — |
| Proceso / otro | Report Production Incident | Report Production Incident | — | — | — |
| Proceso / otro | Report Productive process losses | Report Productive process losses | — | — | — |
| Proceso / otro | Report Used machine capacity | Report Used machine capacity | — | Report Used machine capacity | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Daily Work Requirements Report | Daily Work Requirements Report | RV_ReportWorkRequirementDaily | Java `ReportWorkRequirementDaily` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `org/openbravo/erpCommon/ad_reports/ReportWorkRequirementDailyEdit.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementDaily.java` |
| Reporte | Generic Print Part Of Work | Generic Print Part Of Work | Generic Print Part Of Work | Java `Ssprod_GenericPrintPartOfWork` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `0D49D788605449178F19CBB42B5335EA|M_PRODUCTION_ID`. | `src/ec/com/sidesoft/production/ad_process/Ssprod_GenericPrintPartOfWork.java` |
| Reporte | Pending Work Requirement | Pending Work Requirement | ReportWorkRequirementJR | Java `ReportWorkRequirementJR` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementJR.java` |
| Reporte | Production Cost Report | Production Cost Report | RV_ReportProductionCost | Java `ReportProductionCost` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionCost.java` |
| Reporte | Production Run Status Report | Production Run Status Report | ReportProductionRunJR | Java `ReportProductionRunJR` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `org/openbravo/erpCommon/ad_reports/ReportProductionRun.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionRunJR.java` |
| Reporte | Standard Costs Report | Standard Costs Report | ReportStandardCostJR | Java `ReportStandardCostJR` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/production/ad_reports/reports/ReportStandardCostJR.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 16**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **6**; archivos `*.jrxml` en el repo = **16**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Daily Work Requirements Report | `RV_ReportWorkRequirementDaily` | Java `ReportWorkRequirementDaily`; JRXML `org/openbravo/erpCommon/ad_reports/ReportWorkRequirementDailyEdit.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | In this report are showed the work requirements of type ramp. By default only from actual date.. JRXML: `org/openbravo/erpCommon/ad_reports/ReportWorkRequirementDailyEdit.jrxml` |
| 2 | Generic Print Part Of Work | `Generic Print Part Of Work` | Java `Ssprod_GenericPrintPartOfWork`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Generic Print Part Of Work |
| 3 | Pending Work Requirement | `ReportWorkRequirementJR` | Java `ReportWorkRequirementJR`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | In this report are all the open work requirement phases and the quantities done and that left to do. |
| 4 | Production Cost Report | `RV_ReportProductionCost` | Java `ReportProductionCost`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Production Cost Report |
| 5 | Production Run Status Report | `ReportProductionRunJR` | Java `ReportProductionRunJR`; JRXML `org/openbravo/erpCommon/ad_reports/ReportProductionRun.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | Production Run Status Report. JRXML: `org/openbravo/erpCommon/ad_reports/ReportProductionRun.jrxml` |
| 6 | Standard Costs Report | `ReportStandardCostJR` | Java `ReportStandardCostJR`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Manufacturing Standard Cost |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/production/ad_reports/RptM_PartOfWork.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/RptSsprd_Employee.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/RptSsprod_StandarTime.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/RptSsprod_SubMachine.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/Rpt_ComplianceProductionProjection.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/Rpt_Evolution_Costs_By_product.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/Rpt_Materials_List_Valued.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/Rpt_PlanProductionCostVersion.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/Rpt_Production_Incidents.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/Rpt_Productive_Process_Losses.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/RtpSsprod_CapacityUsedMachine.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/SubReport_ProductosP.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionRun.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/reports/ReportStandardCostsJR.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementJR.jrxml`
- `src/ec/com/sidesoft/production/ad_reports/reports/Rpt_Work_Requirement_By_Area.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Ssprod_Startdate_Major` | The start time can not be longer than the end time. | The start time can not be longer than the end time. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssprod_Dates_Not_Equals` | Start date and end date must be equal. | Start date and end date must be equal. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo utiliza Java para manejar la lógica de negocio relacionada con la generación de informes y la gestión de procesos, lo que permite personalizar y extender la funcionalidad del sistema a través de clases específicas como 'PlanProduccionCostActionHandler'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.production`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `PlanProduccionCostActionHandler` | actionhandler | BaseReportActionHandler | — | `src/ec/com/sidesoft/production/actionhandler/PlanProduccionCostActionHandler.java` |
| `CreateStandards` | ad_actionButton | org | — | `src/ec/com/sidesoft/production/ad_actionButton/CreateStandards.java` |
| `ssprodupdatenumberrequest` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/production/ad_callouts/ssprodupdatenumberrequest.java` |
| `ImportLDM` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_process/ImportLDM.java` |
| `Ssprod_GenericPrintPartOfWork` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_process/Ssprod_GenericPrintPartOfWork.java` |
| `ProcessPlanComboData` | ad_reports | FieldProvider | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_reports/reports/ProcessPlanComboData.java` |
| `ProcessPlanVersionComboData` | ad_reports | FieldProvider | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_reports/reports/ProcessPlanVersionComboData.java` |
| `ReportProductionCost` | ad_reports | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionCost.java` |
| `ReportProductionRunData` | ad_reports | FieldProvider | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionRunData.java` |
| `ReportProductionRunJR` | ad_reports | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_reports/reports/ReportProductionRunJR.java` |
| `ReportStandardCostJR` | ad_reports | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_reports/reports/ReportStandardCostJR.java` |
| `ReportWorkRequirementDaily` | ad_reports | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementDaily.java` |
| `ReportWorkRequirementDailyData` | ad_reports | FieldProvider | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementDailyData.java` |
| `ReportWorkRequirementJR` | ad_reports | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/production/ad_reports/reports/ReportWorkRequirementJR.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSPROD_COSTCENTERUSE_TRG` | `m_productionplan` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPROD_DATECONTROL_TRG` | `m_productionplan` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPROD_M_PROD_ISSOTRX_TRG` | `m_production` | after INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Ssprod_User_id` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Ssprod_ValidateProdCategory` | `M_PRODUCT_CATEGORY.M_PRODUCT_CATEGORY_ID IN (SELECT MP.M_PRODUCT_CATEGORY_ID FROM M_PRODUCTIONLINE MPL JOIN M_PRODUCT MP` |
| AD_VAL_RULE | — | `Ssprod_M_Locator of Warehouse` | `M_Locator.M_Warehouse_ID=@m_warehouse_id@` |
| AD_VAL_RULE | — | `Validate User` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Ssprod_List_of_Materials_Product` | `IsBOM ='Y'` |
| AD_VAL_RULE | — | `Ssprod_ValidateProductProduction` | `M_PRODUCT.M_PRODUCT_ID IN (SELECT M_PRODUCT_ID FROM M_PRODUCTIONLINE WHERE productiontype='+' GROUP BY M_PRODUCT_ID )` |
| Función PL `ssprod_production_run` | — | invocación proceso | Proposed stock from given warehouse is priorized.; RAISE_APPLICATION_ERROR(-20000, 'Verifica correctamente los materiales');; Check the header belongs to a organization where transactions are posible and ready to use |
| Función PL `ssprod_productionrun_standard` | — | invocación proceso | ORDER BY MS.PRIORITY, t.m_product_id asc, mattsi.guaranteedate asc ;; It's taken the toolset with higher number of uses; Get StdPrecision of Uom of Product to be used in Production Line. |
| Función PL `ssprod_workrequirement` | — | invocación proceso | Validar que el tipo de documento tenga secuencia asignada |
| Función PL `ssprod_workrequirement_process` | — | invocación proceso | Check if all the required fields are filled; Check if it hasn't already been processed; OPEN Cur_SeqProduct (Cur_Sequence.MA_Sequence_ID); |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers desempeñan un rol crítico en el módulo, activándose en momentos clave para ejecutar rutinas PL/pgSQL que aseguran la correcta manipulación de los datos. Las funciones PL también son fundamentales para proporcionar soporte a los procesos dentro del módulo, permitiendo automatizar tareas y mejorar la eficiencia operativa en las distintas etapas del ciclo de producción.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSPROD_M_PROD_ISSOTRX_TRG` | `m_production` | after | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPROD_M_PROD_ISSOTRX_TRG.xml` |
| `SSPROD_COSTCENTERUSE_TRG` | `m_productionplan` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPROD_COSTCENTERUSE_TRG.xml` |
| `SSPROD_DATECONTROL_TRG` | `m_productionplan` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPROD_DATECONTROL_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssprod_getattribinstance_prd` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPROD_GETATTRIBINSTANCE_PRD.xml` |
| `ssprod_production_run` | — | Proposed stock from given warehouse is priorized.; RAISE_APPLICATION_ERROR(-20000, 'Verifica correctamente los materiales');; Check the header belongs to a organization where transactions are posible and ready to use; C… | Proposed stock from given warehouse is priorized.; RAISE_APPLICATION_ERROR(-20000, 'Verifica correctamente los materiales');; Check the header belongs to a organization where transactions are posible and ready to use; Check the lines belong to the same business unit or legal entity as the header; Check the period control is opened (only if it is legal entity with accounting); If AllowNegativeStock is enabled and MustBeStocked is disabled and there is not enough stock, | `model/functions/SSPROD_PRODUCTION_RUN.xml` |
| `ssprod_productionrun_standard` | Create Standards NewSql | ORDER BY MS.PRIORITY, t.m_product_id asc, mattsi.guaranteedate asc ;; It's taken the toolset with higher number of uses; Get StdPrecision of Uom of Product to be used in Production Line.; Insert production plan for used… | ORDER BY MS.PRIORITY, t.m_product_id asc, mattsi.guaranteedate asc ;; It's taken the toolset with higher number of uses; Get StdPrecision of Uom of Product to be used in Production Line.; Insert production plan for used products P-; Get StdPrecision for Uom of product to be used in Production Line; Get Locator with negative Stock that belongs to the same Warehosue | `model/functions/SSPROD_PRODUCTIONRUN_STANDARD.xml` |
| `ssprod_workrequirement` | Generate Work_Requirement Prod | Validar que el tipo de documento tenga secuencia asignada | Validar que el tipo de documento tenga secuencia asignada | `model/functions/SSPROD_WORKREQUIREMENT.xml` |
| `ssprod_workrequirement_process` | — | Check if all the required fields are filled; Check if it hasn't already been processed; OPEN Cur_SeqProduct (Cur_Sequence.MA_Sequence_ID);; MA_Workrequirement_Process - Finish Process Extension Point | Check if all the required fields are filled; Check if it hasn't already been processed; OPEN Cur_SeqProduct (Cur_Sequence.MA_Sequence_ID);; MA_Workrequirement_Process - Finish Process Extension Point; v_Message := v_Message || '@Created@: ' || v_NoRecords;; p_Invoice_ID := 0;        --  Error Indicator | `model/functions/SSPROD_WORKREQUIREMENT_PROCESS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Create Standards New | `CreateStandardsProcessNEW` | Botón (Java) | Java `CreateStandards` | N | Clase `CreateStandards` extiende `—`. |
| 2 | Calculate Standard Costs | `MA_StandardCost` | Botón (PL/pgSQL) | PL `Ma_Standard_Cost` | N | Calculates the standard cost of manufactured products. |
| 3 | Create Production Costs | `MA_Production_Cost_Generate` | Botón (PL/pgSQL) | PL `MA_Production_Cost_Generate` | N | Create Production Costs |
| 4 | Create Standards NewSql | `Ssprod_ProductionRun_Standard` | Botón (PL/pgSQL) | PL `ssprod_productionrun_standard` | N | ORDER BY MS.PRIORITY, t.m_product_id asc, mattsi.guaranteedate asc ;; It's taken the toolset with higher number of uses; Get StdPrecision of Uom of Product to be used in Production |
| 5 | Generate Work_Requirement Prod | `ssprod_workrequirement` | Botón (PL/pgSQL) | PL `ssprod_workrequirement` | N | Validar que el tipo de documento tenga secuencia asignada |
| 6 | Insert Maintenances | `MA_Maint_All` | Botón (PL/pgSQL) | PL `MA_Maint_All` | N | Insert Maintenances |
| 7 | Daily Work Requirements Report | `RV_ReportWorkRequirementDaily` | Reporte | Java `ReportWorkRequirementDaily` | S | Genera PDF desde JRXML `org/openbravo/erpCommon/ad_reports/ReportWorkRequirementDailyEdit.jrxml`; contexto sesión `—`. |
| 8 | Generic Print Part Of Work | `Generic Print Part Of Work` | Reporte | Java `Ssprod_GenericPrintPartOfWork` | S | Genera PDF desde JRXML `—`; contexto sesión `0D49D788605449178F19CBB42B5335EA|M_PRODUCTION_ID`. |
| 9 | Pending Work Requirement | `ReportWorkRequirementJR` | Reporte | Java `ReportWorkRequirementJR` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 10 | Production Cost Report | `RV_ReportProductionCost` | Reporte | Java `ReportProductionCost` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 11 | Production Run Status Report | `ReportProductionRunJR` | Reporte | Java `ReportProductionRunJR` | S | Genera PDF desde JRXML `org/openbravo/erpCommon/ad_reports/ReportProductionRun.jrxml`; contexto sesión `—`. |
| 12 | Standard Costs Report | `ReportStandardCostJR` | Reporte | Java `ReportStandardCostJR` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |

**Total acciones documentadas (extract):** **12** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `ec.com.sidesoft.production`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | presente |
| `AD_WINDOW.xml` | presente |
| `OBUIAPP_PROCESS.xml` | presente |
| Traducción `.es_ES` | no |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SSPROD`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPROD` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.production` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `CreateStandardsProcessNEW` — Create Standards New
- `MA_StandardCost` — Calculate Standard Costs
- `MA_Production_Cost_Generate` — Create Production Costs
- `Ssprod_ProductionRun_Standard` — Create Standards NewSql
- `ssprod_workrequirement` — Generate Work_Requirement Prod
- `MA_Maint_All` — Insert Maintenances
- `Ssprod_CompliancewithProduction` — Compliance with the Production Projection
- `Ssprod_Materials_List_Valued` — Materials List Valued
- `Report Efficiency by standard time` — Report Efficiency by standard time
- `Report Evolution of costs by product` — Report Evolution of costs by product
- `Report Manufacturing Order Registration` — Report Manufacturing Order Registration by Areas
- `Report Production Incident` — Report Production Incident
- `Report Productive process losses` — Report Productive process losses
- `Report Used machine capacity` — Report Used machine capacity
- `RV_ReportWorkRequirementDaily` — Daily Work Requirements Report

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Additional Information for Production
**Package:** `ec.com.sidesoft.production.additional.information`

# Module overview — Additional Information for Production

## Functional

El módulo 'Additional Information for Production' tiene como objetivo proporcionar información adicional en el proceso de producción dentro del ERP Openbravo. Los actores principales son los usuarios de negocio involucrados en la gestión de la producción, así como el personal de soporte y desarrollo que mantiene y optimiza el sistema. Este módulo se integra con el módulo de producción estándar, facilitando un flujo de trabajo más eficiente. No presenta dependencias con otros módulos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/production/additional/information` |
| Web | `web/ec.com.sidesoft.production.additional.information/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**0.0.1** (from `AD_MODULE.xml`).

### DB prefix

`SPDAI`

# Guía de chat — Additional Information for Production

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.production.additional.information`).

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

- ¿Cómo puedo acceder a la información adicional de producción?
- ¿Qué cambios en la tabla de producción debo tener en cuenta?
- ¿Qué sucede si se modifica el tipo de documento en un registro de producción?
- ¿Cómo se asegura la secuencialidad de los números de documento?
- ¿Dónde se reflejan los cambios realizados por el módulo?
- ¿Existen informes generados relacionados con el módulo?
- ¿Cómo se valida la información adicional en el proceso de producción?
- ¿Qué debo hacer si encuentro un error en los números de documento?

# Domain — data model

## Functional

La entidad cabecera principal del módulo es la tabla 'M_PRODUCTION', que se modifica por la funcionalidad de este módulo. Se realizan actualizaciones a esta tabla mediante el trigger 'SPDAI_ASSIGN_DOCUMENTNO_TRG', el cual asigna un número de documento relacionado con el tipo de documento específico en el proceso de producción. Este trigger valida si se ha modificado el tipo de documento y actualiza secuencialmente el número correspondiente, asegurando la coherencia de los datos.

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

`M_PRODUCTION`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no incluye ventanas específicas en la interfaz de usuario. Sin embargo, las modificaciones se reflejan en la gestión de la producción a través del sistema operativo de Openbravo. Los usuarios interactúan con la tabla de producción directamente mediante las funciones estándar de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.production.additional.information.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.production.additional.information.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `319`

- **AD_TAB_ID:** `319` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Document Type | `EM_Spdai_C_Doctype_ID` | No | No | — |
| 30 | Document No | `—` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que no hay procesos definidos para botones, informes o validaciones en este módulo, la funcionalidad básica se limita a la actualización automática de la tabla de producción a través del trigger mencionado anteriormente. La operación del módulo es manejada en conjunto con las funciones del módulo de producción estándar, donde las validaciones y reportes son gestionados de forma genérica.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.production.additional.information.es_ES/referencedata/translation/`.

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

Este módulo no incluye desarrollo en Java, lo que indica que todas las funcionalidades se realizan mediante configuraciones en la base de datos y triggers.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.production.additional.information`.

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
| Trigger `SPDAI_ASSIGN_DOCUMENTNO_TRG` | `m_production` | before INSERT/UPDATE | OBTENGO ID DE LA SEQUENCIA RELACIONADA AL TIPO DE DOCUMENTO; ACTUALIZO LA SECUENCIA AL SIGUIENTE NUMERO QUE LE CORRESPONDE; VALIDA SI SE MODIFICO EL TIPO DE DOCUMENTO; select distinct EM_Spdai_C_Doctype_ID from m_produc… |
| AD_VAL_RULE | — | `Production LDM` | `C_DocType.DocBaseType='SPDAI_LDM'` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El trigger 'SPDAI_ASSIGN_DOCUMENTNO_TRG' juega un papel crucial en el mantenimiento de la integridad de los datos en la tabla 'M_PRODUCTION'. Esta función asegura que los números que se asignan a los documentos de producción sean únicos y secuenciales, esencial para el seguimiento y la gestión de documentación en el ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SPDAI_ASSIGN_DOCUMENTNO_TRG` | `m_production` | before | INSERT/UPDATE | OBTENGO ID DE LA SEQUENCIA RELACIONADA AL TIPO DE DOCUMENTO; ACTUALIZO LA SECUENCIA AL SIGUIENTE NUMERO QUE LE CORRESPONDE; VALIDA SI SE MODIFICO EL TIPO DE DOCUMENTO; select distinct EM_Spdai_C_Doctype_ID from m_produc… | `model/triggers/SPDAI_ASSIGN_DOCUMENTNO_TRG.xml` |
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

Módulo: `ec.com.sidesoft.production.additional.information`.

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

# Glosario — prefijo `SPDAI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPDAI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.production.additional.information` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Localization Production Lote
**Package:** `ec.com.sidesoft.localization.production.lotautogen`

# Module overview — Sidesoft Localization Production Lote

## Functional

El módulo Sidesoft Localization Production Lote tiene como propósito manejar el desarrollo del IRBP (Impuesto a Botellas) de manera eficiente dentro del sistema Openbravo ERP. Entre los actores involucrados se encuentran los usuarios de negocio, que utilizan la interfaz para gestionar impuestos, y el equipo de soporte técnico que asegura el correcto funcionamiento del módulo. Este módulo se integra dentro del framework de Openbravo 3.0 y es compatible con versiones de 2.50 a 3.00, por lo que las dependencias técnicas son cruciales para su implementación exitosa.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/production/lotautogen` |
| Web | `web/ec.com.sidesoft.localization.production.lotautogen/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLPLAG`

# Guía de chat — Sidesoft Localization Production Lote

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.production.lotautogen`).

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
- «¿Qué es la tabla slplag_kindpackage?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo se establece el tipo de envase para un producto?
- ¿Qué pasos debo seguir si quiero eliminar una línea de factura?
- ¿Cómo puedo verificar si un producto está sujeto al impuesto IRBP?
- ¿Qué sucede si el total de impuestos a eliminar es cero?
- ¿Cómo afecta el tipo de envase al plan de pago?
- ¿Qué validaciones se realizan al agregar un nuevo producto?
- ¿Es posible modificar la configuración de un impuesto existente?
- ¿Qué aspectos debo considerar al realizar un informe de impuestos?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad cabecera relacionada principalmente con las líneas de facturas y pedidos a través de las tablas c_invoiceline y c_orderline, donde se registran los productos sujetos al impuesto IRBP. Las relaciones principales incluyen la validación de si los productos son de tipo IRBP (PET o SFP), lo que activa la creación automática de líneas de impuestos correspondientes. Se han implementado triggers clave, como SLPLAG_INVLINETAX_IRBP y SLPLAG_ORDLINETAX_IRBP, que garantizan que la información de impuestos se mantenga actualizada al momento de realizar inserciones o eliminaciones en las líneas de facturas y órdenes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `slplag_kindpackage` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `slplag_kindpackage` | slplag_kindpackage | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `slplag_kp_key`; Cols: name, description, presirbp, identifier; `SLPLAG_KP_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `slplag_kindpackage` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_TAX`, `M_PRODUCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de la ventana 'Tipo de envase IRBP', donde los usuarios pueden visualizar y gestionar la configuración de los tipos de envase que afectan el cálculo del importe del impuesto. Desde esta ventana, se accede a los campos correspondientes para establecer las características específicas de cada tipo de envase y su relación con el impuesto IRBP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.production.lotautogen.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Tipo de envase IRBP | Pakage Type |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Tipo de envase IRBP | Pakage Type | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.production.lotautogen.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Tipo de envase IRBP

- **AD_WINDOW_ID:** `574C4BE20E9D4320AE7ECC3601F2F802`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `84178D2F95BA48068C29DBAA69370F93` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `174`

- **AD_TAB_ID:** `174` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 380 | EM_Slplag_Irbp | `EM_Slplag_Irbp` | No | No | — |

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 1430 | Em_Slplag_Prodclasif | `Em_Slplag_Prodclasif` | No | No | A31BDC99288149C8B99BC5A1A7EA998F |
| 1440 | Em_Slplag_Brand | `Em_Slplag_Brand` | No | No | A31BDC99288149C8B99BC5A1A7EA998F |
| 1450 | Em_Slplag_Prodcap | `Em_Slplag_Prodcap` | No | No | A31BDC99288149C8B99BC5A1A7EA998F |
| 1460 | Em_Slplag_Irbpunit | `Em_Slplag_Irbpunit` | No | No | A31BDC99288149C8B99BC5A1A7EA998F |
| 1470 | Em_Slplag_Galcohol | `Em_Slplag_Galcohol` | No | No | A31BDC99288149C8B99BC5A1A7EA998F |
| 1475 | EM_Slplag_Package | `EM_Slplag_Package` | No | No | A31BDC99288149C8B99BC5A1A7EA998F |
| 1480 | EM_Slplag_Mantainpackage_ID | `EM_Slplag_Mantainpackage_ID` | No | No | A31BDC99288149C8B99BC5A1A7EA998F |

### Header (ventana: Tipo de envase IRBP)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 25 | Identifier | `Identifier` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | kpname | `Name` | No | No | — |
| 50 | kpdescription | `Description` | No | No | — |
| 60 | Presirbp | `Presirbp` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Aunque el módulo no cuenta con botones específicos para procesos, es fundamental destacar que las líneas de facturas y órdenes se manejan mediante validaciones automáticas al momento de guardar o eliminar registros. Los usuarios pueden esperar validaciones frecuentes que verifican la presencia de productos sujetos al IRBP y la correcta aplicación de los impuestos. Aunque no se presentan informes específicos, la lógica interna del módulo asegura que los datos sean consistentes para su análisis posterior.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.production.lotautogen.es_ES/referencedata/translation/`.

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

Dentro del módulo se incluye una clase Java dedicada a la gestión de cambios en los montos de impuestos, específicamente la clase SLPLAG_InvoiceTax_Amt, que se encarga de actualizar los montos de impuestos y verificar condiciones según los datos ingresados por el usuario, asegurando la integridad de los cálculos de impuestos en cada operación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.production.lotautogen`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SLPLAG_InvoiceTax_Amt` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/production/lotautogen/ad_callouts/SLPLAG_InvoiceTax_Amt.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SLPLAG_DEL_INVLNTAX_IRBP` | `c_invoiceline` | before DELETE | DETERMINAR SI LA LINEA A ELIMIANR TIENE PRODUCTO CON IMPEUSTO IRBP; DETERMINAR TODAS LAS LINEAS DE IMPUESTOS CON IRBP SUMAR CANTIDADES taxamt; SI EL TOTAL A RESTAR DEJA EN 0 EL IMPUESTO ELIMINAR LA LINEA; ELIMINAR LA LI… |
| Trigger `SLPLAG_DEL_ORDLNTAX_IRBP` | `c_orderline` | before DELETE | DETERMINAR SI LA LINEA A ELIMIANR TIENE PRODUCTO CON IMPEUSTO IRBP; DETERMINAR TODAS LAS LINEAS DE IMPUESTOS CON IRBP SUMAR CANTIDADES taxamt; SI EL TOTAL A RESTAR DEJA EN 0 EL IMPUESTO ELIMINAR LA LINEA; ELIMINAR LA LI… |
| Trigger `SLPLAG_INVLINETAX_IRBP` | `c_invoiceline` | after INSERT/UPDATE/DELETE | Caso 1 - IRBP - Determinar si el producto de la linea es de tipo IRBP (PET - SFP); Nueva linea a la linea de Impuestos del producto; Verirficar si no existe linea impuesto irbp o ldm crear la linea; CASO 2 - LDM (Lista… |
| Trigger `SLPLAG_ORDLINETAX_IRBP` | `c_orderline` | after INSERT/UPDATE/DELETE | Caso 1 - IRBP - Determinar si el producto de la linea es de tipo IRBP (PET - SFP); Nueva linea a la linea de Impuestos del producto; Verirficar si no existe linea impuesto irbp o ldm crear la linea; CASO 2 - LDM (Lista… |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers desempeñan un rol esencial en la lógica de base de datos del módulo, asegurando que las líneas de impuestos se actualicen o eliminen correctamente según las acciones del usuario. Esto incluye el manejo de cantidades y el ajuste automático a cero para los impuestos correspondientes cuando ya no hay productos asociados. Al no haber funciones PL específicas, el trabajo de soporte se centra en el monitoreo y la depuración de estas reglas automatizadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SLPLAG_DEL_INVLNTAX_IRBP` | `c_invoiceline` | before | DELETE | DETERMINAR SI LA LINEA A ELIMIANR TIENE PRODUCTO CON IMPEUSTO IRBP; DETERMINAR TODAS LAS LINEAS DE IMPUESTOS CON IRBP SUMAR CANTIDADES taxamt; SI EL TOTAL A RESTAR DEJA EN 0 EL IMPUESTO ELIMINAR LA LINEA; ELIMINAR LA LI… | `model/triggers/SLPLAG_DEL_INVLNTAX_IRBP.xml` |
| `SLPLAG_INVLINETAX_IRBP` | `c_invoiceline` | after | INSERT/UPDATE/DELETE | Caso 1 - IRBP - Determinar si el producto de la linea es de tipo IRBP (PET - SFP); Nueva linea a la linea de Impuestos del producto; Verirficar si no existe linea impuesto irbp o ldm crear la linea; CASO 2 - LDM (Lista… | `model/triggers/SLPLAG_INVLINETAX_IRBP.xml` |
| `SLPLAG_DEL_ORDLNTAX_IRBP` | `c_orderline` | before | DELETE | DETERMINAR SI LA LINEA A ELIMIANR TIENE PRODUCTO CON IMPEUSTO IRBP; DETERMINAR TODAS LAS LINEAS DE IMPUESTOS CON IRBP SUMAR CANTIDADES taxamt; SI EL TOTAL A RESTAR DEJA EN 0 EL IMPUESTO ELIMINAR LA LINEA; ELIMINAR LA LI… | `model/triggers/SLPLAG_DEL_ORDLNTAX_IRBP.xml` |
| `SLPLAG_ORDLINETAX_IRBP` | `c_orderline` | after | INSERT/UPDATE/DELETE | Caso 1 - IRBP - Determinar si el producto de la linea es de tipo IRBP (PET - SFP); Nueva linea a la linea de Impuestos del producto; Verirficar si no existe linea impuesto irbp o ldm crear la linea; CASO 2 - LDM (Lista… | `model/triggers/SLPLAG_ORDLINETAX_IRBP.xml` |
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

Módulo: `ec.com.sidesoft.localization.production.lotautogen`.

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

# Glosario — prefijo `SLPLAG`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLPLAG` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.production.lotautogen` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Production LDM Reports
**Package:** `ec.com.sidesoft.ldm.report`

# Module overview — Sidesoft Production LDM Reports

## Functional

El módulo 'Sidesoft Production LDM Reports' permite a los usuarios generar informes relacionados con la producción LDM dentro del sistema Openbravo. Está diseñado para ser utilizado por usuarios de negocio que necesiten obtener reportes específicos de producción y por desarrolladores que requieran integrar y extender la funcionalidad del módulo. Este módulo se integra perfectamente en el entorno Openbravo, pero no tiene dependencias externas adicionales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/ldm/report` |
| Web | `web/ec.com.sidesoft.ldm.report/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSLDMRP`

# Guía de chat — Sidesoft Production LDM Reports

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.ldm.report`).

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

- ¿Cómo puedo generar un informe de producción?
- ¿Qué tipos de formatos de informe están disponibles?
- ¿Dónde encuentro el informe generado después de ejecutarlo?
- ¿Qué datos se requieren para generar un informe de producción?
- ¿Puedo personalizar un informe existente?
- ¿Qué debo hacer si el informe no se genera correctamente?
- ¿Hay algún límite en la cantidad de datos que se puede reportar?
- ¿Cómo se exportan los informes a Excel o PDF?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la creación de informes, utilizando la tabla M_PRODUCT como entidad principal. Aunque no hay etapas explícitas definidas, el proceso de generación de informes implica la preparación de los datos necesarios y su transformación a un formato de presentación. Los triggers y funciones específicos no están definidos en este módulo, pero se espera que actúen en conjunción con el sistema Openbravo para manejar la lógica de negocio relacionada con los informes.

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

El módulo no cuenta con ventanas específicas dentro de la interfaz de usuario; sin embargo, permite acceder a los informes a través de procesos definidos que los usuarios pueden invocar mediante los menús y funcionalidades de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.ldm.report.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.ldm.report.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 560 | EM_Ssldmrp_Cost_Ldm | `EM_Ssldmrp_Cost_Ldm` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso principal para la impresión de un plan de producción genérico. Los usuarios pueden invocar este proceso para generar y exportar informes en diferentes formatos. Las validaciones comunes suelen centrarse en asegurar que se proporcionen los parámetros requeridos antes de la ejecución, garantizando que el sistema produzca un informe válido y utilizable.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.ldm.report.es_ES/referencedata/translation/`.

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
| Reporte | GENERIC - PRINT PRODUCTION PLAN | GENERIC - PRINT PRODUCTION PLAN | GENERIC - PRINT PRODUCTION PLAN | Java `Ssldmrp_GenericPrintProductionPlan` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `191|M_PRODUCTIONPLAN_ID`. | `src/ec/com/sidesoft/ldm/report/ad_process/Ssldmrp_GenericPrintProductionPlan.java` |
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
| Reporte | GENERIC - PRINT PRODUCTION PLAN | `Ssldmrp_GenericPrintProductionPlan` | Informe (servlet PDF) | `191|M_PRODUCTIONPLAN_ID` | — | `src/ec/com/sidesoft/ldm/report/ad_process/Ssldmrp_GenericPrintProductionPlan.java` |
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
| Reporte | GENERIC - PRINT PRODUCTION PLAN | GENERIC - PRINT PRODUCTION PLAN | GENERIC - PRINT PRODUCTION PLAN | Java `Ssldmrp_GenericPrintProductionPlan` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `191|M_PRODUCTIONPLAN_ID`. | `src/ec/com/sidesoft/ldm/report/ad_process/Ssldmrp_GenericPrintProductionPlan.java` |
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
| 1 | GENERIC - PRINT PRODUCTION PLAN | `GENERIC - PRINT PRODUCTION PLAN` | Java `Ssldmrp_GenericPrintProductionPlan`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | GENERIC - PRINT PRODUCTION PLAN |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/ldm/report/ad_reports/ReportCostLDM.jrxml`
- `src/ec/com/sidesoft/ldm/report/ad_reports/RptSsldmrp_ProductionPlan.jrxml`
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

El módulo incluye clases Java que manejan la generación de informes, facilitando la personalización y la extensión de funcionalidades de informe según las necesidades del negocio. Estas clases interactúan con las bases de datos y administran la lógica de presentación del informe generado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.ldm.report`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Ssldmrp_ReportCostLDM` | ad_actionbutton | BaseReportActionHandler | Proceso / informe Java | `src/ec/com/sidesoft/ldm/report/ad_actionbutton/Ssldmrp_ReportCostLDM.java` |
| `Ssldmrp_GenericPrintProductionPlan` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/ldm/report/ad_process/Ssldmrp_GenericPrintProductionPlan.java` |
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

No se han definido triggers ni funciones PL específicas en este módulo, lo que implica que el soporte técnico dependerá de la funcionalidad estándar de Openbravo. Esto facilita el mantenimiento y la escalabilidad del sistema sin complicaciones adicionales por lógica o estructura de datos personalizadas.

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
| 1 | GENERIC - PRINT PRODUCTION PLAN | `GENERIC - PRINT PRODUCTION PLAN` | Reporte | Java `Ssldmrp_GenericPrintProductionPlan` | S | Genera PDF desde JRXML `—`; contexto sesión `191|M_PRODUCTIONPLAN_ID`. |

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

Módulo: `ec.com.sidesoft.ldm.report`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | presente |
| Traducción `.es_ES` | sí |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SSLDMRP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSLDMRP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.ldm.report` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `GENERIC - PRINT PRODUCTION PLAN` — GENERIC - PRINT PRODUCTION PLAN

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
