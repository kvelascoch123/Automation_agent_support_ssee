---
name: ob-fe-eei-invoicelog-analysis
description: >-
  Diagnoses Ecuador electronic invoicing (SRI) rejections stored in Openbravo EEI_INVOICELOG by
  correlating SQL data (invoice, taxes, lines) with XML generation in ec.cusoft.facturaec. Use when
  the user provides an EEI_INVOICELOG_ID or C_INVOICE_ID, mentions "Registro Histórico FE", factura
  electrónica Ecuador, error SRI, NO AUTORIZADO, liquidación de compra código 03, or asks to
  analyze an FE log record.
---

# Análisis de errores FE (EEI_INVOICELOG) — Ecuador / Openbravo

## Entradas que debe pedir o inferir

1. **`EEI_INVOICELOG_ID`** (32 chars hex): identifica la línea en solapa **Registro Histórico FE** (tabla `EEI_INVOICELOG`).
2. **`C_INVOICE_ID`** (opcional pero útil): si el usuario solo da la factura/transacción, trabajar desde aquí y listar logs relacionados.

Si solo hay un ID y no está claro: probar primero como `EEI_INVOICELOG_ID`; si no existe, asumir `C_INVOICE_ID`.

## Flujo obligatorio

1. **Leer el descriptor del MCP** `user-postgres` (`query`) antes de ejecutar SQL.
2. **Cargar el log**:
   - Por id de log: `SELECT line, c_invoice_id, logtype, edoc_type, description FROM eei_invoicelog WHERE eei_invoicelog_id = '<id>'`.
   - Por id de factura: `SELECT * FROM eei_invoicelog WHERE c_invoice_id = '<id>' ORDER BY line` (analizar la línea con error, suele `logtype = 'E'`).
3. **Cargar cabecera** (`C_INVOICE`): `documentno`, `dateinvoiced`, `totallines`, `grandtotal`, `docstatus`, `c_doctype_id` si hace falta el tipo.
4. **Impuestos cabecera** — cruce con parametrización SRI:
   ```sql
   SELECT it.c_invoicetax_id, t.name, t.rate, t.istaxdeductable,
          t.em_eei_sri_tax_type, t.em_eei_sri_taxcat_code,
          it.taxbaseamt, it.taxamt
   FROM c_invoicetax it
   JOIN c_tax t ON t.c_tax_id = it.c_tax_id
   WHERE it.c_invoice_id = '<C_INVOICE_ID>'
   ORDER BY t.rate;
   ```
5. **Líneas y impuestos por línea** (tabla `c_invoicelinetax`):
   ```sql
   SELECT il.line, il.qtyinvoiced, il.pricelist, il.priceactual, il.linenetamt,
          t.name, t.rate, t.em_eei_sri_tax_type, t.em_eei_sri_taxcat_code,
          ilt.taxbaseamt, ilt.taxamt
   FROM c_invoiceline il
   LEFT JOIN c_invoicelinetax ilt ON ilt.c_invoiceline_id = il.c_invoiceline_id
   LEFT JOIN c_tax t ON t.c_tax_id = ilt.c_tax_id
   WHERE il.c_invoice_id = '<C_INVOICE_ID>' AND il.isactive = 'Y'
   ORDER BY il.line;
   ```
6. **Código Java que genera el XML** según `EDOC_TYPE` del log (ajustar si el proyecto usa otra clase):
   - **`03`** — Liquidación de compra: `modules/ec.cusoft.facturaec/src/ec/cusoft/facturaec/filewriter/PurchaseSettlementGenerationEcuador.java` (`totalConImpuestos` desde `InvoiceTax` con `isTaxdeductable`; detalle desde `InvoiceLineTax`).
   - Otros tipos: localizar con búsqueda `generateFile` / `EDOC_TYPE` / `FileGenerationEcuador` en el mismo módulo.

## Lectura del mensaje SRI (Description)

- Los rechazos suelen incluir **código impuesto** (`codigo=2` → IVA) y **código porcentaje** (`codigoPorcentaje`).
- **Desajuste tarifa**: el XML envía `tarifa` = `C_TAX.rate`, pero el SRI valida contra la **tarifa parametrizada** del catálogo para ese `codigoPorcentaje`. Si `em_eei_sri_taxcat_code` apunta a otro % (ej. `4` históricamente 15 % mientras `rate` = 5), el SRI reporta error de tarifa y totales recalculados (ej. 45 vs 135 sobre base 900).
- **Totalizado vs detalle**: suma de `valor` en líneas debe ser coherente con `totalImpuesto` del mismo `codigo` + `codigoPorcentaje`; discrepancias vienen de datos, líneas filtradas/colapsadas en código, o de la validación anterior del catálogo.

## Formato de respuesta al usuario

Entregar en este orden:

1. **Resumen ejecutivo**: por qué no autoriza (causa raíz en negocio/norma/parametrización).
2. **Evidencia BD**: documento, impuestos (rate vs `em_eei_sri_taxcat_code`), líneas relevantes.
3. **Evidencia código**: qué nodos XML se llenan desde qué campos (clase y sección; citar archivo si aplica).
4. **Acción correctiva**: cambios en `C_TAX` / líneas / proceso, y comprobar ficha técnica vigente SRI para códigos de porcentaje.

Responder en el idioma del usuario si lo indican; por defecto español para este dominio.

## Plantilla de prompt (copiar para el usuario)

Ver `PROMPT-SNIPPET.md` en este directorio.
