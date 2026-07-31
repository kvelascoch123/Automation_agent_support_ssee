# Openbravo Sidesoft — Recursos Humanos

> Gestión de empleados, contratos, datos de empleado, carga automática, feriados, DINARDAP, telecommuting.

**Paquetes incluidos (8):**
- `com.sidesoft.ecuador.humanResources` — Human Resources
- `ec.com.sidesoft.payroll.employee.data` — Sidesoft Automatic Upload of Employee Data
- `ec.com.sidesoft.holidays` — Holidays
- `ec.com.sidesoft.dinardap` — Dinardap
- `ec.com.sidesoft.dinardap.advanced` — Sidesoft Dinardap Advanced
- `ec.com.sidesoft.dinardap.custom.canton` — Sidesoft Actuaria  Dinardap Custom Canton
- `ec.com.sidesoft.payroll.telecommuting.dialing` — Module Telecommuting dialing
- `ec.com.sideosft.localization.payroll.datasets` — Ecuador Localization Payroll Datasets


---
## Human Resources
**Package:** `com.sidesoft.ecuador.humanResources`

# Module overview — Human Resources

## Functional

El módulo de Recursos Humanos está diseñado para gestionar todos los aspectos relacionados con el capital humano de una organización. Los actores principales de este módulo son los usuarios de negocio encargados de la gestión de personal, así como el soporte técnico de segundo nivel que ayuda en la resolución de problemas. El alcance del módulo incluye, pero no se limita a, la gestión de empleados, posiciones, discapacidades y departamentos. Este módulo depende de los módulos Core y Human Resources Management - Payroll, lo que asegura su funcionalidad integrada en el sistema ERP de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/com/sidesoft/ecuador/humanResources` |
| Web | `web/com.sidesoft.ecuador.humanResources/` |

### Declared dependencies

- Core
- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSHR`

# Guía de chat — Human Resources

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`com.sidesoft.ecuador.humanResources`).

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
- «¿Qué es la tabla sshr_job?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo añadir un nuevo empleado al sistema?
- ¿Cuáles son los pasos para gestionar una discapacidad en un empleado?
- ¿Dónde puedo encontrar información sobre las vacantes disponibles?
- ¿Cómo puedo actualizar la posición de un empleado?
- ¿Qué debo hacer si un empleado ya no trabaja en la empresa?
- ¿Cómo puedo generar un informe de actividades de recursos humanos?
- ¿Qué validaciones se aplican al crear un nuevo puesto?
- ¿Dónde puedo ver el historial de un candidato?

# Domain — data model

## Functional

La entidad cabecera del módulo de Recursos Humanos está representada por la tabla SSHR_JOB, que almacena información clave sobre cada puesto disponible. Entre las etapas, se destacan procesos relacionados con la gestión de candidatos (Applicant) y empleados (Employee Position), así como su relación con otras entidades como Departament y Cargo/Position. Los triggers clave como SSHR_JOB_POST_TRG1 y SSHR_POSITION_TRG1 aseguran la integridad y la automatización de ciertas acciones al modificar registros en estas tablas, permitiendo así un flujo de trabajo más eficiente y evitando inconsistencias en la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sshr_activity` |
| `sshr_applicant` |
| `sshr_applicant_concours` |
| `sshr_ch_int_ext` |
| `sshr_ch_responsibilities` |
| `sshr_cha_activity` |
| `sshr_competence` |
| `sshr_configure360` |
| `sshr_department` |
| `sshr_details_position` |
| `sshr_disability` |
| `sshr_employee_language` |
| `sshr_employee_position` |
| `sshr_employee_project` |
| `sshr_employee_promotion` |
| `sshr_examination_test` |
| `sshr_experience` |
| `sshr_job` |
| `sshr_level_studies` |
| `sshr_posit_sub_title` |
| `sshr_position_title` |
| `sshr_qapplicants` |
| `sshr_qeducation` |
| `sshr_qinterview` |
| `sshr_qlanguages` |
| `sshr_qlicenses` |
| `sshr_qskills` |
| `sshr_qtesting` |
| `sshr_qwork_expirence` |
| `sshr_race` |
| `sshr_reportto` |
| `sshr_responsibilities` |
| `sshr_rules_concours` |
| `sshr_rules_education` |
| `sshr_rules_experience` |
| `sshr_rules_skills` |
| `sshr_rules_trainings` |
| `sshr_salary_component` |
| `sshr_salary_grade` |
| `sshr_skills` |
| `sshr_specialization` |
| `sshr_tcourses` |
| `sshr_training` |
| `sshr_training_calendar` |
| `sshr_training_type` |
| `sshr_trainingline` |
| `sshr_type_examination` |
| `sshr_type_project` |
| `sshr_types_test` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sshr_activity` | sshr_activity | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_activity_key`; Cols: value, name, description; `SSHR_ACTIVITY_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_applicant` | sshr_applicant | — | — | ad_client_id→ad_client; sshr_disability_id→sshr_disability; sshr_level_studies_id→sshr_level_studies; ad_org_id→ad_org; sshr_skills_id→sshr_skills (+1) | Detalle enlazado a ad_client, sshr_disability, sshr_level_studies. | PK `sshr_applicant_id_key`; Cols: name, documenttype, documentno, gender, sshr_disability_id; `SSHR_APPLICANT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_applicant_concours` | sshr_applicant_concours | — | — | sshr_applicant_id→sshr_applicant; ad_client_id→ad_client; ad_org_id→ad_org; sshr_rules_concours_id→sshr_rules_concours | Detalle enlazado a ad_client, ad_org, sshr_applicant. | PK `sshr_applicantc_id_key`; Cols: sshr_applicant_id, sshr_rules_concours_id; `SSHR_APPLICANTC_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_ch_int_ext` | sshr_ch_int_ext | — | — | sshr_ext_id→c_bpartner; sshr_int_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org; sshr_employee_position_id→sshr_employee_position | Detalle enlazado a ad_client, c_bpartner. | PK `sshr_ch_int_ext_key`; Cols: observation, sshr_employee_position_id, sshr_int_id, sshr_ext_id; `SSHR_CH_INT_EXT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_ch_responsibilities` | sshr_ch_responsibilities | — | — | sshr_employee_position_id→sshr_employee_position; ad_client_id→ad_client; ad_org_id→ad_org; sshr_responsibilities_id→sshr_responsibilities; sspr_position_id→sspr_position | Detalle enlazado a ad_client, ad_org, sshr_employee_position. | PK `sshr_ch_responsibilities_key`; Cols: sshr_responsibilities_id, frecuency, consequence, complexity, total; `SSHR_CH_RESPON_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_cha_activity` | sshr_cha_activity | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sshr_activity_id→sshr_activity; sshr_employee_position_id→sshr_employee_position; sspr_position_id→sspr_position | Detalle enlazado a ad_client, ad_org, sshr_activity. | PK `sshr_cha_activity_key`; Cols: sshr_activity_id, frecuency, consequence, complexity, total; `SSHR_CHA_ACT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_competence` | sshr_competence | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sshr_employee_position_id→sshr_employee_position; sshr_skills_id→sshr_skills | Detalle enlazado a ad_client, ad_org, sshr_employee_position. | PK `sshr_competence_key`; Cols: sshr_skills_id, sshr_employee_position_id; `SSHR_COMPETENCE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_configure360` | sshr_configure360 | — | — | sspr_position_id→sspr_position; ad_client_id→ad_client; ad_org_id→ad_org | Parametrización / catálogo de soporte. | PK `sshr_configure360_key`; Cols: self_evaluation, pair, subordinate, supervisor, customer; `SSHR_CONFIGURE360_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_department` | sshr_department | — | — | c_costcenter_id→c_costcenter; ad_client_id→ad_client; c_location_id→c_location; ad_org_id→ad_org; department2_id→sshr_department | Detalle enlazado a ad_client, c_costcenter, c_location. | PK `sshr_department_id_key`; Cols: name, value, c_location_id, description, c_costcenter_id; `SSHR_DEPART_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_details_position` | sshr_details_position | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sspr_occupation_id→sspr_occupation; sshr_position_title_id→sshr_position_title | Detalle enlazado a ad_client, ad_org, sspr_occupation. | PK `sshr_details_post_key`; Cols: sshr_position_title_id, sspr_occupation_id; `SSHR_DETAILS_POS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_disability` | sshr_disability | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_disability_id_key`; Cols: name, description, value; `SSHR_DISAB_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_employee_language` | sshr_employee_language | — | — | ad_client_id→ad_client; ad_language_id→ad_language; ad_org_id→ad_org; c_bpartner_id→c_bpartner | Detalle enlazado a ad_client, ad_language, ad_org. | PK `sshr_employee_language_key`; Cols: c_bpartner_id, ad_language_id, writing_skills, spoken_skills, description; `SSHR_EPROJECT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_employee_position` | sshr_employee_position | — | — | ad_client_id→ad_client; sspr_position_id→sspr_position; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sspr_position. | PK `sshr_employee_position_key`; Cols: sspr_position_id, description; `SSHR_EMPL_POS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_employee_project` | sshr_employee_project | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sshr_type_project_id→sshr_type_project | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sshr_employee_project_key`; Cols: c_bpartner_id, sshr_type_project_id, startdate, enddate, description; `SSHR_EPROJECT1_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_employee_promotion` | sshr_employee_promotion | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sshr_position_id→sspr_position | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sshr_employee_promotion_key`; Cols: sshr_position_id, description, c_bpartner_id, sshr_datefrom, sshr_dateto; `SSHR_EPROMOTION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_examination_test` | sshr_examination_test | — | — | sshr_types_test_id→sshr_types_test; ad_org_id→ad_org; c_bpartner_id→c_bpartner; ad_client_id→ad_client | Detalle enlazado a ad_org, c_bpartner, sshr_types_test. | PK `sshr_examination_test_key`; Cols: c_bpartner_id, examination_date, examination_score, description, sshr_types_test_id; `SSHR_TEXAMINATION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_experience` | sshr_experience | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_experience_key`; Cols: value, name, description; `SSHR_EXPERIENCE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_job` | sshr_job | `SSHR_JOB_POST_TRG1`; `SSHR_JOB_TRG1` | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; sshr_department_id→sshr_department; c_location_id→c_location; ad_org_id→ad_org (+3) | Detalle enlazado a ad_client, c_bpartner, sshr_department. Validado por trigger(s): SSHR_JOB_POST_TRG1, SSHR_JOB_TRG1. | PK `sshr_job_id_key`; Cols: c_bpartner_id, sshr_position_title_id, sshr_department_id, c_location_id, start_date; `SSHR_JOB_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_level_studies` | sshr_level_studies | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_level_studies_id_key`; Cols: value, name, description; `SSHR_EVELSTUDISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_posit_sub_title` | sshr_posit_sub_title | — | — | ad_org_id→ad_org; ad_client_id→ad_client | Detalle enlazado a ad_client, ad_org. | PK `sshr_posit_sub_title_id_key`; Cols: name, description, value, position_totalno, positions_occupied; `SSHR_POSTITLE_SUB_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_position_title` | sshr_position_title | `SSHR_POSITION_TRG1` | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. Validado por trigger(s): SSHR_POSITION_TRG1. | PK `sshr_position_title_id_key`; Cols: name, description, value, position_totalno, positions_occupied; `SSHR_POS_TITLE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_qapplicants` | sshr_qapplicants | — | — | sshr_applicant_concours_id→sshr_applicant_concours; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sshr_applicant_concours. | PK `sshr_qapplicants_id_key`; Cols: approved_trainings, approved_experience, approved_instruccion, sshr_applicant_concours_id; `SSHR_QAPPLICANTS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_qeducation` | sshr_qeducation | — | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; sshr_c_country_id→c_country; sshr_level_studies_id→sshr_level_studies; ad_org_id→ad_org (+1) | Detalle enlazado a ad_client, c_bpartner, c_country. | PK `sshr_qeducation_id_key`; Cols: c_bpartner_id, years, date_start, date_end, sshr_c_country_id; `SSHR_QEDUC_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_qinterview` | sshr_qinterview | — | — | sshr_applicant_concours_id→sshr_applicant_concours; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sshr_applicant_concours. | PK `sshr_qinterview_id_key`; Cols: score_interview, sshr_applicant_concours_id; `SSHR_QINTERVIEW_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_qlanguages` | sshr_qlanguages | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_qlanguages_id_key`; Cols: language, fluency, competency, comments; `SSHR_QLANGUA_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_qlicenses` | sshr_qlicenses | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_qlicenses_id_key`; Cols: name, licensenumber, date_issued, date_expiry; `SSHR_QLICENCES_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_qskills` | sshr_qskills | — | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sshr_qskills_id_key`; Cols: c_bpartner_id, skills, comments; `SSHR_QSKILL_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_qtesting` | sshr_qtesting | `SSHR_QTESTING_TRG1` | — | sshr_applicant_concours_id→sshr_applicant_concours; ad_client_id→ad_client; ad_org_id→ad_org; sshr_types_test_psycho→sshr_types_test; sshr_types_test_know→sshr_types_test | Detalle enlazado a ad_client, ad_org, sshr_applicant_concours. Validado por trigger(s): SSHR_QTESTING_TRG1. | PK `sshr_qtesting_id_key`; Cols: sshr_types_test_know, score_tknowledge, sshr_types_test_psycho, score_tpsychology, total; `SSHR_QTESTING_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_qwork_expirence` | sshr_qwork_expirence | — | — | ad_org_id→ad_org; c_bpartner_id→c_bpartner; ad_client_id→ad_client | Detalle enlazado a ad_client, ad_org, c_bpartner. | PK `sshr_qwork_expirence_id_key`; Cols: c_bpartner_id, company, job_title, date_from, date_to; `SSHR_QWORK_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_race` | sshr_race | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_race_id_key`; Cols: name, description; `SSHR_RACE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_reportto` | sshr_reportto | — | — | c_bpartner_alt→c_bpartner; c_bpartner_boss→c_bpartner; c_bpartner_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a c_bpartner. | PK `sshr_reportto_id_key`; Cols: c_bpartner_id, c_bpartner_boss, c_bpartner_alt, description; `SSHR_REPORT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_responsibilities` | sshr_responsibilities | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_responsibilities_key`; Cols: value, name, description; `SSHR_RESPON_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_rules_concours` | sshr_rules_concours | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sshr_employee_position_id→sshr_position_title; sshr_salary_grade_id→sshr_salary_grade; sshr_department_id→sshr_department | Detalle enlazado a ad_client, ad_org, sshr_position_title. | PK `sshr_rconcours_id_key`; Cols: sshr_employee_position_id, sshr_department_id, sshr_salary_grade_id, amount_salary, name; `SSHR_RCONCOURS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_rules_education` | sshr_rules_education | — | — | ad_client_id→ad_client; sshr_level_studies_id→sshr_level_studies; ad_org_id→ad_org; sshr_rules_concours_id→sshr_rules_concours; sshr_specialization_id→sshr_specialization | Detalle enlazado a ad_client, ad_org, sshr_level_studies. | PK `sshr_reducation_id_key`; Cols: sshr_level_studies_id, sshr_specialization_id, sshr_rules_concours_id; `SSHR_REDUCATION_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_rules_experience` | sshr_rules_experience | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sshr_rules_concours_id→sshr_rules_concours; sshr_experience_id→sshr_experience | Detalle enlazado a ad_client, ad_org, sshr_rules_concours. | PK `sshr_rexperience_id_key`; Cols: years_experience, desc_experience, sshr_rules_concours_id, sshr_experience_id; `SSHR_REXPERIENCE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_rules_skills` | sshr_rules_skills | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sshr_rules_concours_id→sshr_rules_concours; sshr_skills_id→sshr_skills | Detalle enlazado a ad_client, ad_org, sshr_rules_concours. | PK `sshr_rskills_id_key`; Cols: sshr_skills_id, sshr_rules_concours_id; `SSHR_RSKILLS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_rules_trainings` | sshr_rules_trainings | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sshr_rules_concours_id→sshr_rules_concours | Detalle enlazado a ad_client, ad_org, sshr_rules_concours. | PK `sshr_rtrainings_id_key`; Cols: hours_trainings, desc_trainings, sshr_rules_concours_id; `SSHR_RTRAININGS_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_salary_component` | sshr_salary_component | — | — | c_bpartner_id→c_bpartner; ad_client_id→ad_client; c_currency_id→c_currency; ad_org_id→ad_org; sshr_salary_grade_id→sshr_salary_grade | Detalle enlazado a ad_client, c_bpartner, c_currency. | PK `sshr_salary_component_id_key`; Cols: c_bpartner_id, sshr_salary_grade_id, salary_component, frecuency, c_currency_id; `SSHR_SALARYC_DEPOSIT_CHK`: ISDIRECTDEPOSIT IN ('Y', 'N'); `SSHR_SALARYC_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_salary_grade` | sshr_salary_grade | `SSHR_SALARY_GRADE_TRG1` | — | ad_client_id→ad_client; c_currency→c_currency; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_currency. Validado por trigger(s): SSHR_SALARY_GRADE_TRG1. | PK `sshr_salary_grade_id_key`; Cols: name, description, salary_min, salary_max, c_currency; `SSHR_SALARYG_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_skills` | sshr_skills | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_skills_id_key`; Cols: value, name, description, sshr_position_sk; `SSHR_SKILISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_specialization` | sshr_specialization | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sshr_level_studies_id→sshr_level_studies | Detalle enlazado a ad_client, ad_org, sshr_level_studies. | PK `sshr_especialization_key`; Cols: value, name, description, sshr_level_studies_id; `SSHR_ESP_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_tcourses` | sshr_tcourses | — | — | c_bpartner_id→c_bpartner; sshr_training_id→sshr_training; sshr_training_type_id→sshr_training_type; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a c_bpartner, sshr_training, sshr_training_type. | PK `sshr_tcourses_key`; Cols: sshr_training_id, sshr_training_type_id, nohours, startdate, enddate; `SSHR_TCOURSES_INT_EXT_CHK`: INTERNAL_EXTERNAL IN ('Y', 'N'); `SSHR_TCOURSES_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_training` | sshr_training | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_training_id_key`; Cols: value, name; `SSHR_TRAIN_ISACTIVE_FK`: ISACTIVE IN ('Y', 'N') |
| `sshr_training_calendar` | sshr_training_calendar | — | — | sshr_training_id→sshr_training; ad_client_id→ad_client; ad_org_id→ad_org; c_bpartner_id→c_bpartner; sshr_training_type_id→sshr_training_type | Detalle enlazado a ad_client, ad_org, sshr_training. | PK `sshr_training_calendar_key`; Cols: description, nohours, startdate, enddate, certified; `SSHR_TRAINING_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_training_type` | sshr_training_type | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_training_type_key`; Cols: value, name; `SSHR_TTYPE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_trainingline` | sshr_trainingline | `SSHR_TRAINING_EMPLOYEE_TRG` | — | sshr_training_calendar_id→sshr_training_calendar; c_bpartner_id→c_bpartner; ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, c_bpartner, sshr_training_calendar. Validado por trigger(s): SSHR_TRAINING_EMPLOYEE_TRG. | PK `sshr_trainingline_id_key`; Cols: c_bpartner_id, assistance, training_status, startdate, enddate; `SSHR_TRAININGLINE_ISACTIVE_FK`: ISACTIVE IN ('Y', 'N') |
| `sshr_type_examination` | sshr_type_examination | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_type_examination_key`; Cols: value, name, description; `SSHR_TEXAM1_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_type_project` | sshr_type_project | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sshr_type_project_key`; Cols: value, name, description; `SSHR_TPROJECT_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `sshr_types_test` | sshr_types_test | — | — | ad_client_id→ad_client; ad_org_id→ad_org; sshr_position_title_id→sshr_position_title | Detalle enlazado a ad_client, ad_org, sshr_position_title. | PK `sshr_types_test_id_key`; Cols: name, score_max, score_min, sshr_position_title_id, tests_knowledge; `SSHR_TYP_QTESTING_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sshr_activity` |
| `sshr_applicant` |
| `sshr_applicant_concours` |
| `sshr_ch_int_ext` |
| `sshr_ch_responsibilities` |
| `sshr_cha_activity` |
| `sshr_competence` |
| `sshr_configure360` |
| `sshr_department` |
| `sshr_details_position` |
| `sshr_disability` |
| `sshr_employee_language` |
| `sshr_employee_position` |
| `sshr_employee_project` |
| `sshr_employee_promotion` |
| `sshr_examination_test` |
| `sshr_experience` |
| `sshr_job` |
| `sshr_level_studies` |
| `sshr_posit_sub_title` |
| `sshr_position_title` |
| `sshr_qapplicants` |
| `sshr_qeducation` |
| `sshr_qinterview` |
| `sshr_qlanguages` |
| `sshr_qlicenses` |
| `sshr_qskills` |
| `sshr_qtesting` |
| `sshr_qwork_expirence` |
| `sshr_race` |
| `sshr_reportto` |
| `sshr_responsibilities` |
| `sshr_rules_concours` |
| `sshr_rules_education` |
| `sshr_rules_experience` |
| `sshr_rules_skills` |
| `sshr_rules_trainings` |
| `sshr_salary_component` |
| `sshr_salary_grade` |
| `sshr_skills` |
| `sshr_specialization` |
| `sshr_tcourses` |
| `sshr_training` |
| `sshr_training_calendar` |
| `sshr_training_type` |
| `sshr_trainingline` |
| `sshr_type_examination` |
| `sshr_type_project` |
| `sshr_types_test` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_USER`, `C_BPARTNER`, `SSPR_FAMILY`, `SSPR_LEAVE_EMP`, `SSPR_SHIFT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación a través del módulo de Recursos Humanos se realiza mediante un conjunto de ventanas específicas como Activity, Applicant y Employee Position. Los usuarios pueden acceder a estas ventanas a través del menú de navegación de Openbravo, lo que proporciona un acceso intuitivo y organizado a las diversas funcionalidades del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Activity | Activity |
| Applicant | Applicant |
| Bank | Bank |
| Cargo/Position | Cargo/Position |
| Configure360 | Configure360 |
| Departament | Departament |
| Disability | Disability |
| Employee Position | Employee Position |
| Experience | Experience |
| Job Specifications | Job Specifications |
| Languages | Languages |
| Level Studies | Level Studies |
| Licenses | Licenses |
| Personal | Personal |
| Proffesional Tittle | Proffesional Tittle |
| Race | Race |
| Responsibilities | Responsibilities |
| Rulers Concuors | Rulers Concuors |
| Salary Grade | Salary Grade |
| Skills | Skills |
| Specialization | Specialization |
| Training | Training |
| Training TYpe | Training TYpe |
| Type Examination | Type Examination |
| Type Project | Type Project |
| Types Test | Types Test |
| Work Shift | Work Shift |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Activity | Activity | No |
| Administrator | Administrator | Sí |
| Applicant | Applicant | No |
| Bank | Bank | No |
| Cargo/Position | Cargo/Position | No |
| Configure360 | Configure360 | No |
| Departament | Departament | No |
| Disability | Disability | No |
| Employee | Employee | Sí |
| Employee Position | Employee Position | No |
| Experience | Experience | No |
| Human Resource Management | Human Resource Management | Sí |
| Information | Information | Sí |
| Job Specifications | Job Specifications | No |
| Level Studies | Level Studies | No |
| Personal | Personal | No |
| Position | Position | Sí |
| Proffesional Tittle | Proffesional Tittle | No |
| Qualify Applicant | Qualify Applicant | No |
| Race | Race | No |
| Recluitment | Recluitment | Sí |
| Responsibilities | Responsibilities | No |
| Rulers Concuors | Rulers Concuors | No |
| Salary Grade | Salary Grade | No |
| Set Up | Set Up | Sí |
| Set up | Set up | Sí |
| Setup | Setup | Sí |
| Skills | Skills | No |
| Specialization | Specialization | No |
| Training | Training | No |
| Training TYpe | Training TYpe | No |
| Trainings | Trainings | Sí |
| Transactions | Transactions | Sí |
| Transactions | Transactions | Sí |
| Transactions | Transactions | Sí |
| Type Examination | Type Examination | No |
| Type Project | Type Project | No |
| Types | Types | Sí |
| Types Test | Types Test | No |
| Work Shift | Work Shift | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

<!-- knowledge-extract:window_specs -->
### Ventana: Activity

- **AD_WINDOW_ID:** `7371368A1B364DE4ABDC5299F1285DB9`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Activity | `C241029961754B9881642089277CE256` | 0 |

### Ventana: Applicant

- **AD_WINDOW_ID:** `7D845C3DEC5841A390D12AF1C77582D5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Applicant | `821E5B4B8EDA427AA663E068853857DB` | 0 |

