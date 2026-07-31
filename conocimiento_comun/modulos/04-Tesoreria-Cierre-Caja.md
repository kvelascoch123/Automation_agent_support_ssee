# Openbravo Sidesoft — Tesorería y Cierre de Caja

> Cuentas financieras, cierre de caja estándar y avanzado, conciliación bancaria, tarjetas de crédito, flujo de caja, cargo de cierre diario.

**Paquetes incluidos (17):**
- `com.sidesoft.localization.ecuador.finances` — Localization of Ecuador - Finances
- `ec.com.sidesoft.localization.ecuador.financial.account` — Sidesoft Complement Financial Account
- `ec.com.sidesoft.financialaccount.document.type` — Financial Account
- `ec.com.sidesoft.custom.closecash` — Sidesoft Custom Close Cash
- `ec.com.sidesoft.custom.closecash.advanced` — Sidesoft Custom Close Cash Advanced
- `ec.com.sidesoft.closecash.financial.account` — Closecash Financial Account
- `ec.com.sidesoft.closecash.sales.order` — Sidesoft Close Cash for Sales Order
- `ec.com.sidesoft.closecash.report.print` — Sidesoft Close Cash Report for Printing Process
- `ec.com.sidesoft.closecash.indumot` — Sidesoft Custom Close Cash for Indumot
- `ec.com.sidesoft.creditcard.closecash` — Sidesoft Credit Card Reconciliation Close Cash
- `ec.com.sidesoft.creditcard.reconciliation` — Sidesoft Credit Card Reconciliation
- `ec.com.sidesoft.creditcard.reconciliation.transaction` — Card Settlement Loading Transaction
- `ec.com.sidesoft.localization.checkbook` — Ecuador Checkbook Modules
- `ec.com.sidesoft.localization.custom.checkbook` — Ecuador Checkbook Custom Module
- `ec.com.sidesoft.cash.flow` — Sidesoft Cash Flow
- `ec.com.sidesoft.daily.closing.charge` — Daily Closing Charge
- `ec.com.sidesoft.reconcilation.reports` — Standard  - Automatic Reconcilation Report


---
## Localization of Ecuador - Finances
**Package:** `com.sidesoft.localization.ecuador.finances`

# Module overview — Localization of Ecuador - Finances

## Functional

El módulo 'Localization of Ecuador - Finances' está diseñado para gestionar las finanzas específicas del Ecuador, facilitando a las empresas el seguimiento y control de sus operaciones financieras. Los actores principales incluyen usuarios de negocio, personal de soporte técnico en nivel 2 y desarrolladores que realizan personalizaciones y mantenimientos. El alcance abarca funcionalidades como la gestión de cuentas bancarias y la realización de transferencias entre estas. Este módulo depende del 'Openbravo 3.0 Framework' y de la '2.50 to 3.00 Compatibility Skin' para su correcto funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/localization/ecuador/finances` |
| Web | `web/com.sidesoft.localization.ecuador.finances/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSFI`

# Guía de chat — Localization of Ecuador - Finances

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.localization.ecuador.finances`).

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
- «¿Qué es la tabla ssfi_financial_user?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo realizar una transferencia bancaria?
- ¿Dónde encuentro el resumen de mis cuentas?
- ¿Qué información necesito para registrar un nuevo pago?
- ¿Cómo puedo generar el Reporte Detallado de Ventas?
- ¿Existen validaciones especiales para los pagos?
- ¿Cómo se actualiza la información de las cuentas bancarias?
- ¿Qué debo hacer si mi transacción fue rechazada?
- ¿Dónde se almacenan los datos de los proveedores?

# Domain — data model

## Functional

El modelo de datos del módulo incluye entidades clave como 'C_BPARTNER' y 'FIN_FINANCIAL_ACCOUNT', que representan respectivamente a las contrapartes comerciales y las cuentas financieras. Las operaciones dentro del módulo pueden verse reflejadas en etapas como la creación y validación de pagos, utilizando la tabla 'ssfi_financial_user' como punto de anclaje. Entre los triggers que gestionan la integridad de los datos se encuentra 'SSFI_CURRENCY_TRG', que actúa sobre la tabla 'C_BPARTNER'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssfi_banktransfer` |
| `ssfi_fin_account` |
| `ssfi_financial_user` |
| `ssfi_model_prod` |
| `ssfi_setofaccounts` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssfi_banktransfer` | ssfi_banktransfer | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssfi_banktransfer_key`; Cols: name, code, value, savingcode_aux, paymentmethod; `SSFI_BANKTRANSFER_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssfi_fin_account` | ssfi_fin_account | — | — | ad_client_id→ad_client; ad_org_id→ad_org; fin_financial_account_id→fin_financial_account; ssfi_setofaccounts_id→ssfi_setofaccounts | Detalle enlazado a ad_client, ad_org, fin_financial_account. | PK `ssfi_fin_account_key`; Cols: ssfi_setofaccounts_id, fin_financial_account_id; `SSFI_SETACCOUNTS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssfi_financial_user` | ssfi_financial_user | — | — | fin_financial_account_id→fin_financial_account; ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org; ad_user_id→ad_user | Detalle enlazado a ad_client, c_doctype, fin_financial_account. | PK `ssfi_financial_user_key`; Cols: ad_user_id, fin_financial_account_id, c_doctype_id, isdefault; `SSFI_FINANCIAL_USER_ISCHK`: ISACTIVE IN ('Y', 'N') |
| `ssfi_model_prod` | ssfi_model_prod | — | — | ad_client_id→ad_client; ad_org_id→ad_org; m_brand_id→m_brand | Detalle enlazado a ad_client, ad_org, m_brand. | PK `ssfi_mod_prod_key`; Cols: m_brand_id, value, name, description; `SSFI_MOD_PROD_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssfi_setofaccounts` | ssfi_setofaccounts | — | `SSFI_SETOFACCOUNTS_CODE` (code); `SSFI_SETOFACCOUNTS_NAME` (name) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssfi_setofaccounts_key`; Cols: code, name, description; `SSFI_SETACCOUNTS2_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssfi_banktransfer` |
| `ssfi_fin_account` |
| `ssfi_fin_payment_detail_v` |
| `ssfi_financial_user` |
| `Ssfi_InvoiceSummaryV` |
| `ssfi_model_prod` |
| `ssfi_setofaccounts` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_BPARTNER`, `C_BP_BANKACCOUNT`, `C_DOCTYPE`, `C_ELEMENTVALUE`, `C_GLITEM`, `C_INVOICELINE`, `FIN_FINANCIAL_ACCOUNT`, `FIN_PAYMENT`, `FIN_PAYMENT_CREDIT`, `FIN_PAYMENT_DETAIL`, `FIN_PAYMENT_SCHEDULEDETAIL`, `FIN_RECONCILIATION`, `M_PRODUCT`

### Views

`SSFI_ACCT_RECEIVAB_PAYAB_V`, `SSFI_ADVANCEDPAYMENT_V`, `SSFI_BASES_V`, `SSFI_FIN_PAYMENT_DETAIL_V`, `SSFI_INVOICE_SUMMARY_V`, `SSFI_INVOICE_V`, `SSFI_INV_SUM_COSTC_V`, `SSFI_PAYMENT_CREDIT_V`, `SSFI_PAYMENT_V`, `SSFI_WITHHOLDINGSALES_V`

# Functional — windows and menus

## Functional

El módulo se navega a través de dos ventanas principales: 'Banco para Transferencia' y 'Conjunto de Cuentas'. Estas ventanas permiten a los usuarios gestionar transacciones bancarias y consolidar cuentas de manera intuitiva. Las funcionalidades están organizadas en pestañas que proporcionan acceso a diferentes aspectos de la gestión financiera.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.localization.ecuador.finances.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Banco para Transferencia | Bank Transfer |
| Conjunto de Cuentas | Set of Accounts |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Anticipos por cobrar detallado | Detail Account Receivable WAdjust | No |
| Anticipos por Liquidar - Clientes | Summary Account Receivable WAdjust | No |
| Anticipos por Liquidar Proveedores | Summary Account Payable WAdjust | No |
| Anticipos por pagar detallado | Detail Account Payable WAdjust | No |
| Análisis general de compras | General analysis of purchases | No |
| Banco para Transferencia | Bank Transfer | No |
| Cash Report | Cash Report | No |
| Conjunto de Cuentas | Set of Accounts | No |
| Consolidado de Guías de salida por periodo | Summary Deliveries by Period | No |
| Detalle contabilidad cliente | Customer Account Detail | No |
| Detalle contabilidad proveedor | Provider Accounting Detail | No |
| Detalle Crédito Clientes | Customer Credit Detail | No |
| Detalle Kardex sin Costos | Kardex Detail without Costs | No |
| Estado contabilidad cliente | Customer Account Status | No |
| Estado contabilidad proveedor | Provider Account Status | No |
| Estado CxC - Con Bonos | Account Statement Receivable | No |
| Estado CxC - Detallado(Sin Anticipos) | Summary Account Receivab UAdjust | No |
| Estado CxC - Resumido(Sin Anticipos) | Total Acount Receivable UAdjust | No |
| Estado de Anticipo Clientes | Customer Advance Status | No |
| Estado de Anticipo Proveedores | Provider Advance Status | No |
| Estado de CxP - Con Abonos | Account Statement Payable | No |
| Estado de CxP - Detallado(Sin Anticipos) | Summary Account Payable UAdjust | No |
| Estado de CxP - Resumido(Sin Anticipos) | Total Account Payable UAdjust | No |
| Evolución de precios de compra | Purchase Price Evolution | No |
| Kardex | Kardex | No |
| Kardex con costos | Kardex with costs | No |
| Kardex sin costos | Kardex without costs | No |
| Movimientos de la Cuenta Financiera | Financial account movements | No |
| Notas de Crédito por Vendedor | Credit Notes by Vendor | No |
| Proyección Recaudación | Collection Projection | No |
| Reporte asientos por fechas | Report Journal | No |
| Reporte de Cuentas Vencidas | Report of past due accounts | No |
| Reporte de pagos por proveedor y periodo | Detail expenses provider | No |
| Reporte Detallado de Ventas | Detailed Sales Summary Report | No |
| Reporte recaudación por vendedor | Colletion by seller | No |
| Resumen(Detalle de Ventas) | Summary(Detail Sales) | No |
| Tarifas con costo | Tarifas con costo | No |
| Transacciones Pendientes de Pago | Payments Report | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.localization.ecuador.finances.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Banco para Transferencia

- **AD_WINDOW_ID:** `6155A67D6D0449FBB21F51AC864513C0`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Bank Transfer | `C9ED871C09C846C198FE7FBA40704F19` | 0 |

### Ventana: Conjunto de Cuentas

- **AD_WINDOW_ID:** `0CCB03EACF6F4B0BA53D50C8A716812D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Set of Accounts | `8A5CFE6D2AEA4F209383659515B3EA25` | 0 |
| 20 | Financial Accounts | `46B6D5BAED5F44B9AF5289CE0F4AD79B` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Set of Accounts (ventana: Conjunto de Cuentas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Code | `Code` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Pestaña `132`

- **AD_TAB_ID:** `132` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 114 | Mandatory Cost Center | `EM_Ssfi_Iscostcenter` | No | No | — |
| 115 | Mandatory 1st Dimension | `EM_Ssfi_Isuser1` | No | No | — |
| 116 | Mandatory 2nd Dimension | `EM_Ssfi_Isuser2` | No | No | — |

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 340 | EM_Ssfi_Iscrossing | `EM_Ssfi_Iscrossing` | No | No | — |

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 217 | Model | `EM_Ssfi_Model_Prod_ID` | No | No | — |

### Pestaña `220`

- **AD_TAB_ID:** `220` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 370 | Foreign | `em_ssfi_foreign` | No | No | — |

### Pestaña `226`

- **AD_TAB_ID:** `226` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 15 | Bank Transfer | `em_ssfi_banktransfer_id` | No | No | — |
| 270 | Location / Address | `em_ssfi_c_location_id` | No | No | — |
| 280 | Exchange Bank | `em_ssfi_ex_bank` | No | No | — |
| 290 | ABA | `EM_Ssfi_Aba` | No | No | — |

### Pestaña `270`

- **AD_TAB_ID:** `270` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 66 | Initial subtotal | `EM_Ssfi_Initial_Subtotal` | No | Sí | — |

### Bank Transfer (ventana: Banco para Transferencia)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 25 | Search Key | `Value` | No | No | — |
| 30 | Commercial Name | `Name` | No | No | — |
| 40 | Codigo | `Code` | No | No | — |
| 50 | Saving code | `Savingcode` | No | No | — |
| 60 | Current code | `Currentcode` | No | No | — |
| 70 | Payment method | `Paymentmethod` | No | No | — |

### User

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 40 | User/Contact | `AD_User_ID` | No | No | — |
| 60 | Document Type | `C_Doctype_ID` | No | No | — |
| 70 | Default | `Isdefault` | No | No | — |

### Financial Accounts (ventana: Conjunto de Cuentas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 40 | Active | `Isactive` | No | No | — |

### Pestaña `C4B6506838E14A349D6717D6856F1B56`

- **AD_TAB_ID:** `C4B6506838E14A349D6717D6856F1B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 75 | Description 2 | `EM_Ssfi_Description` | No | No | — |

### Model

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |

### Pestaña `F7A52FDAAA0346EFA07D53C125B40404`

- **AD_TAB_ID:** `F7A52FDAAA0346EFA07D53C125B40404` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 75 | Description 2 | `EM_Ssfi_Description` | No | No | — |

### Pestaña `FF8080813320657F0133209DE21B0042`

- **AD_TAB_ID:** `FF8080813320657F0133209DE21B0042` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 280 | Conciliation Banks | `EM_Ssfi_Conciliationbank` | No | No | — |
| 290 | Reverse conciliation | `EM_Ssfi_Reverse` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los botones típicos en el módulo incluyen opciones como 'completar', 'retornar' y 'rechazar' dentro de los procesos de pago. Se generan informes como el 'Reporte Detallado de Ventas' y el 'Resumen(Detalle de Ventas)', que ofrecen una visión clara del desempeño financiero. Las validaciones frecuentes están relacionadas con la correcta asignación de cuentas bancarias y la verificación de datos del usuario antes de procesar transacciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.localization.ecuador.finances.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Proceso de conteo de inventario | Process Inventory Count | SSFI M_Inventory Post | Java `Ssfi_InventoryCountProcess` (AD_MODEL_OBJECT `P`) | Clase `Ssfi_InventoryCountProcess` extiende `Object`. | `src/com/sidesoft/localization/ecuador/finances/ad_process/Ssfi_InventoryCountProcess.java` |
| Botón (PL/pgSQL) | Reversar conciliación | ssfi_reverse_reconcile | ssfi_reverse_reconcile | `ssfi_reverse_reconcile` | ERROR=Existen reconciliaciones posteriores en estado completado, se requiere su reversión.; ERROR=Requiere descontabilizar la reconciliación antes de aplicar la reversión; Validar si se permite reversar la conciliación;… | — |
| Informe (servlet) | Conciliación Bancos | Conciliation Banks | SSFI_ConciliationBankReport | Java `SSFI_ReportConciliationBank` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/localization/ecuador/finances/reports/SSFI_ReportConciliationBank.java` |
| Informe (servlet) | Detalle de Reconciliación | Reconciliation Details | SSFI_ReconciliationDetailReport | Java `ReportReconciliationDetailFlopec` (AD_MODEL_OBJECT `S`) | Clase `ReportReconciliationDetailFlopec` extiende `ReportReconciliationFlopec`. | `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliationDetailFlopec.java` |
| Informe (servlet) | Resumen de Reconciliación | Reconciliation Summary | SSFI_ReconciliationSummaryReport | Java `ReportReconciliationSummaryFlopec` (AD_MODEL_OBJECT `S`) | Clase `ReportReconciliationSummaryFlopec` extiende `ReportReconciliationFlopec`. | `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliationSummaryFlopec.java` |
| Proceso / otro | Anticipos por cobrar detallado | Detail Account Receivable WAdjust | Detail Account Receivable WAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Anticipos por Liquidar - Clientes | Summary Account Receivable WAdjust | Summary Account Receivable WAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Anticipos por Liquidar Proveedores | Summary Account Payable WAdjust | Summary Account Payable WAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Anticipos por pagar detallado | Detail Account Payable WAdjust | Detail Account Payable WAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Análisis general de compras | General analysis of purchases | Ssfi_Analysis_Purchases | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Cash Report | Cash Report | Cash_Report | *(OBUIAPP / manual)* | Cash Report | — |
| Proceso / otro | Consolidado de Guías de salida por periodo | Summary Deliveries by Period | Ssfi_SummaryDeliveriesByPeriod | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Cuenta total por pagar sin anticipo | Total Account Payable UAdjust | Total Account Payable UAdjust | *(OBUIAPP / manual)* | Total Acount Payable UAdjust | — |
| Proceso / otro | Detalle contabilidad cliente | Customer Account Detail | C_Customer_Accounting_Detail | *(OBUIAPP / manual)* | Customer Accounting Detail | — |
| Proceso / otro | Detalle contabilidad proveedor | Provider Accounting Detail | C_Provider_Accounting_Detail | *(OBUIAPP / manual)* | Provider Accounting Detail | — |
| Proceso / otro | Detalle Crédito Clientes | Customer Credit Detail | Customer Credit Detail | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle Kardex sin Costos | Kardex Detail without Costs | Kardex Detail without Costs | *(OBUIAPP / manual)* | Kardex Detail without Costs | — |
| Proceso / otro | Estado contabilidad cliente | Customer Account Status | C_Customer_Accounting_Status | *(OBUIAPP / manual)* | Customer Accounting Status | — |
| Proceso / otro | Estado contabilidad proveedor | Provider Account Status | C_Provider_Accounting_Status | *(OBUIAPP / manual)* | Provider Accounting Status | — |
| Proceso / otro | Estado CxC - Con Bonos | Account Statement Receivable | Account Statement Receivable | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Detallado(Sin Anticipos) | Summary Account Receivab UAdjust | Summary Account Receivab UAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Resumido(Sin Anticipos) | Total Acount Receivable UAdjust | Total Account Receivable UAdjust | *(OBUIAPP / manual)* | Total Acount Receivable UAdjust | — |
| Proceso / otro | Estado de Anticipo Clientes | Customer Advance Status | Customer Advance Status | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado de Anticipo Proveedores | Provider Advance Status | Provider Advance Status | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado de CxP - Con Abonos | Account Statement Payable | Account Statement Payable | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Evolución de precios de compra | Purchase Price Evolution | Ssfi_PurchasePriceEvoltion | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Kardex | Kardex | Report_Kardex | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Kardex con Costos Consolidado | Kardex Consolidate | Report_Kardex_Consolidate | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Kardex sin costos | Kardex without costs | Report_Kardex_Without_Costed | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Kardex with costs | Kardex with costs | Report_Kardex_Costed | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Listado de Pagos | Payments Report | Payments Report | *(OBUIAPP / manual)* | Payments Report | — |
| Proceso / otro | Movimientos de la Cuenta Financiera | Financial account movements | Financial account movements | *(OBUIAPP / manual)* | Financial account movements | — |
| Proceso / otro | Notas de Crédito por Vendedor | Credit Notes by Vendor | Credit Notes by Vendor | *(OBUIAPP / manual)* | Credit Notes by Seller | — |
| Proceso / otro | Proyección Recaudación | Collection Projection | Collection Projection | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Journal | Report Journal | Report Journal | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de pagos por proveedor y periodo | Detail expenses provider | Detail expenses provider | *(OBUIAPP / manual)* | Detail expenses provider | — |
| Proceso / otro | Reporte recaudación por vendedor | Colletion by seller | Colletion by seller | *(OBUIAPP / manual)* | Colletion by seller | — |
| Proceso / otro | Resumen Cuenta por pagar sin anticipo | Summary Account Payable UAdjust | Summary Account Payable UAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Tarifas con costo | Tarifas con costo | ReportPriceWithCostlist | *(OBUIAPP / manual)* | Tarifas con costo | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Reporte Detallado de Ventas | Detailed Sales Summary Report | Detailed Sales Summary Report | `RptF_SalesDetail` | Sales Detail | — |
| Reporte | Resumen(Detalle de Ventas) | Summary(Detail Sales) | Summary(Detail Sales) | `RptF_SalesDetailSub.jrxml` | Summary(Detail Sales) | — |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Background | Consumo de anticipos generados | Consumption imprest accounts generated | Ssfi_ConsumptionImprestAccountsGenerated | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Proceso de conteo de inventario | `Ssfi_InventoryCountProcess` | Java (otro) | `—` | — | `src/com/sidesoft/localization/ecuador/finances/ad_process/Ssfi_InventoryCountProcess.java` |
| Informe (servlet) | Conciliación Bancos | `SSFI_ReportConciliationBank` | Informe (servlet PDF) | `—` | — | `src/com/sidesoft/localization/ecuador/finances/reports/SSFI_ReportConciliationBank.java` |
| Informe (servlet) | Detalle de Reconciliación | `ReportReconciliationDetailFlopec` | Java (otro) | `—` | — | `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliationDetailFlopec.java` |
| Informe (servlet) | Resumen de Reconciliación | `ReportReconciliationSummaryFlopec` | Java (otro) | `—` | — | `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliationSummaryFlopec.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Proceso de conteo de inventario | Process Inventory Count | SSFI M_Inventory Post | Java `Ssfi_InventoryCountProcess` (AD_MODEL_OBJECT `P`) | Clase `Ssfi_InventoryCountProcess` extiende `Object`. | `src/com/sidesoft/localization/ecuador/finances/ad_process/Ssfi_InventoryCountProcess.java` |
| Botón (PL/pgSQL) | Reversar conciliación | ssfi_reverse_reconcile | ssfi_reverse_reconcile | `ssfi_reverse_reconcile` | ERROR=Existen reconciliaciones posteriores en estado completado, se requiere su reversión.; ERROR=Requiere descontabilizar la reconciliación antes de aplicar la reversión; Validar si se permite reversar la conciliación;… | — |
| Informe (servlet) | Conciliación Bancos | Conciliation Banks | SSFI_ConciliationBankReport | Java `SSFI_ReportConciliationBank` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/localization/ecuador/finances/reports/SSFI_ReportConciliationBank.java` |
| Informe (servlet) | Detalle de Reconciliación | Reconciliation Details | SSFI_ReconciliationDetailReport | Java `ReportReconciliationDetailFlopec` (AD_MODEL_OBJECT `S`) | Clase `ReportReconciliationDetailFlopec` extiende `ReportReconciliationFlopec`. | `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliationDetailFlopec.java` |
| Informe (servlet) | Resumen de Reconciliación | Reconciliation Summary | SSFI_ReconciliationSummaryReport | Java `ReportReconciliationSummaryFlopec` (AD_MODEL_OBJECT `S`) | Clase `ReportReconciliationSummaryFlopec` extiende `ReportReconciliationFlopec`. | `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliationSummaryFlopec.java` |
| Proceso / otro | Anticipos por cobrar detallado | Detail Account Receivable WAdjust | Detail Account Receivable WAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Anticipos por Liquidar - Clientes | Summary Account Receivable WAdjust | Summary Account Receivable WAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Anticipos por Liquidar Proveedores | Summary Account Payable WAdjust | Summary Account Payable WAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Anticipos por pagar detallado | Detail Account Payable WAdjust | Detail Account Payable WAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Análisis general de compras | General analysis of purchases | Ssfi_Analysis_Purchases | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Cash Report | Cash Report | Cash_Report | *(OBUIAPP / manual)* | Cash Report | — |
| Proceso / otro | Consolidado de Guías de salida por periodo | Summary Deliveries by Period | Ssfi_SummaryDeliveriesByPeriod | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Cuenta total por pagar sin anticipo | Total Account Payable UAdjust | Total Account Payable UAdjust | *(OBUIAPP / manual)* | Total Acount Payable UAdjust | — |
| Proceso / otro | Detalle contabilidad cliente | Customer Account Detail | C_Customer_Accounting_Detail | *(OBUIAPP / manual)* | Customer Accounting Detail | — |
| Proceso / otro | Detalle contabilidad proveedor | Provider Accounting Detail | C_Provider_Accounting_Detail | *(OBUIAPP / manual)* | Provider Accounting Detail | — |
| Proceso / otro | Detalle Crédito Clientes | Customer Credit Detail | Customer Credit Detail | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle Kardex sin Costos | Kardex Detail without Costs | Kardex Detail without Costs | *(OBUIAPP / manual)* | Kardex Detail without Costs | — |
| Proceso / otro | Estado contabilidad cliente | Customer Account Status | C_Customer_Accounting_Status | *(OBUIAPP / manual)* | Customer Accounting Status | — |
| Proceso / otro | Estado contabilidad proveedor | Provider Account Status | C_Provider_Accounting_Status | *(OBUIAPP / manual)* | Provider Accounting Status | — |
| Proceso / otro | Estado CxC - Con Bonos | Account Statement Receivable | Account Statement Receivable | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Detallado(Sin Anticipos) | Summary Account Receivab UAdjust | Summary Account Receivab UAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Resumido(Sin Anticipos) | Total Acount Receivable UAdjust | Total Account Receivable UAdjust | *(OBUIAPP / manual)* | Total Acount Receivable UAdjust | — |
| Proceso / otro | Estado de Anticipo Clientes | Customer Advance Status | Customer Advance Status | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado de Anticipo Proveedores | Provider Advance Status | Provider Advance Status | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado de CxP - Con Abonos | Account Statement Payable | Account Statement Payable | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Evolución de precios de compra | Purchase Price Evolution | Ssfi_PurchasePriceEvoltion | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Kardex | Kardex | Report_Kardex | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Kardex con Costos Consolidado | Kardex Consolidate | Report_Kardex_Consolidate | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Kardex sin costos | Kardex without costs | Report_Kardex_Without_Costed | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Kardex with costs | Kardex with costs | Report_Kardex_Costed | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Listado de Pagos | Payments Report | Payments Report | *(OBUIAPP / manual)* | Payments Report | — |
| Proceso / otro | Movimientos de la Cuenta Financiera | Financial account movements | Financial account movements | *(OBUIAPP / manual)* | Financial account movements | — |
| Proceso / otro | Notas de Crédito por Vendedor | Credit Notes by Vendor | Credit Notes by Vendor | *(OBUIAPP / manual)* | Credit Notes by Seller | — |
| Proceso / otro | Proyección Recaudación | Collection Projection | Collection Projection | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Report Journal | Report Journal | Report Journal | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de pagos por proveedor y periodo | Detail expenses provider | Detail expenses provider | *(OBUIAPP / manual)* | Detail expenses provider | — |
| Proceso / otro | Reporte recaudación por vendedor | Colletion by seller | Colletion by seller | *(OBUIAPP / manual)* | Colletion by seller | — |
| Proceso / otro | Resumen Cuenta por pagar sin anticipo | Summary Account Payable UAdjust | Summary Account Payable UAdjust | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Tarifas con costo | Tarifas con costo | ReportPriceWithCostlist | *(OBUIAPP / manual)* | Tarifas con costo | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Proceso de conteo de inventario | Process Inventory Count | Java `Ssfi_InventoryCountProcess` | Clase `Ssfi_InventoryCountProcess` extiende `Object`. | Clase `Ssfi_InventoryCountProcess` extiende `Object`. |
| Botón (PL/pgSQL) | Reversar conciliación | ssfi_reverse_reconcile | PL `ssfi_reverse_reconcile` | ERROR=Existen reconciliaciones posteriores en estado completado, se requiere su reversión.; ERROR=Requiere descontabilizar la reconciliación antes de aplicar la reversión; Validar si se permite reversar la conciliación;… | ERROR=Existen reconciliaciones posteriores en estado completado, se requiere su reversión.; ERROR=Requiere descontabilizar la reconciliación antes de aplicar la reversión; Validar si se permite reversar la conciliación; 1) Descontabilizar manualmente la transaccion de Reconciliacion; 2) La reconciliacion a estado Borrador - requiere bajar trigger; 3) Cambiar el esatdo de las Lineas de la Reconciliacion satdo  => 'PWNC' (Concilaido a Pago reintegrado ) para q permita la reactivacion de la linea |
| Informe (servlet) | Conciliación Bancos | Conciliation Banks | Java `SSFI_ReportConciliationBank` | Genera PDF desde JRXML `—`; contexto sesión `—`. | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| Informe (servlet) | Detalle de Reconciliación | Reconciliation Details | Java `ReportReconciliationDetailFlopec` | Clase `ReportReconciliationDetailFlopec` extiende `ReportReconciliationFlopec`. | Clase `ReportReconciliationDetailFlopec` extiende `ReportReconciliationFlopec`. |
| Informe (servlet) | Resumen de Reconciliación | Reconciliation Summary | Java `ReportReconciliationSummaryFlopec` | Clase `ReportReconciliationSummaryFlopec` extiende `ReportReconciliationFlopec`. | Clase `ReportReconciliationSummaryFlopec` extiende `ReportReconciliationFlopec`. |
| Proceso / otro | Anticipos por cobrar detallado | Detail Account Receivable WAdjust | — | — | — |
| Proceso / otro | Anticipos por Liquidar - Clientes | Summary Account Receivable WAdjust | — | — | — |
| Proceso / otro | Anticipos por Liquidar Proveedores | Summary Account Payable WAdjust | — | — | — |
| Proceso / otro | Anticipos por pagar detallado | Detail Account Payable WAdjust | — | — | — |
| Proceso / otro | Análisis general de compras | General analysis of purchases | — | — | — |
| Proceso / otro | Cash Report | Cash Report | — | Cash Report | — |
| Proceso / otro | Consolidado de Guías de salida por periodo | Summary Deliveries by Period | — | — | — |
| Proceso / otro | Cuenta total por pagar sin anticipo | Total Account Payable UAdjust | — | Total Acount Payable UAdjust | — |
| Proceso / otro | Detalle contabilidad cliente | Customer Account Detail | — | Customer Accounting Detail | — |
| Proceso / otro | Detalle contabilidad proveedor | Provider Accounting Detail | — | Provider Accounting Detail | — |
| Proceso / otro | Detalle Crédito Clientes | Customer Credit Detail | — | — | — |
| Proceso / otro | Detalle Kardex sin Costos | Kardex Detail without Costs | — | Kardex Detail without Costs | — |
| Proceso / otro | Estado contabilidad cliente | Customer Account Status | — | Customer Accounting Status | — |
| Proceso / otro | Estado contabilidad proveedor | Provider Account Status | — | Provider Accounting Status | — |
| Proceso / otro | Estado CxC - Con Bonos | Account Statement Receivable | — | — | — |
| Proceso / otro | Estado CxC - Detallado(Sin Anticipos) | Summary Account Receivab UAdjust | — | — | — |
| Proceso / otro | Estado CxC - Resumido(Sin Anticipos) | Total Acount Receivable UAdjust | — | Total Acount Receivable UAdjust | — |
| Proceso / otro | Estado de Anticipo Clientes | Customer Advance Status | — | — | — |
| Proceso / otro | Estado de Anticipo Proveedores | Provider Advance Status | — | — | — |
| Proceso / otro | Estado de CxP - Con Abonos | Account Statement Payable | — | — | — |
| Proceso / otro | Evolución de precios de compra | Purchase Price Evolution | — | — | — |
| Proceso / otro | Kardex | Kardex | — | — | — |
| Proceso / otro | Kardex con Costos Consolidado | Kardex Consolidate | — | — | — |
| Proceso / otro | Kardex sin costos | Kardex without costs | — | — | — |
| Proceso / otro | Kardex with costs | Kardex with costs | — | — | — |
| Proceso / otro | Listado de Pagos | Payments Report | — | Payments Report | — |
| Proceso / otro | Movimientos de la Cuenta Financiera | Financial account movements | — | Financial account movements | — |
| Proceso / otro | Notas de Crédito por Vendedor | Credit Notes by Vendor | — | Credit Notes by Seller | — |
| Proceso / otro | Proyección Recaudación | Collection Projection | — | — | — |
| Proceso / otro | Report Journal | Report Journal | — | — | — |
| Proceso / otro | Reporte de pagos por proveedor y periodo | Detail expenses provider | — | Detail expenses provider | — |
| Proceso / otro | Reporte recaudación por vendedor | Colletion by seller | — | Colletion by seller | — |
| Proceso / otro | Resumen Cuenta por pagar sin anticipo | Summary Account Payable UAdjust | — | — | — |
| Proceso / otro | Tarifas con costo | Tarifas con costo | — | Tarifas con costo | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Reporte Detallado de Ventas | Detailed Sales Summary Report | Detailed Sales Summary Report | `RptF_SalesDetail` | Sales Detail | — |
| Reporte | Resumen(Detalle de Ventas) | Summary(Detail Sales) | Summary(Detail Sales) | `RptF_SalesDetailSub.jrxml` | Summary(Detail Sales) | — |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 50**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **2**; archivos `*.jrxml` en el repo = **50**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Reporte Detallado de Ventas | `Detailed Sales Summary Report` | — | *(ver AD_PROCESS_PARA / servlet)* | Sales Detail |
| 2 | Resumen(Detalle de Ventas) | `Summary(Detail Sales)` | — | *(ver AD_PROCESS_PARA / servlet)* | Summary(Detail Sales) |

