# Openbravo Sidesoft — Contabilidad General

> Libro mayor, asientos contables, proceso contable, diario GL, conciliación de cuentas, carga masiva de asientos, subcuentas, reversiones, balances.

**Paquetes incluidos (14):**
- `ec.com.sidesoft.accounting.general.ledger.grouped` — General Ledger Agrouped Grouped
- `ec.com.sidesoft.accounting.process` — Customization Accounting Process
- `ec.com.sidesoft.gljournal.mods` — GL journal mods
- `ec.com.sidesoft.balancing.accounts` — balancing accounts
- `ec.com.sidesoft.subaccount.validation` — Subaccount Validation
- `ec.com.sidesoft.modify.accounting` — Sidesoft Modify Accounting
- `ec.com.sidesoft.transaction.reversal` — Accounting reverses
- `ec.com.sidesoft.loaddata.into.accounting.entries` — Mass loading of data into accounting entries
- `ec.com.sidesoft.amount.validation` — Sidesoft Amount Validation
- `ec.com.sidesoft.localization.inventoryaccounting` — Accounting Inventory Modules
- `ec.com.sidesoft.localization.report.notposted` — Not Posted Transaction Report
- `ec.com.sidesoft.finances.custom.balancereports` — Balance Report
- `ec.com.sidesoft.localization.finance.reports` — Finance Reports
- `ec.com.sidesoft.balance.performance` — Sidesoft Balance customization for big data volume


---
## General Ledger Agrouped Grouped
**Package:** `ec.com.sidesoft.accounting.general.ledger.grouped`

# Module overview — General Ledger Agrouped Grouped

## Functional

El módulo 'General Ledger Agrouped Grouped' tiene como propósito gestionar y agrupar la contabilidad general dentro del sistema Openbravo. Está diseñado para ser utilizado por profesionales de contabilidad y finanzas, quienes manipularán y visualizarán datos contables agrupados. El alcance del módulo se extiende desde la entrada de datos contables hasta la generación de reportes para la toma de decisiones, integrando datos relevantes de otras áreas del ERP. Dependencias incluyen la compatibilidad con versiones previas de Openbravo y el uso de su framework estándar.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/accounting/general/ledger/grouped` |
| Web | `web/ec.com.sidesoft.accounting.general.ledger.grouped/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SACGLD`

# Guía de chat — General Ledger Agrouped Grouped

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.accounting.general.ledger.grouped`).

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

- ¿Cómo puedo acceder al módulo de contabilidad general?
- ¿Qué funciones están disponibles en el proceso contable?
- ¿Cómo se valida la información ingresada al ledger?
- ¿Dónde puedo ver mis transacciones contables agrupadas?
- ¿Qué hacer si encuentro un error en mis registros contables?
- ¿Cuáles son las dependencias del módulo y cómo afectan mi configuración?
- ¿Existen reportes predefinidos que pueda utilizar?
- ¿Cómo puedo asegurarme de que mis datos contables son consistentes?

# Domain — data model

## Functional

La entidad principal del modelo de datos es el ledger de contabilidad, que agrupa transacciones y asientos contables. Este módulo interactúa principalmente con tablas clave como 'AD_ORG', 'C_BPARTNER', y 'FACT_ACCT', asegurando que las relaciones entre organizaciones, socios comerciales y cuentas del sistema sean coherentes y estén debidamente enlazadas. Aunque no se definen etapas dentro del módulo, el flujo se establece a través de procesos de contabilidad agrupados. Actualmente, no hay triggers específicos configurados en el módulo.

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

`AD_ORG`, `AD_TABLE`, `C_BPARTNER`, `C_COSTCENTER`, `C_ELEMENTVALUE`, `FACT_ACCT`, `FIN_PAYMENT`, `USER1`, `USER2`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no cuenta con ventanas específicas definidas en la interfaz de usuario, lo que sugiere que se puede acceder a sus funciones a través de un menú principal del ERP. Los usuarios navegarán a través de las opciones provistas bajo el menú, accediendo a funciones específicas para la gestión de la contabilidad general y su agrupamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.accounting.general.ledger.grouped.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Reporte Libro Mayor | General Ledger Report Detailed Agruped | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.accounting.general.ledger.grouped.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `132`

- **AD_TAB_ID:** `132` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 200 | EM_Sacgld_Noshow_Client | `EM_Sacgld_Noshow_Client` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un único proceso contable clave que permite a los usuarios completar, retornar o rechazar transacciones contables según sea necesario. Este proceso puede estar acompañado de validaciones frecuentes que aseguran la consistencia de los datos ingresados. Sin embargo, no se han definido informes específicos dentro del módulo, lo que puede limitar la capacidad de los usuarios para obtener reportes detallados del estado contable agrupado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.accounting.general.ledger.grouped.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Libro Mayor | General Ledger Report Detailed Agruped | General Ledger Report Detailed Agruped | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Reporte Libro Mayor | General Ledger Report Detailed Agruped | General Ledger Report Detailed Agruped | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Libro Mayor | General Ledger Report Detailed Agruped | — | — | — |
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

No se han definido clases Java específicas para este módulo, por lo tanto, toda la funcionalidad se maneja a través de las funciones PL y la configuración dentro del framework de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.accounting.general.ledger.grouped`.

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
| AD_VAL_RULE | — | `SACGLD_Validationuser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers dentro del módulo son inexistentes, pero se implementan varias funciones PL que brindan soporte en la gestión contable. Estas funciones son críticas para garantizar que los datos se procesen correctamente en la base de datos y cumplir con los requisitos del negocio, así como para la validación y el ingreso de datos contables.

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
| `sacgld_costcenter` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SACGLD_COSTCENTER.xml` |
| `sacgld_factacct_des` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SACGLD_FACTACCT_DES.xml` |
| `sacgld_factacct_docn` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SACGLD_FACTACCT_DOCN.xml` |
| `sacgld_factacct_ref` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SACGLD_FACTACCT_REF.xml` |
| `sacgld_factacct_transno` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SACGLD_FACTACCT_TRANSNO.xml` |
| `sacgld_factacct_trx_descr` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SACGLD_FACTACCT_TRX_DESCR.xml` |
| `sacgld_user` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SACGLD_USER.xml` |
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

Módulo: `ec.com.sidesoft.accounting.general.ledger.grouped`.

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

# Glosario — prefijo `SACGLD`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SACGLD` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.accounting.general.ledger.grouped` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `General Ledger Report Detailed Agruped` — Reporte Libro Mayor

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Customization Accounting Process
**Package:** `ec.com.sidesoft.accounting.process`

# Module overview — Customization Accounting Process

## Functional

El módulo 'Customization Accounting Process' tiene como propósito extender y personalizar el proceso contable dentro del ERP Openbravo. Está diseñado para ser utilizado por usuarios de negocio que gestionan la contabilidad, así como por desarrolladores y el equipo de soporte de nivel 2 (L2) que necesitarán entender su integración y funcionamiento. Su implementación depende del marco de trabajo de Openbravo 3.0, lo que garantiza la compatibilidad y el acceso a las funcionalidades básicas del ERP. Este módulo se centra en la gestión y restauración de documentos contables, facilitando el cumplimiento normativo y la exactitud en los reportes financieros.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/accounting/process` |
| Web | `web/ec.com.sidesoft.accounting.process/` |

### Declared dependencies

- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SACCP`

# Guía de chat — Customization Accounting Process

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.accounting.process`).

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

- ¿Cómo puedo restaurar un documento contable específico?
- ¿Qué acciones se realizan durante el proceso de contabilidad personalizada?
- ¿Cuáles son los requisitos para configurar un nuevo tipo de documento contable?
- ¿Dónde puedo ver los registros de los procesos contables ejecutados?
- ¿Qué validaciones se aplican al crear un nuevo registro contable?
- ¿Cómo se pueden manejar las excepciones durante el proceso de contabilidad?
- ¿Qué hacer si un documento contable no se puede completar?
- ¿Cómo se lleva a cabo la integración con otros módulos del ERP?

# Domain — data model

## Functional

El módulo no contiene tablas físicas, sino que se basa en la manipulación de datos a través de las entidades del ERP. El proceso principal está encapsulado en la entidad de cabecera que está vinculada a las instancias de proceso (ad_pinstance). Existe un trigger clave, 'SACCP_PINSTANCE_TRG', que se ejecuta en la tabla 'ad_pinstance' para manejar eventos relacionados con la ejecución del proceso. Este trigger, implementado en PL/pgSQL, es fundamental para asegurar la integridad de los datos durante la creación y modificación de instancias de los documentos contables.

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

El módulo no tiene ventanas definidas en la interfaz de usuario de Openbravo, lo que sugiere que su funcionalidad puede estar integrada directamente en procesos existentes o accederse a través de herramientas de administración backend. Los usuarios accederán a las funcionalidades del módulo a través de las rutas ya establecidas dentro del sistema ERP, orientadas a la gestión contable.

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
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo no incluye botones de proceso específicos ni reportes como parte de su funcionalidad. Sin embargo, las validaciones frecuentes pueden incluir asegurar que los tipos de documentos contables sean válidos y que las fechas ingresadas se encuentren dentro de los parámetros permitidos. En el contexto general del ERP, los usuarios estarán familiarizados con botones de completar, retornar y rechazar, que permiten gestionar los ciclos de vida de los documentos contables.

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

El módulo incluye varias clases Java que proporcionan funcionalidades específicas, como 'DocumenTypeFilterExpression' y 'ResetAccountingDocumentTypeHandler', que gestionan la lógica de filtrado y reinicio de tipos de documentos contables. Estas clases permiten establecer condiciones en las consultas y manejar la lógica de negocio durante la ejecución de procesos contables complejos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.accounting.process`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `DocumenTypeFilterExpression` | root | FilterExpression | — | `src/ec/com/sidesoft/accounting/process/DocumenTypeFilterExpression.java` |
| `ResetAccountingDocumentTypeHandler` | root | ResetAccountingHandler | — | `src/ec/com/sidesoft/accounting/process/ResetAccountingDocumentTypeHandler.java` |
| `ResetAccountingUtil` | root | — | — | `src/ec/com/sidesoft/accounting/process/ResetAccountingUtil.java` |
| `SaccpPeriodControlEventListener` | event | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/accounting/process/event/SaccpPeriodControlEventListener.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SACCP_PINSTANCE_TRG` | `ad_pinstance` | after UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Java event/validator | `SaccpPeriodControlEventListener` | persistencia/UI | *(leer `src/ec/com/sidesoft/accounting/process/event/SaccpPeriodControlEventListener.java`)* |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El rol de los triggers en este módulo es primordial para el apoyo al proceso contable, asegurando que se tomen las acciones adecuadas cuando se crean o modifican instancias de procesos contables. Además, aunque no se han definido funciones PL específicas, las operaciones del trigger permiten mantener el control sobre la lógica de negocio y la integridad referencial de los datos durante la ejecución del proceso contable.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SACCP_PINSTANCE_TRG` | `ad_pinstance` | after | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SACCP_PINSTANCE_TRG.xml` |
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

