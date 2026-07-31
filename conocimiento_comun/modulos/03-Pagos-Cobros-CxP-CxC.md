# Openbravo Sidesoft — Pagos, Cobros, CxP y CxC

> Gestión avanzada de pagos y cobros, planes de pago, pagos anulados, importación de pagos, propuesta de pagos, cheques posfechados.

**Paquetes incluidos (14):**
- `ec.com.sidesoft.custom.advpaymentmngt` — Custom Advanced Payables and Receivables Mngmt
- `ec.com.sidesoft.custom.advpaymentmngt.multiple.payments` — Customization to Multiple Payments Windows
- `ec.com.sidesoft.account.payment` — Sidesoft Account Payment
- `ec.com.sidesoft.account.purchase` — Sidesoft Account Purchase
- `ec.com.sidesoft.payment.plan.info` — Sidesoft Payment Plan Information
- `ec.com.sidesoft.payment.voided` — Sidesoft Payment In Voided
- `ec.com.sidesoft.payments.upgrades` — Payments Upgrades
- `ec.com.sidesoft.importdata.payments` — Sidesoft ImportData for Payments
- `ec.com.sidesoft.localization.proposal.payments` — Proposal Payments
- `ec.com.sidesoft.localization.ecuador.payment.complement` — Complement of Payments
- `ec.com.sidesoft.postdated.check` — Sidesoft Postdated Check
- `ec.com.sidesoft.deposit.number` — Sidesoft Deposit Number
- `ec.com.sidesoft.deposit.reconciliation` — Sidesoft Deposit Reconciliation
- `ec.com.sidesoft.transfer.authorization` — Sidesoft transfer authorization


---
## Custom Advanced Payables and Receivables Mngmt
**Package:** `ec.com.sidesoft.custom.advpaymentmngt`

# Module overview — Custom Advanced Payables and Receivables Mngmt

## Functional

El módulo 'Custom Advanced Payables and Receivables Management' tiene como propósito la gestión avanzada de cuentas por pagar y recibir en Openbravo, facilitando a los usuarios la administración de transacciones financieras relacionadas. Este módulo es relevante para los departamentos de finanzas y contabilidad de las empresas que utilizan Openbravo, así como para los desarrolladores encargados de su implementación y mantenimiento. El alcance del módulo incluye la posibilidad de validar y gestionar pagos y cobros de manera eficiente. Las dependencias clave son el Core de Openbravo, la Localización de Ecuador en Finanzas y la compatibilidad con la interfaz de usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/advpaymentmngt` |
| Web | `web/ec.com.sidesoft.custom.advpaymentmngt/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Localization of Ecuador - Finances
- User Interface Selector

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`ECSCAP`

# Guía de chat — Custom Advanced Payables and Receivables Mngmt

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.advpaymentmngt`).

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
- «¿Qué es la tabla ecscap_general_process?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo registrar un nuevo pago?
- ¿Qué validaciones se aplican al registrar un cobro?
- ¿Cómo elimino un depósito que ya no se necesita?
- ¿Qué debo hacer si un pago es rechazado?
- ¿Dónde puedo ver el historial de transacciones realizadas?
- ¿Existen informes disponibles para los pagos registrados?
- ¿Cuál es el proceso para reactivar un cobro?
- ¿La validación de campos es automática al ingresar datos?

# Domain — data model

## Functional

La entidad cabecera principal es 'FIN_PAYMENT', que gestiona la información relativa a los pagos. Este módulo no cuenta con tablas de etapas específicas, pero la operación puede relacionarse a través de la tabla 'ecscap_general_process'. Se mantienen relaciones entre las diferentes entidades que componen el proceso de pagos, facilitando así las transacciones y su seguimiento. Existen triggers clave como 'ECSCAP_REMOVEDEPOSIT_TRG', que elimina la referencia de depósitos al reactivar y eliminar cobros, y 'ECSCAP_STATUS_PROPOSAL_TRG', que se basa en la rutina PL/pgSQL del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ecscap_general_process` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ecscap_general_process` | ecscap_general_process | — | — | fin_financial_account_id→fin_financial_account; c_acctschema_id→c_acctschema; ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org (+1) | Detalle enlazado a ad_client, c_acctschema, fin_financial_account. | PK `ecscap_gp_key`; Cols: c_acctschema_id, c_doctype_id, fin_financial_account_id, fin_paymentmethod_id; `ECSCAP_GP_ACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ecscap_general_process` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`FIN_PAYMENT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

Aunque no se especifican ventanas en el módulo, la navegación se realiza típicamente a través de menús y enlaces en la interfaz de usuario de Openbravo. Los usuarios pueden acceder a las funciones del módulo siguiendo las pautas de navegación estándar de Openbravo, enfocándose en la gestión de pagos y cobros.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.advpaymentmngt.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.advpaymentmngt.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `2700A962BC484D4C9B3E30B1C3C66BFB`

- **AD_TAB_ID:** `2700A962BC484D4C9B3E30B1C3C66BFB` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 25 | Bank Name | `EM_Ecscap_Banktransfer_ID` | No | Sí | — |
| 25 | Charger For | `—` | No | Sí | — |

### General Processes

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 100 | Document Type | `C_Doctype_ID` | No | No | — |
| 110 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 120 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |

### Pestaña `C4B6506838E14A349D6717D6856F1B56`

- **AD_TAB_ID:** `C4B6506838E14A349D6717D6856F1B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 106 | No. Check | `EM_Ecscap_No_Check` | No | No | FFC1717BB6E141E9B66EF7992732EFF5 |
| 106 | Bank Name | `EM_Ecscap_Banktransfer_ID` | No | No | FFC1717BB6E141E9B66EF7992732EFF5 |
| 106 | Account Holder | `EM_Ecscap_Account_Holder` | No | No | FFC1717BB6E141E9B66EF7992732EFF5 |
| 107 | Deposit | `EM_Ecscap_Deposit` | No | No | FFC1717BB6E141E9B66EF7992732EFF5 |
| 108 | Effective Date | `EM_Ecscap_Effective_Date` | No | No | FFC1717BB6E141E9B66EF7992732EFF5 |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo no incluye botones de procesos típicos, ya que está diseñado principalmente para la gestión de pagos y no incorpora un flujo definido de procesos adicionales. Sin embargo, es importante tener en cuenta las validaciones frecuentes mencionadas en el trigger 'ECSCAP_VALIDATE_DPTNO_TRG', que asegura que los campos sean adecuados para la operación. La generación de informes dentro de este módulo no está implementada directamente, lo que implica que las validaciones y procesos se realizan en el contexto de la administración de transacciones.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.advpaymentmngt.es_ES/referencedata/translation/`.

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
| `ECSCAP_ErrorDespositNo` | The Deposit Number is already registered. | The Deposit Number is already registered. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye una clase Java, 'CustomAddMultiplePaymentsHandler', que permite manejar la lógica detrás de la adición de múltiples pagos, integrándose con los procesos de Openbravo para facilitar la operatividad del módulo a nivel de código.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.advpaymentmngt`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `CustomAddMultiplePaymentsHandler` | actionHandler | BaseProcessActionHandler | — | `src/ec/com/sidesoft/custom/advpaymentmngt/actionHandler/CustomAddMultiplePaymentsHandler.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `ECSCAP_REMOVEDEPOSIT_TRG` | `fin_finacc_transaction` | before DELETE | Elimina la referencia del deposito al reactivar y eliminar los cobros/pagos registrados en la cuenta financiera |
| Trigger `ECSCAP_STATUS_PROPOSAL_TRG` | `fin_payment` | after INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `ECSCAP_VALIDATE_DPTNO_TRG` | `fin_payment` | before INSERT/UPDATE | Validación reutilizable de campos. |
| AD_VAL_RULE | — | `Scscap C_DocType Payment IN` | `AD_Table_ID = 'D1A97202E832470285C9B1EB026D54E2' AND IsSOTrx = 'Y'` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers juegan un papel crucial en la lógica de negocios del módulo, asegurando la integridad de los datos y la correcta ejecución de las operaciones, como se observa con 'ECSCAP_REMOVEDEPOSIT_TRG' y 'ECSCAP_STATUS_PROPOSAL_TRG'. Asimismo, aunque no se utilizan funciones PL específicas dentro del módulo, estos elementos de la base de datos se integran adecuadamente con el resto de los componentes de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `ECSCAP_REMOVEDEPOSIT_TRG` | `fin_finacc_transaction` | before | DELETE | Elimina la referencia del deposito al reactivar y eliminar los cobros/pagos registrados en la cuenta financiera | `model/triggers/ECSCAP_REMOVEDEPOSIT_TRG.xml` |
| `ECSCAP_STATUS_PROPOSAL_TRG` | `fin_payment` | after | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/ECSCAP_STATUS_PROPOSAL_TRG.xml` |
| `ECSCAP_VALIDATE_DPTNO_TRG` | `fin_payment` | before | INSERT/UPDATE | Validación reutilizable de campos. | `model/triggers/ECSCAP_VALIDATE_DPTNO_TRG.xml` |
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

Módulo: `ec.com.sidesoft.custom.advpaymentmngt`.

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

# Glosario — prefijo `ECSCAP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `ECSCAP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.advpaymentmngt` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Customization to Multiple Payments Windows
**Package:** `ec.com.sidesoft.custom.advpaymentmngt.multiple.payments`

# Module overview — Customization to Multiple Payments Windows

## Functional

La personalización para ventanas de múltiples pagos tiene como objetivo facilitar la gestión de pagos dentro del entorno del ERP Openbravo, permitiendo a los usuarios realizar múltiples transacciones de manera más eficiente. Este módulo está diseñado para ser utilizado principalmente por personal de negocio encargado de la gestión de pagos, así como por desarrolladores que deseen extender o modificar su funcionalidad. Su implementación es dependiente del marco de trabajo de Openbravo 3.0, garantizando así una integración fluida con las características existentes del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/advpaymentmngt/multiple/payments` |
| Web | `web/ec.com.sidesoft.custom.advpaymentmngt.multiple.payments/` |

### Declared dependencies

- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`CSCAMP`

# Guía de chat — Customization to Multiple Payments Windows

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.advpaymentmngt.multiple.payments`).

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

- ¿Cómo puedo realizar pagos múltiples en el ERP?
- ¿Hay una guía para entender las funciones de este módulo?
- ¿Qué debo hacer si un pago no se completa correctamente?
- ¿Dónde encuentro los informes relacionados con los pagos múltiples?
- ¿Puedo personalizar aún más las ventanas de pagos?
- ¿Qué sucede si necesito ayuda técnica con este módulo?
- ¿Este módulo afecta otros procesos en el ERP?
- ¿Cuáles son las dependencias que necesito considerar al usar esta personalización?

# Domain — data model

## Functional

Este módulo no incluye tablas físicas ni entidades cabecera definidas en el inventario proporcionado, lo que sugiere que su funcionalidad se basa principalmente en la personalización de la interfaz y en el uso de componentes ya existentes en Openbravo. Aunque no se especifican etapas ni relaciones complejas, se debe tener en cuenta que la personalización puede involucrar la modificación o extensión de procesos existentes, aunque no se detallan disparadores o funciones PL relevantes en este inventario.

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

Al no contener ventanas específicas descritas en el inventario, es probable que la navegación en este módulo se realice a través de la interfaz de usuario de Openbravo, utilizando las opciones y funciones disponibles dentro del marco general del ERP. Los usuarios habrían de utilizar los menús y herramientas ya implementados en Openbravo, al que se le añade esta personalización para facilitar el manejo de pagos múltiples.

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

El módulo no detalla botones de proceso típicos ni informes específicos; sin embargo, podemos inferir que su uso incluiría botones estándares de Openbravo para completar, retornar o rechazar pagos múltiples. Las validaciones frecuentes se centrarían en asegurar que los datos de los pagos sean consistentes y cumplan con las políticas de la empresa. Dado que no se declaran procesos o informes en el inventario, es probable que se soporte a través de funcionalidades adicionales ya presentes en Openbravo.

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

El rol del módulo Java está representado por la clase 'Cscamp_PaymentProporsalMultiplePaymentsProvider', la cual gestiona la provisión de componentes para la interfaz de usuario. Aunque no se detalla un uso intensivo de esta clase en la personalización, su función principal consiste en aportar recursos de JavaScript necesarios para el correcto funcionamiento del módulo dentro del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.advpaymentmngt.multiple.payments`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Cscamp_PaymentProporsalMultiplePaymentsProvider` | root | BaseComponentProvider | ComponentProvider / UI | `src/ec/com/sidesoft/custom/advpaymentmngt/multiple/payments/Cscamp_PaymentProporsalMultiplePaymentsProvider.java` |
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

