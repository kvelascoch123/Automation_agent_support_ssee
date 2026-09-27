# Playbook — HappyPay: corrección de estado de crédito / estado de cuenta

## Cuándo aplica
Proyecto HAPPYPAY. El usuario pide corregir el estado de uno o varios créditos (nº de operación de 11 dígitos, ej. `20261462008`) o de cuotas: "de PAGADO a PENDIENTE", "quitar/eliminar anticipo AOC", "regularizar crédito", "asentar cuota", valores de anticipo que no cuadran.

## Investigación obligatoria (por cada crédito listado)
1. Resolver el crédito en BD (`c_invoice` por `documentno` = nº de operación) y leer su plan de pagos completo en `fin_payment_schedule` (no solo la cuota reportada): nº de cuota, estado de cuota (`em_shpps_fee_status`: PYT pagada, PDG pendiente, DFT vencida), `paidamt`, `outstandingamt`, fecha de vencimiento.
2. Verificar **cobros reales** asociados a cada cuota antes de aceptar lo que pide el usuario: una cuota PYT con `paidamt = 0` y `outstandingamt` igual al importe es una contradicción de datos (KB 438); una cuota PDG con cobro completo también lo es.
3. Revisar anticipos: documentos AOC (Anticipo Operación Crédito) del tercero y su crédito usado (`used_credit`). Un AOC con crédito sin aplicar y sin su COC (Cobro Operación Crédito) explica cuotas vencidas con dinero ya recibido (KB 460).
4. Revisar la cabecera del crédito en `c_invoice`: valor anticipado en cuotas (`EM_Shpic_Advancevalue`), estado de la operación, próxima cuota, última cuota pagada, cuota más vencida. Estos valores deben calcularse desde el plan de pagos real, nunca asignarse genéricos (KB 441).
5. Buscar reversos a medias: COC con sufijo `*Z*`, importe 0 y estado RPR. Si existe, es un documento híbrido que requiere decisión de negocio antes de corregir (KB 460, ticket 9852).
6. **Alcance:** los tres patrones anteriores han sido sistémicos (12, 51 y cientos de créditos). Medir cuántos créditos comparten la condición antes de tratar el caso como aislado.

## Causas conocidas (hipótesis a verificar)
- Cuota N+1 (a veces N+2) marcada PYT sin cobro, justo después del último pago real; sospecha en el proceso/WS de aplicación de cobro (KB 438).
- AOC generado por el canal de cobro sin completar el COC que lo aplica a la cuota (KB 460).
- Valor anticipado residual por cobros del archivo Recover de Banco Pichincha no aplicados (KB 441).

## Solución habitual
- **Vía operativa, cuando exista:** completar el COC usando el crédito del AOC, aplicándolo primero a la cuota vencida más antigua (KB 460).
- **Corrección de datos:** script sugerido (6-B), por crédito y cuota, con `BEGIN`/verificación previa y posterior, filtrando por `c_invoice_id` y nº de cuota, y condicionado al estado de pago real (ej. `AND paidamt = 0`). Recalcular los campos de cabecera desde el plan real. Si el volumen es alto: Fase 1 (créditos del ticket) y Fase 2 (resto).
- En §7: qué se encontró por crédito y qué quedará corregido, sin nombres de campos.

## Qué NO hacer
- Cambiar una cuota a PENDIENTE o PAGADO solo porque el usuario lo pide, sin verificar los cobros reales.
- Poner valores genéricos en próxima cuota, última pagada o estado de la operación.
- Tocar un crédito con reverso híbrido `*Z*` sin decisión de negocio.

## Asignación sugerida
Técnico (corrección de datos con script). Si la causa no está clara o hay decisión de negocio pendiente: consultor.
