# Openbravo Sidesoft — Devoluciones y Descuentos

> Devoluciones de clientes y proveedores, descuentos en factura, descuento de cuota, descuentos backoffice, IRBP.

**Paquetes incluidos (6):**
- `com.sidesoft.localization.ecuador.refunds` — Localization of Ecuador - Refunds
- `ec.cusoft.refund` — Sidesoft Cusoft Refund
- `ec.com.sidesoft.factura.discount` — Sidesoft Discounts Invoice
- `ec.com.sidesoft.discount.accounting` — Discount accouting
- `ec.com.sidesoft.discount.quota.salesinvoices` — Sidesoft Discount of Quota of Sales Invoices to Employees
- `ec.com.sidesoft.backoffice.discount` — Sidesoft Back Office Discount


---
## Localization of Ecuador - Refunds
**Package:** `com.sidesoft.localization.ecuador.refunds`

# Module overview — Localization of Ecuador - Refunds

## Functional

El módulo 'Localization of Ecuador - Refunds' se encarga de la gestión de reembolsos en Ecuador, permitiendo a las empresas manejar devoluciones de forma efectiva dentro del sistema ERP Openbravo. Los actores principales son los usuarios de negocio que gestionan las devoluciones y el soporte técnico, que pueden necesitar soportar la configuración y problemáticas relacionadas. El alcance incluye la integración con otras funcionalidades de localización ecuatoriana, como las retenciones fiscales y la contabilidad integral. Sus dependencias incluyen la compatibilidad con otros módulos relacionados con la localización y la gestión de datos fiscales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/localization/ecuador/refunds` |
| Web | `web/com.sidesoft.localization.ecuador.refunds/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Localization of Ecuador - Withholdings

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSRE`

# Guía de chat — Localization of Ecuador - Refunds

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.localization.ecuador.refunds`).

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
- «¿Qué es la tabla ssre_refundinvoice?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo crear un nuevo reembolso?
- ¿Qué validaciones se aplican al número de factura del reembolso?
- ¿Cómo puedo modificar un reembolso ya creado?
- ¿Dónde encuentro el informe de reembolsos?
- ¿Qué debo hacer si el sistema no me permite completar un reembolso?
- ¿Cómo se gestionan los impuestos en un reembolso?
- ¿Puedo rechazar un reembolso y cuáles son las consecuencias?
- ¿Qué datos son necesarios para registrar un reembolso?

# Domain — data model

## Functional