Módulo: `ec.com.sidesoft.accounting.process`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | presente |
| Traducción `.es_ES` | no |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SACCP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SACCP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.accounting.process` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## GL journal mods
**Package:** `ec.com.sidesoft.gljournal.mods`

# Module overview — GL journal mods

## Functional

El módulo GL journal mods tiene como propósito modificar el comportamiento del botón 'Copiar detalles' en la ventana 'Asientos manuales' del ERP Openbravo. Actores principales incluyen usuarios contables y administradores de ERP que utilizan esta funcionalidad para optimizar la creación de asientos. El alcance del módulo se limita a la mejora en la gestión de los asientos contables, proporcionando una forma más ordenada de copiar detalles de un asiento a otro. No depende de otros módulos, funcionando de manera autónoma dentro del sistema Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/gljournal/mods` |
| Web | `web/ec.com.sidesoft.gljournal.mods/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SGLJ`

# Guía de chat — GL journal mods

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.gljournal.mods`).

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

- ¿Cómo puedo utilizar el módulo GL journal mods en Openbravo?
- ¿Qué cambios introduce el módulo en el proceso de copiado de asientos?
- ¿Dónde encuentro la opción para copiar detalles de asientos manuales?
- ¿Este módulo afecta a otros procesos en la gestión de asientos?
- ¿Qué debo hacer si no puedo ver el botón de copiar detalles?
- ¿Es posible revertir cambios realizados por el módulo?
- ¿Cómo se ordenan las líneas en el nuevo asiento copiado?
- ¿Dónde puedo encontrar ayuda adicional sobre este módulo?

# Domain — data model

## Functional

El módulo introduce un fork de la clase responsable de la funcionalidad de copiar asientos contables, enfocándose en la reordenación de los datos por número de documento en el nuevo asiento. Aunque no se definen tablas físicas nuevas, se utiliza la estructura existente de asientos contables para realizar las modificaciones. Las relaciones se mantienen dentro del contexto de los asientos y las transacciones relacionadas, aunque no se han definido disparadores (triggers) ni funciones PL en este módulo, lo que indica que se centra únicamente en el proceso de la interfaz.

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

El módulo no incluye nuevas ventanas, pero la funcionalidad se integra en la existente ventana 'Asientos manuales'. Los usuarios navegan dentro de esta ventana para acceder a la opción de copiar detalles de asientos, activando así la lógica implementada en el módulo de manera seamless.

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
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso principal implica el uso del botón 'Copiar detalles', donde al ejecutarlo, se generan nuevas líneas de asientos contables basadas en el asiento seleccionado, reordenadas por número de documento. No se registran validaciones frecuentes o informes asociados, lo que sugiere que el enfoque está destinado a simplificar y optimizar el proceso sin añadir pasos adicionales de verificación.

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

La clase Java 'CopyFromGLJournal' es central en la ejecución de la lógica de negocio, actuando como el controlador principal que gestiona la solicitud del usuario para copiar asientos contables y ordenar las entradas de acuerdo a un criterio específico (número de documento).

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.gljournal.mods`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `CopyFromGLJournal` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/gljournal/mods/ad_process/CopyFromGLJournal.java` |
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

Dado que el módulo no incluye disparadores ni funciones PL, su rol en la base de datos es mínimo y se centra en facilitar la operación de copiar detalles dentro del contexto de la aplicación. Sin embargo, la interacción con bases de datos se realiza a través de la lógica encapsulada en la clase Java del módulo.

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

Módulo: `ec.com.sidesoft.gljournal.mods`.

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

# Glosario — prefijo `SGLJ`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SGLJ` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.gljournal.mods` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## balancing accounts
**Package:** `ec.com.sidesoft.balancing.accounts`

# Module overview — balancing accounts

## Functional

El módulo de 'balancing accounts' permite gestionar las cuentas contables que se utilizarán para la conciliación en el dashboard de Metabase. Este módulo fue desarrollado como respuesta al ticket '21110 - SOPORTE - Incluir cuentas para cuadre en METABASE'. Los principales actores son los usuarios de negocio que gestionan las cuentas contables y los desarrolladores que configuran el sistema. Su alcance se limita a la configuración de cuentas contables y no interactúa directamente con otros módulos, aunque depende de componentes del núcleo de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/balancing/accounts` |
| Web | `web/ec.com.sidesoft.balancing.accounts/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**1.0.0** (from `AD_MODULE.xml`).

### DB prefix

`ECSBA`

# Guía de chat — balancing accounts

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.balancing.accounts`).

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
- «¿Qué es la tabla ecsba_accounting_accounts?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo agregar una nueva cuenta contable?
- ¿Qué debo hacer si mi cuenta contable no se carga correctamente?
- ¿Cómo elimino una cuenta contable que ya no necesito?
- ¿Dónde puedo ver las cuentas contables existentes?
- ¿Qué validaciones se realizan al crear una cuenta contable?
- ¿Cómo puedo saber si una cuenta está asociada a un desglose?
- ¿Qué hacer si no puedo modificar una cuenta contable?
- ¿Dónde encuentro la configuración para reconciliación en Metabase?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la entidad cabecera 'ecsba_accounting_accounts', que almacena información sobre las cuentas contables. Este modelo incluye varias relaciones con otras tablas, como 'ecsba_breakdown_balance', que representa líneas de desglose asociadas a las cuentas. Las etapas del flujo son principalmente la creación y modificación de cuentas contables, donde se activan triggers para validar datos y mantener la integridad referencial. Los triggers clave incluyen 'ECSBA_ACC_ACC_CKNAME_TRG' en la tabla 'ecsba_accounting_accounts' y 'ECSBA_BREAKDOWN_BAL_TRG' en 'ecsba_breakdown_balance', que se encargan de verificar condiciones antes de que se realicen cambios en la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ecsba_account_paramet` |
| `ecsba_accounting_accounts` |
| `ecsba_breakdown` |
| `ecsba_breakdown_balance` |
| `ecsba_module` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ecsba_account_paramet` | ECSBA_Account_Paramet | — | — | ad_client_id→ad_client; c_element_id→c_element; ecsba_module_id→ecsba_module; ad_org_id→ad_org | Detalle enlazado a ad_client, c_element, ecsba_module. | PK `ecsba_account_paramet_key`; Cols: ecsba_module_id, description, c_element_id; `ECSBA_ACCOUNT_PARAMET_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ecsba_accounting_accounts` | ECSBA_Accounting_Accounts | `ECSBA_ACC_ACC_CKNAME_TRG` | — | ad_client_id→ad_client; c_elementvalue_id→c_elementvalue; ad_org_id→ad_org; ecsba_breakdown_balance_id→ecsba_breakdown_balance | Detalle enlazado a ad_client, ad_org, c_elementvalue. Validado por trigger(s): ECSBA_ACC_ACC_CKNAME_TRG. | PK `ecsba_accounting_acc_key`; Cols: c_elementvalue_id, description, ecsba_breakdown_balance_id; `ECSBA_ACCOUNTING_ACC_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ecsba_breakdown` | ECSBA_Breakdown | `ECSBA_BREAKDOWN_CKNAME_TRG` | — | ad_client_id→ad_client; ecsba_module_id→ecsba_module; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, ecsba_module. Validado por trigger(s): ECSBA_BREAKDOWN_CKNAME_TRG. | PK `ecsba_breakdown_key`; Cols: name, description, formule, ecsba_module_id; `ECSBA_BREAKDOWN_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ecsba_breakdown_balance` | ECSBA_Breakdown_Balance | `ECSBA_BREAKDOWN_BAL_TRG` | — | ecsba_breakdown_id→ecsba_breakdown; ad_client_id→ad_client; ad_org_id→ad_org; ecsba_account_paramet_id→ecsba_account_paramet | Detalle enlazado a ad_client, ad_org, ecsba_breakdown. Validado por trigger(s): ECSBA_BREAKDOWN_BAL_TRG. | PK `ecsba_breakdown_bal_key`; Cols: ecsba_breakdown_id, description, ecsba_acc_load, ecsba_account_paramet_id; `ECSBA_BREAKDOWN_BAL_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ecsba_module` | ECSBA_Module | `ECSBA_MODULE_CKNAME_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. Validado por trigger(s): ECSBA_MODULE_CKNAME_TRG. | PK `ecsba_module_key`; Cols: name, description; `ECSBA_MODULE_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ECSBA_Account_Paramet` |
| `ECSBA_Accounting_Accounts` |
| `ECSBA_Breakdown` |
| `ECSBA_Breakdown_Balance` |
| `ECSBA_Module` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de dos ventanas en la interfaz de usuario: 'Módulo' y 'Parametrización Cuentas Contables'. Desde estas ventanas, los usuarios pueden gestionar las cuentas contables y acceder a la configuración necesaria para la conciliación contable. Cada ventana contiene múltiples pestañas que permiten ingresar y visualizar datos específicos relacionados con las cuentas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.balancing.accounts.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Módulo | Module |
| Parametrización Cuentas Contables | Accounting Account Parameterization |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración | Configuration | Sí |
| Cuadre Módulo vs Contabilidad | Reconciliation Module vs. Accounting | Sí |
| Módulo | Module | No |
| Parametrización Cuentas Contables | Accounting Account Parameterization | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.balancing.accounts.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Módulo

- **AD_WINDOW_ID:** `E00A9DCB254C4DA98D39F64EA0F407AA`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Module | `FADFC775E4C941F1827A6C7F0FF04C9C` | 0 |
| 20 | Breakdown | `9C505E7A33B643FA84128CFB4316E7CC` | 1 |

### Ventana: Parametrización Cuentas Contables

- **AD_WINDOW_ID:** `E19452BEACD64729A6B7E0BDB28057B4`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Accounting Account Parameterization | `D0491BEAED164F82A97FE26C484F7712` | 0 |
| 20 | Breakdown of Balance | `82D7911DD8814560968932A3203DAD8C` | 1 |
| 30 | Accounting Accounts | `D624DEF9400248EABDFDAC925AD78B7F` | 2 |

## Campos añadidos por el módulo (AD_FIELD)

### Accounting Accounts (ventana: Parametrización Cuentas Contables)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Account Element | `C_Elementvalue_ID` | No | No | — |
| 20 | Description | `Description` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |

### Module (ventana: Módulo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Name | `Name` | No | No | — |
| 30 | Description | `Description` | No | No | — |
| 40 | Active | `Isactive` | No | No | — |

### Accounting Account Parameterization (ventana: Parametrización Cuentas Contables)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Ecsba_Module_ID | `Ecsba_Module_ID` | No | No | — |
| 30 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Breakdown (ventana: Módulo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Name | `Name` | No | No | — |
| 20 | Description | `Description` | No | No | — |
| 30 | Formule | `Formule` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Breakdown of Balance (ventana: Parametrización Cuentas Contables)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Ecsba_Breakdown_ID | `Ecsba_Breakdown_ID` | No | No | — |
| 20 | Description | `Description` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 50 | bulk upload of accounting accounts | `Ecsba_Acc_Load` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un único proceso que se activa mediante un botón que permite la carga masiva de cuentas contables. Durante este proceso, se realizan varias validaciones, como asegurar que no existan registros dependientes antes de permitir eliminaciones. Los informes no están habilitados en este módulo, pero se generan mensajes de error comunes para validar la integridad de la información durante la carga o modificación de registros.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.balancing.accounts.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar masiva de cuentas contables | bulk upload of accounting accounts | ECSBA_ACC_LOAD | Java `EcsbaAccLoad` (AD_MODEL_OBJECT `P`) | Proceso Openbravo ver `doExecute` en fuente | `src/ec/com/sidesoft/balancing/accounts/EcsbaAccLoad.java` |
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
| Botón (Java) | Cargar masiva de cuentas contables | `EcsbaAccLoad` | Proceso Java (toolbar/background) | `—` | — | `src/ec/com/sidesoft/balancing/accounts/EcsbaAccLoad.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar masiva de cuentas contables | bulk upload of accounting accounts | ECSBA_ACC_LOAD | Java `EcsbaAccLoad` (AD_MODEL_OBJECT `P`) | Proceso Openbravo ver `doExecute` en fuente | `src/ec/com/sidesoft/balancing/accounts/EcsbaAccLoad.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar masiva de cuentas contables | bulk upload of accounting accounts | Java `EcsbaAccLoad` | Proceso Openbravo ver `doExecute` en fuente | Proceso Openbravo ver `doExecute` en fuente |
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
| `ECSBA_Deletemsg` | The record cannot be deleted. It has records on the lines. | The record cannot be deleted. It has records on the lines. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `ECSBA_DuplicateName` | Name can't be duplicated | Name can't be duplicated | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye clases Java que manejan la lógica de carga y validación de las cuentas contables, como 'EcsbaAccLoad'. Estas clases permiten ejecutar procesos específicos, interactuar con la base de datos y gestionar las transacciones de manera eficiente dentro del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.balancing.accounts`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `EcsbaAccLoad` | root | DalBaseProcess | — | `src/ec/com/sidesoft/balancing/accounts/EcsbaAccLoad.java` |
| `Ecsba_AccountParametValid` | ad_actionHandler | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/balancing/accounts/ad_actionHandler/Ecsba_AccountParametValid.java` |
| `Ecsba_BreakdownBalanceValid` | ad_actionHandler | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/balancing/accounts/ad_actionHandler/Ecsba_BreakdownBalanceValid.java` |
| `Ecsba_ModuleValid` | ad_actionHandler | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/balancing/accounts/ad_actionHandler/Ecsba_ModuleValid.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `ECSBA_ACC_ACC_CKNAME_TRG` | `ecsba_accounting_accounts` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `ECSBA_BREAKDOWN_BAL_TRG` | `ecsba_breakdown_balance` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `ECSBA_BREAKDOWN_CKNAME_TRG` | `ecsba_breakdown` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `ECSBA_MODULE_CKNAME_TRG` | `ecsba_module` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `ECSBA_C_ELEMENT_ID` | `td0.ElementLevel = 'S' AND td0.EM_Ssav_Ismodule = 'Y' AND td0.Isactive = 'Y'` |
| AD_VAL_RULE | — | `ECSBA_BREAKDOWN_MODULE_ID` | `ECSBA_Module_ID = @ECSBA_MODULE_ID@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y las funciones PL desempeñan un rol crucial en el soporte, asegurando la integridad de los datos a medida que se realizan operaciones en las tablas del módulo. Los triggers establecidos utilizan rutinas PL/pgSQL para aplicar las validaciones definidas y evitar operaciones no permitidas, como la eliminación de cuentas contables utilizadas en balances.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `ECSBA_ACC_ACC_CKNAME_TRG` | `ecsba_accounting_accounts` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/ECSBA_ACC_ACC_CKNAME_TRG.xml` |
| `ECSBA_BREAKDOWN_CKNAME_TRG` | `ecsba_breakdown` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/ECSBA_BREAKDOWN_CKNAME_TRG.xml` |
| `ECSBA_BREAKDOWN_BAL_TRG` | `ecsba_breakdown_balance` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/ECSBA_BREAKDOWN_BAL_TRG.xml` |
| `ECSBA_MODULE_CKNAME_TRG` | `ecsba_module` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/ECSBA_MODULE_CKNAME_TRG.xml` |
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
| 1 | Cargar masiva de cuentas contables | `ECSBA_ACC_LOAD` | Botón (Java) | Java `EcsbaAccLoad` | N | Proceso Openbravo ver `doExecute` en fuente |

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

Módulo: `ec.com.sidesoft.balancing.accounts`.

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

# Glosario — prefijo `ECSBA`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `ECSBA` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.balancing.accounts` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `ECSBA_ACC_LOAD` — Cargar masiva de cuentas contables

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Subaccount Validation
**Package:** `ec.com.sidesoft.subaccount.validation`

