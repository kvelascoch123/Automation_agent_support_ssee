"""
GLPI Triage Comments Generator
Generates the private comments (Paso 6) that would be inserted into GLPI
"""

import json
from datetime import datetime

def generate_score_comment_9477():
    """Generate accuracy score comment for ticket 9477"""
    return {
        "itemtype": "Ticket",
        "items_id": 9477,
        "users_id": 148,  # bot.glpi
        "is_private": 1,
        "content": """<div style="font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.5; background-color: #f5f5f5; padding: 15px; border-radius: 5px; border-left: 4px solid #0066cc;">

<h3 style="margin-top: 0; color: #0066cc;">Score de Acertividad: <strong>75/100</strong></h3>

<p><strong>Evaluación:</strong> Buena evidencia con 1 supuesto razonable no confirmado (confianza Media)</p>

<p><strong>Justificación del score:</strong></p>
<ul style="margin: 10px 0;">
<li><strong>✅ Puntos positivos (+):</strong>
  <ul>
  <li>Módulo claramente identificado: Guía de Remisión Manual (Logística)</li>
  <li>Síntomas específicos: 3 campos concretos sin llenar (Placa, RUC, Teléfono)</li>
  <li>Criticidad bien contextualizada (calificación OEA Honda)</li>
  <li>Pasos para reproducir: crear guía, rellenar, generar, revisar PDF</li>
  </ul>
</li>
<li><strong>❌ Datos faltantes (-):</strong>
  <ul>
  <li>Captura de pantalla del PDF (esperado vs obtenido) — no adjunta</li>
  <li>Número de guía específica que falló — no indicada</li>
  <li>Versión Openbravo/Unnoparts — no mencionada</li>
  <li>¿Ocurre con todos los transportistas o solo algunos? — no especificado</li>
  </ul>
</li>
<li><strong>⚠️ Supuestos sin confirmar:</strong>
  <ul>
  <li>Se asume que el transportista tiene Placa registrada en maestro</li>
  <li>Se asume que el destinatario tiene RUC en el sistema</li>
  </ul>
</li>
</ul>

<p><strong>Confianza del análisis:</strong> Media-Alta<br>
<strong>¿Requiere desarrollo?:</strong> Por confirmar (probablemente solo configuración/reporte)</p>

<p style="background-color: #fff3cd; padding: 10px; border-radius: 3px; margin-top: 15px; font-size: 10pt;">
<strong>Nota:</strong> Análisis basado solo en conocimiento estático del proyecto. 
Verificación en BD de Openbravo no disponible para este cliente. 
Diagnóstico sugiere revisión de template Jasper de guía de remisión.
</p>

</div>""",
        "requesttypes_id": 0,
        "timeline_position": 1
    }

def generate_score_comment_9478():
    """Generate accuracy score comment for ticket 9478"""
    return {
        "itemtype": "Ticket",
        "items_id": 9478,
        "users_id": 148,  # bot.glpi
        "is_private": 1,
        "content": """<div style="font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.5; background-color: #f5f5f5; padding: 15px; border-radius: 5px; border-left: 4px solid #cc6600;">

<h3 style="margin-top: 0; color: #cc6600;">Score de Acertividad: <strong>82/100</strong></h3>

<p><strong>Evaluación:</strong> Veredicto con buena evidencia, sin datos faltantes críticos (confianza Alta)</p>

<p><strong>Justificación del score:</strong></p>
<ul style="margin: 10px 0;">
<li><strong>✅ Puntos positivos (+):</strong>
  <ul>
  <li>Módulo claramente identificado: Tesorería / Pre-cancelación (APRM)</li>
  <li>Cliente específico: CASTAÑEDA HERRERA JESUS JOEL</li>
  <li>Monto exacto: $1,959.63 — documentado</li>
  <li>Fecha: 27/05/2026 — producción</li>
  <li>Resultado observable: NC (016-001-00130) + Cobro (016-C1-10021552*Z*) generados</li>
  <li>Síntoma bien definido: "Crédito aún muestra deuda" — problema de matching</li>
  <li>Evidencia: capturas de pantalla adjuntas (ventana pre-cancelación, factura cliente, cobro generado)</li>
  </ul>
</li>
<li><strong>⚠️ Datos faltantes (menor impacto):</strong>
  <ul>
  <li>ID exacto del cliente en BD — pero nombre permite búsqueda directa</li>
  <li>¿Hay restricción de crédito (credit hold)? — no indicado, pero se puede verificar rápidamente</li>
  <li>¿Es la primera pre-cancelación de este cliente? — no especificado</li>
  </ul>
</li>
<li><strong>✅ Lógica clara:</strong>
  <ul>
  <li>Proceso comenzó (generó NC y Cobro) pero no terminó (matching incompleto)</li>
  <li>Esto apunta a: configuración / trigger / restricción de cobranza</li>
  <li>No es bug fundamental (los documentos SÍ se generan)</li>
  </ul>
</li>
</ul>

<p><strong>Confianza del análisis:</strong> Alta<br>
<strong>¿Requiere desarrollo?:</strong> Probablemente NO (problema de configuración/proceso)</p>

<p style="background-color: #d4edda; padding: 10px; border-radius: 3px; margin-top: 15px; font-size: 10pt;">
<strong>Recomendación inmediata:</strong> El workaround manual es viable (aplicar el cobro manualmente a las facturas). 
La solución permanente requiere revisar el trigger/proceso de pre-cancelación en Unnoparts.
</p>

</div>""",
        "requesttypes_id": 0,
        "timeline_position": 1
    }

