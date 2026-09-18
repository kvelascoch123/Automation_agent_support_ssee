---
name: openbravo-functional-ticket-analysis
description: >-
  Analiza tickets e incidencias funcionales de Openbravo ERP, y consultas de viabilidad
  ("¿el sistema permite…?", "¿existe la posibilidad de…?"): normaliza el texto libre,
  clasifica el caso, explora el repo de código del cliente (graphify-out/ y código fuente) para
  identificar módulos y reglas de personalización, valida core + personalizaciones,
  desglosa en sub-capacidades y entrega veredicto SÍ/NO/PARCIAL con workaround operativo.
  Encadena con openbravo-operational-walkthrough para GUIA OPERATIVA. No usar para
  desarrollo puro, creación de módulos o BDC.
---

# Análisis de tickets funcionales Openbravo

## Activación

Ejecutar esta skill cuando el usuario:

- reporte un **error funcional**, **incidencia** o **ticket de soporte** en Openbravo, o
- use disparadores: `ANALIZA TICKET`, `analizar ticket`, `analizar caso`, `ticket funcional`, `incidencia funcional`, o
- describa síntomas operativos: no funciona, no concilia, no deja, falla, error en pantalla, pasos para reproducir, mensaje popup, captura de error, o
- formule una **consulta de viabilidad / capacidad funcional** sobre un flujo del ERP, por ejemplo:
  - «¿Existe la posibilidad de…?», «¿El sistema permite…?», «¿Se puede… en Openbravo?»
  - «Necesito saber si…», «¿Cómo se hace…?» (cuando el foco es **si es posible** y **cómo operarlo**, no desarrollo)
  - Pregunta directa con contexto de negocio: documento, plan de pagos, cuotas, conciliación, FE, devolución, etc.

**No activar** si el usuario pide solo: desarrollar código, crear módulo/ventana, compilar, versionamiento git, o análisis exclusivo con **BDC** (priorizar skill BDC en ese caso).

---

## Detección de subtipo (obligatorio, antes de analizar)

| Subtipo | Señales | Flujo principal |
|---------|---------|-----------------|
| **A. Incidencia / error** | Falla, mensaje de error, no deja guardar, inconsistencia con documento concreto | Pasos 0-A → 0 → 1 → 2 → 4 (formato incidencia) |
| **B. Consulta de viabilidad** | «¿Existe…?», «¿Se puede…?», sin síntoma de fallo; pregunta por capacidad o procedimiento | Pasos 0B → 1B → 2B → 4B (formato viabilidad) |

Si la consulta mezcla ambos (ej. «¿se puede hacer X?» y «me sale error Y»), aplicar **ambos** flujos: primero viabilidad, luego incidencia sobre el error.

---

## Paso 0-A — Evaluar suficiencia de contexto (obligatorio, subtipo Incidencia)

Antes de normalizar y analizar, evaluar si el ticket trae los **5 mínimos funcionales**:

| # | Mínimo funcional | Pregunta que responde |
|---|---|---|
| 1 | **Módulo y documento** | ¿Es factura de venta/compra, retención, pago, ajuste de inventario, asiento, nómina…? ¿Qué número/tipo de documento? |
| 2 | **Acción exacta** | ¿Qué estaba haciendo el usuario cuando falló? (contabilizar, anular, reactivar, procesar, generar XML…) |
| 3 | **Síntoma literal** | ¿Mensaje de error textual, código, o comportamiento observado? "No funciona" no es un síntoma. |
| 4 | **Resultado esperado vs. obtenido** | ¿Qué debía pasar y qué pasó en su lugar? |
| 5 | **Alcance y entorno** | ¿Un documento puntual o todos? ¿Producción? ¿Desde cuándo? ¿Qué cliente/alias de BD? |

**Decisión:**
- **Faltan 2 o más** → contexto insuficiente. En uso interactivo (consultor en Cursor), generar entre 3 y 8 preguntas concretas orientadas a cerrar exactamente los mínimos ausentes (usar el mapa 5B para identificar el módulo probable y afinar las preguntas) y presentarlas al usuario antes de seguir. En uso automático vía `triage-glpi-auto`, esta es la misma evaluación que aplica el Paso 4.3 de ese orquestador — no se repite ahí como un chequeo aparte, es este mismo paso.
- **Faltan 0 o 1** → contexto suficiente. Continuar a Paso 0, señalando igual el dato faltante en la sección 9 del documento final.

---

## Paso 0 — Normalizar entrada: incidencia (obligatorio)

Antes de analizar, **reestructura mentalmente** (no mostrar al usuario salvo que falten datos críticos) el texto libre en esta plantilla:

```markdown
=== TICKET NORMALIZADO (INCIDENCIA) ===
ID/Título: {inferir o "No indicado"}
Módulo/Ventana/Proceso: {inferir de pantalla, menú o proceso mencionado}
Organización: {si aplica}
Descripción del problema: {texto del usuario}
Resultado esperado: {inferir o marcar "No indicado"}
Resultado actual: {síntoma / error}
Mensaje de error exacto: {popup, log o "No indicado"}
Pasos para reproducir: {lista o "No indicados"}
Documentos/datos clave: {nº doc, importes, fechas, refs, terceros, cuentas}
Evidencia: {capturas, CSV, XML adjuntos}
Hipótesis del usuario: {si la menciona}
Restricciones: {contabilizado, conciliado, ambiente, urgencia}
```

Extrae del texto todo lo disponible. **No inventes** IDs, importes ni mensajes no evidenciados.

---

## Paso 0B — Normalizar entrada: consulta de viabilidad (obligatorio)

Desglosa la pregunta del usuario en capacidades concretas antes de buscar en código:

```markdown
=== CONSULTA NORMALIZADA (VIABILIDAD) ===
Pregunta en una línea: {resumen}
Dominio ERP: {ventas | tesorería | compras | inventario | FE | crédito | POS | integración | otro}
Operación de negocio: {qué quiere lograr en lenguaje de negocio}
Documentos / entidades involucradas: {factura, NC, cobro, pedido, plan de pagos, etc.}
Alcance solicitado:
  - ¿Emitir / crear el documento? (Sí/No/No indicado)
  - ¿Aplicar / impactar otro documento o plan? (Sí/No/No indicado)
  - ¿De forma automática al completar? (Sí/No/No indicado)
  - ¿Parcial (por línea, cuota, importe)? (Sí/No/No indicado)
Restricciones de instalación inferidas: {cobranza secuencial, FE Ecuador, financiamiento, etc.}
Resultado esperado del usuario: {inferir}
Datos del caso: {documentos, importes, cuotas — o "No indicados"}
```

**Regla de desglose:** una pregunta amplia suele ocultar **2–4 sub-preguntas**. Ejemplo:

> «¿NC al cliente afectando el plan de pagos parcialmente por cuota?»

Se desglosa en:

1. ¿Se puede **emitir** NC al cliente?
2. ¿Se puede **impactar** el plan de pagos de la factura origen?
3. ¿Ese impacto puede ser **parcial**?
4. ¿Puede hacerse **por cuota** (y no solo a nivel cabecera)?

Cada sub-pregunta debe recibir veredicto propio antes del veredicto global.

---

## Paso 1 — Clasificar el caso (incidencia)

| Tipo | Indicadores |
|------|-------------|
| **Operativo** | Proceso mal usado, documento incorrecto, flujo de negocio invertido |
| **Configuración** | Maestros, permisos, parámetros, conceptos contables, tipos de documento |
| **Integración/datos** | Importación CSV/XML, WS, archivos externos |
| **Bug/desarrollo** | Comportamiento contradice lógica estándar documentada en código |
| **Infraestructura** | Solo si hay evidencia: OOM, timeout, lentitud, caídas |

Indica **confianza** (Alta/Media/Baja) y si **requiere desarrollo** (Sí/No/Por confirmar).

---

## Paso 1B — Clasificar consulta de viabilidad

| Tipo | Indicadores |
|------|-------------|
| **Viabilidad operativa** | «¿Se puede hacer X?» — procedimiento estándar o workaround |
| **Viabilidad con personalización** | Core permite algo pero el proyecto tiene reglas/triggers que lo restringen |
| **Configuración previa** | Depende de tipos de documento, parámetros, módulos activos |
| **No implementado / requiere desarrollo** | No hay ventana, proceso ni lógica en el repo |
| **Fuera de alcance ERP** | Proceso que corresponde a otro sistema o manual externo |

Indica **confianza** y **requiere desarrollo** (Sí/No/Por confirmar).

---

## Paso 2 — Análisis técnico (incidencia)

1. Identificar **síntoma** vs **causa raíz** (no confundir).
2. Separar **dos capas** cuando ambas existan (obligatorio antes de redactar §7):
   - **Capa negocio / proceso:** documento, flujo o concepto contable incorrecto (ej. devolución de anticipo registrada como cobro negativo en lugar de salida de banco / pago reintegrado con concepto de anticipos).
   - **Capa operativa / síntoma:** por qué falla en pantalla hoy (ej. depósito y reintegro con el mismo importe en signos opuestos → conciliación duplica el valor).
   - No reducir la §7 solo a la capa operativa si la evidencia muestra también error de proceso documental.