# Module overview — Subaccount Validation

## Functional

El módulo de Validación de Subcuentas tiene como objetivo garantizar que las subcuentas contables en Openbravo cumplan con determinadas reglas y validaciones antes de ser guardadas. Los actores principales incluyen usuarios de negocio que gestionan cuentas contables y desarrolladores que implementan logísticas de validación. Este módulo es compatible con la versión de Openbravo que va desde 2.50 hasta 3.00 y depende de la '2.50 to 3.00 Compatibility Skin'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/subaccount/validation` |
| Web | `web/ec.com.sidesoft.subaccount.validation/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSAV`

# Guía de chat — Subaccount Validation

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.subaccount.validation`).

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

- ¿Qué sucede si intento guardar una subcuenta no válida?
- ¿Dónde puedo encontrar la información sobre las subcuentas validadas?
- ¿Cómo puedo modificar una subcuenta existente después de su validación?
- ¿Hay algún límite en el número de subcuentas que puedo validar a la vez?
- ¿Cómo puedo saber si una subcuenta se ha guardado correctamente?
- ¿Qué mensajes de error puedo esperar al validar subcuentas?
- ¿Qué configuraciones debo verificar si no puedo guardar una subcuenta?
- ¿Existen permisos específicos que necesito para acceder a estas validaciones?

# Domain — data model

## Functional

La entidad central del módulo es 'GLItemAccounts', la cual se encarga de gestionar las cuentas del libro mayor. El proceso de validación se activa en etapas de inserción y actualización de registros en esta entidad, lo cual permite asegurar la integridad de los datos contables. Se modificó la tabla 'C_ELEMENTVALUE' para incluir las validaciones requeridas y garantizar que se puedan realizar comprobaciones adicionales antes de guardar los datos. Aunque no se definen triggers específicos en el módulo, las validaciones se implementan a través de funciones en Java.

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

`C_ELEMENTVALUE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo de validación de subcuentas no cuenta con ventanas o tabs definidos en la interfaz de usuario, por lo que las interacciones se realizan principalmente a través de eventos en las entidades afectadas como 'GLItemAccounts' y 'GLJournalLine'. Cualquier acción de guardar o actualizar desencadena las validaciones necesarias.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.subaccount.validation.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.subaccount.validation.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `132`

- **AD_TAB_ID:** `132` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 210 | EM_Ssav_Ismodule | `EM_Ssav_Ismodule` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Las acciones típicas en este módulo incluyen la inserción y actualización de cuentas contables, donde se invocan validaciones automáticas que pueden impedir el guardado si las subcuentas no cumplen con las reglas establecidas. Aunque no se definen botones específicos, la funcionalidad de retorno y validación es esencial. No hay informes generados, ni procesos asociados definidos en el inventario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.subaccount.validation.es_ES/referencedata/translation/`.

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

Las clases Java en este módulo, como 'SsavGLItemAccountsEvent' y 'SsavGlJournalEvent', están diseñadas para observar eventos de persistencia en las entidades 'GLItemAccounts' y 'GLJournalLine'. A través de estas clases, se gestionan validaciones específicas cada vez que se crean o actualizan registros en estas entidades.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.subaccount.validation`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SsavGLItemAccountsEvent` | root | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/subaccount/validation/SsavGLItemAccountsEvent.java` |
| `SsavGlJournalEvent` | root | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/subaccount/validation/SsavGlJournalEvent.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Java event/validator | `SsavGLItemAccountsEvent` | persistencia/UI | *(leer `src/ec/com/sidesoft/subaccount/validation/SsavGLItemAccountsEvent.java`)* |
| Java event/validator | `SsavGlJournalEvent` | persistencia/UI | *(leer `src/ec/com/sidesoft/subaccount/validation/SsavGlJournalEvent.java`)* |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL no están presentes en este módulo; sin embargo, se utilizan eventos en Java para manejar la lógica de validación. Esto proporciona un mecanismo flexible para integrar la lógica de negocio en el ciclo de vida de las entidades sin requerir un gran número de personalizaciones en la base de datos.

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

Módulo: `ec.com.sidesoft.subaccount.validation`.

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

# Glosario — prefijo `SSAV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSAV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.subaccount.validation` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Modify Accounting
**Package:** `ec.com.sidesoft.modify.accounting`

# Module overview — Sidesoft Modify Accounting

## Functional

El módulo Sidesoft Modify Accounting permite la modificación de asientos contables dentro del sistema Openbravo. Su propósito principal es garantizar que las modificaciones realizadas a los asientos contables cumplan con ciertas validaciones y restricciones antes de ser aceptadas. Los actores principales son los usuarios del negocio que gestionan la contabilidad, así como el soporte técnico de nivel 2 que proporciona asistencia en caso de problemas. El alcance se limita a la modificación de asientos contables y se basa en la dependencia del núcleo del sistema Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/modify/accounting` |
| Web | `web/ec.com.sidesoft.modify.accounting/` |

### Declared dependencies

- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSMAACT`

# Guía de chat — Sidesoft Modify Accounting

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.modify.accounting`).

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
- «¿Qué es la tabla ssmaact_accounting?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo modificar un asiento contable?
- ¿Qué validaciones se aplican al modificar un asiento?
- ¿Qué sucede si intento borrar un asiento contable?
- ¿Hay límites en las modificaciones que puedo hacer?
- ¿Cómo puedo comprobar el historial de modificaciones de asientos?
- ¿Qué debo hacer si el sistema no me permite modificar un asiento?
- ¿Cómo se manejan los errores al intentar completar la modificación de un asiento?
- ¿Dónde puedo encontrar más información sobre este módulo?

# Domain — data model

## Functional

El módulo se basa en la entidad cabecera 'ssmaact_accounting', que actúa como el núcleo para las modificaciones contables. No existen etapas adicionales, ya que el proceso se centra en la modificación directa de los asientos existentes. Las relaciones clave se mantienen entre los registros de contabilidad y las configuraciones de cuentas. Un trigger importante, 'SSMAACT_CONTROL_TRG', se activa para validar que las modificaciones no excedan un valor de 0.05 y que los asientos que se intentan borrar no estén vinculados a cuentas inapropiadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssmaact_accounting` |
| `ssmaact_audit` |
| `ssmaact_modify_acct` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssmaact_accounting` | Ssmaact_Accounting | `SSMAACT_CONTROL_TRG` | — | ad_org_id→ad_org; ad_orgtrx_id→ad_org; c_bpartner_id→c_bpartner; c_currency_id→c_currency; c_doctype_id→c_doctype (+22) | Detalle enlazado a ad_org, c_bpartner. Validado por trigger(s): SSMAACT_CONTROL_TRG. | PK `ssmaact_acct_key`; Cols: c_acctschema_id, account_id, datetrx, dateacct, c_period_id; `SSMAACT_ACCT_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); `SSMAACT_ACCT_ISMODIFY_CHECK`: ISMODIFY IN ('Y', 'N') |
| `ssmaact_audit` | Ssmaact_Audit | — | — | ad_org_id→ad_org; ad_orgtrx_id→ad_org; c_bpartner_id→c_bpartner; c_currency_id→c_currency; c_doctype_id→c_doctype (+22) | Detalle enlazado a ad_org, c_bpartner. | PK `ssmaact_audt_key`; Cols: c_acctschema_id, account_id, datetrx, dateacct, c_period_id; `SSMAACT_AUDT_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); `SSMAACT_AUDT_ISMODIFY_CHECK`: ISMODIFY IN ('Y', 'N') |
| `ssmaact_modify_acct` | Ssmaact_Modify_Acct | — | — | ad_client_id→ad_client; c_invoice_id→c_invoice; ad_org_id→ad_org; fin_payment_id→fin_payment | Detalle enlazado a ad_client, ad_org, c_invoice. | PK `ssmaact_modify_acct_key`; Cols: name, date, transaction, c_invoice_id, fin_payment_id; `SSMAACT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Ssmaact_Accounting` |
| `Ssmaact_Audit` |
| `Ssmaact_Modify_Acct` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El acceso al módulo se realiza a través de la ventana 'Modificar contabilidad', donde los usuarios pueden visualizar y gestionar los asientos contables. La interfaz permite una navegación sencilla entre los diferentes asientos, asegurando que los usuarios puedan realizar modificaciones de manera eficiente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.modify.accounting.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Modificar contabilidad | Modify accounting |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Modificar contabilidad | Modify accounting | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.modify.accounting.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Modificar contabilidad

