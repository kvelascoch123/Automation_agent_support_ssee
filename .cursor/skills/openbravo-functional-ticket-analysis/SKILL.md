---
name: openbravo-functional-ticket-analysis
description: >-
  Analiza tickets e incidencias funcionales de Openbravo ERP, y consultas de viabilidad
  ("¿el sistema permite…?", "¿existe la posibilidad de…?"): normaliza el texto libre,
  clasifica el caso, consulta markdowns de módulos vía skill openbravo-modules
  (docs/knowledge y docs_customization/knowledge), valida core + personalizaciones,
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
| **A. Incidencia / error** | Falla, mensaje de error, no deja guardar, inconsistencia con documento concreto | Pasos 0 → 1 → 2 → 4 (formato incidencia) |
| **B. Consulta de viabilidad** | «¿Existe…?», «¿Se puede…?», sin síntoma de fallo; pregunta por capacidad o procedimiento | Pasos 0B → 1B → 2B → 4B (formato viabilidad) |

Si la consulta mezcla ambos (ej. «¿se puede hacer X?» y «me sale error Y»), aplicar **ambos** flujos: primero viabilidad, luego incidencia sobre el error.

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
4. **Consulta obligatoria de módulos (skill `openbravo-modules`):** identificar 1–4 módulos candidatos y leer sus markdowns en **`docs_customization/knowledge/`** (prioridad Unnoparts) y **`docs/knowledge/`** antes de concluir. Ver § *Encadenamiento con openbravo-modules* más abajo.
5. Si aplica, **revisar código del repo** (Java, SQL/XML functions, AD) solo para confirmar o ampliar lo documentado en los markdowns.
6. Diferenciar: error del **usuario/proceso** vs **defecto del sistema** vs **dato maestro**.
7. Antes de proponer solución: **¿el usuario usó el documento/proceso correcto según la documentación del módulo?**

---

## Paso 2B — Análisis de viabilidad (obligatorio)

### Checklist interno (responder antes de redactar)

1. **¿Qué capacidad exacta se pregunta?** (crear, aplicar, automatizar, parcial, por cuota/línea/documento)
2. **¿Qué dice el core Openbravo?** (módulos estándar: `org.openbravo.*`, APRM, etc.)
3. **¿Qué dice esta instalación (Unnoparts)?** Invocar skill **`openbravo-modules`** y leer markdowns en:
   - `{M}/docs_customization/knowledge/` (**prioridad**)
   - `{M}/docs/knowledge/` (complemento / inventario)
   Archivos clave: `01-user-chat-guide.md`, `30-functional-processes.md`, `35-messages-and-errors.md`, `50-technical-db-triggers-functions.md`. Solo si falta evidencia en markdowns, buscar triggers/funciones en código.
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

Prioridad de evidencia: **markdown `docs_customization/knowledge/`** > **markdown `docs/knowledge/`** > trigger/código del proyecto > comportamiento core genérico.

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
...

## 5) Plan de solución (consultor / soporte técnico)
### A. Corrección inmediata (paso a paso)
### B. Validaciones previas (checklist)
### C. Riesgos/controles

## 6) Escalamiento (si aplica)
...

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
### D. Evidencia técnica breve (2–5 bullets: módulo + markdown consultado, proceso, trigger, mensaje — para L2)

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

**Solución a aplicar ahora**
Paso 1 — [...]
Paso 2 — [...]
Paso 3 — [...]