3. Ubicar **punto de fallo**: ventana, botón, proceso, validación, matching, posting.
4. **Exploración obligatoria del repo del cliente:** identificar 1–4 módulos candidatos (por dominio/keywords, ver mapa 5B) y explorar directamente el repo de código de ese cliente para esos módulos — vía `graphify-out/` y código fuente (Java, SQL/XML functions, AD_*), siguiendo el procedimiento del Paso 5A — antes de concluir.
5. Diferenciar: error del **usuario/proceso** vs **defecto del sistema** vs **dato maestro**.
6. Antes de proponer solución: **¿el usuario usó el documento/proceso correcto según lo que confirma el código?**
7. **Comparación obligatoria contra pares — antes de cerrar cualquier diagnóstico, incluida la conclusión de "no hay error" o "es el comportamiento esperado".**
   **Disparador automático — no depende de que el análisis "sospeche" configuración.** Si el síntoma del ticket coincide con alguno de estos patrones, clasificar la hipótesis como registro-maestro-anómalo **por defecto** y entrar directo al procedimiento de este punto, sin esperar a que otra evidencia lo sugiera primero: "no genera/arma/completa/aplica X automáticamente" (cuando X sí ocurre en otros documentos/flujos similares), "funciona para unos [tipos de documento / conceptos / sucursales] y para otros no", "antes funcionaba y ahora no" sin cambio de código reciente, o cualquier variante de "¿por qué aquí sí y allá no?". Estos patrones son la señal misma de una diferencia de configuración entre registros hermanos — no hace falta una pista adicional para activar la comparación.
   Distinguir el nivel correcto de comparación:
   - Si el síntoma se explica por el comportamiento de un **registro transaccional** (un pedido, una factura) siguiendo su propio flujo: comparar contra otros registros transaccionales similares mide **alcance**, pero no valida que la configuración que comparten esté bien — por definición, todos se comportarán "igual entre sí".
   - Si el síntoma puede explicarse por un **flag, parámetro o regla de un registro maestro/de configuración** (un tipo de documento, un concepto, un parámetro de módulo): la comparación obligatoria es contra **los registros maestros hermanos de la misma familia de negocio** (ej. los demás tipos de documento del mismo grupo), **nunca** contra las transacciones que usan esa configuración. Antes de aceptar una explicación de tipo "así funciona este flujo/documento", identificar primero qué registro de configuración específico controla ese comportamiento y compararlo contra sus hermanos — confirmar que el patrón es igual siempre para ese mismo registro **no es evidencia suficiente** para cerrar el caso.
   - **Esta comparación se ejecuta por consulta SQL a la BD de producción del cliente (`pg_query`, vía MCP-DB), no por `graphify-out/` ni por lectura de código.** `graphify` y el código fuente solo confirman que el campo/columna **existe** como parte de la definición del módulo (ej. una columna `EM_*` agregada por una extensión); el **valor** concreto de esa columna para cada registro maestro (ej. cada fila de `C_DocType`) vive únicamente en los datos de producción, cargados por implementación o configuración manual — nunca aparece en el repo de código. Cuando la causa candidata sea de este tipo, y esta sesión tenga acceso a `pg_query`/MCP-DB (disponible siempre que esta skill corre dentro del flujo automático de `triage-glpi-auto`, o si el consultor lo tiene conectado en Cursor): (1) identificar vía código/`graphify` **todos** los campos de configuración relevantes al síntoma reportado (no solo el primero que aparezca — ej. para "no genera el albarán automáticamente" son candidatos tanto `invoicerule`/`deliveryrule` del core como cualquier columna `EM_*` de extensión que controle generación automática de documentos), (1-bis) **buscar explícitamente, además de los campos core ya conocidos, si el módulo de personalización propio del cliente (patrón `ec.com.<cliente>.*`, `*.special.customization.*`, según `clientes.json`) agrega columnas de extensión (`EM_*`) sobre la misma tabla involucrada** (ej. `C_DocType`) — leyendo directamente los archivos XML de ese módulo en el repo (Application Dictionary / `AD_Column`), **nunca vía `graphify-out/`, que no indexa `.xml`**. No asumir que los únicos campos candidatos son los estándar de Openbravo que ya se conocen de memoria: la causa suele estar en una extensión propia del cliente que el grafo no muestra y que solo aparece leyendo el módulo de personalización directamente, (2) consultar por BD el valor de cada uno de esos campos para el registro del caso, (3) consultar los mismos campos para los demás registros de la misma familia/dominio, y (4) señalar explícitamente, **para cada campo comparado**, si el registro del caso es una excepción dentro de ese grupo. **No detenerse en el primer campo que arroja un resultado "coherente" o "esperado"** — si hay más de un campo de configuración plausible para el síntoma, compararlos todos y reportar el resultado de cada uno, aunque uno solo ya "confirme" una hipótesis; una diferencia real en un segundo campo (ej. otro flag que también se aparta del patrón de la mayoría de hermanos) es evidencia complementaria u otra causa candidata, no algo que se pueda omitir porque el primer campo ya cerró el caso. **Si esta sesión no tiene acceso a `pg_query`/MCP-DB**, no cerrar el caso como "comportamiento esperado" apoyado solo en código/graphify — declarar en sección 9 que la comparación de valores de configuración contra sus pares queda pendiente de verificación por BD, y bajar la confianza de la sección 1 en consecuencia.

**7-bis. Enumeración exhaustiva de campos candidatos — obligatoria y previa a comparar cualquier campo (no delegable a graphify ni a memoria).** El paso 1 y 1-bis de este punto piden identificar "todos los campos de configuración relevantes", pero identificar no es lo mismo que enumerar de forma verificable: `graphify-out/` puede no estar indexado (404), estar desactualizado, o simplemente no cubrir `.xml` de Application Dictionary, y la memoria del analista solo trae a la mesa el campo que ya conoce o el primero que aparece. Por eso, antes de elegir qué campo(s) comparar contra pares:

1. Identificar la tabla maestra involucrada en el síntoma (ej. `C_DocType`, `M_Product`, `C_BPartner`, `AD_Role`).
2. Si esta sesión tiene `pg_query`/MCP-DB, ejecutar sobre esa tabla **una introspección directa del esquema vivo** — `pg_describe_table` o `SELECT column_name FROM information_schema.columns WHERE table_name = '<tabla>'` — y de ese listado extraer **todas** las columnas con prefijo `EM_*` (extensiones de cualquier módulo de personalización, sin importar cuál las agregó). Esta fuente es independiente del repo: el valor y la existencia de la columna viven en la BD del cliente, no en `graphify-out/`, así que este paso **no depende de que el repo esté indexado, actualizado o accesible**.
3. Cuando `graphify` retorna 404/omitido o el repo no resuelve el módulo, este paso deja de ser un complemento y se vuelve la **única fuente válida** de candidatos — no se cierra el caso citando solo "graphify: OMITIDO" en sección 9 sin haber intentado la introspección por BD.
4. El resultado de este paso (lista completa de columnas `EM_*` encontradas en la tabla) es evidencia obligatoria de 5D, **antes** de reportar cuál de ellas se comparó y con qué resultado. Si la lista tiene 2+ columnas `EM_*` plausibles para el síntoma, todas se comparan contra pares (ver regla de "no detenerse en el primer campo" arriba) — ninguna se descarta de la comparación solo por parecer menos relacionada a primera vista.
5. Este método aplica a **cualquier** tabla maestra y **cualquier** ticket — no es un procedimiento especial para `C_DocType` ni para casos de tipo "Proformado"/despacho. Se ejecuta siempre que la causa candidata sea un flag/parámetro de un registro maestro, sin importar el dominio funcional del ticket.

Esto se hace siempre, no solo cuando ya se sospecha un problema de configuración: es un paso de verificación previo al cierre. El resultado (qué pares se revisaron — transaccionales o de configuración — y qué diferencias o coincidencias se encontraron) es evidencia obligatoria de la sección 5D.

---

## Paso 2B — Análisis de viabilidad (obligatorio)

### Checklist interno (responder antes de redactar)

1. **¿Qué capacidad exacta se pregunta?** (crear, aplicar, automatizar, parcial, por cuota/línea/documento)
2. **¿Qué dice el core Openbravo?** (módulos estándar: `org.openbravo.*`, APRM, etc.)
3. **¿Qué dice esta instalación (la del cliente resuelto en `clientes.json` para este ticket)?** Explorar directamente el repo de código de ese cliente para el módulo candidato — `graphify-out/` y código fuente (Java, funciones PL/SQL, `AD_*.xml`) — siguiendo el procedimiento del Paso 5A. Buscar ahí triggers/reglas propias del proyecto (`SSPCH_*`, `SSOREL_*`, extensiones `em_*`).
4. **¿Hay reglas de negocio que restrinjan el flujo?** (cobranza secuencial, FE obligatoria, estados de documento, etc.)
5. **Si NO es posible de forma directa:** ¿existe **workaround operativo** documentado o inferible en el proyecto?
6. **¿Hay flujo alternativo específico del proyecto?** (pre-cancelación, acuerdo de pago, cruce de anticipo, etc.)

### Regla crítica: Core vs personalización del proyecto

**Prohibido** concluir solo con comportamiento estándar de Openbravo.

| Nivel | Qué validar | Ejemplo de error a evitar |
|-------|-------------|---------------------------|
| Core | Documentos ARC, cobros, plan de pagos APRM | «Se puede aplicar crédito por cuota en cobro» |
| Proyecto | Triggers `SSPCH_*`, `SSOREL_*`, extensiones `em_*` | Sin revisar secuencia de cuotas en cobranza |
| Negocio | Workaround NC + nueva factura + cruce | Inventariar módulos sin dar procedimiento |