En este módulo, la entidad principal es 'ssre_refundinvoice', que actúa como cabecera de los reembolsos. Esta entidad se relaciona con otras tablas como 'C_INVOICE', 'C_INVOICELINE' y 'C_INVOICELINETAX' para llevar un control preciso de los datos de facturación asociados a los reembolsos. Las etapas del proceso de reembolso incluyen el registro del detalle de la factura original y la validación de campos a través de varios triggers, como 'SSRE_VALIDATEDOCUMENTNO_TRG' y 'SSRE_VALIDAUTHORIREFUND_TRG', que aseguran que los datos ingresados cumplan con las normativas locales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssre_refund` |
| `ssre_refund_configuration` |
| `ssre_refundinvoice` |
| `ssre_refundinvoiceline` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssre_refund` | ssre_refund | — | — | ad_client_id→ad_client; sswh_codelivelihoodt_id→sswh_codelivelihoodt; sswh_livelihoodt_id→sswh_livelihoodt; ad_org_id→ad_org | Detalle enlazado a ad_client, sswh_codelivelihoodt, sswh_livelihoodt. | PK `ssre_refunded_key`; Cols: type, code, value, sswh_livelihoodt_id, sswh_codelivelihoodt_id; `SSRE_REFUNDED_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssre_refund_configuration` | SSRE_Refund_Configuration | — | `SSRE_REFUND_CONFIGURATION_UN` (ad_client_id, ad_org_id) | ad_client_id→ad_client; ad_org_id→ad_org; m_product_id→m_product | Parametrización / catálogo de soporte. | PK `ssre_refund_configuration_key`; Cols: quantity, m_product_id; `SSRE_REF_CONFIG_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `ssre_refundinvoice` | ssre_refundinvoice | `SSRE_DATEREFUND_TRG`; `SSRE_REFUNDINVOICE_AUTO_TRG`; `SSRE_UPDATE_AMOUNTS_TRG`; `SSRE_VALIDATEDOCUMENTNO_TRG` (+2) | — | sswh_codelivelihoodt_id→sswh_codelivelihoodt; ad_client_id→ad_client; c_invoice_id→c_invoice; sswh_livelihoodt_id→sswh_livelihoodt; ad_org_id→ad_org | Detalle enlazado a ad_client, c_invoice, sswh_codelivelihoodt. Validado por trigger(s): SSRE_DATEREFUND_TRG, SSRE_REFUNDINVOICE_AUTO_TRG, SSRE_UPDATE_AMOUNTS_TRG, SSRE_VALIDATEDOCUMENTNO_TRG, SSRE_VA… | PK `ssre_refundinvoice_key`; Cols: c_invoice_id, sswh_livelihoodt_id, sswh_codelivelihoodt_id, taxidtype, taxidruc; `SSRE_REFUNDINV_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssre_refundinvoiceline` | ssre_refundinvoiceline | `SSRE_REFUNDINVOICE_LINE_TRG`; `SSRE_REFUNDINV_DROPLINE_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; m_product_id→m_product; ssre_refundinvoice_id→ssre_refundinvoice; c_tax_id→c_tax | Detalle enlazado a ad_client, ad_org, m_product. Validado por trigger(s): SSRE_REFUNDINVOICE_LINE_TRG, SSRE_REFUNDINV_DROPLINE_TRG. | PK `ssre_refundinvoiceline_key`; Cols: ssre_refundinvoice_id, m_product_id, taxbase, c_tax_id, taxamt; `SSRE_REFUNDINVLINE_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssre_refund` |
| `SSRE_Refund_Configuration` |
| `ssre_refundinvoice` |
| `ssre_refundinvoiceline` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_INVOICE`, `C_INVOICELINE`, `C_INVOICELINETAX`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Los usuarios navegan por el módulo a través de dos ventanas principales: 'Refund Configuration' y 'Refunded'. La primera permite la configuración de parámetros relacionados con los reembolsos, mientras que la segunda muestra el estado y los detalles de los reembolsos registrados, facilitando la gestión y consulta de información relevante.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.localization.ecuador.refunds.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Refund Configuration | Refund Configuration |
| Refunded | Refunded |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Detalle de Reembolsos | Refunds Details | No |
| Liquidación de Reembolsos | Refund | No |
| Reembolsos | Refund of report | No |
| Refund Configuration | Refund Configuration | No |
| Refunded | Refunded | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.localization.ecuador.refunds.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Refund Configuration

- **AD_WINDOW_ID:** `A9F1984EB63B41569F9803B5239A7F5C`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Refund Configuration | `881D8DE122E7416CB612121BC0F3B747` | 0 |

### Ventana: Refunded

- **AD_WINDOW_ID:** `38E07F3943A440F6BD5315CCF0D5CB80`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Refunded | `7F12FB4BCEEE4B57A39E7AC93F885EB8` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `263`

- **AD_TAB_ID:** `263` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 120 | Is Refund | `EM_Ssre_Isrefund` | No | Sí | — |

### Pestaña `290`

- **AD_TAB_ID:** `290` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 103 | Refund | `em_ssre_refunded_id` | No | No | — |
| 104 | Customer | `EM_Ssre_C_Bpartner_ID` | No | No | — |

### Pestaña `291`

- **AD_TAB_ID:** `291` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 78 | Refund | `EM_Ssre_Refunded_ID` | No | No | — |
| 79 | Customer | `EM_Ssre_C_Bpartner_ID` | No | No | — |

### Refund Invoice Line

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | EM_Imdlv_Product_ID | `M_Product_ID` | No | No | — |
| 50 | Tax | `C_Tax_ID` | No | No | — |
| 60 | Taxbaseline | `Taxbase` | No | No | — |
| 70 | Taxamt | `Taxamt` | No | No | — |
| 80 | Taxice | `Taxice` | No | No | — |
| 90 | Grand Total Amount | `Grandtotal` | No | No | — |

### Refunded (ventana: Refunded)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 25 | Search Key | `Value` | No | No | — |
| 30 | Type | `Type` | No | No | — |
| 40 | Code | `Code` | No | No | — |
| 60 | Livelihood | `Sswh_Livelihoodt_ID` | No | No | — |
| 70 | Sswh_Codelivelihoodt_ID | `Sswh_Codelivelihoodt_ID` | No | No | — |
| 80 | Customer Account | `Customer_Account` | No | No | — |

### Refund Configuration (ventana: Refund Configuration)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Product | `M_Product_ID` | No | No | — |
| 30 | Quantity | `Quantity` | No | No | — |

### Refund Invoice

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Invoice | `C_Invoice_ID` | No | Sí | — |
| 40 | Livelihood | `Sswh_Livelihoodt_ID` | No | No | — |
| 50 | Sswh_Codelivelihoodt_ID | `Sswh_Codelivelihoodt_ID` | No | No | — |
| 55 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 60 | Taxidtype | `Taxidtype` | No | No | — |
| 70 | Taxidruc | `Taxidruc` | No | No | — |
| 80 | Stablishment | `Stablishment` | No | No | — |
| 90 | Shell | `Shell` | No | No | — |
| 100 | Order Reference | `Poreference` | No | No | — |
| 110 | Dateemission | `Dateemission` | No | No | — |
| 120 | Withholding authorization | `Withholdingauthorization` | No | No | — |
| 140 | Tax Base Refund | `Taxbaserefund` | No | Sí | — |
| 150 | Taxable Amount | `Taxbaseamt` | No | Sí | — |
| 160 | Tax Amount | `Taxamt` | No | Sí | — |
| 170 | Taxice | `Taxice` | No | Sí | — |
| 180 | Untaxed basis | `Untaxed_Basis` | No | Sí | — |
| 190 | Exempt Base | `Exemptbase` | No | Sí | — |
| 200 | Grand Total Amount | `Grandtotal` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos típicos en este módulo incluyen botones como 'Completar', 'Retornar' y 'Rechazar', que permiten gestionar el flujo de las solicitudes de reembolso. El informe relacionado, 'Ssre_ProcessPrintRefoundInvoice', proporciona un formato estandarizado para la impresión de las facturas de reembolso. Frecuentemente se llevan a cabo validaciones de campos como el número de factura y el ID tributario, asegurando así la integridad de los datos introducidos en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.localization.ecuador.refunds.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Pos Load Lines RefundInv | Pos Load Lines RefundInv | Ssre_PosLoadLinesRefundInv | `Ssre_PosLoadLinesRefundInv` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Botón (PL/pgSQL) | Pre Load Lines RefundInv | Pre Load Lines RefundInv | Ssre_PreLoadLinesRefundInv | `Ssre_PreLoadLinesRefundInv` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Proceso / otro | Informe de Reembolso | Refund of report | Refund of report | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Refunds Details | Refunds Details | Refunds Details | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Ssre_ProcessPrintRefoundInvoice | Ssre_ProcessPrintRefoundInvoice | Ssre_ProcessPrintRefoundInvoice | Java `Ssre_ReportPrintRefoundInvoice` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/localization/ecuador/refunds/ad_process/Ssre_ReportPrintRefoundInvoice.java` |
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
| Reporte | Ssre_ProcessPrintRefoundInvoice | `Ssre_ReportPrintRefoundInvoice` | Informe (servlet PDF) | `—` | — | `src/com/sidesoft/localization/ecuador/refunds/ad_process/Ssre_ReportPrintRefoundInvoice.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Pos Load Lines RefundInv | Pos Load Lines RefundInv | Ssre_PosLoadLinesRefundInv | `Ssre_PosLoadLinesRefundInv` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Botón (PL/pgSQL) | Pre Load Lines RefundInv | Pre Load Lines RefundInv | Ssre_PreLoadLinesRefundInv | `Ssre_PreLoadLinesRefundInv` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Proceso / otro | Informe de Reembolso | Refund of report | Refund of report | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Refunds Details | Refunds Details | Refunds Details | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Pos Load Lines RefundInv | Pos Load Lines RefundInv | PL `Ssre_PosLoadLinesRefundInv` | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point |
| Botón (PL/pgSQL) | Pre Load Lines RefundInv | Pre Load Lines RefundInv | PL `Ssre_PreLoadLinesRefundInv` | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point |
| Proceso / otro | Informe de Reembolso | Refund of report | — | — | — |
| Proceso / otro | Refunds Details | Refunds Details | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Ssre_ProcessPrintRefoundInvoice | Ssre_ProcessPrintRefoundInvoice | Ssre_ProcessPrintRefoundInvoice | Java `Ssre_ReportPrintRefoundInvoice` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/localization/ecuador/refunds/ad_process/Ssre_ReportPrintRefoundInvoice.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 4**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **1**; archivos `*.jrxml` en el repo = **4**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Ssre_ProcessPrintRefoundInvoice | `Ssre_ProcessPrintRefoundInvoice` | Java `Ssre_ReportPrintRefoundInvoice`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Ssre_ProcessPrintRefoundInvoice |

### Plantillas sin proceso en diccionario

- `src/com/sidesoft/localization/ecuador/refunds/ad_reports/RptR_Refund.jrxml`
- `src/com/sidesoft/localization/ecuador/refunds/ad_reports/Rpt_RefoundInvoice.jrxml`
- `src/com/sidesoft/localization/ecuador/refunds/ad_reports/Rpt_RefoundInvoiceT.jrxml`
- `src/com/sidesoft/localization/ecuador/refunds/ad_reports/Rpt_RefundsDetail.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `SSRE_MoreThanOnePricelist` | The selected lines have associated more than one price list. Please, select one Price List for the Sales Invoice. | The selected lines have associated more than one price list. Please, select one Price List for the Sales Invoice. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRE_Duplicate_Authorization` | The authorization number entered has already been used on another refund invoice. Please use a unique number to continue | The authorization number entered has already been used on another refund invoice. Please use a unique number to continue | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRE_MoreThanOneOrg` | The selected lines are from more than one organization. Please, select the Organization of the Sales Invoice. | The selected lines are from more than one organization. Please, select the Organization of the Sales Invoice. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRE_Refund` | This process will create the Sales Invoices necessary to complete all the refund lines. 
An invoice line is created for each refund line.
The Invoice Date is the date of the Sales Invoices. 
The Business Partner is the preferred customer the Sales Invoices. If it is left blank, then the Partner defined in the refund is used. If these are not defined, then the current vendor set for the product is used.
The Price List is the price list for the Business Partner.
The Organization is the organization used by the Sales Invoices. | This process will create the Sales Invoices necessary to complete all the refund lines. 
An invoice line is created for each refund line.
The Invoice Date is the date of the Sales Invoices. 
The Business Partner is the preferred customer the Sales Invoices. If it is left blank, then the Partner defined in the refund is used. If these are not defined, then the current vendor set for the product is used.
The Price List is the price list for the Business Partner.
The Organization is the organization used by the Sales Invoices. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRE_CustomerWithNoPaymentTerm` | The customer does not have a default Payment Term defined. | The customer does not have a default Payment Term defined. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRE_ReferenceRefund` | No se ha registrado Facturas de Reembolso | No se ha registrado Facturas de Reembolso | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRE_MoreThanOneCustomer` | The selected lines have associated more than one customer. Please select the desired customer of the Sales Invoice. | The selected lines have associated more than one customer. Please select the desired customer of the Sales Invoice. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRE_AllLinesNullCustomer` | None of the selected lines have a customer associated.  Please select the desired customer of the Sales Invoice. | None of the selected lines have a customer associated.  Please select the desired customer of the Sales Invoice. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRE_DateRefund` | Fecha reembolso debe ser menor o igual a la fecha de la cabecera de la factura | Fecha reembolso debe ser menor o igual a la fecha de la cabecera de la factura | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `EM_SSRE_Refund_Customer` | No customer to be refunded. | No customer to be refunded. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSRE_AllLinesSameCustomer` | All the selected lines have the same associated customer | All the selected lines have the same associated customer | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo también incorpora funcionalidades en Java, como las clases en la ruta 'src/com/sidesoft/localization/ecuador/refunds/ad_callouts', que se encargan de manejar la lógica de negocio dentro de las solicitudes de reembolso a través de llamadas automáticas que verifican y ajustan datos en función de entradas del usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.localization.ecuador.refunds`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Add_Refund` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/refunds/ad_callouts/Add_Refund.java` |
| `UpdateOnlyTotalRefund` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/refunds/ad_callouts/UpdateOnlyTotalRefund.java` |
| `UpdateTaxidEmployeeRefund` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/refunds/ad_callouts/UpdateTaxidEmployeeRefund.java` |
| `UpdateTotalRefund` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/refunds/ad_callouts/UpdateTotalRefund.java` |
| `UpdateTotalRefundLines` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/refunds/ad_callouts/UpdateTotalRefundLines.java` |
| `Refund` | ad_forms | HttpSecureAppServlet | — | `src/com/sidesoft/localization/ecuador/refunds/ad_forms/Refund.java` |
| `Ssre_ReportPrintRefoundInvoice` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/refunds/ad_process/Ssre_ReportPrintRefoundInvoice.java` |
| `InvoiceLineEventHandle` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/localization/ecuador/refunds/event/InvoiceLineEventHandle.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSRE_C_INVOICE_TRG` | `c_invoice` | before UPDATE | Se comenta esta linea ya que no permite descontabilizar; EXECUTE IMMEDIATE 'ALTER TRIGGER c_invoicelinetax_trg DISABLE';; EXECUTE IMMEDIATE 'ALTER TRIGGER c_invoicelinetax_trg ENABLE'; |
| Trigger `SSRE_DATEREFUND_TRG` | `ssre_refundinvoice` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSRE_FACT_ACCT_TRG` | `fact_acct` | before INSERT | La Cuenta del Producto y del Impuesto es la misma |
| Trigger `SSRE_INVOICELINE_TRG` | `c_invoiceline` | before INSERT/UPDATE | Check if is customer refund and customer is not null |
| Trigger `SSRE_INVOICE_TRG` | `c_invoice` | after INSERT/UPDATE | Check if is customer refund and customer is not null |
| Trigger `SSRE_REFUNDINVOICE_AUTO_TRG` | `ssre_refundinvoice` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSRE_REFUNDINVOICE_LINE_TRG` | `ssre_refundinvoiceline` | after INSERT/UPDATE | Variables Iniciales para los Impuestos de cada linea |
| Trigger `SSRE_REFUNDINV_DROPLINE_TRG` | `ssre_refundinvoiceline` | after DELETE | Variables Iniciales para los Impuestos de cada linea |
| Trigger `SSRE_UPDATE_AMOUNTS_TRG` | `ssre_refundinvoice` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSRE_VALIDATEDOCUMENTNO_TRG` | `ssre_refundinvoice` | before INSERT/UPDATE | El Nro. de Factura debe tener 9 digitos.; La Fecha del Reembolso no puede ser mayor a la fecha de la Factura(Cabecera). |
| Trigger `SSRE_VALIDATETAXID_TRG` | `ssre_refundinvoice` | before INSERT/UPDATE | Validación reutilizable de campos. |
| Trigger `SSRE_VALIDATE_ISREFUND_TRG` | `c_invoice` | before INSERT/UPDATE | Validación reutilizable de campos. |
| Trigger `SSRE_VALIDAUTHORIREFUND_TRG` | `ssre_refundinvoice` | before INSERT/UPDATE | RAISE_APPLICATION_ERROR(-20000, '@SSWH_AutorizationMustBeLengthNumeric@'); |
| AD_VAL_RULE | — | `TaxRate - Withholding Type` | `—` |
| Java event/validator | `InvoiceLineEventHandle` | persistencia/UI | *(leer `src/com/sidesoft/localization/ecuador/refunds/event/InvoiceLineEventHandle.java`)* |
| Función PL `ssre_posloadlinesrefundinv` | — | invocación proceso | sccc_preunprocess - PreUnprocess Extension Point |
| Función PL `ssre_preloadlinesrefundinv` | — | invocación proceso | sccc_preunprocess - PreUnprocess Extension Point |
| Función PL `ssre_validatelivelihood_refund` | — | invocación proceso | ERROR=Debe Ingresar Facturas de Reembolso; ERROR=El valor de Facturas de Reembolso supera el valor de la factura; ERROR=El valor de las Facturas de Reembolso deben ser igual al valor total de la factura |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers juegan un papel clave en la validación de datos y en la ejecución de procedimientos necesarios durante la creación y modificación de registros de reembolsos. Las funciones PL/pgSQL ayudan a mantener la lógica de negocio, las cuales son ejecutadas a través de los triggers definidos, como 'SSRE_REFUNDINVOICE_AUTO_TRG', que contiene procedimientos para actualizar automáticamente campos relevantes en el modelo de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSRE_C_INVOICE_TRG` | `c_invoice` | before | UPDATE | Se comenta esta linea ya que no permite descontabilizar; EXECUTE IMMEDIATE 'ALTER TRIGGER c_invoicelinetax_trg DISABLE';; EXECUTE IMMEDIATE 'ALTER TRIGGER c_invoicelinetax_trg ENABLE'; | `model/triggers/SSRE_C_INVOICE_TRG.xml` |
| `SSRE_INVOICE_TRG` | `c_invoice` | after | INSERT/UPDATE | Check if is customer refund and customer is not null | `model/triggers/SSRE_INVOICE_TRG.xml` |
| `SSRE_VALIDATE_ISREFUND_TRG` | `c_invoice` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SSRE_VALIDATE_ISREFUND_TRG.xml` |
| `SSRE_INVOICELINE_TRG` | `c_invoiceline` | before | INSERT/UPDATE | Check if is customer refund and customer is not null | `model/triggers/SSRE_INVOICELINE_TRG.xml` |
| `SSRE_FACT_ACCT_TRG` | `fact_acct` | before | INSERT | La Cuenta del Producto y del Impuesto es la misma | `model/triggers/SSRE_FACT_ACCT_TRG.xml` |
| `SSRE_DATEREFUND_TRG` | `ssre_refundinvoice` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSRE_DATEREFUND_TRG.xml` |
| `SSRE_REFUNDINVOICE_AUTO_TRG` | `ssre_refundinvoice` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSRE_REFUNDINVOICE_AUTO_TRG.xml` |
| `SSRE_UPDATE_AMOUNTS_TRG` | `ssre_refundinvoice` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSRE_UPDATE_AMOUNTS_TRG.xml` |
| `SSRE_VALIDATEDOCUMENTNO_TRG` | `ssre_refundinvoice` | before | INSERT/UPDATE | El Nro. de Factura debe tener 9 digitos.; La Fecha del Reembolso no puede ser mayor a la fecha de la Factura(Cabecera). | `model/triggers/SSRE_VALIDATEDOCUMENTNO_TRG.xml` |
| `SSRE_VALIDATETAXID_TRG` | `ssre_refundinvoice` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SSRE_VALIDATETAXID_TRG.xml` |
| `SSRE_VALIDAUTHORIREFUND_TRG` | `ssre_refundinvoice` | before | INSERT/UPDATE | RAISE_APPLICATION_ERROR(-20000, '@SSWH_AutorizationMustBeLengthNumeric@'); | `model/triggers/SSRE_VALIDAUTHORIREFUND_TRG.xml` |
| `SSRE_REFUNDINVOICE_LINE_TRG` | `ssre_refundinvoiceline` | after | INSERT/UPDATE | Variables Iniciales para los Impuestos de cada linea | `model/triggers/SSRE_REFUNDINVOICE_LINE_TRG.xml` |
| `SSRE_REFUNDINV_DROPLINE_TRG` | `ssre_refundinvoiceline` | after | DELETE | Variables Iniciales para los Impuestos de cada linea | `model/triggers/SSRE_REFUNDINV_DROPLINE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssre_posloadlinesrefundinv` | Pos Load Lines RefundInv | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point | `model/functions/SSRE_POSLOADLINESREFUNDINV.xml` |
| `ssre_preloadlinesrefundinv` | Pre Load Lines RefundInv | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point | `model/functions/SSRE_PRELOADLINESREFUNDINV.xml` |
| `ssre_validatelivelihood_refund` | — | ERROR=Debe Ingresar Facturas de Reembolso; ERROR=El valor de Facturas de Reembolso supera el valor de la factura; ERROR=El valor de las Facturas de Reembolso deben ser igual al valor total de la factura; ERROR=Este Tipo… | ERROR=Debe Ingresar Facturas de Reembolso; ERROR=El valor de Facturas de Reembolso supera el valor de la factura; ERROR=El valor de las Facturas de Reembolso deben ser igual al valor total de la factura; ERROR=Este Tipo de Comprobante no puede tener lineas de Reembolso; SELECT I.issotrx, I.docstatus, I.c_doctype_id, I.em_sswh_livelihood, I.totallines --old; VALIDO QUE SEA FACTURA DE REEMBOLSO Y QUE TENGA FACTURAS REGISTRADAS | `model/functions/SSRE_VALIDATELIVELIHOOD_REFUND.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Pos Load Lines RefundInv | `Ssre_PosLoadLinesRefundInv` | Botón (PL/pgSQL) | PL `Ssre_PosLoadLinesRefundInv` | N | sccc_preunprocess - PreUnprocess Extension Point |
| 2 | Pre Load Lines RefundInv | `Ssre_PreLoadLinesRefundInv` | Botón (PL/pgSQL) | PL `Ssre_PreLoadLinesRefundInv` | N | sccc_preunprocess - PreUnprocess Extension Point |
| 3 | Ssre_ProcessPrintRefoundInvoice | `Ssre_ProcessPrintRefoundInvoice` | Reporte | Java `Ssre_ReportPrintRefoundInvoice` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |

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