### Ventana: Bank

- **AD_WINDOW_ID:** `E054587120C44F19B287662C234970D5`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Bank | `296` | 0 |

### Ventana: Cargo/Position

- **AD_WINDOW_ID:** `93800A7CD765483F9AE210A4B8A9DE3C`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Cargo/Position | `770F8CD42B4D4E0AB981F0F1CDC29B48` | 0 |

### Ventana: Configure360

- **AD_WINDOW_ID:** `2C82EE620B244C2095BD98EA8FCCA02D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Configure360 | `AD522F298DDD4F2EAE6E3ACF515B6077` | 0 |

### Ventana: Departament

- **AD_WINDOW_ID:** `B357680866CA4494B16B93E4A0B8D51F`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Departament | `D7234B914BC7492D8530021A12DDEDDE` | 0 |

### Ventana: Disability

- **AD_WINDOW_ID:** `826E55E8FE9F46A483171272DE8B3C58`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Disability | `E398779B11C044E790A6B97DF109090D` | 0 |

### Ventana: Employee Position

- **AD_WINDOW_ID:** `828A477A184A4B9A94BB0B612F0510E2`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Employee Position | `F7B63658461548A586C33645186502FD` | 0 |
| 20 | Activity | `AC4923881CBD4994992707F8423D8D31` | 1 |
| 30 | Responsabilities | `DB9A8822142A40E8B26CDCC0C0EE37BF` | 1 |
| 40 | Competence | `41BA0D84B1E448E38AE5D09BA55B078E` | 1 |
| 50 | Relation Int / Ext | `9AFC8CC4C1DE4D9E81DAAB1E4968B803` | 1 |

### Ventana: Experience

- **AD_WINDOW_ID:** `28FFD15B4C924EEE9596ACD7463E5E5F`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Experience | `86E659678E094C76BCEE5838CF9C0E72` | 0 |

### Ventana: Job Specifications

- **AD_WINDOW_ID:** `0C00F2DE39D641C2BE1EE9865C7CB5C7`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Job Specifications | `A1C36D3250324D33B4EE7F1CF048BC94` | 0 |

### Ventana: Languages

- **AD_WINDOW_ID:** `DBD7B821538F4A19850E7007F7BB18F5`

### Ventana: Level Studies

- **AD_WINDOW_ID:** `B9F25CD2BD97411786BC916913DD9214`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Level Studies | `8451628121804BE7802F5C00E4100D87` | 0 |

### Ventana: Licenses

- **AD_WINDOW_ID:** `4BF0EC849DB54A71B18050B4CF1ED3A3`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Licenses | `CD0BEDC089F74B7D9757B5BFA0D9DA13` | 0 |

### Ventana: Personal

- **AD_WINDOW_ID:** `8BA09A447EA4418DBFF0347E45C49A82`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Employee | `291` | 0 |
| 120 | Report to | `D5EDB5E1758945019EA6F96F00156865` | 1 |
| 130 | Work Experience | `F39F4F67732D49F2AFB681F07B62A5E2` | 1 |
| 140 | Education | `05453468834F4CFD90E0B0AB5BFF94B7` | 1 |
| 150 | Skills | `ABEB1C55DA8A41B3826AEE4FF2F6F45A` | 1 |
| 160 | Training Courses | `6D998ACDC3E94F799282F94CAA280193` | 1 |
| 170 | Family | `430BB1DC1B49499D88249287FB058A12` | 1 |
| 180 | Language | `631CCDEF06874D9BB176E3CE018E3297` | 1 |
| 190 | Examination Test | `55F6AD6D0A8A437996ABA23C38A8469C` | 1 |
| 20 | Location/Address | `293` | 1 |
| 200 | Project | `5774DDD7DC1943DDA0734CB9B215E0A9` | 1 |
| 21 | Contact Emergency | `114` | 1 |
| 210 | Promotion | `176C8236B0044608952472773485E38F` | 1 |
| 30 | Bank Account | `298` | 1 |
| 60 | Contract | `470C94417A3A49B2B742E688B956E5F9` | 1 |
| 70 | Contract Position | `831CEEDC9E254FD182EEEFA5F792F337` | 2 |

### Ventana: Proffesional Tittle

- **AD_WINDOW_ID:** `E1EA9C6D0D9C4EE399D36E3AA5277EC1`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Proffesional Tittle | `14763F62A0334F8FAF03A12C305F4986` | 0 |

### Ventana: Race

- **AD_WINDOW_ID:** `F3F596AA46C14E359A3E46C5E9F722F0`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Race | `BA25D2B4E68A4ED4A1E60E51A3DC81E4` | 0 |

### Ventana: Responsibilities

- **AD_WINDOW_ID:** `ED3EC2A028384DB68C0EB100772B5A02`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Responsibilities | `3DC5A335C84B4AA18E11111F343747EF` | 0 |

### Ventana: Rulers Concuors

- **AD_WINDOW_ID:** `3986A566728F456EA3DEB1BFD43F719A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 100 | Qualification Interview | `7887F5302E9A43368694C871856226F4` | 2 |
| 20 | Rules Concours | `F299D2A6C5954560B681626E002EBB17` | 0 |
| 30 | Academic Formation | `8D1D0427A001487385CB1772B95DB685` | 1 |
| 40 | Trainings | `394F9EF661D44918ABDF307D04B18673` | 1 |
| 50 | Experience | `7531DB6557AF4CACA04CCAA436878EC3` | 1 |
| 60 | Skills | `7F01E7741ABF4C4FAD023F4E0F8B89DF` | 1 |
| 70 | Applicant | `2F765E6D899F4113A641EE984EB43C3D` | 1 |
| 80 | Qualification Applicant | `402A69786B514227AC8C0A333256EC07` | 2 |
| 90 | Qualification Testing | `9DC658A7AD7641A19752F314BA6E544D` | 2 |