Prioridad de evidencia: **`graphify-out/` + código del proyecto** (repo del cliente) > comportamiento core genérico.

### Matriz de capacidades (obligatoria en consultas de viabilidad)

Construir internamente y reflejar en secciones 3–4:

| Sub-capacidad | Veredicto | Condición / evidencia |
|---------------|-----------|------------------------|
| {ej. Emitir documento} | Sí / No / Parcial | {tipo doc, módulo, config} |
| {ej. Impactar plan de pagos} | Sí / No / Parcial | {automático vs manual vs workaround} |
| {ej. Afectación parcial por cuota} | Sí / No / Parcial | {trigger secuencial, etc.} |

**Veredicto global:** sintetizar en **SÍ**, **NO**, **PARCIAL** o **SÍ CON CONDICIONES**, nunca ambiguo.

### Enrutamiento por dominio ERP

Usar para focalizar la búsqueda en código y docs (aplica a **cualquier** flujo, no solo tesorería):

| Dominio | Palabras clave del usuario | Dónde buscar primero |
|---------|---------------------------|----------------------|
| Ventas / facturación | factura, NC, ND, devolución, pedido | `saleorder.relations`, `facturaec`, `C_Invoice`, ARC/ARI |
| Tesorería / cobros | cobro, pago, plan de pagos, cuota, conciliación | `advpaymentmngt`, `detailed.paymentin`, `payment.plan.info`, `postdated.check` |
| Compras | factura proveedor, retención, liquidación | `withholdings`, `APC`, proveedor |
| Inventario / logística | albarán, movimiento, stock | `M_InOut`, `M_Movement`, módulos logísticos `ec.com.*` |
| FE Ecuador | SRI, autorización, XML, electrónico | skill `ob-fe-eei-invoicelog-analysis`, `ec.cusoft.facturaec` |
| Crédito / cotización | cuota, financiamiento, entrada, amortización | `fast.quotation`, `credit.operation.request`, `order.interest`, `credit.factory` |
| Pre-cancelación / cartera | liquidación anticipada, anticipo | `pre.cancellations` |
| Acuerdos / mora | interés mora, nota débito, redistribución | `debitnote.interest.due`, `payment.agreement` |
| POS / retail | TPV, ticket, caja | regla `openbravo-pos`, `retail.*` |
| Integraciones | WS, Magento, importación | `integration.*`, `webservices` |

Si el dominio no está claro, declararlo en sección 9 y bajar confianza a **Media/Baja**.

---

## Paso 3 — Reglas de conducta

- Audiencia global: **técnico funcional / consultor de soporte** (secciones 1–6 y 8–9).
- Audiencia sección 7: **usuario final / área operativa** — lenguaje claro, sin jerga técnica ni SQL.
- No proponer cambios de código ni compilación salvo que el caso lo exija y esté justificado.
- No ejecutar `update.sh` / `smartbuild.sh` sin confirmación explícita (regla openbravo-build).
- Priorizar precisión sobre extensión.
- Si hay varias causas, ordenar por probabilidad e indicar cómo descartarlas.
- **Descuadres contables (asientos, cuentas mal asignadas, conciliación con diferencia):** la verificación en BD de producción (Paso 5A + `pg_query`) es siempre obligatoria antes de cerrar el diagnóstico — nunca cerrar un caso contable solo con conocimiento estático o lectura de código, aunque el síntoma parezca claro.
- Al proponer revertir un flujo A→B→C (ej. descontabilizar antes de reactivar), siempre en orden inverso: primero C, luego B, luego A.
- Retenciones en Ecuador (fuente e IVA): tributariamente sensibles — máxima precaución, respaldo en ATS antes de sugerir corrección, y escalar si hay duda en vez de asumir.
- **Disciplina SQL contra la BD de producción del cliente (`pg_query`/MCP-DB), siempre:** solo `SELECT` — nunca `INSERT`/`UPDATE`/`DELETE`/`DDL` ejecutado por este análisis. Siempre `WHERE` con filtros precisos (organización, cliente, fechas, ID de documento) y `LIMIT` en tablas de alto volumen (`Fact_Acct`, `C_Invoice`, `C_Payment`, `M_Transaction`, `C_AllocationLine`, `C_BankStatementLine`, y sus equivalentes en minúscula del modelo físico). Si el resultado es extenso, resumir — no volcar tablas completas en ningún comentario o respuesta. Un script correctivo que sí requiera escritura se entrega siempre como texto sugerido para ejecución manual (ver Paso 6-B de `triage-glpi-auto` en modo automático, o directo al consultor en modo interactivo) — nunca ejecutado por esta skill.

### Separación obligatoria: consultor vs usuario final

| Sección | Audiencia | Contenido permitido |
|---------|-----------|---------------------|
| **5–6** | Consultor / soporte técnico | SQL, IDs, código, parches BD, escalamiento a desarrollo |
| **7** | Usuario final (copiable) | Lenguaje de negocio, veredicto claro, workaround operativo, pasos numerados |

**Prohibido en la sección 7:** SQL, tablas, IDs técnicos, parches para forzar datos.

### Prioridad de redacción según subtipo

| Subtipo | Sección 7 debe priorizar |
|---------|--------------------------|
| Incidencia | **Qué se identificó** (1 frase) + **por qué está mal** (proceso de negocio primero, síntoma en pantalla después si aplica) + flujo correcto + corrección inmediata y prevención |
| Viabilidad | **Respuesta directa SÍ/NO/PARCIAL en prosa** + **Por qué** narrativo + **procedimiento numerado** |

En consultas de viabilidad:
- La **matriz de sub-capacidades** (Sí/No/Parcial) va **solo en secciones 3–5** para el consultor.
- La **sección 7 no debe listar** «Detalle por capacidad 1, 2, 3…» salvo que el usuario pida explícitamente un desglose técnico para otro consultor.
- La sección 7 debe leerse como un **correo o ticket de soporte**: primera línea responde la pregunta; el usuario entiende qué puede y qué no puede hacer **sin contar ítems**.

En consultas de viabilidad, la sección 7 debe poder copiarse **tal cual** en un ticket de soporte (estilo consultor funcional), no solo como apéndice técnico.

---

## Paso 4 — Formato de respuesta: incidencia

Entregar **siempre** en este orden:

```markdown
## 1) Clasificación del caso
- Tipo: ...
- Subtipo: Incidencia
- Confianza: ...
- ¿Requiere desarrollo?: ...

## 2) Entendimiento del requerimiento
...

## 3) Diagnóstico técnico
...

## 4) Causa raíz probable
- **Síntoma:** qué reporta o percibe el usuario.
- **Causa inmediata:** qué dispara el error o comportamiento (trigger, validación, condición puntual). Clasificar además con uno de estos 5 tipos (vocabulario estándar, siempre en este nivel o en Causa raíz — nunca en Síntoma ni en Causa estructural): configuración faltante o incorrecta / estado del documento (contabilizado, pagado, período cerrado) / restricción de negocio del sistema (trigger/función que valida) / dato del cliente erróneo / bug real (último recurso, no la primera hipótesis).
- **Causa raíz:** por qué existe esa condición (qué proceso/flujo la generó). Si el tipo de la lista anterior describe mejor este nivel que el de "Causa inmediata" (ej. la condición inmediata es un síntoma de un dato del cliente erróneo que se originó más arriba), documentarlo aquí en vez de en el nivel anterior — el tipo se declara una sola vez, en el nivel donde realmente corresponde.
- **Causa estructural:** por qué el sistema permitió que esa condición se produjera sin corregirse sola (ej. una sincronización que el flujo estándar hace pero un módulo custom no replica).

Los cuatro niveles son obligatorios siempre que la evidencia alcance para distinguirlos; si alguno no se pudo determinar con las fuentes de esta corrida, declararlo explícitamente en vez de omitirlo o colapsarlo con el nivel anterior. El tipo de causa (los 5 mencionados arriba) es un dato más granular que complementa un nivel — nunca un quinto nivel aparte, y nunca se repite en más de un nivel para la misma causa.
{Si la conclusión es "no hay error" / "comportamiento esperado": no cerrar solo con consistencia interna del propio registro — citar aquí el resultado concreto de la comparación contra pares del Paso 2, punto 7 (sección 5D) que la respalda. Si se comparó más de un campo de configuración, listar el resultado de cada uno (no solo el que confirma la hipótesis principal) — cualquier otro campo que también resulte una excepción frente a sus hermanos se reporta aquí como causa candidata adicional o complementaria, para que el plan de solución (sección 5) ofrezca esa alternativa al usuario en vez de omitirla. Los campos que resulten alineados con sus hermanos o que no expliquen el síntoma pero gobiernen un comportamiento automático del mismo flujo se marcan **Informativa** (ver definición en la tabla de hipótesis) — se listan también aquí y pasan a §7 como punto a validar, aunque no sean la causa.}

**Tabla de hipótesis (obligatoria cuando la causa candidata sea un registro maestro/configuración):**

| Hipótesis | Campo evaluado (nombre exacto de columna) | Evidencia (valor caso vs. pares) | Resultado | Estado |
|---|---|---|---|---|
| {ej. Doctype anómalo — campo A} | `nombre_columna_1` | ... | Coincide / No coincide | Confirmada / Descartada / Complementaria / Informativa |
| {ej. Doctype anómalo — campo B} | `nombre_columna_2` | ... | Coincide / No coincide | Confirmada / Descartada / Complementaria / Informativa |

**Estado "Complementaria":** se usa cuando un campo no es la causa raíz confirmada del síntoma reportado, pero representa una **vía de solución alternativa** que resolvería o evitaría el mismo síntoma por un mecanismo distinto (ej. la causa raíz confirmada es una regla de facturación mal configurada, pero activar un flag de completar automático en el mismo tipo de documento también resolvería el caso, por una vía distinta). Toda fila marcada Complementaria debe traer en la columna Evidencia/Resultado una explicación **en lenguaje llano de qué hace ese campo cuando está activo** (no solo el valor técnico) — ej. "cuando está en 'Y', el sistema genera automáticamente el albarán y la factura al completar el pedido" — para que la sección 5 y la §7 puedan convertirla en una opción entendible, no solo un nombre de columna.

**Estado "Informativa":** existe para cerrar un hueco entre "Complementaria" y "Descartada". Se usa cuando un campo evaluado (columna `EM_*` o core enumerada en el Paso 2, punto 7-bis) **no es la causa raíz y tampoco resolvería por sí solo el síntoma de este caso** (por eso no es Complementaria), pero **gobierna un comportamiento automático del mismo documento/flujo del ticket** que el usuario querría conocer y validar (ej. completar automáticamente el albarán o la factura al generarlos, reglas de entrega o facturación del tipo de documento). **Descartar un campo como causa no autoriza a callarlo:** que un campo no explique el síntoma no significa que el usuario no deba enterarse de que existe ni de cómo está configurado hoy. Criterio de inclusión: el campo controla un comportamiento del flujo del ticket visible para el usuario. Columnas sin relación funcional con ese flujo (auditoría, campos técnicos internos) siguen siendo Descartada a secas y no van a §7. Una fila Informativa debe traer en Evidencia/Resultado: (a) qué hace el campo en lenguaje llano cuando está activo, (b) su valor actual en el registro del caso, y (c) **de forma explícita, si resuelve o no el síntoma de este caso** (ej. "no saca este pedido de Proformado, solo cambia cómo se completan los documentos que se generen desde ahora"). Este estado solo aplica a filas que no llegan a Confirmada ni a Complementaria, y no altera la regla de la hipótesis general de "registro maestro anómalo" (una fila Informativa cuenta como probada y sin desviación causal).

Regla de esta tabla: **una fila por cada columna `EM_*` distinta identificada en el Paso 2, punto 7-bis** — nunca se colapsan dos o más columnas bajo una sola fila de hipótesis genérica (ej. "Doctype anómalo") con un solo resultado. Una hipótesis general de tipo "registro maestro anómalo" solo puede marcarse **Descartada** cuando **todas** las filas de columnas candidatas fueron probadas individualmente y ninguna mostró desviación frente a sus hermanos; si al menos una columna sí muestra desviación, la hipótesis general se marca **Confirmada** aunque otras columnas evaluadas hayan salido alineadas — el resultado de un campo no invalida ni reemplaza el de otro.

**Coincidir con un hermano no es lo mismo que coincidir con la mayoría.** "Coincide"/"Descartada" en esta tabla nunca se decide comparando el registro del caso contra un solo hermano elegido como referencia — se decide contra el **patrón que sigue la mayoría** de los registros de la familia (ver matriz completa, punto siguiente). Si el registro del caso comparte un valor con **otro** registro que **también** se aparta de la mayoría de la familia, eso **no** descarta la hipótesis — al contrario, ambos registros pasan a ser evidencia conjunta de una posible anomalía compartida (el mismo error de configuración replicado en más de un registro, no dos registros "normales" entre sí). Antes de escribir "Descartada — alineado con [registro X]": construir primero la matriz completa (punto siguiente) y confirmar en ella que [registro X] efectivamente sigue el valor que tiene la **mayoría** de la familia. Si [registro X] es tan minoritario como el caso, el resultado correcto es **Confirmada**, y la sección 4 reporta el grupo completo de registros atípicos (caso + par(es) minoritario(s)) — nunca "Descartada" apoyada en un par que no representa a la mayoría.

**Matriz de comparación completa (obligatoria cuando la hipótesis de registro maestro anómalo se marque Confirmada o Descartada) — no basta con la fila resumen de arriba.** Construir una segunda tabla con **una fila por cada registro maestro hermano evaluado** (no solo el del caso) y **una columna por cada campo `EM_*`/core candidato enumerado en el Paso 2, punto 7-bis** — el mismo formato que una matriz de tipos de documento × flags de configuración, con el valor exacto de cada celda (Y/N, el código del valor, o lo que corresponda), para que el patrón se vea de un vistazo en vez de tener que inferirlo de una descripción resumida. Esta matriz es también la fuente que resuelve la regla anterior: **antes de marcar cualquier fila de la tabla de hipótesis como "Descartada — alineado con X", identificar en esta matriz cuál es el valor que sigue la mayoría de las filas de cada columna** (no solo mirar si dos filas cualquiera coinciden entre sí) — ese valor mayoritario, y no un par arbitrario, es el punto de referencia:

| Registro maestro | `{campo_candidato_1}` | `{campo_candidato_2}` | ... |
|---|---|---|---|
| {registro del caso} | {valor} | {valor} | ... |
| {registro hermano 1} | {valor} | {valor} | ... |
| {registro hermano 2} | {valor} | {valor} | ... |
| ... | | | |
| **Patrón mayoritario de la columna** | {valor que más se repite} | {valor que más se repite} | ... |

La fila final "Patrón mayoritario de la columna" es obligatoria en esta matriz — es contra ese valor, no contra un hermano puntual, que se decide si el registro del caso (y cualquier otro que comparta su valor) es la excepción.

Incluir **todos** los registros hermanos de la familia/dominio que se hayan consultado en el Paso 2 punto 7 — si la familia tiene más de ~15 registros, incluir todos los que compartan el mismo comportamiento que el caso (la excepción) más una muestra representativa de los que sí siguen el patrón mayoritario, y declarar en sección 9 el conteo total de la familia y cuántos se muestran aquí. Nunca reducir esta matriz a una sola fila de resumen ni a solo el registro del caso — el valor de esta evidencia está en que se vean todos los registros comparados en la misma tabla, no en el resultado final.

**Evidencia compuesta — dos o más campos anómalos en el mismo registro se reportan juntos, no como hallazgos independientes.** Si la matriz anterior muestra que el registro del caso se aparta de sus hermanos en **más de una columna a la vez**, no tratar cada columna como una hipótesis separada a confirmar una por una: declarar en la sección 4 que ambos campos apuntan a la misma causa raíz (el registro quedó configurado de forma incompleta/distinta al resto en más de un aspecto relacionado), y en la sección 5 corregir todos los campos anómalos identificados en el mismo ajuste — nunca proponer una corrección parcial que arregle un campo y deje el otro sin resolver.

**Mostrar el camino completo, no solo el hallazgo ganador.** La sección 4 y la sección 5D deben listar **todos** los campos/hipótesis evaluados en el Paso 2 punto 7 — incluidos los que resultaron alineados con sus hermanos y se descartaron — no solo el campo o la hipótesis que terminó explicando el caso. Un documento que solo menciona el hallazgo final sin mostrar qué otras alternativas se revisaron y por qué se descartaron no cumple este paso, aunque la conclusión sea correcta: el objetivo es que quien lea el análisis vea el recorrido completo, no solo el destino.

## 5) Plan de solución (consultor / soporte técnico)
### A. Corrección inmediata (paso a paso)
### B. Workaround vs. solución definitiva (si aplica)
Si existe una forma de mitigar el síntoma mientras se corrige la causa raíz de fondo, declarar ambas por separado y etiquetadas explícitamente — nunca presentar una como si fuera la otra: **Solución temporal/workaround** (qué hacer ya para reducir el impacto inmediato) y **Solución definitiva** (qué corrige la causa raíz/estructural de la sección 4). Si no hay distinción entre ambas (la corrección inmediata ya cierra el caso de fondo), omitir esta subsección.
### C. Validaciones previas (checklist)
### D. Riesgos/controles

## 6) Escalamiento (si aplica)
...
{Antes de recomendar aquí el cambio de un campo/parámetro como solución de fondo: confirmar que el nombre exacto de columna propuesto para cambiar es **el mismo** que quedó "Confirmada" en la tabla de hipótesis del punto 4 — no un campo de nombre o dominio parecido (distintos módulos de personalización pueden definir su propio campo con semántica similar, ej. varias columnas "InvoiceRule" de distintos prefijos `EM_*` sobre la misma tabla, cada una gobernando un comportamiento distinto salvo que el código confirme lo contrario). Si el campo propuesto no es el mismo que la causa raíz confirmada, declararlo explícitamente y no ofrecerlo como solución de fondo. **Pero si ese campo quedó marcado Complementaria en la tabla de hipótesis (vía alternativa viable para el mismo síntoma), es obligatorio incluirlo en §7 como una opción numerada aparte** — nunca omitirlo solo porque no es la causa raíz principal. **Lo mismo aplica a los campos marcados Informativa: van a §7 como punto adicional a validar (aclarando que no corrigen este caso puntual), aunque no se ofrezcan como solución.** El usuario puede preferir la vía alternativa (ej. activar auto-generación) sobre la corrección de la causa raíz confirmada (ej. cambiar una regla de facturación), y no tiene forma de elegir si el análisis solo le muestra una opción.}

## 7) Respuesta sugerida al usuario final (copiable)
{Plantilla incidencia o viabilidad según subtipo}

## 8) Prevención
...

## 9) Datos faltantes (solo si aplica)
...
```

