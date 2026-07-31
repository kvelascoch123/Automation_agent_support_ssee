# Openbravo Sidesoft — Nómina

> Nómina base y avanzada, rol de pagos mensual y quincenal, anticipos, préstamos, décimos, biometría, asistencia, centro de costos, IR, formulario 107, LOTAIP.

**Paquetes incluidos (22):**
- `com.sidesoft.hrm.payroll` — Human Resources Management - Payroll
- `com.sidesoft.hrm.payroll.advanced` — Advanced PayRoll
- `com.sidesoft.hrm.payroll.biometrical` — Sidesoft Payroll Biometrical Interface
- `com.sidesoft.hrm.payroll.disaccounting` — Payroll Accounting Distributed by Cost Center
- `com.sidesoft.hrm.payroll.early.payment` — Payroll Anticipated Payments
- `com.sidesoft.hrm.payroll.indebtedness` — Payroll Indebtedness
- `com.sidesoft.hrm.payroll.tenth` — Human Resources Management - Payroll - Tenth
- `ec.com.sidesoft.hrm.payroll.attendancepayroll` — Attendance Payroll Module
- `ec.com.sidesoft.hrm.payroll.payment.rol` — Sidesoft Automatic Process of Payment Roles Monthly
- `ec.com.sidesoft.hrm.payroll.payment.rol.fortnight` — Sidesoft Automatic Process of Payment Roles Fortnight
- `ec.com.sidesoft.hrm.payroll.early.payment.sentmail` — Payroll Anticipated Payments - Sentmail
- `ec.com.sidesoft.hrm.payroll.reports` — Sidesoft Payroll Reports
- `ec.com.sidesoft.custom.payroll.reports` — Custom Payroll Reports
- `ec.com.sidesoft.custom.payroll.sentmail` — Payroll - Sent Mail
- `ec.com.sidesoft.payroll.costcenter` — Payroll by Cost Center
- `ec.com.sidesoft.payroll.events` — Sidesoft Payroll Events
- `ec.com.sidesoft.payroll.ir` — Sidesoft Payroll IR
- `ec.com.sidesoft.payroll.overtime` — Sidesoft Overtime for Biometrical
- `ec.com.sidesoft.payroll.report.actuarial` — Actuarial Report
- `ec.com.sidesoft.payroll.reports.lotaip` — Sidesoft Payroll Report - Lotaip
- `ec.com.sidesoft.payroll.setup.formulary107` — Payroll Setup Formulary 107
- `ec.com.sidesoft.incometax.batch` — Sidesoft Income Tax Batch Charge


---
## Human Resources Management - Payroll
**Package:** `com.sidesoft.hrm.payroll`

# Module overview — Human Resources Management - Payroll

## Functional

El módulo de Gestión de Recursos Humanos - Nómina tiene como propósito la administración completa del proceso de nómina dentro de una organización. Los actores principales son los departamentos de recursos humanos y contabilidad, así como los empleados que son beneficiarios de los servicios de nómina. El alcance del módulo cubre desde la aprobación de permisos y préstamos hasta la generación de informes de liquidación y detalles de nómina. Este módulo depende del núcleo del ERP Openbravo, asegurando su correcta implementación y funcionamiento en integración con otros módulos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/hrm/payroll` |
| Web | `web/com.sidesoft.hrm.payroll/` |

### Declared dependencies

- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPR`

# Guía de chat — Human Resources Management - Payroll

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.hrm.payroll`).

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
- «¿Qué es la tabla sspr_leave_emp?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo solicitar un permiso a través del módulo?
- ¿Qué procesos son necesarios para aprobar un préstamo?
- ¿Dónde puedo ver el historial de mis liquidaciones?
- ¿Cómo se gestionan las vacaciones dentro del sistema?
- ¿Qué informes puedo generar sobre la nómina?
- ¿Cómo se registran nuevas deducciones en la nómina?
- ¿Qué pasos debo seguir para modificar un registro de empleado?
- ¿Cómo puedo validar si mis datos están actualizados en el sistema?

# Domain — data model

## Functional

La entidad principal en este módulo es la nómina, la cual se registra en la tabla `sspr_payroll`. El sistema permite gestionar distintas etapas como la aprobación de permisos a través de la tabla `sspr_leave_emp` y la gestión de préstamos en `sspr_line_loans`. Relaciones clave incluyen las interacciones entre las tablas de empleados (`c_bpartner`) y conceptos de nómina (`sspr_concept`). Trigger clave como `SSPR_EMPLOYEE_DEFAULT` permiten establecer valores predeterminados para nuevos registros de empleados, mientras que `SSPR_PAYROLL_AUT_CREATE_TRG` verifica la existencia de registros de nómina de manera automatizada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sspr_acctledger` |
| `sspr_actuarial_calc_study` |
| `sspr_asientonomina` |
| `sspr_asientonomina_prov` |
| `sspr_attendance` |
| `sspr_bank` |
| `sspr_benefit_dismissal` |
| `sspr_calculation_concepts` |
| `sspr_category` |
| `sspr_category_acct` |
| `sspr_codeformulary107` |
| `sspr_concept` |
| `sspr_concept_acct` |
| `sspr_concept_amount` |
| `sspr_configurationutility` |
| `sspr_contract` |
| `sspr_contract_position` |
| `sspr_contracttype` |
| `sspr_costdeductiblemax` |
| `sspr_costemployee` |
| `sspr_costemployeeline` |
| `sspr_cumulativeconcept` |
| `sspr_disability` |
| `sspr_disabilityline` |
| `sspr_employeesettlement` |
| `sspr_employeesettlementline` |
| `sspr_establishmentcode` |
| `sspr_family` |
| `sspr_formulary107` |
| `sspr_formularyline107` |
| `sspr_general_param_payroll` |
| `sspr_holiday` |
| `sspr_hours_work` |
| `sspr_iessrate` |
| `sspr_iessrateline` |
| `sspr_incometax` |
| `sspr_incometaxline` |
| `sspr_incometotal` |
| `sspr_labor_regime` |
| `sspr_labor_regime_detail` |
| `sspr_leave_category` |
| `sspr_leave_conf_default` |
| `sspr_leave_emp` |
| `sspr_leave_emp_details` |
| `sspr_leave_emp_mant` |
| `sspr_leave_emp_notes` |
| `sspr_leave_emp_vac` |
| `sspr_leave_group` |
| `sspr_leave_hr_management` |
| `sspr_leave_type` |
| `sspr_level_ed` |
| `sspr_line_loans` |
| `sspr_loans` |
| `sspr_occupation` |
| `sspr_other_tax_income` |
| `sspr_other_tax_income_line` |
| `sspr_payroll` |
| `sspr_payroll_aut` |
| `sspr_payroll_aut_line` |
| `sspr_payroll_emp` |
| `sspr_payroll_ticket` |
| `sspr_payroll_ticket_concept` |
| `sspr_payrollpayment` |
| `sspr_pension_system` |
| `sspr_period` |
| `sspr_period_concept` |
| `sspr_position` |
| `sspr_process_payroll` |
| `sspr_profits` |
| `sspr_prolltem_lines` |
| `sspr_prolltemplate` |
| `sspr_readmissions` |
| `sspr_relationship` |
| `sspr_renewal_data` |
| `sspr_settlement` |
| `sspr_settlementconfig` |
| `sspr_settlementconfigline` |
| `sspr_settlementdata` |
| `sspr_settlementline` |
| `sspr_shift` |
| `sspr_supplementary_data` |
| `sspr_typeguarantor` |
| `sspr_typeguarantorline` |
| `sspr_utilities` |
| `sspr_utility_detail` |
| `sspr_vacations` |
| `sspr_valuesindicesperiod` |
| `sspr_work_week` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sspr_acctledger` | sspr_acctledger | — | — | c_validcombination_id→c_validcombination; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_validcombination. | PK `sspr_acctledger_key`; Cols: name, c_validcombination_id, closingaccount, ishaveaccount; `SSPR_INCOMETAX_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_INCOMETAX_ISCLOSE_CHK`: CLOSINGACCOUNT IN ('Y', 'N') (+1) |
| `sspr_actuarial_calc_study` | sspr_actuarial_calc_study | — | `SSPR_OTI_PEC` (c_period_id, taxid, concept) | ad_client_id→ad_client; ad_org_id→ad_org; c_period_id→c_period | Detalle enlazado a ad_client, ad_org, c_period. | PK `sspr_acs_key`; Cols: c_period_id, taxid, name, date_birth, date_admission; `SSPR_ACS_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `sspr_asientonomina` | SSPR_Asientonomina | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_asientonomina_pk`; Cols: cuenta, tercero, descripcioncuenta, movimiento, debe |
| `sspr_asientonomina_prov` | SSPR_Asientonomina_prov | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_asientnomina_pro_pk`; Cols: cuenta, tercero, descripcion, movimiento, debe |
| `sspr_attendance` | sspr_attendance | — | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_attendance_id_key`; Cols: c_bpartner_id, hoursentry, hoursout, hoursextra, days; `SSPR_ATTENDANCE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_bank` | sspr_bank | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_bank_key`; Cols: name, code, description; `SSPR_BANK_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_benefit_dismissal` | sspr_benefit_dismissal | — | — | sspr_concept_tenth_id→sspr_concept; ad_client_id→ad_client; sspr_concept_id→sspr_concept; ad_org_id→ad_org | Detalle enlazado a ad_client, sspr_concept. | PK `sspr_benefit_dismissal_key`; Cols: line, sspr_concept_id, value, description, rate; `SSPR_SETTLEMENTLINE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_calculation_concepts` | SSPR_Calculation_Concepts | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_pension_system_id→sspr_pension_system | Detalle enlazado a ad_client, ad_org, sspr_pension_system. | PK `sspr_calculation_concepts_key`; Cols: sspr_pension_system_id, name, description, rate; `SSPR_CONCEPTS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_category` | SSPR_Category | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sspr_pension_system_id→sspr_pension_system; sspr_occupation_id→sspr_occupation | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_category_key`; Cols: category, c_bpartner_id, pensiontype, entrydate, situation; `SSPR_CATEGORY_INSURANCE_CHK`: ISHEALTHINSURANCE IN ('Y', 'N'); `SSPR_CATEGORY_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') (+1) |
| `sspr_category_acct` | sspr_category_acct | — | — | balanceacct_id→c_validcombination; clearance_account_id→c_validcombination; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, c_validcombination. | PK `sspr_category_acct_id_key`; Cols: name, value, description, balanceacct_id, clearance_account_id; `SSPR_CATEGORY_ACCT_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_codeformulary107` | sspr_codeformulary107 | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_codeformulary107_key`; Cols: value, name, typeconcept; `SSPR_CODEFORMULARY107_ISACT_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_concept` | SSPR_Concept | `SSPR_VAL_CONCEPTTYPE` | `SSPR_CONCEPT_NAME_UN` (name); `SSPR_CONCEPT_VALUE_UN` (value) | ad_client_id→ad_client; ad_org_id→ad_org; sspr_codeformulary107_id→sspr_codeformulary107; sspr_concept_formula_id→sspr_concept; conceptformulates→sspr_concept | Detalle enlazado a ad_client, ad_org, sspr_codeformulary107. Validado por trigger(s): SSPR_VAL_CONCEPTTYPE. | PK `sspr_concept_key`; Cols: name, value, affectationtype, conceptsubtype, sspr_concept_formula_id; `SSPR_CONCEPT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_CONCEPT_ISCUMULA`: ISCUMULATIVE IN ('Y', 'N') (+1) |
| `sspr_concept_acct` | sspr_concept_acct | — | `SSPR_CONCEPT_ACCT_CATEGORY_UN` (sspr_category_acct_id, sspr_concept_id, c_acctschema_id) | ad_client_id→ad_client; ad_org_id→ad_org; c_acctschema_id→c_acctschema; c_credit_acct→c_validcombination; c_debit_acct→c_validcombination (+2) | Detalle enlazado a ad_client, ad_org, c_acctschema. | PK `sspr_concept_acct_key`; Cols: sspr_concept_id, c_acctschema_id, c_debit_acct, c_credit_acct, isaccountcharge; `SSPR_CONCEPT_ACCOUNTPAY`: ISACCOUNTPAYROLL IN ('Y', 'N'); `SSPR_CONCEPT_ACCT_ISACCT`: ISACCOUNTCHARGE IN ('Y', 'N') (+1) |
| `sspr_concept_amount` | SSPR_Concept_Amount | `SSPR_CONCEPT_AMOUNT_TRG` | `SSPR_AMOUNTS_UN` (sspr_concept_id, c_period_id, c_bpartner_id) | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_period_id→c_period; sspr_concept_id→sspr_concept | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SSPR_CONCEPT_AMOUNT_TRG. | PK `sspr_concept_amount_key`; Cols: sspr_concept_id, c_bpartner_id, c_period_id, amount, ismodified; `SSPR_CONCEPT_AMOUNT_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSPR_CONCEPT_AMOUNT_COMB` (sspr_concept_id, c_period_id); idx `SSPR_CONCEPT_AMOUNT_COMB1` (sspr_concept_id) (+2) |
| `sspr_configurationutility` | sspr_configurationutility | — | `SSPR_CONFUTI_YEAR_UNIQUE` (c_year_id) | c_period_incometax_id→c_period; c_period_id→c_period; sspr_codeformulary107_id→sspr_codeformulary107; sspr_concept_id→sspr_concept; ad_client_id→ad_client (+2) | Parametrización / catálogo de soporte. | PK `sspr_configurationutility_key`; Cols: c_year_id, perc_participation_employee, perc_earnings_employee, perc_utility_loads, age_limit_child; `SSPR_CONFUTI_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_contract` | SSPR_Contract | `SSPR_UPDATEENTRYDATE_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_year_id→c_year; c_city_id→c_city (+6) | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SSPR_UPDATEENTRYDATE_TRG. | PK `sspr_contract_key`; Cols: c_bpartner_id, contractcondition, startdate, enddate, isnight; `SSPR_CONTRACT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_CONTRACT_ISCUMULATIVE_CHK`: ISCUMULATIVEREGIME IN ('Y', 'N') (+1) |
| `sspr_contract_position` | SSPR_Contract_Position | — | — | ad_org_id→ad_org; ad_client_id→ad_client; sspr_contract_id→sspr_contract; sspr_position_id→sspr_position | Detalle enlazado a ad_client, ad_org, sspr_contract. | PK `sspr_contract_position_key`; Cols: sspr_contract_id, sspr_position_id, startdate, enddate, boss; `SSPR_POSITION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_contracttype` | SSPR_ContractType | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_contracttype_key`; Cols: name, description, code, format; `SSPR_CONTRACTTYPE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_costdeductiblemax` | sspr_costdeductiblemax | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_year_id→c_year | Detalle enlazado a ad_client, ad_org, c_year. | PK `sspr_costdeducmax_key`; Cols: c_year_id, startdate, enddate, deductibleexpense, basemax; `SSPR_COSTDEDUCMAX_ISAC_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_costemployee` | sspr_costemployee | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_year_id→c_year | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_costemployee_key`; Cols: c_bpartner_id, c_year_id, startdate, enddate, amountcost; `SSPR_COSTEMPLOYEE_ISAC_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_costemployeeline` | sspr_costemployeeline | `SSPR_COSTEMPLOYEE_TRG`; `SSPR_VALIDACOSTDEDUCTIBLE_TRG` | — | sspr_codeformulary107_id→sspr_codeformulary107; ad_client_id→ad_client; sspr_costemployee_id→sspr_costemployee; ad_org_id→ad_org | Detalle enlazado a ad_client, sspr_codeformulary107, sspr_costemployee. Validado por trigger(s): SSPR_COSTEMPLOYEE_TRG, SSPR_VALIDACOSTDEDUCTIBLE_TRG. | PK `sspr_costemployeeline_key`; Cols: deductibleexpense, amountdeductible, sspr_costemployee_id, sspr_codeformulary107_id; `SSPR_COSTEMPLOYEELINE_ISAC_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_cumulativeconcept` | sspr_cumulativeconcept | — | — | c_bpartner_id→c_bpartner; sspr_concept_id→sspr_concept; c_period_id→c_period; c_year_id→c_year; ad_client_id→ad_client (+1) | Detalle enlazado a c_bpartner, c_period, sspr_concept. | PK `sspr_cumulativeconcept_key`; Cols: sspr_concept_id, c_bpartner_id, c_period_id, amountconcept, periodno; `SSPR_CONCEPTS2_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_disability` | sspr_disability | — | `SSPR_DISABILITY_C_YEAR` (c_year_id) | ad_client_id→ad_client; ad_org_id→ad_org; c_year_id→c_year | Detalle enlazado a ad_client, ad_org, c_year. | PK `sspr_disability_key`; Cols: c_year_id, description, value_seniors; `SSPR_DISABILITY_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_disabilityline` | sspr_disabilityline | — | — | ad_client_id→ad_client; sspr_disability_id→sspr_disability; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sspr_disability. | PK `sspr_disabilityline_key`; Cols: sspr_disability_id, grade_disability_from, grade_disability_to, percentage, description; `SSPR_DISABILITYLINE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_employeesettlement` | sspr_employeesettlement | — | — | ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `sspr_esettlement_key`; Cols: c_doctype_id, documentno, c_bpartner_id, datetrx, dateout; `SSPR_ESETTLEMENT_ISAC_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_employeesettlementline` | sspr_employeesettlementline | — | — | ad_client_id→ad_client; sspr_concept_id→sspr_concept; sspr_employeesettlement_id→sspr_employeesettlement; ad_org_id→ad_org | Detalle enlazado a ad_client, sspr_concept, sspr_employeesettlement. | PK `sspr_esettlementl_key`; Cols: sspr_concept_id, amount, description, sspr_employeesettlement_id; `SSPR_ESETTLEMENTL_ISAC_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_establishmentcode` | sspr_establishmentcode | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_establishmentcode_id_key`; Cols: value, name, description; `SSPR_ESTABLISHMENTCODE_IACT_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_family` | SSPR_Family | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_location_id→c_location | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_family_key`; Cols: birthday, c_bpartner_id, c_location_id, leavedate, accreditationdoc; `SSPR_FAMILY_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_FAMILY_ISADDRESS_CHK`: ISADDRESS IN ('Y', 'N') (+1) |
| `sspr_formulary107` | sspr_formulary107 | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_year_id→c_year | Detalle enlazado a ad_client, ad_org, c_year. | PK `sspr_formulary107_key`; Cols: c_year_id, observations; `SSPR_FORMULARY107_ISACT_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_formularyline107` | sspr_formularyline107 | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_codeformulary107_id→sspr_codeformulary107; sspr_formulary107_id→sspr_formulary107; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, ad_org, sspr_codeformulary107. | PK `sspr_formularyline107_key`; Cols: sspr_formulary107_id, c_bpartner_id, sspr_codeformulary107_id, amount; `SSPR_FORMULARYLINE107_ISACT_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_general_param_payroll` | sspr_general_param_payroll | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_gparam_payroll_key`; Cols: processing_by_costcenter; `SSPR_GPARAM_PRLL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_GPARAM_PRLL_PBCC_CHK`: PROCESSING_BY_COSTCENTER IN ('Y', 'N') |
| `sspr_holiday` | sspr_holiday | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_holiday_id_key`; Cols: name, value, description, modified_date, annually; `SSPR_HOLIDAY_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_hours_work` | sspr_hours_work | — | `SSPR_NAME` (name) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_hours_work_key`; Cols: hours, name, value, daysmonth, full_time_hours; `SSPR_HOURS_WORK_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_iessrate` | sspr_iessrate | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_iessrate_id_key`; Cols: name, value; `SSPR_IESSRATE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_iessrateline` | sspr_iessrateline | — | — | sspr_iessrate_id→sspr_iessrate; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sspr_iessrate. | PK `sspr_iessrateline_key`; Cols: sspr_iessrate_id, validfrom, validto, value; `SSPR_IESSRATELINE_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_incometax` | sspr_incometax | — | `SSPR_INCOMETAX_VALUE_UN` (value) | ad_client_id→ad_client; ad_org_id→ad_org; c_year_id→c_year | Detalle enlazado a ad_client, ad_org, c_year. | PK `sspr_incometax_key`; Cols: name, value, c_year_id, startdate, enddate; `SSPR_INCOMETAX1_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_incometaxline` | sspr_incometaxline | — | — | ad_client_id→ad_client; sspr_incometax_id→sspr_incometax; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sspr_incometax. | PK `sspr_incometaxline_key`; Cols: basemin, basemax, taxamount, percentajetax, sspr_incometax_id; `SSPR_INCOMETAXLINE_ISACT`: ISACTIVE IN ('Y', 'N') |
| `sspr_incometotal` | sspr_incometotal | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_year_id→c_year; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, ad_org, c_year. | PK `sspr_incometotal_key`; Cols: c_year_id, c_bpartner_id, totalin, totaliess, totaldeductible; `SSPR_CONCEPTS1_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_INCOMETOTAL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_labor_regime` | SSPR_Labor_Regime | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_labor_regime_key`; Cols: name, description, vacationdays, vacationdays_add; `SSPR_LABOR_REGIME_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_labor_regime_detail` | SSPR_Labor_Regime_Detail | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_month_id→ad_month; sspr_labor_regime_id→sspr_labor_regime | Detalle enlazado a ad_client, ad_month, ad_org. | PK `sspr_labor_regime_detail_key`; Cols: startdate, enddate, vacations, sspr_labor_regime_id, ad_month_id; `SSPR_REGIME_DETAIL_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_category` | sspr_leave_category | — | — | sspr_concept_id→sspr_concept; ad_client_id→ad_client; sspr_leave_type_id→sspr_leave_type; ad_org_id→ad_org | Detalle enlazado a ad_client, sspr_concept, sspr_leave_type. | PK `sspr_leave_category_key`; Cols: value, name, sspr_leave_type_id, description, specs; `SSPR_LEAVE_CATEGORY_CHGPAY_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_LEAVE_CATEGORY_ISACTI_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_conf_default` | sspr_leave_conf_default | — | — | ad_client_id→ad_client; c_bpartner_id→c_bpartner; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_leave_conf_default_key`; Cols: c_bpartner_id, isdefault_approver; `SSPR_LEAVE_CONF_DEFAULT_ACT_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_emp` | SSPR_Leave_Emp | `SSPR_LEAVEDELETE_TRG`; `SSPR_LEAVEVALIDATEVAC_TRG1` | — | authorizer_id→c_bpartner; c_costcenter_id→c_costcenter; c_city_id→c_city; ad_client_id→ad_client; current_user_id→c_bpartner (+7) | Detalle enlazado a c_bpartner, c_city, c_costcenter. Validado por trigger(s): SSPR_LEAVEDELETE_TRG, SSPR_LEAVEVALIDATEVAC_TRG1. | PK `sspr_leaveemp_key`; Cols: stardate, enddate, description, status, sspr_leave_type_id; `SSPR_LEAVEEMP_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_emp_details` | sspr_leave_emp_details | — | — | ad_client_id→ad_client; sspr_leave_emp_id→sspr_leave_emp; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sspr_leave_emp. | PK `sspr_leave_emp_details_key`; Cols: sspr_leave_emp_id, description; `SSPR_LEAVE_EMP_DETAIL_ISACT_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_emp_mant` | sspr_leave_emp_mant | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_leave_type_id→sspr_leave_type | Detalle enlazado a ad_client, ad_org, sspr_leave_type. | PK `sspr_leave_emp_mant_key`; Cols: revision, writtenby, approbedby, identificaction, sgi; `SSPR_LEAVE_EMP_MANT_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_emp_notes` | sspr_leave_emp_notes | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_leave_type_id→sspr_leave_type | Detalle enlazado a ad_client, ad_org, sspr_leave_type. | PK `sspr_leave_emp_notes_key`; Cols: sspr_leave_type_id, note; `SSPR_LEAVE_EMP_NOTES_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_emp_vac` | sspr_leave_emp_vac | — | — | ad_client_id→ad_client; sspr_leave_emp_id→sspr_leave_emp; ad_org_id→ad_org; sspr_vacations_id→sspr_vacations | Detalle enlazado a ad_client, ad_org, sspr_leave_emp. | PK `sspr_leave_emp_vac_key`; Cols: sspr_leave_emp_id, sspr_vacations_id, startdate, enddate, nodays; `SSPR_LEAVE_EMP_VAC_ID_ISACT_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_group` | sspr_leave_group | — | — | sspr_concept_id→sspr_concept; ad_client_id→ad_client; sspr_leave_emp_id→sspr_leave_emp; ad_org_id→ad_org; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, sspr_concept, sspr_leave_emp. | PK `sspr_leave_group_key`; Cols: c_bpartner_id, currentsalary, stardate, enddate, percentage_company; `SSPR_LEAVE_GROUP_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_hr_management` | sspr_leave_hr_management | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sspr_leave_type_id→sspr_leave_type | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_leave_management_key`; Cols: sspr_leave_type_id, c_bpartner_id, description; `SSPR_LEAVE_MANAGEMENT_ISACT_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_leave_type` | sspr_leave_type | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_leave_type_key`; Cols: name, value, description, add_to_vacancies, nodays; `SSPR_ISACTIVE1_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_level_ed` | sspr_level_ed | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_level_ed_key`; Cols: name, description, identificador; `SSPR_LEVEL_ED_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_line_loans` | sspr_line_loans | `SSPR_LOANS_TRG` | — | sspr_loans_id→sspr_loans; c_period_id→c_period; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, c_period, sspr_loans. Validado por trigger(s): SSPR_LOANS_TRG. | PK `sspr_lineloans_key`; Cols: line, paydate, amount, status, sspr_loans_id; `SSPR_LINELOANSISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_MANUAL_CANCELLATION`: MANUAL_CANCELLATION IN ('Y', 'N') |
| `sspr_loans` | sspr_loans | — | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; sspr_concept_id→sspr_concept; ad_org_id→ad_org; sspr_typeguarantor_id→sspr_typeguarantor | Detalle enlazado a ad_client, c_bpartner, sspr_concept. | PK `sspr_loans_id_key`; Cols: c_bpartner_id, previous_balance, requestdate, amount, interest; `SSPR_LOANS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_LOANS_PROCESSING`: PROCESSING IN ('Y', 'N') |
| `sspr_occupation` | SSPR_Occupation | — | `SSPR_OCCUPATION_NAME_UQ` (name) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_occupation_key`; Cols: pdtcode, name, description; `SSPR_OCCUPATION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_other_tax_income` | sspr_other_tax_income | — | — | ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `sspr_oti_key`; Cols: c_doctype_id, documentno, description, processed, process_date; `SSPR_OTI_ISACTIVE`: ISACTIVE IN ('Y', 'N'); `SSPR_OTI_PROCESSED`: PROCESSED IN ('Y', 'N') |
| `sspr_other_tax_income_line` | sspr_other_tax_income_line | — | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; sspr_concept_id→sspr_concept; ad_org_id→ad_org; sspr_other_tax_income_id→sspr_other_tax_income | Detalle enlazado a ad_client, c_bpartner, sspr_concept. | PK `sspr_otil_key`; Cols: sspr_other_tax_income_id, c_bpartner_id, taxid, sspr_concept_id, amount; `SSPR_OTIL_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `sspr_payroll` | SSPR_Payroll | `SSPR_VALIDATEPAYROLL_TRG` | `SSPR_JOURNAL_UNIQUE` (gl_journalbatch_id); `SSPR_PAYROLL_DOCUMENTNO_UN` (documentno) | ad_client_id→ad_client; ad_org_id→ad_org; c_period_id→c_period; c_doctype_id→c_doctype; gl_journalbatch_id→gl_journalbatch (+1) | Detalle enlazado a ad_client, ad_org, c_period. Validado por trigger(s): SSPR_VALIDATEPAYROLL_TRG. | PK `sspr_payroll_key`; Cols: documentno, datedoc, c_period_id, processed, description; `SSPR_PAYROLL_AUT_PROC_CHK`: AUTOMATICPROCESS IN ('Y', 'N'); `SSPR_PAYROLL_COMLIQ_CHK`: COMPLETE_LIQUIDATION IN ('Y', 'N') (+1); idx `SSPR_PAYROLL_PERIOD` (c_period_id) |
| `sspr_payroll_aut` | sspr_payroll_aut | `SSPR_PAYROLL_AUT_CREATE_TRG`; `SSPR_VALIDATEPAYROLL_AUT_TRG` | `SSPR_PAYROLL_AUT_DOCUMENTNO` (documentno) | ad_client_id→ad_client; ad_org_id→ad_org; c_period_id→c_period | Detalle enlazado a ad_client, ad_org, c_period. Validado por trigger(s): SSPR_PAYROLL_AUT_CREATE_TRG, SSPR_VALIDATEPAYROLL_AUT_TRG. | PK `sspr_payroll_aut_key`; Cols: documentno, datedoc, c_period_id, processed, description; `SSPR_PAYROLL_AUT_COMLIQ_CHK`: COMPLETE_LIQUIDATION IN ('Y', 'N'); `SSPR_PAYROLL_AUT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') (+1) |
| `sspr_payroll_aut_line` | sspr_payroll_aut_line | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_payroll_aut_id→sspr_payroll_aut; sspr_payroll_id→sspr_payroll | Detalle enlazado a ad_client, ad_org, sspr_payroll_aut. | PK `sspr_payroll_aut_line_key`; Cols: sspr_payroll_aut_id, documentno, sspr_payroll_id, ispayroll, isliquidation; `SSPR_PAYROLL_AUT_ACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_payroll_emp` | sspr_payroll_emp | — | `SSPR_PAYROLL_EMP_UNIQUE` (sspr_payroll_id, c_bpartner_id) | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sspr_payroll_id→sspr_payroll; sspr_contract_id→sspr_contract | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_payroll_emp_key`; Cols: sspr_payroll_id, c_bpartner_id, sspr_contract_id, liquidated; `SSPR_PAYROLL_EMP_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_PAYROLL_EMP_LIQ_CHK`: LIQUIDATED IN ('Y', 'N'); idx `SSPR_PAYEMP_PAYROLL` (sspr_payroll_id) |
| `sspr_payroll_ticket` | SSPR_Payroll_Ticket | — | `SSPR_PAYROLL_TICKET_UN` (sspr_payroll_id, c_bpartner_id) | c_bpartner_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org; sspr_payroll_id→sspr_payroll | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_payroll_ticket_key`; Cols: sspr_payroll_id, c_bpartner_id, totalincome, totalexpense, totalnet; `SSPR_PAYROLL_TICKET_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSPR_PAYROLL_TICKET_COMB1` (c_bpartner_id); idx `SSPR_PAYROLL_TICKET_COMB2` (sspr_payroll_id) |
| `sspr_payroll_ticket_concept` | SSPR_Payroll_Ticket_Concept | `SSPR_PAYROLL_TICK_CONCEPT_TRG` | `SSPR_PAYROLL_TICKET_CONCEPT_UN` (sspr_payroll_ticket_id, sspr_concept_id) | ad_client_id→ad_client; ad_org_id→ad_org; sspr_concept_id→sspr_concept; sspr_payroll_ticket_id→sspr_payroll_ticket | Detalle enlazado a ad_client, ad_org, sspr_concept. Validado por trigger(s): SSPR_PAYROLL_TICK_CONCEPT_TRG. | PK `sspr_ticket_concept_key`; Cols: sspr_payroll_ticket_id, sspr_concept_id, amount, isincomecalculated, iscumulative; `SSPR_TICKET_CONCEPT_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SSPR_PAYTICKCONCEPT_CONCEPT` (sspr_concept_id); idx `SSPR_PAYTICKCONCEPT_TICKET` (sspr_payroll_ticket_id) |
| `sspr_payrollpayment` | sspr_payrollpayment | — | — | fin_financial_account_id→fin_financial_account; ad_client_id→ad_client; c_doctype_id→c_doctype; c_glitem_id→c_glitem; fin_paymentmethod_id→fin_paymentmethod (+1) | Detalle enlazado a ad_client, c_doctype, fin_financial_account. | PK `sspr_payrollpayment_key`; Cols: fin_paymentmethod_id, fin_financial_account_id, c_doctype_id, c_glitem_id; `SSPR_PAYROLLPAYMENT_ISACTIV_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_pension_system` | SSPR_Pension_System | — | `SSPR_PENSION_SYSTEM_NAME_UQ` (name) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_pension_system_key`; Cols: pdtcode, name, description, value; `SSPR_PENSION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_period` | SSPR_Period | — | `SSPR_PERIOD_UN` (c_period_id, c_bpartner_id) | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_period_id→c_period | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_period_key`; Cols: c_period_id, c_bpartner_id; `SSPR_PERIOD_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_period_concept` | SSPR_Period_Concept | `SSPR_PERIOD_CONCEPT_TRG` | `SSPR_PERIOD_CONCEPT_UN` (sspr_period_id, sspr_concept_id) | ad_client_id→ad_client; ad_org_id→ad_org; sspr_concept_id→sspr_concept; sspr_period_id→sspr_period | Detalle enlazado a ad_client, ad_org, sspr_concept. Validado por trigger(s): SSPR_PERIOD_CONCEPT_TRG. | PK `sspr_period_concept_key`; Cols: sspr_period_id, sspr_concept_id; `SSPR_PERIOD_CONCEPT_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_position` | SSPR_Position | `SSPR_COPYPOSITION_TRG`; `SSPR_DELETEPOSITION_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. Validado por trigger(s): SSPR_COPYPOSITION_TRG, SSPR_DELETEPOSITION_TRG. | PK `sspr_position_key`; Cols: name, description, id_compers; `SSPR_POSITION1_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_process_payroll` | sspr_process_payroll | — | — | ad_client_id→ad_client; sspr_conceptin_id→sspr_concept; sspr_conceptout_id→sspr_concept; ad_org_id→ad_org | Detalle enlazado a ad_client, sspr_concept. | PK `sspr_processpayroll_key`; Cols: line, value, processname, sspr_conceptin_id, sspr_conceptout_id; `SSPR_PROCESSPAYROLL_ISACTCHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_profits` | sspr_profits | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sspr_supplementary_data_id→sspr_supplementary_data; c_year_id→c_year | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_profits_id_key`; Cols: c_bpartner_id, c_year_id, averageincome, livingwage, wagecompensation; `SSPR_PROFITS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_prolltem_lines` | SSPR_prolltem_lines | `SSPR_PROLLTEM_LINES_TRG` | `SSPR_PROLLTEM_LINES_UN` (sspr_prolltemplate_id, sspr_concept_id) | ad_client_id→ad_client; ad_org_id→ad_org; sspr_concept_id→sspr_concept; sspr_prolltemplate_id→sspr_prolltemplate | Detalle enlazado a ad_client, ad_org, sspr_concept. Validado por trigger(s): SSPR_PROLLTEM_LINES_TRG. | PK `sspr_prolltem_lines_key`; Cols: sspr_concept_id, sspr_prolltemplate_id; `SSPR_PROLLTEM_LINES_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_prolltemplate` | SSPR_prolltemplate | — | `SSPR_PROLLTEMPLATE_UN` (name) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_prolltemplate_key`; Cols: name; `SSPR_PROLLTEMPLATE_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_readmissions` | sspr_readmissions | — | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_readmissions_key`; Cols: startdate, enddate, description, type_readmission, c_bpartner_id; `SSPR_READMISSION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_relationship` | SSPR_relationship | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_relationship_key`; Cols: value, name; `SSPR_RELATIONSHIP_ISACTIV_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_renewal_data` | sspr_renewal_data | — | — | ad_client_id→ad_client; sspr_loans_id→sspr_loans; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sspr_loans. | PK `sspr_rd_key`; Cols: sspr_loans_id, amount, time, firstdate; `SSPR_RD_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `sspr_settlement` | sspr_settlement | `SSPR_VALIDATESETTLEMENT_TRG` | — | ad_client_id→ad_client; sspr_contract_id→sspr_contract; c_doctype_id→c_doctype; ad_org_id→ad_org; c_bpartner_id→c_bpartner (+2) | Detalle enlazado a ad_client, c_doctype, sspr_contract. Validado por trigger(s): SSPR_VALIDATESETTLEMENT_TRG. | PK `sspr_settlement_key`; Cols: c_doctype_id, documentno, movementdate, docaction, processed; `SSPR_SETTLEMENT_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_SETTLEMENT_COMPLETE_CHK`: COMPLETE IN ('Y', 'N') |
| `sspr_settlementconfig` | SSPR_SettlementConfig | — | — | ad_client_id→ad_client; sspr_contracttype_id→sspr_contracttype; ad_org_id→ad_org | Parametrización / catálogo de soporte. | PK `sspr_settlement_config_key`; Cols: sspr_contracttype_id, reasonendperiod, description, byinterval, intervalfrom; `SSPR_SETTLEMENT_CONFIG_CHK`: ISACTIVE IN ('Y', 'N'); UNIQUE `SSPR_SETTLEMENTCONFIG_IDX` (sspr_contracttype_id, reasonendperiod, ad_client_id, ad_org_id, byinterval, intervalfrom, intervalto) |
| `sspr_settlementconfigline` | SSPR_SettlementConfigLine | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_benefit_dismissal_id→sspr_benefit_dismissal; sspr_settlementconfig_id→sspr_settlementconfig | Parametrización / catálogo de soporte. | PK `sspr_settlementconfigline_key`; Cols: description, sspr_settlementconfig_id, sspr_benefit_dismissal_id; `SSPR_SETTLCFGLINE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); UNIQUE `SSPR_SETTLEMENTCONFIGLINE_IDX` (sspr_settlementconfig_id, sspr_benefit_dismissal_id) |
| `sspr_settlementdata` | sspr_settlementdata | — | — | ad_client_id→ad_client; sspr_concept_id→sspr_concept; sspr_payroll_id→sspr_payroll; sspr_settlement_id→sspr_settlement; ad_org_id→ad_org | Detalle enlazado a ad_client, sspr_concept, sspr_payroll. | PK `sspr_settlementdata_key`; Cols: sspr_settlement_id, line, sspr_concept_id, amount, qty; `SSPR_SETTLEMENTDATA_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_SETTLEMENTDATA_DIS_CHK`: DISPLAY IN ('Y', 'N') |
| `sspr_settlementline` | sspr_settlementline | — | — | sspr_settlement_id→sspr_settlement; ad_client_id→ad_client; sspr_concept_id→sspr_concept; ad_org_id→ad_org; sspr_payroll_id→sspr_payroll | Detalle enlazado a ad_client, sspr_concept, sspr_settlement. | PK `sspr_settlementline_key`; Cols: sspr_settlement_id, line, sspr_concept_id, amount, qty; `SSPR_SETTLEMENTLINE_DIS_CHK`: DISPLAY IN ('Y', 'N'); `SSPR_SETTLEMENTLINES_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_shift` | SSPR_Shift | — | — | ad_client_id→ad_client; ad_org_id→ad_org; name→sspr_position | Detalle enlazado a ad_client, ad_org, sspr_position. | PK `sspr_shift_key`; Cols: starttime, endtime, islunch, lunchtimemin, lunchtimemax; `SSPR_SHIFT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_SHIFT_ISLUNCH_CHK`: ISLUNCH IN ('Y', 'N') |
| `sspr_supplementary_data` | sspr_supplementary_data | `SSPR_SUPP_DATA_TAXIDBP_TRG`; `SSPR_SUPP_DATA_TAXIDORG_TRG`; `SSPR_SUPP_DATA_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_year_id→c_year | Detalle enlazado a ad_client, ad_org, c_year. Validado por trigger(s): SSPR_SUPP_DATA_TAXIDBP_TRG, SSPR_SUPP_DATA_TAXIDORG_TRG, SSPR_SUPP_DATA_TRG. | PK `sspr_supplementary_data_key`; Cols: c_year_id, taxid_company, taxid_partner, name, surname; `SSPR_SUPP_DATA_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_typeguarantor` | sspr_typeguarantor | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_typeguarantor_key`; Cols: name, value, code; `SSPR_TYPEGUARANTOR_ISACTIV_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_typeguarantorline` | sspr_typeguarantorline | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_typeguarantor_id→sspr_typeguarantor | Detalle enlazado a ad_client, ad_org, sspr_typeguarantor. | PK `sspr_typeguarantorl_key`; Cols: requirements, value, sspr_typeguarantor_id; `SSPR_TYPEGUARANTORL_ISACTIV_CK`: ISACTIVE IN ('Y', 'N') |
| `sspr_utilities` | sspr_utilities | — | — | ad_client_id→ad_client; sspr_codeformulary107_id→sspr_codeformulary107; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sspr_supplementary_data_id→sspr_supplementary_data (+1) | Detalle enlazado a ad_client, ad_org, sspr_codeformulary107. | PK `sspr_utilities_key`; Cols: c_bpartner_id, c_year_id, averageincome, livingwage, wagecompensation; `SSPR_UTILITIES_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_utility_detail` | sspr_utility_detail | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_year_id→c_year | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspr_utility_detail_id`; Cols: c_year_id, c_bpartner_id, startdate, enddate, days_worked; `SSPR_UDETAIL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_vacations` | sspr_vacations | `SSPR_VACATIONS_VAL_ADIC_TRG` | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org; sspr_concept_id→sspr_concept; sspr_contract_id→sspr_contract (+2) | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SSPR_VACATIONS_VAL_ADIC_TRG. | PK `sspr_vacancies_id_key`; Cols: c_bpartner_id, entrydate, end_date, nodays, nodaystomados; `SSPR_VACANCY_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPR_VACATIONS_STARTBAL`: STARTINGBALANCE IN ('Y', 'N') (+1) |
| `sspr_valuesindicesperiod` | sspr_valuesindicesperiod | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_year_id→c_year | Detalle enlazado a ad_client, ad_org, c_year. | PK `sspr_valuesindicesperiod_id`; Cols: c_year_id, utilities_years, employee_participation, utility_employee, utility_loads; `SSPR_VALINDPER_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspr_work_week` | sspr_work_week | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspr_work_week_key`; Cols: name, description, monday, tuesday, wednesday; `SSPR_WORK_WEEK_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sspr_acctledger` |
| `sspr_actuarial_calc_study` |
| `SSPR_Asientonomina` |
| `SSPR_Asientonomina_prov` |
| `sspr_attendance` |
| `sspr_bank` |
| `sspr_benefit_dismissal` |
| `SSPR_Calculation_Concepts` |
| `SSPR_Category` |
| `sspr_category_acct` |
| `sspr_codeformulary107` |
| `SSPR_Concept` |
| `sspr_concept_acct` |
| `SSPR_Concept_Amount` |
| `sspr_configurationutility` |
| `SSPR_Contract` |
| `SSPR_Contract_Position` |
| `SSPR_ContractType` |
| `sspr_costdeductiblemax` |
| `sspr_costemployee` |
| `sspr_costemployeeline` |
| `sspr_cumulativeconcept` |
| `sspr_disability` |
| `sspr_disabilityline` |
| `sspr_employeesettlement` |
| `sspr_employeesettlementline` |
| `sspr_establishmentcode` |
| `SSPR_Family` |
| `sspr_formulary107` |
| `sspr_formulary107_detail_v` |
| `sspr_formularyline107` |
| `sspr_general_param_payroll` |
| `sspr_holiday` |
| `sspr_hours_work` |
| `sspr_iessrate` |
| `sspr_iessrateline` |
| `sspr_incometax` |
| `sspr_incometaxline` |
| `sspr_incometotal` |
| `SSPR_Labor_Regime` |
| `SSPR_Labor_Regime_Detail` |
| `sspr_leave_category` |
| `sspr_leave_conf_default` |
| `SSPR_Leave_Emp` |
| `sspr_leave_emp_details` |
| `sspr_leave_emp_mant` |
| `sspr_leave_emp_notes` |
| `sspr_leave_emp_vac` |
| `sspr_leave_group` |
| `sspr_leave_hr_management` |
| `sspr_leave_type` |
| `sspr_level_ed` |
| `sspr_line_loans` |
| `sspr_loans` |
| `SSPR_Occupation` |
| `sspr_other_tax_income` |
| `sspr_other_tax_income_line` |
| `SSPR_Payroll` |
| `sspr_payroll_aut` |
| `sspr_payroll_aut_line` |
| `sspr_payroll_emp` |
| `SSPR_Payroll_Ticket` |
| `SSPR_Payroll_Ticket_Concept` |
| `sspr_payrollpayment` |
| `SSPR_Pension_System` |
| `SSPR_Period` |
| `SSPR_Period_Concept` |
| `SSPR_Position` |
| `sspr_process_payroll` |
| `sspr_profits` |
| `SSPR_prolltem_lines` |
| `SSPR_prolltemplate` |
| `sspr_readmissions` |
| `SSPR_relationship` |
| `sspr_renewal_data` |
| `sspr_settlement` |
| `SSPR_SettlementConfig` |
| `SSPR_SettlementConfigLine` |
| `sspr_settlementdata` |
| `sspr_settlementline` |
| `SSPR_Shift` |
| `sspr_supplementary_data` |
| `sspr_typeguarantor` |
| `sspr_typeguarantorline` |
| `sspr_utilities` |
| `sspr_utility_detail` |
| `sspr_vacations` |
| `sspr_valuesindicesperiod` |
| `sspr_work_week` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_CLIENT`, `AD_CLIENTINFO`, `C_ACCTSCHEMA_DEFAULT`, `C_BPARTNER`, `C_BP_BANKACCOUNT`, `C_CITY`, `C_COUNTRY`, `C_GLITEM`, `SFB_PAYROLL_CERTIFICATELIN`, `SFPR_EMPLOYEE_RVE`, `SFPR_EMPLOYEE_SITUATION`, `SFPR_EMPLOYEE_SITUATION2`, `SSHR_POSIT_SUB_TITLE`, `SSHR_SALARY_GRADE`, `SSHR_SKILLS`, `SSPD_PCTDIST_COSTCENTER`, `SSPH_TENTH_SETTLEMENT`

### Views

`SSPR_COSTEMPLOYEE_V`, `SSPR_CUMULATIVECONCEPT_V`, `SSPR_DATAFORMULARY107_V`, `SSPR_FORMULARY107_DETAIL_V`, `SSPR_FORMULARY107_V`, `SSPR_OTHER_TAX_INCOME_V`, `SSPR_RPT_ASIENTONOMINA`, `SSPR_RPT_ASIENTONOMINA_PRO`, `SSPR_RPT_ASIENTONOMINA_PROV`, `SSPR_SETTLEMENT_V`, `SSPR_TENTH_SETTLEMENT_V`, `SSPR_UTILITYEMPLOYEE_V`

# Functional — windows and menus

## Functional

El módulo se navega a través de diferentes ventanas específicas, tales como 'Aprobación de Permiso' y 'Banco para Nómina', que permiten a los usuarios gestionar sus respectivas áreas de trabajo. Desde la interfaz de usuario, los empleados pueden acceder a formularios para solicitudes de permisos y revisión de conceptos de nómina con facilidad.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.hrm.payroll.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Aprobación de Permiso | Approbation Leave |
| Aprobación de Permiso Empleado | Approbation Leave Employee |
| Aprobación Prestamos | Approbation Loan |
| Asistencia | Attendance |
| Automatic Payroll | Automatic Payroll |
| Banco para Nómina | Bank Payroll |
| Beneficios Despido | Benefits Dismissal |
| Cargo del Empleado | Employee Position |
| Categoria Permiso | Leave Category |
| Categoría Contable | Category Accounting |
| Ciudad del Empleado | Employee City |
| Codigo Formulario | Code Formulary 107 |
| Concepto Laboral | Business Concept |
| Configuración de Liquidaciones | Settlement Config |
| Configuración Proceso de Nonima | Process Payroll Configuration |
| Configuración Utilidades | Configuration of Utility |
| Contabilidad de Nomina | Accounting Ledger Payroll |
| Costo Maximo de Deducible | Cost Deductible Maximum |
| Código de Establecimiento | Establishment Code |
| Datos Adicionales Formulario | Data Formulary 107 |
| Datos Complemtarios | Supplementary Data |
| Discapacidad - mayor | Disability - Senior |
| Días Festivos | Holiday |
| Empleado | Employee |
| Gasto del Empleado | Cost Income Employee |
| Horas Laborables | General Configuration |
| HR Administrador | HR Management |
| Información para el Estudio de Cálculo Actuarial | Information for the Actuarial Calculation Study |
| Liquidación de Empleado | Settlement Employee |
| Liquidación Final | Final Settlement |
| Nivel de Educación | Level Education |
| Notas | Notes |
| Nómina | Payroll |
| Ocupación | Occupation |
| Otros Ingresos Impuesto a la Renta | Other Income Income Tax |
| Pago Nómina | Payroll Payment Out |
| Parámetros Generales Nómina | General Parameters Payroll |
| Plantilla de Nómina | Payroll Template |
| Porcentaje IESS | IESS Rate |
| Relación | Relationship |
| Reportes de Mantenimiento | Maintenance Reports |
| Régimen Laboral | Labor Regime |
| Semana Laboral | Work Week |
| Sistema de Pensiones | Pension System |
| Solicitud de prestamos - Anticipo Pago | Request Loans - Lines - Advance Payment |
| Solicitud de prestamos - Pre-Cancelación | Request Loans - Pre-Cancellation |
| Solicitud Permiso | Request Leave |
| Solicitud Permiso Empleado | Request Leave Employee |
| Solicitud Préstamo | Request Loans |
| Tabla de Impuesto a la Renta | Incometax Table |
| Tipo de Contrato | Contract Type |
| Tipo de Permiso | Leave Type |
| Tipo Garante | Type Guarantor |
| Turno | Shift |
| Usuario de Aprobación por Defecto | User Approval Default |
| Utilidades | Utilities |
| Vacaciones | Vacancies |
| Vacaciones Balance Inicial | Vacations Initial Balance |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Amortización Préstamos | Amortization Loans | No |
| Aprobación de Permiso | Approbation Leave | No |
| Aprobación de Permiso Empleado | Approbation Leave Employee | No |
| Aprobación Prestamos | Approbation Loan | No |
| Archivo de Variación de Extras IESS | IESS Extras Variation File | No |
| Archivo Pago Banco Pichincha TXT | File Payment Pichincha Bank TXT | No |
| Archivo Pago Banco Rumiñahui TXT | Archive Payment Ruminahui Bank TXT | No |
| Archivo Pago Decimos  Produbanco TXT | Archive Payment Tenth Produbanco TXT | No |
| Archivo Pago Utilidades Produbanco TXT | Archive Payment Utilities Produbanco TXT | No |
| Archivo Pagos Banco Produbanco Txt | Archive Payment Produbanco Bank TXT | No |
| Archivo Transferencia Nómina Banco de Guayaquil | Bank of Guayaquil Payroll Transfer File | No |
| Archivo Transferencia Nómina Banco del Austro | Archive Transfer Payroll Austro | No |
| Archivo Transferencia Utilidades del Austro | Archive Transfer Utilites Austro TXT | No |
| Asistencia | Attendance | No |
| Banco | Bank | No |
| Banco para Nómina | Bank Payroll | No |
| Beneficios Despido | Benefits Dismissal | No |
| Calcular Vacaciones | Calculate Vacation | No |
| Cargar Acumulables | Load AcumulativeIn | No |
| Cargar Acumulables | Load AcumulativeIn | No |
| Cargar Concepto Préstamo | Load Concept Loan | No |
| Cargar Plantilla de Nomina | Cargar Plantilla de Nomina | No |
| Cargo del Empleado | Employee Position | No |
| Categoria Permiso | Leave Category | No |
| Categoría Contable | Category Accounting | No |
| Cheque de Pago | Paycheck | No |
| Ciudad del Empleado | Employee City | No |
| Codigo Formulario | Code Formulary 107 | No |
| Concepto Laboral | Business Concept | No |
| Configuración | Setup | Sí |
| Configuración de Liquidaciones | Settlement Config | No |
| Configuración de Utilidad | Configuration of Utility | Sí |
| Configuración Proceso de Nonima | Process Payroll Configuration | No |
| Configuración Utilidades | Configuration of Utility | No |
| Contabilidad de Nomina | Accounting Ledger Payroll | No |
| Copiar Conceptos | Copy Concepts | No |
| Copiar Plantilla | Copy Template | No |
| Costo Detallado de Nómina | Detailed Payroll Cost | No |
| Costo Maximo de Deducible | Cost Deductible Maximum | No |
| Cronograma de Vacaciones | Vacation Schedule | No |
| Código de Establecimiento | Establishment Code | No |
| Datos Adicionales Formulario | Data Formulary 107 | No |
| Datos Complemtarios | Supplementary Data | No |
| Deposito a Banco | Deposit Bank | No |
| Detalle Acumulado Decimo 3ro Resumido por Centro de Costo | Accumulated Detail Thirteenth Summarized by Cost Center | No |
| Detalle Acumulado Decimo 4to Resumido por Centro de Costo | Accumulated Detail Fourteenth Summarized by Cost Center | No |
| Detalle Cargo Concepto | Detail Paid by Concept | No |
| Detalle de Cuotas Prestamos por Centro de Costos | Payment Details Loans by Cost Center | No |
| Detalle de Provisión Vacaciones Resumido por centro de costo | Detail of Vacation Provision Summarized by cost center | No |
| Detalle de Préstamos | Detailed Loans | No |
| Detalle General de Empleados | General Employees Detail | No |
| Detalle General de Nómina | General Payroll Detailed | No |
| Detalle nómina Banco | Payroll Bank Detail | No |
| Discapacidad - mayor | Disability - Senior | No |
| Días Festivos | Holiday | No |
| Eliminar Diario Manual | Delete Manual Journal | No |
| Empleado | Employee | No |
| Estado de Cuenta de Vacaciones por Empleado | Vacation Statement by Employee | No |
| Extras Resumidos | Extras Summarized | No |
| Fondos de Reserva | Reserve Funds | No |
| Formato Décimo Cuarto | 14th Remuneration Format | No |
| Formulario 101 - Gastos Personales | Formulary 101 - Cost Employee | Sí |
| Formulario 107 | Formulary 107 | Sí |
| Gasto del Empleado | Cost Income Employee | No |
| General Report of Family Responsibilities | General Report of Family Responsibilities | No |
| Generar Datos para Asiento Manual | Manual Journal Entries | No |
| Generar Formulario 107 Xml | Generate Formulary 107 Xml | No |
| Generar Impuesto a la Renta | Tax Income | No |
| Generar Quincena | Generate Fortnight | No |
| Generate Formulary 101 - Cost Employee | Generate Formulary 101 - Cost Employee | No |
| Gestión de Nómina | Payroll Management | Sí |
| Herramientas de Análisis | Analysis tools | Sí |
| Herramientas de Análisis | Analysis tools | Sí |
| Herramientas de Análisis | Analysis tools | Sí |
| Herramientas de Análisis | Analysis tools | Sí |
| Herramientas de análisis | Analysis Tools | Sí |
| Herramientas de Análisis | Analysis tools | Sí |
| Herramientas de Análisis Nómina | Herramientas de Análisis payroll | Sí |
| Horas Laborables | General Configuration | No |
| HR Administrador | HR Management | No |
| Importe a Cobrar - RVA | Amounts Receivable - RVA | No |
| Importe a Cobrar Décimo Tercero por categoría de empleado | Amounts Receivable - 13th remuneration for employee category | No |
| Importes a cobrar Décimo Cuarto por categoría de empleado | Amounts Receivable - 14th remuneration for employee category | No |
| Impuesto a la Renta | Income Tax | Sí |
| Información para el Estudio de Cálculo Actuarial | Information for the Actuarial Calculation Study | No |
| Informe de Utilidades | Report of Utilities | No |
| Informe Impuesto a la Renta | Report IncomeTax | No |
| Ingreso por Permanencia | Amounts Receivable - Residence | No |
| Ingresos - Empleados por Categoría | Amounts Receivable - Payroll Employee Category | No |
| Liquidación de Empleado | Settlement Employee | No |
| Liquidación de haberes por proyecto | Salary liquidation by project | No |
| Liquidación Final | Final Settlement | Sí |
| Liquidación Final | Final Settlement | No |
| Modificar Salario CSV | Modify Salary CSV | No |
| Monto total Decimocuarta Bono | Total Amount Fourteenth Bonus | No |
| Nivel de Educación | Level Education | No |
| Notas | Notes | No |
| Nómina | Payroll | No |
| Nómina Automática | Automatic Payroll | No |
| Nómina avanzada Individual | Individual Payroll Advance | No |
| Nómina General | General Payroll | No |
| Nómina General Detallada por Centro de Costo | General Payroll Detailed By Cost Center | No |
| Ocupación | Occupation | No |
| Otros Ingresos Impuesto a la Renta | Other Income Income Tax | No |
| Pago Archivo Banco Central TXT | Archive Payment Central Bank TXT | No |
| Pago Archivo Banco General Rumiñahui Utilidades TXT | Payment Archive BanK General Ruminahui Utilities TXT | No |
| Pago Nómina | Payroll Payment Out | No |
| Pago Nómina | Payroll Payment Out | No |
| Parámetros Generales Nómina | General Parameters Payroll | No |
| Permisos | Payroll Changes | Sí |
| Plantilla base imponible  impuesto a la renta | Taxable Base Income Tax | No |
| Plantilla de Nómina | Payroll Template | No |
| Porcentaje IESS | IESS Rate | No |
| Porcentaje IESS | IESS Rate | No |
| Proceso de Utilidades | Process of Utilities | No |
| Provisiones | Provisions | No |
| Préstamos | Loan | Sí |
| Relación | Relationship | No |
| Reporte Acumulado de Décimo Cuarto | Accumulated Fourteenth Report | No |
| Reporte Acumulado de Décimo Tercero | Accumulated Report of Thirteenth | No |
| Reporte de Fondos de Reserva | Reserve Fund Report | No |
| Reporte de Gastos personales. | Personal expenses report | No |
| Reporte Detallado de Vacaciones | Detailed Vacations | No |
| Reporte Formulario Individual 107 | Report Individual Formulary 107 | No |
| Reporte General del Formulario 107 por mes | Report General Formulary 107 by Month | No |
| Reporte General Formulario 107 | Report General Formulary 107 | No |
| Reporte Pago de Utilidades Banco del Pacifico | Report Utilitis Pacific Bank | No |
| Reporte pago nómina Banco Pacifico | Payment Payroll Pacific Bank | No |
| Reporte Resumen de Vacaciones | Summary Vacations | No |
| Reporte Utilidades CSV | CSV Utilities Report | No |
| Reportes de Mantenimiento | Maintenance Reports | No |
| Rerpote de Vacaciones tomadas por centro de costos | Rerpot of Vacation taken by cost center | No |
| Resumen Definitivo de Liquidación | Definitive Summary of Liquidation | No |
| Rol Empleados - Firmas | Payroll Firms | No |
| Rol Individual - Nómina Fondos de Reserva | Individual Payroll Reserve Funds | No |
| Rol Mensual Detallado | Detailed Monthly Role | No |
| Régimen Laboral | Labor Regime | No |
| Semana Laboral | Work Week | No |
| Sistema de Pensiones | Pension System | No |
| Solicitud Permiso | Request Leave | No |
| Solicitud Permiso Empleado | Request Leave Employee | No |
| Solicitud Préstamo | Request Loans | No |
| Tabla de Impuesto a la Renta | Incometax Table | No |
| Tipo de Contrato | Contract Type | No |
| Tipo de Permiso | Leave Type | No |
| Tipo Garante | Type Guarantor | No |
| Transacciones | Transactions | Sí |
| Transacciónes | Transactions | Sí |
| Turno | Shift | No |
| Usuario de Aprobación por Defecto | User Approval Default | No |
| Utilidades | Utilities | No |
| Vacaciones | Vacations | Sí |
| Vacaciones | Vacancies | No |
| Vacaciones Balance Inicial | Vacations Initial Balance | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.hrm.payroll.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Aprobación de Permiso

- **AD_WINDOW_ID:** `EADFCC9FB0D04E088F50393A47E721B1`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Approbation Leave | `881B6BC8F33E49168898C1FB4994099F` | 0 |
| 20 | Lines | `AA708C757AE4416E8544C72E1EF378C1` | 1 |

### Ventana: Aprobación de Permiso Empleado

- **AD_WINDOW_ID:** `1143BE455E91420CB1DFE4AA45EC8566`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Approbation Leave Employee | `881B6BC8F33E49168898C1FB4994099F` | 0 |

### Ventana: Aprobación Prestamos

- **AD_WINDOW_ID:** `46823D326B7044E58ABA3B846E703527`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Approbation Loan | `DBD54B8529D345B6B39AFE917AB5E7D9` | 0 |

### Ventana: Asistencia

- **AD_WINDOW_ID:** `04B8228FD924498CA75F9A5345DF52D8`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Attendance | `B554CB4729A7474695657BA0A0CBED2D` | 0 |

### Ventana: Automatic Payroll

- **AD_WINDOW_ID:** `9014CCFBDDB6435797D2D1DA812EBFE5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Automatic Payroll | `229B5839EF644ACA88C94BCA39A39C02` | 0 |
| 20 | Lines | `FE357DB5305D43E7A2964D5D0BB1F589` | 1 |

### Ventana: Banco para Nómina

- **AD_WINDOW_ID:** `1F8907EAEB434D349C3DCE6DDC4F2039`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Bank Payroll | `A4F06B1F4507489E9DE6589772A26449` | 0 |

### Ventana: Beneficios Despido

- **AD_WINDOW_ID:** `7A6E79662D734841ACE3A89DB176DA7D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Benefits Dismissal | `A02B2BE3E6E24E1EB1FD1CDA05E5F289` | 0 |

### Ventana: Cargo del Empleado

- **AD_WINDOW_ID:** `194D2400BBD04DD686742CF5864E0D5A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Employee Position | `DB8A4A9751C14760BC1FB098273D6E63` | 0 |

### Ventana: Categoria Permiso

- **AD_WINDOW_ID:** `929DD94061E74272A4A7CCAFED257895`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Leave Category | `5DB2715749FF4529BE31E9B4A15E2A2D` | 0 |

### Ventana: Categoría Contable

- **AD_WINDOW_ID:** `7A170208A97145AF90EA701A432BF894`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Category Accounting | `01D540CE3FD34CAAB4214AD25F88A167` | 0 |

### Ventana: Ciudad del Empleado

- **AD_WINDOW_ID:** `FA48BF58C32A4FB48450D660568DFC5D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Employee City | `186` | 0 |

### Ventana: Codigo Formulario

- **AD_WINDOW_ID:** `962FD827B06746D79F4DD567F0040E87`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Code Formulary 107 | `E80C6E90118E4C658091927DD10BDC33` | 0 |

### Ventana: Concepto Laboral

- **AD_WINDOW_ID:** `D0D450C8478F4586B4CDD0F71844B266`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Business Concept | `2DC9C7FD76B047CB9911B38976CF2C0F` | 0 |
| 20 | Amount | `44CAAE74D1B9402591A85F7FF01F35AF` | 1 |
| 30 | Accounting | `10C9CDDF05404952B50E0EF1B35CDC65` | 1 |

### Ventana: Configuración de Liquidaciones

- **AD_WINDOW_ID:** `877419E7823745428B4A764F7BFF0BB2`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Settlement Config | `D9283CF705E644778BD21FF93CF4637E` | 0 |
| 20 | Benefits by Settlement | `12A742E7531043589E0B1A4CD8344BBE` | 1 |

### Ventana: Configuración Proceso de Nonima

- **AD_WINDOW_ID:** `BAEC3A5A06EA40E58BB09D20E163678A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Process Payroll Configuration | `398CAD37AF984573AE2410A09F50DBF5` | 0 |

### Ventana: Configuración Utilidades

- **AD_WINDOW_ID:** `BD9218C2B3C74D52B4EB87277FAFE756`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Configuration of Utility | `B224A5F50A3A40C5972869F4B203F4BF` | 0 |

### Ventana: Contabilidad de Nomina

- **AD_WINDOW_ID:** `F7D1ACD34B6A452F842D6195A7817E80`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Accounting Ledger | `F45F6FD6232A435195C2929A13D4F38D` | 0 |

### Ventana: Costo Maximo de Deducible

- **AD_WINDOW_ID:** `1B9554354EA141D0B8C580EB29444A4E`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Cost Deductible Maximum | `AB41AA6B80994DA980B06D151068DE7F` | 0 |

### Ventana: Código de Establecimiento

- **AD_WINDOW_ID:** `B9807B90EE15446D94A35246FEB311B5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Establishment Code | `5646115C73474BEE8B0B375778FA1FD9` | 0 |

### Ventana: Datos Adicionales Formulario

- **AD_WINDOW_ID:** `8C84412AF2B54B5D96FF33567CF56765`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Data Formulary 107 | `BCF318E772B946DCA1C73187D45C4E7D` | 0 |
| 20 | Lines | `8E250E224B3F4CE8ACDBD644921FF6D9` | 1 |

### Ventana: Datos Complemtarios

- **AD_WINDOW_ID:** `103715E7CC0040ECA5EABF706E08465B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Supplementary Data | `BA964DC3945D413C941B166045188991` | 0 |

### Ventana: Discapacidad - mayor

- **AD_WINDOW_ID:** `0684DF3266A54685B5D44F58B3558F97`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Disability - Senior | `2BC23D8FE89944199A07C41FB8C6696D` | 0 |
| 20 | Line | `75DF8D4E7C3748DBA3540EFADDA3F432` | 1 |

### Ventana: Días Festivos

- **AD_WINDOW_ID:** `E0DE808C7D494DF1B71001C36B632806`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Holiday | `8C68A945CEA24B00BBE61A36F381E6A9` | 0 |

### Ventana: Empleado

- **AD_WINDOW_ID:** `DB061BED6348461D9D11D24699BDF566`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Employee | `291` | 0 |
| 100 | Period Concept | `A22B37C55C01489EB179FD4C2082674A` | 2 |
| 110 | Readmissions | `F6CBAEA45A8341FBB0C5FC4AF4D31BDD` | 1 |
| 20 | Location/Address | `293` | 1 |
| 30 | Bank Account | `298` | 1 |
| 40 | Employee Accounting | `184` | 1 |
| 50 | Family | `430BB1DC1B49499D88249287FB058A12` | 1 |
| 60 | Contract | `470C94417A3A49B2B742E688B956E5F9` | 1 |
| 70 | Contract Position | `831CEEDC9E254FD182EEEFA5F792F337` | 2 |
| 80 | Category | `920A6EF9B5EE4A3C9DBC1915870DDBBF` | 1 |
| 90 | Period | `011C7C2C206E474F911A4409E2A32C2B` | 1 |

### Ventana: Gasto del Empleado

- **AD_WINDOW_ID:** `0FB688F87DF94081B504A44FD0E936E5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Cost Employee | `DB6B28D0146241E09C3DA351EE0BA030` | 0 |
| 20 | Cost Employee Line | `78733B1D8387473C8B952FC1E48D3774` | 1 |

### Ventana: Horas Laborables

- **AD_WINDOW_ID:** `BF2E9F822F3B4EF1A35516CF2DE4F1C7`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | General Configuration | `FA229FE152584C38B739D63B627BB180` | 0 |

### Ventana: HR Administrador

- **AD_WINDOW_ID:** `4619D6F9A62247F49E7AA6394D9E5976`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | HR Management | `3B2A4C14425242859F13BE4F239BE042` | 0 |

### Ventana: Información para el Estudio de Cálculo Actuarial

- **AD_WINDOW_ID:** `CEE5652AE0F54F97B5EC5B30051D8B96`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `757A2AD82D1541DBB6083E7B2E101184` | 0 |

### Ventana: Liquidación de Empleado

- **AD_WINDOW_ID:** `44D42A180AAF43E6BD44DD66A64A88DE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Settlement Employee | `FDEC8ED00D9C42E9BAB2AE82FDD49230` | 0 |
| 20 | Lines | `D6AB04EC24644B8B957EEE534C6F31B3` | 1 |

### Ventana: Liquidación Final

- **AD_WINDOW_ID:** `3F0BFA1E7F2643CD84E05BA6BDA8220D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Final Settlement | `DC962E28F8E2426DB8C0AD4BF8744B8D` | 0 |
| 100 | Accounting | `270` | 1 |
| 20 | Lines | `691DB9449BB14DEF91E457D65FD3D697` | 1 |
| 30 | Datos Adicionales | `EF01C3BC8D094261BA59750678248834` | 1 |

### Ventana: Nivel de Educación

- **AD_WINDOW_ID:** `3CBD459A24E5498085DA8A3ECB42E664`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Level Education | `E2CABD4363D240CCBACF2F596E04AE25` | 0 |

### Ventana: Notas

- **AD_WINDOW_ID:** `07D83EF8F9BE4A149C5B0C3538E68897`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Notes | `0FDE4ADA74BC45F9BAC577F67C96E487` | 0 |

### Ventana: Nómina

- **AD_WINDOW_ID:** `FD76646320E84CEB8F243C1A6628020B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Payroll | `BCEEDEC4FE2B4B3FAEA32084BB88AD95` | 0 |
| 20 | Payroll Ticket | `6F2D7AFF3DA0466F9C14E84E3E794EB8` | 1 |
| 30 | Payroll Ticket Concept | `3719F273615F4BF287F92E9FA3E0A72C` | 2 |
| 30 | Payroll Employee | `733C9E3E511F4A5E97906CE98DD5EA58` | 1 |

### Ventana: Ocupación

- **AD_WINDOW_ID:** `3A5E2582B61A4A94B6E631649CA1ED9A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Occupation | `A1C36D3250324D33B4EE7F1CF048BC94` | 0 |

### Ventana: Otros Ingresos Impuesto a la Renta

- **AD_WINDOW_ID:** `291FF6CC2B994B60B41829F78F656E2B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `6017C3D7B42348A0A9F2B4FB3C176B86` | 0 |
| 20 | Lines | `F22B5CBD107741E1B109771FF83C8AB3` | 1 |

### Ventana: Pago Nómina

- **AD_WINDOW_ID:** `EAED212D30BE46B9B88C6EDB24A216E5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Payroll Payment Out | `95965F6D8D914BFB84D57571A51FF0FD` | 0 |

### Ventana: Parámetros Generales Nómina

- **AD_WINDOW_ID:** `FCAC4C7A86744CD3B799E47CED821731`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | General Parameters Payroll | `FBDDC669C9A946B9BDC043DFC94FADE3` | 0 |

### Ventana: Plantilla de Nómina

- **AD_WINDOW_ID:** `714825A297144FDEB92747E989131AAD`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Payroll Template | `1B1F09A9B09A41D2A97468CDE88E654F` | 0 |
| 20 | Lines | `8DA7E09E978440C0842F90FEA77BA4E6` | 1 |

### Ventana: Porcentaje IESS

- **AD_WINDOW_ID:** `ACA9176A85C849E09ACE5A2EE9B5E9E6`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | IESS Rate | `820DA5F3F40347E49A7EF50269FFE138` | 0 |
| 20 | Line | `40BD2EBF56714A658DBAD2C1C969F6A8` | 1 |

### Ventana: Relación

- **AD_WINDOW_ID:** `CAC6E0F7DD364487AC3B10E631BA0C25`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Relationship | `D7090277C10A44549DA060670834BC56` | 0 |

### Ventana: Reportes de Mantenimiento

- **AD_WINDOW_ID:** `7E19D2206E02498189B446E7911A0F42`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Maintenance Reports | `42CAA254170D4B3D97658BD343D2736C` | 0 |

### Ventana: Régimen Laboral

- **AD_WINDOW_ID:** `1129B7D3D1564072BF0A964FF3BC2373`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Labor Regime | `F1E01B7A523B4C18A98C3397D2357C8D` | 0 |
| 20 | Detail | `CD8AFC176E944ECABC6986479182A41A` | 1 |

### Ventana: Semana Laboral

- **AD_WINDOW_ID:** `EEB7102B9232427E9568A4D712E268D4`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Work Week | `D80307CAB1784387853DED1BA5487EA3` | 0 |

### Ventana: Sistema de Pensiones

- **AD_WINDOW_ID:** `649C0660C7F1435985485DE60E47F8A5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Pension System | `2CA0603D3B39484C93E829F151F4C024` | 0 |
| 20 | Calculation Concepts | `E08CC7C6294348D680FF3F9C3342803B` | 1 |

### Ventana: Solicitud de prestamos - Anticipo Pago

- **AD_WINDOW_ID:** `60B78202D0DE4AA69AC7589AAF90CC96`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `7AEB59732ADB4559B34076D251BC5CBE` | 0 |

### Ventana: Solicitud de prestamos - Pre-Cancelación

- **AD_WINDOW_ID:** `E3C6EF1C9B9D4EF79DE906F78BEB5711`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `7AEB59732ADB4559B34076D251BC5CBE` | 0 |

### Ventana: Solicitud Permiso

- **AD_WINDOW_ID:** `10EEAB9C1A8845FC8929DABBD7428E26`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Payroll - 0.1.0 - English (USA) 	 Request Leave | `881B6BC8F33E49168898C1FB4994099F` | 0 |
| 20 | Details Activity | `4CEFA6124F6240C581FD8BC53133E8B3` | 1 |

### Ventana: Solicitud Permiso Empleado

- **AD_WINDOW_ID:** `7B87886207A34449813E6D3681D4D34F`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Request Leave Employee | `881B6BC8F33E49168898C1FB4994099F` | 0 |
| 20 | Details Activity | `4CEFA6124F6240C581FD8BC53133E8B3` | 1 |

### Ventana: Solicitud Préstamo

- **AD_WINDOW_ID:** `DC31E6F121DF4D76B896CCE17FF3E699`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Request Loans | `DBD54B8529D345B6B39AFE917AB5E7D9` | 0 |
| 20 | Lines | `7AEB59732ADB4559B34076D251BC5CBE` | 1 |
| 30 | Renewal Data | `EF4AE2F76C8C4B3C8EC40700EA4838BD` | 1 |

### Ventana: Tabla de Impuesto a la Renta

- **AD_WINDOW_ID:** `B260DED991C441F2BA6CDCF219B46C9E`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Income Tax | `F6300094D64F471B83B934E26DD39C3C` | 0 |
| 20 | Income Tax Line | `8F251F2D383B4B7497D7BEA2DD41BAB6` | 1 |

### Ventana: Tipo de Contrato

- **AD_WINDOW_ID:** `0E9C04B2BFF844E2915B2A6B9A2984A2`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Contract Type | `20EE96E48AF145F6BDFF2635179B45D1` | 0 |

### Ventana: Tipo de Permiso

- **AD_WINDOW_ID:** `2F4750D3C32241A086356CBA14CB0AC6`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Leave Type | `4383044C33EF4304B4EB18EEECB34B85` | 0 |

### Ventana: Tipo Garante

- **AD_WINDOW_ID:** `6716BC093980410EA7448794796EB096`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Type Guarantor | `9D9CB47BB107488685E9A9C4CA68D263` | 0 |
| 20 | Lines | `EA1258D7D2064490AACCA9C84D45A1F7` | 1 |

### Ventana: Turno

- **AD_WINDOW_ID:** `B7B5C4841F90478C92050C58056AF912`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Shift | `B1130944B7D04699BCBBD5BFD1110E5B` | 0 |

### Ventana: Usuario de Aprobación por Defecto

- **AD_WINDOW_ID:** `A99BAB814526404CAC239723213874E4`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | User Approval Default | `BFD290FA1E3249508F054570B4B5192E` | 0 |

### Ventana: Utilidades

- **AD_WINDOW_ID:** `AFBC32CD2738417F8F21E9F9D528A57F`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Utilities | `02AC66B9F96949D3B550B558787C866E` | 0 |

### Ventana: Vacaciones

- **AD_WINDOW_ID:** `A11F4A091A3D4ACF9067D711FF4E4AD4`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Vacations | `52EB8F836B014B4D83B4F1CC19612F32` | 0 |

### Ventana: Vacaciones Balance Inicial

- **AD_WINDOW_ID:** `D37DE0EC6E874111A9C7926B2B484510`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Vacations | `52EB8F836B014B4D83B4F1CC19612F32` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Contract (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Empleado | `C_Bpartner_ID` | No | Sí | — |
| 50 | Format Type | `Formattype` | No | No | — |
| 60 | Original Contract | `Contractaddendum_ID` | No | No | — |
| 70 | Labor Regime | `Sspr_Labor_Regime_ID` | No | No | — |
| 80 | Shift | `Sspr_Shift_ID` | No | No | — |
| 90 | Starting Date | `Startdate` | No | No | — |
| 100 | Ending Date | `Enddate` | No | No | — |
| 120 | Contract Condition | `Contractcondition` | No | No | — |
| 130 | Contract Type | `Sspr_Contracttype_ID` | No | No | — |
| 140 | Reason end Labor Relations | `Reasonendperiod` | No | No | — |
| 150 | Night | `Isnight` | No | No | — |
| 160 | Cumulative Regime | `Iscumulativeregime` | No | No | — |
| 170 | Activity | `Activity` | No | No | — |
| 180 | Employee Status | `Employeestatus` | No | No | — |
| 190 | Maximum Working Hours | `Istimemax` | No | No | — |
| 195 | Status Liquidation | `Statusliquidation` | No | No | — |
| 200 | Hours per Week | `Hoursperweek` | No | No | — |
| 210 | Previous Income | `Previousincome` | No | No | 8BA9765D29804923A493AA6C925B77CB |
| 220 | Previous Withholding | `Previouswithholding` | No | No | 8BA9765D29804923A493AA6C925B77CB |
| 230 | Year | `C_Year_ID` | No | No | 8BA9765D29804923A493AA6C925B77CB |
| 240 | Business Concept | `Sspr_Concept_ID` | No | No | 8BA9765D29804923A493AA6C925B77CB |
| 250 | Startdate_Enddate | `Startdate_Enddate` | No | No | — |
| 260 | City | `C_City_ID` | No | No | — |
| 270 | Update Salary | `Update_Salary` | No | No | — |
| 280 | Is Part Time | `Isparttime` | No | No | — |
| 290 | Weekly Hours Part Time | `Weeklyhoursparttime` | No | No | — |
| 300 | 1st Dimension | `User1_ID` | No | No | — |

### Header (ventana: Solicitud de prestamos - Pre-Cancelación)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Line No. | `Line` | No | Sí | — |
| 110 | Manual Cancellation | `Manual_Cancellation` | No | No | — |
| 120 | Paydate | `Paydate` | No | Sí | — |
| 130 | Amount | `Amount` | No | Sí | — |
| 140 | Loan Advance | `Loan_Advance` | No | Sí | — |
| 150 | Total Balance | `Total_Balance` | No | Sí | — |
| 160 | Status | `Status` | No | Sí | — |

### Approbation Loan (ventana: Aprobación Prestamos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `c_bpartner_id` | No | Sí | — |
| 45 | Type Guarantor | `Sspr_Typeguarantor_ID` | No | Sí | — |
| 46 | Guarantor | `Guarantor` | No | Sí | — |
| 50 | Previous Balance | `Previous_Balance` | No | Sí | — |
| 60 | Requestdate | `Requestdate` | No | Sí | — |
| 70 | Amount | `Amount` | No | Sí | — |
| 80 | Time | `Time` | No | Sí | — |
| 90 | Interest | `Interest` | No | Sí | — |
| 100 | Firstdate | `Firstdate` | No | Sí | — |
| 110 | Status | `Status` | No | Sí | — |
| 120 | Description | `Description` | No | No | — |
| 140 | Business Concept | `Sspr_Concept_ID` | No | No | — |
| 190 | Approve Loan | `Completestatus_Approve` | No | No | — |

### Pestaña `051B953930CA4F99937CB644344267EC`

- **AD_TAB_ID:** `051B953930CA4F99937CB644344267EC` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 80 | Boss | `Boss` | No | No | — |

### Header (ventana: Solicitud de prestamos - Anticipo Pago)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Line No. | `Line` | No | Sí | — |
| 110 | Manual Cancellation | `Manual_Cancellation` | No | Sí | — |
| 120 | Paydate | `Paydate` | No | No | — |
| 130 | Amount | `Amount` | No | Sí | — |
| 140 | Loan Advance | `Loan_Advance` | No | Sí | — |
| 150 | Total Balance | `Total_Balance` | No | Sí | — |
| 160 | Status | `Status` | No | Sí | — |

### Category (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Empleado | `C_Bpartner_ID` | No | Sí | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Category | `Category` | No | No | — |
| 80 | Type of Employee | `Employeetype` | No | No | — |
| 90 | Occupation | `Sspr_Occupation_ID` | No | No | — |
| 100 | ESSALUD Code | `Essaludcode` | No | No | — |
| 110 | Pension System | `Sspr_Pension_System_ID` | No | No | — |
| 120 | Entry Date | `Entrydate` | No | No | — |
| 130 | CUSSP | `Cussp` | No | No | — |
| 140 | Type of Pension | `Pensiontype` | No | No | — |
| 150 | Status of the Worker or Pensioner | `Situation` | No | No | — |
| 160 | RUC | `Ruc` | No | No | — |
| 170 | Suspension Tax Fourth | `Istaxfourth` | No | No | — |
| 180 | Type of Training Method | `Modetype` | No | No | — |
| 190 | Study Center | `Studycenter` | No | No | — |
| 200 | Health Insurance | `Ishealthinsurance` | No | No | — |
| 210 | Responsible Mother | `Isresponsiblemother` | No | No | — |
| 220 | Night | `Isnight` | No | No | — |
| 230 | Third RUC | `Thirdruc` | No | No | — |

### Vacations (ventana: Vacaciones)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | Sí | — |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | Active | `Isactive` | No | Sí | — |
| 40 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 70 | Entrydate | `Entrydate` | No | Sí | — |
| 80 | End Date | `END_Date` | No | Sí | — |
| 85 | Días Ganados | `Earneddays` | No | No | — |
| 85 | Days Vacations | `Nodaysvacations` | No | No | — |
| 90 | Nodaystomados | `Nodaystomados` | No | Sí | — |
| 100 | Nodays | `Nodays` | No | Sí | — |
| 121 | Total Días Ganados Adicionales | `Earneddays_Add` | No | No | — |
| 121 | Additional Days | `Noadditionaldays` | No | No | — |
| 122 | Additional Days Taken | `Noadditionaltomados` | No | Sí | — |
| 123 | Total Additional Days | `Noadditionaltotal` | No | Sí | — |
| 124 | Nodaystotal | `Nodaystotal` | No | Sí | — |
| 125 | Total Días Ganados | `Earneddays_Tot` | No | No | — |
| 130 | Alert Status | `Status` | No | Sí | — |
| 140 | Business Concept | `Sspr_Concept_ID` | No | No | — |
| 160 | Starting Balance | `Startingbalance` | No | Sí | — |
| 170 | Total Value | `Totalvalue` | No | Sí | — |
| 180 | Day  Value | `Dayvalue` | No | Sí | — |
| 190 | Valued Vacations | `Vacationsvalue` | No | Sí | — |
| 200 | Cancel liquidation | `Cancelliquidation` | No | Sí | — |
| 210 | additional_assessment | `additional_assessment` | No | Sí | — |
| 220 | additional_day_value | `additional_day_value` | No | Sí | — |
| 290 | Additional Valued Vacation | `Sspr_Vac_Val_Adic` | No | Sí | — |

### Pestaña `135`

- **AD_TAB_ID:** `135` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 230 | Apply Agreement to Avoid Double Taxation | `EM_Sspr_Applyagreement` | No | No | 87F48CC975124FCCAF1A7B3C623890A5 |
| 240 | Code Residence | `EM_Sspr_Coderesidence` | No | No | 87F48CC975124FCCAF1A7B3C623890A5 |

### Pestaña `145`

- **AD_TAB_ID:** `145` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 420 | Manage Budget | `EM_Sspr_Managebudget` | No | No | — |

### Notes (ventana: Notas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Leave Type | `Sspr_Leave_Type_ID` | No | No | — |
| 40 | Comments | `Note` | No | No | — |

### Data Formulary 107 (ventana: Datos Adicionales Formulario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Year | `C_Year_ID` | No | No | — |
| 40 | Observations | `Observations` | No | No | — |

### Pestaña `169`

- **AD_TAB_ID:** `169` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 270 | Accountant | `EM_Sspr_C_Bpartner_ID` | No | No | — |

### Employee Accounting (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Empleado | `—` | No | Sí | — |
| 40 | General Ledger | `—` | No | No | — |
| 50 | Active | `—` | No | No | — |
| 60 | Employee Expenses | `—` | No | No | — |
| 70 | Employee Prepayments | `—` | No | No | — |

### Detail (ventana: Régimen Laboral)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Concept | `Typeconcept` | No | No | — |
| 45 | Month Payroll | `AD_Month_ID` | No | No | — |
| 50 | Vacations | `Vacations` | No | No | — |
| 60 | Starting Date | `Startdate` | No | No | 9EFB2074D9B847A594DE30D052CACBA9 |
| 70 | Ending Date | `Enddate` | No | No | 9EFB2074D9B847A594DE30D052CACBA9 |

### Leave Category (ventana: Categoria Permiso)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Value | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Leave Type | `Sspr_Leave_Type_ID` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Specs | `Specs` | No | No | — |
| 80 | Charged to Payroll | `Charged_Payroll` | No | No | — |
| 90 | Percentage Covered by Company | `Percentage_Company` | No | No | — |
| 100 | Business Concept | `Sspr_Concept_ID` | No | No | — |

### Code Formulary 107 (ventana: Codigo Formulario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | 54DF5E90B1184471ABF20F0C852A5ACD |
| 40 | Name | `Name` | No | No | 54DF5E90B1184471ABF20F0C852A5ACD |
| 60 | Type Concept Formulary | `Typeconcept` | No | No | — |

### Pestaña `1AEAAD595A9145DA8A94E3B0FB9C18C0`

- **AD_TAB_ID:** `1AEAAD595A9145DA8A94E3B0FB9C18C0` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 185 | IESS Rate | `EM_Sspr_Iessrate_ID` | No | No | — |
| 260 | Discapacitado | `EM_Sspr_Isdisabled` | No | No | — |
| 270 | Porcentaje de Discapacidad | `EM_Sspr_Disability` | No | No | — |

### Employee City (ventana: Ciudad del Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | No | — |
| 30 | Country | `—` | No | No | — |
| 40 | Region | `—` | No | No | — |
| 50 | Search Key | `EM_Sspr_Value` | No | No | — |
| 60 | Name | `—` | No | No | — |

### Calculation Concepts (ventana: Sistema de Pensiones)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Pension System | `Sspr_Pension_System_ID` | No | Sí | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Rate | `Rate` | No | No | — |

### Pestaña `220`

- **AD_TAB_ID:** `220` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 380 | Level | `—` | No | No | — |

### Pestaña `2216F9BAFB204D168BD03E11AE1D9E13`

- **AD_TAB_ID:** `2216F9BAFB204D168BD03E11AE1D9E13` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 92 | Concept | `EM_Sspr_Concept_ID` | No | No | — |

### Pestaña `225`

- **AD_TAB_ID:** `225` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | ID Compers | `EM_Sspr_Compers_ID` | No | Sí | — |

### Employee Position (ventana: Cargo del Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | ID Compers | `ID_Compers` | No | Sí | — |

### Pestaña `252`

- **AD_TAB_ID:** `252` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 680 | Debit | `EM_Sspr_C_Debit_Acct` | No | No | 7D6DF1A86E64426F9E9BEC4356D9BDE7 |
| 690 | Credit | `EM_Sspr_C_Credit_Acct` | No | No | 7D6DF1A86E64426F9E9BEC4356D9BDE7 |
| 700 | Closing | `EM_Sspr_C_Closing_Acct` | No | No | 7D6DF1A86E64426F9E9BEC4356D9BDE7 |

### Bank Account (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Empleado | `—` | No | Sí | — |
| 45 | Bank Transfer | `—` | No | No | — |
| 50 | Account Type | `—` | No | No | — |
| 60 | Country | `—` | No | No | — |
| 70 | Routing No | `—` | No | No | — |
| 80 | Generic Account No. | `—` | No | No | — |
| 90 | Use Generic Account No. | `—` | No | No | — |
| 100 | IBAN | `—` | No | No | — |
| 110 | Use IBAN | `—` | No | No | — |
| 120 | CC Type | `—` | No | No | — |
| 130 | Credit Card No. | `—` | No | No | — |
| 140 | Expiry Month | `—` | No | No | — |
| 150 | Expiry Year | `—` | No | No | — |
| 160 | Name | `—` | No | No | — |
| 170 | Street | `—` | No | No | — |
| 180 | City | `—` | No | No | — |
| 190 | Postal Code | `—` | No | No | — |
| 200 | State | `—` | No | No | — |
| 210 | Banco | `EM_Sspr_Bank_ID` | No | No | — |
| 220 | Is payroll | `EM_Sspr_Ispayroll` | No | No | — |

### Lines (ventana: Liquidación Final)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | Sí | — |
| 40 | Line No. | `Line` | No | No | — |
| 50 | Business Concept | `Sspr_Concept_ID` | No | No | — |
| 60 | Amount | `Amount` | No | No | — |
| 70 | Quantity | `Qty` | No | No | — |
| 80 | Total Net | `Totalnet` | No | No | — |
| 140 | Description | `Description` | No | No | — |

### Payroll Payment Out (ventana: Pago Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 40 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 50 | Document Type | `C_Doctype_ID` | No | No | — |
| 60 | G/L Item | `C_Glitem_ID` | No | No | — |

### Automatic Payroll (ventana: Automatic Payroll)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document No. | `Documentno` | No | No | — |
| 40 | Document Date | `Datedoc` | No | No | — |
| 50 | Period | `C_Period_ID` | No | No | — |
| 60 | Automatic Payroll Process Class | `Processed` | No | No | — |
| 100 | Description | `Description` | No | No | — |

### Lines (ventana: Liquidación de Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Business Concept | `Sspr_Concept_ID` | No | No | — |
| 40 | Amount | `Amount` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Pestaña `35FEEDC0BF8F4AF49303BB0B60B35DC9`

- **AD_TAB_ID:** `35FEEDC0BF8F4AF49303BB0B60B35DC9` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 70 | Category Accounting | `EM_Sspr_Category_Acct_ID` | No | No | — |

### Settlement Config (ventana: Configuración de Liquidaciones)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Contract Type | `Sspr_Contracttype_ID` | No | No | — |
| 50 | Reason end Labor Relations | `Reasonendperiod` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | By Interval | `Byinterval` | No | No | — |
| 80 | Interval From | `Intervalfrom` | No | No | — |
| 90 | Interval To | `Intervalto` | No | No | — |

### Level Education (ventana: Nivel de Educación)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Identificador | `Identificador` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Relationship (ventana: Relación)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Value | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |

### Request Leave Employee (ventana: Solicitud Permiso Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 25 | Document No. | `Documentno` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `c_bpartner_id` | No | Sí | — |
| 42 | Leave Type | `Sspr_Leave_Type_ID` | No | No | — |
| 45 | Leave Category | `Sspr_Leave_Category_ID` | No | No | — |
| 47 | Specs | `Specs` | No | Sí | — |
| 48 | Details Names | `Details_Names` | No | No | — |
| 50 | Relationship | `Sspr_Relationship_ID` | No | No | — |
| 50 | Date Sinister | `Date_Sinister` | No | No | — |
| 55 | Details Sinister | `Details_Sinister` | No | No | — |
| 55 | Date Death | `Date_Death` | No | No | — |
| 56 | Start Date Absent | `Stardateabsent` | No | No | — |
| 60 | Calculate Start Date | `Stardate` | No | No | — |
| 70 | Calculate End Date | `Enddate` | No | No | — |
| 72 | No. Days available | `Nodays` | No | Sí | — |
| 75 | Start Hour | `Starthour` | No | No | — |
| 78 | End Hour | `Endhour` | No | No | — |
| 80 | Nohours | `Nohours` | No | Sí | — |
| 90 | Add To Vacancies | `ADD_To_Vacancies` | No | No | — |
| 91 | Paid Vacations | `Paid_Vacations` | No | No | — |
| 92 | Type Vacations | `Typevacations` | No | No | — |
| 95 | City | `C_City_ID` | No | No | — |
| 100 | Description | `Description` | No | No | — |
| 130 | Status Request | `Status_Request` | No | No | — |
| 170 | Who Replace | `Whoreplace_ID` | No | No | — |
| 180 | Authorized | `Authorizer_ID` | No | No | — |
| 240 | Oficial Specs | `Oficial_Specs` | No | No | — |
| 280 | Cost Center | `C_Costcenter_ID` | No | Sí | — |
| 300 | Authorized Date | `Authorized_Date` | No | Sí | — |
| 310 | Closed | `Closed` | No | Sí | — |

### General Configuration (ventana: Horas Laborables)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Hours | `Hours` | No | No | — |
| 40 | Type | `Value` | No | No | — |
| 50 | Description | `Name` | No | No | — |
| 60 | Days Month | `Daysmonth` | No | No | — |
| 70 | Full-time hours | `Full_Time_Hours` | No | No | — |

### Cost Employee (ventana: Gasto del Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Year | `C_Year_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 80 | Amount Cost | `Amountcost` | No | Sí | — |

### Cost Deductible Maximum (ventana: Costo Maximo de Deducible)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Year | `C_Year_ID` | No | No | — |
| 40 | Starting Date | `Startdate` | No | No | — |
| 50 | Ending Date | `Enddate` | No | No | — |
| 60 | Deductible Expense | `Deductibleexpense` | No | No | — |
| 70 | Base Max. | `Basemax` | No | No | — |
| 80 | Base Max. Disabled | `Basemaxdisabled` | No | No | — |
| 90 | Base Max. Seniors | `Basemaxseniors` | No | No | — |

### Location/Address (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Empleado | `—` | No | Sí | — |
| 40 | Name | `—` | No | No | — |
| 50 | Active | `—` | No | No | — |
| 60 | Location / Address | `—` | No | No | — |
| 70 | Phone | `—` | No | No | — |
| 80 | Alternative Phone | `—` | No | No | — |
| 90 | Fax | `—` | No | No | — |
| 100 | Tax Location | `—` | No | No | — |

### Lines (ventana: Datos Adicionales Formulario)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Concept Formulary | `Sspr_Codeformulary107_ID` | No | No | — |
| 60 | Amount | `Amount` | No | No | — |

### Benefits by Settlement (ventana: Configuración de Liquidaciones)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Sspr_Benefit_Dismissal_ID | `Sspr_Benefit_Dismissal_ID` | No | No | — |

### Lines (ventana: Otros Ingresos Impuesto a la Renta)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 110 | Tax ID | `Taxid` | No | Sí | — |
| 120 | Business Concept | `Sspr_Concept_ID` | No | No | — |
| 130 | Value | `Amount` | No | No | — |

### Category Accounting (ventana: Categoría Contable)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Value | `Value` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 60 | Balance Account | `Balanceacct_ID` | No | No | — |
| 70 | Clearance Account | `Clearance_Account_ID` | No | No | — |

### Vacations (ventana: Vacaciones Balance Inicial)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 70 | Entrydate | `Entrydate` | No | No | — |
| 80 | End Date | `END_Date` | No | No | — |
| 90 | Days Vacations | `Nodaysvacations` | No | No | — |
| 100 | Nodaystomados | `Nodaystomados` | No | No | — |
| 110 | Nodays | `Nodays` | No | No | — |
| 120 | Additional Days | `Noadditionaldays` | No | No | — |
| 130 | Additional Days Taken | `Noadditionaltomados` | No | No | — |
| 140 | Total Additional Days | `Noadditionaltotal` | No | No | — |
| 150 | Nodaystotal | `Nodaystotal` | No | No | — |
| 160 | Starting Balance | `Startingbalance` | No | Sí | — |
| 170 | Total Value | `Totalvalue` | No | No | — |
| 180 | Day  Value | `Dayvalue` | No | No | — |
| 190 | Valued Vacations | `Vacationsvalue` | No | No | — |
| 210 | Alert Status | `Status` | No | No | — |
| 260 | Business Concept | `Sspr_Concept_ID` | No | No | — |
| 300 | Complete Days | `Completedays` | No | No | — |

### Line (ventana: Discapacidad - mayor)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Grade Disability From | `Grade_Disability_From` | No | No | — |
| 50 | Grade Disability To | `Grade_Disability_To` | No | No | — |
| 60 | Percentage | `Percentage` | No | No | — |
| 70 | Description | `Description` | No | No | — |

### Maintenance Reports (ventana: Reportes de Mantenimiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Revision | `Revision` | No | No | — |
| 40 | Writtenby | `Writtenby` | No | No | — |
| 50 | Approbedby | `Approbedby` | No | No | — |
| 60 | Identificaction | `Identificaction` | No | No | — |
| 70 | Sgi | `Sgi` | No | No | — |
| 80 | Valided | `Valided` | No | No | — |
| 90 | Original | `Original` | No | No | — |
| 100 | Copy | `Copy` | No | No | — |
| 110 | Leave Type | `Sspr_Leave_Type_ID` | No | No | — |

### Holiday (ventana: Días Festivos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Date | `modified_date` | No | No | — |
| 70 | Timeday | `Timeday` | No | No | — |
| 80 | Annually | `Annually` | No | No | — |
| 90 | Description | `Description` | No | No | — |

### Line (ventana: Porcentaje IESS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Date From | `Validfrom` | No | No | — |
| 50 | Date To | `Validto` | No | No | — |
| 60 | Value IESS Rate | `Value` | No | No | — |

### Accounting (ventana: Liquidación Final)

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

### Lines (ventana: Plantilla de Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Payroll Template 1 | `Sspr_Prolltemplate_ID` | No | Sí | — |
| 50 | Business Concept | `Sspr_Concept_ID` | No | No | — |

### Labor Regime (ventana: Régimen Laboral)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 80 | Vacation Days | `Vacationdays` | No | No | — |
| 90 | Additional Vacation Days | `Vacationdays_Add` | No | No | — |

### Payroll - 0.1.0 - English (USA) 	 Request Leave (ventana: Solicitud Permiso)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 25 | Document No. | `Documentno` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `c_bpartner_id` | No | No | — |
| 42 | Leave Type | `Sspr_Leave_Type_ID` | No | No | — |
| 45 | Leave Category | `Sspr_Leave_Category_ID` | No | No | — |
| 47 | Specs | `Specs` | No | Sí | — |
| 48 | Details Names | `Details_Names` | No | No | — |
| 50 | Date Sinister | `Date_Sinister` | No | No | — |
| 50 | Relationship | `Sspr_Relationship_ID` | No | No | — |
| 55 | Details Sinister | `Details_Sinister` | No | No | — |
| 55 | Date Death | `Date_Death` | No | No | — |
| 56 | Start Date Absent | `Stardateabsent` | No | No | — |
| 60 | Calculate Start Date | `Stardate` | No | No | — |
| 70 | Calculate End Date | `Enddate` | No | No | — |
| 72 | No. Days available | `Nodays` | No | No | — |
| 75 | Start Hour | `Starthour` | No | No | — |
| 78 | End Hour | `Endhour` | No | No | — |
| 80 | Nohours | `Nohours` | No | Sí | — |
| 90 | Add To Vacancies | `ADD_To_Vacancies` | No | No | — |
| 91 | Paid Vacations | `Paid_Vacations` | No | No | — |
| 95 | Discount labor day | `Isdiscountlaborday` | No | No | — |
| 95 | City | `C_City_ID` | No | No | — |
| 95 | Type Vacations | `Typevacations` | No | No | — |
| 100 | Description | `Description` | No | No | — |
| 130 | Status Request | `Status_Request` | No | No | — |
| 170 | Who Replace | `Whoreplace_ID` | No | No | — |
| 180 | Authorized | `Authorizer_ID` | No | No | — |
| 240 | Oficial Specs | `Oficial_Specs` | No | No | — |
| 280 | Cost Center | `C_Costcenter_ID` | No | Sí | — |
| 340 | Authorized Date | `Authorized_Date` | No | Sí | — |
| 350 | Closed | `Closed` | No | Sí | — |

### Settlement Employee (ventana: Liquidación de Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `Documentno` | No | No | — |
| 50 | Employee | `C_Bpartner_ID` | No | No | — |
| 60 | Transaction Date | `Datetrx` | No | No | — |
| 70 | Date Out | `Dateout` | No | No | — |
| 80 | Description | `Description` | No | No | — |
| 90 | Generate Settlement Employee | `Processed` | No | No | — |
| 100 | Generate settlement | `Generatesettlement` | No | No | — |

### Work Week (ventana: Semana Laboral)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Monday | `Monday` | No | No | — |
| 60 | Tuesday | `Tuesday` | No | No | — |
| 70 | Wednesday | `Wednesday` | No | No | — |
| 80 | Thursday | `Thursday` | No | No | — |
| 90 | Friday | `Friday` | No | No | — |
| 100 | Saturday | `Saturday` | No | No | — |
| 110 | Sunday | `Sunday` | No | No | — |

### Details Activity (ventana: Solicitud Permiso Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Description | `Description` | No | No | — |

### Income Tax (ventana: Tabla de Impuesto a la Renta)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Year | `C_Year_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Search Key | `Value` | No | No | — |
| 80 | Name | `Name` | No | No | — |
| 90 | Basic Family Basket | `Basic_Family_Basket` | No | No | — |
| 100 | Minimum % to Deduct Expenses | `Min_Perc_Deduct_Expenses` | No | No | — |
| 110 | Maximum % to Deduct Expenses | `Max_Perc_Deduct_Expenses` | No | No | — |

### Payroll (ventana: Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Payroll | `Ispayroll` | No | No | — |
| 50 | Liquidation | `Isliquidation` | No | No | — |
| 50 | Document No. | `DocumentNo` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Period | `C_Period_ID` | No | No | — |
| 80 | Document Date | `DateDoc` | No | No | — |
| 90 | Process Payroll | `Processed` | No | No | — |
| 100 | Journal Batch | `GL_Journalbatch_ID` | No | Sí | — |
| 110 | Posted | `Posted` | No | No | — |
| 120 | Document Type | `C_Doctype_ID` | No | No | — |
| 120 | Automatic Process | `Automaticprocess` | No | Sí | — |

### Bank Payroll (ventana: Banco para Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Code | `Code` | No | No | — |
| 30 | Name of Institution | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Final Settlement (ventana: Liquidación Final)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Type Name | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `Documentnonew` | No | No | — |
| 50 | Movement Date | `Movementdate` | No | No | — |
| 70 | Create Lines Settlement | `Processed` | No | No | — |
| 80 | Employee | `C_Bpartner_ID` | No | No | — |
| 110 | Payroll Liquidation | `Sspr_Payroll_Id_Normal` | No | No | — |
| 120 | Payroll Provision Liquidation | `Sspr_Payroll_Id_Provision` | No | No | — |
| 130 | Description | `Description` | No | No | — |
| 140 | Contract | `Sspr_Contract_ID` | No | No | — |
| 150 | Complete Settlement | `Complete` | No | No | — |
| 160 | Status Payroll | `Status_Payroll` | No | No | — |
| 170 | Posted | `Posted` | No | No | — |

### Pestaña `7E06E1703EC84DDEA1AB2A0E3884181B`

- **AD_TAB_ID:** `7E06E1703EC84DDEA1AB2A0E3884181B` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 105 | Concept Formulary | `EM_Sspr_Codeformulary107_ID` | No | No | — |

### Amount (ventana: Concepto Laboral)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Concept | `Sspr_Concept_ID` | No | Sí | — |
| 50 | Period | `C_Period_ID` | No | No | 9EFB2074D9B847A594DE30D052CACBA9 |
| 60 | Empleado | `C_Bpartner_ID` | No | No | 9EFB2074D9B847A594DE30D052CACBA9 |
| 65 | Hours Amount | `Hoursamt` | No | No | — |
| 70 | Amount | `Amount` | No | No | 9EFB2074D9B847A594DE30D052CACBA9 |
| 80 | Ismodified | `Ismodified` | No | No | — |

### Configuration of Utility (ventana: Configuración Utilidades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Year | `C_Year_ID` | No | No | — |
| 40 | Net Profit | `Netprofit` | No | No | — |
| 50 | Living Wage Value | `Livingwage` | No | No | — |
| 80 | Age limit child | `AGE_Limit_Child` | No | No | — |
| 150 | % Participation Employee | `Perc_Participation_Employee` | No | No | — |
| 160 | % Utility Employee | `Perc_Earnings_Employee` | No | No | — |
| 170 | % Utility Loads | `Perc_Utility_Loads` | No | No | — |
| 230 | Print Type | `Concepttypepayroll` | No | No | — |
| 240 | Concept Formulary | `Sspr_Codeformulary107_ID` | No | No | — |
| 310 | Description | `Description` | No | No | — |
| 320 | Work cocept | `Sspr_Concept_ID` | No | No | — |
| 330 | Period | `C_Period_ID` | No | No | — |
| 340 | Living Wage Month | `Living_Wage_Month` | No | No | — |
| 350 | Month Partial Living Wage | `Month_Partial_Living_Wage` | No | No | — |
| 420 | Income Tax Calculation | `Isincometaxcalculation` | No | No | — |
| 430 | Period | `C_Period_Incometax_ID` | No | No | — |

### Pestaña `800033`

- **AD_TAB_ID:** `800033` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 90 | Payment Thirteenth | `—` | No | No | — |
| 100 | Business Concept | `EM_Sspr_Concept_ID` | No | No | — |

### Benefits Dismissal (ventana: Beneficios Despido)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Line No. | `Line` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 45 | Name | `Name` | No | No | — |
| 50 | Business Concept | `Sspr_Concept_ID` | No | No | — |
| 55 | Monthly Tenth | `Sspr_Concept_Tenth_ID` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Rate | `Rate` | No | No | — |
| 80 | Per Year | `Peryear` | No | No | — |
| 90 | Full Year | `Fullyear` | No | No | — |
| 100 | Max Value | `Maxvalue` | No | No | — |

### Process Payroll Configuration (ventana: Configuración Proceso de Nonima)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Line No. | `Line` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Process Name | `Processname` | No | No | — |
| 80 | Description | `Description` | No | No | — |
| 90 | Concept In | `Sspr_Conceptin_ID` | No | No | — |
| 100 | Concept Out | `Sspr_Conceptout_ID` | No | No | — |

### Type Guarantor (ventana: Tipo Garante)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Code | `Code` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |

### Payroll Template (ventana: Plantilla de Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | 1A66F4FF7D52416E8E80B9C1965592C5 |

### Header (ventana: Información para el Estudio de Cálculo Actuarial)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 100 | Period | `C_Period_ID` | No | No | — |
| 110 | Tax ID | `Taxid` | No | No | — |
| 120 | Name | `Name` | No | No | — |
| 130 | Date Birth | `Date_Birth` | No | No | — |
| 140 | Date Admission | `Date_Admission` | No | No | — |
| 150 | Age | `Age` | No | Sí | — |
| 160 | TS | `TS` | No | No | — |
| 170 | Remuneration | `Remuneration` | No | No | — |
| 180 | Concept | `Concept` | No | No | — |
| 190 | Obligation | `Obligation` | No | No | — |
| 200 | Projected running cost | `Cost` | No | No | — |
| 210 | Projected net interest | `Interest` | No | No | — |
| 220 | Total | `Total` | No | Sí | — |
| 230 | Sex | `Sex` | No | No | — |
| 240 | Status_Actuarial | `Status_Actuarial` | No | No | — |
| 250 | Deferred_Tax_Generation | `Deferred_Tax_Generation` | No | No | — |
| 260 | Deferred_Tax_Reversal | `Deferred_Tax_Reversal` | No | No | — |

### General Parameters Payroll (ventana: Parámetros Generales Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Post by Cost Center | `Processing_By_Costcenter` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |

### Shift (ventana: Turno)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 35 | Search Key | `Value` | No | No | — |
| 36 | Name | `Name_Movement` | No | No | — |
| 40 | Shift Type | `Shifttype` | No | No | — |
| 60 | Starttime | `Starttime` | No | No | — |
| 70 | Endtime | `Endtime` | No | No | — |
| 80 | Entry | `Entry` | No | No | — |
| 90 | Exit | `Exit` | No | No | — |
| 100 | Position | `Name` | No | No | — |
| 110 | Lunch | `Islunch` | No | No | — |
| 120 | Minimun Duration | `Lunchtimemin` | No | No | — |
| 130 | Maximun Duration | `Lunchtimemax` | No | No | — |

### Payroll Ticket (ventana: Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Payroll | `Sspr_Payroll_ID` | No | Sí | — |
| 50 | Empleado | `C_Bpartner_ID` | No | No | — |
| 60 | Total Income | `Totalincome` | No | Sí | 103 |
| 70 | Total Expense | `Totalexpense` | No | Sí | 103 |
| 80 | Total Net | `Totalnet` | No | Sí | 103 |
| 100 | Working Days | `Workingdays` | No | No | 103 |
| 110 | Worked Days | `Workeddays` | No | No | 103 |
| 180 | Disabled | `Disabled` | No | No | 103 |
| 190 | Senior | `Senior` | No | No | 103 |
| 290 | Days Worked Benefits | `Worked_Days_Benefits` | No | Sí | — |
| 300 | Part-time Hours | `Partial_Work_Hours` | No | No | — |

### Establishment Code (ventana: Código de Establecimiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Renewal Data (ventana: Solicitud Préstamo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Amount | `Amount` | No | No | — |
| 110 | Time | `Time` | No | No | — |
| 120 | Firstdate | `Firstdate` | No | No | — |

### Period (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Empleado | `C_Bpartner_ID` | No | Sí | — |
| 50 | Period | `C_Period_ID` | No | No | — |

### Approbation Leave Employee (ventana: Aprobación de Permiso Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 25 | Document No. | `Documentno` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `c_bpartner_id` | No | Sí | — |
| 42 | Leave Type | `Sspr_Leave_Type_ID` | No | Sí | — |
| 45 | Leave Category | `Sspr_Leave_Category_ID` | No | Sí | — |
| 47 | Specs | `Specs` | No | Sí | — |
| 48 | Details Names | `Details_Names` | No | Sí | — |
| 48 | Details Sinister | `Details_Sinister` | No | Sí | — |
| 50 | Date Sinister | `Date_Sinister` | No | Sí | — |
| 50 | Relationship | `Sspr_Relationship_ID` | No | Sí | — |
| 55 | Date Death | `Date_Death` | No | Sí | — |
| 60 | Calculate Start Date | `Stardate` | No | Sí | — |
| 70 | Calculate End Date | `Enddate` | No | Sí | — |
| 72 | No. Days available | `Nodays` | No | Sí | — |
| 75 | Start Hour | `Starthour` | No | Sí | — |
| 78 | End Hour | `Endhour` | No | Sí | — |
| 80 | Nohours | `Nohours` | No | Sí | — |
| 90 | Add To Vacancies | `ADD_To_Vacancies` | No | No | — |
| 91 | Paid Vacations | `Paid_Vacations` | No | Sí | — |
| 100 | Description | `Description` | No | Sí | — |
| 170 | Status Request | `Status_Request` | No | Sí | — |
| 180 | Status Approve | `Status_Approve` | No | Sí | — |
| 200 | Who Replace | `Whoreplace_ID` | No | Sí | — |
| 210 | Authorized | `Authorizer_ID` | No | No | — |
| 270 | Oficial Specs | `Oficial_Specs` | No | Sí | — |
| 320 | Cost Center | `C_Costcenter_ID` | No | Sí | — |
| 340 | Authorized Date | `Authorized_Date` | No | No | — |
| 350 | Closed | `Closed` | No | No | — |
| 360 | Process Reactive | `Process_Reactive` | No | No | — |
| 370 | Approve | `Approved_Status` | No | No | — |

### Header (ventana: Otros Ingresos Impuesto a la Renta)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 0 | Process | `Process` | No | No | — |
| 0 | Load Lines | `Load_Lines` | No | No | — |
| 0 | Reactivate | `Reactivate` | No | No | — |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 100 | Document Type | `C_Doctype_ID` | No | No | — |
| 110 | Document No. | `Documentno` | No | Sí | — |
| 120 | Description | `Description` | No | No | — |
| 130 | Process Date | `Process_Date` | No | No | — |
| 140 | Processed | `Processed` | No | Sí | — |

### Details Activity (ventana: Solicitud Permiso)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Description | `Description` | No | No | — |

### Accounting (ventana: Concepto Laboral)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 50 | Is provision account | `Isaccountpayroll` | No | No | — |
| 60 | General Ledger | `C_Acctschema_ID` | No | No | — |
| 70 | Debit | `C_Debit_Acct` | No | No | — |
| 80 | Credit | `C_Credit_Acct` | No | No | — |
| 90 | Liability | `Isliability` | No | No | — |
| 100 | Ispassiveprovision | `Isaccountcharge` | No | No | — |
| 110 | Isexpend | `Isexpend` | No | No | — |
| 140 | Accounting Category | `Sspr_Category_Acct_ID` | No | No | — |

### Lines (ventana: Aprobación de Permiso)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Leave Employee | `Sspr_Leave_Emp_ID` | No | No | — |
| 40 | Vacations | `Sspr_Vacations_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Nodays | `Nodays` | No | No | — |
| 80 | Amount | `Amount` | No | No | — |

### HR Management (ventana: HR Administrador)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Leave Type | `Sspr_Leave_Type_ID` | No | No | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Employee (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 35 | ID Compers | `EM_Sspr_Compers_ID` | No | Sí | — |
| 40 | Search Key | `—` | No | No | 123 |
| 50 | Status | `EM_SSPR_Status` | No | No | — |
| 60 | Birth of Day | `EM_SSPR_Birthday` | No | No | — |
| 70 | Entry Date | `EM_SSPR_Entrydate` | No | Sí | — |
| 80 | Document Type Name | `EM_SSPR_Documenttype` | No | No | — |
| 90 | Document No | `EM_SSPR_DocumentNo` | No | No | — |
| 100 | Fiscal Name | `—` | No | No | — |
| 104 | First Name | `EM_Sspr_Firstname` | No | No | — |
| 105 | Last Name | `EM_Sspr_Lastname` | No | No | — |
| 106 | Is Passant | `EM_Sspr_Ispassant` | No | No | — |
| 110 | Special Situation | `EM_SSPR_Specialsituation` | No | No | — |
| 130 | Income Frequency | `EM_SSPR_Incomefrequency` | No | No | — |
| 140 | Type of Income | `EM_SSPR_Typeofincome` | No | No | — |
| 150 | Payroll Template 1 | `EM_SSPR_Prolltemplate_ID` | No | No | — |
| 160 | Payroll Template 2 | `EM_SSPR_Prolltemplate2_ID` | No | No | — |
| 170 | Project Employee | `EM_Sspr_Project_ID` | No | No | — |
| 180 | City | `EM_SSPR_City` | No | No | — |
| 190 | Reserve Funds Iess | `em_sspr_reservefundsiess` | No | No | — |
| 206 | Code Ocupational IESS | `EM_Sspr_Cod_Ocupac_Iess` | No | No | — |
| 207 | Blood Type | `—` | No | No | — |
| 209 | License Type | `—` | No | No | — |
| 210 | Concept | `em_sspr_concept_id` | No | No | — |
| 211 | Current Salary | `EM_Sspr_Currentsalary` | No | Sí | — |
| 212 | IESS Rate | `EM_Sspr_Iessrate_ID` | No | No | — |
| 215 | Nivel Instruccion | `EM_Sspr_Level_Ed_ID` | No | No | — |
| 216 | Accounting Category | `EM_Sspr_Category_Acct_ID` | No | No | — |
| 217 | Discapacitado | `EM_Sspr_Isdisabled` | No | No | — |
| 219 | Porcentaje de Discapacidad | `EM_Sspr_Disability` | No | No | — |
| 220 | Disability Type | `EM_Sspr_Descrip_Disab` | No | No | — |
| 221 | Disability Date | `EM_Sspr_Date_Disab` | No | No | — |
| 222 | Represents to Disabled | `EM_Sspr_Representsdisabled` | No | No | — |
| 223 | Employee Disabled | `EM_Sspr_Bpartner_Disabled_ID` | No | No | — |
| 225 | Gender | `—` | No | No | — |
| 226 | Vacations Concept | `EM_Sspr_Concept_Vac_ID` | No | No | — |
| 240 | Thirteenth | `EM_Sspr_Thirteenth` | No | No | — |
| 241 | Concept Thirteenth | `EM_Sspr_Concept_Thirteenth_ID` | No | No | — |
| 242 | Fourteenth | `EM_Sspr_Fourteenth` | No | No | — |
| 243 | Concept Fourteenth | `EM_Sspr_Concept_Fourteenth_ID` | No | No | — |
| 245 | EM_Sspr_Email | `EM_Sspr_Email` | No | No | — |
| 250 | Establishment Code | `EM_Sspr_Establishmentcode_ID` | No | No | — |
| 260 | Civil status | `—` | No | No | — |
| 320 | Business Unit | `EM_Sspr_Costcenter_ID` | No | No | 800000 |
| 330 | Product | `EM_Sspr_User1_ID` | No | No | 800000 |
| 340 | 2nd Dimension | `EM_Sspr_User2_ID` | No | No | 800000 |
| 360 | Executive | `EM_Sspr_Isexecutive` | No | No | — |
| 370 | Fortnight | `EM_Sspr_Fortnight` | No | No | C1CE792930674D08832CCFCACAE3F1AC |
| 380 | Comply Bonos | `EM_Sspr_Comply_Bonos` | No | No | C1CE792930674D08832CCFCACAE3F1AC |
| 390 | Mobilization | `EM_Sspr_Mobilization` | No | No | C1CE792930674D08832CCFCACAE3F1AC |
| 400 | Extra Hours | `EM_Sspr_Extra_Hours` | No | No | C1CE792930674D08832CCFCACAE3F1AC |
| 410 | Bonus Punctual | `EM_Sspr_Bonus_Punctual` | No | No | C1CE792930674D08832CCFCACAE3F1AC |
| 431 | Province of Galapagos benefit | `EM_Sspr_Galapagosbenf` | No | No | D5963F6CA30542AAB419655573809DD1 |
| 441 | Worker with catastrophic illness | `EM_Sspr_Workwci` | No | No | D5963F6CA30542AAB419655573809DD1 |
| 451 | Net salary system | `EM_Sspr_Netsalarysys` | No | No | D5963F6CA30542AAB419655573809DD1 |
| 461 | Worker has a spouse | `EM_Sspr_Work_Spouse` | No | No | D5963F6CA30542AAB419655573809DD1 |

### Datos Adicionales (ventana: Liquidación Final)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Sspr_Settlement_ID | `Sspr_Settlement_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Line No. | `Line` | No | No | — |
| 50 | Business Concept | `Sspr_Concept_ID` | No | No | — |
| 60 | Amount | `Amount` | No | No | — |
| 70 | Quantity | `Qty` | No | No | — |
| 80 | Total Net | `Totalnet` | No | No | — |
| 90 | Payroll | `Sspr_Payroll_ID` | No | No | — |
| 140 | Description | `Description` | No | No | — |

### Leave Type (ventana: Tipo de Permiso)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Commercial Name | `Name` | No | No | — |
| 50 | Nodays | `Nodays` | No | No | — |
| 55 | Nohours | `Nohours` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 80 | Add To Vacancies | `ADD_To_Vacancies` | No | No | — |

### Business Concept (ventana: Concepto Laboral)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | 54DF5E90B1184471ABF20F0C852A5ACD |
| 50 | Name | `Name` | No | No | 54DF5E90B1184471ABF20F0C852A5ACD |
| 60 | Affectation Type | `Affectationtype` | No | No | FC33CC83D7974BEF8EE845F91133218E |
| 70 | Effect | `Conceptsubtype` | No | No | FC33CC83D7974BEF8EE845F91133218E |
| 80 | Concept Type | `Concepttype` | No | No | FC33CC83D7974BEF8EE845F91133218E |
| 85 | Concept Formulary | `Sspr_Codeformulary107_ID` | No | No | FC33CC83D7974BEF8EE845F91133218E |
| 90 | Business Concept | `Sspr_Concept_Formula_ID` | No | No | A7E47467BE5C4094902379340CC1A0F9 |
| 100 | Operation | `Operation` | No | No | A7E47467BE5C4094902379340CC1A0F9 |
| 110 | Amount | `Amount` | No | No | A7E47467BE5C4094902379340CC1A0F9 |
| 120 | Formula | `Formula` | No | No | A7E47467BE5C4094902379340CC1A0F9 |
| 125 | Delete formula | `Deleteformula` | No | No | — |
| 130 | Create Concept Amounts | `Create_Concept_Amounts` | No | No | — |
| 140 | Is Income Calculated | `Isincomecalculated` | No | No | 3D25BC58769C437F97EC766BE800D42D |
| 160 | Is Cumulative | `Iscumulative` | No | No | 3D25BC58769C437F97EC766BE800D42D |
| 170 | IsProjected | `Isprojected` | No | No | 3D25BC58769C437F97EC766BE800D42D |
| 180 | Is iess | `Isiess` | No | No | 3D25BC58769C437F97EC766BE800D42D |
| 260 | Print Type | `concepttypepayroll` | No | No | — |
| 280 | Formulated Concepts | `conceptformulates` | No | No | — |
| 290 | Order Print | `orderprint` | No | No | — |
| 300 | Variation salary | `Variationsalary` | No | No | — |
| 310 | Print Observation Report | `Print_Observ_Report` | No | No | — |
| 320 | Group_Concept | `Group_Concept` | No | No | — |
| 330 | Print | `Print_Report` | No | No | — |
| 340 | It is for calculation gross salary | `Is_Calc_Gross_Salary` | No | No | — |
| 350 | Do not prorate income tax | `Not_Prorate_Income_Tax` | No | No | — |
| 500 | Living Wage Calculation | `Living_Wage_Calculation` | No | No | 6DEFF2A75B724283873A5134B71DD2C5 |

### Utilities (ventana: Utilidades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | Sí | — |
| 30 | Employee | `C_Bpartner_ID` | No | Sí | — |
| 35 | Supplementary Data | `Sspr_Supplementary_Data_ID` | No | Sí | — |
| 40 | Year | `C_Year_ID` | No | Sí | — |
| 50 | Average Income | `Averageincome` | No | Sí | — |
| 60 | Living Wage | `Livingwage` | No | Sí | — |
| 70 | Wage Compensation | `Wagecompensation` | No | Sí | — |
| 80 | Value 10% | `Value_Tenpct` | No | Sí | — |
| 90 | Value 5% | `Values_Fivepct` | No | Sí | — |
| 93 | Advance Utilities | `Advance_Utilities` | No | No | — |
| 95 | Judicial Retention | `Judicial_Retention` | No | Sí | — |
| 100 | Total Utilities | `total_utilities` | No | Sí | — |
| 110 | Number Charges | `Numbercharges` | No | Sí | — |
| 120 | Working Days | `Workingdays` | No | Sí | — |
| 130 | Worked Days | `Workeddays` | No | Sí | — |
| 150 | Income Tax Withholding | `Incometaxwithholding` | No | Sí | — |

### Contract Type (ventana: Tipo de Contrato)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Code | `Code` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Format | `Format` | No | No | — |

### Lines (ventana: Solicitud Préstamo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | Sí | — |
| 20 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | Active | `Isactive` | No | Sí | — |
| 40 | Line No. | `Line` | No | Sí | — |
| 50 | Paydate | `Paydate` | No | Sí | — |
| 60 | Amount | `Amount` | No | Sí | — |
| 62 | Loan Advance | `Loan_Advance` | No | No | — |
| 65 | Total Balance | `Total_Balance` | No | Sí | — |
| 70 | Status | `Status` | No | Sí | — |
| 90 | Cancel liquidation | `Cancelliquidation` | No | No | — |
| 100 | Manual Cancellation | `Manual_Cancellation` | No | No | — |

### Cost Employee Line (ventana: Gasto del Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Deductible Expense | `Deductibleexpense` | No | No | — |
| 50 | Amount Deductible | `Amountdeductible` | No | No | — |
| 60 | Concept Formulary | `Sspr_Codeformulary107_ID` | No | No | — |

### Payroll Ticket Concept (ventana: Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Payroll Ticket | `Sspr_Payroll_Ticket_ID` | No | Sí | — |
| 50 | Business Concept | `Sspr_Concept_ID` | No | No | 103 |
| 60 | Amount | `Amount` | No | No | 103 |
| 130 | Value Concept | `Valueconcept` | No | No | — |

### Accounting Ledger (ventana: Contabilidad de Nomina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Accounting Combination | `C_Validcombination_ID` | No | No | — |
| 60 | Ishaveaccount | `Ishaveaccount` | No | No | — |
| 70 | Closingaccount | `Closingaccount` | No | No | — |

### Family (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Empleado | `C_Bpartner_ID` | No | Sí | — |
| 50 | Family Ties | `Familyties` | No | No | — |
| 60 | First Name | `Firstname` | No | No | — |
| 70 | Last Name | `Lastname` | No | No | — |
| 80 | Document Type Name | `Documenttype` | No | No | — |
| 90 | Document No | `Documentno` | No | No | — |
| 100 | Birth of Day | `Birthday` | No | No | — |
| 120 | Join Date | `Joindate` | No | No | — |
| 130 | Leave Date | `Leavedate` | No | No | — |
| 140 | Reason for Leaving | `Reasonforleaving` | No | No | — |
| 150 | Paternity Accreditation | `Paternityaccreditation` | No | No | — |
| 160 | Accreditation Document | `Accreditationdoc` | No | No | — |
| 170 | Employee Address | `Isaddress` | No | No | — |
| 180 | Location / Address | `C_Location_ID` | No | No | — |
| 190 | Discapacitado | `Isdisabled` | No | No | — |
| 200 | Porcentaje Discapacidad | `Disability` | No | No | — |
| 210 | Judicial Retention | `Judicial_Retention` | No | No | — |

### Lines (ventana: Tipo Garante)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Requirements | `Requirements` | No | No | — |

### Income Tax Line (ventana: Tabla de Impuesto a la Renta)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Base Min. | `Basemin` | No | No | — |
| 50 | Base Max. | `Basemax` | No | No | — |
| 60 | Tax Amount | `Taxamount` | No | No | — |
| 70 | Percentaje Tax | `Percentajetax` | No | No | — |

### Disability - Senior (ventana: Discapacidad - mayor)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Year | `C_Year_ID` | No | No | — |
| 40 | Value Seniors | `Value_Seniors` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Occupation (ventana: Ocupación)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 60 | Pdt Code | `Pdtcode` | No | No | — |

### Contract Position (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Contract | `Sspr_Contract_ID` | No | Sí | — |
| 50 | Position | `Sspr_Position_ID` | No | No | — |
| 60 | Starting Date | `Startdate` | No | No | 9EFB2074D9B847A594DE30D052CACBA9 |
| 70 | Ending Date | `Enddate` | No | No | 9EFB2074D9B847A594DE30D052CACBA9 |
| 80 | Boss | `Boss` | No | No | — |

### Supplementary Data (ventana: Datos Complemtarios)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Year | `C_YEAR_ID` | No | No | — |
| 40 | Ruc Complementary Company | `Taxid_Company` | No | No | — |
| 50 | Identification Card | `Taxid_Partner` | No | No | — |
| 60 | Name | `Name` | No | No | — |
| 70 | Surname | `Surname` | No | No | — |
| 80 | Gender | `Gender` | No | No | — |
| 90 | Occupationnal code IESS | `Occup_Code_Iess` | No | No | — |
| 100 | Family Responsabilities | `NUM_Charges` | No | No | — |
| 110 | Days Worked | `Daysworked` | No | No | — |
| 120 | Payment Type | `Paymenttype` | No | No | — |
| 130 | Judicial Retention | `Judicial_Retention` | No | No | — |

### Period Concept (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Period | `Sspr_Period_ID` | No | Sí | — |
| 50 | Business Concept | `Sspr_Concept_ID` | No | No | — |

### Payroll Employee (ventana: Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Active | `Isactive` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Employee | `C_Bpartner_ID` | No | No | — |

### User Approval Default (ventana: Usuario de Aprobación por Defecto)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Employee | `C_Bpartner_ID` | No | No | — |
| 40 | Is Default Approver | `Isdefault_Approver` | No | No | — |

### Attendance (ventana: Asistencia)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 50 | Waiting Period (Days) | `Days` | No | No | — |
| 60 | Hoursentry | `Hoursentry` | No | No | — |
| 70 | Hoursout | `Hoursout` | No | No | — |
| 80 | Hoursextra | `Hoursextra` | No | No | — |

### Readmissions (ventana: Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Type Readmission | `Type_Readmission` | No | No | — |
| 40 | Starting Date | `Startdate` | No | No | — |
| 50 | Ending Date | `Enddate` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Request Loans (ventana: Solicitud Préstamo)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `c_bpartner_id` | No | No | — |
| 45 | Type Guarantor | `Sspr_Typeguarantor_ID` | No | No | — |
| 46 | Guarantor | `Guarantor` | No | No | — |
| 50 | Previous Balance | `Previous_Balance` | No | No | — |
| 70 | Requestdate | `Requestdate` | No | No | — |
| 80 | Amount | `Amount` | No | No | — |
| 90 | Time | `Time` | No | No | — |
| 100 | Interest | `Interest` | No | No | — |
| 110 | Firstdate | `Firstdate` | No | No | — |
| 120 | Status | `Status` | No | Sí | — |
| 130 | Description | `Description` | No | No | — |
| 140 | Create Line Loans | `Complete` | No | No | — |
| 150 | Apply Loan | `Completestatus` | No | No | — |
| 170 | Reactive | `Reactive` | No | No | — |
| 180 | Pre-Cancellation | `Pre_Cancellation` | No | No | — |
| 190 | Renewal | `Renewal` | No | No | — |
| 200 | Advance Payment | `Advance_Payment` | No | No | — |

### Lines (ventana: Automatic Payroll)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Document No. | `Documentno` | No | No | — |
| 60 | Payroll | `Ispayroll` | No | No | — |

### IESS Rate (ventana: Porcentaje IESS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Name IESS Rate | `Name` | No | No | — |
| 40 | Value IESS Rate | `Value` | No | No | — |

### Pension System (ventana: Sistema de Pensiones)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Pdt Code | `Pdtcode` | No | No | — |
| 50 | Search Key | `Value` | No | No | — |
| 60 | Name | `Name` | No | No | — |
| 70 | Description | `Description` | No | No | — |

### Approbation Leave (ventana: Aprobación de Permiso)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 25 | Document No. | `Documentno` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `c_bpartner_id` | No | Sí | — |
| 42 | Leave Type | `Sspr_Leave_Type_ID` | No | Sí | — |
| 45 | Leave Category | `Sspr_Leave_Category_ID` | No | Sí | — |
| 47 | Specs | `Specs` | No | Sí | — |
| 48 | Details Names | `Details_Names` | No | Sí | — |
| 48 | Details Sinister | `Details_Sinister` | No | Sí | — |
| 50 | Relationship | `Sspr_Relationship_ID` | No | Sí | — |
| 50 | Date Sinister | `Date_Sinister` | No | Sí | — |
| 55 | Date Death | `Date_Death` | No | Sí | — |
| 60 | Calculate Start Date | `Stardate` | No | Sí | — |
| 70 | Calculate End Date | `Enddate` | No | Sí | — |
| 72 | No. Days available | `Nodays` | No | Sí | — |
| 75 | Start Hour | `Starthour` | No | Sí | — |
| 78 | End Hour | `Endhour` | No | Sí | — |
| 80 | Nohours | `Nohours` | No | Sí | — |
| 90 | Add To Vacancies | `ADD_To_Vacancies` | No | No | — |
| 91 | Paid Vacations | `Paid_Vacations` | No | Sí | — |
| 100 | Description | `Description` | No | Sí | — |
| 170 | Status Request | `Status_Request` | No | Sí | — |
| 180 | Status Approve | `Status_Approve` | No | Sí | — |
| 200 | Who Replace | `Whoreplace_ID` | No | Sí | — |
| 210 | Authorized | `Authorizer_ID` | No | No | — |
| 270 | Oficial Specs | `Oficial_Specs` | No | Sí | — |
| 320 | Cost Center | `C_Costcenter_ID` | No | Sí | — |
| 380 | Closed | `Closed` | No | No | — |
| 390 | Authorized Date | `Authorized_Date` | No | No | — |
| 460 | Process Reactive | `Process_Reactive` | No | No | — |
| 530 | Approve | `Approved_Status` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los principales botones dentro de los procesos incluyen opciones para completar, retornar o rechazar solicitudes de permisos y aprobación de nómina. Informes como 'Impresión de Liquidación final' y 'Generación de Reporte de Gastos Personales' permiten a los usuarios obtener resultados de sus gestiones. Validaciones frecuentes incluyen la verificación de campos obligatorios en solicitudes, como en el trigger `SSPR_LEAVEVALIDATEVAC_TRG1`, que controla que el campo tipo vacaciones esté correctamente completado antes de proceder.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.hrm.payroll.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archive Payment Utilities Produbanco TXT | Archive Payment Utilities Produbanco TXT | Sspr_Payment Utilities Produbanco TXT | Java `ArchivePaymentUtilitiesProdubanco` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentUtilitiesProdubanco.java` |
| Botón (Java) | Archivo Pago Decimos  Produbanco TXT | Archive Payment Tenth Produbanco TXT | Sspr_ArchivePaymentTenthProdubanco | Java `ArchivePaymentTenthProdubanco` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentTenthProdubanco.java` |
| Botón (Java) | Archivo Pagos Banco Produbanco Txt | Archive Payment Produbanco Bank TXT | Sspr_ArchProdubancoBankTxt | Java `ArchivePaymentProdubancoBankTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentProdubancoBankTXT.java` |
| Botón (Java) | Archivo Transferencia Nómina Banco de Guayaquil | Bank of Guayaquil Payroll Transfer File | Bank of Guayaquil Payroll Transfer File | Java `ArchPayrollGuayaquilBankTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchPayrollGuayaquilBankTXT.java` |
| Botón (Java) | Archivo Transferencia Nómina Banco del Austro | Archive Transfer Payroll Austro | Archive Transfer Payroll Austro | Java `ArchTransferPayrollBankAustro` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchTransferPayrollBankAustro.java` |
| Botón (Java) | Archivo Transferencia Utilidades del Austro | Archive Transfer Utilites Austro TXT | Archive Transfer Utilites Austro TXT | Java `ArchTransferUtilitesBankAustro` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/create_txt/ArchTransferUtilitesBankAustro.java` |
| Botón (Java) | Automatic Payroll Process Class | Automatic Payroll Process Class | Automatic Payroll Process Class | Java `Sspr_AutomaticPayroll` (AD_MODEL_OBJECT `P`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_process/Sspr_AutomaticPayroll.java` |
| Botón (Java) | Cargar líneas | Load Lines | OtherTaxIncomeLoadLines | Java `OtherTaxIncomeLoadLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sspr_Other_Tax_Income_ID`, Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo | `src/com/sidesoft/hrm/payroll/ad_process/OtherTaxIncomeLoadLines.java` |
| Botón (PL/pgSQL) | Actualización del Empleado - Fecha de Entrada | Update Date Entry Employee | SSPR_UpdateDatEntryEmployee | `sspr_updatedateentry` | ACTUALIZO FECHA DE INGRESO DEL EMPLEADO CON LA DEL REINGRESO | — |
| Botón (PL/pgSQL) | Actualizar Salario | Update Salary | Sspr_UpdateSalaryEmployee | `sspr_updatesalary_employee` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Approve | Approve | SSPR_change_status_leave | `sspr_change_status_leave` | No tiene vacaciones disponibles días normales; No tiene vacaciones disponibles días adicionales; Cur_vacations.nodays + (Cur_vacations.Noadditionaltotal):; VALIDA DIAS DE VACACIONES DISPONIBLES NORMALES | — |
| Botón (PL/pgSQL) | Aprobar Prestamos | Approve Loan | SSPR_change_status_approve | `sspr_change_status` | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN | — |
| Botón (PL/pgSQL) | Borrar fórmula | Delete formula | sspr_deleteformula | `sspr_deleteformula` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Calcular Vacaciones | Calculate Vacation | Calculate Vacation | `sspr_calculatevacation` | AND A.C_BPARTNER_ID = '3C0596B9EB424089B757554EF5BCACD6'; ELIMINA REGISTROS MAYORES A LA FECHA DE PROCESO; Cuenta vacaciones que la fecha inicio y fecha fin cumplan 1 año.; En caso de que el empleado no cuente con linea… | — |
| Botón (PL/pgSQL) | Cargar Acumulables | Load AcumulativeIn | Acumulative In | `sspr_acumulativeconcepts` | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; AND TO_CHAR(pe.startdate,'YYYY-MM') = TO_CHAR(oti.process_date,'YYYY-MM'); INSERTA LIQUIDACIONES PESTA… | — |
| Botón (PL/pgSQL) | Cargar Concepto Préstamo | Load Concept Loan | Load Concept Loan | `sspr_load_concept_loan` | RAISE NO_DATA_FOUND||Cur_LINELOANS.sshr_loans_id; | — |
| Botón (PL/pgSQL) | Cargar Plantilla de Nómina | Load Payroll Template | load_payroll_template | `sspr_load_payroll_template` | Insert concepts of the template into period. | — |
| Botón (PL/pgSQL) | Completar Liquidación | Complete Settlement | sspr_complete_settlement | `sspr_complete_settlement` | CAMBIA DE ESTADO NOMINA NORMAL A LIQUIDADO; CAMBIA DE ESTADO NOMINA DE PROVISIONES A LIQUIDADO; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA NORMAL; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA DE PROVISIONES | — |
| Botón (PL/pgSQL) | Copiar Conceptos | Copy Concepts | Copy_Concepts | `sspr_copy_concept_amounts` | raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-'||v_SSconcept_ID;; raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-test'||v_EndPeriod_ID||'test'; | — |
| Botón (PL/pgSQL) | Copiar Plantilla | Copy Template | Copy Template | `sspr_copy_template` | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; and em_sspr_category_acct_id = Cur_partner.em_sspr_status; | — |
| Botón (PL/pgSQL) | Crear línea Préstamos | Create Line Loans | Create Line Loans | `sspr_createlineloans` | v_MontoCuota := (v_amount / v_time) + v_MontoInteres; | — |
| Botón (PL/pgSQL) | Crear líneas de Liquidación | Create Lines Settlement | sspr_lines_settlement | `sspr_lines_settlement` | Date to contract out the payroll provision period; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE LA NOMINA DE PROVISIONES- PERIODO, ESTADO; VALIDACION FECHA FIN DEL CONTRATO VS FECHA DE LA NOMINA DE LIQ… | — |
| Botón (PL/pgSQL) | Crear Montos de Conceptos | Create Concept Amounts | Create_Concept_Amounts | `sspr_create_concept_amounts` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Eliminar Diario Manual | Delete Manual Journal | Delete Manual Journal | `sspr_delete_manual_journal` | VALIDO QUE EL ASIENTO NO ESTE CONTABILIZADO; ACTUALIZO CABECERA DE LA NOMINA PARA QUE PERMITA GENERAR EL ASIENTO; OBTENGO REFERENCIA DE LAS LINEAS DEL ASIENTO; ELIMINO CABECERA Y AGRUPACION DEL ASIENTO | — |
| Botón (PL/pgSQL) | Fondos de Reserva | Reserve Funds | SSPR_ReserveFunds | `sspr_generate_reservefounds` | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_… | — |
| Botón (PL/pgSQL) | Generar Datos para Asiento Manual | Manual Journal Entries | Manual Journal Entries | `sspr_generate_manual_journal` | NO HAY NINGUNA REFERENCIA DE TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; NO EXISTE UN ESQUEMA CONTABLE CONFIGURADO PARA LA ORGANIZACION; ** NUEVO DESARROLLO PARA UNIFICAR EL PROCESO DE CONTABILIDAD DE NOMINA(FERNANDA IGU… | — |
| Botón (PL/pgSQL) | Generar Impuesto a la Renta | Tax Income | Tax Income | `sspr_incometotals` | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES PARA INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES; TOTAL DE INGRESOS ACUMULABLES Y NO PROYECTABLES… | — |
| Botón (PL/pgSQL) | Generar Liquidación del Empleado | Generate Settlement Employee | Generate Settlement Employee | `SSPR_generatesettlementemp` | OBTENGO EL ID DEL EMPLEADO Y FECHA DE SALIDA PARA VALIDAR LA VACACIONES; OBTENGO DIAS PENDIENTES DE VACACIONES DEL EMPLEADO | — |
| Botón (PL/pgSQL) | Generar Quincena | Generate Fortnight | Generate_fortnight | `sspr_get_fortnight_concept` | SELECT SSPR_CONCEPT_ID INTO v_Qconcept_ID FROM SSPR_CONCEPT WHERE isfortnight ='Y' limit 1;; raise exception '%', '@Concepto Quincena No existe@';--OBTG:2000-; SELECT SSPR_CONCEPT_ID INTO v_Salary_ID FROM SSPR_CONCEPT W… | — |
| Botón (PL/pgSQL) | Pago Nómina | Payroll Payment Out | Payroll Payment Out | `sspr_payrollpayment` | ERROR=NO TIENE TIEPO DE DOCUMENTO CONFIGURADO PARA PAGO DE NOMINA; OBTENGO CUENTA CONFIGURADA PARA PAGOS DE NOMINA; ACTUALIZA ESTADO DEL COBRO A PROCESADO PARA PODER CONTABILIZAR | — |
| Botón (PL/pgSQL) | Procesar | Process | OtherTaxIncomeProcess | `sspr_other_tax_income_process` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Procesar Nómina | Process Payroll | sspr_process_payroll | `sspr_process_payroll` | 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE ORDEN DE PROCESO DE GENERACION DE NOMINA; RAISE_APPLICATION_ERROR(-20000, 'new v_value' || v_value); | — |
| Botón (PL/pgSQL) | Proceso de Nómina Automático | Automatic Payroll Process | Automatic Payroll Process | `sspr_automatic_payroll_process` | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA; RECUPERA INSTANCIA PARA DESPROCESAR NOMINAS | — |
| Botón (PL/pgSQL) | Proceso de Utilidades | Process of Utilities | Process of Utilities | `sspr_process_utility` | No existe configuración utilidades para el año de proceso; Ya existe Utilidades generadas para este período; Debe configurar el período de impuesto a la renta; El período IR configurado no pertenece al año de proceso | — |
| Botón (PL/pgSQL) | Préstamos Cambio de Estado | Apply Loan | SSPR_change_status | `sspr_change_status` | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN | — |
| Botón (PL/pgSQL) | Reactivar | Reactive | sspr_reactive_loan | `sspr_reactiveloan` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Reactivar | Reactivate | sspr_oti_reactivate | `sspr_oti_reactivate` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Reactivar Proceso | Process Reactive | Process Reactive | `sspr_leave_reactive` | Cannot Reactive, Transaction is add to vacations and have related payroll; OBTENGO EL PERIODO RELACIONADO A ESE PERMISO; VALIDO SI EXISTE UNA NOMINA PROCESADA PARA ESE PERIODO | — |
| Botón (PL/pgSQL) | Renovación | Renewal | sspr_renewal | `sspr_renewal` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Informe (servlet) | Archivo de Variación de Extras IESS | IESS Extras Variation File | IESS Extras Variation File | Java `ArchVariationSalaryCSV` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `adOrgId` | `src/com/sidesoft/hrm/payroll/create_txt/ArchVariationSalaryCSV.java` |
| Informe (servlet) | Archivo Pago Banco Pichincha TXT | File Payment Pichincha Bank TXT | File Payment Pichincha Bank TXT | Java `ArchPaymentPichinchaBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchPaymentPichinchaBankTXT.java` |
| Informe (servlet) | Archivo Pago Banco Rumiñahui TXT | Archive Payment Ruminahui Bank TXT | Sspr_ArchRuminahuiBanKTxt | Java `ArchivePayrollPaymentRuminahuiBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePayrollPaymentRuminahuiBankTXT.java` |
| Informe (servlet) | Generar Formulario 107 Xml | Generate Formulary 107 Xml | Generate Formulary 107 Xml | Java `Formulary107_xml` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/create_xml/Formulary107_xml.java` |
| Informe (servlet) | Modificar Salario CSV | Modify Salary CSV | Modify Salary CSV | Java `ModifySalaryCSV` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cPeriodId` | `src/com/sidesoft/hrm/payroll/create_txt/ModifySalaryCSV.java` |
| Informe (servlet) | Pago Archivo Banco Central TXT | Archive Payment Central Bank TXT | Archive Payment Central Bank TXT | Java `ArchPaymentCtralBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchPaymentCtralBankTXT.java` |
| Informe (servlet) | Pago Archivo Banco General Rumiñahui Utilidades TXT | Payment Archive BanK General Ruminahui Utilities TXT | PaymentArchiveBankRuminahuiUtilities | Java `ArchivePaymentUtilitiesRuminahuiBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentUtilitiesRuminahuiBankTXT.java` |
| Informe (servlet) | Reporte Utilidades CSV | CSV Utilities Report | CSV Utilities Report | Java `UtilitiesCSV` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/create_txt/UtilitiesCSV.java` |
| Proceso / otro | Amortización Préstamos | Amortization Loans | Amortization Loans | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Archivo variación salarial | File variation salary | File variation salary | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Banco | Bank | Bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Cheque de Pago | Paycheck | Paycheck | *(OBUIAPP / manual)* | Paycheck | — |
| Proceso / otro | Cronograma de Vacaciones | Vacation Schedule | Vacation Schedule | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Deposito a Banco | Deposit Bank | Deposit Bank | *(OBUIAPP / manual)* | Deposit Bank | — |
| Proceso / otro | Detailed Payroll Cost | Detailed Payroll Cost | Detailed Payroll Cost | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle Acumulado Decimo 4to Resumido por Centro de Costo | Accumulated Detail Fourteenth Summarized by Cost Center | Report Accumulated Detail Fourteenth | *(OBUIAPP / manual)* | Accumulated Detail Fourteenth Summarized by Cost Center | — |
| Proceso / otro | Detalle Cargo Concepto | Detail Paid by Concept | Detail Paid by Concept | *(OBUIAPP / manual)* | Detail Paid by Concept | — |
| Proceso / otro | Detalle de Cuotas Prestamos por Centros de Costos | Payment Details Loans by Cost Center | Report Payment Details Loans by Cost C | *(OBUIAPP / manual)* | Payment Details Loans by Cost Center | — |
| Proceso / otro | Detalle de Provisión de vacaciones resumida por Centro de Costos | Detail of Vacation Provision Summarized by cost center | Report Detail of Vacation Provision | *(OBUIAPP / manual)* | Detail of Vacation Provision Summarized by cost center | — |
| Proceso / otro | Detalle General de Empleados | General Employees Detail | General Employees Detail | *(OBUIAPP / manual)* | General Employees Detail | — |
| Proceso / otro | Detalle nómina Banco | Payroll Bank Detail | Payroll Bank Detail | *(OBUIAPP / manual)* | Payroll Bank Detail | — |
| Proceso / otro | Detalle Prestamos | Detailed Loans | Detailed Loans | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado de Cuenta de Vacaciones por Empleado | Vacation Statement by Employee | Vacation Statement by Employee | *(OBUIAPP / manual)* | Vacation Statement by Employee | — |
| Proceso / otro | Extras Resumidos | Extras Summarized | Extras Summarized | *(OBUIAPP / manual)* | Extras Summarized | — |
| Proceso / otro | Formato Décimo Cuarto | 14th Remuneration Format | 14th Remuneration Format | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | General Report of Family Responsibilities | General Report of Family Responsibilities | GeneralReportofFamilyResponsibilities | *(OBUIAPP / manual)* | General Report of Family Responsibilities | — |
| Proceso / otro | Generar Formulario 101 - Costos Empleado | Generate Formulary 101 - Cost Employee | Generate Formulary 101 - Cost Employee | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Importe a Cobrar - RVA | Amounts Receivable - RVA | Amounts Receivable - RVA | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Importe a Cobrar Décimo Tercero por categoría de empleado | Amounts Receivable - 13th remuneration for employee category | Amounts Receivable - 13th Remuneration | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Importes a cobrar Décimo Cuarto por categoría de empleado | Amounts Receivable - 14th remuneration for employee category | Amounts Receivable - 14th Remuneration | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Informe de Utilidades | Report of Utilities | Report of Utilities | *(OBUIAPP / manual)* | Report of Utilities | — |
| Proceso / otro | Informe Impuesto a la Renta | Report IncomeTax | IncomeTax | *(OBUIAPP / manual)* | Report IncomeTax | — |
| Proceso / otro | Ingreso por Permanencia | Amounts Receivable - Residence | Amounts Receivable - Residence | *(OBUIAPP / manual)* | Amounts Receivable - Residence | — |
| Proceso / otro | Ingresos - Empleados por Categoría | Amounts Receivable - Payroll Employee Category | Amounts Receivable - Payroll Employee Ca | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Liquidación de haberes por proyecto | Salary liquidation by project | Salary liquidation report by project | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Modificar Salario | Modify Salary | Modify Salary | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Monto total Decimocuarta Bono | Total Amount Fourteenth Bonus | Total Amount Fourteenth Bonus | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Nomina General Detallada | General Payroll Detailed | General Payroll Detailed | *(OBUIAPP / manual)* | General Payroll Detailed | — |
| Proceso / otro | Nómina avanzada Individual | Individual Payroll Advance | Individual Payroll Advance | *(OBUIAPP / manual)* | Individual Payroll Advance | — |
| Proceso / otro | Nómina General | General Payroll | General Payroll | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Nómina General Detallado por Centro de Costo | General Payroll Detailed By Cost Center | General Payroll Detailed By Cost Center | *(OBUIAPP / manual)* | General Payroll Detailed By Cost Center | — |
| Proceso / otro | Nómina Individual | Individual Payroll | Individual Payroll | *(OBUIAPP / manual)* | Individual Payroll | — |
| Proceso / otro | Pago Archivo Banco Central | Archive Payment Central Bank | Archive Payment Central Bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Plantilla base imponible  impuesto a la renta | Taxable Base Income Tax | Sspr_Taxable Base Income Tax | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Provisiones | Provisions | Provisions | *(OBUIAPP / manual)* | Provisions | — |
| Proceso / otro | Reporte Acumulado de Décimo Cuarto | Accumulated Fourteenth Report | Accumulated Fourteenth Report | *(OBUIAPP / manual)* | Accumulated Fourteenth Report | — |
| Proceso / otro | Reporte Acumulado de Décimo Tercero | Accumulated Report of Thirteenth | Accumulated Report of Thirteenth | *(OBUIAPP / manual)* | Accumulated Report of Thirteenth | — |
| Proceso / otro | Reporte de Fondos de Reserva | Reserve Fund Report | Reserve Fund Report | *(OBUIAPP / manual)* | Reserve Fund Report | — |
| Proceso / otro | Reporte Detallado de Vacaciones | Detailed Vacations | Detailed_Vacations | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Formulario Individual 107 | Report Individual Formulary 107 | Report Individual Formulary 107 | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte General Formulario 107 | Report General Formulary 107 | Report General Formulary 107 | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Pago de Utilidades Banco del Pacifico | Report Utilitis Pacific Bank | Report Utilitis Pacific Bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte pago nómina Banco Pacifico | Payment Payroll Pacific Bank | Rpt_Payroll_Pacific_Bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Resumen de Vacaciones | Summary Vacations | Summary_Vacations | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Rerpote de Vacaciones tomadas por centro de costos | Rerpot of Vacation taken by cost center | Vacations by Cost Center | *(OBUIAPP / manual)* | Rerpot of Vacation taken by cost center | — |
| Proceso / otro | Resumen Definitivo de Liquidación | Definitive Summary of Liquidation | Definitive Summary of Liquidation | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Rol Empleados - Firmas | Payroll Firms | Payroll Firms | *(OBUIAPP / manual)* | Payroll Firms | — |
| Proceso / otro | Rol Individual - Nómina Fondos de Reserva | Individual Payroll Reserve Funds | Individual Payroll Reserve Funds | *(OBUIAPP / manual)* | Individual Payroll Reserve Funds | — |
| Proceso / otro | Rol Mensual Detallado | Detailed Monthly Role | Detailed Monthly Role | *(OBUIAPP / manual)* | Detailed Monthly Role | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Detalle Acumulado Decimo 3ro Resumido por Centro de Costo | Accumulated Detail Thirteenth Summarized by Cost Center | Report Accumulated Detail Thirteenth | *(OBUIAPP / manual)* | Accumulated Detail Thirteenth Summarized by Cost Center | — |
| Reporte | GENERIC - FINAL SETTLEMENT | GENERIC - FINAL SETTLEMENT | GENERIC - FINAL SETTLEMENT | Java `Sspr_ReportPrintFinalSettlement` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_process/Sspr_ReportPrintFinalSettlement.java` |
| Reporte | Impresión de Contrato | PRINT CONTRACT | PRINT CONTRACT | Java `ReportContractType` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.jrxml`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.java` |
| Reporte | Imprimir Aprovación de Permiso | Print Approvation Leave | Print Approvation Leave | Java `ApprovationLeave` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/ApprovationLeave.java` |
| Reporte | Imprimir Aprovación de Permiso Emp | Print Approvation Leave Emp | Print Approvation Leave Emp | Java `ApprovationLeaveE` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/ApprovationLeaveE.java` |
| Reporte | Imprimir Liquidación final | Print Final Settlement | PRINT  SETTLEMENT | Java `Rpt_FinalSettlement` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement.jrxml`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement.java` |
| Reporte | Imprimir Solicitud de Empleado | Print Request Leave | PRINT LEAVE | Java `Rpt_RequestLeave` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestLeave.jrxml`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestLeave.java` |
| Reporte | Imprimir Solicitud Préstamo | Print Request Loan | PRINT LOANS | Java `RptRequestLoan` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/ad_Reports/RptRequestLoan.jrxml`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/RptRequestLoan.java` |
| Reporte | Reporte de Gastos personales. | Personal expenses report | Personal expenses report | *(OBUIAPP / manual)* | Personal expenses report | — |
| Reporte | Reporte General del Formulario 107 por mes | Report General Formulary 107 by Month | Report General Formulary 107 by Month | *(OBUIAPP / manual)* | — | — |
| Reporte | Request Leave Print | Request Leave Print | Request Leave Print | Java `RequestLeave` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/RequestLeave.java` |
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
| Botón (Java) | Archive Payment Utilities Produbanco TXT | `ArchivePaymentUtilitiesProdubanco` | Proceso Java (toolbar/background) | `cYearId` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentUtilitiesProdubanco.java` |
| Botón (Java) | Archivo Pago Decimos  Produbanco TXT | `ArchivePaymentTenthProdubanco` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentTenthProdubanco.java` |
| Botón (Java) | Archivo Pagos Banco Produbanco Txt | `ArchivePaymentProdubancoBankTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentProdubancoBankTXT.java` |
| Botón (Java) | Archivo Transferencia Nómina Banco de Guayaquil | `ArchPayrollGuayaquilBankTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchPayrollGuayaquilBankTXT.java` |
| Botón (Java) | Archivo Transferencia Nómina Banco del Austro | `ArchTransferPayrollBankAustro` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchTransferPayrollBankAustro.java` |
| Botón (Java) | Archivo Transferencia Utilidades del Austro | `ArchTransferUtilitesBankAustro` | Proceso Java (toolbar/background) | `cYearId` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchTransferUtilitesBankAustro.java` |
| Botón (Java) | Automatic Payroll Process Class | `Sspr_AutomaticPayroll` | Informe (servlet PDF) | `—` | — | `src/com/sidesoft/hrm/payroll/ad_process/Sspr_AutomaticPayroll.java` |
| Botón (Java) | Cargar líneas | `OtherTaxIncomeLoadLines` | Proceso Java (toolbar/background) | `Sspr_Other_Tax_Income_ID` | Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo | `src/com/sidesoft/hrm/payroll/ad_process/OtherTaxIncomeLoadLines.java` |
| Informe (servlet) | Archivo de Variación de Extras IESS | `ArchVariationSalaryCSV` | Proceso Java (toolbar/background) | `adOrgId` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchVariationSalaryCSV.java` |
| Informe (servlet) | Archivo Pago Banco Pichincha TXT | `ArchPaymentPichinchaBankTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchPaymentPichinchaBankTXT.java` |
| Informe (servlet) | Archivo Pago Banco Rumiñahui TXT | `ArchivePayrollPaymentRuminahuiBankTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePayrollPaymentRuminahuiBankTXT.java` |
| Informe (servlet) | Generar Formulario 107 Xml | `Formulary107_xml` | Proceso Java (toolbar/background) | `cYearId` | — | `src/com/sidesoft/hrm/payroll/create_xml/Formulary107_xml.java` |
| Informe (servlet) | Modificar Salario CSV | `ModifySalaryCSV` | Proceso Java (toolbar/background) | `cPeriodId` | — | `src/com/sidesoft/hrm/payroll/create_txt/ModifySalaryCSV.java` |
| Informe (servlet) | Pago Archivo Banco Central TXT | `ArchPaymentCtralBankTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchPaymentCtralBankTXT.java` |
| Informe (servlet) | Pago Archivo Banco General Rumiñahui Utilidades TXT | `ArchivePaymentUtilitiesRuminahuiBankTXT` | Proceso Java (toolbar/background) | `cYearId` | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentUtilitiesRuminahuiBankTXT.java` |
| Informe (servlet) | Reporte Utilidades CSV | `UtilitiesCSV` | Informe (servlet PDF) | `—` | — | `src/com/sidesoft/hrm/payroll/create_txt/UtilitiesCSV.java` |
| Reporte | GENERIC - FINAL SETTLEMENT | `Sspr_ReportPrintFinalSettlement` | Informe (servlet PDF) | `—` | — | `src/com/sidesoft/hrm/payroll/ad_process/Sspr_ReportPrintFinalSettlement.java` |
| Reporte | Impresión de Contrato | `ReportContractType` | Informe (servlet PDF) | `—` | com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.jrxml | `src/com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.java` |
| Reporte | Imprimir Aprovación de Permiso | `ApprovationLeave` | Informe (servlet PDF) | `—` | — | `src/com/sidesoft/hrm/payroll/ad_Reports/ApprovationLeave.java` |
| Reporte | Imprimir Aprovación de Permiso Emp | `ApprovationLeaveE` | Informe (servlet PDF) | `—` | — | `src/com/sidesoft/hrm/payroll/ad_Reports/ApprovationLeaveE.java` |
| Reporte | Imprimir Liquidación final | `Rpt_FinalSettlement` | Informe (servlet PDF) | `—` | com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement.jrxml | `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement.java` |
| Reporte | Imprimir Solicitud de Empleado | `Rpt_RequestLeave` | Informe (servlet PDF) | `—` | com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestLeave.jrxml | `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestLeave.java` |
| Reporte | Imprimir Solicitud Préstamo | `RptRequestLoan` | Informe (servlet PDF) | `—` | com/sidesoft/hrm/payroll/ad_Reports/RptRequestLoan.jrxml | `src/com/sidesoft/hrm/payroll/ad_Reports/RptRequestLoan.java` |
| Reporte | Request Leave Print | `RequestLeave` | Informe (servlet PDF) | `—` | — | `src/com/sidesoft/hrm/payroll/ad_Reports/RequestLeave.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archive Payment Utilities Produbanco TXT | Archive Payment Utilities Produbanco TXT | Sspr_Payment Utilities Produbanco TXT | Java `ArchivePaymentUtilitiesProdubanco` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentUtilitiesProdubanco.java` |
| Botón (Java) | Archivo Pago Decimos  Produbanco TXT | Archive Payment Tenth Produbanco TXT | Sspr_ArchivePaymentTenthProdubanco | Java `ArchivePaymentTenthProdubanco` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentTenthProdubanco.java` |
| Botón (Java) | Archivo Pagos Banco Produbanco Txt | Archive Payment Produbanco Bank TXT | Sspr_ArchProdubancoBankTxt | Java `ArchivePaymentProdubancoBankTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentProdubancoBankTXT.java` |
| Botón (Java) | Archivo Transferencia Nómina Banco de Guayaquil | Bank of Guayaquil Payroll Transfer File | Bank of Guayaquil Payroll Transfer File | Java `ArchPayrollGuayaquilBankTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchPayrollGuayaquilBankTXT.java` |
| Botón (Java) | Archivo Transferencia Nómina Banco del Austro | Archive Transfer Payroll Austro | Archive Transfer Payroll Austro | Java `ArchTransferPayrollBankAustro` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchTransferPayrollBankAustro.java` |
| Botón (Java) | Archivo Transferencia Utilidades del Austro | Archive Transfer Utilites Austro TXT | Archive Transfer Utilites Austro TXT | Java `ArchTransferUtilitesBankAustro` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/create_txt/ArchTransferUtilitesBankAustro.java` |
| Botón (Java) | Automatic Payroll Process Class | Automatic Payroll Process Class | Automatic Payroll Process Class | Java `Sspr_AutomaticPayroll` (AD_MODEL_OBJECT `P`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_process/Sspr_AutomaticPayroll.java` |
| Botón (Java) | Cargar líneas | Load Lines | OtherTaxIncomeLoadLines | Java `OtherTaxIncomeLoadLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sspr_Other_Tax_Income_ID`, Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo | `src/com/sidesoft/hrm/payroll/ad_process/OtherTaxIncomeLoadLines.java` |
| Botón (PL/pgSQL) | Actualización del Empleado - Fecha de Entrada | Update Date Entry Employee | SSPR_UpdateDatEntryEmployee | `sspr_updatedateentry` | ACTUALIZO FECHA DE INGRESO DEL EMPLEADO CON LA DEL REINGRESO | — |
| Botón (PL/pgSQL) | Actualizar Salario | Update Salary | Sspr_UpdateSalaryEmployee | `sspr_updatesalary_employee` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Approve | Approve | SSPR_change_status_leave | `sspr_change_status_leave` | No tiene vacaciones disponibles días normales; No tiene vacaciones disponibles días adicionales; Cur_vacations.nodays + (Cur_vacations.Noadditionaltotal):; VALIDA DIAS DE VACACIONES DISPONIBLES NORMALES | — |
| Botón (PL/pgSQL) | Aprobar Prestamos | Approve Loan | SSPR_change_status_approve | `sspr_change_status` | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN | — |
| Botón (PL/pgSQL) | Borrar fórmula | Delete formula | sspr_deleteformula | `sspr_deleteformula` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Calcular Vacaciones | Calculate Vacation | Calculate Vacation | `sspr_calculatevacation` | AND A.C_BPARTNER_ID = '3C0596B9EB424089B757554EF5BCACD6'; ELIMINA REGISTROS MAYORES A LA FECHA DE PROCESO; Cuenta vacaciones que la fecha inicio y fecha fin cumplan 1 año.; En caso de que el empleado no cuente con linea… | — |
| Botón (PL/pgSQL) | Cargar Acumulables | Load AcumulativeIn | Acumulative In | `sspr_acumulativeconcepts` | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; AND TO_CHAR(pe.startdate,'YYYY-MM') = TO_CHAR(oti.process_date,'YYYY-MM'); INSERTA LIQUIDACIONES PESTA… | — |
| Botón (PL/pgSQL) | Cargar Concepto Préstamo | Load Concept Loan | Load Concept Loan | `sspr_load_concept_loan` | RAISE NO_DATA_FOUND||Cur_LINELOANS.sshr_loans_id; | — |
| Botón (PL/pgSQL) | Cargar Plantilla de Nómina | Load Payroll Template | load_payroll_template | `sspr_load_payroll_template` | Insert concepts of the template into period. | — |
| Botón (PL/pgSQL) | Completar Liquidación | Complete Settlement | sspr_complete_settlement | `sspr_complete_settlement` | CAMBIA DE ESTADO NOMINA NORMAL A LIQUIDADO; CAMBIA DE ESTADO NOMINA DE PROVISIONES A LIQUIDADO; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA NORMAL; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA DE PROVISIONES | — |
| Botón (PL/pgSQL) | Copiar Conceptos | Copy Concepts | Copy_Concepts | `sspr_copy_concept_amounts` | raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-'||v_SSconcept_ID;; raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-test'||v_EndPeriod_ID||'test'; | — |
| Botón (PL/pgSQL) | Copiar Plantilla | Copy Template | Copy Template | `sspr_copy_template` | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; and em_sspr_category_acct_id = Cur_partner.em_sspr_status; | — |
| Botón (PL/pgSQL) | Crear línea Préstamos | Create Line Loans | Create Line Loans | `sspr_createlineloans` | v_MontoCuota := (v_amount / v_time) + v_MontoInteres; | — |
| Botón (PL/pgSQL) | Crear líneas de Liquidación | Create Lines Settlement | sspr_lines_settlement | `sspr_lines_settlement` | Date to contract out the payroll provision period; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE LA NOMINA DE PROVISIONES- PERIODO, ESTADO; VALIDACION FECHA FIN DEL CONTRATO VS FECHA DE LA NOMINA DE LIQ… | — |
| Botón (PL/pgSQL) | Crear Montos de Conceptos | Create Concept Amounts | Create_Concept_Amounts | `sspr_create_concept_amounts` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Eliminar Diario Manual | Delete Manual Journal | Delete Manual Journal | `sspr_delete_manual_journal` | VALIDO QUE EL ASIENTO NO ESTE CONTABILIZADO; ACTUALIZO CABECERA DE LA NOMINA PARA QUE PERMITA GENERAR EL ASIENTO; OBTENGO REFERENCIA DE LAS LINEAS DEL ASIENTO; ELIMINO CABECERA Y AGRUPACION DEL ASIENTO | — |
| Botón (PL/pgSQL) | Fondos de Reserva | Reserve Funds | SSPR_ReserveFunds | `sspr_generate_reservefounds` | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_… | — |
| Botón (PL/pgSQL) | Generar Datos para Asiento Manual | Manual Journal Entries | Manual Journal Entries | `sspr_generate_manual_journal` | NO HAY NINGUNA REFERENCIA DE TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; NO EXISTE UN ESQUEMA CONTABLE CONFIGURADO PARA LA ORGANIZACION; ** NUEVO DESARROLLO PARA UNIFICAR EL PROCESO DE CONTABILIDAD DE NOMINA(FERNANDA IGU… | — |
| Botón (PL/pgSQL) | Generar Impuesto a la Renta | Tax Income | Tax Income | `sspr_incometotals` | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES PARA INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES; TOTAL DE INGRESOS ACUMULABLES Y NO PROYECTABLES… | — |
| Botón (PL/pgSQL) | Generar Liquidación del Empleado | Generate Settlement Employee | Generate Settlement Employee | `SSPR_generatesettlementemp` | OBTENGO EL ID DEL EMPLEADO Y FECHA DE SALIDA PARA VALIDAR LA VACACIONES; OBTENGO DIAS PENDIENTES DE VACACIONES DEL EMPLEADO | — |
| Botón (PL/pgSQL) | Generar Quincena | Generate Fortnight | Generate_fortnight | `sspr_get_fortnight_concept` | SELECT SSPR_CONCEPT_ID INTO v_Qconcept_ID FROM SSPR_CONCEPT WHERE isfortnight ='Y' limit 1;; raise exception '%', '@Concepto Quincena No existe@';--OBTG:2000-; SELECT SSPR_CONCEPT_ID INTO v_Salary_ID FROM SSPR_CONCEPT W… | — |
| Botón (PL/pgSQL) | Pago Nómina | Payroll Payment Out | Payroll Payment Out | `sspr_payrollpayment` | ERROR=NO TIENE TIEPO DE DOCUMENTO CONFIGURADO PARA PAGO DE NOMINA; OBTENGO CUENTA CONFIGURADA PARA PAGOS DE NOMINA; ACTUALIZA ESTADO DEL COBRO A PROCESADO PARA PODER CONTABILIZAR | — |
| Botón (PL/pgSQL) | Procesar | Process | OtherTaxIncomeProcess | `sspr_other_tax_income_process` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Procesar Nómina | Process Payroll | sspr_process_payroll | `sspr_process_payroll` | 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE ORDEN DE PROCESO DE GENERACION DE NOMINA; RAISE_APPLICATION_ERROR(-20000, 'new v_value' || v_value); | — |
| Botón (PL/pgSQL) | Proceso de Nómina Automático | Automatic Payroll Process | Automatic Payroll Process | `sspr_automatic_payroll_process` | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA; RECUPERA INSTANCIA PARA DESPROCESAR NOMINAS | — |
| Botón (PL/pgSQL) | Proceso de Utilidades | Process of Utilities | Process of Utilities | `sspr_process_utility` | No existe configuración utilidades para el año de proceso; Ya existe Utilidades generadas para este período; Debe configurar el período de impuesto a la renta; El período IR configurado no pertenece al año de proceso | — |
| Botón (PL/pgSQL) | Préstamos Cambio de Estado | Apply Loan | SSPR_change_status | `sspr_change_status` | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN | — |
| Botón (PL/pgSQL) | Reactivar | Reactive | sspr_reactive_loan | `sspr_reactiveloan` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Reactivar | Reactivate | sspr_oti_reactivate | `sspr_oti_reactivate` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Reactivar Proceso | Process Reactive | Process Reactive | `sspr_leave_reactive` | Cannot Reactive, Transaction is add to vacations and have related payroll; OBTENGO EL PERIODO RELACIONADO A ESE PERMISO; VALIDO SI EXISTE UNA NOMINA PROCESADA PARA ESE PERIODO | — |
| Botón (PL/pgSQL) | Renovación | Renewal | sspr_renewal | `sspr_renewal` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Informe (servlet) | Archivo de Variación de Extras IESS | IESS Extras Variation File | IESS Extras Variation File | Java `ArchVariationSalaryCSV` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `adOrgId` | `src/com/sidesoft/hrm/payroll/create_txt/ArchVariationSalaryCSV.java` |
| Informe (servlet) | Archivo Pago Banco Pichincha TXT | File Payment Pichincha Bank TXT | File Payment Pichincha Bank TXT | Java `ArchPaymentPichinchaBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchPaymentPichinchaBankTXT.java` |
| Informe (servlet) | Archivo Pago Banco Rumiñahui TXT | Archive Payment Ruminahui Bank TXT | Sspr_ArchRuminahuiBanKTxt | Java `ArchivePayrollPaymentRuminahuiBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePayrollPaymentRuminahuiBankTXT.java` |
| Informe (servlet) | Generar Formulario 107 Xml | Generate Formulary 107 Xml | Generate Formulary 107 Xml | Java `Formulary107_xml` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/create_xml/Formulary107_xml.java` |
| Informe (servlet) | Modificar Salario CSV | Modify Salary CSV | Modify Salary CSV | Java `ModifySalaryCSV` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cPeriodId` | `src/com/sidesoft/hrm/payroll/create_txt/ModifySalaryCSV.java` |
| Informe (servlet) | Pago Archivo Banco Central TXT | Archive Payment Central Bank TXT | Archive Payment Central Bank TXT | Java `ArchPaymentCtralBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/create_txt/ArchPaymentCtralBankTXT.java` |
| Informe (servlet) | Pago Archivo Banco General Rumiñahui Utilidades TXT | Payment Archive BanK General Ruminahui Utilities TXT | PaymentArchiveBankRuminahuiUtilities | Java `ArchivePaymentUtilitiesRuminahuiBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentUtilitiesRuminahuiBankTXT.java` |
| Informe (servlet) | Reporte Utilidades CSV | CSV Utilities Report | CSV Utilities Report | Java `UtilitiesCSV` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/create_txt/UtilitiesCSV.java` |
| Proceso / otro | Amortización Préstamos | Amortization Loans | Amortization Loans | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Archivo variación salarial | File variation salary | File variation salary | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Banco | Bank | Bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Cheque de Pago | Paycheck | Paycheck | *(OBUIAPP / manual)* | Paycheck | — |
| Proceso / otro | Cronograma de Vacaciones | Vacation Schedule | Vacation Schedule | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Deposito a Banco | Deposit Bank | Deposit Bank | *(OBUIAPP / manual)* | Deposit Bank | — |
| Proceso / otro | Detailed Payroll Cost | Detailed Payroll Cost | Detailed Payroll Cost | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Detalle Acumulado Decimo 4to Resumido por Centro de Costo | Accumulated Detail Fourteenth Summarized by Cost Center | Report Accumulated Detail Fourteenth | *(OBUIAPP / manual)* | Accumulated Detail Fourteenth Summarized by Cost Center | — |
| Proceso / otro | Detalle Cargo Concepto | Detail Paid by Concept | Detail Paid by Concept | *(OBUIAPP / manual)* | Detail Paid by Concept | — |
| Proceso / otro | Detalle de Cuotas Prestamos por Centros de Costos | Payment Details Loans by Cost Center | Report Payment Details Loans by Cost C | *(OBUIAPP / manual)* | Payment Details Loans by Cost Center | — |
| Proceso / otro | Detalle de Provisión de vacaciones resumida por Centro de Costos | Detail of Vacation Provision Summarized by cost center | Report Detail of Vacation Provision | *(OBUIAPP / manual)* | Detail of Vacation Provision Summarized by cost center | — |
| Proceso / otro | Detalle General de Empleados | General Employees Detail | General Employees Detail | *(OBUIAPP / manual)* | General Employees Detail | — |
| Proceso / otro | Detalle nómina Banco | Payroll Bank Detail | Payroll Bank Detail | *(OBUIAPP / manual)* | Payroll Bank Detail | — |
| Proceso / otro | Detalle Prestamos | Detailed Loans | Detailed Loans | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Estado de Cuenta de Vacaciones por Empleado | Vacation Statement by Employee | Vacation Statement by Employee | *(OBUIAPP / manual)* | Vacation Statement by Employee | — |
| Proceso / otro | Extras Resumidos | Extras Summarized | Extras Summarized | *(OBUIAPP / manual)* | Extras Summarized | — |
| Proceso / otro | Formato Décimo Cuarto | 14th Remuneration Format | 14th Remuneration Format | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | General Report of Family Responsibilities | General Report of Family Responsibilities | GeneralReportofFamilyResponsibilities | *(OBUIAPP / manual)* | General Report of Family Responsibilities | — |
| Proceso / otro | Generar Formulario 101 - Costos Empleado | Generate Formulary 101 - Cost Employee | Generate Formulary 101 - Cost Employee | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Importe a Cobrar - RVA | Amounts Receivable - RVA | Amounts Receivable - RVA | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Importe a Cobrar Décimo Tercero por categoría de empleado | Amounts Receivable - 13th remuneration for employee category | Amounts Receivable - 13th Remuneration | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Importes a cobrar Décimo Cuarto por categoría de empleado | Amounts Receivable - 14th remuneration for employee category | Amounts Receivable - 14th Remuneration | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Informe de Utilidades | Report of Utilities | Report of Utilities | *(OBUIAPP / manual)* | Report of Utilities | — |
| Proceso / otro | Informe Impuesto a la Renta | Report IncomeTax | IncomeTax | *(OBUIAPP / manual)* | Report IncomeTax | — |
| Proceso / otro | Ingreso por Permanencia | Amounts Receivable - Residence | Amounts Receivable - Residence | *(OBUIAPP / manual)* | Amounts Receivable - Residence | — |
| Proceso / otro | Ingresos - Empleados por Categoría | Amounts Receivable - Payroll Employee Category | Amounts Receivable - Payroll Employee Ca | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Liquidación de haberes por proyecto | Salary liquidation by project | Salary liquidation report by project | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Modificar Salario | Modify Salary | Modify Salary | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Monto total Decimocuarta Bono | Total Amount Fourteenth Bonus | Total Amount Fourteenth Bonus | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Nomina General Detallada | General Payroll Detailed | General Payroll Detailed | *(OBUIAPP / manual)* | General Payroll Detailed | — |
| Proceso / otro | Nómina avanzada Individual | Individual Payroll Advance | Individual Payroll Advance | *(OBUIAPP / manual)* | Individual Payroll Advance | — |
| Proceso / otro | Nómina General | General Payroll | General Payroll | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Nómina General Detallado por Centro de Costo | General Payroll Detailed By Cost Center | General Payroll Detailed By Cost Center | *(OBUIAPP / manual)* | General Payroll Detailed By Cost Center | — |
| Proceso / otro | Nómina Individual | Individual Payroll | Individual Payroll | *(OBUIAPP / manual)* | Individual Payroll | — |
| Proceso / otro | Pago Archivo Banco Central | Archive Payment Central Bank | Archive Payment Central Bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Plantilla base imponible  impuesto a la renta | Taxable Base Income Tax | Sspr_Taxable Base Income Tax | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Provisiones | Provisions | Provisions | *(OBUIAPP / manual)* | Provisions | — |
| Proceso / otro | Reporte Acumulado de Décimo Cuarto | Accumulated Fourteenth Report | Accumulated Fourteenth Report | *(OBUIAPP / manual)* | Accumulated Fourteenth Report | — |
| Proceso / otro | Reporte Acumulado de Décimo Tercero | Accumulated Report of Thirteenth | Accumulated Report of Thirteenth | *(OBUIAPP / manual)* | Accumulated Report of Thirteenth | — |
| Proceso / otro | Reporte de Fondos de Reserva | Reserve Fund Report | Reserve Fund Report | *(OBUIAPP / manual)* | Reserve Fund Report | — |
| Proceso / otro | Reporte Detallado de Vacaciones | Detailed Vacations | Detailed_Vacations | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Formulario Individual 107 | Report Individual Formulary 107 | Report Individual Formulary 107 | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte General Formulario 107 | Report General Formulary 107 | Report General Formulary 107 | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Pago de Utilidades Banco del Pacifico | Report Utilitis Pacific Bank | Report Utilitis Pacific Bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte pago nómina Banco Pacifico | Payment Payroll Pacific Bank | Rpt_Payroll_Pacific_Bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Resumen de Vacaciones | Summary Vacations | Summary_Vacations | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Rerpote de Vacaciones tomadas por centro de costos | Rerpot of Vacation taken by cost center | Vacations by Cost Center | *(OBUIAPP / manual)* | Rerpot of Vacation taken by cost center | — |
| Proceso / otro | Resumen Definitivo de Liquidación | Definitive Summary of Liquidation | Definitive Summary of Liquidation | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Rol Empleados - Firmas | Payroll Firms | Payroll Firms | *(OBUIAPP / manual)* | Payroll Firms | — |
| Proceso / otro | Rol Individual - Nómina Fondos de Reserva | Individual Payroll Reserve Funds | Individual Payroll Reserve Funds | *(OBUIAPP / manual)* | Individual Payroll Reserve Funds | — |
| Proceso / otro | Rol Mensual Detallado | Detailed Monthly Role | Detailed Monthly Role | *(OBUIAPP / manual)* | Detailed Monthly Role | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archive Payment Utilities Produbanco TXT | Archive Payment Utilities Produbanco TXT | Java `ArchivePaymentUtilitiesProdubanco` | Proceso Openbravo registro `cYearId` | Proceso Openbravo registro `cYearId` |
| Botón (Java) | Archivo Pago Decimos  Produbanco TXT | Archive Payment Tenth Produbanco TXT | Java `ArchivePaymentTenthProdubanco` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Botón (Java) | Archivo Pagos Banco Produbanco Txt | Archive Payment Produbanco Bank TXT | Java `ArchivePaymentProdubancoBankTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Botón (Java) | Archivo Transferencia Nómina Banco de Guayaquil | Bank of Guayaquil Payroll Transfer File | Java `ArchPayrollGuayaquilBankTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Botón (Java) | Archivo Transferencia Nómina Banco del Austro | Archive Transfer Payroll Austro | Java `ArchTransferPayrollBankAustro` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Botón (Java) | Archivo Transferencia Utilidades del Austro | Archive Transfer Utilites Austro TXT | Java `ArchTransferUtilitesBankAustro` | Proceso Openbravo registro `cYearId` | Proceso Openbravo registro `cYearId` |
| Botón (Java) | Automatic Payroll Process Class | Automatic Payroll Process Class | Java `Sspr_AutomaticPayroll` | Genera PDF desde JRXML `—`; contexto sesión `—`. | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| Botón (Java) | Cargar líneas | Load Lines | Java `OtherTaxIncomeLoadLines` | Proceso Openbravo registro `Sspr_Other_Tax_Income_ID`, Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo | Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo |
| Botón (PL/pgSQL) | Actualización del Empleado - Fecha de Entrada | Update Date Entry Employee | PL `sspr_updatedateentry` | ACTUALIZO FECHA DE INGRESO DEL EMPLEADO CON LA DEL REINGRESO | ACTUALIZO FECHA DE INGRESO DEL EMPLEADO CON LA DEL REINGRESO |
| Botón (PL/pgSQL) | Actualizar Salario | Update Salary | PL `sspr_updatesalary_employee` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Approve | Approve | PL `sspr_change_status_leave` | No tiene vacaciones disponibles días normales; No tiene vacaciones disponibles días adicionales; Cur_vacations.nodays + (Cur_vacations.Noadditionaltotal):; VALIDA DIAS DE VACACIONES DISPONIBLES NORMALES | No tiene vacaciones disponibles días normales; No tiene vacaciones disponibles días adicionales; Cur_vacations.nodays + (Cur_vacations.Noadditionaltotal):; VALIDA DIAS DE VACACIONES DISPONIBLES NORMALES; VALIDA DIAS DE VACACIONES DISPONIBLE ADICIONALES; ACTUALIZA DIAS TOMADOS EN LA TABLA DE VACACIONES |
| Botón (PL/pgSQL) | Aprobar Prestamos | Approve Loan | PL `sspr_change_status` | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN |
| Botón (PL/pgSQL) | Borrar fórmula | Delete formula | PL `sspr_deleteformula` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Calcular Vacaciones | Calculate Vacation | PL `sspr_calculatevacation` | AND A.C_BPARTNER_ID = '3C0596B9EB424089B757554EF5BCACD6'; ELIMINA REGISTROS MAYORES A LA FECHA DE PROCESO; Cuenta vacaciones que la fecha inicio y fecha fin cumplan 1 año.; En caso de que el empleado no cuente con linea… | AND A.C_BPARTNER_ID = '3C0596B9EB424089B757554EF5BCACD6'; ELIMINA REGISTROS MAYORES A LA FECHA DE PROCESO; Cuenta vacaciones que la fecha inicio y fecha fin cumplan 1 año.; En caso de que el empleado no cuente con lineas, Tomara la fecha de inicio del contrato; OBTENGO LA FECHA DE CADUCIDAD DEL CONTRATO EN CASO DE LIQUIDAC-ION DE EMPLEADOS; VALIDA FECHA FIN DE CONTRATO EN CASO DE SER LIQUIDACIÓN DE EMPLEADOS |
| Botón (PL/pgSQL) | Cargar Acumulables | Load AcumulativeIn | PL `sspr_acumulativeconcepts` | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; AND TO_CHAR(pe.startdate,'YYYY-MM') = TO_CHAR(oti.process_date,'YYYY-MM'); INSERTA LIQUIDACIONES PESTA… | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; AND TO_CHAR(pe.startdate,'YYYY-MM') = TO_CHAR(oti.process_date,'YYYY-MM'); INSERTA LIQUIDACIONES PESTAÑA LINEAS Y DATOS ADICIONALES; COMPLETA DIAS MESES DE RETENCION DE IMPUESTO A LA RENTA; and c_bpartner.c_bpartner_id = v_c_bpartner_id |
| Botón (PL/pgSQL) | Cargar Concepto Préstamo | Load Concept Loan | PL `sspr_load_concept_loan` | RAISE NO_DATA_FOUND||Cur_LINELOANS.sshr_loans_id; | RAISE NO_DATA_FOUND||Cur_LINELOANS.sshr_loans_id; |
| Botón (PL/pgSQL) | Cargar Plantilla de Nómina | Load Payroll Template | PL `sspr_load_payroll_template` | Insert concepts of the template into period. | Insert concepts of the template into period. |
| Botón (PL/pgSQL) | Completar Liquidación | Complete Settlement | PL `sspr_complete_settlement` | CAMBIA DE ESTADO NOMINA NORMAL A LIQUIDADO; CAMBIA DE ESTADO NOMINA DE PROVISIONES A LIQUIDADO; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA NORMAL; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA DE PROVISIONES | CAMBIA DE ESTADO NOMINA NORMAL A LIQUIDADO; CAMBIA DE ESTADO NOMINA DE PROVISIONES A LIQUIDADO; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA NORMAL; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA DE PROVISIONES; and sspr_contract_id = v_sspr_contract_id;; ACTUALIZA DIAS TOMADOS EN LA TABLA DE VACACIONES |
| Botón (PL/pgSQL) | Copiar Conceptos | Copy Concepts | PL `sspr_copy_concept_amounts` | raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-'||v_SSconcept_ID;; raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-test'||v_EndPeriod_ID||'test'; | raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-'||v_SSconcept_ID;; raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-test'||v_EndPeriod_ID||'test'; |
| Botón (PL/pgSQL) | Copiar Plantilla | Copy Template | PL `sspr_copy_template` | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; and em_sspr_category_acct_id = Cur_partner.em_sspr_status; | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; and em_sspr_category_acct_id = Cur_partner.em_sspr_status; |
| Botón (PL/pgSQL) | Crear línea Préstamos | Create Line Loans | PL `sspr_createlineloans` | v_MontoCuota := (v_amount / v_time) + v_MontoInteres; | v_MontoCuota := (v_amount / v_time) + v_MontoInteres; |
| Botón (PL/pgSQL) | Crear líneas de Liquidación | Create Lines Settlement | PL `sspr_lines_settlement` | Date to contract out the payroll provision period; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE LA NOMINA DE PROVISIONES- PERIODO, ESTADO; VALIDACION FECHA FIN DEL CONTRATO VS FECHA DE LA NOMINA DE LIQ… | Date to contract out the payroll provision period; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE LA NOMINA  DE PROVISIONES- PERIODO, ESTADO; VALIDACION FECHA FIN DEL CONTRATO VS FECHA DE LA NOMINA DE LIQUIDACION NORMAL; OBTENGO FECHA INICIO Y FECHA FIN DE PERIODO; VALIDACION FECHA FIN DEL CONTRATO VS FECHA DE LA NOMINA DE LIQUIDACION PROVISIONES |
| Botón (PL/pgSQL) | Crear Montos de Conceptos | Create Concept Amounts | PL `sspr_create_concept_amounts` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Eliminar Diario Manual | Delete Manual Journal | PL `sspr_delete_manual_journal` | VALIDO QUE EL ASIENTO NO ESTE CONTABILIZADO; ACTUALIZO CABECERA DE LA NOMINA PARA QUE PERMITA GENERAR EL ASIENTO; OBTENGO REFERENCIA DE LAS LINEAS DEL ASIENTO; ELIMINO CABECERA Y AGRUPACION DEL ASIENTO | VALIDO QUE EL ASIENTO NO ESTE CONTABILIZADO; ACTUALIZO CABECERA DE LA NOMINA PARA QUE PERMITA GENERAR EL ASIENTO; OBTENGO REFERENCIA DE LAS LINEAS DEL ASIENTO; ELIMINO CABECERA Y AGRUPACION DEL ASIENTO; v_Message := '@RowsInserted@: ' || v_n_insertions || '.'; |
| Botón (PL/pgSQL) | Fondos de Reserva | Reserve Funds | PL `sspr_generate_reservefounds` | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_… | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_Period P ON CBP.C_BPartner_ID = P.C_BPartner_ID; VALIDACIONES PARA OBTENER LOS DIAS  LABORADOS; CREA CONCEPTO FONDOS DE RESERVA EN LAS LINEAS; VALIDO SI ENVIO AL IEES LOS FONDOS DE RESERVA  SEGUN LA CONFIGURACION DEL EMPLEADO |
| Botón (PL/pgSQL) | Generar Datos para Asiento Manual | Manual Journal Entries | PL `sspr_generate_manual_journal` | NO HAY NINGUNA REFERENCIA DE TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; NO EXISTE UN ESQUEMA CONTABLE CONFIGURADO PARA LA ORGANIZACION; ** NUEVO DESARROLLO PARA UNIFICAR EL PROCESO DE CONTABILIDAD DE NOMINA(FERNANDA IGU… | NO HAY NINGUNA REFERENCIA DE TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; NO EXISTE UN ESQUEMA CONTABLE CONFIGURADO PARA LA ORGANIZACION; ** NUEVO  DESARROLLO PARA UNIFICAR EL PROCESO DE CONTABILIDAD DE NOMINA(FERNANDA IGUAMBA)**--; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA CABECERA DEL ASIENTO; select TO_NUMBER(max(documentno))+1 into v_documento_jb from gl_journalbatch;; VALIDA QUE HAYA DATOS PARA CREAR EL ASIENTO |
| Botón (PL/pgSQL) | Generar Impuesto a la Renta | Tax Income | PL `sspr_incometotals` | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES PARA INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES; TOTAL DE INGRESOS ACUMULABLES Y NO PROYECTABLES… | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES  PARA  INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES; TOTAL DE INGRESOS ACUMULABLES Y NO PROYECTABLES Y CON IESS; TOTAL DE INGRESO ACUMULABLES Y NO PROYECTABLES Y SIN IESS; SUM DE INGRESO ACUMULABLES Y NO PROYECTABLES CON Y SIN IESS |
| Botón (PL/pgSQL) | Generar Liquidación del Empleado | Generate Settlement Employee | PL `SSPR_generatesettlementemp` | OBTENGO EL ID DEL EMPLEADO Y FECHA DE SALIDA PARA VALIDAR LA VACACIONES; OBTENGO DIAS PENDIENTES DE VACACIONES DEL EMPLEADO | OBTENGO EL ID DEL EMPLEADO Y FECHA DE SALIDA PARA VALIDAR LA VACACIONES; OBTENGO DIAS PENDIENTES DE VACACIONES DEL EMPLEADO |
| Botón (PL/pgSQL) | Generar Quincena | Generate Fortnight | PL `sspr_get_fortnight_concept` | SELECT SSPR_CONCEPT_ID INTO v_Qconcept_ID FROM SSPR_CONCEPT WHERE isfortnight ='Y' limit 1;; raise exception '%', '@Concepto Quincena No existe@';--OBTG:2000-; SELECT SSPR_CONCEPT_ID INTO v_Salary_ID FROM SSPR_CONCEPT W… | SELECT SSPR_CONCEPT_ID INTO v_Qconcept_ID FROM SSPR_CONCEPT WHERE isfortnight ='Y' limit 1;; raise exception '%', '@Concepto Quincena No existe@';--OBTG:2000-; SELECT SSPR_CONCEPT_ID INTO v_Salary_ID FROM SSPR_CONCEPT WHERE issalary ='Y' limit 1;; raise exception '%', '@Concepto Sueldo No existe@';--OBTG:-2000--; BUSCA EL ID DEL PERIODO ANTERIOR AL SELECCIONADO EN LE PROCESO; raise exception '%', '@Periodo No existe@';--OBTG:-2000-- |
| Botón (PL/pgSQL) | Pago Nómina | Payroll Payment Out | PL `sspr_payrollpayment` | ERROR=NO TIENE TIEPO DE DOCUMENTO CONFIGURADO PARA PAGO DE NOMINA; OBTENGO CUENTA CONFIGURADA PARA PAGOS DE NOMINA; ACTUALIZA ESTADO DEL COBRO A PROCESADO PARA PODER CONTABILIZAR | ERROR=NO TIENE TIEPO DE DOCUMENTO CONFIGURADO PARA PAGO DE NOMINA; OBTENGO CUENTA CONFIGURADA PARA PAGOS DE NOMINA; ACTUALIZA ESTADO DEL COBRO A PROCESADO PARA PODER CONTABILIZAR |
| Botón (PL/pgSQL) | Procesar | Process | PL `sspr_other_tax_income_process` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Procesar Nómina | Process Payroll | PL `sspr_process_payroll` | 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE ORDEN DE PROCESO DE GENERACION DE NOMINA; RAISE_APPLICATION_ERROR(-20000, 'new v_value' || v_value); | 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE ORDEN DE PROCESO DE GENERACION DE NOMINA; RAISE_APPLICATION_ERROR(-20000, 'new v_value' || v_value);; RAISE_APPLICATION_ERROR(-20000, ' 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO '||Cur_Concept.SSPR_Concept_ID||' '|| v_Period_ID||' '|| Cur_Employee.C_BPartner_ID);; SSPR_GET_BUSINESS_CONCEPT(Cur_Concept.SSPR_Concept_ID, v_Period_ID, Cur_Employee.C_BPartner_ID) |
| Botón (PL/pgSQL) | Proceso de Nómina Automático | Automatic Payroll Process | PL `sspr_automatic_payroll_process` | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA; RECUPERA INSTANCIA PARA DESPROCESAR NOMINAS | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA; RECUPERA INSTANCIA PARA DESPROCESAR NOMINAS; PERFORM SSPR_CALCULATEVACATION(v_pinstance_vac_id);; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL |
| Botón (PL/pgSQL) | Proceso de Utilidades | Process of Utilities | PL `sspr_process_utility` | No existe configuración utilidades para el año de proceso; Ya existe Utilidades generadas para este período; Debe configurar el período de impuesto a la renta; El período IR configurado no pertenece al año de proceso | No existe configuración utilidades para el año de proceso; Ya existe Utilidades generadas para este período; Debe configurar el período de impuesto a la renta; El período IR configurado no pertenece al año de proceso; VALIDA QUE EXISTA CONFIGURACION PARA EL AÑO DE PROCESO; Revisa si existe una Utilidad para el perìodo ejecutado |
| Botón (PL/pgSQL) | Préstamos Cambio de Estado | Apply Loan | PL `sspr_change_status` | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN |
| Botón (PL/pgSQL) | Reactivar | Reactive | PL `sspr_reactiveloan` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Reactivar | Reactivate | PL `sspr_oti_reactivate` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Reactivar Proceso | Process Reactive | PL `sspr_leave_reactive` | Cannot Reactive, Transaction is add to vacations and have related payroll; OBTENGO EL PERIODO RELACIONADO A ESE PERMISO; VALIDO SI EXISTE UNA NOMINA PROCESADA PARA ESE PERIODO | Cannot Reactive, Transaction is add to vacations and have related payroll; OBTENGO EL PERIODO RELACIONADO A ESE PERMISO; VALIDO SI EXISTE UNA NOMINA PROCESADA PARA ESE PERIODO |
| Botón (PL/pgSQL) | Renovación | Renewal | PL `sspr_renewal` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Informe (servlet) | Archivo de Variación de Extras IESS | IESS Extras Variation File | Java `ArchVariationSalaryCSV` | Proceso Openbravo registro `adOrgId` | Proceso Openbravo registro `adOrgId` |
| Informe (servlet) | Archivo Pago Banco Pichincha TXT | File Payment Pichincha Bank TXT | Java `ArchPaymentPichinchaBankTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Informe (servlet) | Archivo Pago Banco Rumiñahui TXT | Archive Payment Ruminahui Bank TXT | Java `ArchivePayrollPaymentRuminahuiBankTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Informe (servlet) | Generar Formulario 107 Xml | Generate Formulary 107 Xml | Java `Formulary107_xml` | Proceso Openbravo registro `cYearId` | Proceso Openbravo registro `cYearId` |
| Informe (servlet) | Modificar Salario CSV | Modify Salary CSV | Java `ModifySalaryCSV` | Proceso Openbravo registro `cPeriodId` | Proceso Openbravo registro `cPeriodId` |
| Informe (servlet) | Pago Archivo Banco Central TXT | Archive Payment Central Bank TXT | Java `ArchPaymentCtralBankTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Informe (servlet) | Pago Archivo Banco General Rumiñahui Utilidades TXT | Payment Archive BanK General Ruminahui Utilities TXT | Java `ArchivePaymentUtilitiesRuminahuiBankTXT` | Proceso Openbravo registro `cYearId` | Proceso Openbravo registro `cYearId` |
| Informe (servlet) | Reporte Utilidades CSV | CSV Utilities Report | Java `UtilitiesCSV` | Genera PDF desde JRXML `—`; contexto sesión `—`. | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| Proceso / otro | Amortización Préstamos | Amortization Loans | — | — | — |
| Proceso / otro | Archivo variación salarial | File variation salary | — | — | — |
| Proceso / otro | Banco | Bank | — | — | — |
| Proceso / otro | Cheque de Pago | Paycheck | — | Paycheck | — |
| Proceso / otro | Cronograma de Vacaciones | Vacation Schedule | — | — | — |
| Proceso / otro | Deposito a Banco | Deposit Bank | — | Deposit Bank | — |
| Proceso / otro | Detailed Payroll Cost | Detailed Payroll Cost | — | — | — |
| Proceso / otro | Detalle Acumulado Decimo 4to Resumido por Centro de Costo | Accumulated Detail Fourteenth Summarized by Cost Center | — | Accumulated Detail Fourteenth Summarized by Cost Center | — |
| Proceso / otro | Detalle Cargo Concepto | Detail Paid by Concept | — | Detail Paid by Concept | — |
| Proceso / otro | Detalle de Cuotas Prestamos por Centros de Costos | Payment Details Loans by Cost Center | — | Payment Details Loans by Cost Center | — |
| Proceso / otro | Detalle de Provisión de vacaciones resumida por Centro de Costos | Detail of Vacation Provision Summarized by cost center | — | Detail of Vacation Provision Summarized by cost center | — |
| Proceso / otro | Detalle General de Empleados | General Employees Detail | — | General Employees Detail | — |
| Proceso / otro | Detalle nómina Banco | Payroll Bank Detail | — | Payroll Bank Detail | — |
| Proceso / otro | Detalle Prestamos | Detailed Loans | — | — | — |
| Proceso / otro | Estado de Cuenta de Vacaciones por Empleado | Vacation Statement by Employee | — | Vacation Statement by Employee | — |
| Proceso / otro | Extras Resumidos | Extras Summarized | — | Extras Summarized | — |
| Proceso / otro | Formato Décimo Cuarto | 14th Remuneration Format | — | — | — |
| Proceso / otro | General Report of Family Responsibilities | General Report of Family Responsibilities | — | General Report of Family Responsibilities | — |
| Proceso / otro | Generar Formulario 101 - Costos Empleado | Generate Formulary 101 - Cost Employee | — | — | — |
| Proceso / otro | Importe a Cobrar - RVA | Amounts Receivable - RVA | — | — | — |
| Proceso / otro | Importe a Cobrar Décimo Tercero por categoría de empleado | Amounts Receivable - 13th remuneration for employee category | — | — | — |
| Proceso / otro | Importes a cobrar Décimo Cuarto por categoría de empleado | Amounts Receivable - 14th remuneration for employee category | — | — | — |
| Proceso / otro | Informe de Utilidades | Report of Utilities | — | Report of Utilities | — |
| Proceso / otro | Informe Impuesto a la Renta | Report IncomeTax | — | Report IncomeTax | — |
| Proceso / otro | Ingreso por Permanencia | Amounts Receivable - Residence | — | Amounts Receivable - Residence | — |
| Proceso / otro | Ingresos - Empleados por Categoría | Amounts Receivable - Payroll Employee Category | — | — | — |
| Proceso / otro | Liquidación de haberes por proyecto | Salary liquidation by project | — | — | — |
| Proceso / otro | Modificar Salario | Modify Salary | — | — | — |
| Proceso / otro | Monto total Decimocuarta Bono | Total Amount Fourteenth Bonus | — | — | — |
| Proceso / otro | Nomina General Detallada | General Payroll Detailed | — | General Payroll Detailed | — |
| Proceso / otro | Nómina avanzada Individual | Individual Payroll Advance | — | Individual Payroll Advance | — |
| Proceso / otro | Nómina General | General Payroll | — | — | — |
| Proceso / otro | Nómina General Detallado por Centro de Costo | General Payroll Detailed By Cost Center | — | General Payroll Detailed By Cost Center | — |
| Proceso / otro | Nómina Individual | Individual Payroll | — | Individual Payroll | — |
| Proceso / otro | Pago Archivo Banco Central | Archive Payment Central Bank | — | — | — |
| Proceso / otro | Plantilla base imponible  impuesto a la renta | Taxable Base Income Tax | — | — | — |
| Proceso / otro | Provisiones | Provisions | — | Provisions | — |
| Proceso / otro | Reporte Acumulado de Décimo Cuarto | Accumulated Fourteenth Report | — | Accumulated Fourteenth Report | — |
| Proceso / otro | Reporte Acumulado de Décimo Tercero | Accumulated Report of Thirteenth | — | Accumulated Report of Thirteenth | — |
| Proceso / otro | Reporte de Fondos de Reserva | Reserve Fund Report | — | Reserve Fund Report | — |
| Proceso / otro | Reporte Detallado de Vacaciones | Detailed Vacations | — | — | — |
| Proceso / otro | Reporte Formulario Individual 107 | Report Individual Formulary 107 | — | — | — |
| Proceso / otro | Reporte General Formulario 107 | Report General Formulary 107 | — | — | — |
| Proceso / otro | Reporte Pago de Utilidades Banco del Pacifico | Report Utilitis Pacific Bank | — | — | — |
| Proceso / otro | Reporte pago nómina Banco Pacifico | Payment Payroll Pacific Bank | — | — | — |
| Proceso / otro | Reporte Resumen de Vacaciones | Summary Vacations | — | — | — |
| Proceso / otro | Rerpote de Vacaciones tomadas por centro de costos | Rerpot of Vacation taken by cost center | — | Rerpot of Vacation taken by cost center | — |
| Proceso / otro | Resumen Definitivo de Liquidación | Definitive Summary of Liquidation | — | — | — |
| Proceso / otro | Rol Empleados - Firmas | Payroll Firms | — | Payroll Firms | — |
| Proceso / otro | Rol Individual - Nómina Fondos de Reserva | Individual Payroll Reserve Funds | — | Individual Payroll Reserve Funds | — |
| Proceso / otro | Rol Mensual Detallado | Detailed Monthly Role | — | Detailed Monthly Role | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Detalle Acumulado Decimo 3ro Resumido por Centro de Costo | Accumulated Detail Thirteenth Summarized by Cost Center | Report Accumulated Detail Thirteenth | *(OBUIAPP / manual)* | Accumulated Detail Thirteenth Summarized by Cost Center | — |
| Reporte | GENERIC - FINAL SETTLEMENT | GENERIC - FINAL SETTLEMENT | GENERIC - FINAL SETTLEMENT | Java `Sspr_ReportPrintFinalSettlement` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_process/Sspr_ReportPrintFinalSettlement.java` |
| Reporte | Impresión de Contrato | PRINT CONTRACT | PRINT CONTRACT | Java `ReportContractType` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.jrxml`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.java` |
| Reporte | Imprimir Aprovación de Permiso | Print Approvation Leave | Print Approvation Leave | Java `ApprovationLeave` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/ApprovationLeave.java` |
| Reporte | Imprimir Aprovación de Permiso Emp | Print Approvation Leave Emp | Print Approvation Leave Emp | Java `ApprovationLeaveE` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/ApprovationLeaveE.java` |
| Reporte | Imprimir Liquidación final | Print Final Settlement | PRINT  SETTLEMENT | Java `Rpt_FinalSettlement` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement.jrxml`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement.java` |
| Reporte | Imprimir Solicitud de Empleado | Print Request Leave | PRINT LEAVE | Java `Rpt_RequestLeave` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestLeave.jrxml`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestLeave.java` |
| Reporte | Imprimir Solicitud Préstamo | Print Request Loan | PRINT LOANS | Java `RptRequestLoan` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/ad_Reports/RptRequestLoan.jrxml`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/RptRequestLoan.java` |
| Reporte | Reporte de Gastos personales. | Personal expenses report | Personal expenses report | *(OBUIAPP / manual)* | Personal expenses report | — |
| Reporte | Reporte General del Formulario 107 por mes | Report General Formulary 107 by Month | Report General Formulary 107 by Month | *(OBUIAPP / manual)* | — | — |
| Reporte | Request Leave Print | Request Leave Print | Request Leave Print | Java `RequestLeave` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/ad_Reports/RequestLeave.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 96**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **11**; archivos `*.jrxml` en el repo = **96**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | Detalle Acumulado Decimo 3ro Resumido por Centro de Costo | `Report Accumulated Detail Thirteenth` | — | *(ver AD_PROCESS_PARA / servlet)* | Accumulated Detail Thirteenth Summarized by Cost Center |
| 2 | GENERIC - FINAL SETTLEMENT | `GENERIC - FINAL SETTLEMENT` | Java `Sspr_ReportPrintFinalSettlement`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | GENERIC - FINAL SETTLEMENT |
| 3 | Impresión de Contrato | `PRINT CONTRACT` | Java `ReportContractType`; JRXML `com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.jrxml` | *(ver AD_PROCESS_PARA / servlet)* | Print of different contract type by employee. JRXML: `com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.jrxml` |
| 4 | Imprimir Aprovación de Permiso | `Print Approvation Leave` | Java `ApprovationLeave`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Print Approvation Leave |
| 5 | Imprimir Aprovación de Permiso Emp | `Print Approvation Leave Emp` | Java `ApprovationLeaveE`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Print Approvation Leave Emp |
| 6 | Imprimir Liquidación final | `PRINT  SETTLEMENT` | Java `Rpt_FinalSettlement`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Process to print final settlement |
| 7 | Imprimir Solicitud de Empleado | `PRINT LEAVE` | Java `Rpt_RequestLeave`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Print Request Leave |
| 8 | Imprimir Solicitud Préstamo | `PRINT LOANS` | Java `RptRequestLoan`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Process to print request loan |
| 9 | Reporte de Gastos personales. | `Personal expenses report` | — | *(ver AD_PROCESS_PARA / servlet)* | Personal expenses report |
| 10 | Reporte General del Formulario 107 por mes | `Report General Formulary 107 by Month` | — | *(ver AD_PROCESS_PARA / servlet)* | Report General Formulary 107 by Month |
| 11 | Request Leave Print | `Request Leave Print` | Java `RequestLeave`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Request Leave Print |

### Plantillas sin proceso en diccionario

- `src/com/sidesoft/hrm/payroll/ad_Reports/Amount_decimo_cuarto_lab.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/DetailedMonthlyRole.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/GeneralPayroll.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/GeneralPayrollByCostCenter.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/GeneralPayrollCost.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/GeneralPayroll_4.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/ReportUtilitybyEmployee.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RequestLeaveCommission.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RequestLeaveDomesticCalamity.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RequestLeaveOccasional.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RequestLeaveVacation.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RequestLeaveVacationCustom.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptPR_PayrollGeneral.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptRequestLoan.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_AccumulatedFourteenthByCostCenter.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_AccumulatedThirteenthByCostCenter.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_Fourteenth.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_GeneralFormulary107ByMonth.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_LiquidationDC.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_LiquidationDT.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_LiquidationVC.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_PersonalExpensesReport.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_ReserveFundReport.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_SubReportFourteenth.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_Thirteenth.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_VacationStatementByEmployee.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/RptSspr_VacationsByCostCenter.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_14thRemuneration.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_AmortizationLoans.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_AmountsReceivable.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_AmountsReceivable_13thRemuneration.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_AmountsReceivable_14thRemuneration.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_AmountsReceivable_RVA.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_AmountsReceivable_Residence.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_ArchivePaymentCentralBank.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_ArchiveVariationSalary.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_Banks.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_DepositBank.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_Detail_PaidByConcept.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_Employee_Detail.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement1.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlementCont.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlementIN.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlementOUT.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_GeneralDetailFamilyResponsabilities.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_General_Employee_Detail.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_General_Employee_Detail_Reingresos.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollIEgr.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollIEgr2.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollIEgr_FReserva.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollITot.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollImportePatronal.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollImportePatronal2.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollIng.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollIng2.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollIng_FReserva.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollObservation.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollObservation2.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollTot.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayrollTot_FReserva.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_IndividualPayroll_FReserva.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_LoansDetailByCostCenter.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_ModifySalary.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_PR_SingelPayroll.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_PR_SubSinglePayroll.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_PaymentCheck.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_PayrollBankDetailed.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_PayrollFirm.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_Payroll_Pacific_Bank.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_ProvisionPayroll.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_ProvisionsPayroll.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_ReportCenter.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestLeave.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestVacactions.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_Salary_Liquidation_By_Project.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_Sspr_Vacation_Cancelation.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_SummaryLiquidation.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_Taxable_Base_Income_Tax.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_UtilitiesEmployee.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_Utilitis_Pacific_Bank.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_VacationSchedule.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_VacationsSummary.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_Vacationsdetail.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_XtrasSummarized.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_loansdetail.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rptc_Formulary101Gen.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rptc_GeneralFormulary107.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rptc_IndividualFormulary107.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rptm_IndividualPayroll.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rptm_IndividualPayroll2.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Rptm_IndividualPayrollNomina.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/Sspr_DetailVacationProvisionSummarizedByCostCenter.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/VacationRequestAuthReport.jrxml`
- `src/com/sidesoft/hrm/payroll/ad_Reports/VacationRequestAuthReport_resume.jrxml`
- `src/com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Sspr_ValidateContracPosition` | There is already an active position | There is already an active position | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_CifMustEndWith` | Ruc Company must end with 00 #. | Ruc Company must end with 00 #. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_general_configuration` | General Configuration - Month Days | General Configuration - Month Days | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_leave_delete` | You can not removed request leave is approved | You can not removed request leave is approved | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_ProceseedPosted` | The record can not be deleted, registration completed or posted. | The record can not be deleted, registration completed or posted. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_partner_liquidation` | Field employee is mandatory | Field employee is mandatory | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_MustBeNumeric` | Must be numeric the fields: Taxid, Ruc Company | Must be numeric the fields: Taxid, Ruc Company | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_ValidateIncometax` | Existe un concepto seleccionado con este atributo | Existe un concepto seleccionado con este atributo | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_RowsInsertedwarning` | No existe nómina anterior al periodo, el valor para “ultimo ingreso” será igual a cero - fila/s añadida/s | No existe nómina anterior al periodo, el valor para “ultimo ingreso” será igual a cero - fila/s añadida/s | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_contract_liquidation` | Contract is not final settlement | Contract is not final settlement | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_label_RequestLeaveVacation_Authorized` | Authorized | Authorized | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_ValidateReactiveLoan` | This request can not be reactivated because it has lines in the Canceled state. | This request can not be reactivated because it has lines in the Canceled state. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_accounting_payroll` | You cannot unprocess, payroll is accounted | You cannot unprocess, payroll is accounted | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_InfoPartner` | The CIF / NIF and Fiscal Name fields are mandatory. | The CIF / NIF and Fiscal Name fields are mandatory. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_DuplicatePeriod` | No se puede guardar este registro, ya existe un registro con el mismo Periodo | No se puede guardar este registro, ya existe un registro con el mismo Periodo | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_INACTIVECONCEPT` | You cannot create or modify records if the laboral concept is inactive. | You cannot create or modify records if the laboral concept is inactive. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_ValidateLineEvolutionSalary` | No lines of Salary Evolution were found. | No lines of Salary Evolution were found. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_noaccountcategory` | No configured account for the account category. | No configured account for the account category. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_DigitVerfied` | Incorrect: Ruc Company o Taxid | Incorrect: Ruc Company o Taxid | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_NoNormalPayroll` | No normal payroll found | No normal payroll found | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_CifDigitLocation` | Ruc Company location incorrect code | Ruc Company location incorrect code | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_ValidateRefundIess` | If you selected the field 'IESS Reserve Funds', you must configure the 'Concept' field. | If you selected the field 'IESS Reserve Funds', you must configure the 'Concept' field. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_ValidateConepts` | The concepts of the fields: Thirteenth and Fourteenth must be different. | The concepts of the fields: Thirteenth and Fourteenth must be different. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_AdvancePayment` | The advance payment must be less or equal to the amount. | The advance payment must be less or equal to the amount. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_EndStartPeriod` | End Period must be greater than Start Period. | End Period must be greater than Start Period. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_readmission` | Can not insert / update. There is a record with the Start date less than the inserted date and the Final date is null. | Can not insert / update. There is a record with the Start date less than the inserted date and the Final date is null. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_NoConceptAcct` | No configured account for the Concept. | No configured account for the Concept. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_label_RequestLeaveVacation_HumanTalentCoordinator` | Human Talent Coordinator | Human Talent Coordinator | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_ErrorExpireEvolutionSalary` | You can not have more than 1 line of Salary Evolution without Expiring. | You can not have more than 1 line of Salary Evolution without Expiring. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_FormulaConceptNoAmounts` | The Concepts of type Formula are not be able to have any amount. | The Concepts of type Formula are not be able to have any amount. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_loans_delete` | You can not removed request is approved | You can not removed request is approved | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_payroll_liquidation` | This payroll is attached to  liquidation | This payroll is attached to  liquidation | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_payroll_auto_msg` | No se puede eliminar esta Nómina Automática porque existen nóminas generadas asociadas | No se puede eliminar esta Nómina Automática porque existen nóminas generadas asociadas | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_ConceptNoAffectation` | It is not possible to add a Concept with affectation type No. | It is not possible to add a Concept with affectation type No. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_hour_work_null` | Not exist number working hours | Not exist number working hours | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_validate_payroll_documenttype` | No document type found for payroll | No document type found for payroll | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_Message` | Set up a budget item | Set up a budget item | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_NifMustBeLengthNumeric` | Iincorrect: Ruc Company or Taxid | Iincorrect: Ruc Company or Taxid | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_NoSettlementConfig` | No Settlement Configuration founded | No Settlement Configuration founded | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_vacation_delete` | You can not delete | You can not delete | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspr_ValidateUpdateSalary` | The date of the contract must be less than or equal to the date of the Salary Evolution. | The date of the contract must be less than or equal to the date of the Salary Evolution. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_ConceptInUse` | The Concept is being used in a formula. | The Concept is being used in a formula. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_ispayroll_unique` | Partner can not have two active accounts for payroll | Partner can not have two active accounts for payroll | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPR_NoSettlement` | No Settlement founded | No Settlement founded | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspr_val_concepttype` | Fields concept formulates is mandatory | Fields concept formulates is mandatory | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `FieldReasonNull` | Employee has no end of period reason defined in labor contract. | Employee has no end of period reason defined in labor contract. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye clases Java como `ConceptInfo` y `DocLine_Payroll` que implementan la lógica de negocio y manejan las interacciones con la base de datos, facilitando así la integración y el procesamiento de información de nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.hrm.payroll`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ConceptInfo` | accounting | — | — | `src/com/sidesoft/hrm/payroll/accounting/ConceptInfo.java` |
| `DocLine_Payroll` | accounting | DocLine | — | `src/com/sidesoft/hrm/payroll/accounting/DocLine_Payroll.java` |
| `DocLine_Settlement` | accounting | DocLine | — | `src/com/sidesoft/hrm/payroll/accounting/DocLine_Settlement.java` |
| `DocPayroll` | accounting | AcctServer | — | `src/com/sidesoft/hrm/payroll/accounting/DocPayroll.java` |
| `DocSettlement` | accounting | AcctServer | — | `src/com/sidesoft/hrm/payroll/accounting/DocSettlement.java` |
| `Sspr_AdvancePayment` | action_handler | BaseProcessActionHandler | — | `src/com/sidesoft/hrm/payroll/action_handler/Sspr_AdvancePayment.java` |
| `Sspr_PreCancellation` | action_handler | BaseProcessActionHandler | — | `src/com/sidesoft/hrm/payroll/action_handler/Sspr_PreCancellation.java` |
| `ApprovationLeave` | ad_Reports | HttpSecureAppServlet | — | `src/com/sidesoft/hrm/payroll/ad_Reports/ApprovationLeave.java` |
| `ApprovationLeaveE` | ad_Reports | HttpSecureAppServlet | — | `src/com/sidesoft/hrm/payroll/ad_Reports/ApprovationLeaveE.java` |
| `RequestLeave` | ad_Reports | HttpSecureAppServlet | — | `src/com/sidesoft/hrm/payroll/ad_Reports/RequestLeave.java` |
| `RptRequestLoan` | ad_Reports | HttpSecureAppServlet | — | `src/com/sidesoft/hrm/payroll/ad_Reports/RptRequestLoan.java` |
| `Rpt_FinalSettlement` | ad_Reports | HttpSecureAppServlet | — | `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement.java` |
| `Rpt_RequestLeave` | ad_Reports | HttpSecureAppServlet | — | `src/com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestLeave.java` |
| `Add_Concept` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/Add_Concept.java` |
| `Add_Operation` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/Add_Operation.java` |
| `Add_contract` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/Add_contract.java` |
| `CalcAge` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/CalcAge.java` |
| `Doctype_Settlement` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/Doctype_Settlement.java` |
| `OtherTaxIncomeEmployee` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/OtherTaxIncomeEmployee.java` |
| `SSPR_CheckTS` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/SSPR_CheckTS.java` |
| `SS_IDcompers` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/SS_IDcompers.java` |
| `SS_LeaveCategory` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/SS_LeaveCategory.java` |
| `SS_LeaveType` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/SS_LeaveType.java` |
| `SS_ValidateHour` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/SS_ValidateHour.java` |
| `SearchBPartner` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/SearchBPartner.java` |
| `SumTotal` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/SumTotal.java` |
| `Timetoamount` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/Timetoamount.java` |
| `UpdateDateLeave` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/UpdateDateLeave.java` |
| `UptadeLoanTotalBalance` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/ad_callouts/UptadeLoanTotalBalance.java` |
| `YearHelper` | ad_callouts | — | — | `src/com/sidesoft/hrm/payroll/ad_callouts/YearHelper.java` |
| `ActuarialCalculationStudy` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/ad_process/ActuarialCalculationStudy.java` |
| `ConceptAmountExcel` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/ad_process/ConceptAmountExcel.java` |
| `ConceptAmountHourExcel` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/ad_process/ConceptAmountHourExcel.java` |
| `ImportEvolutionSalaryExcell` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/ad_process/ImportEvolutionSalaryExcell.java` |
| `ImportRequestLeave` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/ad_process/ImportRequestLeave.java` |
| `OtherTaxIncomeLoadLines` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/ad_process/OtherTaxIncomeLoadLines.java` |
| `Sspr_AutomaticPayroll` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/ad_process/Sspr_AutomaticPayroll.java` |
| `Sspr_FinalSettlement` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/ad_process/Sspr_FinalSettlement.java` |
| `Sspr_ReportPrintFinalSettlement` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/ad_process/Sspr_ReportPrintFinalSettlement.java` |
| `ArchPaymentCtralBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchPaymentCtralBankTXT.java` |
| `ArchPaymentPichinchaBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchPaymentPichinchaBankTXT.java` |
| `ArchPayrollGuayaquilBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchPayrollGuayaquilBankTXT.java` |
| `ArchTransferPayrollBankAustro` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchTransferPayrollBankAustro.java` |
| `ArchTransferUtilitesBankAustro` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchTransferUtilitesBankAustro.java` |
| `ArchVariationSalaryCSV` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchVariationSalaryCSV.java` |
| `ArchivePaymentProdubancoBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentProdubancoBankTXT.java` |
| `ArchivePaymentTenthProdubanco` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentTenthProdubanco.java` |
| `ArchivePaymentUtilitiesProdubanco` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentUtilitiesProdubanco.java` |
| `ArchivePaymentUtilitiesRuminahuiBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePaymentUtilitiesRuminahuiBankTXT.java` |
| `ArchivePayrollPaymentRuminahuiBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ArchivePayrollPaymentRuminahuiBankTXT.java` |
| `ModifySalaryCSV` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/ModifySalaryCSV.java` |
| `UtilitiesCSV` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_txt/UtilitiesCSV.java` |
| `Formulary107_xml` | create_xml | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/create_xml/Formulary107_xml.java` |
| `OtherTaxIncomeBlockRecord` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/hrm/payroll/event/OtherTaxIncomeBlockRecord.java` |
| `SsprSettlementDataEventHandler` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/event/SsprSettlementDataEventHandler.java` |
| `SsprSettlementLineEventHandler` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/event/SsprSettlementLineEventHandler.java` |
| `SsprUtilitiesEventListener` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/event/SsprUtilitiesEventListener.java` |
| `UpdateBirthdayEmployeePREvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/event/UpdateBirthdayEmployeePREvent.java` |
| `UpdateSequenceSettlementEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/event/UpdateSequenceSettlementEvent.java` |
| `ValidateConeptEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/event/ValidateConeptEvent.java` |
| `ValidateContractLiquidated` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/hrm/payroll/event/ValidateContractLiquidated.java` |
| `ValidateContractPositionEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/event/ValidateContractPositionEvent.java` |
| `ValidateDateContract` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/hrm/payroll/event/ValidateDateContract.java` |
| `ValidateDateIessRateLine` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/hrm/payroll/event/ValidateDateIessRateLine.java` |
| `ValidateHourDays` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/hrm/payroll/event/ValidateHourDays.java` |
| `ValidateIspayroll` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/hrm/payroll/event/ValidateIspayroll.java` |
| `ValidateReadmission` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/hrm/payroll/event/ValidateReadmission.java` |
| `ReportContractType` | reportcontracttype | HttpSecureAppServlet | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSPR_BPARTNER_RFIESS_TRG` | `c_bpartner` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_CONCEPT_AMOUNT_TRG` | `sspr_concept_amount` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_COPYPOSITION_TRG` | `sspr_position` | after INSERT/DELETE | raise exception '%' , 'ID = ' || V_NewPositionID; |
| Trigger `SSPR_COSTEMPLOYEE_TRG` | `sspr_costemployeeline` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_C_BPARTNER_TRG` | `c_bpartner` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_DELETEPOSITION_TRG` | `sspr_position` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_EMPLOYEE_DEFAULT` | `c_bpartner` | before INSERT/UPDATE | Asignamos los valores por defecto para empleados |
| Trigger `SSPR_LEAVEDELETE_TRG` | `sspr_leave_emp` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_LEAVEVALIDATEVAC_TRG1` | `sspr_leave_emp` | before INSERT/UPDATE | error= campo tipo vacaciones es obligatorio |
| Trigger `SSPR_LIQUIDATION_CONTRACT_TRG` | `c_bpartner` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_LOANS_TRG` | `sspr_line_loans` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_PAYROLL_AUT_CREATE_TRG` | `sspr_payroll_aut` | before INSERT | Verifica si ya existe otro registro con el mismo C_Period_ID |
| Trigger `SSPR_PAYROLL_TICK_CONCEPT_TRG` | `sspr_payroll_ticket_concept` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_PERIOD_CONCEPT_TRG` | `sspr_period_concept` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_PROLLTEM_LINES_TRG` | `sspr_prolltem_lines` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_SUPP_DATA_TAXIDBP_TRG` | `sspr_supplementary_data` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_SUPP_DATA_TAXIDORG_TRG` | `sspr_supplementary_data` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_SUPP_DATA_TRG` | `sspr_supplementary_data` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_UPDATEENTRYDATE_TRG` | `sspr_contract` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPR_VACATIONS_VAL_ADIC_TRG` | `sspr_vacations` | before INSERT/UPDATE | recalcula solo cuando cambian los campos relevantes |
| Trigger `SSPR_VALIDACOSTDEDUCTIBLE_TRG` | `sspr_costemployeeline` | before INSERT/UPDATE | VALIDO SI EL TERCERO TIENE CONFIGURADO ALGUNA DISCAPACIDAD; OBTENGO MONTO CONFIGURADO PARA EL TIPO DE DEDUCIBLE |
| Trigger `SSPR_VALIDATEPAYROLL_AUT_TRG` | `sspr_payroll_aut` | before DELETE | Validación reutilizable de campos. |
| Trigger `SSPR_VALIDATEPAYROLL_TRG` | `sspr_payroll` | before DELETE | Validación reutilizable de campos. |
| Trigger `SSPR_VALIDATESETTLEMENT_TRG` | `sspr_settlement` | before DELETE | Validación reutilizable de campos. |
| Trigger `SSPR_VALIDATE_CONCEPT_TRG` | `c_bpartner` | before INSERT/UPDATE | Validación reutilizable de campos. |
| Trigger `SSPR_VALIDATE_INFOPARTNER_TRG` | `c_bpartner` | before INSERT/UPDATE | Validación reutilizable de campos. |
| Trigger `SSPR_VAL_CONCEPTTYPE` | `sspr_concept` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Leave Category` | `Sspr_Leave_Category.sspr_leave_type_id =@sspr_leave_type_id@` |
| AD_VAL_RULE | — | `Doctype Payroll Payment Out` | `C_DocType.DocBaseType IN ('APP', 'ARR') AND ISSOTRX='N'` |
| AD_VAL_RULE | — | `Validate Concept Out` | `sspr_concept.conceptsubtype = 'Out'` |
| AD_VAL_RULE | — | `sspr_concept is utility` | `sspr_concept.concepttypepayroll='UT'` |
| AD_VAL_RULE | — | `Doctype Payroll Certificate` | `C_DocType.ad_table_id in ('E9BD6DF7A6B44E6184288F65159A32CC')` |
| AD_VAL_RULE | — | `Concept In Formulary` | `SSPR_Concept.Conceptsubtype = 'In' AND SSPR_Concept.Sspr_Codeformulary107_ID IS NOT NULL` |
| AD_VAL_RULE | — | `Filter Boss Leave` | `C_BPartner.C_BPartner_ID IN (select sspr_contract. C_BPartner_ID from sspr_contract 
left join sspr_contract_position on` |
| AD_VAL_RULE | — | `Sspr_Payroll_Liquidation_Normal` | `sspr_payroll.ispayroll = 'Y' and sspr_payroll.isliquidation = 'Y' 
and sspr_payroll.sspr_payroll_id in(select sspr_payro` |
| AD_VAL_RULE | — | `Period Payroll` | `C_Period.openclose = 'C'` |
| AD_VAL_RULE | — | `End Period` | `(C_Period.startdate >= (select startdate from c_period cp where cp.c_period_id = @StartPeriod@) or @StartPeriod@ is null` |
| AD_VAL_RULE | — | `Concept Loan` | `sspr_concept.concepttypepayroll='LO'` |
| AD_VAL_RULE | — | `Sspr_ValidateActive` | `C_BPARTNER.ISACTIVE='Y'` |
| AD_VAL_RULE | — | `Payroll DocType` | `C_DocType.DocBaseType='SSPR_PRL'` |
| AD_VAL_RULE | — | `Document Type Settlement` | `c_doctype.AD_TABLE_ID IN (
SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(TABLENAME) = UPPER('sspr_settlement'))` |
| AD_VAL_RULE | — | `sspr_employee_status_leave` | `C_BPARTNER.ISEMPLOYEE = 'Y' and C_BPARTNER.em_sspr_status = 'L' and C_BPARTNER.isactive= 'Y'` |
| AD_VAL_RULE | — | `SSPR_CONCEPT TYPE DATA` | `SSPR_CONCEPT.CONCEPTTYPE='D'` |
| AD_VAL_RULE | — | `Validate Costcenter Leave` | `c_costcenter.c_costcenter_id IN (select em_sspr_costcenter_id from c_bpartner where c_bpartner_id = @c_bpartner_id@)` |
| AD_VAL_RULE | — | `Benefit Dismissal from Org` | `AD_ISORGINCLUDED(@AD_Org_ID@, Sspr_Benefit_Dismissal.AD_Org_ID, @#AD_Client_ID@) <> -1` |
| AD_VAL_RULE | — | `Filter contract employee` | `sspr_contract.c_bpartner_id = @c_bpartner_id@` |
| AD_VAL_RULE | — | `SSPR_SettlementConfig show child organizations` | `AD_ISORGINCLUDED(ad_org.ad_org_id, CASE WHEN (@Parent_AD_Org@ IS NULL OR @Parent_AD_Org@ = '') THEN @AD_ORG_ID@ ELSE @Pa` |
| AD_VAL_RULE | — | `Ssfi_Banktransfer payroll Code` | `code='17'` |
| AD_VAL_RULE | — | `c_bpartner_category_account` | `c_bpartner.em_sspr_category_acct_id = @sspr_category_acct_id@` |
| AD_VAL_RULE | — | `filter document period` | `SSPR_Payroll.C_Period_ID = @c_period_id@` |
| AD_VAL_RULE | — | `Contract Partner` | `sspr_contract_id IN (select sspr_contract_id from sspr_contract where  c_bpartner_id = @c_bpartner_id@)` |
| AD_VAL_RULE | — | `Logged User` | `ad_user.ad_user_id =@#ad_user_id@` |
| AD_VAL_RULE | — | `Loggin User  Parameter` | `AD_User.AD_User_ID = @#AD_User_ID@` |
| AD_VAL_RULE | — | `sspr_employee_inactive` | `C_BPARTNER.ISEMPLOYEE = 'Y'` |
| AD_VAL_RULE | — | `Import Order` | `C_Order.C_DocTypeTarget_id in (select c_doctype_id from c_doctype where name like 'Import Purchase')` |
| AD_VAL_RULE | — | `Concept Affectation Yes` | `SSPR_Concept.affectationtype = 'Y'` |
| AD_VAL_RULE | — | `OtherTaxIncome DocType` | `C_Doctype.AD_Table_ID = '6017C3D7B42348A0A9F2B4FB3C176B86'` |
| AD_VAL_RULE | — | `Employee Disabled` | `C_BPartner.Isemployee='Y' and C_BPartner.EM_SSPR_Status = 'L' and C_BPartner.EM_Sspr_Isdisabled='Y'` |
| AD_VAL_RULE | — | `Employee` | `C_BPartner.IsEmployee = 'Y'` |
| AD_VAL_RULE | — | `Start Period` | `(C_Period.enddate <= (select enddate from c_period cp where cp.c_period_id = @EndPeriod@) or @EndPeriod@ is null)` |
| AD_VAL_RULE | — | `SSPR_ISEMPLOYEE` | `C_BPARTNER.ISEMPLOYEE = 'Y'` |
| AD_VAL_RULE | — | `Doctype Leave emp` | `C_DocType.ad_table_id in ('881B6BC8F33E49168898C1FB4994099F')` |
| AD_VAL_RULE | — | `Employee Active` | `C_BPartner.IsActive = 'Y'` |
| AD_VAL_RULE | — | `Sspr_Payroll_Liquidation_Provision` | `sspr_payroll.ispayroll = 'N' and sspr_payroll.isliquidation = 'Y' 
and sspr_payroll.sspr_payroll_id in(select sspr_payro` |
| AD_VAL_RULE | — | `Validated Concept Formulates` | `sspr_concept.concepttype = 'F' or sspr_concept.concepttype = 'D'` |
| AD_VAL_RULE | — | `Period Open  Control PR` | `C_PERIOD.openclose = 'C'` |
| AD_VAL_RULE | — | `sspr_Employee_Category_Accounting` | `C_BPartner.em_sspr_category_acct_id = @sspr_category_acct_id@` |
| AD_VAL_RULE | — | `Data Concept` | `SSPR_Concept.concepttype='D'` |
| AD_VAL_RULE | — | `SSPR_PERIOD_OPENCLOSE` | `C_PERIOD.OPENCLOSE='C'` |
| AD_VAL_RULE | — | `Sspr_ValidUser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| Java event/validator | `SsprSettlementDataEventHandler` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/event/SsprSettlementDataEventHandler.java`)* |
| Java event/validator | `SsprSettlementLineEventHandler` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/event/SsprSettlementLineEventHandler.java`)* |
| Java event/validator | `SsprUtilitiesEventListener` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/event/SsprUtilitiesEventListener.java`)* |
| Java event/validator | `UpdateBirthdayEmployeePREvent` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/event/UpdateBirthdayEmployeePREvent.java`)* |
| Java event/validator | `UpdateSequenceSettlementEvent` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/event/UpdateSequenceSettlementEvent.java`)* |
| Java event/validator | `ValidateConeptEvent` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/event/ValidateConeptEvent.java`)* |
| Java event/validator | `ValidateContractPositionEvent` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/event/ValidateContractPositionEvent.java`)* |
| Función PL `sspr_acumulativeconcepts` | — | invocación proceso | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; AND TO_CHAR(pe.startdate,'YYYY-MM') = TO_CHAR(oti.process_date,'YYYY-MM') |
| Función PL `sspr_acumulativeconcepts_liq` | — | invocación proceso | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; COMPLETA DIAS MESES DE RETENCION DE IMPUESTO A LA RENTA |
| Función PL `sspr_acumulativeconceptsx` | — | invocación proceso | VALOR DEL CONCEPTO A LA FECHA DEL ROL MAXIMO; VALOR DEL CONCEPTO A LA FECHA DEL ROL MAXIMO - 1 (DEL ROL ANTERIOR); RAISE notice '%', '@sueldo a variado@'||CUR_EMPLEADO.C_BPARTNER_ID||' anterior'||VALOR_ANTERIOR ||' - actual'||VALOR_ACTUAL; |
| Función PL `sspr_asiento_total` | — | invocación proceso | v_Client_ID:=(SELECT ad_client_id from ad_client where name<>'0');; ,v_Org_ID:=(select ad_org_id from ad_org where name<>'0' and ad_client_id = v_Client_ID );--AD_ORG; v_C_Currency:=(select c_currency_id from ad_client where name<>'0'); |
| Función PL `sspr_automatic_payroll_process` | — | invocación proceso | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA |
| Función PL `sspr_calculatevacation` | — | invocación proceso | AND A.C_BPARTNER_ID = '3C0596B9EB424089B757554EF5BCACD6'; ELIMINA REGISTROS MAYORES A LA FECHA DE PROCESO; Cuenta vacaciones que la fecha inicio y fecha fin cumplan 1 año. |
| Función PL `sspr_calculatevacation_inibal` | — | invocación proceso | AND (a.completedays = 'N' or a.completedays is null); AND (completedays = 'N' or completedays is null); INSERTA DIAS ADICIONALES DEL AÑO SALDO INICIAL |
| Función PL `sspr_change_status` | — | invocación proceso | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN |
| Función PL `sspr_change_status_leave` | — | invocación proceso | No tiene vacaciones disponibles días normales; No tiene vacaciones disponibles días adicionales; Cur_vacations.nodays + (Cur_vacations.Noadditionaltotal): |
| Función PL `sspr_complete_settlement` | — | invocación proceso | CAMBIA DE ESTADO NOMINA NORMAL A LIQUIDADO; CAMBIA DE ESTADO NOMINA DE PROVISIONES A LIQUIDADO; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA NORMAL |
| Función PL `sspr_completevacations` | — | invocación proceso | OBTENGO LA FECHA DE CADUCIDAD DEL CONTRATO EN CASO DE LIQUIDACION DE EMPLEADOS; Si la ultima vacación aun no completa el año y el contrato aún no expira.; BUCLE PARA ASIGNAR DIAS DE VACIONES SEGUN AÑOS LABORADOS |
| Función PL `sspr_copy_concept_amounts` | — | invocación proceso | raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-'||v_SSconcept_ID;; raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-test'||v_EndPeriod_ID||'test'; |
| Función PL `sspr_copy_template` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; and em_sspr_category_acct_id = Cur_partner.em_sspr_status; |
| Función PL `sspr_createlineloans` | — | invocación proceso | v_MontoCuota := (v_amount / v_time) + v_MontoInteres; |
| Función PL `sspr_delete_manual_journal` | — | invocación proceso | VALIDO QUE EL ASIENTO NO ESTE CONTABILIZADO; ACTUALIZO CABECERA DE LA NOMINA PARA QUE PERMITA GENERAR EL ASIENTO; OBTENGO REFERENCIA DE LAS LINEAS DEL ASIENTO |
| Función PL `sspr_executeconfigutility` | — | invocación proceso | Begin Calculate of totals - days worked and (child * days worked); Set of value : starting date of the contract of employee; Set of value : endding date of the contract of employee |
| Función PL `sspr_fourteenth` | — | invocación proceso | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO CUARTO Y ASIGNO CONCEPTO CORRESPONDIENTE; CREA CONCEPTO DECIMO TERCERO EN LAS LINEAS |
| Función PL `sspr_fourteenth_liq` | — | invocación proceso | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO CUARTO Y ASIGNO CONCEPTO CORRESPONDIENTE; VALIDO SI EL MONTO DEL CONCEPTO ES DIFERENTE DE 0 PARA INSERTAR LA LINEA |
| Función PL `sspr_generate_manual_journal` | — | invocación proceso | NO HAY NINGUNA REFERENCIA DE TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; NO EXISTE UN ESQUEMA CONTABLE CONFIGURADO PARA LA ORGANIZACION; ** NUEVO  DESARROLLO PARA UNIFICAR EL PROCESO DE CONTABILIDAD DE NOMINA(FERNANDA IGUAMBA)**-- |
| Función PL `sspr_generate_reservefounds` | — | invocación proceso | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_Period P ON CBP.C_BPartner_ID = P.C_BPartner_ID |
| Función PL `sspr_generate_reservefounds2` | — | invocación proceso | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_Period P ON CBP.C_BPartner_ID = P.C_BPartner_ID |
| Función PL `sspr_generateresvfounds2_liq` | — | invocación proceso | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO Y LO ELIMINO; OBTENGO FECHA DE LA NOMINA PARA VALIDAR SI CUMPLE AÑO DE FONDOS DE RESERVA; CREA CONCEPTO FONDOS DE RESERVA EN LAS LINEAS |
| Función PL `sspr_generatesettlementemp` | — | invocación proceso | OBTENGO EL ID DEL EMPLEADO Y FECHA DE SALIDA PARA VALIDAR LA VACACIONES; OBTENGO DIAS PENDIENTES DE VACACIONES DEL EMPLEADO |
| Función PL `sspr_get_business_concept` | — | invocación proceso | WHERE SSPR_Concept_ID = p_SSPR_Concept_ID AND C_Period_ID = p_C_Period_ID; RAISE_APPLICATION_ERROR(-20000, 'INGRESO LOOP 2  '||v_amount);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO LOOP 2'|| v_value||' FORMULA '||v_formula); |
| Función PL `sspr_get_fortnight_concept` | — | invocación proceso | SELECT SSPR_CONCEPT_ID INTO v_Qconcept_ID FROM SSPR_CONCEPT WHERE isfortnight ='Y' limit 1;; raise exception '%', '@Concepto Quincena No existe@';--OBTG:2000-; SELECT SSPR_CONCEPT_ID INTO v_Salary_ID FROM SSPR_CONCEPT WHERE issalary ='Y' limit 1; |
| Función PL `sspr_get_total_income` | — | invocación proceso | FormulaSyntaxError o Division by zero in concept; RAISE_APPLICATION_ERROR(-20000, ' primer select PRUEBA '||p_SSPR_Concept_ID);; WHERE SSPR_Concept_ID = p_SSPR_Concept_ID AND C_Period_ID = p_C_Period_ID |
| Función PL `sspr_incometotals` | — | invocación proceso | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES  PARA  INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES |
| Función PL `sspr_incometotals_liq` | — | invocación proceso | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES  PARA  INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES |
| Función PL `sspr_incometotals_p` | — | invocación proceso | DATOS FINALES  PARA  INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y MENSUALES; TOTAL DEL IESS DE VALORES NO PROYECTABLES, SOLO ACUMULABLES Y MENSUALES |
| Función PL `sspr_leave_paid` | — | invocación proceso | ELimina los registros de la tabla temporal |
| Función PL `sspr_leave_reactive` | — | invocación proceso | Cannot Reactive, Transaction is add to vacations and have related payroll; OBTENGO EL PERIODO RELACIONADO A ESE PERMISO; VALIDO SI EXISTE UNA NOMINA PROCESADA PARA ESE PERIODO |
| Función PL `sspr_leave_taken` | — | invocación proceso | ELimina los registros de la tabla temporal; insert into logs(logs_id, c_bpartner_id , amount,; sspr_payroll_id,v_salarydayslabo,v_salarytotal) |
| Función PL `sspr_lines_settlement` | — | invocación proceso | Date to contract out the payroll provision period; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE LA NOMINA  DE PROVISIONES- PERIODO, ESTADO |
| Función PL `sspr_load_concept_loan` | — | invocación proceso | RAISE NO_DATA_FOUND||Cur_LINELOANS.sshr_loans_id; |
| Función PL `sspr_load_concept_loan2` | — | invocación proceso | IF v_sspr_line_loans_id='21883BD629104868A1CFC659A8805C27' THEN; RAISE NO_DATA_FOUND || Cur_insertemployee.c_bpartner_id; |
| Función PL `sspr_load_concept_loan2_liq` | — | invocación proceso | and to_date(to_char(a.paydate,'dd-MM-yyyy')) between to_date('01-01-2014') and to_date('31-01-2014'); and ((to_char(a.paydate,'dd-MM-yyyy'))>= (to_char(v_StartPeriod,'dd-MM-yyyy')) and to_char(a.paydate,'dd-MM-yyyy')<= (to_char(v_EndPeriod,'dd-MM-yyyy'))); IF v_sspr_line_loans_id='21883BD629104868A1CFC659A8805C27' THEN |
| Función PL `sspr_load_concept_loan3` | — | invocación proceso | raise exception '%' , 'sidesfot ' || p_conceptout_id;; and ((to_char(a.paydate,'dd-MM-yyyy'))>= (to_char(v_StartPeriod,'dd-MM-yyyy')) and to_char(a.paydate,'dd-MM-yyyy')<= (to_char(v_EndPeriod,'dd-MM-yyyy'))); Insert into sspr_concept_amount(SSPR_CONCEPT_AMOUNT_ID,AD_CLIENT_ID,AD_ORG_ID,ISACTIVE,CREATED,CREATEDBY,UPDATED,UPDATEDBY, |
| Función PL `sspr_load_payroll_template` | — | invocación proceso | Insert concepts of the template into period. |
| Función PL `sspr_payrollpayment` | — | invocación proceso | ERROR=NO TIENE TIEPO DE DOCUMENTO CONFIGURADO PARA PAGO DE NOMINA; OBTENGO CUENTA CONFIGURADA PARA PAGOS DE NOMINA; ACTUALIZA ESTADO DEL COBRO A PROCESADO PARA PODER CONTABILIZAR |
| Función PL `sspr_process_payroll` | — | invocación proceso | 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE ORDEN DE PROCESO DE GENERACION DE NOMINA |
| Función PL `sspr_process_utility` | — | invocación proceso | No existe configuración utilidades para el año de proceso; Ya existe Utilidades generadas para este período; Debe configurar el período de impuesto a la renta |
| Función PL `sspr_return_additional_days` | — | invocación proceso | select sspr_return_additional_days('37A26E7FF0EC4AD7A034C1CFBDDB1454','8D27600B5CE44014BDE7ED427C43F05F','DN', '01-09-2015', '31-03-2016') from dual; select sspr_return_additional_days('80548089CC0D49F69E1BB7290E5A6D53','3C6899997D46408E998ECDAB7F83DB50', 'DA', '01-05-2015', '31-01-2016') from dual |
| Función PL `sspr_return_date` | — | invocación proceso | **********************VARIABLES PARA PROCESAMIENTO DE FECHAS*******************************************; RAISE NOTICE '%','RESULT v_dias_del_mes_ant = '  ||to_char(v_dias_del_mes_ant);; RAISE NOTICE '%','RESULT v_cast = '  || v_cast; |
| Función PL `sspr_return_dis_persoexpen` | — | invocación proceso | Retorna valor de gastos deducibles, si no tiene registrado los gastos personales el valor es 0 |
| Función PL `sspr_return_vacationsdays` | — | invocación proceso | select sspr_return_additional_days('8C8DAB9662AB4CA5BE69EF2C7BE67D03','5BB61A167BD343B08F681D0BD2F38C67', 'DA', '01-') from dual; select sspr_return_additional_days('37A26E7FF0EC4AD7A034C1CFBDDB1454','8D27600B5CE44014BDE7ED427C43F05F','DN', '01-09-2015', '31-03-2016') from dual; select sspr_return_vacationsdays('78BEEB13BC81458EB5A958C2362AB9E2','232D654950D34952B898F82CC51273F7', 'DN', '01-05-2015', '29-02-2016') from dual |
| Función PL `sspr_salary_leave` | — | invocación proceso | Error: El proceso subsidio salarial no tiene configurado el concepto de salida en la categoria del permiso; ELimina los registros de la tabla temporal; and (('01-06-2015' between a.stardate and a.enddate or '30-06-2015' between a.stardate and a.enddate) or |
| Función PL `sspr_settl_add_adi` | — | invocación proceso | select coalesce((select round(sum(totalvalue),2) |
| Función PL `sspr_settl_add_payroll` | — | invocación proceso | INSERTO LINEAS CONCEPTOS ROL DE LIQUIDACIONES NORMAL |
| Función PL `sspr_settl_add_per` | — | invocación proceso | This concepts type can not be assigned in; No process desahucio, rate field has no value; If(Cur_benefit_dismissal.value = 'DSH' OR  Cur_benefit_dismissal.value = 'ING')Then |
| Función PL `sspr_settl_add_spe` | — | invocación proceso | This concepts type can not be assigned in; No process desahucio, rate field has no value; OBTENGO EL SALARIO CORRESPONDIENTE DEL EMPLEADO |
| Función PL `sspr_settl_add_tenth` | — | invocación proceso | No exits concept 13TH in payroll provision; No existe configurado el sueldo básico actual para el periodo; NUEVA LOGICA: variables para ajuste de decimo mensualizado |
| Función PL `sspr_thirteenth` | — | invocación proceso | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO TERCERO Y ASIGNO CONCEPTO CORRESPONDIENTE; CREA CONCEPTO DECIMO TERCERO EN LAS LINEAS |
| Función PL `sspr_thirteenth_liq` | — | invocación proceso | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO TERCERO Y ASIGNO CONCEPTO CORRESPONDIENTE; VALIDO SI EL MONTO DEL CONCEPTO ES DIFERENTE DE 0 PARA INSERTAR LA LINEA |
| Función PL `sspr_update_salary` | — | invocación proceso | v_SSconceptIess_ID VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsCompany VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsIess VARCHAR(32); --OBTG:VARCHAR2-- |
| Función PL `sspr_update_salary_liq` | — | invocación proceso | v_SSconceptIess_ID VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsCompany VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsIess VARCHAR(32); --OBTG:VARCHAR2-- |
| Función PL `sspr_update_workingdays` | — | invocación proceso | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; Valida configuracion inicial de dias del mes |
| Función PL `sspr_update_workingdays_liq` | — | invocación proceso | Valida configuracion inicial de dias del mes; v_days := to_number(to_char(v_EndPeriod,'dd'));; VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO |
| Función PL `sspr_updatedateentry` | — | invocación proceso | ACTUALIZO FECHA DE INGRESO DEL EMPLEADO CON LA DEL REINGRESO |
| Función PL `sspr_updateworkeddays` | — | invocación proceso | RAISE_APPLICATION_ERROR(-20000,'@Error: End date this contract is null@');; CALCULO DE NUMERO DE DIAS LABORADOS LIQUIDACION; v_daysliquidation := to_number(to_char(v_enddate_liquidation,'dd')); |
| Función PL `sspr_updateworkeddays_liq` | — | invocación proceso | OBTENGO EL TIPO DE NOMINA Y EMPLEADOsueldo dias; CALCULO DE NUMERO DE DIAS LABORADOS LIQUIDACION; OBTENGO LA FECHA DE CADUCIDAD DEL CONTRATO |
| Función PL `sspr_validareservfound` | — | invocación proceso | from sspr_concept where isreservefunds='Y' limit 1; |
| Función PL `sspr_validareservfound_liq` | — | invocación proceso | from sspr_concept where isreservefunds='Y' limit 1; |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers juegan un rol esencial en la lógica del negocio, ejecutando validaciones automatizadas y ajustes en la base de datos al insertar o modificar registros. Funciones PL vinculadas ofrecen una base robusta para el manejo de procesos complejos y validaciones, garantizando que los datos se mantengan coherentes y en línea con las políticas de la empresa.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSPR_BPARTNER_RFIESS_TRG` | `c_bpartner` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_BPARTNER_RFIESS_TRG.xml` |
| `SSPR_C_BPARTNER_TRG` | `c_bpartner` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_C_BPARTNER_TRG.xml` |
| `SSPR_EMPLOYEE_DEFAULT` | `c_bpartner` | before | INSERT/UPDATE | Asignamos los valores por defecto para empleados | `model/triggers/SSPR_EMPLOYEE_DEFAULT.xml` |
| `SSPR_LIQUIDATION_CONTRACT_TRG` | `c_bpartner` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_LIQUIDATION_CONTRACT_TRG.xml` |
| `SSPR_VALIDATE_CONCEPT_TRG` | `c_bpartner` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SSPR_VALIDATE_CONCEPT_TRG.xml` |
| `SSPR_VALIDATE_INFOPARTNER_TRG` | `c_bpartner` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SSPR_VALIDATE_INFOPARTNER_TRG.xml` |
| `SSPR_VAL_CONCEPTTYPE` | `sspr_concept` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_VAL_CONCEPTTYPE.xml` |
| `SSPR_CONCEPT_AMOUNT_TRG` | `sspr_concept_amount` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_CONCEPT_AMOUNT_TRG.xml` |
| `SSPR_UPDATEENTRYDATE_TRG` | `sspr_contract` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_UPDATEENTRYDATE_TRG.xml` |
| `SSPR_COSTEMPLOYEE_TRG` | `sspr_costemployeeline` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_COSTEMPLOYEE_TRG.xml` |
| `SSPR_VALIDACOSTDEDUCTIBLE_TRG` | `sspr_costemployeeline` | before | INSERT/UPDATE | VALIDO SI EL TERCERO TIENE CONFIGURADO ALGUNA DISCAPACIDAD; OBTENGO MONTO CONFIGURADO PARA EL TIPO DE DEDUCIBLE | `model/triggers/SSPR_VALIDACOSTDEDUCTIBLE_TRG.xml` |
| `SSPR_LEAVEDELETE_TRG` | `sspr_leave_emp` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_LEAVEDELETE_TRG.xml` |
| `SSPR_LEAVEVALIDATEVAC_TRG1` | `sspr_leave_emp` | before | INSERT/UPDATE | error= campo tipo vacaciones es obligatorio | `model/triggers/SSPR_LEAVEVALIDATEVAC_TRG1.xml` |
| `SSPR_LOANS_TRG` | `sspr_line_loans` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_LOANS_TRG.xml` |
| `SSPR_VALIDATEPAYROLL_TRG` | `sspr_payroll` | before | DELETE | Validación reutilizable de campos. | `model/triggers/SSPR_VALIDATEPAYROLL_TRG.xml` |
| `SSPR_PAYROLL_AUT_CREATE_TRG` | `sspr_payroll_aut` | before | INSERT | Verifica si ya existe otro registro con el mismo C_Period_ID | `model/triggers/SSPR_PAYROLL_AUT_CREATE_TRG.xml` |
| `SSPR_VALIDATEPAYROLL_AUT_TRG` | `sspr_payroll_aut` | before | DELETE | Validación reutilizable de campos. | `model/triggers/SSPR_VALIDATEPAYROLL_AUT_TRG.xml` |
| `SSPR_PAYROLL_TICK_CONCEPT_TRG` | `sspr_payroll_ticket_concept` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_PAYROLL_TICK_CONCEPT_TRG.xml` |
| `SSPR_PERIOD_CONCEPT_TRG` | `sspr_period_concept` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_PERIOD_CONCEPT_TRG.xml` |
| `SSPR_COPYPOSITION_TRG` | `sspr_position` | after | INSERT/DELETE | raise exception '%' , 'ID = ' || V_NewPositionID; | `model/triggers/SSPR_COPYPOSITION_TRG.xml` |
| `SSPR_DELETEPOSITION_TRG` | `sspr_position` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_DELETEPOSITION_TRG.xml` |
| `SSPR_PROLLTEM_LINES_TRG` | `sspr_prolltem_lines` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_PROLLTEM_LINES_TRG.xml` |
| `SSPR_VALIDATESETTLEMENT_TRG` | `sspr_settlement` | before | DELETE | Validación reutilizable de campos. | `model/triggers/SSPR_VALIDATESETTLEMENT_TRG.xml` |
| `SSPR_SUPP_DATA_TAXIDBP_TRG` | `sspr_supplementary_data` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_SUPP_DATA_TAXIDBP_TRG.xml` |
| `SSPR_SUPP_DATA_TAXIDORG_TRG` | `sspr_supplementary_data` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_SUPP_DATA_TAXIDORG_TRG.xml` |
| `SSPR_SUPP_DATA_TRG` | `sspr_supplementary_data` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPR_SUPP_DATA_TRG.xml` |
| `SSPR_VACATIONS_VAL_ADIC_TRG` | `sspr_vacations` | before | INSERT/UPDATE | recalcula solo cuando cambian los campos relevantes | `model/triggers/SSPR_VACATIONS_VAL_ADIC_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sspr_acumulativeconcepts` | Cargar Acumulables | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; AND TO_CHAR(pe.startdate,'YYYY-MM') = TO_CHAR(oti.process_date,'YYYY-MM'); INSERTA LIQUIDACIONES PESTA… | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; AND TO_CHAR(pe.startdate,'YYYY-MM') = TO_CHAR(oti.process_date,'YYYY-MM'); INSERTA LIQUIDACIONES PESTAÑA LINEAS Y DATOS ADICIONALES; COMPLETA DIAS MESES DE RETENCION DE IMPUESTO A LA RENTA; and c_bpartner.c_bpartner_id = v_c_bpartner_id | `model/functions/SSPR_ACUMULATIVECONCEPTS.xml` |
| `sspr_acumulativeconcepts_liq` | — | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; COMPLETA DIAS MESES DE RETENCION DE IMPUESTO A LA RENTA; select sspr_concept_id, iscumulative, isproje… | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; COMPLETA DIAS MESES DE RETENCION DE IMPUESTO A LA RENTA; select sspr_concept_id, iscumulative, isprojected, isiess, conceptsubtype; into v_sspr_concept_id, v_iscumulative, v_isprojected, v_isiess, v_conceptsubtype | `model/functions/SSPR_ACUMULATIVECONCEPTS_LIQ.xml` |
| `sspr_acumulativeconceptsx` | — | VALOR DEL CONCEPTO A LA FECHA DEL ROL MAXIMO; VALOR DEL CONCEPTO A LA FECHA DEL ROL MAXIMO - 1 (DEL ROL ANTERIOR); RAISE notice '%', '@sueldo a variado@'||CUR_EMPLEADO.C_BPARTNER_ID||' anterior'||VALOR_ANTERIOR ||' - ac… | VALOR DEL CONCEPTO A LA FECHA DEL ROL MAXIMO; VALOR DEL CONCEPTO A LA FECHA DEL ROL MAXIMO - 1 (DEL ROL ANTERIOR); RAISE notice '%', '@sueldo a variado@'||CUR_EMPLEADO.C_BPARTNER_ID||' anterior'||VALOR_ANTERIOR ||' - actual'||VALOR_ACTUAL;; V_MESSAGE_ACUM := '@sueldo a variado@'|| COALESCE(TO_CHAR((SELECT NAME FROM C_BPARTNER WHERE C_BPARTNER_ID = CUR_EMPLEADO.C_BPARTNER_ID)),'') ||' anterior'||VALOR_ANTERIOR ||' - actual'||VALOR_ACTUAL;; INSERT INTO SSPR_LOG_RENTA VALUES (V_MESSAGE_ACUM);; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | `model/functions/SSPR_ACUMULATIVECONCEPTSX.xml` |
| `sspr_asiento_total` | — | v_Client_ID:=(SELECT ad_client_id from ad_client where name<>'0');; ,v_Org_ID:=(select ad_org_id from ad_org where name<>'0' and ad_client_id = v_Client_ID );--AD_ORG; v_C_Currency:=(select c_currency_id from ad_client… | v_Client_ID:=(SELECT ad_client_id from ad_client where name<>'0');; ,v_Org_ID:=(select ad_org_id from ad_org where name<>'0' and ad_client_id = v_Client_ID );--AD_ORG; v_C_Currency:=(select c_currency_id from ad_client where name<>'0');; insert into ssim_errores values (v_ResultStr||' '||Cur_journal.cuenta||'-'||Cur_journal.tercero );; RETURN v_ResultStr||' '||Cur_journal.cuenta||'-'||Cur_journal.tercero; | `model/functions/SSPR_ASIENTO_TOTAL.xml` |
| `sspr_automatic_payroll_process` | Proceso de Nómina Automático | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA; RECUPERA INSTANCIA PARA DESPROCESAR NOMINAS | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA; RECUPERA INSTANCIA PARA DESPROCESAR NOMINAS; PERFORM SSPR_CALCULATEVACATION(v_pinstance_vac_id);; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL | `model/functions/SSPR_AUTOMATIC_PAYROLL_PROCESS.xml` |
| `sspr_bono_compliance` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_BONO_COMPLIANCE.xml` |
| `sspr_calculatevacation` | Calcular Vacaciones | AND A.C_BPARTNER_ID = '3C0596B9EB424089B757554EF5BCACD6'; ELIMINA REGISTROS MAYORES A LA FECHA DE PROCESO; Cuenta vacaciones que la fecha inicio y fecha fin cumplan 1 año.; En caso de que el empleado no cuente con linea… | AND A.C_BPARTNER_ID = '3C0596B9EB424089B757554EF5BCACD6'; ELIMINA REGISTROS MAYORES A LA FECHA DE PROCESO; Cuenta vacaciones que la fecha inicio y fecha fin cumplan 1 año.; En caso de que el empleado no cuente con lineas, Tomara la fecha de inicio del contrato; OBTENGO LA FECHA DE CADUCIDAD DEL CONTRATO EN CASO DE LIQUIDAC-ION DE EMPLEADOS; VALIDA FECHA FIN DE CONTRATO EN CASO DE SER LIQUIDACIÓN DE EMPLEADOS | `model/functions/SSPR_CALCULATEVACATION.xml` |
| `sspr_calculatevacation_inibal` | — | AND (a.completedays = 'N' or a.completedays is null); AND (completedays = 'N' or completedays is null); INSERTA DIAS ADICIONALES DEL AÑO SALDO INICIAL; REVISA QUE SEA LA ÚLTIMA DE LAS VACACIONES. | AND (a.completedays = 'N' or a.completedays is null); AND (completedays = 'N' or completedays is null); INSERTA DIAS ADICIONALES DEL AÑO SALDO INICIAL; REVISA QUE SEA LA ÚLTIMA DE LAS VACACIONES. | `model/functions/SSPR_CALCULATEVACATION_INIBAL.xml` |
| `sspr_change_status` | Préstamos Cambio de Estado, Aprobar Prestamos | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN | `model/functions/SSPR_CHANGE_STATUS.xml` |
| `sspr_change_status_leave` | Approve | No tiene vacaciones disponibles días normales; No tiene vacaciones disponibles días adicionales; Cur_vacations.nodays + (Cur_vacations.Noadditionaltotal):; VALIDA DIAS DE VACACIONES DISPONIBLES NORMALES | No tiene vacaciones disponibles días normales; No tiene vacaciones disponibles días adicionales; Cur_vacations.nodays + (Cur_vacations.Noadditionaltotal):; VALIDA DIAS DE VACACIONES DISPONIBLES NORMALES; VALIDA DIAS DE VACACIONES DISPONIBLE ADICIONALES; ACTUALIZA DIAS TOMADOS EN LA TABLA DE VACACIONES | `model/functions/SSPR_CHANGE_STATUS_LEAVE.xml` |
| `sspr_codestablishment` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_CODESTABLISHMENT.xml` |
| `sspr_complete_settlement` | Completar Liquidación | CAMBIA DE ESTADO NOMINA NORMAL A LIQUIDADO; CAMBIA DE ESTADO NOMINA DE PROVISIONES A LIQUIDADO; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA NORMAL; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA DE PROVISIONES | CAMBIA DE ESTADO NOMINA NORMAL A LIQUIDADO; CAMBIA DE ESTADO NOMINA DE PROVISIONES A LIQUIDADO; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA NORMAL; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA DE PROVISIONES; and sspr_contract_id = v_sspr_contract_id;; ACTUALIZA DIAS TOMADOS EN LA TABLA DE VACACIONES | `model/functions/SSPR_COMPLETE_SETTLEMENT.xml` |
| `sspr_completevacations` | — | OBTENGO LA FECHA DE CADUCIDAD DEL CONTRATO EN CASO DE LIQUIDACION DE EMPLEADOS; Si la ultima vacación aun no completa el año y el contrato aún no expira.; BUCLE PARA ASIGNAR DIAS DE VACIONES SEGUN AÑOS LABORADOS; v_fech… | OBTENGO LA FECHA DE CADUCIDAD DEL CONTRATO EN CASO DE LIQUIDACION DE EMPLEADOS; Si la ultima vacación aun no completa el año y el contrato aún no expira.; BUCLE PARA ASIGNAR DIAS DE VACIONES SEGUN AÑOS LABORADOS; v_fecha_fin := (v_DateIngEmpleado + INTERVAL '1' year) - 1;; earneddays_add = 0,--Total días ganados adicionales | `model/functions/SSPR_COMPLETEVACATIONS.xml` |
| `sspr_copy_concept_amounts` | Copiar Conceptos | raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-'||v_SSconcept_ID;; raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-test'||v_EndPeriod_ID||'test'; | raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-'||v_SSconcept_ID;; raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-test'||v_EndPeriod_ID||'test'; | `model/functions/SSPR_COPY_CONCEPT_AMOUNTS.xml` |
| `sspr_copy_template` | Copiar Plantilla | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; and em_sspr_category_acct_id = Cur_partner.em_sspr_status; | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; and em_sspr_category_acct_id = Cur_partner.em_sspr_status; | `model/functions/SSPR_COPY_TEMPLATE.xml` |
| `sspr_create_concept_amounts` | Crear Montos de Conceptos | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_CREATE_CONCEPT_AMOUNTS.xml` |
| `sspr_createlineloans` | Crear línea Préstamos | v_MontoCuota := (v_amount / v_time) + v_MontoInteres; | v_MontoCuota := (v_amount / v_time) + v_MontoInteres; | `model/functions/SSPR_CREATELINELOANS.xml` |
| `sspr_currentcontract` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_CURRENTCONTRACT.xml` |
| `sspr_dateadmission` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_DATEADMISSION.xml` |
| `sspr_dateasecondadmission` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_DATEASECONDADMISSION.xml` |
| `sspr_datedeparture` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_DATEDEPARTURE.xml` |
| `sspr_days360` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_DAYS360.xml` |
| `sspr_delete_manual_journal` | Eliminar Diario Manual | VALIDO QUE EL ASIENTO NO ESTE CONTABILIZADO; ACTUALIZO CABECERA DE LA NOMINA PARA QUE PERMITA GENERAR EL ASIENTO; OBTENGO REFERENCIA DE LAS LINEAS DEL ASIENTO; ELIMINO CABECERA Y AGRUPACION DEL ASIENTO | VALIDO QUE EL ASIENTO NO ESTE CONTABILIZADO; ACTUALIZO CABECERA DE LA NOMINA PARA QUE PERMITA GENERAR EL ASIENTO; OBTENGO REFERENCIA DE LAS LINEAS DEL ASIENTO; ELIMINO CABECERA Y AGRUPACION DEL ASIENTO; v_Message := '@RowsInserted@: ' || v_n_insertions || '.'; | `model/functions/SSPR_DELETE_MANUAL_JOURNAL.xml` |
| `sspr_deleteformula` | Borrar fórmula | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_DELETEFORMULA.xml` |
| `sspr_executeconfigutility` | — | Begin Calculate of totals - days worked and (child * days worked); Set of value : starting date of the contract of employee; Set of value : endding date of the contract of employee; UPDATE INDEX IN THE TABLE SSPR_VALUES… | Begin Calculate of totals - days worked and (child * days worked); Set of value : starting date of the contract of employee; Set of value : endding date of the contract of employee; UPDATE INDEX IN THE TABLE SSPR_VALUESINDICESPERIOD; VALIDATED IF EMPLOYEE HAVE LOADS, AND CALCULATE INDEX EMPLOYEE AND LOADS | `model/functions/SSPR_EXECUTECONFIGUTILITY.xml` |
| `sspr_fourteenth` | — | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO CUARTO Y ASIGNO CONCEPTO CORRESPONDIENTE; CREA CONCEPTO DECIMO TERCERO EN LAS… | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO CUARTO Y ASIGNO CONCEPTO CORRESPONDIENTE; CREA CONCEPTO DECIMO TERCERO EN LAS LINEAS | `model/functions/SSPR_FOURTEENTH.xml` |
| `sspr_fourteenth_liq` | — | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO CUARTO Y ASIGNO CONCEPTO CORRESPONDIENTE; VALIDO SI EL MONTO DEL CONCEPTO ES… | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO CUARTO Y ASIGNO CONCEPTO CORRESPONDIENTE; VALIDO SI EL MONTO DEL CONCEPTO ES DIFERENTE DE 0 PARA INSERTAR LA LINEA; CREA CONCEPTO DECIMO TERCERO EN LAS LINEAS; RAISE EXCEPTION '%' ,V_Concept_FT||' '||Cur_Employee.C_BPARTNER_ID||' '||v_Period_ID; | `model/functions/SSPR_FOURTEENTH_LIQ.xml` |
| `sspr_generate_manual_journal` | Generar Datos para Asiento Manual | NO HAY NINGUNA REFERENCIA DE TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; NO EXISTE UN ESQUEMA CONTABLE CONFIGURADO PARA LA ORGANIZACION; ** NUEVO DESARROLLO PARA UNIFICAR EL PROCESO DE CONTABILIDAD DE NOMINA(FERNANDA IGU… | NO HAY NINGUNA REFERENCIA DE TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; NO EXISTE UN ESQUEMA CONTABLE CONFIGURADO PARA LA ORGANIZACION; ** NUEVO  DESARROLLO PARA UNIFICAR EL PROCESO DE CONTABILIDAD DE NOMINA(FERNANDA IGUAMBA)**--; OBTENGO SECUENCIA DEL TIPO DE DOCUMENTO PARA CABECERA DEL ASIENTO; select TO_NUMBER(max(documentno))+1 into v_documento_jb from gl_journalbatch;; VALIDA QUE HAYA DATOS PARA CREAR EL ASIENTO | `model/functions/SSPR_GENERATE_MANUAL_JOURNAL.xml` |
| `sspr_generate_reservefounds` | Fondos de Reserva | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_… | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_Period P ON CBP.C_BPartner_ID = P.C_BPartner_ID; VALIDACIONES PARA OBTENER LOS DIAS  LABORADOS; CREA CONCEPTO FONDOS DE RESERVA EN LAS LINEAS; VALIDO SI ENVIO AL IEES LOS FONDOS DE RESERVA  SEGUN LA CONFIGURACION DEL EMPLEADO | `model/functions/SSPR_GENERATE_RESERVEFOUNDS.xml` |
| `sspr_generate_reservefounds2` | — | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_… | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; LEFT JOIN SSPR_Period P ON CBP.C_BPartner_ID = P.C_BPartner_ID; CREA CONCEPTO FONDOS DE RESERVA EN LAS LINEAS; VALIDO SI ENVIO AL IEES LOS FONDOS DE RESERVA  SEGUN LA CONFIGURACION DEL EMPLEADO; V_Concept_FR:=v_SSconceptIess_ID;--COMENTADO X CAMBIO PARA FONDOS DE CESANTIA | `model/functions/SSPR_GENERATE_RESERVEFOUNDS2.xml` |
| `sspr_generateresvfounds2_liq` | — | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO Y LO ELIMINO; OBTENGO FECHA DE LA NOMINA PARA VALIDAR SI CUMPLE AÑO DE FONDOS DE RESERVA; CREA CONCEPTO FONDOS DE RESERVA E… | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO Y LO ELIMINO; OBTENGO FECHA DE LA NOMINA PARA VALIDAR SI CUMPLE AÑO DE FONDOS DE RESERVA; CREA CONCEPTO FONDOS DE RESERVA EN LAS LINEAS; VALIDO SI ENVIO AL IEES LOS FONDOS DE RESERVA  SEGUN LA CONFIGURACION DEL EMPLEADO; V_Concept_FR:=v_SSconceptIess_ID;--COMENTADO X CAMBIO PARA FONDOS DE CESANTIA | `model/functions/SSPR_GENERATERESVFOUNDS2_LIQ.xml` |
| `sspr_generatesettlementemp` | Generar Liquidación del Empleado | OBTENGO EL ID DEL EMPLEADO Y FECHA DE SALIDA PARA VALIDAR LA VACACIONES; OBTENGO DIAS PENDIENTES DE VACACIONES DEL EMPLEADO | OBTENGO EL ID DEL EMPLEADO Y FECHA DE SALIDA PARA VALIDAR LA VACACIONES; OBTENGO DIAS PENDIENTES DE VACACIONES DEL EMPLEADO | `model/functions/SSPR_GENERATESETTLEMENTEMP.xml` |
| `sspr_get_area` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_GET_AREA.xml` |
| `sspr_get_business_concept` | — | WHERE SSPR_Concept_ID = p_SSPR_Concept_ID AND C_Period_ID = p_C_Period_ID; RAISE_APPLICATION_ERROR(-20000, 'INGRESO LOOP 2 '||v_amount);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO LOOP 2'|| v_value||' FORMULA '||v_formul… | WHERE SSPR_Concept_ID = p_SSPR_Concept_ID AND C_Period_ID = p_C_Period_ID; RAISE_APPLICATION_ERROR(-20000, 'INGRESO LOOP 2  '||v_amount);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO LOOP 2'|| v_value||' FORMULA '||v_formula);; End replacement concept values to amounts.; RAISE notice '%', '@FormulaSyntaxError@'; --OBTG:-20000--*/ | `model/functions/SSPR_GET_BUSINESS_CONCEPT.xml` |
| `sspr_get_fortnight_concept` | Generar Quincena | SELECT SSPR_CONCEPT_ID INTO v_Qconcept_ID FROM SSPR_CONCEPT WHERE isfortnight ='Y' limit 1;; raise exception '%', '@Concepto Quincena No existe@';--OBTG:2000-; SELECT SSPR_CONCEPT_ID INTO v_Salary_ID FROM SSPR_CONCEPT W… | SELECT SSPR_CONCEPT_ID INTO v_Qconcept_ID FROM SSPR_CONCEPT WHERE isfortnight ='Y' limit 1;; raise exception '%', '@Concepto Quincena No existe@';--OBTG:2000-; SELECT SSPR_CONCEPT_ID INTO v_Salary_ID FROM SSPR_CONCEPT WHERE issalary ='Y' limit 1;; raise exception '%', '@Concepto Sueldo No existe@';--OBTG:-2000--; BUSCA EL ID DEL PERIODO ANTERIOR AL SELECCIONADO EN LE PROCESO; raise exception '%', '@Periodo No existe@';--OBTG:-2000-- | `model/functions/SSPR_GET_FORTNIGHT_CONCEPT.xml` |
| `sspr_get_settlementconfig` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_GET_SETTLEMENTCONFIG.xml` |
| `sspr_get_suma_digito` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_GET_SUMA_DIGITO.xml` |
| `sspr_get_total_income` | — | FormulaSyntaxError o Division by zero in concept; RAISE_APPLICATION_ERROR(-20000, ' primer select PRUEBA '||p_SSPR_Concept_ID);; WHERE SSPR_Concept_ID = p_SSPR_Concept_ID AND C_Period_ID = p_C_Period_ID; RAISE_APPLICATI… | FormulaSyntaxError o Division by zero in concept; RAISE_APPLICATION_ERROR(-20000, ' primer select PRUEBA '||p_SSPR_Concept_ID);; WHERE SSPR_Concept_ID = p_SSPR_Concept_ID AND C_Period_ID = p_C_Period_ID; RAISE_APPLICATION_ERROR(-20000, ' primer select '||v_amount);; RAISE_APPLICATION_ERROR(-20000, ' formula '||v_value || ' - ' || p_sspr_payroll_id || ' - ' || p_C_BPartner_ID);; RAISE_APPLICATION_ERROR(-20000, ' segundo select '||v_value); | `model/functions/SSPR_GET_TOTAL_INCOME.xml` |
| `sspr_getcontract` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_GETCONTRACT.xml` |
| `sspr_getdependencies_area` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_GETDEPENDENCIES_AREA.xml` |
| `sspr_getdesahucio` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_GETDESAHUCIO.xml` |
| `sspr_getmax_dateloan` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_GETMAX_DATELOAN.xml` |
| `sspr_incometotals` | Generar Impuesto a la Renta | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES PARA INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES; TOTAL DE INGRESOS ACUMULABLES Y NO PROYECTABLES… | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES  PARA  INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES; TOTAL DE INGRESOS ACUMULABLES Y NO PROYECTABLES Y CON IESS; TOTAL DE INGRESO ACUMULABLES Y NO PROYECTABLES Y SIN IESS; SUM DE INGRESO ACUMULABLES Y NO PROYECTABLES CON Y SIN IESS | `model/functions/SSPR_INCOMETOTALS.xml` |
| `sspr_incometotals_liq` | — | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES PARA INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES; TOTAL DE INGRESOS ACUMULABLES Y NO PROYECTABLES… | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES  PARA  INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES; TOTAL DE INGRESOS ACUMULABLES Y NO PROYECTABLES Y CON IESS; TOTAL DE INGRESO ACUMULABLES Y NO PROYECTABLES Y SIN IESS; SUM DE INGRESO ACUMULABLES Y NO PROYECTABLES CON Y SIN IESS | `model/functions/SSPR_INCOMETOTALS_LIQ.xml` |
| `sspr_incometotals_p` | — | DATOS FINALES PARA INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y MENSUALES; TOTAL DEL IESS DE VALORES NO PROYECTABLES, SOLO ACUMULABLES Y MENSUALES; BASE 2 (TOTAL INGRESO SOLO ACUMULABLES Y MENSUALES - T… | DATOS FINALES  PARA  INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y MENSUALES; TOTAL DEL IESS DE VALORES NO PROYECTABLES, SOLO ACUMULABLES Y MENSUALES; BASE 2 (TOTAL INGRESO  SOLO ACUMULABLES Y MENSUALES - TOTAL DEL IESS); IF  QUE CALCULA EL IMPUESTO A LA RENTA DE LA BASE 1; IF QUE CALCULA EL IMPUESTO A LA RENTA DE LA BASE TOTAL | `model/functions/SSPR_INCOMETOTALS_P.xml` |
| `sspr_leave_paid` | — | ELimina los registros de la tabla temporal | ELimina los registros de la tabla temporal | `model/functions/SSPR_LEAVE_PAID.xml` |
| `sspr_leave_reactive` | Reactivar Proceso | Cannot Reactive, Transaction is add to vacations and have related payroll; OBTENGO EL PERIODO RELACIONADO A ESE PERMISO; VALIDO SI EXISTE UNA NOMINA PROCESADA PARA ESE PERIODO | Cannot Reactive, Transaction is add to vacations and have related payroll; OBTENGO EL PERIODO RELACIONADO A ESE PERMISO; VALIDO SI EXISTE UNA NOMINA PROCESADA PARA ESE PERIODO | `model/functions/SSPR_LEAVE_REACTIVE.xml` |
| `sspr_leave_taken` | — | ELimina los registros de la tabla temporal; insert into logs(logs_id, c_bpartner_id , amount,; sspr_payroll_id,v_salarydayslabo,v_salarytotal); values(get_uuid(),Cur_sspr_leave_group.c_bpartner_id, | ELimina los registros de la tabla temporal; insert into logs(logs_id, c_bpartner_id , amount,; sspr_payroll_id,v_salarydayslabo,v_salarytotal); values(get_uuid(),Cur_sspr_leave_group.c_bpartner_id,; v_value,v_sspr_payroll_id,Cur_sspr_leave_group.amountleave,v_salarytotal); | `model/functions/SSPR_LEAVE_TAKEN.xml` |
| `sspr_lines_settlement` | Crear líneas de Liquidación | Date to contract out the payroll provision period; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE LA NOMINA DE PROVISIONES- PERIODO, ESTADO; VALIDACION FECHA FIN DEL CONTRATO VS FECHA DE LA NOMINA DE LIQ… | Date to contract out the payroll provision period; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE LA NOMINA  DE PROVISIONES- PERIODO, ESTADO; VALIDACION FECHA FIN DEL CONTRATO VS FECHA DE LA NOMINA DE LIQUIDACION NORMAL; OBTENGO FECHA INICIO Y FECHA FIN DE PERIODO; VALIDACION FECHA FIN DEL CONTRATO VS FECHA DE LA NOMINA DE LIQUIDACION PROVISIONES | `model/functions/SSPR_LINES_SETTLEMENT.xml` |
| `sspr_load_concept_loan` | Cargar Concepto Préstamo | RAISE NO_DATA_FOUND||Cur_LINELOANS.sshr_loans_id; | RAISE NO_DATA_FOUND||Cur_LINELOANS.sshr_loans_id; | `model/functions/SSPR_LOAD_CONCEPT_LOAN.xml` |
| `sspr_load_concept_loan2` | — | IF v_sspr_line_loans_id='21883BD629104868A1CFC659A8805C27' THEN; RAISE NO_DATA_FOUND || Cur_insertemployee.c_bpartner_id; | IF v_sspr_line_loans_id='21883BD629104868A1CFC659A8805C27' THEN; RAISE NO_DATA_FOUND || Cur_insertemployee.c_bpartner_id; | `model/functions/SSPR_LOAD_CONCEPT_LOAN2.xml` |
| `sspr_load_concept_loan2_liq` | — | and to_date(to_char(a.paydate,'dd-MM-yyyy')) between to_date('01-01-2014') and to_date('31-01-2014'); and ((to_char(a.paydate,'dd-MM-yyyy'))>= (to_char(v_StartPeriod,'dd-MM-yyyy')) and to_char(a.paydate,'dd-MM-yyyy')<=… | and to_date(to_char(a.paydate,'dd-MM-yyyy')) between to_date('01-01-2014') and to_date('31-01-2014'); and ((to_char(a.paydate,'dd-MM-yyyy'))>= (to_char(v_StartPeriod,'dd-MM-yyyy')) and to_char(a.paydate,'dd-MM-yyyy')<= (to_char(v_EndPeriod,'dd-MM-yyyy'))); IF v_sspr_line_loans_id='21883BD629104868A1CFC659A8805C27' THEN; RAISE NO_DATA_FOUND || Cur_insertemployee.c_bpartner_id; | `model/functions/SSPR_LOAD_CONCEPT_LOAN2_LIQ.xml` |
| `sspr_load_concept_loan3` | — | raise exception '%' , 'sidesfot ' || p_conceptout_id;; and ((to_char(a.paydate,'dd-MM-yyyy'))>= (to_char(v_StartPeriod,'dd-MM-yyyy')) and to_char(a.paydate,'dd-MM-yyyy')<= (to_char(v_EndPeriod,'dd-MM-yyyy'))); Insert in… | raise exception '%' , 'sidesfot ' || p_conceptout_id;; and ((to_char(a.paydate,'dd-MM-yyyy'))>= (to_char(v_StartPeriod,'dd-MM-yyyy')) and to_char(a.paydate,'dd-MM-yyyy')<= (to_char(v_EndPeriod,'dd-MM-yyyy'))); Insert into sspr_concept_amount(SSPR_CONCEPT_AMOUNT_ID,AD_CLIENT_ID,AD_ORG_ID,ISACTIVE,CREATED,CREATEDBY,UPDATED,UPDATEDBY,; SSPR_CONCEPT_ID,C_BPARTNER_ID,C_PERIOD_ID,AMOUNT,ISMODIFIED); values(get_uuid(), v_Client_ID, v_Org_ID, 'Y',	to_date(now()),v_User_ID, to_date(now()), v_User_ID,; p_conceptout_id ,v_employee_id,v_Period_ID,v_mnt,'N'); | `model/functions/SSPR_LOAD_CONCEPT_LOAN3.xml` |
| `sspr_load_concept_loan4` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_LOAD_CONCEPT_LOAN4.xml` |
| `sspr_load_concept_loan5` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_LOAD_CONCEPT_LOAN5.xml` |
| `sspr_load_payroll_template` | Cargar Plantilla de Nómina | Insert concepts of the template into period. | Insert concepts of the template into period. | `model/functions/SSPR_LOAD_PAYROLL_TEMPLATE.xml` |
| `sspr_mobilization` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_MOBILIZATION.xml` |
| `sspr_other_tax_income_process` | Procesar | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_OTHER_TAX_INCOME_PROCESS.xml` |
| `sspr_oti_reactivate` | Reactivar | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_OTI_REACTIVATE.xml` |
| `sspr_payrollpayment` | Pago Nómina | ERROR=NO TIENE TIEPO DE DOCUMENTO CONFIGURADO PARA PAGO DE NOMINA; OBTENGO CUENTA CONFIGURADA PARA PAGOS DE NOMINA; ACTUALIZA ESTADO DEL COBRO A PROCESADO PARA PODER CONTABILIZAR | ERROR=NO TIENE TIEPO DE DOCUMENTO CONFIGURADO PARA PAGO DE NOMINA; OBTENGO CUENTA CONFIGURADA PARA PAGOS DE NOMINA; ACTUALIZA ESTADO DEL COBRO A PROCESADO PARA PODER CONTABILIZAR | `model/functions/SSPR_PAYROLLPAYMENT.xml` |
| `sspr_pinstance_para_insert` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_PINSTANCE_PARA_INSERT.xml` |
| `sspr_process_payroll` | Procesar Nómina | 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE ORDEN DE PROCESO DE GENERACION DE NOMINA; RAISE_APPLICATION_ERROR(-20000, 'new v_value' || v_value); | 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE ORDEN DE PROCESO DE GENERACION DE NOMINA; RAISE_APPLICATION_ERROR(-20000, 'new v_value' || v_value);; RAISE_APPLICATION_ERROR(-20000, ' 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO '||Cur_Concept.SSPR_Concept_ID||' '|| v_Period_ID||' '|| Cur_Employee.C_BPartner_ID);; SSPR_GET_BUSINESS_CONCEPT(Cur_Concept.SSPR_Concept_ID, v_Period_ID, Cur_Employee.C_BPartner_ID) | `model/functions/SSPR_PROCESS_PAYROLL.xml` |
| `sspr_process_utility` | Proceso de Utilidades | No existe configuración utilidades para el año de proceso; Ya existe Utilidades generadas para este período; Debe configurar el período de impuesto a la renta; El período IR configurado no pertenece al año de proceso | No existe configuración utilidades para el año de proceso; Ya existe Utilidades generadas para este período; Debe configurar el período de impuesto a la renta; El período IR configurado no pertenece al año de proceso; VALIDA QUE EXISTA CONFIGURACION PARA EL AÑO DE PROCESO; Revisa si existe una Utilidad para el perìodo ejecutado | `model/functions/SSPR_PROCESS_UTILITY.xml` |
| `sspr_reactiveloan` | Reactivar | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_REACTIVELOAN.xml` |
| `sspr_renewal` | Renovación | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_RENEWAL.xml` |
| `sspr_return_additional_days` | — | select sspr_return_additional_days('37A26E7FF0EC4AD7A034C1CFBDDB1454','8D27600B5CE44014BDE7ED427C43F05F','DN', '01-09-2015', '31-03-2016') from dual; select sspr_return_additional_days('80548089CC0D49F69E1BB7290E5A6D53'… | select sspr_return_additional_days('37A26E7FF0EC4AD7A034C1CFBDDB1454','8D27600B5CE44014BDE7ED427C43F05F','DN', '01-09-2015', '31-03-2016') from dual; select sspr_return_additional_days('80548089CC0D49F69E1BB7290E5A6D53','3C6899997D46408E998ECDAB7F83DB50', 'DA', '01-05-2015', '31-01-2016') from dual | `model/functions/SSPR_RETURN_ADDITIONAL_DAYS.xml` |
| `sspr_return_date` | — | **********************VARIABLES PARA PROCESAMIENTO DE FECHAS*******************************************; RAISE NOTICE '%','RESULT v_dias_del_mes_ant = ' ||to_char(v_dias_del_mes_ant);; RAISE NOTICE '%','RESULT v_cast =… | **********************VARIABLES PARA PROCESAMIENTO DE FECHAS*******************************************; RAISE NOTICE '%','RESULT v_dias_del_mes_ant = '  ||to_char(v_dias_del_mes_ant);; RAISE NOTICE '%','RESULT v_cast = '  || v_cast; | `model/functions/SSPR_RETURN_DATE.xml` |
| `sspr_return_dis_persoexpen` | — | Retorna valor de gastos deducibles, si no tiene registrado los gastos personales el valor es 0 | Retorna valor de gastos deducibles, si no tiene registrado los gastos personales el valor es 0 | `model/functions/SSPR_RETURN_DIS_PERSOEXPEN.xml` |
| `sspr_return_month` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_RETURN_MONTH.xml` |
| `sspr_return_vacationsdays` | — | select sspr_return_additional_days('8C8DAB9662AB4CA5BE69EF2C7BE67D03','5BB61A167BD343B08F681D0BD2F38C67', 'DA', '01-') from dual; select sspr_return_additional_days('37A26E7FF0EC4AD7A034C1CFBDDB1454','8D27600B5CE44014BD… | select sspr_return_additional_days('8C8DAB9662AB4CA5BE69EF2C7BE67D03','5BB61A167BD343B08F681D0BD2F38C67', 'DA', '01-') from dual; select sspr_return_additional_days('37A26E7FF0EC4AD7A034C1CFBDDB1454','8D27600B5CE44014BDE7ED427C43F05F','DN', '01-09-2015', '31-03-2016') from dual; select sspr_return_vacationsdays('78BEEB13BC81458EB5A958C2362AB9E2','232D654950D34952B898F82CC51273F7', 'DN', '01-05-2015', '29-02-2016') from dual | `model/functions/SSPR_RETURN_VACATIONSDAYS.xml` |
| `sspr_salary_leave` | — | Error: El proceso subsidio salarial no tiene configurado el concepto de salida en la categoria del permiso; ELimina los registros de la tabla temporal; and (('01-06-2015' between a.stardate and a.enddate or '30-06-2015'… | Error: El proceso subsidio salarial no tiene configurado el concepto de salida en la categoria del permiso; ELimina los registros de la tabla temporal; and (('01-06-2015' between a.stardate and a.enddate or '30-06-2015' between a.stardate and a.enddate) or; (a.stardate between '01-06-2015' and '30-06-2015' or a.enddate between '01-06-2015' and '30-06-2015')) | `model/functions/SSPR_SALARY_LEAVE.xml` |
| `sspr_settl_add_adi` | — | select coalesce((select round(sum(totalvalue),2) | select coalesce((select round(sum(totalvalue),2) | `model/functions/SSPR_SETTL_ADD_ADI.xml` |
| `sspr_settl_add_payroll` | — | INSERTO LINEAS CONCEPTOS ROL DE LIQUIDACIONES NORMAL | INSERTO LINEAS CONCEPTOS ROL DE LIQUIDACIONES NORMAL | `model/functions/SSPR_SETTL_ADD_PAYROLL.xml` |
| `sspr_settl_add_per` | — | This concepts type can not be assigned in; No process desahucio, rate field has no value; If(Cur_benefit_dismissal.value = 'DSH' OR Cur_benefit_dismissal.value = 'ING')Then | This concepts type can not be assigned in; No process desahucio, rate field has no value; If(Cur_benefit_dismissal.value = 'DSH' OR  Cur_benefit_dismissal.value = 'ING')Then | `model/functions/SSPR_SETTL_ADD_PER.xml` |
| `sspr_settl_add_spe` | — | This concepts type can not be assigned in; No process desahucio, rate field has no value; OBTENGO EL SALARIO CORRESPONDIENTE DEL EMPLEADO; If(Cur_benefit_dismissal.value = 'DSH' OR Cur_benefit_dismissal.value = 'ING')Th… | This concepts type can not be assigned in; No process desahucio, rate field has no value; OBTENGO EL SALARIO CORRESPONDIENTE DEL EMPLEADO; If(Cur_benefit_dismissal.value = 'DSH' OR  Cur_benefit_dismissal.value = 'ING')Then | `model/functions/SSPR_SETTL_ADD_SPE.xml` |
| `sspr_settl_add_tenth` | — | No exits concept 13TH in payroll provision; No existe configurado el sueldo básico actual para el periodo; NUEVA LOGICA: variables para ajuste de decimo mensualizado; INSERTO LINEAS CONCEPTOS ROL DE LIQUIDACIONES DE PRO… | No exits concept 13TH in payroll provision; No existe configurado el sueldo básico actual para el periodo; NUEVA LOGICA: variables para ajuste de decimo mensualizado; INSERTO LINEAS CONCEPTOS ROL DE LIQUIDACIONES DE PROVISIONES TOTAL; DESARROLLO DECIMO TERCERO Y DECIMO CUARTO; RAISE_APPLICATION_ERROR(-20000,'@No exits concept 13TH@' || v_date_val || ' - ' || p_enddate) ; | `model/functions/SSPR_SETTL_ADD_TENTH.xml` |
| `sspr_substr_formula` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_SUBSTR_FORMULA.xml` |
| `sspr_test` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_TEST.xml` |
| `sspr_thirteenth` | — | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO TERCERO Y ASIGNO CONCEPTO CORRESPONDIENTE; CREA CONCEPTO DECIMO TERCERO EN LA… | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO TERCERO Y ASIGNO CONCEPTO CORRESPONDIENTE; CREA CONCEPTO DECIMO TERCERO EN LAS LINEAS | `model/functions/SSPR_THIRTEENTH.xml` |
| `sspr_thirteenth_liq` | — | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO TERCERO Y ASIGNO CONCEPTO CORRESPONDIENTE; VALIDO SI EL MONTO DEL CONCEPTO ES… | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; VALIDA SI ACUMULA O NO EL CONCEPTO DE DECIMO TERCERO Y ASIGNO CONCEPTO CORRESPONDIENTE; VALIDO SI EL MONTO DEL CONCEPTO ES DIFERENTE DE 0 PARA INSERTAR LA LINEA; CREA CONCEPTO DECIMO TERCERO EN LAS LINEAS | `model/functions/SSPR_THIRTEENTH_LIQ.xml` |
| `sspr_update_additional_days` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_UPDATE_ADDITIONAL_DAYS.xml` |
| `sspr_update_salary` | — | v_SSconceptIess_ID VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsCompany VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsIess VARCHAR(32); --OBTG:VARCHAR2--; v_CONCEPT_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2-- | v_SSconceptIess_ID VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsCompany VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsIess VARCHAR(32); --OBTG:VARCHAR2--; v_CONCEPT_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2--; VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; LEFT JOIN SSPR_Period P ON CBP.C_BPartner_ID = P.C_BPartner_ID | `model/functions/SSPR_UPDATE_SALARY.xml` |
| `sspr_update_salary_liq` | — | v_SSconceptIess_ID VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsCompany VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsIess VARCHAR(32); --OBTG:VARCHAR2--; v_CONCEPT_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2-- | v_SSconceptIess_ID VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsCompany VARCHAR(32); --OBTG:VARCHAR2--; V_ReserveFundsIess VARCHAR(32); --OBTG:VARCHAR2--; v_CONCEPT_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2--; VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO | `model/functions/SSPR_UPDATE_SALARY_LIQ.xml` |
| `sspr_update_workingdays` | — | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; Valida configur… | VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Period_ID = v_Period_ID;; Valida configuracion inicial de dias del mes; LEFT JOIN SSPR_Period P ON CBP.C_BPartner_ID = P.C_BPartner_ID; v_days := to_number(to_char(v_EndPeriod,'dd')); | `model/functions/SSPR_UPDATE_WORKINGDAYS.xml` |
| `sspr_update_workingdays_liq` | — | Valida configuracion inicial de dias del mes; v_days := to_number(to_char(v_EndPeriod,'dd'));; VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO | Valida configuracion inicial de dias del mes; v_days := to_number(to_char(v_EndPeriod,'dd'));; VALIDO SI EXISTE EL CONCEPTO  YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO | `model/functions/SSPR_UPDATE_WORKINGDAYS_LIQ.xml` |
| `sspr_updatedateentry` | Actualización del Empleado - Fecha de Entrada | ACTUALIZO FECHA DE INGRESO DEL EMPLEADO CON LA DEL REINGRESO | ACTUALIZO FECHA DE INGRESO DEL EMPLEADO CON LA DEL REINGRESO | `model/functions/SSPR_UPDATEDATEENTRY.xml` |
| `sspr_updatesalary_employee` | Actualizar Salario | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPR_UPDATESALARY_EMPLOYEE.xml` |
| `sspr_updateworkeddays` | — | RAISE_APPLICATION_ERROR(-20000,'@Error: End date this contract is null@');; CALCULO DE NUMERO DE DIAS LABORADOS LIQUIDACION; v_daysliquidation := to_number(to_char(v_enddate_liquidation,'dd'));; select to_date(to_char('… | RAISE_APPLICATION_ERROR(-20000,'@Error: End date this contract is null@');; CALCULO DE NUMERO DE DIAS LABORADOS LIQUIDACION; v_daysliquidation := to_number(to_char(v_enddate_liquidation,'dd'));; select to_date(to_char('30' || '-' || to_char(to_date('01-10-2015'),'mm') || '-' || to_char(to_date('01-10-2015'),'yyyy')),'DD-MM-YYYY'); v_daysmonth := (to_number(to_char(v_EndPeriod,'dd')) - v_dayseentry) + 1 ; | `model/functions/SSPR_UPDATEWORKEDDAYS.xml` |
| `sspr_updateworkeddays_liq` | — | OBTENGO EL TIPO DE NOMINA Y EMPLEADOsueldo dias; CALCULO DE NUMERO DE DIAS LABORADOS LIQUIDACION; OBTENGO LA FECHA DE CADUCIDAD DEL CONTRATO | OBTENGO EL TIPO DE NOMINA Y EMPLEADOsueldo dias; CALCULO DE NUMERO DE DIAS LABORADOS LIQUIDACION; OBTENGO LA FECHA DE CADUCIDAD DEL CONTRATO | `model/functions/SSPR_UPDATEWORKEDDAYS_LIQ.xml` |
| `sspr_validareservfound` | — | from sspr_concept where isreservefunds='Y' limit 1; | from sspr_concept where isreservefunds='Y' limit 1; | `model/functions/SSPR_VALIDARESERVFOUND.xml` |
| `sspr_validareservfound_liq` | — | from sspr_concept where isreservefunds='Y' limit 1; | from sspr_concept where isreservefunds='Y' limit 1; | `model/functions/SSPR_VALIDARESERVFOUND_LIQ.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Archive Payment Utilities Produbanco TXT | `Sspr_Payment Utilities Produbanco TXT` | Botón (Java) | Java `ArchivePaymentUtilitiesProdubanco` | N | Proceso Openbravo registro `cYearId` |
| 2 | Archivo Pago Decimos  Produbanco TXT | `Sspr_ArchivePaymentTenthProdubanco` | Botón (Java) | Java `ArchivePaymentTenthProdubanco` | N | Proceso Openbravo registro `documentno` |
| 3 | Archivo Pagos Banco Produbanco Txt | `Sspr_ArchProdubancoBankTxt` | Botón (Java) | Java `ArchivePaymentProdubancoBankTXT` | N | Proceso Openbravo registro `documentno` |
| 4 | Archivo Transferencia Nómina Banco de Guayaquil | `Bank of Guayaquil Payroll Transfer File` | Botón (Java) | Java `ArchPayrollGuayaquilBankTXT` | N | Proceso Openbravo registro `documentno` |
| 5 | Archivo Transferencia Nómina Banco del Austro | `Archive Transfer Payroll Austro` | Botón (Java) | Java `ArchTransferPayrollBankAustro` | N | Proceso Openbravo registro `documentno` |
| 6 | Archivo Transferencia Utilidades del Austro | `Archive Transfer Utilites Austro TXT` | Botón (Java) | Java `ArchTransferUtilitesBankAustro` | N | Proceso Openbravo registro `cYearId` |
| 7 | Automatic Payroll Process Class | `Automatic Payroll Process Class` | Botón (Java) | Java `Sspr_AutomaticPayroll` | N | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 8 | Cargar líneas | `OtherTaxIncomeLoadLines` | Botón (Java) | Java `OtherTaxIncomeLoadLines` | N | Proceso Openbravo registro `Sspr_Other_Tax_Income_ID`, Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo |
| 9 | Actualización del Empleado - Fecha de Entrada | `SSPR_UpdateDatEntryEmployee` | Botón (PL/pgSQL) | PL `sspr_updatedateentry` | N | ACTUALIZO FECHA DE INGRESO DEL EMPLEADO CON LA DEL REINGRESO |
| 10 | Actualizar Salario | `Sspr_UpdateSalaryEmployee` | Botón (PL/pgSQL) | PL `sspr_updatesalary_employee` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 11 | Approve | `SSPR_change_status_leave` | Botón (PL/pgSQL) | PL `sspr_change_status_leave` | N | No tiene vacaciones disponibles días normales; No tiene vacaciones disponibles días adicionales; Cur_vacations.nodays + (Cur_vacations.Noadditionaltotal):; VALIDA DIAS DE VACACIONE |
| 12 | Aprobar Prestamos | `SSPR_change_status_approve` | Botón (PL/pgSQL) | PL `sspr_change_status` | N | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN |
| 13 | Borrar fórmula | `sspr_deleteformula` | Botón (PL/pgSQL) | PL `sspr_deleteformula` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 14 | Calcular Vacaciones | `Calculate Vacation` | Botón (PL/pgSQL) | PL `sspr_calculatevacation` | N | AND A.C_BPARTNER_ID = '3C0596B9EB424089B757554EF5BCACD6'; ELIMINA REGISTROS MAYORES A LA FECHA DE PROCESO; Cuenta vacaciones que la fecha inicio y fecha fin cumplan 1 año.; En caso |
| 15 | Cargar Acumulables | `Acumulative In` | Botón (PL/pgSQL) | PL `sspr_acumulativeconcepts` | N | SUMA PESTAÑA LINEAS DE LA LIQUIDACION PARA ACUMULAR; SUMA PESTAÑA DATOS ADICIONALES DE LA LIQUIDACION PARA ACUMULAR; AND TO_CHAR(pe.startdate,'YYYY-MM') = TO_CHAR(oti.process_date, |
| 16 | Cargar Concepto Préstamo | `Load Concept Loan` | Botón (PL/pgSQL) | PL `sspr_load_concept_loan` | N | RAISE NO_DATA_FOUND||Cur_LINELOANS.sshr_loans_id; |
| 17 | Cargar Plantilla de Nómina | `load_payroll_template` | Botón (PL/pgSQL) | PL `sspr_load_payroll_template` | N | Insert concepts of the template into period. |
| 18 | Completar Liquidación | `sspr_complete_settlement` | Botón (PL/pgSQL) | PL `sspr_complete_settlement` | N | CAMBIA DE ESTADO NOMINA NORMAL A LIQUIDADO; CAMBIA DE ESTADO NOMINA DE PROVISIONES A LIQUIDADO; CAMBIA DE ESTADO EMPLEADO LIQUIDADO NOMINA NORMAL; CAMBIA DE ESTADO EMPLEADO LIQUIDA |
| 19 | Copiar Conceptos | `Copy_Concepts` | Botón (PL/pgSQL) | PL `sspr_copy_concept_amounts` | N | raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-'||v_SSconcept_ID;; raise exception '%', v_org_id ||'-'||v_client_id||'-'||v_StartPeriod_ID||'-test'||v_E |
| 20 | Copiar Plantilla | `Copy Template` | Botón (PL/pgSQL) | PL `sspr_copy_template` | N | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; and em_sspr_category_acct_id = Cur_partne |
| 21 | Crear línea Préstamos | `Create Line Loans` | Botón (PL/pgSQL) | PL `sspr_createlineloans` | N | v_MontoCuota := (v_amount / v_time) + v_MontoInteres; |
| 22 | Crear líneas de Liquidación | `sspr_lines_settlement` | Botón (PL/pgSQL) | PL `sspr_lines_settlement` | N | Date to contract out the payroll provision period; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE LA NOMINA DE PROVISIONES- PERIODO, ESTADO; VALIDACION FECHA FIN DE |
| 23 | Crear Montos de Conceptos | `Create_Concept_Amounts` | Botón (PL/pgSQL) | PL `sspr_create_concept_amounts` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 24 | Eliminar Diario Manual | `Delete Manual Journal` | Botón (PL/pgSQL) | PL `sspr_delete_manual_journal` | N | VALIDO QUE EL ASIENTO NO ESTE CONTABILIZADO; ACTUALIZO CABECERA DE LA NOMINA PARA QUE PERMITA GENERAR EL ASIENTO; OBTENGO REFERENCIA DE LAS LINEAS DEL ASIENTO; ELIMINO CABECERA Y A |
| 25 | Fondos de Reserva | `SSPR_ReserveFunds` | Botón (PL/pgSQL) | PL `sspr_generate_reservefounds` | N | VALIDO SI EXISTE EL CONCEPTO YA CREADO CON REFERENCIA A ESE EMPLEADO EN LAS LINEAS DEL CONCEPTO; DELETE FROM SSPR_Concept_Amount WHERE SSPR_Concept_ID = v_SSconceptIess_ID AND C_Pe |
| 26 | Generar Datos para Asiento Manual | `Manual Journal Entries` | Botón (PL/pgSQL) | PL `sspr_generate_manual_journal` | N | NO HAY NINGUNA REFERENCIA DE TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; NO EXISTE UN ESQUEMA CONTABLE CONFIGURADO PARA LA ORGANIZACION; ** NUEVO DESARROLLO PARA UNIFICAR EL PROCESO |
| 27 | Generar Impuesto a la Renta | `Tax Income` | Botón (PL/pgSQL) | PL `sspr_incometotals` | N | EXECUTE IMMEDIATE 'SELECT ' || SSPR_ACUMULATIVECONCEPTSX() || 'FROM DUAL';; DATOS FINALES PARA INSERTAR EN SSPR_INCOMETOTAL; TOTAL DE INGRESOS ACUMULABLES Y PROJECTABLES; TOTAL DE  |
| 28 | Generar Liquidación del Empleado | `Generate Settlement Employee` | Botón (PL/pgSQL) | PL `SSPR_generatesettlementemp` | N | OBTENGO EL ID DEL EMPLEADO Y FECHA DE SALIDA PARA VALIDAR LA VACACIONES; OBTENGO DIAS PENDIENTES DE VACACIONES DEL EMPLEADO |
| 29 | Generar Quincena | `Generate_fortnight` | Botón (PL/pgSQL) | PL `sspr_get_fortnight_concept` | N | SELECT SSPR_CONCEPT_ID INTO v_Qconcept_ID FROM SSPR_CONCEPT WHERE isfortnight ='Y' limit 1;; raise exception '%', '@Concepto Quincena No existe@';--OBTG:2000-; SELECT SSPR_CONCEPT_ |
| 30 | Pago Nómina | `Payroll Payment Out` | Botón (PL/pgSQL) | PL `sspr_payrollpayment` | N | ERROR=NO TIENE TIEPO DE DOCUMENTO CONFIGURADO PARA PAGO DE NOMINA; OBTENGO CUENTA CONFIGURADA PARA PAGOS DE NOMINA; ACTUALIZA ESTADO DEL COBRO A PROCESADO PARA PODER CONTABILIZAR |
| 31 | Procesar | `OtherTaxIncomeProcess` | Botón (PL/pgSQL) | PL `sspr_other_tax_income_process` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 32 | Procesar Nómina | `sspr_process_payroll` | Botón (PL/pgSQL) | PL `sspr_process_payroll` | N | 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; OBTENGO DATOS DE ORDEN DE PROCESO DE GENERACION DE NOMINA; RAISE_APPLICATION_ERROR |
| 33 | Proceso de Nómina Automático | `Automatic Payroll Process` | Botón (PL/pgSQL) | PL `sspr_automatic_payroll_process` | N | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA; RECUPERA INSTANCIA PA |
| 34 | Proceso de Utilidades | `Process of Utilities` | Botón (PL/pgSQL) | PL `sspr_process_utility` | N | No existe configuración utilidades para el año de proceso; Ya existe Utilidades generadas para este período; Debe configurar el período de impuesto a la renta; El período IR config |
| 35 | Préstamos Cambio de Estado | `SSPR_change_status` | Botón (PL/pgSQL) | PL `sspr_change_status` | N | El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; elsIF (v_status = 'ap' AND v_StatusDocumento_P = 'ap') THEN |
| 36 | Reactivar | `sspr_reactive_loan` | Botón (PL/pgSQL) | PL `sspr_reactiveloan` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 37 | Reactivar | `sspr_oti_reactivate` | Botón (PL/pgSQL) | PL `sspr_oti_reactivate` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 38 | Reactivar Proceso | `Process Reactive` | Botón (PL/pgSQL) | PL `sspr_leave_reactive` | N | Cannot Reactive, Transaction is add to vacations and have related payroll; OBTENGO EL PERIODO RELACIONADO A ESE PERMISO; VALIDO SI EXISTE UNA NOMINA PROCESADA PARA ESE PERIODO |
| 39 | Renovación | `sspr_renewal` | Botón (PL/pgSQL) | PL `sspr_renewal` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 40 | Archivo de Variación de Extras IESS | `IESS Extras Variation File` | Informe (servlet) | Java `ArchVariationSalaryCSV` | N | Proceso Openbravo registro `adOrgId` |
| 41 | Archivo Pago Banco Pichincha TXT | `File Payment Pichincha Bank TXT` | Informe (servlet) | Java `ArchPaymentPichinchaBankTXT` | N | Proceso Openbravo registro `documentno` |
| 42 | Archivo Pago Banco Rumiñahui TXT | `Sspr_ArchRuminahuiBanKTxt` | Informe (servlet) | Java `ArchivePayrollPaymentRuminahuiBankTXT` | N | Proceso Openbravo registro `documentno` |
| 43 | Generar Formulario 107 Xml | `Generate Formulary 107 Xml` | Informe (servlet) | Java `Formulary107_xml` | N | Proceso Openbravo registro `cYearId` |
| 44 | Modificar Salario CSV | `Modify Salary CSV` | Informe (servlet) | Java `ModifySalaryCSV` | N | Proceso Openbravo registro `cPeriodId` |
| 45 | Pago Archivo Banco Central TXT | `Archive Payment Central Bank TXT` | Informe (servlet) | Java `ArchPaymentCtralBankTXT` | N | Proceso Openbravo registro `documentno` |
| 46 | Pago Archivo Banco General Rumiñahui Utilidades TXT | `PaymentArchiveBankRuminahuiUtilities` | Informe (servlet) | Java `ArchivePaymentUtilitiesRuminahuiBankTXT` | N | Proceso Openbravo registro `cYearId` |
| 47 | Reporte Utilidades CSV | `CSV Utilities Report` | Informe (servlet) | Java `UtilitiesCSV` | N | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 48 | Detalle Acumulado Decimo 3ro Resumido por Centro de Costo | `Report Accumulated Detail Thirteenth` | Reporte | — | S | Accumulated Detail Thirteenth Summarized by Cost Center |
| 49 | GENERIC - FINAL SETTLEMENT | `GENERIC - FINAL SETTLEMENT` | Reporte | Java `Sspr_ReportPrintFinalSettlement` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 50 | Impresión de Contrato | `PRINT CONTRACT` | Reporte | Java `ReportContractType` | S | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/reportcontracttype/ReportContractType.jrxml`; contexto sesión `—`. |
| 51 | Imprimir Aprovación de Permiso | `Print Approvation Leave` | Reporte | Java `ApprovationLeave` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 52 | Imprimir Aprovación de Permiso Emp | `Print Approvation Leave Emp` | Reporte | Java `ApprovationLeaveE` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 53 | Imprimir Liquidación final | `PRINT  SETTLEMENT` | Reporte | Java `Rpt_FinalSettlement` | S | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/ad_Reports/Rpt_FinalSettlement.jrxml`; contexto sesión `—`. |
| 54 | Imprimir Solicitud de Empleado | `PRINT LEAVE` | Reporte | Java `Rpt_RequestLeave` | S | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/ad_Reports/Rpt_RequestLeave.jrxml`; contexto sesión `—`. |
| 55 | Imprimir Solicitud Préstamo | `PRINT LOANS` | Reporte | Java `RptRequestLoan` | S | Genera PDF desde JRXML `com/sidesoft/hrm/payroll/ad_Reports/RptRequestLoan.jrxml`; contexto sesión `—`. |
| 56 | Reporte de Gastos personales. | `Personal expenses report` | Reporte | — | S | Personal expenses report |
| 57 | Reporte General del Formulario 107 por mes | `Report General Formulary 107 by Month` | Reporte | — | S | — |
| 58 | Request Leave Print | `Request Leave Print` | Reporte | Java `RequestLeave` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |

**Total acciones documentadas (extract):** **58** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/images/sri.jpg` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `com.sidesoft.hrm.payroll`.

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

# Glosario — prefijo `SSPR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.hrm.payroll` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Sspr_Payment Utilities Produbanco TXT` — Archive Payment Utilities Produbanco TXT
- `Sspr_ArchivePaymentTenthProdubanco` — Archivo Pago Decimos  Produbanco TXT
- `Sspr_ArchProdubancoBankTxt` — Archivo Pagos Banco Produbanco Txt
- `Bank of Guayaquil Payroll Transfer File` — Archivo Transferencia Nómina Banco de Guayaquil
- `Archive Transfer Payroll Austro` — Archivo Transferencia Nómina Banco del Austro
- `Archive Transfer Utilites Austro TXT` — Archivo Transferencia Utilidades del Austro
- `Automatic Payroll Process Class` — Automatic Payroll Process Class
- `OtherTaxIncomeLoadLines` — Cargar líneas
- `SSPR_UpdateDatEntryEmployee` — Actualización del Empleado - Fecha de Entrada
- `Sspr_UpdateSalaryEmployee` — Actualizar Salario
- `SSPR_change_status_leave` — Approve
- `SSPR_change_status_approve` — Aprobar Prestamos
- `sspr_deleteformula` — Borrar fórmula
- `Calculate Vacation` — Calcular Vacaciones
- `Acumulative In` — Cargar Acumulables

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Advanced PayRoll
**Package:** `com.sidesoft.hrm.payroll.advanced`

# Module overview — Advanced PayRoll

## Functional

El módulo Advanced PayRoll proporciona funciones avanzadas para la gestión de nómina y recursos humanos en Openbravo. Facilita el cálculo de salarios, actualizaciones de empleados y gestión de subrogaciones. Los actores principales incluyen personal de nómina, administradores de recursos humanos y desarrolladores que soportan e integran estas funcionalidades. El módulo depende de compatibilidad con la interfaz de usuario y otras características del ERP, lo que garantiza su integración sin problemas en entornos existentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/hrm/payroll/advanced` |
| Web | `web/com.sidesoft.hrm.payroll.advanced/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- User Interface Application

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SFPR`

# Guía de chat — Advanced PayRoll

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.hrm.payroll.advanced`).

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
- «¿Qué es la tabla sfpr_rve_detail?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo actualizar la información de un empleado en el sistema?
- ¿Qué pasos debo seguir para procesar la nómina de este mes?
- ¿Cómo valido la información de un contrato laboral?
- ¿Dónde encuentro las herramientas para calcular los salarios?
- ¿Qué sucede si un campo de la nómina contiene errores?
- ¿Cómo se registra un movimiento o cambio en la posición de un empleado?
- ¿Qué debo hacer si el número de documento no se genera correctamente?
- ¿Cómo se gestionan los días de licencia para los empleados?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad cabecera 'sfpr_rve_detail', que representa detalles de la evolución salarial. Incluye relaciones con tablas como 'SSPR_ATTENDANCE', 'SSPR_CONCEPT' y 'SSPR_CONTRACT', entre otras. Los triggers juegan un papel crucial en la validación y gestión de la integridad de los datos, como es el caso de 'SFPR_DATE_VALIDATE_TRG', que se utiliza para validar campos de fecha en la tabla 'sfpr_evolution_salary'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sfpr_action_type` |
| `sfpr_employee_contribution` |
| `sfpr_employee_other` |
| `sfpr_employee_permit` |
| `sfpr_employee_rve` |
| `sfpr_employee_situation` |
| `sfpr_employee_situation2` |
| `sfpr_employee_surrogate` |
| `sfpr_employee_vacation` |
| `sfpr_evolution_salary` |
| `sfpr_grade` |
| `sfpr_job_action` |
| `sfpr_job_actionline` |
| `sfpr_level` |
| `sfpr_movement_type` |
| `sfpr_provision` |
| `sfpr_provision_property` |
| `sfpr_rve` |
| `sfpr_rve_detail` |
| `sfpr_surrogate_detail` |
| `sfpr_type_job_action` |
| `sfpr_type_provision` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sfpr_action_type` | sfpr_action_type | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sfpr_action_type_key`; Cols: value, name; `SFPR_ATYPE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_employee_contribution` | sfpr_employee_contribution | `SFPR_VALIDCONTRIBUTION_TRG` | — | income_concept_id→sspr_concept; concept_bosses→sspr_concept; ad_client_id→ad_client; ad_org_id→ad_org; total_income_concept→sspr_concept (+1) | Detalle enlazado a ad_client, sspr_concept. Validado por trigger(s): SFPR_VALIDCONTRIBUTION_TRG. | PK `sfpr_econtribution_key`; Cols: name, personal_concept, porc_personal, concept_bosses, porc_bosses; `SFPR_ECONTRIB_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_employee_other` | sfpr_employee_other | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sfpr_movement_type_id→sfpr_movement_type | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sfpr_employee_other_key`; Cols: sfpr_movement_type_id, c_bpartner_id, startdate, enddate, nohours; `SFPR_EOTHER_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_employee_permit` | sfpr_employee_permit | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sfpr_movement_type_id→sfpr_movement_type | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sfpr_employee_permit_key`; Cols: startdate, enddate, sfpr_movement_type_id, line, description; `SFPR_EPERMIT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_employee_rve` | sfpr_employee_rve | `SFPR_ERVE_DETAIL_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_costcenter_id→c_costcenter; surrogate_to_id→sspr_position (+1) | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SFPR_ERVE_DETAIL_TRG. | PK `sfpr_employee_rve_key`; Cols: c_bpartner_id, startdate, enddate, sfpr_movement_type_id, surrogate_to_id; `SFPR_EMPRVE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SFPR_EMPRVE_PROCESSED_CHK`: PROCESSED IN ('Y', 'N') (+1) |
| `sfpr_employee_situation` | sfpr_employee_situation | `SFPR_INVALID_COSTCENTER_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; sfpr_action_type_id→sfpr_action_type; c_costcenter_id→c_costcenter; sfpr_employee_position_id→sspr_position | Detalle enlazado a ad_client, ad_org, sfpr_action_type. Validado por trigger(s): SFPR_INVALID_COSTCENTER_TRG. | PK `sfpr_employee_situation_key`; Cols: sfpr_action_type_id, actual_rmu, startdate, enddate, c_costcenter_id; `SFPR_ESITUATION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_employee_situation2` | sfpr_employee_situation2 | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sfpr_action_type_id→sfpr_action_type; c_costcenter_id→c_costcenter; sfpr_employee_position_id→sspr_position | Detalle enlazado a ad_client, ad_org, sfpr_action_type. | PK `sfpr_employee_situation2_key`; Cols: sfpr_action_type_id, proposal_rmu, startdate, enddate, c_costcenter_id; `SFPR_ESITUATION2_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_employee_surrogate` | sfpr_employee_surrogate | `SFPR_ESURROGATE_DETAIL_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; surrogate_to_id→sspr_position; sfpr_movement_type_id→sfpr_movement_type | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SFPR_ESURROGATE_DETAIL_TRG. | PK `sfpr_employee_surrogate_key`; Cols: c_bpartner_id, startdate, enddate, sfpr_movement_type_id, surrogate_to_id; `SFPR_ESURROGATE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SFPR_ESURROGATE_PROCESSED_CHK`: PROCESSED IN ('Y', 'N') |
| `sfpr_employee_vacation` | sfpr_employee_vacation | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sfpr_movement_type_id→sfpr_movement_type | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sfpr_employee_vacation_key`; Cols: c_bpartner_id, startdate, enddate, sfpr_movement_type_id, line; `SFPR_EVACATION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_evolution_salary` | sfpr_evolution_salary | `SFPR_DATE_VALIDATE_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_contract_id→sspr_contract | Detalle enlazado a ad_client, ad_org, sspr_contract. Validado por trigger(s): SFPR_DATE_VALIDATE_TRG. | PK `sfpr_evolution_salary_key`; Cols: value, startdate, enddate, amount, sspr_contract_id; `SFPR_ESALARY_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_grade` | sfpr_grade | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sfpr_employee_position_id→sspr_position | Detalle enlazado a ad_client, ad_org, sspr_position. | PK `sfpr_grade_key`; Cols: value, name, sfpr_employee_position_id, rmu; `SFPR_GRADE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_job_action` | sfpr_job_action | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sfpr_job_action_key`; Cols: value, c_bpartner_id; `SFPR_JOB_ACTION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_job_actionline` | sfpr_job_actionline | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sfpr_job_action_id→sfpr_job_action; sspr_concept_id→sspr_concept; sfpr_type_job_action_id→sfpr_type_job_action | Detalle enlazado a ad_client, ad_org, sfpr_job_action. | PK `sfpr_job_actionline_key`; Cols: sfpr_type_job_action_id, sspr_concept_id, date_job_action, amount, status; `SFPR_JACTIONLINE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_level` | sfpr_level | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sfpr_employee_position_id→sspr_position | Detalle enlazado a ad_client, ad_org, sspr_position. | PK `sfpr_level_id`; Cols: value, sfpr_employee_position_id, rmu; `SFPR_LEVEL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_movement_type` | sfpr_movement_type | `SFPR_VALIDATE_MOVEMENT_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype | Detalle enlazado a ad_client, ad_org, c_doctype. Validado por trigger(s): SFPR_VALIDATE_MOVEMENT_TRG. | PK `sfpr_movement_type_key`; Cols: c_doctype_id, documentno, transaction_date, description; `SFPR_MTYPE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_provision` | sfpr_provision | — | — | sfpr_type_provision_id→sfpr_type_provision; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sfpr_type_provision. | PK `sfpr_provision_key`; Cols: value, name, sfpr_type_provision_id; `SFPR_PROVISION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_provision_property` | sfpr_provision_property | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_costcenter_id→c_costcenter; sfpr_provision_id→sfpr_provision | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sfpr_provision_property_key`; Cols: value, c_bpartner_id, c_costcenter_id, sfpr_provision_id, provision_date; `SFPR_PPROPERTY_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_rve` | sfpr_rve | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sfpr_grade_id→sfpr_grade; sfpr_employee_position_id→sspr_position | Detalle enlazado a ad_client, ad_org, sfpr_grade. | PK `sfpr_rve_key`; Cols: sfpr_grade_id, sfpr_employee_position_id, rmu, porc_handimax, rve_handimax; `SFPR_RVE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_rve_detail` | sfpr_rve_detail | `SFPR_VALIDATE_RVE_DETAIL_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_costcenter_id→c_costcenter; c_period_id→c_period (+8) | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SFPR_VALIDATE_RVE_DETAIL_TRG. | PK `sfpr_rve_detail_key`; Cols: sfpr_rve_id, c_period_id, c_bpartner_id, nodays, grandtotal; `SFPR_RVE_DETAIL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_surrogate_detail` | sfpr_surrogate_detail | `SFPR_VALIDATE_SDETAIL_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_period_id→c_period; sfpr_employee_surrogate_id→sfpr_employee_surrogate (+5) | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SFPR_VALIDATE_SDETAIL_TRG. | PK `sfpr_surrogate_detail_key`; Cols: sfpr_movement_type_id, c_period_id, c_bpartner_id, sfpr_employee_position_id, surrogate_rmu; `SFPR_SDETAIL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_type_job_action` | sfpr_type_job_action | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sfpr_type_job_action_key`; Cols: value, name; `SFPR_TJOB_ACTION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sfpr_type_provision` | sfpr_type_provision | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sfpr_type_provision_key`; Cols: value, name; `SFPR_TPROVISION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sfpr_action_type` |
| `sfpr_employee_contribution` |
| `sfpr_employee_other` |
| `sfpr_employee_permit` |
| `sfpr_employee_rve` |
| `sfpr_employee_situation` |
| `sfpr_employee_situation2` |
| `sfpr_employee_surrogate` |
| `sfpr_employee_vacation` |
| `sfpr_evolution_salary` |
| `sfpr_grade` |
| `sfpr_job_action` |
| `sfpr_job_actionline` |
| `sfpr_level` |
| `sfpr_movement_type` |
| `sfpr_provision` |
| `sfpr_provision_property` |
| `sfpr_rve` |
| `sfpr_rve_detail` |
| `sfpr_surrogate_detail` |
| `sfpr_type_job_action` |
| `sfpr_type_provision` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_BPARTNER`, `SSPR_ATTENDANCE`, `SSPR_CONCEPT`, `SSPR_CONCEPT_AMOUNT`, `SSPR_CONTRACT`, `SSPR_LABOR_REGIME`, `SSPR_LEAVE_EMP`, `SSPR_LOANS`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de diferentes ventanas que permiten gestionar acciones laborales, actualizar información de empleados y procesar nóminas. Estas ventanas ofrecen un acceso intuitivo a funcionalidades específicas, permitiendo a los usuarios realizar operaciones como registrar movimientos, modificar niveles y manejar detalles de subrogaciones de manera eficiente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.hrm.payroll.advanced.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Acción Laboral | Job Action |
| Actualización Empleado | Employee Actualization |
| Detalle RVE | RVE Detail |
| Detalle Subrrogación | Surrogate Detail |
| Grado | Grade |
| Movimiento | Movement |
| Nivel | Level |
| Proceso Nómina | Process Payroll |
| Provisión | Provision |
| RVE | RVE |
| Tipo Acción | Action Type |
| Tipo acción laboral | Type Job Action |
| Tipo Contribución | Contribution Type |
| Tipo Provisión | Type Provision |
| Uniform or Property of Provision | Uniform or Property of Provision |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Acción Laboral | Job Action | No |
| Actualización Empleado | Employee Actualization | No |
| Archivo Pago Decimos Pichincha TXT | File Payment Tenth  pichincha  TXT | No |
| Archivo Pago Utilidades Banco Pichincha TXT | File Utilities Payment Pichincha Bank TXT | No |
| Calcular RVE | RVE Calculate | No |
| Calcular Subrrogacion | Surrogate Calculate | No |
| Cargar Concepto RVE | Load Concept RVE | No |
| Cargar Concepto Subrrogación | Load Concept Surrogate | No |
| Detalle RVE | RVE Detail | No |
| Detalle Subrrogación | Surrogate Detail | No |
| Grado | Grade | No |
| Historia Laboral IESS | History Laboral IESS | No |
| Movimiento | Movement | No |
| Nivel | Level | No |
| Proceso Contribución IESS | Process Contribution IESS | No |
| Proceso Nómina | Process Payroll | No |
| Provisión | Provision | No |
| RVE | RVE | No |
| Tipo Acción | Action Type | No |
| Tipo acción laboral | Type Job Action | No |
| Tipo Contribución | Contribution Type | No |
| Tipo Provisión | Type Provision | No |
| Total Ingresos Vs Total Egresos | Total Ingresos Vs Total Egresos | No |
| Transacción | Transaction | Sí |
| Uniform or Property of Provision | Uniform or Property of Provision | No |
| Utilidad | Uitlity | Sí |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.hrm.payroll.advanced.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Acción Laboral

- **AD_WINDOW_ID:** `64DC988AA3624C9C95A59CE98598848D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Job Action | `26AE9A95B43F41F1A93F8FAD3A0388A4` | 0 |
| 20 | Lines | `C89EC3480CF24B2BB03FA9112C50372F` | 1 |

### Ventana: Actualización Empleado

- **AD_WINDOW_ID:** `162294E68A1E4737A0A7EAAFE38A457C`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Employee Actualization | `291` | 0 |
| 20 | Direcciones | `293` | 1 |

### Ventana: Detalle RVE

- **AD_WINDOW_ID:** `9531A117DCC64D88BC9D9A0173EB370A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | RVE Detail | `15C69455EBE54B4CAFB914AE8FC5B73C` | 0 |

### Ventana: Detalle Subrrogación

- **AD_WINDOW_ID:** `7B8A10D042574B6AA92A292DA6C650A0`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Surrogate Detail | `FAEBC1C3F4CB48428946FC15F68F073D` | 0 |

### Ventana: Grado

- **AD_WINDOW_ID:** `AEA0216A8AA54DDB961CD86B6B6A610B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Grade | `CE049943C486427186F05D5D7B388B28` | 0 |

### Ventana: Movimiento

- **AD_WINDOW_ID:** `5FB72E20DC274B81BB78FCD078E8F681`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Movement | `C78F2BFBE41441AEA0C11D7275D5BABF` | 0 |
| 20 | Surrogate | `925ECB7560B64213B9DCFB51761257BF` | 1 |
| 30 | RVE.A | `6EA44F6633AF49C38075F6B0628381EA` | 1 |
| 40 | Permission | `A9EE952B89D644A397117CA1BF0946B2` | 1 |
| 50 | Vacation | `A0998636CA674D43A01069079B69954C` | 1 |
| 60 | Others | `BFCD5177C026472E8604F8E5E04E1330` | 1 |

### Ventana: Nivel

- **AD_WINDOW_ID:** `7B8F750318EA49CCB2672CAE9569993F`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Level | `CAD068F8BD664F1B812859594F2894FF` | 0 |

### Ventana: Proceso Nómina

- **AD_WINDOW_ID:** `2436AE69637341A98C9FB5E868642870`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Process Payroll | `291` | 0 |

### Ventana: Provisión

- **AD_WINDOW_ID:** `9FD0D46867094C94A53462A7780EE375`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Provision | `D694D67A36D74C4685A50D34B9ED1397` | 0 |

### Ventana: RVE

- **AD_WINDOW_ID:** `A58820464D464C39807261B646DB5A58`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | RVE | `FB9EDE5E9FAF43C0A24FD4385FB6D350` | 0 |

### Ventana: Tipo Acción

- **AD_WINDOW_ID:** `794ED8E8761A4971BFF0ECD3C78B3168`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Action Type | `80E19FA47C804C09928696C5AA9EBEBC` | 0 |

### Ventana: Tipo acción laboral

- **AD_WINDOW_ID:** `8C617188CE584135AB399053C4BF7DDE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Type Job Action | `6787BBF493CE4E2EB08729462487E181` | 0 |

### Ventana: Tipo Contribución

- **AD_WINDOW_ID:** `A21663EB705B44738926787C7D214451`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Contribution Type | `15CC38EF6BA34928ABE69A2F49525F53` | 0 |

### Ventana: Tipo Provisión

- **AD_WINDOW_ID:** `BCE725345D8A4E9D9279DBBCDF5CB06C`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Type Provision | `C9F9D45B356E41BD955B9E1D40F085D3` | 0 |

### Ventana: Uniform or Property of Provision

- **AD_WINDOW_ID:** `54A007A683EA4DDC878C7CB4DD9E25F8`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Uniform or Property of Provision | `26439FEA326D4BA5B4A20E53D8404742` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Action Type (ventana: Tipo Acción)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Commercial Name | `Name` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Pestaña `021070CA34AE41C69879B5B047E5F0C8`

- **AD_TAB_ID:** `021070CA34AE41C69879B5B047E5F0C8` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 133 | Grado | `EM_Sfpr_Grade_ID` | No | No | — |
| 135 | Nivel | `EM_Sfpr_Level_ID` | No | No | — |

### Pestaña `04845F7C140E4220B134160F403CA380`

- **AD_TAB_ID:** `04845F7C140E4220B134160F403CA380` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 33 | Document Type | `EM_Sfpr_C_Doctype_ID` | No | Sí | — |
| 35 | Document No. | `EM_Sfpr_Documentno` | No | Sí | — |

### Job Action (ventana: Acción Laboral)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Employee | `C_Bpartner_ID` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### RVE Detail (ventana: Detalle RVE)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Period | `C_Period_ID` | No | Sí | — |
| 50 | Employee | `C_Bpartner_ID` | No | Sí | — |
| 60 | No. Days | `Nodays` | No | Sí | — |
| 70 | Grand Total Amount | `Grandtotal` | No | Sí | — |
| 72 | RVE Paid on Board | `Payonboard` | No | Sí | — |
| 75 | Cost Center | `C_Costcenter_ID` | No | Sí | — |
| 82 | RVE Paid on Board | `Ispaymentrve` | No | No | — |
| 83 | Concept Paid on Board | `Concept_Payment_Rve_ID` | No | No | — |
| 84 | To Discount | `Amount` | No | No | — |
| 90 | Concept | `Concept_Rve` | No | Sí | — |
| 100 | Status | `Status_Rve` | No | No | — |
| 110 | Processed | `Processed` | No | Sí | — |
| 120 | Period Process | `Period_Processed` | No | Sí | — |
| 125 | Observation | `Description` | No | Sí | — |
| 130 | Active | `Isactive` | No | No | — |
| 150 | Unprocessed RVE | `Unprocessed` | No | No | — |
| 170 | Starting Date | `Startdate` | No | Sí | — |
| 180 | Ending Date | `Enddate` | No | Sí | — |
| 190 | Category Accounting | `Sspr_Category_Acct_ID` | No | Sí | — |
| 210 | RMU | `Rmu` | No | Sí | — |
| 220 | Position | `Sspr_Position_ID` | No | Sí | — |
| 230 | Extraordinary Hours | `Extraordinary_Hours` | No | Sí | — |
| 240 | Supplementary Hours | `Supplementary_Hours` | No | Sí | — |

### Employee Actualization (ventana: Actualización Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Search Key | `—` | No | Sí | 123 |
| 50 | Status | `—` | No | Sí | — |
| 60 | Birth of Day | `—` | No | No | — |
| 70 | Entry Date | `—` | No | Sí | — |
| 80 | Document Type Name | `—` | No | No | — |
| 90 | Document No | `—` | No | Sí | — |
| 100 | Commercial Name | `—` | No | Sí | — |
| 110 | Special Situation | `—` | No | No | — |
| 120 | Labor Regime | `—` | No | No | — |
| 130 | Income Frequency | `—` | No | No | — |
| 140 | Type of Income | `—` | No | No | — |
| 150 | Payroll Template 1 | `—` | No | No | — |
| 160 | Payroll Template 2 | `—` | No | No | — |
| 170 | Project Employee | `—` | No | No | — |
| 180 | City | `—` | No | No | — |
| 190 | Reserve Funds Iess | `—` | No | No | — |
| 200 | Field new disable | `—` | No | No | — |
| 205 | Severance founds | `—` | No | No | — |
| 210 | Concept | `—` | No | No | — |
| 220 | Business Unit | `—` | No | No | 800000 |
| 230 | Product | `—` | No | No | 800000 |
| 240 | 2nd Dimension | `—` | No | No | 800000 |

### RVE.A (ventana: Movimiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Line No. | `Line` | No | Sí | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Surrogate To | `Surrogate_To_ID` | No | No | — |
| 75 | Cost Center | `C_Costcenter_ID` | No | No | — |
| 91 | RVE of surrogate | `Isrve_Surrogate` | No | No | — |
| 92 | Higher Command | `Superior` | No | No | — |
| 95 | Process | `Processed` | No | Sí | — |
| 100 | Description | `Description` | No | No | — |
| 110 | Active | `Isactive` | No | No | — |
| 120 | Link | `Link_Rve` | No | No | — |

### Surrogate Detail (ventana: Detalle Subrrogación)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Period | `C_Period_ID` | No | Sí | — |
| 50 | Employee | `C_Bpartner_ID` | No | Sí | — |
| 60 | Position | `Sfpr_Employee_Position_ID` | No | Sí | — |
| 70 | Surrogate RMU | `Surrogate_Rmu` | No | Sí | — |
| 80 | Employee RMU | `Bpartner_Rmu` | No | Sí | — |
| 90 | Diference RMU | `Diference_Rmu` | No | Sí | — |
| 100 | No. Days | `Nodays` | No | Sí | — |
| 110 | Grand Total Amount | `Grandtotal` | No | Sí | — |
| 120 | Concept Surrogate | `Concept_Surrogate` | No | Sí | — |
| 130 | Processed | `Processed` | No | Sí | — |
| 140 | Period Process | `Period_Processed` | No | Sí | — |
| 150 | Status | `Status_Surrogate` | No | No | — |
| 160 | Active | `Isactive` | No | No | — |
| 170 | Unprocessed Surrogate | `Unprocessed` | No | No | — |
| 190 | Observation | `Description` | No | No | — |
| 200 | Category Accounting | `Sspr_Category_Acct_ID` | No | Sí | — |
| 210 | Starting Date | `Startdate` | No | Sí | — |
| 220 | Ending Date | `Enddate` | No | Sí | — |

### Lines (ventana: Acción Laboral)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Type Job Action | `Sfpr_Type_Job_Action_ID` | No | No | — |
| 40 | Concept | `Sspr_Concept_ID` | No | No | — |
| 50 | Date | `Date_Job_Action` | No | No | — |
| 60 | Amount | `Amount` | No | No | — |
| 70 | Status | `Status` | No | No | — |
| 80 | Observation | `Description` | No | No | — |
| 100 | Active | `Isactive` | No | No | — |
| 120 | Process | `Approve_Jaction` | No | No | — |

### Process Payroll (ventana: Proceso Nómina)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `—` | No | Sí | — |
| 30 | Commercial Name | `—` | No | Sí | — |
| 110 | Active | `—` | No | Sí | — |
| 120 | Create Payroll | `—` | No | No | — |

### Level (ventana: Nivel)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 50 | Rmu | `Rmu` | No | No | — |
| 60 | Active | `Isactive` | No | No | — |
| 70 | Position | `Sfpr_Employee_Position_ID` | No | No | — |

### Others (ventana: Movimiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Line No. | `Line` | No | Sí | — |
| 50 | Employee | `C_Bpartner_ID` | No | No | — |
| 60 | Starting Date | `Startdate` | No | No | — |
| 70 | Ending Date | `Enddate` | No | No | — |
| 80 | Hours No. | `Nohours` | No | No | — |
| 90 | Observation | `Description` | No | No | — |
| 100 | Active | `Isactive` | No | No | — |

### Vacation (ventana: Movimiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Line No. | `Line` | No | Sí | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 80 | Hours No. | `Nohours` | No | No | — |
| 90 | Observation | `Description` | No | No | — |
| 100 | Active | `Isactive` | No | No | — |

### Surrogate (ventana: Movimiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Line No. | `Line` | No | Sí | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Surrogate To | `Surrogate_To_ID` | No | No | — |
| 95 | Processed | `Processed` | No | Sí | — |
| 100 | Observation | `Description` | No | No | — |
| 110 | Active | `Isactive` | No | No | — |
| 115 | Link | `Link_Surrogate` | No | No | — |

### Proposal Situation

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Action Type | `Sfpr_Action_Type_ID` | No | No | — |
| 30 | Position | `Sfpr_Employee_Position_ID` | No | No | — |
| 40 | Proposal RMU | `Proposal_Rmu` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Cost Center | `C_Costcenter_ID` | No | No | — |
| 80 | Active | `Isactive` | No | No | — |

### Movement (ventana: Movimiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Transaction Document | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `Documentno` | No | No | — |
| 50 | Movement of Date | `Transaction_Date` | No | No | — |
| 60 | Observation | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |

### Pestaña `6868C16BE4D7497CAF158389B062B030`

- **AD_TAB_ID:** `6868C16BE4D7497CAF158389B062B030` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 60 | Amount | `EM_Sfpr_Amount` | No | No | — |
| 70 | Concept | `EM_Sfpr_Concept_ID` | No | No | — |

### Pestaña `7E1CBBD4749342EDBCF91F796CA2388D`

- **AD_TAB_ID:** `7E1CBBD4749342EDBCF91F796CA2388D` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 110 | Observation | `EM_Sfpr_Description` | No | No | — |

### RVE (ventana: RVE)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Grade | `Sfpr_Grade_ID` | No | No | — |
| 30 | Position | `Sfpr_Employee_Position_ID` | No | No | — |
| 40 | Rmu | `Rmu` | No | No | — |
| 50 | % Handimax | `Porc_Handimax` | No | No | — |
| 60 | RVE Handimax Daily | `RVE_Handimax` | No | Sí | — |
| 70 | % Panamax | `Porc_Panamax` | No | No | — |
| 80 | RVE Panamax Daily | `RVE_Panamax` | No | Sí | — |
| 90 | % Aframax | `Porc_Aframax` | No | No | — |
| 100 | RVE Aframax Daily | `RVE_Aframax` | No | Sí | — |
| 110 | Active | `Isactive` | No | No | — |
| 120 | Value of 1st level | `Value1` | No | No | 01AAAE11C5854DE2BA64466BC3419231 |
| 130 | Value of 2nd level | `Value2` | No | No | 01AAAE11C5854DE2BA64466BC3419231 |
| 140 | Value of 3rd level | `Value3` | No | No | 01AAAE11C5854DE2BA64466BC3419231 |

### Grade (ventana: Grado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Search Key | `Value` | No | No | — |
| 30 | Commercial Name | `Name` | No | No | — |
| 50 | Rmu | `Rmu` | No | No | — |
| 60 | Active | `Isactive` | No | No | — |
| 70 | Position | `Sfpr_Employee_Position_ID` | No | No | — |

### Uniform or Property of Provision (ventana: Uniform or Property of Provision)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Cost Center | `C_Costcenter_ID` | No | No | — |
| 60 | Provision | `Sfpr_Provision_ID` | No | No | — |
| 65 | Amount | `Amount` | No | No | — |
| 70 | Delivery Date | `Provision_Date` | No | No | — |
| 75 | Status Provision | `Status_Provision` | No | No | — |
| 80 | Active | `Isactive` | No | No | — |

### Permission (ventana: Movimiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Line No. | `Line` | No | Sí | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 80 | Hours No. | `Nohours` | No | No | — |
| 90 | Recoverable | `Recoverable` | No | No | — |
| 100 | Observation | `Description` | No | No | — |
| 110 | Active | `Isactive` | No | No | — |

### Pestaña `AE4D0B14798E47A5B0CEF62C52DB235B`

- **AD_TAB_ID:** `AE4D0B14798E47A5B0CEF62C52DB235B` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 215 | Nodays | `EM_Sfpr_Nodays` | No | No | — |

### Type Provision (ventana: Tipo Provisión)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Provision (ventana: Provisión)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Type Provision | `Sfpr_Type_Provision_ID` | No | No | — |
| 60 | Active | `Isactive` | No | No | — |

### Contribution Type (ventana: Tipo Contribución)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 25 | Is Laboral Regimen | `Islaboralregime` | No | No | — |
| 30 | Commercial Name | `Name` | No | No | — |
| 40 | Personal Concept | `Personal_Concept` | No | No | — |
| 50 | % Personal | `Porc_Personal` | No | No | — |
| 60 | Concept Bosses | `Concept_Bosses` | No | No | — |
| 70 | % Bosses | `Porc_Bosses` | No | No | — |
| 80 | Total Income Concept | `Total_Income_Concept` | No | No | — |
| 85 | Income | `Income_Concept_ID` | No | No | — |
| 90 | Active | `Isactive` | No | No | — |

### Actual Situation

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Action Type | `Sfpr_Action_Type_ID` | No | No | — |
| 40 | Position | `Sfpr_Employee_Position_ID` | No | No | — |
| 50 | Actual RMU | `Actual_Rmu` | No | No | — |
| 60 | Starting Date | `Startdate` | No | No | — |
| 70 | Ending Date | `Enddate` | No | No | — |
| 80 | Cost Center | `C_Costcenter_ID` | No | Sí | — |
| 90 | Active | `Isactive` | No | No | — |

### Direcciones (ventana: Actualización Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Empleado | `—` | No | Sí | — |
| 40 | Name | `—` | No | No | — |
| 50 | Active | `—` | No | No | — |
| 60 | Location / Address | `—` | No | No | — |
| 70 | Phone | `—` | No | No | — |
| 80 | Alternative Phone | `—` | No | No | — |
| 90 | Fax | `—` | No | No | — |
| 100 | Tax Location | `—` | No | No | — |

### Salary Evolution

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Starting Date | `Startdate` | No | No | — |
| 50 | Ending Date | `Enddate` | No | No | — |
| 60 | Amount | `Amount` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |
| 90 | Expire | `Expire` | No | No | — |

### Pestaña `F39C06C880BC449FA87E03CA4CC8DDD9`

- **AD_TAB_ID:** `F39C06C880BC449FA87E03CA4CC8DDD9` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 90 | Status | `EM_Sfpr_Status` | No | No | — |
| 100 | Approved by | `EM_Sfpr_Approved_By` | No | No | — |

### Type Job Action (ventana: Tipo acción laboral)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Pestaña `F5EC9FEDEAB74C77A92942201415EE7D`

- **AD_TAB_ID:** `F5EC9FEDEAB74C77A92942201415EE7D` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 33 | Document Type | `EM_Sfpr_C_Doctype_ID` | No | No | — |
| 35 | Document No. | `EM_Sfpr_Documentno` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos en el módulo incluyen botones típicos como 'Completar', 'Retornar' y 'Rechazar', que guían a los usuarios en el flujo de trabajo. Aunque no hay informes específicos, se implementan validaciones internas en cada proceso para asegurar la coherencia de los datos, utilizando funciones que permiten la manipulación y gestión segura de la información. Ejemplos incluyen validaciones en los movimientos y contribuciones de los empleados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.hrm.payroll.advanced.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archivo Pago Decimos Pichincha TXT | File Payment Tenth  pichincha  TXT | File Payment Tenth  pichincha  TXT | Java `ArchPayTenthBankPichinchaTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/advanced/create_txt/ArchPayTenthBankPichinchaTXT.java` |
| Botón (Java) | Archivo Pago Utilidades Banco Pichincha TXT | File Utilities Payment Pichincha Bank TXT | File UtiliesPayment Pichincha Bank TXT | Java `ArchUtilitiesBankPichinchaTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/advanced/create_txt/ArchUtilitiesBankPichinchaTXT.java` |
| Botón (PL/pgSQL) | Caducar | Expire | Sfpr_ExpireEvolutionSalary | `sfpr_expiresalary_employee` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Calcular RVE | RVE Calculate | RVE Calculate | `sfpr_rve_calculate` | No existe valor configurado para RVE - Aframax. Empleado-; No existe valor configurado para RVE - Handimax. Empleado-; No existe valor configurado para RVE - Panamax. Empleado-; La columna Category Accounting es obligat… | — |
| Botón (PL/pgSQL) | Calcular Subrrogacion | Surrogate Calculate | Surrogate Calculate | `sfpr_surrogate_calculate` | Error: La columna Surrogate RMU es obligatoria y no se puede dejar en blanco. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL,… | — |
| Botón (PL/pgSQL) | Cargar Concepto RVE | Load Concept RVE | Load Concept RVE | `sfpr_create_concept_rve` | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_RVE_ID FR… | — |
| Botón (PL/pgSQL) | Cargar Concepto Subrrogación | Load Concept Surrogate | Load Concept Surrogate | `sfpr_create_concept_surrogate` | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_SURROGATE… | — |
| Botón (PL/pgSQL) | Cargar Plantilla de Nomina | Cargar Plantilla de Nomina | LoadPayrollTampleteAdvanced | `sfpr_load_payroll_template` | RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP4 '||v_Period_ID);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP5 '||v_Period_ID);; Insert concepts of the template into period. | — |
| Botón (PL/pgSQL) | Proceso Contribución IESS | Process Contribution IESS | Process Contribution IESS | `sfpr_updatecontributioniess` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | RVE desprocesado | Unprocessed RVE | Unprocessed RVE | `sfpr_unprocessed_rve_detail` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Subrrogacion Desprocesada | Unprocessed Surrogate | Unprocessed Surrogate | `sfpr_unprocessed_sdetail` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Historia Laboral IESS | History Laboral IESS | History Laboral IESS | *(OBUIAPP / manual)* | History Laboral IESS | — |
| Proceso / otro | Total Ingresos Vs Total Egresos | Total Ingresos Vs Total Egresos | TotalIngresosVsTotalEgresos | *(OBUIAPP / manual)* | Total Ingresos Vs Total Egresos | — |
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
| Botón (Java) | Archivo Pago Decimos Pichincha TXT | `ArchPayTenthBankPichinchaTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/advanced/create_txt/ArchPayTenthBankPichinchaTXT.java` |
| Botón (Java) | Archivo Pago Utilidades Banco Pichincha TXT | `ArchUtilitiesBankPichinchaTXT` | Proceso Java (toolbar/background) | `cYearId` | — | `src/com/sidesoft/hrm/payroll/advanced/create_txt/ArchUtilitiesBankPichinchaTXT.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archivo Pago Decimos Pichincha TXT | File Payment Tenth  pichincha  TXT | File Payment Tenth  pichincha  TXT | Java `ArchPayTenthBankPichinchaTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/advanced/create_txt/ArchPayTenthBankPichinchaTXT.java` |
| Botón (Java) | Archivo Pago Utilidades Banco Pichincha TXT | File Utilities Payment Pichincha Bank TXT | File UtiliesPayment Pichincha Bank TXT | Java `ArchUtilitiesBankPichinchaTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cYearId` | `src/com/sidesoft/hrm/payroll/advanced/create_txt/ArchUtilitiesBankPichinchaTXT.java` |
| Botón (PL/pgSQL) | Caducar | Expire | Sfpr_ExpireEvolutionSalary | `sfpr_expiresalary_employee` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Calcular RVE | RVE Calculate | RVE Calculate | `sfpr_rve_calculate` | No existe valor configurado para RVE - Aframax. Empleado-; No existe valor configurado para RVE - Handimax. Empleado-; No existe valor configurado para RVE - Panamax. Empleado-; La columna Category Accounting es obligat… | — |
| Botón (PL/pgSQL) | Calcular Subrrogacion | Surrogate Calculate | Surrogate Calculate | `sfpr_surrogate_calculate` | Error: La columna Surrogate RMU es obligatoria y no se puede dejar en blanco. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL,… | — |
| Botón (PL/pgSQL) | Cargar Concepto RVE | Load Concept RVE | Load Concept RVE | `sfpr_create_concept_rve` | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_RVE_ID FR… | — |
| Botón (PL/pgSQL) | Cargar Concepto Subrrogación | Load Concept Surrogate | Load Concept Surrogate | `sfpr_create_concept_surrogate` | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_SURROGATE… | — |
| Botón (PL/pgSQL) | Cargar Plantilla de Nomina | Cargar Plantilla de Nomina | LoadPayrollTampleteAdvanced | `sfpr_load_payroll_template` | RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP4 '||v_Period_ID);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP5 '||v_Period_ID);; Insert concepts of the template into period. | — |
| Botón (PL/pgSQL) | Proceso Contribución IESS | Process Contribution IESS | Process Contribution IESS | `sfpr_updatecontributioniess` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | RVE desprocesado | Unprocessed RVE | Unprocessed RVE | `sfpr_unprocessed_rve_detail` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Subrrogacion Desprocesada | Unprocessed Surrogate | Unprocessed Surrogate | `sfpr_unprocessed_sdetail` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Historia Laboral IESS | History Laboral IESS | History Laboral IESS | *(OBUIAPP / manual)* | History Laboral IESS | — |
| Proceso / otro | Total Ingresos Vs Total Egresos | Total Ingresos Vs Total Egresos | TotalIngresosVsTotalEgresos | *(OBUIAPP / manual)* | Total Ingresos Vs Total Egresos | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archivo Pago Decimos Pichincha TXT | File Payment Tenth  pichincha  TXT | Java `ArchPayTenthBankPichinchaTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Botón (Java) | Archivo Pago Utilidades Banco Pichincha TXT | File Utilities Payment Pichincha Bank TXT | Java `ArchUtilitiesBankPichinchaTXT` | Proceso Openbravo registro `cYearId` | Proceso Openbravo registro `cYearId` |
| Botón (PL/pgSQL) | Caducar | Expire | PL `sfpr_expiresalary_employee` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Calcular RVE | RVE Calculate | PL `sfpr_rve_calculate` | No existe valor configurado para RVE - Aframax. Empleado-; No existe valor configurado para RVE - Handimax. Empleado-; No existe valor configurado para RVE - Panamax. Empleado-; La columna Category Accounting es obligat… | No existe valor configurado para RVE - Aframax. Empleado-; No existe valor configurado para RVE - Handimax. Empleado-; No existe valor configurado para RVE - Panamax. Empleado-; La columna Category Accounting es obligatoria. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ; |
| Botón (PL/pgSQL) | Calcular Subrrogacion | Surrogate Calculate | PL `sfpr_surrogate_calculate` | Error: La columna Surrogate RMU es obligatoria y no se puede dejar en blanco. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL,… | Error: La columna Surrogate RMU es obligatoria y no se puede dejar en blanco. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; LEFT JOIN SSFL_VESSEL_TYPE VT ON SSFL_VESSEL_TYPE_ID = EM_SSFL_VESSEL_TYPE_ID |
| Botón (PL/pgSQL) | Cargar Concepto RVE | Load Concept RVE | PL `sfpr_create_concept_rve` | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_RVE_ID FR… | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_RVE_ID FROM SFPR_RVE_DETAIL; WHERE STATUS_RVE='CO' AND PROCESSED = 'Y' |
| Botón (PL/pgSQL) | Cargar Concepto Subrrogación | Load Concept Surrogate | PL `sfpr_create_concept_surrogate` | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_SURROGATE… | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_SURROGATE_ID FROM SFPR_EMPLOYEE_SURROGATE |
| Botón (PL/pgSQL) | Cargar Plantilla de Nomina | Cargar Plantilla de Nomina | PL `sfpr_load_payroll_template` | RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP4 '||v_Period_ID);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP5 '||v_Period_ID);; Insert concepts of the template into period. | RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP4 '||v_Period_ID);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP5 '||v_Period_ID);; Insert concepts of the template into period. |
| Botón (PL/pgSQL) | Proceso Contribución IESS | Process Contribution IESS | PL `sfpr_updatecontributioniess` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | RVE desprocesado | Unprocessed RVE | PL `sfpr_unprocessed_rve_detail` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Subrrogacion Desprocesada | Unprocessed Surrogate | PL `sfpr_unprocessed_sdetail` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Historia Laboral IESS | History Laboral IESS | — | History Laboral IESS | — |
| Proceso / otro | Total Ingresos Vs Total Egresos | Total Ingresos Vs Total Egresos | — | Total Ingresos Vs Total Egresos | — |
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
| `Sfpr_ValidRVE` | The selected RVE is processed. | The selected RVE is processed. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfpr_ErrorInvalidDates` | The End Date must be greater than the Start Date. | The End Date must be greater than the Start Date. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfpr_ValidSurrogate` | The select Surrogate is processed. | The select Surrogate is processed. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `em_sfpr_surrogateinvalid` | The vessel type is already selected surrogate and has different substitutions within the same periods. | The vessel type is already selected surrogate and has different substitutions within the same periods. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SFPR_INVALIDCONTRIBUTION` | The type of contribution is icorrecto, please check the configuration. | The type of contribution is icorrecto, please check the configuration. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `em_sfpr_vesseltypesurrogate` | The vessel type is already selected surrogate | The vessel type is already selected surrogate | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfpr_ValidateRVEDetail` | The selected RVE is being used by another process. | The selected RVE is being used by another process. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SFPR_INVALIDCONTRIBUTIONBOSSES` | The type of contribution bosses  is invalid. | The type of contribution bosses  is invalid. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfpr_ValidateEvolutionSalaryExpire` | To continue must expire the other lines of Salary Evolution that belong to this contract. | To continue must expire the other lines of Salary Evolution that belong to this contract. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfpr_ValidMovement` | Delete detail lines to continue. | Delete detail lines to continue. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfpr_ValidateDate` | The End Date must be greater than the Start Date | The End Date must be greater than the Start Date | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `em_sfpr_dateincorrect` | Different substitutions within the same periods. | Different substitutions within the same periods. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SFPR_INVALIDCONTRIBUTIONPERSONAL` | The type of personal contribution is invalid. | The type of personal contribution is invalid. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfpr_ValidateSurrogateDetail` | The selected surrogate is being used by another process. | The selected surrogate is being used by another process. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sfpr_validate_frp` | Enter the number of days. | Enter the number of days. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfpr_InvalidDate` | El periodo en el cual intenta grabar se encuentra cerrado. | El periodo en el cual intenta grabar se encuentra cerrado. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sfpr_movement_process` | The Movement Type is being used by another process. | The Movement Type is being used by another process. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sfpr_ErrorExpire` | The line in the Expired state can not be deleted. | The line in the Expired state can not be deleted. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SFPR_INVALID_CONTRIBUTION` | The type of contribution is invalid. | The type of contribution is invalid. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sfpr_validate_costcenter` | The selected Vessel - Area is invalid, please parameterize the Vessel - Area at the head | The selected Vessel - Area is invalid, please parameterize the Vessel - Area at the head | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SFPR_EndStartPeriod` | End Period must be greater than Start Period. | End Period must be greater than Start Period. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo utilza clases Java para gestionar la lógica de negocio compleja, como la actualización de datos relacionados con los contratos y las posiciones actuales de los empleados. Clases como 'UpdateActualPositionRMU' y 'UpdateAmountRMU' realizan llamadas de retorno para asegurar que la interfaz del usuario se complete correctamente basándose en la información almacenada en las tablas de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.hrm.payroll.advanced`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `UpdateActualPositionRMU` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/advanced/ad_callouts/UpdateActualPositionRMU.java` |
| `UpdateAmountRMU` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/advanced/ad_callouts/UpdateAmountRMU.java` |
| `UpdateDocumentSequencePR` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/advanced/ad_callouts/UpdateDocumentSequencePR.java` |
| `UpdateDocumentSequencePRAL` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/advanced/ad_callouts/UpdateDocumentSequencePRAL.java` |
| `UpdateDocumentSequencePRAV` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/advanced/ad_callouts/UpdateDocumentSequencePRAV.java` |
| `UpdatePorcentageRMU` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/advanced/ad_callouts/UpdatePorcentageRMU.java` |
| `ArchPayTenthBankPichinchaTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/advanced/create_txt/ArchPayTenthBankPichinchaTXT.java` |
| `ArchUtilitiesBankPichinchaTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/advanced/create_txt/ArchUtilitiesBankPichinchaTXT.java` |
| `ByteArrayDataSource` | email | DataSource | — | `src/com/sidesoft/hrm/payroll/advanced/email/ByteArrayDataSource.java` |
| `EMailAuthenticator` | email | Authenticator | — | `src/com/sidesoft/hrm/payroll/advanced/email/EMailAuthenticator.java` |
| `EMailUtils` | email | — | — | `src/com/sidesoft/hrm/payroll/advanced/email/EMailUtils.java` |
| `UpdateBirthdayEmployeeEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/advanced/event/UpdateBirthdayEmployeeEvent.java` |
| `UpdateConceptLineEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/advanced/event/UpdateConceptLineEvent.java` |
| `UpdateSequenceLoansEvent` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/advanced/event/UpdateSequenceLoansEvent.java` |
| `ValidateDateEvolutionSalary` | event | EntityPersistenceEventObserver | — | `src/com/sidesoft/hrm/payroll/advanced/event/ValidateDateEvolutionSalary.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SFPR_DATE_VALIDATE_TRG` | `sfpr_evolution_salary` | before INSERT/UPDATE | Validación reutilizable de campos. |
| Trigger `SFPR_ERVE_DETAIL_TRG` | `sfpr_employee_rve` | before UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SFPR_ESURROGATE_DETAIL_TRG` | `sfpr_employee_surrogate` | before UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SFPR_INVALID_COSTCENTER_TRG` | `sfpr_employee_situation` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SFPR_VALIDATE_MOVEMENT_TRG` | `sfpr_movement_type` | before INSERT/UPDATE/DELETE | Validación reutilizable de campos. |
| Trigger `SFPR_VALIDATE_RVE_DETAIL_TRG` | `sfpr_rve_detail` | before UPDATE/DELETE | Validación reutilizable de campos. |
| Trigger `SFPR_VALIDATE_SDETAIL_TRG` | `sfpr_surrogate_detail` | before UPDATE/DELETE | Validación reutilizable de campos. |
| Trigger `SFPR_VALIDCONTRIBUTION_TRG` | `sfpr_employee_contribution` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `sfpr_period_calculate` | `C_Period.openclose= 'C'` |
| AD_VAL_RULE | — | `sfpr_c_doctype_loans` | `c_doctype.AD_TABLE_ID IN (
SELECT AD_TABLE_ID FROM AD_TABLE WHERE UPPER(TABLENAME) = UPPER('sspr_loans'))` |
| AD_VAL_RULE | — | `sfpr_document_type` | `C_DocType.C_DocType_ID in (Select C_Doctype_id From sfpr_movement_type)` |
| AD_VAL_RULE | — | `SFPR_IsEmployee` | `C_BPartner.IsEmployee = 'Y'` |
| AD_VAL_RULE | — | `open period control` | `EXISTS (SELECT * FROM c_periodcontrol_log pc WHERE C_Period.C_Period_ID=pc.periodno AND pc.Periodaction='O')` |
| AD_VAL_RULE | — | `period payroll open` | `C_Period.openclose = 'C'` |
| AD_VAL_RULE | — | `SFPR_DOCUMENT_TYPE` | `C_DOCTYPE.AD_TABLE_ID = (SELECT AD_TABLE_ID FROM AD_TABLE  WHERE UPPER(NAME) = 'SFPR_MOVEMENT_TYPE')` |
| AD_VAL_RULE | — | `Data Concept` | `SSPR_Concept.concepttype='D'` |
| AD_VAL_RULE | — | `sfpr_employee` | `C_BPartner.IsEmployee = 'Y' and C_BPartner.IsActive = 'Y'` |
| AD_VAL_RULE | — | `Sfpr_endperiod` | `(C_Period.startdate = (select startdate from c_period cp where cp.c_period_id = @EndPeriod@) or @EndPeriod@ is null)` |
| AD_VAL_RULE | — | `sfpr_startperiod` | `(C_Period.startdate = (select startdate from c_period cp where cp.c_period_id = @StartPeriod@) or @StartPeriod@ is null)` |
| AD_VAL_RULE | — | `Formula Concept` | `SSPR_Concept.concepttype='F'` |
| Java event/validator | `UpdateBirthdayEmployeeEvent` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/advanced/event/UpdateBirthdayEmployeeEvent.java`)* |
| Java event/validator | `UpdateConceptLineEvent` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/advanced/event/UpdateConceptLineEvent.java`)* |
| Java event/validator | `UpdateSequenceLoansEvent` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/advanced/event/UpdateSequenceLoansEvent.java`)* |
| Función PL `sfpr_create_concept_rve` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee |
| Función PL `sfpr_create_concept_rve2` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee |
| Función PL `sfpr_create_concept_surrogate` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee |
| Función PL `sfpr_create_concept_surrogate2` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee |
| Función PL `sfpr_load_payroll_template` | — | invocación proceso | RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP4 '||v_Period_ID);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP5 '||v_Period_ID);; Insert concepts of the template into period. |
| Función PL `sfpr_process_payroll` | — | invocación proceso | Ya existen nóminas superiores a fecha de proceso; Imposible desprocesar, vacacaciones calculadas a la fecha; ERROR= EXISTE CONFIGURADO MAS DE UN CONCEPTO PARA DIAS LABORADOS |
| Función PL `sfpr_rve_calculate` | — | invocación proceso | No existe valor configurado para RVE - Aframax. Empleado-; No existe valor configurado para RVE - Handimax. Empleado-; No existe valor configurado para RVE - Panamax. Empleado- |
| Función PL `sfpr_rve_calculate2` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee |
| Función PL `sfpr_surrogate_calculate` | — | invocación proceso | Error: La columna Surrogate RMU es obligatoria y no se puede dejar en blanco. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ; |
| Función PL `sfpr_surrogate_calculate2` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; LEFT JOIN SSFL_VESSEL_TYPE VT ON SSFL_VESSEL_TYPE_ID = EM_SSFL_VESSEL_TYPE_ID |
| Función PL `sfpr_surrogate_calculate2_liq` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; LEFT JOIN SSFL_VESSEL_TYPE VT ON SSFL_VESSEL_TYPE_ID = EM_SSFL_VESSEL_TYPE_ID |
| Función PL `sfpr_updatecontribiess2_liq` | — | invocación proceso | PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; |
| Función PL `sfpr_updatecontributioniess2` | — | invocación proceso | PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y las funciones PL son fundamentales para mantener la integridad y la lógica de negocio del módulo. Con un total de 8 triggers y 17 funciones PL, estos elementos garantizan que las operaciones sobre las tablas se realicen conforme a las reglas de negocio definidas, facilitando así el soporte en caso de problemas de datos o inconsistencias en la información registrada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SFPR_VALIDCONTRIBUTION_TRG` | `sfpr_employee_contribution` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SFPR_VALIDCONTRIBUTION_TRG.xml` |
| `SFPR_ERVE_DETAIL_TRG` | `sfpr_employee_rve` | before | UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SFPR_ERVE_DETAIL_TRG.xml` |
| `SFPR_INVALID_COSTCENTER_TRG` | `sfpr_employee_situation` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SFPR_INVALID_COSTCENTER_TRG.xml` |
| `SFPR_ESURROGATE_DETAIL_TRG` | `sfpr_employee_surrogate` | before | UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SFPR_ESURROGATE_DETAIL_TRG.xml` |
| `SFPR_DATE_VALIDATE_TRG` | `sfpr_evolution_salary` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/SFPR_DATE_VALIDATE_TRG.xml` |
| `SFPR_VALIDATE_MOVEMENT_TRG` | `sfpr_movement_type` | before | INSERT/UPDATE/DELETE | Validación reutilizable de campos. | `model/triggers/SFPR_VALIDATE_MOVEMENT_TRG.xml` |
| `SFPR_VALIDATE_RVE_DETAIL_TRG` | `sfpr_rve_detail` | before | UPDATE/DELETE | Validación reutilizable de campos. | `model/triggers/SFPR_VALIDATE_RVE_DETAIL_TRG.xml` |
| `SFPR_VALIDATE_SDETAIL_TRG` | `sfpr_surrogate_detail` | before | UPDATE/DELETE | Validación reutilizable de campos. | `model/triggers/SFPR_VALIDATE_SDETAIL_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sfpr_create_concept_rve` | Cargar Concepto RVE | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_RVE_ID FR… | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_RVE_ID FROM SFPR_RVE_DETAIL; WHERE STATUS_RVE='CO' AND PROCESSED = 'Y' | `model/functions/SFPR_CREATE_CONCEPT_RVE.xml` |
| `sfpr_create_concept_rve2` | — | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; PERFORM AD_UPDATE_PINSTANCE(PInsta… | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | `model/functions/SFPR_CREATE_CONCEPT_RVE2.xml` |
| `sfpr_create_concept_surrogate` | Cargar Concepto Subrrogación | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_SURROGATE… | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; IN (SELECT SFPR_EMPLOYEE_SURROGATE_ID FROM SFPR_EMPLOYEE_SURROGATE | `model/functions/SFPR_CREATE_CONCEPT_SURROGATE.xml` |
| `sfpr_create_concept_surrogate2` | — | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; PERFORM AD_UPDATE_PINSTANCE(PInsta… | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | `model/functions/SFPR_CREATE_CONCEPT_SURROGATE2.xml` |
| `sfpr_expiresalary_employee` | Caducar | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SFPR_EXPIRESALARY_EMPLOYEE.xml` |
| `sfpr_load_payroll_template` | Cargar Plantilla de Nomina | RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP4 '||v_Period_ID);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP5 '||v_Period_ID);; Insert concepts of the template into period. | RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP4 '||v_Period_ID);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP5 '||v_Period_ID);; Insert concepts of the template into period. | `model/functions/SFPR_LOAD_PAYROLL_TEMPLATE.xml` |
| `sfpr_process_payroll` | — | Ya existen nóminas superiores a fecha de proceso; Imposible desprocesar, vacacaciones calculadas a la fecha; ERROR= EXISTE CONFIGURADO MAS DE UN CONCEPTO PARA DIAS LABORADOS; 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL A… | Ya existen nóminas superiores a fecha de proceso; Imposible desprocesar, vacacaciones calculadas a la fecha; ERROR= EXISTE CONFIGURADO MAS DE UN CONCEPTO PARA DIAS LABORADOS; 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; ELIMINAR RASTROS DEL FONDO DE RESERVA IESS | `model/functions/SFPR_PROCESS_PAYROLL.xml` |
| `sfpr_rve_calculate` | Calcular RVE | No existe valor configurado para RVE - Aframax. Empleado-; No existe valor configurado para RVE - Handimax. Empleado-; No existe valor configurado para RVE - Panamax. Empleado-; La columna Category Accounting es obligat… | No existe valor configurado para RVE - Aframax. Empleado-; No existe valor configurado para RVE - Handimax. Empleado-; No existe valor configurado para RVE - Panamax. Empleado-; La columna Category Accounting es obligatoria. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ; | `model/functions/SFPR_RVE_CALCULATE.xml` |
| `sfpr_rve_calculate2` | — | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; COALESCE((CASE WHEN UPPER(VT.VESSE… | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by employee; COALESCE((CASE WHEN UPPER(VT.VESSEL_TYPE) = 'A' THEN RV.RVE_AFRAMAX * (TO_NUMBER((ES.ENDDATE - ES.STARTDATE))+1); WHEN UPPER(VT.VESSEL_TYPE) = 'H' THEN RV.RVE_HANDIMAX * (TO_NUMBER((ES.ENDDATE - ES.STARTDATE))+1); WHEN UPPER(VT.VESSEL_TYPE) = 'P' THEN RV.RVE_PANAMAX * (TO_NUMBER((ES.ENDDATE - ES.STARTDATE))+1) END),0) AS GRANDTOTAL | `model/functions/SFPR_RVE_CALCULATE2.xml` |
| `sfpr_surrogate_calculate` | Calcular Subrrogacion | Error: La columna Surrogate RMU es obligatoria y no se puede dejar en blanco. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL,… | Error: La columna Surrogate RMU es obligatoria y no se puede dejar en blanco. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; LEFT JOIN SSFL_VESSEL_TYPE VT ON SSFL_VESSEL_TYPE_ID = EM_SSFL_VESSEL_TYPE_ID | `model/functions/SFPR_SURROGATE_CALCULATE.xml` |
| `sfpr_surrogate_calculate2` | — | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; LEFT JOIN SSFL_VESSEL_TYPE VT ON SSFL_VESSEL_TYPE_ID = EM_SSFL_VESSEL_TYPE_ID; P… | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; LEFT JOIN SSFL_VESSEL_TYPE VT ON SSFL_VESSEL_TYPE_ID = EM_SSFL_VESSEL_TYPE_ID; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | `model/functions/SFPR_SURROGATE_CALCULATE2.xml` |
| `sfpr_surrogate_calculate2_liq` | — | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; LEFT JOIN SSFL_VESSEL_TYPE VT ON SSFL_VESSEL_TYPE_ID = EM_SSFL_VESSEL_TYPE_ID; P… | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; LEFT JOIN SSFL_VESSEL_TYPE VT ON SSFL_VESSEL_TYPE_ID = EM_SSFL_VESSEL_TYPE_ID; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | `model/functions/SFPR_SURROGATE_CALCULATE2_LIQ.xml` |
| `sfpr_unprocessed_rve_detail` | RVE desprocesado | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SFPR_UNPROCESSED_RVE_DETAIL.xml` |
| `sfpr_unprocessed_sdetail` | Subrrogacion Desprocesada | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SFPR_UNPROCESSED_SDETAIL.xml` |
| `sfpr_updatecontribiess2_liq` | — | PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | `model/functions/SFPR_UPDATECONTRIBIESS2_LIQ.xml` |
| `sfpr_updatecontributioniess` | Proceso Contribución IESS | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SFPR_UPDATECONTRIBUTIONIESS.xml` |
| `sfpr_updatecontributioniess2` | — | PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 1, v_Message) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | `model/functions/SFPR_UPDATECONTRIBUTIONIESS2.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Archivo Pago Decimos Pichincha TXT | `File Payment Tenth  pichincha  TXT` | Botón (Java) | Java `ArchPayTenthBankPichinchaTXT` | N | Proceso Openbravo registro `documentno` |
| 2 | Archivo Pago Utilidades Banco Pichincha TXT | `File UtiliesPayment Pichincha Bank TXT` | Botón (Java) | Java `ArchUtilitiesBankPichinchaTXT` | N | Proceso Openbravo registro `cYearId` |
| 3 | Caducar | `Sfpr_ExpireEvolutionSalary` | Botón (PL/pgSQL) | PL `sfpr_expiresalary_employee` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 4 | Calcular RVE | `RVE Calculate` | Botón (PL/pgSQL) | PL `sfpr_rve_calculate` | N | No existe valor configurado para RVE - Aframax. Empleado-; No existe valor configurado para RVE - Handimax. Empleado-; No existe valor configurado para RVE - Panamax. Empleado-; La |
| 5 | Calcular Subrrogacion | `Surrogate Calculate` | Botón (PL/pgSQL) | PL `sfpr_surrogate_calculate` | N | Error: La columna Surrogate RMU es obligatoria y no se puede dejar en blanco. Empleado-; RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PI |
| 6 | Cargar Concepto RVE | `Load Concept RVE` | Botón (PL/pgSQL) | PL `sfpr_create_concept_rve` | N | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by emplo |
| 7 | Cargar Concepto Subrrogación | `Load Concept Surrogate` | Botón (PL/pgSQL) | PL `sfpr_create_concept_surrogate` | N | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; Create the RVE and Copy Concepts by emplo |
| 8 | Cargar Plantilla de Nomina | `LoadPayrollTampleteAdvanced` | Botón (PL/pgSQL) | PL `sfpr_load_payroll_template` | N | RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP4 '||v_Period_ID);; RAISE_APPLICATION_ERROR(-20000, 'INGRESO AL LOOP5 '||v_Period_ID);; Insert concepts of the template into period. |
| 9 | Proceso Contribución IESS | `Process Contribution IESS` | Botón (PL/pgSQL) | PL `sfpr_updatecontributioniess` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 10 | RVE desprocesado | `Unprocessed RVE` | Botón (PL/pgSQL) | PL `sfpr_unprocessed_rve_detail` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 11 | Subrrogacion Desprocesada | `Unprocessed Surrogate` | Botón (PL/pgSQL) | PL `sfpr_unprocessed_sdetail` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

**Total acciones documentadas (extract):** **11** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `com.sidesoft.hrm.payroll.advanced`.

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

# Glosario — prefijo `SFPR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SFPR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.hrm.payroll.advanced` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `File Payment Tenth  pichincha  TXT` — Archivo Pago Decimos Pichincha TXT
- `File UtiliesPayment Pichincha Bank TXT` — Archivo Pago Utilidades Banco Pichincha TXT
- `Sfpr_ExpireEvolutionSalary` — Caducar
- `RVE Calculate` — Calcular RVE
- `Surrogate Calculate` — Calcular Subrrogacion
- `Load Concept RVE` — Cargar Concepto RVE
- `Load Concept Surrogate` — Cargar Concepto Subrrogación
- `LoadPayrollTampleteAdvanced` — Cargar Plantilla de Nomina
- `Process Contribution IESS` — Proceso Contribución IESS
- `Unprocessed RVE` — RVE desprocesado
- `Unprocessed Surrogate` — Subrrogacion Desprocesada
- `History Laboral IESS` — Historia Laboral IESS
- `TotalIngresosVsTotalEgresos` — Total Ingresos Vs Total Egresos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Payroll Biometrical Interface
**Package:** `com.sidesoft.hrm.payroll.biometrical`

# Module overview — Sidesoft Payroll Biometrical Interface

## Functional

La interfaz biométrica de nómina de Sidesoft tiene como propósito conectar la gestión de asistencia y tiempos de los empleados con el módulo de nómina del ERP Openbravo. Este módulo es utilizado principalmente por el departamento de Recursos Humanos y contabilidad para gestionar eficazmente las horas trabajadas y calcular la nómina correspondiente. Los actores involucrados son los administradores de RRHH, supervisores de área y contadores que son responsables de la supervisión y ejecución de nóminas. Dependencias clave incluyen la compatibilidad con la skin 2.50 a 3.00 y el módulo de gestión de recursos humanos y nómina, asegurando una integración fluida entre estas funcionalidades.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/hrm/payroll/biometrical` |
| Web | `web/com.sidesoft.hrm.payroll.biometrical/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPRBI`

# Guía de chat — Sidesoft Payroll Biometrical Interface

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.hrm.payroll.biometrical`).

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
- «¿Qué es la tabla sprbi_department_area?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo ingreso las marcaciones biométricas de un empleado?
- ¿Qué sucede si quiero borrar una entrada ya procesada?
- ¿Qué validaciones se aplican al procesar las horas de trabajo?
- ¿Cómo se gestionan las novedades en los horarios de los empleados?
- ¿Es posible ver el historial de marcaciones de un empleado?
- ¿Cómo se corrigen errores en las horas registradas?
- ¿Qué debo hacer si un empleado no aparece en la lista de marcaciones?
- ¿Qué significan los diferentes campos en la ventana de Mantenimiento Novedades?

# Domain — data model

## Functional

El modelo de datos del módulo incluye varias entidades clave, destacando principalmente la tabla 'sprbi_department_area' como la entidad cabecera que estructura la relación entre áreas y los empleados biométricos. Las etapas relevantes del proceso comprenden la manutención de novedades y la gestión de marcaciones biométricas, las cuales permiten al usuario ingresar y modificar datos sobre horas de entrada y salida. Un trigger importante es 'SPRBI_VALIDATEDELETE_TRG', que previene la eliminación de registros en estado procesado, asegurando la integridad de los datos históricos referentes a la asistencia de los empleados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sprbi_area` |
| `sprbi_biometric` |
| `sprbi_days` |
| `sprbi_department_area` |
| `sprbi_maintenance_news` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sprbi_area` | SPRBI_Area | — | `SPRBI_AREA_VALUE` (ad_client_id, identify) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sprbi_area_key`; Cols: identify, name, observation; `SPRBI_AREA_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sprbi_biometric` | sprbi_biometric | `SPRBI_VALIDATEDELETE_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SPRBI_VALIDATEDELETE_TRG. | PK `sprbi_biometric_key`; Cols: datemovement, entryhour_m, exithour_m, entryhour_a, exithour_a; `SPRBI_BIOMETRIC_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sprbi_days` | sprbi_days | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_shift_id→sspr_shift | Detalle enlazado a ad_client, ad_org, sspr_shift. | PK `sprbi_days_key`; Cols: line, day, name, description, sspr_shift_id; `SPRBI_DAYS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sprbi_department_area` | SPRBI_Department_Area | — | — | ad_client_id→ad_client; sprbi_area_id→sprbi_area; sshr_department_id→sshr_department; ad_org_id→ad_org | Detalle enlazado a ad_client, sprbi_area, sshr_department. | PK `sprbi_department_area_key`; Cols: line, sprbi_area_id, boss, sshr_department_id; `SPRBI_DEP_AREA_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sprbi_maintenance_news` | SPRBI_Maintenance_News | — | `SPRBI_MAIN_NEW_SEARCH_KEY` (ad_client_id, search_key) | ad_client_id→ad_client; sspr_concept_id→sspr_concept; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sspr_concept. | PK `sprbi_maintenance_news_key`; Cols: description, search_key, sspr_concept_id, valid, formula; `SPRBI_MAIN_NEW_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SPRBI_Area` |
| `sprbi_biometric` |
| `sprbi_days` |
| `SPRBI_Department_Area` |
| `SPRBI_Maintenance_News` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_BPARTNER`, `SSPR_CONTRACT`, `SSPR_SHIFT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo presenta una interfaz de usuario a través de tres ventanas principales: 'Mantenimiento Novedades', 'Marcaciones Biometrico' y 'Áreas', que permiten navegar y gestionar la información relativa a las asistencias de los empleados. Los usuarios pueden acceder a estas ventanas desde el menú principal del ERP, facilitando la administración de horarios y áreas de trabajo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.hrm.payroll.biometrical.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Mantenimiento Novedades | Maintenance news |
| Marcaciones Biometrico | Biometric Marking |
| Áreas | Areas |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración | Setup | Sí |
| Mantenimiento Novedades | Maintenance news | No |
| Marcaciones Biometrico | Biometric Marking | No |
| Procesar Marcaciones Biometrico | Process Marking Biometric | No |
| Transacciones | Transactions | Sí |
| Áreas | Areas | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.hrm.payroll.biometrical.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Mantenimiento Novedades

- **AD_WINDOW_ID:** `3DB88A55A0634673BAC9339C16F54C99`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Maintenance news | `3418AAF0A8D943FD8BBA0CDB3A67E513` | 0 |

### Ventana: Marcaciones Biometrico

- **AD_WINDOW_ID:** `C5AC4DFC86B348F08683C078352E554B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Biometric Marking | `9B7C800EBA454785BF65E1B9B00234DA` | 0 |

### Ventana: Áreas

- **AD_WINDOW_ID:** `11374175AC1549EE9C0C82970E57A787`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Areas | `DAAF7854214346F78A4E5BE7BBC3D7E1` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `021070CA34AE41C69879B5B047E5F0C8`

- **AD_TAB_ID:** `021070CA34AE41C69879B5B047E5F0C8` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 165 | Biometric Control | `EM_Sprbi_Biometric_Control` | No | No | — |

### Areas (ventana: Áreas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Identify | `Identify` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Observation | `Observation` | No | No | — |

### Biometric Marking (ventana: Marcaciones Biometrico)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | Sí | — |
| 30 | Identify | `Identify` | No | Sí | — |
| 50 | Movement Date | `Datemovement` | No | Sí | — |
| 60 | Employee | `C_Bpartner_ID` | No | Sí | — |
| 70 | Entry  dial 1 | `Entryhour_M` | No | Sí | — |
| 110 | State | `State` | No | Sí | — |

### Area

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Line No. | `Line` | No | No | — |
| 30 | Area | `Sprbi_Area_ID` | No | No | — |
| 40 | Boss | `Boss` | No | No | — |

### Pestaña `8E36BD6FE29C43A986293F91A45DA786`

- **AD_TAB_ID:** `8E36BD6FE29C43A986293F91A45DA786` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 110 | EM_Sprbi_Configuration_Lines | `EM_Sprbi_Configuration_Lines` | No | No | — |
| 111 | Feeding parameter | `EM_Sprbi_Feed_Param` | No | No | — |
| 112 | Feeding value | `EM_Sprbi_Feed_Value` | No | No | — |
| 113 | Maximum Hours a Day | `EM_Sprbi_Hours_Max_Day` | No | No | — |
| 114 | Maximum Hours a Week | `EM_Sprbi_Hours_Max_Week` | No | No | — |
| 115 | Maximum Hours per Month | `EM_Sprbi_Hours_Max_Month` | No | No | — |
| 116 | Minimum Hours Worked | `EM_Sprbi_Hours_Min_Worked` | No | No | — |
| 200 | Entry from | `EM_Sprbi_Entry_From` | No | No | FDA8D3A3AB2F4F5F82D51668B8707C65 |
| 210 | Entry until | `EM_Sprbi_Entry_Until` | No | No | FDA8D3A3AB2F4F5F82D51668B8707C65 |
| 220 | Minute delay parameter | `EM_Sprbi_Minute_Delay_Param` | No | No | FDA8D3A3AB2F4F5F82D51668B8707C65 |
| 300 | Exit from | `EM_Sprbi_Exit_From` | No | No | 465F3B0B20B14EB7BBF15432D9C223B8 |
| 310 | Exit Util | `EM_Sprbi_Exit_Until` | No | No | 465F3B0B20B14EB7BBF15432D9C223B8 |
| 320 | Overtime parameter | `EM_Sprbi_Overtime_Param` | No | No | 465F3B0B20B14EB7BBF15432D9C223B8 |

### Days

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Line No. | `Line` | No | No | — |
| 40 | Day | `Day` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Starttime | `Starttime` | No | No | FDA8D3A3AB2F4F5F82D51668B8707C65 |
| 80 | Entry | `Entry` | No | No | FDA8D3A3AB2F4F5F82D51668B8707C65 |
| 90 | Entry_From | `Entry_From` | No | No | FDA8D3A3AB2F4F5F82D51668B8707C65 |
| 100 | Entry_Until | `Entry_Until` | No | No | FDA8D3A3AB2F4F5F82D51668B8707C65 |
| 110 | Minute_Delay_Param | `Minute_Delay_Param` | No | No | FDA8D3A3AB2F4F5F82D51668B8707C65 |
| 120 | Endtime | `Endtime` | No | No | 465F3B0B20B14EB7BBF15432D9C223B8 |
| 130 | Exit | `Exit` | No | No | 465F3B0B20B14EB7BBF15432D9C223B8 |
| 140 | Exit_From | `Exit_From` | No | No | 465F3B0B20B14EB7BBF15432D9C223B8 |
| 150 | Exit_Until | `Exit_Until` | No | No | 465F3B0B20B14EB7BBF15432D9C223B8 |
| 160 | Overtime_Param | `Overtime_Param` | No | No | 465F3B0B20B14EB7BBF15432D9C223B8 |

### Pestaña `AE4D0B14798E47A5B0CEF62C52DB235B`

- **AD_TAB_ID:** `AE4D0B14798E47A5B0CEF62C52DB235B` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 203 | Area | `EM_Sprbi_Area_ID` | No | No | — |

### Maintenance news (ventana: Mantenimiento Novedades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Search Key | `Search_Key` | No | No | — |
| 30 | Description | `Description` | No | No | — |
| 40 | Concept | `Sspr_Concept_ID` | No | No | — |
| 50 | Value | `Value` | No | No | — |
| 60 | Valid | `Valid` | No | No | — |
| 70 | Formula | `Formula` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso típico dentro del módulo incluye la opción de activar el botón de procesamiento, el cual corresponde a la recopilación y validación de marcaciones de los empleados. Es común realizar validaciones que aseguren que los datos ingresados se ajustan a los criterios establecidos, como la hora de entrada y salida. Como no se especifican informes en el inventario, se infiere que el enfoque está más en el manejo de entradas y validaciones en tiempo real, en lugar de la generación de informes estadísticos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.hrm.payroll.biometrical.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Procesar Marcaciones Biometrico | Process Marking Biometric | sprbi_process_biometric | `sprbi_process_biometric` | Si existe valor en la entrada y salida procesada; Si la entrada procesada es mayor a la entrada del turno; Si la salida procesada es mayor a la del turno; Si la salida procesada es menor a la del turno | — |
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
| Botón (PL/pgSQL) | Procesar Marcaciones Biometrico | Process Marking Biometric | sprbi_process_biometric | `sprbi_process_biometric` | Si existe valor en la entrada y salida procesada; Si la entrada procesada es mayor a la entrada del turno; Si la salida procesada es mayor a la del turno; Si la salida procesada es menor a la del turno | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Procesar Marcaciones Biometrico | Process Marking Biometric | PL `sprbi_process_biometric` | Si existe valor en la entrada y salida procesada; Si la entrada procesada es mayor a la entrada del turno; Si la salida procesada es mayor a la del turno; Si la salida procesada es menor a la del turno | Si existe valor en la entrada y salida procesada; Si la entrada procesada es mayor a la entrada del turno; Si la salida procesada es mayor a la del turno; Si la salida procesada es menor a la del turno |
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
| `sprbi_config_required` | Entry and Exit information is required. | Entry and Exit information is required. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sprbi_config_line` | Config valid only in lines | Config valid only in lines | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sprbi_existing_config_line` | Existing line configuration | Existing line configuration | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPRBI_DateFormatInvalid` | Invalid date format | Invalid date format | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPRBI_EmployeeNotExits` | Employee not found indicator | Employee not found indicator | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sprbi_config_head` | Config valid only in headboard. | Config valid only in headboard. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPRBI_NoShift` | No shift configured | No shift configured | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPRBI_MarkingExits` | Duplicate dialing | Duplicate dialing | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

Dentro del módulo, se utilizan varias clases Java para realizar cálculos y validaciones durante el ingreso de datos biométricos. Por ejemplo, la clase 'SprbiEmployee' implementa funcionalidades específicas para obtener y validar datos relacionados con el empleado, asegurando así que la experiencia del usuario y la lógica de negocios sean consistentes y eficaces.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.hrm.payroll.biometrical`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SprbiEmployee` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/hrm/payroll/biometrical/ad_callouts/SprbiEmployee.java` |
| `SprbiEntryProcessed` | ad_callouts | SimpleCallout | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/biometrical/ad_callouts/SprbiEntryProcessed.java` |
| `SprbiExitProcessed` | ad_callouts | SimpleCallout | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/biometrical/ad_callouts/SprbiExitProcessed.java` |
| `ImportBiometic` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/biometrical/ad_process/ImportBiometic.java` |
| `ImportBiometricMarking` | ad_process | IdlServiceJava | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/biometrical/ad_process/ImportBiometricMarking.java` |
| `SprbiDaysEventListener` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/biometrical/event/SprbiDaysEventListener.java` |
| `SprbiShiftEventListener` | event | EntityPersistenceEventObserver | Event handler | `src/com/sidesoft/hrm/payroll/biometrical/event/SprbiShiftEventListener.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SPRBI_VALIDATEDELETE_TRG` | `sprbi_biometric` | before INSERT/UPDATE/DELETE | No es posible eliminar un registro en estado procesado |
| AD_VAL_RULE | — | `sprbi_area` | `Sprbi_Area.Sprbi_Area_Id  in (
select AU.Sprbi_Area_id from Sprbi_Area AU
	inner join Sprbi_Department_Area AD on AD.Spr` |
| AD_VAL_RULE | — | `sprbi_filter_employee` | `C_BPARTNER.ISEMPLOYEE = 'Y'  and C_BPARTNER.isactive= 'Y'` |
| Java event/validator | `SprbiDaysEventListener` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/biometrical/event/SprbiDaysEventListener.java`)* |
| Java event/validator | `SprbiShiftEventListener` | persistencia/UI | *(leer `src/com/sidesoft/hrm/payroll/biometrical/event/SprbiShiftEventListener.java`)* |
| Función PL `sprbi_absences` | — | invocación proceso | Sino tiene marcacion el dia anterior pero tiene marcaciones anteriores a la fecha, validamos el porque; SELECT sprbi_absences(v_lastday::DATE, v_employee) INTO v_result; |
| Función PL `sprbi_nhour_100` | — | invocación proceso | Si las horas extras son mayores a las autorizadas; Si existen horas 100, no pagar alimentacion ni calcular atraso |
| Función PL `sprbi_nhour_50` | — | invocación proceso | Si el dia esta entre lunes y viernes, lo tiene configurado, no es feriado y no tiene el check de horas extras; Si las horas extras son mayores a las autorizadas; Si el acumulado supera al maximo permitido en la semana |
| Función PL `sprbi_overtime` | — | invocación proceso | Si la marcacion tiene el check de validado |
| Función PL `sprbi_process_biometric` | — | invocación proceso | Si existe valor en la entrada y salida procesada; Si la entrada procesada es mayor a la entrada del turno; Si la salida procesada es mayor a la del turno |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Las funciones PL (Procedures Language) y triggers en la base de datos desempeñan un papel crucial en el soporte del módulo. Las funciones garantizan que las operaciones de entrada y salida estén sincronizadas con las reglas de negocio, mientras que los triggers como 'SPRBI_VALIDATEDELETE_TRG' ayudan a mantener la integridad de los datos, protegiendo contra eliminaciones indebidas de registros procesados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SPRBI_VALIDATEDELETE_TRG` | `sprbi_biometric` | before | INSERT/UPDATE/DELETE | No es posible eliminar un registro en estado procesado | `model/triggers/SPRBI_VALIDATEDELETE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sprbi_absences` | — | Sino tiene marcacion el dia anterior pero tiene marcaciones anteriores a la fecha, validamos el porque; SELECT sprbi_absences(v_lastday::DATE, v_employee) INTO v_result; | Sino tiene marcacion el dia anterior pero tiene marcaciones anteriores a la fecha, validamos el porque; SELECT sprbi_absences(v_lastday::DATE, v_employee) INTO v_result; | `model/functions/SPRBI_ABSENCES.xml` |
| `sprbi_nhour_100` | — | Si las horas extras son mayores a las autorizadas; Si existen horas 100, no pagar alimentacion ni calcular atraso | Si las horas extras son mayores a las autorizadas; Si existen horas 100, no pagar alimentacion ni calcular atraso | `model/functions/SPRBI_NHOUR_100.xml` |
| `sprbi_nhour_50` | — | Si el dia esta entre lunes y viernes, lo tiene configurado, no es feriado y no tiene el check de horas extras; Si las horas extras son mayores a las autorizadas; Si el acumulado supera al maximo permitido en la semana;… | Si el dia esta entre lunes y viernes, lo tiene configurado, no es feriado y no tiene el check de horas extras; Si las horas extras son mayores a las autorizadas; Si el acumulado supera al maximo permitido en la semana; Si el acumulado supera al maximo permitido al mes | `model/functions/SPRBI_NHOUR_50.xml` |
| `sprbi_overtime` | — | Si la marcacion tiene el check de validado | Si la marcacion tiene el check de validado | `model/functions/SPRBI_OVERTIME.xml` |
| `sprbi_process_biometric` | Procesar Marcaciones Biometrico | Si existe valor en la entrada y salida procesada; Si la entrada procesada es mayor a la entrada del turno; Si la salida procesada es mayor a la del turno; Si la salida procesada es menor a la del turno | Si existe valor en la entrada y salida procesada; Si la entrada procesada es mayor a la entrada del turno; Si la salida procesada es mayor a la del turno; Si la salida procesada es menor a la del turno | `model/functions/SPRBI_PROCESS_BIOMETRIC.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Procesar Marcaciones Biometrico | `sprbi_process_biometric` | Botón (PL/pgSQL) | PL `sprbi_process_biometric` | N | Si existe valor en la entrada y salida procesada; Si la entrada procesada es mayor a la entrada del turno; Si la salida procesada es mayor a la del turno; Si la salida procesada es |

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

Módulo: `com.sidesoft.hrm.payroll.biometrical`.

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

# Glosario — prefijo `SPRBI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPRBI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.hrm.payroll.biometrical` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `sprbi_process_biometric` — Procesar Marcaciones Biometrico

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Payroll Accounting Distributed by Cost Center
**Package:** `com.sidesoft.hrm.payroll.disaccounting`

# Module overview — Payroll Accounting Distributed by Cost Center

## Functional

El módulo 'Payroll Accounting Distributed by Cost Center' permite gestionar la contabilidad de nómina distribuida por centros de costo, facilitando a las empresas asignar correctamente los costos de la nómina a diferentes departamentos o proyectos. Esto es esencial para un análisis financiero detallado y la optimización de recursos. Los actores principales de este módulo son los responsables de la gestión de nómina y contabilidad. El alcance del módulo incluye la distribución de cuentas y la generación de informes financieros básicos en el ámbito de nómina, sin depender de otros módulos de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/hrm/payroll/disaccounting` |
| Web | `web/com.sidesoft.hrm.payroll.disaccounting/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPD`

# Guía de chat — Payroll Accounting Distributed by Cost Center

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.hrm.payroll.disaccounting`).

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
- «¿Qué es la tabla sspd_pctdist_costcenter?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo asignar un centro de costo a un empleado?
- ¿Qué pasos debo seguir para realizar la distribución de nómina?
- ¿Puedo modificar la asignación de costos una vez que se ha completado?
- ¿Cómo se validan los datos introducidos en el módulo?
- ¿Existen informes disponibles para analizar la distribución de costos?
- ¿Qué debo hacer si encuentro un error en la distribución?
- ¿Cómo se gestionan los cambios en los centros de costo?
- ¿Qué funciones PL están disponibles para este módulo?

# Domain — data model

## Functional

La entidad cabecera principal es 'sspd_pctdist_costcenter', que actúa como ancla para la contabilidad de nómina. Desde esta tabla, se gestionan diversas etapas de distribución que permiten a los usuarios asignar y gestionar costos específicos por centro de costo. Las relaciones dentro del modelo de datos son claras, ya que permiten una fácil referencia y vinculación entre los diferentes centros de costo y los empleados que los representan. Aunque no hay triggers definidos para este módulo, se utilizan funciones PL para la validación y gestión de procesos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sspd_pctdist` |
| `sspd_pctdist_costcenter` |
| `sspd_pctdist_emp` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sspd_pctdist` | sspd_pctdist | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_period_id→c_period | Detalle enlazado a ad_client, ad_org, c_period. | PK `sspd_pctdist_key`; Cols: c_period_id, description, processed; `SSPD_PCTDIST_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspd_pctdist_costcenter` | sspd_pctdist_costcenter | — | — | c_costcenter_id→c_costcenter; ad_client_id→ad_client; ad_org_id→ad_org; sspd_pctdist_emp_id→sspd_pctdist_emp; user1_id→user1 | Detalle enlazado a ad_client, ad_org, c_costcenter. | PK `sspd_pd_costcenter_key`; Cols: sspd_pctdist_emp_id, c_costcenter_id, percentage, user1_id; `SSPD_PD_COSTCENTER_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspd_pctdist_emp` | sspd_pctdist_emp | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sspd_pctdist_id→sspd_pctdist | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sspd_pctdist_emp_key`; Cols: sspd_pctdist_id, c_bpartner_id, description, percentagetotal; `SSPD_PCTDIST_EMP_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sspd_pctdist` |
| `sspd_pctdist_costcenter` |
| `sspd_pctdist_emp` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de la ventana 'Distribución de Centros de Costo por Empleado', donde los usuarios pueden acceder fácilmente a las distintas tabulaciones y campos necesarios para la gestión. La interfaz es intuitiva, permitiendo una rápida visualización y edición de datos relacionados con la contabilidad de nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.hrm.payroll.disaccounting.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Distribución de Centros de Costo por Empleado | Cost Center by Employee and Period |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Contabilidad | Accounting | Sí |
| Copiar Distribución por Centro de Costo | Copy Distribution Cost Center | No |
| Diario Contable de Nómina | Payroll Accounting Journal | No |
| Distribución de Centros de Costo por Empleado | Cost Center by Employee and Period | No |
| Validación de Datos | Data Validation | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.hrm.payroll.disaccounting.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Distribución de Centros de Costo por Empleado

- **AD_WINDOW_ID:** `3E6975CE3BFA4A86AB9640DF18AB1EB9`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Peiod | `873CCEBD9BF84EF29B35F0F827925A5A` | 0 |
| 20 | Employee | `5BFADD5E477C486FAEA3CA6764E7CC79` | 1 |
| 30 | Percentages by Employee | `FC547AD22E75400AA2EB69220C981963` | 2 |

## Campos añadidos por el módulo (AD_FIELD)

### Percentages by Employee (ventana: Distribución de Centros de Costo por Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Business Unit | `C_Costcenter_ID` | No | No | — |
| 50 | Product | `User1_ID` | No | No | — |
| 60 | Porcentage | `Percentage` | No | No | — |

### Employee (ventana: Distribución de Centros de Costo por Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Peiod (ventana: Distribución de Centros de Costo por Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Period | `C_Period_ID` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Process Distribution Percentages | `Processed` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dentro del módulo, se encuentran botones típicos que facilitan la gestión de procesos, como 'Completar', 'Retornar' y 'Rechazar'. Aunque no se disponen de informes predefinidos, las funciones PL vinculadas a los botones apoyan la ejecución de validaciones frecuentes y aseguran la integridad de los datos al momento de realizar la distribución de costos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.hrm.payroll.disaccounting.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Copiar Distribución por Centro de Costo | Copy Distribution Cost Center | Copy Distribution Cost Center | `sspd_copy_dist_costcenter` | ELSIF (Cur_Parameter.ParameterName = 'SSPR_Concept_ID') THEN; v_SSconcept_ID := Cur_Parameter.P_String; | — |
| Botón (PL/pgSQL) | Process Distribution Percentages | Process Distribution Percentages | sspd_process_pctdist | `sspd_process_pctdist` | Valor incorrecto, El valor de las líneas deben sumar 100% Empleado: | — |
| Proceso / otro | Diario Contable de Nómina | Payroll Accounting Journal | Payroll Accounting Journal | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Validación de Datos | Data Validation | Data Validation | *(OBUIAPP / manual)* | — | — |
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
| Botón (PL/pgSQL) | Copiar Distribución por Centro de Costo | Copy Distribution Cost Center | Copy Distribution Cost Center | `sspd_copy_dist_costcenter` | ELSIF (Cur_Parameter.ParameterName = 'SSPR_Concept_ID') THEN; v_SSconcept_ID := Cur_Parameter.P_String; | — |
| Botón (PL/pgSQL) | Process Distribution Percentages | Process Distribution Percentages | sspd_process_pctdist | `sspd_process_pctdist` | Valor incorrecto, El valor de las líneas deben sumar 100% Empleado: | — |
| Proceso / otro | Diario Contable de Nómina | Payroll Accounting Journal | Payroll Accounting Journal | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Validación de Datos | Data Validation | Data Validation | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Copiar Distribución por Centro de Costo | Copy Distribution Cost Center | PL `sspd_copy_dist_costcenter` | ELSIF (Cur_Parameter.ParameterName = 'SSPR_Concept_ID') THEN; v_SSconcept_ID := Cur_Parameter.P_String; | ELSIF (Cur_Parameter.ParameterName = 'SSPR_Concept_ID') THEN; v_SSconcept_ID := Cur_Parameter.P_String; |
| Botón (PL/pgSQL) | Process Distribution Percentages | Process Distribution Percentages | PL `sspd_process_pctdist` | Valor incorrecto, El valor de las líneas deben sumar 100% Empleado: | Valor incorrecto, El valor de las líneas deben sumar 100% Empleado: |
| Proceso / otro | Diario Contable de Nómina | Payroll Accounting Journal | — | — | — |
| Proceso / otro | Validación de Datos | Data Validation | — | — | — |
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

No se requiere Java para el funcionamiento de este módulo, ya que no hay clases de Java integradas en su diseño.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.hrm.payroll.disaccounting`.

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
| AD_VAL_RULE | — | `Period Payroll Accounting Distributed` | `C_Period.openclose = 'C'` |
| AD_VAL_RULE | — | `FIlter Employee Payroll Accounting Distributed` | `C_BPARTNER.ISEMPLOYEE = 'Y' and C_BPARTNER.em_sspr_status = 'A'` |
| Función PL `sspd_copy_dist_costcenter` | — | invocación proceso | ELSIF (Cur_Parameter.ParameterName = 'SSPR_Concept_ID') THEN; v_SSconcept_ID := Cur_Parameter.P_String; |
| Función PL `sspd_process_pctdist` | — | invocación proceso | Valor incorrecto, El valor de las líneas deben sumar 100% Empleado: |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers no son utilizados en este módulo; sin embargo, las funciones PL juegan un papel importante al permitir la ejecución de procesos específicos necesarios para la correcta contabilización de la nómina distribuida. Estas funciones son esenciales para la validación de datos y la integración de cálculos necesarios para cumplir con los requerimientos contables.

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
| `sspd_copy_dist_costcenter` | Copiar Distribución por Centro de Costo | ELSIF (Cur_Parameter.ParameterName = 'SSPR_Concept_ID') THEN; v_SSconcept_ID := Cur_Parameter.P_String; | ELSIF (Cur_Parameter.ParameterName = 'SSPR_Concept_ID') THEN; v_SSconcept_ID := Cur_Parameter.P_String; | `model/functions/SSPD_COPY_DIST_COSTCENTER.xml` |
| `sspd_process_pctdist` | Process Distribution Percentages | Valor incorrecto, El valor de las líneas deben sumar 100% Empleado: | Valor incorrecto, El valor de las líneas deben sumar 100% Empleado: | `model/functions/SSPD_PROCESS_PCTDIST.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Copiar Distribución por Centro de Costo | `Copy Distribution Cost Center` | Botón (PL/pgSQL) | PL `sspd_copy_dist_costcenter` | N | ELSIF (Cur_Parameter.ParameterName = 'SSPR_Concept_ID') THEN; v_SSconcept_ID := Cur_Parameter.P_String; |
| 2 | Process Distribution Percentages | `sspd_process_pctdist` | Botón (PL/pgSQL) | PL `sspd_process_pctdist` | N | Valor incorrecto, El valor de las líneas deben sumar 100% Empleado: |

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

Módulo: `com.sidesoft.hrm.payroll.disaccounting`.

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

# Glosario — prefijo `SSPD`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPD` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.hrm.payroll.disaccounting` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Copy Distribution Cost Center` — Copiar Distribución por Centro de Costo
- `sspd_process_pctdist` — Process Distribution Percentages
- `Payroll Accounting Journal` — Diario Contable de Nómina
- `Data Validation` — Validación de Datos

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Payroll Anticipated Payments
**Package:** `com.sidesoft.hrm.payroll.early.payment`

# Module overview — Payroll Anticipated Payments

## Functional

El módulo de Pagos Anticipados de Nómina (Payroll Anticipated Payments) tiene como propósito facilitar la gestión de pagos anticipados de salarios a los empleados. Está diseñado para ser utilizado por profesionales de recursos humanos y administradores de nómina que buscan optimizar el proceso de pagos. El alcance incluye la generación de archivos necesarios para la transferencia de fondos a bancos, y se integra con otros módulos de Openbravo, como el de gestión de recursos humanos y nómina. Las dependencias del módulo son la skin de compatibilidad y el módulo de gestión de nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/hrm/payroll/early/payment` |
| Web | `web/com.sidesoft.hrm.payroll.early.payment/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPEP`

# Guía de chat — Payroll Anticipated Payments

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.hrm.payroll.early.payment`).

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
- «¿Qué es la tabla spep_advance_payment?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo solicitar un pago anticipado para un empleado?
- ¿Qué parámetros debo configurar para los pagos anticipados?
- ¿Cómo genero el archivo de pagos anticipados para el banco Pichincha?
- ¿Qué sucede si un pago anticipado es rechazado?
- ¿Cómo verifico el estado de un pago anticipado solicitado?
- ¿Cómo puedo modificar un pago anticipado existente?
- ¿Cuál es el proceso para devolver un pago anticipado?
- ¿Cómo se actualizan los montos de los pagos anticipados en el sistema?

# Domain — data model

## Functional

La entidad cabecera del modelo de datos es la tabla 'spep_advance_payment', que almacena la información de cada solicitud de pago anticipado. Las relaciones se mantienen con tablas como 'C_BPARTNER' y 'SSPR_CONCEPT_AMOUNT', permitiendo vincular información de socios comerciales y montos específicos relacionados con los pagos. Aunque no se han definido triggers en el módulo, cuenta con una función PL que facilita la ejecución de procesos vinculados a los pagos anticipados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `spep_advance_payment` |
| `spep_advance_payment_cfg` |
| `spep_advance_paymentdetail` |
| `spep_advance_paymentline` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `spep_advance_payment` | SPEP_Advance_Payment | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype; c_period_id→c_period | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `spep_advpaym_key`; Cols: documentno, c_period_id, c_doctype_id, observation, docstatus; `SPEP_ADVPAYM_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `spep_advance_payment_cfg` | SPEP_Advance_Payment_Cfg | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_concept_in_id→sspr_concept; sspr_concept_out_id→sspr_concept | Detalle enlazado a ad_client, ad_org, sspr_concept. | PK `spep_advpaymcfg_key`; Cols: seqno, sspr_concept_in_id, sspr_concept_out_id, observation, configuration_type; `SPEP_ADVPAYMCFG_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SPEP_PE_ISACTIVE_CHECK`: PERCENTAGE_EMPLOYED IN ('Y', 'N') |
| `spep_advance_paymentdetail` | SPEP_Advance_PaymentDetail | — | — | ad_client_id→ad_client; ad_org_id→ad_org; spep_advance_paymentline_id→spep_advance_paymentline; sspr_concept_id→sspr_concept | Detalle enlazado a ad_client, ad_org, spep_advance_paymentline. | PK `spep_advpaymdet_key`; Cols: line, sspr_concept_id, amount, spep_advance_paymentline_id, description; `SPEP_ADVPAYMDET_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `spep_advance_paymentline` | SPEP_Advance_PaymentLine | — | — | ad_client_id→ad_client; ad_org_id→ad_org; spep_advance_payment_id→spep_advance_payment; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, ad_org, spep_advance_payment. | PK `spep_advpaymline_key`; Cols: line, c_bpartner_id, typeofincome, amount, spep_advance_payment_id; `SPEP_ADVPAYMLINE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SPEP_Advance_Payment` |
| `SPEP_Advance_Payment_Cfg` |
| `SPEP_Advance_PaymentDetail` |
| `SPEP_Advance_PaymentLine` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_BPARTNER`, `SSPR_CONCEPT_AMOUNT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo cuenta con dos ventanas principales: 'Pago anticipado' y 'Parámetros de Pagos Anticipados'. En la interfaz de usuario, los usuarios pueden navegar fácilmente entre estas ventanas para realizar las gestiones adecuadas, donde pueden introducir datos, configurar parámetros y generar archivos necesarios para los bancos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.hrm.payroll.early.payment.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Pago anticipado | Advance Payment |
| Parámetros de Pagos Anticipados | Advance Payments Setup |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Archivo de pago anticipado de nomina Rumiñauhi | Archive Payroll Advance Payment Rumiñauhi | No |
| Archivo de Pago Quincena Produbanco TXT | Payment File Fortnight Produbanco TXT | No |
| Archivo Pago Quincena Pichincha TXT | Payment File Fortnight Pichincha TXT | No |
| Herramientas de Análisis | Analysis tools | Sí |
| Pago anticipado | Advance Payment | No |
| Pago anticipado de nómina | Payroll Advance Payment | Sí |
| Pago anticipado de nómina totalizado | Payroll Advance Payment Totalized | No |
| Parámetros de Pagos Anticipados | Advance Payments Setup | No |
| Reporte de Pago Anticipado Individual | Individual Advance Payment Report | No |
| Reporte Pago de Quincena Banco del Pacifico | Report Fortnight Pacific Bank | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.hrm.payroll.early.payment.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Pago anticipado

- **AD_WINDOW_ID:** `2051044732DC473D8D9802953120CD54`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Advance Payment | `AEB50F249694406AA64F370CC01D86B9` | 0 |
| 20 | Lines | `635B3984E0EE488F9DDCAD344AC3B11E` | 1 |
| 30 | Detail | `E8D75CE4344E4F5D808569D67387D869` | 2 |

### Ventana: Parámetros de Pagos Anticipados

- **AD_WINDOW_ID:** `9B92579B16564AF3B6A34FEAF735E0DE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Advance Payments Setup | `CF770C543E5E40388771F2F7DA5EA682` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Advance Payments Setup (ventana: Parámetros de Pagos Anticipados)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Sequence Number | `Seqno` | No | No | — |
| 40 | Concept In | `Sspr_Concept_In_ID` | No | No | — |
| 50 | Concept Out | `Sspr_Concept_Out_ID` | No | No | — |
| 52 | Configuration Type | `Configuration_Type` | No | No | — |
| 55 | Percentage | `Percentage` | No | No | — |
| 60 | Comments | `Observation` | No | No | — |
| 70 | % Employed | `Percentage_Employed` | No | No | — |

### Detail (ventana: Pago anticipado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | Sí | — |
| 30 | Line No. | `Line` | No | Sí | — |
| 40 | Business Concept | `Sspr_Concept_ID` | No | Sí | — |
| 50 | Amount | `Amount` | No | Sí | — |
| 55 | Observations | `Description` | No | No | — |

### Pestaña `AE4D0B14798E47A5B0CEF62C52DB235B`

- **AD_TAB_ID:** `AE4D0B14798E47A5B0CEF62C52DB235B` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 350 | Payroll Advance Payment | `EM_Spep_PayrollAdvPaym` | No | No | — |
| 422 | EM_Spep_Work_Concept | `EM_Spep_Work_Concept` | No | No | 3CA89475EB9342BCAF79B7DD29F20EB1 |

### Advance Payment (ventana: Pago anticipado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document No. | `Documentno` | No | No | — |
| 40 | Period | `C_Period_ID` | No | No | — |
| 50 | Document Type | `C_Doctype_ID` | No | No | — |
| 60 | Comments | `Observation` | No | No | — |
| 90 | Process Payroll Anticipated Payment | `Processed` | No | No | — |

### Lines (ventana: Pago anticipado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Line No. | `Line` | No | No | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | Type Of Income | `Typeofincome` | No | No | — |
| 60 | Amount | `Amount` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye siete botones de proceso que permiten a los usuarios completar acciones como generar los archivos necesarios para realizar transferencias a diferentes bancos (Pichincha, Rumiñahui, etc.). Los usuarios pueden completar pagos anticipados, retornar solicitudes o rechazar requisitos. Las validaciones frecuentes incluyen asegurar que los montos sean correctos y que los registros estén completos antes de generar y enviar archivos a los bancos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.hrm.payroll.early.payment.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archivo Pago Quincena Pichincha TXT | Archive Payment fortnight Pichincha TXT | Archive Payment fortnight Pichincha TXT | Java `ArchPaymentFortnightPichinchaBankTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/early/payment/create_txt/ArchPaymentFortnightPichinchaBankTXT.java` |
| Botón (PL/pgSQL) | Procesar pago anticipado de nómina | Process Payroll Anticipated Payment | SPEP_ProcessProcessPayrollAnticipated | `SPEP_AdvPaym_Process` | Get payroll advance payment processed status; UPDATE or DELETE the line acording with amount value | — |
| Informe (servlet) | Archivo de pago anticipado de nomina Rumiñauhi | Archive Payroll Advance Payment Rumiñauhi | Archive Payr Adv Paym Rumiñauhi | Java `ArchPayrAdvPayRuminahuiBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/early/payment/create_txt/ArchPayrAdvPayRuminahuiBankTXT.java` |
| Informe (servlet) | Archivo de Pago Quincena Produbanco TXT | Payment File Fortnight Produbanco TXT | Payment File Fortnight Produbanco TXT | Java `ArchivePaymentFortnightTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/early/payment/ad_process/ArchivePaymentFortnightTXT.java` |
| Proceso / otro | Pago anticipado de nómina totalizado | Payroll Advance Payment Totalized | Payroll Advance Payment Totalized | *(OBUIAPP / manual)* | Payroll Advance Payment Totalized | — |
| Proceso / otro | Reporte de Pago Anticipado Individual | Individual Advance Payment Report | Individual Advance Payment Report | *(OBUIAPP / manual)* | Individual Advance Payment Report | — |
| Proceso / otro | Reporte Pago de Quincena Banco del Pacifico | Report Fortnight Pacific Bank | Report Fortnight Pacific Bank | *(OBUIAPP / manual)* | Report Fortnight Pacific Bank | — |
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
| Botón (Java) | Archivo Pago Quincena Pichincha TXT | `ArchPaymentFortnightPichinchaBankTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/early/payment/create_txt/ArchPaymentFortnightPichinchaBankTXT.java` |
| Informe (servlet) | Archivo de pago anticipado de nomina Rumiñauhi | `ArchPayrAdvPayRuminahuiBankTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/early/payment/create_txt/ArchPayrAdvPayRuminahuiBankTXT.java` |
| Informe (servlet) | Archivo de Pago Quincena Produbanco TXT | `ArchivePaymentFortnightTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/early/payment/ad_process/ArchivePaymentFortnightTXT.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archivo Pago Quincena Pichincha TXT | Archive Payment fortnight Pichincha TXT | Archive Payment fortnight Pichincha TXT | Java `ArchPaymentFortnightPichinchaBankTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/early/payment/create_txt/ArchPaymentFortnightPichinchaBankTXT.java` |
| Botón (PL/pgSQL) | Procesar pago anticipado de nómina | Process Payroll Anticipated Payment | SPEP_ProcessProcessPayrollAnticipated | `SPEP_AdvPaym_Process` | Get payroll advance payment processed status; UPDATE or DELETE the line acording with amount value | — |
| Informe (servlet) | Archivo de pago anticipado de nomina Rumiñauhi | Archive Payroll Advance Payment Rumiñauhi | Archive Payr Adv Paym Rumiñauhi | Java `ArchPayrAdvPayRuminahuiBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/early/payment/create_txt/ArchPayrAdvPayRuminahuiBankTXT.java` |
| Informe (servlet) | Archivo de Pago Quincena Produbanco TXT | Payment File Fortnight Produbanco TXT | Payment File Fortnight Produbanco TXT | Java `ArchivePaymentFortnightTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/early/payment/ad_process/ArchivePaymentFortnightTXT.java` |
| Proceso / otro | Pago anticipado de nómina totalizado | Payroll Advance Payment Totalized | Payroll Advance Payment Totalized | *(OBUIAPP / manual)* | Payroll Advance Payment Totalized | — |
| Proceso / otro | Reporte de Pago Anticipado Individual | Individual Advance Payment Report | Individual Advance Payment Report | *(OBUIAPP / manual)* | Individual Advance Payment Report | — |
| Proceso / otro | Reporte Pago de Quincena Banco del Pacifico | Report Fortnight Pacific Bank | Report Fortnight Pacific Bank | *(OBUIAPP / manual)* | Report Fortnight Pacific Bank | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archivo Pago Quincena Pichincha TXT | Archive Payment fortnight Pichincha TXT | Java `ArchPaymentFortnightPichinchaBankTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Botón (PL/pgSQL) | Procesar pago anticipado de nómina | Process Payroll Anticipated Payment | PL `SPEP_AdvPaym_Process` | Get payroll advance payment processed status; UPDATE or DELETE the line acording with amount value | Get payroll advance payment processed status; UPDATE or DELETE the line acording with amount value |
| Informe (servlet) | Archivo de pago anticipado de nomina Rumiñauhi | Archive Payroll Advance Payment Rumiñauhi | Java `ArchPayrAdvPayRuminahuiBankTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Informe (servlet) | Archivo de Pago Quincena Produbanco TXT | Payment File Fortnight Produbanco TXT | Java `ArchivePaymentFortnightTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Proceso / otro | Pago anticipado de nómina totalizado | Payroll Advance Payment Totalized | — | Payroll Advance Payment Totalized | — |
| Proceso / otro | Reporte de Pago Anticipado Individual | Individual Advance Payment Report | — | Individual Advance Payment Report | — |
| Proceso / otro | Reporte Pago de Quincena Banco del Pacifico | Report Fortnight Pacific Bank | — | Report Fortnight Pacific Bank | — |
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
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo contiene tres clases Java que facilitan la creación y gestión de los archivos de texto necesarios para las transferencias bancarias. Estas clases son responsables de la lógica de proceso, creando archivos según los requerimientos de cada banco.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.hrm.payroll.early.payment`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ArchivePaymentFortnightTXT` | ad_process | DalBaseProcess | Proceso / informe Java | `src/com/sidesoft/hrm/payroll/early/payment/ad_process/ArchivePaymentFortnightTXT.java` |
| `ArchPaymentFortnightPichinchaBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/early/payment/create_txt/ArchPaymentFortnightPichinchaBankTXT.java` |
| `ArchPayrAdvPayRuminahuiBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/early/payment/create_txt/ArchPayrAdvPayRuminahuiBankTXT.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Spep_ValidUser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Payroll Anticipated Payment DocType` | `C_DocType.DocBaseType='SPEP_PAP'` |
| AD_VAL_RULE | — | `Spep_ValidPartner` | `C_BPARTNER.ISEMPLOYEE = 'Y'` |
| Función PL `spep_advpaym_process` | — | invocación proceso | Get payroll advance payment processed status; UPDATE or DELETE the line acording with amount value |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers no están activos en este módulo, pero la función PL vinculada desempeña un papel crucial para la lógica de negocio relacionada con la generación de archivos de pagos. Proporciona una herramienta útil para los desarrolladores y el soporte técnico a la hora de validar y gestionar las operaciones relacionadas con el procesamiento de pagos.

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
| `spep_advpaym_process` | Procesar pago anticipado de nómina | Get payroll advance payment processed status; UPDATE or DELETE the line acording with amount value | Get payroll advance payment processed status; UPDATE or DELETE the line acording with amount value | `model/functions/SPEP_ADVPAYM_PROCESS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Archivo Pago Quincena Pichincha TXT | `Archive Payment fortnight Pichincha TXT` | Botón (Java) | Java `ArchPaymentFortnightPichinchaBankTXT` | N | Proceso Openbravo registro `documentno` |
| 2 | Procesar pago anticipado de nómina | `SPEP_ProcessProcessPayrollAnticipated` | Botón (PL/pgSQL) | PL `SPEP_AdvPaym_Process` | N | Get payroll advance payment processed status; UPDATE or DELETE the line acording with amount value |
| 3 | Archivo de pago anticipado de nomina Rumiñauhi | `Archive Payr Adv Paym Rumiñauhi` | Informe (servlet) | Java `ArchPayrAdvPayRuminahuiBankTXT` | N | Proceso Openbravo registro `documentno` |
| 4 | Archivo de Pago Quincena Produbanco TXT | `Payment File Fortnight Produbanco TXT` | Informe (servlet) | Java `ArchivePaymentFortnightTXT` | N | Proceso Openbravo registro `documentno` |

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

Módulo: `com.sidesoft.hrm.payroll.early.payment`.

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

# Glosario — prefijo `SPEP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPEP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.hrm.payroll.early.payment` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Archive Payment fortnight Pichincha TXT` — Archivo Pago Quincena Pichincha TXT
- `SPEP_ProcessProcessPayrollAnticipated` — Procesar pago anticipado de nómina
- `Archive Payr Adv Paym Rumiñauhi` — Archivo de pago anticipado de nomina Rumiñauhi
- `Payment File Fortnight Produbanco TXT` — Archivo de Pago Quincena Produbanco TXT
- `Payroll Advance Payment Totalized` — Pago anticipado de nómina totalizado
- `Individual Advance Payment Report` — Reporte de Pago Anticipado Individual
- `Report Fortnight Pacific Bank` — Reporte Pago de Quincena Banco del Pacifico

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Payroll Indebtedness
**Package:** `com.sidesoft.hrm.payroll.indebtedness`

# Module overview — Payroll Indebtedness

## Functional

El módulo 'Payroll Indebtedness' tiene como objetivo gestionar el endeudamiento dentro del sistema de nómina de Openbravo. Está diseñado para ser utilizado por el departamento de Recursos Humanos y Finanzas, facilitando el seguimiento y gestión de los préstamos solicitados por los empleados. El alcance incluye la definición de parámetros relacionados con el endeudamiento, así como la generación de informes específicos. Este módulo depende del módulo 'Advanced PayRoll', asegurando la integración adecuada con las funcionalidades avanzadas de nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/hrm/payroll/indebtedness` |
| Web | `web/com.sidesoft.hrm.payroll.indebtedness/` |

### Declared dependencies

- Advanced PayRoll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPI`

# Guía de chat — Payroll Indebtedness

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.hrm.payroll.indebtedness`).

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
- «¿Qué es la tabla sspi_indebtednessline?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar una nueva solicitud de préstamo?
- ¿Qué datos necesito para configurar los parámetros de endeudamiento?
- ¿Dónde puedo generar el informe de préstamos solicitados?
- ¿Qué sucede si no se completa una solicitud de préstamo?
- ¿Cuántos préstamos puedo solicitar al mismo tiempo?
- ¿Cómo puedo ver el estado de mis solicitudes de préstamo?
- ¿Es posible rechazar una solicitud de préstamo después de haberla enviado?
- ¿Cómo se actualizan los datos de un préstamo existente?

# Domain — data model

## Functional

El modelo de datos del módulo se basa en la entidad principal 'sspi_indebtednessline', que actúa como cabecera para el registro de las líneas de endeudamiento. Este módulo incluye tablas modificadas como 'SSPR_LOANS' que se usan para almacenar detalles de los préstamos de los empleados. Aunque no hay triggers definidos, el manejo de datos se apoya en funciones PL/pgSQL que permiten la ejecución de lógica de negocio en la base de datos, asegurando la integridad y la validez de las transacciones relacionadas con el endeudamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sspi_indebtedness` |
| `sspi_indebtednessline` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sspi_indebtedness` | sspi_indebtedness | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspi_indebtedness_key`; Cols: control_debt, percentage_debt, observation; `SSPI_INDEBTEDNESS_CTLDEB_CHK`: CONTROL_DEBT IN ('Y', 'N'); `SSPI_INDEBTEDNESS_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `sspi_indebtednessline` | sspi_indebtednessline | — | `SSPI_INDEBT_CONCEPT` (sspr_concept_id) | ad_client_id→ad_client; sspr_concept_id→sspr_concept; sspi_indebtedness_id→sspi_indebtedness; ad_org_id→ad_org | Detalle enlazado a ad_client, sspi_indebtedness, sspr_concept. | PK `sspi_indebt_line_key`; Cols: line, sspr_concept_id, observation, sspi_indebtedness_id |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sspi_indebtedness` |
| `sspi_indebtednessline` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`SSPR_LOANS`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega principalmente a través de la ventana 'Parametros Control de Endeudamiento'. Desde esta ventana, los usuarios pueden acceder a las distintas configuraciones y funcionalidades relacionadas con el manejo de endeudamiento, además de visualizar informes y realizar operaciones sobre los préstamos, todo ello a través de una interfaz de usuario intuitiva.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.hrm.payroll.indebtedness.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Parametros Control de Endeudamiento | Control parameters Indebtedness |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Endeudamiento | Indebtedness | No |
| Parametros Control de Endeudamiento | Control parameters Indebtedness | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.hrm.payroll.indebtedness.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Parametros Control de Endeudamiento

- **AD_WINDOW_ID:** `4B4247DAD6794179B5F55F9B9A13DBF6`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Control Parameters Indebtedness | `F39D980BDA56434BB6540DB2F04E2E18` | 0 |
| 20 | Line | `6F6CBBF2E45447C9848C6FDBD111FCC5` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Line (ventana: Parametros Control de Endeudamiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Line No. | `Line` | No | No | — |
| 40 | Concept | `Sspr_Concept_ID` | No | No | — |
| 50 | Comments | `Observation` | No | No | — |

### Control Parameters Indebtedness (ventana: Parametros Control de Endeudamiento)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Control Debt | `Control_Debt` | No | No | — |
| 40 | Percentage of Debt | `Percentage_Debt` | No | No | — |
| 50 | Comments | `Observation` | No | No | — |

### Pestaña `F5EC9FEDEAB74C77A92942201415EE7D`

- **AD_TAB_ID:** `F5EC9FEDEAB74C77A92942201415EE7D` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 170 | Debt Calculation Result | `EM_Sspi_Debtresult` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso de gestión de endeudamiento incluye botones típicos como 'Completar' y 'Retornar', que permiten a los usuarios finalizar o revertir acciones según sea necesario. Entre los informes disponibles, destaca el 'Print Request Loans Advanced', que permite generar un informe detallado sobre las solicitudes de préstamos, asegurando que toda la información relevante esté disponible para la revisión y análisis. Las validaciones frecuentes garantizan que los datos ingresados cumplan con los criterios establecidos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.hrm.payroll.indebtedness.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Aprobar prestamo | Approve Loan | Sspi_change_status_approve | `sspi_change_status` | El empleado no tiene ingresos para el calculo; El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; Seleccione el concepto, para continuar con la aprobación del préstamo | — |
| Proceso / otro | Endeudamiento | Indebtedness | Indebtedness | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Print Request Loans Advanced | Print Request Loans Advanced | Print Request Loan Advanced | Java `RptRequestLoanAdvanced` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/indebtedness/ad_reports/RptRequestLoanAdvanced.java` |
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
| Reporte | Print Request Loans Advanced | `RptRequestLoanAdvanced` | Informe (servlet PDF) | `—` | — | `src/com/sidesoft/hrm/payroll/indebtedness/ad_reports/RptRequestLoanAdvanced.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Aprobar prestamo | Approve Loan | Sspi_change_status_approve | `sspi_change_status` | El empleado no tiene ingresos para el calculo; El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; Seleccione el concepto, para continuar con la aprobación del préstamo | — |
| Proceso / otro | Endeudamiento | Indebtedness | Indebtedness | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Aprobar prestamo | Approve Loan | PL `sspi_change_status` | El empleado no tiene ingresos para el calculo; El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; Seleccione el concepto, para continuar con la aprobación del préstamo | El empleado no tiene ingresos para el calculo; El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; Seleccione el concepto, para continuar con la aprobación del préstamo; Recupera si el submodulo controla endeudamiento; where '26-05-2016' between p.startdate and p.enddate |
| Proceso / otro | Endeudamiento | Indebtedness | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | Print Request Loans Advanced | Print Request Loans Advanced | Print Request Loan Advanced | Java `RptRequestLoanAdvanced` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/com/sidesoft/hrm/payroll/indebtedness/ad_reports/RptRequestLoanAdvanced.java` |
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
| 1 | Print Request Loans Advanced | `Print Request Loan Advanced` | Java `RptRequestLoanAdvanced`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Print Request Loans Advanced |

### Plantillas sin proceso en diccionario

- `src/com/sidesoft/hrm/payroll/indebtedness/ad_reports/RptRequestAdvance.jrxml`
- `src/com/sidesoft/hrm/payroll/indebtedness/ad_reports/RptRequestLoanAdvanced.jrxml`
- `src/com/sidesoft/hrm/payroll/indebtedness/ad_reports/Rpt_indebtedness.jrxml`
<!-- /knowledge-extract:reports_inventory -->

# 35 — Mensajes y errores

## Functional

Catálogo `AD_MESSAGE` del módulo y guía de soporte (completar columna «cuándo aparece» con IA o analista).

## Technical

<!-- knowledge-extract:messages -->
| VALUE | Texto (en_US) | Texto (es_ES) | Tipo | Cuándo aparece | Origen |
| --- | --- | --- | --- | --- | --- |
| `Sspi_FailedApproveLoan` | A indebtedness exceeded the percentage does not recommend approving the loan. | A indebtedness exceeded the percentage does not recommend approving the loan. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspi_LoanRefused` | Request approved. | Request approved. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo también incluye una clase Java designada para la generación de informes, específicamente 'RptRequestLoanAdvanced'. Esta clase es responsable de la compilación y generación de informes en formato Jasper, lo que permite una presentación estructurada de la información de endeudamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.hrm.payroll.indebtedness`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `RptRequestLoanAdvanced` | ad_reports | HttpSecureAppServlet | — | `src/com/sidesoft/hrm/payroll/indebtedness/ad_reports/RptRequestLoanAdvanced.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Función PL `sspi_change_status` | — | invocación proceso | El empleado no tiene ingresos para el calculo; El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo |
| Función PL `sspi_numbertoletter_es` | — | invocación proceso | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test); |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers no están presentes en este módulo; sin embargo, las funciones PL/pgSQL juegan un papel crucial en el soporte de las operaciones del sistema. Estas funciones permiten manejar la lógica de negocio, facilitando la gestión de solicitudes de préstamos y asegurando que se cumplan las directrices establecidas por la organización.

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
| `sspi_change_status` | Aprobar prestamo | El empleado no tiene ingresos para el calculo; El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; Seleccione el concepto, para continuar con la aprobación del préstamo | El empleado no tiene ingresos para el calculo; El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; Seleccione el concepto, para continuar con la aprobación del préstamo; Recupera si el submodulo controla endeudamiento; where '26-05-2016' between p.startdate and p.enddate | `model/functions/SSPI_CHANGE_STATUS.xml` |
| `sspi_numbertoletter_es` | — | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas… | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas = ' || v_armar_texto_d;; RAISE NOTICE '%','RESULT v_tnumero >= 101 and v_tnumero <200 v_number_test = ' || to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_tnumero >= 101 and v_tnumero <200 v_number_test = ' || vTexto ; | `model/functions/SSPI_NUMBERTOLETTER_ES.xml` |
| `sspi_percentageloan` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPI_PERCENTAGELOAN.xml` |
| `sspi_return_period` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPI_RETURN_PERIOD.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Aprobar prestamo | `Sspi_change_status_approve` | Botón (PL/pgSQL) | PL `sspi_change_status` | N | El empleado no tiene ingresos para el calculo; El prestamo ya se encuentra en estado Seleccionado; Debe aplicarse primero el prestamo; Seleccione el concepto, para continuar con la |
| 2 | Print Request Loans Advanced | `Print Request Loan Advanced` | Reporte | Java `RptRequestLoanAdvanced` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |

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

Módulo: `com.sidesoft.hrm.payroll.indebtedness`.

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

# Glosario — prefijo `SSPI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.hrm.payroll.indebtedness` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Sspi_change_status_approve` — Aprobar prestamo
- `Indebtedness` — Endeudamiento
- `Print Request Loan Advanced` — Print Request Loans Advanced

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Human Resources Management - Payroll - Tenth
**Package:** `com.sidesoft.hrm.payroll.tenth`

# Module overview — Human Resources Management - Payroll - Tenth

## Functional

El módulo de Gestión de Recursos Humanos - Nómina - Décimos tiene como propósito gestionar y procesar el pago de décimos a empleados. Los actores principales son los departamentos de recursos humanos y finanzas, que se encargan de calcular, procesar y reportar dichas nóminas. El alcance del módulo incluye la gestión de ingresos básicos y la liquidación de décimos. Las dependencias del módulo son la compatibilidad con el Skin de 2.50 a 3.00 y el módulo de Gestión de Recursos Humanos - Nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/hrm/payroll/tenth` |
| Web | `web/com.sidesoft.hrm.payroll.tenth/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPH`

# Guía de chat — Human Resources Management - Payroll - Tenth

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.hrm.payroll.tenth`).

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
- «¿Qué es la tabla ssph_tenth_settlement?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo calcular los décimos para un empleado específico?
- ¿Qué pasos debo seguir para liquidar los décimos de este mes?
- ¿Dónde puedo encontrar el histórico de décimos pagados?
- ¿Qué datos necesito para iniciar un nuevo proceso de liquidación de décimos?
- ¿Cómo puedo corregir un error en la liquidación ya procesada?
- ¿Cuáles son los criterios para aprobar un pago de décimos?
- ¿Puedo generar un informe de los décimos pagados a todos los empleados?
- ¿Qué hacer si no veo la opción de liquidar décimos en mi menú?

# Domain — data model

## Functional

La entidad cabecera principal en este módulo es 'ssph_tenth_settlement', que representa las liquidaciones de décimos. Este módulo tiene varias etapas donde se incluyen la creación y procesamiento de liquidaciones de nómina. La relación más importante se establece entre 'ssph_tenth_settlement' y 'ssph_tenth_settlement_line', que representa los detalles de cada liquidación. Los triggers clave como 'SSPH_TENTH_SETTLEMENT_TRG' y 'SSPH_TENTH_SETT_LINE_TRG' se utilizan para mantener la integridad de los datos y realizar validaciones automáticas al insertar o actualizar registros.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssph_basicincome` |
| `ssph_tenth_settlement` |
| `ssph_tenth_settlement_line` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssph_basicincome` | SSPH_Basicincome | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `ssph_basicincome_key`; Cols: dateupdated, datefrom, dateto, amount |
| `ssph_tenth_settlement` | SSPH_Tenth_Settlement | `SSPH_TENTH_SETTLEMENT_TRG` | — | ad_client_id→ad_client; c_doctype_id→c_doctype; sspr_labor_regime_id→sspr_labor_regime; ad_org_id→ad_org; c_year_id→c_year | Detalle enlazado a ad_client, c_doctype, sspr_labor_regime. Validado por trigger(s): SSPH_TENTH_SETTLEMENT_TRG. | PK `ssph_tenth_settlement_key`; Cols: description, c_doctype_id, documentno, processing, processed; `SSPH_TENTH_SETT_ACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `ssph_tenth_settlement_line` | SSPH_Tenth_Settlement_Line | `SSPH_TENTH_SETT_LINE_TRG` | — | c_bpartner_id→c_bpartner; sspr_labor_regime_id→sspr_labor_regime; ssph_tenth_settlement_id→ssph_tenth_settlement; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a c_bpartner, ssph_tenth_settlement, sspr_labor_regime. Validado por trigger(s): SSPH_TENTH_SETT_LINE_TRG. | PK `ssph_tenth_sett_line_key`; Cols: description, ssph_tenth_settlement_id, line, c_bpartner_id, linenetamt; `SSPH_TENTH_SETT_LINE_ACT_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SSPH_Basicincome` |
| `SSPH_Tenth_Settlement` |
| `SSPH_Tenth_Settlement_Line` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_GLITEM`, `SSPR_CODEFORMULARY107`, `SSPR_PAYROLL_TICKET_CONCEPT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de dos ventanas principales: 'Ingresos Básicos' y 'Liquidación de Décimos'. Desde estas ventanas, los usuarios pueden acceder a las distintas funciones relacionadas con la gestión de nómina, permitiendo un flujo de trabajo ordenado y facilitando el acceso a las operaciones esenciales.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `com.sidesoft.hrm.payroll.tenth.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Ingresos Básicos | Basic Income |
| Liquidación de Décimos | Tenth Settlement |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Archivo de Décimos Banco Central | Archive Tenth Central Bank | No |
| Archivo Transferencia Decimos Banco del Austro | Archive Transfer Tenth Austro TXT | No |
| Archivo TXT décimos Banco de Guayaquil | TXT file tenths Banco de Guayaquil | No |
| Beneficios de Liquidación - MRL | Settlemente Benefits - MRL | No |
| Beneficios de liquidación por categoría contable | Settlement benefits by accounting category | No |
| Ingresos Básicos | Basic Income | No |
| Liquidación de Décimos | Tenth Settlement | No |
| Liquidación de Décimos | Tenth Settlement | Sí |
| Reporte  Pago Decimos “Banco Pacifico” | Report Payment Tenth pacific bank | No |
| Reporte de Liquidación de Décimo Cuarto | Liquidation Fourteenth Report | No |
| Reporte de Liquidación de Décimo Tercero | Liquidation Thirteenth Report | No |
| Reporte de Liquidación Décimo 3ro CSV | Report of Settlement Thenth  3th CSV | No |
| Reporte de Liquidación Décimo 4to CSV | Report of Settlement Thenth  4th CSV | No |
| Reporte Décimo Tercero MRL | Thirteenth MRL Report | No |
| Reporte Liquidación de Décimos | Tenth Settlement Reports | Sí |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `com.sidesoft.hrm.payroll.tenth.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Ingresos Básicos

- **AD_WINDOW_ID:** `D278F1C9AB734452B98EAC73B127EC84`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Basic Income | `E40E116CDDCE4256B1F043144CAA92B1` | 0 |

### Ventana: Liquidación de Décimos

- **AD_WINDOW_ID:** `0B869CDD039E4358AEF6C6E62DD36A74`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Tenth Settlement | `8FDDAEFC6DB1476A9F83109F4828BE36` | 0 |
| 20 | Lines | `ACD4B3C66AF14CFEB762BF6009FE9C84` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `1AC3E6831C2449B19A7F422528AD2180`

- **AD_TAB_ID:** `1AC3E6831C2449B19A7F422528AD2180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 50 | Earned | `EM_Ssph_Earned` | No | No | — |

### Basic Income (ventana: Ingresos Básicos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Date Updated | `Dateupdated` | No | No | — |
| 40 | Date From | `Datefrom` | No | No | — |
| 50 | Date To | `Dateto` | No | No | — |
| 60 | Amount | `Amount` | No | No | — |

### Tenth Settlement (ventana: Liquidación de Décimos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Description | `Description` | No | No | — |
| 40 | Document Type | `C_Doctype_ID` | No | No | — |
| 50 | Document No. | `Documentno` | No | No | — |
| 90 | Settlement Date | `Settlementdate` | No | No | — |
| 100 | Concept | `Typeconcept` | No | No | — |
| 110 | Labor Regime | `Sspr_Labor_Regime_ID` | No | No | — |
| 115 | Starting Date | `Startdate` | No | No | — |
| 117 | Ending Date | `Enddate` | No | No | — |
| 120 | Get Tenth Lines | `Createlines` | No | No | — |
| 130 | Year | `C_Year_ID` | No | No | — |
| 140 | Tenth Settlement Process | `Processed` | No | No | — |

### Lines (ventana: Liquidación de Décimos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 30 | Description | `Description` | No | Sí | — |
| 50 | Line No. | `Line` | No | Sí | — |
| 60 | Employee | `C_Bpartner_ID` | No | Sí | — |
| 70 | Line Net Amount | `Linenetamt` | No | Sí | — |
| 75 | Monthly Value | `monthly_value` | No | Sí | — |
| 80 | Labor Regime | `Sspr_Labor_Regime_ID` | No | Sí | — |
| 90 | Adjustment Amount | `Adjustmentamt` | No | No | — |
| 95 | Adjustment 2 Amount | `Adjustment2amt` | No | No | — |
| 97 | Judicial Retention | `Judicial_Retention` | No | No | — |
| 100 | Adjusted Amount | `Adjustedamt` | No | Sí | — |
| 110 | Calculate Amount | `Calculateamount` | No | No | — |
| 120 | Days Worked | `Daysworked` | No | No | — |
| 130 | Monthly Amount | `Monthlytotalamount` | No | No | — |

### Pestaña `C1A9469938F241F3A9E870B06743EA9B`

- **AD_TAB_ID:** `C1A9469938F241F3A9E870B06743EA9B` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 70 | Earned | `EM_Ssph_Earned` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo cuenta con 13 procesos relacionados con la gestión de nómina, donde se incluyen botones típicos como 'Completar', 'Retornar', y 'Rechazar' para manejar el estado de la liquidación. Aunque no hay informes predefinidos, el módulo permite la creación de datos de salida en texto para facilitar su integración con sistemas externos. Las validaciones frecuentes incluyen la comprobación de datos de nómina y la integridad de las entradas antes de permitir su procesamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `com.sidesoft.hrm.payroll.tenth.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archivo Transferencia Decimos Banco del Austro | Archive Transfer Tenth Austro TXT | Archive Transfer Tenth Austro TXT | Java `ArchTransferTenthBankAustro` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTransferTenthBankAustro.java` |
| Botón (Java) | Archivo TXT décimos Banco de Guayaquil | TXT file tenths Banco de Guayaquil | TXT file tenths Banco de Guayaquil | Java `ArchTenthGuayaquilBankTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTenthGuayaquilBankTXT.java` |
| Botón (PL/pgSQL) | Cargar Líneas de Décimos | Get Tenth Lines | SSPH_GetTenthLines | `SSPH_GetTenthLines` | Ya existe una liquidación para esta fecha | — |
| Botón (PL/pgSQL) | Procesar Liquidación de Décimos | Tenth Settlement Process | SSPH_Tenth_Sett_Process | `SSPH_Tenth_Sett_Process` | La transacción está intentando afectar una provisión ya liquidada; RAISE_APPLICATION_ERROR(-20000,' Error OB = ' || Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID);; IF (coalesce(trim(Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID),'1') <>… | — |
| Informe (servlet) | Archivo de Décimos Banco Central | Archive Tenth Central Bank | Archive Tenth Central Bank | Java `ArchTenthCtralBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTenthCtralBankTXT.java` |
| Proceso / otro | Beneficios de Liquidación - MRL | Settlemente Benefits - MRL | Pay the fourteenth | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Beneficios de liquidación por categoría contable | Settlement benefits by accounting category | SBBAC | *(OBUIAPP / manual)* | Settlement benefits by accounting category | — |
| Proceso / otro | Reporte  Pago Decimos “Banco Pacifico” | Report Payment Tenth pacific bank | Report Payment Tenth pacific bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de Liquidación de Décimo Cuarto | Liquidation Fourteenth Report | ssph_liquidationFourteenthReport | *(OBUIAPP / manual)* | Liquidation Fourteenth Report | — |
| Proceso / otro | Reporte de Liquidación de Décimo Tercero | Liquidation Thirteenth Report | ssph_liquidationThirteenthReport | *(OBUIAPP / manual)* | Liquidation Thirteenth Report | — |
| Proceso / otro | Reporte de Liquidación Décimo 3ro CSV | Report of Settlement Thenth  3th CSV | SBCM | *(OBUIAPP / manual)* | Report of Settlement Thenth  3th CSV | — |
| Proceso / otro | Reporte de Liquidación Décimo 4to CSV | Report of Settlement Thenth  4th CSV | RSF_CSV | *(OBUIAPP / manual)* | Report of Settlement Thenth  4th CSV | — |
| Proceso / otro | Reporte Décimo Tercero MRL | Thirteenth MRL Report | Thirteenth MRL Report | *(OBUIAPP / manual)* | Thirteenth MRL Report | — |
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
| Botón (Java) | Archivo Transferencia Decimos Banco del Austro | `ArchTransferTenthBankAustro` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTransferTenthBankAustro.java` |
| Botón (Java) | Archivo TXT décimos Banco de Guayaquil | `ArchTenthGuayaquilBankTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTenthGuayaquilBankTXT.java` |
| Informe (servlet) | Archivo de Décimos Banco Central | `ArchTenthCtralBankTXT` | Proceso Java (toolbar/background) | `documentno` | — | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTenthCtralBankTXT.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archivo Transferencia Decimos Banco del Austro | Archive Transfer Tenth Austro TXT | Archive Transfer Tenth Austro TXT | Java `ArchTransferTenthBankAustro` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTransferTenthBankAustro.java` |
| Botón (Java) | Archivo TXT décimos Banco de Guayaquil | TXT file tenths Banco de Guayaquil | TXT file tenths Banco de Guayaquil | Java `ArchTenthGuayaquilBankTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTenthGuayaquilBankTXT.java` |
| Botón (PL/pgSQL) | Cargar Líneas de Décimos | Get Tenth Lines | SSPH_GetTenthLines | `SSPH_GetTenthLines` | Ya existe una liquidación para esta fecha | — |
| Botón (PL/pgSQL) | Procesar Liquidación de Décimos | Tenth Settlement Process | SSPH_Tenth_Sett_Process | `SSPH_Tenth_Sett_Process` | La transacción está intentando afectar una provisión ya liquidada; RAISE_APPLICATION_ERROR(-20000,' Error OB = ' || Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID);; IF (coalesce(trim(Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID),'1') <>… | — |
| Informe (servlet) | Archivo de Décimos Banco Central | Archive Tenth Central Bank | Archive Tenth Central Bank | Java `ArchTenthCtralBankTXT` (AD_MODEL_OBJECT `S`) | Proceso Openbravo registro `documentno` | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTenthCtralBankTXT.java` |
| Proceso / otro | Beneficios de Liquidación - MRL | Settlemente Benefits - MRL | Pay the fourteenth | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Beneficios de liquidación por categoría contable | Settlement benefits by accounting category | SBBAC | *(OBUIAPP / manual)* | Settlement benefits by accounting category | — |
| Proceso / otro | Reporte  Pago Decimos “Banco Pacifico” | Report Payment Tenth pacific bank | Report Payment Tenth pacific bank | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte de Liquidación de Décimo Cuarto | Liquidation Fourteenth Report | ssph_liquidationFourteenthReport | *(OBUIAPP / manual)* | Liquidation Fourteenth Report | — |
| Proceso / otro | Reporte de Liquidación de Décimo Tercero | Liquidation Thirteenth Report | ssph_liquidationThirteenthReport | *(OBUIAPP / manual)* | Liquidation Thirteenth Report | — |
| Proceso / otro | Reporte de Liquidación Décimo 3ro CSV | Report of Settlement Thenth  3th CSV | SBCM | *(OBUIAPP / manual)* | Report of Settlement Thenth  3th CSV | — |
| Proceso / otro | Reporte de Liquidación Décimo 4to CSV | Report of Settlement Thenth  4th CSV | RSF_CSV | *(OBUIAPP / manual)* | Report of Settlement Thenth  4th CSV | — |
| Proceso / otro | Reporte Décimo Tercero MRL | Thirteenth MRL Report | Thirteenth MRL Report | *(OBUIAPP / manual)* | Thirteenth MRL Report | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Archivo Transferencia Decimos Banco del Austro | Archive Transfer Tenth Austro TXT | Java `ArchTransferTenthBankAustro` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Botón (Java) | Archivo TXT décimos Banco de Guayaquil | TXT file tenths Banco de Guayaquil | Java `ArchTenthGuayaquilBankTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Botón (PL/pgSQL) | Cargar Líneas de Décimos | Get Tenth Lines | PL `SSPH_GetTenthLines` | Ya existe una liquidación para esta fecha | Ya existe una liquidación para esta fecha |
| Botón (PL/pgSQL) | Procesar Liquidación de Décimos | Tenth Settlement Process | PL `SSPH_Tenth_Sett_Process` | La transacción está intentando afectar una provisión ya liquidada; RAISE_APPLICATION_ERROR(-20000,' Error OB = ' || Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID);; IF (coalesce(trim(Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID),'1') <>… | La transacción está intentando afectar una provisión ya liquidada; RAISE_APPLICATION_ERROR(-20000,' Error OB = ' || Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID);; IF (coalesce(trim(Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID),'1') <> Cur_Lines.tenth_sett_line_id) THEN; RAISE_APPLICATION_ERROR(-20000,'@La transacción está intentando afectar una provisión ya liquidada@'); |
| Informe (servlet) | Archivo de Décimos Banco Central | Archive Tenth Central Bank | Java `ArchTenthCtralBankTXT` | Proceso Openbravo registro `documentno` | Proceso Openbravo registro `documentno` |
| Proceso / otro | Beneficios de Liquidación - MRL | Settlemente Benefits - MRL | — | — | — |
| Proceso / otro | Beneficios de liquidación por categoría contable | Settlement benefits by accounting category | — | Settlement benefits by accounting category | — |
| Proceso / otro | Reporte  Pago Decimos “Banco Pacifico” | Report Payment Tenth pacific bank | — | — | — |
| Proceso / otro | Reporte de Liquidación de Décimo Cuarto | Liquidation Fourteenth Report | — | Liquidation Fourteenth Report | — |
| Proceso / otro | Reporte de Liquidación de Décimo Tercero | Liquidation Thirteenth Report | — | Liquidation Thirteenth Report | — |
| Proceso / otro | Reporte de Liquidación Décimo 3ro CSV | Report of Settlement Thenth  3th CSV | — | Report of Settlement Thenth  3th CSV | — |
| Proceso / otro | Reporte de Liquidación Décimo 4to CSV | Report of Settlement Thenth  4th CSV | — | Report of Settlement Thenth  4th CSV | — |
| Proceso / otro | Reporte Décimo Tercero MRL | Thirteenth MRL Report | — | Thirteenth MRL Report | — |
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
**Total de reportes del módulo: 8**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **8**.

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

El módulo incluye clases de Java que gestionan la generación de archivos de texto, facilitando la exportación de datos de nómina para su posterior uso fuera del sistema. Estas clases utilizan técnicas estándar de conexión y respuesta HTTP para facilitar la creación de archivos de salida que pueden ser utilizados en diferentes formatos por otras aplicaciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.hrm.payroll.tenth`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ArchTenthCtralBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTenthCtralBankTXT.java` |
| `ArchTenthGuayaquilBankTXT` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTenthGuayaquilBankTXT.java` |
| `ArchTransferTenthBankAustro` | create_txt | DalBaseProcess | — | `src/com/sidesoft/hrm/payroll/tenth/create_txt/ArchTransferTenthBankAustro.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSPH_TENTH_SETTLEMENT_TRG` | `ssph_tenth_settlement` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSPH_TENTH_SETT_LINE_TRG` | `ssph_tenth_settlement_line` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Ssfi_Banktransfer Code` | `code='17'` |
| AD_VAL_RULE | — | `Concept by type` | `sspr_concept_id IN (SELECT sspr_concept_id FROM sspr_concept WHERE concepttypepayroll IN ('DC','DT') )` |
| AD_VAL_RULE | — | `ssph_ValidateUserLogg` | `AD_User.AD_User_ID = @#AD_User_ID@` |
| AD_VAL_RULE | — | `Ssph_ValidateTenthThird` | `SSPH_TENTH_SETTLEMENT.TYPECONCEPT= '13TH' AND  SSPH_TENTH_SETTLEMENT.C_YEAR_ID=@C_YEAR_ID@` |
| AD_VAL_RULE | — | `Sspr_TenthSettlement14Th` | `SSPH_Tenth_Settlement.Typeconcept='14TH'` |
| AD_VAL_RULE | — | `Tenth Settlement DocType` | `DocBaseType='SSPH_TS'` |
| Función PL `ssph_gettenthlines` | — | invocación proceso | Ya existe una liquidación para esta fecha |
| Función PL `ssph_tenth_sett_process` | — | invocación proceso | La transacción está intentando afectar una provisión ya liquidada; RAISE_APPLICATION_ERROR(-20000,' Error OB = ' || Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID);; IF (coalesce(trim(Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID),'1') <> Cur_Lines.tenth_sett_line_id) THEN |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL son esenciales para asegurarse de que las operaciones en la base de datos se realicen de manera eficiente y segura. Dos triggers importantes ayudan a definir la lógica de negocio en la inserción y actualización de datos en las tablas relacionadas con la nómina, garantizando así la coherencia de la información manejada en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSPH_TENTH_SETTLEMENT_TRG` | `ssph_tenth_settlement` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPH_TENTH_SETTLEMENT_TRG.xml` |
| `SSPH_TENTH_SETT_LINE_TRG` | `ssph_tenth_settlement_line` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPH_TENTH_SETT_LINE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssph_active_contract_ident` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPH_ACTIVE_CONTRACT_IDENT.xml` |
| `ssph_gettenthlines` | Cargar Líneas de Décimos | Ya existe una liquidación para esta fecha | Ya existe una liquidación para esta fecha | `model/functions/SSPH_GETTENTHLINES.xml` |
| `ssph_tenth_sett_process` | Procesar Liquidación de Décimos | La transacción está intentando afectar una provisión ya liquidada; RAISE_APPLICATION_ERROR(-20000,' Error OB = ' || Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID);; IF (coalesce(trim(Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID),'1') <>… | La transacción está intentando afectar una provisión ya liquidada; RAISE_APPLICATION_ERROR(-20000,' Error OB = ' || Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID);; IF (coalesce(trim(Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID),'1') <> Cur_Lines.tenth_sett_line_id) THEN; RAISE_APPLICATION_ERROR(-20000,'@La transacción está intentando afectar una provisión ya liquidada@'); | `model/functions/SSPH_TENTH_SETT_PROCESS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Archivo Transferencia Decimos Banco del Austro | `Archive Transfer Tenth Austro TXT` | Botón (Java) | Java `ArchTransferTenthBankAustro` | N | Proceso Openbravo registro `documentno` |
| 2 | Archivo TXT décimos Banco de Guayaquil | `TXT file tenths Banco de Guayaquil` | Botón (Java) | Java `ArchTenthGuayaquilBankTXT` | N | Proceso Openbravo registro `documentno` |
| 3 | Cargar Líneas de Décimos | `SSPH_GetTenthLines` | Botón (PL/pgSQL) | PL `SSPH_GetTenthLines` | N | Ya existe una liquidación para esta fecha |
| 4 | Procesar Liquidación de Décimos | `SSPH_Tenth_Sett_Process` | Botón (PL/pgSQL) | PL `SSPH_Tenth_Sett_Process` | N | La transacción está intentando afectar una provisión ya liquidada; RAISE_APPLICATION_ERROR(-20000,' Error OB = ' || Cur_Lines.EM_SSPH_TENTH_SETT_LINE_ID);; IF (coalesce(trim(Cur_Li |
| 5 | Archivo de Décimos Banco Central | `Archive Tenth Central Bank` | Informe (servlet) | Java `ArchTenthCtralBankTXT` | N | Proceso Openbravo registro `documentno` |

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

Módulo: `com.sidesoft.hrm.payroll.tenth`.

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

# Glosario — prefijo `SSPH`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPH` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.hrm.payroll.tenth` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Archive Transfer Tenth Austro TXT` — Archivo Transferencia Decimos Banco del Austro
- `TXT file tenths Banco de Guayaquil` — Archivo TXT décimos Banco de Guayaquil
- `SSPH_GetTenthLines` — Cargar Líneas de Décimos
- `SSPH_Tenth_Sett_Process` — Procesar Liquidación de Décimos
- `Archive Tenth Central Bank` — Archivo de Décimos Banco Central
- `Pay the fourteenth` — Beneficios de Liquidación - MRL
- `SBBAC` — Beneficios de liquidación por categoría contable
- `Report Payment Tenth pacific bank` — Reporte  Pago Decimos “Banco Pacifico”
- `ssph_liquidationFourteenthReport` — Reporte de Liquidación de Décimo Cuarto
- `ssph_liquidationThirteenthReport` — Reporte de Liquidación de Décimo Tercero
- `SBCM` — Reporte de Liquidación Décimo 3ro CSV
- `RSF_CSV` — Reporte de Liquidación Décimo 4to CSV
- `Thirteenth MRL Report` — Reporte Décimo Tercero MRL

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Attendance Payroll Module
**Package:** `ec.com.sidesoft.hrm.payroll.attendancepayroll`

# Module overview — Attendance Payroll Module

## Functional

El Módulo de Nómina de Asistencia sirve para gestionar y procesar la nómina de los empleados según su asistencia. Está diseñado para ser utilizado por funcionarios de recursos humanos y personal administrativo que requieren llevar un control efectivo de las horas trabajadas y su correlación con los pagos. Este módulo depende de componentes centrales de Openbravo y está en sintonía con otros módulos relacionados con la gestión de recursos humanos y finanzas en Ecuador.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/hrm/payroll/attendancepayroll` |
| Web | `web/ec.com.sidesoft.hrm.payroll.attendancepayroll/` |

### Declared dependencies

- Core
- Human Resources Management - Payroll
- Localization of Ecuador - Finances
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SHPAPR`

# Guía de chat — Attendance Payroll Module

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.hrm.payroll.attendancepayroll`).

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

- ¿Cómo registro la asistencia de un empleado?
- ¿Qué debo hacer si un registro de asistencia es incorrecto?
- ¿Cómo completo la nómina de asistencia?
- ¿Puedo ver un informe de asistencia de todos los empleados?
- ¿Por qué algunos registros no se pueden completar?
- ¿Dónde puedo encontrar la documentación del módulo?
- ¿Cómo se relaciona este módulo con la nómina general?
- ¿Qué pasos seguir si una incidencia ocurre en el sistema?

# Domain — data model

## Functional

El modelo de datos de este módulo se centra en un encabezado que representa el registro de asistencia de los empleados. Este registro puede contener distintas etapas, como la carga de asistencia y la generación de la nómina. Aunque no hay tablas físicas definidas en el inventario, se pueden inferir ligeras relaciones entre los registros de los empleados y sus asistencias. Es importante destacar que este módulo no cuenta con triggers significativos ni funciones PL asociadas.

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

`AD_USER`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no presenta ventanas específicas en la interfaz de usuario, lo que sugiere que su funcionalidad se accede a través de los menús de Openbravo. Los usuarios pueden navegar por las opciones disponibles para gestionar y acceder a las funcionalidades relacionadas con la nómina de asistencia.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.hrm.payroll.attendancepayroll.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Reporte Detallado de Vacaciones por empleado | Detailed Vacation Report per employee | No |
| Reporte Nómina Individual por Empleado | Individual Payroll Report by Employee | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.hrm.payroll.attendancepayroll.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `118`

- **AD_TAB_ID:** `118` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 295 | EM_Shpapr_Adminassis | `EM_Shpapr_Adminassis` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo cuenta con dos botones de proceso principales que permiten gestionar la nómina de forma efectiva: uno para completar el registro de asistencia y otro para retornar o rechazar entradas. Aunque no hay informes generados dentro del módulo, se pueden prever validaciones comunes relacionadas con la asistencia y los horarios que los empleados han trabajado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.hrm.payroll.attendancepayroll.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Detallado de Vacaciones por empleado | Detailed Vacation Report per employee | Detailed Vacation Report per employee | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Nómina Individual por Empleado | Individual Payroll Report by Employee | Individual Payroll Report by Employee | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Reporte Detallado de Vacaciones por empleado | Detailed Vacation Report per employee | Detailed Vacation Report per employee | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Nómina Individual por Empleado | Individual Payroll Report by Employee | Individual Payroll Report by Employee | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Detallado de Vacaciones por empleado | Detailed Vacation Report per employee | — | — | — |
| Proceso / otro | Reporte Nómina Individual por Empleado | Individual Payroll Report by Employee | — | — | — |
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
**Total de reportes del módulo: 9**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **9**.

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

El módulo no especifica la implementación de clases Java, lo que indica que su funcionalidad se integra a través de las capacidades nativas de Openbravo, sin la necesidad de extensiones personalizadas en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.hrm.payroll.attendancepayroll`.

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
| AD_VAL_RULE | — | `PDF Type` | `value in ('pdf')` |
| AD_VAL_RULE | — | `SHPAPR_ValidUser` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `SHPAPR_IsEmployee` | `(C_BPARTNER.ISEMPLOYEE = 'Y'  and  C_BPARTNER.C_BPARTNER_ID in (
	SELECT AU.C_BPARTNER_ID 
	FROM AD_ROLE AROLE
	JOIN AD_` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

No se han definido triggers ni funciones PL específicas para este módulo, lo que significa que no hay roles críticos relacionados con estos elementos en la base de datos. Sin embargo, las interacciones con tablas modificadas, como 'AD_USER', pueden haber implicaciones en el manejo de la nómina y la seguridad de los datos.

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

Módulo: `ec.com.sidesoft.hrm.payroll.attendancepayroll`.

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

# Glosario — prefijo `SHPAPR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SHPAPR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.hrm.payroll.attendancepayroll` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Detailed Vacation Report per employee` — Reporte Detallado de Vacaciones por empleado
- `Individual Payroll Report by Employee` — Reporte Nómina Individual por Empleado

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Automatic Process of Payment Roles Monthly
**Package:** `ec.com.sidesoft.hrm.payroll.payment.rol`

# Module overview — Sidesoft Automatic Process of Payment Roles Monthly

## Functional

El módulo 'Sidesoft Automatic Process of Payment Roles Monthly' tiene como propósito automatizar el proceso de envío de roles de pago mensual dentro de la gestión de nómina. Los actores principales incluyen administradores de recursos humanos y personal de contabilidad que gestionan nóminas y pagos. Su alcance abarca la generación y envío de reportes de nómina a los empleados y la conciliación de pagos. Este módulo depende de la versión compatible de la interfaz (Skin) y de la gestión de recursos humanos específicamente en el área de nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/hrm/payroll/payment/rol` |
| Web | `web/ec.com.sidesoft.hrm.payroll.payment.rol/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPRPR`

# Guía de chat — Sidesoft Automatic Process of Payment Roles Monthly

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.hrm.payroll.payment.rol`).

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
- «¿Qué es la tabla ssprpr_config?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo configurar el envío de roles de pago en el módulo?
- ¿Qué hago si no recibo los roles de pago enviados?
- ¿Puedo modificar la configuración de envío después de haberla establecido?
- ¿Dónde encuentro la información sobre los pagos de mis empleados?
- ¿El módulo genera algún tipo de reporte de los pagos enviados?
- ¿Cómo puedo asegurarme de que los datos de nómina son correctos antes de enviar?
- ¿Existen notificaciones por correo electrónico sobre el estado de los envíos de rol?
- ¿Cuál es el proceso para corregir un rol de pago enviado incorrectamente?

# Domain — data model

## Functional

La entidad principal de este módulo es 'SSPR_PAYROLL_TICKET', que se relaciona a su vez con la tabla de configuración 'ssprpr_config'. No se definen etapas intermedias en el flujo descrito, lo que indica que el proceso es más directo. Aunque no hay triggers definidos, la integración y los procesos dependen de las funciones y la lógica encapsulada en las clases Java relacionadas que garantizan la correcta ejecución de la automatización y los envíos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssprpr_config` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssprpr_config` | SSPRPR_Config | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_user_id→ad_user | Parametrización / catálogo de soporte. | PK `ssprpr_config_key`; Cols: ad_user_id, body, footer, subject, reportformat; `SSPRPR_CONFIG_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SSPRPR_Config` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`SSPR_PAYROLL_TICKET`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de una única ventana llamada 'Configuración Envío de roles de pago'. Esta ventana permite a los usuarios acceder a las configuraciones necesarias para establecer cómo se enviarán los roles de pago a los empleados. La interfaz es intuitiva y está diseñada para facilitar la visualización y modificación de estas configuraciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.hrm.payroll.payment.rol.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuración Envío de roles de pago | Configuration Sending Payment Roles |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración Envío de roles de pago | Configuration Sending Payment Roles | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.hrm.payroll.payment.rol.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuración Envío de roles de pago

- **AD_WINDOW_ID:** `A1831A019D8244BE9A67A2B3CA8C7EAD`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Configuration Sending Payment Roles | `F10136463FE14714952EFFE216D86CE9` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `92F08CF4C33445AA921728AD1F73D19E`

- **AD_TAB_ID:** `92F08CF4C33445AA921728AD1F73D19E` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 240 | Email Sended | `EM_Ssprpr_Issended` | No | No | E66B5C86123F4DB5BB1EAB7D5A72B675 |
| 250 | Email Log | `EM_Ssprpr_Emaillog` | No | No | E66B5C86123F4DB5BB1EAB7D5A72B675 |

### Configuration Sending Payment Roles (ventana: Configuración Envío de roles de pago)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Report Format | `Reportformat` | No | No | — |
| 20 | Subject | `Subject` | No | No | 427F16054D9F46B1A5BB6190982F51BC |
| 30 | Body | `Body` | No | No | 427F16054D9F46B1A5BB6190982F51BC |
| 50 | Footer | `Footer` | No | No | 427F16054D9F46B1A5BB6190982F51BC |
| 120 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso identificado que permite completar el envío de roles de pago, lo que implica la ejecución de la lógica de negocio para garantizar que todos los empleados reciban su información de nómina adecuada. Los botones típicos que se utilizan incluyen aquellos para completar o retroceder en el envío, aunque en este caso el proceso se ejecuta automáticamente en un fondo programado sin la necesidad de intervención manual constante. A pesar de no haber informes específicos incorporados, es crítico aplicar validaciones al iniciar el proceso para asegurar que todos los datos sean correctos antes del envío.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.hrm.payroll.payment.rol.es_ES/referencedata/translation/`.

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
| Background | Proceso Background Envío de roles de pago | Sending Payment Roles Background | SendingPaymentRolesBackground | *(OBUIAPP / manual)* | — | — |
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

El rol de Java en este módulo es clave, con al menos tres clases definidas que manejan la lógica para la impresión de reportes, gestión de envíos en segundo plano y el manejo de correos electrónicos. Estas clases son responsables de los procesos de comunicación y notificación hacia los empleados y administradores, asegurando un funcionamiento fluido y eficiente del proceso automático.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.hrm.payroll.payment.rol`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SSPRPR_PrintReportPaymentRol` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/hrm/payroll/payment/rol/ad_process/SSPRPR_PrintReportPaymentRol.java` |
| `SendingPaymentRolesBackground` | background | DalBaseProcess | — | `src/ec/com/sidesoft/hrm/payroll/payment/rol/background/SendingPaymentRolesBackground.java` |
| `EmailManager` | utility | — | — | `src/ec/com/sidesoft/hrm/payroll/payment/rol/utility/EmailManager.java` |
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

Dentro del módulo, los triggers y funciones PL no están directamente implementados, lo que indica que el manejo de procesos depende de las funciones Java. Sin embargo, se ha identificado que se requiere una correcta gestión en la tabla modificada 'SSPR_PAYROLL_TICKET' para asegurar que todos los detalles de los roles de pago estén actualizados. Esto permite al soporte L2 resolver problemas rápidamente accediendo y ajustando la configuración según sea necesario.

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

Módulo: `ec.com.sidesoft.hrm.payroll.payment.rol`.

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

# Glosario — prefijo `SSPRPR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPRPR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.hrm.payroll.payment.rol` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `SendingPaymentRolesBackground` — Proceso Background Envío de roles de pago

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Automatic Process of Payment Roles Fortnight
**Package:** `ec.com.sidesoft.hrm.payroll.payment.rol.fortnight`

# Module overview — Sidesoft Automatic Process of Payment Roles Fortnight

## Functional

El módulo 'Sidesoft Automatic Process of Payment Roles Fortnight' tiene como propósito facilitar la gestión automática de los pagos de roles quincenales en el ámbito de la nómina. Los actores principales son los usuarios del área de recursos humanos que gestionan los pagos y los administradores del sistema. El alcance del módulo incluye la generación de informes de pagos y la ejecución de procesos en segundo plano para enviar los roles de pago automáticamente. Este módulo depende de 'Human Resources Management - Payroll', 'Payroll Anticipated Payments' y 'Sidesoft Automatic Process of Payment Roles Monthly'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/hrm/payroll/payment/rol/fortnight` |
| Web | `web/ec.com.sidesoft.hrm.payroll.payment.rol.fortnight/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Payroll Anticipated Payments
- Sidesoft Automatic Process of Payment Roles Monthly

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPRPRF`

# Guía de chat — Sidesoft Automatic Process of Payment Roles Fortnight

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.hrm.payroll.payment.rol.fortnight`).

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

- ¿Cómo puedo configurar el proceso de pago de roles quincenales?
- ¿Qué procesos en segundo plano se ejecutan para el envío de pagos?
- ¿Existen reportes específicos que puedo generar con este módulo?
- ¿Cómo se controla el estado de un envío de rol de pago?
- ¿Cuáles son los errores más comunes al ejecutar el proceso de pago?
- ¿Dónde puedo encontrar la configuración de roles en Openbravo?
- ¿Se puede integrar este módulo con otros sistemas de nómina?
- ¿Qué dependencias debo considerar antes de implementar este módulo?

# Domain — data model

## Functional

La entidad principal del módulo es la configuración de pagos de rol quincenal, representada en la tabla 'SSPRPR_CONFIG'. Este módulo no incluye tablas adicionales de etapas o relaciones complejas, ya que su función principal se centra en automatizar el proceso de envío de pagos. No obstante, se han implementado disparadores y funciones para la validación y ejecución adecuada de procesos sin necesidad de modificar la estructura de base de datos existente. No se especifican triggers claves en el inventario, lo que sugiere que la lógica de negocios se maneja principalmente a través de procesos programáticos.

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

`SSPRPR_CONFIG`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no incluye ventanas definidas en la interfaz de usuario de Openbravo; por lo tanto, la navegación se realizará a través de acciones específicas que involucran el uso de funciones programáticas para gestionar el proceso de pago directamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.hrm.payroll.payment.rol.fortnight.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.hrm.payroll.payment.rol.fortnight.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `B1689C7BB4AF4D698A9404950C031869`

- **AD_TAB_ID:** `B1689C7BB4AF4D698A9404950C031869` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 90 | Subject Fortnight | `EM_Ssprprf_Subject` | No | No | 2F1B1ABEF837411BA1B1832F0FAE5441 |
| 95 | Body Fortnight | `EM_Ssprprf_Body` | No | No | 2F1B1ABEF837411BA1B1832F0FAE5441 |
| 100 | Footer Fortnight | `EM_Ssprprf_Footer` | No | No | 2F1B1ABEF837411BA1B1832F0FAE5441 |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso principal relacionado con el envío de roles de pago, el cual se ejecuta en segundo plano. Este proceso permite iniciar la ejecución automáticamente basado en la configuración establecida. Las acciones típicas incluirían completar el proceso de envío, y, aunque no hay botones específicos mencionados, las validaciones frecuentes se centran en la correcta configuración de los datos de entrada para evitar errores durante la ejecución. No se especifican informes dentro del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.hrm.payroll.payment.rol.fortnight.es_ES/referencedata/translation/`.

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
| Background | Proceso Background Envío de roles de pago quincenal | SendingPaymentRolesFortnightBackground | SendingPaymentRolesFortnightBackground | *(OBUIAPP / manual)* | — | — |
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

El módulo incluye dos clases Java que gestionan la generación de reportes en formato PDF y la ejecución de procesos en segundo plano, facilitando así la automatización y la integración de la lógica de negocio con la interfaz de usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.hrm.payroll.payment.rol.fortnight`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SSPRPRF_PrintReportPaymentRoFortnight` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/hrm/payroll/payment/rol/fortnight/ad_process/SSPRPRF_PrintReportPaymentRoFortnight.java` |
| `SendingPaymentRolesFortnightBackground` | background | DalBaseProcess | — | `src/ec/com/sidesoft/hrm/payroll/payment/rol/fortnight/background/SendingPaymentRolesFortnightBackground.java` |
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

El módulo utiliza PL/SQL para gestionar la lógica del negocio relacionada con el envío de los roles quincenales. Aunque no se detallan triggers específicos, es probable que la funcionalidad se apoye en procesos que se habiliten bajo condiciones específicas, asegurando la integridad de los datos y la correcta ejecución de procesos relacionados con nómina.

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

Módulo: `ec.com.sidesoft.hrm.payroll.payment.rol.fortnight`.

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

# Glosario — prefijo `SSPRPRF`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPRPRF` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.hrm.payroll.payment.rol.fortnight` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `SendingPaymentRolesFortnightBackground` — Proceso Background Envío de roles de pago quincenal

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Payroll Anticipated Payments - Sentmail
**Package:** `ec.com.sidesoft.hrm.payroll.early.payment.sentmail`

# Module overview — Payroll Anticipated Payments - Sentmail

## Functional

El módulo de 'Payroll Anticipated Payments - Sentmail' está diseñado para gestionar los pagos anticipados en nómina, permitiendo un flujo eficiente de información entre las gestiones de recursos humanos y la contabilidad. Su principal actor son los empleados del departamento de nómina, quienes utilizan este módulo para procesar pagos adaptados a las necesidades de los empleados. El alcance del módulo incluye la preparación y gestión de las solicitudes de pagos anticipados. Dependencias clave incluyen la integración con la funcionalidad básica del Core del ERP Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/hrm/payroll/early/payment/sentmail` |
| Web | `web/ec.com.sidesoft.hrm.payroll.early.payment.sentmail/` |

### Declared dependencies

- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPEPM`

# Guía de chat — Payroll Anticipated Payments - Sentmail

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.hrm.payroll.early.payment.sentmail`).

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

- ¿Cómo puedo registrar un pago anticipado?
- ¿Qué información necesito para procesar un pago anticipado?
- ¿Puedo cancelar un pago anticipado una vez que ha sido solicitado?
- ¿Cuál es el tiempo de procesamiento estimado para un pago anticipado?
- ¿Hay un límite en la cantidad que se puede solicitar como pago anticipado?
- ¿Cómo se afecta mi sueldo por un pago anticipado?
- ¿A quién contacto si tengo problemas con el sistema de pagos anticipados?
- ¿Se generan informes de los pagos anticipados realizados?

# Domain — data model

## Functional

Este módulo opera sobre la tabla SPEP_ADVANCE_PAYMENT, donde se registran los datos relacionados con los pagos anticipados. Aunque no hay etapas específicas definidas, se entienda que el flujo implica la creación, procesamiento y registro de las solicitudes de pago. La tabla de pagos anticipados sirve como la entidad cabecera del modelo y no se han definido triggers clave ni relaciones adicionales en el contexto actual.

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

`SPEP_ADVANCE_PAYMENT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no incluye ventanas definidas para la navegación, lo que sugiere que puede operar principalmente detrás de escenas o que su uso está pensado para integrarse con otros módulos del sistema. La funcionalidad se limita a las acciones relacionadas con los registros de pagos anticipados en la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.hrm.payroll.early.payment.sentmail.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.hrm.payroll.early.payment.sentmail.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `AEEEB8CBBE3E4665A6EA3CED390E25FD`

- **AD_TAB_ID:** `AEEEB8CBBE3E4665A6EA3CED390E25FD` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 110 | EM_Spepm_Sendmail | `EM_Spepm_Sendmail` | No | No | — |
| 120 | EM_Spepm_Sentmail | `EM_Spepm_Sentmail` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

No se han establecido botones o procesos típicos como completar, retornar o rechazar dentro de este módulo. Por lo tanto, el enfoque se centra en el manejo de registros de pagos anticipados mediante la modificación de la tabla correspondiente. Dado que no se presentan informes ni validaciones específicas en este contexto, el uso se limita a las actualizaciones generadas en la tabla SPEP_ADVANCE_PAYMENT.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.hrm.payroll.early.payment.sentmail.es_ES/referencedata/translation/`.

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

Este módulo no incluye clases Java definidas, lo que sugiere que su implementación actual está limitada a la ejecución de SQL sobre la base de datos sin intervención de lógica adicional implementada en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.hrm.payroll.early.payment.sentmail`.

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

En el contexto del soporte, aunque no se han definido triggers ni funciones PL para este módulo, es crucial el reconocimiento de la tabla SPEP_ADVANCE_PAYMENT como la base que almacena las solicitudes y registros de pagos anticipados. Cualquier funcionalidad adicional podría integrarse en futuras versiones del módulo.

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

Módulo: `ec.com.sidesoft.hrm.payroll.early.payment.sentmail`.

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

# Glosario — prefijo `SPEPM`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPEPM` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.hrm.payroll.early.payment.sentmail` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Payroll Reports
**Package:** `ec.com.sidesoft.hrm.payroll.reports`

# Module overview — Sidesoft Payroll Reports

## Functional

El módulo Sidesoft Payroll Reports tiene como propósito principal la generación de informes relacionados con la nómina, facilitando así el cumplimiento de obligaciones fiscales y la toma de decisiones en la gestión de recursos humanos. Este módulo es utilizado por los departamentos de recursos humanos y finanzas que requieren información precisa y actualizada sobre los reportes de nómina y sus ajustes. El alcance del módulo incluye la generación de informes de manera fácil y eficiente, dependiendo de la integración con el módulo de Human Resources Management - Payroll.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/hrm/payroll/reports` |
| Web | `web/ec.com.sidesoft.hrm.payroll.reports/` |

### Declared dependencies

- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPRRE`

# Guía de chat — Sidesoft Payroll Reports

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.hrm.payroll.reports`).

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

- ¿Cómo puedo generar el informe de nómina mensual?
- ¿Qué datos se incluyen en el reporte de ajustes de nómina?
- ¿Dónde encuentro los reportes de retenciones fiscales?
- ¿Es posible personalizar los informes generados?
- ¿Se pueden exportar los informes a formatos como Excel o PDF?
- ¿Qué otras dependencias debo tener en cuenta para usar este módulo?
- ¿Cómo puedo validar que los datos en el informe son correctos?
- ¿Con qué frecuencia se actualizan los reportes de nómina?

# Domain — data model

## Functional

Aunque no se especifican tablas físicas, el módulo se basa en la integración con el sistema de nómina para extraer datos relevantes. Se infiere que las etapas del flujo de trabajo están relacionadas con la preparación y generación de informes, asegurando que los datos se presenten de forma clara y precisa. Las relaciones con el módulo de nómina son clave, pues permiten el acceso a datos actualizados y relevantes para la elaboración de reportes. No se han definido triggers o funciones PL dentro de este módulo.

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

Actualmente, no se han definido ventanas específicas en la interfaz de usuario para el módulo Sidesoft Payroll Reports. Sin embargo, se espera que los usuarios naveguen a través de los menús relacionados con informes dentro de la plataforma de Openbravo, utilizando los elementos ya disponibles en el sistema.

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

Dado que el módulo no tiene botones o procesos específicos definidos, se puede suponer que los usuarios interactúan principalmente a través de la generación y ejecución de informes que ya se encuentran integrados en el sistema. Las validaciones frecuentes pueden incluir verificaciones de datos antes de la generación de informes para asegurar la precisión y cumplimiento de las normativas fiscales vigentes.

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
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

No se han definido clases Java específicas para este módulo, lo que podría indicar que la funcionalidad se basa en configuraciones directas dentro del ERP sin necesidad de lógica adicional programada en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.hrm.payroll.reports`.

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

No se identifican triggers ni funciones PL dentro del módulo Sidesoft Payroll Reports, lo que sugiere que las operaciones del módulo son directas y se ejecutan en base a la relación con otros módulos de gestión de nómina. Esto implica que el soporte debe estar preparado para trabajar en la integración de datos entre módulos.

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

Módulo: `ec.com.sidesoft.hrm.payroll.reports`.

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

# Glosario — prefijo `SSPRRE`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPRRE` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.hrm.payroll.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Custom Payroll Reports
**Package:** `ec.com.sidesoft.custom.payroll.reports`

# Module overview — Custom Payroll Reports

## Functional

El módulo Custom Payroll Reports tiene como propósito principal facilitar la generación de informes personalizados relacionados con la nómina dentro del ERP Openbravo. Este módulo está destinado a los usuarios del área de recursos humanos y contabilidad, así como a los desarrolladores y personal de soporte que requieran personalizar o mantener los informes de nómina. El alcance de este módulo incluye la generación de certificados de informes de nómina, permitiendo la visualización y exportación de datos relevantes. Dependencias del módulo incluyen compatibilidad con la piel del sistema de la versión 2.50 a la 3.00, el núcleo del ERP y el módulo de gestión de recursos humanos y nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/payroll/reports` |
| Web | `web/ec.com.sidesoft.custom.payroll.reports/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSCPR`

# Guía de chat — Custom Payroll Reports

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.payroll.reports`).

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
- «¿Qué es la tabla sscpr_reportcertificate?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo generar un certificado de nómina?
- ¿Qué criterios debo seguir para configurar un informe?
- ¿Es posible personalizar los informes que genero?
- ¿Cómo puedo visualizar un informe después de crearlo?
- ¿Dónde encuentro la opción para retornar a la ventana anterior?
- ¿Qué debo hacer si necesito cancelar una operación en curso?
- ¿Los informes generados se pueden exportar a otros formatos?
- ¿Hay algún límite en la cantidad de certificados que puedo generar?

# Domain — data model

## Functional

El módulo se centra en la tabla ancla sscpr_reportcertificate, la cual almacena todos los datos necesarios para generar los certificados de nómina. Este módulo no presenta etapas complejas ni relaciones adicionales con otras tablas, lo que simplifica su gestión. Sin embargo, es importante destacar que, aunque no existen triggers y funciones PL asociadas directamente a este módulo, la estructura de la tabla permite realizar estadísticas sobre los informes generados, garantizando la integridad y disponibilidad de la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sscpr_reportcertificate` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sscpr_reportcertificate` | sscpr_reportcertificate | — | — | ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `sscpr_reportcertificate_key`; Cols: value, name, c_doctype_id, description, format; `SSCPR_REPORTCERTIFICATE_ISACT`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sscpr_reportcertificate` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo cuenta con una ventana principal llamada 'Configuration Report Certificate', donde los usuarios pueden interactuar para configurar y generar informes. La navegación en esta ventana es intuitiva, facilitando la selección de criterios para la generación de certificados, aunque solo hay una ventana disponible, lo que centraliza la funcionalidad de informes en este punto.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.payroll.reports.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuration Report Certificate | Configuration Report Certificate |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuracion Reportes de Certificado | Configuration Report Certificate | No |
| Nómina General por Departamento | General Payroll For Department | No |
| Reporte Certificado de Trabajo | Report Job Cetificate | No |
| Reporte Detalle Roles Individuales | Individual Roles Detail Report | No |
| Reporte rol histórico detallado | Reporte Nomina General Detallada | No |
| Rol Nómina Histórico Totalizado | Totalized Historical Payroll Role | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.payroll.reports.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuration Report Certificate

- **AD_WINDOW_ID:** `4349ECB37BBF4CD4832FC3192DAFC412`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Configuration Report Certificate | `5D4B5ABA21A64BD08E4A892B8918C14A` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Configuration Report Certificate (ventana: Configuration Report Certificate)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Document Type | `C_Doctype_ID` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Format | `Format` | No | No | — |
| 80 | Footer | `Footer` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dentro del módulo, se ofrecen cinco botones típicos para llevar a cabo operaciones sobre los informes de nómina. Estos botones incluyen opciones como 'Completar' para finalizar la configuración del informe, 'Retornar' para volver a la ventana anterior y 'Rechazar' para cancelar acciones en curso. Aunque no se generan informes específicos directamente desde el módulo, el sistema permite almacenar configuraciones previas para su uso en futuros períodos. Las validaciones frecuentes aseguran que se cumplan los criterios establecidos al momento de generar certificados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.payroll.reports.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Nómina General por Departamento | General Payroll For Department | General Payroll For Department | *(OBUIAPP / manual)* | General Payroll For Department | — |
| Proceso / otro | Reporte Certificado de Trabajo | Report Job Cetificate | Report Job Cetificate | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Detalle Roles Individuales | Individual Roles Detail Report | Rpt_IndividualPayrollNomina | *(OBUIAPP / manual)* | Individual Roles Detail Report | — |
| Proceso / otro | Reporte rol histórico detallado | Detailed General Payroll | Rpt_DetailedGeneralPayroll | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Rol Nómina Histórico Totalizado | Totalized Historical Payroll Role | Totalized Historical Payroll Role | *(OBUIAPP / manual)* | Totalized Historical Payroll Role | — |
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
| Proceso / otro | Nómina General por Departamento | General Payroll For Department | General Payroll For Department | *(OBUIAPP / manual)* | General Payroll For Department | — |
| Proceso / otro | Reporte Certificado de Trabajo | Report Job Cetificate | Report Job Cetificate | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Reporte Detalle Roles Individuales | Individual Roles Detail Report | Rpt_IndividualPayrollNomina | *(OBUIAPP / manual)* | Individual Roles Detail Report | — |
| Proceso / otro | Reporte rol histórico detallado | Detailed General Payroll | Rpt_DetailedGeneralPayroll | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Rol Nómina Histórico Totalizado | Totalized Historical Payroll Role | Totalized Historical Payroll Role | *(OBUIAPP / manual)* | Totalized Historical Payroll Role | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Nómina General por Departamento | General Payroll For Department | — | General Payroll For Department | — |
| Proceso / otro | Reporte Certificado de Trabajo | Report Job Cetificate | — | — | — |
| Proceso / otro | Reporte Detalle Roles Individuales | Individual Roles Detail Report | — | Individual Roles Detail Report | — |
| Proceso / otro | Reporte rol histórico detallado | Detailed General Payroll | — | — | — |
| Proceso / otro | Rol Nómina Histórico Totalizado | Totalized Historical Payroll Role | — | Totalized Historical Payroll Role | — |
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
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

Este módulo no utiliza clases Java, por lo que no hay desarrollo específico requerido en este sentido, manteniendo la funcionalidad de informes a través de la lógica de la base de datos y las interacciones de usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.payroll.reports`.

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
| AD_VAL_RULE | — | `SSCPR_Logged User` | `ad_user.ad_user_id =@#ad_user_id@` |
| AD_VAL_RULE | — | `CustomPayrall_IsEmployee` | `c_bpartner.isemployee='Y'` |
| AD_VAL_RULE | — | `DOCTYPE FOR REPORT CERTIFICATE` | `C_DOCTYPE.C_DOCTYPE_ID IN (SELECT DISTINCT C_DOCTYPE_ID FROM C_DOCTYPE WHERE AD_TABLE_ID = '5D4B5ABA21A64BD08E4A892B8918` |
| AD_VAL_RULE | — | `sscpr_bpartner` | `c_bpartner.isemployee='Y'` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

En este módulo, los triggers y las funciones PL no tienen un rol activo, ya que los procesos se manejan directamente a través de la interfaz de usuario. La gestión de estos aspectos se centra en la tabla ancla, optimizando el rendimiento sin necesidad de utilizar lógica de base de datos adicional, lo que simplifica la estructura del módulo.

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

Módulo: `ec.com.sidesoft.custom.payroll.reports`.

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

# Glosario — prefijo `SSCPR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSCPR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.payroll.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `General Payroll For Department` — Nómina General por Departamento
- `Report Job Cetificate` — Reporte Certificado de Trabajo
- `Rpt_IndividualPayrollNomina` — Reporte Detalle Roles Individuales
- `Rpt_DetailedGeneralPayroll` — Reporte rol histórico detallado
- `Totalized Historical Payroll Role` — Rol Nómina Histórico Totalizado

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Payroll - Sent Mail
**Package:** `ec.com.sidesoft.custom.payroll.sentmail`

# Module overview — Payroll - Sent Mail

## Functional

El módulo 'Payroll - Sent Mail' está diseñado para la gestión y seguimiento del envío de correos electrónicos relacionados con nóminas en la plataforma Openbravo. Este módulo es utilizado principalmente por el departamento de recursos humanos y el equipo de administración de la nómina, quienes requieren verificar la correcta comunicación de la información salarial a los empleados. Su alcance se limita a la gestión del envío de correos y su integración con otros módulos, especialmente aquellos relacionados con la gestión de nómina. Dependencias clave incluyen: '2.50 to 3.00 Compatibility Skin', 'Core' y 'Human Resources Management - Payroll'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/payroll/sentmail` |
| Web | `web/ec.com.sidesoft.custom.payroll.sentmail/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPM`

# Guía de chat — Payroll - Sent Mail

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.payroll.sentmail`).

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

- ¿Cómo puedo confirmar que los correos de nómina se han enviado?
- ¿Qué hacer si un empleado no recibió su recibo de nómina?
- ¿Cómo puedo realizar un seguimiento de los correos enviados?
- ¿Hay un registro de correos que no han podido ser entregados?
- ¿Cómo puedo modificar la configuración de correo electrónico para el envío de nómina?
- ¿Existen informes sobre las entregas de correos de nómina?
- ¿Qué medidas tomar si un correo es devuelto?
- ¿Hay alguna validación para asegurar la correcta dirección de correo electrónico de los empleados?

# Domain — data model

## Functional

Este módulo interactúa principalmente con la tabla modificada 'SSPR_PAYROLL', que contiene los datos de la nómina que se pretende enviar por correo. Aunque no se especifican otras tablas físicas ni procesos adicionales, la estructura de este módulo se basa en facilitar el flujo de envío de la información de nómina a través de las herramientas de correo electrónico disponibles en Openbravo. No se especifican triggers ni funciones PL asociados, lo que sugiere que la lógica del módulo depende directamente de su capacidad de integración con el módulo de nómina ya existente.

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

`SSPR_PAYROLL`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no cuenta con ventanas específicas, lo que indica que probablemente se desarrolla como una funcionalidad integrada en el flujo general del módulo de nómina. Navegar la funcionalidad implicaría gestionar correctamente los correos electrónicos a través de la interfaz existente del módulo de recursos humanos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.payroll.sentmail.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.payroll.sentmail.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `746B6484EF2F4B7F9F4733CFE9638C41`

- **AD_TAB_ID:** `746B6484EF2F4B7F9F4733CFE9638C41` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 110 | Send Mail | `EM_Sspm_Sendmail` | No | No | — |
| 120 | Sent Mail | `EM_Sspm_Sentmail` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que no se detallan procesos, botones específicos o informes en el módulo, se sobreentiende que las acciones típicas pueden incluir confirmar el envío de correos, retornar correos rebotados o reportar problemas de entrega. Las validaciones frecuentes se centrarán en asegurar que la información enviada es la correcta y que los correos no son rechazados por su configuración o dirección.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.payroll.sentmail.es_ES/referencedata/translation/`.

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

No se incluye código Java específico para este módulo, lo que sugiere que la funcionalidad está implementada únicamente en el entorno de Openbravo sin clases adicionales asociadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.payroll.sentmail`.

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

Aunque el módulo no especifica triggers ni funciones PL, se puede inferir que en el contexto del soporte, se trabajará con la modificación de la tabla 'SSPR_PAYROLL' para asegurar que el estado de envío de los correos sea manejado adecuadamente. Esto implica que cualquier ajuste o mejora requerirá interacción con este modelo de base de datos.

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

Módulo: `ec.com.sidesoft.custom.payroll.sentmail`.

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

# Glosario — prefijo `SSPM`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPM` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.payroll.sentmail` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Payroll by Cost Center
**Package:** `ec.com.sidesoft.payroll.costcenter`

# Module overview — Payroll by Cost Center

## Functional

El módulo 'Payroll by Cost Center' permite procesar la nómina de los empleados según el centro de costos, así como dimensiones adicionales. Está diseñado principalmente para su uso por los departamentos de recursos humanos y de finanzas, donde los actores clave son los especialistas en nómina y los analistas de costos. El alcance de este módulo incluye el cálculo y la distribución de la nómina a nivel de cost center, además de sus respectivas dimensiones. Este módulo depende del módulo principal de 'Human Resources Management - Payroll' para su funcionamiento adecuado, integrando datos y procesos pertinentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payroll/costcenter` |
| Web | `web/ec.com.sidesoft.payroll.costcenter/` |

### Declared dependencies

- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPRC`

# Guía de chat — Payroll by Cost Center

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payroll.costcenter`).

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

- ¿Cómo puedo generar un informe de nómina por centro de costos?
- ¿Qué pasos debo seguir para corregir un error en un ticket de nómina?
- ¿Cómo puedo agregar una nueva dimensión a la nómina?
- ¿Dónde encuentro las configuraciones para los centros de costos?
- ¿Qué validaciones se realizan antes de procesar la nómina?
- ¿Puedo auditar los cambios realizados en los tickets de nómina?
- ¿Cómo se gestiona la importación de datos desde otros sistemas?
- ¿Qué hago si los montos de la nómina no coinciden con las expectativas?

# Domain — data model

## Functional

La entidad cabecera del módulo se basa en la tabla modificada 'SSPR_PAYROLL_TICKET', que guarda información relacionada con los salarios y los centros de costos. Aunque no se especifican tablas adicionales de etapas en este inventario, la relación entre la nómina y los centros de costos se establece a través de la configuración en el sistema. Un trigger clave, 'SPRC_AMOUNT_CONCEPT_TRG', asegura la correcta actualización de los montos en la tabla correspondiente a los conceptos de nómina, invocando rutinas PL/pgSQL para mantener la integridad de los datos.

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

`SSPR_PAYROLL_TICKET`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no contiene ventanas específicas definidas en este inventario; sin embargo, se puede acceder a las funcionalidades a través de las interfaces disponibles en el módulo de nómina de recursos humanos. Los usuarios navegarán por el sistema habitual de Openbravo, utilizando las opciones del menú para ejecutar procesos relacionados con la payroll según las necesidades del centro de costos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payroll.costcenter.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payroll.costcenter.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `92F08CF4C33445AA921728AD1F73D19E`

- **AD_TAB_ID:** `92F08CF4C33445AA921728AD1F73D19E` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 200 | Cost Center | `EM_Sprc_Costcenter_ID` | No | No | — |
| 210 | 1st Dimension | `EM_Sprc_User1_ID` | No | Sí | — |
| 230 | Accounting Category | `EM_Sprc_Cat_Acct_ID` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo carece de botones de proceso definidos, pero se hacen necesarios informes y validaciones para garantizar la precisión en el cálculo de la nómina. Cuando se procesa la nómina, es común utilizar informes para verificar la correcta distribución entre los distintos centros de costos y dimensiones antes de la finalización del proceso. Las validaciones frecuentes incluyen la revisión de entradas erróneas en los tickets de nómina y la consistencia de datos entre los centros de costos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payroll.costcenter.es_ES/referencedata/translation/`.

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
**Total de reportes del módulo: 10**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **0**; archivos `*.jrxml` en el repo = **10**.

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

El módulo no incluye clases de Java, por lo que el enfoque se centra en el desarrollo en PL/pgSQL para manejar la lógica del negocio relacionada con el procesamiento de nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payroll.costcenter`.

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
| Trigger `SPRC_AMOUNT_CONCEPT_TRG` | `sspr_concept_amount` | after INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Función PL `sprc_automatic_payroll_process` | — | invocación proceso | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA |
| Función PL `sprc_process_payroll` | — | invocación proceso | Ya existen nóminas superiores a fecha de proceso; Imposible desprocesar, vacacaciones calculadas a la fecha; ERROR= EXISTE CONFIGURADO MAS DE UN CONCEPTO PARA DIAS LABORADOS |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers, como 'SPRC_AMOUNT_CONCEPT_TRG', juegan un rol crucial en la base de datos al asegurar que los cálculos de nómina sean precisos y que los registros se actualicen correctamente. Las funciones PL/pgSQL proporcionan la lógica necesaria para manejar operaciones complejas dentro del módulo, facilitando así el soporte técnico necesario cuando surgen problemas en la contabilidad de la nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SPRC_AMOUNT_CONCEPT_TRG` | `sspr_concept_amount` | after | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPRC_AMOUNT_CONCEPT_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sprc_automatic_payroll_process` | — | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA; RECUPERA INSTANCIA PARA DESPROCESAR NOMINAS | Obtengo el periodo de las nomina a procesar; CREA INSTANCIA PARA VACACIONES P_INSTANCE AND P_INSTANCE_PARA; VALIDA QUE NO EXISTA NINGUNA NOMINA CONTABILIZADA; RECUPERA INSTANCIA PARA DESPROCESAR NOMINAS; PERFORM SSPR_CALCULATEVACATION(v_pinstance_vac_id);; RECUPERA ERROR DE LA FUNCION SPRC_PROCESS_PAYROLL | `model/functions/SPRC_AUTOMATIC_PAYROLL_PROCESS.xml` |
| `sprc_process_payroll` | — | Ya existen nóminas superiores a fecha de proceso; Imposible desprocesar, vacacaciones calculadas a la fecha; ERROR= EXISTE CONFIGURADO MAS DE UN CONCEPTO PARA DIAS LABORADOS; 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL A… | Ya existen nóminas superiores a fecha de proceso; Imposible desprocesar, vacacaciones calculadas a la fecha; ERROR= EXISTE CONFIGURADO MAS DE UN CONCEPTO PARA DIAS LABORADOS; 2 NO HAY TIPO DE DOCUMENTO PARA GENERAR EL ASIENTO; OBTENGO DATOS DE LA NOMINA - PERIODO, ESTADO; ELIMINAR RASTROS DEL FONDO DE RESERVA IESS | `model/functions/SPRC_PROCESS_PAYROLL.xml` |
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

Módulo: `ec.com.sidesoft.payroll.costcenter`.

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

# Glosario — prefijo `SPRC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPRC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payroll.costcenter` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Payroll Events
**Package:** `ec.com.sidesoft.payroll.events`

# Module overview — Sidesoft Payroll Events

## Functional

El módulo Sidesoft Payroll Events permite gestionar eventos relacionados con la nómina de una organización. Está diseñado para ser utilizado por usuarios de negocio encargados de la administración de nómina, así como por personal de soporte y desarrolladores que requieren interactuar con la lógica interna del módulo. El alcance incluye la creación, configuración y auditoría de novedades en la nómina, así como la gestión de dichas novedades en tiempo real. Este módulo depende de la compatibilidad con el '2.50 to 3.00 Compatibility Skin' y posee diversas ventanas y funciones que permiten su utilización completa.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payroll/events` |
| Web | `web/ec.com.sidesoft.payroll.events/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPEV`

# Guía de chat — Sidesoft Payroll Events

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payroll.events`).

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
- «¿Qué es la tabla spev_detail_news?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar una nueva novedad en la nómina?
- ¿Qué debo hacer si mi novedad fue rechazada?
- ¿Cómo se auditan las novedades registradas?
- ¿Qué significa cada estado de las novedades?
- ¿Puedo modificar una novedad una vez registrada?
- ¿Cómo se configuran las diferentes plantillas de auditoría?
- ¿Dónde encuentro la configuración del inventario faltante?
- ¿Qué acciones puedo realizar desde la ventana de Configuración de Novedades?

# Domain — data model

## Functional

El modelo de datos se centra en entidades como 'spev_register_news' que actúan como cabecera para registrar novedades y 'spev_detail_news' que gestiona los detalles de cada novedad. Las relaciones están bien definidas: por ejemplo, 'spev_register_news' tiene asociadas múltiples líneas a través de 'spev_register_newsline'. Los triggers como 'SPEV_REGISTERNEWS_TRG' y 'SPEV_DETAIL_NEWS_TRG' se utilizan para implementar lógica de negocio en los eventos de inserción o actualización, asegurando la integridad de los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `spev_audit_detail` |
| `spev_config_iauditor` |
| `spev_config_inventory` |
| `spev_config_news` |
| `spev_config_newsline` |
| `spev_config_template` |
| `spev_detail_news` |
| `spev_maintenance_news` |
| `spev_product_category` |
| `spev_register_news` |
| `spev_register_newsline` |
| `spev_temp_auditor` |
| `spev_temp_inventory` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `spev_audit_detail` | SPEV_Audit_Detail | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; spev_detail_news_id→spev_detail_news; spev_maintenance_news_id→spev_maintenance_news (+1) | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `spev_audit_detail_key`; Cols: value_old, value_new, user_modified_id, spev_maintenance_news_id, c_bpartner_id; `SPEV_AUD_DETA_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `spev_config_iauditor` | SPEV_Config_Iauditor | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Parametrización / catálogo de soporte. | PK `spev_config_iauditor_key`; Cols: urlbase, token; `SPEV_CONFIA_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `spev_config_inventory` | SPEV_Config_Inventory | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Parametrización / catálogo de soporte. | PK `spev_config_inventory_key`; Cols: urlbase, last_date_processed; `SPEV_CONFINV_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `spev_config_news` | SPEV_Config_News | — | `C_GLITEM_ID` (c_glitem_id, spev_maintenance_news_id) | ad_client_id→ad_client; spev_maintenance_news_id→spev_maintenance_news; c_glitem_id→c_glitem; sspr_concept_id→sspr_concept; ad_org_id→ad_org | Parametrización / catálogo de soporte. | PK `spev_config_news_key`; Cols: spev_maintenance_news_id, c_glitem_id, sspr_concept_id, percentage, boss; `SPEV_CONF_NEW_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `spev_config_newsline` | SPEV_Config_Newsline | — | — | ad_client_id→ad_client; spev_config_news_id→spev_config_news; ad_org_id→ad_org | Parametrización / catálogo de soporte. | PK `spev_config_newsline_key`; Cols: startp, endp, percentage, type, value; `SPEV_CONF_NEWLI_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `spev_config_template` | SPEV_Config_Template | — | `SPEV_CONFIG_TEMPLATE_VALUE` (value) | ad_client_id→ad_client; ad_org_id→ad_org | Parametrización / catálogo de soporte. | PK `spev_config_template_key`; Cols: value, name, type; `SPEV_CONFTEM_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `spev_detail_news` | SPEV_Detail_News | `SPEV_AUDIT_DETAIL_TRG`; `SPEV_DETAIL_NEWS_TRG` | — | ad_client_id→ad_client; c_bpartner_id→c_bpartner; c_period_id→c_period; c_costcenter_id→c_costcenter; c_glitem_id→c_glitem (+4) | Detalle enlazado a ad_client, c_bpartner, c_period. Validado por trigger(s): SPEV_AUDIT_DETAIL_TRG, SPEV_DETAIL_NEWS_TRG. | PK `spev_detail_news_key`; Cols: date_detail, doumentno, c_bpartner_id, spev_config_news_id, value; `SPEV_DETA_NEW_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); idx `SPEV_DETAIL_NEWS_COMB` (c_bpartner_id, c_period_id); idx `SPEV_DETAIL_NEWS_COMB1` (c_bpartner_id, c_period_id, sspr_concept_id) (+2) |
| `spev_maintenance_news` | SPEV_Maintenance_News | — | `SPEV_MAIN_NEW_SEARCH_KEY` (ad_client_id, search_key) | ad_client_id→ad_client; sspr_concept_id→sspr_concept; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sspr_concept. | PK `spev_maintenance_news_key`; Cols: description, search_key, sspr_concept_id, valid, formula; `SPEV_MAIN_NEW_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `spev_product_category` | SPEV_Product_Category | — | — | ad_client_id→ad_client; ad_org_id→ad_org; m_product_id→m_product; spev_config_news_id→spev_config_news | Detalle enlazado a ad_client, ad_org, m_product. | PK `spev_product_category_key`; Cols: product_type, m_product_id, spev_config_news_id; `SPEV_PRO_CAT_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `spev_register_news` | SPEV_Register_News | `SPEV_DATECONTROL_TRG`; `SPEV_REGISTERNEWS_TRG` | — | c_doctypetarget_id→c_doctype; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_doctype. Validado por trigger(s): SPEV_DATECONTROL_TRG, SPEV_REGISTERNEWS_TRG. | PK `spev_register_news_key`; Cols: date_register, observations, state, processed, doumentno; `SPEV_REGIS_NEWS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `spev_register_newsline` | SPEV_Register_Newsline | `SPEV_REGISTERNEWSLINE_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; spev_maintenance_news_id→spev_maintenance_news; spev_register_news_id→spev_register_news | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SPEV_REGISTERNEWSLINE_TRG. | PK `spev_register_newsline_key`; Cols: spev_register_news_id, c_bpartner_id, spev_maintenance_news_id, value; `SPEV_REGIS_NEWSLI_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `spev_temp_auditor` | SPEV_Temp_Auditor | — | — | ad_client_id→ad_client; ad_org_id→ad_org; spev_config_template_id→spev_config_template | Detalle enlazado a ad_client, ad_org, spev_config_template. | PK `spev_temp_auditor_key`; Cols: spev_config_template_id, percentage, audit_date, start_date, end_date; `SPEV_TEMP_AU_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `spev_temp_inventory` | SPEV_Temp_Inventory | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; c_costcenter_id→c_costcenter | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `spev_temp_inventory_key`; Cols: c_bpartner_id, c_costcenter_id, processed_date, processed; `SPEV_TEMP_IN_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SPEV_Audit_Detail` |
| `SPEV_Config_Iauditor` |
| `SPEV_Config_Inventory` |
| `SPEV_Config_News` |
| `SPEV_Config_Newsline` |
| `SPEV_Config_Template` |
| `SPEV_Detail_News` |
| `SPEV_Maintenance_News` |
| `SPEV_Product_Category` |
| `SPEV_Register_News` |
| `SPEV_Register_Newsline` |
| `SPEV_Temp_Auditor` |
| `SPEV_Temp_Inventory` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ORG`, `C_BPARTNER`, `C_INVOICE`, `C_ORDER`, `FIN_FINACC_TRANSACTION`, `M_PRODUCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación dentro del módulo Sidesoft Payroll Events se realiza a través de varias ventanas clave como 'Novedades', 'Registro de Novedades' y 'Detalle de Novedades'. Cada ventana ofrece funcionalidades específicas que permiten a los usuarios gestionar las novedades de la nómina y acceder a auditorías y configuraciones relevantes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payroll.events.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Auditoría Detalle de Novedades | Detail Payroll Events Audit |
| Configuración de Novedades | Configuration Payroll Events |
| Configuración iAuditor | Configuration iAuditor |
| Configuración Inventario Faltante | Configuration Missing Inventory |
| Configuración Plantilla iAuditor | Configuration iAuditor Template |
| Detalle de Novedades | Detail Payroll Events |
| Novedades | Payroll Event |
| Registro de Novedades | Register Payroll Events |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Auditoría Detalle de Novedades | Detail Payroll Events Audit | No |
| Configuración | Setup | Sí |
| Configuración de Novedades | Configuration Payroll Events | No |
| Configuración iAuditor | Configuration iAuditor | No |
| Configuración Inventario Faltante | Configuration Missing Inventory | No |
| Configuración Plantilla iAuditor | Configuration iAuditor Template | No |
| Detalle de Novedades | Detail Payroll Events | No |
| Herramientas de análisis | Analysis Tools | Sí |
| Novedades | Payroll Event | No |
| Novedades | Payroll Events | Sí |
| Procesar Ajuste de Inventario | Procesar Ajuste de Inventario | No |
| Registro de Novedades | Register Payroll Events | No |
| Transacciones | Transactions | Sí |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payroll.events.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Auditoría Detalle de Novedades

- **AD_WINDOW_ID:** `621228FA11414B41B0FC7867DB7D6AB4`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Detail Payroll Events Audit | `44A6474BB0CF4BFEAC6012D51A1BA044` | 0 |

### Ventana: Configuración de Novedades

- **AD_WINDOW_ID:** `14EBADA66F2446BDA6C03B5F8E62809D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Configuration Payroll Events | `2A5C9CB6882342FF850CB5236A4D16D3` | 0 |
| 20 | Lines | `993D142153994CFB93A7C7F6DA1CC091` | 1 |
| 30 | Category of Products | `4FAFD506883B4446A0DCE89297DD4E49` | 1 |

### Ventana: Configuración iAuditor

- **AD_WINDOW_ID:** `34DE02B97801400C95AD1A105FBC3E84`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Configuration iAuditor | `3378F06E603749C791394AE7BDF65EBE` | 0 |

### Ventana: Configuración Inventario Faltante

- **AD_WINDOW_ID:** `15654F6EA31A454AA9E32DB0D7E8BA00`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Configuration Missing Inventory | `6DEEC22BEDC64C0CAABD748175A74375` | 0 |

### Ventana: Configuración Plantilla iAuditor

- **AD_WINDOW_ID:** `A2BB1F2D69BB4173A9FB559BC5CCE6D2`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Configuration iAuditor Template | `14DD4E0D1F544F559BB23890A219C2D8` | 0 |

### Ventana: Detalle de Novedades

- **AD_WINDOW_ID:** `7F08515965D548FBB330E6223E79503D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Detail Payroll Events | `12752CE34E264E9EA5F260C9A7C0FB7F` | 0 |

### Ventana: Novedades

- **AD_WINDOW_ID:** `315E4E8F2DD04B3C9091E8592E2CE53B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Payroll Event | `849C5044484B48E9B62E89BB631F27F3` | 0 |

### Ventana: Registro de Novedades

- **AD_WINDOW_ID:** `EE5CB3579C7144D5AC43EF7D6D369850`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Register Payroll Events | `C43E09B0BB994421AE2AFEE113015B76` | 0 |
| 20 | Lines | `51444C43CC7A46FFB4FF94901A33D513` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `143`

- **AD_TAB_ID:** `143` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 640 | EM_Spev_C_Costcenter_ID | `EM_Spev_C_Costcenter_ID` | No | No | — |

### Pestaña `180`

- **AD_TAB_ID:** `180` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 598 | Discountable | `EM_Spev_Discountable` | No | No | — |

### Configuration Payroll Events (ventana: Configuración de Novedades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | News | `Spev_Maintenance_News_ID` | No | No | — |
| 40 | Accounting Concept | `C_Glitem_ID` | No | No | — |
| 50 | Work Concept | `Sspr_Concept_ID` | No | No | — |
| 60 | Percentage | `Percentage` | No | No | — |
| 70 | Boss | `Boss` | No | No | — |
| 80 | Value | `Value` | No | No | — |
| 90 | Start Day | `Start_Day` | No | No | — |
| 100 | End Day | `END_Day` | No | No | — |
| 110 | Function | `Function` | No | No | — |
| 120 | Active | `Isactive` | No | No | — |
| 130 | Utilities | `Utilities` | No | No | — |

### Lines (ventana: Registro de Novedades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 50 | News | `Spev_Maintenance_News_ID` | No | No | — |
| 60 | Value | `Value` | No | No | — |

### Lines (ventana: Configuración de Novedades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Start | `Startp` | No | No | — |
| 40 | End | `Endp` | No | No | — |
| 50 | Percentage | `Percentage` | No | No | — |
| 60 | Type | `Type` | No | No | — |
| 70 | Value | `Value` | No | No | — |

### Configuration Missing Inventory (ventana: Configuración Inventario Faltante)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Base URL | `Urlbase` | No | No | — |
| 30 | Last Date Processed | `Last_Date_Processed` | No | Sí | — |
| 40 | Active | `Isactive` | No | No | — |

### Payroll Event (ventana: Novedades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Search Key | `Search_Key` | No | No | — |
| 30 | Name | `Description` | No | No | — |
| 60 | Insert Value | `Valid` | No | No | — |
| 70 | Show News | `Formula` | No | No | — |

### Category of Products (ventana: Configuración de Novedades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Product Category | `Product_Type` | No | No | — |
| 40 | Products | `M_Product_ID` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Register Payroll Events (ventana: Registro de Novedades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 15 | Transaction Document | `C_Doctypetarget_ID` | No | Sí | — |
| 20 | Document Number | `Doumentno` | No | Sí | — |
| 30 | Date | `Date_Register` | No | No | — |
| 35 | State | `State` | No | Sí | — |
| 40 | Observations | `Observations` | No | No | — |
| 160 | Process | `Processed` | No | No | — |

### Configuration iAuditor Template (ventana: Configuración Plantilla iAuditor)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Name | `Name` | No | No | — |
| 30 | Template ID | `Value` | No | No | — |
| 50 | Template Type | `Type` | No | No | — |
| 60 | Active | `Isactive` | No | No | — |

### Configuration iAuditor (ventana: Configuración iAuditor)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Base URL | `Urlbase` | No | No | — |
| 40 | Authorization Token | `Token` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Pestaña `AE4D0B14798E47A5B0CEF62C52DB235B`

- **AD_TAB_ID:** `AE4D0B14798E47A5B0CEF62C52DB235B` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 415 | Local | `EM_Spev_Local` | No | No | C1CE792930674D08832CCFCACAE3F1AC |
| 420 | Type | `EM_Spev_Type` | No | No | 800000 |
| 421 | EM_Spev_Type_Labor | `EM_Spev_Type_Labor` | No | No | — |

### Detail Payroll Events (ventana: Detalle de Novedades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Date | `Date_Detail` | No | Sí | — |
| 40 | Document Number | `Doumentno` | No | Sí | — |
| 45 | Order Number | `Order_Number` | No | Sí | — |
| 46 | Cash | `C_Glitem_ID` | No | Sí | — |
| 47 | Reference | `C_Costcenter_ID` | No | Sí | — |
| 50 | Employee | `C_Bpartner_ID` | No | Sí | — |
| 60 | News | `Spev_Maintenance_News_ID` | No | Sí | — |
| 70 | Value | `Value` | No | No | — |
| 80 | Work Concept | `Sspr_Concept_ID` | No | Sí | — |
| 90 | Type | `Concept_Type` | No | Sí | — |
| 100 | Process | `Process` | No | Sí | — |
| 110 | State | `Type` | No | Sí | — |
| 130 | Period | `C_Period_ID` | No | Sí | — |

### Detail Payroll Events Audit (ventana: Auditoría Detalle de Novedades)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Spev_Detail_News_ID | `Spev_Detail_News_ID` | No | Sí | — |
| 30 | Old Value | `Value_Old` | No | No | — |
| 40 | New Value | `Value_New` | No | No | — |
| 50 | User that Modifies | `User_Modified_ID` | No | No | — |
| 60 | News | `Spev_Maintenance_News_ID` | No | Sí | — |
| 70 | Employee | `C_Bpartner_ID` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos en este módulo incluyen operaciones típicas como 'Completar', 'Retornar' y 'Rechazar' novedades. Para obtener un estado actualizado de la nómina, se cuenta con procesos que validan las novedades antes de su procesamiento final. Aunque no se especifican informes adicionales, los usuarios pueden esperar validaciones frecuentes relacionadas con el estado y la configuración de las novedades registradas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payroll.events.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Procesar Ajuste de Inventario | Procesar Ajuste de Inventario | Procesar Ajuste de Inventario | Java `PayrollEventsMissingInventoryDaily` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `fecha` | `src/ec/com/sidesoft/payroll/events/ad_process/PayrollEventsMissingInventoryDaily.java` |
| Botón (PL/pgSQL) | Procesar Novedad | Process News | SPEV_RegisterProcess | `spev_payroll_events` | Process News | — |
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
| Background | Proceso de background de novedades | Payroll Events Background  Process | PayrollEventsBackground | *(OBUIAPP / manual)* | Payroll Events Background  Process | — |
| Background | Proceso de background de novedades mensual | Payroll Events Background  Process Month | PayrollEventsBackgroundMonth | *(OBUIAPP / manual)* | Payroll Events Background  Process Month | — |
| Background | Proceso de background del Bono Checklist | Payroll Events Background Process Bonus Cheklist | PayrollEventsBackgroundChecklistBonus | *(OBUIAPP / manual)* | — | — |
| Background | Proceso de background Faltante Inventario | Payroll Events Background Process Missing Inventory | PayrollEventsMissingInventory | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Procesar Ajuste de Inventario | `PayrollEventsMissingInventoryDaily` | Proceso Java (toolbar/background) | `fecha` | — | `src/ec/com/sidesoft/payroll/events/ad_process/PayrollEventsMissingInventoryDaily.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Procesar Ajuste de Inventario | Procesar Ajuste de Inventario | Procesar Ajuste de Inventario | Java `PayrollEventsMissingInventoryDaily` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `fecha` | `src/ec/com/sidesoft/payroll/events/ad_process/PayrollEventsMissingInventoryDaily.java` |
| Botón (PL/pgSQL) | Procesar Novedad | Process News | SPEV_RegisterProcess | `spev_payroll_events` | Process News | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Procesar Ajuste de Inventario | Procesar Ajuste de Inventario | Java `PayrollEventsMissingInventoryDaily` | Proceso Openbravo registro `fecha` | Proceso Openbravo registro `fecha` |
| Botón (PL/pgSQL) | Procesar Novedad | Process News | PL `spev_payroll_events` | Process News | — |
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
| `SPEV_is_processed` | The registration has already been processed. | The registration has already been processed. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPEV_process_fail` | Process failed | Process failed | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPEV_Not_deleted` | Record can not be deleted | Record can not be deleted | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Spev_DateRange` | Date out of range. | Date out of range. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPEV_process_success` | Process completed successfully | Process completed successfully | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo también incorpora clases Java que proporcionan funcionalidades adicionales, como el manejo de eventos al registrar novedades y la actualización de valores en tiempo real utilizando la lógica de negocio definida en las clases de llamada. Esto permite la integración eficaz entre la UI y la lógica del negocio.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payroll.events`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `RegisterNewsDocType` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/payroll/events/ad_callouts/RegisterNewsDocType.java` |
| `UpdateValuePayrollEvent` | ad_callouts | SimpleCallout | Event handler | `src/ec/com/sidesoft/payroll/events/ad_callouts/UpdateValuePayrollEvent.java` |
| `PayrollEventsMissingInventoryDaily` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/payroll/events/ad_process/PayrollEventsMissingInventoryDaily.java` |
| `ProcessPayrollEvent` | ad_process | BaseProcessActionHandler | Proceso / informe Java | `src/ec/com/sidesoft/payroll/events/ad_process/ProcessPayrollEvent.java` |
| `PayrollEventsBackground` | background | DalBaseProcess | Event handler | `src/ec/com/sidesoft/payroll/events/background/PayrollEventsBackground.java` |
| `PayrollEventsBackgroundMonth` | background | DalBaseProcess | Event handler | `src/ec/com/sidesoft/payroll/events/background/PayrollEventsBackgroundMonth.java` |
| `PayrollEventsChecklistBonus` | background | DalBaseProcess | Event handler | `src/ec/com/sidesoft/payroll/events/background/PayrollEventsChecklistBonus.java` |
| `PayrollEventsMissingInventory` | background | DalBaseProcess | Event handler | `src/ec/com/sidesoft/payroll/events/background/PayrollEventsMissingInventory.java` |
| `UpdateSequenceSPEVRegisterNewsVoided` | event | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/payroll/events/event/UpdateSequenceSPEVRegisterNewsVoided.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SPEV_AUDIT_DETAIL_TRG` | `spev_detail_news` | after UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPEV_DATECONTROL_TRG` | `spev_register_news` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPEV_DETAIL_NEWS_TRG` | `spev_detail_news` | after UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPEV_REGISTERNEWSLINE_TRG` | `spev_register_newsline` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPEV_REGISTERNEWS_TRG` | `spev_register_news` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPEV_VAL_PRINTTYPE` | `sspr_concept` | before INSERT/UPDATE | Solo puede contar con un Concepto laboral Tipo "Falta injustificada". |
| AD_VAL_RULE | — | `SPEV_DocTypeRegisterNews` | `C_DocType.DocBaseType IN ('SPEV_REGNEW') AND C_DocType.AD_Table_ID = 'C43E09B0BB994421AE2AFEE113015B76'` |
| AD_VAL_RULE | — | `Validate Payroll Events` | `SPEV_Maintenance_News.formula = 'Y'` |
| AD_VAL_RULE | — | `SPEV_ValidateEmployee` | `C_BPARTNER.ISEMPLOYEE = 'Y' and C_BPARTNER.isactive= 'Y' and C_BPARTNER.em_sspr_status= 'A' and C_BPARTNER.em_sspr_costc` |
| Java event/validator | `UpdateValuePayrollEvent` | persistencia/UI | *(leer `src/ec/com/sidesoft/payroll/events/ad_callouts/UpdateValuePayrollEvent.java`)* |
| Java event/validator | `PayrollEventsMissingInventoryDaily` | persistencia/UI | *(leer `src/ec/com/sidesoft/payroll/events/ad_process/PayrollEventsMissingInventoryDaily.java`)* |
| Java event/validator | `ProcessPayrollEvent` | persistencia/UI | *(leer `src/ec/com/sidesoft/payroll/events/ad_process/ProcessPayrollEvent.java`)* |
| Java event/validator | `PayrollEventsBackground` | persistencia/UI | *(leer `src/ec/com/sidesoft/payroll/events/background/PayrollEventsBackground.java`)* |
| Java event/validator | `PayrollEventsBackgroundMonth` | persistencia/UI | *(leer `src/ec/com/sidesoft/payroll/events/background/PayrollEventsBackgroundMonth.java`)* |
| Java event/validator | `PayrollEventsChecklistBonus` | persistencia/UI | *(leer `src/ec/com/sidesoft/payroll/events/background/PayrollEventsChecklistBonus.java`)* |
| Java event/validator | `PayrollEventsMissingInventory` | persistencia/UI | *(leer `src/ec/com/sidesoft/payroll/events/background/PayrollEventsMissingInventory.java`)* |
| Función PL `spev_cashmissing` | — | invocación proceso | BUSCO LAS CUENTAS CONTABLES QUE SEAN DE TIPO CAJA; BUSCO EN LAS LINEAS PARA CADA CABECERA DE TIPO CAJA LAS QUE TENGAN; EL CHECK DE PROCESADO EN N Y LAS QUE TENGAN |
| Función PL `spev_checklistbonus` | — | invocación proceso | VERIFICO QUE PARA LA CONFIGURACION DE BONOS CHECKLIST TENGA LINEAS CREADAS; SI TIENE LINEAS LA CONFIGURACION DE LOS BONOS CHECKLIST; BUSCO LOS EMPLEADOS QUE SEAN DE TIPO LOCAL Y QUE PERTENEZCAN AL CENTRO DE COSTO DE LA ORGANIZACION |
| Función PL `spev_events` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; |
| Función PL `spev_events_liquidation` | — | invocación proceso | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; |
| Función PL `spev_get_period` | — | invocación proceso | Recupero SOLO la fecha inicio y le resto 1 para encontrar la fecha fin. |
| Función PL `spev_missinginventory` | — | invocación proceso | CONTADORES DE LOS EMPLEADOS (JEFES Y SERVICIOS / PRODUCCION); V_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2--; VERIFICO QUE EXISTA CONFIGURACION PARA FALTANTE DE INVENTARIO |
| Función PL `spev_missinginventorydaily` | — | invocación proceso | CONTADORES DE LOS EMPLEADOS (JEFES Y SERVICIOS / PRODUCCION); V_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2--; VERIFICO QUE EXISTA CONFIGURACION PARA FALTANTE DE INVENTARIO |
| Función PL `spev_salesbonus` | — | invocación proceso | VERIFICO QUE PARA LA CONFIGURACION DE BONOS DE VENTAS; INICIO SI TIENE LINEAS LA CONFIGURACION DE LOS BONOS DE VENTAS; SI HAY UN PRESUPUESTO PARA EL AÑO EN CURSO |
| Función PL `spev_special_bonus_cc` | — | invocación proceso | SI HAY UN PRESUPUESTO PARA EL AÑO EN CURSO; INICIO SI LAS VENTAS CUMPLEN CON EL PRESUPUESTO; INICIO (MONTO FACTURA / NUMERO EMPLEADOS > UTILIDADES DE LA CONFIGURACION) |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL son críticos para el soporte del módulo, permitiendo que se ejecute la lógica de negocio automáticamente en respuesta a eventos en las bases de datos. Se cuenta con un total de seis triggers que gestionan desde auditorías hasta control de datos específicos en las tablas relevantes, asegurando que la información se mantenga coherente con las reglas establecidas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SPEV_AUDIT_DETAIL_TRG` | `spev_detail_news` | after | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPEV_AUDIT_DETAIL_TRG.xml` |
| `SPEV_DETAIL_NEWS_TRG` | `spev_detail_news` | after | UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPEV_DETAIL_NEWS_TRG.xml` |
| `SPEV_DATECONTROL_TRG` | `spev_register_news` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPEV_DATECONTROL_TRG.xml` |
| `SPEV_REGISTERNEWS_TRG` | `spev_register_news` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPEV_REGISTERNEWS_TRG.xml` |
| `SPEV_REGISTERNEWSLINE_TRG` | `spev_register_newsline` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPEV_REGISTERNEWSLINE_TRG.xml` |
| `SPEV_VAL_PRINTTYPE` | `sspr_concept` | before | INSERT/UPDATE | Solo puede contar con un Concepto laboral Tipo "Falta injustificada". | `model/triggers/SPEV_VAL_PRINTTYPE.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `spev_cashmissing` | — | BUSCO LAS CUENTAS CONTABLES QUE SEAN DE TIPO CAJA; BUSCO EN LAS LINEAS PARA CADA CABECERA DE TIPO CAJA LAS QUE TENGAN; EL CHECK DE PROCESADO EN N Y LAS QUE TENGAN; UN CONCEPTO CONTABLE ASOCIADO QUE ESTE ACTIVO EN LAS CO… | BUSCO LAS CUENTAS CONTABLES QUE SEAN DE TIPO CAJA; BUSCO EN LAS LINEAS PARA CADA CABECERA DE TIPO CAJA LAS QUE TENGAN; EL CHECK DE PROCESADO EN N Y LAS QUE TENGAN; UN CONCEPTO CONTABLE ASOCIADO QUE ESTE ACTIVO EN LAS CONFIGURACIONES; INICIO GUARDAR EN LA TABLA DETALLES DE NOVEDADES MULTA FALTANTE DE CAJA; FIN GUARDAR EN LA TABLA DETALLES DE NOVEDADES FALTANTE DE CAJA | `model/functions/SPEV_CASHMISSING.xml` |
| `spev_checklistbonus` | — | VERIFICO QUE PARA LA CONFIGURACION DE BONOS CHECKLIST TENGA LINEAS CREADAS; SI TIENE LINEAS LA CONFIGURACION DE LOS BONOS CHECKLIST; BUSCO LOS EMPLEADOS QUE SEAN DE TIPO LOCAL Y QUE PERTENEZCAN AL CENTRO DE COSTO DE LA… | VERIFICO QUE PARA LA CONFIGURACION DE BONOS CHECKLIST TENGA LINEAS CREADAS; SI TIENE LINEAS LA CONFIGURACION DE LOS BONOS CHECKLIST; BUSCO LOS EMPLEADOS QUE SEAN DE TIPO LOCAL Y QUE PERTENEZCAN AL CENTRO DE COSTO DE LA ORGANIZACION; POR CADA EMPLEADO SE VERIFICA QUE QUE EN EL PERIODO ANTERIOR HAYA TRABAJADO 30 DIAS; NOMINA > BOLETA DE NOMINA > DIAS LABORADOS => 30 DIAS; BUSCO EN LAS LINEAS DE LA CONFIGURACION DEL BONO CHECKLIT | `model/functions/SPEV_CHECKLISTBONUS.xml` |
| `spev_events` | — | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | `model/functions/SPEV_EVENTS.xml` |
| `spev_events_liquidation` | — | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | RAISE NOTICE '%','Updating PInstance - Processing ' || PInstance_ID ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_ResultStr) ; | `model/functions/SPEV_EVENTS_LIQUIDATION.xml` |
| `spev_get_costcenter` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SPEV_GET_COSTCENTER.xml` |
| `spev_get_period` | — | Recupero SOLO la fecha inicio y le resto 1 para encontrar la fecha fin. | Recupero SOLO la fecha inicio y le resto 1 para encontrar la fecha fin. | `model/functions/SPEV_GET_PERIOD.xml` |
| `spev_missinginventory` | — | CONTADORES DE LOS EMPLEADOS (JEFES Y SERVICIOS / PRODUCCION); V_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2--; VERIFICO QUE EXISTA CONFIGURACION PARA FALTANTE DE INVENTARIO; EMPLEADOS DE SERVICIO Y PRODUCCION, SE EXCLUYEN… | CONTADORES DE LOS EMPLEADOS (JEFES Y SERVICIOS / PRODUCCION); V_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2--; VERIFICO QUE EXISTA CONFIGURACION PARA FALTANTE DE INVENTARIO; EMPLEADOS DE SERVICIO Y PRODUCCION, SE EXCLUYEN LOS MOTORIZADOS; PORCENTAJE QUE SE TIENE QUE DESCONTAR AL JEFE; SE DIVIDE ENTRE EL NUMERO DE EMPLEADOS QUE SON JEFES | `model/functions/SPEV_MISSINGINVENTORY.xml` |
| `spev_missinginventorydaily` | — | CONTADORES DE LOS EMPLEADOS (JEFES Y SERVICIOS / PRODUCCION); V_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2--; VERIFICO QUE EXISTA CONFIGURACION PARA FALTANTE DE INVENTARIO; EMPLEADOS DE SERVICIO Y PRODUCCION, SE EXCLUYEN… | CONTADORES DE LOS EMPLEADOS (JEFES Y SERVICIOS / PRODUCCION); V_EMPLOYEE_ID VARCHAR(32); --OBTG:VARCHAR2--; VERIFICO QUE EXISTA CONFIGURACION PARA FALTANTE DE INVENTARIO; EMPLEADOS DE SERVICIO Y PRODUCCION, SE EXCLUYEN LOS MOTORIZADOS; PORCENTAJE QUE SE TIENE QUE DESCONTAR AL JEFE; SE DIVIDE ENTRE EL NUMERO DE EMPLEADOS QUE SON JEFES | `model/functions/SPEV_MISSINGINVENTORYDAILY.xml` |
| `spev_motorizedorder` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SPEV_MOTORIZEDORDER.xml` |
| `spev_processed_invoice` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SPEV_PROCESSED_INVOICE.xml` |
| `spev_salesbonus` | — | VERIFICO QUE PARA LA CONFIGURACION DE BONOS DE VENTAS; INICIO SI TIENE LINEAS LA CONFIGURACION DE LOS BONOS DE VENTAS; SI HAY UN PRESUPUESTO PARA EL AÑO EN CURSO; QUERY DE LAS FACTURAS Y LAS NOTAS DE CREDITO | VERIFICO QUE PARA LA CONFIGURACION DE BONOS DE VENTAS; INICIO SI TIENE LINEAS LA CONFIGURACION DE LOS BONOS DE VENTAS; SI HAY UN PRESUPUESTO PARA EL AÑO EN CURSO; QUERY DE LAS FACTURAS Y LAS NOTAS DE CREDITO; BUSCO EN LAS LINEAS DE LA CONFIGURACION PARA VERIFICAR EN QUE TIPO DE PORCENTAJE; SE ENCUENTRA EL PORCENTAJE DE CUMPLIMIENTO | `model/functions/SPEV_SALESBONUS.xml` |
| `spev_special_bonus_cc` | — | SI HAY UN PRESUPUESTO PARA EL AÑO EN CURSO; INICIO SI LAS VENTAS CUMPLEN CON EL PRESUPUESTO; INICIO (MONTO FACTURA / NUMERO EMPLEADOS > UTILIDADES DE LA CONFIGURACION); FIN SI LAS VENTAS CUMPLEN CON EL MPRESUPUESTO | SI HAY UN PRESUPUESTO PARA EL AÑO EN CURSO; INICIO SI LAS VENTAS CUMPLEN CON EL PRESUPUESTO; INICIO (MONTO FACTURA / NUMERO EMPLEADOS > UTILIDADES DE LA CONFIGURACION); FIN SI LAS VENTAS CUMPLEN CON EL MPRESUPUESTO; FIN SI HAY UN PRESUPUESTO PARA EL AÑO EN CURSO | `model/functions/SPEV_SPECIAL_BONUS_CC.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Procesar Ajuste de Inventario | `Procesar Ajuste de Inventario` | Botón (Java) | Java `PayrollEventsMissingInventoryDaily` | N | Proceso Openbravo registro `fecha` |
| 2 | Procesar Novedad | `SPEV_RegisterProcess` | Botón (PL/pgSQL) | PL `spev_payroll_events` | N | Process News |

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

Módulo: `ec.com.sidesoft.payroll.events`.

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

# Glosario — prefijo `SPEV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPEV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payroll.events` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `PayrollEventsBackground` — Proceso de background de novedades
- `PayrollEventsBackgroundMonth` — Proceso de background de novedades mensual
- `PayrollEventsBackgroundChecklistBonus` — Proceso de background del Bono Checklist
- `PayrollEventsMissingInventory` — Proceso de background Faltante Inventario
- `Procesar Ajuste de Inventario` — Procesar Ajuste de Inventario
- `SPEV_RegisterProcess` — Procesar Novedad

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Payroll IR
**Package:** `ec.com.sidesoft.payroll.ir`

# Module overview — Sidesoft Payroll IR

## Functional

El módulo Sidesoft Payroll IR es una herramienta diseñada para gestionar aspectos relacionados con la nómina y las obligaciones laborales en empresas. Está dirigido principalmente a usuarios de negocio encargados de la administración de recursos humanos y a desarrolladores que necesiten implementar o personalizar funcionalidades del ERP Openbravo. Su alcance se centra en la gestión eficiente de información de nómina, facilitando el cumplimiento de normativas laborales. Depende de la compatibilidad con el 'Core' de Openbravo y de un skin de compatibilidad entre las versiones 2.50 y 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payroll/ir` |
| Web | `web/ec.com.sidesoft.payroll.ir/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPIRT`

# Guía de chat — Sidesoft Payroll IR

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payroll.ir`).

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
- «¿Qué es la tabla spirt_familyload_config?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo agregar un nuevo empleado en el sistema?
- ¿Dónde encuentro la información sobre la carga familiar de un empleado?
- ¿Qué requisitos debo cumplir para realizar cambios en la nómina?
- ¿Qué debo hacer si detecto un error en la información salarial de un empleado?
- ¿El módulo calcula automáticamente las deducciones fiscales?
- ¿Cómo se actualiza la información de un empleado existente?
- ¿Es posible generar un reporte de nómina mensual?
- ¿Qué pasos seguir para eliminar un registro de empleado?

# Domain — data model

## Functional

El módulo cuenta con la tabla principal SSPR_COSTEMPLOYEE, que es utilizada para almacenar los datos relacionados con los empleados y sus cargas familiares. Aunque no hay un modelo complejo de etapas en este módulo, la gestión de la nómina se puede inferir en las relaciones entre las entidades y cómo se gestionan los datos de los empleados en función de sus cargas familiares. Actualmente, no se han definido triggers clave ni funciones PL dentro del módulo, lo que implica un diseño relativamente sencillo en cuanto a la interactividad y la manipulación de los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `spirt_familyload_config` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `spirt_familyload_config` | spirt_familyload_config | — | — | ad_client_id→ad_client; sspr_incometax_id→sspr_incometax; ad_org_id→ad_org | Parametrización / catálogo de soporte. | PK `spirt_flc_key`; Cols: family_load, basic_family_basket, total_personal_expenses, sspr_incometax_id; `SPIRT_FLC_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `spirt_familyload_config` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`SSPR_COSTEMPLOYEE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El usuario navega a través del módulo Sidesoft Payroll IR mediante la interfaz básica de Openbravo, donde se muestra información relacionada con la nómina de empleados. A pesar de que no se reportan ventanas específicas en este módulo, se puede acceder a los datos relevantes a través de las interfaces estándar del ERP, permitiendo visualizar, ingresar y editar información necesaria para el correcto funcionamiento del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payroll.ir.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payroll.ir.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `44876E0A506D4D81A39AB9BAC50AC349`

- **AD_TAB_ID:** `44876E0A506D4D81A39AB9BAC50AC349` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 90 | EM_Spirt_Familyloads | `EM_Spirt_Familyloads` | No | No | — |
| 100 | EM_Spirt_Catastr_Illness | `EM_Spirt_Catastr_Illness` | No | No | — |

### Family Load Config

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Family_Load | `Family_Load` | No | No | — |
| 50 | Basic_Family_Basket | `Basic_Family_Basket` | No | No | — |
| 60 | Total_Personal_Exepeses | `Total_Personal_Expenses` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que no se han definido botones de proceso, informes específicos o validaciones más complejas dentro del módulo, se espera que los usuarios realicen acciones básicas como agregar o modificar datos en la tabla SSPR_COSTEMPLOYEE. Las validaciones frecuentes pueden centrarse en asegurar que la información básica de cada empleado esté completa y sea coherente con las regulaciones laborales vigentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payroll.ir.es_ES/referencedata/translation/`.

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

El módulo no incluye clases Java, lo que implica que su funcionalidad se encuentra centrada en la manipulación directa de datos a través de la base de datos y la interfaz de usuario de Openbravo, sin agregar lógica adicional a través de programación en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payroll.ir`.

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

En el contexto de la base de datos, no se han implementado triggers ni funciones PL dentro de este módulo, lo que sugiere que las funcionalidades se manejan mayoritariamente a través de transacciones directas en la tabla de empleados. Esto simplifica el mantenimiento y soporte del módulo, aunque también puede limitar la automatización de ciertos procesos.

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

Módulo: `ec.com.sidesoft.payroll.ir`.

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

# Glosario — prefijo `SPIRT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPIRT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payroll.ir` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Overtime for Biometrical
**Package:** `ec.com.sidesoft.payroll.overtime`

# Module overview — Sidesoft Overtime for Biometrical

## Functional

El módulo Sidesoft Overtime for Biometrical tiene como objetivo gestionar el cálculo y autorización de horas extraordinarias de los empleados, permitiendo una administración efectiva del tiempo trabajado fuera del horario regular. Los actores principales incluyen los responsables de recursos humanos, los supervisores que autorizan las horas y los empleados que registran su tiempo. Este módulo es parte de un sistema mayor ERP que permite integrar la nómina con otros procesos empresariales como la gestión de personal y finanzas. Dependencias incluyen la compatibilidad con el '2.50 to 3.00 Compatibility Skin'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payroll/overtime` |
| Web | `web/ec.com.sidesoft.payroll.overtime/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPROV`

# Guía de chat — Sidesoft Overtime for Biometrical

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payroll.overtime`).

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
- «¿Qué es la tabla sprov_overtime?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar horas extraordinarias?
- ¿Qué debo hacer si mi solicitud de horas extras es rechazada?
- ¿Cómo se manejan las validaciones de horas extraordinarias?
- ¿Puedo modificar una solicitud ya enviada?
- ¿Qué información necesito para autorizar horas extraordinarias?
- ¿Dónde encuentro el historial de mis solicitudes de horas extras?
- ¿Hay un límite en el número de horas extraordinarias que puedo registrar?
- ¿Cómo se calculan las horas extraordinarias y cómo se reflejan en la nómina?

# Domain — data model

## Functional

La entidad central del módulo es la tabla 'sprov_overtime', que almacena información sobre las horas extraordinarias. Las principales relaciones se encuentran con las tablas relacionadas con los empleados, periodos y actividades planificadas. El flujo de datos comienza con la creación de registros de horas extraordinarias, los cuales pasan por etapas de autorización y validación. Se destacan triggers como 'SPROV_EMPLOYEE_OVERTIME_TRG' y 'SPROV_TOTALHOURS_TRG', que se encargan de la lógica de negocio, asegurando que el cálculo de horas sea preciso y se aplique correctamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sprov_employee` |
| `sprov_employee_overtime` |
| `sprov_extra_reason_maint` |
| `sprov_newness` |
| `sprov_overtime` |
| `sprov_overtime_line` |
| `sprov_overtime_type` |
| `sprov_period` |
| `sprov_planned_activity` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sprov_employee` | sprov_employee | `SPROV_EMPLOYEE_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sprov_period_id→sprov_period | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SPROV_EMPLOYEE_TRG. | PK `sprov_employee_key`; Cols: c_bpartner_id, description, sprov_period_id; `SPROV_EMPLOYEE_ACTIVE`: ISACTIVE IN ('Y', 'N') |
| `sprov_employee_overtime` | SPROV_Employee_Overtime | `SPROV_EMPLOYEE_OVERTIME_TRG` | — | ad_client_id→ad_client; c_bpartner_id→c_bpartner; ad_org_id→ad_org; sprov_extra_reason_maint_id→sprov_extra_reason_maint; sspr_shift_id→sspr_shift | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SPROV_EMPLOYEE_OVERTIME_TRG. | PK `sprov_empover_key`; Cols: identify, c_bpartner_id, datemovement, entry_1, exit_1; `SPROV_EMPOVER_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `sprov_extra_reason_maint` | SPROV_Extra_Reason_Maint | — | `SPROV_EXTREASON_VALUE` (ad_client_id, value) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sprov_extreason_key`; Cols: value, name, description; `SPROV_EXTREASON_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sprov_newness` | sprov_newness | `SPROV_NEWNESS_TRG` | — | ad_client_id→ad_client; sspr_concept_id→sspr_concept; sprbi_maintenance_news_id→sprbi_maintenance_news; ad_org_id→ad_org; sprov_employee_overtime_id→sprov_employee_overtime | Detalle enlazado a ad_client, sprbi_maintenance_news, sspr_concept. Validado por trigger(s): SPROV_NEWNESS_TRG. | PK `sprov_newness_id_key`; Cols: sprbi_maintenance_news_id, amount, sspr_concept_id, sprov_employee_overtime_id, processed; `SPROV_NEWNESS_ISACT`: ISACTIVE IN ('Y', 'N') |
| `sprov_overtime` | sprov_overtime | — | `SPROV_OVERTIME_UNIQ` (datemovement, sshr_department_id, c_city_id) | c_city_id→c_city; ad_client_id→ad_client; sshr_department_id→sshr_department; c_doctype_id→c_doctype; ad_org_id→ad_org (+1) | Detalle enlazado a ad_client, c_city, sshr_department. | PK `sprov_overtime_key`; Cols: c_doctype_id, documentno, datemovement, sshr_department_id, c_bpartner_id; `SPROV_OVERTIME_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sprov_overtime_line` | sprov_overtime_line | `SPROV_TOTALHOURS_TRG` | — | sprov_extra_reason_maint_id→sprov_extra_reason_maint; ad_client_id→ad_client; ad_org_id→ad_org; sprov_overtime_id→sprov_overtime; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, ad_org, sprov_extra_reason_maint. Validado por trigger(s): SPROV_TOTALHOURS_TRG. | PK `sprov_overtimeline_key`; Cols: c_bpartner_id, exit_shift2, exit_marking2, authorized_time, sprov_extra_reason_maint_id; `SPROV_OVERTIMELINE_ACTIVE`: ISACTIVE IN ('Y', 'N') |
| `sprov_overtime_type` | sprov_overtime_type | — | `SPROV_OTTYPE_HOURTYPE` (hourtype) | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sprov_ottype_key`; Cols: name, value, monday_to_friday, fromhour, tohour; `SPROV_OTTYPE_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `sprov_period` | sprov_period | `SPROV_PERIOD_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_period_id→c_period; c_doctype_id→c_doctype | Detalle enlazado a ad_client, ad_org, c_period. Validado por trigger(s): SPROV_PERIOD_TRG. | PK `sprov_period_key`; Cols: period, c_doctype_id, documentno, description, status; `SPROV_PERIOD_ACTIVE`: ISACTIVE IN ('Y', 'N') |
| `sprov_planned_activity` | sprov_planned_activity | `SPROV_PLANNED_ACTIVITY_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; sprov_employee_id→sprov_employee; sprov_extra_reason_maint_id→sprov_extra_reason_maint | Detalle enlazado a ad_client, ad_org, sprov_employee. Validado por trigger(s): SPROV_PLANNED_ACTIVITY_TRG. | PK `sprov_planned_key`; Cols: date, n_hour, date_compensation, sprov_employee_id, payment; `SPROV_PLANNED_ACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sprov_employee` |
| `SPROV_Employee_Overtime` |
| `SPROV_Extra_Reason_Maint` |
| `sprov_newness` |
| `sprov_overtime` |
| `sprov_overtime_line` |
| `sprov_overtime_type` |
| `sprov_period` |
| `sprov_planned_activity` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`SSPR_SHIFT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de varias ventanas, entre ellas 'Authorization Overtime', donde se gestionan las solicitudes de horas extras. Otro acceso importante es en 'Overtime Planning', que permite a los supervisores planificar y autorizar las horas necesarias. La interfaz de usuario facilita la interacción en cada paso del proceso, permitiendo a los usuarios manejar eficazmente la información relacionada con el tiempo extraordinario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Authorization Overtime | Authorization Overtime |
| Extra Reason Maintenance | Extra Reason Maintenance |
| Overtime Detail Employee | Overtime Detail Employee |
| Overtime Planning | Overtime Planning |
| Type of Overtime | Type of Overtime |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Analysis Tools | Analysis Tools | Sí |
| Authorization Overtime | Authorization Overtime | No |
| Biometric Integration | Biometric Integration | Sí |
| Configuración | Configuración | Sí |
| Detail Generated Overtime | Detail Generated Overtime | No |
| Extra Reason Maintenance | Extra Reason Maintenance | No |
| Integración Biométrico | Integración Biométrico | Sí |
| Overtime Detail Employee | Overtime Detail Employee | No |
| Overtime Planning | Overtime Planning | No |
| Process Biometric  News | Process Biometric  News | No |
| Report Absence | Report Absence | No |
| Report Arrears | Report Arrears | No |
| Report Overtime | Report Overtime | No |
| Setup | Setup | Sí |
| Type of Overtime | Type of Overtime | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

<!-- knowledge-extract:window_specs -->
### Ventana: Authorization Overtime

- **AD_WINDOW_ID:** `C8D98A47570C4C98B235C7A74EAED0B5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Authorization Overtime | `2D45CC4FE0154BC0AA6C0F779D65287A` | 0 |
| 20 | Line | `423E4A323F0F4A2FA89B9B3E114C1207` | 1 |

### Ventana: Extra Reason Maintenance

- **AD_WINDOW_ID:** `53CDD6FAFC9844ABA9640F02E049EEB1`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Extra Reason Maintenance | `E15EFB94B9004472B7AE08E9C57C0E2B` | 0 |

### Ventana: Overtime Detail Employee

- **AD_WINDOW_ID:** `6698080363AA4DFC9172A63ED5B1CD5D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Markings Detail | `3FCCE7C65BB84FD5A1ACDAE5C60061ED` | 0 |
| 20 | Newness | `D961175CF533426CBDC75F86DA5AC7E0` | 1 |

### Ventana: Overtime Planning

- **AD_WINDOW_ID:** `FD82225C38D84C4DAB3DC03AFE671CD0`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Period | `8C5146ABABCF40F9B64B383547EBF652` | 0 |
| 20 | Employee | `8D7936AB4ADB4434B22AAAC7D6D2745E` | 1 |
| 30 | Planned  Activity | `6758A7366D60484ABBC322B69EA24106` | 2 |

### Ventana: Type of Overtime

- **AD_WINDOW_ID:** `51C9101E38B346EAB5258958293B9DAE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Type of Overtime | `60B003E4553B4DAEA95150F56960E4D1` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Period (ventana: Overtime Planning)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Period | `C_Period_ID` | No | No | — |
| 40 | Transaction Type | `C_Doctype_ID` | No | No | — |
| 50 | Document No. | `Documentno` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Status | `Status` | No | Sí | — |
| 80 | Process Period | `AB_Process` | No | No | — |

### Markings Detail (ventana: Overtime Detail Employee)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Identify | `Identify` | No | No | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 60 | Date Movement | `Datemovement` | No | No | — |
| 80 | Entry | `Entry_1` | No | No | — |
| 90 | Exit | `Exit_1` | No | No | — |
| 200 | Entry Dial 1 | `Entry_Dial_1` | No | No | 126E05CD3A8947A89DA022BD8F8520C5 |
| 210 | Chek Out 1 | `Chek_Out_1` | No | No | 126E05CD3A8947A89DA022BD8F8520C5 |
| 220 | Entry Time Processed | `Entry_Time_Processed` | No | No | 126E05CD3A8947A89DA022BD8F8520C5 |
| 230 | Output Time Processed | `Output_Time_Processed` | No | No | 126E05CD3A8947A89DA022BD8F8520C5 |
| 400 | Worked Hour | `Worked_Hour` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 410 | Early Dismissal Hour | `Early_Dismissal_Hours` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 420 | Delay time | `Delay_1` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 430 | Feed Value | `Feed_Value` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 440 | Authorized Time | `Authorized_Time` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 450 | Reason Generation time | `Sprov_Extra_Reason_Maint_ID` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 460 | Generated Time | `Generated_Time` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 470 | Validated | `Validated` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 480 | Time 25 | `Time_25` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 490 | Time 50 | `Time_50` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 500 | Time 100 | `Time_100` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 510 | Processed | `Processed_Check` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 520 | 25% Time Value | `Time_Value_25` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 530 | 50% Time Value | `Time_Value_50` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 540 | 100% Time Value | `Time_Value_100` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |
| 550 | Non-attendance | `NON_Attendance` | No | No | B2AA7B65648D41B6B559BB05DB1BD278 |

### Extra Reason Maintenance (ventana: Extra Reason Maintenance)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Observation | `Description` | No | No | — |

### Authorization Overtime (ventana: Authorization Overtime)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `DocumentNo` | No | No | — |
| 50 | Date Movement | `Datemovement` | No | No | — |
| 60 | Deparment | `Sshr_Department_ID` | No | No | — |
| 70 | Boss | `C_Bpartner_ID` | No | No | — |
| 80 | City | `C_City_ID` | No | No | — |
| 90 | Hours Authorized | `Hours_Auth` | No | Sí | — |
| 100 | Description | `Description` | No | No | — |
| 110 | Status | `Status` | No | Sí | — |
| 120 | Process load biometric | `Load_Biometric` | No | No | — |
| 130 | Autorization Biometric | `Authorization_Process` | No | No | — |

### Type of Overtime (ventana: Type of Overtime)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Name | `Name` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Monday to Friday | `Monday_To_Friday` | No | No | — |
| 60 | From Hour | `Fromhour` | No | No | — |
| 70 | To Hour | `Tohour` | No | No | — |
| 80 | Shift Type | `Shifttype` | No | No | — |
| 90 | Hour Type | `Hourtype` | No | No | — |

### Pestaña `8E36BD6FE29C43A986293F91A45DA786`

- **AD_TAB_ID:** `8E36BD6FE29C43A986293F91A45DA786` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 117 | Minimum Overtime | `EM_Sprov_Minimum_Overtime` | No | No | — |
| 118 | Working Hours | `EM_Sprov_Working_Hours` | No | No | — |

### Line (ventana: Authorization Overtime)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Employee | `C_Bpartner_ID` | No | Sí | — |
| 40 | Exit Shift 2 | `Exit_Shift2` | No | Sí | — |
| 50 | Exit Marking 2 | `Exit_Marking2` | No | Sí | — |
| 60 | Authorized Time | `Authorized_Time` | No | No | — |
| 80 | Reason Generation time | `Sprov_Extra_Reason_Maint_ID` | No | No | — |

### Planned  Activity (ventana: Overtime Planning)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Date | `Date` | No | No | — |
| 40 | N Hour | `N_Hour` | No | No | — |
| 50 | Activity | `Sprov_Extra_Reason_Maint_ID` | No | No | — |
| 60 | Date Compensation | `Date_Compensation` | No | No | — |
| 80 | Payment | `Payment` | No | No | — |

### Newness (ventana: Overtime Detail Employee)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Newness | `Sprbi_Maintenance_News_ID` | No | No | — |
| 50 | Amount | `Amount` | No | No | — |
| 60 | Concept | `Sspr_Concept_ID` | No | Sí | — |
| 80 | Processed | `Processed` | No | No | — |

### Employee (ventana: Overtime Planning)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Employee | `C_Bpartner_ID` | No | No | — |
| 40 | Description | `Description` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Entre los procesos disponibles, se incluyen típicos botones como 'Completar' para finalizar la autorización de horas y 'Retornar' para devolver una solicitud para más revisión. Aunque no se proporcionan informes específicos, cada paso en el proceso incluye validaciones frecuentes como verificar la autenticidad del registro de horas y la disponibilidad de la documentación necesaria. Estas validaciones aseguran la integridad y precisión de los datos ingresados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Autorization Biometric | Autorization Biometric | sprov_authorization_biometric | `sprov_authorization_biometric` | Campo Horas Autorizadas esta vacio para el Empleado:; Campo Horas Generadas esta vacio para el Empleado:; Campo Motivo de Generación de Horas esta vacio para el Empleado:; Valida el campo horas extras del maestro de emp… | — |
| Botón (PL/pgSQL) | Calculate Overtime | Calculate Overtime | sprov_calculate_overtime | `sprov_calculate_overtime` | to_timestamp((to_char(a.datemovement,'YYYY-MM-DD') || ' ' || to_char(a.authorized_time,'HH24:MI:SS')),'yyyy-mm-dd HH24:MI:SS') as authorized_time | — |
| Botón (PL/pgSQL) | Process Biometric  News | Process Biometric  News | sprov_biometric_news | `sprov_biometric_news` | Concepto laboral, novedades y tipo alimentacion | — |
| Botón (PL/pgSQL) | Process load biometric | Process load biometric | sprov_process_load_biometric | `sprov_load_biometric` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Process newness line | Process newness line | sprov_process_newness | `sprov_process_newness` | RAISE_APPLICATION_ERROR(-20000, ' Cur_newness.value ' || Cur_newness.value || ' Cur_newness.total_arrears ' || Cur_newness.total_arrears); | — |
| Botón (PL/pgSQL) | Process Period | Process Period | Process Period | `sprov_abprocess` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Detail Generated Overtime | Detail Generated Overtime | Detail Generated Overtime | *(OBUIAPP / manual)* | Detail Generated Overtime | — |
| Proceso / otro | Report Absence | Report Absence | Report Absence | *(OBUIAPP / manual)* | Report Absence | — |
| Proceso / otro | Report Arrears | Report Arrears | Report Arrears | *(OBUIAPP / manual)* | Report Arrears | — |
| Proceso / otro | Report Overtime | Report Overtime | Report Overtime | *(OBUIAPP / manual)* | REPORT EXTRAORDINARY AND EXTRAORDINARY HOURS | — |
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
| Botón (PL/pgSQL) | Autorization Biometric | Autorization Biometric | sprov_authorization_biometric | `sprov_authorization_biometric` | Campo Horas Autorizadas esta vacio para el Empleado:; Campo Horas Generadas esta vacio para el Empleado:; Campo Motivo de Generación de Horas esta vacio para el Empleado:; Valida el campo horas extras del maestro de emp… | — |
| Botón (PL/pgSQL) | Calculate Overtime | Calculate Overtime | sprov_calculate_overtime | `sprov_calculate_overtime` | to_timestamp((to_char(a.datemovement,'YYYY-MM-DD') || ' ' || to_char(a.authorized_time,'HH24:MI:SS')),'yyyy-mm-dd HH24:MI:SS') as authorized_time | — |
| Botón (PL/pgSQL) | Process Biometric  News | Process Biometric  News | sprov_biometric_news | `sprov_biometric_news` | Concepto laboral, novedades y tipo alimentacion | — |
| Botón (PL/pgSQL) | Process load biometric | Process load biometric | sprov_process_load_biometric | `sprov_load_biometric` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Process newness line | Process newness line | sprov_process_newness | `sprov_process_newness` | RAISE_APPLICATION_ERROR(-20000, ' Cur_newness.value ' || Cur_newness.value || ' Cur_newness.total_arrears ' || Cur_newness.total_arrears); | — |
| Botón (PL/pgSQL) | Process Period | Process Period | Process Period | `sprov_abprocess` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Detail Generated Overtime | Detail Generated Overtime | Detail Generated Overtime | *(OBUIAPP / manual)* | Detail Generated Overtime | — |
| Proceso / otro | Report Absence | Report Absence | Report Absence | *(OBUIAPP / manual)* | Report Absence | — |
| Proceso / otro | Report Arrears | Report Arrears | Report Arrears | *(OBUIAPP / manual)* | Report Arrears | — |
| Proceso / otro | Report Overtime | Report Overtime | Report Overtime | *(OBUIAPP / manual)* | REPORT EXTRAORDINARY AND EXTRAORDINARY HOURS | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Autorization Biometric | Autorization Biometric | PL `sprov_authorization_biometric` | Campo Horas Autorizadas esta vacio para el Empleado:; Campo Horas Generadas esta vacio para el Empleado:; Campo Motivo de Generación de Horas esta vacio para el Empleado:; Valida el campo horas extras del maestro de emp… | Campo Horas Autorizadas esta vacio para el Empleado:; Campo Horas Generadas esta vacio para el Empleado:; Campo Motivo de Generación de Horas esta vacio para el Empleado:; Valida el campo horas extras del maestro de empleado para el calculo Valor horas extras 100% 50% 25%; RAISE_APPLICATION_ERROR(-20000, 'Despues del proceso v_hour100  ' || v_hour100); |
| Botón (PL/pgSQL) | Calculate Overtime | Calculate Overtime | PL `sprov_calculate_overtime` | to_timestamp((to_char(a.datemovement,'YYYY-MM-DD') || ' ' || to_char(a.authorized_time,'HH24:MI:SS')),'yyyy-mm-dd HH24:MI:SS') as authorized_time | to_timestamp((to_char(a.datemovement,'YYYY-MM-DD') || ' ' || to_char(a.authorized_time,'HH24:MI:SS')),'yyyy-mm-dd HH24:MI:SS') as authorized_time |
| Botón (PL/pgSQL) | Process Biometric  News | Process Biometric  News | PL `sprov_biometric_news` | Concepto laboral, novedades y tipo alimentacion | Concepto laboral, novedades y tipo alimentacion |
| Botón (PL/pgSQL) | Process load biometric | Process load biometric | PL `sprov_load_biometric` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Botón (PL/pgSQL) | Process newness line | Process newness line | PL `sprov_process_newness` | RAISE_APPLICATION_ERROR(-20000, ' Cur_newness.value ' || Cur_newness.value || ' Cur_newness.total_arrears ' || Cur_newness.total_arrears); | RAISE_APPLICATION_ERROR(-20000, ' Cur_newness.value ' || Cur_newness.value || ' Cur_newness.total_arrears ' || Cur_newness.total_arrears); |
| Botón (PL/pgSQL) | Process Period | Process Period | PL `sprov_abprocess` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
| Proceso / otro | Detail Generated Overtime | Detail Generated Overtime | — | Detail Generated Overtime | — |
| Proceso / otro | Report Absence | Report Absence | — | Report Absence | — |
| Proceso / otro | Report Arrears | Report Arrears | — | Report Arrears | — |
| Proceso / otro | Report Overtime | Report Overtime | — | REPORT EXTRAORDINARY AND EXTRAORDINARY HOURS | — |
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
| `SPROV_DuplicatePeriod` | Duplicate Period | Duplicate Period | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPROV_CanNotDelete` | You cannot delete records | You cannot delete records | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPROV_UnvalidatedRecords` | There are lines without validation | There are lines without validation | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SPROV_Processed` | You cannot delete a processed transaction | You cannot delete a processed transaction | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye una clase Java, 'Calculategeneratehours', que se utiliza para calcular las horas generadas en base a ciertos eventos, integrándose con la lógica del sistema mediante callouts simples para ajustes dinámicos en la interfaz según los inputs de los usuarios.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payroll.overtime`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Calculategeneratehours` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/payroll/overtime/ad_callouts/Calculategeneratehours.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SPROV_EMPLOYEE_OVERTIME_TRG` | `sprov_employee_overtime` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPROV_EMPLOYEE_TRG` | `sprov_employee` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPROV_NEWNESS_TRG` | `sprov_newness` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPROV_PERIOD_TRG` | `sprov_period` | before INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPROV_PLANNED_ACTIVITY_TRG` | `sprov_planned_activity` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SPROV_TOTALHOURS_TRG` | `sprov_overtime_line` | before INSERT/UPDATE/DELETE | set hours_auth = hours_auth + new.generated_time; set hours_auth = hours_auth + (new.generated_time - :old.generated_time); set hours_auth = hours_auth - :old.generated_time |
| AD_VAL_RULE | — | `User Validation Overtime` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
| AD_VAL_RULE | — | `Logger user overtime` | `AD_User.AD_User_ID = @#AD_User_ID@` |
| AD_VAL_RULE | — | `sprov_filter_boss` | `C_BPARTNER.C_BPARTNER_id in(select a.c_bpartner_id
from c_bpartner a
left join sspr_contract b on b.c_bpartner_id = a.c_` |
| AD_VAL_RULE | — | `sprov_documenttype_overtime` | `C_DocType.DocBaseType='SPROV_AO'` |
| AD_VAL_RULE | — | `Organization Validation Overtime` | `AD_ORG.AD_ORG_ID = @#AD_ORG_ID@` |
| AD_VAL_RULE | — | `Overtime period` | `C_Period.openclose = 'C'` |
| AD_VAL_RULE | — | `Active Employee` | `C_BPartner.IsEmployee = 'Y' and C_BPartner.EM_SSPR_Status = 'A'` |
| AD_VAL_RULE | — | `Periods By Current Year` | `c_period_id IN (SELECT c_period_id FROM c_period JOIN c_year ON c_year.c_year_id=c_period.c_year_id WHERE c_year.year=TO` |
| AD_VAL_RULE | — | `sprov_filter_employee` | `C_BPARTNER.ISEMPLOYEE = 'Y'  and C_BPARTNER.isactive= 'Y'` |
| Función PL `sprov_authorization_biometric` | — | invocación proceso | Campo Horas Autorizadas esta vacio para el Empleado:; Campo Horas Generadas esta vacio para el Empleado:; Campo Motivo de Generación de Horas esta vacio para el Empleado: |
| Función PL `sprov_biometric_news` | — | invocación proceso | Concepto laboral, novedades y tipo alimentacion |
| Función PL `sprov_calculate_hour` | — | invocación proceso | Inserta novedades de las lineas del detalle de horas extras empleado |
| Función PL `sprov_calculate_overtime` | — | invocación proceso | to_timestamp((to_char(a.datemovement,'YYYY-MM-DD') || ' ' || to_char(a.authorized_time,'HH24:MI:SS')),'yyyy-mm-dd HH24:MI:SS') as authorized_time |
| Función PL `sprov_create_newnewss` | — | invocación proceso | Inserta novedades de las lineas del detalle de horas extras empleado |
| Función PL `sprov_overtime_100` | — | invocación proceso | Datos de la configuracion de horas extras; RAISE_APPLICATION_ERROR(-20000, ' v_authorized_time_final 1 ' || v_authorized_time_final || ' v_starttime_final ' || v_starttime_final);; RAISE_APPLICATION_ERROR(-20000, ' v_nohours 2 '  || v_nohours); |
| Función PL `sprov_overtime_25` | — | invocación proceso | Datos de la configuracion de horas extras; RAISE_APPLICATION_ERROR(-20000, ' v_exit ' ||  v_exit  || ' v_fromhour ' || v_fromhour) ;; RAISE_APPLICATION_ERROR(-20000, ' v_authorized_time_final ' ||  v_authorized_time_final || ' - ' || v_fromhour) ; |
| Función PL `sprov_overtime_50` | — | invocación proceso | Datos de la configuracion de horas extras; RAISE_APPLICATION_ERROR(-20000, 'Error ' ||  v_authorized_time_final || ' >= ' || v_fromhour || ' and '  || v_authorized_time_final || ' <= ' || v_tohour);; RAISE_APPLICATION_ERROR(-20000, 'Error If v_nohours ' ||  v_nohours); |
| Función PL `sprov_process_newness` | — | invocación proceso | RAISE_APPLICATION_ERROR(-20000, ' Cur_newness.value ' || Cur_newness.value || ' Cur_newness.total_arrears ' || Cur_newness.total_arrears); |
| Función PL `sprov_punctuality_bonus` | — | invocación proceso | Ya existe un registro para el concepto BONO DE PUNTUALIDAD Y ASISTENCIA con el mismo periodo para el empleado; No existe concepto tipo Bono Puntualidad y Asistencia; Inserta novedades de las lineas del detalle de horas extras empleado |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers en este módulo juegan un papel fundamental al asegurar que las reglas de negocio se implementen adecuadamente. Las funciones PL/pgSQL, como las incluidas en 'functions_for_buttons', son responsables de la lógica detrás de las acciones de los botones, asegurando que los procesos se realicen sin errores y cumpliendo con las restricciones establecidas en el modelo de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SPROV_EMPLOYEE_TRG` | `sprov_employee` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPROV_EMPLOYEE_TRG.xml` |
| `SPROV_EMPLOYEE_OVERTIME_TRG` | `sprov_employee_overtime` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPROV_EMPLOYEE_OVERTIME_TRG.xml` |
| `SPROV_NEWNESS_TRG` | `sprov_newness` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPROV_NEWNESS_TRG.xml` |
| `SPROV_TOTALHOURS_TRG` | `sprov_overtime_line` | before | INSERT/UPDATE/DELETE | set hours_auth = hours_auth + new.generated_time; set hours_auth = hours_auth + (new.generated_time - :old.generated_time); set hours_auth = hours_auth - :old.generated_time | `model/triggers/SPROV_TOTALHOURS_TRG.xml` |
| `SPROV_PERIOD_TRG` | `sprov_period` | before | INSERT/UPDATE/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPROV_PERIOD_TRG.xml` |
| `SPROV_PLANNED_ACTIVITY_TRG` | `sprov_planned_activity` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SPROV_PLANNED_ACTIVITY_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sprov_abprocess` | Process Period | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SPROV_ABPROCESS.xml` |
| `sprov_authorization_biometric` | Autorization Biometric | Campo Horas Autorizadas esta vacio para el Empleado:; Campo Horas Generadas esta vacio para el Empleado:; Campo Motivo de Generación de Horas esta vacio para el Empleado:; Valida el campo horas extras del maestro de emp… | Campo Horas Autorizadas esta vacio para el Empleado:; Campo Horas Generadas esta vacio para el Empleado:; Campo Motivo de Generación de Horas esta vacio para el Empleado:; Valida el campo horas extras del maestro de empleado para el calculo Valor horas extras 100% 50% 25%; RAISE_APPLICATION_ERROR(-20000, 'Despues del proceso v_hour100  ' || v_hour100); | `model/functions/SPROV_AUTHORIZATION_BIOMETRIC.xml` |
| `sprov_biometric_news` | Process Biometric  News | Concepto laboral, novedades y tipo alimentacion | Concepto laboral, novedades y tipo alimentacion | `model/functions/SPROV_BIOMETRIC_NEWS.xml` |
| `sprov_calculate_hour` | — | Inserta novedades de las lineas del detalle de horas extras empleado | Inserta novedades de las lineas del detalle de horas extras empleado | `model/functions/SPROV_CALCULATE_HOUR.xml` |
| `sprov_calculate_overtime` | Calculate Overtime | to_timestamp((to_char(a.datemovement,'YYYY-MM-DD') || ' ' || to_char(a.authorized_time,'HH24:MI:SS')),'yyyy-mm-dd HH24:MI:SS') as authorized_time | to_timestamp((to_char(a.datemovement,'YYYY-MM-DD') || ' ' || to_char(a.authorized_time,'HH24:MI:SS')),'yyyy-mm-dd HH24:MI:SS') as authorized_time | `model/functions/SPROV_CALCULATE_OVERTIME.xml` |
| `sprov_create_newnewss` | — | Inserta novedades de las lineas del detalle de horas extras empleado | Inserta novedades de las lineas del detalle de horas extras empleado | `model/functions/SPROV_CREATE_NEWNEWSS.xml` |
| `sprov_load_biometric` | Process load biometric | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SPROV_LOAD_BIOMETRIC.xml` |
| `sprov_overtime_100` | — | Datos de la configuracion de horas extras; RAISE_APPLICATION_ERROR(-20000, ' v_authorized_time_final 1 ' || v_authorized_time_final || ' v_starttime_final ' || v_starttime_final);; RAISE_APPLICATION_ERROR(-20000, ' v_no… | Datos de la configuracion de horas extras; RAISE_APPLICATION_ERROR(-20000, ' v_authorized_time_final 1 ' || v_authorized_time_final || ' v_starttime_final ' || v_starttime_final);; RAISE_APPLICATION_ERROR(-20000, ' v_nohours 2 '  || v_nohours);; RAISE_APPLICATION_ERROR(-20000, ' v_nohours 3'  || v_nohours);; RAISE_APPLICATION_ERROR(-20000, ' v_nohours ' || v_nohours); | `model/functions/SPROV_OVERTIME_100.xml` |
| `sprov_overtime_25` | — | Datos de la configuracion de horas extras; RAISE_APPLICATION_ERROR(-20000, ' v_exit ' || v_exit || ' v_fromhour ' || v_fromhour) ;; RAISE_APPLICATION_ERROR(-20000, ' v_authorized_time_final ' || v_authorized_time_final… | Datos de la configuracion de horas extras; RAISE_APPLICATION_ERROR(-20000, ' v_exit ' ||  v_exit  || ' v_fromhour ' || v_fromhour) ;; RAISE_APPLICATION_ERROR(-20000, ' v_authorized_time_final ' ||  v_authorized_time_final || ' - ' || v_fromhour) ; | `model/functions/SPROV_OVERTIME_25.xml` |
| `sprov_overtime_50` | — | Datos de la configuracion de horas extras; RAISE_APPLICATION_ERROR(-20000, 'Error ' || v_authorized_time_final || ' >= ' || v_fromhour || ' and ' || v_authorized_time_final || ' <= ' || v_tohour);; RAISE_APPLICATION_ERR… | Datos de la configuracion de horas extras; RAISE_APPLICATION_ERROR(-20000, 'Error ' ||  v_authorized_time_final || ' >= ' || v_fromhour || ' and '  || v_authorized_time_final || ' <= ' || v_tohour);; RAISE_APPLICATION_ERROR(-20000, 'Error If v_nohours ' ||  v_nohours);; RAISE_APPLICATION_ERROR(-20000, 'Error Else v_nohours ' ||  v_nohours);; RAISE_APPLICATION_ERROR(-20000, 'Error If v_authorized_time_final ' ||  v_authorized_time_final || '  - ' || v_exit) ;; RAISE_APPLICATION_ERROR(-20000, 'Error Else del Else v_nohours ' ||  v_nohours); | `model/functions/SPROV_OVERTIME_50.xml` |
| `sprov_process_newness` | Process newness line | RAISE_APPLICATION_ERROR(-20000, ' Cur_newness.value ' || Cur_newness.value || ' Cur_newness.total_arrears ' || Cur_newness.total_arrears); | RAISE_APPLICATION_ERROR(-20000, ' Cur_newness.value ' || Cur_newness.value || ' Cur_newness.total_arrears ' || Cur_newness.total_arrears); | `model/functions/SPROV_PROCESS_NEWNESS.xml` |
| `sprov_punctuality_bonus` | — | Ya existe un registro para el concepto BONO DE PUNTUALIDAD Y ASISTENCIA con el mismo periodo para el empleado; No existe concepto tipo Bono Puntualidad y Asistencia; Inserta novedades de las lineas del detalle de horas… | Ya existe un registro para el concepto BONO DE PUNTUALIDAD Y ASISTENCIA con el mismo periodo para el empleado; No existe concepto tipo Bono Puntualidad y Asistencia; Inserta novedades de las lineas del detalle de horas extras empleado | `model/functions/SPROV_PUNCTUALITY_BONUS.xml` |
| `sprov_return_position` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SPROV_RETURN_POSITION.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Autorization Biometric | `sprov_authorization_biometric` | Botón (PL/pgSQL) | PL `sprov_authorization_biometric` | N | Campo Horas Autorizadas esta vacio para el Empleado:; Campo Horas Generadas esta vacio para el Empleado:; Campo Motivo de Generación de Horas esta vacio para el Empleado:; Valida e |
| 2 | Calculate Overtime | `sprov_calculate_overtime` | Botón (PL/pgSQL) | PL `sprov_calculate_overtime` | N | to_timestamp((to_char(a.datemovement,'YYYY-MM-DD') || ' ' || to_char(a.authorized_time,'HH24:MI:SS')),'yyyy-mm-dd HH24:MI:SS') as authorized_time |
| 3 | Process Biometric  News | `sprov_biometric_news` | Botón (PL/pgSQL) | PL `sprov_biometric_news` | N | Concepto laboral, novedades y tipo alimentacion |
| 4 | Process load biometric | `sprov_process_load_biometric` | Botón (PL/pgSQL) | PL `sprov_load_biometric` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| 5 | Process newness line | `sprov_process_newness` | Botón (PL/pgSQL) | PL `sprov_process_newness` | N | RAISE_APPLICATION_ERROR(-20000, ' Cur_newness.value ' || Cur_newness.value || ' Cur_newness.total_arrears ' || Cur_newness.total_arrears); |
| 6 | Process Period | `Process Period` | Botón (PL/pgSQL) | PL `sprov_abprocess` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

**Total acciones documentadas (extract):** **6** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
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

Módulo: `ec.com.sidesoft.payroll.overtime`.

## Suposiciones

- *(Ninguna automática; completar tras revisión funcional.)*

## Archivos no proporcionados / ausentes en el módulo

| Recurso | Estado |
| --- | --- |
| `AD_MESSAGE.xml` | presente |
| `AD_WINDOW.xml` | presente |
| `OBUIAPP_PROCESS.xml` | ausente |
| Traducción `.es_ES` | no |

## Huecos de trazabilidad (botón → proceso)

Revise las clases Java de proceso/acción del paquete. Acciones solo en JS, plantillas `configScript` o procesos de módulos dependientes deben documentarse aquí.

- *(Completar filas con «enlace no encontrado en adjuntos».)*

# Glosario — prefijo `SPROV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPROV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payroll.overtime` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `sprov_authorization_biometric` — Autorization Biometric
- `sprov_calculate_overtime` — Calculate Overtime
- `sprov_biometric_news` — Process Biometric  News
- `sprov_process_load_biometric` — Process load biometric
- `sprov_process_newness` — Process newness line
- `Process Period` — Process Period
- `Detail Generated Overtime` — Detail Generated Overtime
- `Report Absence` — Report Absence
- `Report Arrears` — Report Arrears
- `Report Overtime` — Report Overtime

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Actuarial Report
**Package:** `ec.com.sidesoft.payroll.report.actuarial`

# Module overview — Actuarial Report

## Functional

El módulo 'Actuarial Report' se centra en la generación de informes actuariales dentro de la gestión de nómina, permitiendo a los usuarios de negocio obtener análisis detallados sobre aspectos actuariales de sus planillas. Los principales actores son los responsables de Recursos Humanos y Payroll, quienes requieren esta información para la toma de decisiones informadas. El alcance del módulo está limitado al procesamiento y visualización de datos relacionados con la nómina y su contexto actuarial, en conformidad con las funcionalidades ya existentes en Openbravo y sus otras dependencias. Este módulo pretende complementar la gestión de nómina, agregando valor analítico mediante la presentación de datos clave que apoyan la estrategia organizativa.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payroll/report/actuarial` |
| Web | `web/ec.com.sidesoft.payroll.report.actuarial/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Human Resources Management - Payroll
- Openbravo 3.0 Framework

### Version

**1.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPRAL`

# Guía de chat — Actuarial Report

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payroll.report.actuarial`).

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

- ¿Cómo puedo acceder al informe actuarial?
- ¿Qué datos se requieren para generar el informe actuarial?
- ¿El informe puede ser exportado en un formato específico?
- ¿Cómo puedo validar la información antes de generar el informe?
- ¿Es posible programar la generación de informes actuariales de manera automática?
- ¿Dónde encuentro los informes generados?
- ¿Puedo cambiar el período para el cual se genera el informe actuarial?
- ¿A quién debo contactar si encuentro un error en el informe actuarial?

# Domain — data model

## Functional

El 'Actuarial Report' funciona sobre una entidad cabecera que representa las nóminas en un periodo específico. Aunque no hay tablas físicas adicionales elaboradas en el módulo, hay una relación implícita con los datos de Recursos Humanos y la gestión de nómina que son esenciales para el cálculo y la generación de informes actuariales. Este módulo no incluye triggers ni funciones PL, lo que sugiere que su funcionalidad se basa en la simple extracción y presentación de datos. Esto permite una rápida adaptación a los cambios en las estructuras de datos existentes ya que su operación se apoya completamente en el núcleo de Openbravo y sus dependencias.

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

El acceso al módulo se realiza a través de un menú que permite iniciar el proceso de generación del informe actuarial. La interfaz de usuario es sencilla y sigue la misma estructura visual que otros módulos de Openbravo, asegurando una experiencia de usuario coherente y familiar. El usuario podrá navegar fácilmente por las opciones de generación del informe dentro del contexto de gestión de nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payroll.report.actuarial.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Reporte para Cálculo Actuarial | Reporte para Cálculo Actuarial | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payroll.report.actuarial.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo cuenta con un único botón procesar, que permite a los usuarios generar el 'Actuarial Report' de acuerdo a los datos disponibles en la nómina. Una vez que se ejecuta el proceso, se generará el informe sin generar informes adicionales debido a la naturaleza del módulo. Las validaciones frecuentes pueden incluir verificaciones sobre los datos de nómina antes de la generación del informe, asegurando que todos los registros necesarios estén presentes y correctos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payroll.report.actuarial.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte para Cálculo Actuarial | Reporte para Cálculo Actuarial | JR_CalculoActuarial | *(OBUIAPP / manual)* | Reporte para Cálculo Actuarial | — |
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
| Proceso / otro | Reporte para Cálculo Actuarial | Reporte para Cálculo Actuarial | JR_CalculoActuarial | *(OBUIAPP / manual)* | Reporte para Cálculo Actuarial | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte para Cálculo Actuarial | Reporte para Cálculo Actuarial | — | Reporte para Cálculo Actuarial | — |
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

El módulo 'Actuarial Report' no contiene clases Java personalizadas, lo que significa que no hay lógica de negocio adicional implementada en Java, dependiendo completamente de las funcionalidades nativas del framework Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payroll.report.actuarial`.

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

Sin implementar triggers ni funciones PL asociadas, el rol en la base de datos se enfoca en el acceso y la manipulación de datos dentro del sistema existente. Esto implica un uso directo de la estructura de datos del ERP para la extracción de informes actuariales, dependiendo de la integridad de la base de datos del sistema principal.

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

Módulo: `ec.com.sidesoft.payroll.report.actuarial`.

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

# Glosario — prefijo `SPRAL`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPRAL` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payroll.report.actuarial` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `JR_CalculoActuarial` — Reporte para Cálculo Actuarial

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Payroll Report - Lotaip
**Package:** `ec.com.sidesoft.payroll.reports.lotaip`

# Module overview — Sidesoft Payroll Report - Lotaip

## Functional

El módulo Sidesoft Payroll Report - Lotaip tiene como propósito generar informes relacionados con la nómina bajo las regulaciones LOTAIP, asegurando el cumplimiento legal en la gestión de personal. Los actores principales son los usuarios de negocio encargados de la gestión de recursos humanos y el personal administrativo que requiere datos precisos para reportes. El alcance del módulo incluye la generación de reportes específicos en formato JRXML, los cuales son utilizados por el departamento de recursos humanos. Este módulo depende del módulo de Gestión de Recursos Humanos - Nómina y es compatible con la versión del sistema que va de la 2.50 a la 3.00 del Skin de compatibilidad.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payroll/reports/lotaip` |
| Web | `web/ec.com.sidesoft.payroll.reports.lotaip/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPRLT`

# Guía de chat — Sidesoft Payroll Report - Lotaip

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payroll.reports.lotaip`).

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

- ¿Cómo puedo generar el reporte LOTAIP?
- ¿Dónde encuentro el informe una vez que ha sido generado?
- ¿Qué datos se requieren para la generación del reporte?
- ¿Se pueden personalizar los reportes generados?
- ¿Qué hacer si encuentro errores en los datos de nómina?
- ¿Hay algún plazo para la presentación de estos informes?
- ¿Puedo ver ejemplos de reportes LOTAIP previamente generados?
- ¿Cómo puedo acceder al módulo de Recursos Humanos para actualizar datos?

# Domain — data model

## Functional

Aunque el módulo no cuenta con tablas físicas específicas, su funcionalidad se basa en consultas dinámicas que extraen información de las tablas relevantes del módulo de nómina existente. La entidad principal en esta funcionalidad es la información consolidada de la nómina, que se relaciona con los datos de empleados y sus respectivos salarios. Al ser un módulo centrado en generar reportes, se destaca la importancia de la recolección y validación de datos previos, aunque no se establecen triggers específicos o funciones PL en esta versión del módulo.

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

El módulo se navega a través de dos menús principales que permiten al usuario acceder a las funcionalidades del reporte de forma sencilla. Dado que no se dispone de ventanas físicas o tabs específicas, la navegación es principalmente a través de opciones de menú que dirigen a la generación de reportes en formato JRXML.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payroll.reports.lotaip.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Analysis Tools | Analysis Tools | Sí |
| Reporte Lotaip | Lotaip Report | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payroll.reports.lotaip.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso donde los usuarios pueden ejecutar la generación del reporte de nómina LOTAIP mediante un botón que inicia la compilación de datos necesarios. Aunque no se presentan informes adicionales o validaciones complejas, es esencial que los usuarios verifiquen que todos los datos de nómina estén correctamente ingresados antes de generar los reportes. Las validaciones comunes incluyen el aseguramiento de que todos los empleados tienen sus datos actualizados en el sistema, así como la correcta categorización de sus remuneraciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payroll.reports.lotaip.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Lotaip | Lotaip Report | Lotaip Report | *(OBUIAPP / manual)* | — | — |
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
| Proceso / otro | Reporte Lotaip | Lotaip Report | Lotaip Report | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte Lotaip | Lotaip Report | — | — | — |
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

Este módulo no incluye componentes Java ni clases específicas, por lo que toda su funcionalidad se centra en la capacidad de generación de informes utilizando herramientas de reporte estándar del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payroll.reports.lotaip`.

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
| AD_VAL_RULE | — | `Org Validation` | `AD_ORG.AD_ORG_ID = @#AD_ORG_ID@` |
| AD_VAL_RULE | — | `User lotaip validate` | `AD_USER.AD_USER_ID = @#AD_USER_ID@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El módulo se apoya principalmente en la consultas SQL que permiten extraer la información necesaria para la generación del reporte. No se utilizan triggers o funciones PL específicas en este módulo, lo que simplifica el esquema de datos utilizado, aunque el soporte técnico debe ser consciente de las tablas del módulo de nómina subyacente que alimentan el reporte.

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

Módulo: `ec.com.sidesoft.payroll.reports.lotaip`.

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

# Glosario — prefijo `SSPRLT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPRLT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payroll.reports.lotaip` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Lotaip Report` — Reporte Lotaip

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Payroll Setup Formulary 107
**Package:** `ec.com.sidesoft.payroll.setup.formulary107`

# Module overview — Payroll Setup Formulary 107

## Functional

El módulo 'Payroll Setup Formulary 107' se diseñó para optimizar el manejo de la nómina dentro de Openbravo, facilitando el acceso a formularios y configuraciones específicas para la gestión de la seguridad social y la clasificación de empleadores. Este módulo está destinado a usuarios de negocio que trabajan con nómina, así como a personal de soporte técnico de nivel 2 y desarrolladores que necesitan integrarse con la funcionalidad de nómina. Su implementación requiere de compatibilidad con la versión del framework de Openbravo y otros módulos relacionados, asegurando así un rendimiento óptimo. Este módulo no contiene triggers ni funciones PL, lo cual simplifica su arquitectura y concentración en la configuración de la interfaz y datos necesarios para la operación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payroll/setup/formulary107` |
| Web | `web/ec.com.sidesoft.payroll.setup.formulary107/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SPFM`

# Guía de chat — Payroll Setup Formulary 107

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payroll.setup.formulary107`).

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
- «¿Qué es la tabla spfm_social_security_entity?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo ingreso una nueva entidad de seguridad social?
- ¿Qué información es necesaria para clasificar un tipo de empleador?
- ¿Puedo modificar la información de una entidad de seguridad social una vez que ha sido creada?
- ¿Hay algún procedimiento para validar la información ingresada en los formularios?
- ¿Cómo acceder a los formularios desde el menú principal?
- ¿Qué pasa si encuentro un error en la configuración de un tipo de empleador?
- ¿Es posible enlazar entidades de seguridad social con empleados en el sistema?
- ¿Qué debo hacer si no encuentro una opción que necesito en el módulo?

# Domain — data model

## Functional

En la base de datos, las entidades clave del módulo son las tablas relacionadas con 'spfm_social_security_entity' y 'type employer', que forman la base del modelo de datos para el módulo. Estas tablas permiten la gestión de entidades de seguridad social y la clasificación de empleadores, facilitando la conexión entre las características de los empleados y sus respectivas obligaciones legales. Aunque no se han definido triggers ni funciones PL en este módulo, la estructura de tablas implica relaciones directas que apoyan la integridad de los datos en los procesos de nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `spfm_social_security_entity` |
| `spfm_type_employer` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `spfm_social_security_entity` | spfm_social_security_entity | — | — | — | Entidad de datos del módulo (ver columnas y FK). | PK `spfm_social_security_entity_pkey`; Cols: code, description |
| `spfm_type_employer` | SPFM_type_employer | — | — | — | Entidad de datos del módulo (ver columnas y FK). | PK `spfm_type_employer_pkey`; Cols: code, description |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `spfm_social_security_entity` |
| `SPFM_type_employer` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Los usuarios pueden navegar por el módulo a través de dos ventanas principales: 'Social security entity' y 'type employer'. Cada ventana contendrá formularios que les permitirán ingresar y modificar la información relacionada. Se facilita el acceso a estas ventanas desde el menú principal del módulo, mejorando la experiencia del usuario al interactuar con las funciones necesarias para su trabajo diario en la gestión de nómina.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payroll.setup.formulary107.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Social security entity | Social security entity |
| type employer | type employer |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración | Setup | Sí |
| Ente de seguridad social | social_security_entity | No |
| Tipo de empleador | Type of employer | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payroll.setup.formulary107.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Social security entity

- **AD_WINDOW_ID:** `5C3C060E96A24C8C915748D804EEF2E6`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Social security entity | `E9D5B05954604BD8863D10BC5ED6CBCE` | 0 |

### Ventana: type employer

- **AD_WINDOW_ID:** `43BC0558ADDA4D0895F85FB16EE5053A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Type employer | `1CC673256C284C13AB351037E5827991` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Type employer (ventana: type employer)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Validation Code | `code` | No | No | — |
| 30 | Description | `Description` | No | No | — |
| 40 | Active | `Isactive` | No | No | — |

### Social security entity (ventana: Social security entity)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Code | `Code` | No | No | — |
| 30 | Description | `Description` | No | No | — |
| 40 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo no incorpora procesos automatizados con botones típicos, ni informes asociados que demanden acciones de completar, retornar o rechazar. Sin embargo, los usuarios deberán validar regularmente la información ingresada, asegurándose de que cumpla con los requisitos legales y normativos en lo que respecta a la nómina y la seguridad social. Se recomienda a los usuarios tener atención especial sobre la consistencia de los datos de las entidades de seguridad social.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payroll.setup.formulary107.es_ES/referencedata/translation/`.

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

Este módulo no incluye clases Java específicas, por lo que carece de implementaciones en este ámbito. La funcionalidad del módulo se concentra en la configuración y manejo de datos a través de las interfaces de usuario y las tablas correspondientes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payroll.setup.formulary107`.

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

Aunque no existen triggers ni funciones PL en este módulo, la simplicidad de su estructura hace que sea más fácil para el soporte técnico comprender y gestionar su funcionalidad. Las dos tablas principales mantienen la integridad de los datos y aseguran que la información se almacene correctamente, facilitando así futuras actualizaciones y mantenimiento por parte de los desarrolladores.

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

Módulo: `ec.com.sidesoft.payroll.setup.formulary107`.

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

# Glosario — prefijo `SPFM`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SPFM` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payroll.setup.formulary107` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Income Tax Batch Charge
**Package:** `ec.com.sidesoft.incometax.batch`

# Module overview — Sidesoft Income Tax Batch Charge

## Functional

El módulo Sidesoft Income Tax Batch Charge permite gestionar la carga masiva de los impuestos a la renta en Openbravo. Este proceso es esencial para las empresas que desean automatizar la presentación de sus obligaciones fiscales. Los actores principales son los usuarios de negocio que cargan los datos, y el soporte técnico que resolverá cualquier incidencia. El alcance del módulo incluye la preparación y validación de datos antes de la carga, así como la generación de reportes relacionados. El módulo tiene dependencias con la 'Core' de Openbravo y el '2.50 to 3.00 Compatibility Skin', lo que garantiza su correcto funcionamiento en versiones específicas del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/incometax/batch` |
| Web | `web/ec.com.sidesoft.incometax.batch/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSITBCH`

# Guía de chat — Sidesoft Income Tax Batch Charge

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.incometax.batch`).

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

- ¿Cómo inicio el proceso de carga masiva de impuestos a la renta?
- ¿Qué validaciones se realizan antes de cargar los datos?
- ¿Qué debo hacer si la carga de datos no se completa correctamente?
- ¿Puedo ver un informe después de la carga de datos?
- ¿Existen requisitos especiales para los datos que voy a cargar?
- ¿Qué sucede si tengo un error en uno de los registros de la carga?
- ¿Cómo puedo verificar si mis datos cumplieron con las validaciones?
- ¿Cómo se relaciona este módulo con otros procesos de negocio en Openbravo?

# Domain — data model

## Functional

No se han definido tablas físicas específicas para el módulo, lo que sugiere que las operaciones se realizan principalmente a nivel de procesos sin persistencia de datos en modelos relacionales. Sin embargo, se sugiere que la entidad cabecera puede estar relacionada con el manejo de gastos deducibles y las correspondientes retenciones fiscales. Las etapas abarcan la carga de datos en el sistema, donde se validarán y procesarán las entradas según las reglas fiscales pertinentes. Aunque no hay triggers definidos, la lógica de negocio puede depender de validaciones que aseguran la integridad de los datos introducidos.

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

No se han definido ventanas específicamente para este módulo, lo que implica que la interacción puede realizarse mediante procesos backend o a través de módulos complementarios en la interfaz de usuario de Openbravo. Los usuarios deben estar familiarizados con la función de importar datos a través de un proceso sin una interfaz gráfica dedicada en esta versión del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.incometax.batch.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.incometax.batch.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso de carga batch es fundamental y se caracteriza por contar con botones típicos de completado y retorno, así como la posibilidad de rechazar cargas erróneas. Aunque no hay informes detallados generados por el módulo, el enfoque principal radica en asegurar que los datos que se van a cargar cumplen con las validaciones requeridas. Las validaciones frecuentes incluyen chequear que los campos estén correctamente formateados y que las entradas no superen los límites establecidos para su correcta inserción en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.incometax.batch.es_ES/referencedata/translation/`.

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

El módulo incluye una clase en Java, 'ImportPersonalExpenses', que se encarga de gestionar la importación de gastos personales deducibles. Esta clase utiliza diversos parámetros para validar y procesar la información necesaria, lo que indica que el código Java tiene un papel central en la ejecución de las cargas de datos dentro del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.incometax.batch`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ImportPersonalExpenses` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/incometax/batch/ad_process/ImportPersonalExpenses.java` |
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

Dado que en este módulo no existen triggers o funciones PL definidos, la funcionalidad de la base de datos parece centrarse en el manejo de errores a nivel de procesamiento, asegurando que no se inserten datos erróneos en la base de datos. Esto podría implicar el uso de lógica de control en el backend para gestionar excepciones y mantener la integridad de los datos.

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

Módulo: `ec.com.sidesoft.incometax.batch`.

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

# Glosario — prefijo `SSITBCH`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSITBCH` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.incometax.batch` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