**Importante**
- [Qué no hacer — ej. no forzar conciliación parcial cuando el importe aparece duplicado.]
```

**Reglas de redacción sección 7 (incidencia):**

| Hacer | Evitar |
|-------|--------|
| Explicar **entrada vs salida de banco** cuando aplique | Arrancar solo por depósito/reintegro o mensaje técnico |
| Unir causa de negocio + síntoma si ambas están evidenciadas | §7 solo con parche de datos sin decir por qué se registró mal |
| Pasos numerados accionables (reactivar, corregir, conciliar) | SQL, IDs de trigger, nombres de columnas |
| Cerrar con **Importante** breve | Escalar a soporte como única salida |

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

**Solución a aplicar ahora**
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

### Consultas de viabilidad (§7)

| Anti-patrón | Por qué falla | Qué hacer en su lugar |
|-------------|---------------|------------------------|
| Responder solo con inventario de módulos | No responde SÍ/NO al usuario | Veredicto primero, módulos en sección 5D |
| Asumir capacidad del core sin revisar `ec.com.*` | Conclusión incorrecta en Unnoparts | Buscar triggers y validaciones del proyecto |
| Proponer flujo manual que contradice triggers | Usuario fallará en pantalla | Validar secuencia, cobranza, estados |
| Omitir workaround cuando la respuesta es NO | Ticket sin solución | Siempre pasos alternativos operativos |
| Mezclar SQL/código en sección 7 | Audiencia incorrecta | Reservar para sección 5D |
| **Lista «Detalle por capacidad» Sí/No/Parcial en sección 7** | Confunde al usuario final; parece informe técnico | Matriz solo en secciones 3–5; sección 7 = respuesta directa en prosa |
| Una sola respuesta sin desglose interno | Pregunta amplia mal analizada | Desglosar en pasos 0B/3 (consultor); redactar sección 7 unificada |

---

## Paso 5 — Exploración: módulos, markdowns y código (cuando aplique)

### 5A. Consulta de módulos (obligatoria)

**Antes** de buscar en código, ejecutar el flujo de skill **`openbravo-modules`**:

1. Descubrir knowledge roots: `docs_customization/knowledge/` y `docs/knowledge/`.
2. Elegir módulos por dominio, keywords del ticket o `MANIFEST.json` / `INDEX.md`.
3. Leer markdowns según prioridad definida en `openbravo-modules` §3.
4. Anotar para sección **5D**: ventanas, procesos, mensajes, restricciones y handoff a módulos hermanos.
5. **Verificar despliegue en repo** (`openbravo-modules` §4): indicar si el módulo tiene `src-db/` o es solo documentación. Los botones **solo-docs** no deben ir al workaround de §7 como acción principal si existe alternativa en código (ej. NC manual vs **Generar NC**).

### 5B. Mapa dominio → módulos (punto de partida)

| Dominio | Módulos / knowledge a revisar |
|---------|-------------------------------|
| Conciliación / tesorería | `org.openbravo.advpaymentmngt`, `ec.com.sidesoft.detailed.paymentin`, `ec.com.sidesoft.deposit.reconciliation` |
| Cobros/pagos | `detailed.paymentin`, `org.openbravo.advpaymentmngt` |
| Plan de pagos / cuotas | `payment.plan.info`, `payment.schedule`, `postdated.check`, `advpaymentmngt` |
| Facturación / FE Ecuador | `ec.cusoft.facturaec`, skill `ob-fe-eei-invoicelog-analysis` |
| NC / devoluciones venta | `creditNoteRefenence` (código), `saleorder.relations`; `financialcreditnote.sales.auto` **solo si tiene `src-db` en repo** |
| Pre-cancelación / acuerdos | `pre.cancellations`, `payment.agreement`, `debitnote.interest.due` |
| Crédito / cotización | `fast.quotation`, `unnoparts.credit.factory`, `credit.operation.request` |
| POS | regla `openbravo-pos` + markdown del módulo retail |

### 5C. Código (confirmar UI y reglas no documentadas)

1. Para **botones/campos citados en §7**: confirmar en `AD_FIELD.xml` / `AD_PROCESS.xml` del módulo (`openbravo-modules` §4).
2. Si el markdown no cierra el caso: triggers, funciones PL o Java en `50-technical-db-triggers-functions.md` o búsqueda en `src/`.

Citar archivos/funciones solo cuando confirmen el veredicto. Traducir hallazgos a **lenguaje de proceso** en la sección 7.

### 5D. Evidencia desde markdowns y código (obligatoria en sección 5)

Incluir bullets del tipo:

- Módulo `{M}` — `{docs_customization|docs}/knowledge/30-functional-processes.md`: [proceso/botón y validación]
- Módulo `{M}` — `35-messages-and-errors.md`: [mensaje y cuándo aparece]
- Módulo `{M}` — **`src-db` en repo: Sí/No** — si No, indicar módulo alternativo con código para la guía operativa
- Módulo `{M}` — `AD_FIELD` / proceso confirmado: [nombre UI es_ES] (solo si aplica a pasos de usuario)

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
2. Skill **`openbravo-modules`**: leer markdowns de `creditNoteRefenence`, `saleorder.relations`, `postdated.check`, `detailed.paymentin`, `advpaymentmngt` (`docs_customization` primero).
3. Veredicto cruzando core + personalización documentada; sección **5D** con módulos citados.
4. Sección 7: plantilla viabilidad, copiable al ticket.

### Consulta de viabilidad (otro dominio)

> ¿Se puede facturar parcialmente un pedido de compra y recibir solo parte en almacén?

**Acción:** dominio compras/inventario → reglas de facturación y recepción → matriz de capacidades → sección 7 con veredicto y pasos.

---

## Encadenamiento con `openbravo-modules` (obligatorio)

En **todo** análisis (incidencia o viabilidad):

1. Tras Paso 0 / 0B, invocar skill **`openbravo-modules`** (§1–§3 de esa skill).
2. Leer **`docs_customization/knowledge/`** del módulo si existe; complementar con **`docs/knowledge/`**.
3. Incorporar en secciones 3–5D: procesos, ventanas, mensajes y restricciones documentados.
4. **No contradecir** un markdown de personalización con suposiciones del core.

Si no hay markdown para un módulo candidato, declararlo en sección 9 y bajar confianza; entonces sí explorar código directamente.

---

## Encadenamiento — Guía operativa

La sección 7 es resumen copiable. Para manual en pantalla (menús, botones, campos):

> *Para el paso a paso en Openbravo, solicite: **GUIA OPERATIVA** o **CREA FLUJO**.*

Activa skill **`openbravo-operational-walkthrough`**, pasando:

- Sección 7 del análisis (procedimiento resumido).
- **Sección 5D** (módulos y markdowns ya consultados).
- Matriz de sub-capacidades (viabilidad) o causa raíz (incidencia).

La guía operativa **debe** volver a consultar `openbravo-modules` para nombres UI exactos (es_ES) y validaciones de pantalla, y aplicar formato **compacto** según `openbravo-operational-walkthrough/GUIDE-SCHEMA.md` (Revisar → Corregir → Validar; sin escalar a soporte como única salida).

---

## Recursos

- Prompts para usuarios: [PROMPT-SNIPPET.md](PROMPT-SNIPPET.md)
- Guía operativa: skill `openbravo-operational-walkthrough`
- **Hub documentación modular:** skill `openbravo-modules` (`docs/knowledge` + `docs_customization/knowledge`)
- BDC: solo si el usuario activa BDC explícitamente