---

## Paso 4B — Formato de respuesta: consulta de viabilidad

Mismo esqueleto de 9 secciones, con contenido adaptado:

```markdown
## 1) Clasificación del caso
- Tipo: Viabilidad operativa | Viabilidad con personalización | Configuración | No implementado
- Subtipo: Consulta de viabilidad
- Dominio ERP: {ventas, tesorería, ...}
- Confianza: ...
- ¿Requiere desarrollo?: ...

## 2) Entendimiento del requerimiento
- Pregunta original (una línea)
- Desglose en sub-capacidades (lista numerada)
- Qué resultado espera el usuario

## 3) Diagnóstico técnico
- Veredicto por sub-capacidad (tabla Sí/No/Parcial)
- Comportamiento core Openbravo (resumen breve)
- Reglas o módulos **de este proyecto** que modifican el veredicto (evidencia)
- Punto exacto de limitación (si aplica)

## 4) Causa raíz / razón de la limitación
- Por qué SÍ o por qué NO (lógica de negocio o validación)
- Alternativas operativas existentes en el proyecto

## 5) Plan de solución (consultor / soporte técnico)
### A. Procedimiento recomendado (workaround si no es directo) — pasos numerados
### B. Validaciones previas (checklist: tipos doc, config, estados, módulos)
### C. Riesgos / qué no hacer
### D. Evidencia técnica breve (2–5 bullets: módulo + archivo/función confirmado en repo, proceso, trigger, mensaje — para L2)

## 6) Escalamiento (si aplica)
- Solo si requiere desarrollo o parametrización inexistente

## 7) Respuesta sugerida al usuario final (copiable)
{Plantilla viabilidad: respuesta directa SÍ/NO/PARCIAL + Por qué (prosa) + procedimiento numerado + Importante — **sin** lista «Detalle por capacidad»}

## 8) Prevención
- Procedimiento estándar recomendado para este tipo de operación

## 9) Datos faltantes (solo si aplica)
- Datos concretos para cerrar el caso al 100%
```

---

## Plantillas obligatorias — Sección 7

### A. Incidencia

Redactar en lenguaje de tesorería/contabilidad. **Sin** triggers, tablas, SQL ni nombres de módulo. Si hay dos capas de causa, **numerar primero el error de proceso** y **después el efecto visible** (mensaje popup, no concilia, importe duplicado).

```markdown
En el análisis del caso se identifica que [qué pasó y qué impide cerrar la operación — una oración clara].

**Qué se identificó**
[1–2 oraciones: documento/movimiento implicado + síntoma en pantalla, ej. «devolución de anticipo registrada como cobro negativo; al conciliar, el sistema muestra el doble del importe del banco».]

**Por qué está mal**
1. [Error de **proceso o documento** — naturaleza del movimiento, tipo de documento, concepto contable, flujo invertido.]
2. [Efecto en **tesorería/conciliación** — por qué no cuadra con el extracto o el mensaje de error, en términos de entrada/salida de banco o importes visibles. Omitir si no hay capa operativa distinta.]

**Qué debieron hacer (proceso correcto en Openbravo)**
- [...]

**Solución a aplicar o verificar**
Paso 1 — [...]
Paso 2 — [...]
Paso 3 — [...]

**Otras opciones a considerar** [incluir si la tabla de hipótesis (sección 4) tiene una o más filas marcadas Complementaria o Informativa. Omitir todo el bloque solo si no hay ninguna de las dos]
[Por cada fila **Complementaria** (resolvería también este caso por otra vía): una opción numerada, en el mismo lenguaje llano, explicando qué configuración activa/cambia y qué efecto tiene. Ej.: "2. Si prefieren que el sistema genere el albarán y la factura automáticamente al completar el pedido, sin depender de la regla de facturación, el ajuste se hace en el Tipo de documento 001-C9-MAYOREO-Matriz, activando la opción de completar automático (hoy está desactivada, a diferencia de la mayoría de tipos de documento de mayoreo)."]
[Por cada fila **Informativa** (no es la causa de este caso ni lo resuelve por sí sola, pero es una configuración relacionada del mismo flujo que el usuario debe validar): un punto numerado que diga (a) qué hace ese campo en lenguaje llano, (b) cómo está hoy en ese tipo de documento/registro, (c) **explícitamente que no corrige este caso puntual**, y (d) dónde se cambia si desean modificarlo. Ej.: "3. Punto adicional a validar: en el Tipo de documento 001-C9-MAYOREO-Matriz, las casillas Completar Albarán y Completar Factura están desmarcadas (igual que en C1). Si al generar esos documentos quieren que se completen solos, se marcan ahí. Esto no es la causa del Proformado de este pedido y no lo corrige por sí solo: solo cambia cómo se comportan los documentos que se generen de ahora en adelante."] Usar la etiqueta exacta del campo tal como aparece en la ventana (5C), nunca el nombre técnico de la columna. Si hay más de una opción complementaria o informativa, numerarlas todas — no elegir una y omitir las demás. Distinguir siempre en el texto cuáles resolverían el caso (Complementarias) y cuáles son solo puntos de validación (Informativas), para no llevar al usuario a creer que marcar una casilla informativa corrige su problema.

**Importante**
- [Qué no hacer — ej. no forzar conciliación parcial cuando el importe aparece duplicado.]
```

**Reglas de redacción sección 7 (incidencia):**

| Hacer | Evitar |
|-------|--------|
| Explicar **entrada vs salida de banco** cuando aplique | Arrancar solo por depósito/reintegro o mensaje técnico |
| Unir causa de negocio + síntoma si ambas están evidenciadas | §7 solo con parche de datos sin decir por qué se registró mal |
| Pasos numerados accionables (reactivar, corregir, conciliar) | SQL, IDs de trigger, nombres de columnas |
| **Nombrar la ventana exacta (ruta de menú es_ES, confirmada en 5C)** cuando la solución sea una acción de UI | Decir «consulte a su consultor» u omitir la ruta cuando el nombre ya se confirmó en el código/AD_MENU |
| Cuando la causa sea una regla de negocio/configuración (aun si el veredicto es "comportamiento esperado"), decir **dónde se configura** esa regla (5C, punto 5) | Nombrar la regla ("la facturación es Después de entregado") sin decir dónde se define ni cómo cambiarla si el negocio lo requiere |
| Toda afirmación de tipo **"alineado con [otro documento/registro]"** o **"es el comportamiento esperado"** en §7 debe corresponder a una hipótesis marcada **Descartada** en la tabla del punto 4 con **todas** sus columnas `EM_*` candidatas probadas (Paso 2, punto 7-bis) | Escribir "alineado con X" en §7 respaldado en la comparación de una sola columna, cuando la tabla de hipótesis del punto 4 aún tiene otras columnas candidatas sin marcar o sin probar |
| Cerrar con **Importante** breve | Escalar a soporte como única salida |
| Incluir **Otras opciones a considerar** cuando exista una hipótesis Complementaria o Informativa (sección 4) — en lenguaje llano, describiendo qué hace el campo, cómo está hoy y si resuelve o no este caso | Omitir una vía de solución alternativa ya identificada solo porque no es la causa raíz confirmada, o mencionarla solo con el nombre técnico de la columna sin explicar qué hace |
| Cuando un campo evaluado se descartó como causa pero gobierna un comportamiento automático del mismo flujo, informarlo como punto a validar dejando claro que **no corrige este caso puntual** | Callar un campo relacionado por haberlo descartado como causa, o presentarlo como si su activación resolviera el síntoma reportado |

**Ejemplo de tono (conciliación — devolución de anticipo mal registrada):**

```markdown
En el análisis del caso se identifica que la devolución de anticipo al cliente no puede conciliarse con el extracto del Banco Pichincha Pagadora porque el movimiento quedó registrado con un flujo y unos importes que no representan una salida de banco.

**Qué se identificó**
Se intentó devolver anticipo mediante cobros con importe negativo («Cantidad devuelta») en lugar de usar el flujo de salida de dinero al cliente. Al conciliar, el sistema compara el débito del extracto (134,48) con una transacción que suma depósito negativo y reintegro positivo, mostrando el doble del importe (-268,96).

**Por qué está mal**
1. Un Cobro representa dinero que **entra** al banco; la devolución de anticipo es dinero que **sale**. Registrar la devolución como cobro negativo invierte la naturaleza del movimiento y no es el procedimiento adecuado para cruzar contra el concepto de anticipos de clientes.
2. Por ese registro, la transacción en cuenta financiera quedó inconsistente (importe en depósito y en reintegro), por eso no coincide con la línea del extracto y aparece el mensaje de conciliación parcial con un valor duplicado.

**Qué debieron hacer (proceso correcto en Openbravo)**
- Devolver el anticipo con el flujo de **salida de banco** / pago o reintegro vinculado al concepto contable de **anticipos de clientes**, alineado al movimiento que refleja el extracto (débito bancario).

**Solución a aplicar o verificar**
Paso 1 — Con tesorería, identificar los cobros afectados (referencia 129647175) y no forzar la conciliación parcial.
Paso 2 — Corregir o rehacer el movimiento para que represente la salida de banco (reintegro = importe del débito del extracto; depósito en cero) o revertir y registrar con el flujo correcto de devolución de anticipo.
Paso 3 — Volver a conciliar con la línea del extracto y validar que el importe neto coincida con el banco.

**Importante**
- No aceptar conciliación parcial para «empatar» un importe duplicado; eso no corrige el origen del error.
- Revisar otros cobros con «Cantidad devuelta» en la misma cuenta antes de cerrar el periodo.
```

