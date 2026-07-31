---
name: openbravo-modules
description: >-
  Answers questions about Openbravo Sidesoft modules in this repo: windows,
  menus, processes, errors, data model, Java/SQL. Discovers the right module
  from user text (screen names, package name, keywords) and reads that module's
  knowledge markdowns in docs/knowledge and docs_customization/knowledge
  (MANIFEST.json, INDEX.md). Hub skill linked from openbravo-functional-ticket-analysis
  and openbravo-operational-walkthrough. Use for ventana, menú, proceso, botón,
  no funciona, error, mensaje, Openbravo, fábrica de crédito, UAFE, formalidad,
  reportes, mantenimiento, factores, o cualquier carpeta ec.com.* / org.openbravo.*.
---

# Openbravo — conocimiento por módulo

Skill **hub** de documentación modular. Las skills de **análisis consultor** (`openbravo-functional-ticket-analysis`) y **guía operativa** (`openbravo-operational-walkthrough`) **deben invocar esta skill** antes de concluir veredictos o redactar pasos en pantalla.

---

## 1. Descubrir módulos con documentación

Desde la **raíz del repo**, localiza **ambas** bases de conocimiento por módulo:

```bash
find . \( -path '*/docs/knowledge/MANIFEST.json' -o -path '*/docs_customization/knowledge/MANIFEST.json' \) -not -path './.git/*' | sort
```

| Ruta | Rol |
| --- | --- |
| `{M}/docs_customization/knowledge/` | **Prioridad Unnoparts** — personalización del proyecto, escenarios de soporte, reglas de negocio del cliente |
| `{M}/docs/knowledge/` | Inventario técnico del módulo (ventanas, procesos, triggers, modelo) |

Un mismo módulo `{M}` puede tener **solo `docs`**, **solo `docs_customization`**, o **ambos**. Si existen los dos, **leer siempre los dos**; la personalización complementa o prevalece sobre el inventario base para veredicto y guía operativa.

Cada knowledge root es independiente. El campo `module` y `display_name` están en su `MANIFEST.json`.

Carpetas `*.es_ES` y `*.template` **no** tienen knowledge propio: las etiquetas en español viven en el módulo de traducción; la lógica en el módulo base.

---

## 2. Elegir el módulo correcto

1. Si el usuario nombra un **paquete Java** o carpeta (`ec.com.sidesoft…`, `org.openbravo…`), usar ese módulo.
2. Si no, abrir **`MANIFEST.json`** de cada candidato (en `docs_customization/knowledge/` primero, luego `docs/knowledge/`) y comparar `entrypoints[].keywords`, `topics[].keywords` y `example_user_queries`.
3. Leer **`INDEX.md`** del módulo elegido (sección *handoff* / módulos hermanos) y saltar al otro knowledge root o módulo relacionado si la pregunta cruza cotización, tesorería, FE, etc.
4. Preguntas amplias de **fábrica de crédito / operaciones / COM / buró**: empezar en `ec.com.sidesoft.credit.factory` o `ec.com.sidesoft.unnoparts.credit.factory`; derivar a hermanos según `INDEX.md`.
5. Si ningún MANIFEST encaja, buscar en código del módulo más probable (`AD_WINDOW`, procesos) y sugerir generar docs con `generate_module_docs.py`.

### Módulos frecuentes por dominio (Unnoparts)

| Dominio | Módulos a revisar (entre otros) |
| --- | --- |
| NC / factura referenciada | `ec.com.sidesoft.creditNoteRefenence`, `ec.com.sidesoft.saleorder.relations`; `ec.com.sidesoft.financialcreditnote.sales.auto` (verificar `src-db` — en Unnoparts suele ser solo `docs/`) |
| Plan de pagos / cuotas | `org.openbravo.advpaymentmngt`, `ec.com.sidesoft.payment.plan.info`, `ec.com.sidesoft.payment.schedule`, `ec.com.sidesoft.postdated.check` |
| Cobros detallados | `ec.com.sidesoft.detailed.paymentin` |
| FE Ecuador | `ec.cusoft.facturaec` |
| Pre-cancelación / acuerdos | `ec.com.sidesoft.pre.cancellations`, `ec.com.sidesoft.payment.agreement` |
| Crédito / cotización | `ec.com.sidesoft.fast.quotation`, `ec.com.sidesoft.unnoparts.credit.factory` |

Actualizar con el comando `find` si hay más módulos documentados.

---

