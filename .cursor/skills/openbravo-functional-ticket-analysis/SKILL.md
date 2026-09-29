---
name: openbravo-functional-ticket-analysis
description: >-
  Analiza tickets e incidencias funcionales de Openbravo ERP y consultas de viabilidad
  ("¿el sistema permite…?"): normaliza el texto, clasifica el caso, lee el código fuente
  real del repo del cliente vía MCP GitHub y confirma en la BD del cliente (solo lectura)
  el código desplegado, los valores de configuración y los nombres exactos de ventanas;
  valida core + personalizaciones y entrega el documento de 9 secciones con veredicto y
  solución operativa verificable por el usuario. Encadena con openbravo-operational-walkthrough
  para GUIA OPERATIVA cuando está disponible. No usar para desarrollo puro, creación de módulos o BDC.
---

# Análisis de tickets funcionales Openbravo

**Versión de la skill:** `motor-2026-09-29` (el orquestador la registra en su log).

## Activación

Ejecutar ante: error funcional, incidencia o ticket de soporte de Openbravo; disparadores `ANALIZA TICKET`, `analizar ticket/caso`, `ticket funcional`; síntomas (no funciona, no concilia, no deja, falla, popup, captura de error); o consultas de viabilidad («¿Existe la posibilidad de…?», «¿El sistema permite…?», «¿Cómo se hace…?» cuando el foco es si es posible y cómo operarlo).

**No activar** para: desarrollar código, crear módulo/ventana, compilar, git, o análisis exclusivo con **BDC** (priorizar skill BDC).

## Principio rector — investigar, no suponer

Toda afirmación del documento se apoya en una fuente abierta **en esta corrida**: código del repo del cliente, BD del cliente, texto/imágenes del ticket, contexto del cliente o un ticket previo verificado. Lo que no se pudo confirmar se declara en §9 como pendiente y baja la confianza; **nunca** se rellena con una suposición, un nombre de ventana/columna inventado ni un "comportamiento esperado" sin evidencia. Una respuesta incompleta pero honesta vale más que una completa inventada.

**Jerarquía de fuentes:** lo que está **desplegado** vive en la BD del cliente (funciones y triggers PL/SQL, Application Dictionary, traducciones es_ES, valores de configuración); el repo del cliente es la fuente para Java, reportes (jrxml) y para ubicar módulos. Si repo y BD difieren en un objeto PL/SQL o de diccionario, **manda la BD** y se declara `REPO_DESACTUALIZADO` (Paso 5A.0).

**Objetivo de la respuesta:** que el usuario final pueda corregir o verificar el caso sin volver a preguntar: ventana con ruta completa, campo con su etiqueta en pantalla, valor exacto, orden de pasos, cómo comprobar que quedó resuelto y qué hacer si no.

## Detección de subtipo (obligatorio)

| Subtipo | Señales | Flujo |
|---|---|---|
| **A. Incidencia** | Falla, mensaje de error, no deja guardar, inconsistencia con un documento concreto | 0-A → 0 → 1 → 1.5 → 2 → 4 |
| **B. Viabilidad** | «¿Existe…?», «¿Se puede…?», sin síntoma de fallo | 0B → 1B → 2B → 4B |

Si mezcla ambos: primero viabilidad, luego incidencia sobre el error.

**Varios problemas independientes en un mismo ticket** (distintos documentos, síntomas o módulos sin relación causal): numerarlos como sub-casos P1, P2… y ejecutar el flujo completo para cada uno. En el documento, §3 y §4 van por sub-caso, §5 y §7 con un bloque numerado por sub-caso, y la confianza global es la **menor** de los sub-casos. Si un síntoma es consecuencia de otro, no es independiente: se trata como una sola cadena causal.

---

## Paso 0-A — Suficiencia de contexto (incidencia)

| # | Mínimo funcional | Responde |
|---|---|---|
| 1 | Módulo y documento | ¿Qué documento/tipo y número? |
| 2 | Acción exacta | ¿Qué hacía al fallar (contabilizar, anular, procesar…)? |
| 3 | Síntoma literal | Mensaje textual o comportamiento observado ("no funciona" no es síntoma) |
| 4 | Esperado vs obtenido | ¿Qué debía pasar y qué pasó? |
| 5 | Alcance y entorno | ¿Uno o todos? ¿Desde cuándo? ¿Qué empresa/BD? |

- **Faltan 2 o más** → contexto insuficiente: 3–8 preguntas concretas que cierren exactamente los mínimos ausentes (usar el mapa 5B para orientarlas). En `triage-glpi-auto` es su Paso 4.3/4.4.
- **Faltan 0 o 1** → continuar y señalar el faltante en §9.
- Antes de declarar un mínimo como faltante, intentar cubrirlo con la BD cuando haya un identificador (ej. el nº de documento da tipo, organización, estado y fecha): un dato que se puede consultar no se pregunta.

## Paso 0 / 0B — Normalizar (interno, no mostrar)

