# Openbravo Sidesoft — Plataforma y Configuración

> Core Openbravo, seguridad avanzada, procesos en background, alertas por email, carga masiva de datos, widgets, información de organización, configuración extendida, performance, índices de BD.

**Paquetes incluidos (17):**
- `ec.com.sidesoft.core.openbravo` — Sidesoft Custom Core Openbravo
- `ec.com.sidesoft.user.advanced.security` — Sidesoft User Advanced Security
- `ec.com.sidesoft.backgroundprocess` — Additional parameters for execution of background process
- `ec.com.sidesoft.email.alert` — Send Email Alert
- `ec.com.sidesoft.bulk.data.upload` — Sidesoft Bulk Data Upload
- `ec.com.sidesoft.widgets` — Sidesoft Widgets
- `ec.com.sidesoft.orginfo` — Sidesoft Organization Information
- `ec.com.sidesoft.unnoparts.extended.config` — Unnoparts Extended Config
- `ec.com.sidesoft.estandar.performance` — Estandar Performance
- `ec.com.sidesoft.balance.performance` — Sidesoft Balance customization for big data volume
- `ec.com.sidesoft.index.optmizations` — Sidesoft Database Index Optmizations
- `ec.com.sidesoft.standar.validations` — Standar Validations
- `ec.com.sidesoft.localization.special.customization` — Sidesoft localization special customization
- `ec.com.sidesoft.localization.importdata.loadvouchers` — Import data vaucher Module
- `ec.com.sidesfot.localizacion.ecuador.juliandate` — localization julian date
- `ec.com.sidesoft.report.utility` — Sidesoft Reporting Utilities
- `ec.com.sidesoft.custom.reports` — Customization -Print Reports Generics


---
## Sidesoft Custom Core Openbravo
**Package:** `ec.com.sidesoft.core.openbravo`

# Module overview — Sidesoft Custom Core Openbravo

## Functional

El módulo Sidesoft Custom Core Openbravo tiene como propósito extender las funcionalidades básicas del ERP Openbravo a través de personalizaciones que responden a necesidades específicas de los negocios. Este módulo es utilizado por actores como usuarios de negocio, soporte de nivel 2 y desarrolladores que buscan integrar o adaptar el software a sus realidades operativas. El alcance del módulo está limitado a las funcionalidades incorporadas y su interacción con otros módulos del sistema, especialmente la compatibilidad con el '2.50 to 3.00 Compatibility Skin' y el núcleo de Openbravo 3.0. Las dependencias del módulo aseguran su correcto funcionamiento en el entorno de Openbravo y sus core functionalities.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/core/openbravo` |
| Web | `web/ec.com.sidesoft.core.openbravo/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SIDCO`

# Guía de chat — Sidesoft Custom Core Openbravo

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.core.openbravo`).

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

- ¿Cómo puedo personalizar un informe existente en Openbravo?
- ¿Qué debo hacer si un proceso no se ejecuta correctamente?
- ¿Cómo puedo integrar un nuevo campo en la interfaz de usuario?
- ¿Existen guardados automáticos en el sistema?
- ¿Cómo puedo ver el historial de cambios en un registro?
- ¿Qué rol tiene cada usuario en el sistema?
- ¿Cómo puedo acceder a la configuración de permisos?
- ¿Es posible importar datos masivos al sistema?

# Domain — data model

## Functional

En el modelo de datos, se contempla que aunque no existen tablas físicas definidas dentro del módulo, se puede inferir que este se integra y trabaja en conjunto con las estructuras de datos de Openbravo. Las entidades cabecera y sus respectivas relaciones probablemente se manejan a través de configuraciones en las tablas existentes en Openbravo. Sin embargo, se debe tener en cuenta que no se han especificado disparadores o funciones PL en este módulo, lo que sugiere que la lógica de negocio se implementa de forma más ligera o mediante extensiones a nivel de configuración.

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

El módulo no presenta ventanas específicas o personalizadas, lo que indica que puede estar gestionando sus funcionalidades a través de las interfaces proporcionadas por Openbravo. La navegación a través del módulo se realizaría por medio del menú de acceso general del ERP, donde no se han indicado ventanas específicas relacionadas con este módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.core.openbravo.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Generate Audit | Generate Audit | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.core.openbravo.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

En cuanto a los procesos, dado que no hay botones, informes o procesos asociados directamente a este módulo, la ejecución de operaciones podría estar supeditada a otras funciones proporcionadas por Openbravo. Las validaciones y controles se asumen que se mantienen en el marco de las prácticas estándar del ERP, por lo que se recomienda a los usuarios familiarizarse con los procesos de Openbravo en general.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.core.openbravo.es_ES/referencedata/translation/`.

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

El módulo no incluye clases Java, lo que implica que su integración y personalizaciones están diseñadas para ser manejadas eficientemente mediante las herramientas y configuraciones disponibles en Openbravo, sin necesidad de programación adicional en Java por parte de los desarrolladores.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.core.openbravo`.

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

El módulo no contempla disparadores ni funciones PL, lo que sugiere que se está utilizando un enfoque menos dependiente de los procesos de base de datos tradicionales. Esto podría facilitar la mantenibilidad y escalabilidad del sistema, aunque se limita el control de la lógica de negocio a nivel de base de datos.

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

Módulo: `ec.com.sidesoft.core.openbravo`.

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

# Glosario — prefijo `SIDCO`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SIDCO` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.core.openbravo` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft User Advanced Security
**Package:** `ec.com.sidesoft.user.advanced.security`

# Module overview — Sidesoft User Advanced Security

## Functional

El módulo Sidesoft User Advanced Security tiene como propósito fortalecer la seguridad del sistema gestionando la complejidad de las contraseñas, los intentos de inicio de sesión, y la desactivación de usuarios por inactividad. Los actores principales son administradores de sistemas y usuarios que requieren un entorno seguro. El alcance del módulo incluye configuraciones de seguridad y auditoría de usuarios dentro del ERP Openbravo. Las dependencias del módulo incluyen compatibilidad con el 'Core' y con una 'Compatibility Skin' específica para versiones 2.50 a 3.00.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/user/advanced/security` |
| Web | `web/ec.com.sidesoft.user.advanced.security/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSUAS`

# Guía de chat — Sidesoft User Advanced Security

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.user.advanced.security`).

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
- «¿Qué es la tabla ssuas_security_config?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo establecer la longitud mínima de las contraseñas?
- ¿Qué sucede si un usuario excede el número de intentos de inicio de sesión?
- ¿Cómo se desactivan automáticamente los usuarios inactivos?
- ¿Dónde puedo ver el historial de auditoría de usuarios?
- ¿Cuál es la complejidad mínima requerida para las contraseñas?
- ¿Cómo configuro la notificación por email para usuarios desactivados?
- ¿Qué configuraciones son necesarias para activar la seguridad avanzada?
- ¿Cómo puedo validar si una contraseña cumple con los criterios establecidos?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad principal 'ssuas_security_config', que almacena la configuración de seguridad del módulo. Aunque no hay etapas adicionales o tablas relacionadas, la integración se maneja a través de esta única entidad que se utiliza para definir parámetros de seguridad como longitud mínima de contraseñas y días de inactividad permitidos. No hay triggers configurados en este módulo, lo que sugiere que la lógica de validación y de negocio se gestiona principalmente a través de clases Java y procesos en segundo plano.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssuas_excluded_user` |
| `ssuas_security_config` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssuas_excluded_user` | SSUAS_excluded_user | — | — | ad_client_id→ad_client; ssuas_security_config_id→ssuas_security_config; ad_org_id→ad_org; ad_user_id→ad_user | Detalle enlazado a ad_client, ad_org, ssuas_security_config. | PK `ssuas_eu_pk`; Cols: ssuas_security_config_id, ad_user_id; `SSUAS_EU_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `ssuas_security_config` | SSUAS_security_config | — | — | ad_client_id→ad_client; ad_org_id→ad_org | Parametrización / catálogo de soporte. | PK `ssuas_sc_key`; Cols: password_complexity, password_length, notification_email, inactivity_days, attempts; `SSUAS_SC_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SSUAS_excluded_user` |
| `SSUAS_security_config` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo se navega a través de una única ventana llamada 'Parametros de seguridad', donde los usuarios pueden gestionar la configuración de seguridad requerida. Desde esta ventana, se permite ajustar los parámetros de validación y seguimiento de usuarios, facilitando el acceso a las configuraciones necesarias para mantener un entorno seguro.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.user.advanced.security.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Parametros de seguridad | Security Parameters |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Parametros de seguridad | Security Parameters | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.user.advanced.security.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Parametros de seguridad

- **AD_WINDOW_ID:** `19C757BE115C46748013FE13E22AD48C`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `6253B189570D4D9B8DDB9BBB9AF970ED` | 0 |
| 20 | Inactivity Exceptions | `D66DFF4304C44A7AA8BE95C000926B6D` | 1 |

## Campos añadidos por el módulo (AD_FIELD)

### Inactivity Exceptions (ventana: Parametros de seguridad)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 30 | Active | `Isactive` | No | No | — |
| 50 | User/Contact | `AD_User_ID` | No | No | — |

### Header (ventana: Parametros de seguridad)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | Active | `Isactive` | No | No | — |
| 40 | Password Complexity | `Password_Complexity` | No | No | — |
| 50 | Password Length | `Password_Length` | No | No | — |
| 60 | Notification Email | `Notification_Email` | No | No | — |
| 70 | Inactivity Days | `Inactivity_Days` | No | No | F1A4FC62C476482CB83A3E8FABB7A11F |
| 80 | Attempts | `Attempts` | No | No | 132AE6BE7A0F46D2A9024CA4C5855224 |
| 90 | Validity | `Validity` | No | No | 13613DE7F0964CBBA2090CAD89B3914D |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un proceso en segundo plano para la inactivación de usuarios, el cual se ejecuta de manera automática con base en las configuraciones definidas. Los usuarios pueden activar este proceso mediante un botón en la interfaz, que inicia la evaluación de los usuarios inactivos según los días permitidos desde su última actividad. Las validaciones comunes incluyen asegurarse de que cada configuración de seguridad está única y que cumple con los requisitos establecidos para la longitud y complejidad de las contraseñas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.user.advanced.security.es_ES/referencedata/translation/`.

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
| Background | Proceso Background Inactivación de usuarios por log in | User Inactivation Background Process | UserInactivationBackgroundProcess | *(OBUIAPP / manual)* | — | — |
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
| `SSUAS_DifferentPassword` | The password has been used before | The password has been used before | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSUAS_Val_MinLength` | The maximum length of the field is 3 characters | The maximum length of the field is 3 characters | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSUAS_Only_One_Config` | There can only be one security configuration at a time. | There can only be one security configuration at a time. | Error | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSUAS_PasswordNotStrongEnough` | Passwords must have at least @lenght@ characters and contain at least three of the following: uppercase letters, lowercase letters, numbers and symbols. | Passwords must have at least @lenght@ characters and contain at least three of the following: uppercase letters, lowercase letters, numbers and symbols. | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
| `SSUAS_SamePasswordThanOld` | Please, enter a new one | Please, enter a new one | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El rol del Java en este módulo es fundamental, ya que se emplean varias clases para manejar la validación de configuraciones de seguridad y la inactivación de usuarios en segundo plano. Las clases Java se utilizan para interceptar eventos de creación y actualización, asegurando que las reglas de negocio se apliquen correctamente antes de persistir los cambios en la base de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.user.advanced.security`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `SSUAS_Config_Validation` | ad_event | EntityPersistenceEventObserver | — | `src/ec/com/sidesoft/user/advanced/security/ad_event/SSUAS_Config_Validation.java` |
| `UserInactivationBackgroundProcess` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/user/advanced/security/ad_process/UserInactivationBackgroundProcess.java` |
| `CustomPasswordStrengthChecker` | utility | PasswordStrengthChecker | — | `src/ec/com/sidesoft/user/advanced/security/utility/CustomPasswordStrengthChecker.java` |
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

Aunque el módulo no tiene triggers ni funciones PL específicas, se apoya en las clases Java para la validación y gestión de eventos relacionados con la seguridad. Esto permite que las operaciones críticas sobre las configuraciones y los usuarios sean registradas y gestionadas de manera efectiva mediante la lógica de negocio definida.

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

Módulo: `ec.com.sidesoft.user.advanced.security`.

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

# Glosario — prefijo `SSUAS`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSUAS` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.user.advanced.security` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `UserInactivationBackgroundProcess` — Proceso Background Inactivación de usuarios por log in

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Additional parameters for execution of background process
**Package:** `ec.com.sidesoft.backgroundprocess`

# Module overview — Additional parameters for execution of background process

## Functional

El módulo 'Additional parameters for execution of background process' está diseñado para mejorar la parametrización de procesos en segundo plano dentro de Openbravo ERP. Principalmente, su propósito es permitir una ejecución más eficiente de los procesos de costeo al incrementar el campo fecha de ejecución. Los usuarios de negocio, así como los desarrolladores y soporte técnico, son los actores principales que interactúan con este módulo. Su alcance se limita a la modificación de parámetros en procesos ya existentes, sin introducir nuevas ventanas ni informes. Este módulo no presenta dependencias externas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/backgroundprocess` |
| Web | `web/ec.com.sidesoft.backgroundprocess/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SBKP`

# Guía de chat — Additional parameters for execution of background process

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.backgroundprocess`).

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

- ¿Cómo incremento el campo fecha de ejecución en un proceso de costeo?
- ¿Dónde puedo encontrar información sobre los parámetros adicionales en procesos?
- ¿Existen validaciones antes de ejecutar un proceso en segundo plano?
- ¿Qué debo hacer si mi proceso no se ejecuta correctamente?
- ¿Hay algún informe disponible sobre los procesos en segundo plano?
- ¿Cómo se gestionan los errores que aparecen durante la ejecución?
- ¿Puedo modificar los parámetros de un proceso ya ejecutado?
- ¿Qué impacto tiene la falta de actualización en la fecha de ejecución?

# Domain — data model

## Functional

El modelo de datos se centra en la entidad cabecera 'AD_PROCESS_REQUEST', que almacena solicitudes de ejecución de procesos. En este módulo, se incorpora una función que permite incrementar la fecha de ejecución, optimizando así la gestión del costeo en el sistema. No se definen etapas adicionales, y las relaciones están restringidas a la entidad cabecera mencionada. Es importante resaltar que, aunque el módulo no incluye triggers, la función PL vinculada es clave para garantizar la correcta ejecución de las solicitudes en segundo plano.

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

`AD_PROCESS_REQUEST`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no cuenta con ventanas gráficas específicas dentro de la UI de Openbravo, lo que significa que su operación se realiza de manera más técnica, a través del uso de funciones proporcionadas dentro del backend del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.backgroundprocess.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.backgroundprocess.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `CD573DF1E351485EA2B2DE487DCACA6F`

- **AD_TAB_ID:** `CD573DF1E351485EA2B2DE487DCACA6F` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 68 | Date Prosses | `EM_Sbkp_Dateprosses` | No | No | — |
| 69 | Important Information | `EM_Sbkp_Important_Info` | No | Sí | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye un único proceso de ejecución en segundo plano, que se activa mediante un botón. Este proceso permite a los usuarios completar la ejecución de parámetros necesarios para las tareas de costeo. En este sentido, es fundamental que los usuarios validen frecuentemente los parámetros ingresados antes de ejecutar el proceso, dado que esto puede afectar significativamente los resultados obtenidos. No se generan informes en este módulo, por lo que la información se manejará a través del sistema de logs estándar.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.backgroundprocess.es_ES/referencedata/translation/`.

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
| Background (PL/pgSQL) | Depurando CxC y CxP en zero | Debbuging CxC and CxP to Zero | Debbuging CxC and CxP to Zero | `sbkp_payments` | ,case when psd.fin_payment_id then 'Y' else 'N' end as fpd_id; and inv.c_invoice_id = '1636007F662448EAA90BC790C249E2E2'; and inv.c_invoice_id = '37141D4DCCBC4F11BDEF121DA07AAEC3'; RAISE exception '%','Correction paymen… | — |
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

