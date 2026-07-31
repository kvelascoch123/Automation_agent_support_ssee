---
name: openbravo-operational-walkthrough
description: >-
  Convierte "Qué debieron hacer" y "Solución a aplicar ahora" (de un análisis de ticket Openbravo)
  en guía operativa compacta y accionable: checklist previo, árbol de decisión, pasos ordenados,
  opciones A/B y validación. Usuario no experto; sin SQL ni escalamiento a soporte como única salida.
  Usar con GUIA OPERATIVA, CREA FLUJO, walkthrough o tras ANALIZA TICKET.
---

# Guía operativa paso a paso — Openbravo

## Activación

Ejecutar cuando el usuario:

- pida **guía paso a paso**, **flujo operativo**, **walkthrough**, **instrucciones en pantalla**, o
- use: `GUIA OPERATIVA`, `CREA FLUJO`, `continúa con la guía`, `expande la solución`, o
- pida convertir **"Qué debieron hacer"** / **"Solución a aplicar ahora"** en pasos de pantalla.

**No activar** para desarrollo, SQL, compilación o solo análisis técnico.

---

## Encadenamiento

| Orden | Skill | Aporta |
|-------|-------|--------|
| 1 | `openbravo-functional-ticket-analysis` | §7 procedimiento, §5D módulos, causa raíz |
| 2 | `openbravo-modules` | UI es_ES + verificación `src-db` (§4) |
| 3 | Esta skill + **[GUIDE-SCHEMA.md](GUIDE-SCHEMA.md)** | Formato compacto de salida |

**Regla:** markdown orienta; `AD_FIELD` / `AD_PROCESS` en repo confirman. No citar botones de módulos solo-`docs/`.

---

## Antes de redactar

1. Leer **§5D** y §7 del análisis previo (si existe).
2. Consultar `openbravo-modules` §3–§4 para botones/campos/mensajes del caso.
3. Aplicar plantilla de **[GUIDE-SCHEMA.md](GUIDE-SCHEMA.md)** — **no improvisar** otra estructura.

---

## Reglas de brevedad (obligatorias)

- **Lista lineal** numerada (5–12 pasos); **sin fases**, **sin árboles** («si X vuelva al paso Y»).
- **Contexto:** 1 línea con cuenta, documentos e importe; no repetir diagnóstico.
- **Cada paso:** verbo + menú/ventana + acción (máx. 2 líneas).
- **Notas al pie:** máximo 2, solo para bloqueos habituales (1 línea cada una).
- **Prohibido:** checklists previos, tablas OK/Bloquea, resumen final, opciones A/B extensas.
- **Prohibido:** «escale a soporte»; SQL; IDs internos.
- Valores concretos del caso; si faltan → `[COMPLETAR]`.

---

## Formato de salida (obligatorio)

Seguir **[GUIDE-SCHEMA.md](GUIDE-SCHEMA.md)**:

```
## Guía operativa — [título]
[Caso en 1 línea]

1. …
2. …
…

*Nota:* … (opcional, breve)
```

---

## Reglas de pasos

1. **Un paso = una acción** en pantalla (Reactivar, Eliminar, Procesar, Asociar…).
2. Orden tesorería cuando hay transacción+cobro: **eliminar transacción → reactivar cobro → pago/depositar → conciliar**.
3. Repetir secuencia por cada documento del caso sin re-explicar.

---

## Modo progresivo

Si el usuario pide **de a uno** / **solo paso 1**:

1. Entregar **solo Fase 1** o el primer paso de la fase en curso.
2. Cerrar: *«Confirme al completar y continúo con el siguiente paso.»*
3. Siguiente mensaje: continuar desde último ✓ sin repetir.

---

## Checklist pre-entrega (agente)

- [ ] Lista numerada directa; ≤ ~15 pasos total.
- [ ] Sin «volver al paso X» ni fases Revisar/Validar.
- [ ] Botones citados existen en `src-db`.
- [ ] Notas al pie ≤ 2.

---

## Anti-patrones

| Error | Corrección |
|-------|------------|
| Guía con fases y checklists | Solo pasos 1, 2, 3… |
| Ramas condicionales largas | Un flujo lineal; nota al pie si bloquea |
| Repetir diagnóstico | 1 línea de contexto |

---

## Recursos

- **Plantilla compacta:** [GUIDE-SCHEMA.md](GUIDE-SCHEMA.md)
- **Prompts:** [PROMPT-SNIPPET.md](PROMPT-SNIPPET.md)
- **Rutas UI fallback:** [FLOWS-REFERENCE.md](FLOWS-REFERENCE.md)
- Análisis previo: skill `openbravo-functional-ticket-analysis`
- Módulos: skill `openbravo-modules`
