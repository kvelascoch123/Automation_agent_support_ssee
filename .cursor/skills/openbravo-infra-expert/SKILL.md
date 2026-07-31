---
name: openbravo-infra-expert
description: >
  Guía para razonar sobre infraestructura y rendimiento de Openbravo en Docker:
  límites de memoria/CPU, parámetros de JVM y PostgreSQL, y buenas prácticas
  específicas del entorno de este proyecto. Úsalo cuando el usuario hable de
  servidores, contenedores, memoria, CPU, OOM, docker-compose o configuración
  de base de datos.
---

# Infraestructura Openbravo (Docker)

## Cuándo usar este skill

Usar este skill cuando:
- El usuario hable de **performance**, **memoria**, **CPU**, **OOM**, **docker-compose**,
  **Tomcat**, **PostgreSQL**, **servidores** o **capacidad de la máquina**.
- Se vayan a proponer cambios en:
  - `docker-compose.yml`
  - Dockerfile(s) de Tomcat o Postgres
  - Parámetros de JVM (`JAVA_OPTS`, `CATALINA_OPTS`)
  - Parámetros de PostgreSQL (`shared_buffers`, `effective_cache_size`, etc.).

## Principios generales

1. **Respetar los límites físicos del servidor**
   - Nunca proponer `Xmx` mayor al **50–60% de la RAM física** de la máquina.
   - Sumar siempre memoria de:
     - Heap (`Xmx`)
     - Metaspace, stacks de hilos, buffers nativos
     - Otros contenedores (Postgres, nginx, etc.)
     - Sistema operativo.

2. **Separar memoria por capas**
   - Para un único host con Tomcat + PostgreSQL:
     - Reservar al menos **30% de la RAM** para el sistema operativo y cachés.
     - Repartir el resto entre:
       - JVM (heap + nativo)
       - PostgreSQL (shared_buffers + procesos).

3. **Evitar que el kernel mate procesos (OOM del sistema)**
   - Preferir ajustar **heap de Java (`Xmx`)** y parámetros de Postgres antes de tocar
     `mem_limit` del contenedor.
   - Si hay `dmesg: Out of memory: Killed process java`:
     - Reducir `Xmx`.
     - Reducir `shared_buffers` y `max_connections` en Postgres.
     - Bajar `mem_limit` si está igual o mayor que la RAM física.

4. **Usar límites de Docker razonables**
   - `mem_limit` del contenedor Tomcat ≈ `Xmx` + 30–50%.
   - `cpus` según núcleos físicos compartidos:
     - No asignar más `cpus` sumados que núcleos físicos/virtuales del host.

5. **Priorizar estabilidad sobre rendimiento máximo**
   - Ante la duda, elegir configuraciones que eviten OOM aunque sacrifiquen
     algo de throughput.

## Pasos al analizar un problema de rendimiento/OOM

1. **Leer la configuración actual**
   - Revisar `docker-compose.yml` y Dockerfiles relevantes.
   - Identificar:
     - `mem_limit`, `cpus`
     - `JAVA_OPTS`, `CATALINA_OPTS`
     - Variables de entorno de Postgres (sobre todo `POSTGRESQL_EXTRA_FLAGS`).

2. **Relacionar con la capacidad del servidor**
   - Preguntar (o usar la info del usuario) sobre:
     - RAM total
     - Núcleos CPU
     - Otros servicios en la misma máquina.

3. **Detectar configuraciones peligrosas típicas**
   - `Xmx` > 60% de la RAM física.
   - `mem_limit` del contenedor ≈ RAM física o superior.
   - Postgres con:
     - `shared_buffers` > 25–30% de la RAM física.
     - `max_connections` exageradamente alto (ej. 1000 sin necesidad real).

4. **Proponer ajustes concretos**
   - Reducir `Xmx` y alinear `mem_limit`.
   - Reducir buffers de Postgres si compite con la JVM.
   - Añadir límites de `cpus` en servicios Docker.
   - Activar logs de GC en JVM para futuras investigaciones.

5. **No asumir que se puede ampliar hardware**
   - Primero optimizar parámetros de Docker/JVM/BD.
   - Solo sugerir ampliación de RAM/CPU cuando:
     - Configuración ya es razonable.
     - Carga de trabajo medida supera claramente la capacidad.

## Ejemplo de razonamiento (8GB RAM, 4 CPU)

- RAM física: 8GB.
- Recomendación inicial genérica:
  - JVM:
    - `-Xms` alrededor de 2 GB
    - `-Xmx` alrededor de 4 GB
    - `mem_limit` de Tomcat ≈ 6 GB.
  - PostgreSQL (si comparte host):
    - `shared_buffers` entre 512MB y 768MB.
    - `effective_cache_size` alrededor de 2–3× `shared_buffers`.
    - `max_connections` ajustado al uso real (ej. 200–300).

## Cómo usar información adicional del usuario

Cuando el usuario dé detalles del servidor, la configuración y el código:
- Tomar esa información como **fuente de verdad** para:
  - Dimensionar heap y `mem_limit`.
  - Dimensionar buffers de Postgres.
  - Identificar módulos personalizados (por ejemplo `sidesoft`, `custom`, etc.) donde buscar:
    - Webservices que devuelven grandes volúmenes de datos.
    - Background processes que recorren muchas filas sin paginación.
    - Consultas SQL sin `LIMIT` que construyen listas grandes en memoria.
- Documentar siempre en la respuesta:
  - Suposiciones hechas.
  - Cómo la configuración propuesta se relaciona con:
    - RAM física
    - Número de CPUs
    - Número de contenedores y su rol.

