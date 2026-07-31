# Openbravo Sidesoft — Retenciones

> Retenciones en compras y ventas, ATS, formularios 103/104, control de retenciones, datasets SRI.

**Paquetes incluidos (16):**
- `com.sidesoft.localization.ecuador.withholdings` — Localization of Ecuador - Withholdings
- `com.sidesoft.localization.ecuador.withholdings.dataset` — Datasets ATS - Purchases and sales withholdings
- `com.sidesoft.localization.ecuador.withholdings.paidinvoices` — Withholdings Of Paid Invoices
- `com.sidesoft.localization.ecuador.withholdings.reports` — Localization of Ecuador - Reports
- `com.sidesoft.localization.ecuador.payments.withholdings` — Customization Payment In - Withholdings Modules
- `ec.com.sidesoft.localization.ecuador.withholdingssales` — Localization of Ecuador - Withholdings Sales
- `ec.com.sidesoft.localization.withholding.control` — Control Withholding
- `ec.com.sidesoft.bpartner.search.withholdings` — Business Partner Search Withholdings Modules
- `ec.com.sidesoft.bpartner.search.withholdings.se_ES` — Traducción Búsqueda Terceros - Comprobante de Retención
- `ec.com.sidesoft.custom.withholding.payment` — Custom Withholding Payment
- `ec.com.sidesoft.withholding.summarys` — Sidesoft Withholding Summarys Readonly
- `ec.com.sidesoft.withholdings.advanced.formulary` — Advanced Process Formulary 103 and 104
- `ec.com.sidesoft.xml.irbp` — XML IRBP
- `ec.com.sidesoft.irbp.reports` — IRBP Reports
- `ec.com.sideosft.localization.datasets` — Ecuador Localization Dataset
- `ec.com.sidesoft.localization.rimpe` — Sidesoft Localizacion RIMPE


---
## Localization of Ecuador - Withholdings
**Package:** `com.sidesoft.localization.ecuador.withholdings`

# Module overview — Localization of Ecuador - Withholdings

## Functional

El módulo de Localización de Ecuador - Retenciones está diseñado para gestionar las retenciones de compras y ventas en Ecuador. Su propósito es asegurar que las empresas cumplan con las normativas fiscales mediante el manejo adecuado de las retenciones tributarias. Los actores principales incluyen usuarios de negocio encargados de la administración fiscal, así como desarrolladores y personal de soporte que pueden necesitar implementar personalizaciones o resolver incidencias. El alcance del módulo incluye la generación de formularios de retención, el registro de retenciones aplicadas en transacciones contables, y la integración con otros módulos de finanzas. Las dependencias relevantes son la compatibilidad con versiones específicas de Openbravo y otros módulos relacionados con finanzas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/localization/ecuador/withholdings` |
| Web | `web/com.sidesoft.localization.ecuador.withholdings/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Localization of Ecuador - Finances

### Version

**0.1.0** (from `AD_MODULE.xml`).

### DB prefix

`SSWH`

# Guía de chat — Localization of Ecuador - Withholdings

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.localization.ecuador.withholdings`).

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
- «¿Qué es la tabla sswh_receipt_tax?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar una retención de impuestos en una factura?
- ¿Qué formularios debo presentar para mis retenciones?
- ¿Cómo actualizo la información de mi organización en el módulo?
- ¿Dónde puedo encontrar los informes de retención generados?
- ¿Qué validaciones debo considerar al ingresar datos de retención?
- ¿Cómo se calcula el monto de la retención para mis transacciones?
- ¿Qué debo hacer si el número de autorización de una factura no es válido?
- ¿Cómo puedo acceder a la ayuda del módulo si encuentro un error?

# Domain — data model

## Functional

La entidad central del módulo es la tabla sswh_receipt_tax, que almacena la información de las retenciones aplicadas a invoices. Las etapas del proceso incluyen la creación de comprobantes de retención, validación de autorizaciones fiscales, y la preparación de formularios para su impresión y presentación a la autoridad tributaria. Las relaciones clave se establecen con tablas como c_invoice, c_bpartner, y otras que contienen información relevante de socios comerciales y documentos fiscales. Entre los triggers más importantes se encuentran SSWH_AUTORIZATION_TRG, que se asegura de que el número de autorización de una factura cumpla ciertos criterios, y varios triggers asociados a c_invoice que validan la integridad de los datos que se almacenan y procesan en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sswh_amountldm` |
| `sswh_authorization` |
| `sswh_checkbook` |
| `sswh_checkbookline` |
| `sswh_checkbookpos` |
| `sswh_checkbookposline` |
| `sswh_codelivelihoodt` |
| `sswh_countrypayment` |
| `sswh_dc_note` |
| `sswh_form_aux` |
| `sswh_form_codesline103` |
| `sswh_form_codesline104` |
| `sswh_formulary` |
| `sswh_formulary_codes` |
| `sswh_formularyline` |
| `sswh_inv_exportation` |
| `sswh_livelihoodt` |
| `sswh_other_document` |
| `sswh_pos` |
| `sswh_receipt` |
| `sswh_receipt_tax` |
| `sswh_rpt_ats_purchase` |
| `sswh_rpt_ats_sales` |
| `sswh_rpt_ats_with_purchase` |
| `sswh_rptc_orginform` |
| `sswh_rptc_purchasedet` |
| `sswh_rptc_purchasepaym` |
| `sswh_rptc_purchasewith` |
| `sswh_rptc_salesbystab` |
| `sswh_rptc_salesbystaborg` |
| `sswh_rptc_salescomp` |
| `sswh_rptc_salesdet` |
| `sswh_rptc_salespayform` |
| `sswh_rptc_salesrefund` |
| `sswh_rptc_salesvoided` |
| `sswh_rptc_sql` |
| `sswh_salestickets` |
| `sswh_source` |
| `sswh_taxpayer` |
| `sswh_taxregime` |
| `sswh_termpayment` |
| `sswh_transaction_type` |
| `sswh_typereceipt` |
| `sswh_withh_card_credit` |
| `sswh_withholding` |
| `sswh_withholding_source` |
| `sswh_withholding_vendor` |
| `sswh_withholdings_voided` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sswh_amountldm` | SSWH_Amountldm | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_amountldm_key`; Cols: amount, productov; `SSWH_AMOUNTLDM_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `sswh_authorization` | SSWH_Authorization | — | `SSWH_AUTHORIZATIONNO_UN` (c_doctype_id, authorizationno, establishment, cashregister) | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `sswh_authorization_key`; Cols: establishment, cashregister, datefrom, dateto, authorizationno; `SSWH_AUTHORIZA_DATEFROM_DATETO`: DATEFROM <= DATETO; `SSWH_AUTHORIZA_NUMBFROM_NUMBTO`: NUMBERFROM <= NUMBERTO (+1) |
| `sswh_checkbook` | SSWH_checkbook | `SSWH_CHECKBOOK_TR`; `SSWH_CHECKBOOK_TR1` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bankaccount_id→c_bankaccount; c_currency_id→c_currency | Detalle enlazado a ad_client, ad_org, c_bankaccount. Validado por trigger(s): SSWH_CHECKBOOK_TR, SSWH_CHECKBOOK_TR1. | PK `sswh_checkbook_pkey`; Cols: c_bankaccount_id, c_currency_id, bankaccounttype, genericaccount, typecheck |
| `sswh_checkbookline` | SSWH_Checkbookline | — | — | c_bankstatementline_id→c_bankstatementline; ad_client_id→ad_client; ad_org_id→ad_org; sswh_checkbook_id→sswh_checkbook | Detalle enlazado a ad_client, ad_org, c_bankstatementline. | PK `sswh_checkbookline_pkey`; Cols: doc_line_status, c_bankstatementline_id, linecheck, sswh_checkbook_id, generate_status |
| `sswh_checkbookpos` | SSWH_Checkbookpos | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bank_id→c_bank; c_currency_id→c_currency; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, ad_org, c_bank. | PK `sswh_checkbookpos_pkey`; Cols: c_currency_id, bankaccounttype, genericaccount, typecheck, generateto |
| `sswh_checkbookposline` | SSWH_CheckbookposLine | `SSWH_CHECKBOOKPOSLINE_TR`; `SSWH_CHECKBOOKPOSLINE_TR1` | — | ad_client_id→ad_client; ad_org_id→ad_org; sswh_checkbookpos_id→sswh_checkbookpos; c_debt_payment_id→c_debt_payment; c_invoice_id→c_invoice (+1) | Detalle enlazado a ad_client, ad_org, sswh_checkbookpos. Validado por trigger(s): SSWH_CHECKBOOKPOSLINE_TR, SSWH_CHECKBOOKPOSLINE_TR1. | PK `sswh_checkbookposline_pkey`; Cols: sswh_checkbookpos_id, c_invoice_id, granttotal, c_debt_payment_id, c_bpartner_id |
| `sswh_codelivelihoodt` | SSWH_Codelivelihoodt | — | `SSWH_CODELIVELIHOODT_VALUE` (value) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_clivelihoodt_pkey`; Cols: value, name, description, applies_withholding |
| `sswh_countrypayment` | sswh_countrypayment | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_countrypayment_key`; Cols: value, name, description; `SSWH_COUNTRYPAYMENT_ISACT_FK`: ISACTIVE IN ('Y', 'N') |
| `sswh_dc_note` | sswh_dc_note | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoice_id→c_invoice | Detalle enlazado a ad_client, ad_org, c_invoice. | PK `sswh_dc_note_key`; Cols: c_invoice_id, tipo_comprobante, establecimmiento, caja, secuencia; `SSWH_DC_NOTE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_DC_NOTE_IDX1` (process) |
| `sswh_form_aux` | sswh_form_aux | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_form_aux_key`; Cols: father_code, baseamount, son_code, taxamount, formula; `SSWH_FORM_AUX_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_form_codesline103` | sswh_form_codesline103 | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sswh_formulary_codes_id→sswh_formulary_codes | Detalle enlazado a ad_client, ad_org, sswh_formulary_codes. | PK `sswh_form_codesline103_key`; Cols: sswh_formulary_codes_id, line, father_code, son_code, formula; `SSWH_FRMCDLN103_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_form_codesline104` | sswh_form_codesline104 | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sswh_formulary_codes_id→sswh_formulary_codes | Detalle enlazado a ad_client, ad_org, sswh_formulary_codes. | PK `sswh_form_codesline104_key`; Cols: sswh_formulary_codes_id, line, father_code, son_code, formula; `SSWH_FRMCDLN104_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_formulary` | sswh_formulary | `SSWH_FORMULARY_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. Validado por trigger(s): SSWH_FORMULARY_TRG. | PK `sswh_formulary_key`; Cols: formulary_type, startdate, enddate, name, process; `SSWH_FORMULARY_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_formulary_codes` | sswh_formulary_codes | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_form_codes_key`; Cols: name, description; `SSWH_FORM_CODES_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_formularyline` | sswh_formularyline | `SSWH_FORMULARYLINE_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; sswh_formulary_id→sswh_formulary | Detalle enlazado a ad_client, ad_org, sswh_formulary. Validado por trigger(s): SSWH_FORMULARYLINE_TRG. | PK `sswh_formularyline_key`; Cols: sswh_formulary_id, father_code, baseamount, son_code, taxamount; `SSWH_FORMULARYLINE_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_inv_exportation` | sswh_inv_exportation | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoice_id→c_invoice | Detalle enlazado a ad_client, ad_org, c_invoice. | PK `sswh_inv_exportation_key`; Cols: c_invoice_id, client_type, client_identif, relation_part, identifier_type; `SSWH_INVEXP_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_livelihoodt` | SSWH_Livelihoodt | — | `SSWH_LIVELIHOODT_VALUE` (value) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_livelihoodt_pkey`; Cols: value, name, description, isrefund, isexcludedrefund |
| `sswh_other_document` | SSWH_Other_document | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_other_document_pkey`; Cols: name, description |
| `sswh_pos` | SSWH_Pos | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bank_id→c_bank; c_doctype_id→c_doctype; c_paymentterm_id→c_paymentterm (+1) | Detalle enlazado a ad_client, ad_org, c_bank. | PK `sswh_pos_id_key`; Cols: c_doctype_id, c_paymentterm_id, c_bp_taxcategory_id, documentno, date_pos; `SSWH_POS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_receipt` | SSWH_Receipt | `SSWH_RECEIPT_TRG` | `SSWH_RECEIPT_DOCUMENTNO_UN` (documentno) | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_doctype_id→c_doctype; c_invoice_id→c_invoice | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SSWH_RECEIPT_TRG. | PK `sswh_receipt_key`; Cols: documentno, datedoc, reference, totalwithholdingincome, totalwithholdingvat; `SSWH_RECEIPT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_receipt_tax` | SSWH_Receipt_Tax | `SSWH_RECEIPT_TAX_TRG` | `SSWH_RECEIPT_TAX_TAX_UN` (sswh_receipt_id, c_tax_id) | ad_client_id→ad_client; ad_org_id→ad_org; fin_financial_account_id→fin_financial_account; c_invoicetax_id→c_invoicetax; fin_paymentmethod_id→fin_paymentmethod (+2) | Detalle enlazado a ad_client, ad_org, fin_financial_account. Validado por trigger(s): SSWH_RECEIPT_TAX_TRG. | PK `sswh_receipt_tax_key`; Cols: line, sswh_receipt_id, c_tax_id, taxamt, taxbaseamt; `SSWH_RECEIPT_TAX_ACTIVE_CK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RECEIPT_TAX_IT` (c_invoicetax_id) |
| `sswh_rpt_ats_purchase` | SSWH_Rpt_Ats_Purchase | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_rpt_ats_purchase_key`; Cols: empresa, linea, codsustento, tpidprov, idprov; `SSWH_R_A_PURCHASE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_rpt_ats_sales` | SSWH_Rpt_Ats_Sales | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_rpt_ats_sales_key`; Cols: empresa, linea, tpidcliente, idcliente, tipocomprobante; `SSWH_R_A_SALES_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `sswh_rpt_ats_with_purchase` | SSWH_Rpt_Ats_With_Purchase | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_rpt_ats_with_purchase_key`; Cols: linea, empresa, plinea, codretair, base; `SSWH_R_A_W_PURCH_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_rptc_orginform` | Sswh_Rptc_OrgInform | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_rptc_orginform_key`; Cols: social_name, identif, sswh_taxidtype, process; `SSWH_RPTC_OF_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_ORGINFORM_IDX1` (process) |
| `sswh_rptc_purchasedet` | Sswh_Rptc_PurchaseDet | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoice_id→c_invoice | Detalle enlazado a ad_client, ad_org, c_invoice. | PK `sswh_rptc_pdet_key`; Cols: autori_retencion, autorizacion, autorizacion_nc, base_iva_cero, base_iva_doce; `SSWH_RPTC_PD_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_PD_IDX` (process) |
| `sswh_rptc_purchasepaym` | Sswh_Rptc_PurchasePaym | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_rptc_purch_key`; Cols: documentno, forma_pago, dateacct, dateinvoiced, process; `SSWH_RPTC_PP_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_PPM_IDX` (process) |
| `sswh_rptc_purchasewith` | Sswh_Rptc_PurchaseWith | — | — | ad_org_id→ad_org; c_bpartner_id→c_bpartner; ad_client_id→ad_client | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sswh_rptc_purchasewith_key`; Cols: documentno, document, name, codigo_ret, base_imp; `SSWH_RPTC_PW_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_PPW_IDX` (process) |
| `sswh_rptc_salesbystab` | Sswh_Rptc_SalesByStab | — | — | ad_org_id→ad_org; ad_client_id→ad_client | Detalle enlazado a ad_client, ad_org. | PK `sswh_rptc_salesbystab_key`; Cols: establecimiento, valor, dateacct, compensacion, documentno; `SSWH_RPTC_SSTAB_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_SBS_IDX` (process) |
| `sswh_rptc_salesbystaborg` | sswh_rptc_salesbystaborg | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_rptc_salesbystaborg_key`; Cols: establecimiento, valor, compensacion, process; `SSWH_RPTC_SLSBSTBO_ISA_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_SBSO_IDX` (process) |
| `sswh_rptc_salescomp` | sswh_rptc_salescomp | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_rptc_salescomp_key`; Cols: comp_type, compensated_amount, process; `SSWH_RPTC_SC_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_SC_IDX` (process) |
| `sswh_rptc_salesdet` | Sswh_Rptc_SalesDet | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_period_id→c_period | Detalle enlazado a ad_client, ad_org, c_period. | PK `sswh_rptc_salesdet_key`; Cols: tipo_identificador, identif_cliente, cod_tipo_comprobante, count, base_no_iva; `SSWH_RPTC_SLSD_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_SALESDET_IDX1` (process) |
| `sswh_rptc_salespayform` | sswh_rptc_salespayform | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_rptc_salespayform_key`; Cols: value, process, identif_cliente; `SSWH_RPTC_SF_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_SPF_IDX1` (process); idx `SSWH_RPTC_SSPY_IDX2` (process, identif_cliente) |
| `sswh_rptc_salesrefund` | Sswh_Rptc_SalesRefund | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoice_id→c_invoice | Detalle enlazado a ad_client, ad_org, c_invoice. | PK `sswh_rptc_salesrefund_key`; Cols: codigo_compra, tipo_comp_reemb, tipo_identificador, identificador_proveedor, establecimiento; `SSWH_RPTC_SREF_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_SR_IDX1` (process) |
| `sswh_rptc_salesvoided` | Sswh_Rptc_SalesVoided | — | — | ad_org_id→ad_org; ad_client_id→ad_client | Detalle enlazado a ad_client, ad_org. | PK `sswh_rptc_salesvoided_key`; Cols: tipo_identificador, establecimiento, punto_emision, secuencia_inicio, secuencia_final; `SSWH_RPTC_SLSV_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSWH_RPTC_SV_IDX1` (process) |
| `sswh_rptc_sql` | sswh_rptc_sql | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_rptc_sql_key`; Cols: name, sqlscript, description; `SSWH_RPTC_SQL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_salestickets` | sswh_salestickets | — | — | sswh_transaction_type_id→sswh_transaction_type; ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_doctype_id→c_doctype (+2) | Detalle enlazado a ad_client, ad_org, sswh_transaction_type. | PK `sswh_salestickets_key`; Cols: c_doctype_id, documentno, c_bpartner_id, c_invoice_id, date_doc; `SSWH_SSTICKET_ISACTV_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_source` | SSWH_Source | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_tax_id→c_tax; sswh_withholding_source_id→sswh_withholding_source | Detalle enlazado a ad_client, ad_org, c_tax. | PK `sswh_source_key`; Cols: sswh_withholding_source_id, c_tax_id, code; `SSWH_SOURCE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_taxpayer` | SSWH_Taxpayer | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_taxpayer_key`; Cols: name, description, specialtaxpayer, requiredaccounting, value; `SSWH_TAXPAYER_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSWH_TAXPAYER_REQUIREDACCT_CHK`: REQUIREDACCOUNTING IN ('Y', 'N') (+1) |
| `sswh_taxregime` | SSWH_TaxRegime | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_taxregime_key`; Cols: value, name; `SSWH_TAXREGIME_ISACT_CHK`: ISACTIVE IN ('Y', 'N'); `SSWH_TAXREGIME_VALUE_CHK`: (LENGTH(TRIM(TRANSLATE((VALUE), '0123456789', ' '))) = 0) AN |
| `sswh_termpayment` | SSWH_Termpayment | — | `SSWH_TERMP_UNIQUE` (name, value) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_termpayment_key`; Cols: value, name, description, closed_credit; `SSWH_TERMP_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_transaction_type` | Sswh_Transaction_Type | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_transaction_type_key`; Cols: code, name, iselectronic; `SSWH_ISELECTRONIC_CHK`: ISELECTRONIC IN ('Y', 'N'); `SSWH_TRANSTYPE_ISACTV_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_typereceipt` | sswh_typereceipt | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_typereceipt_key`; Cols: value, name, description; `SSWH_TYPERECEIPT_ISACT_FK`: ISACTIVE IN ('Y', 'N') |
| `sswh_withh_card_credit` | sswh_withh_card_credit | `SSWH_WITHH_CARD_TRG` | — | sswh_transaction_type_id→sswh_transaction_type; fin_paymentmethod_id→fin_paymentmethod; ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner (+2) | Detalle enlazado a ad_client, fin_paymentmethod, sswh_transaction_type. Validado por trigger(s): SSWH_WITHH_CARD_TRG. | PK `sswh_withh_card_credit_key`; Cols: c_doctype_id, documentno, c_bpartner_id, c_invoice_id, date_doc; `SSWH_PROCESSED_CHECK`: PROCESSED IN ('Y', 'N'); `SSWH_PROCESSING_CHECK`: PROCESSING IN ('Y', 'N') (+1) |
| `sswh_withholding` | SSWH_Withholding | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_tax_goods_id→c_tax; c_tax_services_id→c_tax; sswh_taxpayer_id→sswh_taxpayer (+1) | Detalle enlazado a ad_client, ad_org, c_tax. | PK `sswh_withholding_key`; Cols: sswh_taxpayer_id, sswh_taxpayer_ref_id, c_tax_goods_id, c_tax_services_id; `SSWH_WITHHOLDING_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_withholding_source` | SSWH_Withholding_Source | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sswh_withholding_source_key`; Cols: name, description; `SSWH_WITHHOLDIN_SRC_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sswh_withholding_vendor` | SSWH_Withholding_vendor | `SSWH_VALIDATEAUTHORIZATION_TRG` | `SSWH_VENDOR_AUTHORIZATION_UN` (c_bpartner_id, withholdingauthorization, stablishment, shell) | ad_client_id→ad_client; c_bpartner_id→c_bpartner; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SSWH_VALIDATEAUTHORIZATION_TRG. | PK `sswh_withholding_vendor_key`; Cols: c_bpartner_id, withholdingauthorization, shell, stablishment, datefrom; `SSWH_WITHH_VEN_DATEFROM_DATETO`: DATEFROM <= DATETO; `SSWH_WITHH_VEN_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') (+1) |
| `sswh_withholdings_voided` | sswh_withholdings_voided | `SSWH_WITHH_AUTHORIZATIONNO_TRG`; `SSWH_WITHH_STATE_VOIDED_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype; c_doctype2_id→c_doctype | Detalle enlazado a ad_client, ad_org, c_doctype. Validado por trigger(s): SSWH_WITHH_AUTHORIZATIONNO_TRG, SSWH_WITHH_STATE_VOIDED_TRG. | PK `sswh_withholdings_voided_key`; Cols: c_doctype_id, documentno, withholdingdate, stablishment, shell; `SSWH_WITHH_V_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SSWH_Amountldm` |
| `SSWH_Authorization` |
| `SSWH_checkbook` |
| `SSWH_Checkbookline` |
| `SSWH_Checkbookpos` |
| `SSWH_CheckbookposLine` |
| `SSWH_Codelivelihoodt` |
| `sswh_countrypayment` |
| `sswh_dc_note` |
| `sswh_form_aux` |
| `sswh_form_codesline103` |
| `sswh_form_codesline104` |
| `sswh_formulary` |
| `sswh_formulary_codes` |
| `sswh_formularyline` |
| `sswh_inv_exportation` |
| `SSWH_Livelihoodt` |
| `SSWH_Other_document` |
| `SSWH_Pos` |
| `SSWH_Receipt` |
| `SSWH_Receipt_Tax` |
| `SSWH_Rpt_Ats_Purchase` |
| `SSWH_Rpt_Ats_Sales` |
| `SSWH_Rpt_Ats_With_Purchase` |
| `Sswh_Rptc_OrgInform` |
| `Sswh_Rptc_PurchaseDet` |
| `Sswh_Rptc_PurchasePaym` |
| `Sswh_Rptc_PurchaseWith` |
| `Sswh_Rptc_SalesByStab` |
| `sswh_rptc_salesbystaborg` |
| `sswh_rptc_salescomp` |
| `Sswh_Rptc_SalesDet` |
| `sswh_rptc_salespayform` |
| `Sswh_Rptc_SalesRefund` |
| `Sswh_Rptc_SalesVoided` |
| `sswh_rptc_sql` |
| `sswh_salestickets` |
| `SSWH_Source` |
| `SSWH_Taxpayer` |
| `SSWH_TaxRegime` |
| `SSWH_Termpayment` |
| `Sswh_Transaction_Type` |
| `sswh_typereceipt` |
| `sswh_withh_card_credit` |
| `SSWH_Withholding` |
| `SSWH_Withholding_Source` |
| `SSWH_Withholding_vendor` |
| `sswh_withholdings_voided` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ORG`, `AD_ORGINFO`, `C_ACCTSCHEMA_DEFAULT`, `C_BANK`, `C_BANKSTATEMENT`, `C_BANKSTATEMENTLINE`, `C_BPARTNER`, `C_BP_BANKACCOUNT`, `C_BP_GROUP`, `C_COUNTRY`, `C_DOCTYPE`, `C_INVOICE`, `C_INVOICELINE`, `C_INVOICETAX`, `C_PAYMENTTERM`, `C_TAX`, `C_TAXCATEGORY`, `FIN_FINANCIAL_ACCOUNT`, `FIN_PAYMENT`, `FIN_PAYMENTMETHOD`, `M_INVENTORY`, `M_PRODUCT`, `M_PRODUCTION`

### Views

`SSWH_ACCT_RECEIVAB_PAYAB_V`, `SSWH_ACCT_RECEIVAB_PAYAB_ZRO_V`, `SSWH_DC_NOTE_V`, `SSWH_INVOICE_RECEIPT`, `SSWH_INV_TAXABLE_TAX_V`, `SSWH_PURCHASEDETAIL_NATS`, `SSWH_PURCHASE_DETAIL_ATS3`, `SSWH_PURCHASE_DETPROD_NATS`, `SSWH_PURCHASE_FORMPAYMENT_NATS`, `SSWH_RESUMEN_VENTA_CATEGORIA`, `SSWH_RPT_OLD_CUSTOMERS`, `SSWH_RPT_ORDER_PENDING`, `SSWH_RPT_PRODUCT_CLIENT`, `SSWH_RPT_SALES_ORDER`, `SSWH_RPT_SHIPPING`, `SSWH_SALESBYSTABLISHMENT_NATS`, `SSWH_SALESDET_F104_V`, `SSWH_SALESINVOICE_NATS`, `SSWH_SALES_VOIDED_NATS`, `SSWH_VIEW_INVOICE`, `SSWH_WITHHOLDINGPURCHASE_NATS`

# Functional — windows and menus

## Functional

En la interfaz de usuario (UI), el módulo se navega a través de una serie de ventanas como 'Comprobante de Retención' y 'Formularios', donde los usuarios pueden gestionar las retenciones aplicadas. Cada ventana proporciona campos específicos que permiten ingresar o actualizar información relacionada con las retenciones, así como acceso a informes generados que permiten verificar y presentar la información de manera eficiente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.localization.ecuador.withholdings.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Chequera | CheckBook |
| Cheques POS | CheckBook POS |
| Comprobante de Retención | Withholding Receipt |
| Código Sustento | Livelihood Code |
| Códigos de Formulario | Formulary Code |
| Formularios | Formulary |
| Información de la Organización | OrgInfo |
| País Código de Pago | Country Source of payment |
| Retenciones anuladas | Withholings Voided |
| Retención en la Fuente | Withholding at the Source |
| Retención Tarjetas | Withholdings Card |
| Régimen fiscal | Tax Regime |
| Scripts ATS | Scripts ATS |
| Tickets de Venta | Sales Tickets |
| Tipo de Contribuyente | Taxpayer Type |
| Tipo de transacción | Transaction Type |
| Tipo Sustento | Livelihood Type |
| Type Receipt | Type Receipt |
| Términos de Pago | Terms Payment |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Anexo - Soporte | Annex - Support | Sí |
| Archivo Transferencia Proveedor TXT | Archive Provider Transfer TXT | No |
| ATS | ATS | Sí |
| Chequera | CheckBook | No |
| Cheques POS | CheckBook POS | No |
| Cheques PosFechados | CheckBook POS | Sí |
| Compensación de ventas | Sales compensation | No |
| Compras por forma de pago | Purchase Form Payment | No |
| Condiciones de Pago | Terms Payment | No |
| Configuración | Setup | Sí |
| Crear xml - ATS | Create xml - ATS | No |
| Código Sustento | Livelihood Code | No |
| Códigos de Formulario | Formulary Code | No |
| Declaración | Declaration | Sí |
| Declaración de retenciones compras | Purchase Withholding VAT Declaration | No |
| Detalle de compras | Purchase Detail | No |
| Detalle de Retención Iva en Compras | Details of VAT Withholding on Purchases | No |
| Detalle de Retención Renta en Compras | Detail of Income Withholding on Purchases | No |
| Estado CxC - Detallado | Summary Accounts Receivable | No |
| Estado CxC - Detallado (Por Vendedor) | Accounts Receivable Report by Seller | No |
| Estado CxC - Histórico de cancelaciones | Detail Accounts Receivable | No |
| Estado CxC - Resumido | Summary Accounts Receivable Total | No |
| Estado CxC - Resumido (Por Vendedor) | Account receivable summarized by seller | No |
| Estado de CxP - Deetallado(Por Centro de Costos) | Detail Accounts Payable by Cost Center | No |
| Estado de CxP - Detallado | Summary Accounts Payable | No |
| Estado de CxP - Historico de Cancelaciones | Detail Accounts Payable | No |
| Estado de CxP - Resumido | Summary Accounts Payable Total | No |
| Formas de cobro | Forms of payment | No |
| Formularios | Formulary | No |
| Generar ATS | Generate ATS | No |
| Iva Compras - Por Tercero y Factura | VAT Purchases - By Third Party and Invoice | No |
| Iva Ventas - Por cliente | Sales VAT - Per customer | No |
| Iva Ventas - Por cliente y Factura | Sales VAT - By customer and Invoice | No |
| Payment In Methods | Payment In Methods | No |
| Payment Out Methods | Payment Out Methods | No |
| País Código de pago | Country Source of payment | No |
| Reporte Balance de Pagos | Report Balance Payable | No |
| Reporte de Retenciones anuladas | Report of Withholdings Voided | No |
| Reporte resumen impuesto a la renta | Summary Purchase Income Tax | No |
| Resumen retenciones | Summary Withholding | No |
| Retenciones anuladas | Withholings Voided | No |
| Retenciones de compra | Withholding Purchases | No |
| Retenciones Emitidas | Withholdings Issued | No |
| Retenciones por Recuperar | Withholdings By Recovered | No |
| Retención en la Fuente | Withholding at the Source | No |
| Retención Tarjetas | Withholdings Card | No |
| Régimen fiscal | Tax Regime | No |
| Scripts ATS | Scripts ATS | No |
| Tickets de Venta | Sales Tickets | No |
| Tipo de Contribuyente | Taxpayer Type | No |
| Tipo de Recibo | Type Receipt | No |
| Tipo de transacción | Transaction Type | No |
| Tipo Sustento | Livelihood Type | No |
| Venta clientes | Sales Customer | No |
| Ventas Anuladas | Sales Voided | No |
| Ventas por establecimiento | Sales by Stablishment | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.localization.ecuador.withholdings.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Chequera

- **AD_WINDOW_ID:** `0224F2B9D8324832B69AB0D6916927C7`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `3B999CE879704B2CAF22AB3609BA4994` | 0 |
| 20 | Line | `56F1F8DF60054C4FA98AEAF9C822ED39` | 1 |

### Ventana: Cheques POS

- **AD_WINDOW_ID:** `F6BE3DC76035416DB45DF286484C704B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `939A19A69C3E44D080454D05C8E3B2B8` | 0 |
| 20 | Line | `42E567211C2F464CA4C149135B21853F` | 1 |

