#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Atualização dos Tamanhos de Efeito por Escala Clínica Individual
Garante que cada escala em 'escalas_detalhadas' tenha seu próprio tamanho de efeito,
permitindo exibição isolada e contextual quando o usuário alterna as abas na interface.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')

ESCALAS_EFEITO_MAP = {
    # Ataxia Cerebelar - Equilíbrio
    ("ataxia-cerebelar", "equilibrio", "bbs"): "Aumento médio de +11,77% na pontuação da Berg Balance Scale (BBS)",
    ("ataxia-cerebelar", "equilibrio", "sara"): "Melhora média de -14,8% na pontuação da escala SARA (ganho de +31,11% na velocidade no TC10m)",
    
    # Ataxia Cerebelar - Severidade Motora
    ("ataxia-cerebelar", "severidade_motora", "sara"): "Redução média de -25% na escala SARA (e redução de -28% no ICARS)",
    ("ataxia-cerebelar", "severidade_motora", "9hpt"): "Melhora média de 12,83% no tempo de execução do 9-Hole Peg Test (9HPT)",

    # Depressão Maior - Moderada a Grave
    ("depressao-maior", "moderada_grave", "hamd"): "Redução média de ~55% no HDRS-21 (taxa de resposta clínica típica de 50–60%)",
    ("depressao-maior", "moderada_grave", "madrs"): "Redução média de 52% na escala MADRS (taxa de resposta clínica de 50–60%)",

    # Depressão Maior - Tempo Reduzido (TBS)
    ("depressao-maior", "tempo_reduzido", "hamd"): "Redução de 54,7% na HAM-D 17 (não-inferioridade comprovada ao protocolo 10 Hz de 37 min)",
    ("depressao-maior", "tempo_reduzido", "madrs"): "Redução clinicamente equivalente na escala MADRS (não-inferioridade ao 10 Hz convencional)",

    # Depressão Maior - Comorbidade com Ansiedade
    ("depressao-maior", "comorbidade_ansiedade", "hamd"): "Redução média de ~50% nos sintomas depressivos na HAM-D 17",
    ("depressao-maior", "comorbidade_ansiedade", "hama"): "Redução média de 32% a 45% nos escores de ansiedade comórbida na HAM-A",

    # AVC Membro Superior - Dor
    ("avc-membro-superior", "dor", "eva"): "Redução média de 24% a 36% na escala EVA de dor crônica pós-AVC",
    ("avc-membro-superior", "dor", "dn4"): "Resolução dos sintomas neuropáticos e alodinia (pontuação DN4 < 4)",

    # Dor Neuropática Crônica - Geral
    ("dor-neuropatica", "geral", "eva"): "Redução média de 24% a 36% na escala EVA de intensidade da dor",
    ("dor-neuropatica", "geral", "dn4"): "Melhora precoce em alodinia mecânica e hiperalgesia (queda do escore DN4 < 4)",

    # Dor Neuropática Crônica - Espinhal
    ("dor-neuropatica", "espinhal", "eva"): "Redução média de até 20% nos escores de dor radicular crônica na escala EVA",
    ("dor-neuropatica", "espinhal", "dn4"): "Alívio dos sintomas de queimação, choques e dormência espinhal (DN4 < 4)",

    # AVC Afasia - Expressão
    ("avc-afasia", "expressao", "bnt"): "Aumento estatisticamente significativo na precisão de nomeação de itens no BNT",
    ("avc-afasia", "expressao", "fluencia"): "Aumento significativo na velocidade de evocação lexical e número de palavras evocadas por minuto",

    # AVC Afasia - Compreensão
    ("avc-afasia", "compreensao", "wab"): "Evolução clínica de 5 a 8 pontos no Quociente de Afasia (AQ) da WAB-R",
    ("avc-afasia", "compreensao", "token"): "Melhora significativa na acurácia de compreensão de frases e ordens verbais complexas no Teste Token",

    # Alzheimer e CCL - Memória
    ("alzheimer-ccl", "alzheimer_memoria", "meem"): "Ganho médio de 9,0% a 21,9% no MEEM sustentado por até 3 meses",
    ("alzheimer-ccl", "alzheimer_memoria", "adas"): "Melhora média de 32,64% na subescala cognitiva ADAS-cog sustentada por até 3 meses",

    # Alzheimer e CCL - Declínio Inicial
    ("alzheimer-ccl", "ccl_cognicao", "meem"): "Melhora média de 9,12% no MEEM após o ciclo de estimulação",
    ("alzheimer-ccl", "ccl_cognicao", "adas"): "Aumento médio de 29% na retenção de memória episódica na ADAS-cog",
}

def update_scales():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for c in data['condicoes']:
        cid = c['id']
        for mod_id, mod in c.get('modalidades', {}).items():
            mod_effect = mod.get('tamanho_efeito')
            
            # Ajuste específico para sintomas neuropsiquiátricos em Alzheimer
            if cid == "alzheimer-ccl" and mod_id == "sintomas_neuropsiquiatricos":
                mod['escalas_detalhadas'] = [
                    {
                        "id": "npi",
                        "nome": "Inventário Neuropsiquiátrico (NPI)",
                        "sigla": "NPI",
                        "tipo": "continuo_reducao",
                        "meta_texto": "Redução clinicamente relevante ≥ 4 a 8 pontos no escore total do NPI",
                        "tamanho_efeito": "Melhora média de 60,9% no Inventário Neuropsiquiátrico (NPI)",
                        "placeholder": "Ex: 36"
                    },
                    {
                        "id": "cornell",
                        "nome": "Escala de Depressão de Cornell em Demência",
                        "sigla": "Cornell",
                        "tipo": "continuo_reducao",
                        "meta_texto": "Redução clinicamente significativa dos sintomas depressivos em demência",
                        "tamanho_efeito": "Redução média de 43,3% na Escala de Depressão de Cornell após 10 sessões",
                        "placeholder": "Ex: 18"
                    }
                ]
                continue

            scales = mod.get('escalas_detalhadas', [])
            for s in scales:
                sid = s.get('id')
                key = (cid, mod_id, sid)
                if key in ESCALAS_EFEITO_MAP:
                    s['tamanho_efeito'] = ESCALAS_EFEITO_MAP[key]
                elif not s.get('tamanho_efeito'):
                    s['tamanho_efeito'] = mod_effect

    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    sys.path.insert(0, os.path.join(BASE_DIR, 'scripts'))
    from atualizar_base import sincronizar_arquivos
    sincronizar_arquivos(data, BASE_DIR)
    print("Atualização concluída com sucesso!")

if __name__ == '__main__':
    update_scales()