- **AD_WINDOW_ID:** `D2B495DA0BD44182972765FFB47E469D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `9353E6A8C9024978A630FC5E2E4BCBEF` | 0 |
| 20 | Accounting | `CC841B8BDADD49159A0295899D83FF4A` | 1 |
| 30 | Audit | `FC8835C3D654430985F850A4E276E9EB` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Accounting (ventana: Modificar contabilidad)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | No | — |
| 140 | Credit | `Amtacctcr` | No | No | — |
| 150 | Description | `Description` | No | Sí | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |

### Audit (ventana: Modificar contabilidad)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | Sí | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |

### Header (ventana: Modificar contabilidad)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Date | `Date` | No | No | — |
| 50 | Transaction | `Transaction` | No | No | — |
| 60 | Invoice | `C_Invoice_ID` | No | No | — |
| 70 | Payment in/out | `FIN_Payment_ID` | No | No | — |
| 80 | Description | `Description` | No | No | — |
| 90 | Total debit | `Total_Dr` | No | Sí | — |
| 100 | Total credit | `Total_Cr` | No | Sí | — |
| 110 | Status | `Status` | No | Sí | — |
| 120 | Load seats | `Load_Seat` | No | No | — |
| 130 | Complete accouting modification | `Process` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo cuenta con dos botones de proceso: uno para completar modificaciones, 'ssmaact_complete', que verifica que los asientos modificados mantengan la coherencia en debe y haber respecto a los datos originales, y otro para retornar. Las validaciones frecuentes se centran en estas reglas de coherencia y en la restricción de modificaciones inadecuadas. Actualmente, no se generan informes específicos desde este módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.modify.accounting.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar asientos | Load seats | Ssmaact_load_seat | `ssmaact_load_seat` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Completar modificación de contabilidad | Complete accouting modification | Ssmaact_Complete | `ssmaact_complete` | Los asientos deben coincidir en debe y haber con relación a los datos originales. | — |
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
| Botón (PL/pgSQL) | Cargar asientos | Load seats | Ssmaact_load_seat | `ssmaact_load_seat` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Completar modificación de contabilidad | Complete accouting modification | Ssmaact_Complete | `ssmaact_complete` | Los asientos deben coincidir en debe y haber con relación a los datos originales. | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar asientos | Load seats | PL `ssmaact_load_seat` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Completar modificación de contabilidad | Complete accouting modification | PL `ssmaact_complete` | Los asientos deben coincidir en debe y haber con relación a los datos originales. | Los asientos deben coincidir en debe y haber con relación a los datos originales. |
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

No se incluye funcionalidad Java específica en este módulo, ya que no hay clases de Java relacionadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.modify.accounting`.

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
| Trigger `SSMAACT_CONTROL_TRG` | `ssmaact_accounting` | before UPDATE/DELETE | La modificación no puede ser mayor a 0.05; No se puede borrar un asiento con una cuenta que no esté configurada en el campo "Cuenta de asiento no cuadrado" en la pestaña "Contabilidad general" de la ventana "Esquema con… |
| AD_VAL_RULE | — | `Ssmaact_Payment_Val` | `fin_payment.fin_payment_ID IN (SELECT a.fin_payment_id FROM fin_payment a
INNER JOIN fact_acct b ON a.fin_payment_id = b` |
| AD_VAL_RULE | — | `Ssmaact_Invoice_Val` | `C_Invoice.C_Invoice_ID IN (SELECT a.c_invoice_id FROM c_invoice a
INNER JOIN fact_acct b ON a.c_invoice_id = b.record_id` |
| Función PL `ssmaact_complete` | — | invocación proceso | Los asientos deben coincidir en debe y haber con relación a los datos originales. |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL desempeñan un papel fundamental para garantizar la integridad de los datos. En particular, el trigger 'SSMAACT_CONTROL_TRG' es esencial para validar las reglas de modificación. Además, las funciones PL vinculadas a los botones de proceso aseguran que se realicen las comprobaciones necesarias antes de permitir cualquier cambio en los asientos contables.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSMAACT_CONTROL_TRG` | `ssmaact_accounting` | before | UPDATE/DELETE | La modificación no puede ser mayor a 0.05; No se puede borrar un asiento con una cuenta que no esté configurada en el campo "Cuenta de asiento no cuadrado" en la pestaña "Contabilidad general" de la ventana "Esquema con… | `model/triggers/SSMAACT_CONTROL_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssmaact_complete` | Completar modificación de contabilidad | Los asientos deben coincidir en debe y haber con relación a los datos originales. | Los asientos deben coincidir en debe y haber con relación a los datos originales. | `model/functions/SSMAACT_COMPLETE.xml` |
| `ssmaact_load_seat` | Cargar asientos | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSMAACT_LOAD_SEAT.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cargar asientos | `Ssmaact_load_seat` | Botón (PL/pgSQL) | PL `ssmaact_load_seat` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 2 | Completar modificación de contabilidad | `Ssmaact_Complete` | Botón (PL/pgSQL) | PL `ssmaact_complete` | N | Los asientos deben coincidir en debe y haber con relación a los datos originales. |

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

Módulo: `ec.com.sidesoft.modify.accounting`.

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

# Glosario — prefijo `SSMAACT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSMAACT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.modify.accounting` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Ssmaact_load_seat` — Cargar asientos
- `Ssmaact_Complete` — Completar modificación de contabilidad

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Accounting reverses
**Package:** `ec.com.sidesoft.transaction.reversal`

# Module overview — Accounting reverses

## Functional

El módulo 'Reversos Contables' permite la gestión de la reversión de transacciones contables en Openbravo. Está dirigido a usuarios de negocio que requieren revertir asientos contables por diversas razones, así como al soporte de nivel 2 que puede asistir en la resolución de problemas. El alcance de este módulo incluye la capacidad de seleccionar múltiples transacciones para revertir y la creación de registros de reversión asociados. La dependencia principal es del núcleo de Openbravo y del framework Openbravo 3.0.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/transaction/reversal` |
| Web | `web/ec.com.sidesoft.transaction.reversal/` |

### Declared dependencies

- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`STXREV`

# Guía de chat — Accounting reverses

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.transaction.reversal`).

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
- «¿Qué es la tabla stxrev_acct?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo revertir un asiento contable específico?
- ¿Qué debo hacer si no puedo encontrar una transacción para revertir?
- ¿Puedo revertir varias transacciones a la vez?
- ¿Qué pasa si una reversión falla?
- ¿Cómo puedo verificar que una transacción ha sido revertida correctamente?
- ¿Dónde puedo encontrar registro de las reversas que he realizado?
- ¿Hay algún límite en el número de transacciones que puedo revertir?
- ¿Qué tipo de validaciones se realizan antes de proceder con una reversión?

# Domain — data model

## Functional

La entidad principal de este módulo es la tabla 'stxrev_acct', que almacena información relacionada con las transacciones contables que se van a revertir. Aunque no hay etapas de proceso claramente definidas, el flujo implica seleccionar transacciones y ejecutar acciones para crear registros de reversión. Las relaciones principales incluyen la conexión entre transacciones contables y sus respectivas entradas en la tabla de reversión. Este módulo no contiene triggers, pero tiene una función PL que maneja la lógica de reversión.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `stxrev_acct` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `stxrev_acct` | STXREV_FinanciallAccounting | — | — | a_asset_id→a_asset; account_id→c_elementvalue; ad_client_id→ad_client; ad_table_id→ad_table; c_acctschema_id→c_acctschema (+21) | Detalle enlazado a a_asset, ad_client, c_elementvalue. | PK `stxrev_acct_key`; Cols: c_acctschema_id, account_id, datetrx, dateacct, c_period_id; `STXREV_ACCT_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); `STXREV_ACCT_ISMODIFY_CHECK`: ISMODIFY IN ('Y', 'N'); idx `STXREV_ACCT_ACCOUNT` (ad_org_id, c_acctschema_id, account_id); idx `STXREV_ACCT_BPARTNER` (c_bpartner_id) (+2) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `STXREV_FinanciallAccounting` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de la ventana 'Reversed Accounting Data', donde los usuarios pueden visualizar y seleccionar las transacciones contables que desean revertir. Dentro de esta ventana, se facilita la gestión de las entradas contables mediante listas y filtros que permiten a los usuarios encontrar rápidamente las transacciones necesarias.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Reversed Accounting Data | Reversed Accounting Data |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Reversed Accounting Data | Reversed Accounting Data | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

<!-- knowledge-extract:window_specs -->
### Ventana: Reversed Accounting Data

- **AD_WINDOW_ID:** `81A77B200731458AB851C54ADCA3A20E`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Accounting | `228DB2AB6FB347F4964E6D6527AF74F0` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 360 | Sequence Number | `Seqno` | No | Sí | — |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 360 | Sequence Number | `Seqno` | No | Sí | — |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Contabilidad

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

### Accounting

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

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 360 | Sequence Number | `Seqno` | No | Sí | — |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 360 | Sequence Number | `Seqno` | No | Sí | — |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 360 | Sequence Number | `Seqno` | No | Sí | — |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 360 | Sequence Number | `Seqno` | No | Sí | — |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Accounting (ventana: Reversed Accounting Data)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Transaction Date | `Datetrx` | No | Sí | 402880E72F1C15A5012F1C7AA98B00E8 |
| 190 | Quantity | `Qty` | No | Sí | 402880E72F1C15A5012F1C7AA98B00E8 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 200 | UOM | `C_Uom_ID` | No | Sí | 402880E72F1C15A5012F1C7AA98B00E8 |
| 210 | Storage Bin | `M_Locator_ID` | No | Sí | 402880E72F1C15A5012F1C7AA98B00E8 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 230 | Foreign Currency Debit | `Amtsourcedr` | No | Sí | 402880E72F1C15A5012F1C7AA98B00E8 |
| 240 | Foreign Currency Credit | `Amtsourcecr` | No | Sí | 402880E72F1C15A5012F1C7AA98B00E8 |
| 360 | Sequence Number | `Seqno` | No | Sí | — |
| 2010 | Period | `C_Period_ID` | No | Sí | 800000 |
| 2020 | Project | `C_Project_ID` | No | Sí | 800000 |
| 2050 | Sales Region | `C_Salesregion_ID` | No | Sí | 800000 |
| 2060 | Sales Campaign | `C_Campaign_ID` | No | Sí | 800000 |
| 2070 | Activity | `C_Activity_ID` | No | Sí | 800000 |
| 2080 | Reverse | `STXREV_Isreversal` | No | Sí | — |

### Reversed Accounting

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | Sí | — |
| 70 | Currency | `C_Currency_ID` | No | Sí | — |
| 80 | Period | `C_Period_ID` | No | Sí | — |
| 90 | Accounting Date | `Dateacct` | No | Sí | — |
| 100 | Account | `Account_ID` | No | Sí | — |
| 130 | Debit | `Amtacctdr` | No | Sí | — |
| 140 | Credit | `Amtacctcr` | No | Sí | — |
| 150 | Description | `Description` | No | No | — |
| 160 | Business Partner | `C_Bpartner_ID` | No | Sí | 800000 |
| 170 | Product | `M_Product_ID` | No | Sí | 800000 |
| 180 | Project | `C_Project_ID` | No | Sí | 800000 |
| 190 | Cost Center | `C_Costcenter_ID` | No | Sí | 800000 |
| 200 | Asset | `A_Asset_ID` | No | Sí | 800000 |
| 210 | 1st Dimension | `User1_ID` | No | Sí | 800000 |
| 220 | 2nd Dimension | `User2_ID` | No | Sí | 800000 |
| 360 | Sequence Number | `Seqno` | No | Sí | — |
| 470 | Reverse | `STXREV_Isreversal` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos en este módulo se centran en la ejecución de la función PL que maneja la reversión de transacciones. Aunque no hay botones de proceso específicos, los usuarios interactúan con el sistema a través de acciones en la ventana principal. No se generan informes en este módulo, pero es crucial validar las transacciones seleccionadas antes de proceder con la reversión, asegurando que cumplan con los criterios necesarios para su reversión.

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

El módulo contiene una clase Java llamada 'ReversosContableUtils' que es responsable de realizar operaciones como la selección de transacciones a revertir y la creación de registros de reversión en la base de datos. Esta clase juega un papel fundamental en la lógica de inversión, operando bajo el contexto de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.transaction.reversal`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ReversosContableUtils` | root | — | — | `src/ec/com/sidesoft/transaction/reversal/ReversosContableUtils.java` |
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

Los triggers no están presentes en este módulo, pero existe una función PL que se encarga de la lógica para revertir las transacciones contables. Esta función permite el manejo eficiente de las operaciones en la base de datos, asegurando que las reversas se realicen de manera correcta y que se mantenga la integridad de los registros contables en el sistema.

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
| `stxrev_get_documentno` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/STXREV_GET_DOCUMENTNO.xml` |
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

