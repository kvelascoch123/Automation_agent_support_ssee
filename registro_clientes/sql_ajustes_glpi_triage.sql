-- =====================================================================
-- Ajustes GLPI para el triage automático (ejecutar en la BD de GLPI)
-- Generado: 2026-09-27. Revisar y ejecutar en este orden.
-- Hacer respaldo de las tablas afectadas antes de ejecutar.
-- =====================================================================

-- ---------------------------------------------------------------------
-- 1) sidesoft_triage_glpi_log: alinear con el INSERT del Paso 7
-- ---------------------------------------------------------------------
-- estado_procesamiento era VARCHAR(20): no cabían 'proyecto_no_registrado' (22)
-- ni 'esperando_respuesta_cliente' (27). Se agregan las columnas que usa la skill.
ALTER TABLE sidesoft_triage_glpi_log
  MODIFY estado_procesamiento VARCHAR(40) NULL,
  ADD COLUMN repo_cliente       VARCHAR(255) NULL AFTER proyecto_glpi,
  ADD COLUMN tecnico_asignado   VARCHAR(50)  NULL,
  ADD COLUMN tickets_referencia VARCHAR(255) NULL,
  ADD COLUMN playbook           VARCHAR(80)  NULL;

-- Verificación
SHOW COLUMNS FROM sidesoft_triage_glpi_log;

-- ---------------------------------------------------------------------
-- 2) Normalizar valores históricos del log (opcional, recomendado)
-- ---------------------------------------------------------------------
-- Estados truncados/inventados por el agente -> valores oficiales
UPDATE sidesoft_triage_glpi_log SET estado_procesamiento = 'proyecto_no_registrado'
 WHERE estado_procesamiento = 'proy_no_registrado';            -- 28 filas
UPDATE sidesoft_triage_glpi_log SET estado_procesamiento = 'esperando_respuesta_cliente'
 WHERE estado_procesamiento = 'esp_resp_cliente';              -- 6 filas
-- 'skip_idempotent' (75) y 'skip_idempotente' (2) no existen en la skill.
-- Se dejan tal cual; si se decide que equivalen a 'duplicado_abortado', ejecutar:
-- UPDATE sidesoft_triage_glpi_log SET estado_procesamiento = 'duplicado_abortado'
--  WHERE estado_procesamiento IN ('skip_idempotent', 'skip_idempotente');

-- Nivel SLA -> formato 'SLA n'
UPDATE sidesoft_triage_glpi_log SET nivel_sla = 'SLA 2' WHERE nivel_sla IN ('2', 'SLA2', 'Nivel 2');  -- 72 filas
UPDATE sidesoft_triage_glpi_log SET nivel_sla = 'SLA 3' WHERE nivel_sla IN ('3', 'SLA3');             -- 49 filas
-- 'bajo', 'MEJORA' y 'N/A' (4 filas) son ambiguos: se dejan para revisión manual.

-- Verificación
SELECT estado_procesamiento, COUNT(*) FROM sidesoft_triage_glpi_log GROUP BY estado_procesamiento;
SELECT nivel_sla, COUNT(*) FROM sidesoft_triage_glpi_log GROUP BY nivel_sla;

-- ---------------------------------------------------------------------
-- 3) Backfill del campo "Score agente" (scoreagentefield)
--    Fuente: último registro del log con análisis publicado (ok_*) y score.
--    Afecta 131 tickets: 128 filas a actualizar + 3 filas a insertar.
-- ---------------------------------------------------------------------
UPDATE glpi_plugin_fields_ticketticketsformfields f
JOIN (
  SELECT l.ticket_id, l.score_acertividad
  FROM sidesoft_triage_glpi_log l
  JOIN (SELECT ticket_id, MAX(id) AS mid
        FROM sidesoft_triage_glpi_log
        WHERE score_acertividad IS NOT NULL AND estado_procesamiento LIKE 'ok\_%'
        GROUP BY ticket_id) u ON u.mid = l.id
) s ON s.ticket_id = f.items_id
SET f.scoreagentefield = s.score_acertividad
WHERE f.itemtype = 'Ticket'
  AND (f.scoreagentefield IS NULL OR f.scoreagentefield = '');

INSERT INTO glpi_plugin_fields_ticketticketsformfields
  (items_id, itemtype, plugin_fields_containers_id, entities_id, scoreagentefield)
SELECT s.ticket_id, 'Ticket', 11, t.entities_id, s.score_acertividad
FROM (
  SELECT l.ticket_id, l.score_acertividad
  FROM sidesoft_triage_glpi_log l
  JOIN (SELECT ticket_id, MAX(id) AS mid
        FROM sidesoft_triage_glpi_log
        WHERE score_acertividad IS NOT NULL AND estado_procesamiento LIKE 'ok\_%'
        GROUP BY ticket_id) u ON u.mid = l.id
) s
JOIN glpi_tickets t ON t.id = s.ticket_id
LEFT JOIN glpi_plugin_fields_ticketticketsformfields f
       ON f.items_id = s.ticket_id AND f.itemtype = 'Ticket'
WHERE f.id IS NULL;

-- Verificación (debe devolver al menos 131)
SELECT COUNT(*) FROM glpi_plugin_fields_ticketticketsformfields
WHERE itemtype = 'Ticket' AND scoreagentefield IS NOT NULL AND scoreagentefield <> '';