En cuanto a la función de base de datos, el módulo no especifica disparadores ni funciones PL, lo que indica que no hay lógica de soporte directa implementada a este nivel. Sin embargo, es crucial que los desarrolladores que trabajen en la personalización tengan en cuenta la integridad de los datos existente y como esta personalización podría interactuar con otras lógicas de negocio ya definidas.

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
| `web/ec.com.sidesoft.custom.advpaymentmngt.multiple.payments/js/multiplepayments.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.custom.advpaymentmngt.multiple.payments`.

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

# Glosario — prefijo `CSCAMP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `CSCAMP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.advpaymentmngt.multiple.payments` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Account Payment
**Package:** `ec.com.sidesoft.account.payment`

# Module overview — Sidesoft Account Payment

## Functional

El módulo Sidesoft Account Payment está diseñado para gestionar y facilitar los pagos dentro del ERP Openbravo. Su propósito es simplificar el proceso de contabilización y seguimiento de los pagos realizados por la empresa. Los actores involucrados incluyen usuarios de negocio que operan en el módulo financiero, así como el equipo de soporte técnico que se encarga de mantener su funcionalidad. El alcance del módulo abarca la gestión de pagos, desde su creación hasta la validación de su estado. Dependencias clave son la compatibilidad con la versión del skin 2.50 a 3.00, el núcleo de Openbravo y la estructura del marco Openbravo 3.0.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/account/payment` |
| Web | `web/ec.com.sidesoft.account.payment/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SACPMT`

# Guía de chat — Sidesoft Account Payment

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.account.payment`).

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

- ¿Cómo puedo registrar un nuevo pago en el sistema?
- ¿Qué debo hacer si un pago fue rechazado?
- ¿Cómo puedo verificar el estado de un pago registrado?
- ¿Dónde puedo encontrar un informe sobre los pagos realizados?
- ¿Qué pasos debo seguir para corregir un error en un pago existente?
- ¿Cómo se actualizan los estados de los pagos automáticamente?
- ¿Existen limitaciones sobre la cantidad de pagos que puedo registrar?
- ¿Qué hacer si necesito asistencia técnica con el módulo de pagos?

# Domain — data model

## Functional

El módulo se basa en la tabla de cabecera 'fin_payment', que es la entidad central que almacena información sobre los pagos. El flujo de datos implica que cada pago puede pasar por diferentes etapas antes de ser contabilizado correctamente, aunque no se detallan varias tablas de etapa específicas en el inventario. Es crucial el trigger 'SACPMT_POSTED_STATUS_TRG', que maneja el estatus de publicación de los pagos en la tabla 'fin_payment'. Este trigger asegura que cualquier cambio relacionado con el estado del pago se maneje adecuadamente manteniendo la integridad de los datos.

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

No se listan ventanas específicas en el módulo, lo que indica que la interfaz de usuario aún no se ha definido en detalle. Sin embargo, los usuarios normalmente navegan mediante el menú principal de Openbravo, lo que permite acceder a las funcionalidades básicas del módulo de pagos a través de opciones relacionadas con la gestión financiera.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.account.payment.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.account.payment.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo actualmente no incluye botones de proceso adicionales ni informes predefinidos. Sin embargo, se puede suponer que las validaciones frecuentes incluirían el chequeo del estado de los pagos y la corrección de errores antes de su contabilización. Los usuarios pueden esperar realizar acciones típicas como completar, retornar o rechazar pagos en función del flujo financiero estándar.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.account.payment.es_ES/referencedata/translation/`.

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

No se han identificado clases Java en este módulo, lo que sugiere que toda la funcionalidad está implementada a través de los componentes estándar del framework de Openbravo y las rutinas PL PGSQL.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.account.payment`.

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
| Trigger `SACPMT_POSTED_STATUS_TRG` | `fin_payment` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El trigger 'SACPMT_POSTED_STATUS_TRG' juega un rol fundamental en la gestión de la base de datos, ya que se encarga de la lógica necesaria para actualizar el estado de los pagos en el sistema. Al ser una rutina PL/pgSQL, permite expresar de manera consistente las reglas de negocio que deben cumplirse una vez que un pago es registrado o modificado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SACPMT_POSTED_STATUS_TRG` | `fin_payment` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SACPMT_POSTED_STATUS_TRG.xml` |
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

Módulo: `ec.com.sidesoft.account.payment`.

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

# Glosario — prefijo `SACPMT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SACPMT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.account.payment` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

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
## Sidesoft Payment Plan Information
**Package:** `ec.com.sidesoft.payment.plan.info`

# Module overview — Sidesoft Payment Plan Information

## Functional

El módulo 'Sidesoft Payment Plan Information' está diseñado para gestionar y brindar información sobre planes de pagos en el contexto de tesorería. Los actores principales incluyen usuarios de negocio que manejan pagos, así como personal de soporte que puede requerir información técnica. Este módulo es esencial para la gestión de flujos de tesorería, proporcionando datos relevantes para la toma de decisiones financieras. La dependencia con la '2.50 to 3.00 Compatibility Skin' sugiere que los usuarios deben tener compatibilidad con estas versiones para un funcionamiento óptimo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payment/plan/info` |
| Web | `web/ec.com.sidesoft.payment.plan.info/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPPI`

# Guía de chat — Sidesoft Payment Plan Information

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payment.plan.info`).

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

- ¿Cómo puedo acceder a la información sobre planes de pagos?
- ¿Qué modificaciones se han realizado en la tabla de planes de pago?
- ¿Dónde puedo encontrar ayuda sobre la administración de tesorería?
- ¿Existen reportes disponibles para visualizar los planes de pagos?
- ¿Cómo afectará la nueva versión del módulo a la funcionalidad existente?
- ¿Qué hacer si no encuentro la información que necesito sobre pagos?
- ¿Cuál es la dependencia entre este módulo y otras funcionalidades del sistema?
- ¿Cómo se gestionan las modificaciones en los planes de pago?

# Domain — data model

## Functional

El módulo se centra principalmente en la entidad 'FIN_PAYMENT_SCHEDULE', la cual ha sido modificada para incluir campos adicionales relacionados con planes de pago de clientes. Aunque no se proporcionan detalles sobre etapas o relaciones complejas, la simplificación del modelo sugiere un enfoque directo en la entrada y visualización de datos. No existen triggers o funciones PL habilitados, lo que implica que la lógica de negocio puede depender de procesos externos o de la interfaz de usuario para manejar transacciones.

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
| `SSPPI_Payment_Sched_Ord_V` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`FIN_PAYMENT_SCHEDULE`

### Views

`SSPPI_PAYMENT_SCHED_ORD_V`

# Functional — windows and menus

## Functional

Actualmente, no se han definido ventanas específicas en la interfaz de usuario para este módulo, lo que sugiere que la interacción con el mismo se lleva a cabo a través de elementos de menú o accesos directos. Esto puede limitar la navegación, ya que se deberá acceder a la información de manera más dinámica, posiblemente mediante búsqueda de tablas o datos en tiempo real.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payment.plan.info.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payment.plan.info.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `60825C9E68644DBC9C530DDCABE05A6E`

- **AD_TAB_ID:** `60825C9E68644DBC9C530DDCABE05A6E` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 230 | EM_Ssppi_Capital | `EM_Ssppi_Capital` | No | No | — |
| 240 | EM_Ssppi_Shareno | `EM_Ssppi_Shareno` | No | No | — |
| 250 | EM_Ssppi_Interest | `EM_Ssppi_Interest` | No | No | — |
| 260 | EM_Ssppi_Monthly_Surcharge | `EM_Ssppi_Monthly_Surcharge` | No | No | — |

### Pestaña `EB0E0C5A58344F7FA345097E7365CD22`

- **AD_TAB_ID:** `EB0E0C5A58344F7FA345097E7365CD22` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 90 | EM_Ssppi_Shareno | `EM_Ssppi_Shareno` | No | No | — |
| 100 | EM_Ssppi_Capital | `EM_Ssppi_Capital` | No | No | — |
| 110 | EM_Ssppi_Interest | `EM_Ssppi_Interest` | No | No | — |
| 120 | EM_Ssppi_Monthly_Surcharge | `EM_Ssppi_Monthly_Surcharge` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que no hay botones de proceso definidos, las acciones dentro del módulo pueden ser mínimas. Esto sugiere que las funciones se basan en la visualización de información más que en la ejecución de procesos típicos que requerirían botones como 'completar', 'retornar' o 'rechazar'. La falta de informes y validaciones directamente asociadas puede también indicar que las operaciones dependen más de la consulta y visualización de datos ya existentes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payment.plan.info.es_ES/referencedata/translation/`.

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

El módulo no incluye clases Java específicas, lo que sugiere que su funcionalidad se basa completamente en las capacidades nativas de Openbravo y las configuraciones realizadas en la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payment.plan.info`.

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

No existen triggers ni funciones PL específicas para soporte en este módulo, lo que puede indicar un enfoque menos dinámico en cuanto a las operaciones de base de datos. La gestión del módulo depende esencialmente de la estructura de la tabla modificada 'FIN_PAYMENT_SCHEDULE', y su integración en el contexto de otras funcionalidades del sistema.

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

Módulo: `ec.com.sidesoft.payment.plan.info`.

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

# Glosario — prefijo `SSPPI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPPI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payment.plan.info` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Payment In Voided
**Package:** `ec.com.sidesoft.payment.voided`

# Module overview — Sidesoft Payment In Voided

## Functional

El módulo 'Sidesoft Payment In Voided' se diseñó para permitir la anulación de cobros en el sistema Openbravo, facilitando a los usuarios la gestión de transacciones no deseadas. Este módulo está dirigido principalmente a los departamentos de tesorería y finanzas dentro de las organizaciones, quienes requieren una herramienta eficaz para manejar cobros que han sido cancelados. Su alcance abarca desde la identificación de cobros hasta su reversión en el sistema, asegurando así la precisión en los registros contables de la organización. Es importante mencionar que este módulo depende de la gestión avanzada de cuentas por pagar y cobrar, por lo que su implementación debe considerar estas funcionalidades relacionadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payment/voided` |
| Web | `web/ec.com.sidesoft.payment.voided/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Advanced Payables and Receivables Mngmt

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPIV`

# Guía de chat — Sidesoft Payment In Voided

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payment.voided`).

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

- ¿Cómo puedo anular un cobro que he registrado por error?
- ¿Qué validaciones se realizan al intentar anular un cobro?
- ¿El módulo genera algún informe al anular un cobro?
- ¿Qué debo hacer si el botón de anulación no aparece en la UI?
- ¿Puedo revertir la anulación de un cobro una vez realizada?
- ¿Qué efectos tiene la anulación de un cobro en los informes financieros?
- ¿Los usuarios tienen permisos restringidos para anular cobros?
- ¿Cómo afecta la anulación de un cobro a las cuentas por cobrar?

# Domain — data model

## Functional

El módulo se basa en la entidad 'FIN_PAYMENT', que es la cabecera que almacena todos los registros de pagos. La anulación de un cobro se realiza a través de un proceso específico que se activa en la ventana de cobros. A través de un trigger clave, denominado 'SSPIV_ANNULMENT_STATUS', se actualiza el estado del pago según sea necesario cuando se utiliza la funcionalidad de anulación. La relación entre las transacciones se maneja de forma directa a través de la tabla de pagos, y el trigger asegura que se mantenga la integridad de los datos a lo largo del proceso.

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

El módulo no cuenta con ventanas específicas como parte de su diseño, pero se integra dentro de la interfaz de cobros existente de Openbravo, permitiendo a los usuarios acceder a la función de anulación de manera intuitiva. A través de la UI, los usuarios pueden navegar a la sección de cobros y utilizar el botón que activa el proceso de anulación de cobros.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.payment.voided.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.payment.voided.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `C4B6506838E14A349D6717D6856F1B56`

