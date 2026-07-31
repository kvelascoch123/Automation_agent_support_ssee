# Análisis Funcional Ticket #9477 — Guía de Remisión Manual

## 1) Clasificación del caso

- **Tipo**: Configuración
- **Subtipo**: Incidencia
- **Dominio ERP**: Logística / Transporte
- **Confianza**: Media (se requiere verificación en código del módulo de guías)
- **¿Requiere desarrollo?**: Por confirmar

---

## 2) Entendimiento del requerimiento

**Proyecto**: UNNOPARTS  
**Solicitante**: kvelasco  
**Ticket**: 9477  
**Título**: KV - CL - Guía de Remisión Manual  

**Descripción normalizada**:
- Proceso: Generación de Guía de Remisión Manual en Openbravo
- Síntoma: El documento generado (PDF) contiene información incompleta o incorrecta en tres puntos específicos:
  1. El campo "Placa" no se completa automáticamente con datos del transportista
  2. Sección "Destinatario" no muestra RUC ni razón social esperados (UNNOPARTS)
  3. Dirección y teléfono de la agencia no aparecen en la parte inferior del PDF

**Contexto**:
- Sistema: Openbravo ERP (Ecuador)
- Ambiente: Producción
- Relevancia: Proceso de calificación con proveedor (OEA Honda)
- Criticidad: Alta (impacta relaciones comerciales)

---

## 3) Diagnóstico técnico

### Síntoma vs Causa raíz

**Síntomas observados** (capa operativa):
- El campo Placa en el PDF sale vacío cuando debería populated from transportista master data
- Sección Destinatario en el documento muestra campos faltantes (RUC, razón social)
- Pie de página sin dirección y teléfono de agencia origen

**Hipótesis de causa** (capa de configuración/desarrollo):
1. **Causa más probable**: El template XML/Jasper de la guía de remisión no está configurado para leer automáticamente los atributos del transportista (field mapping incompleto en el diseño del reporte)
2. **Causa alternativa**: El maestro de transportistas (Transportista/Vendor) no tiene los datos de Placa, RUC asociados en los campos esperados, o esos campos tienen permisos de lectura restringidos en el contexto del reporte
3. **Causa alternativa 2**: Existe un trigger de generación de guías (`SSPCH_*` o similar en Unnoparts) que sobrescribe los valores del template antes de renderizar el PDF

### Módulo involucrado

- **Módulo principal**: `ec.com.sidesoft.*` (extensión Sidesoft para logística Ecuador) o módulo core de guías de remisión
- **Tablas clave**: `M_Shipper_Waybill`, `M_Shipper_Waybill_Line`, transportista (vendor), datos de agencia
- **Función de reporte**: Plantilla Jasper o generador PDF de guía de remisión manual

### Validación del flujo

Según la documentación esperada de Openbravo:
- Las guías manuales **deberían** levantar datos del transportista si está asignado en la cabecera
- La información de destino **debería** mapear los datos del cliente/destino especificado
- Los datos de agencia (origen) **deberían** venir de la configuración de la sucursal/almacén

**El problema**: La plantilla o el proceso de generación **no está mapeando estos datos correctamente**, lo que indica:
- Configuración incompleta en la definición del reporte, O
- Faltan campos en el maestro de transportistas, O
- Existe lógica personalizada que necesita ajuste

---

## 4) Causa raíz probable

**Clasificación según openbravo-triage-tecnico**:

| Tipo | Probabilidad | Evidencia |
|------|------------|-----------|
| Configuración faltante | **Alta** | Template no mapea campos de transportista |
| Restricción negocio | Media | Módulo de guías podría no soportar llenar Placa automáticamente |
| Dato maestro incorrecto | Media | Transportista posiblemente sin placa en registro |
| Bug / desarrollo | Baja | Comportamiento es predecible si template está bien configurado |

**Veredicto de causa raíz**: **Configuración faltante en el template de generación de guía de remisión** — la plantilla de reporte (Jasper o generador PDF) no tiene mapeados los campos de transportista (Placa) y destinatario (RUC, razón social), y la información de agencia no está siendo inyectada en el documento.

---

## 5) Plan de solución (consultor / soporte técnico)

### A. Verificación previa (Checklist técnico)

1. ✅ **Localizar el template de guía de remisión**:
   - Ruta esperada (AD): `org.openbravo.module.shipper.*` o equivalente en Unnoparts
   - Ruta de customización: `{repo_cliente}/src/org/openbravo/custom/shipper/` o similar
   - Archivo: buscar `WaybillManual_*.jrxml` o nombre similar en Jasper