**Incidencia:** ID/Título · Módulo/Ventana/Proceso · Organización · Problema · Esperado · Actual · Mensaje exacto · Pasos · Documentos/datos clave (nº doc, importes, fechas, terceros) · Evidencia · Hipótesis del usuario · Restricciones. **No inventar** IDs, importes ni mensajes.

**Viabilidad:** pregunta en una línea · dominio ERP · operación de negocio · documentos · alcance (¿emitir? ¿impactar otro documento? ¿automático? ¿parcial por línea/cuota?) · restricciones · resultado esperado. Desglosar en 2–4 sub-capacidades; cada una recibe veredicto propio antes del global.

## Paso 1 — Clasificar (incidencia)

Operativo (proceso mal usado) · Configuración (maestros, permisos, parámetros, tipos de documento) · Integración/datos (CSV/XML/WS) · Bug/desarrollo (contradice la lógica del código) · Infraestructura (solo con evidencia: OOM, timeout, caída). Indicar confianza (Alta/Media/Baja) y ¿requiere desarrollo? (Sí/No/Por confirmar).

## Paso 1B — Clasificar (viabilidad)

Viabilidad operativa · Viabilidad con personalización · Configuración previa · No implementado / requiere desarrollo · Fuera de alcance ERP. Con confianza y ¿requiere desarrollo?.

## Paso 1.5 — Ancla del síntoma y prioridad de fallo de proceso (incidencia)

Del texto, captura o `Detalles Adicionales:` fijar **una** ancla:

| Clase | Señales | Prioridad |
|---|---|---|
| **A. Fallo de proceso/BD** | `violates … constraint`, `ERROR=`, `@ERROR=`, stack SQL, error rojo al Completar/Registrar/Procesar/Contabilizar/Generar | Máxima: auditar el proceso fallido **antes** de explicar estados o flujo |
| **B. Mensaje de negocio** | `@…@`, popup de validación, "no se puede…" | Alta: localizar validación/trigger/mensaje en código |
| **C. Confusión de estado/flujo** | "está Proformado", "no avanza", sin error | Media: explicar regla solo tras confirmar que el Completar/Registrar no falló |
| **D. Sin ancla** | "no funciona" | Volver a 0-A |

**Regla dura:** si coexisten A y C, manda **A**; prohibido cerrar solo con la explicación de C.

**Mensaje de negocio (clase B) — localizarlo por BD primero:** buscar el texto o la clave `@…@` en `ad_message` / `ad_message_trl` (columna `msgtext`, `value`) para obtener la clave exacta y el módulo dueño; luego buscar esa clave en funciones, triggers (Paso 5A.0) y en el repo. Un mensaje no localizado se declara en §9.

**Homónimos — nunca asumir el significado habitual:** `pricelist`/"tarifa" puede ser `m_pricelist_id` (cabecera) o la columna numérica `pricelist` (precio de lista en línea); si el error cita `column "pricelist"`, es la segunda — verificar ambos en BD. "Completar/registrar/procesar" puede ser DocAction `CO`, botón o solo guardar — buscar `ad_pinstance`, no solo `docstatus`. "Proformado"/estado general (`em_*_generalstatus`) ≠ `docstatus`: reportar ambos.

**Auditoría obligatoria clase A (con BD):**
1. Resolver `record_id` del documento por `documentno` u otro ID del ticket.
2. `SELECT p.ad_pinstance_id, pr.value, pr.name, p.result, p.errormsg, p.created, p.ad_user_id FROM ad_pinstance p LEFT JOIN ad_process pr ON pr.ad_process_id = p.ad_process_id WHERE p.record_id = '{record_id}' ORDER BY p.created DESC LIMIT 25`
3. Con `result = 0` y `errormsg` alineado al síntoma → la causa candidata **es ese fallo**; documentarlo en §3/§4 con fecha, proceso y mensaje.
4. Comparar contra 2–5 **hermanos exitosos** (mismo doctype/org/flujo): campos `em_*` que tocan el proceso o sus EP, filas hijas esperadas (líneas, plan de pagos, satélites) y maestros referenciados **en la misma combinación** (producto en la versión activa de la tarifa, oferta con filas hijas…).
5. Leer el código **desplegado** de la función/trigger que emite el error (Paso 5A.0) y ubicar la condición exacta que lo dispara; contrastarla con los valores del documento.
6. Solo después, si el proceso fue exitoso, explicar el flujo posterior.

**Sin BD:** declarar en §9 la auditoría pendiente y bajar confianza; prohibido cerrar como "comportamiento esperado" o "el documento ya está registrado".

**Anti-patrones de este paso:** ver maestro OK en cabecera e ignorar el `ERROR=` de constraint · responder "genere albarán/factura" cuando el Completar falla · tomar `IP` + Proformado como prueba de registro (puede quedar tras `CO` fallidos; cruzar con `ad_pinstance.result`) · cerrar con un playbook de dominio sin mapear el mensaje literal a código/BD (el playbook solo ordena la búsqueda).

---

## Paso 2 — Análisis técnico (incidencia)

