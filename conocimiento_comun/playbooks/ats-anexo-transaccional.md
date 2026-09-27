# Playbook — Errores del ATS (Anexo Transaccional Simplificado)

## Cuándo aplica
El ATS de un mes no se genera, se genera con datos incorrectos o el DIMM/SRI rechaza el XML.

## Investigación obligatoria
1. Obtener el **mensaje literal** del error (captura o `Detalles Adicionales:`) y el período. El mensaje suele señalar la sección (compras, ventas, retenciones) y a veces el documento.
2. Identificar los documentos implicados y revisarlos en BD: tercero (tipo y número de identificación), tipo de comprobante, sustento tributario, códigos de retención en las **líneas**, método de pago.
3. Leer en el código del cliente la generación del ATS para el tag o validación que falla (el módulo del anexo en el repo del cliente).
4. Verificar si el error se repite en **otras empresas/organizaciones** del mismo cliente: una corrección del generador puede afectar a todas (ticket 9825: al corregir un caso se dañaron 3 empresas).
5. Revisar si el período extraído es el correcto (ticket 9541: el ATS de mayo extraía información de 2025).

## Causas conocidas (hipótesis a verificar)
- Método de pago local con campos de exterior diligenciados, o compra al exterior sin método de pago de exterior → "REGFIS DATO NO ES VALIDO" (KB 390).
- Proveedor con identificación tipo 06 (pasaporte) con códigos de retención locales → "Código de retención no permitido para proveedores tipo 06" (KB 413).
- Código de retención en la fuente de las líneas que duplica el tag de retenciones (ticket 9825).
- Tercero con identificación inválida para su tipo (ticket 9846).
- Tag requerido por el SRI ausente en el generador → actualización del módulo (ticket 9758).

## Solución habitual
- Dato o configuración del documento/tercero/método de pago → corrección en la ventana correspondiente (ventana confirmada en código) y volver a generar el ATS.
- Defecto del generador → escalar a desarrollo con el componente confirmado, indicando las empresas afectadas.

## Qué NO hacer
- Corregir retenciones sin respaldo del ATS ni validación tributaria (motor Paso 3: retenciones son sensibles; ante duda, escalar).
- Asumir que la corrección de una empresa no afecta a las demás.

## Asignación sugerida
Consultor para datos y configuración tributaria; técnico si el defecto está en el generador.