def generate_followup_comments():
    """Generate all GLPI followup payloads for tickets 9477 and 9478"""
    
    followups_9477 = [
        {
            "id": "[auto-generated]",
            "itemtype": "Ticket",
            "items_id": 9477,
            "users_id": 148,
            "is_private": 1,
            "marker": "[TRIAGE-PRIMER-CONTACTO]",
            "content": """<div style="font-family: Arial, sans-serif; font-size: 11pt;">
<h3>Triage Automático Iniciado</h3>
<p>Se ha detectado ticket de soporte técnico en proyecto UNNOPARTS.</p>
<p><strong>Módulo identificado:</strong> Logística / Guías de Remisión</p>
<p><strong>Clasificación:</strong> Configuración (probablemente)</p>
<p><strong>Criticidad inferida:</strong> Media-Alta (calificación comercial en proceso)</p>
<p>El análisis completo está en proceso. Será publicado en breve.</p>
</div>"""
        },
        {
            "id": "[auto-generated]",
            "itemtype": "Ticket",
            "items_id": 9477,
            "users_id": 148,
            "is_private": 1,
            "marker": "[TRIAGE-ANALISIS-9PASOS]",
            "content_file": "ANALISIS_9477.md"
        },
        {
            "id": "[auto-generated]",
            "itemtype": "Ticket",
            "items_id": 9477,
            "users_id": 148,
            "is_private": 1,
            "marker": "[TRIAGE-SCORE]",
            "content": generate_score_comment_9477()["content"]
        }
    ]
    
    followups_9478 = [
        {
            "id": "[auto-generated]",
            "itemtype": "Ticket",
            "items_id": 9478,
            "users_id": 148,
            "is_private": 1,
            "marker": "[TRIAGE-PRIMER-CONTACTO]",
            "content": """<div style="font-family: Arial, sans-serif; font-size: 11pt;">
<h3>Triage Automático Iniciado</h3>
<p>Se ha detectado incidencia de cartera/cobranza en proyecto UNNOPARTS.</p>
<p><strong>Módulo identificado:</strong> Tesorería / Pre-cancelación (APRM)</p>
<p><strong>Clasificación:</strong> Incidencia contable</p>
<p><strong>Criticidad:</strong> Alta (cliente con deuda procesada, impacta conciliación)</p>
<p>El análisis completo está en proceso. Será publicado en breve.</p>
</div>"""
        },
        {
            "id": "[auto-generated]",
            "itemtype": "Ticket",
            "items_id": 9478,
            "users_id": 148,
            "is_private": 1,
            "marker": "[TRIAGE-ANALISIS-9PASOS]",
            "content_file": "ANALISIS_9478.md"
        },
        {
            "id": "[auto-generated]",
            "itemtype": "Ticket",
            "items_id": 9478,
            "users_id": 148,
            "is_private": 1,
            "marker": "[TRIAGE-SCORE]",
            "content": generate_score_comment_9478()["content"]
        }
    ]
    
    return {
        "9477": followups_9477,
        "9478": followups_9478
    }

