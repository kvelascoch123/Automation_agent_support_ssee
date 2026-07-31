# Openbravo Sidesoft — Compras

> Pedidos de compra, facturas de compra, albaranes de entrada, aprobaciones, anulación de órdenes, carga automática, proveedores, listas de precios.

**Paquetes incluidos (9):**
- `ec.com.sidesoft.account.purchase` — Sidesoft Account Purchase
- `ec.com.sidesoft.automatic.load.purchase` — Automatic load purchase data
- `ec.com.sidesoft.custom.orderpurchase.voidtrx` — Customization to Enable Void button on the Purchase Order
- `ec.com.sidesoft.purchase.inout.data` — Sidesoft Purchase Inout Importa Data
- `ec.com.sidesoft.purchase.need.approval` — Sidesoft Need Approval
- `ec.com.sidesoft.pending.purchase.invoice` — Sidesoft Pending Purchase Invoice
- `ec.com.sidesoft.imports.pricelist` — Sidesoft Process of Importing Price List
- `ec.com.sidesoft.load.orders` — Sidesoft Load Orders
- `ec.com.sidesoft.localization.ecuador.resupply` — Resupply


---
## Sidesoft Account Purchase
**Package:** `ec.com.sidesoft.account.purchase`

# Module overview — Sidesoft Account Purchase

## Functional

El módulo 'Sidesoft Account Purchase' tiene como propósito gestionar las compras realizadas en el sistema Openbravo, integrando la contabilidad y el manejo de facturas. Actores principales incluyen usuarios de negocio que ejecutan compras, así como desarrolladores que mantienen y expanden la funcionalidad del módulo. El alcance abarca la gestión de documentos de compra y su contabilización, interactuando con módulos de finanzas y contabilidad. Las dependencias clave incluyen la compatibilidad con la '3.00 Compatibility Skin', el módulo core de Openbravo y el framework de Openbravo 3.0.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/account/purchase` |
| Web | `web/ec.com.sidesoft.account.purchase/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SACCPS`

# Guía de chat — Sidesoft Account Purchase

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.account.purchase`).

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

- ¿Cómo puedo registrar una nueva compra en el sistema?
- ¿Qué pasos debo seguir para contabilizar una factura de compra?
- ¿Hay alguna validación automática al crear una factura?
- ¿Puedo modificar una compra una vez registrada?
- ¿Cómo visualizo el estado de mis facturas de compra?
- ¿Qué debo hacer si encuentro un error en una factura registrada?
- ¿Existen informes que me muestren las compras realizadas?
- ¿Cómo afecta la contabilización de una compra en mis estados financieros?

# Domain — data model

## Functional

El modelo de datos del módulo se basa principalmente en la entidad cabecera relacionada con las facturas de compra. Se espera que exista un flujo que pase por etapas como la creación y validación de documentos de compra. Aunque el inventario no especifica disparadores (triggers) ni funciones, es común que se implementen validaciones automáticas para asegurar la integridad de los datos en estas etapas.

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

El módulo no cuenta con ventanas específicas documentadas en el inventario, pero la navegación se espera que sea intuitiva, siguiendo la estructura típica de Openbravo donde los usuarios pueden acceder a las funcionalidades relacionadas a través de menús y opciones disponibles dentro del sistema.

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

Dentro del módulo se pueden esperar procesos típicos asociados a la contabilización de documentos, aunque no se detallan botones específicos en el inventario. Sin embargo, es usual que existan botones de acción como 'Completar', 'Retornar' o 'Rechazar', los cuales permiten a los usuarios gestionar el flujo de compras. Informes y validaciones pueden ser requeridos para asegurar el correcto registro contable de las transacciones.

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

El módulo incluye una clase Java, 'DocInvoice', que parece jugar un papel crítico en la gestión de documentos de compra. Esta clase maneja la lógica necesaria para el tratamiento de las facturas dentro del sistema, integrando la funcionalidad de contabilidad y asegurando que las operaciones sean realizadas de acuerdo a las reglas del negocio.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.account.purchase`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `DocInvoice` | accounting | DocInvoiceTemplate | — | `src/ec/com/sidesoft/account/purchase/accounting/DocInvoice.java` |
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

A través del módulo, si bien no se mencionan triggers específicos, se puede inferir que podrían existir funciones PL para proporcionar apoyo a la lógica de contabilización y gestión de compras. Estas funciones son cruciales para el soporte y mantenimiento del sistema, asegurando que las operaciones se ejecuten correctamente en la base de datos.

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

Módulo: `ec.com.sidesoft.account.purchase`.

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

# Glosario — prefijo `SACCPS`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SACCPS` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.account.purchase` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Automatic load purchase data
**Package:** `ec.com.sidesoft.automatic.load.purchase`

# Module overview — Automatic load purchase data

## Functional

El módulo 'Carga automática de datos de compra' permite la consulta de información fiscal desde los servicios del SRI (Servicio de Rentas Internas) al ingresar la clave de acceso electrónica de una factura de compra. Este proceso está diseñado para facilitar a los usuarios la validación de facturas mediante la carga automática de datos relevantes de terceros y sus transacciones, mejorando la eficacia en la gestión contable. Los actores principales son el usuario de negocio que requiere verificar la información de facturas y los administradores que configuran y mantienen el sistema. El alcance del módulo incluye la consulta de datos de facturas de compra y puede depender de la correcta parametrización en la organización contable.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/automatic/load/purchase` |
| Web | `web/ec.com.sidesoft.automatic.load.purchase/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSALP`

# Guía de chat — Automatic load purchase data

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.automatic.load.purchase`).

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

- ¿Cómo puedo consultar la información de una factura específica?
- ¿Qué debo hacer si la clave de autorización de la factura es incorrecta?
- ¿Dónde configuro la organización contable para usar este módulo?
- ¿Cómo sé si estoy en el entorno de prueba o en producción?
- ¿Qué datos se cargan automáticamente desde el SRI?
- ¿Existen limitaciones en el número de facturas que puedo consultar?
- ¿Qué sucede si no tengo acceso al servicio del SRI?
- ¿Cómo puedo validar que los datos cargados son correctos?

# Domain — data model

## Functional

La entidad cabecera principal está relacionada con la organización contable, la cual debe estar activa para utilizar las funcionalidades del módulo. La etapa de consulta comienza con el ingreso de la clave de acceso de la factura, permitiendo a los usuarios obtener los datos del SRI. Las relaciones se establecen a través de las organizaciones que tienen configurados los parámetros necesarios para interactuar con los servicios SRI, incluido el manejo de URLs para entornos de prueba y producción. Aunque no se destacan triggers o funciones específicas debido a que no se han definido, la funcionalidad está respaldada por aspectos de validación y acceso a datos mediante Java.

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

`AD_ORG`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no presenta ventanas específicas, y su integración se realiza a través de una función de llamada en Java que se invoca desde el interfaz del ERP para obtener la información necesaria. Esto asegura una experiencia de usuario ágil, donde las consultas se realizan de forma directa desde la aplicación, sin necesidad de acceder a múltiples pantallas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.automatic.load.purchase.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.automatic.load.purchase.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `143`

- **AD_TAB_ID:** `143` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 640 | Environment | `EM_Ssalp_Environment` | No | No | B6D2A898EA394E9098B5BFE5A36C7E79 |
| 650 | URL authorization test | `EM_Ssalp_Url_Autho_Test` | No | No | B6D2A898EA394E9098B5BFE5A36C7E79 |
| 660 | URL authorization production | `EM_Ssalp_Url_Autho_Prod` | No | No | B6D2A898EA394E9098B5BFE5A36C7E79 |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo carece de procesos explícitos como botones para completar, retornar o rechazar, lo cual sugiere que su operación es más directa y se basa en la ejecución de consultas. Sin embargo, se requiere que los usuarios ingresen correctamente la clave de autorización para proceder con la consulta. Tiene mecanismos de validación que aseguran que se ingresen datos correctos antes de realizar la consulta a los servicios SRI.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.automatic.load.purchase.es_ES/referencedata/translation/`.

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

El módulo incluye una clase Java, 'UpdatePurchaseData', que contiene la lógica para gestionar la consulta de datos de compra a través de servicios externos, asegurando así la validación de facturas antes de su procesamiento contable.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.automatic.load.purchase`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `UpdatePurchaseData` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/automatic/load/purchase/ad_callouts/UpdatePurchaseData.java` |
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

No se han definido triggers ni funciones PL en este módulo, lo que implica que el soporte operativo se basa más en las funciones Java implementadas. Esto permite manejar interacciones de manera programática, asegurando que las consultas y la recuperación de datos del SRI se realicen con la lógica adecuada para validaciones y controles.

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

Módulo: `ec.com.sidesoft.automatic.load.purchase`.

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

# Glosario — prefijo `SSALP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSALP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.automatic.load.purchase` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Customization to Enable Void button on the Purchase Order
**Package:** `ec.com.sidesoft.custom.orderpurchase.voidtrx`

# Module overview — Customization to Enable Void button on the Purchase Order

## Functional

El módulo 'Customization to Enable Void button on the Purchase Order' tiene como propósito habilitar la funcionalidad de anular pedidos de compra en Openbravo. Este módulo es relevante para los usuarios de negocio que manejan la gestión de compras, así como para el equipo de soporte L2 y desarrolladores que necesitan comprender la implementación técnica. El alcance del módulo incluye la modificación de la entidad de pedidos de compra a fin de permitir una opción de anulación. Las dependencias principales son el núcleo de Openbravo y el marco de Openbravo 3.0, lo que garantiza la compatibilidad con la infraestructura básica del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/orderpurchase/voidtrx` |
| Web | `web/ec.com.sidesoft.custom.orderpurchase.voidtrx/` |

### Declared dependencies

- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`CSCOPV`

# Guía de chat — Customization to Enable Void button on the Purchase Order

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.orderpurchase.voidtrx`).

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

- ¿Cómo puedo anular un pedido de compra?
- ¿Qué sucede si trato de anular un pedido ya enviado?
- ¿Puedo revertir la anulación de un pedido de compra?
- ¿Qué permisos necesito para anular un pedido?
- ¿La anulación del pedido afecta a otros pedidos relacionados?
- ¿Recibiré una notificación una vez que se haya anulado el pedido?
- ¿Cómo puedo verificar el estado de un pedido anulado?
- ¿Hay criterios específicos para qué pedidos puedo anular?