Módulo: `com.sidesoft.localization.ecuador.refunds`.

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

# Glosario — prefijo `SSRE`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSRE` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.localization.ecuador.refunds` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Ssre_PosLoadLinesRefundInv` — Pos Load Lines RefundInv
- `Ssre_PreLoadLinesRefundInv` — Pre Load Lines RefundInv
- `Refund of report` — Informe de Reembolso
- `Refunds Details` — Refunds Details
- `Ssre_ProcessPrintRefoundInvoice` — Ssre_ProcessPrintRefoundInvoice

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Cusoft Refund
**Package:** `ec.cusoft.refund`

# Module overview — Sidesoft Cusoft Refund

## Functional

El módulo Sidesoft Cusoft Refund permite gestionar los reembolsos en Openbravo, asegurando que se sigan los procedimientos adecuados para la restitución de fondos a los clientes. Este módulo es utilizado principalmente por el personal del departamento financiero y contable, así como por los administradores del sistema para llevar un control riguroso de los reembolsos. Se presenta como una herramienta indispensable para optimizar la gestión del ciclo de ingresos y garantizar la corrección fiscal de las operaciones de reembolso. Las dependencias incluyen componentes críticos del núcleo de Openbravo, lo que garantiza su integración y funcionalidad en la versión correcta del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/cusoft/refund` |
| Web | `web/ec.cusoft.refund/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`EEIR`