0. Ejecutar primero el Paso 1.5; con ancla A, la auditoría precede a cualquier explicación de flujo.
1. Separar **síntoma** de **causa raíz**.
2. Separar dos capas cuando existan: **negocio/proceso** (documento, flujo o concepto contable incorrecto) y **operativa/síntoma** (por qué falla hoy en pantalla). La §7 no se reduce a la capa operativa si la evidencia muestra error de proceso.
3. Ubicar el punto de fallo: ventana, botón, proceso, validación, matching, posting.
4. **Leer el código del cliente** (Paso 5A: desplegado en BD + repo) para 1–4 módulos candidatos antes de concluir.
5. Diferenciar error de usuario/proceso vs defecto del sistema vs dato maestro.
6. ¿El usuario usó el documento/proceso correcto según el código?
7. **Comparación obligatoria contra pares, antes de cerrar cualquier diagnóstico — incluido "no hay error" o "comportamiento esperado".**
   - **Disparador automático** (sin esperar otra pista): "no genera/completa/aplica X automáticamente" cuando sí ocurre en otros casos, "funciona para unos tipos/sucursales y para otros no", "antes funcionaba y ahora no" sin cambio de código, o "¿por qué aquí sí y allá no?".
   - **Nivel correcto:** comparar transacciones entre sí mide *alcance*, no valida la configuración que comparten. Si la causa puede ser un flag/parámetro de un **registro maestro** (tipo de documento, concepto, parámetro de módulo), comparar contra **los maestros hermanos de la misma familia**, nunca contra las transacciones que lo usan.
   - Los **valores** viven solo en la BD de producción (`pg_query`); el código solo prueba que la columna existe. Procedimiento: (1) identificar por código **todos** los campos candidatos al síntoma (core + `EM_*`); (1-bis) buscar además columnas `EM_*` que el módulo de personalización del cliente agrega sobre la misma tabla, leyendo sus XML (`AD_COLUMN`) en el repo o `ad_column` en la BD; (2) consultar el valor en el registro del caso; (3) consultar los mismos campos en los hermanos; (4) reportar **por campo** si el caso es excepción. **No detenerse en el primer campo coherente.**
   - **"Antes funcionaba":** además de pares, buscar cambios recientes en el maestro o en el objeto de código: `updated`/`updatedby` del registro maestro, y fecha de modificación del objeto en el diccionario (`ad_column.updated`, `ad_process.updated`) o del módulo (`ad_module.version`). Un cambio con fecha anterior al primer fallo es candidato fuerte.
   - Sin BD: no cerrar como "comportamiento esperado"; declarar la comparación pendiente en §9 y bajar confianza.
8. **Impacto del cambio propuesto:** si la solución cambia un maestro, parámetro o fórmula, medir antes qué más usa ese registro (ej. cuántos documentos/organizaciones usaron ese tipo de documento en los últimos 6 meses, qué otros conceptos referencian esa fórmula). Resultado en §5.D y, si afecta a otros procesos del usuario, advertencia en §7 → **Importante**.

**7-bis. Enumeración exhaustiva de candidatos (previa a comparar):** identificar la tabla maestra; con BD, ejecutar `pg_describe_table` o `SELECT column_name FROM information_schema.columns WHERE table_name = '<tabla>'` y listar **todas** las columnas `EM_*`. Es independiente del repo y es la **única fuente válida** si el repo no es accesible. La lista completa es evidencia de 5D; si hay 2+ columnas plausibles, se comparan todas. Aplica a cualquier tabla maestra y dominio.
- **Relación funcional (para decidir qué columnas llevan fila propia en la tabla de hipótesis):** una columna `EM_*` es *relacionada* si su módulo es el mismo del flujo afectado, si aparece en el código (función, trigger, clase, callout) del proceso que falla o del proceso esperado, o si su nombre/descripción en `ad_column`/`ad_element` alude a la acción del síntoma. Las relacionadas se comparan contra hermanos **siempre**. Las no relacionadas se listan en 5D y se agrupan en una sola fila (ver Paso 4).

## Paso 2B — Análisis de viabilidad

Checklist: (1) capacidad exacta (crear, aplicar, automatizar, parcial, por cuota/línea); (2) qué dice el core (`org.openbravo.*`, APRM); (3) qué dice **esta instalación** (la del cliente del ticket): leer el código del módulo candidato (Paso 5A) — triggers/reglas propias (`SSPCH_*`, `SSOREL_*`, `em_*`); (4) reglas de negocio que restrinjan; (5) si NO es directo, workaround operativo; (6) flujo alternativo propio del proyecto.

**Prohibido** concluir solo con el core: validar Core → Proyecto (triggers y extensiones) → Negocio (workaround). Prioridad de evidencia: código del proyecto > comportamiento core genérico.

**Matriz de capacidades** (en §3–5): Sub-capacidad | Sí/No/Parcial | condición/evidencia. **Veredicto global:** SÍ, NO, PARCIAL o SÍ CON CONDICIONES, nunca ambiguo.

**Enrutamiento por dominio:**