# Domain — data model

## Functional

La entidad cabecera del módulo está relacionada con la tabla 'C_ORDER', que almacena la información sobre los pedidos de compra. El módulo no introduce nuevas etapas, pero modifica un proceso existente al agregar un botón de anulación a los pedidos. Este botón está vinculado a una función PL que se activa para realizar la acción de anulación. Aunque no se definen triggers específicos en el módulo, la integración con la lógica existente de la tabla 'C_ORDER' permite que las operaciones se realicen con eficacia, manteniendo la integridad de los datos.

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

El módulo no introduce nuevas ventanas en la interfaz de usuario, sin embargo, la funcionalidad de anulación se integra en las ventanas existentes de la gestión de pedidos de compra. Los usuarios pueden navegar hacia la sección de pedidos de compra y acceder a los registros para ver el nuevo botón de anulación disponible al editar un pedido, lo que simplifica el flujo de trabajo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.orderpurchase.voidtrx.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.orderpurchase.voidtrx.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `186`

- **AD_TAB_ID:** `186` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2170 | Void Order Sales | `EM_Cscopv_Void` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso que permite a los usuarios completar la acción de anular un pedido de compra. Típicamente, los usuarios pueden interactuar con este proceso a través de un botón que ejecuta la funcionalidad de anulación cuando se activa. Como parte de este flujo, las validaciones se llevan a cabo para asegurar que solo los estados de pedidos permitidos puedan ser anulados. No se generan informes específicos dado que el enfoque está en la funcionalidad de anulación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.orderpurchase.voidtrx.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Anular pedido de venta | Void Order Sales | VoidOrderSales | `cscopv_void_order` | update c_order set docstatus='VO' where c_order_id = p_Record_ID;; p_Invoice_ID := 0; -- Error Indicator | — |
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
| Botón (PL/pgSQL) | Anular pedido de venta | Void Order Sales | VoidOrderSales | `cscopv_void_order` | update c_order set docstatus='VO' where c_order_id = p_Record_ID;; p_Invoice_ID := 0; -- Error Indicator | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Anular pedido de venta | Void Order Sales | PL `cscopv_void_order` | update c_order set docstatus='VO' where c_order_id = p_Record_ID;; p_Invoice_ID := 0; -- Error Indicator | update c_order set docstatus='VO' where c_order_id = p_Record_ID;; p_Invoice_ID := 0;        --  Error Indicator |
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

Este módulo no incluye implementaciones Java, ya que su enfoque está exclusivamente en la personalización del almacenamiento de datos y la funcionalidad del proceso mediante PL.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.orderpurchase.voidtrx`.

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
| Función PL `cscopv_void_order` | — | invocación proceso | update c_order set docstatus='VO' where c_order_id = p_Record_ID;; p_Invoice_ID := 0;        --  Error Indicator |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El rol de la función PL en este módulo es crucial para el soporte operativo, ya que maneja la lógica necesaria detrás de la anulación de pedidos. Esta función garantiza que todos los pasos necesarios se sigan correctamente para mantener la integridad de los datos en la tabla 'C_ORDER'.

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
| `cscopv_void_order` | Anular pedido de venta | update c_order set docstatus='VO' where c_order_id = p_Record_ID;; p_Invoice_ID := 0; -- Error Indicator | update c_order set docstatus='VO' where c_order_id = p_Record_ID;; p_Invoice_ID := 0;        --  Error Indicator | `model/functions/CSCOPV_VOID_ORDER.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Anular pedido de venta | `VoidOrderSales` | Botón (PL/pgSQL) | PL `cscopv_void_order` | N | update c_order set docstatus='VO' where c_order_id = p_Record_ID;; p_Invoice_ID := 0; -- Error Indicator |

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

Módulo: `ec.com.sidesoft.custom.orderpurchase.voidtrx`.

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

# Glosario — prefijo `CSCOPV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `CSCOPV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.orderpurchase.voidtrx` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `VoidOrderSales` — Anular pedido de venta

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Purchase Inout Importa Data
**Package:** `ec.com.sidesoft.purchase.inout.data`

# Module overview — Sidesoft Purchase Inout Importa Data

## Functional

El módulo 'Sidesoft Purchase Inout Importa Data' tiene como propósito facilitar la importación de datos relacionados con albaranes de proveedores en el sistema Openbravo. Está diseñado para ser utilizado por equipos de compras y administración que necesitan cargar masivamente líneas de productos asociadas a órdenes de compra. Este módulo es especialmente útil para mejorar la eficiencia en la carga de datos y reducir errores manuales al procesar múltiples entradas de productos. Presenta dependencias con el '2.50 to 3.00 Compatibility Skin', lo que significa que requiere esta compatibilidad para su funcionamiento óptimo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/purchase/inout/data` |
| Web | `web/ec.com.sidesoft.purchase.inout.data/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPIIMP`

# Guía de chat — Sidesoft Purchase Inout Importa Data

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.purchase.inout.data`).

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

- ¿Cómo puedo importar líneas de productos desde un albarán de proveedor?
- ¿Qué validaciones se realizan al cargar datos de albaranes?
- ¿Cómo puedo verificar si mis datos han sido importados correctamente?
- ¿Qué debo hacer si hay un error en la carga de un albarán?
- ¿Dónde encuentro el registro de las importaciones realizadas?
- ¿Es posible realizar una carga masiva de datos de varios albaranes?
- ¿Qué pasos debo seguir después de importar un albarán?
- ¿Hay algún límite en la cantidad de líneas que se pueden importar a la vez?

# Domain — data model

## Functional

El módulo no define tablas físicas o modelos complejos, ya que se basa en clases Java que manejan la importación de líneas de productos provenientes de albaranes y órdenes. Las entidades clave involucradas son las relacionadas con 'Order' y 'OrderLine', las cuales permiten la gestión de pedidos y sus correspondientes líneas de producto. Aunque no se especifican triggers o funciones PL, el Procesos de Java permite validar y crear líneas de órdenes en el sistema al procesar datos de albaranes, garantizando así la integridad de los datos importados.

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

Dado que el módulo no define ventanas específicas ni un menú visible en la interfaz de usuario, se asume que la interacción se gestiona a través de los procesos Java centralizados. Estos procesos se activan a través del código backend, y los usuarios deben acceder a ellos mediante la ejecución de scripts específicos o acciones programadas.

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

La importación de datos se realiza a través de procesos que permiten completar la carga de líneas de productos. No se especifican botones o informes estándar dentro del módulo, pero la estructura de los procesos sugiere que se podrían implementar informes de carga o validaciones de datos como parte de una revisión posterior. La validación frecuente incluye comprobaciones de formato y existencia de campos requeridos en las entradas donde se comparan valores con definiciones en la base de datos.

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

Las clases Java, específicamente 'ImportLinesOrders' e 'ImportProductLines', contienen la lógica necesaria para la validación y creación de líneas de órdenes y productos en el sistema. Estas clases implementan procesos de importación documentados con métodos para la validación de parámetros y la gestión de datos importados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.purchase.inout.data`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ImportLinesOrders` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/purchase/inout/data/ad_process/ImportLinesOrders.java` |
| `ImportProductLines` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/purchase/inout/data/ad_process/ImportProductLines.java` |
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

En el contexto del módulo, los triggers y las funciones PL juegan un rol indirecto, ya que no se definen explícitamente dentro del inventario. Sin embargo, el uso de clases Java sugiere que la validación y procesamiento de datos se llevan a cabo dentro de una lógica que interactúa con la base de datos a través del acceso a modelos y la lógica de persistencia de Openbravo.

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

Módulo: `ec.com.sidesoft.purchase.inout.data`.

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

# Glosario — prefijo `SPIIMP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPIIMP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.purchase.inout.data` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Need Approval
**Package:** `ec.com.sidesoft.purchase.need.approval`

# Module overview — Sidesoft Need Approval

## Functional

El módulo Sidesoft Need Approval tiene como propósito gestionar el proceso de aprobación de necesidades de material dentro de la plataforma Openbravo. Está destinado a usuarios de negocio que gestionan requisiciones y a equipos de soporte que brindan asistencia en la utilización del sistema. El alcance incluye la aprobación de requisiciones de material y su integración con el flujo de compras. Dependencias clave del módulo incluyen la compatibilidad con la skin de 2.50 a 3.00, el núcleo de Openbravo y el framework de Openbravo 3.0.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/purchase/need/approval` |
| Web | `web/ec.com.sidesoft.purchase.need.approval/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SINNAPP`

# Guía de chat — Sidesoft Need Approval

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.purchase.need.approval`).

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

- ¿Cómo puedo iniciar el proceso de aprobación de una requisición?
- ¿Qué debo hacer si necesito rechazar una requisición?
- ¿Qué información debo proporcionar al aprobar una requisición?
- ¿Cómo puedo ver el estado de una requisición que he aprobado?
- ¿Hay algún informe sobre las requisiciones pendientes de aprobación?
- ¿Qué sucede si hay un error en la requisición aprobada?
- ¿Quiénes son los responsables de aprobar requisiciones en el sistema?
- ¿Cómo se relacionan las requisiciones aprobadas con el proceso de compras?

# Domain — data model

## Functional

La entidad principal es la requisición de material (M_REQUISITION), que se modifica para incluir el proceso de aprobación. Además, el módulo altera la tabla de roles (AD_ROLE) para gestionar permisos de aprobación. La relación principal es entre los usuarios que crean requisiciones y los responsables de aprobarlas. La falta de triggers indica que las validaciones y procesos se manejan a través de una función PL enlazada, garantizando que se sigan los requisitos del flujo de aprobación.

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

`AD_ROLE`, `M_REQUISITION`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no incluye ventanas específicas en la interfaz de usuario, lo que sugiere que se integra de manera transparente en el flujo de trabajo de requisiciones existente. Los usuarios pueden acceder a la funcionalidad de aprobación a través de los procesos vinculados a la requisición de material.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.purchase.need.approval.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.purchase.need.approval.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `119`

- **AD_TAB_ID:** `119` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 210 | Material Need Manager | `EM_Sinnapp_Is_Mn_Manager` | No | No | — |

### Pestaña `800249`

