# Análisis Funcional Ticket #9478 — Error en Pre-Cancelación de Crédito

## 1) Clasificación del caso

- **Tipo**: Contable / Tesorería
- **Subtipo**: Incidencia
- **Dominio ERP**: Tesorería / Cartera / Cobranza
- **Confianza**: Alta (descripción con datos concretos: NC y cobro generados, pero saldo pendiente)
- **¿Requiere desarrollo?**: Probablemente NO (es un proceso o configuración)

---

## 2) Entendimiento del requerimiento

**Proyecto**: UNNOPARTS  
**Solicitante**: kvelasco (soporte técnico-funcional)  
**Ticket**: 9478  
**Título**: KV - CL - RV: ERROR EN PRECANCELACION  

**Descripción normalizada**:

- **Cliente**: CASTAÑEDA HERRERA JESUS JOEL
- **Operación**: Pre-cancelación (liquidación anticipada) de crédito completo
- **Fecha**: 27/05/2026
- **Monto solicitado**: $1,959.63
- **Resultado esperado**: Crédito líquido (saldo = $0)
- **Resultado obtenido**:
  - ✅ Sistema generó Nota de Crédito: 016-001-00130
  - ✅ Sistema generó Cobro: 016-C1-10021552*Z*
  - ❌ Crédito aún muestra deuda en "Factura cliente" (saldo > $0)
- **Síntoma**: La pre-cancelación ejecutó parcialmente — generó NC y cobro, pero no liquidó el crédito completo

**Contexto**:
- Ventana de origen: "Pre-cancelación" (ventana de operación de liquidación en Openbravo)
- Ambiente: Producción
- Impacto: Cliente gestionado por Cartera, ticket urgente (atraso procesado en sistema vs realidad de pago)

---

## 3) Diagnóstico técnico

### Análisis de capas

**Capa de proceso de negocio**:
- La pre-cancelación es un proceso de **liquidación anticipada de crédito** — toma el saldo pendiente del cliente y lo aplica contra el pago/cobro generado
- Esperado: NC por el saldo pendiente + Cobro del monto pagado = Crédito reducido a $0
- Observado: NC + Cobro fueron generados, pero el crédito aún refleja deuda

**Capa operativa (síntoma en pantalla)**:
- La ventana de pre-cancelación completó su proceso (generó documentos)
- Pero el **matching/aplicación del cobro** no se ejecutó correctamente, o
- La **reducción de saldo** no se reflejó en el estado del crédito

### Causa raíz probable: Matching de documentos incompleto

El proceso de pre-cancelación en Openbravo típicamente funciona así:

```
Pre-cancelación (acción):
  1. Genera Nota de Crédito (NC) por diferencia/saldo
  2. Genera Cobro (Payment) con el monto pagado
  3. Aplica el Cobro a las facturas/cuotas pendientes
  4. Reduce el saldo disponible del cliente a $0 (si es completo)
```

**Lo que probablemente falló**:
- El Paso 3 (**aplicación/matching del cobro**) no se ejecutó completo, o
- El matching solo cubrió parte de la deuda (algunas facturas sí, otras no), o
- Existe un **trigger de validación o secuencia de cobranza** que impide el matching automático si hay condiciones no cumplidas

### Datos clave del diagnóstico

| Evidencia | Observación |
|-----------|-------------|
| NC generada | ✅ Sí (016-001-00130) — indica que el sistema SÍ reconoció deuda pendiente |
| Cobro generado | ✅ Sí (016-C1-10021552*Z*) — monto $1,959.63 |
| Saldo del crédito | ❌ Aún muestra deuda — **el matching no se completó** |

**Verificación contable necesaria** (via BD):
```sql
-- Comprobar asientos de NC y Cobro
SELECT * FROM Fact_Acct 
WHERE docbasetype IN ('ACD', 'CPY') -- NC y Payment
  AND c_allocationline_id IS NULL -- Sin matching posterior
ORDER BY dateacct DESC
LIMIT 20;

-- Comprobar saldo real del cliente
SELECT customer_id, SUM(amount) as saldo_pendiente
FROM Fact_Acct
WHERE customer_id = {ID_CASTAÑEDA}
GROUP BY customer_id;
```