### Plantillas sin proceso en diccionario

- `src/com/sidesoft/localization/ecuador/finances/reports/Journal_by_Dates.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/OutstandingDeposit.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/OutstandingPayment.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliation.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Report_CloseBoxByFinancialAccounts.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Report_Colletion_by_seller.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Report_Kardex.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Report_KardexWithoutCost.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Report_Kardex_Consolidate.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Report_Kardex_Costed.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Report_Kardex_Without_Costed.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Report_financial_accounts.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/RptF_SalesDetail.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/RptF_SalesDetailSub.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/RptSsfi_SubRepSetOfAccounts.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_Account_Statement_Payable.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_Account_Statement_Receivable.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_BusinessCredit.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_Collection_Projection.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_Customer_Advance_Status.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_DetailAcountPayable_WAdjust.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_DetailAcountReceivab_WAdjust.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_DocumentBySeller.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_Egre_Prov.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_Interbank_Transfer.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_Payments_Report.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_Provider_Advance_Status.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_Quotation.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_ReconciliationDetaill.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_SumaryAcountReceivab_UAdjust.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_SumaryAcountReceivab_WAdjust.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_ssfi_PurchasePriceEvoltion.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rpt_ssfi_SummaryDeliveriesByPeriod.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rptc_SumaryAcountPayable_UAdjust.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rptc_SumaryAcountPayable_WAdjust.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rptc_TotalAcountPayable_UAdjust.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rptc_TotalAcountReceivable_UAdjust.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Rrp_Cash_Report.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/SSFI_CxcStatusReport.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/SSFI_ReportConciliationBank.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Ssfi_ReportPriceListWithCost.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Ssfi_Rpt_General_Analysis_Purchases.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/Ssfi_SubRepConciliationBank.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/UnreconciledBankStatement.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/c_customer_accounting_status.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/c_customer_accounting_status_detail.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/c_provider_accounting_status.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/c_provider_accounting_status_detail.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/subReportSaldosIniciales.jrxml`
- `src/com/sidesoft/localization/ecuador/finances/reports/subReportSaldosIniciales2.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Ssfi_NoCostProductInLines` | There are no cost products in the lines | There are no cost products in the lines | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_Label_Rpt_Egre_Prov_order` | Order | Order | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_AutoCrossing3` | There is no financial account marked as default value. | There is no financial account marked as default value. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_AutoCrossing7` | The value of the credit note is greater than the value of the referenced invoice. | The value of the credit note is greater than the value of the referenced invoice. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_Label_Rpt_DetailAcountReceivab_WAdjust_title` | Detailed advances receivable report | Detailed advances receivable report | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_AutoCrossing4` | There is more than one financial account marked as the default value. | There is more than one financial account marked as the default value. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_Label_Rpt_DetailAcountPayable_WAdjust_title` | Detailed advance payment report | Detailed advance payment report | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_AutoCrossing1` | There is no type of document corresponding to the payment in window marked as crossing. | There is no type of document corresponding to the payment in window marked as crossing. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_AutoCrossing2` | There is more than one type of document corresponding to the Payment In window marked as crossing. | There is more than one type of document corresponding to the Payment In window marked as crossing. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_ValidateRequisitionTrans` | The transaction has no lines. | The transaction has no lines. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_AutoCrossingMethodPayment` | The payment method of this credit note is not configured in the financial account. | The payment method of this credit note is not configured in the financial account. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_ErrorVoidInvoice` | You can not cancel an invoice that has a related payment / charge. | You can not cancel an invoice that has a related payment / charge. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_ErrorWhithSalesInvoice` | The invoice can not be canceled, it has related retention. | The invoice can not be canceled, it has related retention. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_AutoCrossing6` | The selected credit note does not have the invoice reference configured. | The selected credit note does not have the invoice reference configured. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssfi_ErrorStatusInvoiceReference` | The referenced invoice is in draft status. | The referenced invoice is in draft status. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo también incorpora clases Java, como 'SSFIApplicationProvider', que proporcionan componentes y recursos para la interfaz de usuario, facilitando la integración con la estructura del sistema Openbravo y mejorando la operativa del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.localization.ecuador.finances`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SSFIApplicationProvider` | root | BaseComponentProvider | ComponentProvider / UI | `src/com/sidesoft/localization/ecuador/finances/SSFIApplicationProvider.java` |
| `AddPaymentDocumentNoActionHandler` | actionHandler | BaseActionHandler | — | `src/com/sidesoft/localization/ecuador/finances/actionHandler/AddPaymentDocumentNoActionHandler.java` |
| `SLInOutLineProductData` | ad_callouts | FieldProvider | — | `src/com/sidesoft/localization/ecuador/finances/ad_callouts/SLInOutLineProductData.java` |
| `SLOrderProductData` | ad_callouts | FieldProvider | — | `src/com/sidesoft/localization/ecuador/finances/ad_callouts/SLOrderProductData.java` |
| `Ssfi_InventoryProduct` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/finances/ad_callouts/Ssfi_InventoryProduct.java` |
| `ImportConciliationPos` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/ad_process/ImportConciliationPos.java` |
| `ProcessInvoices` | ad_process | — | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/ad_process/ProcessInvoices.java` |
| `ReconciliationDetailReport` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/ad_process/ReconciliationDetailReport.java` |
| `SsfiConsumptionImprestAccountsGeneratedBackground` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/ad_process/SsfiConsumptionImprestAccountsGeneratedBackground.java` |
| `Ssfi_InventoryCountProcess` | ad_process | Process | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/ad_process/Ssfi_InventoryCountProcess.java` |
| `ssfiImportExcelMaterialNeed` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/ad_process/ssfiImportExcelMaterialNeed.java` |
| `ReportReconciliationDetailFlopec` | reports | ReportReconciliationFlopec | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliationDetailFlopec.java` |
| `ReportReconciliationFlopec` | reports | HttpSecureAppServlet | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliationFlopec.java` |
| `ReportReconciliationSummaryFlopec` | reports | ReportReconciliationFlopec | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/reports/ReportReconciliationSummaryFlopec.java` |
| `SSFI_ReportConciliationBank` | reports | HttpSecureAppServlet | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/finances/reports/SSFI_ReportConciliationBank.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSFI_CURRENCY_TRG` | `c_bpartner` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `C_DocType - Receive/Make Payment 2 - Users` | `C_DocType.DocBaseType IN ('APP', 'ARR') AND C_DocType.IsSOTrx='@Isreceipt@' AND AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.A` |
| AD_VAL_RULE | — | `Ssfi_ValidateModel` | `ssfi_model_prod.m_brand_id = @M_BRAND_ID@` |
| AD_VAL_RULE | — | `Ssfi_Payment` | `FIN_PAYMENT.FIN_PAYMENT_ID  IN (select DISTINCT
pdv.fin_payment_id
FROM c_invoice i
LEFT JOIN c_bpartner bp ON i.c_bpart` |
| AD_VAL_RULE | — | `Ssfi_ValidateBaseDocType` | `C_DOCTYPE.ad_table_id = '318' AND C_DOCTYPE.issotrx='Y' AND C_DOCTYPE.ISACTIVE='Y'` |
| AD_VAL_RULE | — | `Validate - Provider` | `c_bpartner.isvendor='Y'` |
| AD_VAL_RULE | — | `ORG VALIDATION IS SUMMARY - FINANCES` | `AD_ORG.ISSUMMARY ='N' AND AD_ORG.VALUE <> '0'` |
| AD_VAL_RULE | — | `C_Doctype Purchase Order` | `C_DocType.DocBaseType IN ('POO') AND AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.AD_Org_ID, @#AD_Client_ID@) <> '-1'` |
| AD_VAL_RULE | — | `Vendors Validate` | `C_BPARTNER.IsSalesRep='Y'` |
| AD_VAL_RULE | — | `Ssfi_ValidateDocType` | `C_DOCTYPE.docbasetype = 'MMS' AND C_DOCTYPE.issotrx='Y' AND C_DOCTYPE.ISACTIVE='Y'` |
| AD_VAL_RULE | — | `C_DocType - Receive Payment` | `C_DocType.DocBaseType IN ('APP', 'ARR')  AND AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.AD_Org_ID, @#AD_Client_ID@) <> '-1'` |
| AD_VAL_RULE | — | `ssfi_financial_user` | `Fin_Financial_Account_ID IN (SELECT Fin_Financial_Account_ID FROM Fin_Finacc_Paymentmethod WHERE Fin_Paymentmethod_ID=@F` |
| AD_VAL_RULE | — | `ssfi_PartnerCustomer` | `c_bpartner.isactive = 'Y'
AND c_bpartner.iscustomer = 'Y'
AND EXISTS (
  SELECT 1
  FROM fin_payment p
  WHERE p.isrecei` |
| AD_VAL_RULE | — | `Validate User` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `ssfi_PartnerVendor` | `c_bpartner.isvendor='Y'` |
| AD_VAL_RULE | — | `Ssfi_AD_Window` | `AD_Window_Trl.AD_Window_ID in (select aw.ad_window_id from fact_acct a
left join ad_table at on at.ad_table_id = a.ad_ta` |
| AD_VAL_RULE | — | `Validate Document Type Finances` | `C_DOCTYPE.AD_TABLE_ID = '318' AND C_DOCTYPE.ISSOTRX='Y'` |
| AD_VAL_RULE | — | `Financial Accounts` | `fin_financial_account.type = 'C'` |
| AD_VAL_RULE | — | `Ssfi_ValidUser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Validation Account` | `fin_financial_account.type = 'C'` |
| AD_VAL_RULE | — | `Validate Seller` | `C_BPARTNER.IsSalesRep='Y'` |
| AD_VAL_RULE | — | `sswh_PartnerCustomer` | `c_bpartner.iscustomer='Y'` |
| Función PL `ssfi_reverse_reconcile` | — | invocación proceso | ERROR=Existen reconciliaciones posteriores en estado completado, se requiere su reversión.; ERROR=Requiere descontabilizar la reconciliación antes de aplicar la reversión; Validar si se permite reversar la conciliación |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers en este módulo, como 'SSFI_CURRENCY_TRG', juegan un papel crucial en la automatización de ciertas acciones y en la validación de cambios en los datos. Además, las funciones PL/pgSQL desarrolladas (15 en total) son esenciales para el soporte del módulo, ya que permiten ejecutar procesos complejos y mantener la lógica de negocio necesaria para la gestión financiera.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSFI_CURRENCY_TRG` | `c_bpartner` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSFI_CURRENCY_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssfi_general_ledger_journal` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_GENERAL_LEDGER_JOURNAL.xml` |
| `ssfi_get_createdby` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_GET_CREATEDBY.xml` |
| `ssfi_get_datetransaccion` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_GET_DATETRANSACCION.xml` |
| `ssfi_get_desctrans` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_GET_DESCTRANS.xml` |
| `ssfi_get_documentno` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_GET_DOCUMENTNO.xml` |
| `ssfi_getall_costcenter` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_GETALL_COSTCENTER.xml` |
| `ssfi_getconceptname` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_GETCONCEPTNAME.xml` |
| `ssfi_getoutstandingamt` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_GETOUTSTANDINGAMT.xml` |
| `ssfi_previous_costing_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_PREVIOUS_COSTING_GET.xml` |
| `ssfi_pymntscheduledetail_sum` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_PYMNTSCHEDULEDETAIL_SUM.xml` |
| `ssfi_pymntscheduledetail_sum2` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_PYMNTSCHEDULEDETAIL_SUM2.xml` |
| `ssfi_returnpaymentcount` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_RETURNPAYMENTCOUNT.xml` |
| `ssfi_returnwithsalescount` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_RETURNWITHSALESCOUNT.xml` |
| `ssfi_reverse_reconcile` | Reversar conciliación | ERROR=Existen reconciliaciones posteriores en estado completado, se requiere su reversión.; ERROR=Requiere descontabilizar la reconciliación antes de aplicar la reversión; Validar si se permite reversar la conciliación;… | ERROR=Existen reconciliaciones posteriores en estado completado, se requiere su reversión.; ERROR=Requiere descontabilizar la reconciliación antes de aplicar la reversión; Validar si se permite reversar la conciliación; 1) Descontabilizar manualmente la transaccion de Reconciliacion; 2) La reconciliacion a estado Borrador - requiere bajar trigger; 3) Cambiar el esatdo de las Lineas de la Reconciliacion satdo  => 'PWNC' (Concilaido a Pago reintegrado ) para q permita la reactivacion de la linea | `model/functions/SSFI_REVERSE_RECONCILE.xml` |
| `ssfi_revertinvoice` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSFI_REVERTINVOICE.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Proceso de conteo de inventario | `SSFI M_Inventory Post` | Botón (Java) | Java `Ssfi_InventoryCountProcess` | N | Clase `Ssfi_InventoryCountProcess` extiende `Object`. |
| 2 | Reversar conciliación | `ssfi_reverse_reconcile` | Botón (PL/pgSQL) | PL `ssfi_reverse_reconcile` | N | ERROR=Existen reconciliaciones posteriores en estado completado, se requiere su reversión.; ERROR=Requiere descontabilizar la reconciliación antes de aplicar la reversión; Validar  |
| 3 | Conciliación Bancos | `SSFI_ConciliationBankReport` | Informe (servlet) | Java `SSFI_ReportConciliationBank` | N | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 4 | Detalle de Reconciliación | `SSFI_ReconciliationDetailReport` | Informe (servlet) | Java `ReportReconciliationDetailFlopec` | N | Clase `ReportReconciliationDetailFlopec` extiende `ReportReconciliationFlopec`. |
| 5 | Resumen de Reconciliación | `SSFI_ReconciliationSummaryReport` | Informe (servlet) | Java `ReportReconciliationSummaryFlopec` | N | Clase `ReportReconciliationSummaryFlopec` extiende `ReportReconciliationFlopec`. |
| 6 | Reporte Detallado de Ventas | `Detailed Sales Summary Report` | Reporte | PL `RptF_SalesDetail` | S | Sales Detail |
| 7 | Resumen(Detalle de Ventas) | `Summary(Detail Sales)` | Reporte | PL `RptF_SalesDetailSub.jrxml` | S | Summary(Detail Sales) |

**Total acciones documentadas (extract):** **7** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/com.sidesoft.localization.ecuador.finances/js/ob-ssfi-addPayment.js` |
| `web/com.sidesoft.localization.ecuador.finances/js/reconciliationDetail.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `com.sidesoft.localization.ecuador.finances`.

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

# Glosario — prefijo `SSFI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSFI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.localization.ecuador.finances` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Ssfi_ConsumptionImprestAccountsGenerated` — Consumo de anticipos generados
- `SSFI M_Inventory Post` — Proceso de conteo de inventario
- `ssfi_reverse_reconcile` — Reversar conciliación
- `SSFI_ConciliationBankReport` — Conciliación Bancos
- `SSFI_ReconciliationDetailReport` — Detalle de Reconciliación
- `SSFI_ReconciliationSummaryReport` — Resumen de Reconciliación
- `Detail Account Receivable WAdjust` — Anticipos por cobrar detallado
- `Summary Account Receivable WAdjust` — Anticipos por Liquidar - Clientes
- `Summary Account Payable WAdjust` — Anticipos por Liquidar Proveedores
- `Detail Account Payable WAdjust` — Anticipos por pagar detallado
- `Ssfi_Analysis_Purchases` — Análisis general de compras
- `Cash_Report` — Cash Report
- `Ssfi_SummaryDeliveriesByPeriod` — Consolidado de Guías de salida por periodo
- `Total Account Payable UAdjust` — Cuenta total por pagar sin anticipo
- `C_Customer_Accounting_Detail` — Detalle contabilidad cliente

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Complement Financial Account
**Package:** `ec.com.sidesoft.localization.ecuador.financial.account`

# Module overview — Sidesoft Complement Financial Account

## Functional

El módulo Sidesoft Complement Financial Account está diseñado para gestionar cuentas financieras complementarias en el contexto ecuatoriano. Este módulo es utilizado principalmente por usuarios de negocio que gestionan cuentas dentro del ERP Openbravo, así como por equipos de soporte L2 que brindan asistencia técnica. Su propósito es facilitar el manejo y validación de transacciones financieras, asegurando que las referencias y depósitos se administren de manera adecuada. Se requiere del módulo de compatibilidad 2.50 a 3.00, lo que representa una dependencia clave para su correcta implementación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/ecuador/financial/account` |
| Web | `web/ec.com.sidesoft.localization.ecuador.financial.account/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SFIAC`

# Guía de chat — Sidesoft Complement Financial Account

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.ecuador.financial.account`).

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
- «¿Qué es la tabla sfiac_payment_lot_file?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo verificar si un depósito ha sido registrado correctamente?
- ¿Qué hago si veo un error en la referencia de un pago?
- ¿Cómo gestiono un cheque que no tiene cobros asociados?
- ¿Cuál es el proceso para actualizar información en una cuenta financiera?
- ¿Dónde puedo encontrar más información sobre las funciones del módulo?
- ¿Qué debo hacer si mi transacción no se valida correctamente?
- ¿Cómo puedo acceder a la ventana de cuentas financieras?
- ¿Qué campos son obligatorios al crear una nueva cuenta financiera?

# Domain — data model

## Functional

El módulo tiene como entidad cabecera la tabla 'fin_financial_account', donde se gestionan las cuentas financieras. Este módulo no presenta etapas definidas claramente en el flujo, ya que se centra más en la validación y verificación de datos. Las relaciones importantes se encuentran entre las tablas modificadas, las cuales incluyen 'C_ELEMENTVALUE', 'C_INVOICE', 'C_PERIOD', 'FACT_ACCT', y 'FIN_PAYMENT'. Los triggers clave incluyen 'SFIAC_DEPOSITVERIFIED_TRG', que valida la existencia de cobros, y 'SFIAC_VALIDATE_REFERENCE_TRG', que asegura que una referencia no esté duplicada en otras transacciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sfiac_payment_lot_file` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sfiac_payment_lot_file` | Sfiac_Payment_Lot_file | — | — | ad_client_id→ad_client; ad_org_id→ad_org; fin_financial_account_id→fin_financial_account | Detalle enlazado a ad_client, ad_org, fin_financial_account. | PK `sfiac_payment_lot_file_pk`; Cols: fin_financial_account_id, name, templatelocation, reportfilename, templatefilename |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Sfiac_Payment_Lot_file` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_ELEMENTVALUE`, `C_INVOICE`, `C_PERIOD`, `FACT_ACCT`, `FIN_FINANCIAL_ACCOUNT`, `FIN_PAYMENT`, `GL_JOURNAL`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo cuenta con una sola ventana que se encuentra accesible dentro de la interfaz de usuario de Openbravo. Los usuarios pueden navegar a través de esta ventana para acceder a las funcionalidades relacionadas con la gestión de cuentas financieras, permitiendo una interacción directa con los datos implicados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.ecuador.financial.account.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.ecuador.financial.account.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `2845D761A8394468BD3BA4710AA888D4`

- **AD_TAB_ID:** `2845D761A8394468BD3BA4710AA888D4` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 132 | Deposit | `EM_Sfiac_Isdeposit` | No | No | — |
| 133 | Deposit Number | `EM_Sfiac_Deposit` | No | No | — |
| 460 | Payment Lot | `EM_Sfiac_Payment_Lot` | No | No | D2A0D89EDB884813B6833F6880777C27 |
| 470 | Payment Lot Format | `EM_Sfiac_Payment_Lot_Format` | No | No | D2A0D89EDB884813B6833F6880777C27 |
| 480 | Petty Cash | `EM_Sfiac_Petty_Cash` | No | No | 9BB3C3C3EB794C44AE9F4477B0F72CBD |
| 490 | Fixed Amount | `EM_Sfiac_Fixed_Amount` | No | No | 9BB3C3C3EB794C44AE9F4477B0F72CBD |
| 500 | Consumption Percentage | `EM_Sfiac_Percentage` | No | No | 9BB3C3C3EB794C44AE9F4477B0F72CBD |

### Payment Lot File

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 40 | Name | `Name` | No | No | — |
| 50 | Template Location | `Templatelocation` | No | No | — |
| 60 | Template Filename | `Templatefilename` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Aunque el módulo no incluye procesos con botones como completar o rechazar, se centra en la validación de datos mediante triggers que operan en segundo plano. Las validaciones frecuentes incluyen la verificación de depósitos y referencias en el módulo de pagos, asegurando la integridad y la precisión de las transacciones financieras. Actualmente, no se disponen de informes específicos como parte de este módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.ecuador.financial.account.es_ES/referencedata/translation/`.

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
| `Sfiac_DepositExist` | The same check and deposit number already exist. | The same check and deposit number already exist. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfiac_DepositNumberRequired` | Deposit number is required. | Deposit number is required. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

No se dispone de clases Java específicas en este módulo, por lo que no se requiere interacción Java en su funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.ecuador.financial.account`.

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
| Trigger `SFIAC_DEPOSITVERIFIED_TRG` | `fin_finacc_transaction` | after INSERT | NO EXISTEN COBROS CON EL CHEQUE Y NUMERO DE DEPOSITO; UPDATE fin_financial_account SET em_sfiac_isdeposit = 'N', em_sfiac_deposit = NULL WHERE fin_financial_account_id = NEW.fin_financial_account_id; |
| Trigger `SFIAC_DEPOSIT_TRG` | `fin_financial_account` | after INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SFIAC_VALIDATE_REFERENCE_TRG` | `fin_payment` | before INSERT/UPDATE | Número de referencia registrado en otra transacción |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers desempeñan un papel fundamental al garantizar que las operaciones en las tablas se realicen de acuerdo con las reglas de negocio definidas. En particular, se destacan la rutina PL/pgSQL para el manejo de depósitos y la validación de referencias dentro de las transacciones de pago. Estos elementos son esenciales para el soporte y la correcta funcionalidad del módulo dentro del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SFIAC_DEPOSITVERIFIED_TRG` | `fin_finacc_transaction` | after | INSERT | NO EXISTEN COBROS CON EL CHEQUE Y NUMERO DE DEPOSITO; UPDATE fin_financial_account SET em_sfiac_isdeposit = 'N', em_sfiac_deposit = NULL WHERE fin_financial_account_id = NEW.fin_financial_account_id; | `model/triggers/SFIAC_DEPOSITVERIFIED_TRG.xml` |
| `SFIAC_DEPOSIT_TRG` | `fin_financial_account` | after | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SFIAC_DEPOSIT_TRG.xml` |
| `SFIAC_VALIDATE_REFERENCE_TRG` | `fin_payment` | before | INSERT/UPDATE | Número de referencia registrado en otra transacción | `model/triggers/SFIAC_VALIDATE_REFERENCE_TRG.xml` |
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

Módulo: `ec.com.sidesoft.localization.ecuador.financial.account`.

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

# Glosario — prefijo `SFIAC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SFIAC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.ecuador.financial.account` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Financial Account
**Package:** `ec.com.sidesoft.financialaccount.document.type`

# Module overview — Financial Account

## Functional

El módulo Financial Account permite la gestión de cuentas financieras dentro de la plataforma Openbravo, facilitando el registro y control de transacciones financieras. Los actores principales incluyen usuarios de negocio que ingresan y gestionan datos, así como el soporte de nivel 2 (L2) que brinda asistencia técnica. El alcance del módulo abarca la generación y gestión de documentos financieros, asegurando que las transacciones se lleven a cabo de manera eficiente y conforme a las políticas contables establecidas. Este módulo depende de la compatibilidad con la '2.50 to 3.00 Compatibility Skin' y del núcleo de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/financialaccount/document/type` |
| Web | `web/ec.com.sidesoft.financialaccount.document.type/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SFADT`

# Guía de chat — Financial Account

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.financialaccount.document.type`).

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
- «¿Qué es la tabla sfadt_acc_sequences?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar una nueva transacción financiera?
- ¿Qué debo hacer si un campo obligatorio no se completa y no puedo guardar?
- ¿Cómo se genera un número de documento único en el sistema?
- ¿Dónde se pueden visualizar las transacciones financieras registradas?
- ¿Qué pasos debo seguir para editar una transacción existente?
- ¿Cómo funciona la validación de secuencias de documentos?
- ¿Qué hacer si un documento no se puede procesar?
- ¿Cuál es la diferencia entre los tipos de documentos disponibles en el módulo?

# Domain — data model

## Functional

El modelo de datos se centra en la tabla principal 'FIN_FINACC_TRANSACTION', que actúa como la entidad cabecera para las transacciones financieras. La estructura incluye una serie de campos que registran información relevante sobre cada transacción. A pesar de que no se define claramente un flujo de etapas, los triggers asociados permiten la verificación y secuenciación de documentos. Por ejemplo, el trigger 'SFADT_DOCUMENTNO_TRG' asegura que cada transacción tenga un identificador único, mientras que 'SFADT_VERIFYFILL_TGR' valida que todos los campos sean obligatorios antes de permitir una inserción en la tabla correspondiente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sfadt_acc_sequences` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sfadt_acc_sequences` | sfadt_acc_sequences | `SFADT_VERIFYFILL_TGR` | — | c_acctschema_table_id→c_acctschema_table; ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org | Detalle enlazado a ad_client, c_acctschema_table, c_doctype. Validado por trigger(s): SFADT_VERIFYFILL_TGR. | PK `sfadt_ac_key`; Cols: c_doctype_id, type, trxtype, c_acctschema_table_id; `SFADT_AC_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sfadt_acc_sequences` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`FIN_FINACC_TRANSACTION`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Aunque el módulo no presenta ventanas explícitas en su inventario, la navegación se realiza a través de la interfaz de usuario estándar de Openbravo, donde los usuarios pueden acceder a la funcionalidad del módulo utilizando los menús y opciones disponibles en el ERP. Se espera que los usuarios interactúen a través de formularios y listas que hacen uso del modelo de datos descrito.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.financialaccount.document.type.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.financialaccount.document.type.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `23691259D1BD4496BCC5F32645BCA4B9`

- **AD_TAB_ID:** `23691259D1BD4496BCC5F32645BCA4B9` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 3 | C_Doctype | `EM_Sfadt_C_Doctype_ID` | No | No | — |
| 7 | EM_Sfadt_Accsequence | `EM_Sfadt_Accsequence` | No | Sí | — |

### Accounting Sequences

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Type | `Trxtype` | No | No | — |
| 50 | Type of financial account | `Type` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