### Ventana: Salary Grade

- **AD_WINDOW_ID:** `761048DB739F42F88CFF9EE2ACE819D9`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Salary Grade | `9D8279BBAB034233A1AB93AC80A65C13` | 0 |

### Ventana: Skills

- **AD_WINDOW_ID:** `9A8BFC48104740489E2361D52B088DCE`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Skills | `C337807C99EB48CEA4A4A16346A980D8` | 0 |

### Ventana: Specialization

- **AD_WINDOW_ID:** `0B03C79F6B6B4A75A7139E9D93231640`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Specialization | `0CAD084012454CE9A201D67CE3AA3C0B` | 0 |

### Ventana: Training

- **AD_WINDOW_ID:** `FB6FB675F77846E9B13323B4F46BBD4D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Training | `04A8D9DA48A54132AA590A2B6F82B101` | 0 |
| 20 | Calendar Training | `EB5AADE030424813870AC4F8CE8A3AEB` | 1 |
| 30 | Internal Training | `6DAE5BCB916344F29526D32522AC35BD` | 2 |
| 40 | External Training | `6D998ACDC3E94F799282F94CAA280193` | 1 |

### Ventana: Training TYpe

- **AD_WINDOW_ID:** `FA1D0184CD7E47D5BA16A3B02D47E779`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Training Type | `A03FA389EEA4422A9CF2A29C2A2A90E9` | 0 |

### Ventana: Type Examination

- **AD_WINDOW_ID:** `158465A0FB8B4C66A8E58AD3353CDBCC`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Type Examiniation | `B86D8E7AC5F8418A922AF66A606E70D8` | 0 |

### Ventana: Type Project

- **AD_WINDOW_ID:** `A095F2934B904926ACC6BC4CD018A845`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Type Project | `D162F3B4AFE4433E81187BEDC58D15EC` | 0 |

### Ventana: Types Test

- **AD_WINDOW_ID:** `AF37B8FBBF5E4C84B870484F8459AA0B`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Types Test | `E56BFB68086741558315F093CBDADF60` | 0 |

### Ventana: Work Shift

- **AD_WINDOW_ID:** `2C5C627DC9F847E6A30DC4418A037494`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Shift | `B1130944B7D04699BCBBD5BFD1110E5B` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Configure360 (ventana: Configure360)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Self_Evaluation | `Self_Evaluation` | No | No | — |
| 50 | Pair | `Pair` | No | No | — |
| 60 | Subordinate | `Subordinate` | No | No | — |
| 70 | Supervisor | `Supervisor` | No | No | — |
| 80 | Customer | `Customer` | No | No | — |
| 90 | Position | `Sspr_Position_ID` | No | No | — |
| 100 | Active | `Isactive` | No | No | — |

### Contract Position (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Contract | `—` | No | Sí | — |
| 50 | Position | `—` | No | No | — |
| 60 | Starting Date | `—` | No | No | 9EFB2074D9B847A594DE30D052CACBA9 |
| 70 | Ending Date | `—` | No | No | 9EFB2074D9B847A594DE30D052CACBA9 |

### Job Specifications (ventana: Job Specifications)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Name | `—` | No | No | — |
| 50 | Pdt Code | `—` | No | No | — |
| 60 | Description | `—` | No | No | — |

### Language (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Language | `AD_Language_ID` | No | No | — |
| 40 | Writing_Skills | `Writing_Skills` | No | No | — |
| 50 | Spoken_Skills | `Spoken_Skills` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |

### Project (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Type Project | `Sshr_Type_Project_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Description | `Description` | No | No | — |
| 80 | Active | `Isactive` | No | No | — |

### Pestaña `1AEAAD595A9145DA8A94E3B0FB9C18C0`

- **AD_TAB_ID:** `1AEAAD595A9145DA8A94E3B0FB9C18C0` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 250 | Gender | `EM_Sshr_Gender` | No | No | — |
| 280 | Department | `EM_Sshr_Department_ID` | No | No | — |

### Rules Concours (ventana: Rulers Concuors)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Date | `modified_date` | No | No | — |
| 60 | Department | `Sshr_Department_ID` | No | No | — |
| 70 | Position | `Sshr_Employee_Position_ID` | No | No | — |
| 80 | No. vacancies | `Novacancies` | No | No | — |
| 90 | Salary Grade | `Sshr_Salary_Grade_ID` | No | No | — |
| 100 | Amount Salary | `Amount_Salary` | No | No | — |

### Specialization (ventana: Specialization)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Level Studies | `Sshr_Level_Studies_ID` | No | No | — |
| 70 | Description | `Description` | No | No | — |

### Competence (ventana: Employee Position)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Skills | `Sshr_Skills_ID` | No | No | — |
| 60 | Active | `Isactive` | No | No | — |

### Skills (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 50 | Skills | `Skills` | No | No | — |
| 70 | Comments | `Comments` | No | No | — |

### Training Type (ventana: Training TYpe)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Identifier | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Employee Position (ventana: Employee Position)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Position | `Sspr_Position_ID` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 60 | Active | `Isactive` | No | No | — |

### Relation Int / Ext (ventana: Employee Position)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Comments | `Observation` | No | No | — |
| 60 | Internal | `Sshr_Int_ID` | No | No | — |
| 70 | External | `Sshr_Ext_ID` | No | No | — |
| 80 | Active | `Isactive` | No | No | — |

### Skills (ventana: Skills)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |
| 80 | Position | `Sshr_Position_Sk` | No | No | — |

### Activity (ventana: Activity)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Identifier | `Value` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |

### Bank (ventana: Bank)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Name | `—` | No | No | — |

### Activity (ventana: Employee Position)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Activity | `Sshr_Activity_ID` | No | No | — |
| 50 | Frequency | `Frecuency` | No | No | — |
| 60 | Consequence | `Consequence` | No | No | — |
| 70 | Complexity | `Complexity` | No | No | — |
| 80 | Total | `Total` | No | No | — |
| 100 | Permanence | `Permanence` | No | No | — |
| 120 | Active | `Isactive` | No | No | — |

### Pestaña `3FE490095FAE4E248BCF4E8E62811649`

- **AD_TAB_ID:** `3FE490095FAE4E248BCF4E8E62811649` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 290 | Department | `EM_Sshr_Department_ID` | No | Sí | — |

### Internal Training (ventana: Training)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Employee | `C_Bpartner_ID` | No | No | — |
| 60 | Assistance | `Assistance` | No | No | — |
| 70 | Training Status | `Training_Status` | No | No | — |
| 80 | Starting Date | `Startdate` | No | No | — |
| 90 | Ending Date | `Enddate` | No | No | — |
| 100 | Training Institute | `Training_Institute` | No | No | — |
| 110 | No. Hours | `Nohours` | No | No | — |
| 120 | Qualification | `Qualification` | No | No | — |
| 140 | Description | `Description` | No | No | — |
| 150 | Active | `Isactive` | No | No | — |

### Location/Address (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Employee | `—` | No | Sí | — |
| 50 | Location / Address | `—` | No | No | — |
| 60 | Phone | `—` | No | No | — |
| 70 | Alternative Phone | `—` | No | No | — |
| 80 | Fax | `—` | No | No | — |

### Contact Emergency (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | Sí | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Business Partner | `—` | No | Sí | — |
| 50 | First Name | `—` | No | No | — |
| 60 | Relationship | `EM_Sshr_Relationship` | No | No | — |
| 70 | Phone | `—` | No | No | — |
| 80 | Alternative Phone | `—` | No | No | — |
| 100 | Email | `—` | No | No | — |
| 190 | Allergies | `EM_Sshr_Description` | No | No | — |

### Promotion (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Employee Position | `Sshr_Position_ID` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |
| 70 | Date From | `Sshr_Datefrom` | No | No | — |
| 80 | Date To | `Sshr_Dateto` | No | No | — |

### Types Test (ventana: Types Test)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Position Title | `Sshr_Position_Title_ID` | No | No | — |
| 60 | Score Max | `Score_Max` | No | No | — |
| 70 | Score Min | `Score_Min` | No | No | — |
| 80 | Tests Knowledge | `Tests_Knowledge` | No | No | — |
| 90 | Tests Psychological | `Tests_Psychological` | No | No | — |

### Pestaña `69FCC96BB698405FBB2FD3F08714645D`

- **AD_TAB_ID:** `69FCC96BB698405FBB2FD3F08714645D` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 290 | Department | `EM_Sshr_Department_ID` | No | Sí | — |

### Type Examiniation (ventana: Type Examination)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Identifier | `Value` | No | No | — |
| 40 | Commercial Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |
| 60 | Active | `Isactive` | No | No | — |