| Dominio | Palabras clave | Dónde buscar primero |
|---|---|---|
| Ventas/facturación | factura, NC, ND, devolución, pedido | `saleorder.relations`, `facturaec`, `C_Invoice`, ARC/ARI |
| Tesorería/cobros | cobro, pago, plan de pagos, cuota, conciliación | `advpaymentmngt`, `detailed.paymentin`, `payment.plan.info`, `postdated.check` |
| Compras | factura proveedor, retención, liquidación | `withholdings`, APC |
| Inventario | albarán, movimiento, stock | `M_InOut`, `M_Movement`, módulos `ec.com.*` |
| FE Ecuador | SRI, autorización, XML | `ec.cusoft.facturaec` (skill `ob-fe-eei-invoicelog-analysis` si está disponible) |
| Crédito/cotización | cuota, financiamiento, amortización | `fast.quotation`, `credit.operation.request`, `order.interest`, `credit.factory` |
| Pre-cancelación/cartera | liquidación anticipada, anticipo | `pre.cancellations` |
| Acuerdos/mora | interés mora, nota débito | `debitnote.interest.due`, `payment.agreement` |
| Nómina | concepto, rubro, fórmula, IESS, décimo, fondo de reserva | módulo de nómina del cliente; fórmulas hermanas que agrupan conceptos |
| Documentos impresos/contratos | se duplica, repite datos, no imprime | reporte configurado del proceso de impresión + datos de terceros/solicitud que alimentan sus filas |
| POS | TPV, ticket, caja | código del módulo retail (regla `openbravo-pos` si está disponible) |
| Integraciones | WS, importación | `integration.*`, `webservices` |

Dominio no claro → declararlo en §9 y bajar confianza. Los nombres de módulo de esta tabla y de 5B son ejemplos de un implementador: confirmar siempre contra el repo/`ad_module` del cliente.

## Paso 3 — Reglas de conducta

- Audiencia §1–6 y §8–9: consultor/técnico. Audiencia §7: usuario final, sin jerga técnica ni SQL.
- No proponer cambios de código ni compilación salvo que el caso lo exija. No ejecutar `update.sh`/`smartbuild.sh` sin confirmación.
- Varias causas → ordenar por probabilidad e indicar cómo descartar cada una.
- **Descuadres contables:** verificación en BD obligatoria antes de cerrar; nunca solo con lectura de código.
- Revertir un flujo A→B→C siempre en orden inverso (C, B, A).
- Retenciones Ecuador: tributariamente sensibles; respaldo en ATS antes de sugerir corrección; ante duda, escalar.
- **Disciplina SQL con la BD del cliente:** solo `SELECT`, con `WHERE` preciso (org, tercero, fechas, ID) y `LIMIT` en tablas grandes (`Fact_Acct`, `C_Invoice`, `C_Payment`, `M_Transaction`, `C_AllocationLine`, `C_BankStatementLine`…). Resumir resultados extensos. Toda escritura se entrega como **script sugerido** (texto), nunca ejecutada.
- **Formato de scripts sugeridos:** cada sentencia sin punto y coma final, separadas por una línea `-- fin de sentencia`, con la nota "agregar el terminador al ejecutar". Cada escritura va precedida de su `SELECT` de localización y acotada por ID o por el mismo `WHERE` del `SELECT`. Si hay más de una sentencia de escritura, envolver en transacción (`BEGIN` / `COMMIT` también sin punto y coma) e indicar respaldo previo de las filas.

---

## Paso 4 — Formato de respuesta: incidencia (siempre en este orden)

**§1 Clasificación** — Tipo · Subtipo · Confianza · ¿Requiere desarrollo? · Sub-casos (si aplica)
**§2 Entendimiento del requerimiento**
**§3 Diagnóstico técnico**
**§4 Causa raíz** — cuatro niveles, obligatorios cuando la evidencia alcance (si uno no se pudo determinar, declararlo, no colapsarlo):
- **Síntoma:** lo que percibe el usuario.
- **Causa inmediata:** qué dispara el error (trigger, validación, condición).
- **Causa raíz:** por qué existe esa condición (qué proceso/flujo la generó).
- **Causa estructural:** por qué el sistema permitió que ocurriera sin corregirse (ej. un módulo custom que no replica una sincronización del estándar).
- Tipo de causa (una sola vez, en el nivel que corresponda): configuración faltante/incorrecta · estado del documento · restricción de negocio del sistema · dato del cliente erróneo · bug real (último recurso).
- Si la conclusión es "no hay error"/"comportamiento esperado": citar el resultado de la comparación contra pares (Paso 2.7), campo por campo.

