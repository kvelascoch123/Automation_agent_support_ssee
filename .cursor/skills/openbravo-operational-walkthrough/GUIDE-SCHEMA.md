# Esquema de guía operativa — plantilla directa

Referencia obligatoria. **Lista lineal de acciones:** el usuario ejecuta paso 1, 2, 3… sin ramas ni «volver al paso X».

---

## Principios de redacción

| Hacer | Evitar |
|-------|--------|
| 1 línea de contexto + documentos del caso | Diagnóstico, tablas de revisión, fases numeradas |
| **5–12 pasos** numerados, imperativo | Árboles de decisión, «si cumple → paso N» |
| Una acción por paso (menú → botón → dato) | Sub-pasos 2.1, 2.2, opciones A/B extensas |
| Nota breve **solo** si un paso suele bloquearse | Checklists de validación, resumen final, «si algo sale mal» largo |
| Repetir bloque por cada documento a corregir | Repetir explicaciones |

**Formato de cada paso:** `N. [Verbo] — Dónde → qué hacer` (máx. 2 líneas).

**Ante bloqueo habitual:** una nota al pie de **un** paso (ej. «Si no deja reactivar cobro: elimine la transacción en el paso anterior»), no tablas de ramas.

---

## Estructura fija de salida

```markdown
## Guía operativa — [título corto]

[Caso en 1 línea: cuenta, documentos, importe]

1. …
2. …
3. …
…

*Nota:* [solo si aplica, 1–2 líneas]
```

**No usar:** Fase 1/2/3/4, checklists previos, tablas OK/Bloquea, resumen final, más de 3 notas al pie.

---

## Orden lineal frecuente (tesorería / conciliación)

Encadenar en la guía **sin ramas**; insertar pasos extra solo si el caso lo exige (ej. desconciliar antes del paso 1):

1. Cuenta financiera → Transacción → **Reactivar** y **Eliminar** transacción del cobro
2. **Cobros** → **Reactivar** cobro *(nota al pie si bloquea: completar paso 1)*
3. **Revertir pago** en el cobro (o **Procesar** + depositar si aplica al caso)
4. **Pagos** → **Nuevo** → devolución → **Procesar** → **Ejecutar pago**
5. Verificar transacción: reintegro = importe banco, depósito = 0
6. **Conciliación Bancaria** → **Asociar** por importe → **Procesar**

Repetir pasos 1–5 por cada documento (**10000648**, **10000650**, etc.).

Detalle UI: [FLOWS-REFERENCE.md](FLOWS-REFERENCE.md).