# Guía de chat — Sidesoft Cusoft Refund

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.cusoft.refund`).

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
- «¿Qué es la tabla eeir_refund?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo registro un reembolso en el sistema?
- ¿Qué debo hacer si el reembolso no se procesa correctamente?
- ¿Puedo cambiar los datos de un reembolso después de crearlo?
- ¿Cómo se validan los campos requeridos para un reembolso?
- ¿Qué pasos debo seguir para verificar la información de un reembolso?
- ¿Dónde puedo encontrar informes sobre reembolsos anteriores?
- ¿Cómo puedo cancelar un reembolso en el sistema?
- ¿A quién debo dirigir mis preguntas sobre el módulo de reembolsos?

# Domain — data model

## Functional

La entidad central del módulo es la tabla 'eeir_refund', que contiene todos los datos relevantes asociados a cada reembolso. La tabla se compone de siete campos que incluyen información como el ID del reembolso, el monto, la fecha y otros datos pertinentes. La gestión del flujo de datos se ve respaldada por un trigger clave, 'EEIR_VALIDATEFIELS_TRG', que garantiza que todos los campos sean completados adecuadamente antes de que se procese un reembolso, previniendo errores y asegurando la integridad de la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `eeir_refund` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `eeir_refund` | EEIR_Refund | `EEIR_VALIDATEFIELS_TRG` | — | eeir_bpartner_id→c_bpartner; eeir_invoice_id→c_invoice; c_invoice_id→c_invoice; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a c_bpartner, c_invoice. Validado por trigger(s): EEIR_VALIDATEFIELS_TRG. | PK `eeir_refund_key`; Cols: eeir_bpartner_id, c_invoice_id, eeir_invoice_id, eeir_base, eeir_tax; `EEIR_REFUND_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `EEIR_Refund` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Aunque no hay ventanas específicas en la UI, el módulo se integra en el flujo de trabajo general de Openbravo a través de la tabla de reembolsos. Los usuarios navegarán a través del sistema utilizando las funciones del ERP para acceder a los registros de reembolso y gestionar la información relevante dentro del contexto de otras operaciones financieras.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.cusoft.refund.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.cusoft.refund.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Refund

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Business Partner | `Eeir_Bpartner_ID` | No | No | — |
| 40 | Purchase Invoice | `Eeir_Invoice_ID` | No | No | — |
| 50 | Base | `Eeir_Base` | No | No | — |
| 60 | Tax | `Eeir_Tax` | No | No | — |
| 70 | Total | `Eeir_Total` | No | No | — |
| 80 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo no presenta botones de proceso específicos; sin embargo, los usuarios suelen interactuar con funciones típicas como completar, retornar o rechazar transacciones de reembolso. Es crucial que los usuarios estén conscientes de las validaciones frecuentes que pueden surgir, especialmente relacionadas con el completado obligatorio de campos, lo cual es administrado por el trigger mencionado. No hay informes asociados directamente al módulo, lo que sugiere que la extracción de datos o la generación de reportes será a través de herramientas estándares del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.cusoft.refund.es_ES/referencedata/translation/`.

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

El módulo incluye una clase Java, 'Eeir_callValue', que se utiliza para realizar cálculos específicos sobre los reembolsos, como el cálculo de montos impositivos asociados a las facturas, proporcionando así una capa adicional de lógica empresarial que se apoya en la interacción con el modelo de datos de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.cusoft.refund`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Eeir_callValue` | ad_callouts | SimpleCallout | — | `src/ec/cusoft/refund/ad_callouts/Eeir_callValue.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `EEIR_VALIDATEFIELS_TRG` | `eeir_refund` | before INSERT/UPDATE | Se deben llenar todos los campos |
| AD_VAL_RULE | — | `eeir_bpartner_validate` | `C_BPartner.isactive = 'Y'` |
| AD_VAL_RULE | — | `eeir_invoice_validate` | `C_Invoice.issotrx = 'N' 
AND C_Invoice.c_bpartner_id = @Eeir_Bpartner_ID@ 
AND C_Invoice.Docstatus = 'CO' 
AND C_Invoice` |
| Función PL `eeir_validatecheck` | — | invocación proceso | Deben existir registros en la solapa reembolso |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL desempeñan un papel fundamental para el soporte en este módulo, asegurando que se mantenga la calidad de los datos al prevenir la entrada de información incompleta. El único trigger en funcionamiento valida que todos los campos sean llenados, lo que es crucial para mantener la integridad de los procesos contables y financieros.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `EEIR_VALIDATEFIELS_TRG` | `eeir_refund` | before | INSERT/UPDATE | Se deben llenar todos los campos | `model/triggers/EEIR_VALIDATEFIELS_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `eeir_validatecheck` | — | Deben existir registros en la solapa reembolso | Deben existir registros en la solapa reembolso | `model/functions/EEIR_VALIDATECHECK.xml` |
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

Módulo: `ec.cusoft.refund`.

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

# Glosario — prefijo `EEIR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `EEIR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.cusoft.refund` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Discounts Invoice
**Package:** `ec.com.sidesoft.factura.discount`