No se identifican botones de proceso específicos dentro del módulo, lo que sugiere que las interacciones se centran en las operaciones de entrada de datos y la verificación a través de triggers y validaciones. Los informes también son escasos en esta versión, pero es probable que se utilicen consultores personalizados para generar información financiera y análisis de las transacciones, basándose en los datos ingresados. Las validaciones frecuentes incluyen la comprobación de campos obligatorios y la correcta secuenciación de documentos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.financialaccount.document.type.es_ES/referencedata/translation/`.

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

El módulo incluye una clase Java llamada 'sfadt_documentType', que extiende de 'SimpleCallout' para gestionar la lógica de llamadas de backend, facilitando la asociación de un número de documento a un tipo de documento específico durante la creación de nuevas transacciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.financialaccount.document.type`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `sfadt_documentType` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/financialaccount/document/type/ad_callouts/sfadt_documentType.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SFADT_DOCUMENTNO_TRG` | `fin_finacc_transaction` | after INSERT | id unico del tipo de documento para finacc_transaction, tomamos el ultimo creado; vDocTypeID := '44F94AE042F54E929FF360F18D0D28F0'; |
| Trigger `SFADT_FINTRANSACTION_SEQ_TRG` | `fin_finacc_transaction` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SFADT_VERIFYFILL_TGR` | `sfadt_acc_sequences` | before INSERT/UPDATE | Todos los campos son obligatorios para la tabla seleccionada. |
| AD_VAL_RULE | — | `Types of documents for financial account` | `C_DocType.DocBaseType IN ('FAT')` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers desempeñan un papel vital en la lógica de negocio del módulo, garantizando la integridad de los datos y la correcta gestión de la secuenciación de documentos. La función PL/pgSQL definida en el módulo está vinculada a asegurar que las transacciones financieras se manejen según las reglas establecidas, mientras que los triggers se encargan de validar condiciones antes de realizar operaciones sobre la base de datos, contribuyendo a la robustez en la gestión del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SFADT_DOCUMENTNO_TRG` | `fin_finacc_transaction` | after | INSERT | id unico del tipo de documento para finacc_transaction, tomamos el ultimo creado; vDocTypeID := '44F94AE042F54E929FF360F18D0D28F0'; | `model/triggers/SFADT_DOCUMENTNO_TRG.xml` |
| `SFADT_FINTRANSACTION_SEQ_TRG` | `fin_finacc_transaction` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SFADT_FINTRANSACTION_SEQ_TRG.xml` |
| `SFADT_VERIFYFILL_TGR` | `sfadt_acc_sequences` | before | INSERT/UPDATE | Todos los campos son obligatorios para la tabla seleccionada. | `model/triggers/SFADT_VERIFYFILL_TGR.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sfadt_documentno_trgmm` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SFADT_DOCUMENTNO_TRGMM.xml` |
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

Módulo: `ec.com.sidesoft.financialaccount.document.type`.

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

# Glosario — prefijo `SFADT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SFADT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.financialaccount.document.type` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Custom Close Cash
**Package:** `ec.com.sidesoft.custom.closecash`

# Module overview — Sidesoft Custom Close Cash

## Functional

El módulo Sidesoft Custom Close Cash tiene como propósito gestionar el cierre de caja de manera eficiente y adaptada a los requerimientos específicos del negocio. Este módulo es utilizado principalmente por el personal administrativo encargado del manejo de las finanzas y los operadores de caja, permitiendo un control adecuado de las transacciones. El alcance del módulo incluye la configuración del cierre de caja, ejecución del cierre y la gestión de transacciones asociadas. Este módulo depende del núcleo del sistema Openbravo, lo que asegura una integración fluida con otras funcionalidades del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/closecash` |
| Web | `web/ec.com.sidesoft.custom.closecash/` |

### Declared dependencies

- Core

### Version

**2.0.1** (from `AD_MODULE.xml`).

### DB prefix

`SCCC`

# Guía de chat — Sidesoft Custom Close Cash

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.closecash`).

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
- «¿Qué es la tabla sccc_setup?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo configurar el cierre de caja?
- ¿Qué pasos debo seguir para finalizar un cierre de caja?
- ¿Cómo puedo revisar las transacciones afectadas por un cierre de caja?
- ¿Qué hacer si un cierre de caja no se finaliza correctamente?
- ¿Dónde encuentro los registros de cierres de caja realizados?
- ¿Es posible deshacer un cierre de caja realizado accidentalmente?
- ¿Qué validaciones se realizan antes de ejecutar un cierre de caja?
- ¿Cómo solucionar problemas relacionados con el cierre de caja?

# Domain — data model

## Functional

El modelo de datos de este módulo se centra en la entidad principal 'sccc_setup', que representa la configuración del cierre de caja. Este modelo no incluye tablas de etapas explícitas, pero se relaciona con entidades como 'sccc_cash_clousureline' y 'FIN_FinaccTransaction' para llevar a cabo el procesamiento de transacciones. Los triggers clave aseguran la integridad de los datos y la ejecución de funciones específicas, como verificar la existencia de módulos avanzados y mantener la unicidad en la organización.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sccc_cash_clousure` |
| `sccc_cash_clousureline` |
| `sccc_payment_method` |
| `sccc_setup` |
| `sccc_user` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sccc_cash_clousure` | Sccc_Cash_Closure | — | — | sccc_setup_id→sccc_setup; ad_client_id→ad_client; ad_org_id→ad_org; ad_user_id→ad_user | Detalle enlazado a ad_client, ad_org, sccc_setup. | PK `sccc_cashcls_key`; Cols: ad_user_id, name, closingdate, description, totalincome; `SCCC_CASHCLS_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); idx `SCCC_CASH_CLOUSURE_DATE_IDX` (closingdate); idx `SCCC_CASH_CLOUSURE_IDX` (sccc_cash_clousure_id) (+1) |
| `sccc_cash_clousureline` | Sccc_Cash_Clousureline | `SCCC_INSERTCLOSECASH_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_user_id→ad_user; sccc_cash_clousure_id→sccc_cash_clousure; fin_paymentmethod_id→fin_paymentmethod | Detalle enlazado a ad_client, ad_org, ad_user. Validado por trigger(s): SCCC_INSERTCLOSECASH_TRG. | PK `sccc_cline_key`; Cols: ad_user_id, fin_paymentmethod_id, amount, description, sccc_cash_clousure_id; `SCCC_CLINE_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); idx `SCCC_CASH_LINE_ACCOUNT_IDX` (typeaccount); idx `SCCC_CASH_LINE_CLOSEMETHOD_IDX` (sccc_cash_clousure_id, fin_paymentmethod_id) (+2) |
| `sccc_payment_method` | Sccc_Payment_Method | — | `SCCC_PYMNTMETHOD` (fin_paymentmethod_id, typeaccount, sccc_setup_id) | ad_client_id→ad_client; ad_org_id→ad_org; ad_user_id→ad_user; sccc_setup_id→sccc_setup; fin_financial_account_id→fin_financial_account (+1) | Detalle enlazado a ad_client, ad_org, ad_user. | PK `sccc_payment_method_key`; Cols: ad_user_id, fin_paymentmethod_id, order_number, fin_financial_account_id, typeaccount; `SCCC_BLIND_CHECK`: BLIND IN ('Y', 'N'); `SCCC_PYMTMTD_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); idx `SCCC_PMSETUP_IDX` (sccc_setup_id, fin_paymentmethod_id) |
| `sccc_setup` | Sccc_Setup | `SCCC_DOCTYPE_NOT_NULL_TRG`; `SCCC_UNIQUE_ORG_TRG` | — | c_doctype_credit_notes_id→c_doctype; c_doctype_reversed_id→c_doctype; fin_financial_account_id→fin_financial_account; ad_client_id→ad_client; ad_org_id→ad_org (+3) | Detalle enlazado a c_doctype, fin_financial_account. Validado por trigger(s): SCCC_DOCTYPE_NOT_NULL_TRG, SCCC_UNIQUE_ORG_TRG. | PK `sccc_setup_key`; Cols: ad_user_id, name, description, fin_financial_account_id, c_glitem_id; `SCCC_SETUP_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); `SCCC_SETUP_PAYMENTSTODATE_CHCK`: PAYMENTSTODATE IN ('Y', 'N'); idx `SCCC_SETUP_IDX` (sccc_setup_id) |
| `sccc_user` | sccc_user | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sccc_setup_id→sccc_setup; ad_user_id→ad_user | Detalle enlazado a ad_client, ad_org, sccc_setup. | PK `sccc_user_key`; Cols: ad_user_id, sccc_setup_id; `SCCC_USER_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Sccc_Cash_Closure` |
| `Sccc_Cash_Clousureline` |
| `Sccc_Payment_Method` |
| `Sccc_Setup` |
| `sccc_user` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ROLE`, `C_DOCTYPE`, `C_INVOICE`, `FIN_BANKSTATEMENTLINE`, `FIN_FINACC_TRANSACTION`, `FIN_PAYMENT`, `SSCCCIN_INVOICE_DOCTYPE`, `SSCCSO_TYPE_OF_DOCUMENT`, `SSCRCC_PAYMENT_DETAILED`, `SSWS_WITHHOLDINGSALE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Navegar por el módulo Sidesoft Custom Close Cash se realiza a través de tres ventanas principales: 'Cierre de caja', 'Cierre de caja - Administrador' y 'Configuración cierre de caja'. Estas ventanas permiten a los usuarios realizar configuraciones, iniciar cierres y administrar información relacionada con las transacciones de caja. Cada ventana se complementa con distintas pestañas que facilitan la interacción y visualización de datos relevantes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.closecash.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Cierre de caja | Cash Clousure |
| Cierre de caja - Administrador | Cash Clousure - Admin |
| Configuración cierre de caja | Setup - Close Cash |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Cierre de caja | Cash Clousure | No |
| Cierre de caja | Close Cash | Sí |
| Cierre de caja - Administrador | Cash Clousure - Admin | No |
| Configuración cierre de caja | Setup - Close Cash | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.closecash.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Cierre de caja

- **AD_WINDOW_ID:** `67C3F5060FE3451681828B742B3715A2`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `B9AA966B759748ACBAB9E5D9552A6659` | 0 |
| 20 | Lines | `A3332C01540D4D1890EB44798BBFBA6A` | 1 |

### Ventana: Cierre de caja - Administrador

- **AD_WINDOW_ID:** `F9352E711BD144A2BF4021CDCC28945C`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `B9AA966B759748ACBAB9E5D9552A6659` | 0 |
| 20 | Lines | `A3332C01540D4D1890EB44798BBFBA6A` | 1 |

### Ventana: Configuración cierre de caja

- **AD_WINDOW_ID:** `B2C17CF575FE4491B384CD17C172792B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `86E7C7FB87BA4789B79BE5E840346162` | 0 |
| 20 | Payment Method | `74E3CB29580D44DDA891F979525A0158` | 1 |
| 30 | User | `64CDA319B8DD468E90AA68A2562AD585` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `119`

- **AD_TAB_ID:** `119` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 190 | Close Cash | `EM_Sccc_Closingdate` | No | No | — |

### Pestaña `23691259D1BD4496BCC5F32645BCA4B9`

- **AD_TAB_ID:** `23691259D1BD4496BCC5F32645BCA4B9` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2070 | Is Cash Clousure | `EM_Sccc_Iscashclousure` | No | Sí | — |
| 2080 | Sccc_Cash_Clousure_ID | `EM_Sccc_Cash_Clousure_ID` | No | Sí | — |

### Lines (ventana: Cierre de caja - Administrador)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `Order_Number` | No | No | — |
| 20 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 30 | Amount | `Amount` | No | No | — |
| 40 | Typeaccount | `Typeaccount` | No | No | — |
| 80 | Description | `Description` | No | No | — |

### Lines (ventana: Cierre de caja)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `Order_Number` | No | No | — |
| 20 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 30 | Amount | `Amount` | No | No | — |
| 40 | Typeaccount | `Typeaccount` | No | No | — |
| 90 | Description | `Description` | No | No | — |

### Payment Method (ventana: Configuración cierre de caja)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `Order_Number` | No | No | — |
| 20 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 30 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 40 | Typeaccount | `Typeaccount` | No | No | — |
| 130 | Blind | `Blind` | No | No | — |
| 160 | Show in report | `Isshowreport` | No | No | — |

### Header (ventana: Configuración cierre de caja)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Name | `Name` | No | No | — |
| 30 | Description | `Description` | No | No | — |
| 40 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 50 | G/L Item | `C_Glitem_ID` | No | No | — |
| 60 | Cost Center | `C_Costcenter_ID` | No | No | — |
| 65 | Paymentstodate | `Paymentstodate` | No | No | — |
| 70 | Document type sales | `C_Doctype_Sales_ID` | No | No | — |
| 80 | Document type credit note | `C_Doctype_Credit_Notes_ID` | No | No | — |
| 90 | Document type reversed | `C_Doctype_Reversed_ID` | No | No | — |
| 100 | Active | `Isactive` | No | No | — |
| 110 | Blind | `Blind` | No | No | — |

### Header (ventana: Cierre de caja - Administrador)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Name | `Name` | No | No | — |
| 30 | Closingdate | `Closingdate` | No | No | — |
| 33 | Process Date | `Process_Date` | No | No | — |
| 35 | Cash clousure | `Sccc_Setup_ID` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Total income | `Totalincome` | No | Sí | — |
| 60 | Totalexpenses | `Totalexpenses` | No | Sí | — |
| 70 | Totalsales | `Totalsales` | No | Sí | — |
| 80 | Difference | `Difference` | No | No | — |
| 90 | Document Status | `DocStatus` | No | Sí | — |
| 150 | Process | `Process` | No | No | — |
| 170 | Closecash Unprocess | `Unprocess` | No | No | — |

### Header (ventana: Cierre de caja)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Name | `Name` | No | No | — |
| 30 | Closingdate | `Closingdate` | No | No | — |
| 35 | Cash clousure | `Sccc_Setup_ID` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Total income | `Totalincome` | No | Sí | — |
| 60 | Totalexpenses | `Totalexpenses` | No | Sí | — |
| 70 | Totalsales | `Totalsales` | No | Sí | — |
| 75 | Difference | `Difference` | No | Sí | — |
| 80 | Load Lines | `Loadlines` | No | No | — |
| 90 | Document Status | `DocStatus` | No | Sí | — |
| 170 | Record | `Record` | No | No | — |

### User (ventana: Configuración cierre de caja)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 15 | User/Contact | `AD_User_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Entre los procesos más comunes en el módulo se encuentran la finalización o rechazo de cierres de caja, donde los usuarios pueden completar, retornar o rechazar transacciones. Adicionalmente, el módulo cuenta con diversas validaciones para asegurar la correcta ejecución del cierre, incluyendo comprobaciones de requisitos previos y fechas de cierre adecuadas. Aunque no se generan informes directamente desde el módulo, se apoya en la funcionalidad del sistema para monitorear el cumplimiento de los procedimientos necesarios.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.closecash.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Desprocesar | Closecash Unprocess | sccc_closecashunprocess | Java `Unprocess` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sccc_Cash_Clousure_ID`, No se ha logrado recuperar las transacciones afectadas con el presente cierra de caja. | `src/ec/com/sidesoft/custom/closecash/ad_process/Unprocess.java` |
| Botón (PL/pgSQL) | Cargar líneas | Load Lines | Sccc_Load_Lines | `sccc_loadlines` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | — |
| Botón (PL/pgSQL) | PostExtensionPoints CloseCash | PostExtensionPoints CloseCash | sccc_PostExtensionPoints_CloseCash | `sccc_postunprocess` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Botón (PL/pgSQL) | PreExtensionPoints CloseCash | PreExtensionPoints CloseCash | sccc_PreExtensionPoints_CloseCash | `sccc_preunprocess` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Botón (PL/pgSQL) | Proceso Cierre de Caja | Clousure Process | Sccc_Clousure_Process | `sccc_clousureprocess` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN | — |
| Botón (PL/pgSQL) | Registrar | Record | Sccc_Record | `sccc_record` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | — |
| Botón (PL/pgSQL) | Registrar | Record | Sccc_Record | `sccc_record` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | — |
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
| Background (Java) | Proceso Background Cierre de Caja | Process Cash Clousures | Sccc_Cash_Clousure | Java `Sccc_ProcessTransaction` (AD_MODEL_OBJECT `P`) | Proceso Openbravo ver `doExecute` en fuente | `src/ec/com/sidesoft/custom/closecash/background/Sccc_ProcessTransaction.java` |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Background (Java) | Proceso Background Cierre de Caja | `Sccc_ProcessTransaction` | Proceso Java (toolbar/background) | `—` | — | `src/ec/com/sidesoft/custom/closecash/background/Sccc_ProcessTransaction.java` |
| Botón (Java) | Desprocesar | `Unprocess` | Proceso Java (toolbar/background) | `Sccc_Cash_Clousure_ID` | No se ha logrado recuperar las transacciones afectadas con el presente cierra de caja. | `src/ec/com/sidesoft/custom/closecash/ad_process/Unprocess.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Desprocesar | Closecash Unprocess | sccc_closecashunprocess | Java `Unprocess` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sccc_Cash_Clousure_ID`, No se ha logrado recuperar las transacciones afectadas con el presente cierra de caja. | `src/ec/com/sidesoft/custom/closecash/ad_process/Unprocess.java` |
| Botón (PL/pgSQL) | Cargar líneas | Load Lines | Sccc_Load_Lines | `sccc_loadlines` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | — |
| Botón (PL/pgSQL) | PostExtensionPoints CloseCash | PostExtensionPoints CloseCash | sccc_PostExtensionPoints_CloseCash | `sccc_postunprocess` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Botón (PL/pgSQL) | PreExtensionPoints CloseCash | PreExtensionPoints CloseCash | sccc_PreExtensionPoints_CloseCash | `sccc_preunprocess` | sccc_preunprocess - PreUnprocess Extension Point | — |
| Botón (PL/pgSQL) | Proceso Cierre de Caja | Clousure Process | Sccc_Clousure_Process | `sccc_clousureprocess` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN | — |
| Botón (PL/pgSQL) | Registrar | Record | Sccc_Record | `sccc_record` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | — |
| Botón (PL/pgSQL) | Registrar | Record | Sccc_Record | `sccc_record` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Desprocesar | Closecash Unprocess | Java `Unprocess` | Proceso Openbravo registro `Sccc_Cash_Clousure_ID`, No se ha logrado recuperar las transacciones afectadas con el presente cierra de caja. | No se ha logrado recuperar las transacciones afectadas con el presente cierra de caja. |
| Botón (PL/pgSQL) | Cargar líneas | Load Lines | PL `sccc_loadlines` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |
| Botón (PL/pgSQL) | PostExtensionPoints CloseCash | PostExtensionPoints CloseCash | PL `sccc_postunprocess` | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point |
| Botón (PL/pgSQL) | PreExtensionPoints CloseCash | PreExtensionPoints CloseCash | PL `sccc_preunprocess` | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point |
| Botón (PL/pgSQL) | Proceso Cierre de Caja | Clousure Process | PL `sccc_clousureprocess` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN |
| Botón (PL/pgSQL) | Registrar | Record | PL `sccc_record` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |
| Botón (PL/pgSQL) | Registrar | Record | PL `sccc_record` | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |
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
| `SCCC_TOTAL_ZERO` | The sum of income and expenses can not be zero. | The sum of income and expenses can not be zero. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SCCC_NOT_INSERT_LINE` | Can not insert/update/delete lines, if the header is in 'Registered' or 'Processed' status. | Can not insert/update/delete lines, if the header is in 'Registered' or 'Processed' status. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SCCC_LINES_NOT_FOUND` | Lines not found to record. | Lines not found to record. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SCCC_ORG_NOT_FOUND` | Organization not found in setup window. | Organization not found in setup window. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sccc_DoctypeNotNull` | Document type fields are required. | Document type fields are required. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sccc_UniqueOrg` | There is already a record with the same organization. | There is already a record with the same organization. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SCCC_PYMNMETHOD_NOTFOUND` | Payment method not found at lines of the setup window. | Payment method not found at lines of the setup window. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sccc_DocTypeNull` | Types of sales document and / or credit notes not configured. | Types of sales document and / or credit notes not configured. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sccc_SetupNotSet` | Cash closing configuration not selected. | Cash closing configuration not selected. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sccc_Difference_Zero` | The difference must be zero. | The difference must be zero. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye clases Java que proporcionan lógica de negocio necesaria para el manejo de los procesos de cierre de caja. Clases como 'Unprocess' y 'Sccc_ProcessTransaction' ejecutan procesos transaccionales y eventos relacionados con la persistencia de datos, asegurando que las reglas de negocio sean cumplidas durante las interacciones con el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.closecash`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Unprocess` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/custom/closecash/ad_process/Unprocess.java` |
| `Sccc_ProcessTransaction` | background | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/custom/closecash/background/Sccc_ProcessTransaction.java` |
| `Sccc_FinTransactionProcess` | event | EntityPersistenceEventObserver | Proceso / informe Java | `src/ec/com/sidesoft/custom/closecash/event/Sccc_FinTransactionProcess.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SCCC_DOCTYPE_NOT_NULL_TRG` | `sccc_setup` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SCCC_INSERTCLOSECASH_TRG` | `sccc_cash_clousureline` | before INSERT/UPDATE/DELETE | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |
| Trigger `SCCC_UNIQUE_ORG_TRG` | `sccc_setup` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Sccc_DoctypeCreditNotes` | `C_DocType.DocBaseType IN ('ARC') AND C_DocType.AD_Table_ID IN (SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(TABLENAME) =` |
| AD_VAL_RULE | — | `Sccc_Validate_User` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Sccc_DoctypeSales` | `C_DocType.DocBaseType IN ('ARI') AND C_DocType.AD_Table_ID IN (SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(TABLENAME) =` |
| AD_VAL_RULE | — | `Sccc_SetupActive` | `Sccc_Setup.IsActive='Y' AND Sccc_Setup.sccc_setup_id IN (SELECT sccc_setup_id FROM sccc_user WHERE isactive='Y' AND ad_u` |
| Función PL `sccc_clousureprocess` | — | invocación proceso | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN |
| Función PL `sccc_loadlines` | — | invocación proceso | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |
| Función PL `sccc_postunprocess` | — | invocación proceso | sccc_preunprocess - PreUnprocess Extension Point |
| Función PL `sccc_preunprocess` | — | invocación proceso | sccc_preunprocess - PreUnprocess Extension Point |
| Función PL `sccc_record` | — | invocación proceso | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers dentro del módulo desempeñan un papel fundamental para mantener la integridad y consistencia de los datos. Por ejemplo, se incluyen rutinas PL/pgSQL que gestionan la validación de datos en la tabla 'sccc_setup' y aseguran que no se generen duplicados en las organizaciones. Las funciones PL también son esenciales para facilitar el procesamiento en segundo plano y realizar validaciones automáticas a lo largo de las transacciones, ayudando al soporte técnico en la detección de errores.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SCCC_INSERTCLOSECASH_TRG` | `sccc_cash_clousureline` | before | INSERT/UPDATE/DELETE | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | `model/triggers/SCCC_INSERTCLOSECASH_TRG.xml` |
| `SCCC_DOCTYPE_NOT_NULL_TRG` | `sccc_setup` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SCCC_DOCTYPE_NOT_NULL_TRG.xml` |
| `SCCC_UNIQUE_ORG_TRG` | `sccc_setup` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SCCC_UNIQUE_ORG_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sccc_clousureprocess` | Proceso Cierre de Caja | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN | `model/functions/SCCC_CLOUSUREPROCESS.xml` |
| `sccc_loadlines` | Cargar líneas | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | `model/functions/SCCC_LOADLINES.xml` |
| `sccc_postunprocess` | PostExtensionPoints CloseCash | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point | `model/functions/SCCC_POSTUNPROCESS.xml` |
| `sccc_preunprocess` | PreExtensionPoints CloseCash | sccc_preunprocess - PreUnprocess Extension Point | sccc_preunprocess - PreUnprocess Extension Point | `model/functions/SCCC_PREUNPROCESS.xml` |
| `sccc_record` | Registrar, Registrar | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | `model/functions/SCCC_RECORD.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Desprocesar | `sccc_closecashunprocess` | Botón (Java) | Java `Unprocess` | N | Proceso Openbravo registro `Sccc_Cash_Clousure_ID`, No se ha logrado recuperar las transacciones afectadas con el presente cierra de caja. |
| 2 | Cargar líneas | `Sccc_Load_Lines` | Botón (PL/pgSQL) | PL `sccc_loadlines` | N | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |
| 3 | PostExtensionPoints CloseCash | `sccc_PostExtensionPoints_CloseCash` | Botón (PL/pgSQL) | PL `sccc_postunprocess` | N | sccc_preunprocess - PreUnprocess Extension Point |
| 4 | PreExtensionPoints CloseCash | `sccc_PreExtensionPoints_CloseCash` | Botón (PL/pgSQL) | PL `sccc_preunprocess` | N | sccc_preunprocess - PreUnprocess Extension Point |
| 5 | Proceso Cierre de Caja | `Sccc_Clousure_Process` | Botón (PL/pgSQL) | PL `sccc_clousureprocess` | N | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN |
| 6 | Registrar | `Sccc_Record` | Botón (PL/pgSQL) | PL `sccc_record` | N | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |
| 7 | Registrar | `Sccc_Record` | Botón (PL/pgSQL) | PL `sccc_record` | N | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |

**Total acciones documentadas (extract):** **7** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `ec.com.sidesoft.custom.closecash`.

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

# Glosario — prefijo `SCCC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SCCC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.closecash` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Sccc_Cash_Clousure` — Proceso Background Cierre de Caja
- `sccc_closecashunprocess` — Desprocesar
- `Sccc_Load_Lines` — Cargar líneas
- `sccc_PostExtensionPoints_CloseCash` — PostExtensionPoints CloseCash
- `sccc_PreExtensionPoints_CloseCash` — PreExtensionPoints CloseCash
- `Sccc_Clousure_Process` — Proceso Cierre de Caja
- `Sccc_Record` — Registrar
- `Sccc_Record` — Registrar

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Custom Close Cash Advanced
**Package:** `ec.com.sidesoft.custom.closecash.advanced`

# Module overview — Sidesoft Custom Close Cash Advanced

## Functional

El módulo 'Sidesoft Custom Close Cash Advanced' está diseñado para optimizar y facilitar el proceso de cierre de caja en el BackOffice de Openbravo, proporcionando funcionalidades que permiten la liquidación de tarjetas de crédito y la importación de datos relacionados. Los actores principales son los usuarios de negocio que realizan cierres de caja, así como el equipo de soporte que atiende incidencias y personaliza funciones según necesidades específicas. El alcance del módulo incluye la generación de reportes sobre el cierre de caja, así como la gestión de liquidaciones, garantizando una integración fluida con otros módulos como 'Sidesoft Custom Close Cash'. Las dependencias principales son el núcleo de Openbravo y el módulo mencionado anteriormente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/closecash/advanced` |
| Web | `web/ec.com.sidesoft.custom.closecash.advanced/` |

### Declared dependencies

- Core
- Sidesoft Custom Close Cash

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SCCA`

# Guía de chat — Sidesoft Custom Close Cash Advanced

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.closecash.advanced`).

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
- «¿Qué es la tabla scca_cash_clousureline2?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo ver el reporte de cierre de caja?
- ¿Qué información necesito para liquidar una tarjeta de crédito?
- ¿Qué hago si un cierre de caja no se completa correctamente?
- ¿Hay alguna validación que deba tener en cuenta al cerrar la caja?
- ¿Cómo puedo importar datos de liquidación de tarjetas?
- ¿Es posible realizar ajustes después del cierre de caja?
- ¿Dónde encuentro el historial de cierres de caja anteriores?
- ¿Qué hacer si mi rol no me permite acceder al módulo de cierre de caja?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad cabecera del cierre de caja, representada por la tabla 'scca_cash_clousureline2', que almacena los detalles de cada cierre. Las relaciones clave se establecen con la tabla 'FIN_PAYMENTMETHOD' para facilitar la liquidación de pagos. Además, este módulo incluye un trigger, 'SCCA_INSERTCLOSECASH_TRG', que se activa al insertar registros en la tabla de cierre de caja, asegurando la integridad de los datos y el cumplimiento de las reglas de negocio definidas. Este trigger es fundamental para la automatización de procesos que requieren validaciones específicas durante el cierre.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `scca_cards_settlement` |
| `scca_cash_clousureline2` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `scca_cards_settlement` | scca_cards_settlement | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_user_id→ad_user; fin_paymentmethod_id→fin_paymentmethod | Detalle enlazado a ad_client, ad_org, ad_user. | PK `scca_csettlement_key`; Cols: ad_user_id, fin_paymentmethod_id, card_type, lot, date_transaction; `SCCA_CSETTL_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `scca_cash_clousureline2` | scca_cash_clousureline2 | `SCCA_INSERTCLOSECASH_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_user_id→ad_user; sccc_cash_clousure_id→sccc_cash_clousure; fin_paymentmethod_id→fin_paymentmethod (+1) | Detalle enlazado a ad_client, ad_org, ad_user. Validado por trigger(s): SCCA_INSERTCLOSECASH_TRG. | PK `scca_cline2_key`; Cols: ad_user_id, fin_paymentmethod_id, amount, description, sccc_cash_clousure_id; `SCCA_CLINE2_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `scca_cards_settlement` |
| `scca_cash_clousureline2` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ROLE`, `FIN_PAYMENTMETHOD`, `SCCC_CASH_CLOUSURELINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo incluye una ventana principal para la 'Liquidación de tarjetas', que permite al usuario acceder a las funciones requeridas para el cierre de caja. La navegación en esta interfaz de usuario es intuitiva, guiando a los usuarios a través de las distintas pestañas de configuración y reporte, facilitando la liquidación y el análisis de los datos recolectados durante el cierre de caja.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.closecash.advanced.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Liquidación de tarjetas | Cards Settlement |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Herramientas de análisis | Analysis Tools | Sí |
| Liquidación de tarjetas | Cards Settlement | No |
| Reporte cierre de caja | Cash Clousure Report | No |
| Reporte liquidación de tarjetas | Cards Settlement Report | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.closecash.advanced.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Liquidación de tarjetas

- **AD_WINDOW_ID:** `5ECE446AD7224BA49ED958FF53D00DD5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `557B5BF209AA4AE7BDFA126504188587` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `119`

- **AD_TAB_ID:** `119` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 170 | EM_Scca_Cashier | `EM_Scca_Cashier` | No | No | — |
| 180 | EM_Scca_Administrator | `EM_Scca_Administrator` | No | No | — |

### Pestaña `3EC5BA28381C413390A9B3CEA3190B56`

- **AD_TAB_ID:** `3EC5BA28381C413390A9B3CEA3190B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 50 | EM_Scca_Financial_Account_ID | `EM_Scca_Financial_Account_ID` | No | No | — |
| 60 | EM_Scca_Card_Type | `EM_Scca_Card_Type` | No | No | — |
| 70 | EM_Scca_Lot | `EM_Scca_Lot` | No | No | — |

### Lines 2

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `Order_Number` | No | No | — |
| 20 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 30 | Amount | `Amount` | No | No | — |
| 40 | Typeaccount | `Typeaccount` | No | No | — |
| 50 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 60 | Card_Type | `Card_Type` | No | No | — |
| 70 | Lot Name | `Lot` | No | No | — |
| 90 | Description | `Description` | No | No | — |

### Header (ventana: Liquidación de tarjetas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 50 | Card_Type | `Card_Type` | No | No | — |
| 60 | Lot Name | `Lot` | No | No | — |
| 70 | Date_Transaction | `Date_Transaction` | No | No | — |
| 80 | Received_Amount | `Received_Amount` | No | No | — |
| 90 | IVA Retention | `IVA_Retention` | No | No | — |
| 100 | Rent Retention | `Rent_Retention` | No | No | — |
| 110 | Bonded_Amount | `Bonded_Amount` | No | No | — |
| 120 | Commission_Amount | `Commission_Amount` | No | No | — |
| 200 | Active | `Isactive` | No | No | — |

### Pestaña `60B6BA2648A3480CAECCB2F17471B5C5`

- **AD_TAB_ID:** `60B6BA2648A3480CAECCB2F17471B5C5` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 50 | EM_Scca_Financial_Account_ID | `EM_Scca_Financial_Account_ID` | No | No | — |
| 60 | EM_Scca_Card_Type | `EM_Scca_Card_Type` | No | No | — |
| 70 | EM_Scca_Lot | `EM_Scca_Lot` | No | No | — |

### Pestaña `A4A463FA34F946BFA3F687DC8754ED93`

- **AD_TAB_ID:** `A4A463FA34F946BFA3F687DC8754ED93` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 46 | Is Cash | `EM_Scca_Iscash` | No | No | — |
| 320 | EM_Scca_Type_Payment | `EM_Scca_Type_Payment` | No | No | — |

### Lines 2

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `Order_Number` | No | No | — |
| 20 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 30 | Amount | `Amount` | No | No | — |
| 40 | Typeaccount | `Typeaccount` | No | No | — |
| 50 | FIN_Financial_Account | `FIN_Financial_Account_ID` | No | No | — |
| 60 | Card_Type | `Card_Type` | No | No | — |
| 70 | Lot Name | `Lot` | No | No | — |
| 90 | Description | `Description` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Entre los procesos disponibles, los usuarios pueden utilizar botones como 'Completar' y 'Retornar', los cuales gestionan el flujo de cerrados de caja. Además, se pueden generar cuatro tipos diferentes de informes, incluyendo 'PRINT GENERIC - CASH CLOSE' y 'PRINT GENERIC - CASH CLOSE LINE', que proporcionan visualizaciones detalladas del estado de las transacciones. Las validaciones frecuentes durante estos procesos garantizan que se cumplan los requisitos antes de cerrar cualquier operación, evitando errores y asegurando la correcta gestión de fondos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.closecash.advanced.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte cierre de caja | Cash Clousure Report | Cash Clousure Report | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte liquidación de tarjetas | Cards Settlement Report | Cards Settlement Report | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | PRINT GENERIC - CASH CLOSE | PRINT GENERIC - CASH CLOSE | PRINT GENERIC - CASH CLOSE | Java `SCCC_CashCloseAdmin` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `F9352E711BD144A2BF4021CDCC28945C|Sccc_Cash_Clousure_ID`. | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseAdmin.java` |
| Reporte | PRINT GENERIC - CASH CLOSE LINE | PRINT GENERIC - CASH CLOSE LINE | PRINT GENERIC - CASH CLOSE LINE | Java `SCCC_CashCloseAdminLine` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `F9352E711BD144A2BF4021CDCC28945C|Sccc_Cash_Clousureline_ID`. | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseAdminLine.java` |
| Reporte | PRINT GENERIC - CASH CLOSE LINE NORM | PRINT GENERIC - CASH CLOSE LINE NORM | PRINT GENERIC - CASH CLOSE LINE NORM | Java `SCCC_CashCloseLine` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `67C3F5060FE3451681828B742B3715A2|Sccc_Cash_Clousureline_ID`. | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseLine.java` |
| Reporte | PRINT GENERIC - CASH CLOSE NORM | PRINT GENERIC - CASH CLOSE NORM | PRINT GENERIC - CASH CLOSE NORM | Java `SCCC_CashClose` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `67C3F5060FE3451681828B742B3715A2|Sccc_Cash_Clousure_ID`. | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashClose.java` |
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
| Reporte | PRINT GENERIC - CASH CLOSE | `SCCC_CashCloseAdmin` | Informe (servlet PDF) | `F9352E711BD144A2BF4021CDCC28945C|Sccc_Cash_Clousure_ID` | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseAdmin.java` |
| Reporte | PRINT GENERIC - CASH CLOSE LINE | `SCCC_CashCloseAdminLine` | Informe (servlet PDF) | `F9352E711BD144A2BF4021CDCC28945C|Sccc_Cash_Clousureline_ID` | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseAdminLine.java` |
| Reporte | PRINT GENERIC - CASH CLOSE LINE NORM | `SCCC_CashCloseLine` | Informe (servlet PDF) | `67C3F5060FE3451681828B742B3715A2|Sccc_Cash_Clousureline_ID` | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseLine.java` |
| Reporte | PRINT GENERIC - CASH CLOSE NORM | `SCCC_CashClose` | Informe (servlet PDF) | `67C3F5060FE3451681828B742B3715A2|Sccc_Cash_Clousure_ID` | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashClose.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte cierre de caja | Cash Clousure Report | Cash Clousure Report | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte liquidación de tarjetas | Cards Settlement Report | Cards Settlement Report | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte cierre de caja | Cash Clousure Report | — | — | — |
| Proceso / otro | Reporte liquidación de tarjetas | Cards Settlement Report | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | PRINT GENERIC - CASH CLOSE | PRINT GENERIC - CASH CLOSE | PRINT GENERIC - CASH CLOSE | Java `SCCC_CashCloseAdmin` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `F9352E711BD144A2BF4021CDCC28945C|Sccc_Cash_Clousure_ID`. | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseAdmin.java` |
| Reporte | PRINT GENERIC - CASH CLOSE LINE | PRINT GENERIC - CASH CLOSE LINE | PRINT GENERIC - CASH CLOSE LINE | Java `SCCC_CashCloseAdminLine` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `F9352E711BD144A2BF4021CDCC28945C|Sccc_Cash_Clousureline_ID`. | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseAdminLine.java` |
| Reporte | PRINT GENERIC - CASH CLOSE LINE NORM | PRINT GENERIC - CASH CLOSE LINE NORM | PRINT GENERIC - CASH CLOSE LINE NORM | Java `SCCC_CashCloseLine` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `67C3F5060FE3451681828B742B3715A2|Sccc_Cash_Clousureline_ID`. | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseLine.java` |
| Reporte | PRINT GENERIC - CASH CLOSE NORM | PRINT GENERIC - CASH CLOSE NORM | PRINT GENERIC - CASH CLOSE NORM | Java `SCCC_CashClose` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `67C3F5060FE3451681828B742B3715A2|Sccc_Cash_Clousure_ID`. | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashClose.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 4**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **4**; archivos `*.jrxml` en el repo = **4**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | PRINT GENERIC - CASH CLOSE | `PRINT GENERIC - CASH CLOSE` | Java `SCCC_CashCloseAdmin`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | PRINT GENERIC - CASH CLOSE |
| 2 | PRINT GENERIC - CASH CLOSE LINE | `PRINT GENERIC - CASH CLOSE LINE` | Java `SCCC_CashCloseAdminLine`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | PRINT GENERIC - CASH CLOSE LINE |
| 3 | PRINT GENERIC - CASH CLOSE LINE NORM | `PRINT GENERIC - CASH CLOSE LINE NORM` | Java `SCCC_CashCloseLine`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | PRINT GENERIC - CASH CLOSE LINE NORM |
| 4 | PRINT GENERIC - CASH CLOSE NORM | `PRINT GENERIC - CASH CLOSE NORM` | Java `SCCC_CashClose`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | PRINT GENERIC - CASH CLOSE NORM |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/Rpt_CardsSettlement.jrxml`
- `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/Rpt_CashClousureInfo.jrxml`
- `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/Rpt_CloseCash.jrxml`
- `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/Rpt_CloseCashLines.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Scca_Label_Rpt_CloseCash_reviwer` | Treasury | Treasury | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Scca_Label_Rpt_CloseCashLines_reviwer` | Treasury | Treasury | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo también incluye varias clases Java, que se utilizan para manejar la lógica de negocio y la generación de reportes basados en la información capturada durante el proceso de cierre de caja. Estas clases, como 'SCCC_CashClose' y 'SCCC_CashCloseAdmin', juegan un papel crucial en la interacción entre el usuario y la base de datos a través de la interfaz web.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.closecash.advanced`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SCCC_CashClose` | ad_Reports | HttpSecureAppServlet | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashClose.java` |
| `SCCC_CashCloseAdmin` | ad_Reports | HttpSecureAppServlet | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseAdmin.java` |
| `SCCC_CashCloseAdminLine` | ad_Reports | HttpSecureAppServlet | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseAdminLine.java` |
| `SCCC_CashCloseLine` | ad_Reports | HttpSecureAppServlet | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_Reports/SCCC_CashCloseLine.java` |
| `Scca_PaymentMethod1` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_callouts/Scca_PaymentMethod1.java` |
| `Scca_PaymentMethod2` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/custom/closecash/advanced/ad_callouts/Scca_PaymentMethod2.java` |
| `ImportCardSettlement` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/custom/closecash/advanced/ad_process/ImportCardSettlement.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SCCA_INSERTCLOSECASH_TRG` | `scca_cash_clousureline2` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Scca_ValidUser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Scca_ValidFinancialAccount` | `EXISTS (SELECT 1 FROM fin_paymentmethod WHERE (fin_paymentmethod.EM_Scca_Type_Payment = 'CH'  OR fin_paymentmethod.EM_Sc` |
| AD_VAL_RULE | — | `Scca_CardValid` | `EXISTS (SELECT 1 FROM fin_paymentmethod WHERE fin_paymentmethod.EM_Scca_Type_Payment = 'CA' AND fin_paymentmethod.fin_pa` |
| AD_VAL_RULE | — | `Scca_FinacialAcct_Banks` | `type='B'` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL/pgSQL del módulo son esenciales para garantizar que las operaciones sobre los datos sean seguras y eficientes. El único trigger 'SCCA_INSERTCLOSECASH_TRG' asegura que todas las inserciones en la tabla de cierre de caja se procesen de acuerdo a las reglas de negocio definidas. Las funciones PL asociadas con el módulo ayudan a llevar a cabo cálculos y procesamientos necesarios para la generación de reportes y otras operaciones de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SCCA_INSERTCLOSECASH_TRG` | `scca_cash_clousureline2` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SCCA_INSERTCLOSECASH_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `scca_processlines2` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SCCA_PROCESSLINES2.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | PRINT GENERIC - CASH CLOSE | `PRINT GENERIC - CASH CLOSE` | Reporte | Java `SCCC_CashCloseAdmin` | S | Genera PDF desde JRXML `—`; contexto sesión `F9352E711BD144A2BF4021CDCC28945C|Sccc_Cash_Clousure_ID`. |
| 2 | PRINT GENERIC - CASH CLOSE LINE | `PRINT GENERIC - CASH CLOSE LINE` | Reporte | Java `SCCC_CashCloseAdminLine` | S | Genera PDF desde JRXML `—`; contexto sesión `F9352E711BD144A2BF4021CDCC28945C|Sccc_Cash_Clousureline_ID`. |
| 3 | PRINT GENERIC - CASH CLOSE LINE NORM | `PRINT GENERIC - CASH CLOSE LINE NORM` | Reporte | Java `SCCC_CashCloseLine` | S | Genera PDF desde JRXML `—`; contexto sesión `67C3F5060FE3451681828B742B3715A2|Sccc_Cash_Clousureline_ID`. |
| 4 | PRINT GENERIC - CASH CLOSE NORM | `PRINT GENERIC - CASH CLOSE NORM` | Reporte | Java `SCCC_CashClose` | S | Genera PDF desde JRXML `—`; contexto sesión `67C3F5060FE3451681828B742B3715A2|Sccc_Cash_Clousure_ID`. |

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

Módulo: `ec.com.sidesoft.custom.closecash.advanced`.

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

# Glosario — prefijo `SCCA`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SCCA` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.closecash.advanced` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Cash Clousure Report` — Reporte cierre de caja
- `Cards Settlement Report` — Reporte liquidación de tarjetas
- `PRINT GENERIC - CASH CLOSE` — PRINT GENERIC - CASH CLOSE
- `PRINT GENERIC - CASH CLOSE LINE` — PRINT GENERIC - CASH CLOSE LINE
- `PRINT GENERIC - CASH CLOSE LINE NORM` — PRINT GENERIC - CASH CLOSE LINE NORM
- `PRINT GENERIC - CASH CLOSE NORM` — PRINT GENERIC - CASH CLOSE NORM

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Closecash Financial Account
**Package:** `ec.com.sidesoft.closecash.financial.account`

# Module overview — Closecash Financial Account

## Functional

El módulo Closecash Financial Account permite gestionar una cuenta financiera destinada al cierre de caja, facilitando el registro de cobros, tanto de transacciones tradicionales como de ingresos directos a la cuenta. Está dirigido principalmente a usuarios de negocio que gestionan la contabilidad, así como a los desarrolladores y personal de soporte L2 que necesiten mantener y modificar el sistema. El alcance incluye la integración de estos ingresos dentro del ecosistema Openbravo y su compatibilidad con otras funcionalidades del ERP. Este módulo depende de la piel de compatibilidad entre las versiones 2.50 y 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/closecash/financial/account` |
| Web | `web/ec.com.sidesoft.closecash.financial.account/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSCCCFA`

# Guía de chat — Closecash Financial Account

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.closecash.financial.account`).

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
- «¿Qué es la tabla sscccfa_fin_acc_concept?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar un ingreso directo a la cuenta financiera?
- ¿Qué pasos debo seguir para cerrar la caja al final del día?
- ¿Dónde puedo ver los conceptos de cobro registrados?
- ¿Cuáles son las dependencias del módulo Closecash Financial Account?
- ¿Existen informes disponibles sobre los ingresos registrados?
- ¿Cómo puedo verificar que la información de la cuenta financiera es correcta?
- ¿qué hago si encuentro un error en un registro de cobro?
- ¿Cómo se puede extender la funcionalidad de este módulo?

# Domain — data model

## Functional

La entidad cabecera de este módulo es la tabla sscccfa_fin_acc_concept, que define los conceptos relacionados con los cobros financieros. La funcionalidad está diseñada para soportar el registro de ingresos, con la posibilidad de extenderse a otros procesos o tablas según sea necesario. Aunque no se han definido triggers específicos para este módulo, la función PL asociada desempeña un papel clave en la gestión de datos y la validación de la información que se ingresa.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sscccfa_fin_acc_concept` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sscccfa_fin_acc_concept` | sscccfa_fin_acc_concept | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_glitem_id→c_glitem; fin_paymentmethod_id→fin_paymentmethod; sccc_setup_id→sccc_setup | Detalle enlazado a ad_client, ad_org, c_glitem. | PK `sscccfa_fin_acc_c_key`; Cols: c_glitem_id, fin_paymentmethod_id, sccc_setup_id |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sscccfa_fin_acc_concept` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

No se dispone de ventanas específicas dentro del módulo, lo que sugiere que la interacción se realiza a través de formularios o elementos básicos. La navegación puede incluir la búsqueda o el acceso a la información relevante en función de los conceptos financieros registrados.

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

### Financial Account Concept

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | G/L Item | `C_Glitem_ID` | No | No | — |
| 40 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo actualmente no cuenta con procesos con botones definidos como completar, retornar o rechazar. Sin embargo, las validaciones pueden estar integradas en la función PL que supervisa el flujo de datos y asegura la correcta entrada de información financiera. La gestión de informes también está ausente, indicando que las funciones de análisis se podrían realizar a través de otras herramientas o módulos del ERP.

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

No se han definido clases Java para este módulo, lo que implica que la lógica del negocio y las integraciones se gestionan principalmente a través de PL y configuraciones dentro del propio ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.closecash.financial.account`.

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
| Función PL `sscccfa_fin_acc_concept` | — | invocación proceso | por cada linea creada aplicar el valor de transacciones de la cuenta financiera sin relacion a cobros; Determinar la cuenta financiera aplicando filtros de metodo de pago por linea de cierre de caja; JOIN  FIN_FinAcc_PaymentMethod fpm on fpm.FIN_Financial_Account_ID =fac.FIN_Financial_Account_ID |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers no están presentes en este módulo, lo que sugiere que las operaciones se manejan principalmente a través de la función PL. Esta función tiene el rol de asegurar la lógica del negocio y las validaciones necesarias en el contexto de los cobros financieros, contribuyendo así a la integridad de la base de datos.

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
| `sscccfa_fin_acc_concept` | — | por cada linea creada aplicar el valor de transacciones de la cuenta financiera sin relacion a cobros; Determinar la cuenta financiera aplicando filtros de metodo de pago por linea de cierre de caja; JOIN FIN_FinAcc_Pay… | por cada linea creada aplicar el valor de transacciones de la cuenta financiera sin relacion a cobros; Determinar la cuenta financiera aplicando filtros de metodo de pago por linea de cierre de caja; JOIN  FIN_FinAcc_PaymentMethod fpm on fpm.FIN_Financial_Account_ID =fac.FIN_Financial_Account_ID; AND fpm.FIN_PaymentMethod_id in ( vCashClosureLine.FIN_Paymentmethod_ID ); Determinar si el concepto contable de la transaccion esta configurado en la conf del cierre de caja | `model/functions/SSCCCFA_FIN_ACC_CONCEPT.xml` |
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

Módulo: `ec.com.sidesoft.closecash.financial.account`.

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

# Glosario — prefijo `SSCCCFA`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCCCFA` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.closecash.financial.account` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Close Cash for Sales Order
**Package:** `ec.com.sidesoft.closecash.sales.order`

# Module overview — Sidesoft Close Cash for Sales Order

## Functional

El módulo 'Sidesoft Close Cash for Sales Order' tiene como propósito gestionar el cierre de caja para pedidos de venta en el sistema Openbravo. Su actor principal son los usuarios del área financiera y de tesorería, quienes realizarán el cierre de ingresos y egresos a partir de pedidos de venta. El alcance del módulo incluye funcionalidades para registrar, validar y procesar las transacciones relacionadas al cierre de caja. Este módulo depende de la compatibilidad con '2.50 to 3.00 Compatibility Skin' y de 'Sidesoft Custom Close Cash', lo que garantiza su integración adecuada en el entorno de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/closecash/sales/order` |
| Web | `web/ec.com.sidesoft.closecash.sales.order/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Sidesoft Custom Close Cash

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSCCSO`

# Guía de chat — Sidesoft Close Cash for Sales Order

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.closecash.sales.order`).

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
- «¿Qué es la tabla ssccso_cash_inc_exp?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar un ingreso en el cierre de caja?
- ¿Qué debo hacer si un pedido de venta no se refleja en el cierre de caja?
- ¿Cómo se elimina una relación de cierre de caja con un método de pago?
- ¿Cuáles son los pasos para procesar un egreso en la gestión de caja?
- ¿Qué validaciones se realizan al completar el cierre de caja?
- ¿Dónde puedo acceder a la gestión de ingresos y egresos en el sistema?
- ¿Es posible revertir un cierre de caja una vez completado?
- ¿Cómo se actualizan los datos en la tabla de ingresos y egresos?