El módulo incluye una clase Java, 'Sbkp_UpdateImportantInformation', que se encarga de actualizar información importante relacionada con procesos mediante llamadas de retorno. Esta clase gestiona la lógica para obtener datos específicos relacionados con los procesos, lo que es fundamental para la interacción con el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.backgroundprocess`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Sbkp_UpdateImportantInformation` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/backgroundprocess/ad_callouts/Sbkp_UpdateImportantInformation.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Función PL `sbkp_payments` | — | invocación proceso | ,case when psd.fin_payment_id then 'Y' else 'N' end as fpd_id; and inv.c_invoice_id = '1636007F662448EAA90BC790C249E2E2'; and inv.c_invoice_id = '37141D4DCCBC4F11BDEF121DA07AAEC3' |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers no están presentes en este módulo, aunque la función PL es esencial para el soporte técnico, ya que ayuda a manejar las operaciones que modifican el campo fecha de ejecución. Esto asegura que las solicitudes se procesen correctamente y en el momento adecuado, contribuyendo a la integridad y la eficiencia del sistema.

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
| `sbkp_payments` | Depurando CxC y CxP en zero | ,case when psd.fin_payment_id then 'Y' else 'N' end as fpd_id; and inv.c_invoice_id = '1636007F662448EAA90BC790C249E2E2'; and inv.c_invoice_id = '37141D4DCCBC4F11BDEF121DA07AAEC3'; RAISE exception '%','Correction paymen… | ,case when psd.fin_payment_id then 'Y' else 'N' end as fpd_id; and inv.c_invoice_id = '1636007F662448EAA90BC790C249E2E2'; and inv.c_invoice_id = '37141D4DCCBC4F11BDEF121DA07AAEC3'; RAISE exception '%','Correction payments =' || v_SQL; | `model/functions/SBKP_PAYMENTS.xml` |
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

Módulo: `ec.com.sidesoft.backgroundprocess`.

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

# Glosario — prefijo `SBKP`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SBKP` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.backgroundprocess` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Debbuging CxC and CxP to Zero` — Depurando CxC y CxP en zero

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Send Email Alert
**Package:** `ec.com.sidesoft.email.alert`

# Module overview — Send Email Alert

## Functional

El módulo 'Send Email Alert' tiene como propósito facilitar la notificación por correo electrónico en el ERP Openbravo, alertando a los usuarios sobre eventos específicos o cambios en el sistema. Está dirigido principalmente a los usuarios de negocio que buscan automatizar la comunicación y a los desarrolladores que pueden adaptar o extender su funcionalidad. El alcance del módulo se limita a la integración del envío de correos electrónicos, dependiendo de otras configuraciones del sistema y de la disponibilidad de las reglas de alerta definidas en la tabla modificada 'AD_ALERTRULE'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/email/alert` |
| Web | `web/ec.com.sidesoft.email.alert/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SDEA`

# Guía de chat — Send Email Alert

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.email.alert`).

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

- ¿Cómo puedo configurar una regla de alerta para ser notificado por correo?
- ¿Qué eventos pueden activar el envío de una alerta por correo?
- ¿Cómo puedo ver las reglas de alerta que he creado?
- ¿Puedo editar las reglas de alerta después de haberlas creado?
- ¿Qué debo hacer si no recibo la alerta por correo electrónico?
- ¿Hay un límite en la cantidad de correos que puedo enviar a través de las alertas?
- ¿Puedo personalizar el contenido del correo de alerta?
- ¿Cómo puedo eliminar una regla de alerta existente?

# Domain — data model

## Functional

La entidad central del módulo es la tabla 'AD_ALERTRULE', donde se definen las reglas de alerta que desencadenan el envío de correos. No hay etapas adicionales ni tablas relacionadas en el módulo, lo que simplifica su estructura. Las relaciones dentro del sistema se establecen a través de las reglas definidas, aunque no se implementaron triggers clave ni funciones en PL dentro de este módulo, ya que su función principal es la notificación.

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

`AD_ALERTRULE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no cuenta con ventanas o menús específicos en la interfaz de usuario, lo que implica que su funcionalidad está más integrada en el contexto del sistema general. Los usuarios deben interactuar con el módulo a través de las configuraciones de la tabla 'AD_ALERTRULE', donde se gestionan las reglas de alerta.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.email.alert.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.email.alert.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `800265`

- **AD_TAB_ID:** `800265` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 80 | EM_Sdea_Isemail | `EM_Sdea_Isemail` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo no presenta botones ni procesos específicos como completar, retornar o rechazar. Sin embargo, es fundamental que los usuarios comprendan cómo definir y configurar adecuadamente las reglas de alerta para que el envío de correos sea efectivo. Las validaciones frecuentes se centran en asegurarse de que las reglas definidas estén correctamente establecidas en la base de datos para activar las alertas deseadas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.email.alert.es_ES/referencedata/translation/`.

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

Este módulo no incluye clases Java, ya que su funcionalidad está completamente centrada en la configuración de reglas de alerta sin necesidad de procesamiento adicional.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.email.alert`.

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

A pesar de que no hay triggers ni funciones PL específicas dentro del módulo, el impacto en la base de datos se centra en la modificación de la tabla 'AD_ALERTRULE'. Esta modificación es clave para el funcionamiento del módulo, ya que permite que las alertas se envíen correctamente según las configuraciones definidas por los usuarios.

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

Módulo: `ec.com.sidesoft.email.alert`.

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

# Glosario — prefijo `SDEA`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SDEA` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.email.alert` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Bulk Data Upload
**Package:** `ec.com.sidesoft.bulk.data.upload`

# Module overview — Sidesoft Bulk Data Upload

## Functional

El módulo Sidesoft Bulk Data Upload está diseñado para permitir la carga masiva de datos relacionados con cantidades y líneas de pedidos de venta dentro del ERP Openbravo. Este módulo es utilizado principalmente por usuarios de negocio que necesitan importar grandes volúmenes de datos de manera eficiente, así como por el equipo de soporte L2 para resolver problemas relacionados con la carga de datos. El alcance del módulo incluye la integración con versiones de Openbravo desde la 2.50 hasta la 3.00, y es dependiente de módulos como 'Core' y '2.50 to 3.00 Compatibility Skin'.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/bulk/data/upload` |
| Web | `web/ec.com.sidesoft.bulk.data.upload/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSBDUPL`

# Guía de chat — Sidesoft Bulk Data Upload

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.bulk.data.upload`).

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

- ¿Cómo puedo cargar datos masivos de pedidos de venta?
- ¿Qué tipo de información debo incluir en el archivo de carga?
- ¿Qué sucede si un pedido tiene errores en los datos importados?
- ¿Cómo puedo validar que los datos se han cargado correctamente?
- ¿Es necesario seguir un formato específico para el archivo de carga?
- ¿Cómo se maneja la cantidad de productos en el pedido?
- ¿Qué pasa si el producto que intento importar no existe en el sistema?
- ¿Dónde puedo encontrar más información sobre el módulo Sidesoft Bulk Data Upload?

# Domain — data model

## Functional

El modelo de datos del módulo gira en torno a la entidad 'Simple Products', que sirve como cabecera para las líneas de producto relacionadas con pedidos de venta. Aunque no se especifican tablas físicas ni relaciones explícitas, el módulo gestiona un flujo de carga en el que se espera que cada línea del pedido contenga información sobre el producto, cantidad, precio, impuesto y unidad de medida, entre otros. Este proceso podría involucrar validaciones adicionales y tratamiento de errores, aunque no se detallan triggers específicos en el inventario.

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

El módulo no presenta ventanas definidas en la interfaz de usuario debido a su naturaleza centrada en la carga de datos. Los usuarios interactúan principalmente a través de un proceso de importación, utilizando herramientas o scripts para cargar los datos en la base de datos sin una interfaz gráfica activa para esta acción.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.bulk.data.upload.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.bulk.data.upload.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Las operaciones de carga masiva se ejecutan mediante un proceso que involucra la validación de los datos antes de ser importados al sistema. Los botones típicos como 'Completar', 'Retornar' y 'Rechazar' no están claramente definidos en el inventario del módulo; sin embargo, se entiende que hay un proceso de validación en el back-end que asegura la integridad de los datos. Adicionalmente, no se listan informes específicos, sugiriendo que se enfoca en la funcionalidad de carga en lugar de la presentación de resultados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.bulk.data.upload.es_ES/referencedata/translation/`.

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

El módulo incluye una clase Java denominada 'ImportLinesOrders', que es responsable de manejar la lógica de procesamiento de las líneas de pedidos. Esta clase permite la definición de parámetros que se utilizarán durante la importación y valida los datos antes de su inserción en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.bulk.data.upload`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `ImportLinesOrders` | ad_process | IdlServiceJava | Proceso / informe Java | `src/ec/com/sidesoft/bulk/data/upload/ad_process/ImportLinesOrders.java` |
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

En la base de datos, aunque no se especifican triggers ni funciones PL, se asume que podrían existir mecanismos para manejar la inserción y validación de datos importados. Esta funcionalidad es clave para garantizar que los datos cargados cumplan con las reglas del negocio y estén consistentes con el resto del sistema.

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

Módulo: `ec.com.sidesoft.bulk.data.upload`.

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

# Glosario — prefijo `SSBDUPL`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSBDUPL` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.bulk.data.upload` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Widgets
**Package:** `ec.com.sidesoft.widgets`

# Module overview — Sidesoft Widgets

## Functional

El módulo Sidesoft Widgets está diseñado para ampliar las funcionalidades del ERP Openbravo, proporcionando widgets personalizables que mejoran la experiencia del usuario. Está dirigido principalmente a usuarios de negocio que buscan optimizar sus operaciones y a desarrolladores que requieren integrar o modificar estos widgets. El alcance de este módulo incluye la adaptación de widgets a las necesidades específicas del negocio, permitiendo una mayor interacción con otros módulos de Openbravo. Las dependencias con otros módulos como '2.50 to 3.00 Compatibility Skin' y 'Core' son clave para su funcionamiento adecuado.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/widgets` |
| Web | `web/ec.com.sidesoft.widgets/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**1.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSWGT`

# Guía de chat — Sidesoft Widgets

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.widgets`).

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

- ¿Cómo puedo personalizar un widget en mi vista actual?
- ¿Qué widgets están actualmente disponibles para integrar?
- ¿Cómo se asegura que los widgets sean compatibles con otras funcionalidades del ERP?
- ¿Qué tipo de información se puede visualizar a través de los widgets?
- ¿Se pueden crear nuevos widgets desde cero?
- ¿Cómo puedo reportar un error relacionado con un widget específico?
- ¿Existen limitaciones en el número de widgets que puedo usar?
- ¿Dónde puedo encontrar más documentación sobre la integración de widgets?

# Domain — data model

## Functional

Aunque el módulo no incluye tablas físicas, se apoya en la arquitectura existente de Openbravo para gestionar los datos asociados a los widgets. Las relaciones entre los usuarios y los widgets son fundamentales, permitiendo la personalización y configuración de cada widget según preferencias individuales. En este módulo no se han implementado triggers o funciones PL específicas, lo que indica una orientación principalmente hacia la interfaz de usuario y la plugabilidad de los elementos visuales.

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

El módulo Sidesoft Widgets no incluye ventanas definidas en la interfaz de usuario, lo que sugiere que la navegación se basa en la integración de widgets en pantallas existentes de Openbravo. Los usuarios pueden desplegar estos widgets en sus entornos personalizados usando la configuración provista en otros módulos del sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.widgets.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Widgets | Widgets | Sí |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.widgets.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
El módulo **no define** `AD_WINDOW.xml` ni `AD_FIELD.xml` en sourcedata. Si solo extiende ventanas de otros módulos vía plantilla, documente aquí las pestañas afectadas manualmente.
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo no contiene botones de procesos típicos como completar, retornar o rechazar, lo que refuerza su naturaleza como herramienta de soporte visual más que de procesamiento transaccional. Los usuarios deben consultar informes y validaciones disponibles en otros módulos relacionados, donde se integran los datos generados por los widgets en este módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.widgets.es_ES/referencedata/translation/`.

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

No se han definido clases Java para este módulo, lo que implica que la funcionalidad se sostiene principalmente en la configuración del sistema Openbravo sin extenso desarrollo en el backend.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.widgets`.

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

Dado que el módulo no cuenta con triggers ni funciones PL, su rol en la base de datos se limita a aprovechar las funcionalidades básicas de Openbravo sin intervención adicional en la lógica del servidor. Esto permite un entorno más ligero y ágil, ideal para la integración de elementos front-end.

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

Módulo: `ec.com.sidesoft.widgets`.

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

# Glosario — prefijo `SSWGT`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSWGT` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.widgets` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Organization Information
**Package:** `ec.com.sidesoft.orginfo`

# Module overview — Sidesoft Organization Information

## Functional

El módulo Sidesoft Organization Information tiene como propósito gestionar la información organizativa dentro del ERP Openbravo. Está diseñado para ser utilizado por usuarios de negocio y personal de soporte técnico, facilitando la administración de datos clave de las organizaciones. Su alcance abarca la visualización y modificación de la información organizativa, contribuyendo así a una mejor toma de decisiones en la gestión empresarial. Este módulo está diseñado para ser compatible con el skin de versiones desde 2.50 a 3.00, y no presenta dependencias complicadas con otros módulos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/orginfo` |
| Web | `web/ec.com.sidesoft.orginfo/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SORGI`

# Guía de chat — Sidesoft Organization Information

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.orginfo`).

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

- ¿Cómo puedo ver la información organizativa?
- ¿Qué datos puedo modificar en la tabla AD_ORGINFO?
- ¿Existen restricciones al editar la información organizativa?
- ¿Cómo se guarda la información después de realizar cambios?
- ¿Qué debo hacer si no puedo acceder a la información organizativa?
- ¿Existen informes relacionados con la organización?
- ¿Puedo importar datos a la tabla AD_ORGINFO?
- ¿Cómo se manejan los errores durante la modificación de los datos?

# Domain — data model

## Functional

La entidad principal de este módulo es la tabla AD_ORGINFO, que centraliza la información organizativa. Al no haber etapas o relaciones definidas en el inventario, su uso se limita a la manipulación directa de datos en esta tabla, sin flujos complejos. La ausencia de triggers y funciones PL indica una implementación sencilla, enfocada en la modificación de la información más que en procesos automatizados.

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

`AD_ORGINFO`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo carece de ventanas específicas definidas en la interfaz de usuario, lo que sugiere que el acceso a sus funcionalidades se realiza de manera directa a través de las tablas involucradas. Esto puede implicar que los usuarios interactúan con la información organizativa mediante consultas o a través de procesos específicos de backend.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.orginfo.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.orginfo.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `170`

- **AD_TAB_ID:** `170` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 150 | Country | `EM_Sorgi_Country_ID` | No | No | — |
| 160 | Region | `EM_Sorgi_Region_ID` | No | No | — |
| 170 | Cantón | `EM_Sorgi_Canton_ID` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

No se han definido procesos ni botones específicos en el inventario. Esto significa que la interacción con el módulo puede ser directa, consistiendo en la inserción, actualización y consulta de datos en la tabla AD_ORGINFO. Dado que no se han identificado informes o validaciones frecuentes, la función del módulo se enfoca en la simple administración de datos.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.orginfo.es_ES/referencedata/translation/`.

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