### B. Consulta de viabilidad (obligatoria para subtipo B)

Redactar como **respuesta copiable al usuario final**: directa, en prosa, sin listas técnicas de sub-capacidades.

```markdown
Respecto a su consulta sobre [operación en una frase]:

**[SÍ | NO | PARCIAL].** [Oración única y contundente que responda la pregunta tal como la formuló el usuario. Indique con claridad qué **sí** permite el sistema y qué **no** permite. En NO o PARCIAL, use negrita en la limitación principal — ej.: «no permite aplicar la NC directamente sobre cuotas específicas que el usuario elija».]

**Por qué**
[Uno o dos párrafos cortos en lenguaje de negocio. Explique la regla que aplica: cobranza secuencial, pasos separados (emitir vs aplicar crédito), falta de pantalla para X, etc. Incluya un ejemplo concreto si ayuda — ej.: «no existe una pantalla para decir: aplicar esta NC solo a la cuota 4». No usar nombres de tablas, triggers ni módulos.]

**Procedimiento recomendado [subtítulo opcional si aporta contexto — ej.: «(preserva el plan de pagos)»]**
1. [Acción concreta en Openbravo — emitir documento, completar, revisar plan, etc.]
2. [...]
3. [Validación — revisar cuotas, saldos, totales.]
4. [Opcional — escalamiento a tesorería/soporte si tras el proceso queda inconsistencia en capital/interés o política comercial; indicar qué no hacer manualmente.]

**Importante**
- [Qué evitar: saltar cuotas, reactivar documentos FE, confundir flujos alternativos, etc.]
```

**Reglas de redacción sección 7 (viabilidad):**

| Hacer | Evitar |
|-------|--------|
| Primera línea = respuesta clara a la pregunta | Empezar con «Detalle por capacidad» numerado |
| Explicar en párrafos («Por qué») | Matriz Sí/No/Parcial por ítem (eso va en §3–5) |
| Pasos numerados 1, 2, 3… accionables | Pasos genéricos («validar en sistema») |
| Mencionar orden de cuotas / secuencia si aplica | Suponer que el usuario conoce APRM o triggers |
| **Nombrar la ventana/proceso exacto (es_ES, confirmado en 5C)** cuando el procedimiento recomendado sea una acción en pantalla | Dar pasos genéricos («ingrese al sistema y ajuste») cuando el nombre ya se confirmó en el código |
| Cuando la respuesta dependa de una regla de negocio/configuración, decir **dónde se configura** (5C, punto 5) por si el cliente quiere un comportamiento distinto | Explicar la regla sin decir dónde se define ni cómo ajustarla |
| Cerrar con **Importante** breve | Inventario de módulos o referencias técnicas |

**Ejemplo de tono (NC parcial + plan por cuota):**

```markdown
Respecto a su consulta sobre emitir una nota de crédito parcial y afectar el plan de pagos por cuota:

**PARCIAL.** Sí puede emitir la nota de crédito parcial referenciada a la factura original, pero el sistema **no permite aplicar esa NC directamente sobre cuotas específicas** que usted elija del plan de pagos (por ejemplo, «solo a la cuota 4»).

**Por qué**
En facturas a crédito con cuotas numeradas, la cobranza es secuencial: los abonos —incluido el cruce por nota de crédito— deben impactar las cuotas en orden, empezando por la primera cuota pendiente. Al completar la NC parcial, el crédito queda disponible; al aplicarlo mediante cobro sobre la factura original, el plan se actualiza desde la cuota pendiente más antigua, no sobre una cuota intermedia mientras queden cuotas anteriores con saldo.

**Procedimiento recomendado (preserva el plan de pagos)**
1. Emitir la nota de crédito parcial referenciando la factura original, con las líneas e importes a devolver (no el total de la factura).
2. Completar la NC y, si aplica, autorizarla electrónicamente.
3. Registrar un cobro sobre la factura original usando el crédito generado por la NC; el plan de pagos se actualizará en secuencia desde la primera cuota con saldo.
4. Revisar el plan de pagos de la factura original: importes pendientes por cuota y que la suma coincida con el nuevo saldo. Si el desglose capital/interés de cuotas futuras no cuadra con la política comercial, escale a tesorería o soporte para evaluar recálculo de intereses o ajuste controlado del plan (no saltar cuotas manualmente).

**Importante**
- Completar la NC no sustituye el cobro con crédito: sin ese paso, las cuotas no reflejan la reducción.
- No intente imputar el crédito a una cuota futura dejando cuotas anteriores pendientes si la cobranza es secuencial.
```

**Longitud sección 7 (viabilidad):** suficiente para cerrar el ticket; si el usuario necesita menús y campos, cerrar con invitación a **GUIA OPERATIVA**.

---

## Anti-patrones

### Incidencias (§7)

| Anti-patrón | Por qué falla | Qué hacer en su lugar |
|-------------|---------------|------------------------|
| §7 solo con síntoma técnico (depósito/reintegro, trigger) | El cliente no entiende **por qué se registró mal** el documento | Primero proceso/documento; después efecto en conciliación |
| §7 solo con «usaron mal el cobro» sin síntoma | No explica el mensaje de error ni la urgencia operativa | Añadir por qué no concilia hoy (importe duplicado, signo, etc.) |
| Saltar **Qué se identificó** | Respuesta difusa | Una frase que una hecho + consecuencia |
| Mezclar SQL/triggers en §7 | Audiencia incorrecta | Reservar detalle técnico para §5–6 |
| §7 indica corregir un dato/documento sin nombrar la ventana donde se hace | El usuario u operador no sabe dónde ejecutar la acción | Resolver nombre y ruta exacta en 5C y citarla en §7; si no se confirma, declararlo en §9 |
| Cerrar en "no hay error" / "comportamiento esperado" apoyado solo en que otras transacciones del mismo tipo/configuración se comportan igual | Esas transacciones comparten la misma configuración por definición — su consistencia entre sí no prueba que la configuración esté bien | Identificar el registro maestro/de configuración que controla el comportamiento y compararlo contra sus hermanos de la misma familia (Paso 2, punto 7); declarar el resultado en 5D |
| Descartar la hipótesis de "registro maestro anómalo" tras comparar un solo campo `EM_*` que resultó alineado con los hermanos, sin enumerar antes (vía introspección de esquema, Paso 2 punto 7-bis) si existen otras columnas `EM_*` candidatas en la misma tabla | Distintos módulos de personalización agregan columnas independientes sobre la misma tabla maestra (ej. varias variantes de "regla de facturación"); una puede estar alineada mientras otra —la que realmente explica el síntoma— está desviada, y graphify puede no indexarlas todas | Ejecutar la introspección de esquema (información viva de la BD) para listar TODAS las columnas `EM_*` de la tabla antes de comparar; registrar una fila de hipótesis por columna (Paso 4); solo descartar la hipótesis general si ninguna columna enumerada mostró desviación |
| Marcar "Descartada — alineado con [registro X]" solo porque el registro del caso coincide con OTRO registro de la familia, sin verificar si ese otro registro sigue el patrón mayoritario o es igual de minoritario | Dos registros compartiendo el mismo valor atípico no es evidencia de que ese valor sea correcto — puede ser el mismo error de configuración replicado en ambos, no una confirmación mutua de normalidad | Construir la matriz completa con la fila "Patrón mayoritario de la columna" (Paso 4) antes de decidir; comparar siempre contra ese valor mayoritario, nunca contra un solo par elegido; si el par también es minoritario, la hipótesis se marca Confirmada reportando ambos registros como grupo atípico |
| Recomendar cambiar un campo de configuración distinto al confirmado como causa raíz, solo porque tiene un nombre o propósito parecido (ej. "regla de facturación" del core vs. de otro módulo) | La solución no corrige el mecanismo real; dos campos con nombre similar pueden ser independientes y gobernar comportamientos distintos | Confirmar que el campo propuesto en la sección 6 es el mismo, por nombre exacto de columna, que quedó "Confirmada" en la tabla de hipótesis del punto 4 |
| Marcar un campo como "Complementaria" o "Informativa" en la tabla de hipótesis (sección 4) y no mencionarlo en §7 | El usuario se queda sin saber que existe una configuración alternativa que también resolvería su caso — puede rechazar la solución principal sin que se le ofrezca la otra vía | Toda fila Complementaria o Informativa pasa a §7 como una opción/punto numerado en "Otras opciones a considerar", en lenguaje llano y con el efecto funcional de activarla, no solo el nombre de la columna |
| Marcar un campo como "Descartada" porque no explica el síntoma y, por eso, no mencionarlo en §7 aunque gobierne un comportamiento automático del mismo flujo (ej. Completar Albarán / Completar Factura desmarcados en el tipo de documento del caso) | Confunde "no es la causa" con "no le interesa al usuario". El usuario no puede validar una configuración de la que nunca se enteró, y el mismo campo puede ser lo que evite el problema en documentos futuros | Marcarlo **Informativa**, y en §7 indicar qué hace, cómo está hoy, dónde se cambia y que **no** corrige este caso puntual |