### Training Courses (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Training | `Sshr_Training_ID` | No | No | — |
| 40 | Training Type | `Sshr_Training_Type_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Training Institute | `Training_Institute` | No | No | — |
| 80 | Place | `Place` | No | No | — |
| 90 | No. Hours | `Nohours` | No | No | — |
| 100 | Qualification | `Qualification` | No | No | — |
| 110 | Description | `Description` | No | No | — |

### Qualification Applicant (ventana: Rulers Concuors)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 50 | Approved Instruccion | `Approved_Instruccion` | No | No | — |
| 60 | Approved Experience | `Approved_Experience` | No | No | — |
| 70 | Approved Trainings | `Approved_Trainings` | No | No | — |

### Work Experience (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 50 | Company | `Company` | No | No | — |
| 60 | Job Title | `JOB_Title` | No | No | — |
| 70 | Date From | `Date_From` | No | No | — |
| 80 | Date To | `Date_To` | No | No | — |
| 90 | Comments | `Comments` | No | No | — |

### Pestaña `72136DA907314EB6B576C90E561D9E31`

- **AD_TAB_ID:** `72136DA907314EB6B576C90E561D9E31` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 120 | Description | `—` | No | No | — |

### Contract (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Employee | `—` | No | Sí | — |
| 50 | Format Type | `—` | No | No | — |
| 60 | Original Contract | `—` | No | No | — |
| 70 | Labor Regime | `—` | No | No | — |
| 80 | Starting Date | `—` | No | No | — |
| 90 | Ending Date | `—` | No | No | — |
| 100 | Permanent Remuneration | `—` | No | No | — |
| 110 | Contract Condition | `—` | No | No | — |
| 120 | Contract Type | `—` | No | No | — |
| 130 | Reason end Labor Relations | `—` | No | No | — |
| 140 | Night | `—` | No | No | — |
| 150 | Cumulative Regime | `—` | No | No | — |
| 160 | Activity | `—` | No | No | — |
| 170 | Employee Status | `—` | No | No | — |
| 180 | Maximum Working Hours | `—` | No | No | — |
| 190 | Hours per Week | `—` | No | No | — |
| 200 | Shift | `—` | No | No | — |
| 210 | Previous Income | `—` | No | No | 8BA9765D29804923A493AA6C925B77CB |
| 220 | Previous Withholding | `—` | No | No | 8BA9765D29804923A493AA6C925B77CB |

### Proffesional Tittle (ventana: Proffesional Tittle)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Total Position No. | `Position_Totalno` | No | No | — |
| 70 | Occupied Positions | `Positions_Occupied` | No | No | — |
| 80 | Available Positions | `Positions_Available` | No | Sí | — |
| 90 | Description | `Description` | No | No | — |

### Licenses (ventana: Licenses)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 60 | Number | `Licensenumber` | No | No | — |
| 70 | Date_Issued | `Date_Issued` | No | No | — |
| 80 | Date_Expiry | `Date_Expiry` | No | No | — |

### Calendar Training (ventana: Training)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | No. Hours | `Nohours` | No | No | — |
| 40 | No. person | `Noperson` | No | No | — |
| 50 | Training Type | `Sshr_Training_Type_ID` | No | No | — |
| 60 | Sponsor | `Sponsor` | No | No | — |
| 70 | Place | `Place` | No | No | — |
| 80 | Provider | `C_Bpartner_ID` | No | No | — |
| 90 | Certified by | `Certified` | No | No | — |
| 100 | Cost | `Cost` | No | No | — |
| 110 | Detail Cost | `Detail_Cost` | No | No | — |
| 130 | Starting Date | `Startdate` | No | No | — |
| 140 | Ending Date | `Enddate` | No | No | — |
| 150 | Starting Time | `Starttime` | No | No | — |
| 160 | Level | `Training_Level` | No | No | — |
| 170 | Materials | `Materials` | No | No | — |
| 180 | Reason | `Reason` | No | No | — |
| 190 | Priority | `Priority` | No | No | — |
| 200 | Description | `Description` | No | No | — |
| 210 | Active | `Isactive` | No | No | — |

### Salary Grade (ventana: Salary Grade)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Currency | `C_Currency` | No | No | — |
| 60 | Salary Min | `Salary_Min` | No | No | — |
| 70 | Salary Max | `Salary_Max` | No | No | — |
| 90 | Description | `Description` | No | No | — |

### Report to (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 50 | Boss | `C_Bpartner_Boss` | No | No | — |
| 60 | Business Partner | `C_Bpartner_Alt` | No | No | — |
| 70 | Description | `Description` | No | No | — |

### Applicant (ventana: Rulers Concuors)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 50 | Applicant | `Sshr_Applicant_ID` | No | No | — |

### Pestaña `9FCB0C531C9F4B088C7B38EB5F0C48A0`

- **AD_TAB_ID:** `9FCB0C531C9F4B088C7B38EB5F0C48A0` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 330 | Department | `EM_Sshr_Department_ID` | No | Sí | — |

### Departament (ventana: Departament)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Location / Address | `C_Location_ID` | No | No | — |
| 60 | Cost Center | `C_Costcenter_ID` | No | No | — |
| 65 | Parent Department | `Department2_ID` | No | No | — |
| 70 | Description | `Description` | No | No | — |
| 80 | Active | `Isactive` | No | No | — |

### Pestaña `AE4D0B14798E47A5B0CEF62C52DB235B`

- **AD_TAB_ID:** `AE4D0B14798E47A5B0CEF62C52DB235B` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 200 | Department | `EM_Sshr_Department_ID` | No | No | — |
| 205 | Professional Type | `EM_Sshr_Position_Title_ID` | No | No | — |
| 215 | Position Sub Rogado | `EM_Sshr_Posit_Sub_Title_ID` | No | No | — |

### Applicant (ventana: Applicant)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Date | `modified_date` | No | No | — |
| 60 | Document Type | `Documenttype` | No | No | — |
| 70 | Document No. | `Documentno` | No | No | — |
| 80 | Gender | `Gender` | No | No | — |
| 90 | Phone | `Phone` | No | No | — |
| 100 | Alternating Phone | `ALT_Phone` | No | No | — |
| 110 | Address | `Address` | No | No | — |
| 120 | Email | `Email` | No | No | — |
| 130 | Level Studies | `Sshr_Level_Studies_ID` | No | No | — |
| 140 | Specialization | `Sshr_Specialization_ID` | No | No | — |
| 150 | Description Experience | `Desc_Experience` | No | No | — |
| 160 | Years Experience | `Years_Experience` | No | No | — |
| 170 | Description Trainings | `Desc_Trainings` | No | No | — |
| 180 | Hours Trainings | `Hours_Trainings` | No | No | — |
| 190 | Skills | `Sshr_Skills_ID` | No | No | — |
| 200 | Salary Aspiration | `Salary_Aspiration` | No | No | — |
| 210 | Have Disability | `Disability_Chk` | No | No | — |
| 220 | Disability | `Sshr_Disability_ID` | No | No | — |
| 230 | Level Disability | `Level_Disab` | No | No | — |
| 240 | Nocard | `Nocard` | No | No | — |
| 250 | It is Suitable | `Sshr_Competent` | No | No | — |
| 260 | Office Employee | `Sshr_Position` | No | No | — |

### Experience (ventana: Experience)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Identifier | `Value` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |

### Experience (ventana: Rulers Concuors)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 50 | Description Experience | `Desc_Experience` | No | No | — |
| 60 | Years Experience | `Years_Experience` | No | No | — |
| 70 | Experience | `Sshr_Experience_ID` | No | No | — |
| 80 | Active | `Isactive` | No | No | — |

### Training (ventana: Training)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Identifier | `Value` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Trainings (ventana: Rulers Concuors)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Rules Concours | `Sshr_Rules_Concours_ID` | No | No | — |
| 50 | Description Trainings | `Desc_Trainings` | No | No | — |
| 60 | Hours Trainings | `Hours_Trainings` | No | No | — |

### Family (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Employee | `—` | No | Sí | — |
| 50 | Family Ties | `—` | No | No | — |
| 60 | First Name | `—` | No | No | — |
| 70 | Document Type Name | `—` | No | No | — |
| 80 | Document No | `—` | No | No | — |
| 90 | Birth of Day | `—` | No | No | — |
| 100 | Join Date | `—` | No | No | — |
| 110 | Level Studies | `EM_Sshr_Level_Studies_ID` | No | No | — |
| 120 | Have Disability | `EM_Sshr_Disability_Chk` | No | No | — |
| 130 | Type Disability | `EM_Sshr_Disability_ID` | No | No | — |
| 140 | Disability Card No. | `EM_Sshr_Nocard` | No | No | — |
| 150 | Level | `EM_Sshr_Level` | No | No | — |

### Employee (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Search Key | `—` | No | No | 123 |
| 50 | Commercial Name | `—` | No | No | — |
| 60 | Status | `—` | No | No | — |
| 70 | Birth of Day | `—` | No | No | — |
| 80 | Talla/Size | `EM_Sshr_Race` | No | No | — |
| 90 | Gender | `EM_Sshr_Gender` | No | No | — |
| 100 | Document Type Name | `—` | No | No | — |
| 110 | Document No | `—` | No | No | — |
| 120 | Shoes Size | `EM_Sshr_Militaryno` | No | No | — |
| 130 | Country | `EM_Sshr_Country` | No | No | — |
| 140 | Entry Date | `—` | No | No | — |
| 150 | Type Blood | `EM_Sshr_Typeblood` | No | No | — |
| 160 | Have Disability | `EM_Sshr_Disability_Chk` | No | No | — |
| 170 | Type Disability | `EM_Sshr_Disability` | No | No | — |
| 180 | Disability Card No. | `EM_Sshr_Nocard` | No | No | — |
| 190 | Level | `EM_Sshr_Level` | No | No | — |
| 200 | Email | `EM_Sshr_Email` | No | No | — |

### Type Project (ventana: Type Project)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Identifier | `Value` | No | No | — |
| 30 | Commercial Name | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |

### Level Studies (ventana: Level Studies)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Skills (ventana: Rulers Concuors)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 50 | Skills | `Sshr_Skills_ID` | No | No | — |

### Examination Test (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Examination Date | `Examination_Date` | No | No | — |
| 50 | Examination Score | `Examination_Score` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |
| 90 | Test Type | `Sshr_Types_Test_ID` | No | No | — |

### Responsabilities (ventana: Employee Position)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Responsibilities | `Sshr_Responsibilities_ID` | No | No | — |
| 50 | Frequency | `Frecuency` | No | No | — |
| 60 | Consequence | `Consequence` | No | No | — |
| 70 | Complexity | `Complexity` | No | No | — |
| 80 | Total | `Total` | No | No | — |
| 90 | Position | `Sspr_Position_ID` | No | No | — |
| 110 | Active | `Isactive` | No | No | — |

### Responsibilities (ventana: Responsibilities)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Identifier | `Value` | No | No | — |
| 50 | Commercial Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |

### Education (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Business Partner | `C_Bpartner_ID` | No | Sí | — |
| 50 | Level Studies | `Sshr_Level_Studies_ID` | No | No | — |
| 60 | Specialization | `Sshr_Specialization_ID` | No | No | — |
| 70 | Years | `Years` | No | No | — |
| 80 | Start Date | `Date_Start` | No | No | — |
| 90 | End Date | `Date_End` | No | No | — |
| 100 | Country | `Sshr_C_Country_ID` | No | No | — |

### Shift (ventana: Work Shift)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Position | `—` | No | No | — |
| 50 | EM_Sshr_Hourstart | `EM_Sshr_Hourstart` | No | No | — |
| 60 | EM_Sshr_Hourend | `EM_Sshr_Hourend` | No | No | — |

### Academic Formation (ventana: Rulers Concuors)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Rules Concours | `Sshr_Rules_Concours_ID` | No | No | — |
| 50 | Level Studies | `Sshr_Level_Studies_ID` | No | No | — |
| 60 | Specialization | `Sshr_Specialization_ID` | No | No | — |

### Qualification Testing (ventana: Rulers Concuors)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Client | `AD_Client_ID` | No | No | — |
| 30 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Active | `Isactive` | No | No | — |
| 50 | Test knowledge | `Sshr_Types_Test_Know` | No | No | — |
| 60 | Score Test knowledge | `Score_Tknowledge` | No | No | — |
| 70 | Test Psychology | `Sshr_Types_Test_Psycho` | No | No | — |
| 80 | Score Test psychology | `Score_Tpsychology` | No | No | — |
| 90 | Total | `Total` | No | No | — |

### External Training (ventana: Training)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 25 | Employee | `C_Bpartner_ID` | No | No | — |
| 40 | Training Type | `Sshr_Training_Type_ID` | No | No | — |
| 50 | Starting Date | `Startdate` | No | No | — |
| 60 | Ending Date | `Enddate` | No | No | — |
| 70 | Training Institute | `Training_Institute` | No | No | — |
| 80 | Place | `Place` | No | No | — |
| 90 | No. Hours | `Nohours` | No | No | — |
| 100 | Qualification | `Qualification` | No | No | — |
| 110 | Description | `Description` | No | No | — |
| 130 | Active | `Isactive` | No | No | — |

### Cargo/Position (ventana: Cargo/Position)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Position | `Name` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Identifier | `Value` | No | No | — |
| 60 | Total Position No. | `Position_Totalno` | No | No | — |
| 70 | Occupied Positions | `Positions_Occupied` | No | No | — |

### Disability (ventana: Disability)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Search Key | `Value` | No | No | — |
| 50 | Name | `Name` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Qualification Interview (ventana: Rulers Concuors)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Score Interview | `Score_Interview` | No | No | — |

### Pestaña `FAD8E5E902BB4A67AA7EACC40645FB44`

- **AD_TAB_ID:** `FAD8E5E902BB4A67AA7EACC40645FB44` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 330 | Department | `EM_Sshr_Department_ID` | No | Sí | — |

### Race (ventana: Race)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `AD_Client_ID` | No | No | — |
| 20 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |

### Bank Account (ventana: Personal)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Client | `—` | No | No | — |
| 20 | Organization | `—` | No | No | — |
| 30 | Active | `—` | No | No | — |
| 40 | Employee | `—` | No | Sí | — |
| 50 | Account Type | `—` | No | No | — |
| 60 | Generic Account No. | `—` | No | No | — |
| 70 | Street | `—` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso que permite llevar a cabo acciones sobre la gestión de empleados y vacantes. Los botones típicos que un usuario encontrará son 'Completar', que permite finalizar un registro, y 'Retornar', que regresa a la pantalla anterior. Aunque no hay informes predefinidos, se implementan validaciones comunes, asegurando que los datos ingresados cumplen con los requisitos establecidos en la base de datos y están conformes con las políticas de la empresa.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en *(no se detectó módulo `.es_ES`; tablas usan solo en_US)*.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Qualify Applicant | Qualify Applicant | Qualify Applicant | `sshr_qualifyapplicant` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| Botón (PL/pgSQL) | Qualify Applicant | Qualify Applicant | Qualify Applicant | `sshr_qualifyapplicant` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Qualify Applicant | Qualify Applicant | PL `sshr_qualifyapplicant` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| `Sshr_MaxEmpTraining` | You have exceeded the number of places available for this Training course | You have exceeded the number of places available for this Training course | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sshr_MaxEmployee` | You can not take the same course two times | You can not take the same course two times | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo contiene clases Java que facilitan la implementación de lógica de negocio personalizada mediante callouts, permitiendo realizar acciones dinámicas basadas en las interacciones del usuario con el sistema, así como manipular datos en función de las entradas proporcionadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `com.sidesoft.ecuador.humanResources`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SS_Age` | ad_callouts | HttpSecureAppServlet | — | `src/com/sidesoft/ecuador/humanResources/ad_callouts/SS_Age.java` |
| `SS_NoDocumento` | ad_callouts | SimpleCallout | — | `src/com/sidesoft/ecuador/humanResources/ad_callouts/SS_NoDocumento.java` |
| `SS_Vacancies` | ad_callouts | HttpSecureAppServlet | — | `src/com/sidesoft/ecuador/humanResources/ad_callouts/SS_Vacancies.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSHR_COPY_EMAIL_TRG` | `c_bpartner` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSHR_JOB_POST_TRG1` | `sshr_job` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSHR_JOB_TRG1` | `sshr_job` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSHR_POSITION_TRG1` | `sshr_position_title` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSHR_QTESTING_TRG1` | `sshr_qtesting` | before INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSHR_SALARY_GRADE_TRG1` | `sshr_salary_grade` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SSHR_TRAINING_EMPLOYEE_TRG` | `sshr_trainingline` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `AVAILABLE POSITION HR` | `sshr_position_title.positions_available > 0` |
| AD_VAL_RULE | — | `Approved Testing Applicant HR` | `sshr_applicant_id in (select sshr_qtesting.sshr_applicant_id from sshr_qtesting where sshr_qtesting.approved_chk='Y')` |
| AD_VAL_RULE | — | `Specialization_HR` | `SSHR_SPECIALIZATION.SSHR_LEVEL_STUDIES_ID = @SSHR_LEVEL_STUDIES_ID@` |
| AD_VAL_RULE | — | `Approved Applicant HR` | `sshr_applicant_id in (select sshr_qapplicants.sshr_applicant_id from sshr_qapplicants where sshr_qapplicants.approved_tr` |
| AD_VAL_RULE | — | `Validate Department Leave` | `Sshr_Department.Sshr_Department_ID IN (select em_sshr_department_id from c_bpartner where c_bpartner_id = @c_bpartner_id` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y funciones PL/pgSQL desempeñan un rol crucial en el soporte del módulo, permitiendo la automatización de procesos y manteniendo la coherencia de datos mediante validaciones y actualizaciones en tiempo real. En total, hay siete triggers que se activan en acciones específicas dentro de las tablas relacionadas con Recursos Humanos, garantizando que el flujo de datos se maneje correctamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSHR_COPY_EMAIL_TRG` | `c_bpartner` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSHR_COPY_EMAIL_TRG.xml` |
| `SSHR_JOB_POST_TRG1` | `sshr_job` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSHR_JOB_POST_TRG1.xml` |
| `SSHR_JOB_TRG1` | `sshr_job` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSHR_JOB_TRG1.xml` |
| `SSHR_POSITION_TRG1` | `sshr_position_title` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSHR_POSITION_TRG1.xml` |
| `SSHR_QTESTING_TRG1` | `sshr_qtesting` | before | INSERT | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSHR_QTESTING_TRG1.xml` |
| `SSHR_SALARY_GRADE_TRG1` | `sshr_salary_grade` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSHR_SALARY_GRADE_TRG1.xml` |
| `SSHR_TRAINING_EMPLOYEE_TRG` | `sshr_trainingline` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSHR_TRAINING_EMPLOYEE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sshr_qualifyapplicant` | Qualify Applicant | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSHR_QUALIFYAPPLICANT.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Qualify Applicant | `Qualify Applicant` | Botón (PL/pgSQL) | PL `sshr_qualifyapplicant` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

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

Módulo: `com.sidesoft.ecuador.humanResources`.

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

# Glosario — prefijo `SSHR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSHR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `com.sidesoft.ecuador.humanResources` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Qualify Applicant` — Qualify Applicant

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Automatic Upload of Employee Data
**Package:** `ec.com.sidesoft.payroll.employee.data`

# Module overview — Sidesoft Automatic Upload of Employee Data

## Functional

El módulo 'Sidesoft Automatic Upload of Employee Data' está diseñado para facilitar la carga automática de datos de empleados en el sistema de nómina de Openbravo. Su propósito es optimizar la gestión de datos de recursos humanos, permitiendo que los usuarios del negocio, así como los desarrolladores y el soporte técnico, puedan integrar eficientemente la información de los empleados. Los actores principales incluyen el personal de recursos humanos, los administradores de nómina y los desarrolladores que mantienen el sistema. Este módulo depende de varios componentes, incluyendo el módulo de Gestión de Recursos Humanos y Nómina, así como de la compatibilidad con la '2.50 to 3.00 Compatibility Skin' y el núcleo de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payroll/employee/data` |
| Web | `web/ec.com.sidesoft.payroll.employee.data/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Human Resources Management - Payroll

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPEMPD`

# Guía de chat — Sidesoft Automatic Upload of Employee Data

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payroll.employee.data`).

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
- «¿Qué es la tabla sspempd_config_employee?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo cargar datos de empleados automáticamente?
- ¿Qué configuraciones debo hacer antes de la carga de datos?
- ¿Cómo puedo validar que los datos de un empleado son correctos?
- ¿Existen informes para verificar la carga de datos?
- ¿Qué pasos debo seguir para corregir un error en los datos de empleados?
- ¿Cuáles son las dependencias de este módulo?
- ¿Cómo accedo a las configuraciones generales por defecto?
- ¿Puedo agregar nuevos campos a la configuración de empleados?

# Domain — data model

## Functional

El modelo de datos se centra principalmente en la tabla 'sspempd_config_employee', que actúa como la entidad cabecera para la configuración de los datos del empleado. Aunque no se definieron etapas específicas, las relaciones presentes en la tabla permiten gestionar la información de forma centralizada. Este enfoque asegura que cualquier modificación a los datos del empleado se refleje adecuadamente en el sistema. Además, se observa que el módulo no implementa triggers ni funciones PL, lo que sugiere que las operaciones de carga de datos se gestionan de forma directa sin automatización a través de estas herramientas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sspempd_config_employee` |
| `sspempd_occupational_code` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sspempd_config_employee` | sspempd_config_employee | — | — | ad_client_id→ad_client; sspr_concept_id→sspr_concept; ad_org_id→ad_org; sspr_prolltemplate_id→sspr_prolltemplate; sspr_prolltemplate2_id→sspr_prolltemplate | Parametrización / catálogo de soporte. | PK `sspempd_config_employee_pk`; Cols: income_frequency, sspr_prolltemplate_id, sspr_prolltemplate2_id, sspr_concept_id, readmissions; `SSPEMPD_CONFIG_EMPLOYEE_ISACT`: ISACTIVE IN ('Y', 'N') |
| `sspempd_occupational_code` | sspempd_occupational_code | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sspempd_occupational_code_pk`; Cols: value; `SSPEMPD_OCCUPATIONAL_CODE_ISAC`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sspempd_config_employee` |
| `sspempd_occupational_code` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación dentro del módulo se realiza a través de dos ventanas principales: 'Configuraciones Generales por defecto' y 'Configuración Código Ocupacional IESS'. Estas ventanas permiten a los usuarios acceder a las configuraciones necesarias para la carga de datos de empleados. Los usuarios pueden seleccionar la ventana que corresponda según la tarea que deseen realizar, facilitando la experiencia de usuario en la interfaz de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payroll.employee.data.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuraciones Generales por defecto | General default settings |
| Configuración Código Ocupacional IESS | IESS Occupational Code Configuration |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuraciones Generales por defecto | General default settings | No |
| Configuración Código Ocupacional IESS | IESS Occupational Code Configuration | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payroll.employee.data.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuraciones Generales por defecto

- **AD_WINDOW_ID:** `E6CB2D4DADB24609904E5096FBAFB214`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `EF58003C9ED64554AE8E2B325CA5E0E0` | 0 |

### Ventana: Configuración Código Ocupacional IESS

- **AD_WINDOW_ID:** `F7B541DE304C4E0D862267409D35C5C1`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `CF95C2CC08EA4761976C1331A4CE7782` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Header (ventana: Configuración Código Ocupacional IESS)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Code IESS | `Value` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |

### Header (ventana: Configuraciones Generales por defecto)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Income_Frequency | `Income_Frequency` | No | No | — |
| 30 | Template 1 | `Sspr_Prolltemplate_ID` | No | No | — |
| 40 | Template 2 | `Sspr_Prolltemplate2_ID` | No | No | — |
| 50 | Concept V | `Sspr_Concept_ID` | No | No | — |
| 60 | Readmissions | `Readmissions` | No | No | — |
| 70 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo no cuenta con botones de proceso como completar, retornar o rechazar, ni genera informes específicos. Sin embargo, es fundamental que los usuarios realicen validaciones frecuentes de los datos ingresados para asegurar que la información de los empleados es precisa y esté actualizada. Dado que el módulo se centra mayormente en la configuración y carga de datos, es recomendable que los usuarios se familiaricen con los procedimientos para ingresar información correctamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payroll.employee.data.es_ES/referencedata/translation/`.

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

actualmente no se han definido clases Java dentro de este módulo, sugiriendo que el componente no extiende funcionalidad mediante programación en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payroll.employee.data`.

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
| AD_VAL_RULE | — | `Concept Thirteenth` | `concepttypepayroll='DT'` |
| AD_VAL_RULE | — | `Concept Fourteenth` | `concepttypepayroll='DC'` |
| AD_VAL_RULE | — | `Valid Concept` | `concepttypepayroll='RF'` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

En el contexto de la base de datos, se observa que no se han implementado triggers ni funciones PL, lo que significa que el soporte se basa mayormente en las configuraciones manuales y el acceso directo a las tablas. Esto puede simplificar las tareas de soporte, ya que no se requiere el manejo de lógica de negocio compleja a través de estas herramientas.

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

Módulo: `ec.com.sidesoft.payroll.employee.data`.

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

# Glosario — prefijo `SSPEMPD`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPEMPD` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payroll.employee.data` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Holidays
**Package:** `ec.com.sidesoft.holidays`

# Module overview — Holidays

## Functional

El módulo de 'Holidays' permite gestionar los días feriados en la organización, facilitando su registro y visualización. Este módulo es utilizado por personal administrativo y de recursos humanos que necesitan planificar y comunicar días no laborables a los empleados. El alcance del módulo incluye la definición de días feriados estándar y la gestión de días feriados específicos por periodos, asegurando que se ajusten a las regulaciones del lugar de operación. Sus dependencias incluyen la 'Core' y '2.50 to 3.00 Compatibility Skin' que son necesarias para asegurar el correcto funcionamiento del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/holidays` |
| Web | `web/ec.com.sidesoft.holidays/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSHD`

# Guía de chat — Holidays

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.holidays`).

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
- «¿Qué es la tabla sshd_holidays_period?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo añadir un nuevo día feriado?
- ¿Qué debo hacer si hay un error en la fecha de un día feriado?
- ¿Puedo eliminar un día feriado que ya no es relevante?
- ¿Cómo se visualizan los días feriados por periodo?
- ¿Hay un límite en la cantidad de días feriados que puedo registrar?
- ¿Cómo afectará un día feriado al cálculo de nómina?
- ¿Los días feriados se actualizan automáticamente cada año?
- ¿Dónde encontro la documentación relacionada con las reglas de días feriados?

# Domain — data model

## Functional

La entidad cabecera principal en este módulo es 'sshd_holidays_period', que almacena información sobre los días feriados. Las relaciones en el modelo de datos están enfocadas en la vinculación de los días feriados con los periodos específicos en los que son aplicables. A pesar de que no se han especificado disparadores, el módulo cuenta con una función PL que permite manejar ciertas operaciones relacionadas con los días feriados, garantizando la integridad de los datos en el sistema. Este diseño permite que las entidades se mantengan actualizadas y coherentes a lo largo de las diferentes transacciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sshd_holidays_period` |
| `sshd_holidays_period_line` |
| `sshd_holidays_standards` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sshd_holidays_period` | sshd_holidays_period | — | `SSHD_YEAR_UNIQUE` (c_year_id) | c_year_id→c_year | Detalle enlazado a c_year. | PK `sshd_holidays_period_key`; Cols: description, c_year_id, load_holidays |
| `sshd_holidays_period_line` | sshd_holidays_period_line | — | `SSHD_PERIOD_UNIQUE` (value) | sshd_holidays_period_id→sshd_holidays_period | Detalle enlazado a sshd_holidays_period. | PK `sshd_holidays_period_line_key`; Cols: value, name, description, sshd_holidays_period_id, automatic_holidays |
| `sshd_holidays_standards` | sshd_holidays_standards | — | `SSHD_HOLIDAY_UNIQUE` (value) | — | Entidad de datos del módulo (ver columnas y FK). | PK `sshd_holidays_key`; Cols: value, name, description, month, day |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sshd_holidays_period` |
| `sshd_holidays_period_line` |
| `sshd_holidays_standards` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de dos ventanas principales: 'Días Feriados Estandares' y 'Días Feriados por Periodos'. Los usuarios pueden acceder a estas ventanas desde el menú principal del ERP, permitiendo así una rápida localización y edición de los días feriados establecidos. A partir de estas ventanas, los usuarios pueden añadir, modificar o eliminar días feriados conforme a las necesidades de la organización.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.holidays.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Días Feriados Estandares | Holidays standards |
| Días Feriados por Periodos | Holidays by Preriod |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Días Feriados Estandares | Holidays standards | No |
| Días Feriados por Periodos | Holidays by Preriod | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.holidays.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Días Feriados Estandares

- **AD_WINDOW_ID:** `76475C92CFEA41669BFC1827DE12EC8A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Holidays standards | `FA9592D34C8B4E4DA28D450E80A81427` | 0 |

### Ventana: Días Feriados por Periodos

- **AD_WINDOW_ID:** `81D32CD892024F6DABC4C14E99581C9E`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Holidays by Preriod | `1ADA855050C74874BDA7822BD8E2753E` | 0 |
| 20 | Holidays by Period Line | `98AC9535C5294AEE99FB93000E86655E` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Holidays by Preriod (ventana: Días Feriados por Periodos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Year | `C_Year_ID` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Load holidays | `Load_Holidays` | No | No | — |

### Holidays standards (ventana: Días Feriados Estandares)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Commercial Name | `Name` | No | No | — |
| 30 | Search Key | `Value` | No | Sí | — |
| 40 | Day | `Day` | No | No | — |
| 50 | Month | `Month` | No | No | — |
| 60 | Description | `Description` | No | No | — |

### Holidays by Period Line (ventana: Días Feriados por Periodos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Commercial Name | `Name` | No | No | — |
| 50 | Description | `Description` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Existen procesos definidos en los que los usuarios pueden completar, retornar o rechazar cambios en la configuración de días feriados. Por ejemplo, hay un botón de proceso disponible que ejecuta acciones relacionadas con la gestión de días feriados. Aunque no hay informes asociados, se suelen realizar validaciones frecuentes sobre las fechas ingresadas para asegurar que no haya duplicados y que cumplan con el formato requerido.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.holidays.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar Días Feriados | Load holidays | Load_holidays | `sshd_load_holidays` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| Botón (PL/pgSQL) | Cargar Días Feriados | Load holidays | Load_holidays | `sshd_load_holidays` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar Días Feriados | Load holidays | PL `sshd_load_holidays` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| `sshd_day` | The field day should not exceed 31 | The field day should not exceed 31 | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sshd_daynumber` | The day field must be numeric | The day field must be numeric | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye una clase Java, 'sshd_Concatenatedaymonth', que permite manejar la concatenación de día y mes, facilitando la validación y el formateo de las fechas ingresadas por los usuarios. Esta clase contribuye a mejorar la experiencia del usuario al validar entradas en tiempo real.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.holidays`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `sshd_Concatenatedaymonth` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/holidays/ad_callouts/sshd_Concatenatedaymonth.java` |
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

En el contexto de la base de datos, aunque no se han definido disparadores, la función PL tiene un papel crucial para el soporte técnico, permitiendo la ejecución de procesos específicos relacionados con la lógica de negocio del módulo. Esto proporciona a los desarrolladores herramientas necesarias para interactuar con la base de datos de manera controlada y eficiente, garantizando una operatividad fluida.

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
| `sshd_load_holidays` | Cargar Días Feriados | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSHD_LOAD_HOLIDAYS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cargar Días Feriados | `Load_holidays` | Botón (PL/pgSQL) | PL `sshd_load_holidays` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

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

Módulo: `ec.com.sidesoft.holidays`.

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

# Glosario — prefijo `SSHD`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSHD` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.holidays` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Load_holidays` — Cargar Días Feriados

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Dinardap
**Package:** `ec.com.sidesoft.dinardap`

# Module overview — Dinardap

## Functional

El módulo Dinardap de Openbravo tiene como propósito facilitar la gestión administrativa y de reportes para entidades gubernamentales en Ecuador. Los actores principales incluyen usuarios de negocio que requieren realizar operaciones diarias, así como personal técnico de soporte que brinda asistencia a los usuarios. Este módulo está diseñado para integrarse con otros módulos de Openbravo, tales como la gestión avanzada de cuentas por pagar y cobrar, y la gestión de socios de negocio, lo que permite una administración más eficiente de los procesos. Su implementación requiere la compatibilidad con varias extensiones y módulos complementarios también basados en Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/dinardap` |
| Web | `web/ec.com.sidesoft.dinardap/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Advanced Payables and Receivables Mngmt
- Complement of Business Partner
- Ecuador Cities and Parish Management

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SDIN`

# Guía de chat — Dinardap

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.dinardap`).

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

- ¿Cómo puedo acceder al módulo Dinardap?
- ¿Qué procesos debo seguir para generar un reporte?
- ¿Cómo puedo validar los datos ingresados en el sistema?
- ¿Qué documentos son necesarios para completar una transacción?
- ¿Cómo puedo retornar un proceso que he iniciado?
- ¿Dónde puedo encontrar ayuda sobre el uso del módulo?
- ¿Qué hacer si encuentro un error al completar un proceso?
- ¿Cómo se archivan los archivos generados?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la modificación de tablas clave, incluidas AD_ORG, C_BPARTNER, C_DOCTYPE y C_INVOICE, que permiten al módulo interactuar adecuadamente con la información de las organizaciones, socios de negocio, tipos de documento e facturas. A través de estas entidades, el módulo puede gestionar eficazmente las relaciones entre las transacciones y la información del cliente. Aunque no se han definido etapas o tablas ancla específicas dentro del módulo, la lógica del proceso y las relaciones implícitas facilitan un flujo de trabajo coherente y eficiente.

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

`AD_ORG`, `C_BPARTNER`, `C_DOCTYPE`, `C_INVOICE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo Dinardap no tiene ventanas, lo que significa que la navegación se realiza a través de los menús configurados. Los usuarios acceden a las diferentes funcionalidades mediante los menús, pudiendo elegir entre diversas opciones disponibles según sus necesidades y roles.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.dinardap.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Información de Créditos (Dinardap) | Credits Information (Dinardap) | No |
| Operaciones por corte | Operations cut | No |
| Operaciones por periodo | Period operations | No |
| Plazo de operaciones del periodo | Term of period operations | No |
| Plazo de operaciones morosidad del periodo | Term of operations period delinquency | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.dinardap.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `143`

- **AD_TAB_ID:** `143` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 600 | Dinardap ID | `EM_Sdin_Dinardap_ID` | No | No | — |

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 360 | Apply Dinardap | `EM_Sdin_Applydinardap` | No | No | — |

### Pestaña `223`

- **AD_TAB_ID:** `223` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 108 | Subjet Class | `EM_Sdin_Subjet_Class` | No | No | — |
| 110 | Source Of Income | `EM_Sdin_Source_Of_Income` | No | No | — |
| 111 | Wallet Punished | `EM_Sdin_Wallet_Punished` | No | No | — |

### Pestaña `263`

- **AD_TAB_ID:** `263` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 130 | Lawsuit | `EM_Sdin_Lawsuit` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dentro de Dinardap, existen cinco procesos principales que los usuarios pueden ejecutar. Estos procesos incluyen diversas funciones relacionadas con la administración de datos y reportes. Los botones típicos en pantalla permiten al usuario completar, retornar y rechazar transacciones según sea necesario. Aunque no se han especificado informes concretos en el módulo, es posible realizar validaciones frecuentes en los datos ingresados según las reglas del negocio, garantizando la integridad de la información manejada.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.dinardap.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Información de Créditos (Dinardap) | Credits Information (Dinardap) | Sdin_Credits_Information_Dinardap | Java `ArchDinardapTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cYearId` | `src/ec/com/sidesoft/dinardap/create_txt/ArchDinardapTXT.java` |
| Proceso / otro | Operaciones por corte | Operations cut | Operations cut | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Operaciones por periodo | Period operations | Period operations | *(OBUIAPP / manual)* | Period operations | — |
| Proceso / otro | Plazo de operaciones del periodo | Term of period operations | Term of period operations | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Plazo de operaciones morosidad del periodo | Term of operations period delinquency | Term of operations period delinquency | *(OBUIAPP / manual)* | — | — |
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
| Botón (Java) | Información de Créditos (Dinardap) | `ArchDinardapTXT` | Proceso Java (toolbar/background) | `cYearId` | — | `src/ec/com/sidesoft/dinardap/create_txt/ArchDinardapTXT.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Información de Créditos (Dinardap) | Credits Information (Dinardap) | Sdin_Credits_Information_Dinardap | Java `ArchDinardapTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `cYearId` | `src/ec/com/sidesoft/dinardap/create_txt/ArchDinardapTXT.java` |
| Proceso / otro | Operaciones por corte | Operations cut | Operations cut | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Operaciones por periodo | Period operations | Period operations | *(OBUIAPP / manual)* | Period operations | — |
| Proceso / otro | Plazo de operaciones del periodo | Term of period operations | Term of period operations | *(OBUIAPP / manual)* | — | — |
| Proceso / otro | Plazo de operaciones morosidad del periodo | Term of operations period delinquency | Term of operations period delinquency | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Información de Créditos (Dinardap) | Credits Information (Dinardap) | Java `ArchDinardapTXT` | Proceso Openbravo registro `cYearId` | Proceso Openbravo registro `cYearId` |
| Proceso / otro | Operaciones por corte | Operations cut | — | — | — |
| Proceso / otro | Operaciones por periodo | Period operations | — | Period operations | — |
| Proceso / otro | Plazo de operaciones del periodo | Term of period operations | — | — | — |
| Proceso / otro | Plazo de operaciones morosidad del periodo | Term of operations period delinquency | — | — | — |
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
| — | *(sin AD_MESSAGE.xml en el módulo)* | — | — | — | — |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye una clase Java llamada ArchDinardapTXT, que permite la creación y gestión de archivos de texto según los requerimientos del sistema. Esta clase es esencial para la interacción con el sistema y la creación de reportes desde los datos procesados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.dinardap`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ArchDinardapTXT` | create_txt | DalBaseProcess | — | `src/ec/com/sidesoft/dinardap/create_txt/ArchDinardapTXT.java` |
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

El módulo hace uso de cuatro funciones PL que son esenciales para el soporte y funcionamiento del sistema, actuando como intermediarios en la lógica de negocio de los procesos que realizan los usuarios. Los triggers no están definidos, lo que sugiere que las funciones PL cumplen con la mayoría de las necesidades funcionales del módulo.

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
| `sdin_cancellationdate` | — | Anula / desiste la operación de compra. | — | `model/functions/SDIN_CANCELLATIONDATE.xml` |
| `sdin_cancelpaymentmethod` | — | Anula / desiste la operación de compra. | — | `model/functions/SDIN_CANCELPAYMENTMETHOD.xml` |
| `sdin_cc_plazo_periodo` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SDIN_CC_PLAZO_PERIODO.xml` |
| `sdin_due_invoice` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SDIN_DUE_INVOICE.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Información de Créditos (Dinardap) | `Sdin_Credits_Information_Dinardap` | Botón (Java) | Java `ArchDinardapTXT` | N | Proceso Openbravo registro `cYearId` |

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

Módulo: `ec.com.sidesoft.dinardap`.

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

# Glosario — prefijo `SDIN`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SDIN` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.dinardap` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Sdin_Credits_Information_Dinardap` — Información de Créditos (Dinardap)
- `Operations cut` — Operaciones por corte
- `Period operations` — Operaciones por periodo
- `Term of period operations` — Plazo de operaciones del periodo
- `Term of operations period delinquency` — Plazo de operaciones morosidad del periodo

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Dinardap Advanced
**Package:** `ec.com.sidesoft.dinardap.advanced`

# Module overview — Sidesoft Dinardap Advanced

## Functional

El módulo Sidesoft Dinardap Advanced tiene como propósito optimizar la gestión de datos para la entidad Dinardap dentro del sistema Openbravo. Está diseñado para ser utilizado por usuarios de negocio, así como por el personal de soporte técnico que proporciona asistencia de nivel 2 y desarrolladores que implementan personalizaciones. El alcance se centra en la configuración y operación de la base de datos relacionada con las operaciones de Dinardap, asegurando que las interacciones sean eficientes y seguras. Este módulo requiere las dependencias '2.50 to 3.00 Compatibility Skin' y 'Core' para su adecuado funcionamiento.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/dinardap/advanced` |
| Web | `web/ec.com.sidesoft.dinardap.advanced/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SDINDP`

# Guía de chat — Sidesoft Dinardap Advanced

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.dinardap.advanced`).

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
- «¿Qué es la tabla sdindp_dinardap_config?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo configurar los parámetros generales de Dinardap?
- ¿Qué debo hacer si encuentro un error al procesar datos en la ventana de Información Dinardap?
- ¿Existen validaciones automáticas antes de guardar los datos?
- ¿Dónde encuentro la documentación detallada sobre el módulo?
- ¿Cómo se vinculan las tablas en este módulo?
- ¿Cuáles son los triggers más importantes y cómo impactan en el rendimiento?
- ¿Qué acciones debo tomar si necesito descartar registros?
- ¿Cómo puedo exportar datos desde este módulo a un archivo?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la table principal 'sdindp_dinardap_config', que actúa como la entidad cabecera, proporcionando la configuración necesaria para las operaciones del módulo. Adicionalmente, se vincula con las tablas 'sdindp_dinardap_discard' y 'sdindp_dinardap_line' a medida que se procesan los datos. Las relaciones entre estas tablas aseguran que los datos fluyan correctamente durante las transacciones y configuraciones. Existen tres triggers clave que gestionan eventos importantes dentro del sistema, tales como la actualización automática de campos y validaciones al modificar registros.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sdindp_dinardap` |
| `sdindp_dinardap_config` |
| `sdindp_dinardap_discard` |
| `sdindp_dinardap_line` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sdindp_dinardap` | sdindp_dinardap | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org. | PK `sdindp_d_key`; Cols: date_from, date_to, btn_load_lines, btn_debug_info, processing; `SDINDP_D_ISACTIVE`: ISACTIVE IN ('Y', 'N'); `SDINDP_DINARDAP_PROCESSING`: PROCESSING IN ('Y', 'N') |
| `sdindp_dinardap_config` | sdindp_dinardap_config | `SDINDP_DINARDAP_CONFIG_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org | Parametrización / catálogo de soporte. Validado por trigger(s): SDINDP_DINARDAP_CONFIG_TRG. | PK `sdindp_dc_key`; Cols: sql, codigoentidad, max_day_month, min_trade_value, min_value_balance_operation; `SDINDP_DC_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `sdindp_dinardap_discard` | sdindp_dinardap_discard | `SDINDP_MOVE_DISCARD_TRG` | — | ad_client_id→ad_client; sdindp_dinardap_id→sdindp_dinardap; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sdindp_dinardap. Validado por trigger(s): SDINDP_MOVE_DISCARD_TRG. | PK `sdindp_dd_key`; Cols: sdindp_dinardap_id, codigoentidad, fecha, tipoidentificacion, identificacionsujeto; `SDINDP_DD_ISACTIVE`: ISACTIVE IN ('Y', 'N'); `SDINDP_DD_REMOVABLE`: REMOVABLE IN ('Y', 'N') |
| `sdindp_dinardap_line` | sdindp_dinardap_line | `SDINDP_MOVE_LINE_TRG` | — | ad_client_id→ad_client; sdindp_dinardap_id→sdindp_dinardap; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, sdindp_dinardap. Validado por trigger(s): SDINDP_MOVE_LINE_TRG. | PK `sdindp_dl_key`; Cols: sdindp_dinardap_id, codigoentidad, fecha, tipoidentificacion, identificacionsujeto; `SDINDP_DL_ISACTIVE`: ISACTIVE IN ('Y', 'N'); `SDINDP_DL_REMOVABLE`: REMOVABLE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sdindp_dinardap` |
| `sdindp_dinardap_config` |
| `sdindp_dinardap_discard` |
| `sdindp_dinardap_line` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo cuenta con dos ventanas principales: 'Información Dinardap' y 'Parámetros generales Dinardap'. Los usuarios pueden navegar a través de estas ventanas mediante un menú lateral, seleccionando directamente la opción deseada para acceder a las distintas funcionalidades y datos asociados, lo que permite una administración intuitiva de la información.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.dinardap.advanced.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Información Dinardap | Dinardap Information |
| Parámetros generales Dinardap | Dinardap general parameters |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración | Setup | Sí |
| Dinardap | Dinardap | Sí |
| Información Dinardap | Dinardap Information | No |
| Parámetros generales Dinardap | Dinardap general parameters | No |
| Transacciones | Transactions | Sí |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.dinardap.advanced.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Información Dinardap

- **AD_WINDOW_ID:** `D4C47212972C49B98E99FEC511F4B52D`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `2CE2952C624C42DFA430B96C9D6F649C` | 0 |
| 20 | Lines | `AB8C0B705C1F4E7583CC10DA049F39AD` | 1 |
| 30 | Discards | `B637D62B608445B1A90CB459B85923D4` | 1 |

### Ventana: Parámetros generales Dinardap

- **AD_WINDOW_ID:** `2011E35A246F4A70824DA2FE3B3B42F7`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `D8F4FC88E3B5496BBD5CAE3A1ABDCAE0` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Lines (ventana: Información Dinardap)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | CodigoEntidad | `CodigoEntidad` | No | No | — |
| 110 | Fecha | `Fecha` | No | No | — |
| 120 | TipoIdentificacion | `TipoIdentificacion` | No | No | — |
| 130 | IdentificacionSujeto | `IdentificacionSujeto` | No | No | — |
| 140 | NombreSujeto | `NombreSujeto` | No | No | — |
| 150 | ClaseSujeto | `ClaseSujeto` | No | No | — |
| 160 | Provincia | `Provincia` | No | No | — |
| 170 | Canton | `Canton` | No | No | — |
| 180 | Parroquia | `Parroquia` | No | No | — |
| 190 | Sexo | `Sexo` | No | No | — |
| 200 | EstadoCivil | `EstadoCivil` | No | No | — |
| 210 | OrigenIngresos | `OrigenIngresos` | No | No | — |
| 220 | NumeroOperacion | `NumeroOperacion` | No | No | — |
| 230 | ValorOperacion | `ValorOperacion` | No | No | — |
| 240 | SaldoOperacion | `SaldoOperacion` | No | No | — |
| 250 | FechaConcesion | `FechaConcesion` | No | No | — |
| 260 | FechaVencimiento | `FechaVencimiento` | No | No | — |
| 270 | FechaExigible | `FechaExigible` | No | No | — |
| 280 | PlazoOperacion | `PlazoOperacion` | No | No | — |
| 290 | PeriodicidadPagos | `PeriodicidadPagos` | No | No | — |
| 300 | DiasMorosidad | `DiasMorosidad` | No | No | — |
| 310 | MontoMorosidad | `MontoMorosidad` | No | No | — |
| 320 | MontoInteresEnMora | `MontoInteresEnMora` | No | No | — |
| 330 | ValorXVencer1A30 | `ValorXVencer1A30` | No | No | — |
| 340 | ValorXVencer31A90 | `ValorXVencer31A90` | No | No | — |
| 350 | ValorXVencer91A180 | `ValorXVencer91A180` | No | No | — |
| 360 | ValorXVencer181A360 | `ValorXVencer181A360` | No | No | — |
| 370 | ValorXVencerMas360 | `ValorXVencerMas360` | No | No | — |
| 380 | ValorVencido1A30 | `ValorVencido1A30` | No | No | — |
| 390 | ValorVencidoG31A90 | `ValorVencidoG31A90` | No | No | — |
| 400 | ValorVencido91A180 | `ValorVencido91A180` | No | No | — |
| 410 | ValorVencido181A360 | `ValorVencido181A360` | No | No | — |
| 420 | ValorVencidoMas360 | `ValorVencidoMas360` | No | No | — |
| 430 | ValorEnDemandaJudicial | `ValorEnDemandaJudicial` | No | No | — |
| 440 | CarteraCastigada | `CarteraCastigada` | No | No | — |
| 450 | CuotaCredito | `CuotaCredito` | No | No | — |
| 460 | FechaCancelacion | `FechaCancelacion` | No | No | — |
| 470 | FormaCancelacion | `FormaCancelacion` | No | No | — |

### Discards (ventana: Información Dinardap)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | CodigoEntidad | `CodigoEntidad` | No | No | — |
| 110 | Fecha | `Fecha` | No | No | — |
| 120 | TipoIdentificacion | `TipoIdentificacion` | No | No | — |
| 130 | IdentificacionSujeto | `IdentificacionSujeto` | No | No | — |
| 140 | NombreSujeto | `NombreSujeto` | No | No | — |
| 150 | ClaseSujeto | `ClaseSujeto` | No | No | — |
| 160 | Provincia | `Provincia` | No | No | — |
| 170 | Canton | `Canton` | No | No | — |
| 180 | Parroquia | `Parroquia` | No | No | — |
| 190 | Sexo | `Sexo` | No | No | — |
| 200 | EstadoCivil | `EstadoCivil` | No | No | — |
| 210 | OrigenIngresos | `OrigenIngresos` | No | No | — |
| 220 | NumeroOperacion | `NumeroOperacion` | No | No | — |
| 230 | ValorOperacion | `ValorOperacion` | No | No | — |
| 240 | SaldoOperacion | `SaldoOperacion` | No | No | — |
| 250 | FechaConcesion | `FechaConcesion` | No | No | — |
| 260 | FechaVencimiento | `FechaVencimiento` | No | No | — |
| 270 | FechaExigible | `FechaExigible` | No | No | — |
| 280 | PlazoOperacion | `PlazoOperacion` | No | No | — |
| 290 | PeriodicidadPagos | `PeriodicidadPagos` | No | No | — |
| 300 | DiasMorosidad | `DiasMorosidad` | No | No | — |
| 310 | MontoMorosidad | `MontoMorosidad` | No | No | — |
| 320 | MontoInteresEnMora | `MontoInteresEnMora` | No | No | — |
| 330 | ValorXVencer1A30 | `ValorXVencer1A30` | No | No | — |
| 340 | ValorXVencer31A90 | `ValorXVencer31A90` | No | No | — |
| 350 | ValorXVencer91A180 | `ValorXVencer91A180` | No | No | — |
| 360 | ValorXVencer181A360 | `ValorXVencer181A360` | No | No | — |
| 370 | ValorXVencerMas360 | `ValorXVencerMas360` | No | No | — |
| 380 | ValorVencido1A30 | `ValorVencido1A30` | No | No | — |
| 390 | ValorVencidoG31A90 | `ValorVencidoG31A90` | No | No | — |
| 400 | ValorVencido91A180 | `ValorVencido91A180` | No | No | — |
| 410 | ValorVencido181A360 | `ValorVencido181A360` | No | No | — |
| 420 | ValorVencidoMas360 | `ValorVencidoMas360` | No | No | — |
| 430 | ValorEnDemandaJudicial | `ValorEnDemandaJudicial` | No | No | — |
| 440 | CarteraCastigada | `CarteraCastigada` | No | No | — |
| 450 | CuotaCredito | `CuotaCredito` | No | No | — |
| 460 | FechaCancelacion | `FechaCancelacion` | No | No | — |
| 470 | FormaCancelacion | `FormaCancelacion` | No | No | — |

### Header (ventana: Parámetros generales Dinardap)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 100 | Sql | `SQL` | No | No | — |
| 110 | CodigoEntidad | `Codigoentidad` | No | No | — |
| 130 | Minimum value of operation | `MIN_Trade_Value` | No | No | — |
| 140 | Minimum value of transaction balance | `MIN_Value_Balance_Operation` | No | No | — |

### Header (ventana: Información Dinardap)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 50 | Load Lines | `BTN_Load_Lines` | No | No | — |
| 55 | Debug Info | `BTN_Debug_Info` | No | No | — |
| 60 | Generate TXT | `BTN_Gen_TXT` | No | No | — |
| 100 | Date From | `Date_From` | No | No | — |
| 110 | Date To | `Date_To` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

En el módulo, los principales botones de proceso incluyen opciones para completar, retornar y rechazar transacciones. Estas acciones se encuentran en la interfaz de usuario para simplificar la interacción del usuario con las funciones avanzadas del módulo. Las validaciones son una parte crítica del proceso, asegurando que los datos ingresados cumplan con los requisitos antes de ser procesados. Sin embargo, no se generan informes directos desde el módulo, lo que enfatiza su utilidad en la configuración más que en la generación de reportes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.dinardap.advanced.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar TXT | Generate TXT | Gen_TXT | Java `GenerateTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sdindp_Dinardap_ID`, No se encontro configuración de parámetros generales Dinardap; Error al intentar crear el TXT | `src/ec/com/sidesoft/dinardap/advanced/ad_process/GenerateTXT.java` |
| Botón (PL/pgSQL) | Cargar líneas | Load Lines | sdindp_load_lines | `sdindp_load_lines` | No se encontro configuración de parámetros generales Dinardap | — |
| Botón (PL/pgSQL) | Depurar información | Debug Info | sdindp_debug_info | `sdindp_debug_info` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| Botón (Java) | Generar TXT | `GenerateTXT` | Proceso Java (toolbar/background) | `Sdindp_Dinardap_ID` | No se encontro configuración de parámetros generales Dinardap; Error al intentar crear el TXT | `src/ec/com/sidesoft/dinardap/advanced/ad_process/GenerateTXT.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar TXT | Generate TXT | Gen_TXT | Java `GenerateTXT` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Sdindp_Dinardap_ID`, No se encontro configuración de parámetros generales Dinardap; Error al intentar crear el TXT | `src/ec/com/sidesoft/dinardap/advanced/ad_process/GenerateTXT.java` |
| Botón (PL/pgSQL) | Cargar líneas | Load Lines | sdindp_load_lines | `sdindp_load_lines` | No se encontro configuración de parámetros generales Dinardap | — |
| Botón (PL/pgSQL) | Depurar información | Debug Info | sdindp_debug_info | `sdindp_debug_info` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar TXT | Generate TXT | Java `GenerateTXT` | Proceso Openbravo registro `Sdindp_Dinardap_ID`, No se encontro configuración de parámetros generales Dinardap; Error al intentar crear el TXT | No se encontro configuración de parámetros generales Dinardap; Error al intentar crear el TXT |
| Botón (PL/pgSQL) | Cargar líneas | Load Lines | PL `sdindp_load_lines` | No se encontro configuración de parámetros generales Dinardap | No se encontro configuración de parámetros generales Dinardap |
| Botón (PL/pgSQL) | Depurar información | Debug Info | PL `sdindp_debug_info` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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

El módulo incluye la clase Java 'GenerateTXT', que es responsable de la generación de archivos de texto desde los datos del módulo, permitiendo así exportaciones que pueden ser utilizadas fuera del sistema. Esta clase gestiona la creación y escritura de información en archivos, ampliando la funcionalidad del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.dinardap.advanced`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `GenerateTXT` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/dinardap/advanced/ad_process/GenerateTXT.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SDINDP_DINARDAP_CONFIG_TRG` | `sdindp_dinardap_config` | before INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SDINDP_MOVE_DISCARD_TRG` | `sdindp_dinardap_discard` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `SDINDP_MOVE_LINE_TRG` | `sdindp_dinardap_line` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Función PL `sdindp_load_lines` | — | invocación proceso | No se encontro configuración de parámetros generales Dinardap |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers juegan un papel crucial en la gestión de datos, garantizando que las acciones en la base de datos se realicen de manera coherente y se ajusten a las reglas de negocio definidas. Existen dos funciones PL en el módulo que apoyan la lógica de negocio y permiten la ejecución de procesos complejos sin necesidad de intervención directa del usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SDINDP_DINARDAP_CONFIG_TRG` | `sdindp_dinardap_config` | before | INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SDINDP_DINARDAP_CONFIG_TRG.xml` |
| `SDINDP_MOVE_DISCARD_TRG` | `sdindp_dinardap_discard` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SDINDP_MOVE_DISCARD_TRG.xml` |
| `SDINDP_MOVE_LINE_TRG` | `sdindp_dinardap_line` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SDINDP_MOVE_LINE_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sdindp_debug_info` | Depurar información | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SDINDP_DEBUG_INFO.xml` |
| `sdindp_load_lines` | Cargar líneas | No se encontro configuración de parámetros generales Dinardap | No se encontro configuración de parámetros generales Dinardap | `model/functions/SDINDP_LOAD_LINES.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Generar TXT | `Gen_TXT` | Botón (Java) | Java `GenerateTXT` | N | Proceso Openbravo registro `Sdindp_Dinardap_ID`, No se encontro configuración de parámetros generales Dinardap; Error al intentar crear el TXT |
| 2 | Cargar líneas | `sdindp_load_lines` | Botón (PL/pgSQL) | PL `sdindp_load_lines` | N | No se encontro configuración de parámetros generales Dinardap |
| 3 | Depurar información | `sdindp_debug_info` | Botón (PL/pgSQL) | PL `sdindp_debug_info` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

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