# Module overview — Sidesoft Discounts Invoice

## Functional

El módulo Sidesoft Discounts Invoice tiene como propósito gestionar los descuentos aplicados en las facturas electrónicas. Sus principales actores son los usuarios de negocio que necesitan aplicar estos descuentos y los desarrolladores que adminstran la funcionalidad del ERP Openbravo. Este módulo se integra con el sistema de facturación existente y es esencial para mantener la precisión en las transacciones comerciales. No presenta dependencias adicionales que puedan afectar su funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/factura/discount` |
| Web | `web/ec.com.sidesoft.factura.discount/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSEED`

# Guía de chat — Sidesoft Discounts Invoice

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.factura.discount`).

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

- ¿Cómo aplico un descuento en una factura?
- ¿Qué sucede si el descuento supera el precio límite?
- ¿Cómo puedo verificar los descuentos aplicados anteriormente?
- ¿Hay algún informe para ver el impacto de los descuentos?
- ¿Dónde encuentro los parámetros para configurar los descuentos?
- ¿Puedo aplicar descuentos múltiples en una sola línea de factura?
- ¿Qué validaciones se deben cumplir al aplicar un descuento?
- ¿Cómo recupero una factura con un descuento incorrecto?

# Domain — data model

## Functional

Este módulo modifica la tabla principal 'C_INVOICELINE', permitiendo la inclusión de descuentos específicos en las líneas de factura. La gestión de descuentos se realiza a través de un proceso que permite recalcular los importes de las facturas dependiendo de los descuentos aplicados. Aunque no se han definido triggers en este módulo, su lógica puede depender de funciones especiales para recalcular montos, aunque estas no están explícitamente documentadas.

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

`C_INVOICELINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación en el módulo se realiza a través de un entorno de usuario donde se accede a las facturas de ventas y se pueden aplicar descuentos. Al no existir ventanas adicionales definidas para este módulo, la interacción se limita a modificaciones en las facturas existentes ya presentes en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.factura.discount.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.factura.discount.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `270`

- **AD_TAB_ID:** `270` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 71 | Discount | `EM_Sseed_Discount` | No | No | — |
| 72 | Initial subtotal | `EM_Sseed_Initial_Subtotal` | No | Sí | — |
| 73 | Initial unit price | `EM_Sseed_Initialunitprice` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo no incluye botones de proceso específicos ni informes predefinidos, lo cual sugiere que su funcionalidad se centra en la modificación directa de las líneas de factura. Sin embargo, se debe considerar que las validaciones son críticas al aplicar descuentos, y los usuarios deben asegurarse de que las condiciones de descuento se cumplan para evitar errores en la facturación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.factura.discount.es_ES/referencedata/translation/`.

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

La lógica del módulo se apoya en una clase Java que gestiona el cálculo de descuentos basado en las líneas de factura. Esta clase maneja la validación de diferentes parámetros, como precios y cantidades, para asegurar que los descuentos se apliquen correctamente, reflejando estos cambios en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.factura.discount`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Sseed_Invoice_Amt` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/factura/discount/ad_callouts/Sseed_Invoice_Amt.java` |
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

Aunque no se definen triggers o funciones PL concretas, el módulo depende de la lógica de negocio que puede ser implementada a través de las clases Java. Los desarrolladores pueden crear funciones personalizadas que se llamen en respuesta a eventos en las facturas para calcular automáticamente los descuentos aplicados.

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

Módulo: `ec.com.sidesoft.factura.discount`.

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

# Glosario — prefijo `SSEED`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSEED` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.factura.discount` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Discount accouting
**Package:** `ec.com.sidesoft.discount.accounting`

# Module overview — Discount accouting

## Functional

El módulo de contabilidad de descuentos en Openbravo permite gestionar y contabilizar los descuentos aplicados en las facturas de venta. Su propósito es facilitar el seguimiento preciso de los descuentos para una correcta gestión contable. Este módulo es relevante para usuarios de negocio que realizan la contabilización, así como para desarrolladores y personal de soporte que requieren comprender su funcionamiento y personalización. No tiene dependencias adicionales, lo que simplifica su integración en el sistema Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/discount/accounting` |
| Web | `web/ec.com.sidesoft.discount.accounting/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSDACCT`

# Guía de chat — Discount accouting

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.discount.accounting`).

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

- ¿Cómo puedo contabilizar descuentos en una factura de venta?
- ¿Qué cuentas contables se deben configurar para los descuentos?
- ¿Qué ocurre si una factura tiene más de un descuento aplicado?
- ¿Existen validaciones automáticas al contabilizar descuentos?
- ¿Cómo se reflejan los descuentos en los informes financieros?
- ¿Es posible revertir la contabilización de un descuento?
- ¿Cómo puedo verificar la configuración de las cuentas de descuentos?
- ¿Qué debo hacer si no se calcula el descuento en la factura?

# Domain — data model

## Functional

La entidad central del módulo se relaciona con la tabla extendida M_PRODUCT_CATEGORY_ACCT, donde se gestionan las cuentas contables asociadas a las categorías de productos. Aunque no hay etapas identificadas, el módulo realiza un seguimiento esencial en el proceso de facturación de ventas. Los triggers y funciones PL no están definidos en este módulo, por lo que su ejecución se centra en el manejo directo de las transacciones de cuentas de descuentos dentro del contexto de las facturas de venta.

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

`M_PRODUCT_CATEGORY_ACCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no dispone de ventanas específicas que los usuarios puedan navegar, ya que su funcionalidad está centrada en la ejecución de procesos contables de descuentos que se integran dentro del flujo general de facturación de Openbravo. Los usuarios interactúan con él a través de los procesos contables en las facturas de venta de manera implícita.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.discount.accounting.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.discount.accounting.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `324`

- **AD_TAB_ID:** `324` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 110 | EM_Ssdacct_Discount | `EM_Ssdacct_Discount` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que no se han definido botones o informes específicos dentro del módulo, las interacciones típicas que un usuario podría esperar incluyen la contabilización de una factura que incorpora descuentos. Al ejecutar el proceso contable de la factura, el módulo validará automáticamente si hay descuentos aplicados y procederá a la contabilización correspondiente. Las validaciones frecuentes incluyen la configuración previa de cuentas contables para los descuentos, evitando errores durante el proceso.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.discount.accounting.es_ES/referencedata/translation/`.

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

El módulo presenta una clase Java llamada ExtendAcct que implementa la interfaz AcctProcessTemplate, la cual se encarga de procesar la contabilización de descuentos en las facturas. Esta clase contiene la lógica esencial para calcular descuentos y asignar la cuenta contable de descuentos apropiada durante la contabilización.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.discount.accounting`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ExtendAcct` | ec | AcctProcessTemplate | — | `src/ec/com/sidesoft/discount/accouting/ad_process/ExtendAcct.java` |
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

Aunque no se han identificado triggers ni funciones PL específicas dentro del módulo, su rol es crucial en la actualización y mantenimiento de la información de cuentas. Sin embargo, los desarrolladores pueden utilizar el contexto del framework para manejar eventos relacionados con la ejecución de la lógica contable cuando sea necesario.

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

Módulo: `ec.com.sidesoft.discount.accounting`.

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

# Glosario — prefijo `SSDACCT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSDACCT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.discount.accounting` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Discount of Quota of Sales Invoices to Employees
**Package:** `ec.com.sidesoft.discount.quota.salesinvoices`

# Module overview — Sidesoft Discount of Quota of Sales Invoices to Employees

## Functional

El módulo 'Sidesoft Discount of Quota of Sales Invoices to Employees' está diseñado para gestionar descuentos automáticos en las cuotas de facturas de ventas para empleados. Su propósito es facilitar la administración de esquemas de descuento dentro de un sistema ERP como Openbravo. Los usuarios clave son los administradores del sistema y el personal de nómina, quienes podrán utilizar esta funcionalidad para integrar descuentos a la nómina de los empleados de forma eficiente. Este módulo es compatible con las versiones de Openbravo 2.50 a 3.00 y depende del núcleo y del framework de Openbravo 3.0.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/discount/quota/salesinvoices` |
| Web | `web/ec.com.sidesoft.discount.quota.salesinvoices/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSDQSI`