**Tabla de hipótesis** (obligatoria si la causa candidata es un maestro/configuración): Hipótesis | Campo (nombre exacto de columna) | Evidencia (caso vs pares) | Resultado | Estado.
- **Confirmada / Descartada** según evidencia.
- **Complementaria:** no es la causa, pero resolvería el mismo síntoma por otra vía; explicar en lenguaje llano qué hace el campo activo.
- **Informativa:** no es la causa ni lo resuelve, pero gobierna un comportamiento automático del mismo flujo que el usuario debe conocer; indicar qué hace, su valor actual y **explícitamente que no corrige este caso**. Columnas sin relación funcional (auditoría, técnicas) quedan Descartada.
- **Filas por columna `EM_*`:** una fila propia por cada columna **relacionada** (criterio de 7-bis); las **no relacionadas** van en una sola fila agrupada "N columnas sin relación funcional con el flujo — Descartadas en bloque (lista en 5D)". Si al comparar alguna no relacionada resulta atípica frente a sus hermanos, sale del bloque y recibe fila propia. La hipótesis general "maestro anómalo" solo es Descartada si **todas las relacionadas** se probaron sin desviación; basta una desviada para Confirmada.
- **Coincidir con un hermano ≠ coincidir con la mayoría:** decidir contra el patrón mayoritario de la familia; si el par también es minoritario, es anomalía compartida → Confirmada, reportando el grupo.

**Matriz completa** (obligatoria al marcar Confirmada/Descartada un maestro anómalo): filas = registros hermanos evaluados (caso incluido), columnas = campos candidatos relacionados, celdas = valor exacto, última fila **"Patrón mayoritario de la columna"**. Familias de más de ~15 registros: incluir todos los que comparten el valor del caso + muestra de la mayoría, y declarar el conteo total en §9.
- **Evidencia compuesta:** si el caso se aparta en más de una columna, reportarlas juntas como una causa y corregirlas todas en el mismo ajuste.
- **Camino completo:** §4 y 5D listan todas las hipótesis evaluadas, también las descartadas.

**§5 Plan de solución (consultor)** — A. Corrección inmediata paso a paso (si hay cambio de datos: **script SQL sugerido** con `SELECT` de localización + escritura acotada; sin BD, plantilla con placeholders y condición de ejecución) · B. Workaround vs solución definitiva, etiquetados por separado (omitir si no aplica) · C. Validaciones previas y **verificación posterior** (qué consulta o qué acción en pantalla demuestra que quedó resuelto) · D. Riesgos/controles, incluido el **impacto del cambio** (Paso 2.8) con el número medido.
**§6 Escalamiento** — antes de recomendar cambiar un campo como solución de fondo, confirmar que es **el mismo nombre de columna** que quedó Confirmada (módulos distintos pueden tener campos de nombre parecido e independientes). Las filas Complementarias e Informativas pasan obligatoriamente a §7.
**§7 Respuesta sugerida al usuario final** — obligatoria siempre (plantilla abajo). Sin SQL, tablas, columnas ni IDs técnicos. Si el usuario puede resolverlo por la interfaz: ruta de menú completa y pasos.
**§8 Prevención**
**§9 Datos faltantes / evidencia**

## Paso 4B — Formato: viabilidad

Mismas 9 secciones: §1 Tipo, Subtipo, Dominio, Confianza, ¿desarrollo? · §2 pregunta en una línea, sub-capacidades, resultado esperado · §3 veredicto por sub-capacidad (tabla), core, reglas del proyecto con evidencia, punto exacto de limitación · §4 por qué SÍ/NO y alternativas del proyecto · §5 A. procedimiento (workaround si no es directo) B. validaciones C. riesgos D. evidencia técnica (2–5 bullets: módulo + archivo/función confirmado) · §6 solo si requiere desarrollo · §7 plantilla viabilidad · §8 procedimiento estándar · §9 datos faltantes.

## Plantillas §7

**A. Incidencia** (lenguaje de negocio; si hay dos capas, primero el error de proceso y después el efecto visible; con sub-casos, repetir los bloques por problema numerado):

```markdown
En el análisis del caso se identifica que [qué pasó y qué impide cerrar la operación].

**Qué se identificó**
[1–2 oraciones: documento/movimiento implicado + síntoma en pantalla.]

**Por qué está mal**
1. [Error de proceso o documento.]
2. [Efecto visible — omitir si no hay capa operativa distinta.]

**Qué debieron hacer (proceso correcto en Openbravo)**
- [...]

**Solución a aplicar o verificar**
Paso 1 — Ingrese a **[Menú > Submenú > Ventana]** y [acción].
Paso 2 — En el campo **[etiqueta en pantalla]**, cambie el valor de **[valor actual]** a **[valor nuevo exacto]**. [Si es una acción sobre un documento: nº de documento y botón exacto.]
Paso 3 — [...]

**Cómo verificar que quedó resuelto**
- [Acción concreta y resultado visible esperado, ej. "Complete nuevamente el pedido N y confirme que se genera el albarán".]

**Si después de aplicarlo el problema continúa**
- Responda a este ticket indicando [el dato exacto que se necesita: mensaje que aparece, nº de documento, captura de la ventana X].

**Otras opciones a considerar** [solo si hay filas Complementarias o Informativas: una opción numerada por cada una; Complementaria = qué activar y qué efecto tiene; Informativa = qué hace, cómo está hoy, dónde se cambia y que NO corrige este caso. Usar la etiqueta del campo en la ventana, nunca el nombre técnico.]

**Importante**
- [Qué no hacer. Impacto del cambio en otros procesos, si lo hay.]
```

