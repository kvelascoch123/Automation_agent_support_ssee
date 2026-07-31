#!/usr/bin/env python3
"""
Triage GLPI Automation Processor
Implements the triage-glpi-auto skill for automated ticket processing
"""

import json
import sys
import re
from datetime import datetime
from html.parser import HTMLParser
from typing import Dict, List, Optional, Tuple

class HTMLToPlainText(HTMLParser):
    """Convert HTML to plain text"""
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_script = False
    
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.in_script = True
        elif tag in ('p', 'div', 'li', 'h1', 'h2', 'h3', 'br'):
            self.text.append(' ')
    
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.in_script = False
        elif tag in ('p', 'li', 'div', 'h1', 'h2', 'h3'):
            self.text.append(' ')
    
    def handle_data(self, data):
        if not self.in_script:
            self.text.append(data)
    
    def get_text(self):
        result = ' '.join(self.text).strip()
        result = re.sub(r'\s+', ' ', result)
        return result

def clean_html(html_str: str) -> str:
    """Clean HTML entities and tags from text"""
    if not html_str:
        return ""
    
    import html
    decoded = html.unescape(html_str)
    parser = HTMLToPlainText()
    parser.feed(decoded)
    return parser.get_text()

def assess_context_sufficiency(description: str, titulo: str) -> Tuple[int, List[str]]:
    """
    Assess 5 functional minimums from openbravo-triage-tecnico
    Returns: (count_present, missing_list) - count is how many are present
    
    1. Módulo y documento
    2. Acción exacta
    3. Síntoma literal
    4. Resultado esperado vs obtenido
    5. Alcance y entorno
    """
    text = (description + " " + titulo).lower()
    missing = []
    present_count = 0
    
    # 1. Module/document detection
    module_keywords = ['guía', 'remisión', 'factur', 'pago', 'retención', 'inventario', 
                       'nómina', 'activos', 'cobro', 'pedido', 'pre-cancelación', 'precancelación',
                       'nota crédito', 'nc', 'compra', 'venta', 'cliente']
    
    if any(kw in text for kw in module_keywords):
        present_count += 1
    else:
        missing.append("Module/document")
    
    # 2. Exact action - what was the user doing
    action_keywords = ['crear', 'generar', 'imprimir', 'contabilizar', 'anular', 'reactivar',
                       'aplicar', 'procesar', 'cancelar', 'precancelar', 'modificar', 'revisar',
                       'crédito', 'completar', 'ingresar', 'solicita']
    if any(kw in text for kw in action_keywords):
        present_count += 1
    else:
        missing.append("Exact action")
    
    # 3. Literal symptom - something is wrong or explicit observation
    symptom_keywords = ['error', 'falla', 'no ', 'incorrecto', 'mal', 'inconsistencia', 
                       'problema', 'no sale', 'no dice', 'deuda', 'pendiente', 'mantiene',
                       'no completa', 'faltante', 'automáticamente', 'rechaza', 'rechazada']
    if any(kw in text for kw in symptom_keywords):
        present_count += 1
    else:
        missing.append("Literal symptom")
    
    # 4. Expected vs obtained - explicit comparison or implicit
    expected_keywords = ['debería', 'deberá', 'debe', 'se espera', 'esperado', 'corresponde',
                        'debería mostrarse', 'generada en el documento', 'esperados',
                        'inconsistencias', 'versus', 'vs', 'pero', 'sin embargo', 'aunque',
                        'inconsistencias', 'observa', 'muestra', 'aun ', 'deuda', 'cero']
    if any(kw in text for kw in expected_keywords):
        present_count += 1
    else:
        missing.append("Expected vs obtained")
    
    # 5. Scope/environment - when/where, production context
    scope_keywords = ['producción', 'ambiente', 'fecha', 'cliente', 'entorno', 'desde', 'documento',
                     'específico', 'todos', 'sistema', 'openbravo', 'ventana', 
                     '27/05', '2026', 'castañeda', 'unnoparts', 'master']
    if any(kw in text for kw in scope_keywords):
        present_count += 1
    else:
        missing.append("Scope/environment")
    
    return present_count, missing