# Guía de chat — Sidesoft Discount of Quota of Sales Invoices to Employees

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.discount.quota.salesinvoices`).

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
- «¿Qué es la tabla ssdqsi_quota_detail?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo agregar una nueva cuota para un empleado?
- ¿Qué debo hacer si una cuota no se está aplicando correctamente?
- ¿Dónde puedo ver el historial de descuentos aplicados?
- ¿Cómo puedo acceder a los detalles de una factura específica?
- ¿Hay algún informe disponible sobre las cuotas de descuentos?
- ¿Qué sucede si un empleado ya no está en la nómina?
- ¿Se pueden modificar los descuentos después de haber sido aplicados?
- ¿Cómo afecta el proceso de cuotas al cálculo de salarios?

# Domain — data model

## Functional

La entidad cabecera principal del módulo es 'ssdqsi_quota_detail', que almacena los detalles de las cuotas. Esta entidad está relacionada con la gestión de las facturas y puede contener múltiples líneas que representan las facturas específicas asociadas a un empleado. Existen relaciones clave entre las líneas de cuota y otros módulos de facturas y pagos. Un trigger importante dentro del sistema es 'SSDQSI_PENDING_INCOME_STATUS', que se activa en la tabla 'ssdqsi_quota_detail_line' y permite la actualización automática del estado de las cuotas pendientes al realizar cambios en los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssdqsi_quota_detail` |
| `ssdqsi_quota_detail_line` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssdqsi_quota_detail` | SSDQSI_Quota_Detail | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_glitem_id→c_glitem; c_doctype_id→c_doctype (+4) | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `ssdqsi_quota_detail_key`; Cols: c_doctype_id, documentno, c_bpartner_id, payment_date, fin_paymentmethod_id; `SSDQSI_QUOTA_DETAIL_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssdqsi_quota_detail_line` | SSDQSI_Quota_Detail_Line | `SSDQSI_PENDING_INCOME_STATUS` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_invoice_id→c_invoice; ssdqsi_quota_detail_id→ssdqsi_quota_detail | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SSDQSI_PENDING_INCOME_STATUS. | PK `ssdqsi_quota_detail_line_key`; Cols: due_date, c_bpartner_id, c_invoice_id, no_fee, pending_amount; `SSDQSI_QUOTA_DETAIL_LINE_CH`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SSDQSI_Quota_Detail` |
| `SSDQSI_Quota_Detail_Line` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación dentro del módulo se realiza a través de la ventana 'Detalle de Cuotas Facturas Empleados', donde los usuarios pueden visualizar, agregar y modificar las cuotas de las facturas de los empleados. La interfaz permite el acceso a dos pestañas que facilitan la visualización y gestión de la información relacionada con los descuentos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.discount.quota.salesinvoices.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Detalle de Cuotas Facturas Empleados | Detail of Fees Invoices Employees |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Detalle de Cuotas Facturas Empleados | Detail of Fees Invoices Employees | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.discount.quota.salesinvoices.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Detalle de Cuotas Facturas Empleados

- **AD_WINDOW_ID:** `61F5EAF644094E518E27B7E6B2F65277`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `E58A3D9B3234403EB5A84D2E627C836E` | 0 |
| 20 | Lines | `6B67246FEE75442EAE0E766F749F1C0E` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Header (ventana: Detalle de Cuotas Facturas Empleados)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 30 | Document No. | `Documentno` | No | Sí | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Payment_Date | `Payment_Date` | No | No | — |
| 60 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 70 | Tipe_Document_Collections | `Tipe_Document_Collections` | No | No | — |
| 80 | Financial_Account | `FIN_Financial_Account_ID` | No | No | — |
| 90 | G/L Item | `C_Glitem_ID` | No | No | — |
| 100 | Sspr_Concept_ID | `Sspr_Concept_ID` | No | No | — |
| 110 | State | `State` | No | Sí | — |
| 120 | Load_Lines | `Load_Lines` | No | No | — |
| 130 | Process_Lines | `Process` | No | No | — |
| 140 | Active | `Isactive` | No | No | — |
| 150 | Reactive Process | `Reactive` | No | No | — |

### Lines (ventana: Detalle de Cuotas Facturas Empleados)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | DUE_Date | `DUE_Date` | No | Sí | — |
| 30 | Client | `C_Bpartner_ID` | No | Sí | — |
| 40 | Invoice | `C_Invoice_ID` | No | Sí | — |
| 50 | NO_Fee | `NO_Fee` | No | Sí | — |
| 60 | Pending_Amount | `Pending_Amount` | No | Sí | — |
| 80 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los usuarios tienen acceso a tres procesos clave que incluyen botones para cargar líneas de cuotas, procesar líneas de descuentos y posiblemente un botón para realizar acciones específicas en las facturas. Cada proceso se ejecuta mediante un flujo predefinido que valida la información y genera mensajes informativos sobre el estado de la operación, como 'Facturas cargadas' en caso de éxito. Las validaciones frecuentes incluyen la verificación de la existencia de cuotas y la correcta asociación con las facturas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.discount.quota.salesinvoices.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar Lineas | Load_Lines | Load_Lines | Java `LoadLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/LoadLines.java` |
| Botón (Java) | Procesar | Process_Lines | Process_Lines | Java `ProcessLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/ProcessLines.java` |
| Botón (Java) | Reactivar | Reactive Process | Reactive Process | Java `Reactive` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/Reactive.java` |
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
| Botón (Java) | Cargar Lineas | `LoadLines` | Proceso Java (toolbar/background) | `Ssdqsi_Quota_Detail_ID` | — | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/LoadLines.java` |
| Botón (Java) | Procesar | `ProcessLines` | Proceso Java (toolbar/background) | `Ssdqsi_Quota_Detail_ID` | — | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/ProcessLines.java` |
| Botón (Java) | Reactivar | `Reactive` | Proceso Java (toolbar/background) | `Ssdqsi_Quota_Detail_ID` | — | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/Reactive.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar Lineas | Load_Lines | Load_Lines | Java `LoadLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/LoadLines.java` |
| Botón (Java) | Procesar | Process_Lines | Process_Lines | Java `ProcessLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/ProcessLines.java` |
| Botón (Java) | Reactivar | Reactive Process | Reactive Process | Java `Reactive` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/Reactive.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar Lineas | Load_Lines | Java `LoadLines` | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` |
| Botón (Java) | Procesar | Process_Lines | Java `ProcessLines` | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` |
| Botón (Java) | Reactivar | Reactive Process | Java `Reactive` | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` |
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
| `ssdqsi_error_process_line` | error process line | error process line | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