- **AD_TAB_ID:** `800249` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 140 | Approve Need | `EM_Sinnapp_Approve_Need` | No | No | — |
| 150 | EM_Sinnapp_Approvedby | `EM_Sinnapp_Approvedby` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo contiene un único proceso de aprobación de requisiciones que se activa mediante un botón específico para completar o rechazar la necesidad de material. Aunque no incluye informes específicos, es esencial que haya validaciones integradas para asegurar que sólo las requisiciones correctas sean aprobadas. Este proceso está diseñado para facilitar la colaboración entre los usuarios que realizan pedidos y los que los aprueban.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.purchase.need.approval.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Aprobar Necesidad | Approve Need | Approve Need | `sinnapp_approve_need` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| Botón (PL/pgSQL) | Aprobar Necesidad | Approve Need | Approve Need | `sinnapp_approve_need` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Aprobar Necesidad | Approve Need | PL `sinnapp_approve_need` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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

No se identifican clases Java específicas en este módulo, lo que sugiere que toda la lógica de negocio está gestionada a través de funciones PL en lugar de interacciones en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.purchase.need.approval`.

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

Los triggers son inexistentes, lo que implica que el módulo depende en gran medida de la función PL para manejar la lógica de negocio relacionada con el proceso de aprobación. Esta función asegura que el flujo de trabajo se ejecute conforme a las reglas establecidas, facilitando así el soporte a usuarios y operadores del sistema.

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
| `sinnapp_approve_need` | Aprobar Necesidad | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SINNAPP_APPROVE_NEED.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Aprobar Necesidad | `Approve Need` | Botón (PL/pgSQL) | PL `sinnapp_approve_need` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

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

Módulo: `ec.com.sidesoft.purchase.need.approval`.

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

# Glosario — prefijo `SINNAPP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SINNAPP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.purchase.need.approval` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Approve Need` — Aprobar Necesidad

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Pending Purchase Invoice
**Package:** `ec.com.sidesoft.pending.purchase.invoice`

# Module overview — Sidesoft Pending Purchase Invoice

## Functional

El módulo Sidesoft Pending Purchase Invoice tiene como propósito gestionar las facturas de compras pendientes en Openbravo. Es utilizado por los usuarios de negocio para visualizar y gestionar el estado de las facturas y los pagos asociados, así como por el soporte L2 y desarrolladores para extender y dar mantenimiento al módulo. El alcance de este módulo incluye la configuración de propuestas de pago y el resumen de pagos pendientes. Se basa en el framework Openbravo 3.0 y tiene dependencias que incluyen compatibilidad con skins y funciones básicas de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/pending/purchase/invoice` |
| Web | `web/ec.com.sidesoft.pending.purchase.invoice/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPPINV`

# Guía de chat — Sidesoft Pending Purchase Invoice

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.pending.purchase.invoice`).

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
- «¿Qué es la tabla ssppinv_setting?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo configuro una propuesta de pago?
- ¿Dónde puedo ver el resumen de mis pagos pendientes?
- ¿Qué debo hacer si el monto a pagar es mayor que el monto pendiente?
- ¿Cómo selecciono varias facturas para una propuesta de pago?
- ¿Qué información se necesita para registrar una factura pendiente?
- ¿Existen reportes asociados a las propuestas de pago?
- ¿Qué errores comunes debo evitar al gestionar las facturas pendientes?
- ¿Cómo puedo acceder a ayuda adicional o documentación sobre el módulo?

# Domain — data model

## Functional

La entidad cabecera del modelo de datos del módulo es 'ssppinv_setting', la cual almacena configuraciones relacionadas con las facturas de compra. No se presentan tablas de etapa ni relaciones complejas, ya que el enfoque de este módulo es más funcional y orientado a la gestión de datos específicos de las facturas. Las funciones clave en el modelo involucran la validación de monto a través de triggers y una llamada a funciones PL que generan propuestas de pago basadas en facturas seleccionadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssppinv_selectedinvoices` |
| `ssppinv_setting` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssppinv_selectedinvoices` | ssppinv_selectedinvoices | — | — | c_invoice_id→c_invoice; ad_client_id→ad_client; c_bpartner_id→c_bpartner; ad_org_id→ad_org | Detalle enlazado a ad_client, c_bpartner, c_invoice. | PK `ssppinv_si_key`; Cols: c_invoice_id, c_bpartner_id, grandtotal, totalpaid, outstandingamt; `SSPPINV_SI_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssppinv_setting` | ssppinv_setting | — | — | c_currency_id→c_currency; ad_client_id→ad_client; c_doctype_id→c_doctype; fin_financial_account_id→fin_financial_account; ad_org_id→ad_org (+2) | Parametrización / catálogo de soporte. | PK `ssppinv_setting_key`; Cols: c_doctype_id, fin_financial_account_id, fin_paymentmethod_id, c_currency_id, payment_doctype_id; `SSPPINV_SETTING_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssppinv_selectedinvoices` |
| `ssppinv_setting` |
| `ssppinv_summary` |
| `ssppinv_summary2_v` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

`SSPPINV_SUMMARY`, `SSPPINV_SUMMARY2_V`

# Functional — windows and menus

## Functional

El módulo se navega a través de dos ventanas principales: 'Configuración de Propuesta de Pago' y 'Resumen de Pagos Pendientes'. En estas ventanas, los usuarios pueden acceder a distintos tabs para gestionar y visualizar la información relacionada con las facturas de compra pendientes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.pending.purchase.invoice.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuración de Propuesta de Pago | Proposed Payment Configuration |
| Resumen de Pagos Pendientes | Summary of Pending Payments |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración de Propuesta de Pago | Proposed Payment Configuration | No |
| Resumen de Pagos Pendientes | Summary of Pending Payments | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.pending.purchase.invoice.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuración de Propuesta de Pago

- **AD_WINDOW_ID:** `1E155C7EC8E947CA966665F7B758FE46`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Proposed Payment Configuration | `BDE4987B39E64FC986A5450F01BA87C0` | 0 |

### Ventana: Resumen de Pagos Pendientes

- **AD_WINDOW_ID:** `5CDE9A4F3E704405B4AA546B28C7C618`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Summary of Pending Payments | `3AB1FCD952CD45519D58B1A51FD53D39` | 0 |
| 20 | Pending Invoices | `318` | 1 |
| 30 | Selected Invoices | `26BB799ADE8E4C90BF3CC17B4CD3E0E1` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Pending Invoices (ventana: Resumen de Pagos Pendientes)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Transaction Document | `—` | No | No | — |
| 110 | Invoice | `—` | No | No | — |
| 120 | Order Reference | `—` | No | No | — |
| 130 | Business Partner | `—` | No | No | — |
| 140 | Description | `—` | No | No | — |
| 150 | Invoice Date | `—` | No | No | — |
| 160 | Total Gross Amount | `—` | No | No | — |
| 170 | Total Paid | `—` | No | No | — |
| 180 | Outstanding Amount | `—` | No | No | — |
| 190 | Days Till Next Due | `—` | No | No | — |
| 200 | Document Status | `—` | No | No | — |
| — | Pass Selected | `EM_Ssppinv_PassSelected` | No | No | — |

### Selected Invoices (ventana: Resumen de Pagos Pendientes)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 100 | Invoice | `C_Invoice_ID` | No | Sí | — |
| 110 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 120 | Grand Total Amount | `Grandtotal` | No | Sí | — |
| 130 | Total Paid | `Totalpaid` | No | Sí | — |
| 140 | Outstanding Amount | `Outstandingamt` | No | Sí | — |
| 150 | Amount | `Amount` | No | No | — |
| — | Generate Payment Proposal | `GeneratePaymentProposal` | No | No | — |

### Summary of Pending Payments (ventana: Resumen de Pagos Pendientes)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 110 | Tax ID | `Bptaxid` | No | No | — |
| 120 | Total Pending | `Totalpending` | No | No | — |
| 130 | Total Selected Invoices | `Totalselectedinvoices` | No | No | — |

### Proposed Payment Configuration (ventana: Configuración de Propuesta de Pago)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 100 | Document Type | `C_Doctype_ID` | No | No | — |
| 110 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 120 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 130 | Currency | `C_Currency_ID` | No | No | — |
| 140 | Payment Doctype | `Payment_Doctype_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso principal ligado a un botón que permite completar la acción de la propuesta de pago. Este proceso realiza la validación necesaria antes de ejecutarse y, en caso de fallar, proporciona mensajes de error específicos al usuario. Las validaciones frecuentes incluyen la verificación de que el monto a pagar no exceda el monto pendiente, garantizando que se mantenga un control financiero adecuado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.pending.purchase.invoice.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Generar Propuesta de Pago | Generate Payment Proposal | Generate Payment Proposal | `ssppinv_payment_proposal` | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago; Limpiamos las lineas de las facturas seleccionadas | — |
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
| Botón (PL/pgSQL) | Generar Propuesta de Pago | Generate Payment Proposal | Generate Payment Proposal | `ssppinv_payment_proposal` | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago; Limpiamos las lineas de las facturas seleccionadas | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Generar Propuesta de Pago | Generate Payment Proposal | PL `ssppinv_payment_proposal` | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago; Limpiamos las lineas de las facturas seleccionadas | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago; Limpiamos las lineas de las facturas seleccionadas |
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

El rol del código Java dentro del módulo incluye la implementación de clases que manejan las acciones de usuario, como la generación de propuestas de pago y la validación de montos, permitiendo así la automatización y el manejo eficiente de datos a través de las funciones definidas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.pending.purchase.invoice`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SsppinvComponentProvider` | root | BaseComponentProvider | ComponentProvider / UI | `src/ec/com/sidesoft/pending/purchase/invoice/SsppinvComponentProvider.java` |
| `GeneratePaymentProposalActionHandler` | ad_actions | BaseActionHandler | — | `src/ec/com/sidesoft/pending/purchase/invoice/ad_actions/GeneratePaymentProposalActionHandler.java` |
| `PassSelectedActionHandler` | ad_actions | BaseActionHandler | — | `src/ec/com/sidesoft/pending/purchase/invoice/ad_actions/PassSelectedActionHandler.java` |
| `ValidateAmount` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/pending/purchase/invoice/ad_callouts/ValidateAmount.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Ssppinv Payment Proposal` | `C_DocType.DocBaseType IN ('APPP', 'ARRP') AND C_DocType.IsSOTrx='N' AND AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.AD_Org_ID` |
| Función PL `ssppinv_payment_proposal` | — | invocación proceso | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago |
| Función PL `ssppinv_payment_proposal2` | — | invocación proceso | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Dentro del contexto de la base de datos, el módulo no utiliza triggers, pero sostiene dos funciones PL que gestionan la generación de propuestas de pago y la selección de facturas. Estas funciones son esenciales para el correcto funcionamiento del módulo en términos de lógica de negocio y validaciones.

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
| `ssppinv_payment_proposal` | Generar Propuesta de Pago | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago; Limpiamos las lineas de las facturas seleccionadas | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago; Limpiamos las lineas de las facturas seleccionadas | `model/functions/SSPPINV_PAYMENT_PROPOSAL.xml` |
| `ssppinv_payment_proposal2` | — | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago; Limpiamos las lineas de las facturas seleccionadas | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago; Limpiamos las lineas de las facturas seleccionadas | `model/functions/SSPPINV_PAYMENT_PROPOSAL2.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Generar Propuesta de Pago | `Generate Payment Proposal` | Botón (PL/pgSQL) | PL `ssppinv_payment_proposal` | N | No existe configuracion para crear la propuesta de pago; Creamos la cabecera de la propuesta de pago; Creamos las lineas de la propuesta de pago; Limpiamos las lineas de las factur |

**Total acciones documentadas (extract):** **1** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/ec.com.sidesoft.pending.purchase.invoice/js/ssppinv.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.pending.purchase.invoice`.

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