Módulo: `ec.com.sidesoft.transaction.reversal`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | presente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | no |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `STXREV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `STXREV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.transaction.reversal` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Mass loading of data into accounting entries
**Package:** `ec.com.sidesoft.loaddata.into.accounting.entries`

# Module overview — Mass loading of data into accounting entries

## Functional

El módulo 'Mass loading of data into accounting entries' está diseñado para facilitar el proceso de carga masiva de datos en la ventana de entradas contables manuales. Su propósito es optimizar la introducción de datos, permitiendo a los usuarios cargar múltiples registros de manera eficiente. Los actores principales incluyen usuarios de negocio que realizan la carga de datos contables y el equipo de soporte técnico que maneja las configuraciones y problemas relacionados con el módulo. El alcance de este módulo se limita a la carga de datos en el sistema contable, y depende de compatibilidades con la piel de versiones específicas y del core de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/loaddata/into/accounting/entries` |
| Web | `web/ec.com.sidesoft.loaddata.into.accounting.entries/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLIAE`

# Guía de chat — Mass loading of data into accounting entries

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.loaddata.into.accounting.entries`).

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

- ¿Cómo puedo cargar múltiples entradas contables al mismo tiempo?
- ¿Qué formato debe tener el archivo que subo para la carga masiva?
- ¿Cómo puedo verificar si mis entradas han sido correctamente cargadas?
- ¿Qué debo hacer si ocurre un error durante la carga de datos?
- ¿Cómo se manejan los diferentes tipos de cuentas durante la carga masiva?
- ¿Puedo cargar datos de diferentes períodos contables en un único archivo?
- ¿Hay alguna validación que deba considerar antes de cargar los datos?
- ¿Dónde puedo encontrar ayuda si tengo problemas con el módulo?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad cabecera GL_JOURNAL, que representa las entradas contables y su correspondiente detalle. No se definen etapas complejas en este módulo ya que la función principal es la carga masiva de entradas, por lo que la relación con otras entidades es menor pero crítica. Esta entidad GL_JOURNAL se beneficia de la carga masiva a través de un proceso que aseguran la correcta inserción y validación de datos. Al no haber triggers definidos, se rely on validaciones posteriores para asegurar la integridad de los datos en el sistema.

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

`GL_JOURNAL`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo está diseñado para una navegación sencilla, aunque no hay ventanas específicas expuestas para uso por parte del usuario. La carga de datos se realiza a través de un botón de proceso que activa la ejecución del procesamiento del archivo con las entradas contables. Esto indica que la interacción principal del usuario se centra en proporcionar el archivo de datos correcto para iniciar la carga, sin interacciones complejas en múltiples ventanas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.loaddata.into.accounting.entries.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.loaddata.into.accounting.entries.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `160`

- **AD_TAB_ID:** `160` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2080 | Cargar Archivo | `EM_Sliae_Loadacct` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso principal incluye un botón que permite a los usuarios completar la carga de datos desde un archivo. Este botón ejecuta la función de cargar los datos en la entidad GL_JOURNAL, manejando errores y validaciones de manera interna. En términos de informes, el módulo no proporciona informes específicos pero depende de registros internos para cambios realizados. Las validaciones frecuentes incluirán chequear el formato del archivo y la existencia previa de entradas antes de la carga.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.loaddata.into.accounting.entries.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar Archivo | Cargar Archivo | Cargar Archivo | Java `ProcessFileManualEntries` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `GL_Journal_ID`, El archivo CSV no tiene el número correcto de columnas (9).; Existe más de un archivo CSV en adjuntos. | `src/ec/com/sidesoft/loaddata/into/accounting/entries/ad_process/ProcessFileManualEntries.java` |
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
| Botón (Java) | Cargar Archivo | `ProcessFileManualEntries` | Proceso Java (toolbar/background) | `GL_Journal_ID` | El archivo CSV no tiene el número correcto de columnas (9).; Existe más de un archivo CSV en adjuntos. | `src/ec/com/sidesoft/loaddata/into/accounting/entries/ad_process/ProcessFileManualEntries.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar Archivo | Cargar Archivo | Cargar Archivo | Java `ProcessFileManualEntries` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `GL_Journal_ID`, El archivo CSV no tiene el número correcto de columnas (9).; Existe más de un archivo CSV en adjuntos. | `src/ec/com/sidesoft/loaddata/into/accounting/entries/ad_process/ProcessFileManualEntries.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar Archivo | Cargar Archivo | Java `ProcessFileManualEntries` | Proceso Openbravo registro `GL_Journal_ID`, El archivo CSV no tiene el número correcto de columnas (9).; Existe más de un archivo CSV en adjuntos. | El archivo CSV no tiene el número correcto de columnas (9).; Existe más de un archivo CSV en adjuntos. |
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

El módulo incluye una clase Java principal, 'ProcessFileManualEntries', que gestiona la lógica de carga de datos desde un archivo CSV a la tabla GL_JOURNAL. Esta clase implica un procesamiento en fondo que verifica, valida y carga los datos necesarios en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.loaddata.into.accounting.entries`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ProcessFileManualEntries` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/loaddata/into/accounting/entries/ad_process/ProcessFileManualEntries.java` |
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

Los triggers y funciones PL no están presentes en este módulo, pero el soporte se logra a través de procesos Java que se encargan de la carga de datos. Esto asegura que, aunque no haya triggers, las acciones de carga se manejen de manera efectiva y fiable mediante la lógica del negocio implementada en el backend.

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
| 1 | Cargar Archivo | `Cargar Archivo` | Botón (Java) | Java `ProcessFileManualEntries` | N | Proceso Openbravo registro `GL_Journal_ID`, El archivo CSV no tiene el número correcto de columnas (9).; Existe más de un archivo CSV en adjuntos. |

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

Módulo: `ec.com.sidesoft.loaddata.into.accounting.entries`.

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

# Glosario — prefijo `SLIAE`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLIAE` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.loaddata.into.accounting.entries` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Cargar Archivo` — Cargar Archivo

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Amount Validation
**Package:** `ec.com.sidesoft.amount.validation`

# Module overview — Sidesoft Amount Validation

## Functional

El módulo Sidesoft Amount Validation tiene como propósito principal evitar la facturación de montos en cero, promoviendo la integridad de los datos en las transacciones comerciales. Los actores principales incluyen a los usuarios de negocio responsables de la facturación y al equipo de soporte técnico que se encarga de la implementación y mantenimiento del módulo. Este módulo es compatible con versiones de Openbravo desde 2.50 a 3.00, lo que asegura su integración con las versiones actuales del sistema ERP. Las dependencias clave para su funcionamiento son el Core de Openbravo y el framework de Openbravo 3.0.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/amount/validation` |
| Web | `web/ec.com.sidesoft.amount.validation/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSCAV`

# Guía de chat — Sidesoft Amount Validation

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.amount.validation`).

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

- ¿Cómo puedo asegurarme de que no se facture en cero?
- ¿Qué debo hacer si el sistema me permite facturar en cero?
- ¿Cuál es el proceso para instalar el módulo de validación?
- ¿Cómo afecta este módulo a mis procesos de facturación actuales?
- ¿Qué sucede si un monto en cero se registra antes de la instalación?
- ¿A quién debo contactar si encuentro un error en la validación?
- ¿Cómo se actualiza el módulo en futuras versiones de Openbravo?
- ¿Qué dependencias debo considerar antes de la implementación?

# Domain — data model

## Functional

El módulo no define entidades adicionales ni tablas físicas, operando en el contexto de validaciones en las funciones de facturación existentes. Sin embargo, el componente incluye una función PL que se activa durante el proceso de facturación, permitiendo la validación de los montos para prevenir registros en cero. El entorno de trabajo para esta función es el de facturas, donde se interrelacionan distintos datos financieros que permiten la correcta ejecución de las validaciones necesarias durante las transacciones.

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

El módulo no añade nuevas ventanas ni menús dentro de la interfaz de usuario, lo que significa que las validaciones se aplican en los procesos existentes de facturación sin requerir navegación adicional por parte del usuario. Las validaciones se ejecutan en segundo plano durante los procesos de facturación estándar disponibles en Openbravo.

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
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El uso de botones típicos como 'Completar' se mantiene en la interfaz de facturación, donde la función de validación se aplica automáticamente al tratar de registrar una factura. Esta función valida los montos ingresados y asegura que ningún monto cero sea permitido. Aunque no se generan informes adicionales desde este módulo, las validaciones frecuentes se centran en controlar los datos de facturación y asegurar que se cumplan las normativas internas.

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

