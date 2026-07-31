# Referencia — Rutas UI frecuentes Openbravo (es_ES)

Usar como base al redactar pasos. Adaptar si el menú del cliente tiene nombres distintos.

## Navegación general

- **Buscar ventana:** icono de lupa / campo “Application Search” → escribir nombre de ventana → Enter.
- **Guardar registro:** botón **Guardar** (diskette) en barra superior.
- **Procesar documento:** botón de proceso (engranaje / nombre del proceso) → **Procesar** / **Completar**.
- **Estados comunes cobros/pagos:** Borrador → Procesado → Depositado / En tránsito → Conciliado.

---

## Cobros (Payment In / AR Receipt)

| Paso | UI |
|------|-----|
| Abrir | **Menú → Transacciones financieras → Cobros** (o buscar “Cobros”) |
| Nuevo | Botón **Nuevo** |
| Cabecera | Tercero, Fecha, Cuenta financiera, Método de pago, Importe, Referencia |
| Líneas | Pestaña **Líneas de pago** o facturas/pedidos a pagar |
| Procesar | Botón **Procesar** → confirmar |
| Depositar | Desde **Cuenta financiera** → pestaña **Transacción** → **Añadir Múltiples Pagos** o depositar desde el cobro |

---

## Pagos (Payment Out / AP Payment)

| Paso | UI |
|------|-----|
| Abrir | **Menú → Transacciones financieras → Pagos** |
| Nuevo | Botón **Nuevo** |
| Cabecera | Tercero, Fecha, Cuenta financiera, Método de pago, Importe, Nº referencia |
| Conceptos contables | Pestaña **Conceptos contables** → **Nuevo** → Concepto GL, Importe, Tercero (si aplica) |
| Procesar | **Procesar** |
| Ejecutar/Depositar | **Ejecutar pago** o desde cuenta financiera → crear transacción |

**Devolución a cliente / cruce anticipo:** usar **Pago**, no Cobro negativo. Concepto típico: anticipos de clientes (validar nombre exacto en catálogo del cliente).

---

## Cuenta financiera y conciliación

| Paso | UI |
|------|-----|
| Abrir cuenta | **Menú → Transacciones financieras → Cuenta financiera** → buscar la cuenta |
| Transacciones | Pestaña **Transacción** |
| Extracto importado | Pestaña **Extractos bancarios importados** |
| Conciliar | Botón **Conciliación Bancaria** |
| Match manual | Seleccionar línea extracto → **Asociar** / doble clic → elegir transacción → confirmar |
| Cerrar conciliación | **Procesar** conciliación cuando cuadre |

**Columnas relevantes:** Importe Débito / Crédito (extracto); Importe depósito / reintegro (transacción).

---

## Corregir cobro/pago ya depositado (orden obligatorio)

**No reactivar el cobro/pago antes de eliminar la transacción** si el sistema muestra *«El documento no se puede reactivar. El registro ya se ha almacenado en la cuenta financiera»*.

| Orden | Dónde | Acción |
|-------|-------|--------|
| 1 | Cuenta financiera → **Transacción** | Localizar transacción del documento |
| 2 | Misma transacción | Si conciliada: **Reconciliaciones** → **Reactivar** |
| 3 | Misma transacción | Si contabilizada: **Descontabilizar** |
| 4 | Misma transacción | **Reactivar** transacción |
| 5 | Misma transacción | **Eliminar** (DELETE reactiva y elimina) |
| 6 | **Cobros** / **Pagos** | Abrir documento → **Reactivar** |
| 7 | Cobros / Pagos | **Opción A:** reprocesar y depositar · **Opción B:** Revertir pago + nuevo **Pago** (devoluciones) |

**Checkpoint ✓:** transacción eliminada; documento en borrador; importes corregidos antes de volver a depositar.

---

## Conciliación — criterios para el usuario

- El **importe neto** de la transacción debe coincidir con la línea del banco (entrada = depósito; salida = reintegro/débito).
- **Referencia** y **fecha** deben alinearse cuando el matching automático los use.
- No usar **conciliación parcial** para “forzar” importes duplicados o signos incorrectos.

---

## Mensajes frecuentes

| Mensaje (es_ES) | Qué hacer en pantalla |
|-----------------|----------------------|
| Los importes de la línea de banco … y la transacción … no coinciden | Revisar depósito/reintegro duplicados en transacción; corregir documento (Fase 2 GUIDE-SCHEMA); no usar conciliación parcial para forzar. |
| El documento no se puede reactivar… almacenado en la cuenta financiera | Completar pasos 4–5 (reactivar y eliminar transacción) antes de reactivar cobro/pago. |
| Documento contabilizado | Descontabilizar transacción o documento según pantalla; luego continuar orden 1–7. |
| Periodo cerrado | Cambiar fecha del documento o abrir periodo (menú Periodos contables, si tiene permiso). |