# Glosario — prefijo `SSPPINV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPPINV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.pending.purchase.invoice` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Generate Payment Proposal` — Generar Propuesta de Pago

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Process of Importing Price List
**Package:** `ec.com.sidesoft.imports.pricelist`

# Module overview — Sidesoft Process of Importing Price List

## Functional

El proceso Sidesoft de Importación de Lista de Precios permite a las empresas cargar y actualizar información de precios de productos de manera eficiente en el sistema Openbravo ERP. Este módulo es utilizado principalmente por usuarios de negocio encargados de la gestión de precios y por administradores del sistema que requieren actualizar las listas de precios de forma efectiva. Su alcance incluye la importación masiva de precios desde archivos externos y la integración con la base de datos del ERP. La implementación de este proceso depende de la compatibilidad con el 'Core' y la 'Compatibilidad de Skin' de versiones anteriores a 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/imports/pricelist` |
| Web | `web/ec.com.sidesoft.imports.pricelist/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPIMPL`

# Guía de chat — Sidesoft Process of Importing Price List

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.imports.pricelist`).

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
- «¿Qué es la tabla sspimpl_import_price_list?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo importo una lista de precios desde un archivo CSV?
- ¿Qué formatos de archivo son aceptados para la importación?
- ¿Existen limitaciones en el número de productos que puedo importar a la vez?
- ¿Cómo puedo verificar si un producto ya existe antes de la importación?
- ¿Qué debo hacer si ocurre un error durante la importación?
- ¿Cómo puedo actualizar una lista de precios existente?
- ¿Cuánto tiempo tarda en completarse el proceso de importación?
- ¿Cómo puedo realizar una copia de seguridad de mis listas de precios?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la entidad cabecera 'sspimpl_import_price_list', que incluye una serie de campos para gestionar los precios asociados a diversos productos. Este proceso abarca etapas como la preparación de los datos, su validación y la inserción en la base de datos. La relación primaria es entre los productos y sus respectivas listas de precios, asegurando que la información se mantenga estructurada y accesible. No se han implementado triggers para este proceso, lo que indica que la lógica de negocio se gestiona principalmente a través de las funciones del proceso y las clases de Java asociadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sspimpl_import_price_list` |
| `sspimpl_import_product_pl` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sspimpl_import_price_list` | sspimpl_import_price_list | — | — | ad_client_id→ad_client; ad_org_id→ad_org; m_pricelist_id→m_pricelist; m_pricelist_version_id→m_pricelist_version | Detalle enlazado a ad_client, ad_org, m_pricelist. | PK `sspimpl_imp_price_list_key`; Cols: m_pricelist_id, overwrite, m_pricelist_version_id, process, status; `SSPIMPL_IMP_PR_LST_ALL_CHK`: ALLORGANIZATION IN ('Y', 'N'); `SSPIMPL_IMP_PRICE_LIST_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspimpl_import_product_pl` | sspimpl_import_product_pl | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `sspimpl_imp_p_pl_key`; Cols: c_doctype_id, documentno, transaction_date, overwrite, process; `SSPIMPL_IMP_P_PL_CHK`: ISACTIVE IN ('Y', 'N'); `SSPIMPL_IMP_PR_LST_ALL_CHK`: ALLORGANIZATION IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sspimpl_import_price_list` |
| `sspimpl_import_product_pl` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación en el módulo se realiza a través de dos ventanas principales: 'Importar lista de precios' e 'Importar Precios por producto a Múltiples Lista de Precio'. Estas ventanas permiten a los usuarios acceder a las funciones necesarias para cargar los datos de precios, así como seleccionar los archivos que se utilizarán para la importación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.imports.pricelist.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Importar lista de precios | import price list |
| Importar Precios por producto a Multiples Lista de Precio | Import multiple price list by product |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Importar lista de precios | import price list | No |
| Importar Precios por producto a Multiples Lista de Precio | Import multiple price list by product | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.imports.pricelist.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Importar lista de precios

- **AD_WINDOW_ID:** `194A0297B5FA4C0E84CCBF585C3B4DBA`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `DBB7E9547159434682EF8953590D10A9` | 0 |

### Ventana: Importar Precios por producto a Multiples Lista de Precio

- **AD_WINDOW_ID:** `E10BCF6E6F064DA6BAC15F8991085A62`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Head | `43BEBCB674FB4EACB45ECD1D64925937` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Header (ventana: Importar lista de precios)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | M_PriceList_ID SSPIMPL | `M_Pricelist_ID` | No | No | — |
| 25 | Price List Version | `M_Pricelist_Version_ID` | No | No | — |
| 30 | Overwrite | `Overwrite` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |
| 60 | processFile | `Process` | No | No | — |
| 70 | All Organization | `Allorganization` | No | No | — |

### Head (ventana: Importar Precios por producto a Multiples Lista de Precio)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 30 | Document No. | `Documentno` | No | Sí | — |
| 40 | Transaction_Date | `Transaction_Date` | No | No | — |
| 45 | Description | `Description` | No | No | — |
| 50 | Overwrite | `Overwrite` | No | No | — |
| 60 | processFile | `Process` | No | No | — |
| 70 | Status SSPIMPL | `Status` | No | Sí | — |
| 90 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los botones típicos en este módulo incluyen opciones para completar la importación y volver a la pantalla anterior. Las validaciones frecuentes durante el proceso pueden incluir la verificación de formatos de precio y la existencia de productos en la base de datos. Aunque no se generan informes específicos, el sistema proporciona retroalimentación a través de mensajes de error o de éxito durante la ejecución del proceso de importación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.imports.pricelist.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Procesar | processFile | processFile | Java `ProcessFile` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sspimpl_Import_Price_List_ID` | `src/ec/com/sidesoft/imports/pricelist/ad_process/ProcessFile.java` |
| Botón (Java) | Procesar | processFile | processFile product pl | Java `ProcessFileProductPL` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sspimpl_Import_Product_Pl_ID` | `src/ec/com/sidesoft/imports/pricelist/ad_process/ProcessFileProductPL.java` |
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
| Botón (Java) | Procesar | `ProcessFile` | Proceso Java (toolbar/background) | `Sspimpl_Import_Price_List_ID` | — | `src/ec/com/sidesoft/imports/pricelist/ad_process/ProcessFile.java` |
| Botón (Java) | Procesar | `ProcessFileProductPL` | Proceso Java (toolbar/background) | `Sspimpl_Import_Product_Pl_ID` | — | `src/ec/com/sidesoft/imports/pricelist/ad_process/ProcessFileProductPL.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Procesar | processFile | processFile | Java `ProcessFile` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sspimpl_Import_Price_List_ID` | `src/ec/com/sidesoft/imports/pricelist/ad_process/ProcessFile.java` |
| Botón (Java) | Procesar | processFile | processFile product pl | Java `ProcessFileProductPL` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sspimpl_Import_Product_Pl_ID` | `src/ec/com/sidesoft/imports/pricelist/ad_process/ProcessFileProductPL.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Procesar | processFile | Java `ProcessFile` | Proceso Openbravo registro `Sspimpl_Import_Price_List_ID` | Proceso Openbravo registro `Sspimpl_Import_Price_List_ID` |
| Botón (Java) | Procesar | processFile | Java `ProcessFileProductPL` | Proceso Openbravo registro `Sspimpl_Import_Product_Pl_ID` | Proceso Openbravo registro `Sspimpl_Import_Product_Pl_ID` |
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

El módulo incluye varias clases Java que facilitan la lógica de negocio necesaria para el manejo de la importación de listas de precios, tales como 'UpdateDocumentNo' para la gestión de secuencias de documentos y 'ProcessFile' que maneja el procesamiento del archivo de importación. Estas clases permiten una interacción más fluida con los datos y las funcionalidades del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.imports.pricelist`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `UpdateDocumentNo` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/imports/pricelist/ad_callouts/UpdateDocumentNo.java` |
| `Temp` | ad_model | — | — | `src/ec/com/sidesoft/imports/pricelist/ad_model/Temp.java` |
| `TempProductPL` | ad_model | — | — | `src/ec/com/sidesoft/imports/pricelist/ad_model/TempProductPL.java` |
| `ProcessFile` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/imports/pricelist/ad_process/ProcessFile.java` |
| `ProcessFileProductPL` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/imports/pricelist/ad_process/ProcessFileProductPL.java` |
| `ImportPriceListEventListener` | event | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/imports/pricelist/event/ImportPriceListEventListener.java` |
| `ImportProductPlEventListener` | event | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/imports/pricelist/event/ImportProductPlEventListener.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Doctype Import Price List by Product` | `C_DocType.ad_table_id in ('43BEBCB674FB4EACB45ECD1D64925937')` |
| AD_VAL_RULE | — | `PriceListVersion by PriceList` | `M_Pricelist_ID=@M_Pricelist_ID@` |
| Java event/validator | `ImportPriceListEventListener` | persistencia/UI | *(leer `src/ec/com/sidesoft/imports/pricelist/event/ImportPriceListEventListener.java`)* |
| Java event/validator | `ImportProductPlEventListener` | persistencia/UI | *(leer `src/ec/com/sidesoft/imports/pricelist/event/ImportProductPlEventListener.java`)* |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

En este módulo, no se han implementado triggers ni funciones PL específicas, lo que sugiere que la lógica de ejecución y validaciones se podría gestionar completamente por las clases de Java y el proceso principal. Esto permite una mayor flexibilidad en la adaptación y mantenimiento del código dentro del contexto del ERP.

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
| 1 | Procesar | `processFile` | Botón (Java) | Java `ProcessFile` | N | Proceso Openbravo registro `Sspimpl_Import_Price_List_ID` |
| 2 | Procesar | `processFile product pl` | Botón (Java) | Java `ProcessFileProductPL` | N | Proceso Openbravo registro `Sspimpl_Import_Product_Pl_ID` |

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

Módulo: `ec.com.sidesoft.imports.pricelist`.

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

# Glosario — prefijo `SSPIMPL`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPIMPL` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.imports.pricelist` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `processFile` — Procesar
- `processFile product pl` — Procesar

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Load Orders
**Package:** `ec.com.sidesoft.load.orders`

# Module overview — Sidesoft Load Orders

## Functional

El módulo 'Sidesoft Load Orders' permite la carga de datos relacionados con pedidos en el sistema Openbravo. Está diseñado para facilitar la importación masiva de líneas de pedido, beneficiando tanto a usuarios de negocio que buscan optimizar procesos como a desarrolladores que requieren una integración eficaz. Su alcance se limita a la gestión de pedidos y no tiene dependencias externas, lo que simplifica su implementación en diferentes entornos del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/load/orders` |
| Web | `web/ec.com.sidesoft.load.orders/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSLOR`