No se incluyen clases Java específicas en este módulo, por lo que el funcionamiento se basa completamente en funcionalidades de procedimiento y la lógica planificada en las funciones PL integradas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.amount.validation`.

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

El rol de las funciones PL en este módulo es fundamental, ya que dictan la lógica necesaria para llevar a cabo las validaciones sin necesidad de modificar la estructura de la base de datos. Estas funciones son invocadas en el proceso de facturación y ayudan a garantizar la calidad de los datos a través de validaciones programadas.

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
| `sscav_amount_validation_inv` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSCAV_AMOUNT_VALIDATION_INV.xml` |
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

Módulo: `ec.com.sidesoft.amount.validation`.

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

# Glosario — prefijo `SSCAV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCAV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.amount.validation` | Carpeta del módulo en el repositorio |

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
## Not Posted Transaction Report
**Package:** `ec.com.sidesoft.localization.report.notposted`

# Module overview — Not Posted Transaction Report

## Functional

El informe de transacciones no contabilizadas tiene como propósito identificar y listar las transacciones y/o documentos que están en estado 'Completado' pero que no han sido contabilizados en el sistema. Este informe es relevante para los usuarios de negocio que necesitan asegurar que todas las transacciones han sido registradas adecuadamente. Los principales actores incluyen los usuarios del departamento contable y los administradores del sistema. El alcance del informe abarca todas las transacciones en el sistema Openbravo desde la versión 2.50 hasta la 3.00, y depende de la compatibilidad con los cambios de la piel del sistema y del marco de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/report/notposted` |
| Web | `web/ec.com.sidesoft.localization.report.notposted/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`CSLRNP`

# Guía de chat — Not Posted Transaction Report

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.report.notposted`).

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
- «¿Qué es la tabla cslrnp_data_notposted?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo acceder al informe de transacciones no contabilizadas?
- ¿Qué criterios puedo usar para filtrar las transacciones en el informe?
- ¿Qué información se incluye en el informe de transacciones no contabilizadas?
- ¿Cómo puedo corregir un error en una transacción que aparece en el informe?
- ¿Puedo exportar el informe a otros formatos?
- ¿Qué debo hacer si no veo ninguna transacción en el informe?
- ¿Hay algún límite en el número de transacciones que puedo consultar?
- ¿Este informe se actualiza en tiempo real o hay algún retardo?

# Domain — data model

## Functional

El modelo de datos se basa en la tabla cslrnp_data_notposted, que contiene la información relevante de las transacciones clasificadas como no contabilizadas. Aunque no hay etapas intermedias definidas, el flujo de los datos se inicia con la recopilación de información de transacciones, seguida de la generación del informe que muestra estas transacciones. Las relaciones más importantes están entre esta tabla principal y otras entidades relacionadas con las transacciones y su estado. No se han definido triggers específicos para el informe, pero se utilizan funciones PL para consultar y procesar los datos necesarios para la visualización.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `cslrnp_data_notposted` |
| `cslrnp_sql_trx_notposted` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `cslrnp_data_notposted` | cslrnp_data_notposted | — | — | tab_id→ad_tab; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, ad_tab. | PK `cslrnp_dnp_key`; Cols: documentno, dateacct, tablename, cbpid, grandtotal; idx `CSLRNP_DATA_NOTPOSTED_IDX1` (processid) |
| `cslrnp_sql_trx_notposted` | cslrnp_sql_trx_notposted | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `cslrnp_sql_tntp_key`; Cols: name, script, description; `CSLRNP_SQL_TNTP_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `cslrnp_data_notposted` |
| `cslrnp_sql_trx_notposted` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación en el módulo de informe de transacciones no contabilizadas se realiza a través de una única ventana llamada 'Script Transacciones no contabilizadas'. Desde esta ventana, el usuario puede acceder a la información del informe y, si bien no hay botones específicos para la ejecución, la interacción principal se lleva a cabo a través de la selección de fechas y parámetros para generar el informe.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.report.notposted.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Script Transacciones no contabilizadas | Script Transactions Not Posted |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Documentos no contabilizados | Not Posted Transaction Report | No |
| Script Transacciones no contabilizadas | Script Transactions Not Posted | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.report.notposted.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Script Transacciones no contabilizadas

- **AD_WINDOW_ID:** `9FC6493E43D743C29A976A345F9FDA4F`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Script Transactions Not Posted | `E50D5C28B42548229DCB40A7159CBA92` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Script Transactions Not Posted (ventana: Script Transacciones no contabilizadas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Name | `Name` | No | No | — |
| 30 | Script | `Script` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso implicado en el informe se centra en la generación del mismo, donde se especifican fechas de inicio y fin para filtrar las transacciones. Los informes son generados al ejecutar el comando correspondiente, que puede incluir validaciones comunes, como asegurarse de que las fechas de entrada sean coherentes. Este informe permite a los usuarios obtener una visión clara de la situación de las transacciones no contabilizadas, facilitando la toma de decisiones en el proceso contable.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.report.notposted.es_ES/referencedata/translation/`.

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
| Reporte | Documentos no contabilizados | Not Posted Transaction Report | CslrnpReportNotPosted | Java `CslrnpReportNotPosted` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/localization/report/notposted/ad_reports/CslrnpReportNotPosted.java` |
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
| Reporte | Documentos no contabilizados | `CslrnpReportNotPosted` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/localization/report/notposted/ad_reports/CslrnpReportNotPosted.java` |
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
| Reporte | Documentos no contabilizados | Not Posted Transaction Report | CslrnpReportNotPosted | Java `CslrnpReportNotPosted` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/localization/report/notposted/ad_reports/CslrnpReportNotPosted.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 1**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **1**; archivos `*.jrxml` en el repo = **0**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Documentos no contabilizados | `CslrnpReportNotPosted` | Java `CslrnpReportNotPosted`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Not Posted Transaction Report |
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

El módulo cuenta con una clase Java llamada CslrnpReportNotPosted, que gestiona las solicitudes del navegador y la generación del informe de transacciones no contabilizadas, permitiendo la interacción directa con los usuarios a través de un servlet.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.report.notposted`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `CslrnpReportNotPosted` | ad_reports | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/localization/report/notposted/ad_reports/CslrnpReportNotPosted.java` |
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

En la base de datos, las funciones PL desempeñan un papel fundamental en la consulta de datos relacionados con las transacciones no contabilizadas. Aunque no hay triggers asociados a la tabla principal, las funciones permiten obtener datos relevantes de manera eficiente, apoyando a los usuarios y al soporte técnico en situaciones de análisis o problemas de contabilización.

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
| `cslrnp_execute_sql` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/CSLRNP_EXECUTE_SQL.xml` |
| `cslrnp_execute_sql2` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/CSLRNP_EXECUTE_SQL2.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Documentos no contabilizados | `CslrnpReportNotPosted` | Reporte | Java `CslrnpReportNotPosted` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |

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

Módulo: `ec.com.sidesoft.localization.report.notposted`.

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

# Glosario — prefijo `CSLRNP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `CSLRNP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.report.notposted` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `CslrnpReportNotPosted` — Documentos no contabilizados

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Balance Report
**Package:** `ec.com.sidesoft.finances.custom.balancereports`

# Module overview — Balance Report

## Functional

El módulo 'Balance Report' tiene como propósito facilitar la generación de informes de estados financieros para los usuarios de negocio. Actores clave incluyen contadores y analistas financieros que requieren información precisa sobre la situación económica de la empresa. Este módulo es parte del ecosistema Openbravo y depende de core y la compatibilidad con la skin de versiones 2.50 a 3.00. Su alcance abarca la configuración de scripts necesarios para la elaboración de reportes financieros integrales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/finances/custom/balancereports` |
| Web | `web/ec.com.sidesoft.finances.custom.balancereports/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SFCBR`

# Guía de chat — Balance Report

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.finances.custom.balancereports`).

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
- «¿Qué es la tabla sfcbr_conf_res_intg?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo configuro un nuevo script para el reporte?
- ¿Qué datos necesito para generar un estado financiero?
- ¿Puedo usar un centro de costo que no aparece en la lista?
- ¿Dónde encuentro la configuración del reporte integral?
- ¿Cómo retorno un reporte que no fue aceptado?
- ¿Qué funciones PL debo conocer para validar mis datos?
- ¿Cómo puedo acceder a la información de períodos financieros?
- ¿Hay algún requisito especial para utilizar este módulo?

# Domain — data model

## Functional

El modelo de datos del módulo se basa principalmente en la tabla de cabecera 'sfcbr_conf_res_intg', que almacena configuraciones relacionadas con los reportes financieros. Aunque no se han definido etapas intermedias, las relaciones entre las tablas modificadas como 'C_COSTCENTER' y 'C_ELEMENTVALUE' son fundamentales para el correcto funcionamiento de las consultas y reportes. No hay triggers específicos para este módulo, pero las funciones PL son clave para las validaciones de los datos antes de la generación de los informes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sfcbr_conf_res_intg` |
| `sfcbr_inc_statmnt_script` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sfcbr_conf_res_intg` | sfcbr_conf_res_intg | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sfcbr_key`; Cols: line, value, name, amount, description; `SFCBR_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfcbr_inc_statmnt_script` | sfcbr_inc_statmnt_script | — | — | ad_org_id→ad_org; ad_client_id→ad_client | Detalle enlazado a ad_client, ad_org. | PK `sfcbr_incst_script_key`; Cols: rep_sequence, name, rep_group, rep_sql, description; `SFCBR_INCST_S_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sfcbr_conf_res_intg` |
| `sfcbr_inc_statmnt_script` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_MONTH`, `AD_MONTH_TRL`, `AD_ORG`, `AD_TREENODE`, `C_COSTCENTER`, `C_ELEMENTVALUE`, `C_PERIOD`, `C_VALIDCOMBINATION`, `FACT_ACCT`

### Views

`SFCBR_TREE_ACOUNTING_V`

# Functional — windows and menus

## Functional

El módulo se navega a través de dos ventanas principales: 'Configuración de Scripts - Reporte de Estados Financieros' y 'Setup Integral Results'. Estas ventanas permiten a los usuarios configurar los scripts y resultados necesarios para la elaboración de los informes financieros, así como acceder a las configuraciones relevantes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.finances.custom.balancereports.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuración de Scripts - Reporte de Estados Financieros | Setup Scripts Report Comprehensive Income Statement |
| Setup Integral Results | Setup Integral Results |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Balance de Comprobación | Balance Checking | No |
| Balance de Resultado Acumulado | Balance of result | No |
| Balance de Resultado por Centro de Costo | Balance of result by Center Cost | No |
| Balance general por proyectos | Balance Sheet for Projects | No |
| Configuración de Resultados Integrales | Setup Integral Results | No |
| Configuración de Scripts - Reporte de Estados Financieros | Setup Scripts Report Comprehensive Income Statement | No |
| Estado de Resultados Integrales | Comprehensive Income Statement | No |
| Estado de situación Financiera | Balance Sheet | No |
| Reporte - Resultados por Período | Balance of Result by Period | No |
| Reporte - Situación por Período | Balance Sheet by Period | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.finances.custom.balancereports.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuración de Scripts - Reporte de Estados Financieros

- **AD_WINDOW_ID:** `76A275569D5E413D99448C00D4ACB980`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Setup Scripts Report Comprehensive Income Statement | `045E1A0E53AD4E618E6CEF6C60ACA754` | 0 |

### Ventana: Setup Integral Results

