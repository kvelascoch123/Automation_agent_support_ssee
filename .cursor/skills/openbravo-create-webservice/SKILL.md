---
name: openbravo-create-webservice
description: Crea servicios Web portables para Openbravo (POST, JSON/form, sin dependencias de proyecto). Usa cuando el usuario pida crear un nuevo endpoint, servicio REST o WebService en Openbravo, o cuando necesite un servicio reutilizable en cualquier entorno.
---

# Crear Servicio Web Openbravo Portable

## Paso 1: Definir fuente de parámetros

**¿De dónde vienen los parámetros?**

| Escenario | Acción |
|-----------|--------|
| Usuario no especifica | Parámetros se envían vía el servicio (body JSON o form-urlencoded). |
| Usuario indica "ventana", "configuración", "tabla" | **Obligatorio** que el usuario proporcione: nombre de ventana (AD_Window), ruta del archivo/entidad, o tabla (ej. `SHPPWS_CONFIG`). No asumir. Si no lo da, preguntar. |

## Paso 2: Estructura de la clase

```java
public class Nombre_Servicio implements WebService {
    @Override
    public void doGet(...) {
        // 405 + JSON: "Error: Use POST method"
    }
    @Override
    public void doPost(...) {
        processRequest(request, response);
    }
    private String getParam(HttpServletRequest request, JSONObject jsonBody, String name) { ... }
    private void processRequest(HttpServletRequest request, HttpServletResponse response) { ... }
}
```

## Paso 3: Lectura de parámetros (JSON + form)

```java
JSONObject jsonBody = null;
String contentType = request.getContentType();
if (contentType != null && contentType.toLowerCase().contains("application/json")) {
    try (BufferedReader reader = new BufferedReader(
            new InputStreamReader(request.getInputStream(), StandardCharsets.UTF_8))) {
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) sb.append(line);
        if (sb.length() > 0) jsonBody = new JSONObject(sb.toString());
    } catch (Exception e) {
        throw new OBException("JSON inválido en el body: " + e.getMessage());
    }
}

String valor = getParam(request, jsonBody, "NOMBRE_PARAM");
```

```java
private String getParam(HttpServletRequest request, JSONObject jsonBody, String name) throws Exception {
    if (jsonBody != null) {
        if (jsonBody.has(name) && !jsonBody.isNull(name)) {
            Object val = jsonBody.get(name);
            return val == null ? null : String.valueOf(val);
        }
        return null;
    }
    return request.getParameter(name);
}
```

**Imports necesarios:** `BufferedReader`, `InputStreamReader`, `StandardCharsets`, `org.codehaus.jettison.json.JSONObject`. Sin helpers del proyecto.

## Imports y APIs críticos (evitar errores de compilación)

**Usar siempre estos imports y métodos; los alternativos fallan en Openbravo:**

| Uso | Correcto | Incorrecto |
|-----|----------|------------|
| ConnectionProvider | `org.openbravo.database.ConnectionProvider` | — |
| DalConnectionProvider | `org.openbravo.service.db.DalConnectionProvider` | ~~`org.openbravo.database.DalConnectionProvider`~~ (no existe) |
| DocumentType | `org.openbravo.model.common.enterprise.DocumentType` | ~~`org.openbravo.model.common.order.DocumentType`~~ (no existe) |
| Lista precios venta (BP) | `bp.getPriceList()` | ~~`bp.getSalesPriceList()`~~ (no existe) |
| Lista precios compra (BP) | `bp.getPurchasePricelist()` | — |

```java
// Correcto
import org.openbravo.database.ConnectionProvider;
import org.openbravo.service.db.DalConnectionProvider;
import org.openbravo.model.common.enterprise.DocumentType;
// ...
ConnectionProvider conn = new DalConnectionProvider(false);
PriceList priceList = bp.getPriceList();  // lista venta cliente
```

## Paso 4: Validación y lógica

- Validar parámetros obligatorios con `OBException` si faltan.
- Parsear numéricos con `BigDecimal`, manejar `NumberFormatException`.
- Usar solo: `OBDal`, `OBProvider`, `Utility`, entidades Openbravo estándar. Evitar tablas/helpers propios salvo que el usuario lo exija.

## Paso 5: Respuesta y transacciones

```java
response.setContentType("application/json");
response.setCharacterEncoding("UTF-8");
JSONObject records = new JSONObject();
records.put("Message", "Ok");  // o "Error: ..."
records.put("CampoResultado", valor);
// ...
PrintWriter writer = response.getWriter();
writer.write(records.toString());
writer.close();

OBDal.getInstance().getConnection().commit();  // en éxito
OBDal.getInstance().getSession().getTransaction().rollback();  // en catch
```

## Paso 6: Registro del bean

En `config/[modulo]-provider-config.xml`:

```xml
<bean>
  <name>Nombre_Servicio</name>
  <class>paquete.completo.Nombre_Servicio</class>
  <singleton>true</singleton>
</bean>
```

El nombre del bean = ruta del endpoint (ej. `Standard_Invoice_Creation`).

## Ejemplo de referencia

**Servicio:** `Standard_Invoice_Creation`  
**Módulo:** `ec.com.sidesoft.happypay.web.services`  
**Parámetros usados:**

| Parámetro | Obligatorio | Descripción |
|-----------|-------------|-------------|
| AD_Org_ID | Sí | Organización |
| C_DocType_ID | Sí | Tipo documento |
| C_BPARTNER_ID | Sí | Socio de negocio |
| M_PRODUCT_ID | Sí | Producto |
| UnitPrice | Sí | Precio unitario |
| Quantity | No (default 1) | Cantidad |
| Description | No | Descripción factura |
| M_PriceList_ID | No | Lista precios (o del socio) |
| C_Costcenter_ID | No | Centro de costo |
| FIN_PaymentMethod_ID | No | Método pago (o del socio) |
| C_PaymentTerm_ID | No | Condiciones pago (o del socio) |
| Process | No (default N) | Y=Completar, N=Borrador |

**Llamada curl:**
```bash
curl -X POST 'http://host/context/ws/ec.com.sidesoft.happypay.web.services.Standard_Invoice_Creation' \
  -H 'Content-Type: application/json' \
  -d '{"AD_Org_ID":"...","C_DocType_ID":"...","C_BPARTNER_ID":"...","M_PRODUCT_ID":"...","UnitPrice":10}'
```

## Checklist

- [ ] Parámetros por request (salvo que el usuario pida ventana/config explícita)
- [ ] POST principal, GET → 405
- [ ] JSON y form-urlencoded soportados
- [ ] Sin dependencias de helpers/tablas del proyecto
- [ ] Bean registrado en provider-config
- [ ] Respuesta JSON con Message y campos de resultado
- [ ] Commit/rollback correctos