Si la corrección la ejecuta un técnico (script de datos, desarrollo), la sección **Solución a aplicar o verificar** lo dice en lenguaje llano ("el equipo técnico corregirá el registro X; no es necesario que usted modifique nada") y **Cómo verificar** indica qué debe revisar el usuario una vez aplicado.

**B. Viabilidad** (copiable como correo; primera línea responde la pregunta):

```markdown
Respecto a su consulta sobre [operación]:

**[SÍ | NO | PARCIAL].** [Una oración con lo que sí y lo que no permite; en NO/PARCIAL, la limitación en negrita.]

**Por qué**
[1–2 párrafos en lenguaje de negocio, sin tablas, triggers ni módulos.]

**Procedimiento recomendado**
1. Ingrese a **[Menú > Submenú > Ventana]** y [acción concreta].
2. [...]

**Cómo comprobar el resultado**
- [Qué debe ver el usuario al terminar.]

**Importante**
- [Qué evitar.]
```

**Reglas de §7 (ambos subtipos):** nombrar la **ruta de menú completa** confirmada en 5C cuando la solución sea una acción en pantalla — si no se confirmó, declararlo en §9, nunca inventarla ni decir "consulte a su consultor" · campos por su **etiqueta en pantalla** confirmada (`ad_field_trl`/`ad_element_trl`), nunca por nombre de columna · todo cambio de valor con **valor actual y valor nuevo exacto** (fórmulas completas, no "agregar X") · si la causa es una regla de configuración (aun "comportamiento esperado"), decir **dónde se configura** · toda frase "alineado con X"/"comportamiento esperado" debe corresponder a una hipótesis Descartada con **todas** sus columnas relacionadas probadas · el bloque de acciones se titula siempre **"Solución a aplicar o verificar"** · incluir siempre **"Cómo verificar que quedó resuelto"** (o "Cómo comprobar el resultado" en viabilidad) y, en incidencia, **"Si después de aplicarlo el problema continúa"** · en viabilidad, sin lista "Detalle por capacidad" (la matriz va en §3–5) · cerrar con **Importante** breve; nunca escalar a soporte como única salida · si el usuario necesita el paso a paso en pantalla, invitar a **GUIA OPERATIVA** · **única excepción a "sin tablas ni columnas":** cuando el ticket pide expresamente la estructura de BD (tablas/columnas de una ventana), esos nombres, confirmados en el esquema del cliente, son la respuesta y van en §7.

---

## Paso 5 — Lectura del código del cliente (BD desplegada + repo vía MCP GitHub)

**Siempre se lee el código real del cliente**: lo desplegado en su BD (PL/SQL y diccionario) y el repo del cliente (`owner`/`repo` resueltos para el ticket) vía MCP GitHub, archivo por archivo, sin clonar. **No se usa graphify ni `graphify-out/` ni ningún JSON asociado**, y nunca se busca código Openbravo en el repo orquestador.

### 5A. Procedimiento

0. **Código desplegado en la BD (si hay BD):**
   - Funciones: `SELECT p.proname, pg_get_functiondef(p.oid) FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace WHERE n.nspname NOT IN ('pg_catalog','information_schema') AND p.proname ILIKE '%{nombre}%' LIMIT 5`. Para buscar por contenido (mensaje o condición): `... AND p.prosrc ILIKE '%{texto}%'`.
   - Triggers de una tabla: `SELECT tgname, pg_get_triggerdef(t.oid), p.proname FROM pg_trigger t JOIN pg_class c ON c.oid = t.tgrelid JOIN pg_proc p ON p.oid = t.tgfoid WHERE c.relname = '{tabla}' AND NOT t.tgisinternal`, y leer la función de cada trigger relevante.
   - Si el mismo objeto existe en el repo, comparar la lógica que sostiene la causa: si difiere, marcar `REPO_DESACTUALIZADO` en 5D, usar la versión de la BD como evidencia y declararlo en §9.
   - Sin BD: el repo es la única fuente y la confianza de causas PL/SQL no puede ser Alta sin declararlo.
