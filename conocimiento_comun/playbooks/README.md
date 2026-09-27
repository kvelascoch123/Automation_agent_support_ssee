# Playbooks de casos recurrentes

Guías cortas de **investigación** para tipos de ticket que se repiten. Las usa `triage-glpi-auto` en su Paso 3-E: el agente lee este índice, y si el ticket coincide con un disparador lee **solo** ese playbook.

Un playbook **ordena la investigación, no la reemplaza**: dice qué verificar, qué evidencia exigir y qué forma suele tener la solución. Toda causa se confirma igual en el código y la BD del caso actual (motor, regla 5A.7). Las referencias de origen (tickets y artículos de la BDC) documentan de dónde salió el patrón; el agente **no consulta la BDC** para usarlos.

| Playbook | Disparadores (asunto o descripción) | Proyecto | Origen |
|---|---|---|---|
| [happypay-estado-credito.md](happypay-estado-credito.md) | "corrección de estado de crédito", "estado de cuenta", "de PAGADO a PENDIENTE", "anticipo AOC", "eliminar anticipo", "regularizar crédito", nº de operación de crédito | HAPPYPAY | 69 tickets en 2026; KB 438, 441, 460 |
| [reactivar-anular-documento.md](reactivar-anular-documento.md) | "reactivar", "anular", "activar factura", "se cerró por error", pedido/factura/cobro/pago/albarán/retención | Todos | Tickets 9999, 9678, 9984, 9827, 9754, 9604 |
| [ats-anexo-transaccional.md](ats-anexo-transaccional.md) | "ATS", "anexo transaccional", "DIMM", error al generar o subir el anexo | Todos | Tickets 9846, 9825, 9758, 9626, 9541; KB 390, 413, 389, 364 |
| [cierre-de-caja.md](cierre-de-caja.md) | "cierre de caja", "arqueo", "diferencia en caja", "procesar/desprocesar cierre" | Todos | Tickets 9806, 9594, 9482; KB 325, 485–491 |
| [accesos-roles-permisos.md](accesos-roles-permisos.md) | "permiso", "acceso", "rol", "no me aparece el botón/pestaña", "usuario de solo lectura", "crear usuario" | Todos | KB 464, 411; tickets de accesos 2026 |
| [consulta-estructura-bd.md](consulta-estructura-bd.md) | "información de la base de datos", "nombre de la columna/tabla", "para generar un reporte", vistas | Todos | Tickets 8813, 8779, 8733 (VISTAS) |

## Cómo mantenerlos

- **Crear** un playbook cuando un mismo tipo de caso aparezca 3 o más veces con una resolución consistente. Partir de tickets resueltos reales, nunca de supuestos.
- **Formato fijo:** Cuándo aplica · Investigación obligatoria · Causas conocidas (como hipótesis, con su origen) · Solución habitual · Qué NO hacer · Asignación sugerida.
- **Actualizar** cuando un ticket demuestre que una causa conocida era incorrecta o que apareció una nueva; anotar la fecha y el ticket.
- Agregar la fila correspondiente en este índice. El agente solo lee lo que está aquí.
