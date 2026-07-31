---
name: openbravo-kb-error-analysis
description: Analiza consultas usando exclusivamente el contenido de la carpeta BDC del proyecto como fuente de verdad cuando el usuario menciona BDC o pide trabajar con la base de conocimiento. Usar cuando aparezcan "BDC", "base de conocimiento", "carga/recarga/actualiza la BDC" o análisis de errores documentados solo en BDC.
---

# Openbravo — Análisis por base de conocimiento (BDC)

## Entradas

- **user_query**: pregunta o caso del usuario.
- **bdc_folder_content**: contenido efectivo de la carpeta `BDC` del proyecto (solo tras lectura según el flujo de activación y recarga).

## Activación

Ejecutar esta skill **solo** si el usuario:

- menciona explícitamente **"BDC"**, o
- solicita trabajar con la **base de conocimiento** / conocimiento documental del proyecto en esos términos.

Si el usuario no activa la BDC, **no** aplicar este flujo; usar skills y reglas técnicas normales de Openbravo.

## Ubicación de la fuente

1. Localizar en el workspace la carpeta **`BDC`** (raíz del proyecto o ruta acordada en el repo).
2. Tratar todo su contenido como **fuente oficial** de errores, observaciones, evidencias y soluciones documentadas.

## Carga inicial y memoria

1. **Primera vez en la conversación** (BDC activada y aún no cargada en contexto): leer el contenido **relevante** de `BDC` por completo — documentos de texto, Word si aplica, imágenes vinculadas a errores o soluciones.
2. Tras leer, **conservar** el material en memoria de conversación y reutilizarlo en turnos posteriores **sin** volver a abrir archivos.

## Recarga explícita

Volver a leer `BDC` y **reconstruir** la memoria documental **solo** si el usuario pide explícitamente, por ejemplo:

- "carga la BDC"
- "recarga la BDC"
- "actualiza la BDC"

o instrucciones equivalentes en el mismo sentido.

## Análisis de la consulta

Con la memoria BDC disponible:

1. Relacionar `user_query` con lo documentado en BDC.
2. Priorizar: coincidencias exactas; coincidencias semánticas; secciones con **solución propuesta**; imágenes o evidencias alineadas; ítems conectados funcional o técnicamente.

## Imágenes

Si hay imágenes en BDC, interpretarlas como **evidencia** complementaria: mensajes de error, pantallas, validaciones, inconsistencias o flujos observados. No inventar detalles no visibles en la evidencia.

## Integración con reglas/skills técnicas de Openbravo

Las skills o reglas técnicas de Openbravo **solo** sirven para:

- explicar con más claridad lo que **ya** dice la BDC, o
- estructurar la respuesta.

**No** usar conocimiento técnico general para **añadir** soluciones, causas o pasos que **no** estén en la BDC cuando la consulta se atiende bajo este flujo.

## Restricciones

- No inventar soluciones ni completar lagunas con suposiciones.
- No usar conocimiento externo (web, experiencia genérica) como sustituto del contenido BDC para resolver el caso bajo activación BDC.
- No mezclar "memoria técnica general" con hechos atribuidos a la BDC sin cita a ese contenido.
- Si no hay coincidencias razonables con lo documentado, responder **exactamente**:

```text
La base de conocimiento no contiene información relacionada con este caso.
```

## Formato de respuesta

Usar esta plantilla cuando exista información relacionada en BDC:

```markdown
## Análisis del caso
{resumen del problema según la BDC}

## Solución propuesta
{solución documentada en la BDC}

## Ítem de la BDC donde se encontró
- Sección / título: {nombre del ítem o sección}
- Referencia: {detalle breve del fragmento relacionado}

## Ítems relacionados
- {ítem relacionado 1}: {motivo de relación}
- {ítem relacionado 2}: {motivo de relación}

## Validación
Si no existe información relacionada:
La base de conocimiento no contiene información relacionada con este caso.
```

**Nota:** La sección "Validación" con el mensaje fijo solo debe aparecer cuando **no** haya información relacionada; en ese caso puede bastar con ese mensaje (o la plantilla completa con las partes superiores vacías omitidas y solo el mensaje requerido).

## Checklist rápido

- [ ] ¿El usuario activó BDC explícitamente?
- [ ] ¿Está cargada/recargada la memoria según corresponde?
- [ ] ¿La respuesta se basa solo en BDC (más aclaración técnica sin añadir hechos nuevos)?
- [ ] ¿Sin coincidencias → mensaje exacto obligatorio?