2. ✅ **Verificar mapeo de variables en el template**:
   - ¿Existen variables como `$F{transportista_placa}`, `$F{shipment_license_plate}`?
   - ¿El template lee del parámetro de transportista?
   - ¿Están declarados los parámetros de datos de agencia?

3. ✅ **Confirmar datos en maestro de transportistas**:
   ```sql
   SELECT id, name, tax_id, description, phone
   FROM c_vendor
   WHERE isshipper = 'Y'
   LIMIT 5;
   ```
   — Verificar que Placa/License Plate esté en algún campo (custom field o columna estándar)

4. ✅ **Inspeccionar procesos/triggers de generación**:
   - Buscar triggers `SSPCH_*` en el repo de Unnoparts que pueden estar alterando el documento antes de renderizar

### B. Corrección inmediata (opción principal: configuración)

**Si el problema es el template**:

1. Abrir el archivo JRXML en Jasper Designer (o editor XML)
2. Agregar/mapear los campos faltantes:
   - `$F{m_shipper.license_plate}` → campo Placa
   - `$F{bp_shipper.tax_id}` → RUC del destinatario
   - `$F{bp_shipper.name}` → Razón social
   - `$F{org_shipper.address}`, `$F{org_shipper.phone}` → Datos de agencia
3. Recompilar la plantilla (si es necesario)
4. Probar con una guía de prueba

**Si el problema es datos maestros faltantes**:

1. Verificar que el Transportista (Vendor) tenga:
   - Placa registrada (en campo de ley o custom field)
   - RUC del cliente destino en la guía
2. Completar esos datos antes de generar

### C. Riesgos y controles

- ⚠️ **Riesgo**: Modificar el template sin backup puede quebrar generación de guías
  - **Control**: Hacer backup de JRXML antes de editar
  
- ⚠️ **Riesgo**: Si la lógica es más compleja (trigger personalizado), cambios en template no serán suficientes
  - **Control**: Verificar triggers/procesos antes de asumir que es solo template

- ⚠️ **Riesgo**: Los datos de "agencia" (origen) pueden venir de la sucursal, no de maestros simples
  - **Control**: Verificar proceso de lectura de datos de sucursal en el documento

---

## 6) Escalamiento (si aplica)

**Escalamiento a desarrollo** (probable):
- Si la generación de guía requiere campo personalizado para Placa o si los triggers personalizados de Unnoparts no están permitiendo el mapeo automático
- **Justificación**: Modificación de template Jasper + revisión de triggers

**No es escalable a contador/consultor funcional**:
- Este es un problema técnico de configuración de reportes, no de proceso de negocio

---

## 7) Respuesta sugerida al usuario final (copiable)

```
Estimados,

Hemos revisado el proceso de generación de la Guía de Remisión Manual en Openbravo.

Identificamos que los campos de **Placa**, **RUC del destinatario** y **datos de agencia** 
no están siendo completados automáticamente en el documento PDF porque la plantilla de 
generación no tiene mapeados esos datos desde los maestros de transportista y cliente.

**Qué necesitamos hacer**:

1. Verificar que el maestro de Transportistas tenga registrada la **Placa** del vehículo
2. Confirmar que los datos de **RUC y razón social** del cliente destino estén completos en la orden
3. Revisar la configuración de la plantilla PDF (Jasper) para asegurar que está leyendo correctamente 
   los campos de transportista y agencia

**Próximos pasos**:

Nuestro equipo técnico revisará la plantilla de generación y ajustará el mapeo de datos. 
Una vez completado, reabriremos una guía de prueba para validar que los campos se llenen correctamente.

Estaremos en contacto con el resultado en las próximas horas.

Saludos cordiales,
Equipo de Soporte Sidesoft
```

---

## 8) Prevención

1. **Documentación**: Crear guía de procedimiento para llenar datos de Transportista en Openbravo (incluir campo Placa como obligatorio)
2. **Validación en entrada**: Implementar validación al crear guía de remisión que requiera Transportista con Placa asignada
3. **Testing de reportes**: Incluir prueba de generación de guía en el ciclo de QA de customizaciones
4. **Capacitación**: Entrenar usuarios finales sobre datos requeridos para generación correcta del documento

---

## 9) Datos faltantes

- ❌ Captura de pantalla de la guía generada (solicitado para confirmar campos específicos faltantes)
- ❌ Número de guía de ejemplo donde ocurre el problema
- ❌ Versión exacta de Openbravo/Unnoparts
- ✅ Nombre de transportista/cliente involucrado (inferido del contexto)
- ✅ Criticidad (calificación OEA Honda) — ALTA

**Recomendación**: Solicitar captura de pantalla del documento en ambos estados (esperado vs obtenido) para acelerar diagnosis.