---

## 4) Causa raíz probable

**Clasificación según openbravo-triage-tecnico**:

| Tipo | Probabilidad | Evidencia |
|------|------------|-----------|
| Configuración faltante | **Alta** | Proceso de pre-cancelación no automatiza el matching completo |
| Restricción negocio del sistema | **Alta** | Módulo APRM (cobros) de Openbravo puede requerir validaciones previas |
| Dato maestro incorrecto | Media | Tipo de documento de NC o Cobro quizá no configurado para pre-cancelación |
| Bug real | Baja | Si la NC+Cobro se generan, la lógica básica funciona |

**Veredicto**: El proceso de **pre-cancelación en Unnoparts está mal configurado o incompleto** — genera los documentos (NC + Cobro) pero **no aplica/matchea automáticamente el cobro a las facturas pendientes del cliente**. El crédito mantiene su saldo porque el matching no cerró la liquidación.

---

## 5) Plan de solución (consultor / soporte técnico)

### A. Verificación previa (Checklist)

1. ✅ **Revisar el flujo de pre-cancelación en Unnoparts**:
   - Archivo esperado: `{repo}/src/org/openbravo/custom/*/PreCancellation*.java` o similar
   - O buscar proceso: Menu → Configuración → Procesos → "Pre-cancelación" → revisar pasos

2. ✅ **Confirmar configuración de Tipo de Documento para Cobro**:
   ```sql
   SELECT * FROM c_doctype
   WHERE name LIKE '%Cobro%' OR name LIKE '%Payment%';
   ```
   — Verificar que el tipo de cobro generado esté configurado para **permitir matching automático**

3. ✅ **Validar maestro de cliente**:
   ```sql
   SELECT c_customer_id, name, c_creditstatus_id
   FROM c_bpartner
   WHERE name LIKE '%CASTAÑEDA%';
   ```
   — Confirmar que el cliente no tiene restricción de crédito o estado que bloquee operaciones

4. ✅ **Inspeccionar aplicación de cobro**:
   ```sql
   SELECT * FROM c_allocationline
   WHERE c_payment_id = (
     SELECT id FROM c_payment 
     WHERE documentno = '016-C1-10021552*Z*'
   );
   ```
   — Si esta tabla está VACÍA = **el cobro no fue aplicado a ninguna factura**

5. ✅ **Buscar triggers/procesos de matching secuencial**:
   - En Unnoparts hay un módulo de cobranza secuencial (`SSOREL_*` o similar)
   - El proceso de pre-cancelación puede estar ejecutándose ANTES de la lógica de matching
   - Resultado: NC y Cobro se crean, pero no se aplican automáticamente

### B. Corrección inmediata

**Opción 1: Ejecutar el matching manualmente** (workaround temporal):

1. Abrir el Cobro generado (016-C1-10021552*Z*)
2. Ir a la sección "Aplicaciones" o "Matching"
3. Seleccionar las facturas pendientes del cliente CASTAÑEDA
4. Aplicar el monto del cobro a las facturas
5. Guardar

**Opción 2: Reparar el proceso de pre-cancelación** (solución permanente):

Si el proceso está implementado como trigger o procedimiento (`SSPCH_PreCancelation` o similar):

1. Verificar que el trigger llame a la función/procedure de **aplicación de cobros** DESPUÉS de generar NC y Cobro
2. Si no está, agregar el paso de matching en el flujo
3. Probar con otro cliente para validar

**Opción 3: Si existe secuencia de cobranza**:

Si Unnoparts tiene restricción de "cobranza secuencial" (cobrar facturas en orden FIFO):
- El matching puede estar bloqueado hasta que el cliente complete pagos anteriores
- Solución: Revisar el orden de facturas pendientes y confirmar que se cumplen condiciones previas

### C. Riesgos y controles