- **AD_TAB_ID:** `C4B6506838E14A349D6717D6856F1B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 125 | Annulment | `EM_Sspiv_Annulment` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El proceso principal asociado con este módulo es la anulación de cobros, el cual se activa mediante un botón específico en la UI. Este proceso valida que se cumplan todas las condiciones necesarias antes de confirmar la anulación, como la verificación del estado actual del pago. Aunque no se generan informes específicos en esta funcionalidad, se espera que los usuarios sigan procedimientos de validación habituales para asegurar que todos los cobros que se están anulando sean correctos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.payment.voided.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Anular | Annulment | Annulment | `sspiv_cancel_collection` | Anula / desiste la operación de compra. | — |
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
| Botón (PL/pgSQL) | Anular | Annulment | Annulment | `sspiv_cancel_collection` | Anula / desiste la operación de compra. | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Anular | Annulment | PL `sspiv_cancel_collection` | Anula / desiste la operación de compra. | — |
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
| `sspiv_error_process` | not allowed to delete | not allowed to delete | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `sspiv_Annulment` | successful annulment process | successful annulment process | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

Este módulo no incluye funciones o clases Java, centrándose en su funcionalidad únicamente a través de los elementos PL/pgSQL y los triggers mencionados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payment.voided`.

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
| Trigger `SSPIV_ANNULMENT_STATUS` | `fin_payment` | before DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y las funciones PL desempeñan un papel crucial en el soporte del módulo. En particular, el trigger 'SSPIV_ANNULMENT_STATUS' se ejecuta automáticamente en la tabla 'FIN_PAYMENT' al realizar una anulación, lo que garantiza que se actualicen correctamente los registros sin necesidad de intervención manual. Además, existe una función PL vinculada al proceso que ayuda a manejar la lógica de anulación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSPIV_ANNULMENT_STATUS` | `fin_payment` | before | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/SSPIV_ANNULMENT_STATUS.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sspiv_cancel_collection` | Anular | Anula / desiste la operación de compra. | — | `model/functions/SSPIV_CANCEL_COLLECTION.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Anular | `Annulment` | Botón (PL/pgSQL) | PL `sspiv_cancel_collection` | N | Anula / desiste la operación de compra. |

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

Módulo: `ec.com.sidesoft.payment.voided`.

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

# Glosario — prefijo `SSPIV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPIV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payment.voided` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Annulment` — Anular

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Payments Upgrades
**Package:** `ec.com.sidesoft.payments.upgrades`

# Module overview — Payments Upgrades

## Functional

El módulo 'Payments Upgrades' tiene como propósito mejorar y gestionar los procesos de pago en la plataforma Openbravo. Este módulo es utilizado principalmente por usuarios de negocio para gestionar los pagos, así como por el soporte L2 para resolver problemas y optimizar el uso del sistema. Está diseñado para ser compatible con versiones anteriores del software, específicamente desde la versión 2.50 hasta la 3.00, apoyándose en el marco básico de Openbravo 3.0. Las dependencias del módulo aseguran su correcta funcionalidad y la integración con otros elementos del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/payments/upgrades` |
| Web | `web/ec.com.sidesoft.payments.upgrades/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPU`

# Guía de chat — Payments Upgrades

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.payments.upgrades`).

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

- ¿Cómo puedo gestionar un pago fallido?
- ¿Dónde veo el historial de mis pagos?
- ¿Qué hago si necesito revertir un pago?
- ¿Cuáles son los requisitos para procesar un pago exitoso?
- ¿Cómo se visualizan las actualizaciones de pagos en el sistema?
- ¿Hay informes disponibles para analizar las transacciones de pago?
- ¿Cómo se pueden validar los datos de un pago antes de procesarlo?
- ¿Qué pasos seguir para solucionar problemas de integridad en los datos de pago?

# Domain — data model

## Functional

El módulo se basa en una entidad cabecera que rastrea las transacciones de pago y sus respectivas actualizaciones. Aunque no se han definido tablas físicas específicas ni triggers, el módulo incluye funciones PL que son esenciales para procesar las operaciones relacionadas con los pagos. Esto sugiere que los datos de las transacciones se gestionan en etapas que implican la preparación de datos de pago, la validación de estos datos y la finalización del proceso. Las relaciones dentro del modelo de datos se centran principalmente en los antecedentes de pagos y sus actualizaciones en el sistema.

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

No se han definido ventanas específicas para el módulo en la interfaz de usuario (UI), lo que sugiere que su funcionalidad puede estar integrada en otras secciones del sistema o que no se brinda una interfaz gráfica directa para los usuarios. La navegación puede requerir acceso a otros módulos existentes donde se realicen los pagos.

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

El módulo cuenta con un proceso vinculado a una función PL específica, lo que implica que las operaciones de gestión de pagos se ejecutan a través de un solo botón. Este botón permite a los usuarios completar, retornar o rechazar los procesos de pago según sea necesario. Dado que no se especifican informes asociados, es fundamental realizar validaciones mínimas en el proceso para garantizar que los datos ingresados cumplan con los criterios establecidos.

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
| Background (PL/pgSQL) | Update Payment Schedule | Update Payment Schedule | Update Payment Schedule | `sspu_payments` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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

El módulo no incluye clases Java, lo que indica que su funcionalidad se basa principalmente en los procesos de PL y en la integración con los componentes existentes del sistema Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.payments.upgrades`.

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

Aunque el módulo no cuenta con triggers específicos, la función PL es fundamental para el soporte y la gestión de operaciones de pago. Esta función asegura que las transacciones se realicen de manera correcta y que se actualicen los registros, lo que es vital para mantener la integridad de los datos en el sistema.

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
| `sspu_payments` | Update Payment Schedule | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SSPU_PAYMENTS.xml` |
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

Módulo: `ec.com.sidesoft.payments.upgrades`.

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

# Glosario — prefijo `SSPU`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPU` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.payments.upgrades` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Update Payment Schedule` — Update Payment Schedule

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft ImportData for Payments
**Package:** `ec.com.sidesoft.importdata.payments`

# Module overview — Sidesoft ImportData for Payments

## Functional

El módulo 'Sidesoft ImportData for Payments' está diseñado para facilitar la carga de datos relacionados con cobros y pagos en el ERP Openbravo. Su propósito principal es optimizar el proceso de importación de datos financieros desde archivos externos, permitiendo que los usuarios de negocio sin conocimientos técnicos administren esta tarea de manera eficiente. Los principales actores de este módulo incluyen usuarios de negocio que manejan datos financieros, así como desarrolladores y soporte técnico encargados de su implementación y mantenimiento. El alcance del módulo se limita a la carga y procesamiento de datos de pagos, por lo que depende de la correcta configuración y utilización de tablas asociadas en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/importdata/payments` |
| Web | `web/ec.com.sidesoft.importdata.payments/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SIMPPYS`

# Guía de chat — Sidesoft ImportData for Payments

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.importdata.payments`).

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
- «¿Qué es la tabla simppys_payment_detail?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo cargar un archivo de pagos correctamente?
- ¿Qué tipos de archivo son soportados para la carga de pagos?
- ¿Qué debo hacer si recibo un error al intentar cargar un archivo?
- ¿Cómo puedo validar los datos antes de la carga?
- ¿Dónde puedo consultar los resultados de mis cargas de datos?
- ¿Cuáles son los campos obligatorios en el archivo de pagos?
- ¿Cómo puedo manejar pagos duplicados en la carga?
- ¿Qué hacer si necesito modificar un registro ya cargado?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad cabecera 'Simppys_PaymentDataUpload', que almacena información inicial sobre las cargas de datos de pagos. Esta entidad se relaciona con 'Simppys_PaymentDetail', que captura detalles específicos de cada transacción. Aunque no hay triggers definidos, existen funciones Java que ejecutan la lógica de negocio, gestionando las transacciones y validaciones necesarias durante el proceso de importación. Las relaciones entre estas entidades son cruciales, ya que permiten que las operaciones sobre 'Simppys_PaymentDataUpload' generen automáticamente las entradas correspondientes en 'Simppys_PaymentDetail'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `simppys_payment_detail` |
| `simppys_paymentdataupload` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `simppys_payment_detail` | simppys_payment_detail | — | — | c_bp_bankaccount_id→c_bp_bankaccount; ssfi_banktransfer_id→ssfi_banktransfer; c_bpartner_id→c_bpartner; ad_client_id→ad_client; c_costcenter_id→c_costcenter (+11) | Detalle enlazado a c_bp_bankaccount, c_bpartner, ssfi_banktransfer. | PK `simppys_pd_key`; Cols: simppys_paymentdataupload_id, payment_doctype, documentno, referenceno, paymentdate; `SIMPPYS_PD_ISACTIVE`: ISACTIVE IN ('Y', 'N'); `SIMPPYS_PD_ONLY_PAYMENT`: ONLY_PAYMENT IN ('Y', 'N') (+1) |
| `simppys_paymentdataupload` | simppys_paymentdataupload | — | — | ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `simppys_pdu_key`; Cols: payment_type, c_doctype_id, documentno, description, processed; `SIMPPYS_PDU_ISACTIVE`: ISACTIVE IN ('Y', 'N'); `SIMPPYS_PDU_PROCESSED`: PROCESSED IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `simppys_payment_detail` |
| `simppys_paymentdataupload` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo cuenta con una ventana principal 'Carga de datos de cobros/pagos' que permite a los usuarios navegar intuitivamente para cargar archivos, ejecutar procesos de validación y revisar resultados de importación. La interfaz está diseñada para ser sencilla y accesible, asegurando que los usuarios puedan completar sus tareas en pocas etapas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.importdata.payments.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Carga de datos de cobros/pagos | Payment Data Upload |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Carga de datos | Data Upload | Sí |
| Carga de datos de cobros/pagos | Payment Data Upload | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.importdata.payments.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Carga de datos de cobros/pagos