### Ventana: Comprobante de Retención

- **AD_WINDOW_ID:** `8C93474115A444448C5609DAEACB48A7`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Withholding Receipt | `92289F66B9CC4F599447E53D646182FC` | 0 |
| 20 | Withholding | `24C44D3CBA964DFA91540FBB5F868DBD` | 1 |

### Ventana: Código Sustento

- **AD_WINDOW_ID:** `483B8467C1DC4ED5B07BBE00FC633780`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Livelihood Code | `0E0BD68DFD7940F1A496B7A4DA6BA3A8` | 0 |

### Ventana: Códigos de Formulario

- **AD_WINDOW_ID:** `854A46E4CC5A4CE6BF1E386AD730A74C`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Formulary Code | `DF8F1EE149494B5D93A2BD60D9904A38` | 0 |
| 20 | Formulary 103 | `2721861D3D2A49DC8A50E99AF730C1E5` | 1 |
| 30 | Formulary 104 | `8A51917AB9224A0E896B2E87A847FC83` | 1 |

### Ventana: Formularios

- **AD_WINDOW_ID:** `0AA43DE6B4AF41D08058F2407CA11C0D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Formulary | `7F0D28D335664C948473D93B1F096614` | 0 |
| 20 | Lines | `A51380DB60EF44DAA47A6BEB7D244AD7` | 1 |
| 30 | Lines Formulary 104 | `A51380DB60EF44DAA47A6BEB7D244AD7` | 1 |

### Ventana: Información de la Organización

- **AD_WINDOW_ID:** `679EE99AB9FC4AD797F0205D7C8314F5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | OrgInfo | `366AA932BFF043B096C75E6F85365D09` | 0 |

### Ventana: País Código de Pago

- **AD_WINDOW_ID:** `F6BFA1A5A33040389C242A9126167E50`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Country Source of payment | `72DF969D85E340EFB356717E8EBF7338` | 0 |

### Ventana: Retenciones anuladas

- **AD_WINDOW_ID:** `71AD442B55164E4B8482DE2EE117211B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Withholings Voided | `61C5D42FB120458F983EE2F27B62C16E` | 0 |

### Ventana: Retención en la Fuente

- **AD_WINDOW_ID:** `8EF829CA858B4F89A754E8D2CEA13A94`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Withholding at the Source | `DAA272FB84134F4FB23C2FBD64965B6B` | 0 |
| 20 | Source | `1FF64E9C534D42F0AEAADD180D5A6017` | 1 |

### Ventana: Retención Tarjetas

- **AD_WINDOW_ID:** `9A40FFB27B554816AD41F0732442246E`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Withholdings Card | `610D781C7DE142108BDBBBF84107C394` | 0 |
| 100 | Accounting | `270` | 1 |

### Ventana: Régimen fiscal

- **AD_WINDOW_ID:** `D9CECF4277A54DC28450AB14A9CEEEDF`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Tax Regime | `9EAB50D327B3469F8A02AC364EC07F06` | 0 |

### Ventana: Scripts ATS

- **AD_WINDOW_ID:** `B2CCA856718046A7A2E817002E91A07D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Scripts ATS | `BFCE3B5D3BB74143A1E5FC91A674EE80` | 0 |

### Ventana: Tickets de Venta

- **AD_WINDOW_ID:** `DCCA1763751F4BE388A5893676D3E615`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Sales Tickets | `7239C7DF18A34DF5B4E1E03FA4697CF4` | 0 |

### Ventana: Tipo de Contribuyente

- **AD_WINDOW_ID:** `23E2255002F84DD0802F00BECA810489`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Taxpayer Type | `F535CF4CA86A494C8F7A760823D73621` | 0 |
| 20 | Withholding | `E918F766628243FEB9DD4577C4A09DF4` | 1 |

### Ventana: Tipo de transacción

- **AD_WINDOW_ID:** `63A720950623470993D428ED2914AC23`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `8EFEFD4947434799B3D7838A5AB6F0B6` | 0 |

### Ventana: Tipo Sustento

- **AD_WINDOW_ID:** `6C50101204244F1E8E867B7DDA1C58DE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Livelihood Type | `ECA07965607240F7A652E1F418F4A0CE` | 0 |

### Ventana: Type Receipt

- **AD_WINDOW_ID:** `EE4446E4783749B391AB9B642450D59E`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Type Receipt | `3F856A7A8A774902AF78880EC9768620` | 0 |

### Ventana: Términos de Pago

- **AD_WINDOW_ID:** `5EBCBFA6351547DA9586EEC69E318F1A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Terms Payment | `52E5B9E894B842E48DDC401F90279C0E` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Withholding Autorizathion

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Active | `Isactive` | No | No | — |
| 30 | Establishment | `Stablishment` | No | No | — |
| 40 | Shell | `Shell` | No | No | — |
| 40 | Withholding Authorization | `Withholdingauthorization` | No | No | — |
| 50 | Number From | `Numberfrom` | No | No | — |
| 60 | Number To | `Numberto` | No | No | — |
| 70 | Starting Date | `Datefrom` | No | No | — |
| 80 | Ending Date | `Dateto` | No | No | — |

### Lines (ventana: Formularios)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 25 | Line No. | `Line` | No | No | — |
| 30 | Father Code | `Father_Code` | No | No | — |
| 40 | Tax Base | `Baseamount` | No | No | — |
| 50 | Son Code | `SON_Code` | No | No | — |
| 60 | Retained Value | `Taxamount` | No | No | — |
| 70 | Father Code 2 | `Grandfather_Code` | No | No | — |
| 80 | Amount Net | `GF_Amount` | No | No | — |
| 90 | Status | `Status` | No | Sí | — |
| 100 | Active | `Isactive` | No | No | — |

### Pestaña `135`

- **AD_TAB_ID:** `135` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 172 | Tax Regime | `EM_Sswh_Taxregime_ID` | No | No | — |
| 175 | Regime Code | `EM_Sswh_RegimeCode` | No | No | — |
| 178 | Designation Tax | `EM_Sswh_DesignationTax` | No | No | — |

### Pestaña `143`

- **AD_TAB_ID:** `143` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 110 | Description Opcional | `EM_Sswh_Description2` | No | No | — |
| 730 | Minimum payment method | `EM_Sswh_Ats_Amount` | No | No | FF6AA3267ED742D1BCC3B7300C768F2B |

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 220 | Implement Authorization | `EM_Sswh_Implementautoriza` | No | No | — |
| 230 | Withholding | `EM_Sswh_Iswithholding` | No | No | — |
| 240 | Customer | `EM_Sswh_Iscustomer` | No | No | — |
| 250 | Withholding Sale | `EM_Sswh_Iswithholdingsale` | No | No | — |
| 270 | Type receipt | `EM_Sswh_Typereceipt_ID` | No | No | — |
| 295 | Doc. Type | `EM_Sswh_Doctype` | No | No | — |
| 299 | em_sswh_dividends | `EM_Sswh_Dividends` | No | No | — |
| 310 | Afected Zone | `EM_Sswh_Afectedzone` | No | No | — |
| 320 | Code | `EM_Sswh_Code` | No | No | — |
| 330 | Percentage | `EM_Sswh_Percentage` | No | No | — |
| 340 | Exterior Withholding | `EM_Sswh_Ext_Withh` | No | No | — |
| 350 | Withholding Code | `EM_Sswh_Withh_Code` | No | No | — |

### Pestaña `170`

- **AD_TAB_ID:** `170` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 65 | Taxpayer Type | `EM_Sswh_Taxpayer_ID` | No | No | — |

### Pestaña `174`

- **AD_TAB_ID:** `174` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 215 | Withholding at the Source | `EM_Sswh_Iswithholdingsource` | No | No | — |
| 252 | Withholdings Issued | `EM_Sswh_Isrepwithhissued` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |
| 255 | Order Print | `EM_Sswh_Orderprint` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |
| 261 | em_sswh_dividends | `EM_Sswh_Dividends` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |
| 310 | ATS Withholding Source | `EM_Sswh_Ats_Source` | No | No | — |
| 320 | ATS Withholding Iva | `EM_Sswh_Ats_Iva` | No | No | — |
| 350 | No Object VAT | `EM_Sswh_Isnoobjectvat` | No | No | — |
| 360 | Exempt | `EM_Sswh_Isexempt` | No | No | — |
| 370 | Apply withholding | `EM_Sswh_Apply_Withholding` | No | No | — |
| 401 | Exclude withholding code | `EM_Sswh_Exclude_Tax` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |
| — | Code 103-104 | `EM_Sswh_Code_103_104` | No | No | — |

### Pestaña `176`

- **AD_TAB_ID:** `176` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 80 | Withholding Type | `EM_Sswh_Withholdingtype` | No | No | — |

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 110 | Withholding at the Source | `EM_Sswh_Withholding_Source_ID` | No | No | — |
| 686 | Customer Refund | `EM_Sswh_Isrefund_Customer` | No | No | — |

### Formulary 104 (ventana: Códigos de Formulario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | Line No. | `Line` | No | No | — |
| 40 | Father Code | `Father_Code` | No | No | — |
| 45 | Formula | `Formula` | No | No | — |
| 50 | Father Code 2 | `Grandfather_Code` | No | No | — |
| 55 | Formula 3 | `Formula_Gf` | No | No | — |
| 60 | Son Code | `SON_Code` | No | No | — |
| 65 | Formula 2 | `Formula_Son` | No | No | — |
| 80 | Active | `Isactive` | No | No | — |

### Withholding (ventana: Tipo de Contribuyente)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Taxpayer Type | `Sswh_Taxpayer_ID` | No | Sí | — |
| 40 | Active | `Isactive` | No | No | — |
| 50 | Taxpayer Reference | `Sswh_Taxpayer_Ref_ID` | No | No | — |
| 60 | Tax for Goods | `C_Tax_Goods_ID` | No | No | — |
| 70 | Tax for Services | `C_Tax_Services_ID` | No | No | — |

### Pestaña `220`

- **AD_TAB_ID:** `220` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 70 | Name Opcional | `EM_Sswh_Name3` | No | No | — |
| 110 | Type ID | `EM_Sswh_Taxidtype` | No | No | — |
| 150 | Taxpayer Type | `EM_SSWH_Taxpayer_ID` | No | No | — |
| 155 | Resolution No. | `EM_Sswh_Resolutionno` | No | No | — |
| 300 | Code Taxpayer | `Em_Sswh_Codetaxpayer` | No | No | — |

### Pestaña `223`

- **AD_TAB_ID:** `223` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 190 | Sales Advisor | `EM_Sswh_Saleadvisor` | No | No | — |
| 200 | Collecting Agent | `EM_Sswh_Collectingagent` | No | No | — |
| 270 | Terms Payment | `EM_Sswh_Termpay` | No | No | — |

### Pestaña `226`

- **AD_TAB_ID:** `226` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 293 | Type ID | `EM_Sswh_Taxidtype` | No | No | — |
| 297 | Tax ID | `EM_Sswh_Taxidno` | No | No | — |
| 300 | Payment Automatic | `EM_Sswh_Paymentautomatic` | No | No | — |

### Withholding Receipt (ventana: Comprobante de Retención)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Transaction Document | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `DocumentNo` | No | No | — |
| 50 | Document Date | `Datedoc` | No | No | — |
| 60 | Reference | `Reference` | No | No | — |
| 70 | Authorization No. | `Authorizationno` | No | No | — |
| 80 | Active | `Isactive` | No | No | — |
| 90 | Business Partner | `C_Bpartner_ID` | No | No | 125 |
| 100 | Invoice | `C_Invoice_ID` | No | No | 125 |
| 110 | Withholding at the Source Amount - Income | `Totalwithholdingincome` | No | Sí | 103 |
| 120 | Withholding at the Source Amount - VAT | `Totalwithholdingvat` | No | Sí | 103 |
| 130 | Withholding at the Source Amount - Income | `Calculatedtotalwithholdinginco` | No | Sí | 83AB911EA5D443B6A939FAA3BC20FC4E |
| 140 | Withholding at the Source Amount - VAT | `Calculatedtotalwithholdingvat` | No | Sí | 83AB911EA5D443B6A939FAA3BC20FC4E |
| 150 | Process Withholding Receipt | `Processed` | No | No | — |
| 160 | Posted | `Posted` | No | No | — |

### Pestaña `252`

- **AD_TAB_ID:** `252` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 750 | EM_Sswh_Wh_Income_Acct | `EM_Sswh_Wh_Income_Acct` | No | No | 7F59D9FBCD09492CB880A5ACCF82BB7C |
| 760 | EM_Sswh_Wh_Iva_Acct | `EM_Sswh_Wh_Iva_Acct` | No | No | 7F59D9FBCD09492CB880A5ACCF82BB7C |
| 770 | EM_Sswh_Wh_Transit_Acct | `EM_Sswh_Wh_Transit_Acct` | No | No | 7F59D9FBCD09492CB880A5ACCF82BB7C |

### Pestaña `255`

- **AD_TAB_ID:** `255` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 25 | Document No. | `DocumentNo` | No | No | — |
| 75 | Is Transformation | `EM_Sswh_Istransformation` | No | No | — |

### Pestaña `263`

- **AD_TAB_ID:** `263` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 65 | Authorization No. | `EM_Sswh_Nroauthorization` | No | Sí | — |
| 225 | Date End Invoice | `EM_Sswh_Dateendinvoice` | No | No | — |
| 226 | Invoice Reference | `EM_Sswh_Invoice_Ref` | No | No | — |
| 383 | Withholding at the Source Amount - Income | `EM_Sswh_Totalwithholdingincome` | No | Sí | — |
| 384 | Withholding at the Source Amount - VAT | `EM_Sswh_Totalwithholdingvat` | No | Sí | — |
| 385 | Withholding Receipt | `EM_Sswh_Receipt_ID` | No | Sí | — |

### Withholdings Card (ventana: Retención Tarjetas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `Documentno` | No | No | — |
| 50 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 60 | Invoice No. | `C_Invoice_ID` | No | No | — |
| 70 | Transaction Date | `Date_Doc` | No | No | — |
| 75 | Accounting Date | `Dateacct` | No | No | — |
| 80 | Description | `Description` | No | No | — |
| 90 | Process Withholding Card | `Processed` | No | No | — |
| 100 | Status | `Status` | No | Sí | — |
| 110 | Withholding VAT | `Withh_Vat` | No | No | — |
| 120 | Withholding Source | `Withh_Rent` | No | No | — |
| 130 | Active | `Isactive` | No | No | — |
| 140 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 150 | Number of vouchers | `Vouchers_Number` | No | No | — |
| 160 | Sswh_Transaction_Type_ID | `Sswh_Transaction_Type_ID` | No | No | — |
| 180 | Posted | `Posted` | No | No | — |

### Pestaña `270`

- **AD_TAB_ID:** `270` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 250 | Withholding at the Source Amount - Income | `EM_Sswh_Invoicetax_Income_ID` | No | Sí | — |
| 260 | Withholding at the Source Amount - VAT | `EM_Sswh_Invoicetax_Vat_ID` | No | Sí | — |

### Pestaña `2845D761A8394468BD3BA4710AA888D4`

- **AD_TAB_ID:** `2845D761A8394468BD3BA4710AA888D4` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 127 | Withholding type | `EM_Sswh_Withh_Type` | No | No | — |

### Pestaña `290`

- **AD_TAB_ID:** `290` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 106 | E-Invoice | `EM_Sswh_Iseinvoice` | No | No | — |
| 108 | Account Payment Out | `EM_Sswh_Bankaccount_ID` | No | No | — |
| 109 | Authorization manual | `EM_Sswh_Authorizationmanual` | No | No | — |
| 120 | Authorization No. | `EM_Sswh_Nroauthorization` | No | No | — |
| 130 | Expiration Date | `EM_Sswh_Expirationdate` | No | No | — |
| 134 | Credit Note | `EM_Sswh_Creditnote` | No | No | — |
| 138 | Credit Note Reference | `em_sswh_creditnotereference` | No | No | — |
| 531 | Withholding at the Source Amount - Income | `EM_Sswh_Totalwithholdingincome` | No | Sí | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 532 | Withholding at the Source Amount - VAT | `EM_Sswh_Totalwithholdingvat` | No | Sí | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 533 | Withholding manual | `EM_Sswh_Withholdingmanual` | No | No | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 534 | Withholding Document | `EM_Sswh_C_Doctype_ID` | No | No | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 535 | Withholding Reference | `EM_Sswh_Withholdingref` | No | No | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 536 | Authorization | `EM_Sswh_Authorization` | No | No | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 537 | Withholding Date | `EM_Sswh_Datewithhold` | No | No | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 538 | Type of Livelihood | `EM_Sswh_Livelihood` | No | No | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 539 | Livelihood Code | `EM_Sswh_Codelivelihood` | No | No | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 541 | em_sswh_dividend_year | `EM_Sswh_Dividend_Year` | No | No | 7ED3F5A18B9B475184588E1FC11A4BB9 |

### Pestaña `291`

- **AD_TAB_ID:** `291` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 250 | Withholding at the Source Amount - Income | `EM_Sswh_Invoicetax_Income_ID` | No | Sí | 7ED3F5A18B9B475184588E1FC11A4BB9 |
| 251 | Withholding at the Source Amount - VAT | `EM_Sswh_Invoicetax_Vat_ID` | No | Sí | 7ED3F5A18B9B475184588E1FC11A4BB9 |

### OrgInfo (ventana: Información de la Organización)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Organization | `AD_Org_ID` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |
| 60 | Legal Name | `Social_Name` | No | No | — |
| 70 | Identif | `Identif` | No | No | — |
| 80 | Type ID | `Sswh_Taxidtype` | No | No | — |

### Pestaña `319`

- **AD_TAB_ID:** `319` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 160 | Calculate Costing LDM | `EM_Sswh_Calculecoste` | No | No | — |

### Formulary Code (ventana: Códigos de Formulario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Pestaña `322`

- **AD_TAB_ID:** `322` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 70 | Exportation | `EM_Sswh_Isexportation` | No | No | — |
| 80 | Client Type | `EM_Sswh_Clienttype` | No | No | — |
| 90 | Exportation of | `EM_Sswh_Exportation_From` | No | No | — |
| 100 | Type Ing. Exterior | `EM_Sswh_Type_Ing_Ext` | No | No | — |
| 110 | Ing. Exterior Grav. Other Country | `EM_Sswh_IngExtGravOth_Ctry` | No | No | — |

### Pestaña `328`

- **AD_TAB_ID:** `328` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 40 | Document No. | `DocumentNo` | No | Sí | — |
| 50 | Pay With Bank | `EM_Sswh_Paywithbank` | No | No | — |
| 120 | Paymentrule | `EM_Sswh_Paymentrule` | No | No | — |
| 130 | Type Check | `EM_Sswh_Typecheck` | No | No | — |
| 140 | Checkbook | `EM_Sswh_Checkbook` | No | No | — |
| 150 | Linecheck | `EM_Sswh_Linecheck` | No | Sí | — |
| 160 | Is Manual Settlement | `EM_Sswh_Issettlement` | No | No | — |
| 170 | Nro. Document | `EM_Sswh_Operation` | No | No | — |
| 180 | Is Charge | `EM_Sswh_Ischarge` | No | No | — |
| 190 | Other_Document | `EM_Sswh_Other_Document` | No | No | — |
| 230 | Business Partner | `EM_Sswh_Partner_ID` | No | No | 08E0BE9A3096425AABF9D9478F947D18 |
| 240 | No Record | `EM_Sswh_Inrecord` | No | No | 08E0BE9A3096425AABF9D9478F947D18 |
| 270 | Allocated Check | `EM_Sswh_Check` | No | No | — |
| 280 | De AllocatedCheck | `EM_Sswh_Uncheck` | No | No | — |

### Pestaña `329`

- **AD_TAB_ID:** `329` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 70 | Business Partner | `EM_Sswh_Partner_ID` | No | No | — |
| 200 | Linecheck | `EM_Sswh_Linecheck` | No | No | — |
| 210 | Is Print | `EM_Sswh_Print` | No | No | — |

### Sales Tickets (ventana: Tickets de Venta)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `Documentno` | No | No | — |
| 50 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 65 | Establishment No. | `Establishmentno` | No | No | — |
| 70 | Transaction Date | `Date_Doc` | No | No | — |
| 80 | Description | `Description` | No | No | — |
| 90 | Status | `Status` | No | Sí | — |
| 100 | Base No VAT | `BaseNoVAT` | No | No | — |
| 110 | Base 0 | `BaseZero` | No | No | — |
| 120 | Process Tickets | `Processed` | No | No | — |
| 130 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 140 | Vouchers Number | `Vouchers_Number` | No | No | — |
| 150 | Sswh_Transaction_Type_ID | `Sswh_Transaction_Type_ID` | No | No | — |

### Withholding (ventana: Comprobante de Retención)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Line No. | `Line` | No | No | — |
| 30 | Invoice Tax | `C_Invoicetax_ID` | No | Sí | — |
| 40 | Taxable Amount | `Taxbaseamt` | No | No | — |
| 50 | Tax | `C_Tax_ID` | No | No | — |
| 60 | Tax Amount | `Taxamt` | No | No | — |
| 70 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 80 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 100 | Active | `Isactive` | No | No | — |

### Taxpayer Type (ventana: Tipo de Contribuyente)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 60 | Special Taxpayer | `Specialtaxpayer` | No | No | — |
| 70 | Required Accounting | `Requiredaccounting` | No | No | — |
| 80 | Search Key | `Value` | No | No | — |
| 90 | Related part | `Relatedpart` | No | No | — |

### Accounting (ventana: Retención Tarjetas)

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

### Line (ventana: Cheques POS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 100 | Payment | `C_Debt_Payment_ID` | No | No | — |
| 110 | Total | `Granttotal` | No | No | — |

### Type Receipt (ventana: Type Receipt)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Commercial Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Livelihood Code (ventana: Código Sustento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Applies_Withholding | `Applies_Withholding` | No | No | — |

### Formulary (ventana: Formularios)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Formulary Type | `Formulary_Type` | No | No | — |
| 30 | Date From | `Startdate` | No | No | — |
| 40 | Date To | `Enddate` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Process Formulary | `Process` | No | No | — |
| 70 | Document Status | `Status` | No | Sí | — |
| 80 | Active | `Isactive` | No | No | — |
| 90 | Unprocess | `Unprocess` | No | No | — |

### Livelihood Type (ventana: Tipo Sustento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Isrefund | `Isrefund` | No | No | — |
| 80 | Exclude Refund | `Isexcludedrefund` | No | No | — |

### Withholings Voided (ventana: Retenciones anuladas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | active | `Isactive` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `Documentno` | No | No | — |
| 50 | Withholding date | `Withholdingdate` | No | No | — |
| 60 | Stablishment | `Stablishment` | No | No | — |
| 70 | Shell | `Shell` | No | No | — |
| 80 | Series from | `Referenceno_From` | No | No | — |
| 90 | Series to | `Referenceno_To` | No | No | — |
| 100 | Description | `Description` | No | No | — |
| 130 | Voided document | `DOC_Voided` | No | No | — |
| 135 | Reference document type | `C_Doctype2_ID` | No | No | — |
| 140 | Authorization No. | `Authorizationno` | No | No | — |
| 150 | Processed Withhldings Voided | `Processed` | No | No | — |
| 160 | Date_Voided | `Date_Voided` | No | No | — |
| 170 | Imp. Withholding at Source Rent | `AMT_Source_Wh_Rent` | No | No | — |
| 180 | Imp. Withholding at Source Iva | `AMT_Source_Wh_Iva` | No | No | — |

### Lines Formulary 104 (ventana: Formularios)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 25 | Line No. | `Line` | No | No | — |
| 30 | Father Code | `Father_Code` | No | No | — |
| 40 | Tax Base | `Baseamount` | No | No | — |
| 50 | Father Code 2 | `Grandfather_Code` | No | No | — |
| 60 | Amount Net | `GF_Amount` | No | No | — |
| 70 | Son Code | `SON_Code` | No | No | — |
| 80 | Impuesto Generado | `Taxamount` | No | No | — |
| 90 | Status | `Status` | No | Sí | — |
| 100 | Active | `Isactive` | No | No | — |

### Line (ventana: Chequera)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Checkbook | `Sswh_Checkbook_ID` | No | Sí | — |
| 50 | Linecheck | `Linecheck` | No | Sí | — |
| 60 | Bank Statement Line | `C_Bankstatementline_ID` | No | Sí | — |
| 70 | Description | `Description` | No | No | — |
| 80 | Status | `DOC_Line_Status` | No | No | — |
| 90 | Generate Status | `Generate_Status` | No | No | — |

### Header (ventana: Cheques POS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Bank | `C_Bank_ID` | No | No | 61FC84105EFB4E04AA313B6F8481FC8C |
| 50 | Currency | `C_Currency_ID` | No | No | 61FC84105EFB4E04AA313B6F8481FC8C |
| 60 | Generic Account No. | `Genericaccount` | No | No | 61FC84105EFB4E04AA313B6F8481FC8C |
| 70 | Linecheck | `Linecheck` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 80 | Business Partner | `C_Bpartner_ID` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 90 | Date Created | `Datecreated` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 100 | Date Expired | `Dateexpired` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 110 | Total | `Granttotal` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 120 | Type Operation | `Toperation` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 130 | Document Status | `Docstatus` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |

### Pestaña `A4A463FA34F946BFA3F687DC8754ED93`

- **AD_TAB_ID:** `A4A463FA34F946BFA3F687DC8754ED93` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 15 | Value | `EM_Sswh_Value` | No | No | — |
| 45 | Code ats | `EM_Sswh_Codeats` | No | No | — |
| 105 | Withholding Type | `EM_Sswh_Withholdingtype` | No | No | — |
| 230 | Type Payment | `EM_Sswh_Typepayment` | No | No | — |
| 240 | Country Source of payment | `EM_Sswh_Countrypayment_ID` | No | No | — |
| 250 | Subject to withholding | `EM_Sswh_Subjecttowithholding` | No | No | — |
| 260 | Apply double taxation | `EM_Sswh_Applydoubletax` | No | No | — |
| 270 | Fiscal Regime | `EM_Sswh_Fiscalregime` | No | No | — |
| 280 | Electronic Money | `EM_Sswh_Electronicmoney` | No | No | — |
| 290 | Code | `EM_Sswh_Code` | No | No | — |
| 300 | Percentage | `EM_Sswh_Percentage` | No | No | — |

### Scripts ATS (ventana: Scripts ATS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Commercial Name | `Name` | No | No | — |
| 40 | Sql | `Sqlscript` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Authorization

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Active | `Isactive` | No | No | — |
| 20 | Authorization No. | `Authorizationno` | No | No | — |
| 30 | Establishment | `Establishment` | No | No | — |
| 40 | Cash Register | `Cashregister` | No | No | — |
| 50 | Number From | `Numberfrom` | No | No | — |
| 60 | Number To | `Numberto` | No | No | — |
| 70 | Starting Date | `Datefrom` | No | No | — |
| 80 | Ending Date | `Dateto` | No | No | — |

### Source (ventana: Retención en la Fuente)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Withholding at the Source | `Sswh_Withholding_Source_ID` | No | Sí | — |
| 40 | Active | `Isactive` | No | No | — |
| 50 | Tax | `C_Tax_ID` | No | No | — |
| 60 | Code | `Code` | No | No | — |

### Header (ventana: Chequera)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Bank Account | `C_Bankaccount_ID` | No | No | 61FC84105EFB4E04AA313B6F8481FC8C |
| 50 | Account Type | `Bankaccounttype` | No | Sí | 61FC84105EFB4E04AA313B6F8481FC8C |
| 60 | Currency | `C_Currency_ID` | No | Sí | 61FC84105EFB4E04AA313B6F8481FC8C |
| 70 | Generic Account No. | `Genericaccount` | No | Sí | 61FC84105EFB4E04AA313B6F8481FC8C |
| 80 | Typecheck | `Typecheck` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 90 | Nro. Check | `Nrocheck` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 100 | From | `Nrofrom` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 110 | To | `Nroto` | No | No | AF3E340A1C944F1DA6240EBC551BBC79 |
| 120 | Sectory | `Sectory` | No | No | F023FA1071AC4B619265D6073EB6E7B8 |
| 130 | Phone | `Phone` | No | No | F023FA1071AC4B619265D6073EB6E7B8 |
| 140 | Generate Check | `Generateto` | No | No | — |
| 150 | Document Status | `Docstatus` | No | Sí | — |
| 160 | Document Action | `Docaction` | No | No | — |

### Tax Regime (ventana: Régimen fiscal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Commercial Name | `Name` | No | No | — |

### Header (ventana: Tipo de transacción)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Code | `Code` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Is electronic | `Iselectronic` | No | No | — |

### Country Source of payment (ventana: País Código de Pago)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Withholding at the Source (ventana: Retención en la Fuente)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Terms Payment (ventana: Términos de Pago)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Closed Credit | `Closed_Credit` | No | No | — |
| 70 | Description | `Description` | No | No | — |

### Formulary 103 (ventana: Códigos de Formulario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | Line No. | `Line` | No | No | — |
| 40 | Father Code | `Father_Code` | No | No | — |
| 45 | Formula | `Formula` | No | No | — |
| 50 | Son Code | `SON_Code` | No | No | — |
| 55 | Formula 2 | `Formula_Son` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |

### Pestaña `F7A52FDAAA0346EFA07D53C125B40404`

- **AD_TAB_ID:** `F7A52FDAAA0346EFA07D53C125B40404` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 63 | Bank Account | `EM_Sswh_Bp_Bankaccount_ID` | No | No | — |
| 67 | Bank Name | `EM_Sswh_Bank_Name` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos en este módulo incluyen características como completar transacciones de retención mediante botones como 'Completar' y 'Retornar', permitiendo a los usuarios finalizar el flujo de trabajo de retenciones. Los informes disponibles, como la 'Impresión Genérica de Formulario' y el 'Withholding Statement', permiten a los usuarios generar documentos necesarios para la presentación ante las autoridades fiscales. Las validaciones comunes suelen ser aquellas que aseguran que los números de autorización sean válidos y que los datos de las facturas estén completos y sean correctos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.localization.ecuador.withholdings.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Asignar Cheque | Allocated Check | SSWH_AllocatedCheck | `SSWH_Allocatedcheck` | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Barre Las lineas buscando sino existe el tercero y lo actualiza por el tercero del efecto.; Reco… | — |
| Botón (PL/pgSQL) | Calcular Costo LDM | Calculate Costing LDM | Calculate Costing LDM | `sswh_calculate_costing_ldm` | INSERT INTO SSWH_AMOUNTLDM VALUES (OPERACION_PRODUCTO); ----TO FIX; SUMARIZADO DE PROMEDIO DE PRODUCTOS MATERIA PRIMA; RESULTADO COSTO PROMEDIO DEL PRODUCTO FABRICADO | — |
| Botón (PL/pgSQL) | Cheque Procesado | Processed Check | processed_check | `sswh_processed_check` | v_Message := v_Message || 'Datos = ' || v_resultado; | — |
| Botón (PL/pgSQL) | De-Asignar Cheque | De AllocatedCheck | SSWH_Deallocatedcheck | `sswh_deallocatedcheck` | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Obtengo el numero de cheque por cada tercero; Actualizo el linecheck de cada los terceros - deja… | — |
| Botón (PL/pgSQL) | Declaración de retención IVA de compra | Purchase Withholding VAT Declaration | Purchase Withholding VAT Declaration | `RptC_PurchaseWithholding.jrxml` | Purchase Withholding VAT Declaration | — |
| Botón (PL/pgSQL) | Desprocesar | Unprocess | Sswh_Unprocess | `sswh_unprocess_form` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Detalle de Compras | Purchase Detail | Purchase Detail | `RptC_PurchaseDetail.jrxml` | — | — |
| Botón (PL/pgSQL) | Detalle de Retención Renta en Compras | Withholding Incometax Declaration | Withholding Incometax Declaration | `RptC_IncometaxDet.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado CxC - Detallado | Summary Accounts Receivable | Summary Accounts Receivable | `Rpt_SumaryAcountRecCons.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado CxC - Histórico de cancelaciones | Detail Accounts Receivable | Detail Accounts Receivable | `Rpt_DetailAcountReceivab.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado de Cuenta por Pagar Detallado por Centro de Costos | Detail Accounts Payable by Cost Center | Detail Accounts Payable by Cost Center | `RptC_DetailAcountPayableByCC` | Detail Accounts Payable by Cost Center | — |
| Botón (PL/pgSQL) | Estado de CxP - Detallado | Summary Accounts Payable | Summary Accounts Payable | `Rptc_SumaryAcountPayCons.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado de CxP - Historico de Cancelaciones | Detail Accounts Payable | Detail Accounts Payable | `RptC_DetailAcountPayable.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado de CxP - Resumido | Summary Accounts Payable Total | Summary Accounts Payable Total | `Rptc_TotalAcountPayCons.jrxml` | — | — |
| Botón (PL/pgSQL) | Formas de Cobro | Payment In Methods | Payment In Methods | `Rptc_PaymentinMethods.jrxml` | Report by Payment In Methods | — |
| Botón (PL/pgSQL) | Formas de Pago | Payment Out Methods | Payment Out Methods | `Rptc_PaymentoutMethods.jrxml` | Report by Payment Out Methods | — |
| Botón (PL/pgSQL) | Formas de Pago en Compras | Purchase Form Payment | Purchase Form Payment | `RptC_PurchaseFormpayment.jrxml` | — | — |
| Botón (PL/pgSQL) | Generar ATS | Generate ATS | Generate ATS | `sswh_get_ats_ob` | Generate ATS for withholding Source and IVA | — |
| Botón (PL/pgSQL) | Generar Cheque | Generate Check | Generate_Check | `sswh_Generate_Check` | insert into temp values(v_Record_ID,v_Client_ID);; v_resultado :='nlinea :' || v_NextNo || 'nroche :' || v_nrocheck || 'ultline :' || n_linecheck ;; v_Message := v_Message || 'Datos = ' || v_resultado; | — |
| Botón (PL/pgSQL) | Generar Estado | Generate Status Line Withholding | Generate Status Line Withholding | `sswh_generate_line_with` | — | — |
| Botón (PL/pgSQL) | Generar Estado | Generate Status | Generate_Status | `sswh_Generate_Status` | insert into temp values(v_Record_ID,'aromero');; v_Message := v_Message || 'Datos = ' || v_resultado; | — |
| Botón (PL/pgSQL) | Generar Retenciones | Generate Withholding | Generate Withholding | `sswh_generate_whithholding` | — | — |
| Botón (PL/pgSQL) | Iva Compras - Por Tercero y Factura | Purchase VAT Declaration | Purchase VAT Declaration | `RptC_Purchase_iva.jrxml` | — | — |
| Botón (PL/pgSQL) | Iva Ventas - Por cliente | Sales VAT Declaration | Sales VAT Declaration | `RptC_Sales.jrxml` | — | — |
| Botón (PL/pgSQL) | Iva Ventas - Por cliente y Factura | Sales VAT Declaration Detail | Sales VAT Declaration Detail | `RptC_SalesDet.jrxml` | — | — |
| Botón (PL/pgSQL) | Procesar Comprobante de Retención | Process Withholding Receipt | sswh_process_withholding_receipt | `sswh_process_receipt` | v_Client_ID := Cur_Parameter.AD_Client_ID;; NULL, 'RDNC', 'Y', 'N', 'N', --triger no permite insertar un registro procesado (processed); raise exception '%','before insert payment schedule '||' v_Client_ID '||v_Client_I… | — |
| Botón (PL/pgSQL) | Procesar Tickets | Process Tickets | SalesTickets | `sswh_process_salesticket` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Proceso Formulario | Process Formulary | ProcessFormulary | `sswh_formulary_process` | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Actualizar Tabla Auxiliar Campo Padre - Total; Actualizar Tab… | — |
| Botón (PL/pgSQL) | Proceso Tarjeta de Retención | Process Withholding Card | Process Withholding Card | `sswh_process_wthh_card` | la transacción se encuentra contabilizada y que debe ser descontabilizada previamente para permitir su anulación | — |
| Botón (PL/pgSQL) | Reporte Balance por Pagar | Report Balance Payable | Report Balance Payable | `Rptc_BalancePayable.jrxml` | — | — |
| Botón (PL/pgSQL) | Resumen de impuesto sobre la renta | Summary Purchase Income Tax | Summary Purchase Income Tax | `RptC_PurchaseIncometax.jrxml` | — | — |
| Botón (PL/pgSQL) | Resumen de Retenciones | Summary Withholding | Summary Withholding | `RptC_SummaryWithholding.jrxml` | — | — |
| Botón (PL/pgSQL) | Retenciones en Compras | Withholding Purchases | Withholding Purchases | `RptC_PurchaseWitholdingA.jrxml` | — | — |
| Botón (PL/pgSQL) | Ventas Anuladas | Sales Voided | Sales Voided | `RptC_SalesVoided.jrxml` | — | — |
| Botón (PL/pgSQL) | Ventas de Clientes | Sales Customer | Sales Customer | `RptC_SalesAts.jrxml` | — | — |
| Botón (PL/pgSQL) | Ventas por Establecimiento | Sales by Stablishment | Sales by Stablishment | `RptC_SalesbyStablishment.jrxml` | — | — |
| Informe (servlet) | Archivo de Transferencia proveedor TXT | Archive Provider Transfer TXT | Archive Provider Transfer TXT | Java `ArchProviderTransferTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cDoctypeId` | `src/com/sidesoft/localization/ecuador/withholdings/create_xml/ArchProviderTransferTXT.java` |
| Informe (servlet) | Crear xml - ATS | Create xml - ATS | Create xml - ATS | Java `Create_xml` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cPeriodId`, Tipo ATS - Mensual. Seleccione el período para continuar.; Tipo ATS - Semestral. Seleccione el Año para continuar.; El campo Organización es obligatorio | `src/com/sidesoft/localization/ecuador/withholdings/create_xml/Create_xml.java` |
| Informe (servlet) | Proceso Retenciones anuladas | Processed Withhldings Voided | Sswh_Processed_Withhldings_Voided | Java `Sswh_ProcessWithholdingVoided` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `Sswh_Withholdings_Voided_ID` | `src/com/sidesoft/localization/ecuador/withholdings/ad_process/Sswh_ProcessWithholdingVoided.java` |
| Proceso / otro | Archivo de Transferencia Proveedor | Archive Provider Transfer | Archive Provider Transfer | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Compensación de ventas | Sales compensation | Sales compensation | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de Retención Iva en Compras | Detailed Purchases Report | Detailed Purchases Report | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Detallado (Por Vendedor) | Accounts Receivable Report by Seller | Accounts Receivable Report by Seller | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Resumido | Summary Accounts Receivable Total | Summary Accounts Receivable Total | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Resumido (Por Vendedor) | Account receivable summarized by seller | Account receivable summarized by seller | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Formas de cobro | Forms of payment | Forms of payment | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de Cuentas Vencidas | Report of past due accounts | Report of past due accounts | *(OBUIAPP / manual)* | Report of past due accounts | — |
| Proceso / otro | Reporte de Retenciones anuladas | Report of Withholdings Voided | Report of Withholdings Voided | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Retenciones Emitidas | Withholdings Issued | Withholdings Issued | *(OBUIAPP / manual)* | Withholdings Issued | — |
| Proceso / otro | Retenciones por Recuperar | Withholdings By Recovered | Withholdings By Recovered | *(OBUIAPP / manual)* | Withholdings By Recovered | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Impresión Genérica de Formulario | GENERIC - PRINT FORMULARY | GENERIC - PRINT FORMULARY | Java `Sswh_GenericPrintFormulary` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `0AA43DE6B4AF41D08058F2407CA11C0D|SSWH_FORMULARY_ID`. | `src/com/sidesoft/localization/ecuador/withholdings/ad_process/Sswh_GenericPrintFormulary.java` |
| Reporte | Withholding Statement | Withholding Statement | PRINTWHSTATEMENT | Java `RptWithholdingStatement` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatement.jrxml`; contexto sesión `—`. | `src/com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatement.java` |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Background | Payment Monitor(New) | Payment Monitor(New) | Sswh - Payment Monitor | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Archivo de Transferencia proveedor TXT | `ArchProviderTransferTXT` | Proceso Java (toolbar/background) | `cDoctypeId` | — | `src/com/sidesoft/localization/ecuador/withholdings/create_xml/ArchProviderTransferTXT.java` |
| Informe (servlet) | Crear xml - ATS | `Create_xml` | Proceso Java (toolbar/background) | `cPeriodId` | Tipo ATS - Mensual. Seleccione el período para continuar.; Tipo ATS - Semestral. Seleccione el Año para continuar.; El campo Organización es obligatorio | `src/com/sidesoft/localization/ecuador/withholdings/create_xml/Create_xml.java` |
| Informe (servlet) | Proceso Retenciones anuladas | `Sswh_ProcessWithholdingVoided` | Proceso Java (toolbar/background) | `Sswh_Withholdings_Voided_ID` | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_process/Sswh_ProcessWithholdingVoided.java` |
| Reporte | Impresión Genérica de Formulario | `Sswh_GenericPrintFormulary` | Informe (servlet PDF) | `0AA43DE6B4AF41D08058F2407CA11C0D|SSWH_FORMULARY_ID` | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_process/Sswh_GenericPrintFormulary.java` |
| Reporte | Withholding Statement | `RptWithholdingStatement` | Informe (servlet PDF) | `—` | com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatement.jrxml | `src/com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatement.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Asignar Cheque | Allocated Check | SSWH_AllocatedCheck | `SSWH_Allocatedcheck` | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Barre Las lineas buscando sino existe el tercero y lo actualiza por el tercero del efecto.; Reco… | — |
| Botón (PL/pgSQL) | Calcular Costo LDM | Calculate Costing LDM | Calculate Costing LDM | `sswh_calculate_costing_ldm` | INSERT INTO SSWH_AMOUNTLDM VALUES (OPERACION_PRODUCTO); ----TO FIX; SUMARIZADO DE PROMEDIO DE PRODUCTOS MATERIA PRIMA; RESULTADO COSTO PROMEDIO DEL PRODUCTO FABRICADO | — |
| Botón (PL/pgSQL) | Cheque Procesado | Processed Check | processed_check | `sswh_processed_check` | v_Message := v_Message || 'Datos = ' || v_resultado; | — |
| Botón (PL/pgSQL) | De-Asignar Cheque | De AllocatedCheck | SSWH_Deallocatedcheck | `sswh_deallocatedcheck` | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Obtengo el numero de cheque por cada tercero; Actualizo el linecheck de cada los terceros - deja… | — |
| Botón (PL/pgSQL) | Declaración de retención IVA de compra | Purchase Withholding VAT Declaration | Purchase Withholding VAT Declaration | `RptC_PurchaseWithholding.jrxml` | Purchase Withholding VAT Declaration | — |
| Botón (PL/pgSQL) | Desprocesar | Unprocess | Sswh_Unprocess | `sswh_unprocess_form` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Detalle de Compras | Purchase Detail | Purchase Detail | `RptC_PurchaseDetail.jrxml` | — | — |
| Botón (PL/pgSQL) | Detalle de Retención Renta en Compras | Withholding Incometax Declaration | Withholding Incometax Declaration | `RptC_IncometaxDet.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado CxC - Detallado | Summary Accounts Receivable | Summary Accounts Receivable | `Rpt_SumaryAcountRecCons.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado CxC - Histórico de cancelaciones | Detail Accounts Receivable | Detail Accounts Receivable | `Rpt_DetailAcountReceivab.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado de Cuenta por Pagar Detallado por Centro de Costos | Detail Accounts Payable by Cost Center | Detail Accounts Payable by Cost Center | `RptC_DetailAcountPayableByCC` | Detail Accounts Payable by Cost Center | — |
| Botón (PL/pgSQL) | Estado de CxP - Detallado | Summary Accounts Payable | Summary Accounts Payable | `Rptc_SumaryAcountPayCons.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado de CxP - Historico de Cancelaciones | Detail Accounts Payable | Detail Accounts Payable | `RptC_DetailAcountPayable.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado de CxP - Resumido | Summary Accounts Payable Total | Summary Accounts Payable Total | `Rptc_TotalAcountPayCons.jrxml` | — | — |
| Botón (PL/pgSQL) | Formas de Cobro | Payment In Methods | Payment In Methods | `Rptc_PaymentinMethods.jrxml` | Report by Payment In Methods | — |
| Botón (PL/pgSQL) | Formas de Pago | Payment Out Methods | Payment Out Methods | `Rptc_PaymentoutMethods.jrxml` | Report by Payment Out Methods | — |
| Botón (PL/pgSQL) | Formas de Pago en Compras | Purchase Form Payment | Purchase Form Payment | `RptC_PurchaseFormpayment.jrxml` | — | — |
| Botón (PL/pgSQL) | Generar ATS | Generate ATS | Generate ATS | `sswh_get_ats_ob` | Generate ATS for withholding Source and IVA | — |
| Botón (PL/pgSQL) | Generar Cheque | Generate Check | Generate_Check | `sswh_Generate_Check` | insert into temp values(v_Record_ID,v_Client_ID);; v_resultado :='nlinea :' || v_NextNo || 'nroche :' || v_nrocheck || 'ultline :' || n_linecheck ;; v_Message := v_Message || 'Datos = ' || v_resultado; | — |
| Botón (PL/pgSQL) | Generar Estado | Generate Status Line Withholding | Generate Status Line Withholding | `sswh_generate_line_with` | — | — |
| Botón (PL/pgSQL) | Generar Estado | Generate Status | Generate_Status | `sswh_Generate_Status` | insert into temp values(v_Record_ID,'aromero');; v_Message := v_Message || 'Datos = ' || v_resultado; | — |
| Botón (PL/pgSQL) | Generar Retenciones | Generate Withholding | Generate Withholding | `sswh_generate_whithholding` | — | — |
| Botón (PL/pgSQL) | Iva Compras - Por Tercero y Factura | Purchase VAT Declaration | Purchase VAT Declaration | `RptC_Purchase_iva.jrxml` | — | — |
| Botón (PL/pgSQL) | Iva Ventas - Por cliente | Sales VAT Declaration | Sales VAT Declaration | `RptC_Sales.jrxml` | — | — |
| Botón (PL/pgSQL) | Iva Ventas - Por cliente y Factura | Sales VAT Declaration Detail | Sales VAT Declaration Detail | `RptC_SalesDet.jrxml` | — | — |
| Botón (PL/pgSQL) | Procesar Comprobante de Retención | Process Withholding Receipt | sswh_process_withholding_receipt | `sswh_process_receipt` | v_Client_ID := Cur_Parameter.AD_Client_ID;; NULL, 'RDNC', 'Y', 'N', 'N', --triger no permite insertar un registro procesado (processed); raise exception '%','before insert payment schedule '||' v_Client_ID '||v_Client_I… | — |
| Botón (PL/pgSQL) | Procesar Tickets | Process Tickets | SalesTickets | `sswh_process_salesticket` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Proceso Formulario | Process Formulary | ProcessFormulary | `sswh_formulary_process` | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Actualizar Tabla Auxiliar Campo Padre - Total; Actualizar Tab… | — |
| Botón (PL/pgSQL) | Proceso Tarjeta de Retención | Process Withholding Card | Process Withholding Card | `sswh_process_wthh_card` | la transacción se encuentra contabilizada y que debe ser descontabilizada previamente para permitir su anulación | — |
| Botón (PL/pgSQL) | Reporte Balance por Pagar | Report Balance Payable | Report Balance Payable | `Rptc_BalancePayable.jrxml` | — | — |
| Botón (PL/pgSQL) | Resumen de impuesto sobre la renta | Summary Purchase Income Tax | Summary Purchase Income Tax | `RptC_PurchaseIncometax.jrxml` | — | — |
| Botón (PL/pgSQL) | Resumen de Retenciones | Summary Withholding | Summary Withholding | `RptC_SummaryWithholding.jrxml` | — | — |
| Botón (PL/pgSQL) | Retenciones en Compras | Withholding Purchases | Withholding Purchases | `RptC_PurchaseWitholdingA.jrxml` | — | — |
| Botón (PL/pgSQL) | Ventas Anuladas | Sales Voided | Sales Voided | `RptC_SalesVoided.jrxml` | — | — |
| Botón (PL/pgSQL) | Ventas de Clientes | Sales Customer | Sales Customer | `RptC_SalesAts.jrxml` | — | — |
| Botón (PL/pgSQL) | Ventas por Establecimiento | Sales by Stablishment | Sales by Stablishment | `RptC_SalesbyStablishment.jrxml` | — | — |
| Informe (servlet) | Archivo de Transferencia proveedor TXT | Archive Provider Transfer TXT | Archive Provider Transfer TXT | Java `ArchProviderTransferTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cDoctypeId` | `src/com/sidesoft/localization/ecuador/withholdings/create_xml/ArchProviderTransferTXT.java` |
| Informe (servlet) | Crear xml - ATS | Create xml - ATS | Create xml - ATS | Java `Create_xml` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cPeriodId`, Tipo ATS - Mensual. Seleccione el período para continuar.; Tipo ATS - Semestral. Seleccione el Año para continuar.; El campo Organización es obligatorio | `src/com/sidesoft/localization/ecuador/withholdings/create_xml/Create_xml.java` |
| Informe (servlet) | Proceso Retenciones anuladas | Processed Withhldings Voided | Sswh_Processed_Withhldings_Voided | Java `Sswh_ProcessWithholdingVoided` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `Sswh_Withholdings_Voided_ID` | `src/com/sidesoft/localization/ecuador/withholdings/ad_process/Sswh_ProcessWithholdingVoided.java` |
| Proceso / otro | Archivo de Transferencia Proveedor | Archive Provider Transfer | Archive Provider Transfer | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Compensación de ventas | Sales compensation | Sales compensation | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de Retención Iva en Compras | Detailed Purchases Report | Detailed Purchases Report | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Detallado (Por Vendedor) | Accounts Receivable Report by Seller | Accounts Receivable Report by Seller | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Resumido | Summary Accounts Receivable Total | Summary Accounts Receivable Total | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado CxC - Resumido (Por Vendedor) | Account receivable summarized by seller | Account receivable summarized by seller | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Formas de cobro | Forms of payment | Forms of payment | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de Cuentas Vencidas | Report of past due accounts | Report of past due accounts | *(OBUIAPP / manual)* | Report of past due accounts | — |
| Proceso / otro | Reporte de Retenciones anuladas | Report of Withholdings Voided | Report of Withholdings Voided | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Retenciones Emitidas | Withholdings Issued | Withholdings Issued | *(OBUIAPP / manual)* | Withholdings Issued | — |
| Proceso / otro | Retenciones por Recuperar | Withholdings By Recovered | Withholdings By Recovered | *(OBUIAPP / manual)* | Withholdings By Recovered | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Asignar Cheque | Allocated Check | PL `SSWH_Allocatedcheck` | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Barre Las lineas buscando sino existe el tercero y lo actualiza por el tercero del efecto.; Reco… | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Barre Las lineas buscando sino existe el tercero y lo actualiza por el tercero del efecto.; Recorre los Terceros de las lineas del extracto; raise exception '%', Cur_PartnerAsc.line ||'-'||Cur_PartnerAsc.em_sswh_partner_id;; raise exception '%', Cur_PartnerAsc.line ||'-'||Cur_PartnerAsc.em_sswh_partner_id||'-'||v_Partner_ID||'-'||v_Bankstatement_ID; |
| Botón (PL/pgSQL) | Calcular Costo LDM | Calculate Costing LDM | PL `sswh_calculate_costing_ldm` | INSERT INTO SSWH_AMOUNTLDM VALUES (OPERACION_PRODUCTO); ----TO FIX; SUMARIZADO DE PROMEDIO DE PRODUCTOS MATERIA PRIMA; RESULTADO COSTO PROMEDIO DEL PRODUCTO FABRICADO | INSERT INTO SSWH_AMOUNTLDM  VALUES (OPERACION_PRODUCTO); ----TO FIX; SUMARIZADO DE PROMEDIO DE PRODUCTOS MATERIA PRIMA; RESULTADO COSTO PROMEDIO DEL PRODUCTO FABRICADO |
| Botón (PL/pgSQL) | Cheque Procesado | Processed Check | PL `sswh_processed_check` | v_Message := v_Message || 'Datos = ' || v_resultado; | v_Message := v_Message || 'Datos = ' || v_resultado; |
| Botón (PL/pgSQL) | De-Asignar Cheque | De AllocatedCheck | PL `sswh_deallocatedcheck` | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Obtengo el numero de cheque por cada tercero; Actualizo el linecheck de cada los terceros - deja… | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Obtengo el numero de cheque por cada tercero; Actualizo el linecheck de cada los terceros - dejandolo vacios - elimnio el nro de cheque; Actualizo el estado del cheque Ocupado - Disponible |
| Botón (PL/pgSQL) | Declaración de retención IVA de compra | Purchase Withholding VAT Declaration | PL `RptC_PurchaseWithholding.jrxml` | Purchase Withholding VAT Declaration | — |
| Botón (PL/pgSQL) | Desprocesar | Unprocess | PL `sswh_unprocess_form` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Detalle de Compras | Purchase Detail | PL `RptC_PurchaseDetail.jrxml` | — | — |
| Botón (PL/pgSQL) | Detalle de Retención Renta en Compras | Withholding Incometax Declaration | PL `RptC_IncometaxDet.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado CxC - Detallado | Summary Accounts Receivable | PL `Rpt_SumaryAcountRecCons.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado CxC - Histórico de cancelaciones | Detail Accounts Receivable | PL `Rpt_DetailAcountReceivab.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado de Cuenta por Pagar Detallado por Centro de Costos | Detail Accounts Payable by Cost Center | PL `RptC_DetailAcountPayableByCC` | Detail Accounts Payable by Cost Center | — |
| Botón (PL/pgSQL) | Estado de CxP - Detallado | Summary Accounts Payable | PL `Rptc_SumaryAcountPayCons.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado de CxP - Historico de Cancelaciones | Detail Accounts Payable | PL `RptC_DetailAcountPayable.jrxml` | — | — |
| Botón (PL/pgSQL) | Estado de CxP - Resumido | Summary Accounts Payable Total | PL `Rptc_TotalAcountPayCons.jrxml` | — | — |
| Botón (PL/pgSQL) | Formas de Cobro | Payment In Methods | PL `Rptc_PaymentinMethods.jrxml` | Report by Payment In Methods | — |
| Botón (PL/pgSQL) | Formas de Pago | Payment Out Methods | PL `Rptc_PaymentoutMethods.jrxml` | Report by Payment Out Methods | — |
| Botón (PL/pgSQL) | Formas de Pago en Compras | Purchase Form Payment | PL `RptC_PurchaseFormpayment.jrxml` | — | — |
| Botón (PL/pgSQL) | Generar ATS | Generate ATS | PL `sswh_get_ats_ob` | Generate ATS for withholding Source and IVA | — |
| Botón (PL/pgSQL) | Generar Cheque | Generate Check | PL `sswh_Generate_Check` | insert into temp values(v_Record_ID,v_Client_ID);; v_resultado :='nlinea :' || v_NextNo || 'nroche :' || v_nrocheck || 'ultline :' || n_linecheck ;; v_Message := v_Message || 'Datos = ' || v_resultado; | insert into temp values(v_Record_ID,v_Client_ID);; v_resultado :='nlinea :' || v_NextNo || 'nroche :' || v_nrocheck || 'ultline :' || n_linecheck ;; v_Message := v_Message || 'Datos = ' || v_resultado; |
| Botón (PL/pgSQL) | Generar Estado | Generate Status Line Withholding | PL `sswh_generate_line_with` | — | — |
| Botón (PL/pgSQL) | Generar Estado | Generate Status | PL `sswh_Generate_Status` | insert into temp values(v_Record_ID,'aromero');; v_Message := v_Message || 'Datos = ' || v_resultado; | insert into temp values(v_Record_ID,'aromero');; v_Message := v_Message || 'Datos = ' || v_resultado; |
| Botón (PL/pgSQL) | Generar Retenciones | Generate Withholding | PL `sswh_generate_whithholding` | — | — |
| Botón (PL/pgSQL) | Iva Compras - Por Tercero y Factura | Purchase VAT Declaration | PL `RptC_Purchase_iva.jrxml` | — | — |
| Botón (PL/pgSQL) | Iva Ventas - Por cliente | Sales VAT Declaration | PL `RptC_Sales.jrxml` | — | — |
| Botón (PL/pgSQL) | Iva Ventas - Por cliente y Factura | Sales VAT Declaration Detail | PL `RptC_SalesDet.jrxml` | — | — |
| Botón (PL/pgSQL) | Procesar Comprobante de Retención | Process Withholding Receipt | PL `sswh_process_receipt` | v_Client_ID := Cur_Parameter.AD_Client_ID;; NULL, 'RDNC', 'Y', 'N', 'N', --triger no permite insertar un registro procesado (processed); raise exception '%','before insert payment schedule '||' v_Client_ID '||v_Client_I… | v_Client_ID := Cur_Parameter.AD_Client_ID;; NULL, 'RDNC', 'Y', 'N', 'N', --triger no permite insertar un registro procesado (processed); raise exception '%','before insert payment schedule '||' v_Client_ID '||v_Client_ID || ' v_Org_ID '||v_Org_ID|| ' v_User_ID '|| v_User_ID; ||' v_invoice_id '||v_invoice_id|| ' v_datedoc '||v_datedoc||' v_fin_paymentmethod_id '|| v_fin_paymentmethod_id; ||' v_currency_id '|| v_currency_id ||' v_taxamt '|| v_taxamt ||' v_documentno '|| v_documentno;; ((select grandtotal from c_invoice where c_invoice_id = cur_receipt.c_invoice_id)-cur_receipt.taxamt), |
| Botón (PL/pgSQL) | Procesar Tickets | Process Tickets | PL `sswh_process_salesticket` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Proceso Formulario | Process Formulary | PL `sswh_formulary_process` | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Actualizar Tabla Auxiliar Campo Padre - Total; Actualizar Tab… | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Actualizar Tabla Auxiliar Campo Padre - Total; Actualizar Tabla Auxiliar Campo Hijo - Total; Inserta todas las lineas de la tabla temporal a la tabla formulary lines.; Recorre la lista de la vista sswh_salesdet_f104_v - Datos del Formulario 104 |
| Botón (PL/pgSQL) | Proceso Tarjeta de Retención | Process Withholding Card | PL `sswh_process_wthh_card` | la transacción se encuentra contabilizada y que debe ser descontabilizada previamente para permitir su anulación | la transacción se encuentra contabilizada y que debe ser descontabilizada previamente para permitir su anulación |
| Botón (PL/pgSQL) | Reporte Balance por Pagar | Report Balance Payable | PL `Rptc_BalancePayable.jrxml` | — | — |
| Botón (PL/pgSQL) | Resumen de impuesto sobre la renta | Summary Purchase Income Tax | PL `RptC_PurchaseIncometax.jrxml` | — | — |
| Botón (PL/pgSQL) | Resumen de Retenciones | Summary Withholding | PL `RptC_SummaryWithholding.jrxml` | — | — |
| Botón (PL/pgSQL) | Retenciones en Compras | Withholding Purchases | PL `RptC_PurchaseWitholdingA.jrxml` | — | — |
| Botón (PL/pgSQL) | Ventas Anuladas | Sales Voided | PL `RptC_SalesVoided.jrxml` | — | — |
| Botón (PL/pgSQL) | Ventas de Clientes | Sales Customer | PL `RptC_SalesAts.jrxml` | — | — |
| Botón (PL/pgSQL) | Ventas por Establecimiento | Sales by Stablishment | PL `RptC_SalesbyStablishment.jrxml` | — | — |
| Informe (servlet) | Archivo de Transferencia proveedor TXT | Archive Provider Transfer TXT | Java `ArchProviderTransferTXT` | Proceso Openbravo registro `cDoctypeId` | Proceso Openbravo registro `cDoctypeId` |
| Informe (servlet) | Crear xml - ATS | Create xml - ATS | Java `Create_xml` | Proceso Openbravo registro `cPeriodId`, Tipo ATS - Mensual. Seleccione el período para continuar.; Tipo ATS - Semestral. Seleccione el Año para continuar.; El campo Organización es obligatorio | Tipo ATS - Mensual. Seleccione el período para continuar.; Tipo ATS - Semestral. Seleccione el Año para continuar.; El campo Organización es obligatorio; El campo Organización ha excedido los 500 caracteres permitidos. |
| Informe (servlet) | Proceso Retenciones anuladas | Processed Withhldings Voided | Java `Sswh_ProcessWithholdingVoided` | Proceso Openbravo registro `Sswh_Withholdings_Voided_ID` | Proceso Openbravo registro `Sswh_Withholdings_Voided_ID` |
| Proceso / otro | Archivo de Transferencia Proveedor | Archive Provider Transfer | — | — | — |
| Proceso / otro | Compensación de ventas | Sales compensation | — | — | — |
| Proceso / otro | Detalle de Retención Iva en Compras | Detailed Purchases Report | — | — | — |
| Proceso / otro | Estado CxC - Detallado (Por Vendedor) | Accounts Receivable Report by Seller | — | — | — |
| Proceso / otro | Estado CxC - Resumido | Summary Accounts Receivable Total | — | — | — |
| Proceso / otro | Estado CxC - Resumido (Por Vendedor) | Account receivable summarized by seller | — | — | — |
| Proceso / otro | Formas de cobro | Forms of payment | — | — | — |
| Proceso / otro | Reporte de Cuentas Vencidas | Report of past due accounts | — | Report of past due accounts | — |
| Proceso / otro | Reporte de Retenciones anuladas | Report of Withholdings Voided | — | — | — |
| Proceso / otro | Retenciones Emitidas | Withholdings Issued | — | Withholdings Issued | — |
| Proceso / otro | Retenciones por Recuperar | Withholdings By Recovered | — | Withholdings By Recovered | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Impresión Genérica de Formulario | GENERIC - PRINT FORMULARY | GENERIC - PRINT FORMULARY | Java `Sswh_GenericPrintFormulary` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `0AA43DE6B4AF41D08058F2407CA11C0D|SSWH_FORMULARY_ID`. | `src/com/sidesoft/localization/ecuador/withholdings/ad_process/Sswh_GenericPrintFormulary.java` |
| Reporte | Withholding Statement | Withholding Statement | PRINTWHSTATEMENT | Java `RptWithholdingStatement` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatement.jrxml`; contexto sesión `—`. | `src/com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatement.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 44**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **2**; archivos `*.jrxml` en el repo = **44**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Impresión Genérica de Formulario | `GENERIC - PRINT FORMULARY` | Java `Sswh_GenericPrintFormulary`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | GENERIC - PRINT FORMULARY |
| 2 | Withholding Statement | `PRINTWHSTATEMENT` | Java `RptWithholdingStatement`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Withholding Statement |