1. **Ubicar** los archivos del módulo candidato en el repo: listar directorios (`get_file_contents` sobre `modules/<módulo>/…`, `src-db/database/model/functions`, `…/triggers`, `src`) o usar la búsqueda de código del MCP GitHub restringida al repo del cliente (nombre de función, trigger, mensaje literal, `AD_MESSAGE`). Las rutas de la tabla "Technical" de los archivos de `conocimiento_comun/modulos/` sirven para ir directo. Confirmar el módulo instalado y su versión en `ad_module` cuando haya BD.
2. **Leer** triggers y funciones PL/SQL (BD desplegada; repo como apoyo), clases Java de proceso y el Application Dictionary (`AD_COLUMN`, `AD_FIELD`, `AD_PROCESS`, `AD_MENU`, `AD_WINDOW`) del módulo. Es la fuente que resuelve la mayoría de causas de lógica y datos.
3. Anotar para 5D: ventanas, procesos, mensajes literales y restricciones encontradas.
4. **Verificar respaldo en código:** un workaround sin código que lo respalde no va a §7 como acción principal si existe alternativa con código (ej. proceso **Generar NC** con `AD_PROCESS` real vs NC manual). Si existe ventana o proceso estándar para corregir el dato, priorizarlo en §7; el script SQL queda como respaldo en §5–6. Si la corrección es un valor de configuración de interfaz (fórmula, parámetro, flag): consultar el valor actual, construir el valor nuevo exacto siguiendo el patrón de los hermanos (Paso 2.7), medir su impacto (Paso 2.8) y dejarlo en el script de respaldo y, en lenguaje llano, en §7.
5. Repo inaccesible o raíz del código no detectada → declararlo en §9 y bajar confianza. **Excepción:** la lectura de código desplegado (5A.0) y la comparación de maestros por introspección de BD (7-bis) se ejecutan igual.
6. **Rastreo del componente exacto:** no fijar la causa raíz sobre un archivo no confirmado como el que interviene. Reconstruir la cadena: ventana/proceso/botón → definición (`AD_PROCESS`, `AD_REPORTVIEW` o el proceso configurado; con BD, consultar el registro del diccionario para obtener clase Java, procedimiento o reporte asociado) → plantilla/consulta/función exacta (jrxml, SQL) → triggers/funciones/clases involucradas. Cada eslabón se confirma leyendo código o configuración real, nunca por parecido de nombre o de módulo. Si un eslabón no se confirma: `COMPONENTE_NO_CONFIRMADO` en §9 y la causa queda como hipótesis para un técnico.
7. **Precedentes** (ticket previo, playbook, caso parecido): son hipótesis, nunca conclusión. Antes de adoptarlos, verificar contra la fuente un dato concreto **de este caso** que el mecanismo del precedente exija. Si lo contradice, descartarlo explícitamente en §1 y §4.

### 5B. Mapa dominio → módulos (punto de partida)

Los módulos custom se nombran por **flujo** dentro del namespace de quien implementó el repo (ej. `ec.com.sidesoft.<flujo>`); otro implementador (ej. `unnoparts.*`) usa otros nombres para el mismo dominio. Confirmar cada nombre contra el listado real del repo o `ad_module`; si no aparece, buscar por palabra clave del dominio.

| Dominio | Módulos a revisar |
|---|---|
| Conciliación/tesorería | `org.openbravo.advpaymentmngt`, `ec.com.sidesoft.detailed.paymentin`, `ec.com.sidesoft.deposit.reconciliation` |
| Cobros/pagos | `detailed.paymentin`, `advpaymentmngt` |
| Plan de pagos/cuotas | `payment.plan.info`, `payment.schedule`, `postdated.check`, `advpaymentmngt` |
| FE Ecuador | `ec.cusoft.facturaec` (skill `ob-fe-eei-invoicelog-analysis` si está disponible) |
| NC/devoluciones venta | `creditNoteRefenence`, `saleorder.relations`; `financialcreditnote.sales.auto` solo si tiene `src-db` |
| Pre-cancelación/acuerdos | `pre.cancellations`, `payment.agreement`, `debitnote.interest.due` |
| Crédito/cotización | `fast.quotation`, `credit.factory` del implementador, `credit.operation.request` |
| Nómina | módulo de nómina del cliente (conceptos, fórmulas) |
| POS | código del módulo retail |

### 5B-bis. Conocimiento estático (`conocimiento_comun/`)

Archivos por módulo: `01-Facturacion-Electronica`, `02-Retenciones`, `03-Pagos-Cobros-CxP-CxC`, `04-Tesoreria-Cierre-Caja`, `05-Contabilidad`, `06-Devoluciones-Descuentos`, `07-Recursos-Humanos`, `08-Nomina`, `09-Activos-Fijos`, `10-Inventario`, `11-Compras`, `12-Ventas`, `13-Produccion`, `14-Terceros-Business-Partners`, `15-Plataforma-Configuracion`, más `casos_de_uso_openbravo_erp.md` (flujos estándar). Son muy grandes: leer **solo el archivo del módulo identificado** y solo las secciones necesarias (tabla "Technical" para rutas de código, sección funcional del paquete). Los sub-documentos de detalle que citan no existen: ir directo al código con las rutas de "Technical".

### 5C. Nombres exactos de UI (BD primero)

