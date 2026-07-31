# Casos de Uso Estándar — Openbravo ERP

> **Versión:** 1.0  
> **Alcance:** Aplicable a cualquier empresa comercial, distribuidora o de servicios implementando Openbravo ERP.  
> **Nota metodológica:** Este documento describe los casos de uso genéricos del estándar Openbravo. Los flujos aplican independientemente del sector o industria del cliente. Los nombres de roles son funcionales y deben adaptarse a la estructura organizacional de cada empresa.

---

## Índice

1. [Módulo de Compras](#1-módulo-de-compras)
2. [Módulo de Inventarios](#2-módulo-de-inventarios)
3. [Módulo de Ventas](#3-módulo-de-ventas)
4. [Módulo de Tesorería — Pagos](#4-módulo-de-tesorería--pagos)
5. [Módulo de Tesorería — Cobros](#5-módulo-de-tesorería--cobros)
6. [Módulo CRM](#6-módulo-crm)
7. [Módulo de Mantenimiento](#7-módulo-de-mantenimiento)
8. [Módulo de Calidad — Reportes](#8-módulo-de-calidad--reportes)
9. [Módulo de Nómina](#9-módulo-de-nómina)
10. [Módulo de Activos Fijos](#10-módulo-de-activos-fijos)
11. [Módulo de Contabilidad](#11-módulo-de-contabilidad)
12. [Módulo de Producción](#12-módulo-de-producción)
13. [Reportería y Dashboards](#13-reportería-y-dashboards)

---

## 1. Módulo de Compras

El módulo de compras gestiona el ciclo completo de aprovisionamiento: desde la identificación de la necesidad hasta el registro contable de la factura del proveedor y su pago. Cubre compras de materias primas, insumos, servicios, activos fijos y suministros generales.

---

### 1.1 Necesidad de Materiales (General)

**Rol responsable:** Jefe de Área / Responsable de Bodega / Jefe de Producción  
**Tipo de documento:** Necesidad de Materiales (`NM`)  
**Descripción del proceso:**

El área solicitante identifica la necesidad de adquirir un bien o servicio. El proceso puede originarse por:

- Proyección de consumos históricos (comparación de inventario inicial + entradas − salidas).
- Solicitud directa del área responsable cuando el stock es insuficiente.
- Requerimiento del área administrativa (RRHH, mantenimiento, servicios generales).

**Flujo:**

1. El responsable del área genera el documento de necesidad de materiales en el sistema.
2. La necesidad pasa a un estado pendiente de aprobación.
3. El aprobador (Gerencia o Jefe de Compras según el monto) revisa y aprueba la necesidad.
4. Una vez aprobada, el área de compras convierte la necesidad en un pedido de compra.

**Variantes por tipo de compra:**

| Tipo de Compra | Rol Solicitante | Rol Aprobador |
|---|---|---|
| Materia prima / Insumos productivos | Jefe de Producción / Bodeguero | Jefe de Compras |
| Materiales de mantenimiento | Encargado de Mantenimiento | Gerencia (si supera monto mínimo) |
| Uniformes / RRHH | Responsable de RRHH | Gerencia |
| Cafetería / Suministros generales | Responsable de Cocina / Servicios | Jefe de Compras |

**Observaciones:**
- Si el mismo usuario que genera la necesidad es quien la aprueba y realiza el pedido, se puede configurar para que realice el pedido directamente, omitiendo el paso intermedio de aprobación de necesidad.
- Se recomienda una alerta de notificación cuando una necesidad está pendiente de aprobación.

---

### 1.2 Pedido de Compra

**Rol responsable:** Responsable de Compras  
**Tipo de documento:** Pedido de Compra (`PC`)  
**Descripción del proceso:**

El área de compras transforma la necesidad aprobada en un pedido formal al proveedor. Para compras menores o de carácter administrativo, el pedido puede crearse directamente sin necesidad previa.

**Tipos de compra que pueden gestionarse mediante pedido directo:**

- Compras administrativas (suministros de oficina, servicios básicos: agua, luz, teléfono, internet).
- Compras de servicios (contratos de servicio, mantenimiento externo).
- Compras de activos fijos.
- Compras de alimentos para el personal.
- Compras de combustible y mantenimiento de vehículos.
- Compras a terceros para reventa (productos complementarios no fabricados por la empresa).
- Compras de uniformes e implementos de seguridad industrial.

**Flujo:**

1. El responsable de compras crea el pedido de compra referenciando la necesidad aprobada (o directamente si aplica).
2. Se selecciona el proveedor, productos, cantidades y condiciones de entrega.
3. El pedido queda confirmado y se envía al proveedor.
4. Se realiza el seguimiento del pedido hasta la recepción del bien o servicio.

---

### 1.3 Recepción de Mercancía (Albarán Proveedor)

**Rol responsable:** Bodeguero / Asistente de Compras  
**Tipo de documento:** Albarán de Recepción / Recepción (`RP`)  
**Descripción del proceso:**

Al recibir la mercancía, el bodeguero encargado valida la entrega contra el pedido de compra y genera el albarán de recepción en el sistema.

**Flujo:**

1. El proveedor entrega la mercancía en el almacén o punto de recepción designado.
2. El bodeguero verifica físicamente las cantidades, condiciones y lotes de los productos recibidos.
3. Se registra el albarán de recepción en el sistema, vinculado al pedido de compra correspondiente.
4. Se registran los atributos del producto recibido cuando aplica (lote, fecha de elaboración, fecha de caducidad).
5. Si existe discrepancia entre lo pedido y lo recibido, se genera una alerta de producto no entregado para su seguimiento.
6. El albarán queda en estado validado y desencadena la actualización de inventario.

**Consideraciones:**
- En recepciones de productos controlados por lote, se recomienda definir una estructura de codificación estándar para los lotes de entrada.
- Los atributos de lote (fecha de elaboración, fecha de caducidad) deben ser campos obligatorios cuando el producto así lo requiera.
- Se debe validar la posibilidad de modificar los secuenciales automáticos de atributos según la política de cada empresa.

---

### 1.4 Calificación de Proveedores

**Rol responsable:** Responsable de Compras / Calidad  
**Tipo de documento:** Calificación de Proveedor (`CCP`)  
**Descripción del proceso:**

El área de compras registra las condiciones de recepción de materias primas o insumos y evalúa el desempeño del proveedor en cada entrega.

**Flujo:**

1. Al momento de la recepción o posterior a ella, el responsable completa un checklist de condiciones de recepción, que incluye: proveedor, fecha de recepción, fecha de pedido, cantidad pedida, ítems pedidos, precio, fechas de elaboración y caducidad.
2. Se asigna una calificación al proveedor por cada albarán de recepción.
3. La calificación se realiza ítem por ítem, permitiendo evaluar productos de manera individual.
4. Las calificaciones se acumulan para generar un historial de evaluación por proveedor.

**Reportes relacionados:**
- Reporte de evaluación y reevaluación de proveedores (filtros: fecha desde, fecha hasta, proveedor, producto; formatos de salida: Excel, PDF, HTML).

**Observaciones:**
- Los formatos de calidad de recepción se mantienen en el estándar de Openbravo, adaptando las preguntas o actividades al checklist de verificación de la empresa.
- La evaluación de calificación debe poder realizarse directamente desde el albarán de proveedor.

---

### 1.5 Prueba Controlada de Nuevo Lote

**Rol responsable:** Responsable de Compras / Calidad  
**Tipo de documento:** Prueba Controlada de Nuevo Lote (`PCNL`)  
**Descripción del proceso:**

Cuando ingresa un lote nuevo de un insumo o materia prima, se puede realizar una prueba controlada opcional (no bloqueante) antes de autorizar su uso en producción o distribución. Este proceso es evaluativo tanto para el proveedor como para el producto.

**Flujo:**

1. El responsable identifica el ingreso de un nuevo lote.
2. Se genera el documento de prueba controlada registrando: número de lote, fecha de elaboración, fecha de caducidad, cantidad recibida, resultado de la evaluación del proveedor y del producto.
3. La prueba se ejecuta y los resultados se registran en el sistema.
4. El documento queda relacionado al albarán de recepción correspondiente.
5. El estado de calidad (realizada / pendiente) debe ser visible en el encabezado del albarán.

**Observaciones:**
- Esta prueba no es bloqueante; el producto puede usarse mientras se procesa la evaluación.
- Se debe crear un tipo de documento específico en la ventana de Toma de Datos del sistema para manejar los secuenciales de estas pruebas.

---

### 1.6 Control de Peso en Recepción de Insumos

**Rol responsable:** Bodeguero de Insumos  
**Descripción del proceso:**

Para insumos que se comercializan o consumen por peso, el sistema debe permitir capturar el peso real en el momento de la recepción, ya sea de forma manual o integrada con una balanza electrónica.

**Flujo:**

1. Al recibir el insumo, el bodeguero accede al módulo de recepción.
2. El sistema permite ingresar el peso capturado (manual o desde balanza integrada).
3. El peso registrado actualiza la cantidad real recibida en el albarán.

---

### 1.7 Reporte de Existencias de Materia Prima por Lote

**Rol responsable:** Jefe de Compras / Responsable de Inventario  
**Descripción:** Reporte que muestra las existencias actuales de materia prima agrupadas por código de compra o lote. Permite la trazabilidad de los insumos en stock.

---

### 1.8 Factura de Compra

**Rol responsable:** Contabilidad / Responsable de Compras  
**Tipos de documento:** Factura Compra (`FC`)  
**Descripción del proceso:**

Una vez recibida la mercancía o el servicio, el área de contabilidad registra la factura del proveedor en el sistema, vinculándola al albarán de recepción correspondiente.

**Flujo:**

1. Se recibe la factura física o electrónica del proveedor.
2. El responsable de contabilidad registra la factura en el sistema, vinculando el albarán de recepción.
3. La factura queda en estado pendiente de pago y genera las cuentas por pagar correspondientes.

**Tipos de compra que generan facturas:**
- Compra de productos (inventariables y no inventariables).
- Compra de servicios.
- Compra de activos fijos.

---

### 1.9 Nota de Crédito de Proveedor

**Rol responsable:** Contabilidad  

| Tipo | Código | Descripción |
|---|---|---|
| Nota de Crédito Financiera | `NCF` | Por descuentos otorgados por el proveedor o cuando no se recibe la totalidad del producto acordado. |
| Nota de Crédito por Devolución | `NCD` | Por devolución de productos en mal estado, que no pasaron pruebas de calidad o entregados incorrectamente. |

**Flujo:**

1. Se identifica la causa de la nota de crédito (descuento comercial, devolución, diferencia en cantidad).
2. El área de contabilidad registra la nota de crédito vinculada a la factura de compra original.
3. La nota de crédito reduce el saldo pendiente de pago al proveedor.

---

## 2. Módulo de Inventarios

El módulo de inventarios gestiona el control de existencias en todos los almacenes de la empresa, los movimientos entre ellos, los ajustes autorizados y la trazabilidad de los productos mediante guías de remisión.

---

### 2.1 Configuración de Almacenes

**Rol responsable:** Responsable de Inventario / Administrador del Sistema  
**Descripción:**

Antes de operar el módulo de inventarios, se deben configurar los almacenes que la empresa requiere según su estructura operativa. Los tipos de almacén recomendados son:

| Tipo de Almacén | Descripción |
|---|---|
| Almacén de Materia Prima | Almacenamiento de insumos y materiales productivos. |
| Almacén de Producto Terminado | Almacenamiento de productos listos para distribución o venta. |
| Almacén de Suministros | Químicos de limpieza, embalajes, uniformes, suministros de oficina. |
| Almacén de Mantenimiento | Repuestos, herramientas, maquinaria de reserva. |
| Almacén de Producto No Conforme | Productos rechazados en control de calidad. |
| Almacenes de Tránsito | Almacenes virtuales para control de movimientos entre ubicaciones. |
| Puntos de Venta / Locales Comerciales | Almacenes de los puntos de venta. |
| Cuartos Fríos / Cámaras | Almacenes de temperatura controlada (si aplica). |

**Observaciones:**
- Los almacenes de tránsito permiten controlar el inventario durante el movimiento entre locaciones.
- Se deben configurar todos los almacenes necesarios antes del go-live del sistema.

---

### 2.2 Ajuste de Inventario

**Rol responsable:** Responsable de Inventario  
**Tipo de documento:** Ajuste de Inventario (`AIF`)  
**Descripción del proceso:**

Permite corregir las existencias en el sistema cuando existen diferencias entre el stock físico y el registrado. Todo ajuste requiere autorización previa de Gerencia.

**Flujo:**

1. El responsable de inventario identifica la diferencia entre stock físico y sistema.
2. Se genera el documento de ajuste de inventario con la justificación correspondiente.
3. El ajuste requiere aprobación del Gerente antes de ser procesado en el sistema.
4. Una vez aprobado, el sistema actualiza las existencias.

**Observaciones:**
- Los ajustes sin autorización no deben ser procesados. Se recomienda un control de aprobación previo integrado en el flujo del sistema.
- Se puede implementar un proceso de inventario ciego para mayor control.

---

### 2.3 Transferencia Interna entre Almacenes

**Rol responsable:** Responsable de Inventario / Bodeguero  
**Tipos de documento:** Transferencia Interna (`TI`)  
**Descripción del proceso:**

Permite mover mercancía entre los distintos almacenes de la empresa (entre bodegas de producción, entre locales, entre plantas y oficinas, etc.).

**Flujo:**

1. Se crea el documento de transferencia interna especificando el almacén de origen, el almacén de destino y los productos con sus cantidades.
2. Se emite la guía de remisión interna para respaldar el traslado físico.
3. El almacén de destino recepciona la mercancía y confirma la recepción en el sistema.
4. El inventario se actualiza en ambos almacenes.

---

### 2.4 Guía de Remisión

**Rol responsable:** Responsable de Inventario / Facturación  
**Tipo de documento:** Guía de Remisión (`GR`)  
**Descripción del proceso:**

Documento tributario y logístico que respalda el traslado de mercancía entre ubicaciones de la empresa o hacia clientes.

**Flujo:**

1. Se genera la guía de remisión vinculada a la transferencia interna o a la factura de venta.
2. La guía especifica el origen, destino, productos, cantidades y transportista.
3. El transportista o responsable del traslado lleva la guía impresa durante el movimiento.
4. En el destino, el receptor firma la guía de conformidad.

---

### 2.5 Recepción de Transferencia

**Rol responsable:** Bodeguero del Almacén Destino  
**Tipos de documento:** Recepción de Transferencia (`RT`)  
**Descripción del proceso:**

El almacén receptor confirma en el sistema la llegada del producto enviado mediante una transferencia interna.

**Flujo:**

1. El bodeguero destino verifica físicamente los productos recibidos contra la guía de remisión.
2. Se registra la recepción en el sistema, vinculada a la transferencia correspondiente.
3. El stock del almacén destino se actualiza automáticamente.

---

### 2.6 Impresión de Etiquetas de Productos

**Rol responsable:** Responsable de Inventario  
**Descripción:** El sistema permite imprimir etiquetas de los productos recibidos directamente desde el albarán de proveedor o desde la recepción de transferencia. Las etiquetas incluyen información de lote, código de producto y fechas relevantes.

---

### 2.7 Control de Bienes de Control (Activos Menores)

**Rol responsable:** Responsable de Inventario / Contabilidad  
**Descripción del proceso:**

Los bienes de control son activos menores que no califican como activos fijos contables pero que deben ser controlados físicamente (por ejemplo: contenedores, pallets, herramientas, equipos reutilizables de terceros).

**Flujo:**

1. Los bienes de control se gestionan con stock en el sistema, asignándoles almacenes específicos.
2. Los movimientos entre almacenes permiten dar stock a cada ubicación.
3. Los bienes deteriorados o perdidos se registran con el costo correspondiente.
4. Las facturas periódicas de terceros por préstamo de bienes (por ejemplo, contenedores de distribuidores) se registran en compras con una cuenta contable específica.

---

### 2.8 Reporte de Movimientos de Inventario

**Rol responsable:** Responsable de Inventario  
**Descripción:** Reporte que muestra los movimientos de inventario por producto y almacén, incluyendo: saldo inicial, entradas, salidas, saldo final y mermas. Los filtros deben definirse en coordinación con el área de producción cuando aplique.

---

## 3. Módulo de Ventas

El módulo de ventas gestiona el ciclo completo desde la captación del cliente hasta la entrega del producto y el cobro, incluyendo los canales institucional, distribuidores, consumo directo, venta a provincias y puntos de venta (POS).

---

### 3.1 Gestión Comercial y Prospección

**Rol responsable:** Equipo Comercial / Administración  
**Tipo de documento:** Prospecto de Venta / Muestra (`PVM`)  
**Descripción del proceso:**

La prospección comercial permite identificar nuevos clientes potenciales, asignarlos a vendedores y gestionar el proceso de acercamiento hasta la primera compra.

**Flujo:**

1. El equipo comercial identifica prospectos de clientes con potencial de compra.
2. Los prospectos se distribuyen entre los vendedores según criterios de experiencia y zona geográfica.
3. El vendedor realiza el acercamiento: levanta información sobre las necesidades del cliente, tipos de productos que consume, etc.
4. Si el prospecto muestra interés, se programa el envío de muestras.
5. Se genera un pedido interno de muestra y se emite una salida de inventario a nombre de la empresa.
6. El vendedor realiza la entrega al prospecto y obtiene firma de recepción de muestra.

---

### 3.2 Creación de Clientes

**Rol responsable:** Administración / Asistente Comercial  
**Descripción del proceso:**

1. Se recopila la información del nuevo cliente (datos fiscales, RUC, contactos).
2. Se solicita la documentación habilitante (RUC, solicitud de crédito si aplica).
3. Se crea el cliente en el sistema con su lista de precios, condiciones de pago, descuentos y comisiones de vendedor asignadas.
4. Se crea una carpeta o expediente del cliente (físico o digital) con toda la información comercial.

---

### 3.3 Pedido de Venta — Canal Institucional / Distribuidores

**Rol responsable:** Vendedor / Administración  
**Tipo de documento:** Pedido de Venta Institucional (`PDVI`)  
**Descripción del proceso:**

**Preventa:**

1. El vendedor realiza la preventa mediante visita en sitio o llamada telefónica (hasta las 20:00 del día de corte).
2. Se registra el canal de toma de pedido: presencial, telefónico o correo electrónico.
3. El pedido se carga en el sistema con los productos, cantidades y condiciones solicitadas por el cliente.

**Consideraciones:**
- El sistema debe permitir bloquear pedidos de clientes con cartera vencida.
- El canal de toma de pedido debe quedar registrado en el documento.

---

### 3.4 Facturación y Despacho — Canal Institucional

**Rol responsable:** Facturador / Bodeguero / Transportista  
**Tipos de documento:** Factura de Venta (`001-002`), Guía de Remisión  
**Descripción del proceso:**

1. El bodeguero prepara físicamente los pedidos según la guía de despacho impresa, anotando lotes, cantidades y bodega de despacho.
2. El facturador toma el documento físico anotado y realiza el despacho en el sistema, emitiendo la factura electrónica.
3. Los productos se cargan al transporte con verificación contra la factura de venta.
4. El transportista realiza la entrega en la ruta asignada.
5. El cliente firma la guía de remisión como constancia de recepción.
6. Si el cliente realiza un pago en el momento de la entrega, el transportista lo registra en el sistema.

---

### 3.5 Pedido de Venta — Canal Consumo Directo (Domicilio)

**Rol responsable:** Vendedor / Call Center  
**Tipo de documento:** Pedido de Venta Consumo (`PDVC`)  
**Descripción del proceso:**

La venta de consumo directo corresponde a ventas de contado (efectivo o transferencia) a precio de venta al público. Los clientes realizan el pedido directamente al vendedor o a la oficina.

**Características:**
- Precio: PVP (lista de precios de consumo).
- Forma de pago: contado obligatorio (no se entrega sin pago).
- Logística: reparto con flota propia de la empresa.
- Comisiones: aplican cuando el pedido es tomado por un vendedor.
- Seguimiento: mismo flujo que la venta institucional.

---

### 3.6 Pedido de Venta — Canal Provincia / Encomienda

**Rol responsable:** Vendedor / Administración  
**Tipo de documento:** Pedido de Venta Institucional (`PDVI`)  
**Descripción del proceso:**

Se maneja como venta institucional pero con un cargo adicional de flete por el envío. La entrega se realiza a través de empresas de encomienda.

**Características:**
- El costo de logística se incluye como una línea adicional en la factura de venta.
- En la guía de remisión se especifica que la entrega es por encomienda, con dirección y datos del destinatario.
- El pedido debe registrar la información de entrega por encomienda.
- Para zonas especiales (envíos en cadena de frío), se deben usar empaques térmicos y consignar en la guía.

---

### 3.7 Ventas en Punto de Venta (POS) — Retail

**Rol responsable:** Cajero / Vendedor de Local  
**Tipos de documento:** Pedido POS, Albarán POS, Factura POS  
**Descripción del proceso:**

Las ventas en locales comerciales o puntos de venta se gestionan mediante el módulo POS de Openbravo.

**Tipos de venta en POS:**
- Venta de productos empaquetados propios y de terceros.
- Venta de platos preparados y/o alimentos (con receta asociada).
- Venta de combos o productos compuestos (lista de materiales).

**Flujo:**

1. El cajero/vendedor registra los productos en el POS.
2. El sistema aplica automáticamente las listas de precio, descuentos y promociones vigentes.
3. Se emite la factura electrónica o la nota de venta según corresponda.
4. El cierre de caja se realiza al final del turno o del día.

---

### 3.8 Gestión de Recetas / Listas de Materiales (BOM)

**Rol responsable:** Administración / Producción  
**Descripción del proceso:**

Los productos compuestos (combos, platos preparados, kits) requieren una lista de materiales (BOM) o receta que defina sus componentes y proporciones.

**Flujo:**

1. La administración o producción crea la receta/BOM del producto compuesto.
2. Se asignan los componentes con sus cantidades.
3. El sistema calcula el costo total del producto compuesto en función de los costos de sus componentes.
4. En el punto de venta, al facturar un producto compuesto, el sistema descuenta automáticamente los componentes del inventario.

**Reportes relacionados:**
- Reporte de listas de materiales (BOM) con costo por producto compuesto.

---

### 3.9 Descuentos y Promociones

**Rol responsable:** Administración Comercial  
**Descripción del proceso:**

El sistema permite gestionar diferentes tipos de descuentos y promociones:

| Tipo | Descripción |
|---|---|
| Descuento por porcentaje | Descuento de X% sobre el precio de un producto específico. |
| Promoción 2x1 | Se propone la creación de combos de tipo LDM para gestionar este tipo de promoción. |
| Producto gratis por compra | Combinación de productos donde la compra de uno habilita un regalo. Se gestiona mediante combos. |
| Visualización de promoción | El POS debe mostrar las promociones vigentes aplicables al pedido en curso. |

**Observaciones:**
- Para que los combos y promociones funcionen correctamente, deben crearse como productos de tipo BOM y atarse a la lista de surtido de los puntos de venta correspondientes.

---

### 3.10 Control de Entregas — Logística

**Rol responsable:** Transportista / Responsable de Logística  
**Descripción del proceso:**

Los pedidos facturados deben ser entregados a los clientes. Para ello se utiliza un módulo o aplicación web de gestión de rutas.

**Flujo:**

1. Los pedidos facturados se marcan como "listos para entregar".
2. Se organizan por camión/ruta en la plataforma de gestión de rutas.
3. Se definen las zonas de entrega por polígonos geográficos.
4. El transportista realiza la entrega y confirma en la aplicación móvil.
5. La confirmación de entrega es visible para todo el equipo administrativo en tiempo real.

---

### 3.11 Gestión de Presupuesto de Ventas

**Rol responsable:** Contabilidad / Gerencia Comercial  
**Descripción del proceso:**

Se implementa el módulo estándar de presupuesto de Openbravo con ajustes para incluir seguimiento por vendedor.

**Características:**
- Definición de presupuesto general de ventas.
- Seguimiento del presupuesto por vendedor.
- Comparativo presupuesto vs. real.

---

### 3.12 Manejo de Quejas de Clientes

**Rol responsable:** Atención al Cliente / Áreas involucradas (Producción, Calidad, Contabilidad, Mantenimiento)  
**Tipo de documento:** Queja / Caso (`QJ`)  
**Descripción del proceso:**

Se utiliza el módulo de Casos del CRM de Openbravo para gestionar las quejas de clientes.

**Características del flujo:**
- Secuenciales automáticos de casos.
- Clasificación del caso como reclamo o sugerencia.
- Plazos de respuesta automáticos según tipo de caso.
- Asignación automática al área responsable según categoría.
- Campo de acciones a seguir.
- Envío de correo electrónico automático al cliente en función de las acciones registradas.

---

### 3.13 Planificación de Actividades Comerciales

**Rol responsable:** Vendedor / Supervisor Comercial  
**Descripción:** Se utiliza el módulo de Actividades del CRM de Openbravo para planificar y controlar las actividades de los vendedores (visitas, llamadas, seguimientos).

---

### 3.14 Toma de Pedidos en Aplicación Móvil

**Rol responsable:** Vendedor  
**Tipo de documento:** Toma de Pedido de Venta (`TPV`)  
**Descripción:** Los vendedores pueden tomar pedidos de los clientes desde la aplicación móvil de Openbravo (POS en modo móvil), en sitio o en tránsito.

---

### 3.15 Indicadores Comerciales

| Indicador | Descripción |
|---|---|
| % de incremento en ventas | Porcentaje de crecimiento de ventas respecto al período anterior. |
| Evolución de ventas | Comparativo de ventas general, por vendedor y por local o canal. |
| Variación de ventas mensual | Comparativo ventas del mes actual vs. mismo mes del año anterior. |

---

## 4. Módulo de Tesorería — Pagos

El módulo de pagos gestiona todos los flujos de salida de dinero de la empresa, incluyendo pagos a proveedores, obligaciones tributarias y laborales, pagos con tarjeta de crédito empresarial, caja chica y cadenas de valor.

---

### 4.1 Pago con Cheque y/o Transferencia Bancaria (Flujo Estándar)

**Rol responsable:** Contabilidad / Tesorería / Gerencia  
**Tipo de documento:** Propuesta de Pago (`PBNC`)  
**Descripción del proceso:**

**Flujo:**

1. **Preparación:** El área de tesorería organiza las facturas a pagar y prepara la propuesta de pago, que pasa a aprobación de Gerencia (firma física de aprobación).
2. **Registro en sistema:** Se ingresan las transacciones de propuesta de pago en el ERP basándose en los documentos aprobados.
3. **Aprobación en sistema:** El aprobador (Gerencia o nivel autorizado) confirma las propuestas de pago en el sistema.
4. **Ejecución bancaria:** Se ejecutan los pagos en el banco (transferencias). Para pagos por transferencia, se actualiza la referencia bancaria en el pago del sistema una vez confirmada la transacción.

---

### 4.2 Débitos Automáticos (Seguros, Créditos Bancarios)

**Rol responsable:** Tesorería / Contabilidad  
**Tipo de documento:** Pago por Débito (`PDEB`)  
**Descripción del proceso:**

**Flujo:**

1. Se identifican los débitos ejecutados automáticamente en las cuentas bancarias de la empresa (pagos de seguros, cuotas de créditos bancarios, etc.).
2. Se registran en el sistema como pagos con la justificación y concepto correspondiente.
3. Se concilian contra el estado de cuenta bancario.

---

### 4.3 Pagos No Regularizados (Anticipos a Proveedores)

**Rol responsable:** Tesorería / Contabilidad  
**Tipo de documento:** Anticipo a Proveedor (`PANT`)  
**Descripción del proceso:**

Pagos realizados sin una factura previa aprobada (pago anticipado con cheque).

**Flujo:**

1. Se emite el cheque al proveedor.
2. Se verifica el número de cheque y se actualiza la chequera del sistema si es necesario.
3. Se registra en el sistema como un anticipo a nombre del proveedor, con el número de cheque emitido.
4. La documentación del pago se adjunta a la carpeta del proveedor.
5. Cuando llega la factura, se registra en el sistema y se verifica si existen anticipos pendientes de cruzar.
6. Se realiza el cruce del anticipo contra la factura del proveedor.

---

### 4.4 Pagos mediante Cadena de Valor (Factoring Bancario)

**Rol responsable:** Tesorería / Contabilidad  
**Tipo de documento:** Pago Cadena de Valor (`PCV`)  
**Descripción del proceso:**

Mecanismo financiero donde el banco paga al proveedor y la empresa le debe al banco. Permite diferir el pago al proveedor.

**Flujo:**

1. Se realiza el pago de la factura en el sistema financiero del banco.
2. Se ingresa el pago en el ERP usando la cuenta financiera "Cadena de Valor".
3. Se controla periódicamente el saldo y vencimientos de la cuenta financiera Cadena de Valor.
4. Al vencimiento, el banco debita el valor más los intereses. Se registra el pago al banco usando conceptos contables específicos: "Tránsito Cadena de Valor" e "Intereses Cadena de Valor".
5. Se registra la baja de la cuenta financiera Cadena de Valor para cerrar el proceso.

**Configuración requerida:**
- Cuenta financiera: "Cadena de Valor".
- Conceptos contables: "Tránsito Cadena de Valor" e "Intereses Cadena de Valor".

---

### 4.5 Pagos con Tarjeta de Crédito Empresarial

**Rol responsable:** Tesorería / Contabilidad  
**Tipo de documento:** Pago Tarjeta de Crédito (`PTCP`)  
**Descripción del proceso:**

**Flujo:**

1. Se registra la factura de compra pagada con tarjeta de crédito, usando el método de pago correspondiente (Mastercard, Visa, Diners, etc.).
2. Se ingresa el pago en el ERP usando la cuenta financiera de la tarjeta correspondiente.
3. Al llegar el estado de cuenta de la tarjeta, se registra el pago al banco mediante transferencia, usando el concepto contable "Tránsito [Nombre Tarjeta]".
4. Se registra el devengo del valor de la tarjeta desde la cuenta financiera de la tarjeta.
5. Se registran los intereses si aplica, usando el concepto contable "Intereses Tarjeta".

**Configuración requerida:**
- Cuentas financieras por cada tarjeta de crédito.
- Conceptos contables: "Tránsito [Tarjeta]" e "Intereses Tarjeta".

---

### 4.6 Pagos con Concepto Contable (Obligaciones Tributarias y Laborales)

**Rol responsable:** Contabilidad / Tesorería  
**Tipo de documento:** Pago con Concepto Contable (`PCC`)  
**Descripción del proceso:**

Para pagos de obligaciones como IESS, SRI, MRL, nómina, retenciones judiciales, préstamos quirografarios, etc.

**Flujo:**

1. El área responsable (Nómina, Contabilidad) entrega a Tesorería los valores a pagar con el detalle correspondiente.
2. Se realiza el pago desde la cuenta bancaria correspondiente hacia el concepto contable definido.
3. El pago cierra las cuentas por pagar del período.

**Conceptos contables frecuentes:** Retención Judicial, Sueldos por Pagar, Impuesto a la Renta, Préstamos Quirografarios (crear según las necesidades de cada empresa).

---

### 4.7 Pagos con Caja Chica

**Rol responsable:** Responsable de Caja Chica / Tesorería  
**Tipos de documento:** Pago Caja Chica (`PCCH`)  

#### 4.7.1 Pago de Facturas con Caja Chica

**Flujo:**

1. Se registra la factura de compra en el sistema.
2. Se paga la factura usando la cuenta financiera "Caja Chica".
3. Para anticipos a empleados de hasta un monto mínimo establecido, se emite el pago usando el concepto contable "Anticipo Empleados".

#### 4.7.2 Reposición de Caja Chica

**Flujo:**

1. El responsable de caja chica solicita la reposición cuando el fondo baja del mínimo establecido.
2. Se genera la solicitud de reposición en el sistema.
3. Se emite un cheque a nombre de la persona que realizará el cobro en el banco, usando el concepto contable "Caja Chica Tránsito".
4. El responsable de caja chica registra el ingreso de los valores de reposición con el mismo concepto contable.
5. Se evidencia el ingreso del cheque y su cobro en el banco.

**Configuración requerida:**
- Cuenta financiera: "Caja Chica" (con el fondo asignado a cada local o área).
- Conceptos contables: "Anticipo Empleados", "Caja Chica Tránsito", "Reposición Caja Chica".

---

## 5. Módulo de Tesorería — Cobros

El módulo de cobros gestiona todos los ingresos de dinero de la empresa provenientes de ventas a clientes, incluyendo cobros en oficina, cobros en ruta por vendedores o transportistas, cobros en locales POS y gestión de cheques posfechados.

---

### 5.1 Cobros en Oficina / Centro de Distribución

**Rol responsable:** Tesorería / Facturación  
**Tipo de documento:** Cobro en Oficina (`COFI`)  
**Descripción del proceso:**

Clientes que compran directamente en la planta o centro de distribución.

**Flujo:**

1. Se emite la factura de venta al cliente.
2. Se registra el cobro en el sistema según los métodos de pago disponibles (efectivo, cheque, transferencia, tarjeta).
3. Para clientes mayoristas, se imprime el estado de pagos desde el sistema del cliente y se realiza el cobro de las facturas pendientes.

---

### 5.2 Cobros por Vendedores (en Sitio)

**Rol responsable:** Vendedor / Tesorería  
**Tipo de documento:** Cobro por Vendedor (`CVEN`)  
**Descripción del proceso:**

**Flujo:**

1. El vendedor realiza cobros en efectivo y/o cheque durante sus visitas a los clientes.
2. Llena un reporte de cobros con la información necesaria (cliente, factura, valor, forma de pago).
3. Entrega los valores y el reporte en oficina al día siguiente.
4. El área de tesorería sube los estados de cuenta a la cuenta financiera y confirma los cobros.
5. Se genera un reporte de confirmaciones para que los vendedores realicen la gestión de confirmación con los clientes.
6. Los cobros en efectivo y cheque se ingresan al sistema como confirmación de las entregas.

**Observaciones:**
- Los cobros se realizan a través de la aplicación web de cobros en sitio.

---

### 5.3 Cobros por Transportistas (en Ruta)

**Rol responsable:** Transportista / Tesorería  
**Tipo de documento:** Cobro por Transportista (`CTRA`)  
**Descripción del proceso:**

**Flujo:**

1. El transportista realiza cobros de ventas a contado o a crédito durante la ruta de entrega.
2. Llena el reporte de cobros con los valores recibidos.
3. Entrega los valores (efectivo y cheques) en oficina al día siguiente.
4. Los cobros se confirman en el sistema.

---

### 5.4 Cobros en Locales Comerciales (POS)

**Rol responsable:** Cajero / Responsable de Local  
**Descripción del proceso:**

**Flujo:**

1. Se realizan cobros en los diferentes métodos de pago disponibles en el local (efectivo, transferencia, tarjeta de crédito/débito).
2. Al final del turno o día, se realiza el cierre de caja en el POS.
3. El back office confirma los cierres de caja de los locales e interpreta las diferencias.
4. Se realizan los cuadres y depósitos:
   - Valores en efectivo: cuadre y depósito bancario.
   - Valores por transferencia: conciliación con extracto bancario.
   - Valores por tarjeta: cuadre con el voucher de la procesadora.

---

### 5.5 Cobros a Empleados con Crédito

**Rol responsable:** Nómina / Tesorería / Cartera  
**Descripción del proceso:**

Los empleados pueden comprar en los locales comerciales de la empresa a crédito, descontándose el valor de su nómina.

**Flujo:**

1. El empleado compra en cualquier local de distribución con crédito.
2. Se identifican las facturas a crédito del empleado y se totaliza el valor.
3. Nómina realiza los descuentos correspondientes en el rol de pagos.
4. Nómina entrega a Cartera el listado de descuentos por empleado y las facturas asociadas.
5. Cartera cruza los valores usando el concepto contable "Descuentos Empleados Crédito".

**Configuración requerida:**
- Concepto contable: "Descuentos Empleados Crédito".

---

### 5.6 Cobros de Autoconsumos (Muestras, Donaciones, Regalos)

**Rol responsable:** Tesorería / Contabilidad  
**Descripción del proceso:**

Las facturas generadas por autoconsumo (muestras, donaciones, regalos institucionales) no se cobran monetariamente sino que se saldan mediante nota de crédito interna.

**Flujo:**

1. Se emite la factura de autoconsumo.
2. Se genera una nota de crédito por el mismo valor de la factura.
3. Se realiza el cruce entre la factura y la nota de crédito, generando un asiento contable en cero (misma cuenta vs. misma cuenta).

---

### 5.7 Cobros por Cruce con Facturas de Proveedor (Netting)

**Rol responsable:** Cartera / Contabilidad  
**Descripción del proceso:**

Cuando un cliente es también proveedor, se pueden cruzar las facturas de cliente (cuentas por cobrar) con las facturas de proveedor (cuentas por pagar) para liquidar saldos recíprocos.

**Flujo:**

1. Se identifica la factura de cliente que se requiere cobrar.
2. Se cruza con un concepto contable específico para su baja en cuentas por cobrar.
3. Se identifica la factura de proveedor a pagar.
4. Se cruza con el mismo concepto contable para su baja en cuentas por pagar.

**Configuración requerida:**
- Concepto contable: "Cruce Terceros".

---

### 5.8 Control de Cheques Posfechados

**Rol responsable:** Tesorería / Cartera  
**Descripción del proceso:**

**Flujo:**

1. Se reciben cheques posfechados por los diferentes canales de cobranza (vendedores, transportistas, oficina).
2. Se ingresan al sistema registrando la fecha de ingreso y la fecha de confirmación de depósito.
3. Los cobros en estado "A Ejecutar" (pendientes de confirmar) no se consideran en el cálculo de comisiones por vendedor.
4. El responsable de seguimiento verifica periódicamente las fechas de confirmación y ejecuta el proceso de confirmación, actualizando la fecha de cobro.
5. La conciliación bancaria confirma los valores depositados por concepto de cobros en cheque.
6. **Cheque devuelto (protestado):** Si un cheque es devuelto por fondos insuficientes, se genera una Nota de Débito interna al cliente por cheque protestado. Se gestiona la reactivación de las facturas relacionadas y se exige el pago del total incluyendo la nota de débito.

**Configuración requerida:**
- Tipo de documento interno: "ND Cheque Protestado" (no anexo, no aparece en el anexo transaccional).

---

## 6. Módulo CRM

El módulo CRM de Openbravo permite gestionar oportunidades de negocio, actividades comerciales y el seguimiento de relaciones con clientes.

---

### 6.1 Registro de Oportunidades

**Rol responsable:** Vendedor / Equipo Comercial  
**Descripción:** El módulo de oportunidades permite registrar y hacer seguimiento a las oportunidades de negocio identificadas por el equipo comercial. Se recomienda integrarlo con el módulo de actividades para un seguimiento unificado.

---

### 6.2 Registro y Planificación de Actividades

**Rol responsable:** Vendedor / Supervisor Comercial  
**Descripción:** El módulo de actividades permite planificar, asignar y controlar las actividades comerciales (visitas, llamadas, correos, reuniones). Se recomienda integrarlo con el módulo de oportunidades para mantener la trazabilidad del ciclo de ventas.

---

## 7. Módulo de Mantenimiento

El módulo de mantenimiento permite gestionar las órdenes de trabajo preventivo y correctivo sobre la maquinaria y equipos de la empresa.

---

### 7.1 Órdenes de Mantenimiento

**Rol responsable:** Responsable de Mantenimiento / Calidad  
**Descripción del proceso:**

1. Se crean órdenes de mantenimiento programadas por máquina o equipo, según el plan de mantenimiento preventivo.
2. Se asignan las tareas al personal de mantenimiento.
3. El personal ejecuta las tareas y registra su ejecución en el sistema.
4. Se generan alertas de mantenimiento próximo y de calibraciones de equipos.
5. Se controlan los estados de las órdenes (programada, en ejecución, completada).

---

### 7.2 Informe de Orden de Mantenimiento

**Rol responsable:** Responsable de Mantenimiento  
**Descripción:** Permite registrar las tareas asignadas al equipo de mantenimiento y su ejecución, incluyendo tiempos, materiales utilizados y observaciones. Se generan reportes de órdenes de mantenimiento por período, máquina y técnico.

---

## 8. Módulo de Calidad — Reportes

**Rol responsable:** Responsable de Calidad  
**Descripción:**

El área de calidad requiere un conjunto de reportes específicos para el control de procesos. Los reportes de calidad en Openbravo incluyen:

- Ingreso de informes de calidad con campos específicos según el proceso.
- Indicadores de datos históricos de reportes de calidad.
- Modificaciones en la aplicación móvil para captura de datos de calidad en planta.

El alcance típico contempla entre 20 y 30 reportes de calidad, cuyo contenido y estructura deben definirse en conjunto con el área de calidad de cada empresa durante la etapa de relevamiento.

---

## 9. Módulo de Nómina

**Rol responsable:** Responsable de RRHH / Nómina  
**Descripción:**

El módulo de nómina cubre el proceso estándar de:

- Ingreso y configuración de empleados.
- Cálculo del rol de pagos mensual (ingresos, deducciones, beneficios de ley).
- Generación de archivos de pago al banco.
- Integración con el módulo de tesorería para el pago de haberes.
- Manejo de descuentos especiales (crédito empleados, retenciones judiciales, préstamos quirografarios).

---

## 10. Módulo de Activos Fijos

**Rol responsable:** Contabilidad  
**Descripción:**

El módulo de activos fijos gestiona el ciclo de vida de los bienes de capital de la empresa:

- Configuración y registro inicial de activos fijos.
- Cálculo y registro automático de la depreciación.
- Control de ubicación y asignación de activos.
- Retiro o baja de activos.
- Reportes de activos por categoría, ubicación y estado.

---

## 11. Módulo de Contabilidad

**Rol responsable:** Contador / Jefe de Contabilidad  
**Descripción:**

La funcionalidad estándar de contabilidad de Openbravo incluye:

- Plan de cuentas configurable según normativa local.
- Generación automática de asientos contables desde los módulos operativos (compras, ventas, tesorería, nómina).
- Conciliación bancaria.
- Cierre de período y cierre anual.
- Generación de estados financieros: Balance General, Estado de Resultados, Flujo de Efectivo.
- Reportes tributarios y anexos según regulación fiscal local (SRI, en el contexto ecuatoriano).

---

## 12. Módulo de Producción

**Rol responsable:** Jefe de Producción / Responsable de Bodega  
**Descripción:**

El módulo de producción gestiona la transformación de materias primas en productos terminados mediante órdenes de fabricación.

**Funcionalidades principales:**

- Creación y gestión de órdenes de fabricación.
- Consumo de materias primas contra la orden (descargas de inventario de MP).
- Ingreso de producto terminado a bodega.
- Registro de mermas en la cadena productiva.
- Control de procesos intermedios (limpieza, corte, preparación de materiales).

**Reportes relacionados:**
- Reporte de mermas por fecha (acumulado y detallado por proceso).
- Reporte de mermas en toda la cadena productiva.

---

## 13. Reportería y Dashboards

Los dashboards proporcionan una vista consolidada de los indicadores clave del negocio para la toma de decisiones gerencial.

---

### 13.1 Dashboard Comercial

**Rol responsable:** Gerencia Comercial  
**Descripción:** Panel de 8 indicadores comerciales que muestra el desempeño del área de ventas. Los indicadores típicos incluyen: ventas del período, comparativo vs. período anterior, cumplimiento de presupuesto, evolución por vendedor, y mix de productos.

---

### 13.2 Dashboard Financiero-Contable

**Rol responsable:** Gerencia General / Contabilidad  
**Descripción:** Panel de 8 indicadores financieros y contables. Los indicadores típicos incluyen: ingresos, egresos, cuentas por cobrar, cuentas por pagar, liquidez, y márgenes.

---

### 13.3 Dashboard de Manufactura / Producción

**Rol responsable:** Gerencia de Producción  
**Descripción:** Panel de 8 indicadores de manufactura. Los indicadores típicos incluyen: eficiencia productiva, mermas por proceso, cumplimiento de órdenes de fabricación, consumo de materias primas y disponibilidad de máquinas.

---

## Anexo — Tipos de Documentos Estándar

A continuación se listan los tipos de documento más comunes en una implementación de Openbravo ERP, agrupados por módulo:

| Módulo | Tipo de Documento | Código Genérico Sugerido |
|---|---|---|
| Compras | Necesidad de Materiales | NM-XXXXXX |
| Compras | Pedido de Compra | PC-XXXXXX |
| Compras | Albarán de Recepción | RP-XXXXXX |
| Compras | Calificación de Proveedor | CCP-XXXXXX |
| Compras | Prueba Controlada Nuevo Lote | PCNL-XXXXXX |
| Compras | Factura Compra | FC-XXXXXX |
| Compras | Nota de Crédito Financiera | NCF-XXXXXX |
| Compras | Nota de Crédito por Devolución | NCD-XXXXXX |
| Inventarios | Ajuste de Inventario | AIF-XXXXXX |
| Inventarios | Transferencia Interna | TI-XXXXXX |
| Inventarios | Guía de Remisión Interna | GRI-XXXXXX |
| Inventarios | Recepción de Transferencia | RT-XXXXXX |
| Ventas | Pedido de Venta | PDV-XXXXXX |
| Ventas | Factura de Venta | 001-00X-XXXXXXXXX |
| Ventas | Guía de Remisión | 001-00X-XXXXXXXXX |
| Ventas | Nota de Crédito Venta | NCV-XXXXXX |
| Ventas | Queja / Caso CRM | QJ-XXXXXX |
| Ventas | Toma de Pedido Móvil | TPV-XXXXXX |
| Tesorería | Propuesta de Pago | PBNC-XXXXXX |
| Tesorería | Pago por Débito Automático | PDEB-XXXXXX |
| Tesorería | Anticipo a Proveedor | PANT-XXXXXX |
| Tesorería | Pago Cadena de Valor | PCV-XXXXXX |
| Tesorería | Pago Tarjeta de Crédito | PTCP-XXXXXX |
| Tesorería | Pago con Concepto Contable | PCC-XXXXXX |
| Tesorería | Pago Caja Chica | PCCH-XXXXXX |
| Tesorería | Cobro en Oficina | COF-XXXXXX |
| Tesorería | Cobro por Vendedor | CVEN-XXXXXX |
| Tesorería | Cobro por Transportista | CTRA-XXXXXX |
| Tesorería | ND Cheque Protestado | NDCHP-XXXXXX |
| Mantenimiento | Orden de Mantenimiento | OM-XXXXXX |

---

## Anexo — Roles Funcionales Estándar

| Rol | Responsabilidades Principales |
|---|---|
| Jefe de Compras | Gestión de pedidos de compra, evaluación de proveedores, negociación. |
| Bodeguero / Responsable de Inventario | Recepción de mercancía, transferencias, ajustes de inventario. |
| Jefe de Producción | Necesidades de materiales, órdenes de fabricación, control de mermas. |
| Responsable de RRHH | Necesidades de materiales de personal, nómina, descuentos de empleados. |
| Responsable de Mantenimiento | Órdenes de mantenimiento, necesidades de repuestos. |
| Contador / Contabilidad | Facturas de compra/venta, notas de crédito, asientos contables. |
| Tesorero | Pagos a proveedores, cobros de clientes, control de cuentas financieras. |
| Vendedor / Equipo Comercial | Pedidos de venta, cobros en ruta, toma de pedidos, CRM. |
| Cajero / Vendedor de Local | Ventas POS, cobros en local, cierre de caja. |
| Transportista | Entregas de productos, cobros en ruta, confirmación de entregas. |
| Facturador / Administración | Emisión de facturas, guías de remisión, seguimiento de pedidos. |
| Responsable de Calidad | Calificación de proveedores, pruebas de lotes, reportes de calidad. |
| Gerencia | Aprobación de necesidades, ajustes de inventario, propuestas de pago. |

---

*Documento generado por Sidesoft Cía. Ltda. — Base de conocimiento Openbravo ERP — Versión genérica aplicable a cualquier cliente.*
