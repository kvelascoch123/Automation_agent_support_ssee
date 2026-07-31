# Prompt listo para pegar (opcional)

No es obligatorio usar este texto: la regla activa el análisis automáticamente con la descripción del caso o la pregunta de viabilidad.
Úsalo si quieres forzar el flujo o obtener respuestas más alineadas con consultor funcional.

---

## Versión mínima — incidencia

> ANALIZA TICKET — [pega aquí la descripción del usuario, capturas o ticket completo]

---

## Versión mínima — consulta de viabilidad

> ANALIZA TICKET — ¿El sistema permite [operación]? [contexto breve]

---

## Versión estructurada — incidencia

> ANALIZA TICKET
>
> Título: {asunto}
> Pantalla/proceso: {ventana}
> Problema: {qué no funciona}
> Error exacto: {popup/log}
> Pasos: 1) ... 2) ...
> Documentos/datos: {nº, importes, fechas, refs}
> Evidencia: {capturas/archivos}
> Resultado esperado: {qué debería pasar}

---

## Versión estructurada — consulta de viabilidad (alto acierto)

Usar cuando la pregunta sea amplia («¿se puede X afectando Y de forma Z?»). Aplica a **cualquier flujo** del ERP.

> ANALIZA TICKET — Openbravo
>
> **Pregunta:** {¿El sistema permite…?}
>
> **Dominio:** {ventas | tesorería | compras | inventario | FE Ecuador | crédito | POS | otro}
>
> **Contexto de negocio:**
> - Operación: {qué quiere lograr}
> - Documentos: {factura, NC, cobro, pedido, plan de pagos, etc.}
> - ¿Parcial?: {sí/no — por línea, cuota, importe}
> - ¿Automático al completar?: {sí/no}
> - Restricciones conocidas: {cobranza secuencial, FE, financiamiento, etc.}
>
> **Resultado esperado:** {qué debería quedar en sistema / cartera / contabilidad}
>
> **Datos del caso (si hay):** {nº documento, cliente, importes, cuotas}
>
> **Instrucciones de respuesta:**
> 1. Desglosar la pregunta en sub-capacidades (secciones 3–5 del consultor).
> 2. Veredicto SÍ / NO / PARCIAL en matriz interna; **no** listar «Detalle por capacidad» en sección 7.
> 3. Validar core Openbravo y markdowns de módulos (`openbravo-modules`: `docs_customization` + `docs`).
> 4. Sección 7: respuesta **directa en prosa** (SÍ/NO/PARCIAL + qué sí/no permite) → **Por qué** → procedimiento numerado → **Importante**. Sin SQL.
> 5. Si NO es directo: workaround operativo en 3–4 pasos numerados.

---

## Ejemplos por dominio (plantillas cortas)

**Tesorería / plan de pagos**

> ANALIZA TICKET — ¿Se puede emitir NC al cliente y afectar el plan de pagos parcialmente en cada cuota? Factura a crédito con cuotas numeradas. Cobranza secuencial.

**Ventas / devolución**

> ANALIZA TICKET — ¿El sistema permite nota de crédito parcial referenciada a factura de venta y liberar el pedido asociado?

**Compras**

> ANALIZA TICKET — ¿Se puede registrar retención en compra y conciliar el pago al proveedor en el mismo flujo?

**FE Ecuador**

> ANALIZA TICKET — ¿Se puede autorizar nota de crédito electrónica sin referenciar la factura original?

---

## Palabras clave que activan el flujo sin prefijo

**Incidencia**

- ticket funcional / analizar caso / incidencia
- no funciona / no concilia / falla / error en pantalla
- pasos para reproducir + síntoma en Openbravo

**Viabilidad**

- ¿existe la posibilidad? / ¿el sistema permite? / ¿se puede?
- necesito saber si / ¿cómo se hace? (si el foco es viabilidad operativa)

---

## Qué esperar del análisis (9 secciones)

| Sección | Para quién | Incidencia | Viabilidad |
|---------|------------|------------|------------|
| 1–4 | Consultor | Diagnóstico, causa raíz | Desglose, matriz Sí/No/Parcial, limitación |
| 5–6 | Consultor | Plan técnico, escalamiento | Workaround + evidencia L2 |
| **7** | **Usuario final** | Error de proceso + corrección | **Respuesta directa + Por qué + pasos numerados** (sin lista técnica por sub-capacidad) |
| 8–9 | Consultor | Prevención, datos faltantes | Prevención, datos faltantes |

La **sección 7** en viabilidad debe poder pegarse en un ticket de soporte: primera línea responde la pregunta; párrafo «Por qué»; pasos 1, 2, 3… Ver ejemplo NC parcial en la skill (§ Plantillas sección 7).

---

## Después del análisis — guía paso a paso

> GUIA OPERATIVA — Flujo **compacto** (checklist → corrección → validación) a partir de la sección 7. Sin extensión innecesaria.

Variantes: `CREA FLUJO`, `guía paso a paso`, `solo el paso 1` (modo progresivo).

Ver: `.cursor/skills/openbravo-operational-walkthrough/PROMPT-SNIPPET.md` y `GUIDE-SCHEMA.md`