# Domain — data model

## Functional

La entidad cabecera principal del módulo es la tabla 'ssccso_cash_inc_exp', que almacena información relevante sobre ingresos y egresos de caja. Este modelo contiene dos triggers clave: 'SSCCSO_CASH_INC_EXP_TRG', que se ejecuta durante la gestión de ingresos y egresos, y 'SSCCSO_REMOVE_RELATIONS_TRG', que elimina las relaciones entre el cierre de caja y el método de pago correspondiente. Estos triggers son fundamentales para asegurar la integridad de los datos y el correcto flujo del proceso de cierre de caja.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssccso_accounting_concept` |
| `ssccso_cash_inc_exp` |
| `ssccso_type_of_document` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssccso_accounting_concept` | Ssccso_Accounting_Concept | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_glitem_id→c_glitem; sccc_setup_id→sccc_setup | Detalle enlazado a ad_client, ad_org, c_glitem. | PK `ssccso_acc_concept_key`; Cols: c_glitem_id, sccc_setup_id, issummary; `SSCCSO_ACC_CONCEPT_ISACTI_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCSO_ACC_CONCEPT_ISSUMM_CHK`: ISSUMMARY IN ('Y', 'N') |
| `ssccso_cash_inc_exp` | Ssccso_Cash_Inc_Exp | `SSCCSO_CASH_INC_EXP_TRG` | — | sccc_cash_clousure_id→sccc_cash_clousure; ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_doctype_id→c_doctype (+4) | Detalle enlazado a ad_client, ad_org, sccc_cash_clousure. Validado por trigger(s): SSCCSO_CASH_INC_EXP_TRG. | PK `ssccso_cash_inc_exp_key`; Cols: c_doctype_id, documentno, type_of_operation, fin_financial_account_id, dateactual; `SSCCSO_CASH_INC_EXP_ISACTI_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCSO_CASH_INC_EXP_ISREC_CHK`: ISRECONCILED IN ('Y', 'N') (+1) |
| `ssccso_type_of_document` | Ssccso_Type_Of_Document | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype; sccc_setup_id→sccc_setup | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `ssccso_type_of_doc_key`; Cols: c_doctype_id, sccc_setup_id, issummary; `SSCCSO_TYPE_OF_DOC_ISACTI_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCSO_TYPE_OF_DOC_ISSUMM_CHK`: ISSUMMARY IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Ssccso_Accounting_Concept` |
| `Ssccso_Cash_Inc_Exp` |
| `Ssccso_Type_Of_Document` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de la ventana 'Gestión de Ingresos y Egresos Caja', que permite a los usuarios acceder a las diferentes funciones del sistema para el cierre de caja. Dentro de esta ventana, los usuarios pueden interactuar con los diversos tableros y campos disponibles para gestionar los ingresos y egresos de manera eficiente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.closecash.sales.order.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Gestión de Ingresos y Egresos Caja | Management of cash income  and expenses |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Gestión de Ingresos y Egresos Caja | Management of cash income  and expenses | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.closecash.sales.order.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Gestión de Ingresos y Egresos Caja

- **AD_WINDOW_ID:** `5A7D89972F15448087C87E944CE94C71`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Management of cash income  and expenses | `BA28C493E1D9485687B347FBF46CA23C` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Management of cash income  and expenses (ventana: Gestión de Ingresos y Egresos Caja)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 30 | Document No. | `Documentno` | No | No | — |
| 40 | Type of operation | `Type_Of_Operation` | No | No | — |
| 50 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 60 | Date | `Dateactual` | No | No | — |
| 70 | Accounting date | `Accounting_Date` | No | No | — |
| 80 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 90 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 100 | G/L Item | `C_Glitem_ID` | No | No | — |
| 110 | Description | `Description` | No | No | — |
| 120 | Deposit amount | `Deposit_Amount` | No | No | — |
| 130 | Refund amount | `Refund_Amount` | No | No | — |
| 140 | Status | `Status` | No | Sí | — |
| 180 | Process | `Processed` | No | No | — |
| 190 | Financial account transaction | `FIN_Finacc_Transaction_ID` | No | Sí | — |
| 200 | Sccc_Cash_Clousure_ID | `Sccc_Cash_Clousure_ID` | No | Sí | — |

### Type Of Document

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |

### Accounting Concept

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | G/L Item | `C_Glitem_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

En el módulo existe un proceso principal que permite completar el cierre de caja mediante un único botón. Este proceso incluye la validación de campos ingresados y la comprobación de datos para asegurar que no haya inconsistencias antes de completar la operación. Aunque no se generan informes directamente desde el proceso, la funcionalidad se apoya en validaciones frecuentes que ayudan a mantener la calidad de los datos y el correcto funcionamiento del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.closecash.sales.order.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Procesar | Process | Ssccso_Process | `ssccso_process` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| Botón (PL/pgSQL) | Procesar | Process | Ssccso_Process | `ssccso_process` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Procesar | Process | PL `ssccso_process` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| `Ssccso_AmountLessThanZero` | Values less than zero are not allowed. | Values less than zero are not allowed. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo no incluye implementación de clases Java, lo que significa que se basa principalmente en la estructura y lógica proporcionada por los triggers y funciones PL/pgSQL para su funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.closecash.sales.order`.

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
| Trigger `SSCCSO_CASH_INC_EXP_TRG` | `ssccso_cash_inc_exp` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSCCSO_REMOVE_RELATIONS_TRG` | `sccc_cash_clousureline` | before INSERT/UPDATE/DELETE | Quita la relacion de ese cierre de caja y ese método de pago |
| AD_VAL_RULE | — | `FIN_Financial_Account_ID - CloseCash` | `EXISTS (SELECT 1 FROM sccc_setup st WHERE st.ad_org_id  = @AD_Org_ID@
AND st.fin_financial_account_id = fin_financial_ac` |
| AD_VAL_RULE | — | `C_Glitem_ID - CloseCash` | `EXISTS (SELECT 1 
FROM sccc_setup st 
JOIN ssccso_accounting_concept sac on sac.sccc_setup_id = st.sccc_setup_id
where s` |
| AD_VAL_RULE | — | `Ssccso_DocType - ssccso_cash_inc_exp` | `C_DocType.ad_table_id in ('BA28C493E1D9485687B347FBF46CA23C')` |
| Función PL `ssccso_loadlines` | — | invocación proceso | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; Consultar En ventana de ingresos y egresos de caja |
| Función PL `ssccso_record` | — | invocación proceso | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL/pgSQL son esenciales para el soporte del módulo, ya que permiten la ejecución automática de procesos y el manejo de relaciones entre tablas al realizar transacciones en la base de datos. Estos elementos contribuyen a la optimización del rendimiento y la seguridad de las operaciones de cierre de caja.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSCCSO_REMOVE_RELATIONS_TRG` | `sccc_cash_clousureline` | before | INSERT/UPDATE/DELETE | Quita la relacion de ese cierre de caja y ese método de pago | `model/triggers/SSCCSO_REMOVE_RELATIONS_TRG.xml` |
| `SSCCSO_CASH_INC_EXP_TRG` | `ssccso_cash_inc_exp` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSCCSO_CASH_INC_EXP_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssccso_loadlines` | — | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; Consultar En ventana de ingresos y egresos de caja | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; Consultar En ventana de ingresos y egresos de caja | `model/functions/SSCCSO_LOADLINES.xml` |
| `ssccso_process` | Procesar | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSCCSO_PROCESS.xml` |
| `ssccso_record` | — | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced | `model/functions/SSCCSO_RECORD.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Procesar | `Ssccso_Process` | Botón (PL/pgSQL) | PL `ssccso_process` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

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

Módulo: `ec.com.sidesoft.closecash.sales.order`.

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

# Glosario — prefijo `SSCCSO`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCCSO` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.closecash.sales.order` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Ssccso_Process` — Procesar

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Close Cash Report for Printing Process
**Package:** `ec.com.sidesoft.closecash.report.print`

# Module overview — Sidesoft Close Cash Report for Printing Process

## Functional

El módulo 'Sidesoft Close Cash Report for Printing Process' tiene como propósito facilitar la generación de informes de cierre de caja para su impresión, asegurando que los procesos de registro y reportes sean eficientes y precisos. Este módulo está dirigido a usuarios de negocio que necesiten acceder a reportes de cierre de caja, así como a desarrolladores y personal de soporte que requieran generar o modificar dichos reportes. Las dependencias del módulo incluyen 'Sidesoft Custom Close Cash' y otras relacionadas con la interfaz y el núcleo de Openbravo, asegurando su correcta operación dentro del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/closecash/report/print` |
| Web | `web/ec.com.sidesoft.closecash.report.print/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Sidesoft Custom Close Cash
- Sidesoft Custom Close Cash Advanced

### Version

**2.0.1** (from `AD_MODULE.xml`).

### DB prefix

`SSCCRPP`

# Guía de chat — Sidesoft Close Cash Report for Printing Process

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.closecash.report.print`).

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
- «¿Qué es la tabla ssccrpp_report_lines?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo generar un informe de cierre de caja?
- ¿Qué datos se incluyen en el reporte de cierre?
- ¿Cómo reviso los informes generados previamente?
- ¿Qué debo hacer si el informe no se genera correctamente?
- ¿Puedo personalizar el formato del informe de cierre?
- ¿Cómo se manejan los errores durante la generación del informe?
- ¿Hay opciones para imprimir directamente desde el reporte?
- ¿Dónde puedo encontrar la documentación de soporte para este módulo?

# Domain — data model

## Functional

El modelo de datos se centra principalmente en la entidad 'ssccrpp_report_lines', que representa las líneas de los informes de cierre de caja. Aunque no hay etapas intermedias explícitas, los datos fluyen a través de la generación del informe a partir de la información de los pagos y documentos relacionados. Los triggers no están presentes en este módulo, lo que implica que las acciones sobre la base de datos son manejadas principalmente a través de las funciones necesarias para la generación del informe.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssccrpp_report_lines` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssccrpp_report_lines` | ssccrpp_report_lines | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssccrpp_report_lines_pk`; Cols: client_name, doc_no, type_doc, paymentmethod, close_cash; `SSCCRPP_REPORT_LINES_ISACT`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssccrpp_report_lines` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_PAYMENTTERM`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de un único menú que permite acceder a las funcionalidades del reporte de cierre de caja. Aunque no se han definido ventanas específicas en la interfaz, la interacción del usuario se centra en ejecutar el proceso de impresión del informe.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.closecash.report.print.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Reporte Ingresos Cierre de Caja | Cash Closing Income | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.closecash.report.print.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `184`