### Plantillas sin proceso en diccionario

- `src/com/sidesoft/localization/ecuador/withholdings/reports/Fin_Payment.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_DetailAcountPayable.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_DetailAcountPayableByCostCenter.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_IncometaxDet.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_Invoice.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_PurchaseDetail.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_PurchaseDetail_A.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_PurchaseFormpayment.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_PurchaseIncometax.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_PurchaseWithholding.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_PurchaseWitholdingA.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_Purchase_iva.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_Sales.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_SalesAts.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_SalesCompensations.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_SalesDet.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_SalesFormPayment.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_SalesVoided.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_SalesbyStablishment.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptC_SummaryWithholding.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptFIN_Payment.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptSsw_WithholdingsByRecovered.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptSswh_Formulary.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptSswh_Formulary104.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptSswh_WithholdingVoided.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptSswh_WithholdingsIssued.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatement.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatementA.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatementB.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rpt_Account_Receivable_salesman.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rpt_Account_Receivable_salesman_Summary.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rpt_ArchiveProviderTransfer.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rpt_DetailAcountReceivab.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rpt_SumaryAcountRecCons.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rpt_SumaryAcountReceivab.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rptc_BalancePayable.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rptc_PaymentinMethods.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rptc_PaymentoutMethods.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rptc_SumaryAcountPayCons.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rptc_SumaryAcountPayable.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rptc_TotalAcountPayCons.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rptc_TotalAcountPayable.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/Rptc_TotalAcountReceivable.jrxml`
- `src/com/sidesoft/localization/ecuador/withholdings/reports/RtpC_Report_of_past_due_accounts.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `SSWH_AutorizationMustBeNumeric` | Withholding Authorization must be numeric. | Withholding Authorization must be numeric. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_DocumentOrderDeleteFailed` | The selected Order can not be deleted because it has one or more lines created. | The selected Order can not be deleted because it has one or more lines created. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_ErrorWithholdingSource` | The Tax Base of the selected invoice must be higher than the Income Tax. | The Tax Base of the selected invoice must be higher than the Income Tax. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_NoDocumentNoFormat` | The format of Document No. must be like 000-000-000000000. | The format of Document No. must be like 000-000-000000000. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_AutorizationMustBeLengthNumeric` | Withholding Authorization must have 10 or 37 or 49 digits | Withholding Authorization must have 10 or 37 or 49 digits | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_Authoriza_Datefrom_Dateto` | Starting Date must precede Ending Date. | Starting Date must precede Ending Date. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_Withh_Ven_Numbfrom_Numbto` | Number From must be less than Number To. | Number From must be less than Number To. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_CifMustEndWith` | Tax ID must end with 00 # | Tax ID must end with 00 # | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_DocumentCompleted` | No changes can be made, Document Completed. | No changes can be made, Document Completed. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_WithholdingUnauthorized` | Unauthorized Withholding Statement. | Unauthorized Withholding Statement. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_DocumentInvoiceDeleteFailed` | The selected Invoice can not be deleted because it has one or more lines created. | The selected Invoice can not be deleted because it has one or more lines created. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_InvoiceNotProcessed` | Invoices must be processed. | Invoices must be processed. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_SetupFormError` | It is still necessary to create the configuration of the codes of Form 103/104. | It is still necessary to create the configuration of the codes of Form 103/104. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_OnlyOneAuthorizationType` | Only one Authorization Type is allowed. | Only one Authorization Type is allowed. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_WithholdingCardDeleteError` | The current record can not be deleted because it is in a state Completed/Canceled. | The current record can not be deleted because it is in a state Completed/Canceled. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_PasMustBeLengthNumeric` | Tax ID must have 11 digits | Tax ID must have 11 digits | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_CheckbookpostInvoice` | No ingresar 2 veces la misma factura en este cheque. | No ingresar 2 veces la misma factura en este cheque. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_Withh_Ven_Datefrom_Dateto` | Starting Date must precede Ending Date. | Starting Date must precede Ending Date. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_SupplierReferenceUnauthorized` | Supplier Reference Unauthorized. | Supplier Reference Unauthorized. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_Unauthorized` | Unauthorized Transaction Document. | Unauthorized Transaction Document. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_RECEIPT_PROCESSED` | It is not possible to post / process the invoice because it is linked from a withholding receipt. | It is not possible to post / process the invoice because it is linked from a withholding receipt. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_FormularyComplete` | The document can not be deleted because it is in the Completed state. | The document can not be deleted because it is in the Completed state. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_InvoiceNotPosted` | Invoices must be posted. | Invoices must be posted. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_ErrorWithholdingSourceZero` | The income tax must be greater than 0. | The income tax must be greater than 0. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_ErrorWithholdingIVA` | The taxable amount of the selected invoice must be higher than the VAT. | The taxable amount of the selected invoice must be higher than the VAT. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_NifMustBeLengthNumeric` | Tax ID must have 10 digits | Tax ID must have 10 digits | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_CifDigitLocation` | Tax ID location incorrect code. | Tax ID location incorrect code. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_NoWithholdingTaxIncomeForTheDate` | No Withholding tax (Income) found for the date. | No Withholding tax (Income) found for the date. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_ErrorSetupForm104` | Missing to create the code configuration of Form 104. | Missing to create the code configuration of Form 104. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_NoTypeOrCodeOfLivelihood` | Type and Code of Livelihood are mandatory. | Type and Code of Livelihood are mandatory. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_ActiveFormCodeError` | It has more than active configuration of the codes of Form 103/104. | It has more than active configuration of the codes of Form 103/104. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_MustBeNumeric` | Tax ID must be numeric. | Tax ID must be numeric. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sswh_error_code_exclude` | Only one type of tax can have the Exclude withholding code configuration active. | Only one type of tax can have the Exclude withholding code configuration active. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_ValidateDatePurchaseInvoice` | The date of the invoice must be less than or equal to the posted date. | The date of the invoice must be less than or equal to the posted date. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_TaxPayerOrgBp` | Taxpayer not configured in the withholding agent line of the type of organization agent | Taxpayer not configured in the withholding agent line of the type of organization agent | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_DigitVerfied` | Tax ID Digit Verifier | Tax ID Digit Verifier | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_NumberRangeOverlap` | Number Range Overlap. | Number Range Overlap. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_FormularyHeader` | This transaction can not be deleted because it has lines created. | This transaction can not be deleted because it has lines created. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_statePostedToDelete` | It is not allowed to delete a record in processed state | It is not allowed to delete a record in processed state | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_NoWithholdingTaxVATForTheDate` | No Withholding tax (VAT) found for the date. | No Withholding tax (VAT) found for the date. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_NoWithholdingType` | The Tax is not a Withholding Tax. | The Tax is not a Withholding Tax. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_VouchersNumber_Zero` | The number of vouchers must be greater than zero. | The number of vouchers must be greater than zero. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_ApplieWithhLivelihood` | Invalid withholding document due to combination of Withcolding and Livelihoodt | Invalid withholding document due to combination of Withcolding and Livelihoodt | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_DateRangeOverlap` | Date range overlap. | Date range overlap. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_All_Values_Zero` | No value entered can be negative. | No value entered can be negative. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_Authoriza_Numbfrom_Numbto` | Number From must be less than Number To. | Number From must be less than Number To. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_CifMustBeLengthNumeric` | Tax ID must have 13 digits | Tax ID must have 13 digits | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWH_NoReferenceNo` | The Reference No. has already been used by another document for the same Provider. | The Reference No. has already been used by another document for the same Provider. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_Retentions_Zero` | At least one retention value must be greater than 0. | At least one retention value must be greater than 0. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_ErrorSetupForm103` | Missing create the code configuration of Form 103. | Missing create the code configuration of Form 103. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sswh_FormularyLine` | The lines can not be deleted because the document is in the Completed state. | The lines can not be deleted because the document is in the Completed state. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