- **AD_WINDOW_ID:** `4449C1F0BBF04ECA96345ACAF5DE2E9F`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `37A80EBCAA134F2EB34A96B544382302` | 0 |
| 20 | Lines | `82DA90A4F07046CE93BD5A8BAF0CB97F` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Header (ventana: Carga de datos de cobros/pagos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 100 | Type | `Payment_Type` | No | No | — |
| 110 | Document Type | `C_Doctype_ID` | No | No | — |
| 120 | Document No. | `Documentno` | No | Sí | — |
| 130 | Description | `Description` | No | No | — |
| 140 | Process_Date | `Process_Date` | No | Sí | — |
| 150 | Processed | `Processed` | No | Sí | — |
| 160 | Load Lines | `Load_Lines` | No | No | — |
| 170 | Process Payments | `Process` | No | No | — |

### Lines (ventana: Carga de datos de cobros/pagos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 100 | Document Type | `Payment_DocType` | No | No | — |
| 110 | Document No. | `Documentno` | No | No | — |
| 120 | Reference No. | `Referenceno` | No | No | — |
| 130 | Payment date | `Paymentdate` | No | No | — |
| 140 | Business Partner | `C_Bpartner_ID` | No | No | — |
| 150 | Seller | `Seller_ID` | No | No | — |
| 160 | Partner Bank Account | `C_Bp_Bankaccount_ID` | No | No | — |
| 170 | Description | `Description` | No | No | — |
| 180 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 190 | Financial Account | `FIN_Financial_Account_ID` | No | No | — |
| 200 | Currency | `C_Currency_ID` | No | No | — |
| 210 | Amount | `Amount` | No | No | — |
| 220 | Invoice | `C_Invoice_ID` | No | No | — |
| 230 | Fee date | `Duedate` | No | No | — |
| 240 | Client bank | `Ssfi_Banktransfer_ID` | No | No | — |
| 250 | Check No. | `Checkno` | No | No | — |
| 260 | Deposit No. | `Depositno` | No | No | — |
| 270 | Cost Center | `C_Costcenter_ID` | No | No | — |
| 280 | 1st Dimension | `User1_ID` | No | No | — |
| 290 | 2nd Dimension | `User2_ID` | No | No | — |
| 295 | G/L Item | `C_Glitem_ID` | No | No | — |
| 300 | Only Payment | `Only_Payment` | No | No | — |
| 310 | Processed | `Processed` | No | Sí | — |
| 320 | Result | `Result` | No | Sí | — |
| 330 | Error | `Error` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Existen dos procesos clave en el módulo: 'Simppys_LoadLines', que se encarga de la lectura y carga de archivos CSV que contienen datos de pagos, y 'Simppys_ProcessPayments', que procesa los datos cargados y los integra en el sistema financiero de Openbravo. Ambos procesos incluyen botones típicos para completar la carga de datos y manejar excepciones. Durante este flujo, se implementan validaciones frecuentes para asegurar que la información cargada cumpla con las reglas de negocio establecidas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.importdata.payments.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar líneas | Load Lines | Simppys Load Lines | Java `Simppys_LoadLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Simppys_PaymentDataUpload_ID`, Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo | `src/ec/com/sidesoft/importdata/payments/ad_process/Simppys_LoadLines.java` |
| Botón (Java) | Procesar | Process Payments | Simppys Process Payments | Java `Simppys_ProcessPayments` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Simppys_PaymentDataUpload_ID` | `src/ec/com/sidesoft/importdata/payments/ad_process/Simppys_ProcessPayments.java` |
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
| Botón (Java) | Cargar líneas | `Simppys_LoadLines` | Proceso Java (toolbar/background) | `Simppys_PaymentDataUpload_ID` | Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo | `src/ec/com/sidesoft/importdata/payments/ad_process/Simppys_LoadLines.java` |
| Botón (Java) | Procesar | `Simppys_ProcessPayments` | Proceso Java (toolbar/background) | `Simppys_PaymentDataUpload_ID` | — | `src/ec/com/sidesoft/importdata/payments/ad_process/Simppys_ProcessPayments.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar líneas | Load Lines | Simppys Load Lines | Java `Simppys_LoadLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Simppys_PaymentDataUpload_ID`, Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo | `src/ec/com/sidesoft/importdata/payments/ad_process/Simppys_LoadLines.java` |
| Botón (Java) | Procesar | Process Payments | Simppys Process Payments | Java `Simppys_ProcessPayments` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Simppys_PaymentDataUpload_ID` | `src/ec/com/sidesoft/importdata/payments/ad_process/Simppys_ProcessPayments.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar líneas | Load Lines | Java `Simppys_LoadLines` | Proceso Openbravo registro `Simppys_PaymentDataUpload_ID`, Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo | Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo |
| Botón (Java) | Procesar | Process Payments | Java `Simppys_ProcessPayments` | Proceso Openbravo registro `Simppys_PaymentDataUpload_ID` | Proceso Openbravo registro `Simppys_PaymentDataUpload_ID` |
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

El módulo utiliza múltiples clases Java para llevar a cabo su funcionalidad, incluyendo procesos de carga y manejo de eventos de persistencia. Esto implica la validación de datos y la ejecución de lógica empresarial necesaria para asegurar que las entradas de pagos se manejen correctamente en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.importdata.payments`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Simppys_BlockRecord` | ad_events | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/importdata/payments/ad_events/Simppys_BlockRecord.java` |
| `Simppys_LoadLines` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/importdata/payments/ad_process/Simppys_LoadLines.java` |
| `Simppys_ProcessPayments` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/importdata/payments/ad_process/Simppys_ProcessPayments.java` |
| `Simppys_Helper` | utils | — | — | `src/ec/com/sidesoft/importdata/payments/utils/Simppys_Helper.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Simppys_PaymentDataUpload Doctype` | `C_Doctype.AD_Table_ID = '37A80EBCAA134F2EB34A96B544382302'` |
| AD_VAL_RULE | — | `Seller` | `C_BPartner.IsActive = 'Y'
AND C_BPartner.IsEmployee = CASE
    WHEN C_BPartner.IsEmployee = 'Y' AND C_BPartner.IsSalesRe` |
| AD_VAL_RULE | — | `Simppys_PaymentDetail Doctype` | `C_Doctype.AD_Table_ID = 'D1A97202E832470285C9B1EB026D54E2'
AND C_Doctype.IsSoTrx = CASE WHEN @Payment_Type@ = 'C' THEN '` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Aunque el módulo no incorpora triggers ni funciones PL, los procesos Java son esenciales para el soporte de la lógica de negocio, manejando la integridad de los datos y la ejecución de tareas críticas durante el proceso de carga. Estos procesos gestionan las interacciones con la base de datos, permitiendo que las entradas de pago sean creadas y actualizadas de acuerdo con la información suministrada en los archivos.

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
| 1 | Cargar líneas | `Simppys Load Lines` | Botón (Java) | Java `Simppys_LoadLines` | N | Proceso Openbravo registro `Simppys_PaymentDataUpload_ID`, Archivo CSV no encontrado; El numero de columnas no coincide con el formato; No se encontraron datos en el archivo |
| 2 | Procesar | `Simppys Process Payments` | Botón (Java) | Java `Simppys_ProcessPayments` | N | Proceso Openbravo registro `Simppys_PaymentDataUpload_ID` |

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

Módulo: `ec.com.sidesoft.importdata.payments`.

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

# Glosario — prefijo `SIMPPYS`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SIMPPYS` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.importdata.payments` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Simppys Load Lines` — Cargar líneas
- `Simppys Process Payments` — Procesar

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Proposal Payments
**Package:** `ec.com.sidesoft.localization.proposal.payments`

# Module overview — Proposal Payments

## Functional

El módulo 'Proposal Payments' tiene como propósito gestionar propuestas de pagos en el sistema ERP Openbravo. Los actores principales incluyen usuarios de negocio que crean y gestionan propuestas de pagos, así como desarrolladores que pueden interactuar con los procesos y funcionalidades del módulo. Este módulo es fundamental en la gestión financiera, al facilitar la creación y administración de pagos propuestos antes de su ejecución real. Dependencias clave incluyen el módulo 'Core', que proporciona la infraestructura necesaria para la operación del módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/proposal/payments` |
| Web | `web/ec.com.sidesoft.localization.proposal.payments/` |

### Declared dependencies

- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLPP`

# Guía de chat — Proposal Payments

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.proposal.payments`).

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

- ¿Cómo puedo crear una nueva propuesta de pago?
- ¿Qué debo hacer si una propuesta de pago es rechazada?
- ¿Dónde puedo ver el historial de propuestas de pago?
- ¿Cómo se puede editar una propuesta de pago existente?
- ¿Qué información es obligatoria al crear una propuesta de pago?
- ¿Cómo puedo validar que los datos de la propuesta de pago son correctos?
- ¿Qué pasa si necesito eliminar una propuesta de pago?
- ¿Existen reportes disponibles sobre las propuestas de pago realizadas?

# Domain — data model

## Functional

La entidad principal del módulo se centra en la tabla 'FIN_PAYMENT_PROPOSAL', que actúa como cabecera para todas las propuestas de pagos. Aunque el inventario no menciona etapas específicas, se puede inferir que las propuestas de pago pasan por un proceso de creación, revisión y aprobación. Las relaciones con otras tablas, como 'FIN_PAYMENT_PROP_DETAIL', permiten un desglose detallado de cada propuesta de pago. Es importante señalar que no hay triggers asociados, lo que sugiere que la lógica de negocio puede estar en las funciones y en las clases Java del módulo.

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

`FIN_PAYMENT_PROPOSAL`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El acceso al módulo 'Proposal Payments' se realiza a través de la interfaz de usuario de Openbravo, donde no se especifican ventanas ni botones adicionales. La navegación se realiza a través de los menús generales de Openbravo, y las funcionalidades del módulo están integradas dentro del flujo de trabajo existente del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.proposal.payments.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.proposal.payments.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `2DD6F1E2CAE0456AA9797A1D627BFF5E`

- **AD_TAB_ID:** `2DD6F1E2CAE0456AA9797A1D627BFF5E` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 180 | EM_Slpp_Payment_Doctype_ID | `EM_Slpp_Payment_Doctype_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un botón típico asociado a un proceso que permite completar la creación o gestión de una propuesta de pago. Este proceso permite la manipulación de datos y el cálculo de detalles relacionados con la propuesta. Aunque no se especifican informes, es común que los usuarios necesiten validar datos durante el proceso y recibir mensajes de error gestionados a través de la lógica de negocio establecida en las funciones Java y PL generadas en el backend.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.proposal.payments.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Procesar Propuesta de Pago (Customizado) | Custom Process Payment Proposal | Slpp_ProcessPaymentProposal | Java `ProcessPaymentProposal` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/localization/proposal/payments/ad_actionbutton/ProcessPaymentProposal.java` |
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
| Informe (servlet) | Procesar Propuesta de Pago (Customizado) | `ProcessPaymentProposal` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/localization/proposal/payments/ad_actionbutton/ProcessPaymentProposal.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Procesar Propuesta de Pago (Customizado) | Custom Process Payment Proposal | Slpp_ProcessPaymentProposal | Java `ProcessPaymentProposal` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/localization/proposal/payments/ad_actionbutton/ProcessPaymentProposal.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Procesar Propuesta de Pago (Customizado) | Custom Process Payment Proposal | Java `ProcessPaymentProposal` | Genera PDF desde JRXML `—`; contexto sesión `—`. | Genera PDF desde JRXML `—`; contexto sesión `—`. |
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
| `Slpp_Doctype_Not_Found` | Field "Payments Doctype" does not selected. | Field "Payments Doctype" does not selected. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo utiliza varias clases Java para manejar la lógica del proceso de propuesta de pagos. Entre las clases más destacadas se encuentran 'ProcessPaymentProposal' y 'FIN_PaymentProposalProcess', que gestionan las operaciones fundamentales del módulo, incluyendo la creación y gestión de propuestas de pago.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.proposal.payments`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ProcessPaymentProposal` | ad_actionbutton | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/localization/proposal/payments/ad_actionbutton/ProcessPaymentProposal.java` |
| `FIN_AddPayment` | process | — | — | `src/ec/com/sidesoft/localization/proposal/payments/process/FIN_AddPayment.java` |
| `FIN_PaymentProposalProcess` | process | org | Proceso / informe Java | `src/ec/com/sidesoft/localization/proposal/payments/process/FIN_PaymentProposalProcess.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Doctypes Payment Out` | `C_DocType.DocBaseType IN ('APP', 'ARR') AND C_DocType.IsSOTrx='N' AND AD_ISORGINCLUDED(@AD_Org_ID@,C_DocType.AD_Org_ID, ` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y las funciones PL no están presentes en este módulo, lo que implica que la mayoría de la lógica de negocio y las validaciones se manejan a través de las clases Java. Esto proporciona una mayor flexibilidad y control a los desarrolladores que trabajan en el módulo, permitiendo una fácil integración con otros procesos del ERP.

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
| 1 | Procesar Propuesta de Pago (Customizado) | `Slpp_ProcessPaymentProposal` | Informe (servlet) | Java `ProcessPaymentProposal` | N | Genera PDF desde JRXML `—`; contexto sesión `—`. |

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

Módulo: `ec.com.sidesoft.localization.proposal.payments`.

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

# Glosario — prefijo `SLPP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLPP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.proposal.payments` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Slpp_ProcessPaymentProposal` — Procesar Propuesta de Pago (Customizado)

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Complement of Payments
**Package:** `ec.com.sidesoft.localization.ecuador.payment.complement`

# Module overview — Complement of Payments

## Functional

El módulo 'Complement of Payments' se centra en la gestión de complementos de pagos en el sistema Openbravo, específicamente para su uso en el contexto ecuatoriano. Está diseñado para usuarios de negocio que administran transacciones financieras y para el soporte técnico que se encarga de resolver incidentes relacionados. El alcance del módulo incluye la modificación de tablas existentes y la inclusión de funcionalidades que mejoran el manejo de pagos. Depende de la compatibilidad con la 'Compatibility Skin' desde versiones 2.50 hasta 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/ecuador/payment/complement` |
| Web | `web/ec.com.sidesoft.localization.ecuador.payment.complement/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPAC`

# Guía de chat — Complement of Payments

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.ecuador.payment.complement`).

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

- ¿Cómo puedo registrar un complemento de pago?
- ¿Este módulo es compatible con versiones anteriores de Openbravo?
- ¿Qué sucede si un pago complementario falla?
- ¿Puedo modificar la tabla de pagos directamente?
- ¿Dónde encuentro los reportes de pagos realizados?
- ¿Se puede integrar este módulo con otros sistemas?
- ¿Cuáles son los criterios para validar un complemento de pago?
- ¿Hay algún proceso para rechazar un complemento de pago?

# Domain — data model

## Functional

El módulo utiliza la tabla principal 'FIN_PAYMENT', que actúa como entidad cabecera para gestionar las operaciones de pago. Aunque no se especifican etapas formales, se puede inferir que las operaciones implican la manipulación de datos de pago en torno a un flujo que podría incluir complementos a pagos ya realizados. Las relaciones con otras tablas no están claramente definidas en el inventario, dado que no se especifican tablas auxiliares o adicionales en este módulo, lo que puede indicar que su enfoque es más directo sobre los pagos.

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