Módulo: `ec.com.sidesoft.dinardap.advanced`.

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

# Glosario — prefijo `SDINDP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SDINDP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.dinardap.advanced` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Gen_TXT` — Generar TXT
- `sdindp_load_lines` — Cargar líneas
- `sdindp_debug_info` — Depurar información

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Actuaria  Dinardap Custom Canton
**Package:** `ec.com.sidesoft.dinardap.custom.canton`

# Module overview — Sidesoft Actuaria  Dinardap Custom Canton

## Functional

El módulo Sidesoft Actuaria Dinardap Custom Canton permite la gestión de información relacionada con cantones en Ecuador, integrándose a Openbravo ERP. Sus principales actores son los usuarios de negocio que requieren acceso a datos geográficos administrativos y el soporte técnico L2 que lo habilita. El alcance del módulo incluye la interactuación con entes públicos al facilitar la obtención y registro de datos cantoneses, además de integrarse con el módulo de gestión de ciudades y parroquias de Ecuador. Las dependencias incluyen la compatibilidad con versiones del sistema y otros módulos relacionados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/dinardap/custom/canton` |
| Web | `web/ec.com.sidesoft.dinardap.custom.canton/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Ecuador Cities and Parish Management

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SDINCC`

# Guía de chat — Sidesoft Actuaria  Dinardap Custom Canton

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.dinardap.custom.canton`).

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

