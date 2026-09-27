# Playbook — Cierre de caja

## Cuándo aplica
Error al procesar o desprocesar el cierre de caja, diferencias en el arqueo, cobros que no aparecen en el cierre o estados incorrectos del cierre.

## Investigación obligatoria
1. Mensaje literal del error y cierre afectado (caja, fecha, usuario). Con error al procesar: ancla clase A, auditar `ad_pinstance`.
2. Verificar que el **período contable** de la fecha del cierre exista y esté abierto (ticket 9806: "Periodo no existe o no está abierto").
3. Revisar las líneas del cierre contra los cobros, anticipos, ingresos y egresos del día: fechas de cobro vs fechas de las facturas (un cobro con fecha anterior a la factura que paga rompe la línea de tiempo del cierre, KB 325) y anticipos usados con fecha de cobro distinta (ticket 9594).
4. Revisar la configuración de los **métodos de pago** y cuentas financieras de la caja (ticket 9594 se resolvió explicando la configuración correcta).
5. Leer en el código del cliente la lógica del cierre de caja (procesar, desprocesar, validaciones) cuando la causa no sea de datos.

## Causas conocidas (hipótesis a verificar)
- Período cerrado o inexistente (ticket 9806).
- Cobro aplicado a una factura de fecha posterior (KB 325).
- Anticipo usado en un cobro de otra fecha, o método de pago mal configurado (ticket 9594).
- Defecto en los estados del cierre administrador (ticket 9482, corregido con desarrollo).

## Solución habitual
- Operativa: abrir el período, corregir fechas o la aplicación del cobro, ajustar la configuración del método de pago; luego volver a procesar. Procedimientos estándar del cierre (configurar, registrar ingresos/egresos, arqueo, procesar, desprocesar, imprimir, validar contabilidad) documentados por el equipo (KB 485–491).
- Defecto de código → escalar con el componente confirmado.

## Qué NO hacer
- Forzar el cierre por BD para "cuadrar" una diferencia sin identificar su origen.

## Asignación sugerida
Consultor para configuración y operación; técnico si hay defecto de código o corrección de datos.