Dentro del módulo, la programación en Java permite la implementación de lógica de negocio compleja y la gestión de datos a través de clases como ConceptInfo, que facilitan el manejo de registros relacionados con las retenciones. Estas clases están diseñadas para ser utilizadas dentro de la arquitectura de Openbravo, proporcionando funcionalidades sólidas y eficientes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.localization.ecuador.withholdings`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ConceptInfo` | accounting | — | — | `src/com/sidesoft/localization/ecuador/withholdings/accounting/ConceptInfo.java` |
| `DocLine_SswhWithhCardCredit` | accounting | DocLine | — | `src/com/sidesoft/localization/ecuador/withholdings/accounting/DocLine_SswhWithhCardCredit.java` |
| `DocSswhWithhCardCredit` | accounting | AcctServer | — | `src/com/sidesoft/localization/ecuador/withholdings/accounting/DocSswhWithhCardCredit.java` |
| `SSWH_BankAccount` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/SSWH_BankAccount.java` |
| `SS_CheckBook_BankAccount` | ad_callouts | HttpSecureAppServlet | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/SS_CheckBook_BankAccount.java` |
| `SS_CheckBook_LineCheck` | ad_callouts | HttpSecureAppServlet | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/SS_CheckBook_LineCheck.java` |
| `SS_GranTotal` | ad_callouts | HttpSecureAppServlet | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/SS_GranTotal.java` |
| `SS_InvoiceReference` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/SS_InvoiceReference.java` |
| `SS_Withholding_DocType` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/SS_Withholding_DocType.java` |
| `Sswh_Invoice_WithholdingDate` | ad_callouts | SE_Invoice_AccountingDate | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/Sswh_Invoice_WithholdingDate.java` |
| `Sswh_NewSecuence_WithholdingCard` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/Sswh_NewSecuence_WithholdingCard.java` |
| `Sswh_Update_Document_Withholding_Voided` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/Sswh_Update_Document_Withholding_Voided.java` |
| `UpdateDocSeqSalesTickets` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/UpdateDocSeqSalesTickets.java` |
| `UpdateDocumentSequence` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/localization/ecuador/withholdings/ad_callouts/UpdateDocumentSequence.java` |
| `Sswh_GenericPrintFormulary` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/withholdings/ad_process/Sswh_GenericPrintFormulary.java` |
| `Sswh_PaymentMonitorProcess` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/withholdings/ad_process/Sswh_PaymentMonitorProcess.java` |
| `Sswh_ProcessWithholdingVoided` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/localization/ecuador/withholdings/ad_process/Sswh_ProcessWithholdingVoided.java` |
| `ArchProviderTransferTXT` | create_xml | DalBaseProcess | ComponentProvider / UI | `src/com/sidesoft/localization/ecuador/withholdings/create_xml/ArchProviderTransferTXT.java` |
| `Create_xml` | create_xml | DalBaseProcess | — | `src/com/sidesoft/localization/ecuador/withholdings/create_xml/Create_xml.java` |
| `AuthorizationEventHandle` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/localization/ecuador/withholdings/event/AuthorizationEventHandle.java` |
| `CreditNoteReference` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/localization/ecuador/withholdings/event/CreditNoteReference.java` |
| `InvoiceEventHandle` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/localization/ecuador/withholdings/event/InvoiceEventHandle.java` |
| `OrderEventHandle` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/localization/ecuador/withholdings/event/OrderEventHandle.java` |
| `SSWHWithholdingvendorEventHandle` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/localization/ecuador/withholdings/event/SSWHWithholdingvendorEventHandle.java` |
| `SalesTicketBusinessEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/localization/ecuador/withholdings/event/SalesTicketBusinessEvent.java` |
| `Sswh_FormularyEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/localization/ecuador/withholdings/event/Sswh_FormularyEvent.java` |
| `Sswh_UpdateDocumentWithholdingCardEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/localization/ecuador/withholdings/event/Sswh_UpdateDocumentWithholdingCardEvent.java` |
| `UpdateSequenceWithholdingVoided` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/localization/ecuador/withholdings/event/UpdateSequenceWithholdingVoided.java` |
| `RptWithholdingStatement` | reports | HttpSecureAppServlet | — | `src/com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatement.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSWH_AUTORIZATION_TRG` | `c_invoice` | before INSERT/UPDATE | No.Autorizacion Factura debe ser numérico.; No.Autorizacion Factura debe tener 10 o 37 o 49 digitos. |
| Trigger `SSWH_BPARTNER_TRG` | `c_bpartner` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_BP_BANKACCT_DNI_TRG` | `c_bp_bankaccount` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_CHECKBOOKPOSLINE_TR` | `sswh_checkbookposline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_CHECKBOOKPOSLINE_TR1` | `sswh_checkbookposline` | after INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_CHECKBOOK_TR` | `sswh_checkbook` | after INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_CHECKBOOK_TR1` | `sswh_checkbook` | after INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_DIVIDENS_YEAR_TRG` | `c_invoice` | after INSERT/UPDATE | El campo Año declaración de dividendo no debe estar vacío cuando el tipo de documento es dividendo. |
| Trigger `SSWH_DOCTYPE_TRG` | `c_doctype` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_EXCLUDE_CODE_TRG` | `c_tax` | before UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_FORMULARYLINE_TRG` | `sswh_formularyline` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_FORMULARY_TRG` | `sswh_formulary` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_GRANDTOTAL_VAL_TRG` | `c_invoice` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_INVOICEAUTHORIZATION_TRG1` | `c_invoice` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_INVOICEAUTHORIZATION_TRG2` | `c_invoice` | after INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_INVOICEAUTHORIZATION_TRG3` | `c_invoice` | before INSERT/UPDATE | v_establecimiento := substr(v_reference, 1, 3);; v_NoFactura := TO_NUMBER(substr(v_reference, 9, 9));; /* Select authorization by document type, the invoice 'date' must be between authorization 'date from' and 'date to'… |
| Trigger `SSWH_INVOICELINE_TRG` | `c_invoiceline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_INVOICELINE_TRG2` | `c_invoiceline` | after UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_INVOICETAX_TRG` | `c_invoicetax` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_INVOICE_TRG1` | `c_invoice` | after INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_INVOICE_TRG2` | `c_invoice` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_RECEIPT_TAX_TRG` | `sswh_receipt_tax` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_RECEIPT_TRG` | `sswh_receipt` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_TAX_TRG` | `c_tax` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_T_INVOICE_REFNUMBER` | `c_invoice` | before INSERT/UPDATE | Select authorization by business partner, the invoice 'date' must be between authorization 'date from' and 'date to'. |
| Trigger `SSWH_UPDATE_DATEINLINE` | `c_bankstatement` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_VALIDATEAUTHORIZATION_TRG` | `sswh_withholding_vendor` | before INSERT/UPDATE | Validación reutilizable de campos. |
| Trigger `SSWH_VALIDATEDATE_TRG` | `c_invoice` | before INSERT/UPDATE | Validación reutilizable de campos. |
| Trigger `SSWH_WITHH_AUTHORIZATIONNO_TRG` | `sswh_withholdings_voided` | before INSERT/UPDATE | El número de autorización debe ser de 10 o 37 dígitos |
| Trigger `SSWH_WITHH_CARD_TRG` | `sswh_withh_card_credit` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWH_WITHH_STATE_VOIDED_TRG` | `sswh_withholdings_voided` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Segf - Withholdings` | `(C_TAX.EM_Sswh_Ats_Iva = 'Y' OR  C_TAX.EM_Sswh_Ats_Source = 'Y') AND C_TAX.EM_Segf_Withholding_Type = @Withholding_Type@` |
| AD_VAL_RULE | — | `Sswh_ValidUser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Sswh_Client` | `c_bpartner.iscustomer='Y'` |
| AD_VAL_RULE | — | `Sswh_Customer` | `c_bpartner.iscustomer='Y'` |
| AD_VAL_RULE | — | `C_DocType Withholding Receipt` | `C_DocType.DocBaseType = 'SSWH_WHR' AND (AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.AD_Org_ID, @#AD_Client_ID@) <> '-1' OR CO` |
| AD_VAL_RULE | — | `Sswh_Payment_Method_Active` | `isactive='Y'` |
| AD_VAL_RULE | — | `Withholding Taxes` | `exists (select em_sswh_withholdingtype from c_taxcategory where c_taxcategory_id = c_tax.c_taxcategory_id and em_sswh_wi` |
| AD_VAL_RULE | — | `sswh_method_user` | `em_sswh_withholdingtype  IN (SELECT  em_sswh_withholdingtype FROM c_taxcategory WHERE c_taxcategory_id   IN (SELECT  c_t` |
| AD_VAL_RULE | — | `Sswh_SalesRep` | `C_BPARTNER.ISSALESREP='Y'` |
| AD_VAL_RULE | — | `Automatic Payment Bank Account` | `EM_Sswh_Paymentautomatic = 'Y' and C_BPartner_ID = @C_BPartner_ID@` |
| AD_VAL_RULE | — | `SSWH Logged User` | `AD_User.AD_User_ID = @#AD_User_ID@` |
| AD_VAL_RULE | — | `Sswh User Validate` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Sswh_Doctype_WithholdingReference` | `C_DOCTYPE.DOCBASETYPE='SSWH_W_VOIDED' AND C_DOCTYPE.AD_TABLE_ID = '61C5D42FB120458F983EE2F27B62C16E'` |
| AD_VAL_RULE | — | `sswh_financial_user` | `Fin_Financial_Account_ID IN (SELECT Fin_Financial_Account_ID FROM Fin_Finacc_Paymentmethod WHERE Fin_Paymentmethod_ID=@F` |
| AD_VAL_RULE | — | `Is Withholding` | `em_sswh_iswithholding='Y'` |
| AD_VAL_RULE | — | `Withholding Card Invoice` | `C_INVOICE.ISSOTRX='Y' AND C_INVOICE.POSTED='Y' AND C_INVOICE.C_BPARTNER_ID = @C_BPARTNER_ID@` |
| AD_VAL_RULE | — | `Authorization_Vendor_Purchase` | `sswh_withholding_vendor.c_bpartner_id=@c_bpartner_id@ and ci.@dateinvoiced@ between sswh_withholding_vendor.datefrom and` |
| AD_VAL_RULE | — | `SSWH_OPEN_PERIOD_VALIDATE` | `C_Period.openclose='C'` |
| AD_VAL_RULE | — | `Withholding at the Source` | `em_sswh_iswithholdingsource = 'Y'` |
| AD_VAL_RULE | — | `c_debt_payment_bpartner` | `exists (select * from sswh_checkbookpos where sswh_checkbookpos.sswh_checkbookpos_id=@sswh_checkbookpos_id@ and c_debt_p` |
| AD_VAL_RULE | — | `Invoice Reference for Partner` | `C_invoice.C_BPartner_ID = @C_BPartner_ID@ and C_invoice.dateinvoiced >= @em_sswh_dateendinvoice@` |
| AD_VAL_RULE | — | `Validate Bank Account  Payment Out` | `C_BP_BankAccount.C_BPartner_ID = @C_BPartner_ID@` |
| AD_VAL_RULE | — | `Validate Withholdings Type of Livelihood` | `SSWH_Livelihoodt.SSWH_Livelihoodt_ID in (select  SSWH_Livelihoodt_ID from SSWH_Livelihoodt 
where isrefund = (case when ` |
| AD_VAL_RULE | — | `Is Vendor Validate` | `C_BPARTNER.IsSalesRep='Y'` |
| AD_VAL_RULE | — | `Validate DocBaseType Withholding Card` | `C_DOCTYPE.DOCBASETYPE = 'SSWH_WITHH_CARD' AND C_DOCTYPE.AD_TABLE_ID  = '610D781C7DE142108BDBBBF84107C394'` |
| AD_VAL_RULE | — | `SswhSalesTicketValidDoc` | `C_DOCTYPE.DOCBASETYPE = 'SSWH_SLST' AND C_DOCTYPE.AD_TABLE_ID  = '7239C7DF18A34DF5B4E1E03FA4697CF4'` |
| AD_VAL_RULE | — | `SSWH_OrgAll` | `AD_ORG_ID <> '0'` |
| AD_VAL_RULE | — | `Withholding Receipt` | `issotrx = 'Y' AND (em_sswh_receipt_id IS NULL OR em_sswh_receipt_id = @Sswh_Receipt_ID@) AND c_invoice_id NOT IN (SELECT` |
| Java event/validator | `AuthorizationEventHandle` | persistencia/UI | *(leer `src/com/sidesoft/localization/ecuador/withholdings/event/AuthorizationEventHandle.java`)* |
| Java event/validator | `InvoiceEventHandle` | persistencia/UI | *(leer `src/com/sidesoft/localization/ecuador/withholdings/event/InvoiceEventHandle.java`)* |
| Java event/validator | `OrderEventHandle` | persistencia/UI | *(leer `src/com/sidesoft/localization/ecuador/withholdings/event/OrderEventHandle.java`)* |
| Java event/validator | `SSWHWithholdingvendorEventHandle` | persistencia/UI | *(leer `src/com/sidesoft/localization/ecuador/withholdings/event/SSWHWithholdingvendorEventHandle.java`)* |
| Java event/validator | `SalesTicketBusinessEvent` | persistencia/UI | *(leer `src/com/sidesoft/localization/ecuador/withholdings/event/SalesTicketBusinessEvent.java`)* |
| Java event/validator | `Sswh_FormularyEvent` | persistencia/UI | *(leer `src/com/sidesoft/localization/ecuador/withholdings/event/Sswh_FormularyEvent.java`)* |
| Java event/validator | `Sswh_UpdateDocumentWithholdingCardEvent` | persistencia/UI | *(leer `src/com/sidesoft/localization/ecuador/withholdings/event/Sswh_UpdateDocumentWithholdingCardEvent.java`)* |
| Función PL `sswh_allocatedcheck` | — | invocación proceso | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Barre Las lineas buscando sino existe el tercero y lo actualiza por el tercero del efecto. |
| Función PL `sswh_asterisk` | — | invocación proceso | RAISE NOTICE '%','CANTIDA DE CARACTERS ES:   ' || cantidad; |
| Función PL `sswh_c_location_get` | — | invocación proceso | c_region_id = sswh_c_region_get(region) AND |
| Función PL `sswh_calculate_costing_ldm` | — | invocación proceso | INSERT INTO SSWH_AMOUNTLDM  VALUES (OPERACION_PRODUCTO); ----TO FIX; SUMARIZADO DE PROMEDIO DE PRODUCTOS MATERIA PRIMA; RESULTADO COSTO PROMEDIO DEL PRODUCTO FABRICADO |
| Función PL `sswh_convert_numbertoletters` | — | invocación proceso | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test); |
| Función PL `sswh_deallocatedcheck` | — | invocación proceso | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Obtengo el numero de cheque por cada tercero |
| Función PL `sswh_execute_ats_sql` | — | invocación proceso | Para generar el ATS semestral seleccione el Año |
| Función PL `sswh_formulary_process` | — | invocación proceso | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Actualizar Tabla Auxiliar Campo Padre - Total |
| Función PL `sswh_generate_check` | — | invocación proceso | insert into temp values(v_Record_ID,v_Client_ID);; v_resultado :='nlinea :' || v_NextNo || 'nroche :' || v_nrocheck || 'ultline :' || n_linecheck ;; v_Message := v_Message || 'Datos = ' || v_resultado; |
| Función PL `sswh_generate_status` | — | invocación proceso | insert into temp values(v_Record_ID,'aromero');; v_Message := v_Message || 'Datos = ' || v_resultado; |
| Función PL `sswh_get_amount_form` | — | invocación proceso | RAISE notice '%', '@FormulaSyntaxError@'; --OBTG:-20000--*/ |
| Función PL `sswh_get_descriptiontax` | — | invocación proceso | v_SqlResult:= 'select coalesce((' || v_SqlResult ||  '),'''|| '-' || '''' || ') from dual' ; |
| Función PL `sswh_inout_post_posob` | — | invocación proceso | PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL) ;; Check the header belongs to a organization where transactions are posible and ready to use; Check the period control is opened (only if it is legal entity with accounting) |
| Función PL `sswh_invoice_post_posob` | — | invocación proceso | PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL) ;; Allow to complete an invoice only in these cases:; Now, needs to go to END_PROCESSING to unlock |
| Función PL `sswh_movement_post_batch` | — | invocación proceso | Start Processing ------------------------------------------------------; Check the header belongs to a organization where transactions are posible and ready to use; Check the period control is opened (only if it is legal entity with accounting) |
| Función PL `sswh_order_post1__posob` | — | invocación proceso | PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL) ;; Get the name of the org of the Order. Added by P.Sarobe; Verify not managed debtPayments added by ALO |
| Función PL `sswh_process_receipt` | — | invocación proceso | v_Client_ID := Cur_Parameter.AD_Client_ID;; NULL, 'RDNC', 'Y', 'N', 'N', --triger no permite insertar un registro procesado (processed); raise exception '%','before insert payment schedule '||' v_Client_ID '||v_Client_ID || ' v_Org_ID '||v_Org_ID|| ' v_User_ID '|| v_User_ID |
| Función PL `sswh_process_wthh_card` | — | invocación proceso | la transacción se encuentra contabilizada y que debe ser descontabilizada previamente para permitir su anulación |
| Función PL `sswh_processed_check` | — | invocación proceso | v_Message := v_Message || 'Datos = ' || v_resultado; |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL son esenciales para mantener la integridad de los datos en las tablas asociadas con el módulo de retenciones. Por ejemplo, los triggers validan automáticamente que los datos ingresados cumplan con los requisitos fiscales, previniendo errores en la entrada de datos. Las funciones PL permiten llevar a cabo procesos complejos y automatizados que son necesarios para el cálculo y la gestión de retenciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSWH_UPDATE_DATEINLINE` | `c_bankstatement` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_UPDATE_DATEINLINE.xml` |
| `SSWH_BP_BANKACCT_DNI_TRG` | `c_bp_bankaccount` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_BP_BANKACCT_DNI_TRG.xml` |
| `SSWH_BPARTNER_TRG` | `c_bpartner` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_BPARTNER_TRG.xml` |
| `SSWH_DOCTYPE_TRG` | `c_doctype` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_DOCTYPE_TRG.xml` |
| `SSWH_AUTORIZATION_TRG` | `c_invoice` | before | INSERT/UPDATE | No.Autorizacion Factura debe ser numérico.; No.Autorizacion Factura debe tener 10 o 37 o 49 digitos. | `model/triggers/SSWH_AUTORIZATION_TRG.xml` |
| `SSWH_DIVIDENS_YEAR_TRG` | `c_invoice` | after | INSERT/UPDATE | El campo Año declaración de dividendo no debe estar vacío cuando el tipo de documento es dividendo. | `model/triggers/SSWH_DIVIDENDS_YEAR.xml` |
| `SSWH_GRANDTOTAL_VAL_TRG` | `c_invoice` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_GRANDTOTAL_VAL_TRG.xml` |
| `SSWH_INVOICEAUTHORIZATION_TRG1` | `c_invoice` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_INVOICEAUTHORIZATION_TRG1.xml` |
| `SSWH_INVOICEAUTHORIZATION_TRG2` | `c_invoice` | after | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_INVOICEAUTHORIZATION_TRG2.xml` |
| `SSWH_INVOICEAUTHORIZATION_TRG3` | `c_invoice` | before | INSERT/UPDATE | v_establecimiento := substr(v_reference, 1, 3);; v_NoFactura := TO_NUMBER(substr(v_reference, 9, 9));; /* Select authorization by document type, the invoice 'date' must be between authorization 'date from' and 'date to'… | `model/triggers/SSWH_INVOICEAUTHORIZATION_TRG3.xml` |
| `SSWH_INVOICE_TRG1` | `c_invoice` | after | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_INVOICE_TRG1.xml` |
| `SSWH_INVOICE_TRG2` | `c_invoice` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_INVOICE_TRG2.xml` |
| `SSWH_T_INVOICE_REFNUMBER` | `c_invoice` | before | INSERT/UPDATE | Select authorization by business partner, the invoice 'date' must be between authorization 'date from' and 'date to'. | `model/triggers/SSWH_T_INVOICE_REFNUMBER.xml` |
| `SSWH_VALIDATEDATE_TRG` | `c_invoice` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SSWH_VALIDATEDATE_TRG.xml` |
| `SSWH_INVOICELINE_TRG` | `c_invoiceline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_INVOICELINE_TRG.xml` |
| `SSWH_INVOICELINE_TRG2` | `c_invoiceline` | after | UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_INVOICELINE_TRG2.xml` |
| `SSWH_INVOICETAX_TRG` | `c_invoicetax` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_INVOICETAX_TRG.xml` |
| `SSWH_EXCLUDE_CODE_TRG` | `c_tax` | before | UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_EXCLUDE_CODE_TRG.xml` |
| `SSWH_TAX_TRG` | `c_tax` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_TAX_TRG.xml` |
| `SSWH_CHECKBOOK_TR` | `sswh_checkbook` | after | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_CHECKBOOK_TR.xml` |
| `SSWH_CHECKBOOK_TR1` | `sswh_checkbook` | after | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_CHECKBOOK_TR1.xml` |
| `SSWH_CHECKBOOKPOSLINE_TR` | `sswh_checkbookposline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_CHECKBOOKPOSLINE_TR.xml` |
| `SSWH_CHECKBOOKPOSLINE_TR1` | `sswh_checkbookposline` | after | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_CHECKBOOKPOSLINE_TR1.xml` |
| `SSWH_FORMULARY_TRG` | `sswh_formulary` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_FORMULARY_TRG.xml` |
| `SSWH_FORMULARYLINE_TRG` | `sswh_formularyline` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_FORMULARYLINE_TRG.xml` |
| `SSWH_RECEIPT_TRG` | `sswh_receipt` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_RECEIPT_TRG.xml` |
| `SSWH_RECEIPT_TAX_TRG` | `sswh_receipt_tax` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_RECEIPT_TAX_TRG.xml` |
| `SSWH_WITHH_CARD_TRG` | `sswh_withh_card_credit` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_WITHH_CARD_TRG.xml` |
| `SSWH_VALIDATEAUTHORIZATION_TRG` | `sswh_withholding_vendor` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SSWH_VALIDATEAUTHORIZATION_TRG.xml` |
| `SSWH_WITHH_AUTHORIZATIONNO_TRG` | `sswh_withholdings_voided` | before | INSERT/UPDATE | El número de autorización debe ser de 10 o 37 dígitos | `model/triggers/SSWH_WITHH_AUTHORIZATIONNO_TRG.xml` |
| `SSWH_WITHH_STATE_VOIDED_TRG` | `sswh_withholdings_voided` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWH_WITHH_STATE_VOIDED_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sswh_allocatedcheck` | Asignar Cheque | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Barre Las lineas buscando sino existe el tercero y lo actualiza por el tercero del efecto.; Reco… | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Barre Las lineas buscando sino existe el tercero y lo actualiza por el tercero del efecto.; Recorre los Terceros de las lineas del extracto; raise exception '%', Cur_PartnerAsc.line ||'-'||Cur_PartnerAsc.em_sswh_partner_id;; raise exception '%', Cur_PartnerAsc.line ||'-'||Cur_PartnerAsc.em_sswh_partner_id||'-'||v_Partner_ID||'-'||v_Bankstatement_ID; | `model/functions/SSWH_ALLOCATEDCHECK.xml` |
| `sswh_asterisk` | — | RAISE NOTICE '%','CANTIDA DE CARACTERS ES: ' || cantidad; | RAISE NOTICE '%','CANTIDA DE CARACTERS ES:   ' || cantidad; | `model/functions/SSWH_ASTERISK.xml` |
| `sswh_c_bp_group_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_BP_GROUP_GET.xml` |
| `sswh_c_bpartner_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_BPARTNER_GET.xml` |
| `sswh_c_country_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_COUNTRY_GET.xml` |
| `sswh_c_currency_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_CURRENCY_GET.xml` |
| `sswh_c_greeting_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_GREETING_GET.xml` |
| `sswh_c_invoice_post_complete` | — | Completa la etapa del flujo; valida tareas/documentos y actualiza la operación de crédito. | — | `model/functions/SSWH_C_INVOICE_POST_COMPLETE.xml` |
| `sswh_c_invoice_post_completepo` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_INVOICE_POST_COMPLETEPO.xml` |
| `sswh_c_location_get` | — | c_region_id = sswh_c_region_get(region) AND | c_region_id = sswh_c_region_get(region) AND | `model/functions/SSWH_C_LOCATION_GET.xml` |
| `sswh_c_region_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_REGION_GET.xml` |
| `sswh_c_taxcategory_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_TAXCATEGORY_GET.xml` |
| `sswh_c_uom_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_UOM_GET.xml` |
| `sswh_c_validcombination_create` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_VALIDCOMBINATION_CREATE.xml` |
| `sswh_c_validcombination_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_VALIDCOMBINATION_GET.xml` |
| `sswh_c_withholding_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_C_WITHHOLDING_GET.xml` |
| `sswh_calculate_costing_ldm` | Calcular Costo LDM | INSERT INTO SSWH_AMOUNTLDM VALUES (OPERACION_PRODUCTO); ----TO FIX; SUMARIZADO DE PROMEDIO DE PRODUCTOS MATERIA PRIMA; RESULTADO COSTO PROMEDIO DEL PRODUCTO FABRICADO | INSERT INTO SSWH_AMOUNTLDM  VALUES (OPERACION_PRODUCTO); ----TO FIX; SUMARIZADO DE PROMEDIO DE PRODUCTOS MATERIA PRIMA; RESULTADO COSTO PROMEDIO DEL PRODUCTO FABRICADO | `model/functions/SSWH_CALCULATE_COSTING_LDM.xml` |
| `sswh_calculate_taxamt` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_CALCULATE_TAXAMT.xml` |
| `sswh_column_applied` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_COLUMN_APPLIED.xml` |
| `sswh_column_costcenter` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_COLUMN_COSTCENTER.xml` |
| `sswh_column_grandtotal` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_COLUMN_GRANDTOTAL.xml` |
| `sswh_convert_numbertoletters` | — | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas… | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas = ' || v_armar_texto_d;; RAISE NOTICE '%','RESULT v_tnumero >= 101 and v_tnumero <200 v_number_test = ' || to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_tnumero >= 101 and v_tnumero <200 v_number_test = ' || vTexto ; | `model/functions/SSWH_CONVERT_NUMBERTOLETTERS.xml` |
| `sswh_deallocatedcheck` | De-Asignar Cheque | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Obtengo el numero de cheque por cada tercero; Actualizo el linecheck de cada los terceros - deja… | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Obtengo el numero de cheque por cada tercero; Actualizo el linecheck de cada los terceros - dejandolo vacios - elimnio el nro de cheque; Actualizo el estado del cheque Ocupado - Disponible | `model/functions/SSWH_DEALLOCATEDCHECK.xml` |
| `sswh_document_ei` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_DOCUMENT_EI.xml` |
| `sswh_execute_ats_sql` | — | Para generar el ATS semestral seleccione el Año | Para generar el ATS semestral seleccione el Año | `model/functions/SSWH_EXECUTE_ATS_SQL.xml` |
| `sswh_formulary_process` | Proceso Formulario | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Actualizar Tabla Auxiliar Campo Padre - Total; Actualizar Tab… | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Actualizar Tabla Auxiliar Campo Padre - Total; Actualizar Tabla Auxiliar Campo Hijo - Total; Inserta todas las lineas de la tabla temporal a la tabla formulary lines.; Recorre la lista de la vista sswh_salesdet_f104_v - Datos del Formulario 104 | `model/functions/SSWH_FORMULARY_PROCESS.xml` |
| `sswh_generate_check` | Generar Cheque | insert into temp values(v_Record_ID,v_Client_ID);; v_resultado :='nlinea :' || v_NextNo || 'nroche :' || v_nrocheck || 'ultline :' || n_linecheck ;; v_Message := v_Message || 'Datos = ' || v_resultado; | insert into temp values(v_Record_ID,v_Client_ID);; v_resultado :='nlinea :' || v_NextNo || 'nroche :' || v_nrocheck || 'ultline :' || n_linecheck ;; v_Message := v_Message || 'Datos = ' || v_resultado; | `model/functions/SSWH_GENERATE_CHECK.xml` |
| `sswh_generate_status` | Generar Estado | insert into temp values(v_Record_ID,'aromero');; v_Message := v_Message || 'Datos = ' || v_resultado; | insert into temp values(v_Record_ID,'aromero');; v_Message := v_Message || 'Datos = ' || v_resultado; | `model/functions/SSWH_GENERATE_STATUS.xml` |
| `sswh_get_amount_form` | — | RAISE notice '%', '@FormulaSyntaxError@'; --OBTG:-20000--*/ | RAISE notice '%', '@FormulaSyntaxError@'; --OBTG:-20000--*/ | `model/functions/SSWH_GET_AMOUNT_FORM.xml` |
| `sswh_get_conversion_unidades` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_GET_CONVERSION_UNIDADES.xml` |
| `sswh_get_datos_org` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_GET_DATOS_ORG.xml` |
| `sswh_get_datos_producto` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_GET_DATOS_PRODUCTO.xml` |
| `sswh_get_descriptiontax` | — | v_SqlResult:= 'select coalesce((' || v_SqlResult || '),'''|| '-' || '''' || ') from dual' ; | v_SqlResult:= 'select coalesce((' || v_SqlResult ||  '),'''|| '-' || '''' || ') from dual' ; | `model/functions/SSWH_GET_DESCRIPTIONTAX.xml` |
| `sswh_get_nombre_unidad_minima` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_GET_NOMBRE_UNIDAD_MINIMA.xml` |
| `sswh_get_numatuh` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_GET_NUMATUH.xml` |
| `sswh_get_paymentnumber` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_GET_PAYMENTNUMBER.xml` |
| `sswh_get_suma_digito` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_GET_SUMA_DIGITO.xml` |
| `sswh_inout_post_posob` | — | PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL) ;; Check the header belongs to a organization where transactions are posible and ready to use; Check the period control is opened (only if it is legal e… | PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL) ;; Check the header belongs to a organization where transactions are posible and ready to use; Check the period control is opened (only if it is legal entity with accounting); Update OrderLine (if C-, Qty is negative); IF (ABS(Cur_SLines.MovementQty) > ABS(Cur_SLines.QtyOrdered)) THEN; IF (ABS(Cur_ILines.MovementQty) > ABS(Cur_ILines.QtyInvoiced)) THEN | `model/functions/SSWH_INOUT_POST_POSOB.xml` |
| `sswh_invoice_post_posob` | — | PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL) ;; Allow to complete an invoice only in these cases:; Now, needs to go to END_PROCESSING to unlock; This Commit must remanin due differences between PL… | PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL) ;; Allow to complete an invoice only in these cases:; Now, needs to go to END_PROCESSING to unlock; This Commit must remanin due differences between PL execution in Oracle and Postgres; Copy Invoice with reverese Quantities (or Amounts); Delete C_Invoice_Discounts inserted by the trigger | `model/functions/SSWH_INVOICE_POST_POSOB.xml` |
| `sswh_invoicetax_insert` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_INVOICETAX_INSERT.xml` |
| `sswh_m_discountschema_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_DISCOUNTSCHEMA_GET.xml` |
| `sswh_m_get_product_price` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_GET_PRODUCT_PRICE.xml` |
| `sswh_m_inventory_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_INVENTORY_GET.xml` |
| `sswh_m_inventory_linenext` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_INVENTORY_LINENEXT.xml` |
| `sswh_m_locator_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_LOCATOR_GET.xml` |
| `sswh_m_pricelist_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_PRICELIST_GET.xml` |
| `sswh_m_pricelist_version_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_PRICELIST_VERSION_GET.xml` |
| `sswh_m_product_category_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_PRODUCT_CATEGORY_GET.xml` |
| `sswh_m_product_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_PRODUCT_GET.xml` |
| `sswh_m_product_gett` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_PRODUCT_GETT.xml` |
| `sswh_m_product_id_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_PRODUCT_ID_GET.xml` |
| `sswh_m_productprice_create` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_PRODUCTPRICE_CREATE.xml` |
| `sswh_m_warehouse_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_M_WAREHOUSE_GET.xml` |
| `sswh_movement_post_batch` | — | Start Processing ------------------------------------------------------; Check the header belongs to a organization where transactions are posible and ready to use; Check the period control is opened (only if it is lega… | Start Processing ------------------------------------------------------; Check the header belongs to a organization where transactions are posible and ready to use; Check the period control is opened (only if it is legal entity with accounting); End Processing -------------------------------------------------------- | `model/functions/SSWH_MOVEMENT_POST_BATCH.xml` |
| `sswh_nombre_producto` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_NOMBRE_PRODUCTO.xml` |
| `sswh_order_post1__posob` | — | PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL) ;; Get the name of the org of the Order. Added by P.Sarobe; Verify not managed debtPayments added by ALO; Cancel existing Deli very + Invoice Documents | PERFORM AD_UPDATE_PINSTANCE(p_PInstance_ID, NULL, 'Y', NULL, NULL) ;; Get the name of the org of the Order. Added by P.Sarobe; Verify not managed debtPayments added by ALO; Cancel existing Deli very + Invoice Documents; Target Level = 0 if DirectShip='Y' or Binding='N'; ADDED BY P.SAROBE but to be deprecated 26052007 | `model/functions/SSWH_ORDER_POST1__POSOB.xml` |
| `sswh_payterm_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_PAYTERM_GET.xml` |
| `sswh_process_receipt` | Procesar Comprobante de Retención | v_Client_ID := Cur_Parameter.AD_Client_ID;; NULL, 'RDNC', 'Y', 'N', 'N', --triger no permite insertar un registro procesado (processed); raise exception '%','before insert payment schedule '||' v_Client_ID '||v_Client_I… | v_Client_ID := Cur_Parameter.AD_Client_ID;; NULL, 'RDNC', 'Y', 'N', 'N', --triger no permite insertar un registro procesado (processed); raise exception '%','before insert payment schedule '||' v_Client_ID '||v_Client_ID || ' v_Org_ID '||v_Org_ID|| ' v_User_ID '|| v_User_ID; ||' v_invoice_id '||v_invoice_id|| ' v_datedoc '||v_datedoc||' v_fin_paymentmethod_id '|| v_fin_paymentmethod_id; ||' v_currency_id '|| v_currency_id ||' v_taxamt '|| v_taxamt ||' v_documentno '|| v_documentno;; ((select grandtotal from c_invoice where c_invoice_id = cur_receipt.c_invoice_id)-cur_receipt.taxamt), | `model/functions/SSWH_PROCESS_RECEIPT.xml` |
| `sswh_process_salesticket` | Procesar Tickets | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_PROCESS_SALESTICKET.xml` |
| `sswh_process_wthh_card` | Proceso Tarjeta de Retención | la transacción se encuentra contabilizada y que debe ser descontabilizada previamente para permitir su anulación | la transacción se encuentra contabilizada y que debe ser descontabilizada previamente para permitir su anulación | `model/functions/SSWH_PROCESS_WTHH_CARD.xml` |
| `sswh_processed_check` | Cheque Procesado | v_Message := v_Message || 'Datos = ' || v_resultado; | v_Message := v_Message || 'Datos = ' || v_resultado; | `model/functions/SSWH_PROCESSED_CHECK.xml` |
| `sswh_ret_bp_group_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_RET_BP_GROUP_GET.xml` |
| `sswh_ret_product_category_get` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_RET_PRODUCT_CATEGORY_GET.xml` |
| `sswh_substr_formula` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_SUBSTR_FORMULA.xml` |
| `sswh_taxidvalidate` | — | Validación reutilizable de campos. | — | `model/functions/SSWH_TAXIDVALIDATE.xml` |
| `sswh_unprocess_form` | Desprocesar | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSWH_UNPROCESS_FORM.xml` |
| `sswh_validate_taxes` | — | Validación reutilizable de campos. | — | `model/functions/SSWH_VALIDATE_TAXES.xml` |
| `sswh_voidvalidate` | — | Validación reutilizable de campos. | — | `model/functions/SSWH_VOIDVALIDATE.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Asignar Cheque | `SSWH_AllocatedCheck` | Botón (PL/pgSQL) | PL `SSWH_Allocatedcheck` | N | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Barre Las lineas buscando sino existe el tercero y lo act |
| 2 | Calcular Costo LDM | `Calculate Costing LDM` | Botón (PL/pgSQL) | PL `sswh_calculate_costing_ldm` | N | INSERT INTO SSWH_AMOUNTLDM VALUES (OPERACION_PRODUCTO); ----TO FIX; SUMARIZADO DE PROMEDIO DE PRODUCTOS MATERIA PRIMA; RESULTADO COSTO PROMEDIO DEL PRODUCTO FABRICADO |
| 3 | Cheque Procesado | `processed_check` | Botón (PL/pgSQL) | PL `sswh_processed_check` | N | v_Message := v_Message || 'Datos = ' || v_resultado; |
| 4 | De-Asignar Cheque | `SSWH_Deallocatedcheck` | Botón (PL/pgSQL) | PL `sswh_deallocatedcheck` | N | CAPTURA DE LOS PARAMETROS DE CLIENTES, ORGANIZACION Y USUARIOS ACTUALES -----; Recogo el ID de la chequere de la cabecera; Obtengo el numero de cheque por cada tercero; Actualizo e |
| 5 | Declaración de retención IVA de compra | `Purchase Withholding VAT Declaration` | Botón (PL/pgSQL) | PL `RptC_PurchaseWithholding.jrxml` | N | Purchase Withholding VAT Declaration |
| 6 | Desprocesar | `Sswh_Unprocess` | Botón (PL/pgSQL) | PL `sswh_unprocess_form` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 7 | Detalle de Compras | `Purchase Detail` | Botón (PL/pgSQL) | PL `RptC_PurchaseDetail.jrxml` | N | — |
| 8 | Detalle de Retención Renta en Compras | `Withholding Incometax Declaration` | Botón (PL/pgSQL) | PL `RptC_IncometaxDet.jrxml` | N | — |
| 9 | Estado CxC - Detallado | `Summary Accounts Receivable` | Botón (PL/pgSQL) | PL `Rpt_SumaryAcountRecCons.jrxml` | N | — |
| 10 | Estado CxC - Histórico de cancelaciones | `Detail Accounts Receivable` | Botón (PL/pgSQL) | PL `Rpt_DetailAcountReceivab.jrxml` | N | — |
| 11 | Estado de Cuenta por Pagar Detallado por Centro de Costos | `Detail Accounts Payable by Cost Center` | Botón (PL/pgSQL) | PL `RptC_DetailAcountPayableByCC` | N | Detail Accounts Payable by Cost Center |
| 12 | Estado de CxP - Detallado | `Summary Accounts Payable` | Botón (PL/pgSQL) | PL `Rptc_SumaryAcountPayCons.jrxml` | N | — |
| 13 | Estado de CxP - Historico de Cancelaciones | `Detail Accounts Payable` | Botón (PL/pgSQL) | PL `RptC_DetailAcountPayable.jrxml` | N | — |
| 14 | Estado de CxP - Resumido | `Summary Accounts Payable Total` | Botón (PL/pgSQL) | PL `Rptc_TotalAcountPayCons.jrxml` | N | — |
| 15 | Formas de Cobro | `Payment In Methods` | Botón (PL/pgSQL) | PL `Rptc_PaymentinMethods.jrxml` | N | Report by Payment In Methods |
| 16 | Formas de Pago | `Payment Out Methods` | Botón (PL/pgSQL) | PL `Rptc_PaymentoutMethods.jrxml` | N | Report by Payment Out Methods |
| 17 | Formas de Pago en Compras | `Purchase Form Payment` | Botón (PL/pgSQL) | PL `RptC_PurchaseFormpayment.jrxml` | N | — |
| 18 | Generar ATS | `Generate ATS` | Botón (PL/pgSQL) | PL `sswh_get_ats_ob` | N | Generate ATS for withholding Source and IVA |
| 19 | Generar Cheque | `Generate_Check` | Botón (PL/pgSQL) | PL `sswh_Generate_Check` | N | insert into temp values(v_Record_ID,v_Client_ID);; v_resultado :='nlinea :' || v_NextNo || 'nroche :' || v_nrocheck || 'ultline :' || n_linecheck ;; v_Message := v_Message || 'Dato |
| 20 | Generar Estado | `Generate Status Line Withholding` | Botón (PL/pgSQL) | PL `sswh_generate_line_with` | N | — |
| 21 | Generar Estado | `Generate_Status` | Botón (PL/pgSQL) | PL `sswh_Generate_Status` | N | insert into temp values(v_Record_ID,'aromero');; v_Message := v_Message || 'Datos = ' || v_resultado; |
| 22 | Generar Retenciones | `Generate Withholding` | Botón (PL/pgSQL) | PL `sswh_generate_whithholding` | N | — |
| 23 | Iva Compras - Por Tercero y Factura | `Purchase VAT Declaration` | Botón (PL/pgSQL) | PL `RptC_Purchase_iva.jrxml` | N | — |
| 24 | Iva Ventas - Por cliente | `Sales VAT Declaration` | Botón (PL/pgSQL) | PL `RptC_Sales.jrxml` | N | — |
| 25 | Iva Ventas - Por cliente y Factura | `Sales VAT Declaration Detail` | Botón (PL/pgSQL) | PL `RptC_SalesDet.jrxml` | N | — |
| 26 | Procesar Comprobante de Retención | `sswh_process_withholding_receipt` | Botón (PL/pgSQL) | PL `sswh_process_receipt` | N | v_Client_ID := Cur_Parameter.AD_Client_ID;; NULL, 'RDNC', 'Y', 'N', 'N', --triger no permite insertar un registro procesado (processed); raise exception '%','before insert payment  |
| 27 | Procesar Tickets | `SalesTickets` | Botón (PL/pgSQL) | PL `sswh_process_salesticket` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 28 | Proceso Formulario | `ProcessFormulary` | Botón (PL/pgSQL) | PL `sswh_formulary_process` | N | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Actualizar Tabla Auxil |
| 29 | Proceso Tarjeta de Retención | `Process Withholding Card` | Botón (PL/pgSQL) | PL `sswh_process_wthh_card` | N | la transacción se encuentra contabilizada y que debe ser descontabilizada previamente para permitir su anulación |
| 30 | Reporte Balance por Pagar | `Report Balance Payable` | Botón (PL/pgSQL) | PL `Rptc_BalancePayable.jrxml` | N | — |
| 31 | Resumen de impuesto sobre la renta | `Summary Purchase Income Tax` | Botón (PL/pgSQL) | PL `RptC_PurchaseIncometax.jrxml` | N | — |
| 32 | Resumen de Retenciones | `Summary Withholding` | Botón (PL/pgSQL) | PL `RptC_SummaryWithholding.jrxml` | N | — |
| 33 | Retenciones en Compras | `Withholding Purchases` | Botón (PL/pgSQL) | PL `RptC_PurchaseWitholdingA.jrxml` | N | — |
| 34 | Ventas Anuladas | `Sales Voided` | Botón (PL/pgSQL) | PL `RptC_SalesVoided.jrxml` | N | — |
| 35 | Ventas de Clientes | `Sales Customer` | Botón (PL/pgSQL) | PL `RptC_SalesAts.jrxml` | N | — |
| 36 | Ventas por Establecimiento | `Sales by Stablishment` | Botón (PL/pgSQL) | PL `RptC_SalesbyStablishment.jrxml` | N | — |
| 37 | Archivo de Transferencia proveedor TXT | `Archive Provider Transfer TXT` | Informe (servlet) | Java `ArchProviderTransferTXT` | N | Proceso Openbravo registro `cDoctypeId` |
| 38 | Crear xml - ATS | `Create xml - ATS` | Informe (servlet) | Java `Create_xml` | N | Proceso Openbravo registro `cPeriodId`, Tipo ATS - Mensual. Seleccione el período para continuar.; Tipo ATS - Semestral. Seleccione el Año para continuar.; El campo Organización es |
| 39 | Proceso Retenciones anuladas | `Sswh_Processed_Withhldings_Voided` | Informe (servlet) | Java `Sswh_ProcessWithholdingVoided` | N | Proceso Openbravo registro `Sswh_Withholdings_Voided_ID` |
| 40 | Impresión Genérica de Formulario | `GENERIC - PRINT FORMULARY` | Reporte | Java `Sswh_GenericPrintFormulary` | S | Genera PDF desde JRXML `—`; contexto sesión `0AA43DE6B4AF41D08058F2407CA11C0D|SSWH_FORMULARY_ID`. |
| 41 | Withholding Statement | `PRINTWHSTATEMENT` | Reporte | Java `RptWithholdingStatement` | S | Genera PDF desde JRXML `com/sidesoft/localization/ecuador/withholdings/reports/RptWithholdingStatement.jrxml`; contexto sesión `—`. |

**Total acciones documentadas (extract):** **41** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `com.sidesoft.localization.ecuador.withholdings`.

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

# Glosario — prefijo `SSWH`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSWH` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.localization.ecuador.withholdings` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Sswh - Payment Monitor` — Payment Monitor(New)
- `SSWH_AllocatedCheck` — Asignar Cheque
- `Calculate Costing LDM` — Calcular Costo LDM
- `processed_check` — Cheque Procesado
- `SSWH_Deallocatedcheck` — De-Asignar Cheque
- `Purchase Withholding VAT Declaration` — Declaración de retención IVA de compra
- `Sswh_Unprocess` — Desprocesar
- `Purchase Detail` — Detalle de Compras
- `Withholding Incometax Declaration` — Detalle de Retención Renta en Compras
- `Summary Accounts Receivable` — Estado CxC - Detallado
- `Detail Accounts Receivable` — Estado CxC - Histórico de cancelaciones
- `Detail Accounts Payable by Cost Center` — Estado de Cuenta por Pagar Detallado por Centro de Costos
- `Summary Accounts Payable` — Estado de CxP - Detallado
- `Detail Accounts Payable` — Estado de CxP - Historico de Cancelaciones
- `Summary Accounts Payable Total` — Estado de CxP - Resumido

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Datasets ATS - Purchases and sales withholdings
**Package:** `com.sidesoft.localization.ecuador.withholdings.dataset`

# Module overview — Datasets ATS - Purchases and sales withholdings

## Functional

El módulo 'Datasets ATS - Purchases and sales withholdings' está diseñado para gestionar las retenciones de compras y ventas en Ecuador, facilitando el cumplimiento de las normativas fiscales del país. Los actores principales incluyen los usuarios de negocio encargados de la contabilidad y la administración fiscal, así como los desarrolladores y el soporte técnico que ofrecen ayuda y mantenimiento. Este módulo depende de la localización de Ecuador en cuanto a las retenciones, lo que implica que su funcionalidad está alineada con las regulaciones del país.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/localization/ecuador/withholdings/dataset` |
| Web | `web/com.sidesoft.localization.ecuador.withholdings.dataset/` |

### Declared dependencies

- Localization of Ecuador - Withholdings

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

*(sin prefijo en AD_MODULE_DBPREFIX)*

# Guía de chat — Datasets ATS - Purchases and sales withholdings

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.localization.ecuador.withholdings.dataset`).

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

- ¿Cómo puedo generar un reporte de retenciones?
- ¿Dónde se configura la información de mis proveedores para las retenciones?
- ¿Qué pasos debo seguir para validar la información antes de enviarla a la autoridad fiscal?
- ¿Cómo puedo asegurarme de que los cálculos de retenciones son correctos?
- ¿Hay algún proceso automatizado para registrar mis retenciones mensuales?
- ¿Cómo afecta la normativa fiscal actual a mis retenciones en el sistema?
- ¿Cómo puedo acceder a la configuración de las retenciones en el sistema?
- ¿Qué debo hacer si encuentro errores en mis datos fiscales?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la gestión de la información relacionada con retenciones. Aunque no hay tablas físicas definidas en el inventario, el flujo de datos probablemente involucra etapas que permiten capturar, procesar y reportar estas retenciones a las autoridades fiscales. Es probable que existan relaciones entre datos de compras y ventas para consolidar la información necesaria para el reporte. Aunque no hay triggers o funciones PL especificadas, el módulo puede incluir procesos automatizados para verificar datos y asegurar la integridad de la información.

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

El módulo parece carecer de ventanas y campos definidos en la interfaz de usuario, lo que sugiere que los usuarios pueden interactuar con él a través de funciones automatizadas o reportes generados. Sin embargo, los usuarios deben buscar otros módulos complementarios o utilizar interfaces específicas para gestionar las transacciones fiscales.

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

Dado que no se detallan botones o procesos específicos, se puede asumir que el flujo de trabajo es bastante automatizado. Los usuarios pueden esperar informes relacionados con las retenciones que deben ser validados. Las validaciones comunes pueden incluir verificación de datos fiscales y confirmación de formularios requeridos por las autoridades. La ausencia de acciones específicas sugiere que el enfoque está en la integración y automatización de procesos, más que en intervenciones manuales frecuentes.

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

El módulo no incluye clases Java, lo que indica que su funcionalidad está totalmente diseñada a través de la configuración del ERP sin necesidad de programación adicional.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.localization.ecuador.withholdings.dataset`.

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

El rol de triggers y funciones PL es esencial para el soporte del módulo. Aunque no se especifican triggers o funciones, estos podrían ser utilizados para mantener la coherencia de los datos y asegurar que las retenciones se calculen y registren adecuadamente a medida que las transacciones se procesan en el sistema.

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

Módulo: `com.sidesoft.localization.ecuador.withholdings.dataset`.

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

# Glosario — prefijo `DATASET`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `DATASET` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.localization.ecuador.withholdings.dataset` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Withholdings Of Paid Invoices
**Package:** `com.sidesoft.localization.ecuador.withholdings.paidinvoices`

# Module overview — Withholdings Of Paid Invoices

## Functional

El módulo 'Withholdings Of Paid Invoices' tiene como propósito gestionar y facilitar el proceso de creación de reportes relacionados con las retenciones de facturas pagadas. Los principales actores involucrados son los usuarios de negocio que se encargan de la gestión contable y administrativa, así como el personal de soporte técnico que brinda asistencia en el uso del módulo. Este módulo se integra dentro del sistema Openbravo y depende de la compatibilidad con la '2.50 to 3.00 Compatibility Skin'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/localization/ecuador/withholdings/paidinvoices` |
| Web | `web/com.sidesoft.localization.ecuador.withholdings.paidinvoices/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SWHPI`

# Guía de chat — Withholdings Of Paid Invoices

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.localization.ecuador.withholdings.paidinvoices`).

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

- ¿Cómo puedo generar un reporte de retenciones de facturas pagadas?
- ¿Qué información necesito ingresar para las retenciones?
- ¿Qué cambios se han realizado en la tabla de pagos?
- ¿Cómo se accede al módulo de retenciones desde el menú?
- ¿Qué validaciones se aplican al registrar una retención?
- ¿Qué debo hacer si encuentro un error al generar un reporte?
- ¿Dónde se almacenan los datos de las retenciones?
- ¿Hay alguna guía para entender las nuevas funcionalidades del módulo?

# Domain — data model

## Functional

La entidad cabecera de este módulo es la tabla 'FIN_PAYMENT', que ha sido modificada para incluir nuevos campos dedicados a la gestión de retenciones. Aunque no hay etapas definidas o triggers presentados en el inventario, se pueden inferir interacciones relacionadas con el registro y la consulta de datos de pagos y sus retenciones correspondientes. La relación entre los datos de los pagos y las retenciones permite un análisis efectivo de las transacciones que requieren este tipo de deducción fiscal.

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

Dado que no se especifican ventanas en la documentación del módulo, la interacción de los usuarios se realiza mediante un menú único que da acceso a las funcionalidades del módulo, principalmente relacionadas con el reporte y gestión de retenciones. Los usuarios pueden navegar a través de este menú para acceder a las herramientas necesarias para crear y gestionar los registros de retenciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.localization.ecuador.withholdings.paidinvoices.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Retenciones de facturas pagadas | Withholdings Of Paid Invoices | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.localization.ecuador.withholdings.paidinvoices.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `C4B6506838E14A349D6717D6856F1B56`

- **AD_TAB_ID:** `C4B6506838E14A349D6717D6856F1B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 102 | Withholdings Of Paid Invoices | `EM_Swhpi_Withretention` | No | No | — |
| 103 | Num. Retention | `EM_Swhpi_Withholdingsale_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo cuenta con un proceso clave que permite la creación de reportes específicos sobre las retenciones aplicadas a las facturas pagadas, lo cual es fundamental para garantizar el cumplimiento fiscal. Los botones típicos utilizados en este proceso incluyen uno para completar la acción de generación del reporte. En el contexto del módulo, las validaciones frecuentes estarían relacionadas con la correcta información de los campos añadidos en la tabla 'FIN_PAYMENT', asegurando que se cumple con la normativa legal.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.localization.ecuador.withholdings.paidinvoices.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Retenciones de facturas pagadas | Withholdings Of Paid Invoices | Withholdings Of Paid Invoices | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Retenciones de facturas pagadas | Withholdings Of Paid Invoices | Withholdings Of Paid Invoices | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Retenciones de facturas pagadas | Withholdings Of Paid Invoices | — | — | — |
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

No se dispone de clases Java en este módulo, lo que implica que su funcionalidad se limita a procesos y configuraciones a nivel de base de datos y interfaz de usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.localization.ecuador.withholdings.paidinvoices`.

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
| AD_VAL_RULE | — | `swhpi_ValidUser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `swhpi_WithholdingSale is Paidinvoice` | `SSWS_WithholdingSale.Paidinvoice = 'Y'  AND 
(SSWS_WithholdingSale.SSWS_WithholdingSale_id NOT IN (SELECT em_swhpi_withh` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

A pesar de que el módulo no incluye triggers ni funciones PL a nivel de base de datos, la modificación en la tabla 'FIN_PAYMENT' permite una interacción directa en el soporte técnico, facilitando la identificación de posibles errores o incidencias relacionadas con los pagos y sus retenciones. Esto es crucial para mantener la integridad de los datos y la funcionalidad del sistema.

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

Módulo: `com.sidesoft.localization.ecuador.withholdings.paidinvoices`.

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

# Glosario — prefijo `SWHPI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SWHPI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.localization.ecuador.withholdings.paidinvoices` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Withholdings Of Paid Invoices` — Retenciones de facturas pagadas

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Localization of Ecuador - Reports
**Package:** `com.sidesoft.localization.ecuador.withholdings.reports`

# Module overview — Localization of Ecuador - Reports

## Functional

El módulo 'Localization of Ecuador - Reports' tiene como propósito la gestión de informes de compras y ventas en Ecuador. Los actores principales incluyen usuarios de negocio que requieran informes, así como el soporte L2 que facilita la implementación y el uso. Este módulo es esencial para garantizar el cumplimiento de las normativas fiscales locales y proporciona información crítica para la toma de decisiones en las empresas. La compatibilidad se establece con versiones de Openbravo desde 2.50 hasta 3.00 y depende de otros módulos como 'Localization of Ecuador - Withholdings'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/localization/ecuador/withholdings/reports` |
| Web | `web/com.sidesoft.localization.ecuador.withholdings.reports/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Localization of Ecuador - Withholdings

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSWHR`

# Guía de chat — Localization of Ecuador - Reports

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.localization.ecuador.withholdings.reports`).

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

- ¿Cómo puedo acceder a los informes de compras y ventas?
- ¿Qué pasos debo seguir para generar un informe?
- ¿Los informes están actualizados con la normativa fiscal actual?
- ¿Puedo personalizar los informes según mis necesidades?
- ¿Cómo soluciono un error en la generación del informe?
- ¿Quién puede ayudarme si tengo problemas con los datos en los informes?
- ¿Dónde encuentro la documentación para el uso del módulo?
- ¿El módulo es compatible con versiones anteriores de Openbravo?

# Domain — data model

## Functional

El módulo no contiene tablas físicas específicas, sino que se basa en el manejo de informes a través de un único archivo JRXML. Esto implica que la entidad principal está relacionada con la generación y el manejo de estos informes, aunque no hay etapas específicas claramente definidas en el inventario. No se han especificado triggers o funciones PL dentro del módulo, sugiriendo un enfoque simple en la creación de informes sin interdependencias complejas.

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

Actualmente, el módulo no presenta ventanas específicas en la interfaz de usuario, lo que indica que la interacción probablemente se realiza a través de menús o enlaces directos a los informes disponibles. Esto sugiere una navegación simplificada donde el acceso se limita a la generación y visualización de un único tipo de informe.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.localization.ecuador.withholdings.reports.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Estado de cuenta por pagar por  Categoría de Proveedor | Account Pay Supplier Category | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.localization.ecuador.withholdings.reports.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un único proceso que permite la generación de informes, lo que respalda a los usuarios en la visualización rápida de los datos requeridos. Todos los informes generados son accesibles desde este proceso, aunque no se ha detallado la existencia de botones típicos más allá del de completar. Las validaciones más frecuentes pueden surgir en la preparación de datos para el informe, asegurando que la información entregada cumpla con los criterios establecidos por la normativa ecuatoriana.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.localization.ecuador.withholdings.reports.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Estado de cuenta por pagar por  Categoría de Proveedor | Account Pay Supplier Category | Account Pay Supplier Category | `AccSta_CategorySupplier.jrxml` | Account payable statement by Supplier Category | — |
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
| Botón (PL/pgSQL) | Estado de cuenta por pagar por  Categoría de Proveedor | Account Pay Supplier Category | Account Pay Supplier Category | `AccSta_CategorySupplier.jrxml` | Account payable statement by Supplier Category | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Estado de cuenta por pagar por  Categoría de Proveedor | Account Pay Supplier Category | PL `AccSta_CategorySupplier.jrxml` | Account payable statement by Supplier Category | — |
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

No se identifican clases Java específicas en este módulo, lo que sugiere que su operatividad depende exclusivamente de la funcionalidad proporcionada por los componentes existentes de Openbravo y su integración en la generación de informes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.localization.ecuador.withholdings.reports`.

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

Dado que no se han identificado triggers ni funciones PL específicas dentro del módulo, su papel en el soporte es más sobre la configuración y menos sobre la manipulación de datos a nivel de base de datos. El soporte podría implicar la asistencia en la personalización de informes o ajustes menores a nivel de configuración.

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
| 1 | Estado de cuenta por pagar por  Categoría de Proveedor | `Account Pay Supplier Category` | Botón (PL/pgSQL) | PL `AccSta_CategorySupplier.jrxml` | N | Account payable statement by Supplier Category |

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

Módulo: `com.sidesoft.localization.ecuador.withholdings.reports`.

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

# Glosario — prefijo `SSWHR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSWHR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.localization.ecuador.withholdings.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Account Pay Supplier Category` — Estado de cuenta por pagar por  Categoría de Proveedor

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Customization Payment In - Withholdings Modules
**Package:** `com.sidesoft.localization.ecuador.payments.withholdings`

# Module overview — Customization Payment In - Withholdings Modules

## Functional

El módulo 'Customization Payment In - Withholdings' está diseñado para manejar el proceso de retenciones en los pagos entrantes dentro del contexto legislativo ecuatoriano. Su principal propósito es facilitar el registro y la gestión de las retenciones de impuestos en las transacciones comerciales con clientes. Los principales actores son los usuarios de negocio que gestionan las cuentas por cobrar y los administradores del sistema encargados del mantenimiento de los módulos. Este módulo se integraría en el flujo contable del ERP Openbravo, lo que representa una dependencia sobre las funcionalidades de facturación y pagos existentes en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/localization/ecuador/payments/withholdings` |
| Web | `web/com.sidesoft.localization.ecuador.payments.withholdings/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`CSLSW`

# Guía de chat — Customization Payment In - Withholdings Modules

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.localization.ecuador.payments.withholdings`).

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

- ¿Cómo registramos las retenciones en una factura de cliente?
- ¿Qué campos son obligatorios al ingresar una retención?
- ¿Dónde puedo encontrar el historial de retenciones aplicadas?
- ¿Qué tipos de retenciones admite este módulo?
- ¿Qué pasos sigo si deseo corregir una retención ingresada?
- ¿Existen informes específicos para el seguimiento de las retenciones?
- ¿Cómo se valida la correcta implementación del módulo de retenciones?
- ¿Se puede personalizar más la gestión de las retenciones en Openbravo?

# Domain — data model

## Functional

El módulo no introduce nuevas entidades o tablas en el modelo de datos, pero se integra con la entidad cabecera 'Invoice (Customer)' permitiendo añadir el campo de fecha en la pestaña de detalle de pagos. La relación principal es entre el pago y la factura correspondiente, donde se registran las deducciones fiscales aplicables. Aunque no se especifican triggers o funciones clave en la documentación, se infiere que la gestión adecuada del campo de retención puede depender de la correcta validación en la interfaz de usuario para asegurar la precisión en el registro contable.

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

No se especifican ventanas específicas para la navegación de este módulo en la interfaz de usuario de Openbravo. Sin embargo, los usuarios accederán al módulo a través del encabezado de la factura del cliente y el pago correspondiente, donde se ha integrado la funcionalidad de las retenciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.localization.ecuador.payments.withholdings.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.localization.ecuador.payments.withholdings.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `F6C2283A21314407BBBB23FF14B85ED4`

- **AD_TAB_ID:** `F6C2283A21314407BBBB23FF14B85ED4` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 235 | withholdingDate | `—` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Al tratarse de un módulo que se integra en un proceso ya existente, no se listan botones típicos asociados directamente con el módulo. Sin embargo, se espera que se utilicen los botones estándar de completar y retornar en la pantalla de detalles del pago. Las validaciones frecuentes se centrarán en la veracidad de las retenciones ingresadas, asegurando que cumplan con las normativas fiscales. Los informes relacionados podrían enfocarse en la contabilidad de las retenciones gestionadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.localization.ecuador.payments.withholdings.es_ES/referencedata/translation/`.

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

No se han definido clases Java específicas para este módulo, lo que indica una integración mínima en términos de desarrollo más allá de las configuraciones existentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.localization.ecuador.payments.withholdings`.

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

Este módulo no incorpora triggers ni funciones PL, lo que sugiere que su funcionalidad se basa principalmente en la interfaz de usuario. Sin embargo, la consistencia de los datos podría depender de las validaciones que se llevan a cabo al guardar la información sobre las retenciones en el pago, asegurando así su integridad en el contexto del ERP.

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

Módulo: `com.sidesoft.localization.ecuador.payments.withholdings`.

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

# Glosario — prefijo `CSLSW`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `CSLSW` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.localization.ecuador.payments.withholdings` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Localization of Ecuador - Withholdings Sales
**Package:** `ec.com.sidesoft.localization.ecuador.withholdingssales`

# Module overview — Localization of Ecuador - Withholdings Sales

## Functional

El módulo 'Localization of Ecuador - Withholdings Sales' se encarga de la gestión de las retenciones en las compras y ventas en Ecuador, específicamente para las transacciones gravadas con el impuesto del 22%. Los actores principales son los usuarios de negocio que gestionan las retenciones y los desarrolladores que implementan y mantienen el módulo. El alcance incluye la creación, configuración y validación de comprobantes de retención, así como la generación de informes pertinentes. Este módulo depende de otros elementos como el skin de compatibilidad de versiones y las retenciones de facturas pagadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/ecuador/withholdingssales` |
| Web | `web/ec.com.sidesoft.localization.ecuador.withholdingssales/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Withholdings Of Paid Invoices

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSWS`

# Guía de chat — Localization of Ecuador - Withholdings Sales

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.ecuador.withholdingssales`).

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
- «¿Qué es la tabla ssws_config?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo creo un nuevo comprobante de retención?
- ¿Qué información necesito para configurar las retenciones?
- ¿Puedo modificar un comprobante de retención ya creado?
- ¿Qué sucede si no selecciono un concepto contable?
- ¿Cómo se reflejan las retenciones en mis informes financieros?
- ¿Existen validaciones automáticas al crear un comprobante?
- ¿Puedo eliminar un comprobante de retención?
- ¿Cómo se integra el módulo de retenciones con mis facturas?

# Domain — data model

## Functional

La entidad cabecera clave en este módulo es 'ssws_withholdingsale', que representa un comprobante de retención, y está relacionada con otras tablas, como 'ssws_withholdingsaleline' para las líneas de retención y 'ssws_config' para la configuración general del módulo. Las operaciones incluyen validaciones a través de triggers como 'SSWS_CHCK_PAIDINVOICE_TRG', que verifica la selección de un concepto contable cuando se activa la opción de factura pagada, y 'SSWS_POSTINVOICE_TRG', que permite gestionar la lógica de negocio al momento de procesar comprobantes de retención.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssws_advance_payment` |
| `ssws_config` |
| `ssws_withholdingsale` |
| `ssws_withholdingsaleline` |
| `ssws_withholdingsalelog` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssws_advance_payment` | ssws_advance_payment | — | — | fin_financial_account_id→fin_financial_account; ad_client_id→ad_client; c_doctype_id→c_doctype; c_glitem_id→c_glitem; ad_org_id→ad_org (+2) | Detalle enlazado a ad_client, c_doctype, fin_financial_account. | PK `ssws_advance_payment_pk`; Cols: c_doctype_id, ssws_config_id, fin_paymentmethod_id, fin_financial_account_id, action_payment; `SSWS_ADVANCE_PAYMENT_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssws_config` | SSWS_Config | — | — | fin_financial_account_id→fin_financial_account; ad_client_id→ad_client; ad_org_id→ad_org; c_currency_id→c_currency; c_doctype_id→c_doctype (+1) | Parametrización / catálogo de soporte. | PK `ssws_config_key`; Cols: c_doctype_id, fin_paymentmethod_id, fin_financial_account_id, c_currency_id; `SSWS_CONFIG_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssws_withholdingsale` | SSWS_WithholdingSale | `SSWS_CHCK_PAIDINVOICE_TRG`; `SSWS_WITHHOLDIGSALE_TRG` | — | c_currency_id→c_currency; ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_doctype_id→c_doctype (+3) | Detalle enlazado a ad_client, ad_org, c_currency. Validado por trigger(s): SSWS_CHCK_PAIDINVOICE_TRG, SSWS_WITHHOLDIGSALE_TRG. | PK `ssws_withholdingsale_key`; Cols: description, withholdingdate, processing, processed, posted; `SSWS_WITHHOLDINGSALE_ADV_CHK`: GENERATE_ADVANCE_PAYMENT IN ('Y', 'N'); `SSWS_WITHHOLDINGSALE_PAIDINV`: PAIDINVOICE IN ('Y', 'N') |
| `ssws_withholdingsaleline` | SSWS_WithholdingSaleLine | `SSWS_WITHHOLDIGSALELINE_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoiceline_id→c_invoiceline; c_tax_id→c_tax; m_product_id→m_product (+1) | Detalle enlazado a ad_client, ad_org, c_invoiceline. Validado por trigger(s): SSWS_WITHHOLDIGSALELINE_TRG. | PK `ssws_withholdingsaleline_key`; Cols: description, ssws_withholdingsale_id, line, m_product_id, linenetamt |
| `ssws_withholdingsalelog` | SSWS_WithholdingSaleLog | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ssws_withholdingsale_id→ssws_withholdingsale | Detalle enlazado a ad_client, ad_org, ssws_withholdingsale. | PK `ssws_withholdingsalelog_key`; Cols: line, ssws_withholdingsale_id, logtype, description |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssws_advance_payment` |
| `SSWS_Config` |
| `SSWS_WhSaleDetail_V` |
| `SSWS_WithholdingSale` |
| `SSWS_WithholdingSaleLine` |
| `SSWS_WithholdingSaleLog` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`FIN_PAYMENT_SCHEDULEDETAIL`

### Views

`SSWS_GETTAXINCOME`, `SSWS_RECONCILIATION_V`, `SSWS_WHSALEDETAIL_V`

# Functional — windows and menus

## Functional

La navegación en el módulo se realiza a través de dos ventanas principales: 'Comprobante de Retención' y 'Configuración de Retenciones'. En la primera, los usuarios pueden crear y gestionar los comprobantes, mientras que en la segunda se configuran los parámetros requeridos para el manejo de las retenciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.ecuador.withholdingssales.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Comprobante de Retención | Withholdings Sales |
| Configuración de Retenciones | Withholdings Configuration |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Comprobante de Retención | Withholdings Sales | Sí |
| Comprobante de Retención | Withholdings Sales | No |
| Configuración | Setup | Sí |
| Configuración de Retenciones | Withholdings Configuration | No |
| Detalle de Retenciones de Ventas IVA | Sales Withholding IVA Detail | No |
| Detalle de Retenciones de Ventas Renta | Withholding Sales Detail | No |
| Diferencias de retenciones (Cabecera vs Líneas) | Withholdongs Difference(Head and Lines) | No |
| Herramientas de análisis | Analysis Tools | Sí |
| Reporte de Conciliación Mensual | Report Monthly Reconciliation | No |
| Reporte de Retenciones Recibidas por Periodo | Report of Withholdings Received by Period | No |
| Transacciones | Transactions | Sí |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.ecuador.withholdingssales.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Comprobante de Retención

- **AD_WINDOW_ID:** `C68EABB208CB4D9FB99A8ACDC66ECFA1`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Withholdings Sales | `211492B753264EAEBE328BA4FED1F066` | 0 |
| 20 | Withholdings Sales Lines | `A2A68BCBE4894B009663B0492449ACD6` | 1 |
| 30 | Accounting | `270` | 1 |
| 40 | Withholding Sale Log | `60CAE1BE0267452C87AB69E91F51DFE7` | 1 |

### Ventana: Configuración de Retenciones

- **AD_WINDOW_ID:** `049DBC91B8C645518E5323EA8DF1005F`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Withholdings Configuration | `997FEDAD98A04F469766552518DBC594` | 0 |
| 20 | Withholdings Configuration Advance Payment | `65F5FD3D6B614465A82B6C859E8EB2E0` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Withholding Detail

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Withholding Date | `Withholdingdate` | No | No | — |
| 40 | Withholding Sale | `Ssws_Withholdingsale_ID` | No | No | — |
| 50 | Amount | `Amount` | No | No | — |

### Withholding Detail

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 20 | Withholdings Sales | `EM_Ssws_Withholdingsale_ID` | No | No | — |
| 30 | Withholding Date | `EM_SSWS_WithholdingDate` | No | Sí | — |
| 70 | Withholding Amount | `EM_Ssws_Amount_New` | No | No | — |

### Withholding Sale Log (ventana: Comprobante de Retención)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Line No. | `Line` | No | No | — |
| 50 | Logtype | `Logtype` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Withholdings Configuration (ventana: Configuración de Retenciones)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 50 | Deposit To | `FIN_Financial_Account_ID` | No | No | — |
| 60 | Active | `Isactive` | No | No | — |
| 70 | Currency | `C_Currency_ID` | No | No | — |

### Withholdings Configuration Advance Payment (ventana: Configuración de Retenciones)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | DocType Advance Payment | `C_Doctype_ID` | No | No | — |
| 50 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 60 | Financial Account Advance Payment | `FIN_Financial_Account_ID` | No | No | — |
| 90 | G/L Item | `C_Glitem_ID` | No | No | — |
| 200 | Active | `Isactive` | No | No | — |

### Pestaña `7A8D43541F8C49F1BD8A431A0041BF89`

- **AD_TAB_ID:** `7A8D43541F8C49F1BD8A431A0041BF89` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 165 | Number of Withholdings | `EM_SSWS_NumberOfWithholdings` | No | Sí | — |

### Withholdings Sales (ventana: Comprobante de Retención)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 30 | Document No. | `Documentno` | No | No | — |
| 40 | Withholding Date | `WithholdingDate` | No | No | — |
| 50 | Accounting Date | `Dateacct` | No | No | — |
| 60 | Withholding Type | `WithholdingType` | No | No | — |
| 70 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 85 | Paid Invoice | `Paidinvoice` | No | No | — |
| 86 | Generate_Advance_Payment | `Generate_Advance_Payment` | No | No | — |
| 90 | Invoice | `C_Invoice_ID` | No | No | — |
| 95 | G/L Item | `C_Glitem_ID` | No | No | — |
| 100 | Total Withholding Rental Ammount | `TotalWhRentalAmt` | No | Sí | — |
| 130 | Total Withholding IVA Ammount | `TotalWhIVAAmt` | No | Sí | — |
| 140 | Currency | `C_Currency_ID` | No | Sí | — |
| 190 | Withholding Sale Process Adv | `Processed` | No | No | 114 |
| 200 | Posted | `Posted` | No | No | 114 |
| 210 | Get Invoice Lines | `Getlines` | No | No | 114 |
| 220 | Codigo | `Codigo` | No | Sí | — |
| 230 | Numauto | `Numauto` | No | No | — |
| 240 | Fechaautotext | `Fechaautotext` | No | Sí | — |
| 260 | Description | `Description` | No | No | — |
| — | Document Status | `Docstatus` | No | Sí | — |

### Withholdings Sales Lines (ventana: Comprobante de Retención)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Line No. | `Line` | No | No | — |
| 25 | Is Rental | `IsRental` | No | No | — |
| 30 | Product | `M_Product_ID` | No | Sí | — |
| 40 | Tax | `C_Tax_ID` | No | No | — |
| 50 | Line Net Amount | `LineNetAmt` | No | No | — |
| 60 | Whithholding Rental Amount | `WhRentalAmt` | No | No | — |
| 70 | Line IVA Amount | `LineIVAAmt` | No | No | — |
| 80 | Whithholding IVA Amount | `WhIVAAmt` | No | No | — |
| 90 | Description | `Description` | No | No | — |

### Accounting (ventana: Comprobante de Retención)

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

### Pestaña `F6C2283A21314407BBBB23FF14B85ED4`

- **AD_TAB_ID:** `F6C2283A21314407BBBB23FF14B85ED4` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 290 | Withholdings Sales | `EM_Ssws_Withholdingsale_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos típicos incluyen botones para completar, retornar o rechazar comprobantes, así como la validación de datos al momento de crear o editar registros. Además, se implementan funciones PL para asegurar la correcta integración con procesos contables relacionados. Aunque no hay informes específicos generados dentro del módulo, la lógica de retención se aplica de forma directa en las transacciones realizadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.ecuador.withholdingssales.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Withholding Sale Process Adv | Withholding Sale Process Adv | Withholding Sale Process Adv | Java `ProcessWithholdingSale` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssws_Withholdingsale_ID` | `src/ec/com/sidesoft/localization/ecuador/withholdingssales/ad_process/ProcessWithholdingSale.java` |
| Botón (PL/pgSQL) | Cargar líneas | Get Invoice Lines | Get_Invoice_Lines | `SSWS_GETINVOICELINES` | Zero to the fields Amount Withholdings Sales; Determine IVA tax rate according of product type | — |
| Botón (PL/pgSQL) | Withholding Sale Process | Withholding Sale Process | WHSale_Process | `SSWS_WHSALE_PROCESS` | VALIDACIÓN DEL MODULO DE CHEQUES POSFECHADOS; SE COMPRUEBA SI EL PERÍODO ESTÁ CERRADO RELACIONADO A LA LINEA DEL PERIODO POR TIPO DE DOCUMENTO BASE.; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES; CREO UN… | — |
| Proceso / otro | Detalle de Retenciones de Ventas IVA | Sales Withholding IVA Detail | Sales Withholding IVA Detail | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de Retenciones en Ventas Renta | Withholding Sales Detail | Withholding Sales Detail | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Diferencias de retenciones (Cabecera vs Líneas) | Withholdongs Difference(Head and Lines) | Withholdongs Difference(Head and Lines) | *(OBUIAPP / manual)* | Withholdongs Difference(Head and Lines) | — |
| Proceso / otro | Report Monthly Reconciliation | Report Monthly Reconciliation | Report Monthly Reconciliation | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de Retenciones Recibidas por Periodo | Report of Withholdings Received by Period | Report of Withholdings Received by Perio | *(OBUIAPP / manual)* | — | — |
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
| Botón (Java) | Withholding Sale Process Adv | `ProcessWithholdingSale` | Proceso Java (toolbar/background) | `Ssws_Withholdingsale_ID` | — | `src/ec/com/sidesoft/localization/ecuador/withholdingssales/ad_process/ProcessWithholdingSale.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Withholding Sale Process Adv | Withholding Sale Process Adv | Withholding Sale Process Adv | Java `ProcessWithholdingSale` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Ssws_Withholdingsale_ID` | `src/ec/com/sidesoft/localization/ecuador/withholdingssales/ad_process/ProcessWithholdingSale.java` |
| Botón (PL/pgSQL) | Cargar líneas | Get Invoice Lines | Get_Invoice_Lines | `SSWS_GETINVOICELINES` | Zero to the fields Amount Withholdings Sales; Determine IVA tax rate according of product type | — |
| Botón (PL/pgSQL) | Withholding Sale Process | Withholding Sale Process | WHSale_Process | `SSWS_WHSALE_PROCESS` | VALIDACIÓN DEL MODULO DE CHEQUES POSFECHADOS; SE COMPRUEBA SI EL PERÍODO ESTÁ CERRADO RELACIONADO A LA LINEA DEL PERIODO POR TIPO DE DOCUMENTO BASE.; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES; CREO UN… | — |
| Proceso / otro | Detalle de Retenciones de Ventas IVA | Sales Withholding IVA Detail | Sales Withholding IVA Detail | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle de Retenciones en Ventas Renta | Withholding Sales Detail | Withholding Sales Detail | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Diferencias de retenciones (Cabecera vs Líneas) | Withholdongs Difference(Head and Lines) | Withholdongs Difference(Head and Lines) | *(OBUIAPP / manual)* | Withholdongs Difference(Head and Lines) | — |
| Proceso / otro | Report Monthly Reconciliation | Report Monthly Reconciliation | Report Monthly Reconciliation | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de Retenciones Recibidas por Periodo | Report of Withholdings Received by Period | Report of Withholdings Received by Perio | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Withholding Sale Process Adv | Withholding Sale Process Adv | Java `ProcessWithholdingSale` | Proceso Openbravo registro `Ssws_Withholdingsale_ID` | Proceso Openbravo registro `Ssws_Withholdingsale_ID` |
| Botón (PL/pgSQL) | Cargar líneas | Get Invoice Lines | PL `SSWS_GETINVOICELINES` | Zero to the fields Amount Withholdings Sales; Determine IVA tax rate according of product type | Zero to the fields Amount Withholdings Sales; Determine IVA tax rate according of product type |
| Botón (PL/pgSQL) | Withholding Sale Process | Withholding Sale Process | PL `SSWS_WHSALE_PROCESS` | VALIDACIÓN DEL MODULO DE CHEQUES POSFECHADOS; SE COMPRUEBA SI EL PERÍODO ESTÁ CERRADO RELACIONADO A LA LINEA DEL PERIODO POR TIPO DE DOCUMENTO BASE.; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES; CREO UN… | VALIDACIÓN DEL MODULO DE CHEQUES POSFECHADOS; SE COMPRUEBA SI EL PERÍODO ESTÁ CERRADO RELACIONADO A LA LINEA DEL PERIODO POR TIPO DE DOCUMENTO BASE.; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES; CREO UN REGISTRO EN LA CABECERA DE LOS COBROS; Get corresponding FIN_PAYMENT_SCHEDULE_ID; Elimina la relacion del cobro de la retencion con el detalle de plan de pagos |
| Proceso / otro | Detalle de Retenciones de Ventas IVA | Sales Withholding IVA Detail | — | — | — |
| Proceso / otro | Detalle de Retenciones en Ventas Renta | Withholding Sales Detail | — | — | — |
| Proceso / otro | Diferencias de retenciones (Cabecera vs Líneas) | Withholdongs Difference(Head and Lines) | — | Withholdongs Difference(Head and Lines) | — |
| Proceso / otro | Report Monthly Reconciliation | Report Monthly Reconciliation | — | — | — |
| Proceso / otro | Reporte de Retenciones Recibidas por Periodo | Report of Withholdings Received by Period | — | — | — |
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
**Total de reportes del módulo: 5**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **5**.

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
| `SSWS_NotConfigWithholding` | There are no records in the Withholdings Configuration | There are no records in the Withholdings Configuration | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `ssws_config_advance_payment` | Invalid Config | Invalid Config | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWS_WithholdingSalePresent` | Can not unpost the invoice while the withholding sale is present | Can not unpost the invoice while the withholding sale is present | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssws_ErrorExistPeriod` | There is no period created for the retention date | There is no period created for the retention date | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWS_NoWithholdingAmount` | There is not withholding amount | There is not withholding amount | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `ssws_exist_advance_payment` | Exist Advance Payment | Exist Advance Payment | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWS_WithholdingConfigError` | Withholding Configuration Error | Withholding Configuration Error | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssws_ErrorPeriod` | Period | Period | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssws_ErrorWithholdingDate` | is not open for the retention date | is not open for the retention date | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSWS_InsuficientAmountForWithholding` | Insufficient pending amount to apply the withholding. Please mark check "Paid invoice". | Insufficient pending amount to apply the withholding. Please mark check "Paid invoice". | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Ssws_InvoiceNotPosted` | The related invoice must be posted. | The related invoice must be posted. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye varias clases Java que implementan la lógica de negocio, tales como 'DocLine_WithholdingSale' y 'DocWithholdingSales', que gestionan la creación y manejo de documentos relacionados con las retenciones en ventas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.ecuador.withholdingssales`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `DocLine_WithholdingSale` | accounting | DocLine | — | `src/ec/com/sidesoft/localization/ecuador/withholdingssales/accounting/DocLine_WithholdingSale.java` |
| `DocWithholdingSales` | accounting | AcctServer | — | `src/ec/com/sidesoft/localization/ecuador/withholdingssales/accounting/DocWithholdingSales.java` |
| `SS_TaxRate` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/ecuador/withholdingssales/ad_callouts/SS_TaxRate.java` |
| `ProcessWithholdingSale` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/localization/ecuador/withholdingssales/ad_process/ProcessWithholdingSale.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSWS_CHCK_PAIDINVOICE_TRG` | `ssws_withholdingsale` | before INSERT/UPDATE | Necesita escoger un concepto contable cuando está activo el check de factura pagada. |
| Trigger `SSWS_POSTINVOICE_TRG` | `c_invoice` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWS_SCHEDULEDETAIL_TRG` | `fin_payment_scheduledetail` | after INSERT | new.amount:= v_finPaymentAmount + v_SswsAmount; |
| Trigger `SSWS_WITHHOLDIGSALELINE_TRG` | `ssws_withholdingsaleline` | before INSERT/UPDATE/DELETE | If updating or deleting substract old values |
| Trigger `SSWS_WITHHOLDIGSALE_TRG` | `ssws_withholdingsale` | before UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Ssws_Valid_TaxIncome` | `C_TAX.C_TAX_ID IN (SELECT C_TAX_ID FROM ssws_gettaxincome WHERE
TAX = @IsRental@)` |
| AD_VAL_RULE | — | `Withholding Sale DocType` | `DocBaseType='SSWS_WHS'` |
| AD_VAL_RULE | — | `Invoices from Partner` | `C_Invoice.C_BPartner_ID=@C_BPartner_ID@
and C_Invoice.ad_org_id=@ad_org_id@
and
C_Invoice.Posted='Y'
and C_Invoice.IssoT` |
| AD_VAL_RULE | — | `ssws_action_payment` | `value in ('PRD','PRP')` |
| AD_VAL_RULE | — | `SSWS Logged User` | `AD_User.AD_User_ID = @#AD_User_ID@` |
| AD_VAL_RULE | — | `Logged User` | `AD_User.AD_User_ID = @#AD_User_ID@` |
| AD_VAL_RULE | — | `Validate Partner` | `(C_BPARTNER.ISCUSTOMER = (CASE WHEN @withholdingtype@='WS' THEN 'Y' ELSE NULL END) ) OR
(C_BPARTNER.ISVENDOR =  (CASE WH` |
| Función PL `ssws_getinvoicelines` | — | invocación proceso | Zero to the fields Amount Withholdings Sales; Determine IVA tax rate according of product type |
| Función PL `ssws_whsale_process` | — | invocación proceso | VALIDACIÓN DEL MODULO DE CHEQUES POSFECHADOS; SE COMPRUEBA SI EL PERÍODO ESTÁ CERRADO RELACIONADO A LA LINEA DEL PERIODO POR TIPO DE DOCUMENTO BASE.; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El rol de los triggers dentro del módulo es fundamental, ya que permiten ejecutar validaciones y ajustes automáticos al manipular datos en las tablas. Las funciones PL complementarias ayudan a ejecutar procesos específicos que no se manejan directamente en el front-end, proporcionando así un soporte más robusto.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSWS_POSTINVOICE_TRG` | `c_invoice` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWS_POSTINVOICE_TRG.xml` |
| `SSWS_SCHEDULEDETAIL_TRG` | `fin_payment_scheduledetail` | after | INSERT | new.amount:= v_finPaymentAmount + v_SswsAmount; | `model/triggers/SSWS_SCHEDULEDETAIL_TRG.xml` |
| `SSWS_CHCK_PAIDINVOICE_TRG` | `ssws_withholdingsale` | before | INSERT/UPDATE | Necesita escoger un concepto contable cuando está activo el check de factura pagada. | `model/triggers/SSWS_CHCK_PAIDINVOICE_TRG.xml` |
| `SSWS_WITHHOLDIGSALE_TRG` | `ssws_withholdingsale` | before | UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWS_WITHHOLDIGSALE_TRG.xml` |
| `SSWS_WITHHOLDIGSALELINE_TRG` | `ssws_withholdingsaleline` | before | INSERT/UPDATE/DELETE | If updating or deleting substract old values | `model/triggers/SSWS_WITHHOLDIGSALELINE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssws_getinvoicelines` | Cargar líneas | Zero to the fields Amount Withholdings Sales; Determine IVA tax rate according of product type | Zero to the fields Amount Withholdings Sales; Determine IVA tax rate according of product type | `model/functions/SSWS_GETINVOICELINES.xml` |
| `ssws_whsale_process` | Withholding Sale Process | VALIDACIÓN DEL MODULO DE CHEQUES POSFECHADOS; SE COMPRUEBA SI EL PERÍODO ESTÁ CERRADO RELACIONADO A LA LINEA DEL PERIODO POR TIPO DE DOCUMENTO BASE.; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES; CREO UN… | VALIDACIÓN DEL MODULO DE CHEQUES POSFECHADOS; SE COMPRUEBA SI EL PERÍODO ESTÁ CERRADO RELACIONADO A LA LINEA DEL PERIODO POR TIPO DE DOCUMENTO BASE.; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES; CREO UN REGISTRO EN LA CABECERA DE LOS COBROS; Get corresponding FIN_PAYMENT_SCHEDULE_ID; Elimina la relacion del cobro de la retencion con el detalle de plan de pagos | `model/functions/SSWS_WHSALE_PROCESS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Withholding Sale Process Adv | `Withholding Sale Process Adv` | Botón (Java) | Java `ProcessWithholdingSale` | N | Proceso Openbravo registro `Ssws_Withholdingsale_ID` |
| 2 | Cargar líneas | `Get_Invoice_Lines` | Botón (PL/pgSQL) | PL `SSWS_GETINVOICELINES` | N | Zero to the fields Amount Withholdings Sales; Determine IVA tax rate according of product type |
| 3 | Withholding Sale Process | `WHSale_Process` | Botón (PL/pgSQL) | PL `SSWS_WHSALE_PROCESS` | N | VALIDACIÓN DEL MODULO DE CHEQUES POSFECHADOS; SE COMPRUEBA SI EL PERÍODO ESTÁ CERRADO RELACIONADO A LA LINEA DEL PERIODO POR TIPO DE DOCUMENTO BASE.; SE BUSCAN LOS PARAMETROS DE LA |

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

Módulo: `ec.com.sidesoft.localization.ecuador.withholdingssales`.

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

# Glosario — prefijo `SSWS`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSWS` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.ecuador.withholdingssales` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Withholding Sale Process Adv` — Withholding Sale Process Adv
- `Get_Invoice_Lines` — Cargar líneas
- `WHSale_Process` — Withholding Sale Process
- `Sales Withholding IVA Detail` — Detalle de Retenciones de Ventas IVA
- `Withholding Sales Detail` — Detalle de Retenciones en Ventas Renta
- `Withholdongs Difference(Head and Lines)` — Diferencias de retenciones (Cabecera vs Líneas)
- `Report Monthly Reconciliation` — Report Monthly Reconciliation
- `Report of Withholdings Received by Perio` — Reporte de Retenciones Recibidas por Periodo

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Control Withholding
**Package:** `ec.com.sidesoft.localization.withholding.control`

# Module overview — Control Withholding

## Functional

El módulo 'Control Withholding' permite la gestión y control de las retenciones que se eliminan al guardar la información en una pestaña de la ventana de facturas de proveedor. Está diseñado para que los usuarios de negocio puedan llevar un registro eficaz de las retenciones aplicadas. Los actores principales son los contadores y administradores responsables de la contabilidad y gestión financiera. Este módulo es dependiente de varias plataformas y compatibilidades, como '2.50 to 3.00 Compatibility Skin' y 'Core', así como de la localización específica para Ecuador.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/withholding/control` |
| Web | `web/ec.com.sidesoft.localization.withholding.control/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Localization of Ecuador - Withholdings
- Openbravo 3.0 Framework

### Version

**1.1.0** (from `AD_MODULE.xml`).

### DB prefix

`ECSWC`

# Guía de chat — Control Withholding

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.withholding.control`).

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
- «¿Qué es la tabla ecswc_withholding_cancel?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo anular una retención ya registrada?
- ¿Qué información necesito para gestionar las retenciones?
- ¿Dónde encuentro la pestaña para las retenciones de las facturas de proveedor?
- ¿Qué validaciones se realizan al anular una retención?
- ¿Qué sucede si cancelo una retención incorrectamente?
- ¿Hay informes asociados a la gestión de retenciones?
- ¿Qué debo hacer si el botón de anulación no está disponible?
- ¿Cómo se refleja la anulación de retenciones en la contabilidad?

# Domain — data model

## Functional

La entidad cabecera del módulo es la tabla 'ecswc_withholding_cancel', que registra las operaciones de cancelación de retenciones. Esta tabla es clave en el flujo del proceso de gestión de retenciones, permitiendo al usuario anular o desistir de operaciones de compra. El módulo cuenta con un disparador, 'ECSWC_WITHHOLDING_CANCEL_TRG', que se activa para anular las retenciones cuando se realizan modificaciones en la tabla correspondiente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ecswc_withholding_cancel` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ecswc_withholding_cancel` | ecswc_withholding_cancel | `ECSWC_WITHHOLDING_CANCEL_TRG` | — | ad_client_id→ad_client; c_invoice_id→c_invoice; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_invoice. Validado por trigger(s): ECSWC_WITHHOLDING_CANCEL_TRG. | PK `ecswc_withholdingcancel_key`; Cols: c_invoice_id, documentno, status_doc, withholding_date, withholding_date_cancel; `ECSWC_WHCANC_INV_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ecswc_withholding_cancel` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no presenta ventanas adicionales, pero opera dentro de la pestaña de facturas de proveedor, donde los usuarios pueden gestionar las retenciones asociadas. A través de un menú, los usuarios acceden a la opción de anulaciones relacionadas con las retenciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.withholding.control.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Retenciones Anuladas | Withholdings canceled | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.withholding.control.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Withholding cancel

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 40 | documentno | `Documentno` | No | Sí | — |
| 50 | Status_Doc | `Status_Doc` | No | Sí | — |
| 60 | Withholding_Date | `Withholding_Date` | No | Sí | — |
| 70 | Withholding_Date_Cancel | `Withholding_Date_Cancel` | No | Sí | — |
| 72 | Totalwithholdingvat | `Totalwithholdingvat` | No | Sí | — |
| 74 | Totalwithholdingincome | `Totalwithholdingincome` | No | Sí | — |
| 80 | KEY_Access | `KEY_Access` | No | Sí | — |
| 90 | KEY_Access_Auth | `KEY_Access_Auth` | No | Sí | — |
| 100 | Urlxml | `Urlxml` | No | No | — |
| 110 | Urlxml_Ride | `Urlxml_Ride` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso principal del módulo se activa a través de un botón que permite al usuario anular retenciones. No se generan informes adicionales, pero se contemplan validaciones frecuentes en las operaciones para asegurar la integridad de los datos. Es fundamental que se validen las entradas asociadas a las retenciones antes de realizar acciones de anulación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.withholding.control.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Retenciones Anuladas | Withholdings canceled | Withholdings canceled | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Retenciones Anuladas | Withholdings canceled | Withholdings canceled | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Retenciones Anuladas | Withholdings canceled | — | — | — |
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
| `ecswc_delete_withholding_cancel` | No se permite eliminar registros de esta solapa | No se permite eliminar registros de esta solapa | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

No se incluyen clases Java en este módulo, por lo que el enfoque se centra en el uso de PL/SQL y triggers para manejar la lógica de la aplicación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.withholding.control`.

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
| Trigger `ECSWC_WITHHOLDING_CANCEL_TRG` | `ecswc_withholding_cancel` | before DELETE | Anula / desiste la operación de compra. |
| Función PL `ecswc_control_voidinvoice` | — | invocación proceso | INSERTAR EN LA CABECERA RETENCIONES ANULADAS |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El módulo integra un disparador para manejar la lógica de negocio necesaria en la tabla de retenciones canceladas. También incluye una función PL específica que facilita las validaciones y operaciones que aseguran la correcta gestión del proceso de anulación de retenciones en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `ECSWC_WITHHOLDING_CANCEL_TRG` | `ecswc_withholding_cancel` | before | DELETE | Anula / desiste la operación de compra. | `model/triggers/ECSWC_WITHHOLDING_CANCEL_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ecswc_control_voidinvoice` | — | INSERTAR EN LA CABECERA RETENCIONES ANULADAS | INSERTAR EN LA CABECERA RETENCIONES ANULADAS | `model/functions/ECSWC_CONTROL_VOIDINVOICE.xml` |
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

Módulo: `ec.com.sidesoft.localization.withholding.control`.

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

# Glosario — prefijo `ECSWC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `ECSWC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.withholding.control` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Withholdings canceled` — Retenciones Anuladas

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Business Partner Search Withholdings Modules
**Package:** `ec.com.sidesoft.bpartner.search.withholdings`

# Module overview — Business Partner Search Withholdings Modules

## Functional

El módulo 'Business Partner Search Withholdings' tiene como propósito facilitar la búsqueda y selección de socios comerciales en relación con las retenciones fiscales. Está dirigido principalmente a usuarios de negocio que necesiten acceder a información detallada de los socios comerciales, así como a desarrolladores y personal de soporte que requieran el acceso a herramientas y funcionalidades específicas. El alcance del módulo se limita a la ventana de 'Contribución de Retenciones', permitiendo una visualización eficiente de los datos relacionados con este tema específico. No existen dependencias adicionales conocidas para este módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/bpartner/search/withholdings` |
| Web | `web/ec.com.sidesoft.bpartner.search.withholdings/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLSBPS`

# Guía de chat — Business Partner Search Withholdings Modules

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.bpartner.search.withholdings`).

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

- ¿Cómo puedo buscar un socio comercial específico?
- ¿Cuáles son los campos disponibles para filtrar la búsqueda?
- ¿Qué debo hacer si no encuentro a un socio comercial en la lista?
- ¿Cómo se manejan las retenciones fiscales en relación con los socios comerciales?
- ¿Hay alguna funcionalidad para exportar los resultados de la búsqueda?
- ¿Qué tipos de informes puedo generar a partir de los socios comerciales seleccionados?
- ¿Puedo modificar los criterios de búsqueda después de haber realizado una consulta?
- ¿Cómo se actualiza la información de un socio comercial en el sistema?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la entidad cabecera que almacena información sobre los socios comerciales. Aunque no hay tablas físicas en el módulo, la estructura está diseñada para trabajar en conjunto con los datos existentes en Openbravo. Este módulo incluye etapas de búsqueda que permiten filtrar resultados basándose en criterios específicos, lo cual mejora la accesibilidad de la información. Aunque no hay triggers definidos en este módulo, su funcionalidad depende en gran medida de las funciones Java disponibles para llevar a cabo las operaciones de selección.

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

El módulo no cuenta con ventanas específicas en la interfaz de usuario de Openbravo, pero su funcionalidad se integra dentro de la ventana de 'Contribución de Retenciones'. Usuarios pueden navegar a través del módulo usando funcionalidades de búsqueda y filtrado disponibles en este contexto. A pesar de la ausencia de ventanas dedicadas, el acceso a la información se realiza de manera fluida gracias a la estructura del módulo.

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

No se encuentran botones de proceso específicos como completar, retornar o rechazar en este módulo. Sin embargo, el enfoque se centra en la búsqueda y la selección de socios comerciales, donde los usuarios pueden generar informes basados en los resultados de su búsqueda. Las validaciones frecuentes incluyen la necesidad de parámetros correctos para filtrar la búsqueda, asegurando que solo se muestre la información relevante en contexto de las retenciones fiscales.

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

El módulo incluye dos clases Java, 'BusinessPartner' y 'SelectorUtility', las cuales son esenciales para la implementación de la lógica de búsqueda y la gestión de la selección de socios comerciales. Estas clases trabajan en conjunto para manejar las solicitudes del usuario y construir las cláusulas SQL necesarias para obtener información de manera ordenada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.bpartner.search.withholdings`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `BusinessPartner` | info | HttpSecureAppServlet | — | `src/ec/com/sidesoft/bpartner/search/withholdings/info/BusinessPartner.java` |
| `SelectorUtility` | info | — | — | `src/ec/com/sidesoft/bpartner/search/withholdings/info/SelectorUtility.java` |
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

Dado que el módulo no incluye triggers ni funciones PL específicas, su funcionalidad se basa más en la lógica de proceso definida en las clases Java. Esto permite que la interacción de los datos se realice de forma eficiente desde la aplicación, proporcionando resultados en base a los criterios de búsqueda establecidos por los usuarios.

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

Módulo: `ec.com.sidesoft.bpartner.search.withholdings`.

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

# Glosario — prefijo `SLSBPS`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLSBPS` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.bpartner.search.withholdings` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Traducción Búsqueda Terceros - Comprobante de Retención
**Package:** `ec.com.sidesoft.bpartner.search.withholdings.se_ES`

# Module overview — Traducción Búsqueda Terceros - Comprobante de Retención

## Functional

El módulo 'Traducción Búsqueda Terceros - Comprobante de Retención' está diseñado para facilitar la traducción de los comprobantes de retención de terceros dentro del sistema Openbravo. Los actores principales son los usuarios de negocio que trabajan con retenciones fiscales y el equipo de soporte que proporciona asistencia técnica. El alcance del módulo incluye la adaptación del sistema a requisitos normativos específicos relacionados con la búsqueda y gestión de comprobantes de retención. Este módulo depende del 'Selector BPartner Search', que es crucial para su funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/bpartner/search/withholdings/se_ES` |
| Web | `web/ec.com.sidesoft.bpartner.search.withholdings.se_ES/` |

### Declared dependencies

- Selector BPartner Search

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

*(sin prefijo en AD_MODULE_DBPREFIX)*

# Guía de chat — Traducción Búsqueda Terceros - Comprobante de Retención

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.bpartner.search.withholdings.se_ES`).

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

- ¿Cómo puedo acceder a los comprobantes de retención?
- ¿Qué necesito para realizar la traducción de un comprobante de retención?
- ¿El módulo soporta múltiples idiomas para comprobantes?
- ¿Dónde encuentro el historial de búsquedas de terceros?
- ¿Cómo se verifica la información de un tercero en el sistema?
- ¿Hay alguna limitación al buscar comprobantes de retención?
- ¿Qué hacer si no encuentro un comprobante de retención específico?
- ¿Quién debe contactar para soporte técnico relacionado con este módulo?

# Domain — data model

## Functional

Dado que el módulo no especifica tablas físicas ni relaciones complejas, se deduce que su funcionamiento está orientado a integrar y traducir la funcionalidad del módulo relacionado con búsqueda de terceros y su asociación con comprobantes. No se configuraron etapas o triggers específicos, lo que sugiere un enfoque simplificado, posiblemente orientado a la visualización y traducción de datos sin alteraciones en la estructura subyacente.

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

El módulo carece de ventanas y botones específicos, lo que implica que la funcionalidad se integrará dentro de la estructura existente del módulo 'Selector BPartner Search'. Por lo tanto, la navegación se realizará a través de este módulo, utilizando sus interfaces establecidas para acceder y gestionar los datos relacionados con los comprobantes de retención.

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

Al no contar con botones de proceso definidos ni informes específicos, se infiere que la funcionalidad del módulo se limita a la visualización y traducción de las entradas de datos. Probablemente, se espera que los usuarios completen las tareas dentro del contexto del módulo dependiente, y no hay validaciones frecuentes ni procesos automatizados asociados a este módulo nuevo.

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

No existen clases Java asociadas a este módulo, lo cual refuerza la naturaleza simplificada y centrada en la traducción de la funcionalidad que se está implementando.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.bpartner.search.withholdings.se_ES`.

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

El módulo no incluye triggers ni funciones PL, indicando que su rol es puramente de apoyo y traducción, sin la necesidad de lógica adicional en la base de datos. Esto asegura que los usuarios puedan acceder a la funcionalidad sin interferencias de procesos automáticos.

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

Módulo: `ec.com.sidesoft.bpartner.search.withholdings.se_ES`.

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

# Glosario — prefijo `SE_ES`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SE_ES` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.bpartner.search.withholdings.se_ES` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Custom Withholding Payment
**Package:** `ec.com.sidesoft.custom.withholding.payment`

# Module overview — Custom Withholding Payment

## Functional

El módulo 'Custom Withholding Payment' permite a las empresas en Ecuador gestionar los pagos de retenciones de manera eficiente, asegurando el cumplimiento con la normativa local. Sus actores principales son los usuarios de negocio que realizan los pagos, los analistas de soporte (soporte L2) que ayudan con la resolución de problemas y los desarrolladores que mantienen y mejoran el módulo. Este módulo se integra con otros sistemas de Openbravo, como el núcleo y las localizaciones específicas para Ecuador, para proporcionar un flujo de trabajo completo en la gestión de las retenciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/withholding/payment` |
| Web | `web/ec.com.sidesoft.custom.withholding.payment/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Localization of Ecuador - Finances
- Localization of Ecuador - Withholdings

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSCWP`

# Guía de chat — Custom Withholding Payment

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.withholding.payment`).

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

- ¿Cómo puedo registrar un pago de retención?
- ¿Qué información necesito para completar un pago?
- ¿Existen validaciones automáticas al ingresar los datos?
- ¿Qué debo hacer si cometo un error en un registro de pago?
- ¿Cómo puedo visualizar los pagos de retención ya realizados?
- ¿Dónde encuentro la normativa que debo seguir para las retenciones?
- ¿Puedo editar un pago de retención después de haberlo registrado?
- ¿Qué pasos seguir si el sistema presenta un error al procesar un pago?

# Domain — data model

## Functional

El módulo utiliza una entidad cabecera que se encarga de capturar la información básica de cada pago de retención. Aunque no hay tablas físicas especificadas en el inventario, los procesos anteriores y posteriores se basan en las referencias a las localizaciones en Ecuador que permiten calcular las retenciones de acuerdo con las normativas vigentes. A pesar de la ausencia de triggers definidos, el correcto funcionamiento del módulo dependerá de su vinculación con las entidades relacionadas en las localizaciones de finanzas y retenciones.

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

El acceso al módulo se realiza a través del menú correspondiente en la interfaz de usuario de Openbravo. Al no contar con ventanas o pestañas específicas, la navegación se centraliza en el proceso de gestión de pagos de retenciones, permitiendo al usuario realizar el proceso de pago de forma simplificada a través de la funcionalidad disponible.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.withholding.payment.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Archivo Excel Pago Proveedor | Archive Provider Payment Excel | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.withholding.payment.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo tiene un botón de proceso que permite iniciar el registro de los pagos de retenciones. Al ejecutar este proceso, se pueden introducir los datos necesarios y completar la operación. No se generan informes específicos como parte de este módulo, pero se pueden realizar validaciones frecuentes sobre los datos ingresados para asegurar que cumplen con los criterios establecidos por la legislación ecuatoriana. Las etapas de completar, retornar y rechazar un pago están determinadas por el flujo de trabajo manejado por el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.withholding.payment.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Archive Provider Payment Excel | Archive Provider Payment Excel | Archive Provider Payment Excel | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Archive Provider Payment Excel | Archive Provider Payment Excel | Archive Provider Payment Excel | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Archive Provider Payment Excel | Archive Provider Payment Excel | — | — | — |
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

No se han identificado clases de Java dentro del módulo, lo que sugiere que toda la lógica del módulo se gestiona mediante las funcionalidades específicas de Openbravo sin personalizaciones adicionales en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.withholding.payment`.

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

Dado que el módulo no incluye triggers ni funciones PL específicas, su rol en la base de datos depende de la integración con otras partes del sistema. Sin embargo, en un entorno de implementación, se espera que cualquier apoyo vinculado a las consultas o manipulaciones de datos se realice a través de las reglas y procesos del núcleo de Openbravo.

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

Módulo: `ec.com.sidesoft.custom.withholding.payment`.

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

# Glosario — prefijo `SSCWP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCWP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.withholding.payment` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Archive Provider Payment Excel` — Archive Provider Payment Excel

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Withholding Summarys Readonly
**Package:** `ec.com.sidesoft.withholding.summarys`

# Module overview — Sidesoft Withholding Summarys Readonly

## Functional

El módulo 'Sidesoft Withholding Summarys Readonly' tiene como propósito permitir la visualización y gestión de resúmenes de retenciones específicamente configurados para el mercado ecuatoriano. Está diseñado para usuarios de negocio que requieren acceso a datos de retenciones sin permitir modificaciones, asegurando integridad y cumplimiento con la normativa local. Los actores principales son los usuarios que generan reportes y los administradores de sistema que soportan el módulo. Este módulo depende del núcleo de Openbravo y de la localización de Ecuador para retenciones de ventas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/withholding/summarys` |
| Web | `web/ec.com.sidesoft.withholding.summarys/` |

### Declared dependencies

- Core
- Localization of Ecuador - Withholdings Sales

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSWHSRO`

# Guía de chat — Sidesoft Withholding Summarys Readonly

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.withholding.summarys`).

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
- «¿Qué es la tabla sswhsro_withholding_summary?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo consultar un resumen de retenciones?
- ¿Este módulo permite editar los resúmenes de retenciones?
- ¿Dónde encuentro información sobre las dependencias del módulo?
- ¿Qué datos se incluyen en los resúmenes de retenciones?
- ¿Existen opciones para exportar los datos de los resúmenes?
- ¿Puedo recibir asistencia sobre errores en la visualización de los datos?
- ¿Cómo se actualizan los resúmenes en este módulo?
- ¿Quiénes son los encargados de mantener la información de retenciones actualizada?

# Domain — data model

## Functional

La entidad principal del módulo es 'sswhsro_withholding_summary', que almacena los resúmenes de las retenciones. No hay etapas intermedias definidas en el flujo, lo que simplifica su uso. Las relaciones entre las tablas son clave para asegurar que los datos se integren correctamente, especialmente con las tablas modificadas 'SSWS_CONFIG' y 'SSWS_WITHHOLDINGSALELINE'. Se han implementado dos triggers clave: 'SSWHSRO_VALIDATION_TRG' y 'SSWHSRO_WITHSUMMARY_TRG', que se activan en la tabla de 'ssws_withholdingsaleline' para validar y gestionar la lógica del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sswhsro_withholding_summary` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sswhsro_withholding_summary` | Sswhsro_Withholding_Summary | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_tax_id→c_tax; ssws_withholdingsale_id→ssws_withholdingsale | Detalle enlazado a ad_client, ad_org, c_tax. | PK `sswhsro_with_sum_key`; Cols: c_tax_id, ssws_withholdingsale_id, linenetamt, lineivaamt, whrentalamt; `SSWHSRO_WITH_SUM_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSWHSRO_WITH_SUM_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Sswhsro_Withholding_Summary` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`SSWS_CONFIG`, `SSWS_WITHHOLDINGSALELINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no presenta ventanas adicionales ni menús que faciliten el acceso a diferentes funciones. La navegación se realiza dentro de una única pestaña, lo que simplifica la visualización de los resúmenes de las retenciones. Esto permite a los usuarios centrar su atención en la información clave sin distracciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.withholding.summarys.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.withholding.summarys.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Resumen de retenciones

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Tax | `C_Tax_ID` | No | No | — |
| 20 | Income base | `Linenetamt` | No | No | — |
| 30 | Whithholding Rental Amount | `Whrentalamt` | No | No | — |
| 40 | VAT base | `Lineivaamt` | No | No | — |
| 50 | Whithholding IVA Amount | `Whivaamt` | No | No | — |

### Pestaña `6A54E582A78E44B0B1F435F4C6B62A44`

- **AD_TAB_ID:** `6A54E582A78E44B0B1F435F4C6B62A44` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 80 | Create new record | `EM_Sswhsro_Iscreatenew` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo carece de botones de proceso específicos, informes o elementos de validación adicionales. Sin embargo, se espera que los usuarios realicen tareas habituales como la visualización y revisión de datos. Los triggers definidos en el módulo juegan un papel crucial en la validación automática de cualquier dato agregado o modificado, manteniendo así la consistencia de la información presentada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.withholding.summarys.es_ES/referencedata/translation/`.

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
| `Sswhsro_CantCreate` | Cant Create | Cant Create | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo no incluye clases Java diseñadas específicamente, lo que limita su personalización a nivel de programación; sin embargo, se basa en las funcionalidades del núcleo de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.withholding.summarys`.

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
| Trigger `SSWHSRO_VALIDATION_TRG` | `ssws_withholdingsaleline` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSWHSRO_WITHSUMMARY_TRG` | `ssws_withholdingsaleline` | after INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Las funciones PL/pgSQL del módulo no se utilizan explícitamente para gestionar botones o procesos, pero los triggers juegan un rol esencial en la validación de datos y la integridad del módulo. Se aprovechan para mantener la calidad de la información en la tabla de resúmenes de retenciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSWHSRO_VALIDATION_TRG` | `ssws_withholdingsaleline` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWHSRO_VALIDATION_TRG.xml` |
| `SSWHSRO_WITHSUMMARY_TRG` | `ssws_withholdingsaleline` | after | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSWHSRO_WITHSUMMARY_TRG.xml` |
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

Módulo: `ec.com.sidesoft.withholding.summarys`.

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

# Glosario — prefijo `SSWHSRO`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSWHSRO` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.withholding.summarys` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Advanced Process Formulary 103 and 104
**Package:** `ec.com.sidesoft.withholdings.advanced.formulary`

# Module overview — Advanced Process Formulary 103 and 104

## Functional

El módulo 'Advanced Process Formulary 103 and 104' está diseñado para facilitar la gestión de formularios fiscales en Ecuador, especialmente para la retención de impuestos. Los actores principales son los contadores y administradores de empresas que utilizan Openbravo para cumplir con las regulaciones fiscales. Este módulo depende de la localización específica de Ecuador para retenciones, lo que garantiza que las funciones y formularios estén adaptados a la normativa local. Su alcance incluye la generación y manejo de formularios 103 y 104, vitales para la presentación de impuestos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/withholdings/advanced/formulary` |
| Web | `web/ec.com.sidesoft.withholdings.advanced.formulary/` |

### Declared dependencies

- Localization of Ecuador - Withholdings

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`CSWAF`

# Guía de chat — Advanced Process Formulary 103 and 104

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.withholdings.advanced.formulary`).

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
- «¿Qué es la tabla cswaf_form104_data?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo acceder a los formularios 104?
- ¿Qué información debo ingresar en los formularios 103?
- ¿Qué debo hacer si encuentro un error en los datos del contribuyente?
- ¿Cómo verifico si un formulario ha sido correctamente enviado?
- ¿Dónde puedo encontrar las validaciones para los campos obligatorios?
- ¿Qué sucede si no tengo acceso a una funcionalidad en la ventana de Scripts Formulary?
- ¿Cómo se actualizan los datos de los contribuyentes en el módulo?
- ¿A dónde puedo acudir para pedir ayuda sobre este módulo?

# Domain — data model

## Functional

La entidad cabecera principal es 'cswaf_form104_data', que almacena información relacionada con los formularios 104. La modificación de la tabla 'SSWH_TAXPAYER' está alineada con este módulo, lo que sugiere que contiene datos relevantes sobre los contribuyentes que utilizan estos formularios. Aunque no hay etapas o triggers definidos en el inventario, el modelo de datos está diseñado para integrarse con las funcionalidades de la localización ecuatoriana y apoyar la generación de los documentos requeridos por la ley tributaria.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `cswaf_form104_data` |
| `cswaf_form_codes_value` |
| `cswaf_salesdet_f104` |
| `cswaf_scripts_form` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `cswaf_form104_data` | cswaf_form104_data | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `cswaf_form104_data_key`; Cols: fieldtype, code, amount, process; `CSWAF_F104_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `CSWAF_FORM104_IDX1` (process, code) |
| `cswaf_form_codes_value` | cswaf_form_codes_value | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `cswaf_form_codes_value_pk`; Cols: code_father, amount_father, son_code, amount_son, line; `CSWAF_FCV_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N'); idx `CSWAF_FORM104_DATA_IDX1` (process) |
| `cswaf_salesdet_f104` | cswaf_salesdet_f104 | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `cswaf_salesdet_f104_pk`; Cols: cod_tipo_comprobante, base_no_iva, base_iva_cero, base_iva_doce, monto_iva; `CSWAF_SDT104_IA_CHK`: ISACTIVE IN ('Y', 'N'); idx `CSWAF_PROCESS_IDX1` (process) |
| `cswaf_scripts_form` | cswaf_scripts_form | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `cswaf_scripts_form_key`; Cols: form_type, sqlscript, description, line; `CSWAF_SF_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `cswaf_form104_data` |
| `cswaf_form_codes_value` |
| `cswaf_salesdet_f104` |
| `cswaf_scripts_form` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`SSWH_TAXPAYER`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo incluye una ventana denominada 'Scripts Formulary' que permite a los usuarios navegar directamente a las funcionalidades necesarias para manejar los formularios correspondientes. Dentro de esta ventana, los usuarios pueden acceder a los campos requeridos e interactuar con la información necesaria de manera intuitiva.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.withholdings.advanced.formulary.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Scripts Formulary | Scripts Formulary |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Scripts Formulary | Scripts Formulary | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.withholdings.advanced.formulary.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Scripts Formulary

- **AD_WINDOW_ID:** `5447A5B581FC4770984FCBB665FDFF47`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Scripts Formulary | `CCE844043CA94AE39745B208DD7962D4` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `6B2631C1D8FC4194ABC2BFA776FC8D68`

- **AD_TAB_ID:** `6B2631C1D8FC4194ABC2BFA776FC8D68` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 110 | Popular | `EM_Cswaf_Ispopular` | No | No | — |

### Scripts Formulary (ventana: Scripts Formulary)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 5 | Line | `Line` | No | No | — |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Form_Type | `Form_Type` | No | No | — |
| 30 | Sqlscript | `Sqlscript` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo no cuenta con botones de proceso específicos, ya que su función principal se centra en la gestión de datos y la disposición de formularios. Sin embargo, es crucial que los usuarios estén familiarizados con las validaciones que podrían ser comunes, como verificar la corrección de datos antes de presentar formularios y asegurarse de que toda la información cumpla con la normativa fiscal vigente. Dado que no hay informes ni procesos definidos, la atención se concentra en la correcta manipulación de los datos de entrada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.withholdings.advanced.formulary.es_ES/referencedata/translation/`.

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

No se han implementado clases Java en este módulo, por lo que la funcionalidad se basa principalmente en las características de la base de datos y en las funciones PL.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.withholdings.advanced.formulary`.

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
| Función PL `cswaf_execute_form_sql` | — | invocación proceso | V_ORG:= (case when p_org <> to_char('ND') then '''' || p_org  || '''' else to_char('NULL') end) ;; V_CLIENT:= (case when p_client <> to_char('ND') then '''' || p_client  || '''' else to_char('NULL') end) ;; RAISE NOTICE '%' , 'sCRIPT: ' || Cur_Parametersql.LINE || ' - ' || COALESCE( Cur_Parametersql.DESCRIPTION,'-');  --OBTG:-20000-- |
| Función PL `cswaf_formulary_process` | — | invocación proceso | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Procesar y guardar datos en tablas temporales cswaf_execute_form_sql |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y las funciones PL son limitados en este módulo, pero se incluyen dos funciones PL que son utilizadas para la validación de datos y el manejo de excepciones en el proceso de preparación de formularios. Esto es esencial para garantizar que la base de datos mantenga su integridad y que se cumplan las regulaciones fiscales sin errores.

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
| `cswaf_execute_form_sql` | — | V_ORG:= (case when p_org <> to_char('ND') then '''' || p_org || '''' else to_char('NULL') end) ;; V_CLIENT:= (case when p_client <> to_char('ND') then '''' || p_client || '''' else to_char('NULL') end) ;; RAISE NOTICE '… | V_ORG:= (case when p_org <> to_char('ND') then '''' || p_org  || '''' else to_char('NULL') end) ;; V_CLIENT:= (case when p_client <> to_char('ND') then '''' || p_client  || '''' else to_char('NULL') end) ;; RAISE NOTICE '%' , 'sCRIPT: ' || Cur_Parametersql.LINE || ' - ' || COALESCE( Cur_Parametersql.DESCRIPTION,'-');  --OBTG:-20000-- | `model/functions/CSWAF_EXECUTE_FORM_SQL.xml` |
| `cswaf_formulary_process` | — | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Procesar y guardar datos en tablas temporales cswaf_execute_f… | Elimina los archivos de la tabla temporal y las lineas del formulario; Recorre la lista de la vista sswh_withholdingpurchase_nats - Datos del Formulario 103; Procesar y guardar datos en tablas temporales cswaf_execute_form_sql; Actualizar Tabla Auxiliar Campo Padre - Total; Actualizar Tabla Auxiliar Campo Hijo - Total; Inserta todas las lineas de la tabla temporal a la tabla formulary lines. | `model/functions/CSWAF_FORMULARY_PROCESS.xml` |
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

Módulo: `ec.com.sidesoft.withholdings.advanced.formulary`.

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

# Glosario — prefijo `CSWAF`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `CSWAF` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.withholdings.advanced.formulary` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## XML IRBP
**Package:** `ec.com.sidesoft.xml.irbp`

# Module overview — XML IRBP

## Functional

El módulo XML IRBP proporciona funcionalidades para la generación y manejo de archivos XML relacionados con el IRBP (Impuesto a la Renta de Personas Jurídicas) en el entorno de Openbravo. Este módulo es utilizado principalmente por usuarios de negocio que requieren la elaboración de informes tributarios y por personal técnico que da soporte a estas funcionalidades. El alcance de este módulo incluye la interacción con las entidades organizativas y financieras del sistema, garantizando la conformidad con las normativas fiscales aplicables. Depende de otros módulos como '2.50 to 3.00 Compatibility Skin' y 'Sidesoft Localization Production Lote' para su correcta operación, lo que implica que su instalación debe realizarse en entornos donde estos módulos estén presentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/xml/irbp` |
| Web | `web/ec.com.sidesoft.xml.irbp/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Sidesoft Localization Production Lote

### Version

**1.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSXML`

# Guía de chat — XML IRBP

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.xml.irbp`).

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
- «¿Qué es la tabla ssxml_data_xml_ibp?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo generar el archivo XML para el IRBP?
- ¿Qué datos necesito proporcionar para utilizar el módulo XML IRBP?
- ¿Existen validaciones que deba conocer antes de generar el XML?
- ¿Puedo ver un registro de las operaciones realizadas con este módulo?
- ¿Qué hacer si obtengo un error al generar el archivo XML?
- ¿Cómo se relaciona este módulo con otros módulos de Openbravo?
- ¿Hay alguna forma de personalizar el contenido del archivo XML generado?
- ¿Dónde puedo encontrar ayuda adicional sobre el uso del módulo?

# Domain — data model

## Functional

El módulo se basa principalmente en la tabla ancla 'ssxml_data_xml_ibp', que incluye la información necesaria para la generación del XML. Esta tabla se relaciona con entidades importantes como 'AD_ORG' (Organización), 'M_WAREHOUSE' (Almacenes) y 'SLPLAG_KINDPACKAGE' (Paquetes de Tipos de Producto), que son cruciales para la estructura de datos del módulo. No se definen procesos de etapas adicionales, ya que la funcionalidad está centralizada en la generación de XML según los parámetros de entrada. Aunque no hay triggers asociados, se utilizan 7 funciones PL que permiten el procesamiento de datos y la manipulación de la información necesaria para el funcionamiento del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssxml_data_xml_ibp` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssxml_data_xml_ibp` | ssxml_data_xml_ibp | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssxml_data_xml_ibp_pk`; Cols: m_product_id, codeibp, isbom, embibp, sale |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssxml_data_xml_ibp` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ORG`, `M_WAREHOUSE`, `SLPLAG_KINDPACKAGE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Este módulo no cuenta con ventanas específicas visibles en la interfaz de usuario de Openbravo, lo que implica que su funcionamiento está centrado en la ejecución de procesos y la generación de resultados en segundo plano, sin interacción directa a través de interfaces gráficas. Sin embargo, los usuarios pueden acceder a sus funcionalidades a través del menú correspondiente, el cual agrupa las operaciones relacionadas con los informes XML.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.xml.irbp.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Crear xml - IRBP | Create xml - IRBP | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.xml.irbp.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `143`

- **AD_TAB_ID:** `143` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 169 | EM_Ssxml_Gruop_Irbp | `EM_Ssxml_Gruop_Irbp` | No | No | 484446FDD008485B8F5870B04E4584D1 |

### Pestaña `177`

- **AD_TAB_ID:** `177` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 160 | EM_Ssxml_Low_Ibp | `EM_Ssxml_Low_Ibp` | No | No | — |

### Pestaña `402E88C69A3349B7AC8E74514F0C0B62`

- **AD_TAB_ID:** `402E88C69A3349B7AC8E74514F0C0B62` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 70 | EM_Ssxml_Xml_Ats | `EM_Ssxml_Xml_Ats` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un único proceso denominado 'CreateXmlIrbp', que permite la generación del archivo XML. Este proceso se activa mediante un botón en la interfaz que inicia su ejecución, llevando a cabo validaciones de datos y asegurando que la información está completa antes de proceder con la creación del XML. Aunque no se generan informes estándar desde el módulo, se espera que el usuario esté atento a las validaciones comunes que se deban implementar en la acción de generación, asegurando que todos los parámetros requeridos están adecuadamente cargados. También es importante destacar que este módulo implica la devolución de posibles errores durante el proceso, que los usuarios deben tener en cuenta.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.xml.irbp.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Crear xml - IRBP | Create xml - IRBP | Create xml - IRBP | Java `CreateXmlIrbp` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cPeriodId`, No existe un Rango Impuesto que sea de tipo IRBP. | `src/ec/com/sidesoft/xml/irbp/CreateXmlIrbp.java` |
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
| Botón (Java) | Crear xml - IRBP | `CreateXmlIrbp` | Proceso Java (toolbar/background) | `cPeriodId` | No existe un Rango Impuesto que sea de tipo IRBP. | `src/ec/com/sidesoft/xml/irbp/CreateXmlIrbp.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Crear xml - IRBP | Create xml - IRBP | Create xml - IRBP | Java `CreateXmlIrbp` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cPeriodId`, No existe un Rango Impuesto que sea de tipo IRBP. | `src/ec/com/sidesoft/xml/irbp/CreateXmlIrbp.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Crear xml - IRBP | Create xml - IRBP | Java `CreateXmlIrbp` | Proceso Openbravo registro `cPeriodId`, No existe un Rango Impuesto que sea de tipo IRBP. | No existe un Rango Impuesto que sea de tipo IRBP. |
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

El módulo incluye una clase Java denominada 'CreateXmlIrbp', que se encarga de gestionar la lógica de ejecución para la creación del archivo XML. Esta clase se basa en el manejo de datos desde la base de datos, realizando transformaciones y asegurando que la estructura del XML generado cumpla con los requisitos establecidos por la normativa IRBP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.xml.irbp`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `CreateXmlIrbp` | root | DalBaseProcess | — | `src/ec/com/sidesoft/xml/irbp/CreateXmlIrbp.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `XML IRBP OPEN_PERIOD_VALIDATE` | `C_Period.openclose='C'` |
| AD_VAL_RULE | — | `XML IRBP - Org` | `ad_org.ad_org_id in ( select o.ad_org_id from AD_Orgtype ot LEFT JOIN ad_org o ON o.AD_Orgtype_id =  ot.AD_Orgtype_id WH` |
| Función PL `ssxml_dev_qty_ibp` | — | invocación proceso | CONSULTAR EN EL PRODUCTO LDM EL SUBPRODUCTO Y SU CANTIDAD Lista de Materiales |
| Función PL `ssxml_sales_qty_ibp` | — | invocación proceso | CONSULTAR EN EL PRODUCTO LDM EL SUBPRODUCTO Y SU CANTIDAD Lista de Materiales |
| Función PL `ssxml_temp_data_xml_ibp` | — | invocación proceso | AND mp.m_product_Id = '3EAAC2F9A6B842529649A24D73F9A964'; Order by toma primero productos que no son LDM Ingrese esos productos a la tabla; consulte embotellamiento en el Plan de produccion |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Las funciones PL desempeñan un papel vital en el soporte del módulo, ya que permiten la manipulación, validación y preparación de los datos necesarios para la creación del archivo XML. Aunque no existen triggers específicos que actúan automáticamente, las funciones definidas permiten realizar las tareas necesarias en el contexto de operaciones realizadas sobre las tablas relacionadas, asegurando así la integridad y disponibilidad de la información requerida.

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
| `ssxml_baja_ibp` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSXML_BAJA_IBP.xml` |
| `ssxml_code_prod_ibp` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSXML_CODE_PROD_IBP.xml` |
| `ssxml_dev_qty_ibp` | — | CONSULTAR EN EL PRODUCTO LDM EL SUBPRODUCTO Y SU CANTIDAD Lista de Materiales | CONSULTAR EN EL PRODUCTO LDM EL SUBPRODUCTO Y SU CANTIDAD Lista de Materiales | `model/functions/SSXML_DEV_QTY_IBP.xml` |
| `ssxml_emb_ibp` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSXML_EMB_IBP.xml` |
| `ssxml_sales_qty_ibp` | — | CONSULTAR EN EL PRODUCTO LDM EL SUBPRODUCTO Y SU CANTIDAD Lista de Materiales | CONSULTAR EN EL PRODUCTO LDM EL SUBPRODUCTO Y SU CANTIDAD Lista de Materiales | `model/functions/SSXML_SALES_QTY_IBP.xml` |
| `ssxml_temp_data_xml_ibp` | — | AND mp.m_product_Id = '3EAAC2F9A6B842529649A24D73F9A964'; Order by toma primero productos que no son LDM Ingrese esos productos a la tabla; consulte embotellamiento en el Plan de produccion; v_movementqty = CAST((SELECT… | AND mp.m_product_Id = '3EAAC2F9A6B842529649A24D73F9A964'; Order by toma primero productos que no son LDM Ingrese esos productos a la tabla; consulte embotellamiento en el Plan de produccion; v_movementqty = CAST((SELECT ssxml_emb_ibp(p_initDate,p_endDate, Cur_Data.m_product_id, p_group, p_codeImp, p_codeCountry)) AS INTEGER);; SI APLICA TAG VENTAS EN XML ( de subproductos ) * CANTIDAD LDM por ser subproducto; SI APLICA TAG DEVOLUCIONES EN XML ( de subproductos ) | `model/functions/SSXML_TEMP_DATA_XML_IBP.xml` |
| `ssxml_validate_ibps` | — | Validación reutilizable de campos. | — | `model/functions/SSXML_VALIDATE_IBPS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Crear xml - IRBP | `Create xml - IRBP` | Botón (Java) | Java `CreateXmlIrbp` | N | Proceso Openbravo registro `cPeriodId`, No existe un Rango Impuesto que sea de tipo IRBP. |

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

Módulo: `ec.com.sidesoft.xml.irbp`.

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

# Glosario — prefijo `SSXML`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSXML` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.xml.irbp` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Create xml - IRBP` — Crear xml - IRBP

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## IRBP Reports
**Package:** `ec.com.sidesoft.irbp.reports`

# Module overview — IRBP Reports

## Functional

El módulo IRBP Reports tiene como propósito proporcionar herramientas para la generación de informes relacionados con los campos de IRBP dentro de Openbravo. Los actores principales de este módulo son los usuarios de negocio que requieren reportes sobre información específica, así como los desarrolladores y personal de soporte que pueden ajustar y mantener el módulo. El alcance se limita a la generación de informes y su visualización, utilizando la información de los campos de IRBP. Este módulo depende de varias extensiones y componentes del sistema, incluyendo la compatibilidad con la piel de versión 2.50 a 3.00, el núcleo de Openbravo y la localización Sidesoft para la producción de lotes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/irbp/reports` |
| Web | `web/ec.com.sidesoft.irbp.reports/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework
- Sidesoft Localization Production Lote

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSIR`

# Guía de chat — IRBP Reports

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.irbp.reports`).

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

- ¿Cómo puedo generar un informe de IRBP?
- ¿Qué información necesito ingresar para crear un informe?
- ¿Hay algún ejemplo de informe ya disponible en el módulo?
- ¿Cómo puedo acceder a los informes generados?
- ¿Puedo exportar los informes a otro formato?
- ¿Qué sucede si los datos del informe no son correctos?
- ¿Puedo personalizar los informes de IRBP según mis necesidades?
- ¿A quién contacto si tengo problemas al generar un informe?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la creación y manejo de informes, aunque no implementa tablas físicas adicionales ni relaciones complejas. La entidad cabecera que sostiene este módulo sería el propio informe que se origina a partir de campos de IRBP. Existen etapas en la generación de estos informes, que implican la selección de parámetros por parte del usuario, la ejecución del informe y la visualización del resultado. No se disponen de triggers clave en este módulo, lo que simplifica su estructura en términos de manejo de la base de datos.

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

El módulo IRBP Reports se accede a través del menú en la interfaz de usuario de Openbravo. Aunque no se disponen de ventanas específicas dentro del módulo, los usuarios pueden generar informes accediendo a las opciones disponibles en la sección de reportes, donde se les presentará la opción correspondiente para la creación de informes IRBP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.irbp.reports.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Producciones por tipo envase | Production report by type of packaging | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.irbp.reports.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso para la creación de informes que se activa mediante un botón en la interfaz de usuario. Este botón permite a los usuarios completar la acción de generación de un informe basado en los campos IRBP seleccionados previamente. Aunque no hay informes predefinidos dentro del módulo, se sugiere que se implementen validaciones para asegurar que los datos ingresados sean correctos y completos antes de la ejecución del proceso.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.irbp.reports.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Producciones por tipo envase | Production report by type of packaging | Production report by type of packaging | *(OBUIAPP / manual)* | Production report by type of packaging | — |
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
| Proceso / otro | Producciones por tipo envase | Production report by type of packaging | Production report by type of packaging | *(OBUIAPP / manual)* | Production report by type of packaging | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Producciones por tipo envase | Production report by type of packaging | — | Production report by type of packaging | — |
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

El módulo IRBP Reports no incluye implementaciones de clases en Java. Por lo tanto, no hay lógica de procesamiento específica implementada en el lado del servidor en este módulo, lo que lo hace depender completamente de la infraestructura existente de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.irbp.reports`.

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

A pesar de que el módulo no incluye triggers ni funciones PL específicas, se destacan las funciones generales de soporte en la base de datos, que garantizan la integridad y el acceso a los datos necesarios para los informes. Las funciones del módulo dependen en gran medida del funcionamiento del núcleo de Openbravo y su capacidad para manejar consultas sobre los campos de IRBP.

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

Módulo: `ec.com.sidesoft.irbp.reports`.

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

# Glosario — prefijo `SSIR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSIR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.irbp.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Production report by type of packaging` — Producciones por tipo envase

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Ecuador Localization Dataset
**Package:** `ec.com.sideosft.localization.datasets`

# Module overview — Ecuador Localization Dataset

## Functional

El módulo 'Ecuador Localization Dataset' tiene como propósito proporcionar un conjunto de datos adaptados a las necesidades locales de Ecuador en el entorno de Openbravo ERP. Los actores involucrados incluyen usuarios de negocio que requieren información contextualizada, así como desarrolladores que implementan y mantienen este conjunto de datos. El alcance del módulo se limita a la localización geográfica y no incluye funcionalidades específicas de gestión operativa. No posee dependencias con otros módulos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sideosft/localization/datasets` |
| Web | `web/ec.com.sideosft.localization.datasets/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLDA`

# Guía de chat — Ecuador Localization Dataset

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sideosft.localization.datasets`).

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

- ¿Cómo puedo acceder a los datos de localización de Ecuador?
- ¿Este módulo se integra con otros módulos del ERP?
- ¿Dónde encuentro la documentación técnica del módulo?
- ¿Qué requisitos de sistema tiene este módulo?
- ¿Existen actualizaciones disponibles para la versión del módulo?
- ¿Cómo puedo reportar un error relacionado con la localización?
- ¿Qué tipo de soporte se ofrece para este módulo?
- ¿Puedo personalizar los datos de localización según mis necesidades?

# Domain — data model

## Functional

El modelo de datos del módulo no incluye entidades cabecera ni relaciones complejas, ya que se trata de un conjunto de datos específico y no de un sistema de gestión de inventarios extenso. No se identifican etapas ni triggers clave, dado que el inventario indica la ausencia de estructuras de soporte como tablas físicas y funciones PL.

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

No se habilitan ventanas o interfaces específicas en la UI para este módulo. Los usuarios interactuarían con los datos a través de funcionalidades generales del ERP, pero no hay una navegación definida para este conjunto de localización.

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

El módulo carece de procesos determinados, botones de acción o informes específicos. No se encuentran validaciones frecuentes ni procesos adicionales enlazados en el módulo, lo que sugiere su enfoque limitado en la localización de datos sin interacción directa en el flujo de trabajo del ERP.

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

El módulo no incluye clases Java, por lo que no hay funcionalidad JAVA asociada a este conjunto de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sideosft.localization.datasets`.

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

No se definen triggers ni funciones PL en este módulo, lo que implica que no hay un rol activo de estas estructuras en el soporte o en los procesos del sistema. Su contribución es puramente informativa sin manipulación directa de la base de datos.

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

Módulo: `ec.com.sideosft.localization.datasets`.

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

# Glosario — prefijo `SLDA`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLDA` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sideosft.localization.datasets` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Localizacion RIMPE
**Package:** `ec.com.sidesoft.localization.rimpe`

# Module overview — Sidesoft Localizacion RIMPE

## Functional

El módulo Sidesoft Localización RIMPE se implementa para gestionar las retenciones en la fuente en el contexto de la normativa ecuatoriana. Su principal finalidad es facilitar el cumplimiento de las obligaciones fiscales, permitiendo a las empresas configurar y aplicar correctamente los impuestos de retención en sus transacciones. Los actores principales son los usuarios de negocio encargados de la administración contable, así como el soporte técnico que proporciona asistencia a los usuarios. El alcance del módulo se limita a la modificación de tablas específicas asociadas a las entidades de negocio, en este caso, C_BPARTNER y C_INVOICELINE. Este módulo depende de la localización de Ecuador y las retenciones correspondientes que están contempladas en otras configuraciones del ERP Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/rimpe` |
| Web | `web/ec.com.sidesoft.localization.rimpe/` |

### Declared dependencies

- Localization of Ecuador - Withholdings

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSRIMPE`

# Guía de chat — Sidesoft Localizacion RIMPE

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.rimpe`).

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

- ¿Cómo configuro las retenciones para un nuevo socio de negocio?
- ¿Qué debo hacer si un impuesto no aparece en la lista de opciones?
- ¿Cómo puedo verificar que un impuesto de retención se aplicó correctamente?
- ¿Dónde encuentro la información sobre la normatividad de retenciones para Ecuador?
- ¿Qué pasos debo seguir si necesito modificar la retención de una factura?
- ¿Existen informes disponibles para analizar las retenciones aplicadas este mes?
- ¿Cómo se efectúa la carga de datos relacionados con las retenciones?
- ¿A quién debo contactar para soporte técnico respecto al módulo RIMPE?

# Domain — data model

## Functional

El modelo de datos del módulo se centra principalmente en la entidad cabecera C_BPARTNER, que representa a los socios de negocio, y en C_INVOICELINE, que almacena las líneas de las facturas. Las modificaciones realizadas en estas tablas permiten que el sistema gestione las retenciones en la fuente adecuadamente. En cuanto a las etapas, aunque no se especifican flujos directos, se puede inferir que las transacciones de cada socio de negocio implican una revisión de los impuestos aplicables a las facturas generadas. Los triggers clave, como SSRIMPE_EDITWITHH_TRG, se disparan al cambiar el impuesto en el campo de Retención en la fuente, lo que asegura que los datos permanezcan actualizados y consistentes. Otro trigger, SSRIMPE_LOAD_WITHHSRC_TRG, invoca una rutina PL/pgSQL que facilita la cargar los datos relacionados en la línea de factura.

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

`C_BPARTNER`, `C_INVOICELINE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo Sidesoft Localización RIMPE no cuenta con ventanas o tabs visibles en la interfaz de usuario. Las funcionalidades disponibles probablemente se integran en los módulos existentes dentro del ERP, mejorando la capacidad de gestión de retenciones sin la necesidad de una interfaz separada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.rimpe.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.rimpe.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `220`

- **AD_TAB_ID:** `220` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 305 | Edit withholding | `EM_Ssrimpe_Edit_Withholding` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |
| 306 | Withholding at source | `EM_Ssrimpe_Tax_ID` | No | No | 402880E72F1C15A5012F1C7AA98B00E8 |

### Pestaña `291`

- **AD_TAB_ID:** `291` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 66 | Withholding at source | `EM_Ssrimpe_Tax_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

En cuanto a los procesos, este módulo no proporciona botones específicos ni informes adicionales. No obstante, las pruebas habituales incluyen la validación de los impuestos aplicados en la creación o modificación de los registros pertinentes. Es importante mencionar que la interacción con los triggers puede requerir revisiones en la creación de socios de negocio y líneas de factura, asegurando que se seleccionen correctamente los impuestos correspondientes. Las validaciones frecuentes incluyen la correcta selección de retenciones en función de la normativa vigente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.rimpe.es_ES/referencedata/translation/`.

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

No se incluyen clases Java en este módulo, por lo que toda la funcionalidad se basa en la configuración y los triggers en la base de datos para asegurar el cumplimiento de las regulaciones relacionadas con las retenciones fiscales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.rimpe`.

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
| Trigger `SSRIMPE_EDITWITHH_TRG` | `c_bpartner` | before INSERT/UPDATE | Seleccione un impuesto en el campo Retención en la fuente. |
| Trigger `SSRIMPE_LOAD_WITHHSRC_TRG` | `c_invoiceline` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers desempeñan un papel esencial para mantener la integridad y la lógica de negocios en las tablas modificadas. El uso de procesos PL/pgSQL a través del trigger SSRIMPE_LOAD_WITHHSRC_TRG permite cargar datos esenciales de manera eficiente en el sistema, apoyando las operaciones de retención sin intervención manual del usuario, lo que aumenta la eficiencia y reduce errores.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSRIMPE_EDITWITHH_TRG` | `c_bpartner` | before | INSERT/UPDATE | Seleccione un impuesto en el campo Retención en la fuente. | `model/triggers/SSRIMPE_EDITWITHH_TRG.xml` |
| `SSRIMPE_LOAD_WITHHSRC_TRG` | `c_invoiceline` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSRIMPE_LOAD_WITHHSRC_TRG.xml` |
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

Módulo: `ec.com.sidesoft.localization.rimpe`.

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

# Glosario — prefijo `SSRIMPE`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSRIMPE` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.rimpe` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