- ¿Cómo puedo registrar un nuevo cantón en el sistema?
- ¿Qué datos necesito para actualizar la información de un cantón existente?
- ¿Dónde puedo encontrar estadísticas sobre los cantones registrados?
- ¿Cómo se integra el módulo con otros sistemas externos?
- ¿Qué tipo de validaciones se aplican al ingresar datos de cantones?
- ¿Hay alguna funcionalidad para eliminar cantones del sistema?
- ¿Cómo acceder a los informes relacionados con los cantones?
- ¿Qué errores comunes puedo encontrar al utilizar el módulo?

# Domain — data model

## Functional

Este módulo realiza modificaciones en la tabla C_LOCATION, que es la entidad cabecera relacionada con la ubicación geográfica. Aunque no se definen etapas específicas dentro del módulo, la relación entre la información de cantones y otras localidades puede deducirse de la estructura asociativa que este módulo construye sobre la tabla mencionada. No hay triggers definidos en este módulo, lo que sugiere que el procesamiento de datos se maneja principalmente a través de funciones Java y frontales dentro de la interfaz de Openbravo.

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

`C_LOCATION`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no tiene ventanas definidas que se puedan navegar desde la interfaz de usuario. Sin embargo, la interacción con la información geográfica se facilita potencialmente a través de una clase Java que se encarga de gestionar las solicitudes relacionadas con las localizaciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.dinardap.custom.canton.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.dinardap.custom.canton.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