1. **Con BD, los nombres se confirman en las traducciones del cliente** (idioma activo del sistema, normalmente `es_ES`; verificarlo en `ad_language` con `isloginlanguage` o `issystemlanguage`):
   - Ventana: `ad_window` + `ad_window_trl.name`. Pestaña: `ad_tab` + `ad_tab_trl.name`. Campo: `ad_field` + `ad_field_trl.name` (si no hay traducción del campo, `ad_element_trl.name` de su columna). Proceso/botón: `ad_process` + `ad_process_trl.name`. Mensaje: `ad_message_trl.msgtext`.
   - **Ruta de menú completa** a partir del `ad_menu_id` de la ventana o proceso:
     `WITH RECURSIVE ruta AS (SELECT tn.node_id, tn.parent_id, 1 AS nivel FROM ad_treenode tn JOIN ad_tree t ON t.ad_tree_id = tn.ad_tree_id AND t.treetype = 'MM' WHERE tn.node_id = '{ad_menu_id}' UNION ALL SELECT tn.node_id, tn.parent_id, r.nivel + 1 FROM ad_treenode tn JOIN ad_tree t ON t.ad_tree_id = tn.ad_tree_id AND t.treetype = 'MM' JOIN ruta r ON tn.node_id = r.parent_id WHERE r.nivel < 8) SELECT r.nivel, COALESCE(mt.name, m.name) AS nombre FROM ruta r JOIN ad_menu m ON m.ad_menu_id = r.node_id LEFT JOIN ad_menu_trl mt ON mt.ad_menu_id = m.ad_menu_id AND mt.ad_language = '{idioma}' ORDER BY r.nivel DESC`
   - Verificar que la ventana esté activa y que el campo sea visible y editable en ella (`ad_field.isdisplayed`, `ad_column.isupdateable`, `ad_field.isreadonly`); si el campo no es editable en pantalla, la corrección no es por interfaz → script en §5–6.
2. Sin BD: confirmar en `AD_FIELD`/`AD_PROCESS`/`AD_MENU`/`AD_WINDOW` del módulo en el repo (el XML trae el nombre base; la traducción puede no estar).
3. Si no cierra: revisar triggers/funciones o Java.
4. No confirmado → declararlo en §9 ("ventana no confirmada — requiere validación de un técnico"); nunca inventar.
5. Causa = regla de configuración: resolver dónde se define (ruta de menú + pestaña + etiqueta del campo, o tabla/columna) y citarlo en §4/§5; ofrecerlo en §7 como paso opcional.

### 5D. Evidencia (obligatoria en §5)

- Módulo `{M}` — archivos/funciones/triggers abiertos y qué confirman.
- Módulo `{M}` — componente confirmado como responsable: Sí/No (si No, hipótesis pendiente).
- Módulo `{M}` — `src-db` en repo: Sí/No (si No, módulo alternativo con código).
- Código desplegado en BD vs repo: IGUAL / `REPO_DESACTUALIZADO` / SOLO BD / SOLO REPO, por objeto relevante.
- Ventana/proceso UI confirmado: ruta de menú completa y etiqueta de campo, y la fuente (BD `_trl` o repo).
- Columnas `EM_*` enumeradas (7-bis): total, relacionadas (comparadas una a una) y no relacionadas (listadas), y resultado de la comparación contra pares, o por qué no hay conjunto comparable.
- Impacto del cambio propuesto (Paso 2.8): número de registros/procesos afectados y consulta usada, o "no aplica" con motivo.
- Matriz completa: referenciar la de §4 (cuántos registros y campos), sin repetirla.

---

## Encadenamiento y recursos

Para el paso a paso en pantalla: **GUIA OPERATIVA** / **CREA FLUJO** → skill `openbravo-operational-walkthrough` **si está disponible en la sesión**, pasando §7, 5D y la causa raíz o matriz de capacidades; esa guía vuelve a leer el código del cliente para nombres UI exactos. En ejecución automática (`triage-glpi-auto`) no se invoca: la §7 debe ser autosuficiente. Las skills o reglas citadas como opcionales (`ob-fe-eei-invoicelog-analysis`, `openbravo-pos`, `openbravo-build`, `PROMPT-SNIPPET.md`, BDC) solo se usan si existen en la sesión; su ausencia no bloquea el análisis ni se declara como faltante.

## Uso desde `triage-glpi-auto`

- El documento de 9 secciones y su §7 son **únicos por ticket y corrida**: cualquier profundización (Paso 5-B del orquestador) se incorpora aquí **antes** de redactar §7, nunca como segunda versión ni comentario de corrección.
- Las obligaciones de este motor (1.5, 2.0/2.7/2.8/7-bis, 5A.0, 5A.6, 5A.7, 5C) se ejecutan siempre, sean o no repetidas por el orquestador.
- **Contrato ancla A:** con error SQL/constraint/`ERROR=` al Completar/Registrar/Procesar, la auditoría de `ad_pinstance` debe estar hecha antes de permitir score ≥ 90 o un cierre como "comportamiento esperado"; si queda `OMITIDO` o contradice el cierre, se baja confianza y el orquestador aplica el tope de score (su Paso 6.1).
- El motor entrega al orquestador, junto al documento, los datos para su **bloque de evidencia** (Paso 5-C del orquestador): tipo de caso, ancla, estado de `ad_pinstance`, componente confirmado, ventana y ruta confirmadas, comparación contra pares, estado repo vs BD, script incluido, verificación incluida en §7 y sub-casos.