Este módulo no presenta clases Java asociadas, lo que indica que su funcionalidad se basa principalmente en configuraciones de la base de datos y directivas del ERP sin intervención de código Java específico.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.orginfo`.

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
| AD_VAL_RULE | — | `SORGI_ValidateRegion` | `c_region.c_region_id in ( 
select c_region_id 
from  c_region  
where c_country_id = @em_sorgi_country_id@ )` |
| AD_VAL_RULE | — | `SORGI_ValidateCanton` | `secpm_canton.secpm_canton_id in ( 
select secpm_canton_id 
from  secpm_canton  
where c_region_id = @em_sorgi_region_id@` |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El módulo no cuenta con triggers ni funciones PL, lo que sugiere una estructura sencilla en la base de datos. Esto puede facilitar el soporte y mantenimiento, dado que no hay lógica compleja que gestionar o monitorizar.

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

Módulo: `ec.com.sidesoft.orginfo`.

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

# Glosario — prefijo `SORGI`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SORGI` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.orginfo` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Unnoparts Extended Config
**Package:** `ec.com.sidesoft.unnoparts.extended.config`

# Module overview — Unnoparts Extended Config

## Functional

El módulo 'Unnoparts Extended Config' está diseñado para extender la configuración de Unnoparts en el entorno de Openbravo, permitiendo una mayor personalización y adaptación a las necesidades específicas de los usuarios de negocio. Actores clave incluyen administradores de sistemas, ingenieros de soporte y desarrolladores enfocados en la implementación y mantenimiento del ERP. El alcance abarca la configuración de parámetros específicos y su integración con otras funciones del sistema. Este módulo depende de varias bibliotecas y componentes del núcleo de Openbravo, asegurando su compatible operatividad dentro del ecosistema del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/unnoparts/extended/config` |
| Web | `web/ec.com.sidesoft.unnoparts.extended.config/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework
- Standar Validations

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSUEC`

# Guía de chat — Unnoparts Extended Config

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.unnoparts.extended.config`).

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
- «¿Qué es la tabla ssuec_actions?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo extender la configuración de Unnoparts?
- ¿Qué funciones PL se incluyen en este módulo?
- ¿Cómo interactúo con la tabla ssuec_actions?
- ¿Este módulo requiere de alguna configuración adicional?
- ¿Hay alguna guía sobre las dependencias de este módulo?
- ¿Cómo puedo verificar la correcta implementación de configuraciones?
- ¿Qué tipo de soporte técnico está disponible para este módulo?
- ¿Puedo personalizar más allá de lo que ofrece este módulo?

# Domain — data model

## Functional

El modelo de datos del módulo se centra en la tabla 'ssuec_actions', que actúa como la entidad cabecera para gestionar las configuraciones extendidas de Unnoparts. Este módulo no incluye etapas adicionales ni relaciones complejas, dado que se limita a dos tablas físicas y a una función PL que soporta las operaciones necesarias para la configuración. Aunque no hay triggers implementados, el correcto diseño de la tabla garantiza la integridad de los datos a nivel funcional.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `ssuec_actions` |
| `ssuec_userconfigext` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `ssuec_actions` | ssuec_actions | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ssuec_userconfigext_id→ssuec_userconfigext; ad_ref_list_id→ad_ref_list | Detalle enlazado a ad_client, ad_org, ssuec_userconfigext. | PK `ssuec_actions_key`; Cols: ssuec_userconfigext_id, ad_ref_list_id, description; `SSUEC_ACTIONS_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `ssuec_userconfigext` | ssuec_userconfigext | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_process_id→ad_process; ad_user_id→ad_user | Parametrización / catálogo de soporte. | PK `ssuec_userconfigext_key`; Cols: ad_process_id, ad_user_id, description; `SSUEC_USERCONFIGEXT_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `ssuec_actions` |
| `ssuec_userconfigext` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no presenta ventanas específicas en la interfaz de usuario de Openbravo, lo que sugiere que su configuración se realiza a través de la funcionalidad del backend y probablemente mediante scripts o API. Los usuarios deberán tener conocimientos técnicos para interactuar con los elementos de esta extensión.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.unnoparts.extended.config.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.unnoparts.extended.config.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### ConfigUserextended

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Process | `AD_Process_ID` | No | No | — |
| 30 | Description | `Description` | No | No | — |
| 40 | Active | `Isactive` | No | No | — |

### Actions

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 30 | List Reference | `AD_Ref_List_ID` | No | No | — |
| 40 | Description | `Description` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Dado que no se encuentran botones de proceso en este módulo, se considera que las interacciones se realizan a través de funciones específicas vinculadas a la configuración en el backend. La única función PL presente permite a los administradores manejar configuraciones esenciales, mientras que los informes y validaciones se basan en las funcionalidades estándar del sistema sin personalizaciones adicionales en este módulo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.unnoparts.extended.config.es_ES/referencedata/translation/`.

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

No existen implementaciones de clases Java asociadas a este módulo, reafirmando su enfoque en configuraciones directas a través de la base de datos y el uso de funciones específicas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.unnoparts.extended.config`.

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
| AD_VAL_RULE | — | `Ssuec_RefValidation` | `AD_Ref_List.value in (select value from ad_ref_list where ad_reference_id in
(
select max(ad_reference_value_id) from ad` |
| Función PL `ssuec_uservalidation_ep` | — | invocación proceso | Usuario no autorizado para reactivar documentos, revise configuracion extendida de Usuario; RAISE_APPLICATION_ERROR(-20000, p_user || ' - '|| p_record_id); |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers no están presentes en este módulo, lo que simplifica la gestión de datos. Sin embargo, la función PL vinculada proporciona un mecanismo para ejecutar las tareas necesarias que apoyan las operaciones del módulo, asegurando que las configuraciones reflejen correctamente en el sistema database.

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
| `ssuec_uservalidation_ep` | — | Usuario no autorizado para reactivar documentos, revise configuracion extendida de Usuario; RAISE_APPLICATION_ERROR(-20000, p_user || ' - '|| p_record_id); | Usuario no autorizado para reactivar documentos, revise configuracion extendida de Usuario; RAISE_APPLICATION_ERROR(-20000, p_user || ' - '|| p_record_id); | `model/functions/SSUEC_USERVALIDATION_EP.xml` |
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

Módulo: `ec.com.sidesoft.unnoparts.extended.config`.

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

# Glosario — prefijo `SSUEC`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSUEC` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.unnoparts.extended.config` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Estandar Performance
**Package:** `ec.com.sidesoft.estandar.performance`

# Module overview — Estandar Performance

## Functional

El módulo 'Estandar Performance' tiene como propósito principal mejorar y estandarizar el rendimiento del ERP Openbravo para los usuarios de negocio y desarrolladores. Está diseñado para ser utilizado por todos los actores involucrados en la gestión empresarial, incluyendo gerentes de área y personal de IT. Este módulo se integra con la versión Openbravo 3.0 y es compatible con la skin de compatibilidad 2.50 a 3.00. Sus dependencias incluyen componentes clave del núcleo de Openbravo, asegurando su funcionalidad.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/estandar/performance` |
| Web | `web/ec.com.sidesoft.estandar.performance/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**1.0.0** (from `AD_MODULE.xml`).

### DB prefix

`EPERF`

# Guía de chat — Estandar Performance

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.estandar.performance`).

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

- ¿Cómo puedo mejorar el rendimiento de mis informes?
- ¿Qué tablas se han modificado en este módulo?
- ¿Cómo afecta el módulo a mis datos de facturación?
- ¿Qué debo hacer si encuentro errores durante la ejecución?
- ¿Cómo puedo acceder a las nuevas funcionalidades del módulo?
- ¿Este módulo afecta a otros módulos que estoy usando?
- ¿Qué debo considerar al implementar cambios en AD_SESSION?
- ¿Hay alguna limitación en la integración con aplicaciones externas?

# Domain — data model

## Functional

El módulo no define explícitamente tablas físicas individuales, pero modifica y utiliza las tablas existentes como AD_SESSION, C_INVOICE y FACT_ACCT para mejorar la captura y análisis de datos relacionados con el rendimiento. Es crucial entender que este módulo no tiene etapas explícitas al no contar con un esquema de tablas personalizadas, pero su integración con las tablas modificadas permite una mayor eficacia en la gestión de transacciones y el análisis de la contabilidad. No se han implementado triggers específicos en la base de datos para este módulo, lo que indica que su funcionalidad se alinea más con la utilización de los datos existentes.

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

`AD_SESSION`, `C_INVOICE`, `FACT_ACCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El modo de navegación por el módulo 'Estandar Performance' no presenta ventanas ni elementos UI específicos, lo que sugiere que las funcionalidades deben ser accedidas a través del uso de tablas y modificaciones en las existentes. La interacción del usuario será menos directa en términos de navegación visual, enfocándose más en la implementación de procesos que en las ventanas clásicas de un ERP.

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

Dado que el módulo carece de procesos definidos con botones o informes, las interacciones estarán limitadas a la manipulación de datos de las tablas afectadas. Los usuarios deberán centrar su atención en las transacciones normales y la gestión de información a través de las tablas que se han modificado. Las validaciones y reportes más frecuentes dependerán de las configuraciones existentes en las tablas que están siendo usadas, como AD_SESSION y C_INVOICE.

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

No se han definido clases Java específicas para este módulo, lo que indica que la funcionalidad se centra en la configuración y manipulación de la base de datos existente más que en el desarrollo de nuevas características a través de programación en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.estandar.performance`.

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

Este módulo no incluye triggers ni funciones PL específicos, por lo que su rol en el soporte técnico se basa principalmente en la modificación y mejora de las tablas existentes. Las actualizaciones en AD_SESSION, C_INVOICE y FACT_ACCT permiten una adaptación más eficiente de los procesos del ERP, pero el soporte técnico deberá estar preparado para gestionar implicaciones derivadas de este tipo de modificaciones.

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

Módulo: `ec.com.sidesoft.estandar.performance`.

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

# Glosario — prefijo `EPERF`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `EPERF` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.estandar.performance` | Carpeta del módulo en el repositorio |

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

---
## Sidesoft Database Index Optmizations
**Package:** `ec.com.sidesoft.index.optmizations`

# Module overview — Sidesoft Database Index Optmizations

## Functional

El módulo 'Sidesoft Database Index Optimizations' tiene como propósito optimizar el rendimiento de la base de datos de Openbravo mediante la creación de índices en diversas tablas clave. Los actores principales incluyen administradores de bases de datos, arquitectos de sistemas y desarrolladores de Openbravo que buscan mejorar la eficiencia en las consultas. Este módulo es especialmente relevante para instalaciones que manejan grandes volúmenes de transacciones y datos en las tablas especificadas. Las dependencias del módulo incluyen la '2.50 to 3.00 Compatibility Skin' y el componente 'Core' del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/index/optmizations` |
| Web | `web/ec.com.sidesoft.index.optmizations/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core

### Version

**1.0.0** (from `AD_MODULE.xml`).

### DB prefix

`DBIDXO`

# Guía de chat — Sidesoft Database Index Optmizations

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.index.optmizations`).

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

- ¿Cómo puedo verificar si los índices han sido creados correctamente?
- ¿Qué tablas se benefician de las optimizaciones en este módulo?
- ¿Cómo afectará este módulo el rendimiento de mis consultas en Openbravo?
- ¿Existen pasos adicionales para implementar este módulo?
- ¿Cómo puedo deshacer los cambios realizados por este módulo?
- ¿Puedo combinar este módulo con otros módulos de optimización?
- ¿Qué versiones de Openbravo son compatibles con este módulo?
- ¿Debo realizar respaldos antes de implementar este módulo?

# Domain — data model

## Functional

Las entidades cabecera del módulo se centran en las tablas de transacciones y catalogación que se han optimizado mediante la creación de índices. Estas incluyen C_Order, C_OrderLine, M_Inout, entre otras, las cuales son fundamentales para la gestión de pedidos y entradas de mercancías. Aunque no se definen etapas específicas en este módulo, el flujo de trabajo puede implicar desde la creación de pedidos hasta su facturación y entrega. Los índices creados tienen como objetivo mejorar las relaciones entre estas entidades al facilitar el acceso rápido a la información y reducir los tiempos de respuesta en las consultas.

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

`C_BPARTNER`, `C_ELEMENTVALUE`, `C_ORDER`, `C_ORDERLINE`, `C_PROJECT`, `FACT_ACCT`, `M_INOUT`, `M_INOUTLINE`, `M_MATCHINV`, `M_MATCHPO`, `M_PRICELIST`, `M_PRODUCT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

No se define una interfaz gráfica de usuario mediante ventanas en este módulo, ya que su enfoque está en las optimizaciones a nivel de base de datos. Las operaciones relacionadas con el módulo se realizan a través de scripts SQL y configuraciones del sistema en el backend.

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

Este módulo no incluye procesos específicos con botones de acción, informes o validaciones, ya que su función se centra en las mejoras de rendimiento en la base de datos. Aún así, es recomendable que los usuarios estén familiarizados con su entorno de Openbravo para monitorear el desempeño y realizar ajustes según las necesidades operativas.

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

No se han implementado clases Java específicas dentro de este módulo, ya que su objetivo principal reside en la optimización a nivel de base de datos sin modificaciones en la lógica programática.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.index.optmizations`.

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

El rol de los índices en este módulo es fundamental para garantizar un acceso más rápido a las tablas modificadas, como C_Order, M_Inout y M_Product, entre otras. Aunque no hay triggers ni funciones PL definidas en el módulo, la implementación de los índices permite efectuar consultas más eficientes y optimizar la carga de datos en el sistema.

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

Módulo: `ec.com.sidesoft.index.optmizations`.

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

# Glosario — prefijo `DBIDXO`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `DBIDXO` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.index.optmizations` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Standar Validations
**Package:** `ec.com.sidesoft.standar.validations`

# Module overview — Standar Validations

## Functional

El módulo 'Standar Validations' está diseñado para ofrecer una alternativa eficaz al desarrollo manual de triggers en Openbravo. Su propósito es facilitar la gestión de validaciones mediante una interfaz que permite a los usuarios definir y aplicar reglas de validación de forma sencilla. Está dirigido principalmente a usuarios de negocio, desarrolladores y al soporte técnico de nivel 2, quienes podrán utilizar y configurar el módulo sin la necesidad de escribir código adicional. El alcance del módulo incluye la aplicación de validaciones estándar que se pueden integrar con otros módulos del sistema ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/standar/validations` |
| Web | `web/ec.com.sidesoft.standar.validations/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SSSV`

# Guía de chat — Standar Validations

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.standar.validations`).

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
- «¿Qué es la tabla sssv_standarvalidations?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo agregar una nueva validación estándar?
- ¿Dónde encuentro las configuraciones de validación en Openbravo?
- ¿Qué pasos debo seguir para aplicar una validación a un proceso existente?
- ¿Puedo ver ejemplos de validaciones ya configuradas?
- ¿Qué tipo de errores puedo prevenir con las validaciones estándar?
- ¿Cómo se integra el módulo con otros procesos del ERP?
- ¿Es posible desactivar una validación temporalmente?
- ¿Cuál es el procedimiento para modificar una validación existente?

# Domain — data model

## Functional

La entidad principal del módulo es 'sssv_standarvalidations', que actúa como la tabla cabecera donde se almacenan las definiciones de las validaciones. Aunque el módulo no contiene etapas explícitas ni triggers asociados, su diseño permite prever la implementación de validaciones que pueden ser enlazadas a procesos futuros o existentes. Las relaciones entre esta tabla y otros módulos pueden configurarse dependiendo de los requerimientos específicos del negocio, garantizando así una flexibilidad adecuada para diferentes entornos de operación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sssv_standarvalidations` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sssv_standarvalidations` | SSSV_StandarValidations | — | — | ad_client_id→ad_client; ad_org_id→ad_org; ad_tab_id→ad_tab | Detalle enlazado a ad_client, ad_org, ad_tab. | PK `sssv_sv_key`; Cols: sssv_trgname, ad_tab_id, sssv_description; `SSSV_SV_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `SSSV_StandarValidations` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

*(ninguna)*

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo 'Standar Validations' no presenta ventanas específicas en la interfaz de usuario, lo que sugiere que su funcionalidad se integra de manera no visible o a través de configuraciones administrativas. Los usuarios podrían navegar a través de las herramientas de configuración del ERP para acceder a las validaciones de manera indirecta, utilizando los procesos o scripts disponibles en el sistema.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.standar.validations.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.standar.validations.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Validations

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Sssv_Trgname | `Sssv_Trgname` | No | No | — |
| 40 | Tab | `AD_Tab_ID` | No | No | — |
| 50 | Sssv_Description | `Sssv_Description` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo no incluye botones específicos para procesos ni informes asociados. Sin embargo, se prevé que al implementar validaciones estándar se puedan habilitar validaciones automáticas en otros procesos del sistema. Los usuarios deben estar atentos a la correcta configuración de las validaciones para garantizar su eficacia. Las validaciones frecuentes pueden incluir reglas para la entrada de datos o la verificación de datos en bases existentes, asegurando que cualquier recordatorio o alerta se maneje adecuadamente a través del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.standar.validations.es_ES/referencedata/translation/`.

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

Este módulo no incluye clases Java, por lo que no se han definido funcionalidades que requieran soporte a nivel de código en Java.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.standar.validations`.

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

Aunque el módulo 'Standar Validations' no contiene triggers ni funciones PL, su implementación podría eventualmente requerir la creación de estas herramientas en función de las validaciones necesarias. Compatibilidad con la arquitectura del sistema asegura que, al manejar futuras ampliaciones, la base de datos pueda adaptarse a las necesidades del negocio sin interrumpir su funcionamiento.

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

Módulo: `ec.com.sidesoft.standar.validations`.

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

# Glosario — prefijo `SSSV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SSSV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.standar.validations` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft localization special customization
**Package:** `ec.com.sidesoft.localization.special.customization`

# Module overview — Sidesoft localization special customization

## Functional

El módulo de 'Sidesoft localization special customization' está diseñado para adaptar y mejorar las funcionalidades específicas del ERP Openbravo, satisfaciendo requerimientos locales y particularidades normativas. Está destinado a usuarios de negocio, así como a equipos de soporte que necesiten entender su operatividad y personalización. Este módulo no tiene dependencias externas y se integra de manera fluida dentro del ecosistema de Openbravo, siendo crucial para la implementación específica en ciertos territorios.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/special/customization` |
| Web | `web/ec.com.sidesoft.localization.special.customization/` |

### Declared dependencies

- *(ninguna en AD_MODULE_DEPENDENCY.xml)*

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SLOSPCU`

# Guía de chat — Sidesoft localization special customization

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.special.customization`).

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

