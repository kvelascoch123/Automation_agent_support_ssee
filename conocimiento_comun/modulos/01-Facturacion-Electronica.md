# Openbravo Sidesoft — Facturación Electrónica

> Emisión de facturas, notas de crédito/débito, comprobantes electrónicos (SRI), portal web de facturación y documentos de prueba.

**Paquetes incluidos (10):**
- `com.sidesoft.localization.ecuador.invoices` — Localization of Ecuador - Invoices
- `com.sidesoft.localization.custom.invoices` — Customization Localization of Ecuador - Invoices Modules
- `ec.com.sidesoft.custom.facturae.portalweb` — Custom Electronic Invoice
- `ec.cusoft.facturaec` — Ecuador Electronic Invoicing
- `ec.com.sidesoft.facturaec.test` — Invoice Test
- `ec.com.sidesoft.creditNoteRefenence` — Credit Note Reference for Invoices Module
- `ec.com.sidesoft.financialcreditnote.sales.auto` — Financial Credit Note Sales Auto
- `ec.com.sidesoft.invoice.updatedescription` — Update Fiel Invoice Description
- `ec.com.sidesoft.custom.signature` — Sidesoft Custom Signature for Document Type
- `ec.com.sidesoft.doctypeByUser` — Document Type for User


---
## Localization of Ecuador - Invoices
**Package:** `com.sidesoft.localization.ecuador.invoices`

# Module overview — Localization of Ecuador - Invoices

## Functional

El módulo 'Localization of Ecuador - Invoices' está diseñado para gestionar la facturación de compras y ventas en Ecuador. Su principal objetivo es facilitar la creación, manejo y consolidación de facturas, asegurando el cumplimiento de normativas locales. Los actores involucrados incluyen usuarios de negocio que emiten facturas, personal de soporte que brinda asistencia y desarrolladores que implementan nuevas funcionalidades. Este módulo depende del '2.50 to 3.00 Compatibility Skin' para su correcto funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/localization/ecuador/invoices` |
| Web | `web/com.sidesoft.localization.ecuador.invoices/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SFPSI`

# Guía de chat — Localization of Ecuador - Invoices

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.localization.ecuador.invoices`).

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

- ¿Cómo puedo consolidar un pedido de venta?
- ¿Qué debo hacer si quiero rechazar una factura?
- ¿Cómo genero el reporte de compras por centro de costos?
- ¿Dónde encuentro la opción para emitir una nueva factura?
- ¿Qué datos necesito para importar una factura desde un archivo?
- ¿Cómo puedo verificar el estado de una factura emitida?
- ¿Es posible modificar una factura después de emitirla?
- ¿Qué tipos de validaciones se aplican al crear una factura?

# Domain — data model

## Functional