### Consultas de viabilidad (§7)

| Anti-patrón | Por qué falla | Qué hacer en su lugar |
|-------------|---------------|------------------------|
| Responder solo con inventario de módulos | No responde SÍ/NO al usuario | Veredicto primero, módulos en sección 5D |
| Asumir capacidad del core sin revisar los módulos de personalización del cliente (`ec.com.<cliente>.*`, o el namespace propio de ese repo) | Conclusión incorrecta para la instalación real de ese cliente | Buscar triggers y validaciones del proyecto en el repo resuelto vía `clientes.json` |
| Proponer flujo manual que contradice triggers | Usuario fallará en pantalla | Validar secuencia, cobranza, estados |
| Omitir workaround cuando la respuesta es NO | Ticket sin solución | Siempre pasos alternativos operativos |
| Mezclar SQL/código en sección 7 | Audiencia incorrecta | Reservar para sección 5D |
| Procedimiento recomendado sin nombrar la ventana/proceso exacto | Usuario no sabe dónde ejecutar la acción | Resolver nombre es_ES en 5C y citarlo en §7; si no se confirma, declararlo en §9 |
| **Lista «Detalle por capacidad» Sí/No/Parcial en sección 7** | Confunde al usuario final; parece informe técnico | Matriz solo en secciones 3–5; sección 7 = respuesta directa en prosa |
| Una sola respuesta sin desglose interno | Pregunta amplia mal analizada | Desglosar en pasos 0B/3 (consultor); redactar sección 7 unificada |

---

## Paso 5 — Exploración: repo del cliente (graphify + código) (cuando aplique)

### Paso 5A. Exploración de graphify y código (obligatoria)

Toda revisión de módulo se hace sobre el **repo de código del cliente** — nunca sobre documentación pre-generada. Dos fuentes, en este orden:

1. **`graphify-out/`** — descargar y filtrar `manifest.json` por el nombre del módulo candidato (mapa 5B) para saber qué clases/archivos existen ahí; es barato y orienta la lectura de código. `graph.json` es un puntero Git LFS inaccesible en la práctica y `.graphify_analysis.json` no indexa `.xml`, así que para lógica PL/SQL (triggers y funciones) el grafo no alcanza — pasar directo al punto 2.
2. **Código fuente del módulo** (`src-db/database/model/functions/*.xml`, `src-core`, clases Java) — leer directamente los triggers, funciones PL/SQL y procesos que apliquen al síntoma. Es el paso que resuelve la mayoría de causas raíz de datos/lógica, no el grafo.
3. Anotar para sección **5D**: ventanas (`AD_MENU`/`AD_WINDOW`), procesos (`AD_PROCESS`), mensajes de error (literal del código o del trigger) y restricciones encontradas.
4. **Verificar despliegue en repo**: confirmar si el módulo tiene carpeta `src-db/` con lógica real o si el flujo que se está evaluando no tiene contraparte en código. Un workaround **sin código que lo respalde** no debe ir a §7 como acción principal si existe una alternativa con código (ej. NC manual vs proceso **Generar NC** con `AD_PROCESS` real). Este mismo criterio aplica a **cualquier acción correctiva**, no solo botones: si existe una ventana o proceso estándar del sistema para corregir el dato/documento afectado (ej. un ajuste de inventario, una reversión de documento), priorizarla en §7 sobre una corrección vía SQL o backend — el script SQL, si aplica, queda como respaldo técnico en las secciones 5–6, nunca como la única vía ofrecida al usuario. **Cuando la corrección es cambiar un valor de configuración que vive en un campo de interfaz** (fórmula, parámetro, flag) y no un dato roto: no basta con describir la acción en términos genéricos ("agregar X", "activar el flag correspondiente") — consultar el valor actual por BD/código, construir el valor nuevo exacto siguiendo el patrón de los registros hermanos ya identificados en el punto 7 del Paso 2, y dejar ese valor exacto tanto en el script de respaldo (5-6) como, en lenguaje llano y sin nombres de campo técnicos, en §7.
5. Si el repo de código no es accesible o no se pudo determinar dónde arranca el código del módulo, declararlo en sección 9 (no inventar ni suponer) y bajar confianza. **Excepción:** si la causa candidata es un flag/parámetro de un registro maestro (Paso 2, punto 7-bis), la inaccesibilidad del repo **no** exime de comparar contra pares — la introspección de esquema vía `pg_query`/MCP-DB no depende del repo y se ejecuta igual; solo se declara en sección 9 la imposibilidad de confirmar en qué módulo/archivo se definió cada columna `EM_*` encontrada, no la imposibilidad de comparar sus valores.
6. **No fijar la causa raíz sobre un archivo de código (jrxml, función, trigger, clase Java) que no se haya confirmado como el componente que realmente interviene en el proceso reportado.** Cuando `graphify-out/` no resuelve el archivo por nombre, reconstruir la cadena completa antes de concluir: ventana/proceso/botón que dispara la acción → definición del reporte o proceso (`AD_Process`, `AD_ReportView`, o el proceso configurado en la ventana) → plantilla/consulta/función exacta → triggers o clases Java involucradas. Cada eslabón se confirma leyendo código o configuración real — nunca por similitud de nombre o de módulo. Si no se puede confirmar el siguiente eslabón con las fuentes disponibles, declarar en sección 9 que el componente no fue confirmado y dejar esa vía como hipótesis a verificar por un técnico, no como causa raíz cerrada.
7. **Si existe un ticket o caso precedente similar (por síntoma o por módulo)**: tratarlo como una hipótesis más, nunca como conclusión automática. Antes de adoptarlo, identificar un dato concreto y verificable **de este caso** (no del precedente) que el mecanismo del precedente obligue a que sea cierto (ej. número de líneas de un documento, valor de un campo específico) y verificarlo contra la fuente correspondiente antes de redactar la sección 4. Si el dato contradice el precedente, o la evidencia propia de este caso sostiene una causa distinta, descartarlo explícitamente en las secciones 1 y 4 en vez de dejarlo implícito como la solución.

### Paso 5B. Mapa dominio → módulos (punto de partida)

**Nota sobre estos nombres:** los módulos custom no se identifican por el nombre del cliente del registro GLPI — se organizan por **flujo de trabajo** dentro del namespace de quien implementó ese repo (ej. `ec.com.sidesoft.<flujo>` agrupa por función — `bpartner.create`, `blacklist`, `account.doctype`, etc. — no por cliente final; varios clientes distintos pueden compartir ese mismo namespace y catálogo base de módulos). Un repo con implementador o convención propia distinta (ej. Unnoparts, namespace `unnoparts.*`) tendrá nombres de módulo diferentes para el mismo dominio funcional. Esta tabla es un **punto de partida con nombres ya observados en instalaciones exploradas anteriormente** — antes de asumir que un nombre de esta tabla existe en el repo del cliente de este ticket, confirmarlo contra `graphify-out/manifest.json` o el listado real de directorios de ese repo (Paso 5A); si no aparece ahí, buscar por palabra clave del dominio en vez de por el nombre literal.

| Dominio | Módulos a explorar en el repo |
|---------|-------------------------------|
| Conciliación / tesorería | `org.openbravo.advpaymentmngt`, `ec.com.sidesoft.detailed.paymentin`, `ec.com.sidesoft.deposit.reconciliation` |
| Cobros/pagos | `detailed.paymentin`, `org.openbravo.advpaymentmngt` |
| Plan de pagos / cuotas | `payment.plan.info`, `payment.schedule`, `postdated.check`, `advpaymentmngt` |
| Facturación / FE Ecuador | `ec.cusoft.facturaec`, skill `ob-fe-eei-invoicelog-analysis` |
| NC / devoluciones venta | `creditNoteRefenence` (código), `saleorder.relations`; `financialcreditnote.sales.auto` **solo si tiene `src-db` en repo** |
| Pre-cancelación / acuerdos | `pre.cancellations`, `payment.agreement`, `debitnote.interest.due` |
| Crédito / cotización | `fast.quotation`, `unnoparts.credit.factory`, `credit.operation.request` |
| POS | regla `openbravo-pos` + código del módulo retail |

### Paso 5B-bis. Conocimiento estático por módulo (si está cargado en el proyecto)

Antes de ir a `graphify-out/`/código (Paso 5A), revisar si el módulo candidato ya tiene documentación funcional/técnica cargada en el proyecto — es más barato que explorar el repo desde cero y puede resolver el caso sin tocar código:

| Archivo | Módulo / contenido |
|---|---|
| `01-Facturacion-Electronica.md` | Facturación electrónica SRI |
| `02-Retenciones.md` | Retenciones en la fuente e IVA |
| `03-Pagos-Cobros-CxP-CxC.md` | Pagos, cobros, cuentas por pagar/cobrar |
| `04-Tesoreria-Cierre-Caja.md` | Tesorería y cierre de caja |
| `05-Contabilidad.md` | Contabilidad general |
| `06-Devoluciones-Descuentos.md` | Devoluciones y descuentos |
| `07-Recursos-Humanos.md` | Recursos humanos |
| `08-Nomina.md` | Nómina |
| `09-Activos-Fijos.md` | Activos fijos |
| `10-Inventario.md` | Inventario |
| `11-Compras.md` | Compras |
| `12-Ventas.md` | Ventas |
| `13-Produccion.md` | Producción |
| `14-Terceros-Business-Partners.md` | Terceros / Business Partners |
| `15-Plataforma-Configuracion.md` | Plataforma y configuración general |
| `casos_de_uso_openbravo_erp.md` | Casos de uso generales del ERP — flujos estándar para entender qué debería pasar |

Cada archivo de módulo trae su propia tabla "Technical" con rutas de Java/Web/modelo físico — usar esas rutas para ir directo al código en el Paso 5A en vez de explorar el repo a ciegas. Esta tabla de archivos es específica de cada proyecto/cliente: si el repo de este ticket no tiene estos archivos cargados (o tiene un índice distinto, ej. `KN-00-indice-maestro.md`), continuar directo con el Paso 5A sin esta fuente y anotarlo en sección 9. Si algún archivo referencia sub-documentos que no existen en el proyecto (patrón frecuente en clientes migrados desde una versión anterior de esta documentación), ignorar esa referencia e ir directo al código fuente real vía la tabla "Technical" del propio archivo de módulo, no intentar abrir el sub-documento inexistente.

### Paso 5C. Resolver nombres exactos de UI (ventanas, botones, procesos)

1. Para **botones/campos citados en §7**: confirmar en `AD_FIELD.xml` / `AD_PROCESS.xml` del módulo, en el repo de código del cliente.
2. Para **la ventana donde el usuario debe ejecutar la acción correctiva** (ej. un ajuste de inventario, una reversión): resolver su nombre exacto y su ruta de menú en es_ES vía `AD_MENU.xml` / `AD_WINDOW.xml` del módulo correspondiente. Este nombre y ruta son los que van a §7 (ver plantilla) — **nunca** se generaliza a "la ventana correspondiente" o "consulte con su consultor" si ya se pudo confirmar en el código.
3. Si `AD_MENU`/`AD_WINDOW`/`AD_FIELD` no cierran el caso: revisar triggers y funciones PL/SQL o Java en `src-db`/`src-core` directamente.
4. Si, tras revisar el código, no se pudo confirmar el nombre exacto de la ventana, declararlo explícitamente en la sección 9 ("ventana no confirmada — requiere validación de un técnico") en vez de omitir la instrucción en §7 o inventar un nombre.
5. **Cuando la causa raíz sea una regla de negocio controlada por un campo de configuración** (ej. una regla de facturación, un flag de un tipo de documento, un parámetro de módulo) — **incluso cuando el veredicto sea "comportamiento esperado, no un error"** — resolver por código/BD dónde se configura esa regla (ventana, pestaña y campo exactos, o tabla/columna si no tiene ventana propia) y citarlo en la sección 4 o 5. No basta con nombrar la regla ("la facturación es Después de entregado"); hay que decir **dónde se define** ese valor, para que quien lo lea sepa dónde ir si el negocio decide que quiere un comportamiento distinto. Si además el cambio de esa regla es una acción que el cliente podría querer tomar, ofrecerlo como paso opcional en §7 ("Si prefieren que esto se genere de otra forma, el ajuste se hace en [ventana/campo]"), no dejarlo solo en las secciones técnicas.

Citar archivos/funciones solo cuando confirmen el veredicto. Traducir hallazgos a **lenguaje de proceso** en la sección 7.

### Paso 5D. Evidencia desde graphify y código (obligatoria en sección 5)

Incluir bullets del tipo:

- Módulo `{M}` — `graphify-out/manifest.json`: [nº de entradas y archivos indexados del módulo]
- Módulo `{M}` — código fuente: [archivo/función/trigger concreto abierto y qué confirma]
- Módulo `{M}` — **componente confirmado como responsable del proceso/documento: Sí/No** — si No, declarar la hipótesis como pendiente de verificación técnica, no como causa raíz cerrada (ver Paso 5A, punto 6)
- Módulo `{M}` — **`src-db` en repo: Sí/No** — si No, indicar módulo alternativo con código para la guía operativa
- Módulo `{M}` — `AD_MENU`/`AD_FIELD` / proceso confirmado: [nombre UI es_ES] (solo si aplica a pasos de usuario)
- **Comparación contra pares/registros similares** (Paso 2, punto 7): [qué registros/configuraciones comparables se revisaron y qué diferencias o coincidencias se encontraron, o el motivo por el que no existe un conjunto comparable] — obligatoria cuando la conclusión sea "no hay error" o "comportamiento esperado"
- **Matriz de comparación completa** (sección 4): referenciar aquí, no repetir — la matriz con todos los registros hermanos × todos los campos candidatos vive una sola vez en la sección 4, esta sección solo confirma que se construyó y con cuántos registros/campos

Esta sección alimenta la **guía operativa** (`openbravo-operational-walkthrough`): incluir solo módulos/procesos con **código confirmado** o flujo core verificado.

---

## Ejemplos de activación

### Incidencia

> No concilia el banco pagadora, subí el CSV y no hace match. Cobro en negativo.

**Acción:** subtipo A → lógica APRM → sección 7 incidencia.

### Consulta de viabilidad (genérica)

> ¿Existe la posibilidad de emitir una nota de crédito al cliente afectando el plan de pagos parcialmente en cada cuota?

**Acción:**

1. Subtipo B → Paso 0B: desglosar en emitir NC / impactar plan / parcial / por cuota.
2. Explorar directamente en el repo del cliente (`graphify-out/` + código) los módulos `creditNoteRefenence`, `saleorder.relations`, `postdated.check`, `detailed.paymentin`, `advpaymentmngt`, siguiendo el Paso 5A.
3. Veredicto cruzando core + personalización documentada; sección **5D** con módulos citados.
4. Sección 7: plantilla viabilidad, copiable al ticket.

### Consulta de viabilidad (otro dominio)

> ¿Se puede facturar parcialmente un pedido de compra y recibir solo parte en almacén?

**Acción:** dominio compras/inventario → reglas de facturación y recepción → matriz de capacidades → sección 7 con veredicto y pasos.

---

## Consulta de módulos (obligatoria)

En **todo** análisis (incidencia o viabilidad):

1. Tras Paso 0 / 0B, identificar los módulos candidatos (mapa 5B) y explorar directamente el repo de código de ese cliente para esos módulos — `graphify-out/` y código fuente — siguiendo el Paso 5A.
2. Incorporar en secciones 3–5D: procesos, ventanas, mensajes y restricciones confirmados en el repo.
3. No contradecir lo confirmado en el código con suposiciones genéricas del core sin evidencia del proyecto.

Si el repo de código no es accesible para un módulo candidato, declararlo en sección 9 y bajar confianza.

---

## Encadenamiento — Guía operativa

La sección 7 es resumen copiable. Para manual en pantalla (menús, botones, campos):

> *Para el paso a paso en Openbravo, solicite: **GUIA OPERATIVA** o **CREA FLUJO**.*

Activa skill **`openbravo-operational-walkthrough`**, pasando:

- Sección 7 del análisis (procedimiento resumido).
- **Sección 5D** (módulos, graphify y código ya explorados).
- Matriz de sub-capacidades (viabilidad) o causa raíz (incidencia).

La guía operativa **debe** volver a explorar directamente el repo del cliente (código, `AD_MENU`/`AD_FIELD`) para nombres UI exactos (es_ES) y validaciones de pantalla, y aplicar formato **compacto** según `openbravo-operational-walkthrough/GUIDE-SCHEMA.md` (Revisar → Corregir → Validar; sin escalar a soporte como única salida).

---

## Recursos

- Prompts para usuarios: [PROMPT-SNIPPET.md](PROMPT-SNIPPET.md)
- Guía operativa: skill `openbravo-operational-walkthrough`
- BDC: solo si el usuario activa BDC explícitamente

---

## Uso desde `triage-glpi-auto` (ejecución automática)

Cuando esta skill se invoca como motor de diagnóstico del Automation `triage-glpi-auto` (triage de GLPI), aplica una regla adicional de consistencia: si el módulo de profundización de causa raíz de ese orquestador (su Paso 5-B) encuentra un mecanismo o alcance más profundo que el identificado en una primera pasada, ese hallazgo se incorpora a **este mismo documento** (secciones 3, 4, 5 y 9) **antes** de redactar la sección 7 — nunca se genera una segunda sección 7 ni un comentario de corrección aparte para el mismo ticket. El documento y la sección 7 que produce esta skill son, por ticket y por corrida, únicos.

**Esto no reemplaza las obligaciones propias de este motor** (Paso 2 punto 7, Paso 5A puntos 6 y 7): la comparación contra pares, el rastreo del componente exacto, y la validación de cualquier ticket/precedente relacionado se ejecutan siempre como parte de esta skill, sea invocada directamente o a través de `triage-glpi-auto` — no dependen de que el orquestador las repita o las detecte en una pasada separada. El Paso 5-B del orquestador es una capa adicional de consistencia sobre el resultado ya producido aquí, no la única fuente de esa disciplina.