El módulo no incluye ventanas específicas para la interacción a nivel de interfaz de usuario (UI) en su inventario reportado. Esto sugiere que las operaciones se realizarían dentro de un contexto general, probablemente integrándose con procesos existentes en el sistema Openbravo sin interfaces dedicadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.ecuador.payment.complement.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.ecuador.payment.complement.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `C4B6506838E14A349D6717D6856F1B56`

- **AD_TAB_ID:** `C4B6506838E14A349D6717D6856F1B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 61 | Check account | `EM_Sspac_Checkacc` | No | No | — |
| 62 | Charger For | `EM_Sspac_C_Bpartner_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

En términos de procesos funcionales, el módulo no tiene botones de proceso específicos, informes descritos o validaciones para usuarios al momento de registrar o gestionar los complementos de pagos. Sin embargo, se esperaría que los usuarios interactúen con la funcionalidad de la tabla 'FIN_PAYMENT' para realizar todos los ajustes necesarios.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.ecuador.payment.complement.es_ES/referencedata/translation/`.

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

No se reportan clases Java dentro del módulo, lo que indica que la funcionalidad es probable que esté completamente integrada en la lógica del ERP sin necesidad de personalizaciones específicas en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.ecuador.payment.complement`.

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
| AD_VAL_RULE | — | `SSPAC_ChargerForValidate` | `C_BPartner.IsActive = 'Y' 
AND (C_BPartner.IsEmployee = (case when (C_BPartner.IsEmployee = 'Y' and C_BPARTNER.IsSalesRe` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

No se especifican triggers ni funciones PL dentro del módulo, lo que indica que el soporte técnico podría depender de la funcionalidad nativa de Openbravo y su diseño anterior. Esto podría facilitar el manejo de problemas relacionados con la base de datos, aunque limita la capacidad de personalización directa desde el módulo.

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

Módulo: `ec.com.sidesoft.localization.ecuador.payment.complement`.

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

# Glosario — prefijo `SSPAC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPAC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.ecuador.payment.complement` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Postdated Check
**Package:** `ec.com.sidesoft.postdated.check`

# Module overview — Sidesoft Postdated Check

## Functional

El módulo Sidesoft Postdated Check permite a las empresas gestionar cheques posfechados en su sistema ERP Openbravo. Su propósito principal es facilitar el registro y seguimiento de estos cheques, integrando su flujo con los procesos de pagos en la tesorería. Este módulo es utilizado por usuarios de negocio en el área financiera, así como por el equipo de soporte y desarrollo para asegurar la correcta implementación y mantenimiento del sistema.
Este módulo tiene dependencias con otras extensiones que permiten su funcionalidad óptima, incluyendo compatibilidad con la piel para diferentes versiones y localización específica para Ecuador en el ámbito financiero. Los actores principales son los usuarios que realizan la conciliación de pagos y el seguimiento de cheques posfechados en sus procesos contables.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/postdated/check` |
| Web | `web/ec.com.sidesoft.postdated.check/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Complement of Payments
- Custom Advanced Payables and Receivables Mngmt
- Localization of Ecuador - Finances
- Sidesoft Payment Plan Information

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSPCH`

# Guía de chat — Sidesoft Postdated Check

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.postdated.check`).

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
- «¿Qué es la tabla sspch_payment_plan?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo ingreso un cheque posfechado en el sistema?
- ¿Qué hacer si hay un error en el registro de un cheque posfechado?
- ¿Puedo editar la información de un cheque posfechado después de haberlo guardado?
- ¿Cómo puedo validar si un cheque posfechado ha sido pagado?
- ¿Qué pasos debo seguir para generar un reporte de cheques posfechados?
- ¿Cómo se relacionan los cheques posfechados con el plan de pagos?
- ¿Cuál es la función del botón de completar en el módulo?
- ¿Qué sucede si intento ingresar un monto de cheque que es menor o igual a cero?

# Domain — data model

## Functional

La entidad principal del módulo es la tabla 'sspch_payment_plan', que almacena la información relevante sobre los planes de pagos asociados a cheques posfechados. Este módulo interactúa principalmente con las tablas 'FIN_PAYMENT' y 'FIN_PAYMENT_SCHEDULEDETAIL', las cuales se ven modificadas para garantizar la integridad de los datos de pagos en relación con los cheques. Las relaciones entre estas entidades permiten el seguimiento de los cheques posfechados a través de sus diferentes etapas, desde su emisión hasta su pago efectivo.
Los triggers son elementos clave para mantener la calidad de los datos en este módulo. Por ejemplo, el trigger 'SSPCH_PDC_VALIDATIONS_TRG' valida que el total de cheques no sea menor que cero, mientras que 'SSPCH_VAL_SHARE_SECUENCE_TRG' se encarga de excluir registros duplicados o ya procesados sin saldo pendiente, asegurando así que la lógica de negocio se cumpla correctamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sspch_invoice` |
| `sspch_payment_plan` |
| `sspch_postdated_checks` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sspch_invoice` | Sspch_Invoice | `SSPCH_DUPLICATED_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoice_id→c_invoice; sspch_postdated_checks_id→sspch_postdated_checks | Detalle enlazado a ad_client, ad_org, c_invoice. Validado por trigger(s): SSPCH_DUPLICATED_TRG. | PK `sspch_invoice_key`; Cols: c_invoice_id, sspch_postdated_checks_id, description, issummary; `SSPCH_INVOICE_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPCH_INVOICE_ISSUMMARY_CHK`: ISSUMMARY IN ('Y', 'N') |
| `sspch_payment_plan` | Sspch_Payment_Plan | `SSPCH_VALIDATION_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoice_id→c_invoice; c_doctype_id→c_doctype; fin_payment_schedule_id→fin_payment_schedule (+3) | Detalle enlazado a ad_client, ad_org, c_invoice. Validado por trigger(s): SSPCH_VALIDATION_TRG. | PK `sspch_payment_p_key`; Cols: sspch_invoice_id, documentno, shareno, fin_payment_schedule_id, checkno; `SSPCH_PAYMENT_P_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPCH_PAYMENT_P_ISADVANCE_CHK`: ISADVANCE IN ('Y', 'N') (+1) |
| `sspch_postdated_checks` | Sspch_Postdated_Checks | `SSPCH_PDC_VALIDATIONS_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; ssfi_banktransfer_id→ssfi_banktransfer; c_bpartner_id→c_bpartner; c_doctype_id→c_doctype (+3) | Detalle enlazado a ad_client, ad_org, ssfi_banktransfer. Validado por trigger(s): SSPCH_PDC_VALIDATIONS_TRG. | PK `sspch_postd_chk_key`; Cols: check_from, check_up, c_doctype_id, payment_date, isdatepaymentplan; `SSPCH_POSTD_CHK_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `SSPCH_POSTD_CHK_ISDATEPP_CHK`: ISDATEPAYMENTPLAN IN ('Y', 'N') (+1) |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Sspch_Invoice` |
| `Sspch_Payment_Plan` |
| `Sspch_Postdated_Checks` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`FIN_PAYMENT`, `FIN_PAYMENT_SCHEDULEDETAIL`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

La navegación en el módulo se realiza a través de la ventana denominada 'Cheques Posfechados'. Desde esta interfaz, los usuarios pueden acceder a las diferentes opciones y funciones disponibles para gestionar los cheques. La interfaz está diseñada de manera intuitiva, permitiendo búsquedas rápidas y la ejecución de tareas comunes relacionadas con la gestión de cheques posfechados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.postdated.check.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Cheques Posfechados | Post-Dated Checks |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Cheques Posfechados | Post-Dated Checks | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.postdated.check.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Cheques Posfechados

- **AD_WINDOW_ID:** `E6621E62BF854C10ABF9849CAACEEDF8`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Post-Dated Checks | `8C5422198CEC43448BC6BCDF850C1800` | 0 |
| 20 | Inovice | `AF9A0ADF0F904C45BFBDF4DA6CBA8733` | 1 |
| 40 | Payment Plan | `44D4C9252F344623BD6119AA0FCED74E` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Post-Dated Checks (ventana: Cheques Posfechados)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Document Type | `C_Doctype_ID` | No | No | — |
| 30 | Document No. | `Documentno` | No | No | — |
| 40 | Check From | `Check_From` | No | No | — |
| 50 | Check Up | `Check_Up` | No | No | — |
| 60 | Document Type Payment | `FIN_Doctype_ID` | No | No | — |
| 70 | Payment Date | `Payment_Date` | No | No | — |
| 80 | Date based  on payment plan | `Isdatepaymentplan` | No | No | — |
| 90 | Client | `C_Bpartner_ID` | No | No | — |
| 130 | Deposit in financial account | `FIN_Financial_Account_ID` | No | No | — |
| 140 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 150 | Total Checks | `Total_Checks` | No | No | — |
| 160 | Manual registration | `Ismanualreg` | No | No | — |
| 161 | Payment_Day | `Payment_Day` | No | No | — |
| 170 | Load Lines | `Load_Lines` | No | No | — |
| 180 | Process | `Process` | No | No | — |
| 190 | Client bank | `Ssfi_Banktransfer_ID` | No | No | 5DDED8C71B6A484C8D5A1553FB8899EA |
| 200 | Account | `Account` | No | No | 5DDED8C71B6A484C8D5A1553FB8899EA |
| 210 | Accoun Holder | `Account_Holder` | No | No | 5DDED8C71B6A484C8D5A1553FB8899EA |

### Inovice (ventana: Cheques Posfechados)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Bill of sale | `C_Invoice_ID` | No | No | — |
| 20 | Description | `Description` | No | No | — |

### Pestaña `C4B6506838E14A349D6717D6856F1B56`

- **AD_TAB_ID:** `C4B6506838E14A349D6717D6856F1B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2090 | Check | `EM_Sspch_Checkno` | No | No | 5DDED8C71B6A484C8D5A1553FB8899EA |
| 2100 | Account holder | `EM_Sspch_Account_Holder` | No | No | 5DDED8C71B6A484C8D5A1553FB8899EA |

### Payment Plan (ventana: Cheques Posfechados)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Document Type | `C_Doctype_ID` | No | Sí | — |
| 20 | Invoice | `C_Invoice_ID` | No | No | — |
| 20 | Document No | `Documentno` | No | Sí | — |
| 30 | Share No | `Shareno` | No | Sí | — |
| 40 | Payment Date | `Payment_Date` | No | Sí | — |
| 41 | General_Payment_Date | `General_Payment_Date` | No | No | — |
| 50 | Quota value | `Amount_Payment` | No | Sí | — |
| 60 | Check No | `Checkno` | No | No | — |
| 70 | Amount Payment | `Quota_Value` | No | No | — |
| 80 | Advance | `Isadvance` | No | No | — |
| 90 | Advance Value | `Advance_Value` | No | No | — |
| 110 | Client bank | `Ssfi_Banktransfer_ID` | No | No | — |
| 120 | Account | `Account` | No | No | — |
| 130 | Accoun Holder | `Account_Holder` | No | No | — |
| 140 | Sequence | `Sequence` | No | Sí | — |
| — | Fin_Payment_Schedule_ID | `FIN_Payment_Schedule_ID` | No | No | — |

### Pestaña `F6C2283A21314407BBBB23FF14B85ED4`

