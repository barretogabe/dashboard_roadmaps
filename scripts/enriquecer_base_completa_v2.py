#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de enriquecimento e padronização profunda da base de dados dos Roadmaps NAPeN.
Aplica:
1. Substituição de todas as ocorrências de LMR por 'Limiar Motor de Repouso (LMR)'.
2. Detalhamento neurofisiológico de protocolos TBS (iTBS e cTBS).
3. Padronização ABNT em Title Case (primeira letra maiúscula, ex: 'Lefaucheur et al., 2020').
4. Separação explícita entre a Diretriz Internacional (Nível de Evidência) e o Ensaio Clínico Seminal do Protocolo.
5. Inclusão da estrutura 'escalas_detalhadas' em cada modalidade, permitindo alternância entre múltiplas escalas (ex: BBS e SARA nas Ataxias) e modo ordinal na EAM (0, 1, 1+, 2, 3, 4).
6. Remoção de qualquer menção a 'beira do leito' ou 'beira leito'.
"""

import json
import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
JSON_PATH = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

def clean_lmr(text):
    if not isinstance(text, str):
        return text
    # Evita duplicações como "Limiar Motor de Repouso (Limiar Motor de Repouso (LMR))"
    text = re.sub(r'Limiar Motor de Repouso\s*\((?:Limiar Motor de Repouso\s*)?LMR\)', 'LMR_TEMP', text)
    text = re.sub(r'Limiar Motor de Repouso', 'LMR_TEMP', text)
    text = re.sub(r'\bLMR\b', 'LMR_TEMP', text)
    return text.replace('LMR_TEMP', 'Limiar Motor de Repouso (LMR)')

def clean_beira_leito(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'beira\s*(?:do\s*)?leito', 'avaliação clínica individual', text, flags=re.IGNORECASE)
    return text

def parse_scale_options(scale_str, meta_str, condition_id, factor_id):
    """Gera a lista de escalas estruturadas com direção de melhora e parâmetros."""
    scale_str_clean = scale_str or ''
    options = []
    
    # Caso 1: EAM - Escala de Ashworth Modificada
    if 'ashworth' in scale_str_clean.lower() or 'eam' in scale_str_clean.lower():
        if factor_id == 'espasticidade' or 'espasticidade' in scale_str_clean.lower():
            return [{
                "id": "eam",
                "nome": "Escala de Ashworth Modificada (EAM)",
                "sigla": "EAM",
                "tipo": "ordinal_eam",
                "graus": ["0", "1", "1+", "2", "3", "4"],
                "graus_desc": [
                    "0: Tônus muscular normal",
                    "1: Leve aumento no final do arco",
                    "1+: Leve aumento na primeira metade do arco",
                    "2: Aumento pronunciado na maior parte do arco",
                    "3: Aumento considerável, movimento passivo difícil",
                    "4: Parte afetada rígida em flexão ou extensão"
                ],
                "direcao_melhora": "reducao",
                "meta_texto": "Redução de pelo menos 1 nível na EAM para flexores de punho e dedos",
                "min": 0,
                "max": 4
            }]
    
    # Caso 2: Ataxia Cerebelar - Equilíbrio (BBS e SARA)
    if condition_id == 'ataxia-cerebelar' and factor_id == 'equilibrio':
        return [
            {
                "id": "bbs",
                "nome": "Berg Balance Scale (BBS)",
                "sigla": "BBS",
                "tipo": "continua",
                "min": 0,
                "max": 56,
                "direcao_melhora": "aumento",
                "meta_texto": "Ganho clinicamente relevante na pontuação BBS (aumento de pontos)",
                "placeholder": "Ex: 38"
            },
            {
                "id": "sara",
                "nome": "Scale for Assessment and Rating of Ataxia (SARA)",
                "sigla": "SARA",
                "tipo": "continua",
                "min": 0,
                "max": 40,
                "direcao_melhora": "reducao",
                "meta_texto": "Redução clinicamente perceptível na pontuação SARA",
                "placeholder": "Ex: 18"
            }
        ]
        
    # Caso 3: Ataxia Cerebelar - Severidade Motora (SARA e 9HPT)
    if condition_id == 'ataxia-cerebelar' and factor_id == 'severidade_motora':
        return [
            {
                "id": "sara",
                "nome": "Scale for Assessment and Rating of Ataxia (SARA)",
                "sigla": "SARA",
                "tipo": "continua",
                "min": 0,
                "max": 40,
                "direcao_melhora": "reducao",
                "meta_texto": "Redução clinicamente perceptível na pontuação SARA",
                "placeholder": "Ex: 16"
            },
            {
                "id": "9hpt",
                "nome": "9-Hole Peg Test (9HPT)",
                "sigla": "9HPT",
                "tipo": "continua",
                "min": 10,
                "max": 180,
                "direcao_melhora": "reducao",
                "meta_texto": "Redução no tempo de execução do teste (segundos)",
                "placeholder": "Ex: 45 (segundos)"
            }
        ]

    # Caso 4: Dor (EVA e DN4)
    if 'dor' in factor_id or 'eva' in scale_str_clean.lower():
        return [
            {
                "id": "eva",
                "nome": "Escala Visual Analógica de Dor (EVA)",
                "sigla": "EVA",
                "tipo": "continua",
                "min": 0,
                "max": 10,
                "direcao_melhora": "reducao",
                "meta_texto": "Redução clinicamente significativa ≥ 30% na escala EVA de dor",
                "placeholder": "Ex: 8 (de 0 a 10)"
            },
            {
                "id": "dn4",
                "nome": "Questionário de Dor Neuropática DN4",
                "sigla": "DN4",
                "tipo": "continua",
                "min": 0,
                "max": 10,
                "direcao_melhora": "reducao",
                "meta_texto": "Redução dos sintomas neuropáticos (escore < 4)",
                "placeholder": "Ex: 6 (de 0 a 10)"
            }
        ]

    # Caso 5: Afasia (BNT e WAB/Fluência)
    if condition_id == 'avc-afasia':
        if factor_id == 'expressao':
            return [
                {
                    "id": "bnt",
                    "nome": "Teste de Nomeação de Boston (BNT)",
                    "sigla": "BNT",
                    "tipo": "continua",
                    "min": 0,
                    "max": 60,
                    "direcao_melhora": "aumento",
                    "meta_texto": "Ganho substancial na nomeação de itens treinados e não treinados",
                    "placeholder": "Ex: 28"
                },
                {
                    "id": "fluencia",
                    "nome": "Fluência Verbal Semântica/Fonêmica",
                    "sigla": "Fluência Verbal",
                    "tipo": "continua",
                    "min": 0,
                    "max": 50,
                    "direcao_melhora": "aumento",
                    "meta_texto": "Aumento no número de palavras evocadas por minuto",
                    "placeholder": "Ex: 8 (palavras/min)"
                }
            ]
        elif factor_id == 'compreensao':
            return [
                {
                    "id": "wab",
                    "nome": "Western Aphasia Battery (WAB-R)",
                    "sigla": "WAB",
                    "tipo": "continua",
                    "min": 0,
                    "max": 100,
                    "direcao_melhora": "aumento",
                    "meta_texto": "Evolução no Quociente de Afasia (AQ) e compreensão auditiva",
                    "placeholder": "Ex: 62"
                },
                {
                    "id": "token",
                    "nome": "Teste Token de Compreensão Oral",
                    "sigla": "Token",
                    "tipo": "continua",
                    "min": 0,
                    "max": 36,
                    "direcao_melhora": "aumento",
                    "meta_texto": "Aumento de acertos nas ordens complexas",
                    "placeholder": "Ex: 18"
                }
            ]

    # Caso 6: Depressão Maior (HAMD-17 e HAM-A / MADRS)
    if condition_id == 'depressao-maior':
        if factor_id == 'comorbidade_ansiedade':
            return [
                {
                    "id": "hamd",
                    "nome": "Escala Hamilton de Depressão (HAM-D 17)",
                    "sigla": "HAM-D 17",
                    "tipo": "continua",
                    "min": 0,
                    "max": 52,
                    "direcao_melhora": "reducao",
                    "meta_texto": "Redução ≥ 50% na pontuação HAM-D 17 (resposta clínica)",
                    "placeholder": "Ex: 24"
                },
                {
                    "id": "hama",
                    "nome": "Escala Hamilton de Ansiedade (HAM-A)",
                    "sigla": "HAM-A",
                    "tipo": "continua",
                    "min": 0,
                    "max": 56,
                    "direcao_melhora": "reducao",
                    "meta_texto": "Redução concomitante dos sintomas ansiosos",
                    "placeholder": "Ex: 22"
                }
            ]
        else:
            return [
                {
                    "id": "hamd",
                    "nome": "Escala Hamilton de Depressão (HAM-D 17)",
                    "sigla": "HAM-D 17",
                    "tipo": "continua",
                    "min": 0,
                    "max": 52,
                    "direcao_melhora": "reducao",
                    "meta_texto": "Redução ≥ 50% na pontuação HAM-D (resposta) ou escore ≤ 7 (remissão)",
                    "placeholder": "Ex: 22"
                },
                {
                    "id": "madrs",
                    "nome": "Escala Montgomery-Åsberg (MADRS)",
                    "sigla": "MADRS",
                    "tipo": "continua",
                    "min": 0,
                    "max": 60,
                    "direcao_melhora": "reducao",
                    "meta_texto": "Redução ≥ 50% na pontuação MADRS",
                    "placeholder": "Ex: 28"
                }
            ]

    # Caso 7: Alzheimer / CCL (MEEM e ADAS-cog)
    if condition_id == 'alzheimer-ccl':
        return [
            {
                "id": "meem",
                "nome": "Mini-Exame do Estado Mental (MEEM)",
                "sigla": "MEEM",
                "tipo": "continua",
                "min": 0,
                "max": 30,
                "direcao_melhora": "aumento",
                "meta_texto": "Estabilização ou ganho pontual nos domínios cognitivos",
                "placeholder": "Ex: 19"
            },
            {
                "id": "adas",
                "nome": "ADAS-cog (Subescala Cognitiva)",
                "sigla": "ADAS-cog",
                "tipo": "continua",
                "min": 0,
                "max": 70,
                "direcao_melhora": "reducao",
                "meta_texto": "Redução no escore de erro ou estabilização da perda cognitiva",
                "placeholder": "Ex: 32"
            }
        ]

    # Padrão genérico de 1 escala
    is_reduction = any(term in meta_str.lower() for term in ['redução', 'queda', 'diminuição', 'alívio'])
    return [{
        "id": "principal",
        "nome": scale_str_clean,
        "sigla": scale_str_clean.split('(')[-1].replace(')', '').strip() if '(' in scale_str_clean else scale_str_clean[:12],
        "tipo": "continua",
        "min": 0,
        "max": 100,
        "direcao_melhora": "reducao" if is_reduction else "aumento",
        "meta_texto": meta_str,
        "placeholder": "Ex: 20"
    }]

# Itera sobre todas as condições e modalidades
for c in data['condicoes']:
    cid = c['id']
    for fid, m in c.get('modalidades', {}).items():
        # 1. Limpeza de LMR em todos os campos de texto
        m['intensidade'] = clean_lmr(m.get('intensidade', ''))
        m['pulsos_duracao'] = clean_lmr(m.get('pulsos_duracao', ''))
        m['sessoes'] = clean_lmr(m.get('sessoes', ''))
        m['notas_clinicas'] = clean_beira_leito(clean_lmr(m.get('notas_clinicas', '')))
        
        sa = m.get('sessoes_ajuste', {})
        if sa:
            sa['quando_reavaliar'] = clean_beira_leito(clean_lmr(sa.get('quando_reavaliar', '')))
            sa['ajuste_dose'] = clean_beira_leito(clean_lmr(sa.get('ajuste_dose', '')))
            sa['regra_interrupcao'] = clean_beira_leito(clean_lmr(sa.get('regra_interrupcao', '')))
            
        alt = m.get('protocolo_alternativo', {})
        if alt:
            alt['parametros'] = clean_lmr(alt.get('parametros', ''))
            alt['observacoes'] = clean_beira_leito(clean_lmr(alt.get('observacoes', '')))

        # 2. Detalhamento neurofisiológico de protocolos TBS
        tecnica = m.get('tecnica', '')
        if 'tbs' in tecnica.lower() or 'tbs' in m.get('modalidade_sigla', '').lower():
            if 'itbs' in tecnica.lower() or 'intermitente' in tecnica.lower() or 'tempo_reduzido' in fid:
                m['tecnica'] = "Estimulação Magnética Transcraniana por Theta Burst Intermitente (iTBS)"
                m['modalidade_sigla'] = "iTBS"
                if 'frequencia' in m and 'tripletos' not in m['frequencia'].lower():
                    m['frequencia'] = "iTBS: Trens de tripletos a 50 Hz repetidos a 5 Hz (2s ativo, 8s intervalo de repouso)"
                if cid == 'depressao-maior' and fid == 'tempo_reduzido':
                    m['pulsos_duracao'] = "1.800 pulsos totais por sessão (3 blocos de 600 pulsos ou trem contínuo em 3 min 8 s)"
                    m['intensidade'] = "120% do Limiar Motor de Repouso (LMR) ajustado com bobina figura de 8"
            elif 'ctbs' in tecnica.lower() or 'contínuo' in tecnica.lower():
                m['tecnica'] = "Estimulação Magnética Transcraniana por Theta Burst Contínuo (cTBS)"
                m['modalidade_sigla'] = "cTBS"
                if 'frequencia' in m and 'tripletos' not in m['frequencia'].lower():
                    m['frequencia'] = "cTBS: Estimulação contínua ininterrupta a 50 Hz em tripletos a 5 Hz por 40 segundos (600 pulsos)"
                m['intensidade'] = "70% a 80% do Limiar Motor de Repouso (LMR)"

        # 3. Padronização ABNT Title Case em diretriz_ref e artigo_referencia
        dref = m.get('diretriz_ref', {})
        if dref:
            # Garante Title Case: 'Lefaucheur et al., 2020'
            ano = dref.get('ano', 2020)
            dref['autores'] = "Lefaucheur et al."
            dref['nome'] = f"Lefaucheur et al., {ano} (IFCN)"
            dref['citacao_completa'] = f"Lefaucheur et al., {ano}. Clin Neurophysiol, 131(2):474–528." if ano == 2020 else f"Lefaucheur et al., {ano}. Clin Neurophysiol, 128(1):56–92."
            
        # 4. Formatação de diretriz_internacional para a ordem recomendada:
        # "Recomendação Clínica (Nível de Evidência)"
        di = m.get('diretriz_internacional', '')
        if di.startswith('Lefaucheur / IFCN: '):
            m['diretriz_internacional'] = di.replace('Lefaucheur / IFCN: ', '').strip()
        elif di.startswith('Lefaucheur: '):
            m['diretriz_internacional'] = di.replace('Lefaucheur: ', '').strip()
        elif di.startswith('Consenso NAPeN: '):
            m['diretriz_internacional'] = di.replace('Consenso NAPeN: ', 'Recomendação Consensual NAPeN: ').strip()

        # 5. Artigo de Referência com Autores em Title Case
        art = m.get('artigo_referencia', {})
        if art and 'autores' in art:
            # Garante Title Case
            art['autores'] = art['autores'].replace('LEFAUCHEUR', 'Lefaucheur').replace('BLUMBERGER', 'Blumberger')
            if 'citacao_completa' in art:
                art['citacao_completa'] = art['citacao_completa'].replace('LEFAUCHEUR', 'Lefaucheur').replace('BLUMBERGER', 'Blumberger')

        # 6. Escalas Detalhadas (Suporte a Múltiplas Escalas e EAM)
        m['escalas_detalhadas'] = parse_scale_options(m.get('escala_recomendada', ''), m.get('meta_melhora', ''), cid, fid)

# Salva arquivo atualizado
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Base enriquecida com sucesso: {JSON_PATH}")
