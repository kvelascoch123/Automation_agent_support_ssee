# Playbook — Consulta de estructura de base de datos

## Cuándo aplica
El usuario pide los nombres de tablas o columnas que corresponden a una ventana o a sus campos, normalmente para construir un reporte o una vista (tickets 8813, 8779, 8733).

## Investigación obligatoria
1. Identificar la ventana y la pestaña exactas (captura o texto). Si la captura muestra una pestaña secundaria, tratarla por separado.
2. Resolver en el Application Dictionary la tabla de cada pestaña y la columna de cada campo visible: en el código del cliente (`AD_TAB`, `AD_FIELD`, `AD_COLUMN` del módulo) o por consulta de solo lectura en la BD del cliente (`ad_window`, `ad_tab`, `ad_field`, `ad_column`, `ad_table`).
3. Confirmar con `pg_describe_table` que cada columna existe con ese nombre en la BD viva, incluidas las columnas `EM_*` de módulos del cliente.
4. Para campos calculados o que vienen de otra tabla (referencias), indicar la tabla y columna de origen y la columna de enlace.

## Solución habitual
Tabla de equivalencias: etiqueta del campo en pantalla → tabla → columna → observación (clave foránea, calculado, lista de valores). En este tipo de ticket los nombres técnicos **son la respuesta pedida**, por eso se incluyen en la respuesta al usuario (excepción a la regla de §7). Nunca se incluyen credenciales, datos de otros clientes ni consultas que escriban.

## Qué NO hacer
- Dar nombres de columnas "de memoria" sin confirmarlos en el esquema del cliente.
- Ejecutar consultas sobre datos de producción sin `WHERE` ni `LIMIT` para "mostrar ejemplos".

## Asignación sugerida
Técnico (NRIVADENEIRA o DCAZA, según la regla de 6.4).