- **AD_TAB_ID:** `F6C2283A21314407BBBB23FF14B85ED4` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 300 | Pos dated check | `EM_Sspch_Postdated_Checks_ID` | No | No | — |
| 310 | Check | `EM_Sspch_Checkno` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye varios botones de proceso, tales como 'Completar', que permite finalizar la entrada de un cheque posfechado, y 'Retornar', que facilita la corrección de registros si es necesario. A pesar de que no incluye informes predeterminados, las validaciones frecuentes aseguran que los valores ingresados cumplan con los requisitos, notificando a los usuarios sobre cualquier inconsistencia antes de que el cheque sea guardado o procesado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.postdated.check.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar Líneas | Load Lines | Sspch - Load Lines | `sspch_load_lines` | CURSOR DE CUOTAS ORDENADAS POR CUOTAS Y VALOR ACENDENTE; CONDICIONES PARA SECUENCIA DE NUMERO DE CHEQUE(POR NUMERO DE CUOTA); CONDICIONES SEGUN EL DIA DE COBRO DE LA CABECERA; VALIDACIONES PARA VALOR DE CUOTA Y VALOR DE… | — |
| Botón (PL/pgSQL) | Procesar | Process | Sspch - Process | `sspch_processed` | fin_payment_scheduledetail_id , ad_client_id , ad_org_id , createdby , updatedby; , fin_payment_detail_id , amount , writeoffamt , iscanceled , c_bpartner_id; , doubtfuldebt_amount , fin_payment_schedule_invoice , em_ss… | — |
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
| Botón (PL/pgSQL) | Cargar Líneas | Load Lines | Sspch - Load Lines | `sspch_load_lines` | CURSOR DE CUOTAS ORDENADAS POR CUOTAS Y VALOR ACENDENTE; CONDICIONES PARA SECUENCIA DE NUMERO DE CHEQUE(POR NUMERO DE CUOTA); CONDICIONES SEGUN EL DIA DE COBRO DE LA CABECERA; VALIDACIONES PARA VALOR DE CUOTA Y VALOR DE… | — |
| Botón (PL/pgSQL) | Procesar | Process | Sspch - Process | `sspch_processed` | fin_payment_scheduledetail_id , ad_client_id , ad_org_id , createdby , updatedby; , fin_payment_detail_id , amount , writeoffamt , iscanceled , c_bpartner_id; , doubtfuldebt_amount , fin_payment_schedule_invoice , em_ss… | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Cargar Líneas | Load Lines | PL `sspch_load_lines` | CURSOR DE CUOTAS ORDENADAS POR CUOTAS Y VALOR ACENDENTE; CONDICIONES PARA SECUENCIA DE NUMERO DE CHEQUE(POR NUMERO DE CUOTA); CONDICIONES SEGUN EL DIA DE COBRO DE LA CABECERA; VALIDACIONES PARA VALOR DE CUOTA Y VALOR DE… | CURSOR DE CUOTAS ORDENADAS POR CUOTAS Y VALOR ACENDENTE; CONDICIONES PARA SECUENCIA DE NUMERO DE CHEQUE(POR NUMERO DE CUOTA); CONDICIONES SEGUN EL DIA DE COBRO DE LA CABECERA; VALIDACIONES PARA VALOR DE CUOTA Y VALOR DE ANTICIPO; valor de la cuota es mayor a el valor dividido por lineas más sobrantes anteriores; Si el valor calculado para la cuota no tiene sobrantes sumados |
| Botón (PL/pgSQL) | Procesar | Process | PL `sspch_processed` | fin_payment_scheduledetail_id , ad_client_id , ad_org_id , createdby , updatedby; , fin_payment_detail_id , amount , writeoffamt , iscanceled , c_bpartner_id; , doubtfuldebt_amount , fin_payment_schedule_invoice , em_ss… | fin_payment_scheduledetail_id	, ad_client_id				, ad_org_id			, createdby			, updatedby; , fin_payment_detail_id		, amount				, writeoffamt			, iscanceled			, c_bpartner_id; , doubtfuldebt_amount		, fin_payment_schedule_invoice						, em_sspch_postdated_checks_id); VALUES (  get_uuid()			, v_AD_Client_ID			, v_AD_ORG_ID			, v_AD_USER_ID			, v_AD_USER_ID; , v_fin_payment_detail_id	, Cur_fin_payment_plan.amount_payment	, 0.00				, 'N'				, v_c_bpartner_id; , 0.00				, Cur_fin_payment_plan.fin_payment_schedule_id 				, v_Record_ID); |
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
| `Sspch_Amount` | amount | amount | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspch_Processed` | You cannot delete a transaction in the processed state. | You cannot delete a transaction in the processed state. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspch_validation_cunt` | There are no records to process | There are no records to process | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspch_Duplicated` | There is already a record with the same number of checks, bank name and invoice. | There is already a record with the same number of checks, bank name and invoice. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspch_RelatedPostDatedCheck` | Related post-dated check. | Related post-dated check. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspch_Secuence` | You must load the lines sequentially | You must load the lines sequentially | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspch_InsufficientValue` | Collections pending to be executed, insufficient value. | Collections pending to be executed, insufficient value. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `Sspch_PaymentsCreated` | Payments Created | Payments Created | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo incluye la clase Java 'UpdatePaymentSchedule', diseñada para gestionar la actualización de los planes de pago al interactuar en la UI con los cheques posfechados. Esta clase asegura que los datos correctos sean mostrados y validados en los formularios, contribuyendo así a una mejor experiencia de usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.postdated.check`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `UpdatePaymentSchedule` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/postdated/check/ad_callouts/UpdatePaymentSchedule.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `SSPCH_DUPLICATED_TRG` | `sspch_invoice` | before INSERT/UPDATE/DELETE | Check if trying to move object from module not in dev |
| Trigger `SSPCH_PDC_VALIDATIONS_TRG` | `sspch_postdated_checks` | before INSERT/UPDATE/DELETE | El campo Total Cheques es menos a debe ser mayor a 0.; Check if trying to move object from module not in dev |
| Trigger `SSPCH_VALIDATION_TRG` | `sspch_payment_plan` | before INSERT/UPDATE/DELETE | Check if trying to move object from module not in dev |
| Trigger `SSPCH_VAL_SHARE_SECUENCE_TRG` | `fin_payment_scheduledetail` | before INSERT/UPDATE | RAISE EXCEPTION '% | % ', vPaymentAmount, vNoPostedAmount;; Excluir los registros ya cargados y sin saldo pendiente; Excluir las cuotas cargadas por la misma transaccion Y sin saldo pendiente de CH-P; VALIDAR SOLO SI SE… |
| AD_VAL_RULE | — | `Invoice by Default` | `C_Invoice_ID in (Select c_invoice_id from Sspch_Invoice where sspch_postdated_checks_id=@sspch_postdated_checks_id@)` |
| AD_VAL_RULE | — | `Sspch-DocumentType` | `C_DocType.ad_table_id in ('8C5422198CEC43448BC6BCDF850C1800')` |
| AD_VAL_RULE | — | `Banktransfer by Default` | `Ssfi_Banktransfer_ID = (SELECT Ssfi_Banktransfer_ID from sspch_postdated_checks where sspch_postdated_checks_id=@sspch_p` |
| AD_VAL_RULE | — | `Payment Schedule by Default` | `FIN_Payment_Schedule_ID in (select FIN_Payment_Schedule_ID from FIN_Payment_Schedule where c_invoice_id=@c_invoice_id@ )` |
| AD_VAL_RULE | — | `Financial Account Check` | `Fin_Financial_Account_ID in (select fin_financial_account_id from ssfi_financial_user where ad_user_id = @#AD_User_ID@ a` |
| AD_VAL_RULE | — | `Sspch-SalesInvoice` | `C_Invoice.C_BPartner_ID=@C_BPartner_ID@ AND
C_Invoice.outstandingamt > 0` |
| AD_VAL_RULE | — | `Sspch-DocumentType-Payment` | `C_DOCTYPE.DOCBASETYPE = 'ARR' AND C_DOCTYPE.C_DOCTYPE_ID in (
Select fu.c_doctype_id
From fin_financial_account fa  
Joi` |
| AD_VAL_RULE | — | `Sspch-PaymentMethod` | `EXISTS (Select pm.fin_paymentmethod_id 
From fin_paymentmethod pm
	Join fin_pay_exec_process pep on pep.fin_pay_exec_pro` |
| AD_VAL_RULE | — | `Document by Default` | `C_DocType.C_Doctype_ID = (Select C_DocTypeTarget_ID from c_invoice where c_invoice_id=@c_invoice_id@)` |
| Función PL `sspch_load_lines` | — | invocación proceso | CURSOR DE CUOTAS ORDENADAS POR CUOTAS Y VALOR ACENDENTE; CONDICIONES PARA SECUENCIA DE NUMERO DE CHEQUE(POR NUMERO DE CUOTA); CONDICIONES SEGUN EL DIA DE COBRO DE LA CABECERA |
| Función PL `sspch_processed` | — | invocación proceso | fin_payment_scheduledetail_id	, ad_client_id				, ad_org_id			, createdby			, updatedby; , fin_payment_detail_id		, amount				, writeoffamt			, iscanceled			, c_bpartner_id; , doubtfuldebt_amount		, fin_payment_schedule_invoice						, em_sspch_postdated_checks_id) |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers dentro de este módulo juegan un rol crítico para la validación de datos en las operaciones de los cheques posfechados. La función PL está vinculado a los procesos automatizados que se disparan en función de eventos en la base de datos, garantizando que la lógica de negocio se aplique correctamente y evitando errores durante la ejecución de los procesos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `SSPCH_VAL_SHARE_SECUENCE_TRG` | `fin_payment_scheduledetail` | before | INSERT/UPDATE | RAISE EXCEPTION '% | % ', vPaymentAmount, vNoPostedAmount;; Excluir los registros ya cargados y sin saldo pendiente; Excluir las cuotas cargadas por la misma transaccion Y sin saldo pendiente de CH-P; VALIDAR SOLO SI SE… | `model/triggers/SSPCH_VAL_SHARE_SECUENCE_TRG.xml` |
| `SSPCH_DUPLICATED_TRG` | `sspch_invoice` | before | INSERT/UPDATE/DELETE | Check if trying to move object from module not in dev | `model/triggers/SSPCH_DUPLICATED_TRG.xml` |
| `SSPCH_VALIDATION_TRG` | `sspch_payment_plan` | before | INSERT/UPDATE/DELETE | Check if trying to move object from module not in dev | `model/triggers/SSPCH_VALIDATION_TRG.xml` |
| `SSPCH_PDC_VALIDATIONS_TRG` | `sspch_postdated_checks` | before | INSERT/UPDATE/DELETE | El campo Total Cheques es menos a debe ser mayor a 0.; Check if trying to move object from module not in dev | `model/triggers/SSPCH_PDC_VALIDATIONS_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `sspch_load_lines` | Cargar Líneas | CURSOR DE CUOTAS ORDENADAS POR CUOTAS Y VALOR ACENDENTE; CONDICIONES PARA SECUENCIA DE NUMERO DE CHEQUE(POR NUMERO DE CUOTA); CONDICIONES SEGUN EL DIA DE COBRO DE LA CABECERA; VALIDACIONES PARA VALOR DE CUOTA Y VALOR DE… | CURSOR DE CUOTAS ORDENADAS POR CUOTAS Y VALOR ACENDENTE; CONDICIONES PARA SECUENCIA DE NUMERO DE CHEQUE(POR NUMERO DE CUOTA); CONDICIONES SEGUN EL DIA DE COBRO DE LA CABECERA; VALIDACIONES PARA VALOR DE CUOTA Y VALOR DE ANTICIPO; valor de la cuota es mayor a el valor dividido por lineas más sobrantes anteriores; Si el valor calculado para la cuota no tiene sobrantes sumados | `model/functions/SSPCH_LOAD_LINES.xml` |
| `sspch_processed` | Procesar | fin_payment_scheduledetail_id , ad_client_id , ad_org_id , createdby , updatedby; , fin_payment_detail_id , amount , writeoffamt , iscanceled , c_bpartner_id; , doubtfuldebt_amount , fin_payment_schedule_invoice , em_ss… | fin_payment_scheduledetail_id	, ad_client_id				, ad_org_id			, createdby			, updatedby; , fin_payment_detail_id		, amount				, writeoffamt			, iscanceled			, c_bpartner_id; , doubtfuldebt_amount		, fin_payment_schedule_invoice						, em_sspch_postdated_checks_id); VALUES (  get_uuid()			, v_AD_Client_ID			, v_AD_ORG_ID			, v_AD_USER_ID			, v_AD_USER_ID; , v_fin_payment_detail_id	, Cur_fin_payment_plan.amount_payment	, 0.00				, 'N'				, v_c_bpartner_id; , 0.00				, Cur_fin_payment_plan.fin_payment_schedule_id 				, v_Record_ID); | `model/functions/SSPCH_PROCESSED.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cargar Líneas | `Sspch - Load Lines` | Botón (PL/pgSQL) | PL `sspch_load_lines` | N | CURSOR DE CUOTAS ORDENADAS POR CUOTAS Y VALOR ACENDENTE; CONDICIONES PARA SECUENCIA DE NUMERO DE CHEQUE(POR NUMERO DE CUOTA); CONDICIONES SEGUN EL DIA DE COBRO DE LA CABECERA; VALI |
| 2 | Procesar | `Sspch - Process` | Botón (PL/pgSQL) | PL `sspch_processed` | N | fin_payment_scheduledetail_id , ad_client_id , ad_org_id , createdby , updatedby; , fin_payment_detail_id , amount , writeoffamt , iscanceled , c_bpartner_id; , doubtfuldebt_amount |

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

Módulo: `ec.com.sidesoft.postdated.check`.

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

# Glosario — prefijo `SSPCH`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSPCH` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.postdated.check` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Sspch - Load Lines` — Cargar Líneas
- `Sspch - Process` — Procesar

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Deposit Number
**Package:** `ec.com.sidesoft.deposit.number`

# Module overview — Sidesoft Deposit Number

## Functional

El módulo 'Sidesoft Deposit Number' está diseñado para gestionar el número de depósitos dentro del sistema Openbravo ERP. Su propósito principal es facilitar el manejo y la generación de pagos mediante una interfaz intuitiva y accesible. Este módulo es utilizado por usuarios de negocio y administradores financieros que requieren registrar y ejecutar pagos de manera eficiente. Dependiendo de la configuración del ERP, puede integrarse con otros módulos relacionados con la contabilidad y la gestión financiera, asegurando la consistencia de los datos en toda la plataforma.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/deposit/number` |
| Web | `web/ec.com.sidesoft.deposit.number/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSDN`

# Guía de chat — Sidesoft Deposit Number

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.deposit.number`).

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

