#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Construtor Integral dos 18 Roadmaps Oficiais (RM01 a RM18)
Consolida as 13 condições clínicas diretamente de scripts/roadmaps_oficiais.py,
injeta auditoria GRADE/AMSTAR 2 e tolerabilidade específica por roadmap e
aplica higienização terminológica estrita em napen_roadmaps_data.json e js/data.js.
"""

import json
import os
import re
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.avaliar_grade_amstar import (  # noqa: E402
    CATALOG_FILE,
    _build_audit_entry_from_meta,
)
from scripts.roadmaps_oficiais import build_official_conditions  # noqa: E402

JSON_TARGET = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
JS_TARGET = os.path.join(BASE_DIR, 'js', 'data.js')


def higienizar_texto(text):
    """Remove forbidden legacy terms and normalizes clinical terminology."""
    if not isinstance(text, str):
        return text
    text = re.sub(r'\bseminal\b', 'de referência', text, flags=re.IGNORECASE)
    text = re.sub(r'\bseminais\b', 'de referência', text, flags=re.IGNORECASE)
    text = re.sub(r'Ensaio Clínico Randomizado de Referência', 'Estudos de referência', text, flags=re.IGNORECASE)
    text = re.sub(r'Tamanho de Efeito Padronizado', 'Tamanho de Efeito Esperado', text, flags=re.IGNORECASE)
    text = re.sub(r'Moderado a Grande', 'Moderado', text, flags=re.IGNORECASE)
    text = re.sub(r'moderado a grande', 'moderado', text, flags=re.IGNORECASE)
    text = re.sub(r'beira\s*(?:do\s*)?leito', 'avaliação clínica individual', text, flags=re.IGNORECASE)
    return text


def aplicar_higienizacao_recursiva(obj):
    """Recursively applies higienizar_texto across dicts and lists."""
    if isinstance(obj, dict):
        return {k: aplicar_higienizacao_recursiva(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [aplicar_higienizacao_recursiva(elem) for elem in obj]
    if isinstance(obj, str):
        return higienizar_texto(obj)
    return obj


def main():
    print('Iniciando geração integral dos 18 Roadmaps Oficiais (RM01–RM18)...')

    catalog = {}
    if os.path.exists(CATALOG_FILE):
        with open(CATALOG_FILE, 'r', encoding='utf-8') as f:
            catalog = json.load(f)

    existing_meta = {
        'versao': '2025-2026',
        'data_extracao': '2026-11-17',
        'instituicao': 'Rede NAPeN — Rede de Núcleos de Assistência e Pesquisa em Neuromodulação',
        'url_oficial': 'https://www.neuromodulation-net.com/',
    }
    if os.path.exists(JSON_TARGET):
        try:
            with open(JSON_TARGET, 'r', encoding='utf-8') as f:
                old = json.load(f)
            existing_meta['versao'] = old.get('versao', existing_meta['versao'])
            existing_meta['instituicao'] = old.get('instituicao', existing_meta['instituicao'])
            existing_meta['url_oficial'] = old.get('url_oficial', existing_meta['url_oficial'])
        except Exception:
            pass

    condicoes = build_official_conditions()

    # Sincroniza GRADE, AMSTAR 2 e tolerabilidade para todas as modalidades a partir de audit_meta
    for c in condicoes:
        cid = c['id']
        for mk, m in c.get('modalidades', {}).items():
            entry = _build_audit_entry_from_meta(cid, mk, m, catalog)
            if isinstance(m.get('meta_analise'), dict):
                m['meta_analise']['amstar2'] = entry['meta_analise']['amstar2']
            m['grade'] = entry['grade']
            m['tolerabilidade_roadmap'] = entry['tolerabilidade_roadmap']

    target_data = {
        'versao': existing_meta['versao'],
        'data_extracao': '2026-11-17',
        'instituicao': existing_meta['instituicao'],
        'url_oficial': existing_meta['url_oficial'],
        'total_condicoes': len(condicoes),
        'condicoes': aplicar_higienizacao_recursiva(condicoes),
    }

    with open(JSON_TARGET, 'w', encoding='utf-8') as f:
        json.dump(target_data, f, ensure_ascii=False, indent=2)

    with open(JS_TARGET, 'w', encoding='utf-8') as f:
        f.write('// Rede NAPeN — Base de Dados dos Roadmaps Clínicos (Auto-gerada)\n')
        f.write('// Alinhamento integral aos 18 Roadmaps Oficiais (RM01–RM18) e auditoria GRADE/AMSTAR 2\n')
        f.write('window.NAPEN_DATA = ')
        json.dump(target_data, f, ensure_ascii=False, indent=2)
        f.write(';\n')

    print(f'✓ {len(condicoes)} condições oficiais gravadas em {JSON_TARGET} ({os.path.getsize(JSON_TARGET)} bytes)')
    print(f'✓ Base JS gravada em {JS_TARGET} ({os.path.getsize(JS_TARGET)} bytes)')


if __name__ == '__main__':
    main()