- **AD_TAB_ID:** `184` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 180 | Upon Delivery | `EM_Ssccrpp_Upon_Delivery` | No | No | — |
| 190 | Payment Type | `EM_Ssccrpp_Paymenttype` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos disponibles en el módulo incluyen dos botones principales para completar y retornar el procesamiento de informes. Aunque no hay informes adicionales definidos, el módulo permite la generación de una vista de cierre de caja que es fundamental para los resultados financieros diarios. Las validaciones frecuentes pueden involucrar la validez de la información presentada en el informe, asegurando la precisión de los datos antes de la impresión.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.closecash.report.print.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Generate Report Close Cash | Generate Report Close Cash | generate_report_close_cash | `ssccrpp_report_close_cash` | v_C_BPartner_ID VARCHAR(32); --OBTG:VARCHAR2--; v_C_Currency_ID VARCHAR(32); --OBTG:VARCHAR2--; v_PaymentRule VARCHAR(60) ; --OBTG:VARCHAR2--; v_IsReceipt VARCHAR(1) ; --OBTG:VARCHAR2-- | — |
| Proceso / otro | Reporte Ingresos Cierre de Caja | Cash Closing Income | Cash Closing Income | *(OBUIAPP / manual)* | — | — |
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
| Botón (PL/pgSQL) | Generate Report Close Cash | Generate Report Close Cash | generate_report_close_cash | `ssccrpp_report_close_cash` | v_C_BPartner_ID VARCHAR(32); --OBTG:VARCHAR2--; v_C_Currency_ID VARCHAR(32); --OBTG:VARCHAR2--; v_PaymentRule VARCHAR(60) ; --OBTG:VARCHAR2--; v_IsReceipt VARCHAR(1) ; --OBTG:VARCHAR2-- | — |
| Proceso / otro | Reporte Ingresos Cierre de Caja | Cash Closing Income | Cash Closing Income | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Generate Report Close Cash | Generate Report Close Cash | PL `ssccrpp_report_close_cash` | v_C_BPartner_ID VARCHAR(32); --OBTG:VARCHAR2--; v_C_Currency_ID VARCHAR(32); --OBTG:VARCHAR2--; v_PaymentRule VARCHAR(60) ; --OBTG:VARCHAR2--; v_IsReceipt VARCHAR(1) ; --OBTG:VARCHAR2-- | v_C_BPartner_ID VARCHAR(32); --OBTG:VARCHAR2--; v_C_Currency_ID VARCHAR(32); --OBTG:VARCHAR2--; v_PaymentRule VARCHAR(60) ; --OBTG:VARCHAR2--; v_IsReceipt VARCHAR(1) ; --OBTG:VARCHAR2--; v_Description VARCHAR(60) ; --OBTG:VARCHAR2--; Eliminamos las lineas creadas anteriormente |
| Proceso / otro | Reporte Ingresos Cierre de Caja | Cash Closing Income | — | — | — |
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
**Total de reportes del módulo: 12**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **12**.

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

El módulo contiene clases Java que son responsables de manejar la generación del informe de cierre de caja. En particular, la clase 'CashClose' se encarga de la lógica necesaria para obtener y presentar los datos requeridos por el usuario a través de la interfaz web de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.closecash.report.print`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `CashClose` | ad_Reports | HttpSecureAppServlet | — | `src/ec/com/sidesoft/closecash/report/print/ad_Reports/CashClose.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `fin_paymentmethod payment` | `fin_paymentmethod_id in (select fin_paymentmethod_id from fin_payment group by 1)` |
| AD_VAL_RULE | — | `Org Payment` | `ad_org_id in (select ad_org_id from fin_payment group by 1)` |
| AD_VAL_RULE | — | `User Logged` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| Función PL `ssccrpp_report_close_cash` | — | invocación proceso | v_C_BPartner_ID VARCHAR(32); --OBTG:VARCHAR2--; v_C_Currency_ID VARCHAR(32); --OBTG:VARCHAR2--; v_PaymentRule VARCHAR(60) ; --OBTG:VARCHAR2-- |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

En el ámbito de la base de datos, el módulo cuenta con una función PL que se utiliza para las operaciones de generación del informe. Esta función desempeña un papel crítico, ya que se encarga de recoger y procesar la información necesaria desde la tabla 'ssccrpp_report_lines', garantizando que los datos sean coherentes y estén disponibles para los usuarios finales.

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
| `ssccrpp_report_close_cash` | Generate Report Close Cash | v_C_BPartner_ID VARCHAR(32); --OBTG:VARCHAR2--; v_C_Currency_ID VARCHAR(32); --OBTG:VARCHAR2--; v_PaymentRule VARCHAR(60) ; --OBTG:VARCHAR2--; v_IsReceipt VARCHAR(1) ; --OBTG:VARCHAR2-- | v_C_BPartner_ID VARCHAR(32); --OBTG:VARCHAR2--; v_C_Currency_ID VARCHAR(32); --OBTG:VARCHAR2--; v_PaymentRule VARCHAR(60) ; --OBTG:VARCHAR2--; v_IsReceipt VARCHAR(1) ; --OBTG:VARCHAR2--; v_Description VARCHAR(60) ; --OBTG:VARCHAR2--; Eliminamos las lineas creadas anteriormente | `model/functions/SSCCRPP_REPORT_CLOSE_CASH.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Generate Report Close Cash | `generate_report_close_cash` | Botón (PL/pgSQL) | PL `ssccrpp_report_close_cash` | N | v_C_BPartner_ID VARCHAR(32); --OBTG:VARCHAR2--; v_C_Currency_ID VARCHAR(32); --OBTG:VARCHAR2--; v_PaymentRule VARCHAR(60) ; --OBTG:VARCHAR2--; v_IsReceipt VARCHAR(1) ; --OBTG:VARCH |

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

Módulo: `ec.com.sidesoft.closecash.report.print`.

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

# Glosario — prefijo `SSCCRPP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCCRPP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.closecash.report.print` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `generate_report_close_cash` — Generate Report Close Cash
- `Cash Closing Income` — Reporte Ingresos Cierre de Caja

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Custom Close Cash for Indumot
**Package:** `ec.com.sidesoft.closecash.indumot`

# Module overview — Sidesoft Custom Close Cash for Indumot

## Functional

El módulo 'Sidesoft Custom Close Cash for Indumot' está diseñado para facilitar el cierre de caja en organizaciones específicas dentro de Openbravo ERP. Su principal propósito es permitir que los usuarios de negocio realicen cierres de caja de manera eficiente, mientras que el soporte técnico y los desarrolladores pueden asegurarse de que el módulo funcione correctamente conforme a las necesidades operativas del usuario. Este módulo incluye funcionalidades que se conectan con las funcionalidades básicas de Openbravo, creando una sinergia con otros módulos y procesos del sistema. Las dependencias de este módulo incluyen la compatibilidad con la interfaz '2.50 to 3.00 Compatibility Skin', el núcleo de Openbravo y el framework 3.0 de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/closecash/indumot` |
| Web | `web/ec.com.sidesoft.closecash.indumot/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSCCCIN`

# Guía de chat — Sidesoft Custom Close Cash for Indumot

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.closecash.indumot`).

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
- «¿Qué es la tabla sscccin_invoice_doctype?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo realizar un cierre de caja?
- ¿Qué sucede si olvido cerrar una caja al final del día?
- ¿Cómo puedo verificar si el cierre de caja se realizó correctamente?
- ¿Qué pasos seguir para corregir un cierre de caja erróneo?
- ¿Puedo ver un resumen de todos los cierres de caja realizados?
- ¿Cómo se gestionan las transacciones fallidas durante un cierre de caja?
- ¿Existen restricciones al cerrar caja en diferentes organizaciones?
- ¿Qué datos se requieren para completar el cierre de caja?

# Domain — data model

## Functional

El modelo de datos del módulo incluye una tabla principal, 'SCCC_CASH_CLOUSURE', que almacena la información del cierre de caja, junto con varias tablas relacionadas como 'SCCC_CASH_CLOUSURELINE', 'FIN_FINACC_TRANSACTION' y 'FIN_PAYMENT'. Estas tablas están interrelacionadas, lo que permite capturar transacciones financieras y los detalles de los pagos asociados a cada cierre. Los triggers implementados son fundamentales para mantener la integridad de los datos, entre ellos, 'SSCCCIN_CASH_CLOUSURE_TRG' y 'SSCCCIN_PAYMENTDETAILED_TRG', que realizan validaciones y actualizaciones automáticas en la base de datos cada vez que se altera algún registro de cierre de caja o transacción financiera.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sscccin_invoice_doctype` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sscccin_invoice_doctype` | sscccin_invoice_doctype | — | — | ad_client_id→ad_client; c_doctype_credit_notes_id→c_doctype; c_doctype_reversed_id→c_doctype; c_doctype_sales_id→c_doctype; ad_org_id→ad_org (+1) | Detalle enlazado a ad_client, c_doctype. | PK `sscccin_idt_key`; Cols: sccc_setup_id, c_doctype_sales_id, c_doctype_credit_notes_id, c_doctype_reversed_id; `SSCCCIN_IDT_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sscccin_invoice_doctype` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_INVOICE`, `FIN_FINACC_TRANSACTION`, `FIN_PAYMENT`, `SCCC_CASH_CLOUSURE`, `SCCC_CASH_CLOUSURELINE`, `SCCC_PAYMENT_METHOD`, `SCCC_SETUP`, `SSCRCC_PAYMENT_DETAILED`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no cuenta con ventanas específicas visibles en la UI, lo que implica que se debe interactuar con él a través de otros componentes de Openbravo o mediante interfaces personalizadas diseñadas para el flujo de trabajo del cierre de caja. Esto puede incluir botones integrados en formularios o paneles de control donde los usuarios pueden gestionar y ejecutar el cierre de caja.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.closecash.indumot.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.closecash.indumot.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Document Type Invoice

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 100 | Sales Document Type | `C_Doctype_Sales_ID` | No | No | — |
| 110 | Type of Document Credit Note | `C_Doctype_Credit_Notes_ID` | No | No | — |
| 120 | Cancellation Document Type | `C_Doctype_Reversed_ID` | No | No | — |

### Pestaña `23691259D1BD4496BCC5F32645BCA4B9`

- **AD_TAB_ID:** `23691259D1BD4496BCC5F32645BCA4B9` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 72 | Reference Nº | `EM_Sscccin_Reference` | No | No | — |

### Pestaña `3EC5BA28381C413390A9B3CEA3190B56`