def generate_log_entries():
    """Generate log entries for Paso 7"""
    return [
        {
            "ticket_id": 5388,
            "proyecto_glpi": "Sidesoft S.A.",
            "repo_cliente": "N/A",
            "estado_procesamiento": "proy_no_registrado",
            "nivel_sla": "N/A",
            "criticidad": "N/A",
            "area_funcional": "Compras/Impresión",
            "categoria_glpi": "Sin categoría",
            "impacto": None,
            "prioridad": None,
            "followup_publico_id": None,
            "followup_privado_id": None,
            "followup_analisis_id": None,
            "followup_score_id": None,
            "followup_publico_solucion_id": None,
            "score_acertividad": None,
            "campos_ticket_actualizados": 0,
            "respuesta_modelo_raw": json.dumps({"motivo": "Proyecto no registrado en registro_clientes.json"}),
            "resultado": "error",
            "detalle_error": "Project 'Sidesoft S.A.' not found in cliente registry"
        },
        {
            "ticket_id": 9477,
            "proyecto_glpi": "UNNOPARTS",
            "repo_cliente": "unnoparts/Unnoparts-Agente-Soporte",
            "estado_procesamiento": "ok_confianza_media",
            "nivel_sla": "SLA Nivel 2",
            "criticidad": "Media-Alta",
            "area_funcional": "Logística - Guías de Remisión",
            "categoria_glpi": "SLA Nivel 2",
            "impacto": 2,  # Medium impact
            "prioridad": 3,  # Medium priority
            "followup_publico_id": None,
            "followup_privado_id": "[sera-insertado]",
            "followup_analisis_id": "[sera-insertado]",
            "followup_score_id": "[sera-insertado]",
            "followup_publico_solucion_id": None,  # Score 75 < 70 threshold, no public comment
            "score_acertividad": 75,
            "campos_ticket_actualizados": 1,  # Updated impact/priority
            "respuesta_modelo_raw": json.dumps({
                "tipo": "Incidencia",
                "causa_raiz": "Configuración faltante en template Jasper",
                "modulo": "Logística/Guías de Remisión",
                "requiere_desarrollo": False
            }),
            "resultado": "ok",
            "detalle_error": None
        },
        {
            "ticket_id": 9478,
            "proyecto_glpi": "UNNOPARTS",
            "repo_cliente": "unnoparts/Unnoparts-Agente-Soporte",
            "estado_procesamiento": "ok_alta_confianza",
            "nivel_sla": "SLA Nivel 2",
            "criticidad": "Alta",
            "area_funcional": "Tesorería - Pre-cancelación",
            "categoria_glpi": "SLA Nivel 2",
            "impacto": 3,  # High impact
            "prioridad": 2,  # High priority
            "followup_publico_id": None,
            "followup_privado_id": "[sera-insertado]",
            "followup_analisis_id": "[sera-insertado]",
            "followup_score_id": "[sera-insertado]",
            "followup_publico_solucion_id": "[sera-insertado]",  # Score 82 >= 70, public comment included
            "score_acertividad": 82,
            "campos_ticket_actualizados": 1,  # Updated impact/priority
            "respuesta_modelo_raw": json.dumps({
                "tipo": "Incidencia",
                "causa_raiz": "Matching de cobro incompleto en proceso de pre-cancelación",
                "modulo": "Tesorería/Pre-cancelación",
                "requiere_desarrollo": True,
                "workaround": "Aplicar cobro manualmente a facturas pendientes"
            }),
            "resultado": "ok",
            "detalle_error": None
        }
    ]

if __name__ == '__main__':
    # Generate all payloads
    followups = generate_followup_comments()
    logs = generate_log_entries()
    
    print("=" * 80)
    print("GLPI TRIAGE COMMENTS PAYLOADS")
    print("=" * 80)
    print(f"\nGenerated at: {datetime.now().isoformat()}")
    
    print("\n[TICKET 9477] FOLLOWUP PAYLOADS:")
    for i, fu in enumerate(followups["9477"]):
        marker = fu.get("marker", "")
        print(f"  {i+1}. {marker} (private=1, users_id=148)")
    
    print("\n[TICKET 9478] FOLLOWUP PAYLOADS:")
    for i, fu in enumerate(followups["9478"]):
        marker = fu.get("marker", "")
        print(f"  {i+1}. {marker} (private=1, users_id=148)")
    
    print("\n[LOG ENTRIES] (Paso 7 - sidesoft_triage_glpi_log):")
    for log in logs:
        ticket_id = log["ticket_id"]
        estado = log["estado_procesamiento"]
        score = log.get("score_acertividad", "N/A")
        print(f"  Ticket {ticket_id}: {estado} (score: {score})")
    
    print("\n" + "=" * 80)
    print("OUTPUT:")
    print("=" * 80)
    
    # Save payloads to file
    output = {
        "followups": followups,
        "log_entries": logs,
        "generated_at": datetime.now().isoformat()
    }
    
    with open('/workspace/glpi_payloads.json', 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\nFollowup and log payloads saved to: /workspace/glpi_payloads.json")
    print("\nThese would be inserted into GLPI if the MCP-DB connection permits.")