- ¿Cómo puedo ejecutar un pago masivo?
- ¿Qué debo hacer si me aparece un error al intentar ejecutar pagos?
- ¿Dónde puedo ver el historial de pagos procesados?
- ¿Puedo cancelar un pago después de haber sido ejecutado?
- ¿Existen validaciones específicas que debo tener en cuenta al ejecutar pagos?
- ¿Cómo se integran los depósitos en la contabilidad del ERP?
- ¿Qué tipo de errores son comunes al ejecutar pagos?
- ¿Cómo se puede personalizar el módulo para necesidades específicas de mi negocio?

# Domain — data model

## Functional

El módulo está diseñado en torno a entidades clave como el proceso de ejecución de pagos. Este proceso es fundamental ya que permite al usuario seleccionar y gestionar varios métodos de pago mediante un solo flujo de trabajo. Las relaciones entre las entidades se establecen a través de las clases y funciones Java proporcionadas, que interaccionan con el modelo de datos de Openbravo para llevar a cabo los procesos de pago. Es importante destacar que no se han definido triggers específicos ni funciones PL dentro de este módulo, lo que simplifica el mantenimiento y adaptación del mismo.

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

Navegar por el módulo 'Sidesoft Deposit Number' se realiza a través del menú principal de Openbravo, donde los usuarios pueden acceder a las funcionalidades de ejecución de pagos. La interfaz es simple, permitiendo a los usuarios seleccionar pagos y ejecutar procesos mediante botones visibles que guían el flujo de trabajo de manera intuitiva. Aunque no se han especificado ventanas adicionales en el inventario, el módulo se integra fluidamente en la estructura existente del ERP, permitiendo una experiencia de usuario coherente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.deposit.number.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Ejecución de Pagos/Cobros | Payment Execution | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.deposit.number.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo contiene un proceso central que permite a los usuarios ejecutar pagos de manera masiva. Los botones típicos incluyen 'Ejecutar Pagos', que inicia el flujo de pagos, permitiendo a los usuarios completar las transacciones seleccionadas. Durante la ejecución, se llevan a cabo validaciones para asegurar que los datos son correctos y están completos; de no ser así, se notifican errores que deben ser atendidos antes de proceder. Sin embargo, no se han definido informes específicos dentro del módulo, lo que implica que la información puede estar disponible a través de las funcionalidades generales de reportes del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.deposit.number.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Execute Payment | Execute Payment | SSDN_ExecutePayment | Java `ExecutePayments` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/deposit/number/ad_actionbutton/ExecutePayments.java` |
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
| Informe (servlet) | Execute Payment | `ExecutePayments` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/deposit/number/ad_actionbutton/ExecutePayments.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Execute Payment | Execute Payment | SSDN_ExecutePayment | Java `ExecutePayments` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/deposit/number/ad_actionbutton/ExecutePayments.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Informe (servlet) | Execute Payment | Execute Payment | Java `ExecutePayments` | Genera PDF desde JRXML `—`; contexto sesión `—`. | Genera PDF desde JRXML `—`; contexto sesión `—`. |
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

El módulo incluye varias clases Java responsables de implementar la lógica específica para la ejecución de pagos. Estas clases gestionan tanto las interacciones con la interfaz de usuario como la manipulación de los datos subyacentes, asegurando que la información sea procesada correctamente durante la ejecución de las operaciones de pago. Estas clases son críticas para la operación del módulo y permiten extender o modificar el comportamiento según sea necesario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.deposit.number`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ExecutePayments` | ad_actionbutton | HttpSecureAppServlet | — | `src/ec/com/sidesoft/deposit/number/ad_actionbutton/ExecutePayments.java` |
| `BatchPaymentExecution` | ad_forms | HttpSecureAppServlet | — | `src/ec/com/sidesoft/deposit/number/ad_forms/BatchPaymentExecution.java` |
| `SSDNBatchPaymentExecution` | ad_forms | BatchPaymentExecution | — | `src/ec/com/sidesoft/deposit/number/ad_forms/SSDNBatchPaymentExecution.java` |
| `AdvPaymentMngtDao` | dao | — | — | `src/ec/com/sidesoft/deposit/number/dao/AdvPaymentMngtDao.java` |
| `BatchPaymentDao` | dao | — | — | `src/ec/com/sidesoft/deposit/number/dao/BatchPaymentDao.java` |
| `MatchTransactionDao` | dao | BaseOBObject | — | `src/ec/com/sidesoft/deposit/number/dao/MatchTransactionDao.java` |
| `TransactionsDao` | dao | — | — | `src/ec/com/sidesoft/deposit/number/dao/TransactionsDao.java` |
| `FIN_ExecutePayment` | process | — | — | `src/ec/com/sidesoft/deposit/number/process/FIN_ExecutePayment.java` |
| `FIN_TransactionProcess` | process | org | Proceso / informe Java | `src/ec/com/sidesoft/deposit/number/process/FIN_TransactionProcess.java` |
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

En este módulo, aunque no se han definido triggers ni funciones PL, el rol de la lógica de negocio y manejo de datos se realiza a través de las implementaciones en Java. Esta implementación asegura que las operaciones de pago se gestionen correctamente dentro de las bases de datos de Openbravo, utilizando las herramientas y utilidades proporcionadas por el ERP para interacciones con los datos. Esto permite un manejo efectivo de las operaciones a pesar de la ausencia de elementos adicionales en la base de datos.

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
| 1 | Execute Payment | `SSDN_ExecutePayment` | Informe (servlet) | Java `ExecutePayments` | N | Genera PDF desde JRXML `—`; contexto sesión `—`. |

**Total acciones documentadas (extract):** **1** (callouts y guardado estándar: ver el modelo físico del paquete (`model/triggers/`, `model/functions/`)).
<!-- /knowledge-extract:button_matrix -->

# Technical — front-end (JS/CSS)

## Functional

Recursos estáticos registrados vía `ComponentProvider` o referenciados desde ventanas Smartclient.

## Technical

<!-- knowledge-extract:web_assets -->
| Recurso web |
| --- |
| `web/ec.com.sidesoft.deposit.number/FIN_Utilities.js` |
| `web/ec.com.sidesoft.deposit.number/images/GLItemGridCancel-xButt.png` |
| `web/ec.com.sidesoft.deposit.number/images/add.png` |
| `web/ec.com.sidesoft.deposit.number/images/view.png` |
| `web/ec.com.sidesoft.deposit.number/js/ob-aprm-addPayment.js` |
| `web/ec.com.sidesoft.deposit.number/js/ob-aprm-addTransaction.js` |
| `web/ec.com.sidesoft.deposit.number/js/ob-aprm-findTransaction.js` |
| `web/ec.com.sidesoft.deposit.number/js/ob-aprm-fundsTransfer.js` |
| `web/ec.com.sidesoft.deposit.number/js/ob-aprm-matchStatement.js` |
| `web/ec.com.sidesoft.deposit.number/js/ob-aprm-utilities.js` |
<!-- /knowledge-extract:web_assets -->

# Anexo — Suposiciones, archivos no encontrados y huecos

Módulo: `ec.com.sidesoft.deposit.number`.

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

# Glosario — prefijo `SSDN`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSDN` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.deposit.number` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `SSDN_ExecutePayment` — Execute Payment

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Deposit Reconciliation
**Package:** `ec.com.sidesoft.deposit.reconciliation`

# Module overview — Sidesoft Deposit Reconciliation

## Functional

El módulo Sidesoft Deposit Reconciliation tiene como propósito facilitar la reconciliación de depósitos en Openbravo, permitiendo a los usuarios gestionar de manera eficiente las transacciones bancarias. Está diseñado para ser utilizado por analistas financieros y contadores, quienes necesitan asegurar que los registros de los depósitos coincidan con los extractos bancarios. El alcance del módulo abarca la integración de declaraciones bancarias y la validación de pagos, así como la creación de reportes para la toma de decisiones. Este módulo depende de funcionalidades existentes en otros módulos, como la gestión avanzada de cuentas por pagar y cobrar, y requiere de la importación de extractos bancarios en formato CSV o OFX.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/deposit/reconciliation` |
| Web | `web/ec.com.sidesoft.deposit.reconciliation/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Advanced Payables and Receivables Mngmt
- Core
- CSV Generic Bank Statement Importer
- OFX Bank Statement Format
- Openbravo 3.0 Framework
- WePay CSV importer

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSDR`

# Guía de chat — Sidesoft Deposit Reconciliation

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.deposit.reconciliation`).

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

- ¿Cómo puedo iniciar una reconciliación de depósitos?
- ¿Qué hago si un depósito no coincide con el extracto bancario?
- ¿Dónde puedo ver el historial de reconciliaciones realizadas?
- ¿Existen validaciones automáticas en el proceso de reconciliación?
- ¿Qué tipos de errores puedo esperar durante la reconcilación?
- ¿Es posible deshacer una reconciliación ya completada?
- ¿Puedo importar diferentes formatos de extractos bancarios?
- ¿Cómo afectan las reconciliaciones a mis informes financieros?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la entidad cabecera de reconciliación de depósitos, que se nutre de las líneas de extracto bancario (FIN_BANKSTATEMENTLINE) y el algoritmo de coincidencia (FIN_MATCHING_ALGORITHM). Las relaciones entre estas entidades permiten un flujo eficiente desde la importación de datos hasta la validación y conciliación final. Clave para el funcionamiento del módulo son los triggers y funciones que aseguran la correcta actualización de las tablas afectadas a medida que los registros se procesan y verifican frente a los extractos bancarios.

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

`FIN_BANKSTATEMENTLINE`, `FIN_MATCHING_ALGORITHM`, `FIN_PAYMENT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no cuenta con ventanas gráficas específicas, pero las funcionalidades se integran mediante el uso de procesos que se pueden invocar desde otras partes del ERP. Los usuarios navegan a través de estas opciones disponibles en el menú, activando los procesos asociados a la reconciliación de los depósitos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.deposit.reconciliation.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.deposit.reconciliation.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `4764AA8524BC4D3DAA9A86181C778595`

- **AD_TAB_ID:** `4764AA8524BC4D3DAA9A86181C778595` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 140 | EM_Ssdr_Matchconfirmdate | `EM_Ssdr_Matchconfirmdate` | No | No | — |

### Pestaña `7F5E8E4C55914138A358F5087B532B59`

- **AD_TAB_ID:** `7F5E8E4C55914138A358F5087B532B59` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 41 | EM_Ssdr_Referenceno | `EM_Ssdr_Referenceno` | No | No | — |
| 91 | EM_Ssdr_Fin_Payment_ID | `EM_Ssdr_Fin_Payment_ID` | No | No | — |

### Pestaña `C4B6506838E14A349D6717D6856F1B56`