No se han definido botones de proceso específicos en el módulo, lo que implica un flujo de trabajo más centralizado en las funciones Java sin una interfaz de botón convencional. De igual forma, no se presentan informes directamente asociados, lo que sugiere que cualquier reporte derivado debería ser diseñado en función de las necesidades de los usuarios y las funciones del ERP existentes. Las validaciones serán, como en otros módulos, basadas en las reglas de negocio establecidas en Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.dinardap.custom.canton.es_ES/referencedata/translation/`.

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

La clase Java principal en este módulo, Location, extiende la funcionalidad de Openbravo mediante un servlet que maneja las solicitudes relacionadas con localizaciones. Esta clase permite a los usuarios interactuar con la base de datos para obtener información sobre cantones a través de peticiones HTTP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.dinardap.custom.canton`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Location` | location_selector | HttpSecureAppServlet | — | `src/ec/com/sidesoft/dinardap/custom/canton/location_selector/Location.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Canton By Region` | `secpm_canton.C_Region_ID=@C_Region_ID@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Dado que el módulo no presenta triggers o funciones PL, su función de soporte se centraliza en las clases Java, cuya lógica permitirá la búsqueda y manipulación de datos relacionados con cantones. Esto sugiere que se dependerá de la capacidad de las clases Java para sincronizar y gestionar datos eficientemente dentro del contexto de Openbravo.

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