- ¿Cómo puedo acceder a las personalizaciones locales en mi ERP?
- ¿Qué cambios se aplicaron en la tabla de usuarios?
- ¿Existen validaciones específicas para las facturas en este módulo?
- ¿Cómo puedo asegurarme de que los pagos cumplen con las normativas locales?
- ¿Dónde encuentro documentación sobre el módulo de personalización?
- ¿Qué debo hacer si encuentro un error en los procesos del módulo?
- ¿Este módulo afecta la creación de nuevos usuarios?
- ¿Cómo puedo personalizar aún más mi instalación de Openbravo?

# Domain — data model

## Functional

El módulo implementa personalizaciones sobre las tablas claves del sistema, incluyendo AD_USER, C_INVOICE y FIN_PAYMENT. Las relaciones establecidas se centran en la gestión de usuarios, facturas y pagos, permitiendo un flujo de información consistente y acorde a las regulaciones locales. A pesar de que no hay triggers definidos, se dispone de una función PL vinculada que soporta la lógica de negocio y permite realizar ajustes específicos cuando sea necesario.

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

`AD_USER`, `C_INVOICE`, `FIN_PAYMENT`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no presenta ventanas específicas, lo que indica que las personalizaciones se han realizado a nivel de backend y se integran en las funcionalidades existentes del ERP. Los usuarios navegarán por las interfaces administrativas estándar de Openbravo, donde se verán reflejadas las modificaciones realizadas por este módulo en sus procesos de trabajo diarios.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.special.customization.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.special.customization.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `118`

- **AD_TAB_ID:** `118` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 540 | Unlock posted | `EM_Slospcu_Unlock_Posted` | No | No | 099AD41D487E433D91F56D4D1FBA6088 |

### Pestaña `263`

- **AD_TAB_ID:** `263` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 15 | Unlock posted | `EM_Slospcu_Unlock_Posted` | No | No | — |

### Pestaña `290`

- **AD_TAB_ID:** `290` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 15 | Unlock posted | `EM_Slospcu_Unlock_Posted` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Este módulo ofrece un proceso que incluye un botón típico, aunque sin informes específicos asociados. Las validaciones comunes pueden incluir verificaciones en los campos de usuario, facturación y pagos, asegurando que las entradas de datos cumplan con las normativas locales. Los usuarios pueden esperar un manejo típico de acciones como completar, retornar o rechazar procesos según su configuración específica dentro del entorno Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.special.customization.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Desbloquear contabilidad | Unlock account | slospcu_unlock_acct | `slospcu_unlock_acct` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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
| Botón (PL/pgSQL) | Desbloquear contabilidad | Unlock account | slospcu_unlock_acct | `slospcu_unlock_acct` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (PL/pgSQL) | Desbloquear contabilidad | Unlock account | PL `slospcu_unlock_acct` | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — |
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

No se han implementado clases Java dentro de este módulo, lo que indica que todas las funcionalidades se manejan a través de personalizaciones en el backend y ajustes de configuraciones en Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.special.customization`.

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

La función PL presente en el módulo desempeña un rol fundamental para el soporte, permitiendo efectuar operaciones que no se manejan directamente a través de la interfaz de usuario. Aunque no hay triggers activados, la lógica implementada en esta función puede ser invocada para manejar eventos a nivel de base de datos que son críticos para mantener la coherencia de la información según los requerimientos locales.

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
| `slospcu_unlock_acct` | Desbloquear contabilidad | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SLOSPCU_UNLOCK_ACCT.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Desbloquear contabilidad | `slospcu_unlock_acct` | Botón (PL/pgSQL) | PL `slospcu_unlock_acct` | N | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |

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

Módulo: `ec.com.sidesoft.localization.special.customization`.

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

# Glosario — prefijo `SLOSPCU`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SLOSPCU` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.special.customization` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `slospcu_unlock_acct` — Desbloquear contabilidad

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Import data vaucher Module
**Package:** `ec.com.sidesoft.localization.importdata.loadvouchers`

# Module overview — Import data vaucher Module

## Functional

El módulo 'Import data voucher' permite la importación de datos XML provenientes del SRI (Servicio de Rentas Internas) en el sistema Openbravo ERP. Este proceso es fundamental para las empresas que requieren una integración eficiente de datos electrónicos, específicamente para la creación automática de facturas y la homologación de productos. Los actores principales incluyen usuarios de negocio que gestionan la contabilidad, personal de soporte de nivel 2 que maneja el sistema, y desarrolladores que mantienen y personalizan la solución según las necesidades del negocio.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/localization/importdata/loadvouchers` |
| Web | `web/ec.com.sidesoft.localization.importdata.loadvouchers/` |

### Declared dependencies

- Automatic load purchase data
- Core
- Openbravo 3.0 Framework

### Version

**1.0.0** (from `AD_MODULE.xml`).

### DB prefix

`IMDLV`