# Guía de chat — Sidesoft Load Orders

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.load.orders`).

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

- ¿Cómo puedo cargar un pedido utilizando el módulo?
- ¿Qué tipos de validaciones se aplican al importar líneas de pedido?
- ¿Puedo ver un informe de los pedidos cargados recientemente?
- ¿Qué sucede si un pedido contiene un producto que no existe?
- ¿Es posible cancelar un pedido después de cargarlo?
- ¿Cómo se gestionan los errores durante la importación?
- ¿Cuáles son los formatos aceptables para la carga de datos?
- ¿Hay un límite en la cantidad de líneas de pedido que puedo importar a la vez?

# Domain — data model

## Functional

Este módulo se basa en la importación de líneas de pedido, lo que implica la interacción con entidades como 'Order' y 'OrderLine'. Aunque no se especifican tablas físicas ni estructuras complejas en el inventario, se deduce que el flujo implicaría la creación y actualización de pedidos en el sistema mediante un proceso de carga que gestiona los datos de productos, cantidades y precios. Los triggers y funciones no están definidos, pero es probable que se utilicen para validar la integridad de los datos al momento de la importación.

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

El acceso al módulo se realiza a través de la API de Openbravo, utilizando clases Java que manejan la lógica de importación. Los usuarios no interactúan directamente con ventanas gráficas específicas del módulo, ya que su funcionalidad se integra en el backend del ERP para facilitar la carga automática de datos.

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

Los procesos relacionados con este módulo no incluyen botones visibles o informes detallados según el inventario. Sin embargo, se espera que el proceso principal involucre la ejecución del proceso de importación de líneas de pedidos, lo que también puede implicar validaciones en torno a los datos cargados, asegurando que cumplan con los requisitos del sistema. Los usuarios podrían esperar mensajes de error o confirmación basados en la validez de los datos ingresados.

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

El módulo contiene una clase Java, 'ImportLinesOrders', que es responsable de la lógica para importar líneas de pedidos. Esta clase incluye validaciones de los parámetros de entrada y utiliza ORM para interactuar con las entidades de pedidos y productos en Openbravo, lo que permite una gestión adecuada de los datos durante el proceso de carga.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.load.orders`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ImportLinesOrders` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/load/orders/ad_process/ImportLinesOrders.java` |
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

Aunque el módulo no tiene triggers o funciones PL definidas, se puede suponer que existen funciones de validación y control dentro del Java que manejan las interacciones con la base de datos, asegurando que los datos importados sean consistentes y se mantengan dentro de las reglas de negocio definidas por Openbravo.

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

Módulo: `ec.com.sidesoft.load.orders`.

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

# Glosario — prefijo `SSLOR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSLOR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.load.orders` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Resupply
**Package:** `ec.com.sidesoft.localization.ecuador.resupply`

# Module overview — Resupply

## Functional

El módulo Resupply está diseñado para facilitar el proceso de reaprovisionamiento en entornos de negocio, permitiendo a los usuarios gestionar pedidos de manera eficiente. Los actores principales son los administradores de inventario y los empleados de ventas que utilizan el sistema para crear y gestionar pedidos de reaprovisionamiento. El alcance del módulo incluye la creación, modificación y seguimiento de pedidos, así como la impresión de informes relevantes. Sus dependencias incluyen módulos centralizados, como 'Core' y 'Resupply Template', que son fundamentales para su funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/ecuador/resupply` |
| Web | `web/ec.com.sidesoft.localization.ecuador.resupply/` |

### Declared dependencies

- Core
- Resupply Template

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSRS`

