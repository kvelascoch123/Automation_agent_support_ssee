# Playbook — Reactivar o anular un documento

## Cuándo aplica
El usuario pide reactivar o anular un documento que el sistema no le deja: pedido cerrado por error, factura "activar para no anular", cobro/pago que no permite reactivar, albarán que no permite anular, retención.

## Investigación obligatoria
1. Identificar el documento exacto (tipo y número) y su estado actual en BD (`docstatus` y, si existe, el estado general de negocio `em_*`). Confirmar el estado que el usuario espera obtener.
2. Si el usuario reporta un error al intentarlo, es **ancla clase A o B**: leer el mensaje literal, auditar `ad_pinstance` del documento y localizar en el código del cliente el trigger/función que lo emite (ej. `SSWH_ApplieWithhLivelihood` en ticket 9754 venía de actualizar la factura de compra asociada, no del pago).
3. Revisar **documentos dependientes** antes de proponer nada: albaranes y facturas generados desde un pedido, cobros/pagos aplicados a una factura, retenciones vinculadas, reversos y anulaciones asociadas (ej. factura con anulación AN-… y pago `*Z*`, tickets 9604 y 9984).
4. Revisar restricciones que el código impone: facturación electrónica autorizada por el SRI, documento contabilizado (`posted`), período cerrado, conciliación.
5. Verificar si existe **proceso estándar** en la interfaz (botón Reactivar/Anular, Anular retención, reverso) que resuelva el caso; si existe y no está bloqueado, esa es la vía principal.

## Causas conocidas (hipótesis a verificar)
- Pedido cerrado por error de cajero: el proceso estándar no permite reabrir un pedido cerrado; se ha resuelto cambiando su estado a Registrado por BD (tickets 9999, 9678).
- Reverso de anulación a medias: el reverso debe quedar completado para que la anulación proceda (ticket 9984).
- Validación de un módulo custom que falla al actualizar un documento relacionado (ticket 9754, corregido con desarrollo).

## Solución habitual
- Proceso estándar disponible → pasos exactos en §7 con la ventana confirmada.
- Bloqueado por un estado incoherente → script sugerido (6-B) que cambie solo el estado necesario, precedido de `SELECT` que confirme que no hay documentos dependientes activos; indicar en §5 los documentos que deben revertirse antes, en orden inverso a su creación.
- Bloqueado por un error de código → escalar a desarrollo con el componente confirmado.

## Qué NO hacer
- Reactivar por BD un documento con documentos dependientes activos, contabilizado o autorizado por el SRI sin revisar su impacto.
- Proponer anular una factura electrónica autorizada sin el flujo tributario correspondiente (nota de crédito o anulación en el SRI).

## Asignación sugerida
Técnico si requiere cambio por BD o corrección de código; consultor si basta el proceso estándar o hay que definir con el usuario el flujo correcto.
