# Playbook — Accesos, roles y permisos en Openbravo

## Cuándo aplica
El usuario no ve una ventana, pestaña o botón; pide permisos para un rol; pide un usuario de solo lectura o un usuario nuevo.

## Investigación obligatoria
1. Identificar usuario, rol con el que ingresa y la ventana/pestaña/botón exacto (captura).
2. Consultar en BD la configuración del rol: acceso a ventana (lectura/escritura), acceso a procesos del botón, acceso a organizaciones, campo **Avanzado** del rol y preferencias de sesión como `ShowAcct` (mostrar pestañas de contabilidad).
3. **Comparar contra roles hermanos** que sí ven la función (motor Paso 2.7): el rol del caso suele ser la excepción en un solo campo (KB 464: rol con Avanzado = No, a diferencia de los demás roles contables).
4. Si la función depende de un módulo, confirmar en el código del cliente qué proceso o preferencia la controla.
5. Si el usuario no puede ni ingresar al sistema, no es un problema de rol: tratarlo como acceso/infraestructura y derivarlo.

## Causas conocidas (hipótesis a verificar)
- Acceso de lectura/escritura a la ventana sin rol Avanzado ni preferencia `ShowAcct` → no aparecen el botón Contabilizado ni la pestaña Contabilidad (KB 464).
- "Solo lectura" en la ventana no bloquea botones de proceso (Completar, Anular, Reactivar, Contabilizar); para un usuario de solo consulta hay que retirar también esos accesos (KB 411).

## Solución habitual
- Pasos de configuración del rol en §7 (ventana de roles, campo o pestaña exacta confirmada), pidiendo al usuario cerrar sesión y volver a ingresar; probar con un documento real.
- Usuario de solo lectura: rol dedicado con ventanas en solo lectura, sin procesos, con alcance organizacional confirmado con el cliente (KB 411).

## Qué NO hacer
- El agente **nunca crea usuarios, contraseñas ni credenciales**, ni las incluye en un comentario. Solo indica la configuración; la creación la hace un consultor.
- Dar permisos más amplios que los pedidos, o a todas las organizaciones sin confirmación.

## Asignación sugerida
Consultor.