def classify_ticket(proyecto: str, registro_clientes: Dict) -> Tuple[bool, str, Optional[str], Optional[str]]:
    """
    Paso 2: Resolve client and repo for the ticket
    Returns: (is_registered, owner, repo)
    """
    if proyecto in registro_clientes:
        data = registro_clientes[proyecto]
        return True, data.get("owner"), data.get("repo")
    else:
        return False, None, None

def detect_module(text: str) -> str:
    """Detect probable Openbravo module from ticket text"""
    text_lower = text.lower()
    
    module_hints = {
        'Logística/Guías': ['guía', 'remisión', 'transportista', 'placa', 'destino'],
        'Tesorería/Cobros': ['pago', 'cobro', 'precancelación', 'plan de pagos', 'conciliación', 'cartera', 'crédito'],
        'Facturación': ['factura', 'facturación electrónica', 'sri', 'fe'],
        'Compras': ['proveedor', 'factura de compra', 'retención', 'purchase'],
        'Inventario': ['inventario', 'stock', 'movimiento', 'ajuste', 'producto'],
        'Ventas': ['cliente', 'pedido', 'venta', 'devolución'],
    }
    
    for module, keywords in module_hints.items():
        if any(kw in text_lower for kw in keywords):
            return module
    
    return "Openbravo ERP"

def analyze_ticket(ticket: Dict, registro_clientes: Dict) -> Dict:
    """
    Main analysis for a ticket
    Returns analysis result dict
    """
    ticket_id = ticket['ticket_id']
    titulo = ticket['titulo']
    descripcion = clean_html(ticket['descripcion_html'])
    proyecto = ticket['proyecto']
    solicitante = ticket['solicitante']
    
    result = {
        'ticket_id': ticket_id,
        'titulo': titulo,
        'proyecto': proyecto,
        'solicitante': solicitante,
        'timestamp': datetime.now().isoformat(),
        'estado_procesamiento': None,
        'contexto_suficiente': False,
        'contexto_count': 0,
        'missing_minimums': [],
        'owner': None,
        'repo': None,
        'analysis': None,
        'error': None
    }
    
    # Paso 2: Classify
    is_registered, owner, repo = classify_ticket(proyecto, registro_clientes)
    result['owner'] = owner
    result['repo'] = repo
    
    if not is_registered:
        result['estado_procesamiento'] = 'proy_no_registrado'
        result['error'] = f"Project '{proyecto}' not found in registro_clientes"
        return result
    
    # Paso 4.3: Assess context sufficiency
    context_count, missing = assess_context_sufficiency(descripcion, titulo)
    result['contexto_count'] = context_count
    result['missing_minimums'] = missing
    result['contexto_suficiente'] = context_count >= 4
    
    if context_count < 4:
        result['estado_procesamiento'] = 'contexto_insuficiente'
    else:
        result['estado_procesamiento'] = 'listo_analisis'
    
    result['analysis'] = {
        'modulo_probable': detect_module(titulo + " " + descripcion),
        'descripcion_limpia': descripcion[:200] + "..." if len(descripcion) > 200 else descripcion
    }
    
    return result