- **AD_WINDOW_ID:** `6859AD9CF4C1436DB8FABD5135B05222`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Setup Integral Results | `44999823587A4FA1AAF9FA381F1CD660` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Setup Scripts Report Comprehensive Income Statement (ventana: Configuración de Scripts - Reporte de Estados Financieros)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Line No. | `REP_Sequence` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Sql | `REP_Sql` | No | No | — |
| 60 | Total Groups | `REP_Group` | No | No | — |
| 70 | Account | `SQL_Account` | No | No | — |
| 80 | Description | `Description` | No | No | — |
| 90 | Type Header | `Typeheader` | No | No | — |

### Pestaña `143`

- **AD_TAB_ID:** `143` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 300 | Responsible Signature Balance 1 | `EM_Sfcbr_Balance_Sign_1` | No | No | — |
| 310 | Responsible Signature Balance 2 | `EM_Sfcbr_Balance_Sign_2` | No | No | — |

### Setup Integral Results (ventana: Setup Integral Results)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Line No. | `Line` | No | No | — |
| 40 | Code | `Value` | No | No | — |
| 50 | Account name | `Name` | No | No | — |
| 60 | Amount | `Amount` | No | No | — |
| 70 | Description | `Description` | No | No | — |
| 110 | Title | `Istitle` | No | No | — |
| 120 | Active | `Isactive` | No | No | — |
| 130 | Year | `C_Year_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos disponibles en el módulo incluyen botones como completar, retornar y rechazar, que permiten a los usuarios manejar el flujo de trabajo en la generación de informes. A pesar de la ausencia de informes explícitos dentro del módulo, las validaciones frecuentes están relacionadas con la correcta configuración de los elementos y centros de costo, utilizando dos funciones PL para realizar validaciones clave y asegurar la integridad de los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.finances.custom.balancereports.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Balance de Comprobación | Balance Checking | Balance Checking | *(OBUIAPP / manual)* | Balance Checking | — |
| Proceso / otro | Balance de Resultado Acumulado | Balance of result | Balance of result | *(OBUIAPP / manual)* | Balance of result | — |
| Proceso / otro | Balance de Resultado por Centro de Costo | Balance of result by Center Cost | Balance of result by Center Cost | *(OBUIAPP / manual)* | Balance of result by Center Cost | — |
| Proceso / otro | Balance de Resultados por Período | Balance of Result by Period | Balance of Result by Period | *(OBUIAPP / manual)* | Balance of Result by Period | — |
| Proceso / otro | Balance de Situación Acumulado | Balance Sheet | Balance Sheet | *(OBUIAPP / manual)* | Balance Sheet | — |
| Proceso / otro | Balance de Situación por Período | Balance Sheet by Period | Balance Sheet by Period | *(OBUIAPP / manual)* | Balance Sheet by Period | — |
| Proceso / otro | Balance general por proyectos | Balance Sheet for Projects | Balance Sheet for Projects | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado de Resultados Integrales | Comprehensive Income Statement | Comprehensive Income Statement | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Balance de Comprobación | Balance Checking | Balance Checking | *(OBUIAPP / manual)* | Balance Checking | — |
| Proceso / otro | Balance de Resultado Acumulado | Balance of result | Balance of result | *(OBUIAPP / manual)* | Balance of result | — |
| Proceso / otro | Balance de Resultado por Centro de Costo | Balance of result by Center Cost | Balance of result by Center Cost | *(OBUIAPP / manual)* | Balance of result by Center Cost | — |
| Proceso / otro | Balance de Resultados por Período | Balance of Result by Period | Balance of Result by Period | *(OBUIAPP / manual)* | Balance of Result by Period | — |
| Proceso / otro | Balance de Situación Acumulado | Balance Sheet | Balance Sheet | *(OBUIAPP / manual)* | Balance Sheet | — |
| Proceso / otro | Balance de Situación por Período | Balance Sheet by Period | Balance Sheet by Period | *(OBUIAPP / manual)* | Balance Sheet by Period | — |
| Proceso / otro | Balance general por proyectos | Balance Sheet for Projects | Balance Sheet for Projects | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado de Resultados Integrales | Comprehensive Income Statement | Comprehensive Income Statement | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Balance de Comprobación | Balance Checking | — | Balance Checking | — |
| Proceso / otro | Balance de Resultado Acumulado | Balance of result | — | Balance of result | — |
| Proceso / otro | Balance de Resultado por Centro de Costo | Balance of result by Center Cost | — | Balance of result by Center Cost | — |
| Proceso / otro | Balance de Resultados por Período | Balance of Result by Period | — | Balance of Result by Period | — |
| Proceso / otro | Balance de Situación Acumulado | Balance Sheet | — | Balance Sheet | — |
| Proceso / otro | Balance de Situación por Período | Balance Sheet by Period | — | Balance Sheet by Period | — |
| Proceso / otro | Balance general por proyectos | Balance Sheet for Projects | — | — | — |
| Proceso / otro | Estado de Resultados Integrales | Comprehensive Income Statement | — | — | — |
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
**Total de reportes del módulo: 15**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **15**.

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

No se han definido clases Java específicas para este módulo, lo que sugiere que la lógica está implementada mayormente a través de funciones SQL y PL.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.finances.custom.balancereports`.

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
| AD_VAL_RULE | — | `SFCBR_ValidateElementValue` | `C_ELEMENTVALUE.ELEMENTLEVEL in ('E','D','C')` |
| AD_VAL_RULE | — | `Sfcbr_IsEmployee` | `C_BPartner.IsEmployee = 'Y' and C_BPartner.IsActive = 'Y'` |
| AD_VAL_RULE | — | `Sfcbr_Validationuser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

En el contexto de la base de datos, las funciones PL juegan un rol crucial al permitir ejecutar lógica adicional necesaria para el procesamiento de datos y la generación de reportes. Integran las interacciones con las tablas físicas y aseguran que los datos sean precisos y válidos antes de que los informes sean generados.

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
| `sfcbr_get_sqlgroup` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SFCBR_GET_SQLGROUP.xml` |
| `sfcbr_getsignaturedata` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SFCBR_GETSIGNATUREDATA.xml` |
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

Módulo: `ec.com.sidesoft.finances.custom.balancereports`.

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

# Glosario — prefijo `SFCBR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SFCBR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.finances.custom.balancereports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Balance Checking` — Balance de Comprobación
- `Balance of result` — Balance de Resultado Acumulado
- `Balance of result by Center Cost` — Balance de Resultado por Centro de Costo
- `Balance of Result by Period` — Balance de Resultados por Período
- `Balance Sheet` — Balance de Situación Acumulado
- `Balance Sheet by Period` — Balance de Situación por Período
- `Balance Sheet for Projects` — Balance general por proyectos
- `Comprehensive Income Statement` — Estado de Resultados Integrales

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Finance Reports
**Package:** `ec.com.sidesoft.localization.finance.reports`

# Module overview — Finance Reports

## Functional

El módulo Finance Reports proporciona herramientas para la generación de informes financieros clave para las organizaciones, asegurando que los usuarios puedan acceder a datos financieros críticos de manera ágil y precisa. Los actores principales son usuarios de negocio que requieren informes financieros, así como desarrolladores y personal de soporte que mantienen y personalizan el módulo. Este módulo depende de las funcionalidades básicas del núcleo de Openbravo y del framework Openbravo 3.0, siendo esencial para la correcta ejecución y visualización de los informes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/finance/reports` |
| Web | `web/ec.com.sidesoft.localization.finance.reports/` |

### Declared dependencies

- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLOREP`

# Guía de chat — Finance Reports

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.finance.reports`).

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

- ¿Cómo puedo generar un informe financiero en el módulo?
- ¿Qué datos necesito para visualizar un informe específico?
- ¿Qué debo hacer si encuentro un error en el informe generado?
- ¿Es posible personalizar los informes financieros según mis requisitos?
- ¿Cómo se aseguran la precisión y la integridad de los datos en los informes?
- ¿Hay opciones de filtrado avanzadas disponibles al generar informes?
- ¿Qué tipo de datos puedo incluir en mis informes financieros?
- ¿A dónde debo dirigirme para solicitar soporte técnico sobre el módulo?

# Domain — data model

## Functional

Aunque el módulo no cuenta con tablas físicas como tal, su diseño se basa en estructuras de datos que permiten la agrupación de información financiera esencial a partir de criterios establecidos. Los informes generados utilizan criterios transversales y permiten conectar entidades clave como los socios de negocio y las organizaciones, facilitando la extracción de datos relevantes. La ausencia de triggers y funciones PL específicas en este módulo sugiere que la lógica de negocio es mayormente manejada a través de la clase Java principal, optimizando el proceso de generación de informes.

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

Dado que el inventario indica que no hay ventanas específicas definidas para este módulo, los usuarios navegan a través del sistema Openbravo utilizando el menú principal y accediendo a las secciones relacionadas con informes financieros en el marco del ERP. A través de esta interfaz, pueden ejecutar los informes que les interesen directamente desde la opción correspondiente.

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
| Statement of CXC Accounting Balances | Statement of CXC Accounting Balances | No |
| Statement of CXP - Accounting Balances | Statement of CXP - Accounting Balances | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo Finance Reports carece de procesos formales como botones de completar, retornar o rechazar, enfocándose en la generación y visualización de informes. Las validaciones se hacen típicamente a través de la lógica contenida en la clase Java, que asegura que los parámetros necesarios están presentes antes de ejecutar la lógica de generación de informes. Informes temporales se podrían obtener si los criterios de búsqueda se definen adecuadamente al invocar la funcionalidad adecuada desde el sistema.

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

La funcionalidad Java del módulo es crítica, ya que la clase FinanceReports extiende BaseReportActionHandler para gestionar la lógica de ejecución de informes. Esta clase maneja la recepción de parámetros desde la interfaz y la construcción de los informes en formato JSON, asegurando que se produzcan resultados adecuados y ajustados a las necesidades del usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.finance.reports`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `FinanceReports` | root | BaseReportActionHandler | Proceso / informe Java | `src/ec/com/sidesoft/localization/finance/reports/FinanceReports.java` |
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

Este módulo no utiliza triggers o funciones PL en la base de datos, pero está diseñado para interactuar con estas mediante la lógica en Java. Esto permite que el soporte L2 gestione la generación de informes sin la necesidad de modificar elementos a nivel de base de datos, manteniendo la coherencia y la integridad de las funcionalidades del sistema.

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
| `web/ec.com.sidesoft.localization.finance.reports/jasper/Invoice.jrxml` |
| `web/ec.com.sidesoft.localization.finance.reports/jasper/InvoiceSCXSL.jrxml` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.localization.finance.reports`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | ausente |
| `AD_WINDOW.xml` | ausente |
| `OBUIAPP_PROCESS.xml` | presente |
| Traducción `.es_ES` | no |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SLOREP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLOREP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.finance.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Balance customization for big data volume
**Package:** `ec.com.sidesoft.balance.performance`

# Module overview — Sidesoft Balance customization for big data volume

## Functional

El módulo Sidesoft Balance permite la personalización del balance para manejar grandes volúmenes de datos. Su propósito es optimizar la presentación y cálculo de sumas y saldos resumidos, facilitando a los usuarios finalizar reportes contables de forma eficiente. El módulo está diseñado para ser utilizado por usuarios de negocio, además de facilitar el soporte L2 en caso de incidencias y servir como base para desarrolladores que desean realizar personalizaciones adicionales. Dependencias clave incluyen el módulo Core de Openbravo, que proporciona la funcionalidad básica necesaria para el funcionamiento del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/balance/performance` |
| Web | `web/ec.com.sidesoft.balance.performance/` |

### Declared dependencies

- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SBPRF`