- **AD_TAB_ID:** `3EC5BA28381C413390A9B3CEA3190B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 35 | Deposit Nº | `EM_Sscccin_Deposit` | No | No | — |

### Pestaña `4C1E84A848B94837A743BB709807008A`

- **AD_TAB_ID:** `4C1E84A848B94837A743BB709807008A` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 35 | Deposit Nº | `EM_Sscccin_Deposit` | No | No | — |

### Pestaña `60B6BA2648A3480CAECCB2F17471B5C5`

- **AD_TAB_ID:** `60B6BA2648A3480CAECCB2F17471B5C5` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 35 | Deposit Nº | `EM_Sscccin_Deposit` | No | No | — |

### Pestaña `6D42753DD50B4A56927A399B16B8D31B`

- **AD_TAB_ID:** `6D42753DD50B4A56927A399B16B8D31B` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 141 | em_sscccin_valdeposit | `em_sscccin_valdeposit` | No | No | — |
| 142 | em_sscccin_valfinacc | `em_sscccin_valfinacc` | No | No | — |
| 150 | Difference | `EM_Sscccin_Difference` | No | No | — |

### Pestaña `AF29F97DC5CB4FC2B3CD90672FCC8C03`

- **AD_TAB_ID:** `AF29F97DC5CB4FC2B3CD90672FCC8C03` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 120 | Maximum Difference | `EM_Sscccin_Maximumdifference` | No | No | — |
| 130 | Not allow close cash in zero | `EM_Sscccin_Not_Closecash_Zero` | No | No | — |

### Pestaña `D2581973C5984F8785653C9D763B70C6`

- **AD_TAB_ID:** `D2581973C5984F8785653C9D763B70C6` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 35 | Deposit Nº | `EM_Sscccin_Deposit` | No | No | — |

### Pestaña `E8A4F14D7FD94D678CCE89B1A1C52F09`

- **AD_TAB_ID:** `E8A4F14D7FD94D678CCE89B1A1C52F09` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| — | Toggle Document Status | `EM_Sscccin_Toggledocstatus` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo ofrece varios botones para operaciones típicas que incluyen completar, retornar y rechazar cierres de caja. Aunque no se listan informes específicos, se anticipa que los usuarios pueden realizar consultas basadas en los procesos de cierre de caja que se gestionan en el sistema. Es crucial que las validaciones estén en su lugar para evitar errores en transacciones, especialmente al crear o ajustar cierres de caja, donde los triggers juegan un papel clave al asegurar que los datos se procesen correctamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.closecash.indumot.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Alternar Estado de Documento | Toggle Document Status | SscccinToggleDocstatus | `sscccin_toggledocstatus` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Cargar Lineas Cierre de Caja | Load Lines | SscccinLoadLines | `sscccin_loadlines` | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configu… | — |
| Botón (PL/pgSQL) | Procesar Cierre de Caja | Process | SscccinProcess | `sscccin_process` | Sscccin_DocumentTypesUnconfiguredForInvoices; Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; Fin Validación checks validar deposito y validar cuenta financiera… | — |
| Botón (PL/pgSQL) | Registrar Cierre de Caja | Record | SscccinRecord | `sscccin_record` | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configu… | — |
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
| Botón (PL/pgSQL) | Alternar Estado de Documento | Toggle Document Status | SscccinToggleDocstatus | `sscccin_toggledocstatus` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Cargar Lineas Cierre de Caja | Load Lines | SscccinLoadLines | `sscccin_loadlines` | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configu… | — |
| Botón (PL/pgSQL) | Procesar Cierre de Caja | Process | SscccinProcess | `sscccin_process` | Sscccin_DocumentTypesUnconfiguredForInvoices; Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; Fin Validación checks validar deposito y validar cuenta financiera… | — |
| Botón (PL/pgSQL) | Registrar Cierre de Caja | Record | SscccinRecord | `sscccin_record` | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configu… | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Alternar Estado de Documento | Toggle Document Status | PL `sscccin_toggledocstatus` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Cargar Lineas Cierre de Caja | Load Lines | PL `sscccin_loadlines` | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configu… | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configurados; Validar si existe ec.com.sidesoft.custom.closecash.advanced; Actualilizamos el estado al cargar las lineas |
| Botón (PL/pgSQL) | Procesar Cierre de Caja | Process | PL `sscccin_process` | Sscccin_DocumentTypesUnconfiguredForInvoices; Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; Fin Validación checks validar deposito y validar cuenta financiera… | Sscccin_DocumentTypesUnconfiguredForInvoices; Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; Fin Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configurados |
| Botón (PL/pgSQL) | Registrar Cierre de Caja | Record | PL `sscccin_record` | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configu… | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configurados; Precargar tipos de documentos para facturas; Precargar tipos de documentos para notas de crédito |
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
| `SSCCCIN_ReferenceNumberRequired` | Reference Number Required | Reference Number Required | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sscccin_OnlyOneCashClosure` | Only 1 box closure per day is allowed | Only 1 box closure per day is allowed | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sscccin_ProCashClose` | It is not allowed to process a Cash Closing with a processing date less than the Closing Date. | It is not allowed to process a Cash Closing with a processing date less than the Closing Date. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sscccin_DocumentTypesUnconfiguredForInvoices` | Document types for unconfigured invoices | Document types for unconfigured invoices | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sscccin_DocumentTypesUnconfigured` | Document types not configured | Document types not configured | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSCCCIN_RepeatedReference` | The reference number has already been used in the selected financial account | The reference number has already been used in the selected financial account | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSCCCIN_PaymentDetailedBlock` | Processed Cash Closing. Operation not allowed. | Processed Cash Closing. Operation not allowed. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sscccin_PaymentMethodsNotConfigured` | Payment methods not configured | Payment methods not configured | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El rol de Java en este módulo se manifiesta principalmente a través de dos clases que proporcionan funcionalidades adicionales a la experiencia del usuario en Openbravo, gestionando interacciones específicas como actualizaciones de referencia de acuerdo a las transacciones registradas. Estas clases permiten una flexibilidad adicional en la gestión del cierre de caja y su integración con otras áreas del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.closecash.indumot`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SscccinComponentProvider` | root | BaseComponentProvider | ComponentProvider / UI | `src/ec/com/sidesoft/closecash/indumot/SscccinComponentProvider.java` |
| `UpdateReferenceActionHandler` | ad_actions | BaseActionHandler | — | `src/ec/com/sidesoft/closecash/indumot/ad_actions/UpdateReferenceActionHandler.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSCCCIN_CASH_CLOUSURE_TRG` | `sccc_cash_clousure` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSCCCIN_CASH_CLOUSURE_TRG1` | `sccc_cash_clousure` | before UPDATE | Verifica si los disparadores están deshabilitados; Devolver el registro correspondiente según la operación |
| Trigger `SSCCCIN_CASH_DELET_TRG` | `sccc_cash_clousure` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSCCCIN_PAYMENTDETAILED_TRG` | `sscrcc_payment_detailed` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSCCCIN_RECONCILED_BF_TRG` | `fin_finacc_transaction` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSCCCIN_RECONCILED_TRG` | `fin_finacc_transaction` | after UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSCCCIN_REFERENCE_TRG` | `fin_payment` | after INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `SscccinDoctypeSales` | `C_DocType.DocBaseType IN ('ARI')
AND C_DocType.AD_Table_ID IN (SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(TABLENAME)='` |
| AD_VAL_RULE | — | `SscccinDoctypeCreditNotes` | `C_DocType.DocBaseType IN ('ARC','ARI_RM')
AND C_DocType.AD_Table_ID IN (SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(TAB` |
| AD_VAL_RULE | — | `SsccinDoctypeReversed` | `C_DocType.DocBaseType IN ('ARI')
AND C_DocType.AD_Table_ID IN (SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(TABLENAME)='` |
| Función PL `sscccin_loadlines` | — | invocación proceso | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados |
| Función PL `sscccin_process` | — | invocación proceso | Sscccin_DocumentTypesUnconfiguredForInvoices; Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; Fin Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja |
| Función PL `sscccin_record` | — | invocación proceso | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL/pgSQL son esenciales en este módulo, ya que garantizan que la lógica de negocio se ejecute adecuadamente a nivel de base de datos. Con siete triggers activos, como 'SSCCCIN_RECONCILED_BF_TRG' y 'SSCCCIN_REFERENCE_TRG', se aseguran de que los datos se mantengan consistentes y de que se tomen las acciones correctas en respuesta a cambios en la base de datos, facilitando así el mantenimiento y la recuperación de información crítica por parte del equipo de soporte.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSCCCIN_RECONCILED_BF_TRG` | `fin_finacc_transaction` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSCCCIN_RECONCILED_BF_TRG.xml` |
| `SSCCCIN_RECONCILED_TRG` | `fin_finacc_transaction` | after | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSCCCIN_RECONCILED_TRG.xml` |
| `SSCCCIN_REFERENCE_TRG` | `fin_payment` | after | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSCCCIN_REFERENCE_TRG.xml` |
| `SSCCCIN_CASH_CLOUSURE_TRG` | `sccc_cash_clousure` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSCCCIN_CASH_CLOUSURE_TRG.xml` |
| `SSCCCIN_CASH_CLOUSURE_TRG1` | `sccc_cash_clousure` | before | UPDATE | Verifica si los disparadores están deshabilitados; Devolver el registro correspondiente según la operación | `model/triggers/SSCCCIN_CASH_CLOUSURE_TRG1.xml` |
| `SSCCCIN_CASH_DELET_TRG` | `sccc_cash_clousure` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSCCCIN_CASH_DELET_TRG.xml` |
| `SSCCCIN_PAYMENTDETAILED_TRG` | `sscrcc_payment_detailed` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSCCCIN_PAYMENTDETAILED_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sscccin_loadlines` | Cargar Lineas Cierre de Caja | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configu… | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configurados; Validar si existe ec.com.sidesoft.custom.closecash.advanced; Actualilizamos el estado al cargar las lineas | `model/functions/SSCCCIN_LOADLINES.xml` |
| `sscccin_process` | Procesar Cierre de Caja | Sscccin_DocumentTypesUnconfiguredForInvoices; Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; Fin Validación checks validar deposito y validar cuenta financiera… | Sscccin_DocumentTypesUnconfiguredForInvoices; Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; Fin Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configurados | `model/functions/SSCCCIN_PROCESS.xml` |
| `sscccin_pymt_schedule_control` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSCCCIN_PYMT_SCHEDULE_CONTROL.xml` |
| `sscccin_record` | Registrar Cierre de Caja | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configu… | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de documentos para facturas esten configurados; Precargar tipos de documentos para facturas; Precargar tipos de documentos para notas de crédito | `model/functions/SSCCCIN_RECORD.xml` |
| `sscccin_toggledocstatus` | Alternar Estado de Documento | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSCCCIN_TOGGLEDOCSTATUS.xml` |
| `sscccin_update_reference` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSCCCIN_UPDATE_REFERENCE.xml` |
| `sscccin_validar_anticipos` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSCCCIN_VALIDAR_ANTICIPOS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alternar Estado de Documento | `SscccinToggleDocstatus` | Botón (PL/pgSQL) | PL `sscccin_toggledocstatus` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 2 | Cargar Lineas Cierre de Caja | `SscccinLoadLines` | Botón (PL/pgSQL) | PL `sscccin_loadlines` | N | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de |
| 3 | Procesar Cierre de Caja | `SscccinProcess` | Botón (PL/pgSQL) | PL `sscccin_process` | N | Sscccin_DocumentTypesUnconfiguredForInvoices; Validación checks validar deposito y validar cuenta financiera de la ventana configuracion cierre de caja; Fin Validación checks valid |
| 4 | Registrar Cierre de Caja | `SscccinRecord` | Botón (PL/pgSQL) | PL `sscccin_record` | N | Sscccin_DocumentTypesUnconfiguredForInvoices; Validar que los metodos de cobros esten configurados; Validar que los tipos de documentos esten configurados; Validar que los tipos de |

**Total acciones documentadas (extract):** **4** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/ec.com.sidesoft.closecash.indumot/js/updateReference.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.closecash.indumot`.

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

# Glosario — prefijo `SSCCCIN`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCCCIN` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.closecash.indumot` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `SscccinToggleDocstatus` — Alternar Estado de Documento
- `SscccinLoadLines` — Cargar Lineas Cierre de Caja
- `SscccinProcess` — Procesar Cierre de Caja
- `SscccinRecord` — Registrar Cierre de Caja

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Credit Card Reconciliation Close Cash
**Package:** `ec.com.sidesoft.creditcard.closecash`

# Module overview — Sidesoft Credit Card Reconciliation Close Cash

## Functional

El módulo de Sidesoft Credit Card Reconciliation Close Cash permite a los usuarios gestionar el proceso de conciliación de pagos realizados a través de tarjetas de crédito. Los actores principales incluyen los usuarios de negocio que realizan conciliaciones, así como el equipo de soporte que proporciona asistencia. El alcance del módulo se limita a la conciliación de pagos y su cierre, interfiriendo con métodos de pago y detalles de conciliación. Las dependencias incluyen compatibilidad con la skin de versiones anteriores y otro módulo de cierre de efectivo avanzado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/creditcard/closecash` |
| Web | `web/ec.com.sidesoft.creditcard.closecash/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Sidesoft Custom Close Cash Advanced

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSCRCC`

# Guía de chat — Sidesoft Credit Card Reconciliation Close Cash

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.creditcard.closecash`).

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
- «¿Qué es la tabla sscrcc_payment_detailed?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo conciliar un pago con tarjeta de crédito?
- ¿Qué pasos sigo para cerrar el efectivo relacionado con los pagos?
- ¿Existen informes disponibles sobre la conciliación de pagos?
- ¿Qué debo hacer si un pago no concilia correctamente?
- ¿Cómo modifico un método de pago en el sistema?
- ¿Puedo recibir soporte si tengo problemas con la conciliación?
- ¿Cómo se validan los datos de los pagos registrados?
- ¿Hay algún requerimiento específico para instalar el módulo?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad cabecera 'sscrcc_payment_detailed', que almacena la información detallada de los pagos procesados. Esta entidad está diseñada para mantener registros de las transacciones realizadas, favoreciendo un seguimiento detallado del flujo de caja. A pesar de que no se indican triggers, la existencia de funciones PL en el módulo asegura la automatización de procesos clave en la conciliación y gestión de pagos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sscrcc_payment_detailed` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sscrcc_payment_detailed` | Sscrcc_Payment_Detailed | — | — | ad_client_id→ad_client; sccc_cash_clousureline_id→sccc_cash_clousureline; fin_financial_account_id→fin_financial_account; fin_paymentmethod_id→fin_paymentmethod; ad_org_id→ad_org | Detalle enlazado a ad_client, fin_financial_account, sccc_cash_clousureline. | PK `sscrcc_payment_detailed_key`; Cols: description, line, fin_paymentmethod_id, fin_financial_account_id, amount; `SSCRCC_PAYM_DET_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCRCC_PAYM_DET_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Sscrcc_Payment_Detailed` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`SCCC_PAYMENT_METHOD`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

No hay ventanas específicas definidas para este módulo, lo que sugiere que la navegación puede realizarse a través de menús o enlaces existentes relacionados con conciliación de pagos. Los usuarios probablemente acceden a las funciones mediante desplegables en el ERP, donde podrán seleccionar la opción de conciliación de tarjeta de crédito.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.creditcard.closecash.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.creditcard.closecash.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Payment Detail

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `Line` | No | Sí | — |
| 30 | Amount | `Amount` | No | No | — |
| 40 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Pestaña `6D42753DD50B4A56927A399B16B8D31B`

- **AD_TAB_ID:** `6D42753DD50B4A56927A399B16B8D31B` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 140 | Detailed | `EM_Sscrcc_Detailed` | No | No | — |

### Payment Detail

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Line No. | `Line` | No | Sí | — |
| 30 | Amount | `Amount` | No | No | — |
| 40 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 40 | Description | `Description` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo no incluye botones procesales específicos como completar o rechazar, lo que indica que las funciones pueden ser ejecutadas a través de acciones directas en la interfaz. Sin informes dedicados, los usuarios dependerán de las vistas estándar del ERP para validar los datos de pagos. Las validaciones frecuentes pueden incluir la verificación de la coherencia entre las transacciones registradas y los registros de pago.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.creditcard.closecash.es_ES/referencedata/translation/`.

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

No se han identificado clases Java en este módulo, lo que sugiere que todas las funcionalidades están implementadas mediante funcionalidades PL y configuraciones estándar del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.creditcard.closecash`.

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
| Función PL `sscrcc_clousureprocess` | — | invocación proceso | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN; Insertar en la cuenta financiera de manera detallada.(Si existen lineas) |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El módulo integra funciones PL que permiten la manipulación y validación de datos en la base de datos, siendo esencial para el soporte continuo y la resolución de problemas. Los roles de estas funciones son críticos para mantener la integridad de los datos y optimizar el rendimiento en la conciliación de pagos.

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
| `sscrcc_clousureprocess` | — | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN; Insertar en la cuenta financiera de manera detallada.(Si existen lineas) | COMPROBAR EXISTENCIA MÓDULO ec.com.sidesoft.custom.closecash.advanced; CONTROL EXISTENCIA DE MÉTODO DE PAGO EN CONFIGURACIÓN; Insertar en la cuenta financiera de manera detallada.(Si existen lineas) | `model/functions/SSCRCC_CLOUSUREPROCESS.xml` |
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

Módulo: `ec.com.sidesoft.creditcard.closecash`.

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

# Glosario — prefijo `SSCRCC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCRCC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.creditcard.closecash` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Credit Card Reconciliation
**Package:** `ec.com.sidesoft.creditcard.reconciliation`

# Module overview — Sidesoft Credit Card Reconciliation

## Functional

El módulo Sidesoft Credit Card Reconciliation está diseñado para ayudar a las empresas a mantener un control eficiente sobre las transacciones realizadas con tarjetas de crédito. Este módulo es utilizado principalmente por el personal de tesorería y contabilidad, permitiendo una reconciliación precisa de los movimientos bancarios relacionados con tarjetas de crédito. El alcance incluye la integración con diversos puntos de venta y la configuración de métodos de pago. Dependencias importantes incluyen el Openbravo 3.0 Framework y otros módulos personalizados de Sidesoft.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/creditcard/reconciliation` |
| Web | `web/ec.com.sidesoft.creditcard.reconciliation/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Openbravo 3.0 Framework
- Sidesoft Custom Close Cash Advanced
- Sidesoft Custom Close Cash for Indumot

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSCCR`

# Guía de chat — Sidesoft Credit Card Reconciliation

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.creditcard.reconciliation`).

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
- «¿Qué es la tabla ssccr_pos_card_rec_line?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo reconciliar una transacción de tarjeta de crédito?
- ¿Qué debo hacer si no puedo eliminar una transacción procesada?
- ¿Dónde puedo configurar los tipos de tarjeta?
- ¿Cómo puedo acceder al historial de transacciones?
- ¿Qué pasos debo seguir para agregar un nuevo método de pago?
- ¿Es posible revertir una conciliación realizada?
- ¿Cómo se validan las transacciones antes de completar la reconciliación?
- ¿Qué significan los diferentes estados de las transacciones en la lista de conciliación?

# Domain — data model

## Functional

En el centro del modelo de datos se encuentra la tabla 'ssccr_pos_card_rec_line', que almacena las líneas de transacciones de las tarjetas. Este módulo interactúa con varias tablas clave, tales como 'FIN_FINACC_TRANSACTION' y 'FIN_FINANCIAL_ACCOUNT', las cuales están modificadas para adaptarse a las necesidades del módulo. Dos triggers importantes incluyen 'SSCCR_PROCESSED_TRG', que previene la eliminación de transacciones procesadas, y 'SSCCR_UPDATE_LINES_TRG', que realiza actualizaciones en las líneas de transacciones consolidadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssccr_cardmatchingconf` |
| `ssccr_cardmatchingconfline` |
| `ssccr_cards_types` |
| `ssccr_general_setting` |
| `ssccr_pos_card_rec` |
| `ssccr_pos_card_rec_line` |
| `ssccr_pos_card_rec_sum` |
| `ssccr_processor_banck` |
| `ssccr_types_of_credit` |
| `ssccr_withholdings` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssccr_cardmatchingconf` | Ssccr_CardMatchingConf | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ssccr_processor_banck_id→ssccr_processor_banck | Detalle enlazado a ad_client, ad_org, ssccr_processor_banck. | PK `ssccr_cardmconf_key`; Cols: ssccr_processor_banck_id, issummary; `SSCCR_CARDMCONF_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_CARDMCONF_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') |
| `ssccr_cardmatchingconfline` | Ssccr_CardMatchingConfLine | — | — | ssccr_cardmatchingconf_id→ssccr_cardmatchingconf; ad_client_id→ad_client; ad_org_id→ad_org; c_paymentterm_id→c_paymentterm; ssccr_cards_types_id→ssccr_cards_types (+1) | Detalle enlazado a ad_client, ad_org, ssccr_cardmatchingconf. | PK `ssccr_cardmconfl_key`; Cols: ssccr_cards_types_id, ssccr_cardmatchingconf_id, income_withholding, withholding_tax, ssccr_types_of_credit_id; `SSCCR_CARDMCONFL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_CARDMCONFL_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') |
| `ssccr_cards_types` | Ssccr_Cards_Types | — | `SSCCR_CARDSTYPES_VALUE` (ad_client_id, value) | ad_client_id→ad_client; ad_org_id→ad_org; ssccr_processor_banck_id→ssccr_processor_banck | Detalle enlazado a ad_client, ad_org, ssccr_processor_banck. | PK `ssccr_cardstypes_key`; Cols: value, name, description, issummary, ssccr_processor_banck_id; `SSCCR_CARDSTYPES_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_CARDSTYPES_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') |
| `ssccr_general_setting` | Ssccr_General_Setting | — | `SSCCR_GS_VALUE` (ad_client_id, fin_financial_account_id) | ad_client_id→ad_client; ad_org_id→ad_org; fin_financial_account_id→fin_financial_account | Parametrización / catálogo de soporte. | PK `ssccr_gs_key`; Cols: fin_financial_account_id, issummary, agrup; `SSCCR_GS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_GS_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') |
| `ssccr_pos_card_rec` | Ssccr_Pos_Card_Rec | — | `SSCCR_DOCUMENTNO` (documentno) | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype; fin_financial_account_from_id→fin_financial_account; fin_financial_account_to_id→fin_financial_account | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `ssccr_poscardrec_key`; Cols: c_doctype_id, documentno, fin_financial_account_from_id, fin_financial_account_to_id, start_date; `SSCCR_POSCARDREC_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_POSCARDREC_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') (+1) |
| `ssccr_pos_card_rec_line` | Ssccr_Pos_Card_Rec_Line | `SSCCR_PROCESSED_TRG` | — | group_id→fin_finacc_transaction; ad_client_id→ad_client; ad_org_id→ad_org; c_invoice_id→c_invoice; c_order_id→c_order (+6) | Detalle enlazado a ad_client, ad_org, fin_finacc_transaction. Validado por trigger(s): SSCCR_PROCESSED_TRG. | PK `ssccr_poscardline_key`; Cols: c_invoice_id, c_order_id, recap, lot, amount; `SSCCR_POSCARDLINE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_POSCARDLINE_ISSUMM_CHK`: ISSUMMARY IN ('Y', 'N') |
| `ssccr_pos_card_rec_sum` | Ssccr_Pos_Card_Rec_Sum | `SSCCR_UPDATE_LINES_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; ssccr_pos_card_rec_id→ssccr_pos_card_rec; ssccr_processor_banck_id→ssccr_processor_banck | Detalle enlazado a ad_client, ad_org, ssccr_pos_card_rec. Validado por trigger(s): SSCCR_UPDATE_LINES_TRG. | PK `ssccr_poscardsum_key`; Cols: ssccr_pos_card_rec_id, lot, amount, deposit_amount, type; `SSCCR_POSCARDSUM_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_POSCARDSUM_ISSUMM_CHK`: ISSUMMARY IN ('Y', 'N') |
| `ssccr_processor_banck` | Ssccr_Processor_Banck | — | `SSCCR_PRCSSBANCK_VALUE` (ad_client_id, value) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssccr_prcssbanck_key`; Cols: value, name, description, issummary; `SSCCR_PRCSSBANCK_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_PRCSSBANCK_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') |
| `ssccr_types_of_credit` | Ssccr_Types_Of_Credit | — | `SSCCR_TYPESCREDIT_VALUE` (ad_client_id, value) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssccr_typescredit_key`; Cols: value, name, description, issummary; `SSCCR_TYPESCREDIT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_TYPESCREDT_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') |
| `ssccr_withholdings` | Ssccr_Withholdings | — | — | ssccr_cardmatchingconf_id→ssccr_cardmatchingconf; ssccr_cardmatchingconfline_id→ssccr_cardmatchingconfline; ad_client_id→ad_client; ad_org_id→ad_org; c_glitem_id→c_glitem | Detalle enlazado a ad_client, ssccr_cardmatchingconf, ssccr_cardmatchingconfline. | PK `ssccr_withhold_key`; Cols: type, porcentage, c_glitem_id, ssccr_cardmatchingconf_id, isreconciled; `SSCCR_WITHHOLD_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSCCR_WITHHOLD_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') (+1) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssccr_card_rec_detail_v` |
| `ssccr_card_rec_summary_v` |
| `Ssccr_CardMatchingConf` |
| `Ssccr_CardMatchingConfLine` |
| `Ssccr_Cards_Types` |
| `Ssccr_Finacc_Trans` |
| `Ssccr_Finacc_Trans_V` |
| `Ssccr_General_Setting` |
| `Ssccr_Pos_Card_Rec` |
| `Ssccr_Pos_Card_Rec_Line` |
| `Ssccr_Pos_Card_Rec_Sum` |
| `Ssccr_Processor_Banck` |
| `Ssccr_Types_Of_Credit` |
| `Ssccr_Withholdings` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_TAX`, `FIN_FINACC_TRANSACTION`, `FIN_FINANCIAL_ACCOUNT`

### Views

`SSCCR_CARD_REC_DETAIL_V`, `SSCCR_CARD_REC_SUMMARY_V`, `SSCCR_FINACC_TRANS_V`

# Functional — windows and menus

## Functional

El módulo se navega a través de varias ventanas en la interfaz de usuario, incluyendo 'Banco Procesador' y 'Conciliación de Tarjetas POS'. Desde estas ventanas, los usuarios pueden acceder a diferentes funcionalidades de configuración y reconciliación, permitiendo una fácil visualización y administración de las transacciones con tarjetas de crédito.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.creditcard.reconciliation.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Banco Procesador | Processor Banck |
| Conciliación de Tarjetas POS | POS Card Reconciliation |
| Configuración conciliación de tarjetas | Card matching configuration |
| Configuración General | General Configuration |
| Finnancial Transaction POS | Finnancial Transaction POS |
| Tipos de Crédito | Types of credit |
| Tipos de Tarjeta | Cards types |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Banco Procesador | Processor Banck | No |
| Conciliación de Tarjetas | Creditcard Reconciliation | Sí |
| Conciliación de Tarjetas POS | POS Card Reconciliation | No |
| Configuración | Setup | Sí |
| Configuración conciliación de tarjetas | Card matching configuration | No |
| Configuración General | General Configuration | No |
| Herramientas de análisis | Analysis Tools | Sí |
| Tipos de Crédito | Types of credit | No |
| Tipos de Tarjeta | Cards types | No |
| Transacciones | Transactions | Sí |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.creditcard.reconciliation.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Banco Procesador

- **AD_WINDOW_ID:** `1FD0EB8CE6A14C039219A58E6E4F90D4`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Processor Banck | `923A2FB1CEE149C0B305AC5862ECD1BF` | 0 |

### Ventana: Conciliación de Tarjetas POS

- **AD_WINDOW_ID:** `8A82EB0025234AF8BDAA6D8C095BC7DB`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | POS Card Reconciliation | `D3AC9D0A1FFE40239A2ACF8AF86200CD` | 0 |
| 20 | Line | `2AECC7AD1C18470BA065D373313F98CD` | 1 |
| 30 | Summary | `C9C5274618484C25A6DA233C58CD5B23` | 1 |

### Ventana: Configuración conciliación de tarjetas

- **AD_WINDOW_ID:** `F224FD58E5C34C6FB1CDFF3C360EEF1E`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Card  matching configuration | `C8C9BB1B26424069A93B817E0425CA67` | 0 |
| 20 | Lines | `3DEC63CBD94D4F38B38C6D0DAFFAD028` | 1 |
| 30 | Withholdings | `2690CFE2251D4EAD935956871BC63538` | 2 |

### Ventana: Configuración General

- **AD_WINDOW_ID:** `912034ECDC1D4CFEB2F1F49AFFD1A6F7`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | General Configuration | `80FF96B2F3314BEBB7BBFF2A33CF2496` | 0 |

### Ventana: Finnancial Transaction POS

- **AD_WINDOW_ID:** `002722B2A1104415B425F16F4703C0E3`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Finnancial Transaction POS | `65C7190151DA4722896331211DD8440A` | 0 |

### Ventana: Tipos de Crédito

- **AD_WINDOW_ID:** `4D3F023BBBF9440B8529E8C432E1D600`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Types of credit | `7003A1C86EC8449E9712E3E7A23993DC` | 0 |

### Ventana: Tipos de Tarjeta

- **AD_WINDOW_ID:** `79B8280CB9304AF89EE49015FF322B86`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Cards types | `0D01760FFF7A4BA8AD173BBD84CB74AE` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Processor Banck (ventana: Banco Procesador)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Search Key | `Value` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |

### POS Card Reconciliation (ventana: Conciliación de Tarjetas POS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 30 | Document No. | `Documentno` | No | No | — |
| 40 | Date Payment | `Date_Payment` | No | No | — |
| 50 | Account From | `FIN_Financial_Account_From_ID` | No | No | — |
| 60 | Account To | `FIN_Financial_Account_To_ID` | No | No | — |
| 70 | Start Date | `Start_Date` | No | No | — |
| 80 | END_Date | `END_Date` | No | No | — |
| 90 | Description | `Description` | No | No | — |
| 100 | Status | `Status` | No | Sí | — |
| 110 | ssccr_Load_Lines | `Load_Lines` | No | No | — |
| 120 | Process | `Process` | No | No | — |

### Pestaña `174`

- **AD_TAB_ID:** `174` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 400 | EM_Ssccr_Isivacardreconprocess | `EM_Ssccr_Isivacardreconprocess` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |

### Line (ventana: Conciliación de Tarjetas POS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 5 | Payment | `FIN_Payment_ID` | No | Sí | — |
| 10 | Customer Invoice | `C_Invoice_ID` | No | Sí | — |
| 20 | Sales Order | `C_Order_ID` | No | Sí | — |
| 30 | Recap | `Recap` | No | Sí | — |
| 40 | Lot Name | `Lot` | No | Sí | — |
| 50 | Date | `Date_Statement` | No | Sí | — |
| 60 | Amount | `Amount` | No | Sí | — |
| 70 | Deposit Amount | `Deposit_Amount` | No | No | — |
| 75 | Deposit Amount Original | `Deposit_Amount_Original` | No | Sí | — |
| 80 | Type | `Type` | No | Sí | — |
| 90 | Reconciled | `Reconciled` | No | Sí | — |
| 100 | Types Of Credit | `Ssccr_Types_Of_Credit_ID` | No | Sí | — |
| 110 | Expiration Date | `Expiration_Date` | No | Sí | — |
| 120 | Card | `Ssccr_Cards_Types_ID` | No | Sí | — |
| 130 | Issuing bank | `Ssfi_Banktransfer_ID` | No | Sí | — |
| 140 | Processor Banck | `Ssccr_Processor_Banck_ID` | No | Sí | — |
| 150 | Confirmation No. | `Confirmation_No` | No | Sí | — |

### Pestaña `23691259D1BD4496BCC5F32645BCA4B9`

- **AD_TAB_ID:** `23691259D1BD4496BCC5F32645BCA4B9` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2100 | Customer Invoice | `EM_Ssccr_C_Invoice_ID` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |
| 2110 | Sales Order | `EM_Ssccr_C_Order_ID` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |
| 2120 | Lote | `EM_Ssccr_Lot` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |
| 2130 | Reconciled | `EM_Ssccr_Reconciled` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |
| 2140 | Issuing bank | `EM_Ssccr_Ssfi_Banktransfer_ID` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |
| 2150 | Processor Banck | `EM_Ssccr_Processor_Banck_ID` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |
| 2160 | Types Of Credit | `EM_Ssccr_Types_Of_Credit_ID` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |
| 2170 | Card | `EM_Ssccr_Cards_Types_ID` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |
| 2180 | Expiration date | `EM_Ssccr_Expiration_Date` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |
| 2190 | Recap No | `EM_Ssccr_Recapno` | No | No | A9A8CC6BE09940728C77D9BC694C3817 |
| 2200 | Payment | `EM_Ssccr_Fin_Payment_ID` | No | No | A9A8CC6BE09940728C77D9BC694C3817 |
| 2215 | Reconciliation N° | `EM_Ssccr_Pos_Card_Rec_ID` | No | Sí | A9A8CC6BE09940728C77D9BC694C3817 |

### Pestaña `2845D761A8394468BD3BA4710AA888D4`

- **AD_TAB_ID:** `2845D761A8394468BD3BA4710AA888D4` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 450 | Processor Banck | `EM_Ssccr_Isprocessorbanck` | No | No | — |

### Finnancial Transaction POS (ventana: Finnancial Transaction POS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Date | `date` | No | Sí | — |
| 20 | Deposit Amount | `deposit_amount` | No | Sí | — |
| 30 | ReferenceNo/Recap | `reference` | No | Sí | — |
| 40 | Lot Name | `lot` | No | Sí | — |
| 50 | Issuing bank | `ssccr_ssfi_banktransfer_id` | No | Sí | — |
| 60 | Processor Banck | `ssccr_processor_banck_id` | No | Sí | — |
| 70 | Types Of Credit | `ssccr_types_of_credit_id` | No | Sí | — |
| 80 | Cards Types | `ssccr_cards_types_id` | No | Sí | — |
| 90 | Organization | `ad_org_id` | No | Sí | — |

### General Configuration (ventana: Configuración General)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Count Up by Default | `FIN_Financial_Account_ID` | No | No | — |
| 40 | Agrup | `Agrup` | No | No | — |

### Withholdings (ventana: Configuración conciliación de tarjetas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Type | `Type` | No | No | — |
| 30 | Porcentage | `Porcentage` | No | No | — |
| 40 | G/L Item | `C_Glitem_ID` | No | No | — |
| 50 | Isreconciled | `Isreconciled` | No | No | — |

### Cards types (ventana: Tipos de Tarjeta)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Search Key | `Value` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Processor Banck | `Ssccr_Processor_Banck_ID` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Card  matching configuration (ventana: Configuración conciliación de tarjetas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Processor Banck | `Ssccr_Processor_Banck_ID` | No | No | — |

### Lines (ventana: Configuración conciliación de tarjetas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Cards Types | `Ssccr_Cards_Types_ID` | No | No | — |
| 30 | Income Withholding | `Income_Withholding` | No | No | — |
| 40 | Withholding Tax | `Withholding_Tax` | No | No | — |
| 50 | Types Of Credit | `Ssccr_Types_Of_Credit_ID` | No | No | — |
| 60 | Comition | `Comition` | No | No | — |
| 70 | Payment Terms | `C_Paymentterm_ID` | No | No | — |
| 80 | From Validity | `From_Validity` | No | No | — |
| 90 | Valid Up | `Valid_Up` | No | No | — |

### Log Cards

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 40 | Payment | `FIN_Payment_ID` | No | No | — |
| 50 | Invoice | `C_Invoice_ID` | No | No | — |
| 60 | Sales Order | `C_Order_ID` | No | No | — |
| 70 | Recap | `Recap` | No | No | — |
| 80 | Lot Name | `Lot` | No | No | — |
| 90 | Amount | `Amount` | No | No | — |
| 100 | Deposit Amount | `Deposit_Amount` | No | No | — |
| 110 | Type | `Type` | No | No | — |
| 120 | Reconciled | `Reconciled` | No | No | — |
| 130 | Types Of Credit | `Ssccr_Types_Of_Credit_ID` | No | No | — |
| 140 | Expiration Date | `Expiration_Date` | No | No | — |
| 150 | Cards Types | `Ssccr_Cards_Types_ID` | No | No | — |
| 160 | Processor Banck | `Ssccr_Processor_Banck_ID` | No | No | — |
| 170 | Issuing bank | `Ssfi_Banktransfer_ID` | No | No | — |
| 180 | Date | `Date_Statement` | No | No | — |
| 190 | Confirmation No. | `Confirmation_No` | No | No | — |

### Types of credit (ventana: Tipos de Crédito)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Search Key | `Value` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |

### Summary (ventana: Conciliación de Tarjetas POS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Lot Name | `Lot` | No | Sí | — |
| 20 | Amount | `Amount` | No | Sí | — |
| 30 | Deposit Amount | `Deposit_Amount` | No | No | — |
| 40 | Type | `Type` | No | Sí | — |
| 50 | Reconciled | `Reconciled` | No | No | — |
| 60 | Processor Banck | `Ssccr_Processor_Banck_ID` | No | Sí | — |
| 70 | Confirmation No. | `Confirmation_No` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los usuarios pueden realizar procesos típicos como completar y rechazar transacciones. Los botones dentro del módulo están diseñados para ejecutar estas acciones de manera eficiente. No se generan informes específicos dentro del módulo, pero existen validaciones frecuentes que aseguran la integridad de los datos al momento de procesar las entradas relacionadas con las tarjetas de crédito.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.creditcard.reconciliation.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar Líneas | Load Lines | Load Lines | `Ssccr_load_lines` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Procesar | Process | ssccr_process | `ssccr_process` | No hay configuración para el concepto contable del cobro.; No hay configuración para el concepto contable.; Sumar los montos de deposit_amount para tipo 'B'; Insertar transacción única para tipo Banco ('B') | — |
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
| Botón (PL/pgSQL) | Cargar Líneas | Load Lines | Load Lines | `Ssccr_load_lines` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Procesar | Process | ssccr_process | `ssccr_process` | No hay configuración para el concepto contable del cobro.; No hay configuración para el concepto contable.; Sumar los montos de deposit_amount para tipo 'B'; Insertar transacción única para tipo Banco ('B') | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar Líneas | Load Lines | PL `Ssccr_load_lines` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Procesar | Process | PL `ssccr_process` | No hay configuración para el concepto contable del cobro.; No hay configuración para el concepto contable.; Sumar los montos de deposit_amount para tipo 'B'; Insertar transacción única para tipo Banco ('B') | No hay configuración para el concepto contable del cobro.; No hay configuración para el concepto contable.; Sumar los montos de deposit_amount para tipo 'B'; Insertar transacción única para tipo Banco ('B'); CAMBIAR A CONCILIADO REGISTROS DE LA CUENTA FINANCIERA |
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
| `ssccr_duplicateConfirmarion` | Confirmation number already exist | Confirmation number already exist | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSCCR_Load_Too_Many_Lines` | There are too many settings in the card reconciliation settings window, with the processing bank: | There are too many settings in the card reconciliation settings window, with the processing bank: | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSCCR_Load_dont_find_Lines` | There is no configuration in the card reconciliation configuration window with the combination of Processor Bank, Card Types and credit type respectively: | There is no configuration in the card reconciliation configuration window with the combination of Processor Bank, Card Types and credit type respectively: | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSCCR_Load_Config_Empty_Lines` | The Processing Bank, Card Types and Credit Type fields cannot be empty. | The Processing Bank, Card Types and Credit Type fields cannot be empty. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSCCR_DepositNo_Required` | Deposit number required | Deposit number required | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye varias clases Java que permiten la extensión de funcionalidades específicas, como 'SSCCRApplicationProvider' y 'SSCCR_AddFinTransActionHandler'. Estas clases manejan la lógica del módulo, especialmente en la interacción del usuario y la gestión de transacciones financieras.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.creditcard.reconciliation`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SSCCRApplicationProvider` | root | BaseComponentProvider | ComponentProvider / UI | `src/ec/com/sidesoft/creditcard/reconciliation/SSCCRApplicationProvider.java` |
| `PaymentMethodMulticurrencyActionHandler` | actionHandler | BaseActionHandler | — | `src/ec/com/sidesoft/creditcard/reconciliation/actionHandler/PaymentMethodMulticurrencyActionHandler.java` |
| `SSCCR_AddFinTransActionHandler` | actionHandler | AddPaymentActionHandler | — | `src/ec/com/sidesoft/creditcard/reconciliation/actionHandler/SSCCR_AddFinTransActionHandler.java` |
| `SSCCR_AddPaymentActionHandler` | actionHandler | — | — | `src/ec/com/sidesoft/creditcard/reconciliation/actionHandler/SSCCR_AddPaymentActionHandler.java` |
| `SsccrFinTransactionActionHandler` | actionHandler | BaseActionHandler | — | `src/ec/com/sidesoft/creditcard/reconciliation/actionHandler/SsccrFinTransactionActionHandler.java` |
| `Ssccr_ValidateDepositAmount` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/creditcard/reconciliation/ad_callouts/Ssccr_ValidateDepositAmount.java` |
| `AddPaymentDisplayLogicsExpression` | filterexpression | FilterExpression | — | `src/ec/com/sidesoft/creditcard/reconciliation/filterexpression/AddPaymentDisplayLogicsExpression.java` |
| `BankProcessedSelectorFilterExpression` | filterexpression | FilterExpression | Proceso / informe Java | `src/ec/com/sidesoft/creditcard/reconciliation/filterexpression/BankProcessedSelectorFilterExpression.java` |
| `CardsTypeFilterExpression` | filterexpression | FilterExpression | — | `src/ec/com/sidesoft/creditcard/reconciliation/filterexpression/CardsTypeFilterExpression.java` |
| `EndDateSelectorFilterExpression` | filterexpression | FilterExpression | — | `src/ec/com/sidesoft/creditcard/reconciliation/filterexpression/EndDateSelectorFilterExpression.java` |
| `FinnAccountSelectorFilterExpression` | filterexpression | FilterExpression | — | `src/ec/com/sidesoft/creditcard/reconciliation/filterexpression/FinnAccountSelectorFilterExpression.java` |
| `StartDateSelectorFilterExpression` | filterexpression | FilterExpression | — | `src/ec/com/sidesoft/creditcard/reconciliation/filterexpression/StartDateSelectorFilterExpression.java` |
| `TypeCreditFilterExpression` | filterexpression | FilterExpression | — | `src/ec/com/sidesoft/creditcard/reconciliation/filterexpression/TypeCreditFilterExpression.java` |
| `AddFinaccTransformer` | hqlinjections | HqlQueryTransformer | — | `src/ec/com/sidesoft/creditcard/reconciliation/hqlinjections/AddFinaccTransformer.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSCCR_PROCESSED_TRG` | `ssccr_pos_card_rec_line` | before DELETE | No puedes eliminar una trasacción procesada. |
| Trigger `SSCCR_UPDATE_LINES_TRG` | `ssccr_pos_card_rec_sum` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Ssccr_fin_financial_account-Conf` | `exists (select 1 from ssccr_general_setting where fin_financial_account_id = fin_financial_account.fin_financial_account` |
| AD_VAL_RULE | — | `Ssccr_Doctype_pos_card_rec_line` | `c_doctype.ad_table_id='D3AC9D0A1FFE40239A2ACF8AF86200CD'` |
| AD_VAL_RULE | — | `Ssccr_nancial_Account-Card` | `fin_financial_account.em_ssccr_isprocessorbanck='Y' AND EXISTS (Select 1
From fin_finacc_paymentmethod fpm 
	Join fin_pa` |
| AD_VAL_RULE | — | `Ssccr_fin_financial_account-Bank` | `fin_financial_account.type = 'B'` |
| AD_VAL_RULE | — | `Ssccr_Processor_bank` | `Ssccr_Cards_Types.ssccr_processor_banck_id = @ssccr_processor_banck_id@` |
| AD_VAL_RULE | — | `Ssccr_cards_types's Bank` | `e.id in (select a.ssccr_processor_banck_id from ssccr_cards_types a where a.ssccr_cards_types_id = @Ssccr_Cards_Types_ID` |
| Función PL `ssccr_load_lines_one` | — | invocación proceso | Existe más de un impuesto con el check activado; [OPT] Tasa IVA cacheada al inicio (evita subselects repetidos por cada fila/iteracion); [OPT] Validar impuesto configurado y cachear la tasa en una sola consulta |
| Función PL `ssccr_process` | — | invocación proceso | No hay configuración para el concepto contable del cobro.; No hay configuración para el concepto contable.; Sumar los montos de deposit_amount para tipo 'B' |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El módulo utiliza varios triggers y funciones PL/pgSQL para garantizar la integridad de los datos. Estas herramientas son cruciales para el soporte, ya que proporcionan lógica adicional y aseguran que las operaciones se realicen de manera coherente y segura en la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSCCR_PROCESSED_TRG` | `ssccr_pos_card_rec_line` | before | DELETE | No puedes eliminar una trasacción procesada. | `model/triggers/SSCCR_PROCESSED_TRG.xml` |
| `SSCCR_UPDATE_LINES_TRG` | `ssccr_pos_card_rec_sum` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSCCR_UPDATE_LINES_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssccr_div_recap` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSCCR_DIV_RECAP.xml` |
| `ssccr_load_lines` | Cargar Líneas | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSCCR_LOAD_LINES.xml` |
| `ssccr_load_lines_one` | — | Existe más de un impuesto con el check activado; [OPT] Tasa IVA cacheada al inicio (evita subselects repetidos por cada fila/iteracion); [OPT] Validar impuesto configurado y cachear la tasa en una sola consulta; Antes:… | Existe más de un impuesto con el check activado; [OPT] Tasa IVA cacheada al inicio (evita subselects repetidos por cada fila/iteracion); [OPT] Validar impuesto configurado y cachear la tasa en una sola consulta; Antes: dos SELECT COUNT separados sobre c_tax (una por condicion); HEAD VAR: cabecera del documento de conciliacion; [OPT] LEFT JOIN LATERAL: agrega impuestos solo para la factura de esta transaccion. | `model/functions/SSCCR_LOAD_LINES_ONE.xml` |
| `ssccr_process` | Procesar | No hay configuración para el concepto contable del cobro.; No hay configuración para el concepto contable.; Sumar los montos de deposit_amount para tipo 'B'; Insertar transacción única para tipo Banco ('B') | No hay configuración para el concepto contable del cobro.; No hay configuración para el concepto contable.; Sumar los montos de deposit_amount para tipo 'B'; Insertar transacción única para tipo Banco ('B'); CAMBIAR A CONCILIADO REGISTROS DE LA CUENTA FINANCIERA | `model/functions/SSCCR_PROCESS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cargar Líneas | `Load Lines` | Botón (PL/pgSQL) | PL `Ssccr_load_lines` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 2 | Procesar | `ssccr_process` | Botón (PL/pgSQL) | PL `ssccr_process` | N | No hay configuración para el concepto contable del cobro.; No hay configuración para el concepto contable.; Sumar los montos de deposit_amount para tipo 'B'; Insertar transacción ú |

**Total acciones documentadas (extract):** **2** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/ec.com.sidesoft.creditcard.reconciliation/js/Ssccr-addPayment-onchange.js` |
| `web/ec.com.sidesoft.creditcard.reconciliation/js/ob-aprm-addPayment.js` |
| `web/ec.com.sidesoft.creditcard.reconciliation/js/ssccrFinTransaction.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.creditcard.reconciliation`.

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

# Glosario — prefijo `SSCCR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCCR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.creditcard.reconciliation` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Load Lines` — Cargar Líneas
- `ssccr_process` — Procesar

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Card Settlement Loading Transaction
**Package:** `ec.com.sidesoft.creditcard.reconciliation.transaction`

# Module overview — Card Settlement Loading Transaction

## Functional

La Carga de Liquidación de Tarjetas es un módulo diseñado para optimizar el proceso de conciliación de transacciones de tarjetas de crédito. Su propósito principal es permitir a los usuarios cargar y gestionar los datos relacionados con las liquidaciones de tarjetas, asegurando que las transacciones se registren correctamente para un análisis financiero eficiente. Está dirigido a usuarios de negocio que manejan las operaciones financieras, así como a desarrolladores y equipo de soporte que necesitan entender la funcionalidad detrás del módulo. Las dependencias incluyen el núcleo de Openbravo y varios módulos específicos que garantizan una integración fluida.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/creditcard/reconciliation/transaction` |
| Web | `web/ec.com.sidesoft.creditcard.reconciliation.transaction/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework
- Sidesoft Credit Card Reconciliation

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SCCRT`

# Guía de chat — Card Settlement Loading Transaction

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.creditcard.reconciliation.transaction`).

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
- «¿Qué es la tabla sccrt_card_load_line?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo cargar una liquidación de tarjeta?
- ¿Qué debo hacer si el sistema me indica un error al cargar la transacción?
- ¿Cuáles son los pasos para validar una carga de liquidación?
- ¿Dónde puedo encontrar los detalles de las transacciones que he cargado?
- ¿Es posible modificar una transacción una vez cargada?
- ¿Qué información necesito para completar la carga de una liquidación?
- ¿Cómo puedo generar un informe de las transacciones procesadas?
- ¿Qué hacer si necesito eliminar una carga incorrecta?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la tabla cabecera 'sccrt_card_load_transaction', que actúa como ancla para las operaciones de carga de liquidez. Cada transacción se descompone en líneas correspondientes que se almacenan en la tabla vinculada 'sccrt_card_load_line'. La relación entre estas tablas es fundamental para la gestión de las liquidaciones de tarjetas, permitiendo al sistema gestionar múltiples transacciones de manera eficiente. Existen triggers clave, como 'SCCRT_SETTLEMENT_LOAD_TRG' que se encargan de la validación y el manejo de las reglas de negocio al insertar o modificar datos en la tabla de transacciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sccrt_card_load_line` |
| `sccrt_card_load_transaction` |
| `sccrt_concepts` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sccrt_card_load_line` | sccrt_card_load_line | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ssccr_pos_card_rec_id→ssccr_pos_card_rec; fin_finacc_transsaction_id→fin_finacc_transaction; sccrt_card_load_transaction_id→sccrt_card_load_transaction | Detalle enlazado a ad_client, ad_org, ssccr_pos_card_rec. | PK `sccrt_cll_key`; Cols: date_deposit, lot, recap, accredit_value, commision_value; `SCCRT_CLL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SCCRT_CLL_ISERROR_CHK`: ISERROR IN ('Y', 'N') (+1) |
| `sccrt_card_load_transaction` | sccrt_card_load_transaction | `SCCRT_SETTLEMENT_LOAD_TRG` | `SCCRT_DOCUMENTNO` (documentno) | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype; fin_financial_account_from_id→fin_financial_account; fin_financial_account_to_id→fin_financial_account | Detalle enlazado a ad_client, ad_org, c_doctype. Validado por trigger(s): SCCRT_SETTLEMENT_LOAD_TRG. | PK `sccrt_clt_key`; Cols: c_doctype_id, documentno, fin_financial_account_from_id, fin_financial_account_to_id, description; `SCCRT_CLT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SCCRT_CLT_LOADLINES_CHK`: LOAD_LINES IN ('Y', 'N') (+1) |
| `sccrt_concepts` | sccrt_concepts | `SCCRT_CONCEPTS_TYPE_TRG` | — | ssccr_processor_banck_id→ssccr_processor_banck; c_glitem_id→c_glitem; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, c_glitem, ssccr_processor_banck. Validado por trigger(s): SCCRT_CONCEPTS_TYPE_TRG. | PK `sccrt_cp_key`; Cols: type, c_glitem_id, ssccr_processor_banck_id; `SCCRT_CP_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sccrt_card_load_line` |
| `sccrt_card_load_transaction` |
| `sccrt_concepts` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`SSCCR_GENERAL_SETTING`, `SSCCR_POS_CARD_REC`, `SSCCR_POS_CARD_REC_LINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se puede acceder a través de la ventana 'Carga de Liquidación'. Desde la interfaz de usuario (UI), los usuarios navegan utilizando menús que les permiten elegir entre distintas funcionalidades relacionadas con la carga de transacciones de tarjetas, facilitando el manejo de datos en un entorno gráfico intuitivo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.creditcard.reconciliation.transaction.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Carga de Liquidación | Card Settlement Loading Transaction |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Carga de Liquidación | Card Settlement Loading Transaction | No |
| Detalle Conciliaciones Tarjetas | Card Reconciliation Detail | No |
| Reporte Liquidación Tarjetas POS | Settled cards report POS | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.creditcard.reconciliation.transaction.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Carga de Liquidación

- **AD_WINDOW_ID:** `3E3001887190467F99B0080CB5BF9521`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Transacción de Carga de Liquidación de Tarjeta | `EAC23CAC025F46EF93A40824A6531CA4` | 0 |
| 20 | Linea de Transacción de Carga de Liquidación de Tarjeta | `9A9213039DA14CEB93B548758215FBFD` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `1E4A691927F2483CB05E110CA749DBFE`

- **AD_TAB_ID:** `1E4A691927F2483CB05E110CA749DBFE` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 23 | EM_Sccrt_Liquidated | `EM_Sccrt_Liquidated` | No | No | — |
| 25 | EM_Sccrt_Referencecode | `EM_Sccrt_Referencecode` | No | No | — |

### Pestaña `4A5FF4E44F2846109B8B776431922394`

- **AD_TAB_ID:** `4A5FF4E44F2846109B8B776431922394` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 50 | EM_Sccrt_Rentretention_ID | `EM_Sccrt_Rentretention_ID` | No | No | EC0D2B2274734503B45284686CF749F3 |
| 60 | EM_Sccrt_Ivaretention_ID | `EM_Sccrt_Ivaretention_ID` | No | No | EC0D2B2274734503B45284686CF749F3 |
| 70 | EM_Sccrt_Transitvalue_ID | `EM_Sccrt_Transitvalue_ID` | No | No | EC0D2B2274734503B45284686CF749F3 |

### Transacción de Carga de Liquidación de Tarjeta (ventana: Carga de Liquidación)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Document Type | `C_Doctype_ID` | No | Sí | — |
| 30 | Document No. | `Documentno` | No | Sí | — |
| 40 | Date_Payment | `Date_Payment` | No | No | — |
| 50 | FIN_Financial_Account_From_ID | `FIN_Financial_Account_From_ID` | No | No | — |
| 60 | FIN_Financial_Account_To_ID | `FIN_Financial_Account_To_ID` | No | No | — |
| 90 | Description | `Description` | No | No | — |
| 110 | Load_Lines | `Load_Lines` | No | No | — |
| 120 | Generate CR | `Process` | No | No | — |
| 130 | Document Status | `Docstatus` | No | Sí | — |

### Concepts

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Type | `Type` | No | No | — |
| 40 | G/L Item | `C_Glitem_ID` | No | No | — |

### Linea de Transacción de Carga de Liquidación de Tarjeta (ventana: Carga de Liquidación)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Date_Deposit | `Date_Deposit` | No | Sí | — |
| 15 | Grouping_Batch | `Grouping_Batch` | No | No | — |
| 20 | Lot Name | `Lot` | No | Sí | — |
| 30 | Recap | `Recap` | No | Sí | — |
| 40 | Amount | `Amount` | No | No | — |
| 50 | Accredit_Value | `Accredit_Value` | No | Sí | — |
| 60 | Commision_Value | `Commision_Value` | No | Sí | — |
| 70 | Withh_Rent | `Withh_Rent` | No | Sí | — |
| 80 | Withh_Iva | `Withh_Iva` | No | Sí | — |
| 90 | Iva | `Iva` | No | No | — |
| 92 | Iserror | `Iserror` | No | Sí | — |
| 94 | Processed | `Processed` | No | No | — |
| 96 | LOG_Error | `LOG_Error` | No | No | — |
| 100 | Deposit_Reference | `Deposit_Reference` | No | Sí | — |
| 110 | Settled | `Settled` | No | No | — |
| 130 | FIN_Finacc_Transsaction_ID | `FIN_Finacc_Transsaction_ID` | No | No | — |
| 140 | Active | `Isactive` | No | No | — |
| 190 | Textcostcenter | `Textcostcenter` | No | No | — |
| 200 | Textuser | `Textuser` | No | No | — |
| 250 | TC Conciliation | `Ssccr_Pos_Card_Rec_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Se contemplan varios procesos dentro del módulo, cada uno con botones típicos como completar, retornar y rechazar. Los usuarios pueden completar el registro de la carga de transacciones de tarjeta mediante un botón específico, lo que activa las validaciones necesarias y los procesos asociados. Además, aunque no se generan informes directos, las transacciones pueden ser validadas a través de funciones PL que proporcionan retroalimentación y aseguran la integridad de los datos ingresados en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.creditcard.reconciliation.transaction.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Crear CT | Generate CR | Generate CR | Java `SccrtGenerateCR` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sccrt_Card_Load_Transaction_ID` | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/ad_process/SccrtGenerateCR.java` |
| Botón (PL/pgSQL) | Card Settlement Loading | Card Settlement Loading | Card Settlement Loading | `sccrt_card_settlement_line` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Procesar | Process | sccrt_process | `sccrt_process` | No hay configuración para el concepto contable.; COALESCE(Cur_PosCardRecSum.em_sccrt_referencecode,'') --Descripcion; v_description := Cur_PosCardRecSum.confirmation_no||' / '|| Cur_PosCardRecSum.name_processor_bank;; C… | — |
| Botón (PL/pgSQL) | Sccrt_Match_Lines | Sccrt_Match_Lines | Sccrt_Match_Lines | `sccrt_match_lines` | AND coalesce (l.fin_finacc_transsaction_id, '') = ''; RAISE_APPLICATION_ERROR(-20000,'Errores:'||v_LineError) ; | — |
| Botón (PL/pgSQL) | sccrt_update_lines | sccrt_update_lines | sccrt_update_lines | `sccrt_update_lines` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Detalle Conciliaciones Tarjetas | Card Reconciliation Detail | Card Reconciliation Detail | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Liquidación Tarjetas POS | Settled cards report POS | Settled cards report POS | *(OBUIAPP / manual)* | Settled cards report POS | — |
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
| Botón (Java) | Crear CT | `SccrtGenerateCR` | Proceso Java (toolbar/background) | `Sccrt_Card_Load_Transaction_ID` | — | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/ad_process/SccrtGenerateCR.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Crear CT | Generate CR | Generate CR | Java `SccrtGenerateCR` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sccrt_Card_Load_Transaction_ID` | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/ad_process/SccrtGenerateCR.java` |
| Botón (PL/pgSQL) | Card Settlement Loading | Card Settlement Loading | Card Settlement Loading | `sccrt_card_settlement_line` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Procesar | Process | sccrt_process | `sccrt_process` | No hay configuración para el concepto contable.; COALESCE(Cur_PosCardRecSum.em_sccrt_referencecode,'') --Descripcion; v_description := Cur_PosCardRecSum.confirmation_no||' / '|| Cur_PosCardRecSum.name_processor_bank;; C… | — |
| Botón (PL/pgSQL) | Sccrt_Match_Lines | Sccrt_Match_Lines | Sccrt_Match_Lines | `sccrt_match_lines` | AND coalesce (l.fin_finacc_transsaction_id, '') = ''; RAISE_APPLICATION_ERROR(-20000,'Errores:'||v_LineError) ; | — |
| Botón (PL/pgSQL) | sccrt_update_lines | sccrt_update_lines | sccrt_update_lines | `sccrt_update_lines` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Detalle Conciliaciones Tarjetas | Card Reconciliation Detail | Card Reconciliation Detail | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Liquidación Tarjetas POS | Settled cards report POS | Settled cards report POS | *(OBUIAPP / manual)* | Settled cards report POS | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Crear CT | Generate CR | Java `SccrtGenerateCR` | Proceso Openbravo registro `Sccrt_Card_Load_Transaction_ID` | Proceso Openbravo registro `Sccrt_Card_Load_Transaction_ID` |
| Botón (PL/pgSQL) | Card Settlement Loading | Card Settlement Loading | PL `sccrt_card_settlement_line` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Procesar | Process | PL `sccrt_process` | No hay configuración para el concepto contable.; COALESCE(Cur_PosCardRecSum.em_sccrt_referencecode,'') --Descripcion; v_description := Cur_PosCardRecSum.confirmation_no||' / '|| Cur_PosCardRecSum.name_processor_bank;; C… | No hay configuración para el concepto contable.; COALESCE(Cur_PosCardRecSum.em_sccrt_referencecode,'') --Descripcion; v_description := Cur_PosCardRecSum.confirmation_no||' / '|| Cur_PosCardRecSum.name_processor_bank;; CAMBIAR A CONCILIADO REGISTROS DE LA CUENTA FINANCIERA |
| Botón (PL/pgSQL) | Sccrt_Match_Lines | Sccrt_Match_Lines | PL `sccrt_match_lines` | AND coalesce (l.fin_finacc_transsaction_id, '') = ''; RAISE_APPLICATION_ERROR(-20000,'Errores:'||v_LineError) ; | AND coalesce (l.fin_finacc_transsaction_id, '') = ''; RAISE_APPLICATION_ERROR(-20000,'Errores:'||v_LineError) ; |
| Botón (PL/pgSQL) | sccrt_update_lines | sccrt_update_lines | PL `sccrt_update_lines` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Detalle Conciliaciones Tarjetas | Card Reconciliation Detail | — | — | — |
| Proceso / otro | Reporte Liquidación Tarjetas POS | Settled cards report POS | — | Settled cards report POS | — |
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
| `Sccrt_incorrect_user` | No match found for any transaction: User does not match. | No match found for any transaction: User does not match. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sccrt_incorrect_costcenter` | No match found for any transaction: Cost center does not match. | No match found for any transaction: Cost center does not match. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sccrt_incorrect_amount` | No match found for any transaction: amount value does not match. | No match found for any transaction: amount value does not match. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sccrt_not_matchfound` | No match found for any transaction. | No match found for any transaction. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SCCRT_CannotDeleteTrx` | You cannot delete a completed record or one with lines already processed. | You cannot delete a completed record or one with lines already processed. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo también implementa clases Java, como 'SccrtComponentProvider' y 'SCCRT_AddFinTransActionHandler', que se encargan de la lógica de negocio y la integración con el sistema Openbravo, proporcionando funcionalidades adicionales como la carga de archivos y la gestión de transacciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.creditcard.reconciliation.transaction`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SccrtComponentProvider` | root | BaseComponentProvider | ComponentProvider / UI | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/SccrtComponentProvider.java` |
| `SCCRT_AddFinTransActionHandler` | actionHandler | AddPaymentActionHandler | — | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/actionHandler/SCCRT_AddFinTransActionHandler.java` |
| `ImportDataFile` | ad_actionbutton | — | — | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/ad_actionbutton/ImportDataFile.java` |
| `UploadFileProcess` | ad_actionbutton | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/ad_actionbutton/UploadFileProcess.java` |
| `SccrtCardLoadLineEventHandler` | ad_events | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/ad_events/SccrtCardLoadLineEventHandler.java` |
| `SccrtGenerateCR` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/ad_process/SccrtGenerateCR.java` |
| `SCCRT_Helper` | utils | — | — | `src/ec/com/sidesoft/creditcard/reconciliation/transaction/utils/SCCRT_Helper.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SCCRT_CONCEPTS_TYPE_TRG` | `sccrt_concepts` | before INSERT/UPDATE | No se permite duplicar el tipo de Retencion |
| Trigger `SCCRT_SETTLEMENT_LOAD_TRG` | `sccrt_card_load_transaction` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SCCRT_VALIDATETYPE_TRG` | `ssccr_withholdings` | before INSERT/UPDATE | No se permite duplicar el tipo de Retencion |
| AD_VAL_RULE | — | `Doc sccrt_card_load_transaction` | `c_doctype.ad_table_id='EAC23CAC025F46EF93A40824A6531CA4'` |
| Java event/validator | `SccrtCardLoadLineEventHandler` | persistencia/UI | *(leer `src/ec/com/sidesoft/creditcard/reconciliation/transaction/ad_events/SccrtCardLoadLineEventHandler.java`)* |
| Función PL `sccrt_load_lines_one` | — | invocación proceso | Existe más de un impuesto con el check activado; Validate unique tax with credit card conciliation check; Para cada grouping_batch recorremos sus transacciones |
| Función PL `sccrt_match_lines` | — | invocación proceso | AND coalesce (l.fin_finacc_transsaction_id, '') = ''; RAISE_APPLICATION_ERROR(-20000,'Errores:'||v_LineError) ; |
| Función PL `sccrt_process` | — | invocación proceso | No hay configuración para el concepto contable.; COALESCE(Cur_PosCardRecSum.em_sccrt_referencecode,'') --Descripcion; v_description := Cur_PosCardRecSum.confirmation_no||' / '|| Cur_PosCardRecSum.name_processor_bank; |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL juegan un rol crucial en el soporte del módulo. Se utilizan para automatizar procesos de validación y asegurar la consistencia de los datos en la base de datos. Por ejemplo, triggers como 'SCCRT_CONCEPTS_TYPE_TRG' ayudan a prevenir la duplicación de tipos de retención, mientras que las funciones PL facilitan la lógica del negocio que sustenta el flujo de datos en el módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SCCRT_SETTLEMENT_LOAD_TRG` | `sccrt_card_load_transaction` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SCCRT_SETTLEMENT_LOAD_TRG.xml` |
| `SCCRT_CONCEPTS_TYPE_TRG` | `sccrt_concepts` | before | INSERT/UPDATE | No se permite duplicar el tipo de Retencion | `model/triggers/SCCRT_CONCEPTS_TYPE_TRG.xml` |
| `SCCRT_VALIDATETYPE_TRG` | `ssccr_withholdings` | before | INSERT/UPDATE | No se permite duplicar el tipo de Retencion | `model/triggers/SCCRT_VALIDATETYPE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sccrt_card_settlement_line` | Card Settlement Loading | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SCCRT_CARD_SETTLEMENT_LINE.xml` |
| `sccrt_load_lines_one` | — | Existe más de un impuesto con el check activado; Validate unique tax with credit card conciliation check; Para cada grouping_batch recorremos sus transacciones; vCheck := v_c_invoice_id IS NULL OR COALESCE(Cur_Finacc_Tr… | Existe más de un impuesto con el check activado; Validate unique tax with credit card conciliation check; Para cada grouping_batch recorremos sus transacciones; vCheck := v_c_invoice_id IS NULL OR COALESCE(Cur_Finacc_Transaction.impuesto,0) = 0;; Recupera los conceptos de la tabla ssccr_processor_banck; Sumamos todas las transacciones de ese grouping_batch/lote | `model/functions/SCCRT_LOAD_LINES_ONE.xml` |
| `sccrt_match_lines` | Sccrt_Match_Lines | AND coalesce (l.fin_finacc_transsaction_id, '') = ''; RAISE_APPLICATION_ERROR(-20000,'Errores:'||v_LineError) ; | AND coalesce (l.fin_finacc_transsaction_id, '') = ''; RAISE_APPLICATION_ERROR(-20000,'Errores:'||v_LineError) ; | `model/functions/SCCRT_MATCH_LINES.xml` |
| `sccrt_process` | Procesar | No hay configuración para el concepto contable.; COALESCE(Cur_PosCardRecSum.em_sccrt_referencecode,'') --Descripcion; v_description := Cur_PosCardRecSum.confirmation_no||' / '|| Cur_PosCardRecSum.name_processor_bank;; C… | No hay configuración para el concepto contable.; COALESCE(Cur_PosCardRecSum.em_sccrt_referencecode,'') --Descripcion; v_description := Cur_PosCardRecSum.confirmation_no||' / '|| Cur_PosCardRecSum.name_processor_bank;; CAMBIAR A CONCILIADO REGISTROS DE LA CUENTA FINANCIERA | `model/functions/SCCRT_PROCESS.xml` |
| `sccrt_update_lines` | sccrt_update_lines | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SCCRT_UPDATE_LINES.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Crear CT | `Generate CR` | Botón (Java) | Java `SccrtGenerateCR` | N | Proceso Openbravo registro `Sccrt_Card_Load_Transaction_ID` |
| 2 | Card Settlement Loading | `Card Settlement Loading` | Botón (PL/pgSQL) | PL `sccrt_card_settlement_line` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 3 | Procesar | `sccrt_process` | Botón (PL/pgSQL) | PL `sccrt_process` | N | No hay configuración para el concepto contable.; COALESCE(Cur_PosCardRecSum.em_sccrt_referencecode,'') --Descripcion; v_description := Cur_PosCardRecSum.confirmation_no||' / '|| Cu |
| 4 | Sccrt_Match_Lines | `Sccrt_Match_Lines` | Botón (PL/pgSQL) | PL `sccrt_match_lines` | N | AND coalesce (l.fin_finacc_transsaction_id, '') = ''; RAISE_APPLICATION_ERROR(-20000,'Errores:'||v_LineError) ; |
| 5 | sccrt_update_lines | `sccrt_update_lines` | Botón (PL/pgSQL) | PL `sccrt_update_lines` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

**Total acciones documentadas (extract):** **5** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/ec.com.sidesoft.creditcard.reconciliation.transaction/js/uploadFile.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.creditcard.reconciliation.transaction`.

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

# Glosario — prefijo `SCCRT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SCCRT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.creditcard.reconciliation.transaction` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Generate CR` — Crear CT
- `Card Settlement Loading` — Card Settlement Loading
- `sccrt_process` — Procesar
- `Sccrt_Match_Lines` — Sccrt_Match_Lines
- `sccrt_update_lines` — sccrt_update_lines
- `Card Reconciliation Detail` — Detalle Conciliaciones Tarjetas
- `Settled cards report POS` — Reporte Liquidación Tarjetas POS

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Ecuador Checkbook Modules
**Package:** `ec.com.sidesoft.localization.checkbook`

# Module overview — Ecuador Checkbook Modules

## Functional

El módulo Ecuador Checkbook permite gestionar de manera eficiente el manejo de chequeras dentro del sistema ERP Openbravo, facilitando la reconciliación y registro de pagos. Está diseñado para usuarios de negocio que requieren llevar un control adecuado de sus transacciones bancarias. Los actores principales incluyen contadores y administradores financieros que interactúan con el módulo para registrar pagos y consultar información financiera. El alcance del módulo abarca la gestión de cheques, la integración con cuentas financieras y el manejo de métodos de pago. No presenta dependencias con otros módulos específicos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/checkbook` |
| Web | `web/ec.com.sidesoft.localization.checkbook/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLCB`

# Guía de chat — Ecuador Checkbook Modules

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.checkbook`).

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
- «¿Qué es la tabla slcb_checkbookline?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo registro un nuevo cheque en el módulo?
- ¿Qué pasos debo seguir para actualizar un pago existente?
- ¿Cómo puedo validar que un cheque ha sido procesado correctamente?
- ¿Qué sucede si un cheque es rechazado?
- ¿Cómo puedo ver el historial de cheques emitidos?
- ¿Hay alguna forma de generar informes de los pagos realizados?
- ¿Qué validaciones se realizan al registrar un método de pago?
- ¿Cómo puedo manejar situaciones de pagos reintegrados?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la tabla principal slcb_checkbookline, que contiene las líneas de cheques y sus estados asociados. Esta tabla se relaciona con otras entidades como fin_payment, que almacena información sobre los pagos procesados, y fin_finacc_paymentmethod, que define los métodos de pago disponibles. Los triggers clave, como SLCB_UPDREFERENCECHECK_TRG y SLCB_VALIDATECHECKBOOK_TRG, garantizan la integridad de los datos y realizan validaciones necesarias al momento de registrar pagos o al cargar información en las líneas de cheques.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `slcb_checkbook` |
| `slcb_checkbookline` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `slcb_checkbook` | slcb_checkbook | — | — | ad_client_id→ad_client; ad_org_id→ad_org; fin_financial_account_id→fin_financial_account | Detalle enlazado a ad_client, ad_org, fin_financial_account. | PK `slcb_checkbook_key`; Cols: value, description, checkbook_from, checkbook_to, generated; `SLCB_CHECKBOOK_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `slcb_checkbookline` | slcb_checkbookline | `SLCB_VALIDATECHECKBOOK_TRG` | — | fin_payment_id→fin_payment; ad_client_id→ad_client; ad_org_id→ad_org; slcb_checkbook_id→slcb_checkbook | Detalle enlazado a ad_client, ad_org, fin_payment. Validado por trigger(s): SLCB_VALIDATECHECKBOOK_TRG. | PK `slcb_checkbookline_key`; Cols: slcb_checkbook_id, checkno, paymentno, status, description; `SLCB_CKBOOKLINE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `slcb_checkbook` |
| `slcb_checkbookline` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ROLE`, `FIN_FINACC_PAYMENTMETHOD`, `FIN_PAYMENT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de una interfaz de usuario optimizada que permite a los usuarios acceder a las funcionalidades de gestión de cheques. Aunque no se han listado ventanas específicas, los usuarios pueden esperar un menú intuitivo donde podrán visualizar y registrar sus chequeras, línea a línea.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.checkbook.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.checkbook.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `01F5E95D71544D428E1B9004B05D0298`

- **AD_TAB_ID:** `01F5E95D71544D428E1B9004B05D0298` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 27 | Generate Check | `EM_Slcb_Isgeneratecheck` | No | No | — |

### CheckBook

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | SearchKey | `Value` | No | No | — |
| 30 | Observations | `Description` | No | No | — |
| 40 | Check From | `Checkbook_From` | No | No | — |
| 50 | Check To | `Checkbook_To` | No | No | — |
| 60 | Generated | `Generated` | No | Sí | — |
| 70 | Created Checkbook | `Created_Checkbook` | No | No | — |
| 90 | Active | `Isactive` | No | No | — |
| 100 | Void Check | `Void_Checkbook` | No | No | — |

### Pestaña `119`

- **AD_TAB_ID:** `119` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 200 | Check Book | `EM_Slcb_Checkbook` | No | No | — |

### Lines

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 15 | Line | `Line` | No | No | — |
| 30 | Check No. | `Checkno` | No | No | — |
| 40 | Payment No. | `Paymentno` | No | No | — |
| 50 | Status | `Status` | No | No | — |
| 60 | Observations | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |
| 90 | Void Check | `Voided_Checkbook` | No | No | — |
| 100 | Reactive Check | `Reactive_Check` | No | No | — |
| 110 | Payment | `FIN_Payment_ID` | No | Sí | — |

### Pestaña `F7A52FDAAA0346EFA07D53C125B40404`

- **AD_TAB_ID:** `F7A52FDAAA0346EFA07D53C125B40404` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 85 | Checkbook Head | `EM_Slcb_Checkbook_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos en el módulo incluyen varios botones como Completar, Retornar y Rechazar, que permiten a los usuarios gestionar el estado de los pagos de manera sencilla. Las validaciones frecuentes aseguran que la información ingresada sea precisa y que se respeten las reglas de negocio para el manejo de cheques. Aunque no se detallan informes específicos, se espera que el módulo proporcione resúmenes de las transacciones realizadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.checkbook.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Anular Cheque | Void Check | Slcb_Voided_Checkbook | `slcb_voided_check` | Elimina la relacion del cheuqe en el pago; RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
| Botón (PL/pgSQL) | Cerrar Chequera | Void Check | Slcb_VoidedAllCheckBook | `slcb_void_checkbook` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
| Botón (PL/pgSQL) | Generar Chequera | Created Checkbook | Created_Checkbook | `slcb_created_checkbook` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
| Botón (PL/pgSQL) | Reactivar Cheque | Reactive Check | Slcb_ReactiveCheck | `slcb_reactivecheck` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
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
| Botón (PL/pgSQL) | Anular Cheque | Void Check | Slcb_Voided_Checkbook | `slcb_voided_check` | Elimina la relacion del cheuqe en el pago; RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
| Botón (PL/pgSQL) | Cerrar Chequera | Void Check | Slcb_VoidedAllCheckBook | `slcb_void_checkbook` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
| Botón (PL/pgSQL) | Generar Chequera | Created Checkbook | Created_Checkbook | `slcb_created_checkbook` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
| Botón (PL/pgSQL) | Reactivar Cheque | Reactive Check | Slcb_ReactiveCheck | `slcb_reactivecheck` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Anular Cheque | Void Check | PL `slcb_voided_check` | Elimina la relacion del cheuqe en el pago; RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | Elimina la relacion del cheuqe en el pago; RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
| Botón (PL/pgSQL) | Cerrar Chequera | Void Check | PL `slcb_void_checkbook` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
| Botón (PL/pgSQL) | Generar Chequera | Created Checkbook | PL `slcb_created_checkbook` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
| Botón (PL/pgSQL) | Reactivar Cheque | Reactive Check | PL `slcb_reactivecheck` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
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
| `Slcb_ErrorSelectedCheck` | The checkbook has all the sequences used. | The checkbook has all the sequences used. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Slcb_ErrorUsed` | It can not be deleted because this check is in the "Used" state. | It can not be deleted because this check is in the "Used" state. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Slcb_ErrorGenerated` | Can not Delete because the current state is generated. | Can not Delete because the current state is generated. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Slcb_ErrorVoided` | It can not be deleted because this check is in the "Canceled" state. | It can not be deleted because this check is in the "Canceled" state. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Slcb_ErrorSelectedCheckBook` | There are no active checkbooks. | There are no active checkbooks. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Slcb_ErrorReactve` | It can not be reactivated because this checkbook has records in "Used" or "Canceled" status. | It can not be reactivated because this checkbook has records in "Used" or "Canceled" status. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Slcb_ErrorReactive` | This check is referenced. | This check is referenced. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Slcb_ErrorDescriptionVoided` | It can not be canceled because the "Observation" field is empty. | It can not be canceled because the "Observation" field is empty. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Slcb_ErrorVoid` | The status of the check must be "Used" in order to cancel it. | The status of the check must be "Used" in order to cancel it. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Slcb_ValidateRangeChecks` | The sequence of the "Check from" field must be greater than the "Check to" field. | The sequence of the "Check from" field must be greater than the "Check to" field. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye una clase Java denominada Slcb_PaymentMethod_Finaccount, que se encarga de gestionar la lógica de negocio necesaria para las interacciones con los métodos de pago y las cuentas financieras, utilizando las funcionalidades de Openbravo para proporcionar una experiencia de usuario fluida.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.checkbook`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Slcb_PaymentMethod_Finaccount` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/checkbook/ad_callouts/Slcb_PaymentMethod_Finaccount.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SLCB_UPDREFERENCECHECK_TRG` | `fin_payment` | before INSERT/UPDATE/DELETE | Si el antiguo estado era pago reintegrado; Almacenar la cuenta financiera de la cabecera; Almacena el metodo de pago de la cabecera; Almacena el numero de documento de la cabecera |
| Trigger `SLCB_VALIDATECHECKBOOK_TRG` | `slcb_checkbookline` | before INSERT/UPDATE/DELETE | Validación reutilizable de campos. |
| AD_VAL_RULE | — | `Slcb_Checkbook_ID - active` | `Slcb_Checkbook.isactive = 'Y' and Slcb_Checkbook.Fin_Financial_Account_ID = @Fin_Financial_Account_ID@` |
| Función PL `slcb_created_checkbook` | — | invocación proceso | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
| Función PL `slcb_reactivecheck` | — | invocación proceso | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
| Función PL `slcb_void_checkbook` | — | invocación proceso | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
| Función PL `slcb_voided_check` | — | invocación proceso | Elimina la relacion del cheuqe en el pago; RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers en este módulo desempeñan un papel crucial, facilitando la validación de datos y garantizando que se mantenga la coherencia entre las tablas relacionadas, especialmente durante las actualizaciones de estados y registros de pagos. Las funciones PL están diseñadas para asistir en la lógica de negocio relacionada con las operaciones de pagos y cheques, optimizando así el soporte administrativo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SLCB_UPDREFERENCECHECK_TRG` | `fin_payment` | before | INSERT/UPDATE/DELETE | Si el antiguo estado era pago reintegrado; Almacenar la cuenta financiera de la cabecera; Almacena el metodo de pago de la cabecera; Almacena el numero de documento de la cabecera | `model/triggers/SLCB_UPDREFERENCECHECK_TRG.xml` |
| `SLCB_VALIDATECHECKBOOK_TRG` | `slcb_checkbookline` | before | INSERT/UPDATE/DELETE | Validación reutilizable de campos. | `model/triggers/SLCB_VALIDATECHECKBOOK_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `slcb_created_checkbook` | Generar Chequera | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | `model/functions/SLCB_CREATED_CHECKBOOK.xml` |
| `slcb_reactivecheck` | Reactivar Cheque | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | `model/functions/SLCB_REACTIVECHECK.xml` |
| `slcb_void_checkbook` | Cerrar Chequera | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | `model/functions/SLCB_VOID_CHECKBOOK.xml` |
| `slcb_voided_check` | Anular Cheque | Elimina la relacion del cheuqe en el pago; RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | Elimina la relacion del cheuqe en el pago; RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | `model/functions/SLCB_VOIDED_CHECK.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Anular Cheque | `Slcb_Voided_Checkbook` | Botón (PL/pgSQL) | PL `slcb_voided_check` | N | Elimina la relacion del cheuqe en el pago; RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
| 2 | Cerrar Chequera | `Slcb_VoidedAllCheckBook` | Botón (PL/pgSQL) | PL `slcb_void_checkbook` | N | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
| 3 | Generar Chequera | `Created_Checkbook` | Botón (PL/pgSQL) | PL `slcb_created_checkbook` | N | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
| 4 | Reactivar Cheque | `Slcb_ReactiveCheck` | Botón (PL/pgSQL) | PL `slcb_reactivecheck` | N | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |

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

Módulo: `ec.com.sidesoft.localization.checkbook`.

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

# Glosario — prefijo `SLCB`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLCB` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.checkbook` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Slcb_Voided_Checkbook` — Anular Cheque
- `Slcb_VoidedAllCheckBook` — Cerrar Chequera
- `Created_Checkbook` — Generar Chequera
- `Slcb_ReactiveCheck` — Reactivar Cheque

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Ecuador Checkbook Custom Module
**Package:** `ec.com.sidesoft.localization.custom.checkbook`

# Module overview — Ecuador Checkbook Custom Module

## Functional

El módulo personalizado 'Ecuador Checkbook Custom Module' tiene como finalidad adaptar las funcionalidades del sistema ERP Openbravo a las necesidades específicas de la gestión de cheques en Ecuador. Está diseñado para ser usado por usuarios de negocio que requieren un manejo eficiente de sus transacciones bancarias, así como por personal de soporte de nivel 2 y desarrolladores que necesiten implementar y mantener este módulo. El alcance de este módulo se limita a la gestión de cheques y su integración con las transacciones financieras existentes, dependiendo del correcto funcionamiento de otros módulos del ERP para su operatividad.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/custom/checkbook` |
| Web | `web/ec.com.sidesoft.localization.custom.checkbook/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`CSCLCH`

# Guía de chat — Ecuador Checkbook Custom Module

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.custom.checkbook`).

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

- ¿Cómo puedo registrar un cheque en el sistema?
- ¿Qué información necesito proporcionar para gestionar un cheque?
- ¿Cómo se visualizan las transacciones de cheques en el módulo?
- ¿Dónde encuentro ayuda si tengo problemas con el módulo?
- ¿Qué debo hacer si un cheque es devuelto?
- ¿Hay alguna manera de exportar la información de cheques?
- ¿Cómo se vinculan los cheques con otras transacciones en el ERP?
- ¿Qué medidas de seguridad se aplican a la gestión de cheques?

# Domain — data model

## Functional

Este módulo carece de una entidad cabecera y no presenta etapas o relaciones específicas definidas en su estructura actual, ya que no se han documentado tablas físicas ni relaciones entre datos. No hay disparadores (triggers) definidos en este módulo que afecten a la base de datos. Esto implica que la gestión de datos en relación a cheques no está estructurada en un modelo de datos tradicional suficiente con las funcionalidades requeridas.

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

No se han definido ventanas específicas para la interfaz de usuario de este módulo. La falta de ventanas y menús creados limita la navegación y el acceso a las funcionalidades que podrían ofrecerse a los usuarios en el sistema.

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

Dado que el módulo no presenta botones de procesos definibles ni informes asociados, se infiere que las operaciones típicas de completar, retornar o rechazar no están disponibles. Esto limita considerablemente las interacciones de los usuarios dentro del flujo de trabajo del módulo. Asimismo, no se han establecido validaciones frecuentes que fortalezcan el uso correcto del módulo en la práctica diaria.

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

No se han incluido clases Java en el diseño de este módulo, lo que implica que no existe lógica adicional escrita en Java que complemente las funcionalidades del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.custom.checkbook`.

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

El módulo no cuenta con triggers ni funciones PL definidas, lo que significa que actualmente no hay lógica de base de datos que facilite el soporte o la automatización de procesos en la gestión de cheques. Este vacío en la lógica de backend podría impactar negativamente en la integridad y la eficiencia de las operaciones.

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

Módulo: `ec.com.sidesoft.localization.custom.checkbook`.

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

# Glosario — prefijo `CSCLCH`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `CSCLCH` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.custom.checkbook` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Cash Flow
**Package:** `ec.com.sidesoft.cash.flow`

# Module overview — Sidesoft Cash Flow

## Functional

El módulo Sidesoft Cash Flow tiene como propósito gestionar y reportar el flujo de efectivo dentro del sistema Openbravo. Este módulo permite a los usuarios de negocio llevar un control detallado de los gastos en función de los pagos, facilitando la toma de decisiones financieras. Los actores principales incluyen usuarios de negocio, que utilizan la interfaz para la visualización de datos y generación de informes, y el equipo de soporte L2, encargado de resolver incidencias relacionadas con el módulo. El alcance del módulo está limitado a las funcionalidades de reporte y control del flujo de efectivo, dependiente de la instalación del framework Openbravo 3.0.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/cash/flow` |
| Web | `web/ec.com.sidesoft.cash.flow/` |

### Declared dependencies

- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSCFLW`

# Guía de chat — Sidesoft Cash Flow

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.cash.flow`).

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
- «¿Qué es la tabla sscflw_setup_report_cash?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo acceder al reporte de flujo de efectivo?
- ¿Qué información se necesita para configurar el reporte?
- ¿Hay algún botón para generar el reporte automáticamente?
- ¿Cómo puedo visualizar los gastos en función de los pagos?
- ¿Qué hacer si los datos del reporte no son correctos?
- ¿Se pueden agregar nuevos filtros en el reporte?
- ¿Cómo aseguro que tengo todos los permisos necesarios para acceder al módulo?
- ¿Qué debo hacer si tengo problemas al guardar la configuración del reporte?

# Domain — data model

## Functional

La entidad cabecera principal del módulo es 'sscflw_setup_report_cash', que permite la configuración de los reportes de flujo de efectivo. El modelo de datos incluye tablas modificadas que integran información relevante para los informes de flujo, tales como C_VALIDCOMBINATION, FACT_ACCT, FIN_FINACC_TRANSACTION y FIN_PAYMENT_DETAIL. Aunque no hay etapas estrictamente definidas en el modelo, la relación entre estas tablas asegura una adecuada vinculación de la información económica y financiera con los reportes, garantizando así la exactitud de los datos presentados. No se han definido triggers en este módulo, lo que implica que el manejo de datos se lleva a cabo a través de funciones PL específicas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sscflw_setup_report_cash` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sscflw_setup_report_cash` | sscflw_setup_report_cash | — | — | ad_org_id→ad_org; ad_client_id→ad_client | Detalle enlazado a ad_client, ad_org. | PK `sscflw_setup_repcash_key`; Cols: rep_sequence, name, rep_group, rep_sql, description; `SSCFLW_SETREPCASH_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sscflw_expensive_payout_v` |
| `sscflw_setup_report_cash` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_VALIDCOMBINATION`, `FACT_ACCT`, `FIN_FINACC_TRANSACTION`, `FIN_PAYMENT_DETAIL`

### Views

`SSCFLW_EXPENSIVE_PAYOUT_V`

# Functional — windows and menus

## Functional

El módulo ofrece dos ventanas, 'Configuración Reporte de Flujo de Efectivo' y 'Gastos en función de pagos', que se pueden acceder desde el menú principal. Los usuarios navegan entre estas ventanas para configurar y consultar los reportes de flujo de efectivo, utilizando un diseño intuitivo que habilita el manejo sencillo de la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.cash.flow.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuración Reporte de Flujo de Efectivo | Setup Report Cash Flow |
| Gastos en función de pagos | Expensive in function of payment |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración | Setup | Sí |
| Configuración Reporte de Flujo de Efectivo | Setup Report Cash Flow | No |
| Configuración Reporte de Flujo de Efectivo | Setup Report Cash Flow | No |
| Gastos en función de pagos | Expensive in function of payment | No |
| Reporte de Flujo de Efectivo | Report Cash Flow | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.cash.flow.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuración Reporte de Flujo de Efectivo

- **AD_WINDOW_ID:** `48AEC1B8BC474CE9A9EC1786924155AE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Setup Report Cash Flow | `8AE352714F0141E9AFAF8B7A0CAE1116` | 0 |

### Ventana: Gastos en función de pagos

- **AD_WINDOW_ID:** `ADC73691A8CE4FCBB316991A4F3B0108`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Expensive in function of payment | `D1DEFCE128324056A1D53426B0677EFE` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Expensive in function of payment (ventana: Gastos en función de pagos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 40 | Date | `Fecha` | No | No | — |
| 50 | Amount Payment Out | `Amount_Pay` | No | No | — |
| 60 | Payment | `FIN_Payment_ID` | No | No | — |
| 70 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 75 | Tax ID | `—` | No | No | — |
| 80 | Document Type | `C_Doctype_ID` | No | No | — |
| 85 | Invoice | `C_Invoice_ID` | No | No | — |
| 90 | Amount | `Amount` | No | No | — |
| 100 | G/L Item | `C_Glitem_ID` | No | No | — |
| 110 | Product | `M_Product_ID` | No | No | — |
| 130 | Product Category | `M_Product_Category_ID` | No | No | — |
| 140 | Code Account | `C_Elementvalue_ID` | No | No | — |
| 160 | Account | `Cuenta` | No | No | — |
| 170 | Active | `Isactive` | No | No | — |

### Setup Report Cash Flow (ventana: Configuración Reporte de Flujo de Efectivo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Sequence | `REP_Sequence` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Group by | `REP_Group` | No | No | — |
| 60 | Sql | `REP_Sql` | No | No | — |
| 65 | SQL account | `SQL_Account` | No | No | — |
| 70 | Description | `Description` | No | No | — |
| 90 | Active | `Isactive` | No | No | — |
| 100 | Main Title | `Typeheader` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

En la gestión del flujo de efectivo, el módulo incluye un botón de proceso que permite la ejecución de la generación del reporte de flujo de efectivo. Las validaciones frecuentes incluyen verificar que la información de gasto esté completa y que los pagos estén correctamente asociados a los gastos relevantes. Sin embargo, no se han definido informes adicionales dentro del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.cash.flow.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte de Flujo de Efectivo | Report Cash Flow | Report Cash Flow | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Reporte de Flujo de Efectivo | Report Cash Flow | Report Cash Flow | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte de Flujo de Efectivo | Report Cash Flow | — | — | — |
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

No se han implementado clases Java dentro de este módulo, lo que limita su interacción directa con el código más allá de la lógica de base de datos y funciones PL.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.cash.flow`.

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
| AD_VAL_RULE | — | `Valid User CF` | `AD_USER.AD_USER_ID =@#AD_USER_ID@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El módulo integra una función PL que realiza operaciones específicas para soportar la lógica del flujo de efectivo. Esta función es fundamental, ya que permite la manipulación y procesamiento de datos en conjunto con las tablas modificadas del sistema, asegurando que la trazabilidad y la integridad de la información se mantengan a lo largo del uso del módulo.

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
| `sscflw_get_sqlgroup` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSCFLW_GET_SQLGROUP.xml` |
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

Módulo: `ec.com.sidesoft.cash.flow`.

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

# Glosario — prefijo `SSCFLW`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCFLW` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.cash.flow` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Report Cash Flow` — Reporte de Flujo de Efectivo

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Daily Closing Charge
**Package:** `ec.com.sidesoft.daily.closing.charge`

# Module overview — Daily Closing Charge

## Functional

El módulo 'Daily Closing Charge' se enfoca en la gestión y automatización de los cobros diarios dentro de un entorno empresarial. Su propósito es facilitar la recolección de ingresos diarios de manera efectiva, asegurando una contabilidad precisa y en tiempo real. Los actores principales son los usuarios financieros y contables que interactúan con el sistema para realizar los cobros y generar reportes de transacciones. Este módulo tiene dependencia de otros módulos clave, como 'Advanced Payables and Receivables Management' y la 'Localization of Ecuador - Finances', lo que garantiza su adaptación a normativas locales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/daily/closing/charge` |
| Web | `web/ec.com.sidesoft.daily.closing.charge/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Advanced Payables and Receivables Mngmt
- Core
- Localization of Ecuador - Finances
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SDCC`

# Guía de chat — Daily Closing Charge

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.daily.closing.charge`).

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
- «¿Qué es la tabla sdcc_daily_clossing?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo realizar un cierre diario?
- ¿Qué debo hacer si olvido un cobro diario?
- ¿Puedo modificar un cierre diario ya realizado?
- ¿Cómo puedo ver mis cobros diarios anteriores?
- ¿Qué pasa si un cobro diario no se procesa correctamente?
- ¿Existe alguna validación al generar un cierre diario?
- ¿Dónde se almacenan los detalles de los cobros realizados?
- ¿Cómo navegar entre los diferentes registros de cierre diario?

# Domain — data model

## Functional

El modelo de datos de este módulo incluye la tabla principal 'sdcc_daily_clossing', que actúa como entidad cabecera para los registros de cierre diario. Las relaciones entre las tablas están diseñadas para permitir asociar múltiples detalles de pagos a un solo cierre diario, facilitando así el seguimiento de cada transacción. Aunque actualmente no hay triggers definidos, el módulo utiliza dos funciones PL para la manipulación y validación de datos, garantizando la correcta ejecución de los procesos y el mantenimiento de la integridad de la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sdcc_daily_clossing` |
| `sdcc_daily_clossing_payment` |
| `sdcc_daily_clossingline` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sdcc_daily_clossing` | sdcc_daily_clossing | — | — | c_bpartner_id→c_bpartner; c_costcenter_id→c_costcenter; ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org (+5) | Detalle enlazado a ad_client, c_bpartner, c_costcenter. | PK `sdcc_dc_key`; Cols: c_doctype_id, documentno, paymentdate, c_bpartner_id, description; `SDCC_DC_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `sdcc_daily_clossing_payment` | sdcc_daily_clossing_payment | — | — | ad_client_id→ad_client; sdcc_daily_clossing_id→sdcc_daily_clossing; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sdcc_daily_clossing. | PK `sdcc_pmt_key`; Cols: line, documentno, sdcc_daily_clossing_id, amount; `SDCC_PMT_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); idx `SDCC_DAILY_CLOSSING_PMT` (sdcc_daily_clossing_id) |
| `sdcc_daily_clossingline` | sdcc_daily_clossingline | — | — | ad_client_id→ad_client; sdcc_daily_clossing_id→sdcc_daily_clossing; c_invoice_id→c_invoice; ad_org_id→ad_org | Detalle enlazado a ad_client, c_invoice, sdcc_daily_clossing. | PK `sdcc_dcl_key`; Cols: line, documentno, c_invoice_id, detailtrx, grandtotalamount; `SDCC_DCL_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); idx `SDCC_DAILY_CLOSSING_LINES` (sdcc_daily_clossing_id) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sdcc_daily_clossing` |
| `sdcc_daily_clossing_payment` |
| `sdcc_daily_clossingline` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación por el módulo se realiza a través de la ventana 'Cobro de cierre diario', donde los usuarios pueden acceder a las distintas pestañas y opciones de configuración. La interfaz de usuario está diseñada para ser intuitiva, permitiendo a los usuarios realizar operaciones con facilidad a través de botones y formularios claros.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.daily.closing.charge.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Cobro de cierre diario | Daily Clossing |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Cobro de cierre diario | Daily Clossing | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.daily.closing.charge.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Cobro de cierre diario