# Guía de chat — Import data vaucher Module

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.localization.importdata.loadvouchers`).

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
- «¿Qué es la tabla imdlv_lines?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo cargar los comprobantes XML en el sistema?
- ¿Qué debo hacer si ocurre un error durante la importación de datos?
- ¿Cómo se crean automáticamente las facturas a partir de los comprobantes importados?
- ¿Qué datos son requeridos para la homologación de productos?
- ¿Cómo puedo validar los datos por defecto antes de la importación?
- ¿Qué sucede si un tercero no está homologado correctamente?
- ¿Puedo editar los datos de los comprobantes después de la importación?
- ¿Dónde puedo encontrar información sobre los errores de carga?

# Domain — data model

## Functional

La entidad cabecera principal del módulo es la tabla 'imdlv_lines', que representa las líneas de los comprobantes importados. Este módulo abarca varias etapas relacionadas con la carga de datos XML, creación de facturas y gestión de terceros. Las relaciones entre las tablas son clave, especialmente entre 'imdlv_lines' y las tablas que almacenan las facturas y los comprobantes de compra. Los triggers, como 'IMDLV_HEADER2_TRG' y 'IMDLV_LINES_TRG', permiten realizar actualizaciones automáticas y asegurar la integridad de los datos durante el proceso de importación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `imdlv_homologation_product` |
| `imdlv_lines` |
| `imdlv_partner` |
| `imdlv_purchase_invoice` |
| `imdlv_purchaseimp_data` |
| `imdlv_purchaseimp_dline` |
| `imdlv_voucher_purchase` |
| `imdlv_voucherpurchline` |
| `imdlv_withholdingline` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `imdlv_homologation_product` | imdlv_homologation_product | — | — | ad_client_id→ad_client; ad_org_id→ad_org; m_product_id→m_product | Detalle enlazado a ad_client, ad_org, m_product. | PK `imdlv_homologation_key`; Cols: product_file, m_product_id, type_file; `IMDLV_HOMOLOGATION_ISACTIVE`: ISACTIVE IN ('Y', 'N') |
| `imdlv_lines` | imdlv_Lines | `IMDLV_LINES_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; a_asset_id→a_asset; bom_parent_id→imdlv_lines; c_aum→c_uom (+21) | Detalle enlazado a a_asset, ad_client, ad_org. Validado por trigger(s): IMDLV_LINES_TRG. | PK `imdlv_lines_key`; Cols: c_invoice_id, c_orderline_id, m_inoutline_id, line, description; `IMDLV_LINES_ISACTIVE_CHECK`: ISACTIVE IN ('Y', 'N') |
| `imdlv_partner` | imdlv_partner | — | — | c_bp_group_id→c_bp_group; c_country_id→c_country; c_currency_id→c_currency; c_region_id→c_region; ad_client_id→ad_client (+6) | Detalle enlazado a c_bp_group, c_country, c_currency. | PK `imdlv_partner_pk`; Cols: m_pricelist_id, c_paymentterm_id, c_country_id, c_region_id, c_bp_group_id; `IMDLV_PARTNER_ISACT`: ISACTIVE IN ('Y', 'N') |
| `imdlv_purchase_invoice` | imdlv_purchase_invoice | `IMDLV_PURCHASE_INVOICE_TRG` | — | c_cddodctype_id→c_doctype; c_cndoctype_id→c_doctype; c_wsdoctype_id→c_doctype; doctype_inout→c_doctype; doctype_order→c_doctype (+11) | Detalle enlazado a c_doctype. Validado por trigger(s): IMDLV_PURCHASE_INVOICE_TRG. | PK `imdlv_purchase_invoice_pk`; Cols: doctype_purchase_id, doctype_with_support_id, doctype_without_support_id, sswh_livelihoodt_id, sswh_codelivelihoodt_id; `IMDLV_PURCHASE_INVOICE_ISACT`: ISACTIVE IN ('Y', 'N') |
| `imdlv_purchaseimp_data` | imdlv_purchaseimp_data | — | — | ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `imdlv_purchaseimp_data_key`; Cols: c_doctype_id, documentno, dateimport, docstatus, dataload; `IMDLV_PIMPDATA_ISACT_CHK`: ISACTIVE IN ('Y', 'N') |
| `imdlv_purchaseimp_dline` | imdlv_purchaseimp_dline | — | — | ad_client_id→ad_client; imdlv_purchaseimp_data_id→imdlv_purchaseimp_data; ad_org_id→ad_org | Detalle enlazado a ad_client, ad_org, imdlv_purchaseimp_data. | PK `imdlv_purchaseimp_dline_key`; Cols: imdlv_purchaseimp_data_id, namexls, datelxls, cityxls, paymentmethodxls; `IMDLV_PIMP_DLINE_ISACT_CHK`: ISACTIVE IN ('Y', 'N'); `IMDLV_PIMP_DLINE_ISPRO_CHK`: ISPROCESS IN ('Y', 'N') |
| `imdlv_voucher_purchase` | imdlv_voucher_purchase | `IMDLV_VPORCHUSE2_TRG`; `IMDLV_VPORCHUSE_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; c_doctype_id→c_doctype | Detalle enlazado a ad_client, ad_org, c_doctype. Validado por trigger(s): IMDLV_VPORCHUSE2_TRG, IMDLV_VPORCHUSE_TRG. | PK `imdlv_vpurchase_key`; Cols: c_doctype_id, documentno, docstatus, dataload, processdata; `IMDLV_VPUR_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N') |
| `imdlv_voucherpurchline` | imdlv_voucherpurchline | `IMDLV_VOUCHER_TRG` | — | ad_client_id→ad_client; ad_org_id→ad_org; imdlv_voucher_purchase_id→imdlv_voucher_purchase | Detalle enlazado a ad_client, ad_org, imdlv_voucher_purchase. Validado por trigger(s): IMDLV_VOUCHER_TRG. | PK `imdlv_voucherpurchline_key`; Cols: imdlv_voucher_purchase_id, line, dateemision, taxid, bpartner; `IMDLV_VPURCH_ISACTIVE_CHK`: ISACTIVE IN ('Y', 'N'); `IMDLV_VPURCH_ISPROCESS_CHK`: ISPROCESS IN ('Y', 'N') |
| `imdlv_withholdingline` | imdlv_withholdingline | — | — | ad_client_id→ad_client; ad_org_id→ad_org; c_invoiceline_id→c_invoiceline; c_tax_id→c_tax; m_product_id→m_product | Detalle enlazado a ad_client, ad_org, c_invoiceline. | PK `imdlv_withholdingline_key`; Cols: description, line, m_product_id, linenetamt, lineivaamt |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `imdlv_homologation_product` |
| `imdlv_Lines` |
| `imdlv_partner` |
| `imdlv_purchase_invoice` |
| `imdlv_purchaseimp_data` |
| `imdlv_purchaseimp_dline` |
| `imdlv_voucher_purchase` |
| `imdlv_voucherpurchline` |
| `imdlv_withholdingline` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`C_INVOICE`, `C_INVOICELINE`, `SSRE_REFUNDINVOICE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El usuario navega a través de cuatro ventanas principales en la interfaz de usuario: 'Cargar Comprobantes XML', 'Datos por defecto creación Facturas', 'Datos por defecto creación Terceros' y 'Homologación de Productos'. Cada ventana está diseñada para facilitar distintas etapas del proceso de importación de datos, asegurando que los usuarios puedan ejecutar tareas específicas de manera intuitiva.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.localization.importdata.loadvouchers.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Cargar Comprobantes XML | Load Voucher Invoice |
| Datos por defecto creaciòn Facturas | Create Data Default Invoices |
| Datos por defecto creciòn Terceros | Create Data Default Partner |
| Homologación de Productos | Product Approval |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Cargar Comprobantes XML | Load Voucher Invoice | No |
| Configuración | Setup | Sí |
| Datos por defecto creaciòn Facturas | Create Data Default Invoices | No |
| Datos por defecto creciòn Terceros | Create Data Default Partner | No |
| Gestión Importación de datos | Managment Import Data | Sí |
| Homologación de Productos | Product Approval | No |
| Transacciones | Transactions | Sí |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.localization.importdata.loadvouchers.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Cargar Comprobantes XML

- **AD_WINDOW_ID:** `AB6447D2F0424300B2DC95205B0B631A`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Voucher purchase | `094B879B858745BA878EFC56ECFEC067` | 0 |
| 20 | Voucher | `4941CF66B530458E8D2FF0FD104FCD07` | 1 |
| 30 | Lines | `9D10B786B37D4A7296E231538F527D24` | 2 |

### Ventana: Datos por defecto creaciòn Facturas

- **AD_WINDOW_ID:** `A5C2132D9FF84726B0B28254967B9E89`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Create Data Default Invoice | `FDFF8BAD8ECF4DF69FD6865ABE4E6029` | 0 |

### Ventana: Datos por defecto creciòn Terceros

- **AD_WINDOW_ID:** `2183F236BB124BCAB2A5F70885D35E07`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Create Data Default Partner | `9E94151738C147D4BF1A5A6FD5A131BA` | 0 |

### Ventana: Homologación de Productos

- **AD_WINDOW_ID:** `8E53C9CDF5AC4314A5D986D0359E7F96`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `AD938CC1468C40C398CA85B641C7A95A` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Voucher purchase (ventana: Cargar Comprobantes XML)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Document No. | `Documentno` | No | No | — |
| 50 | Document Status | `Docstatus` | No | Sí | — |
| 60 | Authorization Purchase Load | `Dataload` | No | No | — |
| 80 | File Name | `Filenamedata` | No | Sí | — |
| 90 | Description | `Description` | No | No | — |
| 110 | Create Lines | `Createlines` | No | No | — |
| 130 | Transaction Date | `Datetrx` | No | No | — |
| 140 | Create  Order/Invoices | `Createtrx2` | No | No | — |
| 150 | Formato | `Formato` | No | No | — |

### Pestaña `290`

- **AD_TAB_ID:** `290` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 2280 | Load Lines Auth Refund | `EM_Imdlv_Load_Lines_Auth` | No | No | — |

### Header (ventana: Homologación de Productos)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 40 | Product_File | `Product_File` | No | No | — |
| 50 | Product | `M_Product_ID` | No | No | — |
| 60 | Type_File | `Type_File` | No | No | — |

### Lines (ventana: Cargar Comprobantes XML)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 20 | Line No. | `Line` | No | No | — |
| 30 | Product | `M_Product_ID` | No | No | — |
| 40 | Tax | `C_Tax_ID` | No | No | — |
| 50 | Active | `Isactive` | No | No | — |
| 120 | Invoiced Quantity | `Qtyinvoiced` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 130 | Unit Price | `Priceactual` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 150 | Line Net Amount | `Linenetamt` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 210 | Tax Amount | `Taxamt` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 215 | Tax base | `Baseimp` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 216 | Description | `Description` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 750 | Code | `Codexml` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 760 | Code Percentage withholding | `Coderet` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 770 | Code Tax | `Codetax` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 780 | Amount rent line | `Lineamtrent` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 790 | Total withholding source | `Withhrent` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 800 | Amount line VAT | `Lineamtvat` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 810 | Total withholding VAT | `Vatamt` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |

### Create Data Default Partner (ventana: Datos por defecto creciòn Terceros)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Price List | `M_Pricelist_ID` | No | No | — |
| 30 | Payment Terms | `C_Paymentterm_ID` | No | No | — |
| 40 | Country | `C_Country_ID` | No | No | — |
| 50 | Region | `C_Region_ID` | No | No | — |
| 60 | Business Partner Category | `C_Bp_Group_ID` | No | No | — |
| 80 | Taxpayer | `Sswh_Taxpayer_ID` | No | No | — |
| 90 | Language | `AD_Language_ID` | No | No | — |
| 100 | Payment Method | `FIN_Paymentmethod_ID` | No | No | — |
| 110 | Currency | `C_Currency_ID` | No | No | — |
| 120 | Active | `Isactive` | No | No | — |

### Create Data Default Invoice (ventana: Datos por defecto creaciòn Facturas)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Doctype Purchase | `Doctype_Purchase_ID` | No | No | — |
| 30 | Doctype_With_Support_ID | `Doctype_With_Support_ID` | No | No | — |
| 40 | Doctype_Without_Support_ID | `Doctype_Without_Support_ID` | No | No | — |
| 50 | Livelihoodt | `Sswh_Livelihoodt_ID` | No | No | — |
| 60 | Codelivelihoodt | `Sswh_Codelivelihoodt_ID` | No | No | — |
| 70 | Doctype Withholding | `Doctype_Withholding_ID` | No | No | — |
| 80 | Product Default | `Product_Default_ID` | No | No | — |
| 90 | Active | `Isactive` | No | No | — |
| 100 | Typetrx | `Typetrx` | No | No | — |
| 105 | Type xml | `Typetrxxml` | No | No | — |
| 150 | Document Type Order | `Doctype_Order` | No | No | BCE188C8449E4410910F8170C0FE410A |
| 160 | Document type Inout | `Doctype_Inout` | No | No | BCE188C8449E4410910F8170C0FE410A |
| 170 | Warehouse | `M_Warehouse_ID` | No | No | BCE188C8449E4410910F8170C0FE410A |

### Voucher (ventana: Cargar Comprobantes XML)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Line No. | `Line` | No | No | — |
| 30 | Document Type | `Documenttype` | No | No | — |
| 40 | Document No. | `Invoiceno` | No | No | — |
| 45 | Key Acess | `Keyacess` | No | No | — |
| 60 | Tax ID | `Taxid` | No | No | — |
| 70 | Business Partner | `Bpartner` | No | No | — |
| 75 | Date Emision | `Dateemision` | No | No | — |
| 80 | Processed | `Isprocess` | No | Sí | — |
| 85 | Log | `Logserror` | No | No | — |
| 87 | Active | `Isactive` | No | No | — |
| 100 | Emision Type | `Subdocumenttype` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 110 | Receiver Identification | `Documentaffected` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 120 | Subtotal | `Subtotal` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 123 | Tip | `Tipamt` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 130 | Vat | `Vat` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 140 | Total Invoice | `Totalinvoice` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 160 | Authorization No. | `Authorizationno` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 170 | Date Authorization | `Dateauthorization` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 180 | Status invoice | `Statusinvoice` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 190 | Reference Invoice | `Referenceinvoice` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 200 | Status Email | `Statusemail` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 210 | Email | `Emails` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 230 | Create Order | `Iscreateorder` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 240 | Create Invoice | `Iscreateinvoice` | No | No | 507E82F6FBE04347AE7E1966F61AEAC9 |
| 260 | Support Document | `Numdocsustento` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 270 | Date Emission Withholding | `DateEmission2` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 280 | Amount line VAT | `Lineamtvat` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 290 | Total withholding VAT | `Vatamt` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 300 | Amount rent line | `Lineamtrent` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
| 310 | Total withholding source | `Withhrent` | No | No | 4E0FF08009DB4D9CBD9653E9E445E397 |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

El módulo incluye cinco procesos clave que los usuarios pueden desencadenar mediante botones, como 'Completar', 'Retornar' y 'Rechazar'. Estos botones permiten a los usuarios gestionar el flujo de trabajo de importación, asegurando que los datos se validen y procesen correctamente. Aunque no hay informes específicos vinculados a estos procesos, las validaciones frecuentes están integradas para asegurar errores mínimos durante la importación y para mejorar la experiencia del usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.localization.importdata.loadvouchers.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar Comprobantes | Authorization Purchase Load | UploadAuthPurchaseCSV | Java `UploadAuthPurchaseCSV` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/UploadAuthPurchaseCSV.java` |
| Botón (Java) | Cargar Lineas Reembolso | Load Lines Auth Refund | LoadLinesAuthRefund | Java `LoadLinesAuthRefund` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `C_Invoice_ID`, No existen Impuestos validos; No se asigno un producto para para la linea de la factura. | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/LoadLinesAuthRefund.java` |
| Botón (Java) | Crear  Transacciones | Create  Order/Invoices | CreateOrderInvoice | Java `CreateTransactions` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/CreateTransactions.java` |
| Botón (Java) | Crear Facturas | Create Invoice | CreateInvoice | Java `ProcessTrx` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/ProcessTrx.java` |
| Botón (Java) | Crear Lineas | Create Lines | CreateLines | Java `CreateLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/CreateLines.java` |
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
| Botón (Java) | Cargar Comprobantes | `UploadAuthPurchaseCSV` | Proceso Java (toolbar/background) | `Imdlv_Voucher_Purchase_ID` | — | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/UploadAuthPurchaseCSV.java` |
| Botón (Java) | Cargar Lineas Reembolso | `LoadLinesAuthRefund` | Proceso Java (toolbar/background) | `C_Invoice_ID` | No existen Impuestos validos; No se asigno un producto para para la linea de la factura. | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/LoadLinesAuthRefund.java` |
| Botón (Java) | Crear  Transacciones | `CreateTransactions` | Proceso Java (toolbar/background) | `Imdlv_Voucher_Purchase_ID` | — | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/CreateTransactions.java` |
| Botón (Java) | Crear Facturas | `ProcessTrx` | Proceso Java (toolbar/background) | `Imdlv_Voucher_Purchase_ID` | — | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/ProcessTrx.java` |
| Botón (Java) | Crear Lineas | `CreateLines` | Proceso Java (toolbar/background) | `Imdlv_Voucher_Purchase_ID` | — | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/CreateLines.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar Comprobantes | Authorization Purchase Load | UploadAuthPurchaseCSV | Java `UploadAuthPurchaseCSV` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/UploadAuthPurchaseCSV.java` |
| Botón (Java) | Cargar Lineas Reembolso | Load Lines Auth Refund | LoadLinesAuthRefund | Java `LoadLinesAuthRefund` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `C_Invoice_ID`, No existen Impuestos validos; No se asigno un producto para para la linea de la factura. | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/LoadLinesAuthRefund.java` |
| Botón (Java) | Crear  Transacciones | Create  Order/Invoices | CreateOrderInvoice | Java `CreateTransactions` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/CreateTransactions.java` |
| Botón (Java) | Crear Facturas | Create Invoice | CreateInvoice | Java `ProcessTrx` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/ProcessTrx.java` |
| Botón (Java) | Crear Lineas | Create Lines | CreateLines | Java `CreateLines` (AD_MODEL_OBJECT `P`) | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/CreateLines.java` |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Botón (Java) | Cargar Comprobantes | Authorization Purchase Load | Java `UploadAuthPurchaseCSV` | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` |
| Botón (Java) | Cargar Lineas Reembolso | Load Lines Auth Refund | Java `LoadLinesAuthRefund` | Proceso Openbravo registro `C_Invoice_ID`, No existen Impuestos validos; No se asigno un producto para para la linea de la factura. | No existen Impuestos validos; No se asigno un producto para para la linea de la factura. |
| Botón (Java) | Crear  Transacciones | Create  Order/Invoices | Java `CreateTransactions` | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` |
| Botón (Java) | Crear Facturas | Create Invoice | Java `ProcessTrx` | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` |
| Botón (Java) | Crear Lineas | Create Lines | Java `CreateLines` | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` |
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
| `imdlv_duplicate_config_error` | Ya existe un registro activo para esta Organización y Tipo XML | Ya existe un registro activo para esta Organización y Tipo XML | Info | *(revisar Java/SQL adjuntos)* | AD_MESSAGE |
<!-- /knowledge-extract:messages -->

# Technical — Java extensions

## Functional