# Guía de chat — Sidesoft Balance customization for big data volume

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.balance.performance`).

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
- «¿Qué es la tabla sbprf_fact_acct_aggd_doc?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo acceder al balance de sumas y saldos resumido?
- ¿Qué debo hacer si deseo modificar un balance ya creado?
- ¿Cuáles son las validaciones que se aplican al ingresar datos en el balance?
- ¿Cómo puedo utilizar los botones de completar, retornar y rechazar?
- ¿Qué información se muestra en la ventana del balance de sumas y saldos?
- ¿Existen informes disponibles dentro del módulo de balance?
- ¿Qué pasos debo seguir para realizar un cierre contable?
- ¿A quién debo contactar si tengo problemas con la agregación de datos?

# Domain — data model

## Functional

El módulo se basa principalmente en la entidad cabecera 'fact_acct', que almacena las transacciones contables y permite su agregación para el análisis. Las tablas involucradas son la 'sbprf_fact_acct_aggd_doc' como tabla ancla, que ayuda a conectar las transacciones a los documentos relevantes. Dos triggers clave, 'SBPRF_AGGREGATE_DOC_TRG' y 'SBPRF_AGGREGATE_TRG', se ejecutan sobre tabla 'fact_acct' para asegurar la correcta agregación de datos de acuerdo a las reglas definidas en la rutina PL/pgSQL, garantizando así la integridad y optimización de los procesos de balance.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sbprf_fact_acct_aggd` |
| `sbprf_fact_acct_aggd_doc` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sbprf_fact_acct_aggd` | sbprf_fact_acct_aggd | — | — | ad_org_id→ad_org; c_currency_id→c_currency; c_project_id→c_project; c_salesregion_id→c_salesregion; account_id→c_elementvalue (+8) | Detalle enlazado a ad_org, c_currency, c_project. | PK `sbprf_fact_acct_aggd_key`; Cols: c_acctschema_id, account_id, dateacct, c_period_id, c_currency_id; `FACT_ACCT_ISACTIVE_CHECK_AGGD`: ISACTIVE IN ('Y', 'N'); idx `SBPRF_FACT_ACCT_ACCOUNT_AGGD` (ad_org_id, c_acctschema_id, account_id, c_period_id, c_currency_id, c_salesregion_id, c_project_id, c_campaign_id, c_activity_id, user1_id, user2_id, factaccttype); idx `SBPRF_FACT_ACCT_DATEACCT` (dateacct) (+1) |
| `sbprf_fact_acct_aggd_doc` | sbprf_fact_acct_aggd_doc | — | — | ad_org_id→ad_org; c_currency_id→c_currency; c_doctype_id→c_doctype; c_project_id→c_project; c_salesregion_id→c_salesregion (+10) | Detalle enlazado a ad_org, c_currency, c_doctype. | PK `sbprf_fact_acct_aggd_doc_key`; Cols: c_acctschema_id, account_id, dateacct, c_period_id, c_currency_id; `FACT_ACCT_ACTIVE_CHK_AGGD_DOC`: ISACTIVE IN ('Y', 'N'); idx `SBPRF_FACT_ACCT_DOC_ACCT_AGGD` (ad_org_id, c_acctschema_id, account_id, c_period_id, c_currency_id, c_salesregion_id, c_project_id, c_campaign_id, c_activity_id, user1_id, user2_id, factaccttype, description, c_doctype_id, ad_table_id, record_id); idx `SBPRF_FACT_ACCT_DOC_DATEACCT` (dateacct) (+1) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sbprf_fact_acct_aggd` |
| `sbprf_fact_acct_aggd_doc` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`FACT_ACCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo cuenta con una ventana principal denominada 'Balance de sumas y saldos resumido', que permite a los usuarios navegar a través de los diferentes reportes de balance. La interfaz está diseñada para facilitar la visualización de las sumas y saldos de manera clara y concisa, y permite un acceso fácil a las funcionalidades dentro del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.balance.performance.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Balance de sumas y saldos resumido | Trial Balance Summarized |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Balance de sumas y saldos resumido | Trial Balance Summarized | No |
| Balances resumidos | Summarized balances | Sí |
| Resumen - Balance de resultados acumulado | Summary - Balance of result | No |
| Resumen - Balance de resultados por período | Summary - Balance of result by period | No |
| Resumen - Balance de situación acumulado | Summary - Balance sheet | No |
| Resumen - Balance de situación por período | Summary - Balance sheet by period | No |
| Resumen - Balance de sumas y saldos | Summary - Balance | No |
| Resumen - Libro mayor | Summary - General ledger | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.balance.performance.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Balance de sumas y saldos resumido

- **AD_WINDOW_ID:** `5DC6F3B714B3441583F345DED8E328AE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `3909AFF013414C5A8CAD3AE031CF4EA4` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Header (ventana: Balance de sumas y saldos resumido)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | General Ledger | `C_Acctschema_ID` | No | No | — |
| 40 | Account | `Account_ID` | No | No | — |
| 50 | Accounting Date | `Dateacct` | No | No | — |
| 60 | Period | `C_Period_ID` | No | No | — |
| 70 | Currency | `C_Currency_ID` | No | No | — |
| 80 | Foreign Currency Debit | `Amtsourcedr` | No | No | — |
| 90 | Foreign Currency Credit | `Amtsourcecr` | No | No | — |
| 100 | Debit | `Amtacctdr` | No | No | — |
| 110 | Credit | `Amtacctcr` | No | No | — |
| 120 | Sales Region | `C_Salesregion_ID` | No | No | — |
| 130 | Project | `C_Project_ID` | No | No | — |
| 140 | Sales Campaign | `C_Campaign_ID` | No | No | — |
| 150 | Activity | `C_Activity_ID` | No | No | — |
| 160 | 1st Dimension | `User1_ID` | No | No | — |
| 170 | 2nd Dimension | `User2_ID` | No | No | — |
| 180 | Cost Center | `C_Costcenter_ID` | No | No | — |
| 190 | Type | `Factaccttype` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los principales botones disponibles incluyen 'Completar', 'Retornar' y 'Rechazar', que permiten gestionar el flujo de trabajo en la elaboración del balance. Aunque no se incluyen informes, el módulo tiene capacidades para realizar cierres contables y validaciones frecuentes que garantizan que los datos ingresados cumplen con las normativas establecidas. Cada una de estas acciones es crítica para asegurar el manejo correcto de la información contable dentro del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.balance.performance.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Resumen - Balance de resultados acumulado | Summary - Balance of result | Summary - Balance of result | *(OBUIAPP / manual)* | Summary - Balance of result | — |
| Proceso / otro | Resumen - Balance de resultados por período | Summary - Balance of result by period | Summary - Balance of result by period | *(OBUIAPP / manual)* | Summary - Balance of result by period | — |
| Proceso / otro | Resumen - Balance de situación acumulado | Summary - Balance sheet | Summary - Balance sheet | *(OBUIAPP / manual)* | Summary - Balance sheet | — |
| Proceso / otro | Resumen - Balance de situación por período | Summary - Balance sheet by period | Summary - Balance sheet by period | *(OBUIAPP / manual)* | Summary - Balance sheet by period | — |
| Proceso / otro | Resumen - Balance de sumas y saldos | Summary - Balance | Summary - Balance | *(OBUIAPP / manual)* | Summary - Balance | — |
| Proceso / otro | Resumen - Libro mayor | Summary - General ledger | Summary - General ledger | *(OBUIAPP / manual)* | Summary - General ledger | — |
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
| Proceso / otro | Resumen - Balance de resultados acumulado | Summary - Balance of result | Summary - Balance of result | *(OBUIAPP / manual)* | Summary - Balance of result | — |
| Proceso / otro | Resumen - Balance de resultados por período | Summary - Balance of result by period | Summary - Balance of result by period | *(OBUIAPP / manual)* | Summary - Balance of result by period | — |
| Proceso / otro | Resumen - Balance de situación acumulado | Summary - Balance sheet | Summary - Balance sheet | *(OBUIAPP / manual)* | Summary - Balance sheet | — |
| Proceso / otro | Resumen - Balance de situación por período | Summary - Balance sheet by period | Summary - Balance sheet by period | *(OBUIAPP / manual)* | Summary - Balance sheet by period | — |
| Proceso / otro | Resumen - Balance de sumas y saldos | Summary - Balance | Summary - Balance | *(OBUIAPP / manual)* | Summary - Balance | — |
| Proceso / otro | Resumen - Libro mayor | Summary - General ledger | Summary - General ledger | *(OBUIAPP / manual)* | Summary - General ledger | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Resumen - Balance de resultados acumulado | Summary - Balance of result | — | Summary - Balance of result | — |
| Proceso / otro | Resumen - Balance de resultados por período | Summary - Balance of result by period | — | Summary - Balance of result by period | — |
| Proceso / otro | Resumen - Balance de situación acumulado | Summary - Balance sheet | — | Summary - Balance sheet | — |
| Proceso / otro | Resumen - Balance de situación por período | Summary - Balance sheet by period | — | Summary - Balance sheet by period | — |
| Proceso / otro | Resumen - Balance de sumas y saldos | Summary - Balance | — | Summary - Balance | — |
| Proceso / otro | Resumen - Libro mayor | Summary - General ledger | — | Summary - General ledger | — |
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

No se utiliza Java en este módulo, por lo que no hay clases asociadas que requieran una descripción especial.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.balance.performance`.

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
| Trigger `SBPRF_AGGREGATE_DOC_TRG` | `fact_acct` | before INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SBPRF_AGGREGATE_TRG` | `fact_acct` | before INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Sbprf_SessionUser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Present Client` | `AD_Client.AD_Client_ID=@#AD_Client_ID@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers en el módulo desempeñan un rol fundamental al permitir que las transacciones se agreguen y se mantengan actualizadas automáticamente dentro de la tabla 'fact_acct'. La función PL vinculada a estos triggers asegura que las operaciones se realicen de manera eficiente, optimizando el rendimiento del manejo de datos en el ERP. Esto es especialmente importante en entornos con grandes volúmenes de datos, donde la espera por la actualización de balances podría afectar el flujo del negocio.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SBPRF_AGGREGATE_DOC_TRG` | `fact_acct` | before | INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SBPRF_AGGREGATE_DOC_TRG.xml` |
| `SBPRF_AGGREGATE_TRG` | `fact_acct` | before | INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SBPRF_AGGREGATE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sbprf_get_documentno` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SBPRF_GET_DOCUMENTNO.xml` |
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

Módulo: `ec.com.sidesoft.balance.performance`.

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

# Glosario — prefijo `SBPRF`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SBPRF` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.balance.performance` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Summary - Balance of result` — Resumen - Balance de resultados acumulado
- `Summary - Balance of result by period` — Resumen - Balance de resultados por período
- `Summary - Balance sheet` — Resumen - Balance de situación acumulado
- `Summary - Balance sheet by period` — Resumen - Balance de situación por período
- `Summary - Balance` — Resumen - Balance de sumas y saldos
- `Summary - General ledger` — Resumen - Libro mayor

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