- **AD_WINDOW_ID:** `102360ACA82944749866C6B7D5E32DE6`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `85C3F09140EE430399EB08049A037A84` | 0 |
| 20 | Lines | `A0EB74EC9E9643EF828633A682DE537B` | 1 |
| 30 | Lines Payments | `6A53BBAA60F4446CB3087524B3304438` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Lines (ventana: Cobro de cierre diario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Line No. | `Line` | No | Sí | — |
| 40 | Document No. | `Documentno` | No | Sí | — |
| 70 | Business Partner | `—` | No | Sí | — |
| 75 | Grandtotalamount | `Grandtotalamount` | No | Sí | — |
| 80 | Total Paid | `Totalpaid` | No | Sí | — |
| 90 | Outstandingamount | `Outstandingamount` | No | Sí | — |
| 510 | Process | `Process` | No | No | — |
| 1000 | Active | `Isactive` | No | No | — |

### Lines Payments (ventana: Cobro de cierre diario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Line No. | `Line` | No | Sí | — |
| 40 | Document No. | `Documentno` | No | Sí | — |
| 45 | Amount | `Amount` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Header (ventana: Cobro de cierre diario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `Documentno` | No | Sí | — |
| 50 | Payment Date | `Paymentdate` | No | No | — |
| 58 | Starting Date | `Datefrom` | No | No | 8D7ED551578E476986CCFA7B2E7E085E |
| 59 | Ending Date | `Dateto` | No | No | 8D7ED551578E476986CCFA7B2E7E085E |
| 60 | Business Partner | `C_Bpartner_ID` | No | No | 8D7ED551578E476986CCFA7B2E7E085E |
| 61 | Valuefrom | `Valuefrom` | No | No | 8D7ED551578E476986CCFA7B2E7E085E |
| 62 | Valueto | `Valueto` | No | No | 8D7ED551578E476986CCFA7B2E7E085E |
| 80 | Payment Method | `FIN_Paymentmethod_ID` | No | No | 90E096DAE11B47C29D6C2D93E7A87D97 |
| 90 | Financial Account | `FIN_Financial_Account_ID` | No | No | 90E096DAE11B47C29D6C2D93E7A87D97 |
| 190 | C_Doctype_Payment_ID | `C_Doctype_Payment_ID` | No | No | 90E096DAE11B47C29D6C2D93E7A87D97 |
| 195 | Reference No. | `Referenceno` | No | No | 90E096DAE11B47C29D6C2D93E7A87D97 |
| 200 | Cost Center | `C_Costcenter_ID` | No | No | 90E096DAE11B47C29D6C2D93E7A87D97 |
| 225 | 1st Dimension | `User1_ID` | No | No | 90E096DAE11B47C29D6C2D93E7A87D97 |
| 228 | G/L Item | `C_Glitem_ID` | No | No | 90E096DAE11B47C29D6C2D93E7A87D97 |
| 230 | Description | `Description` | No | No | 90E096DAE11B47C29D6C2D93E7A87D97 |
| 240 | Active | `Isactive` | No | No | 90E096DAE11B47C29D6C2D93E7A87D97 |
| 1400 | Execute Payment | `Executepayment` | No | No | — |
| 1410 | sdcc_ChangeRPTStatus | `Readytoprocess` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye procesos típicos que son ejecutados mediante tres botones: completar, retornar y rechazar. Cada uno de estos procesos lleva a cabo funciones específicas relacionadas con el manejo de los cobros diarios, asegurando que todas las transacciones sean registradas correctamente. Sin embargo, no se generan informes adicionales desde el módulo, aunque es común que se realicen validaciones de datos frecuentes para evitar inconsistencias durante el manejo operativo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.daily.closing.charge.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Realizar Cobro | Execute Payment | SdccExecutePayment | Java `Sdcc_AutoCharge` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sdcc_Daily_Clossing_ID`, No se encontró el registro de cierre diario.; No se encontró un tipo de documento para el pago.; No se selecciono ninguna transacción para realiza… | `src/ec/com/sidesoft/daily/closing/charge/ad_process/Sdcc_AutoCharge.java` |
| Botón (PL/pgSQL) | Generate Schedule detail | Generate Schedule detail | Generate Schedule detail | `sdcc_generate_scheduledetail` | Verificar si el SELECT no encontró resultados | — |
| Botón (PL/pgSQL) | Listo para Procesar | sdcc_ChangeRPTStatus | sdcc_ChangeRPTStatus | `sdcc_updateRTPstatus` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
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
| Botón (Java) | Realizar Cobro | `Sdcc_AutoCharge` | Proceso Java (toolbar/background) | `Sdcc_Daily_Clossing_ID` | No se encontró el registro de cierre diario.; No se encontró un tipo de documento para el pago.; No se selecciono ninguna transacción para realizar el cobro. | `src/ec/com/sidesoft/daily/closing/charge/ad_process/Sdcc_AutoCharge.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Realizar Cobro | Execute Payment | SdccExecutePayment | Java `Sdcc_AutoCharge` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sdcc_Daily_Clossing_ID`, No se encontró el registro de cierre diario.; No se encontró un tipo de documento para el pago.; No se selecciono ninguna transacción para realiza… | `src/ec/com/sidesoft/daily/closing/charge/ad_process/Sdcc_AutoCharge.java` |
| Botón (PL/pgSQL) | Generate Schedule detail | Generate Schedule detail | Generate Schedule detail | `sdcc_generate_scheduledetail` | Verificar si el SELECT no encontró resultados | — |
| Botón (PL/pgSQL) | Listo para Procesar | sdcc_ChangeRPTStatus | sdcc_ChangeRPTStatus | `sdcc_updateRTPstatus` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Realizar Cobro | Execute Payment | Java `Sdcc_AutoCharge` | Proceso Openbravo registro `Sdcc_Daily_Clossing_ID`, No se encontró el registro de cierre diario.; No se encontró un tipo de documento para el pago.; No se selecciono ninguna transacción para realiza… | No se encontró el registro de cierre diario.; No se encontró un tipo de documento para el pago.; No se selecciono ninguna transacción para realizar el cobro. |
| Botón (PL/pgSQL) | Generate Schedule detail | Generate Schedule detail | PL `sdcc_generate_scheduledetail` | Verificar si el SELECT no encontró resultados | Verificar si el SELECT no encontró resultados |
| Botón (PL/pgSQL) | Listo para Procesar | sdcc_ChangeRPTStatus | PL `sdcc_updateRTPstatus` | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
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

El módulo contiene varias clases Java que manejan la lógica de negocio, incluida la gestión de eventos relacionados con la creación, actualización y eliminación de registros en el cierre diario. Estas clases permiten expandir la funcionalidad del módulo, proporcionando una integración más estrecha con el sistema ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.daily.closing.charge`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `DocumentNoDailyClosingCharge` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/daily/closing/charge/ad_callouts/DocumentNoDailyClosingCharge.java` |
| `SdccDailyClossingLineEventHandler` | ad_events | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/daily/closing/charge/ad_events/SdccDailyClossingLineEventHandler.java` |
| `Sdcc_AutoCharge` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/daily/closing/charge/ad_process/Sdcc_AutoCharge.java` |
| `Sdcc_AutomaticCharge` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/daily/closing/charge/ad_process/Sdcc_AutomaticCharge.java` |
| `AdvPaymentMngtDao` | dao | BaseOBObject | — | `src/ec/com/sidesoft/daily/closing/charge/dao/AdvPaymentMngtDao.java` |
| `Sdcc_Helper` | utils | — | — | `src/ec/com/sidesoft/daily/closing/charge/utils/Sdcc_Helper.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `FIN_FINACC_PAYMENTMETHOD Daily Closing Charge` | `EXISTS (SELECT 1 
FROM FIN_FINACC_PAYMENTMETHOD 
WHERE FIN_FINACC_PAYMENTMETHOD.FIN_PAYMENTMETHOD_ID = FIN_PAYMENTMETHOD` |
| AD_VAL_RULE | — | `DOCTYPE PAYMENT Daily Closing Charge` | `C_DocType.DocBaseType IN ('APP', 'ARR') AND C_DocType.IsSOTrx='Y' AND AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.AD_Org_ID, ` |
| AD_VAL_RULE | — | `FIN_FINANCIAL_ACCOUNT Daily Closing Charge` | `EXISTS (SELECT 1 
FROM FIN_FINACC_PAYMENTMETHOD 
WHERE FIN_FINACC_PAYMENTMETHOD.FIN_PAYMENTMETHOD_ID = @FIN_Paymentmetho` |
| AD_VAL_RULE | — | `Doctype Closing Charge` | `C_DocType.ad_table_id in ('85C3F09140EE430399EB08049A037A84') AND C_DocType.DocBaseType in ('SDCC_APP')` |
| Java event/validator | `SdccDailyClossingLineEventHandler` | persistencia/UI | *(leer `src/ec/com/sidesoft/daily/closing/charge/ad_events/SdccDailyClossingLineEventHandler.java`)* |
| Función PL `sdcc_generate_scheduledetail` | — | invocación proceso | Verificar si el SELECT no encontró resultados |
| Función PL `sdcc_updatertpstatus` | — | invocación proceso | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL juegan un papel crucial en el soporte del módulo, ya que estas últimas son utilizadas para ejecutar lógicas de negocio específicas como la generación automática de pagos o la validación de datos al momento de las transacciones. Estas funciones aseguran que los datos se procesen de manera eficiente y conforme a las reglas establecidas en el sistema.

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
| `sdcc_generate_scheduledetail` | Generate Schedule detail | Verificar si el SELECT no encontró resultados | Verificar si el SELECT no encontró resultados | `model/functions/SDCC_GENERATE_SCHEDULEDETAIL.xml` |
| `sdcc_updatertpstatus` | Listo para Procesar | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; | `model/functions/SDCC_UPDATERTPSTATUS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Realizar Cobro | `SdccExecutePayment` | Botón (Java) | Java `Sdcc_AutoCharge` | N | Proceso Openbravo registro `Sdcc_Daily_Clossing_ID`, No se encontró el registro de cierre diario.; No se encontró un tipo de documento para el pago.; No se selecciono ninguna trans |
| 2 | Generate Schedule detail | `Generate Schedule detail` | Botón (PL/pgSQL) | PL `sdcc_generate_scheduledetail` | N | Verificar si el SELECT no encontró resultados |
| 3 | Listo para Procesar | `sdcc_ChangeRPTStatus` | Botón (PL/pgSQL) | PL `sdcc_updateRTPstatus` | N | RAISE_APPLICATION_ERROR(-20100, v_ResultStr) ; |

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

Módulo: `ec.com.sidesoft.daily.closing.charge`.

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

# Glosario — prefijo `SDCC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SDCC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.daily.closing.charge` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `SdccExecutePayment` — Realizar Cobro
- `Generate Schedule detail` — Generate Schedule detail
- `sdcc_ChangeRPTStatus` — Listo para Procesar

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Standard  - Automatic Reconcilation Report
**Package:** `ec.com.sidesoft.reconcilation.reports`

# Module overview — Standard  - Automatic Reconcilation Report

## Functional

El módulo 'Standard - Automatic Reconciliation Report' está diseñado para facilitar la conciliación automática de tickets en Openbravo. Los actores principales incluyen los usuarios de negocio encargados de la conciliación financiera y los desarrolladores que mantienen la infraestructura del ERP. Este módulo permite a los usuarios obtener informes de conciliación automática, optimizando así el proceso de verificación de pagos y facturas. Su implementación requiere de compatibilidad con múltiples elementos del sistema, incluyendo el 'Core' y otras dependencias del framework de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/reconcilation/reports` |
| Web | `web/ec.com.sidesoft.reconcilation.reports/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework
- Withholdings Of Paid Invoices

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SRRPT`

# Guía de chat — Standard  - Automatic Reconcilation Report

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.reconcilation.reports`).

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

- ¿Cómo puedo generar un informe de conciliación automática?
- ¿Qué dependencias son necesarias para el módulo?
- ¿Dónde acceso la opción para ejecutar el informe?
- ¿Existen validaciones que deba considerar antes de generar el informe?
- ¿Cuál es el propósito principal del informe de conciliación?
- ¿Dónde se almacenan los resultados de la conciliación generada?
- ¿Este módulo afecta mis reportes financieros actuales?
- ¿A quién contactar si tengo problemas con el módulo?

# Domain — data model

## Functional

El módulo no contiene tablas físicas propias, pero está vinculado al proceso de conciliación de pagos a través de sus informes. Este módulo se basa en un único proceso que permite generar informes de conciliación automática, lo cual es esencial para mantener un flujo financiero claro y organizado. Aunque no hay triggers o funciones PL definidas, el proceso de generación de informes es una etapa clave que respalda la funcionalidad del módulo.

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

Este módulo no cuenta con ventanas específicas ni un diseño de interfaz dedicada, pero se integra en la experiencia de usuario de Openbravo a través de un menú. Los usuarios pueden acceder al informe de conciliación automática desde este menú, lo que permite la navegación rápida y eficiente dentro del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.reconcilation.reports.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Reporte Conciliación Automatica Mensual | Automatic Reconciliation Report | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.reconcilation.reports.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso para la generación del informe de conciliación automática. Este proceso posee un botón de ejecución que permite a los usuarios completar la tarea y obtener el informe deseado. Es recomendable que los usuarios revisen las validaciones frecuentes relacionadas con la conciliación antes de ejecutar el informe para asegurar resultados precisos y adecuados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.reconcilation.reports.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Conciliación Automatica Mensual | Automatic Reconciliation Report | Automatic Reconciliation Report | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Reporte Conciliación Automatica Mensual | Automatic Reconciliation Report | Automatic Reconciliation Report | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Conciliación Automatica Mensual | Automatic Reconciliation Report | — | — | — |
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

El módulo no emplea clases Java específicas, lo que indica que su funcionalidad se basa en componentes del framework de Openbravo sin extensiones personalizadas en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.reconcilation.reports`.

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
| AD_VAL_RULE | — | `Fin_Financial_Account_Estandar` | `FIN_Financial_Account.FIN_Matching_Algorithm_ID in (
select FIN_Matching_Algorithm_ID from FIN_Matching_Algorithm where ` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Dado que el módulo no incluye triggers ni funciones PL, no hay un papel directo de estos elementos en el soporte del módulo. Sin embargo, la generación de informes puede depender de la integridad y precisión de las tablas físicas relacionadas con facturas y pagos en el sistema, que sí utilizan triggers y funciones para mantener datos consistentes.

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

Módulo: `ec.com.sidesoft.reconcilation.reports`.

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

# Glosario — prefijo `SRRPT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SRRPT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.reconcilation.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Automatic Reconciliation Report` — Reporte Conciliación Automatica Mensual

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