## 3. Orden de lectura (por módulo y knowledge root)

Sustituye `{M}` por la carpeta del módulo y `{K}` por `docs_customization` o `docs`.

**Regla de prioridad entre roots:** si existen ambos, recorrer **`docs_customization/knowledge/` completo primero**, luego **`docs/knowledge/`** para lo que falte (pestañas, IDs técnicos, inventario de triggers).

| Prioridad | Archivo | Cuándo |
| --- | --- | --- |
| 1 | `{M}/{K}/knowledge/01-user-chat-guide.md` | Usuario final, soporte, “no funciona”, escenarios reales |
| 2 | `{M}/{K}/knowledge/20-functional-windows-menus.md` | Ventanas, menús, rutas UI |
| 3 | `{M}/{K}/knowledge/30-functional-processes.md` | Botones, procesos, validaciones frecuentes |
| 4 | `{M}/{K}/knowledge/22-window-specifications.md` | Campos visibles, pestañas, secuencias |
| 5 | `{M}/{K}/knowledge/25-functional-key-windows.md` | Solo si existe (ventanas clave) |
| 6 | `{M}/{K}/knowledge/35-messages-and-errors.md` | Mensajes popup, errores AD_MESSAGE |
| 7 | `{M}/{K}/knowledge/45-validations-and-callouts.md` | Callouts, reglas de validación UI |
| 8 | `{M}/{K}/knowledge/55-button-process-matrix.md` | Matriz botón → implementación |
| 9 | `{M}/{K}/knowledge/10-domain-data-model.md` | Entidades, tablas, relaciones |
| 10 | `{M}/{K}/knowledge/50-technical-db-triggers-functions.md` | Triggers/funciones PL (análisis consultor L2) |
| 11 | `{M}/{K}/knowledge/glossary-*.md` | Siglas del módulo |
| 12 | `{M}/{K}/knowledge/40`–`60` o código citado en esos docs | Depuración técnica |

Routing máquina: `{M}/{K}/knowledge/MANIFEST.json` (`entrypoints`, `topics`).

---

## 4. Verificación en código del repo (obligatoria para guías y UI)

Los markdowns de `docs/knowledge/` pueden describir funcionalidad de módulos **no desplegados** en Unnoparts (solo carpeta `docs/` sin `src-db/`). **No basta leer markdown** para afirmar que un botón existe en pantalla.

### 4.1 ¿El módulo está en el proyecto?

| Señal en `modules/{M}/` | Interpretación |
| --- | --- |
| Existe `src-db/database/sourcedata/` o `src/` | Módulo con artefactos desplegables en este repo |
| Solo `docs/` o `docs/knowledge/` | **Documentación sin código** — no citar botones/procesos de ese módulo en guías operativas salvo confirmación explícita en BD del entorno |

Comando rápido:

```bash
test -d "modules/{M}/src-db/database/sourcedata" && echo "codigo: SI" || echo "codigo: NO"
```

### 4.2 Confirmar botón, campo o proceso en ventana

Para cada elemento UI que vaya a la guía operativa (botón, campo de cabecera, pestaña):

1. Localizar en **`modules/{M}/src-db/database/sourcedata/AD_FIELD.xml`** (o core `src-db/...`) el `NAME` / columna y el `AD_TAB_ID` de la ventana destino.
2. Si es proceso de botón: **`AD_COLUMN.xml`** → `AD_PROCESS_ID` → **`AD_PROCESS.xml`** + clase Java en `src/` si aplica.
3. Etiqueta **es_ES**: `{M}.es_ES/referencedata/translation/AD_*_TRL_es_ES.xml`.
4. Cruzar con markdown (`22-window-specifications.md`, `30-functional-processes.md`) — el markdown orienta; **el código confirma**.

Búsquedas útiles (raíz del repo):

```bash
# ¿Existe el botón en algún módulo con código?
rg -l "Generate NC|Generar NC" modules/*/src-db/database/sourcedata/AD_FIELD.xml

# ¿Campo en pestaña Factura venta (Header = 263)?
rg "AD_TAB_ID.*263" modules/{M}/src-db/database/sourcedata/AD_FIELD.xml
```

### 4.3 Matriz interna antes de redactar guía

Completar mentalmente o en borrador (no obligatorio en respuesta al usuario):

| Elemento UI (es_ES) | Módulo | En markdown | En `src-db` repo | ¿Incluir en guía? |
| --- | --- | --- | --- | --- |
| … | … | Sí/No | Sí/No | Solo si **En src-db = Sí** |

