# Prompt listo para pegar

Reemplaza los UUID entre corchetes:

---

**Análisis error facturación electrónica Ecuador (Openbravo)**

Usa el skill **ob-fe-eei-invoicelog-analysis**.

**IDs:**
- `EEI_INVOICELOG_ID`: `[pegar-id-del-registro-en-Registro-Historico-FE]`
- `C_INVOICE_ID` (si ya lo tengo; si no, dedúcelo del log): `[opcional]`

Ejecuta MCP **user-postgres** (solo lectura), cruza con el código de generación XML del módulo `ec.cusoft.facturaec` según `edoc_type`, y explica por qué el SRI no autoriza y qué corregir (parametrización / datos).

---

Versión mínima (solo id de log):

> Analiza el error FE con skill ob-fe-eei-invoicelog-analysis. `EEI_INVOICELOG_ID`: `38403A5CA4C84DA38D6C201174913037`.

Versión con factura conocida:

> Analiza el error FE con skill ob-fe-eei-invoicelog-analysis. `C_INVOICE_ID`: `C0ED28E496D946CBBE8BAFCC1585552F` (y la línea de log con error si hay varias).