El módulo también incluye múltiples clases de Java, como 'GetDataAuthPurchase' y 'Imdlv_ImportDataVoucherPurchaseDocType', que implementan lógica de negocio específica y manejan la interacción entre la base de datos y la interfaz de usuario, asegurando que los datos sean validados y procesados correctamente durante la importación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.localization.importdata.loadvouchers`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `GetDataAuthPurchase` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_callouts/GetDataAuthPurchase.java` |
| `Imdlv_ImportDataVoucherPurchaseDocType` | ad_callouts | SimpleCallout | — | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_callouts/Imdlv_ImportDataVoucherPurchaseDocType.java` |
| `CreateLines` | ad_process | — | Proceso / informe Java | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/CreateLines.java` |
| `CreateTransactions` | ad_process | — | Proceso / informe Java | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/CreateTransactions.java` |
| `ImportVoucherData` | ad_process | — | Proceso / informe Java | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/ImportVoucherData.java` |
| `LoadLinesAuthRefund` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/LoadLinesAuthRefund.java` |
| `ProcessTrx` | ad_process | — | Proceso / informe Java | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/ProcessTrx.java` |
| `UploadAuthPurchaseCSV` | ad_process | DalBaseProcess | Proceso / informe Java | `src/ec/com/sidesoft/localization/importdata/loadvouchers/ad_process/UploadAuthPurchaseCSV.java` |
| `UpdateSequenceImportDataEvent` | bussinessevent | EntityPersistenceEventObserver | Event handler | `src/ec/com/sidesoft/localization/importdata/loadvouchers/bussinessevent/UpdateSequenceImportDataEvent.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| Trigger `IMDLV_HEADER2_TRG` | `c_file` | before INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `IMDLV_LINES_TRG` | `imdlv_lines` | before INSERT/DELETE | update imdlv_voucherpurchline set logserror = coalesce(logserror,' ')|| '"+ StrMsgErrors +"' where imdlv_voucherpurchline_id = ; |
| Trigger `IMDLV_PURCHASE_INVOICE_TRG` | `imdlv_purchase_invoice` | before INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `IMDLV_VOUCHER_TRG` | `imdlv_voucherpurchline` | before INSERT/DELETE | RAISE_APPLICATION_ERROR(-20000, '@20501@'); |
| Trigger `IMDLV_VPORCHUSE2_TRG` | `imdlv_voucher_purchase` | before UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| Trigger `IMDLV_VPORCHUSE_TRG` | `imdlv_voucher_purchase` | after DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). |
| AD_VAL_RULE | — | `ValidationORG` | `AD_ISORGINCLUDED(
    AD_Org.AD_Org_ID, 
    (SELECT ad_org_id FROM imdlv_voucher_purchase WHERE imdlv_voucher_purchase_` |
| AD_VAL_RULE | — | `ValidDoct` | `C_DOCTYPE.DOCBASETYPE='IMDLV_CX' AND C_DOCTYPE.AD_TABLE_ID = '094B879B858745BA878EFC56ECFEC067'` |
| Java event/validator | `UpdateSequenceImportDataEvent` | persistencia/UI | *(leer `src/ec/com/sidesoft/localization/importdata/loadvouchers/bussinessevent/UpdateSequenceImportDataEvent.java`)* |
| Función PL `imdlv_inout_createinvoice` | — | invocación proceso | Get UOM + Tax -- VERY simplified, but should work in most cases |
| Función PL `imdlv_inout_post` | — | invocación proceso | Check only Outgoing documents (Goods Shipment and Return to Vendor Shipment); Skip MovementQtyCheck when it is reversed document; Check whether warehouse belongs to the organization. |
| Función PL `imdlv_order_post1` | — | invocación proceso | Check whether warehouse belongs to the organization.; Get the name of the org of the Order. Added by P.Sarobe; Check the cash vat flag for all the taxes matches the order one |
| Función PL `imdlv_whsale_process` | — | invocación proceso | PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_Msgbox) ;; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

Los triggers y las funciones PL/pgSQL en el módulo son fundamentales para el soporte y mantenimiento de los datos importados. Por ejemplo, los triggers como 'IMDLV_VOUCHER_TRG' son responsables de manejar errores específicos que puedan surgir durante la importación de datos, permitiendo que el sistema opere de manera eficiente y minimizando problemas que puedan afectar el rendimiento de la aplicación.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `IMDLV_HEADER2_TRG` | `c_file` | before | INSERT/DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/IMDLV_HEADER2_TRG.xml` |
| `IMDLV_LINES_TRG` | `imdlv_lines` | before | INSERT/DELETE | update imdlv_voucherpurchline set logserror = coalesce(logserror,' ')|| '"+ StrMsgErrors +"' where imdlv_voucherpurchline_id = ; | `model/triggers/IMDLV_LINES_TRG.xml` |
| `IMDLV_PURCHASE_INVOICE_TRG` | `imdlv_purchase_invoice` | before | INSERT/UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/IMDLV_PURCHASE_INVOICE_TRG.xml` |
| `IMDLV_VPORCHUSE2_TRG` | `imdlv_voucher_purchase` | before | UPDATE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/IMDLV_VPORCHUSE2_TRG.xml` |
| `IMDLV_VPORCHUSE_TRG` | `imdlv_voucher_purchase` | after | DELETE | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | `model/triggers/IMDLV_VPORCHUSE_TRG.xml` |
| `IMDLV_VOUCHER_TRG` | `imdlv_voucherpurchline` | before | INSERT/DELETE | RAISE_APPLICATION_ERROR(-20000, '@20501@'); | `model/triggers/IMDLV_VOUCHER_TRG.xml` |
<!-- /knowledge-extract:triggers -->

### Funciones PL/pgSQL (enlazadas a botones)

<!-- knowledge-extract:functions -->
| Función PL/pgSQL | Proceso / botón (es_ES) | Qué hace (resumen) | Validaciones / errores | Archivo |
| --- | --- | --- | --- | --- |
| `imdlv_inout_createinvoice` | — | Get UOM + Tax -- VERY simplified, but should work in most cases | Get UOM + Tax -- VERY simplified, but should work in most cases | `model/functions/IMDLV_INOUT_CREATEINVOICE.xml` |
| `imdlv_inout_post` | — | Check only Outgoing documents (Goods Shipment and Return to Vendor Shipment); Skip MovementQtyCheck when it is reversed document; Check whether warehouse belongs to the organization.; Check negative quantities on return… | Check only Outgoing documents (Goods Shipment and Return to Vendor Shipment); Skip MovementQtyCheck when it is reversed document; Check whether warehouse belongs to the organization.; Check negative quantities on return inouts; Check the header belongs to a organization where transactions are posible and ready to use; Check the period control is opened (only if it is legal entity with accounting) | `model/functions/IMDLV_INOUT_POST.xml` |
| `imdlv_inserts` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/IMDLV_INSERTS.xml` |
| `imdlv_order_post1` | — | Check whether warehouse belongs to the organization.; Get the name of the org of the Order. Added by P.Sarobe; Check the cash vat flag for all the taxes matches the order one; Verify not managed debtPayments added by ALO | Check whether warehouse belongs to the organization.; Get the name of the org of the Order. Added by P.Sarobe; Check the cash vat flag for all the taxes matches the order one; Verify not managed debtPayments added by ALO; Cancel existing Deli very + Invoice Documents; ADDED BY P.SAROBE but to be deprecated 26052007 | `model/functions/IMDLV_ORDER_POST1.xml` |
| `imdlv_whsale_process` | — | PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_Msgbox) ;; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES; CREO UN REGISTRO EN L… | PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'Y', NULL, NULL) ;; PERFORM AD_UPDATE_PINSTANCE(PInstance_ID, NULL, 'N', 0, v_Msgbox) ;; SE BUSCAN LOS PARAMETROS DE LA CONFIGURACION DE RETENCIONES; CREO UN REGISTRO EN LA CABECERA DE LOS COBROS; Get corresponding FIN_PAYMENT_SCHEDULE_ID; Elimina la relacion del cobro de la retencion con el detalle de plan de pagos | `model/functions/IMDLV_WHSALE_PROCESS.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cargar Comprobantes | `UploadAuthPurchaseCSV` | Botón (Java) | Java `UploadAuthPurchaseCSV` | N | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` |
| 2 | Cargar Lineas Reembolso | `LoadLinesAuthRefund` | Botón (Java) | Java `LoadLinesAuthRefund` | N | Proceso Openbravo registro `C_Invoice_ID`, No existen Impuestos validos; No se asigno un producto para para la linea de la factura. |
| 3 | Crear  Transacciones | `CreateOrderInvoice` | Botón (Java) | Java `CreateTransactions` | N | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` |
| 4 | Crear Facturas | `CreateInvoice` | Botón (Java) | Java `ProcessTrx` | N | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` |
| 5 | Crear Lineas | `CreateLines` | Botón (Java) | Java `CreateLines` | N | Proceso Openbravo registro `Imdlv_Voucher_Purchase_ID` |

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

Módulo: `ec.com.sidesoft.localization.importdata.loadvouchers`.

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

# Glosario — prefijo `IMDLV`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `IMDLV` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.localization.importdata.loadvouchers` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `UploadAuthPurchaseCSV` — Cargar Comprobantes
- `LoadLinesAuthRefund` — Cargar Lineas Reembolso
- `CreateOrderInvoice` — Crear  Transacciones
- `CreateInvoice` — Crear Facturas
- `CreateLines` — Crear Lineas

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## localization julian date
**Package:** `ec.com.sidesfot.localizacion.ecuador.juliandate`

# Module overview — localization julian date

## Functional

El módulo de 'localization julian date' tiene como propósito principal la creación de un atributo automático para el día juliano en el sistema Openbravo. Este módulo es utilizado por usuarios de negocio que requieren registrar fechas julianas y por el equipo de soporte que necesita garantizar su correcto funcionamiento. El alcance del módulo incluye la modificación de los atributos en las instancias de conjuntos de atributos. Presenta dependencias con la versión de Openbravo y otros módulos esenciales que permiten su integración en el entorno del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesfot/localizacion/ecuador/juliandate` |
| Web | `web/ec.com.sidesfot.localizacion.ecuador.juliandate/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`CSLJ`

# Guía de chat — localization julian date

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesfot.localizacion.ecuador.juliandate`).

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

- ¿Cómo puedo ver la fecha juliana en los atributos?
- ¿Qué debo hacer si no se genera el atributo de fecha juliana automáticamente?
- ¿Dónde encuentro información sobre el funcionamiento del módulo?
- ¿Este módulo afecta a otros procesos del ERP?
- ¿Cómo se integra este módulo con los atributos existentes?
- ¿Hay alguna forma de deshabilitar la generación automática del atributo?
- ¿Qué hacer si la fecha generada es incorrecta?
- ¿Existen manuales o recursos adicionales sobre este módulo?

# Domain — data model

## Functional

El módulo se centra en la entidad cabecera relacionada con los conjuntos de atributos, específicamente en las tablas 'M_ATTRIBUTESET' y 'M_ATTRIBUTESETINSTANCE'. A través de la trigger 'CSLJ_JULYDAY_CREATED_TRG', se asegura que, si no se asigna un valor a la fecha juliana, se genere automáticamente usando 'EM_Cslj_DateJulian'. Esta lógica permite mantener la integridad y consistencia de los datos en las tablas relacionadas, asegurando que se actualicen de manera correcta según las operaciones realizadas.

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

`M_ATTRIBUTESET`, `M_ATTRIBUTESETINSTANCE`

### Views

*(ninguna)*

# Functional — windows and menus

## Functional

El módulo no cuenta con ventanas específicas en la interfaz de usuario, lo que sugiere que su funcionalidad está integrada en otras partes del sistema. La navegación y utilización de este módulo se realizaría a través de las pantallas relacionadas con los conjuntos de atributos, donde los usuarios podrían observar los cambios en los atributos automáticamente generados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesfot.localizacion.ecuador.juliandate.es_ES/referencedata/translation/`.

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

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesfot.localizacion.ecuador.juliandate.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
## Campos añadidos por el módulo (AD_FIELD)

### Pestaña `461`

- **AD_TAB_ID:** `461` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 105 | EM_Cslj_Priority | `EM_Cslj_Priority` | No | No | — |
| 160 | EM_Cslj_Juliandate | `EM_Cslj_Juliandate` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

No se especifican botones de proceso dentro de este módulo, por lo que se deduce que su funcionamiento es automático tras la modificación de los atributos. Las validaciones frecuentes aseguradas por el trigger hacen que cualquier instancia nueva de atributos verifique su estado y genere la información necesaria. Aunque no se mencionan informes específicos, el módulo facilita la gestión de atributos al integrar el control de fechas julianas dentro del flujo general de operación del ERP.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesfot.localizacion.ecuador.juliandate.es_ES/referencedata/translation/`.

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

No se ha implementado código Java en este módulo, lo que refuerza el enfoque en la utilización de triggers para la gestión de datos dentro del contexto de Openbravo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesfot.localizacion.ecuador.juliandate`.

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
| Trigger `CSLJ_JULYDAY_CREATED_TRG` | `m_attributesetinstance` | before INSERT/UPDATE | Si no tiene valor, generar EM_Cslj_DateJulian; Devolver el registro dependiendo de la operación |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El trigger 'CSLJ_JULYDAY_CREATED_TRG' desempeña un papel crucial en el soporte de la funcionalidad del módulo al supervisar y manejar las modificaciones de los registros en 'M_ATTRIBUTESETINSTANCE'. Debido a su naturaleza automática, no se requieren funciones PL específicas, pero cualquier operación de modificación en las instancias implica la activación de este trigger para asegurar la correcta configuración de las fechas julianas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Triggers (detalle por tabla y evento)

<!-- knowledge-extract:triggers -->
| Trigger | Tabla | Momento | Eventos | Qué hace (resumen) | Archivo XML |
| --- | --- | --- | --- | --- | --- |
| `CSLJ_JULYDAY_CREATED_TRG` | `m_attributesetinstance` | before | INSERT/UPDATE | Si no tiene valor, generar EM_Cslj_DateJulian; Devolver el registro dependiendo de la operación | `model/triggers/CSLJ_JULYDAY_CREATED_TRG.xml` |
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

Módulo: `ec.com.sidesfot.localizacion.ecuador.juliandate`.

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

# Glosario — prefijo `CSLJ`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `CSLJ` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesfot.localizacion.ecuador.juliandate` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Sidesoft Reporting Utilities
**Package:** `ec.com.sidesoft.report.utility`

# Module overview — Sidesoft Reporting Utilities

## Functional

Sidesoft Reporting Utilities es un módulo diseñado para mejorar la capacidad de generación de informes dentro de Openbravo ERP. Su propósito principal es proporcionar utilidades de informes que permiten a los usuarios extraer y manejar datos de forma más eficiente. Los actores principales que se benefician de este módulo son los usuarios de negocio que generan informes, así como el equipo de soporte y desarrolladores que necesitan adaptar y extender la funcionalidad. Este módulo es compatible con las versiones de Openbravo de la 2.50 a la 3.00 y depende del núcleo de Openbravo y su marco de trabajo.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/report/utility` |
| Web | `web/ec.com.sidesoft.report.utility/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin
- Core
- Openbravo 3.0 Framework

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

*(sin prefijo en AD_MODULE_DBPREFIX)*

# Guía de chat — Sidesoft Reporting Utilities

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.report.utility`).

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

- ¿Cómo puedo generar un nuevo informe usando Sidesoft Reporting Utilities?
- ¿Cuáles son los requisitos para usar scriptlets en mis informes?
- ¿Dónde puedo encontrar más información sobre las utilidades que ofrece este módulo?
- ¿Qué versiones de Openbravo son compatibles con Sidesoft Reporting Utilities?
- ¿Cómo me aseguro de que mis informes reflejan datos precisos?
- ¿Existen ejemplos de scriptlets que puedo utilizar como referencia?
- ¿Es posible personalizar la salida de los informes generados?
- ¿Qué hacer si tengo problemas técnicos al utilizar el módulo?

# Domain — data model

## Functional

El modelo de datos de Sidesoft Reporting Utilities no incluye tablas físicas, funciones PL o triggers, lo que implica que su enfoque está más dirigido a ofrecer utilidades a través de scriptlets para la generación de informes. No hay entidades persistentes o cabeceras de tablas que gestionar, sino que las funciones del módulo se centran en mejorar la interacción con los datos existentes dentro de Openbravo. La relación con otras entidades se da indirectamente a través de las funcionalidades que los informes pueden extraer o manipular, aunque no se definen relaciones explícitas en el modelo.

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

El módulo no incluye ventanas o menús específicos en la interfaz de usuario, lo que sugiere que su uso se integra a través de funcionalidades de scripting más que en una interfaz visual tradicional. La navegación por el módulo se realiza principalmente a través de las funcionalidades que se invocan desde otros contextos del ERP, haciendo uso de scriptlets para personalizar la salida de los informes.

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

Dado que el módulo no cuenta con procesos definidos, no hay botones como completar, retornar o rechazar. Sin embargo, los usuarios pueden generar informes mediante scriptlets, aunque la documentación advierte que estos no deben ser utilizados directamente. Las validaciones frecuentes dependerán de la correcta implementación de estos scriptlets para asegurar la calidad de los datos extraídos.

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

La clase Utility del módulo contiene métodos que facilitan la obtención de información sobre el usuario y la organización que ha iniciado sesión, permitiendo a los desarrolladores acceder a esos datos de manera sencilla. Esta funcionalidad es crucial para personalizar informes y asegurar que la seguridad y contexto del usuario sean correctamente aplicados en las salidas.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.report.utility`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `Utility` | root | — | — | `src/ec/com/sidesoft/report/utility/Utility.java` |
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

No se registran triggers o funciones PL en el módulo, lo que implica que su rol en la base de datos es mínimo. Las interacciones se gestionan principalmente a través de la lógica de aplicación y las clases Java que proporcionan las utilidades necesarias. Cualquier soporte requerirá atención al desarrollo de estos scriptlets y a cómo interactúan con la base de datos de Openbravo.

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

Módulo: `ec.com.sidesoft.report.utility`.

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

# Glosario — prefijo `UTILITY`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `UTILITY` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.report.utility` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

*(Sin procesos con VALUE en AD_PROCESS del módulo.)*

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).

---
## Customization -Print Reports Generics
**Package:** `ec.com.sidesoft.custom.reports`

# Module overview — Customization -Print Reports Generics

## Functional

El módulo 'Customization - Print Reports Generics' permite a los usuarios generar e imprimir reportes y plantillas personalizadas en Openbravo ERP. Está dirigido principalmente a usuarios de negocio que necesitan informes específicos y a desarrolladores que buscan adaptar o mejorar las capacidades de generación de reportes del sistema. Este módulo tiene una dependencia con la '2.50 to 3.00 Compatibility Skin' y se integra dentro de la funcionalidad existente del ERP, extendiendo su capacidad de gestión de reportes.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

| Item | Location |
|------|----------|
| Module descriptor | `src-db/database/sourcedata/AD_MODULE.xml` |
| Dependencies | `src-db/database/sourcedata/AD_MODULE_DEPENDENCY.xml` |
| Application dictionary | `src-db/database/sourcedata/` |
| Physical model | `src-db/database/model/tables/`, `triggers/`, `functions/`, `views/` |
| Core extensions | `src-db/database/model/modifiedTables/` |
| Java | `src/ec/com/sidesoft/custom/reports` |
| Web | `web/ec.com.sidesoft.custom.reports/` |

### Declared dependencies

- 2.50 to 3.00 Compatibility Skin

### Version

**2.0.0** (from `AD_MODULE.xml`).

### DB prefix

`SESCR`

# Guía de chat — Customization -Print Reports Generics

## Cómo preguntar

Describa **lo que ve en pantalla** (nombre de ventana, botón, mensaje de error). No hace falta el nombre del módulo Java (`ec.com.sidesoft.custom.reports`).

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
- «¿Qué es la tabla sescr_template_report?» → catálogo en el modelo físico del paquete (`model/tables/`) y el Application dictionary (`src-db/database/sourcedata/`)

## Preguntas ejemplo (IA)

- ¿Cómo puedo generar un nuevo reporte personalizado?
- ¿Dónde encuentro la plantilla de reporte que necesito editar?
- ¿Qué tipos de reportes puedo generar con este módulo?
- ¿Cómo puedo validar los datos antes de la impresión?
- ¿Existen opciones para programar la generación de reportes automáticamente?
- ¿Cómo puedo solucionar errores al imprimir un reporte?
- ¿Dónde puedo ver los reportes que ya he generado?
- ¿Qué debo hacer si un reporte no se muestra correctamente?

# Domain — data model

## Functional

La entidad principal del módulo es la tabla 'sescr_template_report', que almacena las plantillas de reportes personalizadas. Este modelo soporta etapas de configuración y generación de reportes que son cruciales para la impresión de documentos. Aunque no hay triggers específicos, el módulo hace uso de 24 funciones PL/pgSQL para procesos y validaciones, facilitando así la ejecución de diversas operaciones sobre los datos relacionados con los reportes generados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

### Physical tables (`src-db/database/model/tables/`)

<!-- knowledge-extract:physical_tables -->
| Tabla física |
| --- |
| `sescr_template_report` |
<!-- /knowledge-extract:physical_tables -->

### Catálogo de tablas (funcional y técnico)

<!-- knowledge-extract:tables_catalog -->
| Tabla | AD_TABLE (diccionario) | Triggers | UNIQUE | FK principales | Propósito (funcional) | Notas técnicas |
| --- | --- | --- | --- | --- | --- | --- |
| `sescr_template_report` | sescr_template_report | — | — | ad_client_id→ad_client; c_doctype_id→c_doctype; ad_org_id→ad_org; ad_table_id→ad_table; ad_window_id→ad_window | Detalle enlazado a ad_client, ad_org, c_doctype. | PK `sescr_template_report_pk`; Cols: ad_window_id, template_dir, name_report, title, ad_table_id; `SESCR_TEMPREPORT_ISACTIV_CHK`: ISACTIVE IN ('Y', 'N') |
<!-- /knowledge-extract:tables_catalog -->

### AD_TABLE names (dictionary)

<!-- knowledge-extract:ad_tables -->
| AD_TABLE.NAME |
| --- |
| `sescr_product_data_v` |
| `sescr_template_report` |
<!-- /knowledge-extract:ad_tables -->

### Modified core tables

`FIN_PAYMENT`

### Views

`SESCR_INVOICE_PAYMENT_V`, `SESCR_ORDER_SUMMARY_V`, `SESCR_PRODUCT_DATA_V`, `SESCR_TREENODE_V`

# Functional — windows and menus

## Functional

El módulo incluye dos ventanas principales: 'Configuración - Plantillas de Reportes' y 'Datos de Producto'. Los usuarios pueden navegar a través de estas ventanas para configurar las plantillas necesarias y gestionar los datos de producto relacionados. La interfaz de usuario permite un acceso intuitivo a las funcionalidades de generación de reportes mediante menús organizados y opciones visibles.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_WINDOW.xml`, `AD_MENU.xml` + traducciones en `ec.com.sidesoft.custom.reports.es_ES/referencedata/translation/`.

## Ventanas

<!-- knowledge-extract:windows -->
| Pantalla / ventana (es_ES) | Window name (en_US) |
| --- | --- |
| Configuración - Plantillas de Reportes | Setup - Template Reports |
| Datos de Producto | Product Data |
<!-- /knowledge-extract:windows -->

## Menús

<!-- knowledge-extract:menus -->
| Menú (es_ES) | NAME (en_US) | Resumen |
| --- | --- | --- |
| Configuración | Setup | Sí |
| Configuración - Plantillas de Reportes | Setup - Template Reports | No |
| Datos de Producto | Product Data | No |
| Reporte de ventas por línea con representante de ventas | Sales report by line with sales representative | No |
<!-- /knowledge-extract:menus -->

# 22 — Especificaciones de ventana / pestaña

## Functional

Fichas por ventana o por pestañas con campos definidos en este módulo (`AD_FIELD`). Complementar con narrativa de negocio; `--with-ai` puede enriquecer párrafos.

## Technical

Origen: `AD_WINDOW.xml`, `AD_TAB.xml`, `AD_FIELD.xml`, `AD_COLUMN.xml`, traducciones en `ec.com.sidesoft.custom.reports.es_ES/referencedata/translation/`.

<!-- knowledge-extract:window_specs -->
### Ventana: Configuración - Plantillas de Reportes

- **AD_WINDOW_ID:** `CA8691ADAA714437AFDAD92F47399495`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Setup - Template Reports | `CEEA7D9B89AC452F91677C45F0753842` | 0 |

### Ventana: Datos de Producto

- **AD_WINDOW_ID:** `AD6D2068E7BE466A80BE8EE4A76BB231`
- **Pestañas:**

| Seq | Pestaña | Tabla (AD_TABLE_ID) | Nivel |
| --- | --- | --- | --- |
| 10 | Header | `1467D92DCB584AF3850A61462DD93298` | 0 |

## Campos añadidos por el módulo (AD_FIELD)

### Setup - Template Reports (ventana: Configuración - Plantillas de Reportes)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 25 | Search Key | `Title` | No | No | — |
| 30 | Window | `AD_Window_ID` | No | No | — |
| 35 | Table | `AD_Table_ID` | No | No | — |
| 37 | Document Type | `C_Doctype_ID` | No | No | — |
| 40 | Template Location | `Template_Dir` | No | No | — |
| 50 | Template Filename | `Name_Report` | No | No | — |
| 60 | Output type | `Output_Type` | No | No | — |

### Header (ventana: Datos de Producto)

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 10 | Organization | `AD_Org_ID` | No | No | — |
| 20 | Active | `Isactive` | No | No | — |
| 30 | Search Key | `Value` | No | No | — |
| 40 | Commercial Name | `Name` | No | No | — |
| 50 | UOM | `C_Uom_ID` | No | No | — |
| 60 | Product Category | `M_Product_Category_ID` | No | No | — |
| 70 | Purchase | `Ispurchased` | No | No | — |
| 80 | Sale | `Issold` | No | No | — |
| 90 | Product Type | `Producttype` | No | No | — |
| 100 | Withholding at the Source | `Sswh_Withholding_Source_ID` | No | No | — |
| 110 | Stocked | `Isstocked` | No | No | — |
| 120 | Production | `Production` | No | No | — |
| 130 | Tax Category | `C_Taxcategory_ID` | No | No | — |
| 140 | Bill of Materials | `Isbom` | No | No | — |
| 150 | Product Revenue | `P_Revenue_Acct` | No | No | — |
| 160 | Product Asset | `P_Asset_Acct` | No | No | — |
| 170 | Product Expense | `P_Expense_Acct` | No | No | — |
| 180 | Product COGS | `P_Cogs_Acct` | No | No | — |

### Pestaña `F7A52FDAAA0346EFA07D53C125B40404`

- **AD_TAB_ID:** `F7A52FDAAA0346EFA07D53C125B40404` *(pestaña definida en otro módulo)*

| Seq | Campo (es_ES) | Columna | Obligatorio | Solo lectura | Grupo |
| --- | --- | --- | --- | --- | --- |
| 35 | Name | `EM_Sescr_Name` | No | No | — |
| 55 | Paymentdate | `EM_Sescr_Paymentdate` | No | No | — |
<!-- /knowledge-extract:window_specs -->

# Functional — processes and buttons

## Functional

Las acciones dentro del módulo incluyen un proceso típico para generar e imprimir reportes. Los botones comunes pueden incluir opciones como completar o retornar procesos de impresión. Este módulo cuenta con siete tipos de informes disponibles, que permiten a los usuarios extraer información relevante en formatos específicos, como 'GENERIC - PRINT WITHHOLDING' o 'PRINT GENERIC - REPORT JOURNAL'. Además, incluye validaciones proporcionadas por las funciones PL, lo que asegura la integridad de los datos en los reportes generados.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Origen: `AD_PROCESS.xml`, `AD_MODEL_OBJECT.xml`, `model/functions/`, `src/**/ad_process/*.java`, traducciones en `ec.com.sidesoft.custom.reports.es_ES/referencedata/translation/`.

### Botones (toolbar, PL y Java)

<!-- knowledge-extract:process_buttons -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte de ventas por línea con representante de ventas | Sales report by line with sales representative | Sescr_ReportSalesRepresentative | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:process_buttons -->

### Informes / reportes (Java servlet + JRXML)

<!-- knowledge-extract:process_reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | GENERIC - PARTIAL PAYMENT DETAIL | GENERIC - PARTIAL PAYMENT DETAIL | GENERIC - PARTIAL PAYMENT DETAIL | Java `Sescr_ReportPrintPayrollPartialPayment` (AD_MODEL_OBJECT `S`) | Servlet de informe `Sescr_ReportPrintPayrollPartialPayment` (fuente no en `src/` del módulo). | — |
| Reporte | GENERIC - PRINT GOODS MOVEMENTS | GENERIC - PRINT GOODS MOVEMENTS | GENERIC - PRINT GOODS MOVEMENTS | Java `Sescr_ReportPrintGoodsMovements` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/warehouse/Sescr_ReportPrintGoodsMovements.java` |
| Reporte | GENERIC - PRINT WITHHOLDING | GENERIC - PRINT WITHHOLDING | GENERIC - PRINT WITHHOLDING | Java `Sescr_ReportPrintWithholding` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/withholdings/Sescr_ReportPrintWithholding.java` |
| Reporte | GENERIC PRINT CHECK PAYMENT | GENERIC PRINT CHECK PAYMENT | GENERIC PRINT CHECK PAYMENT | Java `Sescr_ReportPrintCheckPayments` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/finances/Sescr_ReportPrintCheckPayments.java` |
| Reporte | GENERIC STANDARD - PRINT GOODS MOVEMENTS | GENERIC STANDARD - PRINT GOODS MOVEMENTS | GENERIC STANDARD - PRINT GOODS MOVEMENTS | Java `Sescr_ReportPrintGoodsMovementsStandard` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/warehouse/Sescr_ReportPrintGoodsMovementsStandard.java` |
| Reporte | Print Custom Order Service | Print Custom Order Service | SescrPrintServiceOrder | Java `SescrPrintServiceOrder` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/reports/ad_reports/CustomOrdenServicio.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/SescrPrintServiceOrder.java` |
| Reporte | PRINT GENERIC - REPORT JOURNAL | PRINT GENERIC - REPORT JOURNAL | PRINT GENERIC - REPORT JOURNAL | Java `Sescr_ReportPrintManualJournalEntries` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/manualjournalentries/Sescr_ReportPrintManualJournalEntries.java` |
<!-- /knowledge-extract:process_reports -->

### Procesos background

<!-- knowledge-extract:process_background -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | GENERIC - PRINT WITHHOLDING | GENERIC - PRINT WITHHOLDING | GENERIC - PRINT WITHHOLDING | Java `Sescr_ReportPrintWithholding` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/withholdings/Sescr_ReportPrintWithholding.java` |
<!-- /knowledge-extract:process_background -->

### Catálogo clases Java de procesos

<!-- knowledge-extract:java_processes -->
| Tipo | Texto (es_ES) | Clase Java | Base / rol | Parámetro / sesión | JRXML o mensajes | Ruta fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | GENERIC - PARTIAL PAYMENT DETAIL | `Sescr_ReportPrintPayrollPartialPayment` | Informe (servlet) | `—` | — | `—` |
| Reporte | GENERIC - PRINT GOODS MOVEMENTS | `Sescr_ReportPrintGoodsMovements` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/custom/reports/ad_process/warehouse/Sescr_ReportPrintGoodsMovements.java` |
| Reporte | GENERIC - PRINT WITHHOLDING | `Sescr_ReportPrintWithholding` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/custom/reports/ad_process/withholdings/Sescr_ReportPrintWithholding.java` |
| Reporte | GENERIC PRINT CHECK PAYMENT | `Sescr_ReportPrintCheckPayments` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/custom/reports/ad_process/finances/Sescr_ReportPrintCheckPayments.java` |
| Reporte | GENERIC STANDARD - PRINT GOODS MOVEMENTS | `Sescr_ReportPrintGoodsMovementsStandard` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/custom/reports/ad_process/warehouse/Sescr_ReportPrintGoodsMovementsStandard.java` |
| Reporte | Print Custom Order Service | `SescrPrintServiceOrder` | Informe (servlet PDF) | `—` | ec/com/sidesoft/custom/reports/ad_reports/CustomOrdenServicio.jrxml | `src/ec/com/sidesoft/custom/reports/ad_process/SescrPrintServiceOrder.java` |
| Reporte | PRINT GENERIC - REPORT JOURNAL | `Sescr_ReportPrintManualJournalEntries` | Informe (servlet PDF) | `—` | — | `src/ec/com/sidesoft/custom/reports/ad_process/manualjournalentries/Sescr_ReportPrintManualJournalEntries.java` |
<!-- /knowledge-extract:java_processes -->

### Resumen botones (legacy)

<!-- knowledge-extract:processes -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte de ventas por línea con representante de ventas | Sales report by line with sales representative | Sescr_ReportSalesRepresentative | *(OBUIAPP / manual)* | — | — |
<!-- /knowledge-extract:processes -->

### Detalle validaciones

<!-- knowledge-extract:processes_detail -->
| Tipo | Botón (es_ES) | NAME | Implementación | Qué hace | Validaciones / Java |
| --- | --- | --- | --- | --- | --- |
| Proceso / otro | Reporte de ventas por línea con representante de ventas | Sales report by line with sales representative | — | — | — |
<!-- /knowledge-extract:processes_detail -->

### Informes (tabla compacta)

<!-- knowledge-extract:reports -->
| Tipo | Texto (es_ES) | NAME | VALUE | Implementación | Detalle Java / PL | Clase y ruta |
| --- | --- | --- | --- | --- | --- | --- |
| Reporte | GENERIC - PARTIAL PAYMENT DETAIL | GENERIC - PARTIAL PAYMENT DETAIL | GENERIC - PARTIAL PAYMENT DETAIL | Java `Sescr_ReportPrintPayrollPartialPayment` (AD_MODEL_OBJECT `S`) | Servlet de informe `Sescr_ReportPrintPayrollPartialPayment` (fuente no en `src/` del módulo). | — |
| Reporte | GENERIC - PRINT GOODS MOVEMENTS | GENERIC - PRINT GOODS MOVEMENTS | GENERIC - PRINT GOODS MOVEMENTS | Java `Sescr_ReportPrintGoodsMovements` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/warehouse/Sescr_ReportPrintGoodsMovements.java` |
| Reporte | GENERIC - PRINT WITHHOLDING | GENERIC - PRINT WITHHOLDING | GENERIC - PRINT WITHHOLDING | Java `Sescr_ReportPrintWithholding` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/withholdings/Sescr_ReportPrintWithholding.java` |
| Reporte | GENERIC PRINT CHECK PAYMENT | GENERIC PRINT CHECK PAYMENT | GENERIC PRINT CHECK PAYMENT | Java `Sescr_ReportPrintCheckPayments` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/finances/Sescr_ReportPrintCheckPayments.java` |
| Reporte | GENERIC STANDARD - PRINT GOODS MOVEMENTS | GENERIC STANDARD - PRINT GOODS MOVEMENTS | GENERIC STANDARD - PRINT GOODS MOVEMENTS | Java `Sescr_ReportPrintGoodsMovementsStandard` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/warehouse/Sescr_ReportPrintGoodsMovementsStandard.java` |
| Reporte | Print Custom Order Service | Print Custom Order Service | SescrPrintServiceOrder | Java `SescrPrintServiceOrder` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `ec/com/sidesoft/custom/reports/ad_reports/CustomOrdenServicio.jrxml`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/SescrPrintServiceOrder.java` |
| Reporte | PRINT GENERIC - REPORT JOURNAL | PRINT GENERIC - REPORT JOURNAL | PRINT GENERIC - REPORT JOURNAL | Java `Sescr_ReportPrintManualJournalEntries` (AD_MODEL_OBJECT `S`) | Genera PDF desde JRXML `—`; contexto sesión `—`. | `src/ec/com/sidesoft/custom/reports/ad_process/manualjournalentries/Sescr_ReportPrintManualJournalEntries.java` |
<!-- /knowledge-extract:reports -->

# 31 — Inventario de reportes

## Functional

Inventario de informes (`ISREPORT=Y`) y plantillas JRXML del módulo.

## Technical

<!-- knowledge-extract:reports_inventory -->
**Total de reportes del módulo: 35**

Conteo: `ISREPORT=Y` en `AD_PROCESS.xml` = **7**; archivos `*.jrxml` en el repo = **35**.

| # | Nombre pantalla (es_ES) | VALUE | Proceso Java / JRXML | Parámetros | Descripción |
| --- | --- | --- | --- | --- | --- |
| 1 | GENERIC - PARTIAL PAYMENT DETAIL | `GENERIC - PARTIAL PAYMENT DETAIL` | Java `Sescr_ReportPrintPayrollPartialPayment`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | GENERIC - PARTIAL PAYMENT DETAIL |
| 2 | GENERIC - PRINT GOODS MOVEMENTS | `GENERIC - PRINT GOODS MOVEMENTS` | Java `Sescr_ReportPrintGoodsMovements`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | GENERIC - PRINT GOODS MOVEMENTS |
| 3 | GENERIC - PRINT WITHHOLDING | `GENERIC - PRINT WITHHOLDING` | Java `Sescr_ReportPrintWithholding`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | GENERIC - PRINT WITHHOLDING |
| 4 | GENERIC PRINT CHECK PAYMENT | `GENERIC PRINT CHECK PAYMENT` | Java `Sescr_ReportPrintCheckPayments`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | GENERIC PRINT CHECK PAYMENT |
| 5 | GENERIC STANDARD - PRINT GOODS MOVEMENTS | `GENERIC STANDARD - PRINT GOODS MOVEMENTS` | Java `Sescr_ReportPrintGoodsMovementsStandard`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | GENERIC STANDARD - PRINT GOODS MOVEMENTS |
| 6 | Print Custom Order Service | `SescrPrintServiceOrder` | Java `SescrPrintServiceOrder`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | Print Custom Order Service |
| 7 | PRINT GENERIC - REPORT JOURNAL | `PRINT GENERIC - REPORT JOURNAL` | Java `Sescr_ReportPrintManualJournalEntries`; JRXML — | *(ver AD_PROCESS_PARA / servlet)* | PRINT GENERIC - REPORT JOURNAL |

### Plantillas sin proceso en diccionario

- `src/ec/com/sidesoft/custom/reports/ad_process/manualjournalentries/Sescr_ReportPrintManualJournalEntries.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/CustomOrdenServicio.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/Museos/accounting/FactAccout.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/AgingScheduleDetailXLS.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/AgingScheduleXLS.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/C_OrderLinesJR.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/C_QuotationJR.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/PayablesOut_Voucher.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/PayablesOut_Voucher_Detail.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/PayablesOut_Voucher_DetailHeader.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/PayablesOut_Voucher_budget.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/PayablesReceivables_Voucher.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/PayablesReceivables_Voucher_Detail.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/PayablesReceivables_Voucher_DetailHeader.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/PayablesReceivables_Voucher_budgetitem.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/Printcheckpayments.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/Printcheckpayments_PICHINCHA.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/Printcheckpayments_PRODUBANCO.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/Printcheckpayments_PRODUBANCO_Vial.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/finances/Rpt_SalesReportByLineRepresent.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/inout/RptM_InOut_new.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/inout/RptM_Inount_Movement.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/inout/RptM_RMInOut.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/inout/RptM_RMInOut_Lines.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/inout/RptSescr_MaterialReturnStandard.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/inout/Rptm_InOut_Lines_new.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/journal/RptSescr_ManualJournalEntries.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/meetings/ReportMeetings.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/order/C_OrderJR_new.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/order/C_OrderLinesJR_new.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/order/C_OrderLinesTaxIncludedJR_new.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/order/CustomOrdenServicio.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/order/RptC_Order_TaxLines.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/order/RptC_Order_TaxLines_new.jrxml`
- `src/ec/com/sidesoft/custom/reports/ad_reports/estandar/warehouse/RptM_Movement.jrxml`
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

El módulo contiene varias clases Java que gestionan la lógica de impresión y generación de reportes, permitiendo así un control más refinado sobre cómo se gestionan y despliegan estos en la aplicación. La clase 'SescrPrintServiceOrder', por ejemplo, maneja la solicitud de impresión de órdenes de servicio, utilizando un enfoque basado en servlet para procesar las peticiones del usuario.

> *Párrafos refinados con IA (`--with-ai`). Las tablas inferiores se regeneran desde XML/SQL.*


## Technical

Paquete: `ec.com.sidesoft.custom.reports`.

<!-- knowledge-extract:java_classes -->
| Clase | Carpeta | Extiende / implementa | Rol inferido | Ruta |
| --- | --- | --- | --- | --- |
| `GenerateRandomCode` | ad_process | — | Proceso / informe Java | `src/ec/com/sidesoft/custom/reports/ad_process/GenerateRandomCode.java` |
| `SescrPrintServiceOrder` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/custom/reports/ad_process/SescrPrintServiceOrder.java` |
| `Sescr_ReportPrintCheckPayments` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/custom/reports/ad_process/finances/Sescr_ReportPrintCheckPayments.java` |
| `Sescr_ReportPrintManualJournalEntries` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/custom/reports/ad_process/manualjournalentries/Sescr_ReportPrintManualJournalEntries.java` |
| `Sescr_ReportPrintGoodsMovements` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/custom/reports/ad_process/warehouse/Sescr_ReportPrintGoodsMovements.java` |
| `Sescr_ReportPrintGoodsMovementsStandard` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/custom/reports/ad_process/warehouse/Sescr_ReportPrintGoodsMovementsStandard.java` |
| `Sescr_ReportPrintWithholding` | ad_process | HttpSecureAppServlet | Proceso / informe Java | `src/ec/com/sidesoft/custom/reports/ad_process/withholdings/Sescr_ReportPrintWithholding.java` |
<!-- /knowledge-extract:java_classes -->

# 45 — Validaciones y callouts

## Functional

Matriz consolidada de reglas (UI, BD, Java). Ampliar condiciones en lenguaje natural si hace falta.

## Technical

<!-- knowledge-extract:validations -->
| Origen | Entidad / tabla | Condición / disparador | Efecto / mensaje |
| --- | --- | --- | --- |
| AD_VAL_RULE | — | `Validate Table DocType` | `C_DOCTYPE.AD_TABLE_ID = @AD_TABLE_ID@` |
| Función PL `sescr_cnvrt_numtoletters_usa` | — | invocación proceso | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas = ' || v_armar_texto_d; |
| Función PL `sescr_convert_numbertoletters` | — | invocación proceso | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test); |
| Función PL `sescr_get_label_trl` | — | invocación proceso | Se crean ElseIf para que si ya evaluó un típo no tenga que evaluar los otros. |
| Función PL `sescr_getdocument_invoice` | — | invocación proceso | left join c_order co on co.c_order_id = col.c_order_id |
<!-- /knowledge-extract:validations -->

# Technical — database triggers and functions

## Functional

El uso de funciones PL/pgSQL es importante para el soporte del módulo, ya que permiten realizar operaciones complejas y validaciones al momento de generar reportes. Aunque no hay triggers en este módulo, las funciones están diseñadas para optimizar el rendimiento y la integración con las funciones de la base de datos de Openbravo, facilitando así el manejo de datos.

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
| `sescr_bpartnerlocation` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_BPARTNERLOCATION.xml` |
| `sescr_cnvrt_numtoletters_usa` | — | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayo… | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas = ' || v_armar_texto_d;; RAISE NOTICE '%','RESULT mayor a 200 v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 200 vTexto2 = ' || vTexto;; RAISE NOTICE '%','v_tnumero= ' || to_char(v_tnumero); | `model/functions/SESCR_CNVRT_NUMTOLETTERS_USA.xml` |
| `sescr_convert_numbertoletters` | — | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas… | RAISE NOTICE '%','RESULT v_tnumero = ' || to_char(i) || '=' ||to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_number_test = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas v_tnumero = ' || to_char(v_number_test);; RAISE NOTICE '%','RESULT mayor a 100 y menor a 900 solo centenas = ' || v_armar_texto_d;; RAISE NOTICE '%','RESULT v_tnumero >= 101 and v_tnumero <200 v_number_test = ' || to_char(v_tnumero);; RAISE NOTICE '%','RESULT v_tnumero >= 101 and v_tnumero <200 v_number_test = ' || vTexto ; | `model/functions/SESCR_CONVERT_NUMBERTOLETTERS.xml` |
| `sescr_cost_at_date` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_COST_AT_DATE.xml` |
| `sescr_date_multilanguage` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_DATE_MULTILANGUAGE.xml` |
| `sescr_datebirthday` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_DATEBIRTHDAY.xml` |
| `sescr_get_costcentertrans` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GET_COSTCENTERTRANS.xml` |
| `sescr_get_label_trl` | — | Se crean ElseIf para que si ya evaluó un típo no tenga que evaluar los otros. | Se crean ElseIf para que si ya evaluó un típo no tenga que evaluar los otros. | `model/functions/SESCR_GET_LABEL_TRL.xml` |
| `sescr_get_payment_concat` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GET_PAYMENT_CONCAT.xml` |
| `sescr_get_tax_concat` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GET_TAX_CONCAT.xml` |
| `sescr_getall_costcenter` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GETALL_COSTCENTER.xml` |
| `sescr_getdocument_invoice` | — | left join c_order co on co.c_order_id = col.c_order_id | left join c_order co on co.c_order_id = col.c_order_id | `model/functions/SESCR_GETDOCUMENT_INVOICE.xml` |
| `sescr_getlastcost` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GETLASTCOST.xml` |
| `sescr_getlastpurchaserate` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GETLASTPURCHASERATE.xml` |
| `sescr_getmaxdateofpricelist` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GETMAXDATEOFPRICELIST.xml` |
| `sescr_getprodpricelistsales` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GETPRODPRICELISTSALES.xml` |
| `sescr_getuser` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GETUSER.xml` |
| `sescr_getvalue` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_GETVALUE.xml` |
| `sescr_monthtoletters` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_MONTHTOLETTERS.xml` |
| `sescr_returndocumentno` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_RETURNDOCUMENTNO.xml` |
| `sescr_returntax` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_RETURNTAX.xml` |
| `sescr_transprocessdeposit` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_TRANSPROCESSDEPOSIT.xml` |
| `sescr_transprocesspayment` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_TRANSPROCESSPAYMENT.xml` |
| `sescr_years_month` | — | Rutina PL/pgSQL del módulo (ver cuerpo en XML). | — | `model/functions/SESCR_YEARS_MONTH.xml` |
<!-- /knowledge-extract:functions -->

Revise cada XML en `src-db/database/model/` para el cuerpo exacto.

# 55 — Matriz botón / acción → proceso → código

## Functional

Una fila por acción ejecutable registrada en `AD_PROCESS` del módulo. Completar acciones solo-JS o de módulos dependientes manualmente.

## Technical

<!-- knowledge-extract:button_matrix -->
| # | UI / botón (es_ES) | VALUE | Tipo | Implementación | Reporte (S/N) | Resultado (resumen) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | GENERIC - PARTIAL PAYMENT DETAIL | `GENERIC - PARTIAL PAYMENT DETAIL` | Reporte | Java `Sescr_ReportPrintPayrollPartialPayment` | S | Servlet de informe `Sescr_ReportPrintPayrollPartialPayment` (fuente no en `src/` del módulo). |
| 2 | GENERIC - PRINT GOODS MOVEMENTS | `GENERIC - PRINT GOODS MOVEMENTS` | Reporte | Java `Sescr_ReportPrintGoodsMovements` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 3 | GENERIC - PRINT WITHHOLDING | `GENERIC - PRINT WITHHOLDING` | Reporte | Java `Sescr_ReportPrintWithholding` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 4 | GENERIC PRINT CHECK PAYMENT | `GENERIC PRINT CHECK PAYMENT` | Reporte | Java `Sescr_ReportPrintCheckPayments` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 5 | GENERIC STANDARD - PRINT GOODS MOVEMENTS | `GENERIC STANDARD - PRINT GOODS MOVEMENTS` | Reporte | Java `Sescr_ReportPrintGoodsMovementsStandard` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |
| 6 | Print Custom Order Service | `SescrPrintServiceOrder` | Reporte | Java `SescrPrintServiceOrder` | S | Genera PDF desde JRXML `ec/com/sidesoft/custom/reports/ad_reports/CustomOrdenServicio.jrxml`; contexto sesión `—`. |
| 7 | PRINT GENERIC - REPORT JOURNAL | `PRINT GENERIC - REPORT JOURNAL` | Reporte | Java `Sescr_ReportPrintManualJournalEntries` | S | Genera PDF desde JRXML `—`; contexto sesión `—`. |

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

Módulo: `ec.com.sidesoft.custom.reports`.

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

# Glosario — prefijo `SESCR`

## Siglas y prefijos

| Término | Significado |
| --- | --- |
| `SESCR` | Prefijo de tablas/columnas del módulo (`AD_MODULE_DBPREFIX`) |
| `ec.com.sidesoft.custom.reports` | Carpeta del módulo en el repositorio |

## Procesos (VALUE)

- `Sescr_ReportSalesRepresentative` — Reporte de ventas por línea con representante de ventas
- `GENERIC - PARTIAL PAYMENT DETAIL` — GENERIC - PARTIAL PAYMENT DETAIL
- `GENERIC - PRINT GOODS MOVEMENTS` — GENERIC - PRINT GOODS MOVEMENTS
- `GENERIC - PRINT WITHHOLDING` — GENERIC - PRINT WITHHOLDING
- `GENERIC PRINT CHECK PAYMENT` — GENERIC PRINT CHECK PAYMENT
- `GENERIC STANDARD - PRINT GOODS MOVEMENTS` — GENERIC STANDARD - PRINT GOODS MOVEMENTS
- `SescrPrintServiceOrder` — Print Custom Order Service
- `PRINT GENERIC - REPORT JOURNAL` — PRINT GENERIC - REPORT JOURNAL

## Sinónimos usuario ↔ técnico

Complete con el vocabulario de su organización (es_ES ↔ NAME/VALUE Openbravo).
