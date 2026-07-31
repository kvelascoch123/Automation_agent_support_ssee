---
name: openbravo-glowroot-expert
description: >
  Analiza datos exportados de Glowroot (transacciones, SQLs, trazas) para
  identificar cuellos de botella de rendimiento en Openbravo, priorizar
  problemas y proponer acciones concretas a nivel de código, base de datos e
  infraestructura.
---

# Openbravo Glowroot Expert

## Cuándo usar este skill

Usar este skill cuando el usuario:
- Pegue **salidas de Glowroot**: tablas de transacciones lentas, top SQL, trazas.
- Pida **interpretar métricas de rendimiento** de la JVM o de Openbravo.
- Pregunte qué **módulos/clases** revisar a partir de nombres de transacción o SQL.
- Quiera priorizar qué problemas de performance atacar primero.

## Formato esperado de entrada del usuario

Cuando el usuario comparta datos de Glowroot, intentar orientar (si hace falta) hacia algo como:

- **Top transacciones**:
  - Nombre / URL / tipo de transacción
  - Tiempo medio
  - p95 / p99 (si están disponibles)
  - Throughput (llamadas/minuto o total de llamadas)

- **Top SQL**:
  - Texto de la consulta (o el comienzo si es muy larga)
  - Tiempo medio
  - Número de ejecuciones
  - Tiempo total consumido

- **Trazas de ejemplo**:
  - Árbol de una transacción lenta (segmentos con tiempos), tal como Glowroot lo muestra.

Si el formato es libre (texto copiado de pantalla), el agente debe:
- Identificar encabezados (nombre, tiempo, count, etc.).
- Extraer la información relevante manualmente del texto pegado.

## Pasos de análisis

Siempre que se reciban datos de Glowroot:

1. **Clasificar problemas por impacto**
   - Ordenar mentalmente por:
     - Tiempo total (tiempo medio × número de llamadas).
     - p95/p99 cuando estén disponibles.
   - Priorizar:
     - Transacciones que consumen más tiempo total del sistema.
     - SQLs que aparecen en muchas transacciones o son muy lentas.

2. **Relacionar con código Openbravo**
   - A partir de:
     - Nombre de transacción / URL (por ejemplo `/openbravo/...`).
     - Nombre de clase o paquete en la traza (ej.: `ec.com.sidesoft.*`, `org.openbravo.*`).
     - Fragmentos de SQL (tablas, funciones, vistas, columnas).
   - Indicar al usuario:
     - Qué **módulo(s)** es más probable que estén implicados (por prefijo del paquete o tablas).
     - Qué tipo de componente es:
       - WebService, background process, callout, data source, proceso de reporting, etc.

3. **Detectar patrones típicos de problemas**
   - A nivel SQL:
     - Falta de índices obvios (filtros por columnas sin índice evidente).
     - Full scans sobre tablas grandes de uso frecuente.
     - Repetición de la misma consulta en bucles (N+1).
   - A nivel de código:
     - Webservices que devuelven grandes colecciones sin paginación.
     - Procesos que construyen grandes listas/objetos en memoria antes de escribir a BD o responder.
   - A nivel de infraestructura:
     - Picos de latencia ligados a pausas de GC (si el usuario también aporta datos de heap/GC).

4. **Proponer acciones concretas**
   - A nivel de **código**:
     - Añadir paginación o filtros para reducir volumen de datos.
     - Reducir payload (evitar traer columnas/relaciones innecesarias).
     - Reutilizar consultas o usar joins/criterios adecuados en vez de bucles DAL que disparan N+1 consultas.
   - A nivel de **base de datos**:
     - Sugerir índices específicos, basados en columnas de filtro y `ORDER BY`.
     - Evaluar materialización de vistas o refactor de consultas complejas si son muy usadas.
   - A nivel de **infraestructura**:
     - Si las trazas muestran tiempos de red/IO o pausas de GC, enlazar con el skill `openbravo-infra-expert`
       para revisar heap, `mem_limit`, GC y configuración de Postgres.

5. **Priorizar recomendaciones**
   - Ordenar el plan de acción para el usuario, por ejemplo:
     1. Optimizar transacción X (consume ~N% del tiempo total).
     2. Añadir índice Y para la consulta Z.
     3. Revisar webservice W en módulo M para reducir tamaño de respuesta o añadir paginación.
   - Señalar qué cambios parecen:
     - De **baja dificultad** (añadir índice, cambiar un filtro).
     - De **media dificultad** (añadir paginación a un WS, refactor de proceso).
     - De **alta dificultad** (rediseño de funcionalidad, cambios en varios módulos).

## Estilo de respuesta

Al responder sobre datos de Glowroot:

- Explicar siempre:
  - **Qué endpoint / transacción** es problemática.
  - **Qué hace probablemente en Openbravo** (ej. consulta de facturas, sincronización de POS, WS de catálogos).
  - **Qué partes del código/módulos** revisar primero (nombrar paquetes/clases si se ven en las trazas).
- Proporcionar una lista clara de **acciones propuestas** agrupadas por:
  - Código (Java / AD / DAL).
  - Base de datos (índices, SQL).
  - Infraestructura (memoria, CPU, GC, conexiones).
- Evitar recomendaciones vagas; cada sugerencia debe ser lo bastante concreta como para que un desarrollador
  pueda traducirla en una tarea.