Módulo: `ec.com.sidesoft.dinardap.custom.canton`.

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

# Glosario — prefijo `SDINCC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SDINCC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.dinardap.custom.canton` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Module Telecommuting dialing
**Package:** `ec.com.sidesoft.payroll.telecommuting.dialing`

# Module overview — Module Telecommuting dialing

## Functional

El módulo de Marcaciones Teletrabajo Empleado tiene como propósito registrar y gestionar las marcaciones de los empleados en modalidad de teletrabajo. Los actores involucrados son los empleados que realizan las marcaciones, los supervisores que monitorean esta información y el personal de soporte que brinda asistencia técnica. Este módulo es parte del ecosistema de Openbravo, por lo que depende del núcleo del sistema, servicios web REST en JSON, infraestructura móvil y del framework de Openbravo 3.0.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payroll/telecommuting/dialing` |
| Web | `web/ec.com.sidesoft.payroll.telecommuting.dialing/` |

### Declared dependencies

- Core
- JSON REST Webservice
- Mobile Core Infrastructure
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPTDL`

# Guía de chat — Module Telecommuting dialing

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payroll.telecommuting.dialing`).

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
- «¿Qué es la tabla ssptdl_telecomm_dialing?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar mi marcación de teletrabajo?
- ¿Qué debo hacer si mi ubicación no se actualiza correctamente?
- ¿Quién puede ver mis marcaciones de teletrabajo?
- ¿Hay un límite en el número de marcaciones que puedo realizar?
- ¿Puedo modificar una marcación ya registrada?
- ¿Cómo puedo verificar si mi marcación fue registrada exitosamente?
- ¿Qué sucede si tengo problemas con el sistema al intentar marcar?
- ¿Dónde puedo encontrar el historial de mis marcaciones anteriores?

# Domain — data model

## Functional

La entidad central del módulo es 'ssptdl_telecomm_dialing', que almacena las marcaciones de teletrabajo de los empleados. Las principales relaciones se dan con las tablas modificadas 'AD_ROLE' y 'SPRBI_BIOMETRIC', que se integran para ofrecer funcionalidades adicionales relacionadas con la gestión de roles y datos biométricos. Los triggers clave, como 'SSPTDL_LOCATION_TRG' y 'SSPTDL_VALIDTELECOMM_TRG', se encargan de actualizar la ubicación de los empleados y de validar las marcaciones respectivamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssptdl_telecomm_dialing` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssptdl_telecomm_dialing` | ssptdl_telecomm_dialing | `SSPTDL_LOCATION_TRG`; `SSPTDL_VALIDTELECOMM_TRG` | — | ad_client_id→ad_client; c_bpartner_id→c_bpartner; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_bpartner. Validado por trigger(s): SSPTDL_LOCATION_TRG, SSPTDL_VALIDTELECOMM_TRG. | PK `ssptdl_telecomm_dialing_key`; Cols: datemovement, entryhour_m, exithour_m, entryhour_a, exithour_a; `SSPTDL_TLCOMM_D_ISACBTN_CHK`: ISACTIONBUTTOM IN ('Y', 'N'); `SSPTDL_TLCOMM_D_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssptdl_telecomm_dialing` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ROLE`, `SPRBI_BIOMETRIC`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de la ventana 'Marcaciones Teletrabajo Empleado', donde los usuarios pueden registrar sus marcaciones y visualizar su estado. La interfaz de usuario está diseñada para ser intuitiva, permitiendo un acceso sencillo a los formularios necesarios para interactuar con los datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payroll.telecommuting.dialing.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Marcaciones Teletrabajo Empleado | Telecomm Dialing |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Marcaciones Teletrabajo Empleado | Telecomm Dialing | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payroll.telecommuting.dialing.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Marcaciones Teletrabajo Empleado

- **AD_WINDOW_ID:** `AEB31D22CBC34951B6769589EE0BA059`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Telecomm Dialing | `AEE61977329C44E599C31975A4492F97` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `119`

- **AD_TAB_ID:** `119` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 200 | Telecomm Dialing | `EM_Ssptdl_Telecomm_Dialing` | No | No | — |

### Pestaña `4E95FCC962774DFFA7F2923FC1E98FCE`

- **AD_TAB_ID:** `4E95FCC962774DFFA7F2923FC1E98FCE` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 140 | Geolocation | `EM_Ssptdl_Geolocation` | No | No | — |
| 150 | Remote Dialing | `EM_Ssptdl_Remote_Dialing` | No | No | — |

### Telecomm Dialing (ventana: Marcaciones Teletrabajo Empleado)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | Sí | — |
| 20 | Active | `Isactive` | No | Sí | — |
| 25 | Identify | `Identify` | No | Sí | — |
| 30 | Date movement | `Datemovement` | No | Sí | — |
| 35 | Employee | `C_Bpartner_ID` | No | Sí | — |
| 40 | Entry 1 Dailing | `Entryhour_M` | No | Sí | — |
| 45 | State | `State` | No | Sí | — |
| 120 | Location_Marking | `Location_Marking` | No | No | — |
| 130 | Geolocation | `Geolocation` | No | Sí | — |
| 140 | Remote_Dialing | `Remote_Dialing` | No | Sí | — |
| 150 | Process Dialing | `Process_Dialing` | No | No | — |
| 160 | Catch_Location_Gps | `Catch_Location_Gps` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso principal incluye un botón que permite a los empleados completar su marcación. Este proceso se ejecuta mediante una rutina que valida los datos ingresados y actualiza los registros en la base de datos a través de botones de acción. Las validaciones frecuentes se realizan para asegurarse de que las marcaciones sean precisas y cumplan con los requisitos establecidos por la organización.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payroll.telecommuting.dialing.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Procesar marcación | Process Dialing | Process_Dialing | `ssptdl_process_dialing` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| Botón (PL/pgSQL) | Procesar marcación | Process Dialing | Process_Dialing | `ssptdl_process_dialing` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Procesar marcación | Process Dialing | PL `ssptdl_process_dialing` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| `SSPTDL_Manual_Location` | Can't update location manually | Can't update location manually | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSPTDL_Status_Validation` | The location cannot be modified if it is already processed | The location cannot be modified if it is already processed | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye clases Java que manejan la lógica relacionada con las acciones del botón de obtención de ubicación GPS. Estas clases permiten interactuar con la base de datos y realizar operaciones específicas en función de los requerimientos del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payroll.telecommuting.dialing`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Get_Location_GPS` | action_button | BaseActionHandler | — | `src/ec/com/sidesoft/payroll/telecommuting/dialing/action_button/Get_Location_GPS.java` |
| `Ssptdl_ComponentProvider` | action_button | BaseComponentProvider | ComponentProvider / UI | `src/ec/com/sidesoft/payroll/telecommuting/dialing/action_button/Ssptdl_ComponentProvider.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSPTDL_LOCATION_TRG` | `ssptdl_telecomm_dialing` | after INSERT/UPDATE | SE ACTUALIZA LA UBICACION DESDE EL CAMPO EN OPENBRAVO; SE ACTUALIZA LA UBICACION DESDE EL BOTON EN OPENBRAVO |
| Trigger `SSPTDL_VALIDTELECOMM_TRG` | `ssptdl_telecomm_dialing` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `Ssptdl_Valid_Partner` | `C_BPARTNER.C_BPARTNER_ID IN (
SELECT AU.C_BPARTNER_ID 
FROM AD_ROLE AROLE
JOIN AD_USER_ROLES AUR ON AROLE.AD_ROLE_ID = A` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers juegan un rol crucial en el módulo, asegurando que las actualizaciones de la ubicación y las validaciones se realicen de manera eficiente y precisa. La función PL/pgSQL asociada se utiliza para implementar la lógica de negocio necesaria para el correcto funcionamiento del módulo, permitiendo a los usuarios disfrutar de un sistema robusto y confiable.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSPTDL_LOCATION_TRG` | `ssptdl_telecomm_dialing` | after | INSERT/UPDATE | SE ACTUALIZA LA UBICACION DESDE EL CAMPO EN OPENBRAVO; SE ACTUALIZA LA UBICACION DESDE EL BOTON EN OPENBRAVO | `model/triggers/SSPTDL_LOCATION_TRG.xml` |
| `SSPTDL_VALIDTELECOMM_TRG` | `ssptdl_telecomm_dialing` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPTDL_VALIDTELECOMM_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `ssptdl_process_dialing` | Procesar marcación | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPTDL_PROCESS_DIALING.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Procesar marcación | `Process_Dialing` | Botón (PL/pgSQL) | PL `ssptdl_process_dialing` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

**Total acciones documentadas (extract):** **1** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/ec.com.sidesoft.payroll.telecommuting.dialing/js/getlocationgps.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.payroll.telecommuting.dialing`.

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

# Glosario — prefijo `SSPTDL`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPTDL` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payroll.telecommuting.dialing` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Process_Dialing` — Procesar marcación

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Ecuador Localization Payroll Datasets
**Package:** `ec.com.sideosft.localization.payroll.datasets`

# Module overview — Ecuador Localization Payroll Datasets

## Functional

El módulo 'Ecuador Localization Payroll Datasets' tiene como propósito proporcionar un conjunto de datos y configuraciones necesarios para la gestión de nómina en Ecuador. Está destinado a ser utilizado por empresas que operan en este país y necesitan cumplir con la normativa local. Los actores principales incluyen usuarios de negocio que administran la nómina, así como el equipo de soporte técnico que garantizará su funcionamiento adecuado. Este módulo no tiene dependencias externas evidentes, lo que le permite ser utilizado de forma independiente en el sistema Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sideosft/localization/payroll/datasets` |
| Web | `web/ec.com.sideosft.localization.payroll.datasets/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

*(sin prefijo en AD_MODULE_DBPREFIX)*

# Guía de chat — Ecuador Localization Payroll Datasets

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sideosft.localization.payroll.datasets`).

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

- ¿Cómo puedo importar los datos de nómina de Ecuador en Openbravo?
- ¿Existen reportes predefinidos para la nómina ecuatoriana?
- ¿Qué configuraciones debo realizar para utilizar este módulo?
- ¿Este módulo se actualiza automáticamente con cambios en la legislación laboral ecuatoriana?
- ¿Dónde puedo encontrar ejemplos de uso de datos de nómina?
- ¿Cuáles son los requisitos previos para implementar este módulo?
- ¿Hay algún soporte disponible para resolver problemas específicos con el módulo?
- ¿Cómo puedo solicitar mejoras o nuevas funcionalidades?

# Domain — data model

## Functional

Este módulo no incluye entidades cabecera o estructuras de base de datos físicas, lo que indica su enfoque en proporcionar datasets sin modificaciones a las tablas existentes. Sin embargo, se puede inferir que la lógica del módulo estaría vinculada a las tablas y procesos de nómina generales de Openbravo. Al no haber triggers ni funciones PL disponibles, se espera que la integración y el procesamiento de datos dependa de la configuración estándar del ERP.

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

El módulo 'Ecuador Localization Payroll Datasets' no contiene ventanas definidas dentro del sistema, lo que sugiere que su funcionalidad no se presenta a través de una interfaz gráfica típica. Los usuarios pueden necesitar interactuar con los datasets mediante procesos administrativos o a través de otras funcionalidades del ERP.

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

No se han definido procesos específicos ni botones de acción en este módulo, lo que limita la existencia de funciones como 'completar', 'retornar' o 'rechazar'. Asimismo, no hay informes disponibles, lo cual implica que la documentación y las validaciones estarán basadas en la lógica general de la nómina en Openbravo más que en procesos personalizados. Los usuarios podrían requerir apoyo técnico para establecer los vínculos necesarios con otros módulos.

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

Este módulo no incluye clases Java, lo que indica que no se realizan personalizaciones adicionales a nivel de código más allá de la configuración de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sideosft.localization.payroll.datasets`.

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

Dado que el módulo carece de triggers y funciones PL, su rol en la base de datos se limita a servir como un repositorio de datos no estructurado. La ausencia de componentes críticos como triggers sugiere que el enfoque estará en la implementación de datasets que podrán ser utilizados por otros procesos sin afectar directamente a la estructura de datos del ERP.

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

Módulo: `ec.com.sideosft.localization.payroll.datasets`.

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

# Glosario — prefijo `DATASETS`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `DATASETS` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sideosft.localization.payroll.datasets` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