# Guía de chat — Resupply

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.ecuador.resupply`).

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
- «¿Qué es la tabla ssrs_resupplyposline?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo creo un nuevo pedido de reaprovisionamiento?
- ¿Qué debo hacer si un pedido se queda atascado en el proceso?
- ¿Cómo puedo modificar una línea de un pedido existente?
- ¿Qué hacer si el informe de reaprovisionamiento no se imprime correctamente?
- ¿Cómo valido que las cantidades de pedido sean correctas?
- ¿Cuáles son las dependencias del módulo Resupply?
- ¿Existen validaciones específicas para los datos de los pedidos?
- ¿Cómo realizo un seguimiento del estado de un pedido?

# Domain — data model

## Functional

La entidad cabecera en este módulo es 'ssrs_resupply', que registra la información de los pedidos. Cada pedido puede tener varias líneas asociadas a través de la tabla 'ssrs_resupplyline', creando una relación uno a muchos. Las etapas del proceso comienzan con la creación de un pedido, seguido de la adición de líneas de pedido, y pueden incluir validaciones de datos a través de triggers como 'SSRS_RESUPPLYLINE_TRG', que valida datos críticos al momento de guardar. También hay triggers, como 'SSRS_ASSIGN_DOCUMENTNO_TRG', que manejan la asignación de números de documentos de manera automática.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssrs_detail_lots` |
| `ssrs_resupply` |
| `ssrs_resupply_pos` |
| `ssrs_resupplyline` |
| `ssrs_resupplyposline` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssrs_detail_lots` | ssrs_detail_lots | — | — | ad_client_id→ad_client; ad_org_id→ad_org; m_attributesetinstance_id→m_attributesetinstance | Detalle enlazado a ad_client, ad_org, m_attributesetinstance. | PK `ssrs_det_lots_key`; Cols: recordid, qtyonhand, m_attributesetinstance_id; `SSRS_DET_LOTS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSRS_RECORDID_INDX` (recordid, m_attributesetinstance_id) |
| `ssrs_resupply` | ssrs_resupply | `SSRS_RESUPPLYDISPLAYED_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_org_id_req→ad_org; c_bpartner_id→c_bpartner; ssrs_resupply_pos_id→ssrs_resupply_pos (+2) | Detalle enlazado a ad_client, ad_org. Validado por trigger(s): SSRS_RESUPPLYDISPLAYED_TRG. | PK `ssrs_resupply_key`; Cols: description, documentno, c_bpartner_id, createpo, docstatus; `SSRS_RESUPPLY_CREATEPO`: CREATEPO IN ('Y', 'N'); `SSRS_RESUPPLY_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssrs_resupply_pos` | ssrs_resupply_pos | `SSRS_DATESVALIDATE_TRG` | — | m_movement_id→m_movement; m_movement2_id→m_movement; ad_client_id→ad_client; ad_org_id→ad_org; ad_org_id_req→ad_org (+2) | Detalle enlazado a ad_client, m_movement. Validado por trigger(s): SSRS_DATESVALIDATE_TRG. | PK `ssrs_resupply_pos_key`; Cols: description, documentno, c_bpartner_id, createpo, docstatus; `SSRS_RESUPPLY_POS_CREATEPO`: CREATEPO IN ('Y', 'N'); `SSRS_RESUPPLY_POS_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssrs_resupplyline` | ssrs_resupplyline | `SSRS_LINEDISPLAYED_TRG`; `SSRS_PROD_ATTIB_TRG`; `SSRS_RESUPPLYLINE_TRG` | `SSRS_RESUPPLYLINE_PRODUCTU` (m_product_id, ssrs_resupply_id) | c_aum→c_uom; ad_client_id→ad_client; m_attributesetinstance_id→m_attributesetinstance; ad_org_id→ad_org; c_bpartner_id→c_bpartner (+5) | Detalle enlazado a ad_client, c_uom, m_attributesetinstance. Validado por trigger(s): SSRS_LINEDISPLAYED_TRG, SSRS_PROD_ATTIB_TRG, SSRS_RESUPPLYLINE_TRG. | PK `ssrs_resupplyline_key`; Cols: ssrs_resupply_id, m_product_id, qty, pricelist, linenetamt; `SSRS_RESUPPLYLINE_ISACTIVE`: ISACTIVE IN ('Y', 'N'); idx `SSRS_RESSUPLY_BPARTNER_IDX` (c_bpartner_id); idx `SSRS_RESSUPLY_PRODUCT_IDX` (m_product_id) (+1) |
| `ssrs_resupplyposline` | ssrs_resupplyposline | `SSRS_RESUPPLYLINEPOST_TRG` | `SSRS_RESUPPLYPOSLINE_PRODUCTU` (m_product_id, ssrs_resupply_pos_id) | c_aum→c_uom; m_product_category_id→m_product_category; ad_client_id→ad_client; m_attributesetinstance_id→m_attributesetinstance; ad_org_id→ad_org (+6) | Detalle enlazado a ad_client, c_uom, m_product_category. Validado por trigger(s): SSRS_RESUPPLYLINEPOST_TRG. | PK `ssrs_resupplyposline_key`; Cols: ssrs_resupply_pos_id, m_product_id, qty, pricelist, linenetamt; `SSRS_RESUPPLYPOSLINE_ISACTIVE`: ISACTIVE IN ('Y', 'N'); idx `SSRS_POSLINE_BPARTNER_IDX` (c_bpartner_id); idx `SSRS_POSLINE_PRODUCT_IDX` (m_product_id) (+1) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssrs_detail_lots` |
| `ssrs_resupply` |
| `ssrs_resupply_pos` |
| `ssrs_resupplyline` |
| `ssrs_resupplyposline` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ORG`, `AD_USER`, `C_DOCTYPE`, `M_MOVEMENT`, `M_MOVEMENTLINE`, `M_PRODUCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación del módulo Resupply en la interfaz de usuario se realiza a través de dos ventanas principales: 'Pedido de Reaprovisionamiento' y 'Pedido de Reaprovisionamiento PDV'. Los usuarios pueden acceder a estas ventanas para crear y editar pedidos, viendo información relevante a través de múltiples pestañas y campos que facilitan la gestión del inventario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.ecuador.resupply.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Pedido de Reaprovisionamiento | Request Resupply |
| Pedido de Reaprovisionamiento PDV | Request Resupply POS |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Guía de Remisión | Guide Remission | No |
| Pedido de Reaprovisionamiento | Request Resupply | No |
| Pedido de Reaprovisionamiento PDV | Request Resupply POS | No |
| Picking List | Picking List | No |
| Resupply Consolidated | Resupply Consolidated | No |
| Resupply to Movement | Resupply to Movement | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.ecuador.resupply.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Pedido de Reaprovisionamiento

- **AD_WINDOW_ID:** `23A1386D3BDF4B1E938F26775441EF94`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Request Resupply | `2E056D09471E4483BEEBB771BACA7743` | 0 |
| 20 | Line | `86802E6E868E46AEBFE36377879BBE7F` | 1 |

### Ventana: Pedido de Reaprovisionamiento PDV

- **AD_WINDOW_ID:** `60AFF6C2E67141E492C2BDAF20B335C3`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Request Resupply POS | `F47CDC255C054ECABB517C5D07B9E2BC` | 0 |
| 20 | Lines | `6E946A3591B74C81B6E02474D62C86AD` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `118`

- **AD_TAB_ID:** `118` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 270 | Chief of Warehouse | `EM_Ssrs_Boss_Warehouse` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |

### Pestaña `143`

- **AD_TAB_ID:** `143` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 250 | Transitory Storage | `EM_Ssrs_M_Locatortrn_ID` | No | No | — |
| 260 | Reception Storage | `EM_Ssrs_M_Locatorrcp_ID` | No | No | — |
| 270 | Dispatch time | `EM_Ssrs_Timeto` | No | No | — |
| 280 | Document Transaction Send | `EM_Ssrs_C_Doctypefrom_ID` | No | No | — |
| 290 | Document Transaction Reception | `EM_Ssrs_C_Doctypeto_ID` | No | No | — |
| 610 | Center of Distribution | `EM_Ssrs_Centerdistribuion` | No | No | — |

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 260 | Primary Document | `EM_Ssrs_Default` | No | No | — |

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 520 | Warehouse | `EM_Ssrs_M_Warehouse_ID` | No | No | — |
| 597 | Resupply product | `EM_Ssrs_Resupplyproduct` | No | No | — |

### Lines (ventana: Pedido de Reaprovisionamiento PDV)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 5 | Line No. | `Line` | No | Sí | — |
| 40 | Product | `M_Product_ID` | No | No | — |
| 85 | Order Quantity | `Quantityorder` | No | No | — |
| 90 | Alternative UOM | `C_Aum` | No | Sí | — |
| 105 | UOM | `C_Uom_ID` | No | Sí | — |
| 110 | Quantity | `Qty` | No | Sí | — |
| 150 | Search Key | `Value` | No | Sí | — |
| 290 | Description | `Description` | No | No | — |
| 320 | QTY Dispatched | `QTY_Dispatched` | No | No | — |
| 330 | Sec Qty Dispatched | `Secqty_Dispatched` | No | Sí | — |
| 350 | Product Category | `M_Product_Category_ID` | No | Sí | — |

### Pestaña `259`

- **AD_TAB_ID:** `259` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Document Type | `EM_Ssrs_C_Doctype_ID` | No | No | — |
| 45 | Shipper | `EM_Ssrs_M_Shipper_ID` | No | No | — |
| 2170 | Request Resupply POS | `EM_Ssrs_Resupply_Pos_ID` | No | No | — |

### Line (ventana: Pedido de Reaprovisionamiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `Line` | No | Sí | — |
| 40 | Product | `M_Product_ID` | No | No | — |
| 90 | Order Quantity | `Quantityorder` | No | No | — |
| 100 | UOM | `C_Uom_ID` | No | Sí | — |
| 110 | Alternative UOM | `C_Aum` | No | Sí | — |
| 290 | Quantity | `Qty` | No | Sí | — |
| 300 | Search Key | `Value` | No | Sí | — |
| 310 | Description | `Description` | No | No | — |

### Request Resupply POS (ventana: Pedido de Reaprovisionamiento PDV)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Need by date | `Needbydate` | No | No | — |
| 40 | Document No. | `Documentno` | No | No | — |
| 80 | Post Resupply POS | `DocAction` | No | No | — |
| 120 | Description | `Description` | No | No | — |
| 130 | Distribution Center | `AD_Org_Id_Req` | No | No | — |
| 140 | Estimated delivery date | `Estimateddeliverydate` | No | No | — |
| 150 | Process | `Actioncomplete` | No | No | — |
| 160 | Load Template | `Create_Lines` | No | No | — |
| 170 | Movement 1 | `M_Movement_ID` | No | Sí | — |
| 180 | Movement 2 | `M_Movement2_ID` | No | Sí | — |

### Request Resupply (ventana: Pedido de Reaprovisionamiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Need by date | `Needbydate` | No | No | — |
| 30 | Document No. | `DocumentNo` | No | No | — |
| 50 | Distribution Center | `AD_Org_Id_Req` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 80 | Post Resupply | `DocAction` | No | No | 101 |
| 90 | Estimated delivery date | `Estimateddeliverydate` | No | No | — |
| 100 | Warehouse | `M_Warehouse_ID` | No | No | — |
| 110 | Request Resupply POS | `Ssrs_Resupply_Pos_ID` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los botones típicos en el módulo incluyen opciones como completar, retornar o rechazar un pedido. Específicamente, el botón 'Completar' activa la función 'ssrs_resupply_complete_pos', que maneja la validación de pedidos existentes y asegura que no haya errores antes de finalizar el proceso. Además, el módulo genera un informe denominado 'ssrs_PrintRessuply', que permite la impresión de pedidos para su archivo o distribución. También incorpora validaciones frecuentes para asegurar la integridad de los datos ingresados y procesados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.ecuador.resupply.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar Plantilla | Load Template | Ssrs_Load_Template | `ssrs_load_template` | BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; RAISE_APPLICATION_ERROR(-20000, 'La linea ' || Cur_m_inoutline.line || ' producto: ' || Cur_m_inoutline.product || ', N… | — |
| Botón (PL/pgSQL) | Post Resupply | Post Resupply | Ssrs_Resupply_Post | `Ssrs_Resupply_New_Post` | INICIO IF VERIFICAR SI HAY REGISTROS EN REAPROVISIONAMIENTO PDV; INICIO LOOP BUSQUEDA DE LAS LINEAS DEL PEDIDO; INICIO CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODEGA DE LA CABECERA; SE ACRTUALIZA LAS LI… | — |
| Botón (PL/pgSQL) | Post Resupply POS | Post Resupply POS | Ssrs_ResupplyPos_Post | `ssrs_resupplypos_post` | Si el documento está completado y exista tercero en el; Sí este usuaro esta bloqueado o en bloqueo; Recoger datos de las lineas de la transaccion; almacena datos del tercero asociado al registro | — |
| Botón (PL/pgSQL) | Procesar | Process Resupply PDV | Ssrs_Action_Complete | `ssrs_resupply_complete_pos` | Ya existe un movimiento con el numero de documento; Recupera si hay algun error en esta función; Si no hay ningun error en la funcion entra; v_documentSends - documento para quien envia | — |
| Proceso / otro | Guía de Remisión | Guide Remission | GuideRemission | *(OBUIAPP / manual)* | Guide Remission | — |
| Proceso / otro | Picking List | Picking List | pickinglist | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Resupply Consolidated | Resupply Consolidated | ResupplyConsolidated | *(OBUIAPP / manual)* | Resupply Consolidated | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | ssrs_PrintRessuply | ssrs_PrintRessuply | ssrs_PrintRessuply | Java `Ssrs_PrintReportFinalResupply` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_process/Ssrs_PrintReportFinalResupply.java` |
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
| Reporte | ssrs_PrintRessuply | `Ssrs_PrintReportFinalResupply` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_process/Ssrs_PrintReportFinalResupply.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar Plantilla | Load Template | Ssrs_Load_Template | `ssrs_load_template` | BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; RAISE_APPLICATION_ERROR(-20000, 'La linea ' || Cur_m_inoutline.line || ' producto: ' || Cur_m_inoutline.product || ', N… | — |
| Botón (PL/pgSQL) | Post Resupply | Post Resupply | Ssrs_Resupply_Post | `Ssrs_Resupply_New_Post` | INICIO IF VERIFICAR SI HAY REGISTROS EN REAPROVISIONAMIENTO PDV; INICIO LOOP BUSQUEDA DE LAS LINEAS DEL PEDIDO; INICIO CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODEGA DE LA CABECERA; SE ACRTUALIZA LAS LI… | — |
| Botón (PL/pgSQL) | Post Resupply POS | Post Resupply POS | Ssrs_ResupplyPos_Post | `ssrs_resupplypos_post` | Si el documento está completado y exista tercero en el; Sí este usuaro esta bloqueado o en bloqueo; Recoger datos de las lineas de la transaccion; almacena datos del tercero asociado al registro | — |
| Botón (PL/pgSQL) | Procesar | Process Resupply PDV | Ssrs_Action_Complete | `ssrs_resupply_complete_pos` | Ya existe un movimiento con el numero de documento; Recupera si hay algun error en esta función; Si no hay ningun error en la funcion entra; v_documentSends - documento para quien envia | — |
| Proceso / otro | Guía de Remisión | Guide Remission | GuideRemission | *(OBUIAPP / manual)* | Guide Remission | — |
| Proceso / otro | Picking List | Picking List | pickinglist | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Resupply Consolidated | Resupply Consolidated | ResupplyConsolidated | *(OBUIAPP / manual)* | Resupply Consolidated | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar Plantilla | Load Template | PL `ssrs_load_template` | BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; RAISE_APPLICATION_ERROR(-20000, 'La linea ' || Cur_m_inoutline.line || ' producto: ' || Cur_m_inoutline.product || ', N… | BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; RAISE_APPLICATION_ERROR(-20000, 'La linea ' ||  Cur_m_inoutline.line || ' producto: ' || Cur_m_inoutline.product || ', No tiene una ubicacion configurada') ; |
| Botón (PL/pgSQL) | Post Resupply | Post Resupply | PL `Ssrs_Resupply_New_Post` | INICIO IF VERIFICAR SI HAY REGISTROS EN REAPROVISIONAMIENTO PDV; INICIO LOOP BUSQUEDA DE LAS LINEAS DEL PEDIDO; INICIO CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODEGA DE LA CABECERA; SE ACRTUALIZA LAS LI… | INICIO IF VERIFICAR SI HAY REGISTROS EN REAPROVISIONAMIENTO PDV; INICIO LOOP BUSQUEDA DE LAS LINEAS DEL PEDIDO; INICIO CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODEGA DE LA CABECERA; SE ACRTUALIZA LAS LINEAS DEL PEDIDO DE REAPROVISIONAMIENTO PDV; CANTIDAD DESPACHADA PRINCIPAL Y CANTIDAD SECUNDARIA PEDIDA; FIN CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODEGA DE LA CABECERA |
| Botón (PL/pgSQL) | Post Resupply POS | Post Resupply POS | PL `ssrs_resupplypos_post` | Si el documento está completado y exista tercero en el; Sí este usuaro esta bloqueado o en bloqueo; Recoger datos de las lineas de la transaccion; almacena datos del tercero asociado al registro | Si el documento está completado y exista tercero en el; Sí este usuaro esta bloqueado o en bloqueo; Recoger datos de las lineas de la transaccion; almacena datos del tercero asociado al registro; Sí el usuario está bloqueado o en bloqueo; Cuenta que los productos de la linea sean genericos |
| Botón (PL/pgSQL) | Procesar | Process Resupply PDV | PL `ssrs_resupply_complete_pos` | Ya existe un movimiento con el numero de documento; Recupera si hay algun error en esta función; Si no hay ningun error en la funcion entra; v_documentSends - documento para quien envia | Ya existe un movimiento con el numero de documento; Recupera si hay algun error en esta función; Si no hay ningun error en la funcion entra; v_documentSends - documento para quien envia; v_documentTransaction - Es de la matriz quien va a sacar para mi bodega; VALIDACION DEL NUMERO DE DOCUMENTO EN LA M_MOVEMENT |
| Proceso / otro | Guía de Remisión | Guide Remission | — | Guide Remission | — |
| Proceso / otro | Picking List | Picking List | — | — | — |
| Proceso / otro | Resupply Consolidated | Resupply Consolidated | — | Resupply Consolidated | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | ssrs_PrintRessuply | ssrs_PrintRessuply | ssrs_PrintRessuply | Java `Ssrs_PrintReportFinalResupply` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_process/Ssrs_PrintReportFinalResupply.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 7**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **1**; archivos `*.jrxml` en el repo = **7**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | ssrs_PrintRessuply | `ssrs_PrintRessuply` | Java `Ssrs_PrintReportFinalResupply`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | ssrs_PrintRessuply |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/localization/ecuador/resupply/ad_reports/GuiaRemision1.jrxml`
- `src/ec/com/sidesoft/localization/ecuador/resupply/ad_reports/GuiaRemision1_subreport1.jrxml`
- `src/ec/com/sidesoft/localization/ecuador/resupply/ad_reports/GuiaRemisionLine.jrxml`
- `src/ec/com/sidesoft/localization/ecuador/resupply/ad_reports/PickingList.jrxml`
- `src/ec/com/sidesoft/localization/ecuador/resupply/ad_reports/PickingListResupply.jrxml`
- `src/ec/com/sidesoft/localization/ecuador/resupply/ad_reports/RptM_ResupplyConsolidated.jrxml`
- `src/ec/com/sidesoft/localization/ecuador/resupply/ad_reports/Rpt_ResupplyPrint.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Ssrs_ErrorNeedByDate` | The need date must be greater than or equal to the current date and less than or equal to | The need date must be greater than or equal to the current date and less than or equal to | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `ssrs_amountrequest` | Incorrect amount to dispatch, request No: %s line: %s | Incorrect amount to dispatch, request No: %s line: %s | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssrs_ErrorDeliveryDate` | The expected date of shipment must be greater than or equal to the current date and less than or equal to | The expected date of shipment must be greater than or equal to the current date and less than or equal to | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `em_ssrs_Doctype_Org` | Organization has not assigned document transaction | Organization has not assigned document transaction | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `ssrs_ValidationLineResupply` | The Lines do not correspond to the Request Resupply: %s | The Lines do not correspond to the Request Resupply: %s | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssrs_ErrorDeleteLines` | Error deleting. Remove the lines first to continue. | Error deleting. Remove the lines first to continue. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `ssrs_QuantityIncorrect` | Incorrect quantity to dispatch | Incorrect quantity to dispatch | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `em_ssrs_documentnumber` | Transaction Document has not sequence document number. | Transaction Document has not sequence document number. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRS_ActionNoCompleteTime` | Action can not be completed, the request is out of time | Action can not be completed, the request is out of time | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El código Java en el módulo Resupply se usa principalmente para manejar la lógica de negocio relacionada con la interfaz de usuario, asegurando que los datos se procesen y validen adecuadamente. Las clases Java, como 'DisplayedValue' y 'DisplayedSecValue', implementan funcionalidades específicas de llamadas, ayudando a manejar la interacción entre los componentes de la UI y el modelo de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.ecuador.resupply`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `DisplayedSecValue` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_callouts/DisplayedSecValue.java` |
| `DisplayedValue` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_callouts/DisplayedValue.java` |
| `SL_Movement_Doctype` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_callouts/SL_Movement_Doctype.java` |
| `SL_ResupplyLine_AlterUom` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_callouts/SL_ResupplyLine_AlterUom.java` |
| `SL_ResupplyLine_Conversion` | ad_callouts | HttpSecureAppServlet | — | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_callouts/SL_ResupplyLine_Conversion.java` |
| `SL_ResupplyLine_Product` | ad_callouts | HttpSecureAppServlet | — | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_callouts/SL_ResupplyLine_Product.java` |
| `SL_Resupply_Conversion` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_callouts/SL_Resupply_Conversion.java` |
| `RequisitionToOrder` | ad_forms | HttpSecureAppServlet | — | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_forms/RequisitionToOrder.java` |
| `InsertResupplyLineExcell` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_process/InsertResupplyLineExcell.java` |
| `Ssrs_PrintReportFinalResupply` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/localization/ecuador/resupply/ad_process/Ssrs_PrintReportFinalResupply.java` |
| `Ssrs_ValideLineResupply` | businessevent | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/localization/ecuador/resupply/businessevent/Ssrs_ValideLineResupply.java` |
| `Ssrs_ValideLineResupplyPOS` | businessevent | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/localization/ecuador/resupply/businessevent/Ssrs_ValideLineResupplyPOS.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSRS_ASSIGN_DOCUMENTNO_TRG` | `m_movement` | after INSERT/UPDATE | select distinct EM_Ssrs_C_Doctype_ID from m_movement; OBTENGO ID DE LA SEQUENCIA RELACIONADA AL TIPO DE DOCUMENTO; ACTUALIZO LA SECUENCIA AL SIGUIENTE NUMERO QUE LE CORRESPONDE; VALIDA SI SE MODIFICO EL TIPO DE DOCUMENTO |
| Trigger `SSRS_DATESVALIDATE_TRG` | `ssrs_resupply_pos` | before INSERT/UPDATE | Validación reutilizable de campos. |
| Trigger `SSRS_LINEDISPLAYED_TRG` | `ssrs_resupplyline` | before INSERT/UPDATE/DELETE | RAISE_APPLICATION_ERROR(-20000, '@20520@'); |
| Trigger `SSRS_PROD_ATTIB_TRG` | `ssrs_resupplyline` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSRS_RESUPPLYDISPLAYED_TRG` | `ssrs_resupply` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSRS_RESUPPLYLINEPOST_TRG` | `ssrs_resupplyposline` | before INSERT/UPDATE/DELETE | La cantidad de pedido no puede guardarse con el valor de cero.; No se puede eliminar esta transaccion porque ya está procesada.; select * from ssrs_resupplyposline where ssrs_resupply_pos_id; RAISE_APPLICATION_ERROR(-20… |
| Trigger `SSRS_RESUPPLYLINE_TRG` | `ssrs_resupplyline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Resupply Warehouse` | `M_Warehouse.AD_Org_ID = @AD_Org_Id_Req@` |
| AD_VAL_RULE | — | `ssrs_resupply_cuom` | `C_Uom.C_Uom_ID=(Select C_Uom_ID from m_product where  m_product.m_product_id = @M_Product_ID@)` |
| AD_VAL_RULE | — | `C_DocType_MMM` | `C_DocType.DocBaseType IN ('MMM') and C_DocType.em_ssrs_default = 'Y'` |
| AD_VAL_RULE | — | `Ssrs_Category_Product` | `M_Product_Category.M_Product_Category_ID = (SELECT M_Product.M_Product_Category_ID FROM M_Product WHERE M_Product.M_Prod` |
| AD_VAL_RULE | — | `Resupply_Product_UOM` | `M_Product_UOM.M_Product_ID = @M_Product_ID@` |
| AD_VAL_RULE | — | `Alternative UOM` | `C_UOM.c_uom_id IN(select p.c_uom_id from m_product p where p.m_product_id = @M_Product_ID@) or C_UOM.c_uom_id IN(select ` |
| AD_VAL_RULE | — | `Center Distribution` | `AD_Org.em_ssrs_centerdistribuion= 'Y'` |
| AD_VAL_RULE | — | `Resupply Product` | `M_Product.em_ssrs_resupplyproduct = 'Y'` |
| Función PL `ssrs_load_template` | — | invocación proceso | BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; RAISE_APPLICATION_ERROR(-20000, 'La linea ' ||  Cur_m_inoutline.line || ' producto: ' || Cur_m_inoutline.product || ', No tiene una ubicacion configurada') ; |
| Función PL `ssrs_requestreaprline_trg2` | — | invocación proceso | Does not allow to change the attribute set value; for products which attribute set value type is Fixed |
| Función PL `ssrs_resupply_complete_pos` | — | invocación proceso | Ya existe un movimiento con el numero de documento; Recupera si hay algun error en esta función; Si no hay ningun error en la funcion entra |
| Función PL `ssrs_resupply_new_post` | — | invocación proceso | INICIO IF VERIFICAR SI HAY REGISTROS EN REAPROVISIONAMIENTO PDV; INICIO LOOP BUSQUEDA DE LAS LINEAS DEL PEDIDO; INICIO CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODEGA DE LA CABECERA |
| Función PL `ssrs_resupplypos_post` | — | invocación proceso | Si el documento está completado y exista tercero en el; Sí este usuaro esta bloqueado o en bloqueo; Recoger datos de las lineas de la transaccion |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y las funciones PL/pgSQL juegan un papel crucial en el soporte del módulo, permitiendo validar automáticamente los datos y reaccionar ante ciertos eventos en las tablas relevantes. Por ejemplo, el trigger 'SSRS_RESUPPLYLINEPOST_TRG' evita que se ingresen líneas de pedido con cantidades nulas o erróneas, asegurando que las transacciones de reaprovisionamiento sean precisas y confiables.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSRS_ASSIGN_DOCUMENTNO_TRG` | `m_movement` | after | INSERT/UPDATE | select distinct EM_Ssrs_C_Doctype_ID from m_movement; OBTENGO ID DE LA SEQUENCIA RELACIONADA AL TIPO DE DOCUMENTO; ACTUALIZO LA SECUENCIA AL SIGUIENTE NUMERO QUE LE CORRESPONDE; VALIDA SI SE MODIFICO EL TIPO DE DOCUMENTO | `model/triggers/SSRS_ASSIGN_DOCUMENTNO_TRG.xml` |
| `SSRS_RESUPPLYDISPLAYED_TRG` | `ssrs_resupply` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSRS_RESUPPLYDISPLAYED_TRG.xml` |
| `SSRS_DATESVALIDATE_TRG` | `ssrs_resupply_pos` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SSRS_DATESVALIDATE_TRG.xml` |
| `SSRS_LINEDISPLAYED_TRG` | `ssrs_resupplyline` | before | INSERT/UPDATE/DELETE | RAISE_APPLICATION_ERROR(-20000, '@20520@'); | `model/triggers/SSRS_LINEDISPLAYED_TRG.xml` |
| `SSRS_PROD_ATTIB_TRG` | `ssrs_resupplyline` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSRS_PROD_ATTIB_TRG.xml` |
| `SSRS_RESUPPLYLINE_TRG` | `ssrs_resupplyline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSRS_RESUPPLYLINE_TRG.xml` |
| `SSRS_RESUPPLYLINEPOST_TRG` | `ssrs_resupplyposline` | before | INSERT/UPDATE/DELETE | La cantidad de pedido no puede guardarse con el valor de cero.; No se puede eliminar esta transaccion porque ya está procesada.; select * from ssrs_resupplyposline where ssrs_resupply_pos_id; RAISE_APPLICATION_ERROR(-20… | `model/triggers/SSRS_RESUPPLYLINEPOST_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssrs_bpartner_trg` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSRS_BPARTNER_TRG.xml` |
| `ssrs_load_template` | Cargar Plantilla | BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; RAISE_APPLICATION_ERROR(-20000, 'La linea ' || Cur_m_inoutline.line || ' producto: ' || Cur_m_inoutline.product || ', N… | BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; RAISE_APPLICATION_ERROR(-20000, 'La linea ' ||  Cur_m_inoutline.line || ' producto: ' || Cur_m_inoutline.product || ', No tiene una ubicacion configurada') ; | `model/functions/SSRS_LOAD_TEMPLATE.xml` |
| `ssrs_requestreaprline_trg` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSRS_REQUESTREAPRLINE_TRG.xml` |
| `ssrs_requestreaprline_trg2` | — | Does not allow to change the attribute set value; for products which attribute set value type is Fixed | Does not allow to change the attribute set value; for products which attribute set value type is Fixed | `model/functions/SSRS_REQUESTREAPRLINE_TRG2.xml` |
| `ssrs_requestreaprovision` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSRS_REQUESTREAPROVISION.xml` |
| `ssrs_resupply_complete_pos` | Procesar | Ya existe un movimiento con el numero de documento; Recupera si hay algun error en esta función; Si no hay ningun error en la funcion entra; v_documentSends - documento para quien envia | Ya existe un movimiento con el numero de documento; Recupera si hay algun error en esta función; Si no hay ningun error en la funcion entra; v_documentSends - documento para quien envia; v_documentTransaction - Es de la matriz quien va a sacar para mi bodega; VALIDACION DEL NUMERO DE DOCUMENTO EN LA M_MOVEMENT | `model/functions/SSRS_RESUPPLY_COMPLETE_POS.xml` |
| `ssrs_resupply_new_post` | Post Resupply | INICIO IF VERIFICAR SI HAY REGISTROS EN REAPROVISIONAMIENTO PDV; INICIO LOOP BUSQUEDA DE LAS LINEAS DEL PEDIDO; INICIO CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODEGA DE LA CABECERA; SE ACRTUALIZA LAS LI… | INICIO IF VERIFICAR SI HAY REGISTROS EN REAPROVISIONAMIENTO PDV; INICIO LOOP BUSQUEDA DE LAS LINEAS DEL PEDIDO; INICIO CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODEGA DE LA CABECERA; SE ACRTUALIZA LAS LINEAS DEL PEDIDO DE REAPROVISIONAMIENTO PDV; CANTIDAD DESPACHADA PRINCIPAL Y CANTIDAD SECUNDARIA PEDIDA; FIN CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODEGA DE LA CABECERA | `model/functions/SSRS_RESUPPLY_NEW_POST.xml` |
| `ssrs_resupply_post` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSRS_RESUPPLY_POST.xml` |
| `ssrs_resupplyline_status` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSRS_RESUPPLYLINE_STATUS.xml` |
| `ssrs_resupplypos_post` | Post Resupply POS | Si el documento está completado y exista tercero en el; Sí este usuaro esta bloqueado o en bloqueo; Recoger datos de las lineas de la transaccion; almacena datos del tercero asociado al registro | Si el documento está completado y exista tercero en el; Sí este usuaro esta bloqueado o en bloqueo; Recoger datos de las lineas de la transaccion; almacena datos del tercero asociado al registro; Sí el usuario está bloqueado o en bloqueo; Cuenta que los productos de la linea sean genericos | `model/functions/SSRS_RESUPPLYPOS_POST.xml` |
| `ssrs_validateresupply_pos` | — | Validación reutilizable de campos. | — | `model/functions/SSRS_VALIDATERESUPPLY_POS.xml` |
| `ssrs_view_lot_details` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSRS_VIEW_LOT_DETAILS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cargar Plantilla | `Ssrs_Load_Template` | Botón (PL/pgSQL) | PL `ssrs_load_template` | N | BUSCO EL PADRE DE LA ORGANIZACION DEL INVENTARIO; LA ORGANIZACION PADRE DEL INVENTARIO DEBE DE SER; RAISE_APPLICATION_ERROR(-20000, 'La linea ' || Cur_m_inoutline.line || ' product |
| 2 | Post Resupply | `Ssrs_Resupply_Post` | Botón (PL/pgSQL) | PL `Ssrs_Resupply_New_Post` | N | INICIO IF VERIFICAR SI HAY REGISTROS EN REAPROVISIONAMIENTO PDV; INICIO LOOP BUSQUEDA DE LAS LINEAS DEL PEDIDO; INICIO CONTADOR PARA VERIFICAR QUE HAY STOCK DEL PRODUCTO EN LA BODE |
| 3 | Post Resupply POS | `Ssrs_ResupplyPos_Post` | Botón (PL/pgSQL) | PL `ssrs_resupplypos_post` | N | Si el documento está completado y exista tercero en el; Sí este usuaro esta bloqueado o en bloqueo; Recoger datos de las lineas de la transaccion; almacena datos del tercero asocia |
| 4 | Procesar | `Ssrs_Action_Complete` | Botón (PL/pgSQL) | PL `ssrs_resupply_complete_pos` | N | Ya existe un movimiento con el numero de documento; Recupera si hay algun error en esta función; Si no hay ningun error en la funcion entra; v_documentSends - documento para quien  |
| 5 | ssrs_PrintRessuply | `ssrs_PrintRessuply` | Reporte | Java `Ssrs_PrintReportFinalResupply` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |

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

Módulo: `ec.com.sidesoft.localization.ecuador.resupply`.

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

# Glosario — prefijo `SSRS`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSRS` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.ecuador.resupply` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Ssrs_Load_Template` — Cargar Plantilla
- `Ssrs_Resupply_Post` — Post Resupply
- `Ssrs_ResupplyPos_Post` — Post Resupply POS
- `Ssrs_Action_Complete` — Procesar
- `GuideRemission` — Guía de Remisión
- `pickinglist` — Picking List
- `ResupplyConsolidated` — Resupply Consolidated
- `ssrs_PrintRessuply` — ssrs_PrintRessuply

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