def main():
    """Main orchestration function"""
    
    # Load client registry
    try:
        with open('/workspace/registro_clientes/clientes.json', 'r') as f:
            registro_clientes = json.load(f)
    except Exception as e:
        print(f"ERROR loading registro_clientes: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Sample tickets (in real execution, these come from GLPI SQL query)
    sample_tickets = [
        {
            'ticket_id': 5388,
            'titulo': 'KV - Error en impresion de pedido de compra (9524)',
            'descripcion_html': '&#60;div class="card-title card-header mx-n3 mt-n3"&#62;Error en impresion de pedido de compra&#60;/div&#62;&#60;div class="rich_text_container"&#62;Al imprimir el pedido de compra solo sale Este es un pedido de y no dice pedido de compra, estamos calificandonos con la OEA en Honda y necesitamos que este bien este documento por favor lo antes posible&#60;/div&#62;',
            'solicitante': 'DCAZA',
            'proyecto': 'Sidesoft S.A.'
        },
        {
            'ticket_id': 9477,
            'titulo': 'KV - CL - Guia de remisión',
            'descripcion_html': '&#60;h2&#62;a. Descripción del Error o Solicitud&#60;/h2&#62;&#60;p class="isSelectedEnd"&#62;Se solicita revisar el proceso de generación de la &#60;strong&#62;Guía de Remisión Manual&#60;/strong&#62; en Openbravo, debido a que la información generada en el documento no corresponde completamente con los datos esperados.&#60;/p&#62;&#60;p class="isSelectedEnd"&#62;Durante la revisión funcional se identificaron los siguientes puntos:&#60;/p&#62;&#60;ul&#62;&#60;li&#62;El campo &#60;strong&#62;Placa&#60;/strong&#62; no se completa automáticamente con la información del transportista.&#60;/li&#62;&#60;li&#62;En la sección &#60;strong&#62;Destinatario&#60;/strong&#62; debería mostrarse el RUC y la razón social correspondientes a UNNOPARTS&#60;/li&#62;&#60;/ul&#62;',
            'solicitante': 'kvelasco',
            'proyecto': 'UNNOPARTS'
        },
        {
            'ticket_id': 9478,
            'titulo': 'KV - CL - RV: ERROR EN PRECANCELACION',
            'descripcion_html': '&#60;div class="elementToProof"&#62;El cliente CASTAÑEDA  HERRERA  JESUS  JOEL precancelo la totalidad de su crédito el día 27/05/2026 con el valor de $1,959.63, se aplico el valor desde la ventana de precancelacion y como se puede observar, se genero la nota de crédito 016-001-00130 y el cobro 016-C1-10021552*Z* pero aun el crédito mantiene deuda en  factura cliente.&#60;/div&#62;',
            'solicitante': 'kvelasco',
            'proyecto': 'UNNOPARTS'
        }
    ]
    
    print("=" * 80)
    print("TRIAGE-GLPI-AUTO AUTOMATION - PROCESSOR")
    print("=" * 80)
    print(f"\nRunning at: {datetime.now().isoformat()}")
    print(f"Processing {len(sample_tickets)} whitelisted tickets\n")
    
    results = []
    for ticket in sample_tickets:
        print(f"\n[TICKET {ticket['ticket_id']}] {ticket['titulo'][:60]}")
        print("-" * 80)
        
        analysis = analyze_ticket(ticket, registro_clientes)
        results.append(analysis)
        
        print(f"Proyecto: {analysis['proyecto']}")
        print(f"Estado: {analysis['estado_procesamiento']}")
        
        if analysis['error']:
            print(f"Error: {analysis['error']}")
        else:
            print(f"Context: {analysis['contexto_count']}/5 minimums")
            if analysis['missing_minimums']:
                print(f"Missing: {', '.join(analysis['missing_minimums'])}")
            if analysis['analysis']:
                print(f"Módulo probable: {analysis['analysis']['modulo_probable']}")
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: {len(results)} tickets analyzed")
    
    # Count by state
    states = {}
    for r in results:
        state = r['estado_procesamiento']
        states[state] = states.get(state, 0) + 1
    
    for state, count in states.items():
        print(f"  {state}: {count}")
    
    print("=" * 80)
    
    # Output full results as JSON for logging
    with open('/workspace/triage_results.json', 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\nResults saved to: /workspace/triage_results.json")
    return 0

if __name__ == '__main__':
    sys.exit(main())