La entidad cabecera principal de este módulo es 'C_Invoice', que almacena información relevante sobre cada factura emitida. Cada factura puede contener múltiples detalles, como líneas de factura que representan los productos o servicios vendidos. Las relaciones entre las facturas y sus líneas se manejan a través de claves foráneas, permitiendo una estructuración clara de la información. Aunque no se especifican triggers en el inventario, el módulo incluye una función PL que permite la importación de facturas, asegurando que los datos se integren correctamente en el sistema.

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
| `sfpsi_reconcile_so_v` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_INVOICE`

### Views

`SFPSI_RECONCILE_SO_V`

# Functional — windows and menus

## Functional

El módulo cuenta con una ventana principal titulada 'Consolidar pedidos de venta', accesible desde el menú principal. A través de esta ventana, los usuarios pueden gestionar y consolidar pedidos de ventas que se han transformado en facturas, utilizando una interfaz que facilita la navegación y la selección de documentos pertinentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.localization.ecuador.invoices.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Consolidar pedidos de venta | Consolidate sales orders |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Compras efectuadas por Proveedor | Purchases by Provider | No |
| Cuentas Financieras | Financial Account | No |
| Detalle de Factura de Ventas | Details Sales Invoice | No |
| Detalle de Ventas | Sales Detail | No |
| Detalle de ventas | Sales detail | No |
| Orden de Compra VS Factura de Compra | Purchase Order Vs Purchase Invoice | No |
| Reconciliación de Compras | Purchase Reconcile | No |
| Reconciliación de Compras Dinamico | Reconciliación de Compras Dinamico | No |
| Reporte de Ventas por periodo | Sales Reconcile | No |
| Reporte General de Compras por Centro por Costos | General Purchase Report by Cost Center | No |
| Resumen de Factura de Ventas | Resume Sales Invoice | No |
| Resumen de ventas | Sales resume | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.localization.ecuador.invoices.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Consolidar pedidos de venta

- **AD_WINDOW_ID:** `B83335E3970E4EFE8103FEADA1F9F5DC`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `AD9AE35B23144CFEA6DB75FAE4006690` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `263`

- **AD_TAB_ID:** `263` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 0 | Consolidate | `EM_Sfpsi_Reconcile` | No | No | — |
| 2230 | Canceled Document | `EM_SFPSI_Canceled_Document` | No | Sí | — |

### Header (ventana: Consolidar pedidos de venta)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 110 | Sales Order | `C_Order_ID` | No | Sí | — |
| 120 | Sales Order Line | `C_Orderline_ID` | No | Sí | — |
| 130 | Product | `M_Product_ID` | No | Sí | — |
| 140 | UOM | `C_Uom_ID` | No | Sí | — |
| 150 | Ordered Quantity | `Qtyordered` | No | Sí | — |
| 160 | Invoiced Quantity | `Qtyinvoiced` | No | Sí | — |
| 170 | Quantity | `Qty` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dentro del módulo, los usuarios pueden encontrar hasta 11 botones de proceso, que permiten completar acciones como la consolidación de pedidos, aceptación o rechazo de facturas. Además, el módulo ofrece un informe titulado 'Reporte General de Compras por Centro por Costos', el cual facilita la visualización y análisis de datos relacionados con las compras a través de diferentes centros de costos. Las validaciones frecuentes aseguran que los campos requeridos estén debidamente completados antes de aprobar una factura.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.localization.ecuador.invoices.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Compras efectuadas por Proveedor | Purchases by Provider | C_Purchases_by_Provider | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Cuentas Financieras | Financial Accounts | c_financial_accounts | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de Factura de Ventas | Details Sales Invoice | C_Details_Sales_Invoice | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de ventas | Details Sales Invoice V2 | C_Details_Sales_Invoice_V2 | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de Ventas | Sales Detail | Sales Detail | *(OBUIAPP / manual)* | Sales Detail | — |
| Proceso / otro | Orden de Compra VS Factura de Compra | Purchase Order Vs Purchase Invoice | Purchase Order Vs Purchase Invoice | *(OBUIAPP / manual)* | Purchase Order Vs Purchase Invoice | — |
| Proceso / otro | Reconciliación de Compras | Purchase Reconcile | C_Purchase_Reconcile | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reconciliación de Compras Dinamico | C_Purchase_Reconcile_Dynamic | C_Purchase_Reconcile_Dynamic | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de Ventas por periodo | Sales Reconcile | C_Sales_Reconcile | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Resume Sales Invoice | Resume Sales Invoice | C_Resume_Sales_Invoice | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Resumen de ventas | Resume Sales Invoice V2 | C_Resume_Sales_Invoice_V2 | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Reporte General de Compras por Centro por Costos | General Purchase Report by Cost Center | General Purchase Report by Cost Center | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Compras efectuadas por Proveedor | Purchases by Provider | C_Purchases_by_Provider | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Cuentas Financieras | Financial Accounts | c_financial_accounts | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de Factura de Ventas | Details Sales Invoice | C_Details_Sales_Invoice | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de ventas | Details Sales Invoice V2 | C_Details_Sales_Invoice_V2 | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de Ventas | Sales Detail | Sales Detail | *(OBUIAPP / manual)* | Sales Detail | — |
| Proceso / otro | Orden de Compra VS Factura de Compra | Purchase Order Vs Purchase Invoice | Purchase Order Vs Purchase Invoice | *(OBUIAPP / manual)* | Purchase Order Vs Purchase Invoice | — |
| Proceso / otro | Reconciliación de Compras | Purchase Reconcile | C_Purchase_Reconcile | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reconciliación de Compras Dinamico | C_Purchase_Reconcile_Dynamic | C_Purchase_Reconcile_Dynamic | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de Ventas por periodo | Sales Reconcile | C_Sales_Reconcile | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Resume Sales Invoice | Resume Sales Invoice | C_Resume_Sales_Invoice | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Resumen de ventas | Resume Sales Invoice V2 | C_Resume_Sales_Invoice_V2 | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Compras efectuadas por Proveedor | Purchases by Provider | — | — | — |
| Proceso / otro | Cuentas Financieras | Financial Accounts | — | — | — |
| Proceso / otro | Detalle de Factura de Ventas | Details Sales Invoice | — | — | — |
| Proceso / otro | Detalle de ventas | Details Sales Invoice V2 | — | — | — |
| Proceso / otro | Detalle de Ventas | Sales Detail | — | Sales Detail | — |
| Proceso / otro | Orden de Compra VS Factura de Compra | Purchase Order Vs Purchase Invoice | — | Purchase Order Vs Purchase Invoice | — |
| Proceso / otro | Reconciliación de Compras | Purchase Reconcile | — | — | — |
| Proceso / otro | Reconciliación de Compras Dinamico | C_Purchase_Reconcile_Dynamic | — | — | — |
| Proceso / otro | Reporte de Ventas por periodo | Sales Reconcile | — | — | — |
| Proceso / otro | Resume Sales Invoice | Resume Sales Invoice | — | — | — |
| Proceso / otro | Resumen de ventas | Resume Sales Invoice V2 | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Reporte General de Compras por Centro por Costos | General Purchase Report by Cost Center | General Purchase Report by Cost Center | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 18**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **1**; archivos `*.jrxml` en el repo = **18**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Reporte General de Compras por Centro por Costos | `General Purchase Report by Cost Center` | — | *(ver AD_PROCESS_PARA / servlet)* | General Purchase Report by Cost Center |

### Plantillas sin proceso en diccionario

- `src/com/sidesoft/localization/ecuador/invoices/reports/RptC_GeneralDetailPurchase.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/Rpt_SalesDetail.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_ details_sales_invoices.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_ resume_sales_invoices.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_details_sales_invoices.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_details_sales_invoices_v2.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_purchase_by_provider.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_purchase_order_vs_purchase_invoice.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_purchase_reconcile.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_purchase_reconcile_2.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_purchase_reconcile_totals.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_resume_sales_invoices.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_resume_sales_invoices_v2.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_sales_reconcile.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_sales_reconcile_detailed.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_sales_reconcile_general.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_sales_reconcile_general_ivas.jrxml`
- `src/com/sidesoft/localization/ecuador/invoices/reports/c_sales_reconcile_general_ivatable.jrxml`
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

El módulo contiene clases Java que manejan acciones como la consolidación de pedidos de venta, proporcionando lógica adicional que se integra con las operaciones del módulo en Openbravo, facilitando la gestión automatizada de la información y la interacción con la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.localization.ecuador.invoices`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Sfpsi_ConsolidateSalesOrder` | action_handler | BaseProcessActionHandler | — | `src/com/sidesoft/localization/ecuador/invoices/action_handler/Sfpsi_ConsolidateSalesOrder.java` |
| `ImportProvideInvoice` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/invoices/ad_process/ImportProvideInvoice.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Validate User` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Process C_DocType AR/AP Purchase` | `C_DocType.DocBaseType IN ('ARI', 'API','ARC','APC','ARI_RM') AND C_DocType.IsSOTrx='N' AND (AD_ISORGINCLUDED(@#AD_Org_ID` |
| AD_VAL_RULE | — | `Process C_DocType AR/AP Sales` | `C_DocType.DocBaseType IN ('ARI' , 'ARC' , 'ARI_RM') AND (C_DocType.DocBaseType = @DocBaseType@ OR COALESCE(@DocBaseType@` |
| AD_VAL_RULE | — | `Process C_DocType AR/AP` | `C_DocType.DocBaseType IN ('ARI', 'API','ARC','APC','ARI_RM') AND C_DocType.IsSOTrx='N' AND (AD_ISORGINCLUDED(@#AD_Org_ID` |
| AD_VAL_RULE | — | `SFPSI_C_TAX` | `C_TAX.ISTAXDEDUCTABLE='Y'  or C_TAX.ISTAXUNDEDUCTABLE='Y'` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers no están presentes en este módulo, pero la función PL relacionada juega un rol crucial en la importación de facturas, facilitando la manipulación y validación de datos en la base de datos. Esto es vital para el soporte, ya que ayuda a mantener la integridad de la información y permite la automatización de ciertos procesos complejos.

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
| `sfpsi_consolidate_psd` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SFPSI_CONSOLIDATE_PSD.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Reporte General de Compras por Centro por Costos | `General Purchase Report by Cost Center` | Reporte | — | S | — |

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

Módulo: `com.sidesoft.localization.ecuador.invoices`.

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

# Glosario — prefijo `SFPSI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SFPSI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.localization.ecuador.invoices` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `C_Purchases_by_Provider` — Compras efectuadas por Proveedor
- `c_financial_accounts` — Cuentas Financieras
- `C_Details_Sales_Invoice` — Detalle de Factura de Ventas
- `C_Details_Sales_Invoice_V2` — Detalle de ventas
- `Sales Detail` — Detalle de Ventas
- `Purchase Order Vs Purchase Invoice` — Orden de Compra VS Factura de Compra
- `C_Purchase_Reconcile` — Reconciliación de Compras
- `C_Purchase_Reconcile_Dynamic` — Reconciliación de Compras Dinamico
- `C_Sales_Reconcile` — Reporte de Ventas por periodo
- `C_Resume_Sales_Invoice` — Resume Sales Invoice
- `C_Resume_Sales_Invoice_V2` — Resumen de ventas
- `General Purchase Report by Cost Center` — Reporte General de Compras por Centro por Costos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Customization Localization of Ecuador - Invoices Modules
**Package:** `com.sidesoft.localization.custom.invoices`

# Module overview — Customization Localization of Ecuador - Invoices Modules

## Functional

El módulo de Personalización de Localización de Ecuador para Facturas tiene como propósito adaptar el sistema ERP Openbravo a las normativas fiscales y comerciales específicas de Ecuador. Está diseñado para ser utilizado por los usuarios de negocio que gestionan la facturación, por el soporte de segundo nivel (L2) que brinda asistencia técnica, y por desarrolladores que personalizan y extienden las funcionalidades del ERP. Este módulo se encuentra dentro del ámbito de administración de facturas, que es crítico para la gestión financiera de cualquier organización. Su uso depende de la correcta instalación y configuración de la versión 2.50 a 3.00 del skin de compatibilidad, lo que garantiza la correcta visualización e interactividad del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/localization/custom/invoices` |
| Web | `web/com.sidesoft.localization.custom.invoices/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLCI`

# Guía de chat — Customization Localization of Ecuador - Invoices Modules

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.localization.custom.invoices`).

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

- ¿Cómo puedo adaptar el módulo de facturación a las normativas ecuatorianas?
- ¿Qué debo hacer si tengo errores al crear una factura?
- ¿Cómo puedo verificar el estado de mis facturas en el sistema?
- ¿Existen informes disponibles para el seguimiento de la facturación?
- ¿Qué validaciones se hacen automáticamente en las facturas generadas?
- ¿Cómo se actualizan los datos de impuestos en el sistema?
- ¿Qué pasos debo seguir para personalizar la interfaz del módulo?
- ¿Cómo configuro la integración de inventarios con las facturas?

# Domain — data model

## Functional

El modelo de datos del módulo involucra la entidad cabecera C_INVOICE, que representa las facturas generadas. Además, se han realizado modificaciones en las tablas M_INOUT y M_WAREHOUSE relacionadas con el manejo de productos y almacenes. Estos cambios aseguran la alineación con las particularidades de la gestión de inventario y facturación en Ecuador. Aunque no existen triggers definidos, la función PL relacionada contribuye a la lógica de validación y procesamiento de facturas. Es esencial comprender las relaciones de estas tablas para una adecuada gestión de datos y cumplimiento regulatorio.

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

`C_INVOICE`, `M_INOUT`, `M_WAREHOUSE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo carece de ventanas definidas en su inventario, indicando que su implementación podría depender de personalizaciones adicionales o de la integración con otros módulos existentes en Openbravo. Los usuarios navegarían a través del sistema utilizando las funcionalidades generales del ERP, accediendo a los registros de facturación desde la interfaz estándar, aunque esta especificidad del módulo no se refleja en ventanas individuales.

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

### Pestaña `177`

- **AD_TAB_ID:** `177` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 120 | Is Consignment | `EM_Slci_Isconsignment` | No | No | — |

### Pestaña `257`

- **AD_TAB_ID:** `257` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 75 | Shipper | `EM_Slci_Shipper_ID` | No | No | — |

### Pestaña `263`

- **AD_TAB_ID:** `263` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 123 | Shipper | `EM_Slci_Shipper_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo no presenta botones de proceso específicos ni informes definidos, lo cual sugiere que el flujo de trabajo se integra dentro de los procesos generales de facturación de Openbravo. Los usuarios son responsables de completar, retornar o rechazar las facturas según las necesidades del negocio, utilizando las herramientas estándares del ERP. Las validaciones frecuentes pueden incluir comprobaciones de formato de identificación fiscal y cumplimiento de requisitos tributarios locales.

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

El módulo no incluye clases Java, lo que limita su capacidad de personalización a nivel de desarrollo, dejando el enfoque más dependiente de funcionalidades existentes en el entorno de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.localization.custom.invoices`.

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

A pesar de no contar con triggers, la función PL presente juega un rol crítico en el soporte del módulo, garantizando que las facturas sigan las normas legales y fiscales al ser almacenadas y procesadas. Esta función es clave para la integridad y la validez de la información financiera registrada en el sistema.

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
| `slci_date_name_month` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SLCI_DATE_NAME_MONTH.xml` |
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

Módulo: `com.sidesoft.localization.custom.invoices`.

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

# Glosario — prefijo `SLCI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLCI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.localization.custom.invoices` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Custom Electronic Invoice
**Package:** `ec.com.sidesoft.custom.facturae.portalweb`

# Module overview — Custom Electronic Invoice

## Functional

El módulo 'Custom Electronic Invoice' tiene como propósito facilitar la emisión de facturas electrónicas para el mercado ecuatoriano. Está diseñado para ser utilizado por usuarios de negocio que crean y gestionan facturas, así como por el equipo de soporte técnico que garantiza su correcto funcionamiento. El alcance del módulo incluye la integración con el sistema de facturación existente en Openbravo y depende de otros módulos como 'Ecuador Electronic Invoicing'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/facturae/portalweb` |
| Web | `web/ec.com.sidesoft.custom.facturae.portalweb/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Ecuador Electronic Invoicing

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`CEEI`

# Guía de chat — Custom Electronic Invoice

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.facturae.portalweb`).

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

- ¿Cómo creo una factura electrónica desde el módulo?
- ¿Qué debo hacer si la factura no se envía correctamente?
- ¿Dónde puedo ver el historial de facturas que he emitido?
- ¿Cómo actualizo la información de un socio comercial?
- ¿Qué validaciones se realizan antes de enviar la factura electrónica?
- ¿Cómo reviso si se ha confirmado el envío de mi factura?
- ¿Puedo modificar una factura una vez que ha sido enviada?
- ¿Qué hacer si hay un error en la información de una factura ya emitida?

# Domain — data model

## Functional

Este módulo incluye una entidad cabecera asociada a las facturas electrónicas, con un único campo para gestionar la información relacionada. Las etapas del proceso son sencillas, comenzando con la creación de la factura, seguido por su validación y envío. La relación principal se establece a través de la tabla 'c_bpartner' a la cual se le aplica un trigger clave 'CEEI_BPARTNER_TRG' para manejar la lógica de negocio cuando se actualizan los datos de los socios comerciales.

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

`CEEI_EDOCUMENTS`, `CEEI_EDOCUMENTS_PDF`, `CEEI_EDOCUMENTS_XML`

# Functional — windows and menus

## Functional

El módulo se presenta a través de un menú que permite a los usuarios acceder directamente a las funciones necesarias para la gestión de facturas electrónicas. Aunque no hay ventanas específicas definidas en el inventario, la navegación se realiza mediante opciones del menú que permiten completar, retornar o rechazar documentos electrónicos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.facturae.portalweb.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Generar Claves de Acceso al Portal Web | Generate Keys Access Portal Web | No |
| Portal Web | Portal Web | Sí |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.facturae.portalweb.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `223`

- **AD_TAB_ID:** `223` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 310 | Portal Password | `—` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo cuenta con un proceso que incluye un botón para completar la generación de la factura electrónica. Durante este proceso, se realizan validaciones frecuentes para asegurar que toda la información requerida esté correcta antes del envío. Aunque no se especifican informes asociados, es posible que se requieran verificaciones de estado y confirmaciones de envío a través de otras herramientas del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.facturae.portalweb.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Generate Keys Portal Web | Generate Keys Portal Web | Generate Keys Portal Web | `ceei_generatekeys_portalweb` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| Botón (PL/pgSQL) | Generate Keys Portal Web | Generate Keys Portal Web | Generate Keys Portal Web | `ceei_generatekeys_portalweb` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Generate Keys Portal Web | Generate Keys Portal Web | PL `ceei_generatekeys_portalweb` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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

No se especifican clases Java dentro de este módulo, por lo que su funcionalidad se basa principalmente en la lógica de backend a través de PL/pgSQL y triggers.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.facturae.portalweb`.

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
| Trigger `CEEI_BPARTNER_TRG` | `c_bpartner` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL son cruciales para el soporte del módulo, especialmente el trigger 'CEEI_BPARTNER_TRG' que se ejecuta para asegurar que los cambios realizados en la tabla de socios comerciales se gestionen adecuadamente y que las reglas del negocio se apliquen conforme a lo previsto. La función PL especificada en el módulo también desempeña un papel esencial en la implementación de la lógica de procesos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `CEEI_BPARTNER_TRG` | `c_bpartner` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/CEEI_BPARTNER_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ceei_generatekeys_portalweb` | Generate Keys Portal Web | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/CEEI_GENERATEKEYS_PORTALWEB.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Generate Keys Portal Web | `Generate Keys Portal Web` | Botón (PL/pgSQL) | PL `ceei_generatekeys_portalweb` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

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

Módulo: `ec.com.sidesoft.custom.facturae.portalweb`.

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

# Glosario — prefijo `CEEI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `CEEI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.facturae.portalweb` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Generate Keys Portal Web` — Generate Keys Portal Web

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Ecuador Electronic Invoicing
**Package:** `ec.cusoft.facturaec`

# Module overview — Ecuador Electronic Invoicing

## Functional

El módulo de Facturación Electrónica de Ecuador (ec.cusoft.facturaec) permite a las empresas emitir facturas electrónicas cumpliendo con la normativa local (CFDI). Este módulo está diseñado para usuarios de negocio que necesitan gestionar las facturas, así como para el equipo de soporte de nivel 2 y desarrolladores que requieren entender su estructura técnica. La implementación del módulo depende de otros componentes como el Core, la Localización de Ecuador, y los Descuentos de Sidesoft. Los actores principales son los usuarios de las empresas que emiten facturas y el personal técnico encargado de mantener el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/cusoft/facturaec` |
| Web | `web/ec.cusoft.facturaec/` |

### Declared dependencies

- Core
- Localization of Ecuador - Withholdings
- Sidesoft Discounts Invoice

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`EEI`

# Guía de chat — Ecuador Electronic Invoicing

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.cusoft.facturaec`).

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
- «¿Qué es la tabla eei_format?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo generar una factura electrónica?
- ¿Qué debo hacer si tengo un error al enviar una factura?
- ¿Dónde puedo consultar el historial de facturas electrónicas?
- ¿Cómo se configuran las cuentas bancarias para recibir pagos?
- ¿Qué informes puedo generar desde el módulo de facturación electrónica?
- ¿Cómo valido si una factura fue aceptada por la entidad fiscal?
- ¿Qué parámetros configuran la emisión de facturas electrónicas?
- ¿Cómo recupero el número de autorización de una factura electrónica?

# Domain — data model

## Functional

El modelo de datos se basa en la entidad cabecera de la factura (C_INVOICE) y su relación con otros elementos como tasas impositivas (C_INVOICETAX) y tipos de documentos (C_DOCTYPE). El flujo de trabajo incluye procesos como la autorización de facturas y la validación de datos. Los triggers como EEI_CHECK_CREDITNOTE_INV_REF verifican referencias de notas de crédito, y EEI_VLD_INVOICE_NUM_REF asegura la validez del número de factura referente, entre otros. Estas relaciones son claves para mantener la integridad de los procesos contables y fiscales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `eei_bank_account` |
| `eei_contingency` |
| `eei_format` |
| `eei_invoicelog` |
| `eei_mailserver` |
| `eei_param_facturae` |
| `eei_platform` |
| `eei_product` |
| `eei_remissionguidelog` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `eei_bank_account` | eei_bank_account | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `eei_bank_account_key`; Cols: name, account |
| `eei_contingency` | EEI_Contingency | — | `EEI_CONTINGENCY_VALUE` (contingence_key) | c_invoice_id→c_invoice; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_invoice. | PK `eei_contingence_key`; Cols: contingence_key, status, c_invoice_id |
| `eei_format` | EEI_Format | — | `EEI_FORMAT_UK1` (value, ad_org_id, ad_client_id) | ad_client_id→ad_client; ad_org_id→ad_org; createdby→ad_user; updatedby→ad_user | Detalle enlazado a ad_client, ad_org, ad_user. | PK `eei_format_pk`; Cols: value, name |
| `eei_invoicelog` | EEI_Invoicelog | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoice_id→c_invoice | Detalle enlazado a ad_client, ad_org, c_invoice. | PK `eei_invoicelog_key`; Cols: line, c_invoice_id, logtype, description, edoc_type; idx `EEI_INVOICEID_IDX` (c_invoice_id); idx `EEI_LINE_IDX` (line) |
| `eei_mailserver` | EEI_MailServer | — | `EEI_MAILSERVER_NAME_UN` (ad_client_id, name) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `eei_mailserver_key`; Cols: name, description, servername, requiretls, requiressl; `EEI_MAILSERVER_IA`: ISACTIVE IN ('Y', 'N'); `EEI_MAILSERVER_SSL`: ISACTIVE IN ('Y', 'N') (+1) |
| `eei_param_facturae` | EEI_Param_Facturae | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `eei_param_facturae_key`; Cols: description, url_ws_validacion, url_ws_autorizacion, dir_certificado, password; `EEI_KEYACCESS_GEN_CHECK`: KEYACCESS_GENERATION IN ('Y', 'N'); `EEI_SHOWAUXILIARYCODE_CHECK`: SHOWAUXILIARYCODE IN ('Y', 'N') (+1) |
| `eei_platform` | EEI_Platform | — | `EEI_PLATFORM_UK1` (value, ad_org_id, ad_client_id) | ad_client_id→ad_client; ad_org_id→ad_org; createdby→ad_user; updatedby→ad_user | Detalle enlazado a ad_client, ad_org, ad_user. | PK `eei_platform_pk`; Cols: value, name |
| `eei_product` | eei_product | — | — | ad_client_id→ad_client; ad_org_id→ad_org; m_product_id→m_product | Detalle enlazado a ad_client, ad_org, m_product. | PK `eei_product_p_key`; Cols: value, m_product_id, value_ie; `EEI_PRODUCT_ISACTIVES_CHK`: ISACTIVE IN ('Y', 'N') |
| `eei_remissionguidelog` | EEI_RemissionGuideLog | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_table_id→ad_table | Detalle enlazado a ad_client, ad_org, ad_table. | PK `eei_remguidelog_key`; Cols: line, ad_table_id, record_id, logtype, description |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `eei_bank_account` |
| `EEI_Contingency` |
| `EEI_Format` |
| `eei_invoice_logs_v` |
| `EEI_Invoicelog` |
| `EEI_MailServer` |
| `EEI_Param_Facturae` |
| `eei_payment_detail_v` |
| `EEI_Platform` |
| `eei_product` |
| `EEI_RemissionGuideLog` |
| `eei_view_invoice` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ORG`, `AD_USER`, `C_BPARTNER`, `C_DOCTYPE`, `C_INVOICE`, `C_INVOICETAX`, `C_TAX`, `FIN_PAYMENTMETHOD`, `M_INOUT`, `M_MOVEMENT`, `M_PRODUCT`, `M_WAREHOUSE`, `SSWH_TAXPAYER`

### Views

`EEI_INVOICE_LOGS_V`, `EEI_PAYMENT_DETAIL_V`, `EEI_VIEW_INVOICE`

# Functional — windows and menus

## Functional

El módulo se navega a través de una serie de ventanas en la interfaz de usuario, incluyendo 'Consulta Registro Histórico F.E.' y 'Formato Factura Electrónica'. Los usuarios pueden acceder a parámetros de configuración y a las cuentas bancarias necesarias para gestionar pagos y recepción de facturas electrónicas, facilitando así la emisión y el seguimiento de documentos fiscales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.cusoft.facturaec.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Consulta Registro Histórico F.E. | Query F.E. |
| Contingency Window | Contingency Window |
| Cuentas bancarias | Bank account |
| E.I. Product | E.I. Product |
| Formato Factura Electrónica | Formato Factura Electrónica |
| Parámetros Factura NEW | Parámetros Factura NEW |
| Plataforma Factura Electrónica New | Plataforma Factura Electrónica New |
| Servidor de Correos | Servidor de Correos |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración | Tools | Sí |
| Consulta Registro Histórico F.E. | Query F.E | No |
| Cuentas bancarias | Bank account | No |
| E.I. Product | E.I. Product | No |
| Facturación Electrónica | Facturación Electrónica | Sí |
| Formato Factura Electrónica | Formato Factura Electrónica | No |
| Parámetros de Facturación Electrónica | Parámetros de Facturación Electrónica | No |
| Plataforma Factura Electrónica New | Plataforma Factura Electrónica New | No |
| Reporte Retenciones | Report Withholdings | No |
| Servidor de Correos | Servidor de Correos | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.cusoft.facturaec.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Consulta Registro Histórico F.E.

- **AD_WINDOW_ID:** `04CC2ECCBEDD41AB927C60DA1FDECC88`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `CEC0CBF5980841149390F1C02847ECFC` | 0 |

### Ventana: Contingency Window

- **AD_WINDOW_ID:** `63472EF6C12C44C7807B7FE4B6BE8CDF`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Contingence Tab | `C1CF0673BF394774AAB8AFC461D5A9D3` | 0 |

### Ventana: Cuentas bancarias

- **AD_WINDOW_ID:** `DA99A64D3C904E4FB492A8257019E779`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `10351BDC492348AABFDFDE7F59A9B5E0` | 0 |

### Ventana: E.I. Product

- **AD_WINDOW_ID:** `EC9662AF1F894CFC81DF74F147D7FDCE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Electronic Invoice Product | `4C0F3872427C4EE380C7033850A1CDC3` | 0 |

### Ventana: Formato Factura Electrónica

- **AD_WINDOW_ID:** `2738072CB53D43AA9707308076D98EA2`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Formato Factura Electrónica | `DD588EB35B424ACCA3E42CE42F26F6E8` | 0 |

### Ventana: Parámetros Factura NEW

- **AD_WINDOW_ID:** `69F7EE0CB28A4CAEB48471420EF50BA9`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Parámetros Facturación Electrónica | `C2FB6CBF58BF488B808B0F0C838B086D` | 0 |

### Ventana: Plataforma Factura Electrónica New

- **AD_WINDOW_ID:** `7DD9ABB550224FE58A22B4972F2A78A1`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Plataforma Factura Electrónica | `483A155CCF3841B490A2FD64E4EF7559` | 0 |

### Ventana: Servidor de Correos

- **AD_WINDOW_ID:** `6353E9D589C44350A55BF2343F379B96`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Servidor de Correos | `8733F1A9DC1C4BEFAAF39CC5A3EE2771` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Registro Histórico FE

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organización | `AD_Org_ID` | No | Sí | — |
| 40 | Línea | `Line` | No | Sí | — |
| 50 | Edoc_Type | `Edoc_Type` | No | No | — |
| 60 | Tipo de Log | `Logtype` | No | Sí | — |
| 70 | Descripción | `Description` | No | Sí | — |

### Pestaña `118`

- **AD_TAB_ID:** `118` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 300 | Correo Usuario | `EM_Eei_Emailuser` | No | No | 1FA7BB32D75B48249A11EEE5F97E2950 |
| 310 | Servidor de Correo Electrónico | `EM_Eei_Mailserver_ID` | No | No | 1FA7BB32D75B48249A11EEE5F97E2950 |

### Pestaña `143`

- **AD_TAB_ID:** `143` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 630 | EM_Eei_Show_Remission_Guide | `EM_Eei_Show_Remission_Guide` | No | No | — |
| 640 | Reactivate authorized documents | `EM_Eei_Reactivate_Auth_Docs` | No | No | — |
| 650 | Withholding agent | `EM_Eei_Withholding_Agent` | No | No | — |
| 655 | Micro business | `EM_Eei_Micro_Business` | No | No | — |
| 660 | Discount by pricelist | `EM_Eei_Discountbypricelist` | No | No | — |
| 667 | RIMPE REGIME | `EM_Eei_Rimpe` | No | No | — |

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 280 | Documento Electrónico | `EM_Eei_Is_Edoc` | No | No | — |
| 285 | Without Reference Invoice | `EM_Eei_No_Reference_Invoice` | No | No | — |
| 290 | Tipo de Documento Electrónico | `EM_Eei_Edoc_Type` | No | No | — |
| 293 | Remission for sales | `EM_Eei_Remission_For_Sales` | No | No | — |
| 294 | Key access generated | `EM_Eei_Key_Access_Generated` | No | No | — |
| 295 | EM_Eei_Descriptionfields | `EM_Eei_Descriptionfields` | No | No | — |
| 296 | EM_Eei_Isrefund | `EM_Eei_Isrefund` | No | No | — |
| 297 | EM_Eei_Refund_Code | `EM_Eei_Refund_Code` | No | No | — |
| 298 | EM_Eei_Comercial_Inv | `EM_Eei_Comercial_Inv` | No | No | — |

### Pestaña `174`

- **AD_TAB_ID:** `174` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 325 | Tipo de Impuesto SRI | `EM_Eei_Sri_Tax_Type` | No | No | — |
| 330 | Identificador SRI de Impuestos | `EM_Eei_Sri_Taxcat_Code` | No | No | — |
| 390 | Service/Tip | `EM_Eei_Tip` | No | No | — |
| 400 | No Electronic | `EM_Eei_No_Electronic` | No | No | — |

### Pestaña `177`

- **AD_TAB_ID:** `177` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 140 | EM_Eei_Identifier | `EM_Eei_Identifier` | No | No | — |

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 134 | EM_Eei_Alternativeidentifier | `EM_Eei_Alternativeidentifier` | No | No | — |

### Registro Histórico FE

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organización | `AD_Org_ID` | No | Sí | — |
| 40 | Línea | `Line` | No | Sí | — |
| 50 | Logtype | `Edoc_Type` | No | No | — |
| 60 | Tipo de Log | `Logtype` | No | Sí | — |
| 70 | Descripción | `Description` | No | Sí | — |

### Plataforma Factura Electrónica (ventana: Plataforma Factura Electrónica New)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organización | `AD_Org_ID` | No | No | — |
| 20 | Activo | `Isactive` | No | No | — |
| 30 | Clave | `Value` | No | No | — |
| 40 | Nombre | `Name` | No | No | — |

### Pestaña `223`

- **AD_TAB_ID:** `223` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 260 | Electronic document | `EM_EEI_Eeioice` | No | No | CED9F9D0C2754560BDDE16186770EDFD |
| 265 | Correo Electrónico | `EM_EEI_Email` | No | No | CED9F9D0C2754560BDDE16186770EDFD |

### Pestaña `224`

- **AD_TAB_ID:** `224` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 190 | Electronic document | `EM_EEI_Eeioice` | No | No | CED9F9D0C2754560BDDE16186770EDFD |
| 200 | Correo Electrónico | `EM_EEI_Email` | No | No | CED9F9D0C2754560BDDE16186770EDFD |

### Pestaña `257`

- **AD_TAB_ID:** `257` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 71 | Description electronic documents | `EM_Eei_Description` | No | No | — |
| 110 | EM_Eei_Dirorig | `EM_Eei_Dirorig` | No | No | FA5774F051064E9BA23EDAB2C90F3FEA |
| 120 | EM_Eei_Dirdest | `EM_Eei_Dirdest` | No | No | FA5774F051064E9BA23EDAB2C90F3FEA |
| 2050 | Generate Electronic Document | `EM_Eei_Send_To_Sri` | No | No | — |
| 2060 | EM_Eei_Codigo | `EM_Eei_Codigo` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2070 | EM_Eei_Numauto | `EM_Eei_Numauto` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2080 | EM_Eei_Fechaauto | `EM_Eei_Fechaauto` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2090 | EM_Eei_Status | `EM_Eei_Status` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2100 | EM_Eei_Urlxml | `EM_Eei_Urlxml` | No | No | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2110 | EM_Eei_Urlride | `EM_Eei_Urlride` | No | No | 1B2B018580834BF692AC8B0E0364EAA7 |

### Pestaña `259`

- **AD_TAB_ID:** `259` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 41 | Description electronic documents | `EM_Eei_Description` | No | No | — |
| 2050 | Generate Electronic Document | `EM_Eei_Send_To_Sri` | No | No | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2065 | EM_Eei_Codigo | `EM_Eei_Codigo` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2070 | EM_Eei_Numauto | `EM_Eei_Numauto` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2080 | EM_Eei_Fechaauto | `EM_Eei_Fechaauto` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2090 | EM_Eei_Status | `EM_Eei_Status` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2100 | EM_Eei_Urlxml | `EM_Eei_Urlxml` | No | No | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2110 | EM_Eei_Urlride | `EM_Eei_Urlride` | No | No | 1B2B018580834BF692AC8B0E0364EAA7 |

### Pestaña `263`

- **AD_TAB_ID:** `263` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 94 | Referencia Factura | `EM_Eei_Is_Inv_Ref` | No | No | — |
| 95 | Factura Referenciada | `EM_Eei_Ref_Inv_ID` | No | No | — |
| 118 | Description electronic documents | `EM_Eei_Description` | No | No | — |
| 2050 | Código de Acceso | `EM_Eei_Codigo` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2080 | Número de Autorización | `EM_Eei_Numauto` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2100 | Fecha de Autorización | `EM_Eei_Fechaautotext` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2140 | Status | `EM_Eei_Status` | No | Sí | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2150 | Url Xml | `EM_Eei_Urlxml` | No | No | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2160 | Url Ride | `EM_Eei_Urlride` | No | No | 1B2B018580834BF692AC8B0E0364EAA7 |
| 2180 | Generate Electronic Document | `EM_Eei_Generate_Offline` | No | No | — |
| 3000 | Voucher code | `EM_Eei_Voucher_Code` | No | No | 759AFE2CE1264084BB54CF048B481A99 |
| 3010 | Voucher Date | `EM_Eei_Voucher_Date` | No | No | 759AFE2CE1264084BB54CF048B481A99 |
| 3020 | Invoice Number | `EM_Eei_Invoice_Num` | No | No | 759AFE2CE1264084BB54CF048B481A99 |

### Pestaña `290`

- **AD_TAB_ID:** `290` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 106 | Description electronic documents | `EM_Eei_Description` | No | No | — |
| 540 | Habilitar Envio de Retencion | `EM_Eei_Withholding_Send` | No | No | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 2050 | Código de Acceso | `EM_Eei_Codigo` | No | Sí | 7B5BCF16CF25402A9887D06E67CF1E74 |
| 2080 | Número de Autorización | `EM_Eei_Numauto` | No | Sí | 7B5BCF16CF25402A9887D06E67CF1E74 |
| 2100 | Fecha Autorización | `EM_Eei_Fechaautotext` | No | Sí | 7B5BCF16CF25402A9887D06E67CF1E74 |
| 2140 | Status | `EM_Eei_Status` | No | Sí | 7B5BCF16CF25402A9887D06E67CF1E74 |
| 2150 | URL XML | `EM_Eei_Urlxml` | No | No | 7B5BCF16CF25402A9887D06E67CF1E74 |
| 2160 | URL RIDE | `EM_Eei_Urlride` | No | No | 7B5BCF16CF25402A9887D06E67CF1E74 |
| 2170 | Void Invoice | `EM_Eei_ResendInvoice` | No | No | 7B5BCF16CF25402A9887D06E67CF1E74 |
| 2180 | Generate Electronic Document | `EM_Eei_Generate_Offline` | No | No | 7B5BCF16CF25402A9887D06E67CF1E74 |
| 2190 | Access code purchase settlement | `EM_Eei_Codigo_2` | No | Sí | 637AC6CED2884B938045E190E8D6C22E |
| 2200 | Access code authorized purchase settlement | `EM_Eei_Numauto_2` | No | Sí | 637AC6CED2884B938045E190E8D6C22E |
| 2210 | Authorization datetime purchase settlement | `EM_Eei_Fechaautotext_2` | No | Sí | 637AC6CED2884B938045E190E8D6C22E |
| 2220 | Status purchase settlement | `EM_Eei_Status_2` | No | Sí | 637AC6CED2884B938045E190E8D6C22E |
| 2230 | URL XML purchase settlement | `EM_Eei_Urlxml_2` | No | No | 637AC6CED2884B938045E190E8D6C22E |
| 2240 | URL RIDE purchese settlement | `EM_Eei_Urlride_2` | No | No | 637AC6CED2884B938045E190E8D6C22E |
| 2260 | Generate electronic purchase settlement | `EM_Eei_Generate_Offline_2` | No | No | 637AC6CED2884B938045E190E8D6C22E |
| 2270 | Void electronic purchase settlement | `EM_Eei_Resendinvoice_2` | No | No | 637AC6CED2884B938045E190E8D6C22E |

### Parámetros Facturación Electrónica (ventana: Parámetros Factura NEW)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organización | `AD_Org_ID` | No | No | — |
| 20 | Activo | `Isactive` | No | No | — |
| 30 | Descripción | `Description` | No | No | — |
| 40 | Url_Ws_Validacion | `URL_Ws_Validacion` | No | No | — |
| 50 | Type of Batch | `Type_Of_Batch` | No | No | — |
| 60 | Showprincipalcode | `Showprincipalcode` | No | No | — |
| 70 | Showauxiliarycode | `Showauxiliarycode` | No | No | — |
| 75 | Product_Name | `Product_Name` | No | No | — |
| 80 | Timeout_Response | `Timeout_Response` | No | No | — |
| 90 | Default_Email | `Default_Email` | No | No | — |
| 110 | Ambiente | `Environment` | No | No | — |
| 120 | Keyaccess_Generation | `Keyaccess_Generation` | No | No | — |
| 130 | Country_Code | `Country_Code` | No | No | — |
| 140 | SQL_Attributes | `SQL_Attributes` | No | No | — |
| 150 | Adittional_Info | `Adittional_Info` | No | No | — |
| 160 | SQL_Attributes_Inout | `SQL_Attributes_Inout` | No | No | — |
| 170 | SQL_Attributes_Movement | `SQL_Attributes_Movement` | No | No | — |
| 180 | XML_Version | `XML_Version` | No | No | — |
| 180 | Extract_Client_Description | `Extract_Client_Description` | No | No | — |
| 190 | Send_Info_Special | `Send_Info_Special` | No | No | — |
| 200 | Max Date Generation | `MAX_Date_Generation` | No | No | — |

### Formato Factura Electrónica (ventana: Formato Factura Electrónica)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organización | `AD_Org_ID` | No | No | — |
| 20 | Activo | `Isactive` | No | No | — |
| 30 | Clave | `Value` | No | No | — |
| 40 | Nombre | `Name` | No | No | — |

### Servidor de Correos (ventana: Servidor de Correos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organización | `AD_Org_ID` | No | No | — |
| 30 | Activo | `Isactive` | No | No | — |
| 40 | Nombre | `Name` | No | No | — |
| 50 | Descripción | `Description` | No | No | — |
| 60 | Nombre del Servidor | `Servername` | No | No | — |
| 70 | Requiere TLS | `Requiretls` | No | No | — |
| 80 | Requiere SSL | `Requiressl` | No | No | — |
| 90 | Puerto | `Port` | No | No | — |

### Pestaña `6B2631C1D8FC4194ABC2BFA776FC8D68`

- **AD_TAB_ID:** `6B2631C1D8FC4194ABC2BFA776FC8D68` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | No Electronic | `EM_Eei_No_Electronic` | No | No | — |

### Electronic Invoice Product (ventana: E.I. Product)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | Sí | — |
| 40 | Product | `M_Product_ID` | No | No | — |
| 50 | Value_Ie | `Value_Ie` | No | No | — |

### Historical Record ED

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Line | `Line` | No | No | — |
| 60 | Logtype | `Logtype` | No | No | — |
| 70 | Description | `Description` | No | No | — |

### Pestaña `A4A463FA34F946BFA3F687DC8754ED93`

- **AD_TAB_ID:** `A4A463FA34F946BFA3F687DC8754ED93` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 310 | Payment Code FE | `em_eei_code_ei` | No | No | — |

### Header (ventana: Consulta Registro Histórico F.E.)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Organizationame | `Organizationame` | No | Sí | — |
| 40 | Doctypecode | `Doctypecode` | No | Sí | — |
| 50 | Doctype | `Doctype` | No | Sí | — |
| 60 | Documentno | `Documentno` | No | Sí | — |
| 70 | Bpartner | `Bpartner` | No | Sí | — |
| 80 | Dateinvoiced | `Dateinvoiced` | No | Sí | — |
| 90 | Accesskey | `Accesskey` | No | Sí | — |
| 100 | Description | `Description` | No | Sí | — |

### Header (ventana: Cuentas bancarias)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Name | `Name` | No | No | — |
| 40 | Account | `Account` | No | No | — |

### Historical Record ED

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | Line | `Line` | No | Sí | — |
| 60 | Logtype | `Logtype` | No | Sí | — |
| 70 | Description | `Description` | No | Sí | — |

### Contingence Tab (ventana: Contingency Window)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Activo | `Isactive` | No | Sí | — |
| 30 | Clave de Contingencia | `Contingence_Key` | No | No | — |
| 60 | Factura | `C_Invoice_Id` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos del módulo incluyen diversas funcionalidades como la generación de la factura electrónica, que se realiza mediante el proceso 'GenerateFE'. Existen botones típicos como 'Completar', 'Retornar' y 'Rechazar' que regulan el flujo de las facturas, permitiendo a los usuarios gestionar adecuadamente los documentos emitidos. Se generan informes como 'PRINT ELECTRONIC INVOICE' y 'PRINT WITHHOLDINGS ELECTRONIC', permitiendo así la emisión de reportes necesarios para cumplir con las normativas fiscales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.cusoft.facturaec.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar liquidación compra electrónica | Generate purchase settlement | EM_Eei_Generate_Offline_2 | Java `GeneratePurchaseSettlement` (AD_MODEL_OBJECT `P`) | Proceso Openbravo ver `doExecute` en fuente | `src/ec/cusoft/facturaec/ad_process/GeneratePurchaseSettlement.java` |
| Botón (Java) | Generate Document Electronic (Movement) | Generate Document Electronic (Movement) | Generate Document Electronic | Java `Generate_Movement` (AD_MODEL_OBJECT `P`) | Proceso Openbravo El formato del RUC es incorrecto. | `src/ec/cusoft/facturaec/ad_process/Generate_Movement.java` |
| Botón (PL/pgSQL) | Anular liquidación compra electrónica | Void electronic purchase settlement | Void electronic purchase settlement | `eei_void_purchase_settlement` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Anular retención electrónica | Void Invoice | Eei_VoidInvoice | `eei_voidinvoice` | Inicio: Almacenar en ventana Retenciones anuladas; Fin : Almacenar en ventana Retenciones anuladas; eei_voidinvoice - Finish_Process Extension Point | — |
| Informe (servlet) | Generar documento electrónico | Generate Electronic Document | Eei_Generate_EDocument | Java `GenerateFE` (AD_MODEL_OBJECT `S`) | Proceso Openbravo Fecha Retención no seleccionada. | `src/ec/cusoft/facturaec/ad_process/GenerateFE.java` |
| Informe (servlet) | Generate Electronic Document (InOut) | Generate Electronic Document (InOut) | EEI_GenerateRemissionGuide | Java `Generate_Remission_Guide` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `M_InOut_ID` | `src/ec/cusoft/facturaec/ad_process/Generate_Remission_Guide.java` |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | PRINT ELECTRONIC INVOICE | PRINT ELECTRONIC INVOICE | PRINT ELECTRONIC INVOICE | Java `ReportPrintElectronicInvoice` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptC_Invoice_Electronic.jrxml`; contexto sesión `—`. | `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/ReportPrintElectronicInvoice.java` |
| Reporte | PRINT WITHHOLDINGS ELECTRONIC | PRINT WITHHOLDINGS ELECTRONIC | PRINT WITHHOLDINGS ELECTRONIC | Java `ReportPrintElectronicWithholdings` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptSswh_Withholding_Electronic.jrxml`; contexto sesión `—`. | `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/ReportPrintElectronicWithholdings.java` |
| Reporte | Report Withholding | Report Withholding | Report Withholding | *(OBUIAPP / manual)* | Report Withholding | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Background | Electronic Documents Background Process | Electronic Documents Background Process | E.D Backgound Process | *(OBUIAPP / manual)* | Electronic Invoice Background | — |
| Background | Electronic Invoice Offline Batch Backgroud Process | Electronic Invoice Offline Batch Backgroud Process | E.I Offline Batch Background | *(OBUIAPP / manual)* | Electronic Invoice Offline Batch Backgroud Process | — |
| Background | Validación de estados FE | Electronic documents status validate | EEIStatusValidate | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar liquidación compra electrónica | `GeneratePurchaseSettlement` | Proceso Java (toolbar/background) | `—` | — | `src/ec/cusoft/facturaec/ad_process/GeneratePurchaseSettlement.java` |
| Botón (Java) | Generate Document Electronic (Movement) | `Generate_Movement` | Proceso Java (toolbar/background) | `—` | El formato del RUC es incorrecto. | `src/ec/cusoft/facturaec/ad_process/Generate_Movement.java` |
| Informe (servlet) | Generar documento electrónico | `GenerateFE` | Proceso Java (toolbar/background) | `—` | Fecha Retención no seleccionada. | `src/ec/cusoft/facturaec/ad_process/GenerateFE.java` |
| Informe (servlet) | Generate Electronic Document (InOut) | `Generate_Remission_Guide` | Proceso Java (toolbar/background) | `M_InOut_ID` | — | `src/ec/cusoft/facturaec/ad_process/Generate_Remission_Guide.java` |
| Reporte | PRINT ELECTRONIC INVOICE | `ReportPrintElectronicInvoice` | Informe (servlet PDF) | `—` | ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptC_Invoice_Electronic.jrxml | `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/ReportPrintElectronicInvoice.java` |
| Reporte | PRINT WITHHOLDINGS ELECTRONIC | `ReportPrintElectronicWithholdings` | Informe (servlet PDF) | `—` | ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptSswh_Withholding_Electronic.jrxml | `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/ReportPrintElectronicWithholdings.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar liquidación compra electrónica | Generate purchase settlement | EM_Eei_Generate_Offline_2 | Java `GeneratePurchaseSettlement` (AD_MODEL_OBJECT `P`) | Proceso Openbravo ver `doExecute` en fuente | `src/ec/cusoft/facturaec/ad_process/GeneratePurchaseSettlement.java` |
| Botón (Java) | Generate Document Electronic (Movement) | Generate Document Electronic (Movement) | Generate Document Electronic | Java `Generate_Movement` (AD_MODEL_OBJECT `P`) | Proceso Openbravo El formato del RUC es incorrecto. | `src/ec/cusoft/facturaec/ad_process/Generate_Movement.java` |
| Botón (PL/pgSQL) | Anular liquidación compra electrónica | Void electronic purchase settlement | Void electronic purchase settlement | `eei_void_purchase_settlement` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Anular retención electrónica | Void Invoice | Eei_VoidInvoice | `eei_voidinvoice` | Inicio: Almacenar en ventana Retenciones anuladas; Fin : Almacenar en ventana Retenciones anuladas; eei_voidinvoice - Finish_Process Extension Point | — |
| Informe (servlet) | Generar documento electrónico | Generate Electronic Document | Eei_Generate_EDocument | Java `GenerateFE` (AD_MODEL_OBJECT `S`) | Proceso Openbravo Fecha Retención no seleccionada. | `src/ec/cusoft/facturaec/ad_process/GenerateFE.java` |
| Informe (servlet) | Generate Electronic Document (InOut) | Generate Electronic Document (InOut) | EEI_GenerateRemissionGuide | Java `Generate_Remission_Guide` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `M_InOut_ID` | `src/ec/cusoft/facturaec/ad_process/Generate_Remission_Guide.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar liquidación compra electrónica | Generate purchase settlement | Java `GeneratePurchaseSettlement` | Proceso Openbravo ver `doExecute` en fuente | Proceso Openbravo ver `doExecute` en fuente |
| Botón (Java) | Generate Document Electronic (Movement) | Generate Document Electronic (Movement) | Java `Generate_Movement` | Proceso Openbravo El formato del RUC es incorrecto. | El formato del RUC es incorrecto. |
| Botón (PL/pgSQL) | Anular liquidación compra electrónica | Void electronic purchase settlement | PL `eei_void_purchase_settlement` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Anular retención electrónica | Void Invoice | PL `eei_voidinvoice` | Inicio: Almacenar en ventana Retenciones anuladas; Fin : Almacenar en ventana Retenciones anuladas; eei_voidinvoice - Finish_Process Extension Point | Inicio: Almacenar en ventana Retenciones anuladas; Fin : Almacenar en ventana Retenciones anuladas; eei_voidinvoice - Finish_Process Extension Point |
| Informe (servlet) | Generar documento electrónico | Generate Electronic Document | Java `GenerateFE` | Proceso Openbravo Fecha Retención no seleccionada. | Fecha Retención no seleccionada. |
| Informe (servlet) | Generate Electronic Document (InOut) | Generate Electronic Document (InOut) | Java `Generate_Remission_Guide` | Proceso Openbravo registro `M_InOut_ID` | Proceso Openbravo registro `M_InOut_ID` |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | PRINT ELECTRONIC INVOICE | PRINT ELECTRONIC INVOICE | PRINT ELECTRONIC INVOICE | Java `ReportPrintElectronicInvoice` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptC_Invoice_Electronic.jrxml`; contexto sesión `—`. | `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/ReportPrintElectronicInvoice.java` |
| Reporte | PRINT WITHHOLDINGS ELECTRONIC | PRINT WITHHOLDINGS ELECTRONIC | PRINT WITHHOLDINGS ELECTRONIC | Java `ReportPrintElectronicWithholdings` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptSswh_Withholding_Electronic.jrxml`; contexto sesión `—`. | `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/ReportPrintElectronicWithholdings.java` |
| Reporte | Report Withholding | Report Withholding | Report Withholding | *(OBUIAPP / manual)* | Report Withholding | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 10**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **3**; archivos `*.jrxml` en el repo = **10**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | PRINT ELECTRONIC INVOICE | `PRINT ELECTRONIC INVOICE` | Java `ReportPrintElectronicInvoice`; JRXML `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptC_Invoice_Electronic.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | PRINT ELECTRONIC INVOICE. JRXML: `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptC_Invoice_Electronic.jrxml` |
| 2 | PRINT WITHHOLDINGS ELECTRONIC | `PRINT WITHHOLDINGS ELECTRONIC` | Java `ReportPrintElectronicWithholdings`; JRXML `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptSswh_Withholding_Electronic.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | PRINT WITHHOLDINGS ELECTRONIC. JRXML: `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptSswh_Withholding_Electronic.jrxml` |
| 3 | Report Withholding | `Report Withholding` | — | *(ver AD_PROCESS_PARA / servlet)* | Report Withholding |

### Plantillas sin proceso en diccionario

- `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptC_Invoice_Credit.jrxml`
- `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptC_Invoice_Credit_Debit.jrxml`
- `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptC_Invoice_Electronic.jrxml`
- `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptSswh_Withholding_Electronic.jrxml`
- `src/ec/cusoft/facturaec/ad_reports/Offline/fe_ride_factura.jrxml`
- `src/ec/cusoft/facturaec/ad_reports/Offline/fe_ride_guia_remision.jrxml`
- `src/ec/cusoft/facturaec/ad_reports/RptEEI_WithholdingRIDE.jrxml`
- `src/ec/cusoft/facturaec/files/RptC_Invoice.jrxml`
- `src/ec/cusoft/facturaec/files/RptC_Invoice_Electronic.jrxml`
- `src/ec/cusoft/facturaec/files/RptSswh_Withholding_Electronic.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `EEI_IncompleteInfo` | Incomplete Info for Electronic Invoice | Incomplete Info for Electronic Invoice | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Eei_ReactivateNotValid` | The transaction can not be reactivated. There is an authorized electronic document. | The transaction can not be reactivated. There is an authorized electronic document. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_No_Ref_To_Invoice` | La nota de crédito debe seleccionar una factura de venta. | La nota de crédito debe seleccionar una factura de venta. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Eei_Only_One_Line_Excluded` | There can only be one line with taxes excluded in the tax tab. | There can only be one line with taxes excluded in the tax tab. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_No_Deleted` | No es posible eliminar la clave de contingencia seleccionada porque ya ha sido consumida o se encuentra en proceso. | No es posible eliminar la clave de contingencia seleccionada porque ya ha sido consumida o se encuentra en proceso. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_ClassNotFound` | No fue posible localizar la clase de Java indicada | No fue posible localizar la clase de Java indicada | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_FileNotFound` | No se ha encontrado el fichero generado | No se ha encontrado el fichero generado | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_ElectronicInvoiceReact` | Una factura que ya ha sido enviada electrónicamente no puede reactivar | Una factura que ya ha sido enviada electrónicamente no puede reactivar | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Eei_More_Than_One_Tax` | More than one tax was found configured with the code '332' (Withholding Exclude). | More than one tax was found configured with the code '332' (Withholding Exclude). | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_SENT_INVOICE` | La factura seleccionada ya ha sido enviada | La factura seleccionada ya ha sido enviada | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_BPartner_Not_EInvoice` | El Tercero seleccionado no está configurado para realizar Facturación Electrónica | El Tercero seleccionado no está configurado para realizar Facturación Electrónica | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_Authorization` | Authorization Invoice in Mandatory. | Authorization Invoice in Mandatory. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_Hibernate_Error` | Error en Hibernate | Error en Hibernate | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_Authorization_Ret` | Authorization Withholding in Mandatory. | Authorization Withholding in Mandatory. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_ElectronicInvoiceSent` | Una factura que ya ha sido enviada electrónicamente no puede descontabilizarse | Una factura que ya ha sido enviada electrónicamente no puede descontabilizarse | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Eei_Tax_Not_Found` | No tax was found configured with the code '332' (Withholding exclude). | No tax was found configured with the code '332' (Withholding exclude). | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EEI_Cod_Voucher_Num` | The Voucher Code field should only contain numbers | The Voucher Code field should only contain numbers | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Eei_Void_SRI` | Remember to cancel the transaction in the Servicio de Rentas Internas system. If you do not, you can authorize more than one electronic document for this transaction. | Remember to cancel the transaction in the Servicio de Rentas Internas system. If you do not, you can authorize more than one electronic document for this transaction. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye diversas clases Java que permiten gestionar eventos y procesos relacionados con la facturación electrónica, como la clase 'UpdateIdentifierByProduct', que actualiza identificadores basados en productos. Estas funciones Java son esenciales para extender la funcionalidad del ERP y manejar la interacción con los sistemas externos necesarios para la emisión de facturas electrónicas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.cusoft.facturaec`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `UpdateIdentifierByProduct` | ad_callouts | SimpleCallout | — | `src/ec/cusoft/facturaec/ad_callouts/UpdateIdentifierByProduct.java` |
| `fe_generation_offline` | ad_offline | DalBaseProcess | — | `src/ec/cusoft/facturaec/ad_offline/fe_generation_offline.java` |
| `GenerateFE` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/GenerateFE.java` |
| `GeneratePurchaseSettlement` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/GeneratePurchaseSettlement.java` |
| `Generate_Movement` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/Generate_Movement.java` |
| `Generate_Remission_Guide` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/Generate_Remission_Guide.java` |
| `ReportPrintElectronicInvoice` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/ReportPrintElectronicInvoice.java` |
| `ReportPrintElectronicWithholdings` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/ReportPrintElectronicWithholdings.java` |
| `ProcessUtils` | ad_process | — | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/utils/ProcessUtils.java` |
| `WSEstadosPortBindingStub` | ad_process | org | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/WebServiceEstados/WSEstadosPortBindingStub.java` |
| `WSEstadosProxy` | ad_process | WSEstados_PortType | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/WebServiceEstados/WSEstadosProxy.java` |
| `WSEstados_PortType` | ad_process | java | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/WebServiceEstados/WSEstados_PortType.java` |
| `WSEstados_Service` | ad_process | javax | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/WebServiceEstados/WSEstados_Service.java` |
| `WSEstados_ServiceLocator` | ad_process | org | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/WebServiceEstados/WSEstados_ServiceLocator.java` |
| `ClientSOAP` | ad_process | — | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/util/ClientSOAP.java` |
| `ResultWebSrv` | ad_process | — | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/util/ResultWebSrv.java` |
| `WSRecepcionPortBindingStub` | ad_process | org | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/util/wsoap/WSRecepcionPortBindingStub.java` |
| `WSRecepcionProxy` | ad_process | ec | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/util/wsoap/WSRecepcionProxy.java` |
| `WSRecepcion_PortType` | ad_process | java | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/util/wsoap/WSRecepcion_PortType.java` |
| `WSRecepcion_Service` | ad_process | javax | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/util/wsoap/WSRecepcion_Service.java` |
| `WSRecepcion_ServiceLocator` | ad_process | org | Proceso / informe Java | `src/ec/cusoft/facturaec/ad_process/webservices/util/wsoap/WSRecepcion_ServiceLocator.java` |
| `Autorizacion` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/Autorizacion.java` |
| `AutorizacionComprobante` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/AutorizacionComprobante.java` |
| `AutorizacionComprobanteLote` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/AutorizacionComprobanteLote.java` |
| `AutorizacionComprobanteLoteResponse` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/AutorizacionComprobanteLoteResponse.java` |
| `AutorizacionComprobanteResponse` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/AutorizacionComprobanteResponse.java` |
| `AutorizacionComprobantes` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/AutorizacionComprobantes.java` |
| `AutorizacionComprobantesService` | autorizacion | Service | — | `src/ec/cusoft/facturaec/autorizacion/AutorizacionComprobantesService.java` |
| `Mensaje` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/Mensaje.java` |
| `ObjectFactory` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/ObjectFactory.java` |
| `RespuestaComprobante` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/RespuestaComprobante.java` |
| `RespuestaLote` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/RespuestaLote.java` |
| `package-info` | autorizacion | — | — | `src/ec/cusoft/facturaec/autorizacion/package-info.java` |
| `EEIOfflineBatchBackground` | background | DalBaseProcess | — | `src/ec/cusoft/facturaec/background/EEIOfflineBatchBackground.java` |
| `EEIStatusValidate` | background | DalBaseProcess | — | `src/ec/cusoft/facturaec/background/EEIStatusValidate.java` |
| `ByteArrayDataSource` | email | DataSource | — | `src/ec/cusoft/facturaec/email/ByteArrayDataSource.java` |
| `EMailAuthenticator` | email | Authenticator | — | `src/ec/cusoft/facturaec/email/EMailAuthenticator.java` |
| `EMailUtils` | email | — | — | `src/ec/cusoft/facturaec/email/EMailUtils.java` |
| `InvoiceBlockRecord` | event | EntityPersistenceEventObserver | — | `src/ec/cusoft/facturaec/event/InvoiceBlockRecord.java` |
| `PurchaseSettlementData` | event | EntityPersistenceEventObserver | — | `src/ec/cusoft/facturaec/event/PurchaseSettlementData.java` |
| `AbstractFileGeneration` | filewriter | — | — | `src/ec/cusoft/facturaec/filewriter/AbstractFileGeneration.java` |
| `CreditNoteFileGenerationEcuador` | filewriter | AbstractFileGeneration | — | `src/ec/cusoft/facturaec/filewriter/CreditNoteFileGenerationEcuador.java` |
| `DebitNoteFileGenerationEcuador` | filewriter | AbstractFileGeneration | — | `src/ec/cusoft/facturaec/filewriter/DebitNoteFileGenerationEcuador.java` |
| `FileGeneration` | filewriter | — | — | `src/ec/cusoft/facturaec/filewriter/FileGeneration.java` |
| `FileGenerationEcuador` | filewriter | AbstractFileGeneration | — | `src/ec/cusoft/facturaec/filewriter/FileGenerationEcuador.java` |
| `MovementGenerationEcuador` | filewriter | — | — | `src/ec/cusoft/facturaec/filewriter/MovementGenerationEcuador.java` |
| `PurchaseSettlementGenerationEcuador` | filewriter | — | — | `src/ec/cusoft/facturaec/filewriter/PurchaseSettlementGenerationEcuador.java` |
| `RemissionGuideGenerationEcuador` | filewriter | — | — | `src/ec/cusoft/facturaec/filewriter/RemissionGuideGenerationEcuador.java` |
| `WithholdingFileGenerationEcuador` | filewriter | AbstractFileGeneration | — | `src/ec/cusoft/facturaec/filewriter/WithholdingFileGenerationEcuador.java` |
| `ECWSClient` | generador | — | — | `src/ec/cusoft/facturaec/generador/ECWSClient.java` |
| `ManualCall` | generador | — | — | `src/ec/cusoft/facturaec/generador/ManualCall.java` |
| `Autorizacion` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/Autorizacion.java` |
| `AutorizacionComprobante` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/AutorizacionComprobante.java` |
| `AutorizacionComprobanteLote` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/AutorizacionComprobanteLote.java` |
| `AutorizacionComprobanteLoteResponse` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/AutorizacionComprobanteLoteResponse.java` |
| `AutorizacionComprobanteResponse` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/AutorizacionComprobanteResponse.java` |
| `AutorizacionComprobantes` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/AutorizacionComprobantes.java` |
| `AutorizacionComprobantesService` | pruebas | Service | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/AutorizacionComprobantesService.java` |
| `Mensaje` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/Mensaje.java` |
| `ObjectFactory` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/ObjectFactory.java` |
| `RespuestaComprobante` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/RespuestaComprobante.java` |
| `RespuestaLote` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/RespuestaLote.java` |
| `package-info` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/autorizacion/package-info.java` |
| `Comprobante` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/recepcion/Comprobante.java` |
| `Mensaje` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/recepcion/Mensaje.java` |
| `ObjectFactory` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/recepcion/ObjectFactory.java` |
| `RecepcionComprobantes` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/recepcion/RecepcionComprobantes.java` |
| `RecepcionComprobantesService` | pruebas | Service | — | `src/ec/cusoft/facturaec/pruebas/recepcion/RecepcionComprobantesService.java` |
| `RespuestaSolicitud` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/recepcion/RespuestaSolicitud.java` |
| `ValidarComprobante` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/recepcion/ValidarComprobante.java` |
| `ValidarComprobanteResponse` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/recepcion/ValidarComprobanteResponse.java` |
| `package-info` | pruebas | — | — | `src/ec/cusoft/facturaec/pruebas/recepcion/package-info.java` |
| `Comprobante` | recepcion | — | — | `src/ec/cusoft/facturaec/recepcion/Comprobante.java` |
| `Mensaje` | recepcion | — | — | `src/ec/cusoft/facturaec/recepcion/Mensaje.java` |
| `ObjectFactory` | recepcion | — | — | `src/ec/cusoft/facturaec/recepcion/ObjectFactory.java` |
| `RecepcionComprobantes` | recepcion | — | — | `src/ec/cusoft/facturaec/recepcion/RecepcionComprobantes.java` |
| `RecepcionComprobantesService` | recepcion | Service | — | `src/ec/cusoft/facturaec/recepcion/RecepcionComprobantesService.java` |
| `RespuestaSolicitud` | recepcion | — | — | `src/ec/cusoft/facturaec/recepcion/RespuestaSolicitud.java` |
| `ValidarComprobante` | recepcion | — | — | `src/ec/cusoft/facturaec/recepcion/ValidarComprobante.java` |
| `ValidarComprobanteResponse` | recepcion | — | — | `src/ec/cusoft/facturaec/recepcion/ValidarComprobanteResponse.java` |
| `package-info` | recepcion | — | — | `src/ec/cusoft/facturaec/recepcion/package-info.java` |
| `ContigencyService` | services | — | — | `src/ec/cusoft/facturaec/services/ContigencyService.java` |
| `ContingencyStatusEnum` | services | — | — | `src/ec/cusoft/facturaec/services/utils/ContingencyStatusEnum.java` |
| `OBEInvoice_I` | templates | the | — | `src/ec/cusoft/facturaec/templates/OBEInvoice_I.java` |
| `OBWSEInvoice_I` | templates | — | — | `src/ec/cusoft/facturaec/templates/OBWSEInvoice_I.java` |
| `Tester` | test | — | — | `src/ec/cusoft/facturaec/test/Tester.java` |
| `BASE64Encoder` | utils | CharacterEncoder | — | `src/ec/cusoft/facturaec/utils/BASE64Encoder.java` |
| `CharacterEncoder` | utils | — | — | `src/ec/cusoft/facturaec/utils/CharacterEncoder.java` |
| `CryptUtils` | utils | — | — | `src/ec/cusoft/facturaec/utils/CryptUtils.java` |
| `DOMUtils` | utils | — | — | `src/ec/cusoft/facturaec/utils/DOMUtils.java` |
| `Deprecated` | utils | — | — | `src/ec/cusoft/facturaec/utils/Deprecated.java` |
| `FechaUtils` | utils | — | — | `src/ec/cusoft/facturaec/utils/FechaUtils.java` |
| `FileUtils` | utils | — | — | `src/ec/cusoft/facturaec/utils/FileUtils.java` |
| `KSStore` | utils | IPKStoreManager | — | `src/ec/cusoft/facturaec/utils/KSStore.java` |
| `KeyTool` | utils | — | — | `src/ec/cusoft/facturaec/utils/KeyTool.java` |
| `PassStoreKS` | utils | IPassStoreKS | — | `src/ec/cusoft/facturaec/utils/PassStoreKS.java` |
| `Utils` | utils | — | — | `src/ec/cusoft/facturaec/utils/Utils.java` |
| `XMLPrinter` | utils | — | — | `src/ec/cusoft/facturaec/utils/XMLPrinter.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `EEI_CHECK_CREDITNOTE_INV_REF` | `c_invoice` | before INSERT/UPDATE | Verificar que se haya referenciado facturas; Verificar que se haya referenciado a una factura; Verificar que no se haya referenciado facturas |
| Trigger `EEI_DELETE_LOGS` | `c_invoice` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `EEI_INVOICEAUTHORIZATION_TRG4` | `c_invoice` | before INSERT/UPDATE | v_establecimiento := substr(v_reference, 1, 3);; v_NoFactura := TO_NUMBER(substr(v_reference, 9, 9));; /* Select authorization by document type, the invoice 'date' must be between authorization 'date from' and 'date to'… |
| Trigger `EEI_PURCHASE_SETTLEMENT_DATA` | `c_invoice` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `EEI_UNIQUE_EXCLUDEWTH_TRG` | `c_invoicetax` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `EEI_VLD_INVOICE_NUM_REF` | `c_invoice` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `EEI - WITHHOLDING DOCUMENT TYPE` | `C_DOCTYPE.DOCBASETYPE='SSWH_WHR'` |
| AD_VAL_RULE | — | `EEI - WITHHOLDING DOCUMENTTYPE` | `C_DOCTYPE.DOCBASETYPE='API' AND C_DOCTYPE.EM_EEI_IS_EDOC='Y'` |
| Función PL `eei_cusoft_update` | — | invocación proceso | =======================================================================; Secuencia de actualización forzada (Desbloquear -> Actualizar -> Bloquear); CASO 2: M_MOVEMENT (Movimientos de Inventario) |
| Función PL `eei_invoice_date_valid` | — | invocación proceso | v_ResultStr := 'LA FECHA DE LA TRANSACCION NO PUEDE SER DIFERENTE A LA FECHA DE HOY YA QUE ES UN DOCUMENTO ELECTRONICO';; RAISE_APPLICATION_ERROR(-20000,v_ResultStr); |
| Función PL `eei_voidinvoice` | — | invocación proceso | Inicio: Almacenar en ventana Retenciones anuladas; Fin : Almacenar en ventana Retenciones anuladas; eei_voidinvoice - Finish_Process Extension Point |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

La base de datos utiliza triggers y funciones PL/pgSQL para soportar la lógica de negocio del módulo. Estos triggers aseguran que las reglas de validación se apliquen correctamente en tablas críticas como C_INVOICE y C_INVOICETAX, garantizando la integridad de los datos y el cumplimiento normativo. Las funciones PL también facilitan la realización de tareas complejas durante los procesos de facturación, como la generación de documentos de forma automatizada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `EEI_CHECK_CREDITNOTE_INV_REF` | `c_invoice` | before | INSERT/UPDATE | Verificar que se haya referenciado facturas; Verificar que se haya referenciado a una factura; Verificar que no se haya referenciado facturas | `model/triggers/EEI_CHECK_CREDITNOTE_INV_REF.xml` |
| `EEI_DELETE_LOGS` | `c_invoice` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/EEI_DELETE_LOGS.xml` |
| `EEI_INVOICEAUTHORIZATION_TRG4` | `c_invoice` | before | INSERT/UPDATE | v_establecimiento := substr(v_reference, 1, 3);; v_NoFactura := TO_NUMBER(substr(v_reference, 9, 9));; /* Select authorization by document type, the invoice 'date' must be between authorization 'date from' and 'date to'… | `model/triggers/EEI_INVOICEAUTHORIZATION_TRG4.xml` |
| `EEI_PURCHASE_SETTLEMENT_DATA` | `c_invoice` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/EEI_PURCHASE_SETTLEMENT_DATA.xml` |
| `EEI_VLD_INVOICE_NUM_REF` | `c_invoice` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/EEI_VLD_INVOICE_NUM_REF.xml` |
| `EEI_UNIQUE_EXCLUDEWTH_TRG` | `c_invoicetax` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/EEI_UNIQUE_EXCLUDEWTH_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `eei_cusoft_update` | — | =======================================================================; Secuencia de actualización forzada (Desbloquear -> Actualizar -> Bloquear); CASO 2: M_MOVEMENT (Movimientos de Inventario); Restaurar bloqueo solo… | =======================================================================; Secuencia de actualización forzada (Desbloquear -> Actualizar -> Bloquear); CASO 2: M_MOVEMENT (Movimientos de Inventario); Restaurar bloqueo solo si estaba procesado | `model/functions/EEI_CUSOFT_UPDATE.xml` |
| `eei_docno_remissionguide` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/EEI_DOCNO_REMISSIONGUIDE.xml` |
| `eei_exclude_withholding` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/EEI_EXCLUDE_WITHHOLDING.xml` |
| `eei_get_existresuply` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/EEI_GET_EXISTRESUPLY.xml` |
| `eei_get_refund_values` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/EEI_GET_REFUND_VALUES.xml` |
| `eei_get_remissionguidefields` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/EEI_GET_REMISSIONGUIDEFIELDS.xml` |
| `eei_invoice_date_valid` | — | v_ResultStr := 'LA FECHA DE LA TRANSACCION NO PUEDE SER DIFERENTE A LA FECHA DE HOY YA QUE ES UN DOCUMENTO ELECTRONICO';; RAISE_APPLICATION_ERROR(-20000,v_ResultStr); | v_ResultStr := 'LA FECHA DE LA TRANSACCION NO PUEDE SER DIFERENTE A LA FECHA DE HOY YA QUE ES UN DOCUMENTO ELECTRONICO';; RAISE_APPLICATION_ERROR(-20000,v_ResultStr); | `model/functions/EEI_INVOICE_DATE_VALID.xml` |
| `eei_invoice_ret_date_valid` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/EEI_INVOICE_RET_DATE_VALID.xml` |
| `eei_reactivatecontrolinvoice` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/EEI_REACTIVATECONTROLINVOICE.xml` |
| `eei_returndocumentno` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/EEI_RETURNDOCUMENTNO.xml` |
| `eei_void_purchase_settlement` | Anular liquidación compra electrónica | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/EEI_VOID_PURCHASE_SETTLEMENT.xml` |
| `eei_voidinvoice` | Anular retención electrónica | Inicio: Almacenar en ventana Retenciones anuladas; Fin : Almacenar en ventana Retenciones anuladas; eei_voidinvoice - Finish_Process Extension Point | Inicio: Almacenar en ventana Retenciones anuladas; Fin : Almacenar en ventana Retenciones anuladas; eei_voidinvoice - Finish_Process Extension Point | `model/functions/EEI_VOIDINVOICE.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Generar liquidación compra electrónica | `EM_Eei_Generate_Offline_2` | Botón (Java) | Java `GeneratePurchaseSettlement` | N | Proceso Openbravo ver `doExecute` en fuente |
| 2 | Generate Document Electronic (Movement) | `Generate Document Electronic` | Botón (Java) | Java `Generate_Movement` | N | Proceso Openbravo El formato del RUC es incorrecto. |
| 3 | Anular liquidación compra electrónica | `Void electronic purchase settlement` | Botón (PL/pgSQL) | PL `eei_void_purchase_settlement` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 4 | Anular retención electrónica | `Eei_VoidInvoice` | Botón (PL/pgSQL) | PL `eei_voidinvoice` | N | Inicio: Almacenar en ventana Retenciones anuladas; Fin : Almacenar en ventana Retenciones anuladas; eei_voidinvoice - Finish_Process Extension Point |
| 5 | Generar documento electrónico | `Eei_Generate_EDocument` | Informe (servlet) | Java `GenerateFE` | N | Proceso Openbravo Fecha Retención no seleccionada. |
| 6 | Generate Electronic Document (InOut) | `EEI_GenerateRemissionGuide` | Informe (servlet) | Java `Generate_Remission_Guide` | N | Proceso Openbravo registro `M_InOut_ID` |
| 7 | PRINT ELECTRONIC INVOICE | `PRINT ELECTRONIC INVOICE` | Reporte | Java `ReportPrintElectronicInvoice` | S | Genera PDF desde JRXML `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptC_Invoice_Electronic.jrxml`; contexto sesión `—`. |
| 8 | PRINT WITHHOLDINGS ELECTRONIC | `PRINT WITHHOLDINGS ELECTRONIC` | Reporte | Java `ReportPrintElectronicWithholdings` | S | Genera PDF desde JRXML `ec/cusoft/facturaec/ad_process/PrintElectronicDocuments/RptSswh_Withholding_Electronic.jrxml`; contexto sesión `—`. |
| 9 | Report Withholding | `Report Withholding` | Reporte | — | S | Report Withholding |

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

Módulo: `ec.cusoft.facturaec`.

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

# Glosario — prefijo `EEI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `EEI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.cusoft.facturaec` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `E.D Backgound Process` — Electronic Documents Background Process
- `E.I Offline Batch Background` — Electronic Invoice Offline Batch Backgroud Process
- `EEIStatusValidate` — Validación de estados FE
- `EM_Eei_Generate_Offline_2` — Generar liquidación compra electrónica
- `Generate Document Electronic` — Generate Document Electronic (Movement)
- `Void electronic purchase settlement` — Anular liquidación compra electrónica
- `Eei_VoidInvoice` — Anular retención electrónica
- `Eei_Generate_EDocument` — Generar documento electrónico
- `EEI_GenerateRemissionGuide` — Generate Electronic Document (InOut)
- `PRINT ELECTRONIC INVOICE` — PRINT ELECTRONIC INVOICE
- `PRINT WITHHOLDINGS ELECTRONIC` — PRINT WITHHOLDINGS ELECTRONIC
- `Report Withholding` — Report Withholding

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Invoice Test
**Package:** `ec.com.sidesoft.facturaec.test`

# Module overview — Invoice Test

## Functional

El módulo 'Invoice Test' está diseñado para facilitar la generación y gestión de facturas dentro del sistema Openbravo. Los actores clave incluyen usuarios de negocio que manejan las facturas y el equipo de soporte que asegura su correcto funcionamiento. Este módulo es útil especialmente para empresas que requieren una gestión eficaz de su ciclo de facturación. Dependencias notables son las relacionadas con la compatibilidad con versiones específicas del sistema, como la '2.50 to 3.00 Compatibility Skin'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/facturaec/test` |
| Web | `web/ec.com.sidesoft.facturaec.test/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`FETS`

# Guía de chat — Invoice Test

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.facturaec.test`).

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
- «¿Qué es la tabla fets_test?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo crear una nueva factura en el módulo 'Invoice Test'?
- ¿Qué sucede si ingreso datos incorrectos en una factura?
- ¿Puedo ver un historial de facturas previamente generadas?
- ¿Cómo puedo completar una factura una vez que todos los datos estén ingresados?
- ¿Qué validaciones se realizan al completar una factura?
- ¿Es posible personalizar el formato de impresión de las facturas?
- ¿Dónde puedo encontrar la documentación de ayuda para este módulo?
- ¿Con quién debo comunicarme para problemas técnicos relacionados con el módulo 'Invoice Test'?

# Domain — data model

## Functional

La entidad central del módulo es la tabla 'fets_test', que almacena toda la información relevante sobre las facturas de prueba. Aunque no se definen etapas explícitas en el esquema, se entiende que el proceso de facturación abarca desde la creación hasta el cierre de una factura. Actualmente, no existen triggers definidos que registren eventos automáticos, lo que podría limitar ciertas automatizaciones en la gestión de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `fets_test` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `fets_test` | fets_test | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoice_id→c_invoice | Detalle enlazado a ad_client, ad_org, c_invoice. | PK `fets_test_pk`; Cols: c_invoice_id, doctype, xml, fets_generate |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `fets_test` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de la ventana denominada 'Test Factura'. Desde esta interfaz, los usuarios pueden acceder a las funciones básicas para gestionar facturas, lo que facilitará el seguimiento y la modificación de registros de facturación pertinentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.facturaec.test.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Test Factura | Invoice Test |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Test Factura | Invoice Test | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.facturaec.test.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Test Factura

- **AD_WINDOW_ID:** `80576262574B47FA9CC0F44C1DD823B0`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Invoice Test | `35BA38127ED84760AE841CBEE65358F0` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Invoice Test (ventana: Test Factura)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Invoice | `C_Invoice_ID` | No | No | — |
| 30 | Doctype | `Doctype` | No | No | — |
| 40 | Xml | `Xml` | No | No | — |
| 50 | Fets_Generate | `Fets_Generate` | No | No | — |
| 60 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

En cuanto a procesos, el módulo incluye un botón para completar las facturas, lo cual es una acción típica en la gestión documental. Este proceso permitirá validar los datos necesarios antes de marcar una factura como finalizada. No hay informes predefinidos en este módulo, pero la integración con otras funcionalidades del ERP puede permitir generar informes cuando sea necesario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.facturaec.test.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Informe (servlet) | FETSTestInvoiceProcess | FETSTestInvoiceProcess | FETS Test Invoice Process | Java `fe_generation_offline` (AD_MODEL_OBJECT `S`) | Servlet de informe `fe_generation_offline` (fuente no en `src/` del módulo). | — |
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
| Informe (servlet) | FETSTestInvoiceProcess | `fe_generation_offline` | Informe (servlet) | `—` | — | `—` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Informe (servlet) | FETSTestInvoiceProcess | FETSTestInvoiceProcess | FETS Test Invoice Process | Java `fe_generation_offline` (AD_MODEL_OBJECT `S`) | Servlet de informe `fe_generation_offline` (fuente no en `src/` del módulo). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Informe (servlet) | FETSTestInvoiceProcess | FETSTestInvoiceProcess | Java `fe_generation_offline` | Servlet de informe `fe_generation_offline` (fuente no en `src/` del módulo). | Servlet de informe `fe_generation_offline` (fuente no en `src/` del módulo). |
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

No se identifican clases Java dentro de este módulo, lo que implica que la funcionalidad se centra en la implementación estándar de Openbravo sin personalizaciones adicionales en el código Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.facturaec.test`.

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

Dentro del contexto de la base de datos, los triggers y funciones PL no están presentes en este módulo, lo que significa que las operaciones que podrían haberse automatizado deben realizarse manualmente. Esto podría resultar en una gestión menos eficiente en comparación con módulos que poseen lógica de base de datos más avanzada.

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
| 1 | FETSTestInvoiceProcess | `FETS Test Invoice Process` | Informe (servlet) | Java `fe_generation_offline` | N | Servlet de informe `fe_generation_offline` (fuente no en `src/` del módulo). |

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

Módulo: `ec.com.sidesoft.facturaec.test`.

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

# Glosario — prefijo `FETS`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `FETS` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.facturaec.test` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `FETS Test Invoice Process` — FETSTestInvoiceProcess

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Credit Note Reference for Invoices Module
**Package:** `ec.com.sidesoft.creditNoteRefenence`

# Module overview — Credit Note Reference for Invoices Module

## Functional

El módulo 'Credit Note Reference for Invoices' es una extensión diseñada para facilitar la gestión y referencia de notas de crédito en relación con las facturas. Su propósito es mejorar la trazabilidad y la administración de las notas de crédito asociadas a facturas existentes, asegurando un flujo correcto de información entre los documentos contables. Los actores principales son los usuarios de negocio que gestionan las facturas y notas de crédito, así como el equipo de soporte y desarrolladores que lo implementan y mantienen. Este módulo requiere la compatibilidad con la versión de Openbravo entre 2.50 y 3.00, y se integra directamente con la tabla de facturas, 'C_INVOICE'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/creditNoteRefenence` |
| Web | `web/ec.com.sidesoft.creditNoteRefenence/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SCNR`

# Guía de chat — Credit Note Reference for Invoices Module

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.creditNoteRefenence`).

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

- ¿Cómo puedo vincular una nota de crédito a una factura existente?
- ¿Qué pasos debo seguir para visualizar las notas de crédito asociadas a mis facturas?
- ¿Qué sucede si una factura ya tiene una nota de crédito vinculada?
- ¿Hay algún límite en la cantidad de notas de crédito que puedo asociar a una factura?
- ¿Cómo puedo comprobar el estado de una nota de crédito que he creado?
- ¿Puedo deshacer la vinculación de una nota de crédito de una factura?
- ¿Dónde encuentro información sobre las notas de crédito en los informes del sistema?
- ¿Qué validaciones se realizan al asociar notas de crédito a las facturas?

# Domain — data model

## Functional

El módulo se construye sobre la entidad cabecera de las facturas, específicamente la tabla 'C_INVOICE', que ha sido modificada para incluir referencias a notas de crédito. Aunque no hay etapas formales definidas en el modelo, el módulo se centra en establecer la relación entre notas de crédito y facturas, lo que se refleja en la funcionalidad añadida por el módulo. Dado que no hay triggers establecidos, la lógica principal se implementa a través de una función PL específica que permite realizar las operaciones necesarias en la base de datos para mantener la integridad de los datos entre notas de crédito y facturas.

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

`C_INVOICE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no tiene ventanas específicas definidas en su inventario, lo que indica que la funcionalidad se integra dentro de las ventanas existentes de gestión de facturas. Los usuarios navegan por el módulo a través de las funciones ampliadas en la interfaz de usuario al gestionar las facturas en el sistema, aprovechando la nueva funcionalidad que permite vincular notas de crédito desde la vista de facturas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.creditNoteRefenence.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.creditNoteRefenence.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `263`

- **AD_TAB_ID:** `263` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 94 | Reference Invoice | `EM_Scnr_Isref_Inv` | No | No | — |
| 95 | Invoice Referenced | `EM_Scnr_Invoice_ID` | No | No | — |

### Pestaña `290`

- **AD_TAB_ID:** `290` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 94 | Reference Invoice | `EM_Scnr_Isref_Inv` | No | No | — |
| 95 | Invoice Referenced | `EM_Scnr_Invoice_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

En el módulo, no hay botones de proceso específicos, lo que sugiere que las acciones relacionadas con las notas de crédito se manejan directamente desde las operaciones de las facturas. Los informes típicos no están especificados, sin embargo, los usuarios pueden requerir información sobre las notas de crédito asociadas a las facturas. Se espera que haya validaciones internas en la función PL para asegurar que las notas de crédito se asignen correctamente a las facturas correspondientes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.creditNoteRefenence.es_ES/referencedata/translation/`.

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

El módulo no presenta clases Java, lo que indica que toda la lógica se maneja a través de la funcionalidad PL y las integraciones en las ventanas existentes del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.creditNoteRefenence`.

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

El módulo cuenta con una función PL que es crucial para el soporte del sistema, ya que maneja la lógica necesaria para la conexión entre las notas de crédito y las facturas. Aunque no hay triggers implementados, la función PL asegura que las modificaciones a las facturas se sincronicen adecuadamente con las notas de crédito, manteniendo la integridad de los datos.

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
| `scnr_updatefieldelec` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SCNR_UPDATEFIELDELEC.xml` |
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

Módulo: `ec.com.sidesoft.creditNoteRefenence`.

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

# Glosario — prefijo `SCNR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SCNR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.creditNoteRefenence` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Financial Credit Note Sales Auto
**Package:** `ec.com.sidesoft.financialcreditnote.sales.auto`

# Module overview — Financial Credit Note Sales Auto

## Functional

El módulo Financial Credit Note Sales Auto permite la generación automática de notas de crédito financieras en ventas, optimizando el proceso de gestión de devoluciones y ajustes en facturas. Este módulo es especialmente útil para usuarios de negocio que buscan gestionar eficientemente sus transacciones, así como para soporte de nivel 2 que necesita entender el flujo de las notas de crédito. Su alcance abarca la automatización de procesos recurrentes relacionados con las notas de crédito, y depende de otras funcionalidades básicas del ERP Openbravo, así como de su framework y un skin de compatibilidad.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/financialcreditnote/sales/auto` |
| Web | `web/ec.com.sidesoft.financialcreditnote.sales.auto/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SCNSA`

# Guía de chat — Financial Credit Note Sales Auto

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.financialcreditnote.sales.auto`).

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

- ¿Cómo genero una nota de crédito desde una factura existente?
- ¿Qué sucede si la nota de crédito no se genera automáticamente?
- ¿Cuáles son los requisitos para que una nota de crédito se genere correctamente?
- ¿Puedo ver un historial de notas de crédito generadas?
- ¿Qué debo hacer si veo un error en la nota de crédito generada?
- ¿Cómo modifico los parámetros de generación de notas de crédito?
- ¿Dónde encuentro ayuda si tengo problemas con el módulo?
- ¿Qué tipos de documentos son compatibles con notas de crédito en este módulo?

# Domain — data model

## Functional

El módulo se basa en la entidad cabecera de la factura, vinculada a notas de crédito que se generan automáticamente a partir de dicha factura. Las relaciones clave involucran las tablas C_INVOICE y C_DOCTYPE, donde se modulan los tipos de documentos y las facturas que originan las notas de crédito. Aunque no se definen triggers en este módulo, sí se implementan dos funciones PL que facilitan el flujo de la generación automática y aseguran la correcta relación entre las facturas y sus notas de crédito asociadas. Esto permite que los cambios en facturas puedan reflejarse adecuadamente en las notas de crédito generadas.

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

`C_DOCTYPE`, `C_INVOICE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no tiene ventanas específicas definidas en la interfaz de usuario ya que se basa en la funcionalidad del backend para la generación de notas de crédito automáticas. La navegación se realiza a través de los procesos configurados que permiten a los usuarios activar la generación de las notas de crédito desde el contexto de facturación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.financialcreditnote.sales.auto.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.financialcreditnote.sales.auto.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 370 | EM_Scnsa_Automatic_Generate_Nc | `EM_Scnsa_Automatic_Generate_Nc` | No | No | E273C63F2A0E4E38A2A6DB2EF210DEBF |
| 380 | EM_Scnsa_Doc_Nc_Automatic | `EM_Scnsa_Doc_Nc_Automatic` | No | No | E273C63F2A0E4E38A2A6DB2EF210DEBF |
| 390 | EM_Scnsa_Description | `EM_Scnsa_Description` | No | No | E273C63F2A0E4E38A2A6DB2EF210DEBF |

### Pestaña `263`

- **AD_TAB_ID:** `263` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 3030 | Generate NC | `EM_Scnsa_Generatenc` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye tres procesos que permiten generar notas de crédito automáticamente, cada uno vinculado a botones que ejecutan la generación, completan o cancelan el proceso de creación de la nota de crédito. Los informes específicos no están definidos, pero se pueden gestionar validaciones frecuentes sobre la correcta asociación entre facturas y notas de crédito usando las funciones PL. Estas validaciones aseguran que el proceso sea eficiente y sin errores, lo que es crucial para mantener la integridad de la información financiera.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.financialcreditnote.sales.auto.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar NC | Generate NC | Generate NC | Java `Scnsa_GenerateNC` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `C_Invoice_ID`, @scnsa_notconfiginit_generate_nc@; @scnsa_nc_generation_product@; @scnsa_notconfig_generation_nc@ | `src/ec/com/sidesoft/financialcreditnote/sales/auto/ad_actionbutton/Scnsa_GenerateNC.java` |
| Botón (PL/pgSQL) | Pos Generacion NC | Pos Generate NC | Scnsa_PosGenerateNC | `scnsa_posprocessgeneratenc` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Botón (PL/pgSQL) | Pre Generacion NC | Pre Generate NC | Scnsa_PreGenerateNC | `scnsa_preprocessgeneratenc` | sccc_preunprocess - PreUnprocess Extension Point | — |
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
| Botón (Java) | Generar NC | `Scnsa_GenerateNC` | Proceso Java (toolbar/background) | `C_Invoice_ID` | @scnsa_notconfiginit_generate_nc@; @scnsa_nc_generation_product@; @scnsa_notconfig_generation_nc@ | `src/ec/com/sidesoft/financialcreditnote/sales/auto/ad_actionbutton/Scnsa_GenerateNC.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar NC | Generate NC | Generate NC | Java `Scnsa_GenerateNC` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `C_Invoice_ID`, @scnsa_notconfiginit_generate_nc@; @scnsa_nc_generation_product@; @scnsa_notconfig_generation_nc@ | `src/ec/com/sidesoft/financialcreditnote/sales/auto/ad_actionbutton/Scnsa_GenerateNC.java` |
| Botón (PL/pgSQL) | Pos Generacion NC | Pos Generate NC | Scnsa_PosGenerateNC | `scnsa_posprocessgeneratenc` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Botón (PL/pgSQL) | Pre Generacion NC | Pre Generate NC | Scnsa_PreGenerateNC | `scnsa_preprocessgeneratenc` | sccc_preunprocess - PreUnprocess Extension Point | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar NC | Generate NC | Java `Scnsa_GenerateNC` | Proceso Openbravo registro `C_Invoice_ID`, @scnsa_notconfiginit_generate_nc@; @scnsa_nc_generation_product@; @scnsa_notconfig_generation_nc@ | @scnsa_notconfiginit_generate_nc@; @scnsa_nc_generation_product@; @scnsa_notconfig_generation_nc@ |
| Botón (PL/pgSQL) | Pos Generacion NC | Pos Generate NC | PL `scnsa_posprocessgeneratenc` | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point |
| Botón (PL/pgSQL) | Pre Generacion NC | Pre Generate NC | PL `scnsa_preprocessgeneratenc` | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point |
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
| `scnsa_success_generation_nc` | Generate Credit Note: %1 - %2 - %3 | Generate Credit Note: %1 - %2 - %3 | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `scnsa_nc_relation_invoice` | The selected record is related to another NC whose doc. status is Draft or Completed, to identify Validate the relationship in Related Items in the Credit Note Num: %1 | The selected record is related to another NC whose doc. status is Draft or Completed, to identify Validate the relationship in Related Items in the Credit Note Num: %1 | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `scnsa_notconfiginit_generate_nc` | The document type of the original transaction does not meet the initial setting in the document category | The document type of the original transaction does not meet the initial setting in the document category | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `scnsa_nc_generation_product` | Error in the automatic Financial NC generation. There are Warehoused-Inventoried products. Perform a NC for return. | Error in the automatic Financial NC generation. There are Warehoused-Inventoried products. Perform a NC for return. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `scnsa_notconfig_generation_nc` | The automatic NC document type is not configured for the original invoice. | The automatic NC document type is not configured for the original invoice. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye una clase Java denominada Scnsa_GenerateNC que implementa la lógica de generación de notas de crédito a partir de facturas. Esta clase gestiona la interacción con el contexto de datos de Openbravo y se encarga de las operaciones necesarias para crear las notas de crédito automáticamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.financialcreditnote.sales.auto`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Scnsa_GenerateNC` | ad_actionbutton | DalBaseProcess | — | `src/ec/com/sidesoft/financialcreditnote/sales/auto/ad_actionbutton/Scnsa_GenerateNC.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Credit Note Sales Auto` | `c_doctype.GL_Category_ID='102C08DF5D4341D5B7FDF758632503D2' AND c_doctype.DocBaseType = 'ARC' AND c_doctype.Isreversal='` |
| Función PL `scnsa_posprocessgeneratenc` | — | invocación proceso | sccc_preunprocess - PreUnprocess Extension Point |
| Función PL `scnsa_preprocessgeneratenc` | — | invocación proceso | sccc_preunprocess - PreUnprocess Extension Point |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Las funciones PL son cruciales para el soporte de este módulo, facilitando procesos automatizados y asegurando la correcta creación de notas de crédito en función de las variaciones en las facturas. Aunque no se utilizan triggers en este módulo, la funcionalidad de las funciones PL ayuda a encapsular la lógica del negocio y permite mantener la consistencia en la gestión documental.

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
| `scnsa_posprocessgeneratenc` | Pos Generacion NC | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point | `model/functions/SCNSA_POSPROCESSGENERATENC.xml` |
| `scnsa_preprocessgeneratenc` | Pre Generacion NC | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point | `model/functions/SCNSA_PREPROCESSGENERATENC.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Generar NC | `Generate NC` | Botón (Java) | Java `Scnsa_GenerateNC` | N | Proceso Openbravo registro `C_Invoice_ID`, @scnsa_notconfiginit_generate_nc@; @scnsa_nc_generation_product@; @scnsa_notconfig_generation_nc@ |
| 2 | Pos Generacion NC | `Scnsa_PosGenerateNC` | Botón (PL/pgSQL) | PL `scnsa_posprocessgeneratenc` | N | sccc_preunprocess - PreUnprocess Extension Point |
| 3 | Pre Generacion NC | `Scnsa_PreGenerateNC` | Botón (PL/pgSQL) | PL `scnsa_preprocessgeneratenc` | N | sccc_preunprocess - PreUnprocess Extension Point |

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

Módulo: `ec.com.sidesoft.financialcreditnote.sales.auto`.

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

# Glosario — prefijo `SCNSA`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SCNSA` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.financialcreditnote.sales.auto` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Generate NC` — Generar NC
- `Scnsa_PosGenerateNC` — Pos Generacion NC
- `Scnsa_PreGenerateNC` — Pre Generacion NC

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Update Fiel Invoice Description
**Package:** `ec.com.sidesoft.invoice.updatedescription`

# Module overview — Update Fiel Invoice Description

## Functional

El módulo 'Update Fiel Invoice Description' tiene como propósito actualizar la descripción de las facturas FIEL en el sistema Openbravo. Este proceso es relevante para los usuarios que gestionan la emisión de facturas, asegurando que la información reflejada sea precisa y cumpla con las normativas fiscales. Los actores principales son los usuarios de negocio encargados de la facturación y el proceso administrativo. Este módulo no tiene dependencias específicas, lo que simplifica su integración en la plataforma.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/invoice/updatedescription` |
| Web | `web/ec.com.sidesoft.invoice.updatedescription/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**1.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SIUDD`

# Guía de chat — Update Fiel Invoice Description

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.invoice.updatedescription`).

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

- ¿Cómo actualizo la descripción de una factura FIEL?
- ¿Qué necesito verificar antes de ejecutar la función de actualización?
- ¿Hay alguna restricción sobre los datos que puedo ingresar en la descripción?
- ¿Cómo puedo acceder a la función de actualización en el sistema?
- ¿Qué hacer si la actualización no se refleja en el sistema?
- ¿Puedo ejecutar esta función sin ser administrador?
- ¿Cómo se maneja un error durante el proceso de actualización?
- ¿Se registran los cambios realizados en la descripción de la factura?

# Domain — data model

## Functional

El módulo no cuenta con entidades físicas ni tablas específicas, ya que su función principal radica en la ejecución de una función PL única que lleva a cabo la lógica de actualización de descripciones de facturas. No se presentan etapas o relaciones complejas dado que se centra en un proceso específico, pero se debe considerar el correcto cimentado de los datos a través de la estructura de la factura existente en el ERP.

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

No se han definido ventanas específicas en la interfaz de usuario para este módulo, por lo que el acceso y uso de la función se debe realizar directamente a través de las herramientas de desarrollo o scripts. Los usuarios deben tener privilegios adecuados para ejecutar la función disponible.

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

El módulo no incluye botones de proceso ni informes generados. Sin embargo, es importante que los usuarios realicen validaciones frecuentes sobre los datos de las facturas antes de ejecutar la función para evitar inconsistencias. Los tipos de validaciones pueden incluir comprobar la estructura y el formato de los datos de entrada.

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

Este módulo no incluye ninguna clase Java, dado que se enfoca en la funcionalidad de actualización a través de PL/SQL.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.invoice.updatedescription`.

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

La función PL dentro del módulo desempeña un rol crucial en la actualización de las descripciones de las facturas sin requerir la intervención de disparadores, lo que minimiza la complejidad en términos de mantenimiento del sistema. Esta función también proporciona una solución centralizada para la gestión de descripciones.

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
| `siudd_update_invdescription` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SIUDD_UPDATE_INVDESCRIPTION.xml` |
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

Módulo: `ec.com.sidesoft.invoice.updatedescription`.

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

# Glosario — prefijo `SIUDD`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SIUDD` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.invoice.updatedescription` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Custom Signature for Document Type
**Package:** `ec.com.sidesoft.custom.signature`

# Module overview — Sidesoft Custom Signature for Document Type

## Functional

El módulo 'Sidesoft Custom Signature for Document Type' está diseñado para facilitar la gestión de firmas personalizadas asociadas a tipos de documentos dentro del ERP Openbravo. Su principal objetivo es garantizar que los documentos generados contengan las firmas correspondientes, mejorando así la trazabilidad y cumplimiento normativo. Los actores principales que utilizan este módulo son los usuarios de negocio encargados de la gestión documental, así como los administradores del sistema que se encargan del mantenimiento del mismo. No tiene dependencias adicionales, lo que facilita su implementación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/signature` |
| Web | `web/ec.com.sidesoft.custom.signature/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SCSDC`

# Guía de chat — Sidesoft Custom Signature for Document Type

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.signature`).

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
- «¿Qué es la tabla scsdc_signaturesperdoc?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo añadir una firma a un documento?
- ¿Dónde se almacenan las firmas personalizadas?
- ¿Puedo eliminar una firma que ya no es necesaria?
- ¿Qué tipo de documentos pueden tener firmas personalizadas?
- ¿Cómo verifico que una firma se ha añadido correctamente?
- ¿Hay límites en la cantidad de firmas que puedo agregar a un documento?
- ¿Cómo se actualizan las firmas si hay cambios en el documento?
- ¿Puedo visualizar las firmas asociadas a un documento desde la interfaz?

# Domain — data model

## Functional

Este módulo se basa en la tabla 'scsdc_signaturesperdoc', que actúa como entidad cabecera donde se almacenan las firmas personalizadas para cada tipo de documento. Aunque no se especifican etapas en el flujo de trabajo, se puede asumir que la creación y gestión de las firmas implican la interacción inicial con esta tabla. Dado que no hay triggers ni funciones PL asociadas, el manejo de los datos se realiza a través de operaciones directas sobre la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `scsdc_signaturesperdoc` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `scsdc_signaturesperdoc` | SCSDC_signaturesperdoc | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `scsdc_signaturespd_key`; Cols: c_doctype_id, label, name, position, isaudit; `SCSDC_SIGNATURESPD_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SCSDC_SIGNATURESPD_AUDIT_CHK`: ISAUDIT IN ('Y', 'N'); idx `SCSDC_SIGNATURES_CDOCTYPE_LINE` (c_doctype_id, line) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SCSDC_signaturesperdoc` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no incluye ventanas adicionales en la interfaz de usuario, pero se accede a la funcionalidad a través de la tabla mencionada, que puede integrarse a otras funcionalidades dentro del ERP. La navegación se realizaría principalmente donde se gestionen los documentos y sus firmas correspondientes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.signature.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.signature.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Signatures

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 15 | Line No. | `Line` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Label | `Label` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Position | `Position` | No | No | — |
| 70 | Audit | `Isaudit` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

No se identifican botones procesales, informes específicos, o validaciones frecuentes dentro de este módulo, lo que sugiere que las interacciones se limitan a la creación y visualización de las firmas en la tabla de documentos. Es probable que las validaciones ocurran a nivel de entrada de datos, asegurando que las firmas se asocien correctamente a los documentos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.signature.es_ES/referencedata/translation/`.

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

El módulo no incluye clases Java, lo que implica que su funcionalidad se basa únicamente en la base de datos y en la configuración del ERP sin lógica adicional implementada en el lado del servidor.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.signature`.

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

Aunque no hay triggers activos en este módulo, se considera que el manejo de datos se realiza mediante operaciones directas en la base de datos. La ausencia de funciones PL sugiere un enfoque más simple, sin necesidad de lógica compleja durante la gestión de las firmas.

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

Módulo: `ec.com.sidesoft.custom.signature`.

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

# Glosario — prefijo `SCSDC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SCSDC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.signature` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Document Type for User
**Package:** `ec.com.sidesoft.doctypeByUser`

# Module overview — Document Type for User

## Functional

El módulo 'Document Type for User' permite a los usuarios gestionar los tipos de documentos asociados a su perfil dentro del ERP Openbravo. Este módulo está diseñado principalmente para usuarios de negocio que requieran acceder y configurar los documentos a los que tienen derecho, así como para el soporte técnico de nivel 2 que necesite entender la estructura del almacenamiento de estos tipos de documentos. Los actores involucrados incluyen administradores del sistema y usuarios finales que deben interactuar con la funcionalidad de gestión de documentos. Este módulo no tiene dependencias adicionales, lo que facilita su implementación y uso en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/doctypeByUser` |
| Web | `web/ec.com.sidesoft.doctypeByUser/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**0.0.1** (from `AD_MODULE.xml`).

### DB prefix

`SDTU`

# Guía de chat — Document Type for User

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.doctypeByUser`).

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
- «¿Qué es la tabla sdtu_doctype?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo gestionar los tipos de documentos en mi perfil?
- ¿Qué tipos de documentos puedo acceder o modificar?
- ¿Hay validaciones al agregar un nuevo tipo de documento?
- ¿Dónde se almacenan los tipos de documentos que configuro?
- ¿Puedo eliminar un tipo de documento que ya no necesito?
- ¿Cómo puedo saber si tengo permisos para usar ciertos tipos de documentos?
- ¿Es posible personalizar los tipos de documentos que están disponibles para mí?
- ¿Qué debo hacer si encuentro un problema al acceder a los documentos?

# Domain — data model

## Functional

El modelo de datos del módulo se basa en la entidad cabecera 'sdtu_doctype', que almacena los tipos de documentos disponibles para los usuarios. Si bien no se especifican etapas adicionales dentro del proceso, se puede inferir que la entidad podría estar relacionada con otros elementos del sistema a través de llaves foráneas en situaciones de configuración de permisos o asignación de roles. Es importante destacar que el módulo no cuenta con triggers o funciones PL, lo que sugiere que la lógica de negocio está relativamente simplificada y que las interacciones son directas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sdtu_doctype` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sdtu_doctype` | sdtu_doctype | — | — | ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org; ad_user_id→ad_user | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `sdtu_doctype_key`; Cols: c_doctype_id, ad_user_id; `SDTU_DOCTYPE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sdtu_doctype` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

No se han definido ventanas específicas para la interfaz de usuario en este módulo, lo que indica que la presentación y navegación tal vez se manejen mediante una interfaz más genérica, o que la funcionalidad de este módulo se integre en otras áreas del sistema. La ausencia de múltiples ventanas sugiere un enfoque de gestión más centralizado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.doctypeByUser.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.doctypeByUser.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Document Transaction

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Transaction | `C_Doctype_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

No hay procesos definidos, botones de acción o informes específicos asociados al módulo. Aunque esto podría indicar una experiencia de usuario simple en la que las acciones son limitadas, se espera que cualquier interacción se realice a través de formularios estándar o funcionalidades dispuestas en el ERP principal. La validación típica esperada en procesos de este tipo incluiría la verificación de permisos de usuario y la inclusión correcta de los tipos de documentos asociados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.doctypeByUser.es_ES/referencedata/translation/`.

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

No se han definido clases Java para este módulo, lo que sugiere que la funcionalidad está diseñada para operar de manera independiente en su nivel de implementación sin necesidad de lógica adicional basada en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.doctypeByUser`.

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
| AD_VAL_RULE | — | `C_DocType AR/AP Invoices and Credit Memos for User` | `C_DocType.DocBaseType IN ('ARI', 'API','ARC','APC','ARI_RM') 
AND C_DocType.IsSOTrx='@IsSOTrx@' 
AND (AD_ISORGINCLUDED(@` |
| AD_VAL_RULE | — | `C_DocType PO/SO For User` | `C_DocType.DocBaseType IN ('SOO', 'POO') AND C_DocType.IsSOTrx='@IsSOTrx@'
AND (AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.AD` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Dado que el módulo no tiene triggers ni funciones PL definidas, su rol principalmente se centra en el almacenamiento de datos en la tabla 'sdtu_doctype' sin lógica adicional en la base de datos. Esto simplifica la configuración y mantenimiento, aunque podría limitar la flexibilidad para implementaciones más complejas en el futuro.

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

Módulo: `ec.com.sidesoft.doctypeByUser`.

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

# Glosario — prefijo `SDTU`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SDTU` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.doctypeByUser` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