En el módulo, se utilizan cinco clases Java para implementar la lógica de negocio, incluyendo la gestión de eventos relacionados con la creación de nuevas entidades y la actualización de números de documento. Estas clases extienden las funcionalidades del ERP al permitir personalizaciones específicas pertinentes a la gestión de cuotas y descuentos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.discount.quota.salesinvoices`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SL_UpdateDocNumber` | ad_callouts | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_callouts/SL_UpdateDocNumber.java` |
| `UpdateDocNumber` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_callouts/UpdateDocNumber.java` |
| `LoadLines` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/LoadLines.java` |
| `ProcessLines` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/ProcessLines.java` |
| `Reactive` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/discount/quota/salesinvoices/ad_process/Reactive.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSDQSI_PENDING_INCOME_STATUS` | `ssdqsi_quota_detail_line` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `isSequencedDocument` | `C_DocType.IsDocNoControlled='Y'` |
| AD_VAL_RULE | — | `DocType_SSDQSI` | `C_DOCTYPE.AD_TABLE_ID in (select ad_table_id from ad_table where name ='SSDQSI_Quota_Detail')` |
| AD_VAL_RULE | — | `Labor concept` | `Sspr_Concept_ID in (select Sspr_Concept_ID from Sspr_Concept where Conceptsubtype='Out' AND Concepttype='D')` |
| AD_VAL_RULE | — | `Bpartner Active, employee` | `C_Bpartner_ID in (SELECT C_Bpartner_ID FROM C_Bpartner WHERE IsEmployee='Y' AND IsActive='Y')` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers dentro del módulo son fundamentales para manejar las actualizaciones automáticas de los estados de las cuotas. El trigger 'SSDQSI_PENDING_INCOME_STATUS' es responsable de esta funcionalidad, garantizando que el sistema mantenga la coherencia de información en tiempo real. Como no se definen funciones PL adicionales, las lógicas de negocio se manejan principalmente a través de estos triggers.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSDQSI_PENDING_INCOME_STATUS` | `ssdqsi_quota_detail_line` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSDQSI_PENDING_INCOME_STATUS.xml` |
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
| 1 | Cargar Lineas | `Load_Lines` | Botón (Java) | Java `LoadLines` | N | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` |
| 2 | Procesar | `Process_Lines` | Botón (Java) | Java `ProcessLines` | N | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` |
| 3 | Reactivar | `Reactive Process` | Botón (Java) | Java `Reactive` | N | Proceso Openbravo registro `Ssdqsi_Quota_Detail_ID` |

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

Módulo: `ec.com.sidesoft.discount.quota.salesinvoices`.

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

# Glosario — prefijo `SSDQSI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSDQSI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.discount.quota.salesinvoices` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Load_Lines` — Cargar Lineas
- `Process_Lines` — Procesar
- `Reactive Process` — Reactivar

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Back Office Discount
**Package:** `ec.com.sidesoft.backoffice.discount`

# Module overview — Sidesoft Back Office Discount

## Functional

El módulo Sidesoft Back Office Discount es una solución diseñada para gestionar descuentos en el área de finanzas, facilitando modificaciones en los precios de productos y servicios. Los actores principales incluyen usuarios de negocio que manejan el sistema ERP, analistas de soporte de nivel 2 que resuelven incidencias, y desarrolladores que pueden personalizar la funcionalidad. El alcance del módulo se centra en la gestión de descuentos a través de líneas de facturas y órdenes, permitiendo a los usuarios aplicar ajustes según las políticas internas. Existen dependencias con el framework Openbravo 3.0 y compatibilidad con la Skin de versiones del 2.50 al 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/backoffice/discount` |
| Web | `web/ec.com.sidesoft.backoffice.discount/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSBOD`

# Guía de chat — Sidesoft Back Office Discount

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.backoffice.discount`).

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
- «¿Qué es la tabla ssbod_gift_order?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo aplico un descuento a una línea de factura?
- ¿Qué debo hacer si el porcentaje de descuento no se refleja correctamente?
- ¿Cómo puedo revertir un descuento ya aplicado?
- ¿Qué validaciones se realizan al modificar un precio?
- ¿Dónde puedo ver el historial de cambios de precio?
- ¿Cómo se gestiona el límite de precios para los descuentos?
- ¿Qué debo hacer si necesito ayuda con un error en el módulo?
- ¿Hay algún informe que me muestre los descuentos aplicados?

# Domain — data model

## Functional

El módulo se basa en la tabla principal 'ssbod_gift_order', que actúa como entidad cabecera para gestionar las órdenes que incluyen descuentos. Las relaciones más relevantes son con las tablas 'C_INVOICELINE' y 'C_ORDERLINE', donde se aplican los descuentos a las líneas de facturación y de orden. Un trigger clave, 'SSBOD_INVOICE_OFFER', se encarga de obtener el porcentaje de descuento específico sobre la línea de un pedido, garantizando que los ajustes se efectúen de manera adecuada y automática en función de las reglas de negocio definidas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssbod_gc_prodcat` |
| `ssbod_gc_product` |
| `ssbod_gift_catogory` |
| `ssbod_gift_invoice` |
| `ssbod_gift_order` |
| `ssbod_gift_temp` |
| `ssbod_offer_ctg` |
| `ssbod_offer_doc` |
| `ssbod_offer_marketing` |
| `ssbod_offer_pterm` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssbod_gc_prodcat` | Ssbod_gc_prodcat | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ssbod_gift_catogory_id→ssbod_gift_catogory; m_product_category_id→m_product_category | Detalle enlazado a ad_client, ad_org, ssbod_gift_catogory. | PK `ssbod_gc_prct_key`; Cols: m_product_category_id, ssbod_gift_catogory_id, product_selector; `SSBOD_GC_PRCT_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssbod_gc_product` | Ssbod_gc_product | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ssbod_gc_prodcat_id→ssbod_gc_prodcat; m_product_id→m_product | Detalle enlazado a ad_client, ad_org, ssbod_gc_prodcat. | PK `ssbod_gc_prod_key`; Cols: m_product_id, ssbod_gc_prodcat_id; `SSBOD_GC_PROD_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssbod_gift_catogory` | Ssbod_gift_catogory | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssbod_gift_cat_key`; Cols: name, description; `SSBOD_GIFT_CAT_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssbod_gift_invoice` | ssbod_gift_invoice | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoiceline_id→c_invoiceline; m_product_id→m_product | Detalle enlazado a ad_client, ad_org, c_invoiceline. | PK `ssbod_gift_inv_key`; Cols: m_product_id, c_invoiceline_id; `SSBOD_GIFT_INV_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssbod_gift_order` | Ssbod_gift_order | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_orderline_id→c_orderline; m_product_id→m_product; m_attributesetinstance_id→m_attributesetinstance (+1) | Detalle enlazado a ad_client, ad_org, c_orderline. | PK `ssbod_gift_ord_key`; Cols: m_product_id, c_orderline_id, m_warehouse_id, m_attributesetinstance_id; `SSBOD_GIFT_ORD_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssbod_gift_temp` | Ssbod_gift_temp | — | — | ad_client_id→ad_client; ad_org_id→ad_org; m_product_id→m_product; m_attributesetinstance_id→m_attributesetinstance; m_warehouse_id→m_warehouse | Detalle enlazado a ad_client, ad_org, m_product. | PK `ssbod_gift_tmp_key`; Cols: record_id, ad_tab_id, m_product_id, checked, m_warehouse_id; `SSBOD_GIFT_TMP_CHECKED`: CHECKED IN ('Y', 'N'); `SSBOD_GIFT_TMP_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssbod_offer_ctg` | Ssbod_offer_ctg | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ssbod_gift_catogory_id→ssbod_gift_catogory; m_offer_id→m_offer | Detalle enlazado a ad_client, ad_org, ssbod_gift_catogory. | PK `ssbod_offer_ctg_key`; Cols: m_offer_id, ssbod_gift_catogory_id; `SSBOD_OFFER_CTG_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssbod_offer_doc` | Ssbod_offer_doc | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype; m_offer_id→m_offer | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `ssbod_offer_doc_key`; Cols: m_offer_id, c_doctype_id; `SSBOD_OFFER_DOC_ISACTIVE`: ISACTIVE IN ('Y', 'N'); idx `SSBOD_OFFER_DOC_INDEX` (c_doctype_id) |
| `ssbod_offer_marketing` | Ssbod_offer_marketing | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_campaign_id→c_campaign; m_offer_id→m_offer | Detalle enlazado a ad_client, ad_org, c_campaign. | PK `ssbod_offer_mkt_key`; Cols: m_offer_id, c_campaign_id; `SSBOD_OFFER_MKT_ISACTIVE`: ISACTIVE IN ('Y', 'N'); idx `SSBOD_OFFER_MKT_OFFER` (m_offer_id) |
| `ssbod_offer_pterm` | SSBOD_offer_pterm | — | — | ad_client_id→ad_client; ad_org_id→ad_org; m_offer_id→m_offer; c_paymentterm_id→c_paymentterm | Detalle enlazado a ad_client, ad_org, m_offer. | PK `ssbod_offer_ptrm_key`; Cols: m_offer_id, c_paymentterm_id; `SSBOD_OFFER_PTRM_ISACTIVE`: ISACTIVE IN ('Y', 'N'); idx `SSBOD_OFFER_PTRM_OFFER` (m_offer_id) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Ssbod_gc_prodcat` |
| `Ssbod_gc_product` |
| `Ssbod_gift_catogory` |
| `ssbod_gift_invoice` |
| `Ssbod_gift_order` |
| `Ssbod_gift_temp` |
| `Ssbod_offer_ctg` |
| `Ssbod_offer_doc` |
| `Ssbod_offer_marketing` |
| `SSBOD_offer_pterm` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_INVOICELINE`, `C_ORDERLINE`, `M_OFFER`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo cuenta con una única ventana llamada 'Categoria de Regalos', que permite a los usuarios navegar por las distintas funcionalidades relacionadas con los descuentos. Dentro de esta ventana, los usuarios pueden acceder a varias pestañas para realizar acciones específicas y visualizar información relevante sobre las ofertas y descuentos aplicados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.backoffice.discount.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Categoria de Regalos | Gift Category |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Categoria de Regalos | Gift Category | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.backoffice.discount.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Categoria de Regalos

- **AD_WINDOW_ID:** `D5564B6146F5483F93023F2213F936C5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `BB442A2F3B994AECB937FE8ED015E795` | 0 |
| 20 | Product Category | `E3F2E5BBF2614BD8B282F55D114CD69B` | 1 |
| 30 | Product | `48E3E666832742E39634A448D94D4AA8` | 2 |

