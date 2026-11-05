#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Script de Atualização Interna da Base de Dados dos Roadmaps
Uso Exclusivo de Desenvolvedores / GTs Temáticos (Deborah / Gabriel Barreto).

Valida e sincroniza os dados dos roadmaps a partir de novos arquivos relacionais (JSON/CSV)
gerando automaticamente data/napen_roadmaps_data.json e js/data.js.
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Campos obrigatórios para cada condição no schema do dashboard
REQUIRED_CONDITION_FIELDS = [
    'id', 'condicao', 'eixo', 'roadmap_id', 'svg_file',
    'status_auditoria', 'fatores_limitantes', 'modalidades'
]

REQUIRED_MODALITY_FIELDS = [
    'tecnica', 'modalidade_sigla', 'alvo', 'frequencia',
    'pulsos_duracao', 'sessoes', 'escala_recomendada',
    'meta_melhora', 'evidencia', 'protocolo_alternativo'
]

def validar_schema(data):
    """Verifica se o JSON possui a estrutura mínima necessária para o dashboard."""
    erros = []
    
    if not isinstance(data, dict):
        return ["O arquivo raiz deve ser um objeto JSON (dicionário)."]
    
    if 'versao' not in data:
        erros.append("Campo 'versao' ausente na raiz do arquivo.")
    if 'condicoes' not in data or not isinstance(data['condicoes'], list):
        erros.append("Campo 'condicoes' ausente ou não é uma lista.")
        return erros

    for idx, c in enumerate(data['condicoes']):
        cid = c.get('id', f"index_{idx}")
        for req in REQUIRED_CONDITION_FIELDS:
            if req not in c:
                erros.append(f"Condição '{cid}': campo obrigatório '{req}' ausente.")
        
        # Validação do arquivo SVG
        svg_file = c.get('svg_file')
        if svg_file:
            svg_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'svgs', svg_file)
            if not os.path.exists(svg_path):
                erros.append(f"Condição '{cid}': arquivo SVG referenciado não encontrado em disco ({svg_file}).")
        
        # Validação das modalidades
        modalidades = c.get('modalidades', {})
        if not modalidades:
            erros.append(f"Condição '{cid}': nenhuma modalidade terapêutica definida.")
        else:
            for mod_k, mod_v in modalidades.items():
                for m_req in REQUIRED_MODALITY_FIELDS:
                    if m_req not in mod_v:
                        erros.append(f"Condição '{cid}' [modalidade {mod_k}]: campo '{m_req}' ausente.")
                
                # Validação do protocolo alternativo
                alt = mod_v.get('protocolo_alternativo')
                if alt:
                    if 'nome' not in alt or 'observacoes' not in alt:
                        erros.append(f"Condição '{cid}' [modalidade {mod_k}]: protocolo alternativo incompleto (requer 'nome' e 'observacoes').")

    return erros

def sincronizar_arquivos(data, base_dir):
    """Salva os arquivos data/napen_roadmaps_data.json e js/data.js."""
    data_dir = os.path.join(base_dir, 'data')
    js_dir = os.path.join(base_dir, 'js')
    
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(js_dir, exist_ok=True)

    json_path = os.path.join(data_dir, 'napen_roadmaps_data.json')
    js_path = os.path.join(js_dir, 'data.js')

    # Salva JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Salva JS
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write('// Rede NAPeN — Base de Dados dos Roadmaps Clínicos (Auto-gerada)\n')
        f.write(f'// Atualizado em: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        f.write('window.NAPEN_DATA = ')
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(';\n')

    print(f"✓ Base JSON atualizada: {json_path} ({os.path.getsize(json_path)} bytes)")
    print(f"✓ Base JS atualizada: {js_path} ({os.path.getsize(js_path)} bytes)")

def main():
    parser = argparse.ArgumentParser(description="Atualizador de Base de Dados dos Roadmaps NAPeN")
    parser.add_argument('--input', '-i', help="Caminho para arquivo JSON de atualização", default=None)
    parser.add_argument('--check-only', action='store_true', help="Apenas valida a integridade sem sobrescrever arquivos")
    args = parser.parse_args()

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # Se nenhum input for passado, valida o arquivo existente em data/
    target_json = args.input if args.input else os.path.join(base_dir, 'data', 'napen_roadmaps_data.json')
    
    if not os.path.exists(target_json):
        print(f"ERRO: Arquivo não encontrado: {target_json}", file=sys.stderr)
        sys.exit(1)

    print(f"--- Validação de Schema: {target_json} ---")
    try:
        with open(target_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERRO ao carregar JSON: {e}", file=sys.stderr)
        sys.exit(1)

    erros = validar_schema(data)
    if erros:
        print(f"Falha na validação! Encontrados {len(erros)} erros:")
        for err in erros:
            print(f"  ✗ {err}")
        sys.exit(1)

    print(f"✓ Schema validado com sucesso! Total de condições: {len(data['condicoes'])}")
    print(f"  Versão: {data.get('versao')} | Instituição: {data.get('instituicao')}")

    if not args.check_only:
        sincronizar_arquivos(data, base_dir)
        print("Sincronização concluída com sucesso!")

if __name__ == '__main__':
    main()