- **AD_TAB_ID:** `C4B6506838E14A349D6717D6856F1B56` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 105 | EM_Ssdr_Datedeposit | `EM_Ssdr_Datedeposit` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo Sidesoft Deposit Reconciliation incluye dos procesos principales: uno para completar la reconciliación de depósitos y otro para el retorno de transacciones. Estos procesos se ejecutan a través de botones en la interfaz del usuario. Las validaciones frecuentes incluyen la verificación de que los pagos coincidan con los datos importados de los extractos bancarios, garantizando así que las cifras reflejadas sean correctas. Aunque no hay reportes específicos generados desde este módulo, se facilita la generación de informes a partir de los datos reconciliados en las tablas relacionadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.deposit.reconciliation.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | ssdr_deposit_reconclt_post | ssdr_deposit_reconclt_post | ssdr_deposit_reconclt_post | `ssdr_deposit_reconclt_post` | Automatic creation of financial transaction; UPDATE fin_payment_schedule/Plan de pagos; Getting DueAmount from FIN_PAYMENT_SCHEDULE for the Invoice; Updating Payment Monitor values into C_INVOICE | — |
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
| Background | Conciliación de depósitos cobros | Deposit Reconciliation | Deposit Reconciliation | *(OBUIAPP / manual)* | — | — |
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
| Botón (PL/pgSQL) | ssdr_deposit_reconclt_post | ssdr_deposit_reconclt_post | ssdr_deposit_reconclt_post | `ssdr_deposit_reconclt_post` | Automatic creation of financial transaction; UPDATE fin_payment_schedule/Plan de pagos; Getting DueAmount from FIN_PAYMENT_SCHEDULE for the Invoice; Updating Payment Monitor values into C_INVOICE | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | ssdr_deposit_reconclt_post | ssdr_deposit_reconclt_post | PL `ssdr_deposit_reconclt_post` | Automatic creation of financial transaction; UPDATE fin_payment_schedule/Plan de pagos; Getting DueAmount from FIN_PAYMENT_SCHEDULE for the Invoice; Updating Payment Monitor values into C_INVOICE | Automatic creation of financial transaction; UPDATE fin_payment_schedule/Plan de pagos; Getting DueAmount from FIN_PAYMENT_SCHEDULE for the Invoice; Updating Payment Monitor values into C_INVOICE |
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

El módulo incluye varias clases en Java que proporcionan la lógica de negocio necesaria para la reconciliación de depósitos, como la clase DepositReconciliation, que gestiona el proceso de reconciliación de manera programática, interactuando con el modelo de datos y asegurando que los registros sean procesados correctamente.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.deposit.reconciliation`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `DepositReconciliation` | ad_backgrounds | DalBaseProcess | — | `src/ec/com/sidesoft/deposit/reconciliation/ad_backgrounds/DepositReconciliation.java` |
| `FIN_FinaccTransactionEventListener` | event | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/deposit/reconciliation/event/FIN_FinaccTransactionEventListener.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Java event/validator | `FIN_FinaccTransactionEventListener` | persistencia/UI | *(leer `src/ec/com/sidesoft/deposit/reconciliation/event/FIN_FinaccTransactionEventListener.java`)* |
| Función PL `ssdr_deposit_reconclt_post` | — | invocación proceso | Automatic creation of financial transaction; UPDATE fin_payment_schedule/Plan de pagos; Getting DueAmount from FIN_PAYMENT_SCHEDULE for the Invoice |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers en este módulo son fundamentales para mantener la integridad de los datos en las tablas afectadas por las operaciones de reconciliación. No se especifican triggers como parte del inventario, lo que sugiere que la lógica de negocio se maneja principalmente a través de funciones PL. Estas funciones permiten una ejecución programática de las operaciones necesarias para realizar reconciliaciones y manejar los registros en las entidades de bancos y pagos.

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
| `ssdr_deposit_reconclt_post` | ssdr_deposit_reconclt_post | Automatic creation of financial transaction; UPDATE fin_payment_schedule/Plan de pagos; Getting DueAmount from FIN_PAYMENT_SCHEDULE for the Invoice; Updating Payment Monitor values into C_INVOICE | Automatic creation of financial transaction; UPDATE fin_payment_schedule/Plan de pagos; Getting DueAmount from FIN_PAYMENT_SCHEDULE for the Invoice; Updating Payment Monitor values into C_INVOICE | `model/functions/SSDR_DEPOSIT_RECONCLT_POST.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ssdr_deposit_reconclt_post | `ssdr_deposit_reconclt_post` | Botón (PL/pgSQL) | PL `ssdr_deposit_reconclt_post` | N | Automatic creation of financial transaction; UPDATE fin_payment_schedule/Plan de pagos; Getting DueAmount from FIN_PAYMENT_SCHEDULE for the Invoice; Updating Payment Monitor values |

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

Módulo: `ec.com.sidesoft.deposit.reconciliation`.

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

# Glosario — prefijo `SSDR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSDR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.deposit.reconciliation` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Deposit Reconciliation` — Conciliación de depósitos cobros
- `ssdr_deposit_reconclt_post` — ssdr_deposit_reconclt_post

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft transfer authorization
**Package:** `ec.com.sidesoft.transfer.authorization`

# Module overview — Sidesoft transfer authorization

## Functional

El módulo 'Sidesoft transfer authorization' se utiliza para gestionar la autorización de transferencias internas en el sistema ERP Openbravo. Este módulo permite a los usuarios validar y autorizar movimientos internos, lo que es crítico para mantener la integridad de las operaciones logísticas. Los actores principales incluyen los usuarios de negocio que realizan las solicitudes de transferencia y los supervisores que revisan y autorizan dichas solicitudes. El módulo depende de la compatibilidad con la skin de versiones 2.50 a 3.00 de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/transfer/authorization` |
| Web | `web/ec.com.sidesoft.transfer.authorization/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**1.0.0** (from `AD_MODULE.xml`).

### DB prefix

`STAT`

# Guía de chat — Sidesoft transfer authorization

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.transfer.authorization`).

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
- «¿Qué es la tabla stat_user_doc?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo enviar una solicitud de transferencia para autorización?
- ¿Qué hago si mi solicitud de transferencia ha sido rechazada?
- ¿Cómo puedo verificar el estado de una solicitud de transferencia?
- ¿Cuál es el procedimiento si necesito cancelar una transferencia ya solicitada?
- ¿Quién debe aprobar mis solicitudes de transferencia?
- ¿Qué información necesito proporcionar al enviar una solicitud de transferencia?
- ¿Con qué frecuencia se revisan las solicitudes de transferencia?
- ¿Qué sucede si no recibo una notificación de aprobación de transferencia?

# Domain — data model

## Functional

La entidad cabecera central en este módulo es 'stat_user_doc', que almacena la información sobre las transferencias internas y su estado de autorización. Se relaciona con otras tablas clave como 'AD_ORG', 'C_DOCTYPE', y 'M_MOVEMENT', que contienen información organizativa y de documentos relacionados con los movimientos. Aunque no se especifican triggers en el módulo, se incluye una función PL que respalda los procesos de autorización y notificaciones automatizadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `stat_user_doc` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `stat_user_doc` | Stat_User_Doc | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_user_id→ad_user; c_doctype_id→c_doctype | Detalle enlazado a ad_client, ad_org, ad_user. | PK `stat_user_doc_key`; Cols: description, c_doctype_id, ad_user_id; `STAT_USER_DOC_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `Stat_User_Doc` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`AD_ORG`, `C_DOCTYPE`, `M_MOVEMENT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo tiene una única pestaña, la cual muestra la interfaz para gestionar las solicitudes de transferencia. La navegación se realiza a través de acciones en la interfaz, permitiendo a los usuarios acceder a diferentes funcionalidades relacionadas con la autorización de las transferencias. Aunque no hay ventanas adicionales, la usabilidad está enfocada en la eficiencia del proceso de autorización.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.transfer.authorization.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.transfer.authorization.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `143`

- **AD_TAB_ID:** `143` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 110 | Supervisor | `EM_Stat_C_Bpartner_ID` | No | No | — |

### Pestaña `167`

- **AD_TAB_ID:** `167` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 55 | Requires transfer authorization | `EM_Stat_Trans_Authorization` | No | No | — |

### Pestaña `259`

- **AD_TAB_ID:** `259` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 60 | Process Movements | `EM_Stat_Processing` | No | No | — |
| 2160 | Generate Code | `EM_Stat_Generate_Code` | No | No | — |

### User autorization transfer

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 15 | User | `AD_User_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Los procesos en este módulo incluyen dos botones principales: uno para completar la autorización de la transferencia y otro para retornar la solicitud si es necesario más información o si surgió un error. Aunque no se generan informes específicos dentro del módulo, se espera que los usuarios reciban notificaciones sobre el estado de sus solicitudes a través de la función PL asociada, que también ejecuta validaciones frecuentes para asegurar la exactitud de los datos y el cumplimiento de los procesos internos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.transfer.authorization.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar Código | Stat_Generate_Code | Stat_Generate_Code | Java `SendEmailSupervisor` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `M_Movement_ID` | `src/ec/com/sidesoft/transfer/authorization/ad_process/SendEmailSupervisor.java` |
| Botón (PL/pgSQL) | Processar Movimiento | Stat_Process_Movement | Stat_Process_Movement | `Stat_New_Movement_Post` | Almacena el minuto actual con el minuto original; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL | — |
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
| Botón (Java) | Generar Código | `SendEmailSupervisor` | Proceso Java (toolbar/background) | `M_Movement_ID` | — | `src/ec/com/sidesoft/transfer/authorization/ad_process/SendEmailSupervisor.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar Código | Stat_Generate_Code | Stat_Generate_Code | Java `SendEmailSupervisor` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `M_Movement_ID` | `src/ec/com/sidesoft/transfer/authorization/ad_process/SendEmailSupervisor.java` |
| Botón (PL/pgSQL) | Processar Movimiento | Stat_Process_Movement | Stat_Process_Movement | `Stat_New_Movement_Post` | Almacena el minuto actual con el minuto original; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Generar Código | Stat_Generate_Code | Java `SendEmailSupervisor` | Proceso Openbravo registro `M_Movement_ID` | Proceso Openbravo registro `M_Movement_ID` |
| Botón (PL/pgSQL) | Processar Movimiento | Stat_Process_Movement | PL `Stat_New_Movement_Post` | Almacena el minuto actual con el minuto original; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL | Almacena el minuto actual con el minuto original; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL |
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

El módulo incluye una clase Java, 'SendEmailSupervisor', que se encarga de gestionar el envío de correos electrónicos a los supervisores para la confirmación de las transacciones. Esta clase utiliza el sistema de gestión de correos de Openbravo para notificar a los responsables sobre la necesidad de autorizar las transferencias internas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.transfer.authorization`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SendEmailSupervisor` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/transfer/authorization/ad_process/SendEmailSupervisor.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Stpt_C_DocType-MMM` | `C_DocType.DocBaseType IN ('MMM') and C_DocType.em_ssrs_default = 'Y' or (C_DocType.C_DocType_id in (SELECT C_DocType_id ` |
| Función PL `stat_new_movement_post` | — | invocación proceso | Almacena el minuto actual con el minuto original; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers no están implementados en este módulo, pero se utiliza una función PL para manejar la lógica del negocio en la autorización de transferencias y el envío de notificaciones por correo electrónico a los supervisores. Esto asegura que las operaciones de autorización se realicen de manera efectiva y que los usuarios estén informados de manera oportuna sobre el estado de sus solicitudes.

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
| `stat_new_movement_post` | Processar Movimiento | Almacena el minuto actual con el minuto original; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL | Almacena el minuto actual con el minuto original; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL | `model/functions/STAT_NEW_MOVEMENT_POST.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Generar Código | `Stat_Generate_Code` | Botón (Java) | Java `SendEmailSupervisor` | N | Proceso Openbravo registro `M_Movement_ID` |
| 2 | Processar Movimiento | `Stat_Process_Movement` | Botón (PL/pgSQL) | PL `Stat_New_Movement_Post` | N | Almacena el minuto actual con el minuto original; RECUPERA ERROR DE LA FUNCION SFPR_PROCESS_PAYROLL |

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

Módulo: `ec.com.sidesoft.transfer.authorization`.

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

# Glosario — prefijo `STAT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `STAT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.transfer.authorization` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Stat_Generate_Code` — Generar Código
- `Stat_Process_Movement` — Processar Movimiento

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