## Campos añadidos por el módulo (AD_FIELD)

### Payment Term

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Payment Terms | `C_Paymentterm_ID` | No | No | — |

### Pestaña `187`

- **AD_TAB_ID:** `187` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 98 | EM_Ssbod_Discount_Rate | `EM_Ssbod_Discount_Rate` | No | Sí | — |
| 2190 | Add Gifts | `EM_Ssbod_Add_Gifts` | No | No | — |

### Pestaña `270`

- **AD_TAB_ID:** `270` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 66 | EM_Ssbod_Discount_Rate | `EM_Ssbod_Discount_Rate` | No | Sí | — |
| 2070 | Add Gifts | `EM_Ssbod_Add_Gifts` | No | No | — |

### Gifts

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Gift Category | `Ssbod_Gift_Catogory_ID` | No | No | — |

### Sales Offer

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Sales Campaign | `C_Campaign_ID` | No | No | — |

### Product (ventana: Categoria de Regalos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Product | `M_Product_ID` | No | No | — |

### Pestaña `800079`

- **AD_TAB_ID:** `800079` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 45 | Description | `EM_Ssbod_Description` | No | No | — |
| 153 | Marketing Campaign | `EM_Ssbod_Campaign_Selector` | No | No | — |
| 154 | Payment Term | `EM_Ssbod_Term_Selector` | No | No | — |
| 155 | Document Type | `EM_Ssbod_Doctype` | No | No | — |
| 340 | Number of gifts | `EM_Ssbod_Gift_Number` | No | No | — |
| 350 | Gift Per Unit | `EM_Ssbod_Perunit` | No | No | — |

### Gifts

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Product | `M_Product_ID` | No | No | — |

### Product Category (ventana: Categoria de Regalos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Product Category | `M_Product_Category_ID` | No | No | — |
| 40 | Gift Category | `Ssbod_Gift_Catogory_ID` | No | No | — |
| 50 | Product_Selector | `Product_Selector` | No | No | — |

### Header (ventana: Categoria de Regalos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |

### Gifts

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Product | `M_Product_ID` | No | No | — |
| 50 | Warehouse | `M_Warehouse_ID` | No | No | — |
| 60 | Attribute Set Value | `M_Attributesetinstance_ID` | No | No | — |

### Document Type

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Document Type | `C_Doctype_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

En términos de procesos, el módulo incluye un único proceso que permite a los usuarios aplicar precios ajustados en facturas y órdenes. Generalmente, los botones típicos incluyen opciones como 'Completar', que finaliza la operación de descuento, y 'Rechazar', que cancela cualquier ajuste realizado. Las validaciones frecuentes incluyen verificaciones de integración de precios y validación de límites de precios establecidos en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.backoffice.discount.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Añadir Regalos | Add Gifts | ssbod_addgifts | Java `Gift` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/backoffice/discount/ad_action/Gift.java` |
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
| Informe (servlet) | Añadir Regalos | `Gift` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/backoffice/discount/ad_action/Gift.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Añadir Regalos | Add Gifts | ssbod_addgifts | Java `Gift` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/backoffice/discount/ad_action/Gift.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Añadir Regalos | Add Gifts | Java `Gift` | Genera PDF desde JRXML `—`; contexto sesión `—`. | Genera PDF desde JRXML `—`; contexto sesión `—`. |
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
| `ssbod_not_equals_numbers` | You must select correct number of gift(s) | You must select correct number of gift(s) | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye varias clases Java que permiten extender la funcionalidad del sistema ERP, como 'ApplicationProvider' y 'Gift', las cuales se encargan de gestionar la lógica de negocio y los procesos relacionados con la aplicación de descuentos, asegurando que se carguen correctamente los recursos necesarios para su operación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.backoffice.discount`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ApplicationProvider` | root | BaseComponentProvider | ComponentProvider / UI | `src/ec/com/sidesoft/backoffice/discount/ApplicationProvider.java` |
| `Gift` | ad_action | HttpSecureAppServlet | — | `src/ec/com/sidesoft/backoffice/discount/ad_action/Gift.java` |
| `SL_Invoice_Amt` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/backoffice/discount/ad_callouts/SL_Invoice_Amt.java` |
| `SL_Invoice_Product` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/backoffice/discount/ad_callouts/SL_Invoice_Product.java` |
| `SL_Order_Amt` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/backoffice/discount/ad_callouts/SL_Order_Amt.java` |
| `SL_Order_Product` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/backoffice/discount/ad_callouts/SL_Order_Product.java` |
| `PriceAdjustment` | businessUtility | — | — | `src/ec/com/sidesoft/backoffice/discount/businessUtility/PriceAdjustment.java` |
| `MethodsDao` | dao | — | — | `src/ec/com/sidesoft/backoffice/discount/dao/MethodsDao.java` |
| `ProductComplete` | info | HttpSecureAppServlet | — | `src/ec/com/sidesoft/backoffice/discount/info/ProductComplete.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSBOD_INVOICE_OFFER` | `c_invoiceline` | before INSERT | OBTENGO EL PORCETAJE DE DESCUENTO DE LA LINEA DEL PEDIDO |
| AD_VAL_RULE | — | `Ssbod_doctype` | `c_doctype.DocBaseType = 'SOO' or c_doctype.DocBaseType = 'ARI'` |
| Función PL `ssbod_process_gifts` | — | invocación proceso | update ssbod_gift_order set c_order_id = v_order_id where c_orderline_id IN (select ); |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL tienen un papel esencial en el soporte del módulo, donde el trigger 'SSBOD_INVOICE_OFFER' proporciona una lógica automatizada para calcular los descuentos al momento de procesar las líneas de facturas. Además, existe una función PL que contribuye a la gestión eficiente de los datos, asegurando que las modificaciones en las órdenes y facturas tengan coherencia con las políticas de descuentos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSBOD_INVOICE_OFFER` | `c_invoiceline` | before | INSERT | OBTENGO EL PORCETAJE DE DESCUENTO DE LA LINEA DEL PEDIDO | `model/triggers/SSBOD_INVOICE_OFFER.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssbod_process_gifts` | — | update ssbod_gift_order set c_order_id = v_order_id where c_orderline_id IN (select ); | update ssbod_gift_order set c_order_id = v_order_id where c_orderline_id IN (select ); | `model/functions/SSBOD_PROCESS_GIFTS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Añadir Regalos | `ssbod_addgifts` | Informe (servlet) | Java `Gift` | N | Genera PDF desde JRXML `—`; contexto sesión `—`. |

**Total acciones documentadas (extract):** **1** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/ec.com.sidesoft.backoffice.discount/js/ecsap-authorization-process.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.backoffice.discount`.

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

# Glosario — prefijo `SSBOD`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSBOD` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.backoffice.discount` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `ssbod_addgifts` — Añadir Regalos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