- ⚠️ **Riesgo**: Deshacer la pre-cancelación y reintentar puede generar documentos duplicados
  - **Control**: Antes de deshacer, hacer backup de los asientos contables

- ⚠️ **Riesgo**: Si el matching manual se ejecuta, puede afectar conciliación bancaria
  - **Control**: Coordinar con Tesorería antes de aplicar pagos

- ⚠️ **Riesgo**: Si la causa es un trigger personalizado, cambios en código afectan a otros clientes
  - **Control**: Probar en ambiente de prueba primero, luego en producción

---

## 6) Escalamiento (si aplica)

**Escalamiento a desarrollo** (probable si es Unnoparts):
- Si la pre-cancelación no tiene lógica de matching automático implementada
- Requerirá desarrollo de trigger o procedure que ejecute `ApplyPayment` después de generar NC+Cobro

**Escalamiento a consultor funcional**:
- Si el problema es configuración de Tipo de Documento o proceso de Cobranza secuencial
- El consultor puede revisar y ajustar parámetros

**No escala a contador**:
- Es problema de sistema, no de proceso manual

---

## 7) Respuesta sugerida al usuario final (copiable)

```
Estimada Cartera,

Revisamos la pre-cancelación realizada al cliente CASTAÑEDA HERRERA JESUS JOEL 
por el monto de $1,959.63 el 27/05/2026.

**Lo que encontramos**:

El sistema SÍ generó:
- ✅ Nota de Crédito (016-001-00130) — reconoció el saldo pendiente
- ✅ Comprobante de Cobro (016-C1-10021552*Z*) — registró el pago

Sin embargo:
- ❌ El cobro NO se aplicó automáticamente a las facturas pendientes del cliente

**Por qué pasó esto**:

El proceso de pre-cancelación en el sistema tiene un paso de "aplicación de cobro" 
que no se ejecutó correctamente. Esto sucede típicamente porque:

1. El tipo de documento del cobro no está configurado para aplicación automática, O
2. Hay una validación de cobranza secuencial que bloquea el matching, O
3. El cliente tiene una restricción de crédito que impide la aplicación

**Qué hay que hacer**:

Nuestro equipo técnico está investigando la causa exacta. Mientras tanto, 
podemos hacer dos cosas:

**Opción A (rápida, manual)**:
- Abrir el Cobro 016-C1-10021552*Z* en el sistema
- Ingresar a "Aplicación de Pagos" 
- Aplicar el $1,959.63 manualmente contra las facturas pendientes
- Guardar

**Opción B (solución permanente, requiere desarrollo)**:
- Ajustar el proceso de pre-cancelación para que aplique automáticamente el cobro
- Esto evitará que el problema se repita con otros clientes

Estaremos listos para implementar la Opción B en las próximas horas. 
Mientras tanto, pueden usar la Opción A si es urgente procesar al cliente.

Saludos cordiales,
Equipo de Soporte Sidesoft
```

---

## 8) Prevención

1. **Validación de proceso**: Después de generar NC + Cobro en pre-cancelación, verificar que `C_AllocationLine` tenga registros de matching
2. **Testing**: Incluir test case de pre-cancelación completa en QA (verificar saldo = $0 después)
3. **Documentación**: Crear procedimiento de "pre-cancelación manual" como alternativa si el automático falla
4. **Monitoreo**: Alertar si se generan Cobros sin matching dentro de 24 horas

---

## 9) Datos faltantes

- ❌ Estado de las facturas pendientes del cliente CASTAÑEDA (¿cuáles son y cuánto suman?)
- ❌ ID exacto del cliente en BD (facilita query directa)
- ❌ ¿Hay restricción de crédito (credit hold) activa en el cliente?
- ❌ ¿Hay otras pre-cancelaciones previas en este cliente? (para saber si es sistemático)
- ✅ Monto y fecha: claros ($1,959.63, 27/05/2026)
- ✅ Documentos generados: identificados (NC, Cobro)

**Recomendación**: Solicitar ID del cliente y lista de facturas pendientes para acelerar diagnosis en BD.