**Reglas:**

- Markdown **Sí** + código **No** → **excluir** de la guía; usar flujo alternativo que **sí** esté en código (otro módulo o core).
- Código **Sí** + markdown **No** → incluir citando `AD_FIELD` / traducción; no inventar nombre.
- Varios módulos del mismo dominio: priorizar el que tenga **código en repo** (`creditNoteRefenence` vs `financialcreditnote.sales.auto` para NC manual).

### 4.4 Ejemplo Unnoparts — NC parcial

| Elemento | Módulo | Código en repo |
| --- | --- | --- |
| **Generar NC** (botón) | `financialcreditnote.sales.auto` | **No** (solo `docs/knowledge/`) |
| **Referencia Factura** / **Factura Refenciada** | `creditNoteRefenence` | **Sí** (`AD_FIELD` tab 263) |
| **Añadir Cobro/Pago** | `org.openbravo.advpaymentmngt` | **Sí** (`AD_FIELD` tab 263) |
| **Plan de pagos** (pestaña) | `org.openbravo.advpaymentmngt` | **Sí** |

---

## 5. Uso desde otras skills (encadenamiento)

### Desde `openbravo-functional-ticket-analysis`

1. Tras normalizar el ticket (Paso 0 / 0B), identificar **1–4 módulos** candidatos con esta skill.
2. Leer markdowns según §3 **antes** del veredicto final.
3. Reflejar hallazgos en:
   - **Sección 3–4:** capacidades, limitaciones, flujos alternativos del proyecto.
   - **Sección 5D:** módulos consultados + bullets de evidencia (proceso, trigger, mensaje).
   - **Sección 7:** workaround alineado con lo documentado en `01-user-chat-guide.md` / `30-functional-processes.md`.
4. **Prohibido** concluir solo con core Openbravo si existe markdown de personalización que contradice o restringe el flujo.

### Desde `openbravo-operational-walkthrough`

1. Partir del análisis previo (sección 7) **y** de los módulos listados en su sección 5D.
2. Leer markdowns (§3) de cada módulo aplicable (priorizar `docs_customization`).
3. **Aplicar §4 (verificación en código)** a cada botón, campo y proceso antes de incluirlo en pasos.
4. Usar en la guía **solo** elementos con **código confirmado** en `modules/*/src-db/` o `src-db/` core:
   - Nombres **es_ES** desde traducciones o markdown alineado al `AD_FIELD`.
   - Mensajes de **`35-messages-and-errors.md`** del módulo que tenga el proceso.
5. Flujo alternativo en markdown: incluir como **Opción A / B** únicamente si **ambas** rutas tienen artefactos en código; si solo una existe, **un solo flujo** sin opciones ficticias.

---

## 6. Regenerar documentación

Desde la raíz del repo, para el módulo `{M}`:

```bash
python3 generate_module_docs.py {M} --refresh-only
```

Equivalente local (si existe): `python3 {M}/docs/knowledge/scripts/extract_knowledge_tables.py`

Scaffold nuevo: `python3 generate_module_docs.py {M} --init`

Tras cambios de código en un módulo Unnoparts, actualizar **`docs/knowledge/`** y, si aplica, **`docs_customization/knowledge/`** del mismo módulo (ver regla `.cursor/rules/openbravo-modules.mdc`).

---

## 7. Salida esperada al invocar esta skill

Cuando otra skill o el usuario pida contexto modular, devolver internamente (o resumir en la respuesta técnica):

| Elemento | Contenido |
| --- | --- |
| Módulos consultados | Lista `{M}` + root (`docs` / `docs_customization`) + **¿tiene `src-db`?** |
| Ventanas / menús | Desde `20-*` y `22-*`, confirmados en `AD_FIELD` / `AD_TAB` |
| Procesos / botones | Desde `30-*` y `55-*`, **filtrados por §4** |
| Excluidos (solo docs) | Elementos en markdown sin código en repo — no van a guía operativa |
| Restricciones de negocio | Desde `01-*`, triggers en `50-*`, mensajes en `35-*` |
| Handoff | Otros módulos enlazados desde `INDEX.md` |

---

## Recursos

- Análisis consultor: skill `openbravo-functional-ticket-analysis`
- Guía operativa: skill `openbravo-operational-walkthrough`
- Disciplina de docs al editar código: `.cursor/rules/openbravo-modules.mdc`
