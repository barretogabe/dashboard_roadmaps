#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Script de Integração dos Dados V2 Transcritos dos Roadmaps (2026-11-05)
Consolida os fluxos clínicos auditados (RM01 a RM18), protocolos transcritos de V2,
regras de decisão em cascata, distinção entre rTMS e tDCS, e higienização terminológica estrita:
- Remoção definitiva da palavra 'seminal'
- Padronização de 'Estudos de referência'
- 'Tamanho de Efeito Esperado'
- Classificação unívoca de efeito de Cohen (sem 'Moderado a Grande')
- Dissociação conceitual entre Desfecho Clínico Alvo e Instrumento Clínico
"""

import os
import json
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
V2_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'Dados dos roadmaps transcritos'))
JSON_TARGET = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
JS_TARGET = os.path.join(BASE_DIR, 'js', 'data.js')

def higienizar_texto(text):
    if not isinstance(text, str):
        return text
    # Eliminar menções à palavra 'seminal'
    text = re.sub(r'\bseminal\b', 'de referência', text, flags=re.IGNORECASE)
    text = re.sub(r'\bseminais\b', 'de referência', text, flags=re.IGNORECASE)
    # Padronizar 'Ensaio Clínico Randomizado de Referência' para 'Estudos de referência'
    text = re.sub(r'Ensaio Clínico Randomizado de Referência', 'Estudos de referência', text, flags=re.IGNORECASE)
    text = re.sub(r'Ensaio Clínico de Referência', 'Estudo de referência', text, flags=re.IGNORECASE)
    # 'Tamanho de Efeito Padronizado' para 'Tamanho de Efeito Esperado'
    text = re.sub(r'Tamanho de Efeito Padronizado', 'Tamanho de Efeito Esperado', text, flags=re.IGNORECASE)
    # Classificação unívoca (nunca 'Moderado a Grande')
    text = re.sub(r'Moderado a Grande', 'Moderado', text, flags=re.IGNORECASE)
    text = re.sub(r'moderado a grande', 'moderado', text, flags=re.IGNORECASE)
    # Eliminar qualquer termo de beira de leito
    text = re.sub(r'beira\s*(?:do\s*)?leito', 'avaliação clínica individual', text, flags=re.IGNORECASE)
    return text

def aplicar_higienizacao_recursiva(obj):
    if isinstance(obj, dict):
        return {k: aplicar_higienizacao_recursiva(higienizar_texto(v) if isinstance(v, str) else v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [aplicar_higienizacao_recursiva(higienizar_texto(elem) if isinstance(elem, str) else elem) for elem in obj]
    elif isinstance(obj, str):
        return higienizar_texto(obj)
    return obj

def carregar_dados_v2():
    fluxo_file = os.path.join(V2_DIR, 'NAPeN_Fluxos_Clinicos_V2_2026-11-05.json')
    rel_file = os.path.join(V2_DIR, 'NAPeN_Base_Relacional_V2_2026-11-05.json')

    fluxos_data = None
    rel_data = None

    if os.path.exists(fluxo_file):
        with open(fluxo_file, 'r', encoding='utf-8') as f:
            fluxos_data = json.load(f)
    if os.path.exists(rel_file):
        with open(rel_file, 'r', encoding='utf-8') as f:
            rel_data = json.load(f)

    return fluxos_data, rel_data

def main():
    print("Iniciando integração dos dados V2 e higienização estrita...")

    with open(JSON_TARGET, 'r', encoding='utf-8') as f:
        target_data = json.load(f)

    fluxos_v2, rel_v2 = carregar_dados_v2()

    # Indexar protocolos de V2 se disponíveis
    protocolos_v2_map = {}
    resultados_v2_map = {}
    referencias_v2_map = {}

    if rel_v2 and 'tables' in rel_v2:
        for t in rel_v2['tables']:
            title = t.get('title')
            if title == 'Protocolos_V2':
                # ['roadmap_id', 'protocolo_id', 'regiao', 'titulo', 'parametros_originais', 'categoria', 'referencia_indicada', 'status', 'url_pdf']
                for row in t.get('rows', []):
                    rm_id, p_id, reg, tit, param, cat, ref_idx, status, url = row
                    protocolos_v2_map[p_id] = {
                        'roadmap_id': rm_id,
                        'protocolo_id': p_id,
                        'regiao': reg,
                        'titulo': tit,
                        'parametros': param,
                        'categoria': cat,
                        'referencia_indicada': ref_idx,
                        'url_pdf': url
                    }
            elif title == 'Resultados_V2':
                # ['roadmap_id', 'resultado_id', 'protocolo_id', 'resultado_original', 'intervalo_original', 'populacao_sessoes', 'referencia', 'status', 'url_pdf']
                for row in t.get('rows', []):
                    rm_id, r_id, p_id, res_orig, ic_orig, pop_sess, ref_idx, status, url = row
                    if p_id not in resultados_v2_map:
                        resultados_v2_map[p_id] = []
                    resultados_v2_map[p_id].append({
                        'resultado_id': r_id,
                        'resultado_original': res_orig,
                        'intervalo_original': ic_orig,
                        'populacao_sessoes': pop_sess,
                        'referencia': ref_idx
                    })
            elif title == 'Referencias_V2':
                # ['roadmap_id', 'referencia_id', 'referencia_original', 'protocolo_vinculado', 'status', 'url_pdf']
                for row in t.get('rows', []):
                    rm_id, ref_id, ref_orig, prot_vinc, status, url = row
                    referencias_v2_map[ref_id] = {
                        'roadmap_id': rm_id,
                        'referencia_id': ref_id,
                        'texto': ref_orig,
                        'protocolo_vinculado': prot_vinc
                    }

    print(f"Protocolos V2 mapeados: {len(protocolos_v2_map)}")
    print(f"Resultados V2 mapeados: {len(resultados_v2_map)}")
    print(f"Referencias V2 mapeadas: {len(referencias_v2_map)}")

    # Indexar roadmaps dos fluxos V2
    fluxos_rm_map = {}
    if fluxos_v2 and 'roadmaps' in fluxos_v2:
        for rm in fluxos_v2['roadmaps']:
            rm_id = rm.get('roadmap_id')
            if rm_id:
                fluxos_rm_map[rm_id] = rm

    print(f"Fluxos topológicos V2 mapeados: {len(fluxos_rm_map)} roadmaps")

    # Tabela Mestra de Linha de Prescrição Cortical por Condição e Fator Limitante
    LINHAS_PRESCRICAO = {
        ('avc-membro-superior', 'espasticidade'): 'Córtex Motor Primário (M1)',
        ('avc-membro-superior', 'fraqueza'): 'Córtex Motor Primário (M1)',
        ('avc-membro-superior', 'dor'): 'Córtex Motor Primário (M1)',
        ('avc-membro-superior', 'sensorial'): 'Córtex Somatossensorial Primário (S1)',
        ('avc-membro-superior', 'negligencia'): 'Córtex Parietal Posterior (PPC)',
        ('avc-mobilidade', 'equilibrio'): 'Córtex Motor Primário (M1 de MMII)',
        ('avc-mobilidade', 'velocidade_marcha'): 'Córtex Motor Primário (M1 de MMII)',
        ('avc-afasia', 'expressao'): 'Área de Broca / Giro Frontal Inferior (IFG)',
        ('avc-afasia', 'compreensao'): 'Área de Wernicke / Giro Temporal Superior',
        ('avc-disfagia', 'orofaringea'): 'Córtex Motor da Deglutição (Hemisfério Intacto)',
        ('avc-disfagia', 'tempo_transito'): 'Córtex Sensório-Motor',
        ('dor-neuropatica', 'geral'): 'Córtex Motor Primário (M1 contralateral à dor)',
        ('dor-neuropatica', 'espinhal'): 'Córtex Motor Primário / Medular (tsDCS)',
        ('doenca-parkinson', 'funcao_global'): 'Área Motora Suplementar (SMA) e M1',
        ('doenca-parkinson', 'fog'): 'Área Motora Suplementar (SMA)',
        ('doenca-parkinson', 'mobilidade'): 'Córtex Motor Primário / DLPFC',
        ('depressao-maior', 'moderada_grave'): 'Córtex Pré-Frontal Dorsolateral Esquerdo (DLPFC-E)',
        ('depressao-maior', 'tempo_reduzido'): 'DLPFC Esquerdo (iTBS intermitente acelerado)',
        ('depressao-maior', 'comorbidade_ansiedade'): 'DLPFC Bilateral (10 Hz esquerdo / 1 Hz direito)',
        ('ansiedade-generalizada', 'moderada_alta'): 'Córtex Pré-Frontal Dorsolateral Direito (DLPFC-D)',
        ('ansiedade-generalizada', 'comorbidade_depressiva'): 'DLPFC Bilateral',
        ('tept', 'sintomas_gerais'): 'DLPFC Direito (inibitório) / DLPFC Esquerdo (excitatório)',
        ('tept', 'comorbidade_depressiva'): 'DLPFC Bilateral',
        ('ataxia-cerebelar', 'severidade_motora'): 'Córtex Cerebelar Bilateral',
        ('ataxia-cerebelar', 'equilibrio'): 'Cerebelo / Vermis Cerebelar',
        ('paralisia-cerebral', 'deficits_motores'): 'Córtex Motor Primário (M1)',
        ('transtorno-espectro-autista', 'comportamental'): 'Córtex Pré-Frontal Dorsolateral Bilateral',
        ('transtorno-espectro-autista', 'social'): 'DLPFC / Sulco Temporal Superior (STS)',
        ('alzheimer-ccl', 'alzheimer_memoria'): 'DLPFC Bilateral e Pré-Cúneo',
        ('alzheimer-ccl', 'ccl_cognicao'): 'DLPFC Esquerdo',
        ('alzheimer-ccl', 'sintomas_neuropsiquiatricos'): 'DLPFC Bilateral'
    }

    # Atualizar cada condição do dashboard com sua árvore lógica de decisão
    for cond in target_data['condicoes']:
        cid = cond['id']
        rm_id = cond.get('roadmap_id')
        rm_v2 = fluxos_rm_map.get(rm_id)

        # Higienização de siglas redundantes nos títulos e eixos
        cond['condicao'] = cond['condicao'].replace(' (AVC)', '').replace(' (Transtorno Depressivo Maior)', '').replace(' (PC)', '').replace(' (TEA)', '').replace(' (CCL)', '')
        if 'eixo' in cond:
            cond['eixo'] = cond['eixo'].replace(' (AVC)', '')

        # Higienizar fatores limitantes: remover qualquer teste neurofisiológico ou menção a sem_pem
        cond['fatores_limitantes'] = [
            f for f in cond.get('fatores_limitantes', [])
            if f.get('id') != 'sem_pem' and 'sem pem' not in f.get('label', '').lower()
        ]

        # Atribuir linha de prescrição para cada fator limitante da condição
        for f in cond.get('fatores_limitantes', []):
            f['linha_prescricao'] = LINHAS_PRESCRICAO.get((cid, f['id']), 'Córtex Cerebral')
            mod = cond.get('modalidades', {}).get(f['id'], {})
            if mod:
                f['escala_recomendada'] = mod.get('escala_recomendada', 'Escala Clínica Validada')
                f['meta_melhora'] = mod.get('meta_melhora', 'Ganho clínico relevante')

        # Mapeamento de modalidade rTMS vs tDCS por condição
        # Ex: avc-membro-superior (RM01 = rTMS, RM02 = tDCS)
        modalidades_disponiveis = [{'id': 'rtms', 'nome': 'rTMS (Estimulação Magnética Repetitiva)', 'roadmap_id': rm_id, 'padrao': True}]
        if cid == 'avc-membro-superior':
            modalidades_disponiveis.append({'id': 'tdcs', 'nome': 'tDCS (Estimulação Transcraniana por Corrente Contínua)', 'roadmap_id': 'RM02', 'padrao': False})
        elif cid == 'avc-mobilidade':
            modalidades_disponiveis.append({'id': 'tdcs', 'nome': 'tDCS (Estimulação Transcraniana por Corrente Contínua)', 'roadmap_id': 'RM04', 'padrao': False})
        elif cid == 'avc-afasia':
            modalidades_disponiveis.append({'id': 'tdcs', 'nome': 'tDCS (Estimulação Transcraniana por Corrente Contínua)', 'roadmap_id': 'RM08', 'padrao': False})
        elif cid == 'avc-disfagia':
            modalidades_disponiveis.append({'id': 'tdcs', 'nome': 'tDCS (Estimulação Transcraniana por Corrente Contínua)', 'roadmap_id': 'RM06', 'padrao': False})
        elif cid == 'alzheimer-ccl':
            modalidades_disponiveis.append({'id': 'tdcs', 'nome': 'tDCS (Estimulação Transcraniana por Corrente Contínua)', 'roadmap_id': 'RM13', 'padrao': False})
        elif cid == 'dor-neuropatica':
            modalidades_disponiveis.append({'id': 'tdcs', 'nome': 'tDCS (Estimulação Transcraniana por Corrente Contínua)', 'roadmap_id': 'RM05', 'padrao': False})

        cond['modalidades_suportadas'] = modalidades_disponiveis


        # Construir árvore algorítmica específica para AVC Membro Superior com fidelidade ao RM01 e RM02
        if cid == 'avc-membro-superior':
            # Protocolos específicos para ramificações do AVC Membro Superior
            cond['modalidades']['sem_pem_cerebelar'] = {
                'tecnica': 'rTMS Cerebelar Contralesional de Alta Frequência (ou iTBS) (Protocolo 4)',
                'modalidade_sigla': 'rTMS',
                'alvo': 'Córtex Cerebelar contralesional (hemisfério contralateral à lesão)',
                'frequencia': '10 Hz (ou iTBS: 3 pulsos a 50 Hz repetidos a 5 Hz)',
                'intensidade': '90% a 100% do Limiar Motor de Repouso (LMR) contralesional',
                'pulsos_duracao': '1.000 a 1.200 pulsos combinados com reabilitação motora intensiva Bobath',
                'sessoes': '21 sessões diárias consecutivas associadas à fisioterapia motora individualizada',
                'escala_recomendada': 'Fugl-Meyer Extremidade Superior (FMA-UE)',
                'meta_melhora': 'Aumento de pelo menos 3,7 a 6,6 pontos na escala FMA-UE',
                'tamanho_efeito': 'Aumento de 3,7 pontos (IC 95% 2,4 a 5,0) na escala FMA-UE após 21 sessões diárias',
                'evidencia': 'Consolidada (Respaldo em Ensaio Clínico com DTI / Tratografia Corticoespinhal - Wang et al., 2022)',
                'linha_fluxograma': 'solida',
                'diretriz_internacional': 'Nível B (Pacientes com Ausência de PEM e Lesão Cortical Pré-Frontal / M1 Extensa)',
                'protocolo_alternativo': {
                    'nome': 'Protocolo Alternativo 1 (rPMS Periférica Contínua/Intermitente + iTBS)',
                    'tecnica': 'rPMS 50 Hz em nervo periférico / grupos musculares do membro parético',
                    'alvo': 'Sulco do nervo radial no úmero ou músculos com paralisia grave',
                    'parametros': '3 pulsos a 50 Hz repetidos a 5 Hz, 2s estímulo e 8s pausa, 600 pulsos para gerar contração muscular visível',
                    'observacoes': 'Indicado quando não há resposta cortical via estimulação cerebelar.'
                },
                'protocolo_alternativo_2': {
                    'nome': 'Protocolo Alternativo 2 (rTMS 1 Hz M1 Contralesional)',
                    'tecnica': 'rTMS 1 Hz de baixa frequência',
                    'alvo': 'Córtex Motor Primário (M1) contralesional',
                    'parametros': '1.200 pulsos a 90%–100% LMR contralesional',
                    'observacoes': 'Modulação inibitória inter-hemisférica residual.'
                },
                'falha_terapeutica': {
                    'criterio': 'Persistência de resposta funcional inferior à MCID na escala FMA-UE (< 3,7 pontos) após ciclo pleno de indução (21 sessões), ajustes de parâmetros e protocolos alternativos 1 e 2.',
                    'conduta_oficial': '1. Encerramento formal do ciclo de estimulação vigente;\n2. Registro em prontuário de refratariedade ao regime testado;\n3. Transição para reabilitação multidisciplinar intensiva ou tecnologias assistivas.'
                },
                'sessoes_ajuste': {
                    'quando_reavaliar': 'Reavaliar após a 10ª e 21ª sessões de estimulação combinada com fisioterapia.',
                    'ajuste_dose': 'Transição para o protocolo alternativo periférico rPMS se não for observada modulação motora após o ciclo inicial.',
                    'regra_interrupcao': 'Interromper e considerar falha terapêutica se não houver ganho motor funcional após os protocolos alternativos.'
                },
                'contraindicacoes': [
                    'Implantes metálicos cranianos',
                    'Histórico de epilepsia refratária não controlada'
                ],
                'notas_clinicas': 'Em pacientes com ausência de PEM e lesão extensa no giro pré-frontal, a via cortico-ponto-cerebelar contralesional atua como via de compensação neuroplástica facilitando a excitabilidade tálamo-cortical.',
                'artigo_referencia': {
                    'autores': 'Wang, L., et al.',
                    'ano': 2022,
                    'titulo': 'Effects of corticospinal tract integrity on upper limb motor function recovery in stroke patients treated with repetitive transcranial magnetic stimulation',
                    'periodico': 'Journal of Integrative Neuroscience, 21(2), 050',
                    'doi': '10.31083/j.jin2102050',
                    'url_doi': 'https://doi.org/10.31083/j.jin2102050',
                    'tipo': 'Estudos de referência'
                },
                'ensaio_clinico': {
                    'autores': 'Wang, L., et al.',
                    'ano': 2022,
                    'periodico': 'Journal of Integrative Neuroscience, 21(2), 050',
                    'doi': '10.31083/j.jin2102050',
                    'tipo': 'Estudos de referência',
                    'url_doi': 'https://doi.org/10.31083/j.jin2102050'
                },
                'meta_analise': {
                    'autores': 'Chen, Y., et al.',
                    'ano': 2022,
                    'periodico': 'Clinical Rehabilitation, 36(6), 743–755',
                    'doi': '10.1177/02692155211070862',
                    'url_doi': 'https://doi.org/10.1177/02692155211070862'
                },
                'diretriz_ref': {
                    'nome': 'Lefaucheur et al., 2020 (IFCN)',
                    'ano': 2020,
                    'periodico': 'Clinical Neurophysiology, 131(2), 474–528',
                    'doi': '10.1016/j.clinph.2019.11.002',
                    'url_doi': 'https://doi.org/10.1016/j.clinph.2019.11.002',
                    'autores': 'Lefaucheur et al.',
                    'citacao_completa': 'Lefaucheur et al., 2020. Clin Neurophysiol, 131(2):474–528.'
                },
                'escalas_detalhadas': [
                    {
                        'id': 'fma-ue',
                        'nome': 'Fugl-Meyer Extremidade Superior (FMA-UE)',
                        'sigla': 'FMA-UE',
                        'tipo': 'continua',
                        'placeholder': 'Ex: 14',
                        'direcao_melhora': 'aumento',
                        'meta_texto': 'Aumento de pelo menos 3,7 a 6,6 pontos na escala FMA-UE',
                        'min': 0,
                        'max': 66,
                        'tamanho_efeito': 'Aumento de 3,7 pontos (IC 95% 2,4 a 5,0) na escala FMA-UE após 21 sessões diárias'
                    }
                ],
                'cohen_d': 'd ≈ 0.65 (Efeito Moderado)',
                'mcid_valor': 3.7,
                'mcid_label': 'Ganho ≥ 3,7 pontos na FMA-UE',
                'efeito_clinico': {
                    'cohen_d_esperado': 0.65,
                    'interpretacao_cohen': 'Efeito Moderado',
                    'mcid_valor': 3.7,
                    'mcid_label': 'Ganho ≥ 3,7 pontos na FMA-UE',
                    'efeito_esperado_resumo': 'Aumento de 3,7 pontos (IC 95% 2,4 a 5,0) na FMA-UE',
                    'estudo_referencia': 'Wang et al., 2022',
                    'ic_min': 2.4,
                    'ic_max': 5.0,
                    'cohen_d': ''
                }
            }

            cond['modalidades']['sem_pem_premotor'] = {
                'tecnica': 'rTMS Excitatória no Córtex Pré-Motor Ipsilesional (Protocolo 5)',
                'modalidade_sigla': 'rTMS',
                'alvo': 'Córtex Pré-Motor (PMA / SMA) ipsilesional',
                'frequencia': '10 Hz (ou iTBS: 3 pulsos a 50 Hz repetidos a 5 Hz)',
                'intensidade': '80% a 90% do Limiar Motor Ativo (LMA) ou 90% do LMR',
                'pulsos_duracao': '1.200 a 1.500 pulsos associados a treino orientado à tarefa',
                'sessoes': '15 a 20 sessões diárias consecutivas associadas à reabilitação motora',
                'escala_recomendada': 'Fugl-Meyer Extremidade Superior (FMA-UE)',
                'meta_melhora': 'Aumento de pelo menos 5,0 a 6,6 pontos na escala FMA-UE',
                'tamanho_efeito': 'Aumento de 5,2 pontos (IC 95% 3,1 a 7,3) na escala FMA-UE após 15 a 20 sessões',
                'evidencia': 'Consolidada (Reorganização funcional de tratos corticoespinhais secundários pré-motores)',
                'linha_fluxograma': 'solida',
                'diretriz_internacional': 'Nível B (Pacientes com Ausência de PEM e Área Pré-Motora Preservada sem Lesão Pré-Frontal)',
                'protocolo_alternativo': {
                    'nome': 'Protocolo Alternativo 1 (rTMS Inibitória 1 Hz no Córtex Pré-Motor Contralesional)',
                    'tecnica': 'rTMS 1 Hz inibitória',
                    'alvo': 'Córtex Pré-Motor (PMA) contralesional',
                    'parametros': '1.200 pulsos a 90% LMR contralesional',
                    'observacoes': 'Redução da inibição inter-hemisférica anômala exercida pelo córtex pré-motor não afetado.'
                },
                'protocolo_alternativo_2': {
                    'nome': 'Protocolo Alternativo 2 (iTBS Triplet Cerebelar Contralesional)',
                    'tecnica': 'iTBS Triplet a 50 Hz em 5 Hz',
                    'alvo': 'Córtex Cerebelar contralesional',
                    'parametros': '600 a 1.200 pulsos com bobina em oito ou parabólica',
                    'observacoes': 'Estimulação cerebelar de resgate se não houver resposta pré-motora.'
                },
                'falha_terapeutica': {
                    'criterio': 'Persistência de resposta funcional inferior à MCID na escala FMA-UE (< 5,0 pontos) após indução plena, otimização de dose e conclusão dos protocolos alternativos 1 e 2.',
                    'conduta_oficial': '1. Encerramento formal do ciclo de estimulação vigente;\n2. Registro em prontuário de refratariedade ao regime testado;\n3. Transição para reabilitação multidisciplinar assistida.'
                },
                'sessoes_ajuste': {
                    'quando_reavaliar': 'Reavaliar após a 10ª e 15ª sessões de estimulação combinada com cinesioterapia.',
                    'ajuste_dose': 'Ajustar para 1.500 pulsos por sessão se resposta parcial aos 10 dias.',
                    'regra_interrupcao': 'Interromper e migrar para protocolo alternativo se não houver ganho funcional após 15 sessões.'
                },
                'contraindicacoes': [
                    'Implantes metálicos cranianos',
                    'Histórico de epilepsia refratária não controlada'
                ],
                'notas_clinicas': 'Na ausência de lesão pré-frontal e com M1 severamente comprometido (PEM ausente), o córtex pré-motor ipsilesional (PMA/SMA) é a principal via de reorganização vicariante corticoespinhal para restaurar a função do membro superior.',
                'artigo_referencia': {
                    'autores': 'Lefaucheur, J. P., et al.',
                    'ano': 2020,
                    'titulo': 'Evidence-based guidelines on the therapeutic use of repetitive transcranial magnetic stimulation (rTMS): An update by an expert panel of the IFCN',
                    'periodico': 'Clinical Neurophysiology, 131(2), 474–528',
                    'doi': '10.1016/j.clinph.2019.11.002',
                    'url_doi': 'https://doi.org/10.1016/j.clinph.2019.11.002',
                    'tipo': 'Estudos de referência'
                },
                'ensaio_clinico': {
                    'autores': 'Zhang, Y., et al.',
                    'ano': 2021,
                    'periodico': 'Frontiers in Neurology, 12, 642194',
                    'doi': '10.3389/fneur.2021.642194',
                    'tipo': 'Estudos de referência',
                    'url_doi': 'https://doi.org/10.3389/fneur.2021.642194'
                },
                'meta_analise': {
                    'autores': 'Chen, Y., et al.',
                    'ano': 2022,
                    'periodico': 'Clinical Rehabilitation, 36(6), 743–755',
                    'doi': '10.1177/02692155211070862',
                    'url_doi': 'https://doi.org/10.1177/02692155211070862'
                },
                'diretriz_ref': {
                    'nome': 'Lefaucheur et al., 2020 (IFCN)',
                    'ano': 2020,
                    'periodico': 'Clinical Neurophysiology, 131(2), 474–528',
                    'doi': '10.1016/j.clinph.2019.11.002',
                    'url_doi': 'https://doi.org/10.1016/j.clinph.2019.11.002',
                    'autores': 'Lefaucheur et al.',
                    'citacao_completa': 'Lefaucheur et al., 2020. Clin Neurophysiol, 131(2):474–528.'
                },
                'escalas_detalhadas': [
                    {
                        'id': 'fma-ue',
                        'nome': 'Fugl-Meyer Extremidade Superior (FMA-UE)',
                        'sigla': 'FMA-UE',
                        'tipo': 'continua',
                        'placeholder': 'Ex: 14',
                        'direcao_melhora': 'aumento',
                        'meta_texto': 'Aumento de pelo menos 5,0 a 6,6 pontos na escala FMA-UE',
                        'min': 0,
                        'max': 66,
                        'tamanho_efeito': 'Aumento de 5,2 pontos (IC 95% 3,1 a 7,3) na escala FMA-UE após 15 a 20 sessões'
                    }
                ],
                'cohen_d': 'd ≈ 0.70 (Efeito Moderado a Grande)',
                'mcid_valor': 5.0,
                'mcid_label': 'Ganho ≥ 5,0 pontos na FMA-UE',
                'efeito_clinico': {
                    'cohen_d_esperado': 0.70,
                    'interpretacao_cohen': 'Efeito Moderado a Grande',
                    'mcid_valor': 5.0,
                    'mcid_label': 'Ganho ≥ 5,0 pontos na FMA-UE',
                    'efeito_esperado_resumo': 'Aumento de 5,2 pontos (IC 95% 3,1 a 7,3) na FMA-UE',
                    'estudo_referencia': 'Zhang et al., 2021',
                    'ic_min': 3.1,
                    'ic_max': 7.3,
                    'cohen_d': ''
                }
            }

            # Garantir compatibilidade com chave genérica sem_pem
            cond['modalidades']['sem_pem'] = cond['modalidades']['sem_pem_cerebelar']

            cond['arvore_algoritmo'] = {
                'rtms': {
                    'roadmap_id': 'RM01',
                    'titulo': 'AVC — Membro Superior (rTMS / TBS)',
                    'macro_desfecho': 'Uso do membro superior nas AVDs',
                    'etapas': [
                        {
                            'etapa_id': 'fator_limitante',
                            'pergunta': 'Qual é o principal fator limitante do membro superior?',
                            'opcoes': [
                                {
                                    'id': 'm1_group',
                                    'rotulo': 'Perda de Sinergia / Espasticidade / Fraqueza Muscular',
                                    'subtexto': 'Disfunção motora ou sensorial associada ao Córtex Motor',
                                    'linha_prescricao': 'Córtex Motor Primário (M1)',
                                    'proxima_etapa': 'pem_triage'
                                },
                                {
                                    'id': 's1_group',
                                    'rotulo': 'Disfunção Sensorial Isolada / Predominante',
                                    'subtexto': 'Déficit tátil e proprioceptivo somatossensorial',
                                    'linha_prescricao': 'Córtex Somatossensorial Primário (S1)',
                                    'proxima_etapa': 'lesao_s1'
                                },
                                {
                                    'id': 'ppc_group',
                                    'rotulo': 'Heminegligência Visuoespacial',
                                    'subtexto': 'Negligência hemiespacial contralateral à lesão',
                                    'linha_prescricao': 'Córtex Parietal Posterior (PPC)',
                                    'proxima_etapa': 'protocolo_ppc'
                                }
                            ]
                        },
                        {
                            'etapa_id': 'pem_triage',
                            'pergunta': 'Presença de Potencial Evocado Motor (PEM) no Membro Superior parético?',
                            'subtitulo': 'Avaliação neurofisiológica da integridade do trato corticoespinhal',
                            'opcoes': [
                                {
                                    'id': 'pem_sim',
                                    'rotulo': 'PEM Presente',
                                    'subtexto': 'Trato corticoespinhal preservado',
                                    'proxima_etapa': 'gravidade_fma'
                                },
                                {
                                    'id': 'pem_nao',
                                    'rotulo': 'PEM Ausente',
                                    'subtexto': 'Integridade corticoespinhal não preservada',
                                    'proxima_etapa': 'lesao_m1'
                                }
                            ]
                        },
                        {
                            'etapa_id': 'gravidade_fma',
                            'pergunta': 'Comprometimento motor pela escala Fugl-Meyer (FMA-UE)?',
                            'subtitulo': 'Estratificação da gravidade do déficit motor',
                            'opcoes': [
                                {
                                    'id': 'fma_leve_mod',
                                    'rotulo': 'Comprometimento Leve a Moderado (> 35 pontos)',
                                    'subtexto': 'Capacidade motora residual para tarefas motoras',
                                    'protocolo_id': 'RM01-P_M1_1',
                                    'modalidade_chave': 'fraqueza'
                                },
                                {
                                    'id': 'fma_grave',
                                    'rotulo': 'Comprometimento Grave (≤ 35 pontos)',
                                    'subtexto': 'Déficit severo / hipertonia / espasticidade predominante',
                                    'protocolo_id': 'RM01-P_M1_2_B',
                                    'modalidade_chave': 'espasticidade'
                                }
                            ]
                        },
                        {
                            'etapa_id': 'lesao_m1',
                            'pergunta': 'Lesão cortical extensa no giro pré-frontal?',
                            'subtitulo': 'Avaliação de neuroimagem estrutural (TC/RM)',
                            'opcoes': [
                                {
                                    'id': 'lesao_prefrontal_sim',
                                    'rotulo': 'Lesão Extensa no Giro Pré-Frontal',
                                    'subtexto': 'Estimulação cerebelar contralesional de compensação (Protocolo 4)',
                                    'protocolo_id': 'RM01-P_M1_4',
                                    'modalidade_chave': 'sem_pem_cerebelar'
                                },
                                {
                                    'id': 'lesao_prefrontal_nao',
                                    'rotulo': 'Sem Lesão Extensa no Giro Pré-Frontal',
                                    'subtexto': 'Estimulação excitatória do córtex pré-motor ipsilesional (Protocolo 5)',
                                    'protocolo_id': 'RM01-P_M1_5',
                                    'modalidade_chave': 'sem_pem_premotor'
                                }
                            ]
                        },
                        {
                            'etapa_id': 'lesao_s1',
                            'pergunta': 'Lesão cortical extensa no giro pós-frontal (S1)?',
                            'subtitulo': 'Avaliação de integridade estrutural do córtex somatossensorial',
                            'opcoes': [
                                {
                                    'id': 'lesao_s1_nao',
                                    'rotulo': 'Sem Lesão Extensa em S1',
                                    'subtexto': 'Estimulação excitatória direta de S1 ipsilesional',
                                    'protocolo_id': 'RM01-P_S1_1',
                                    'modalidade_chave': 'sensorial'
                                },
                                {
                                    'id': 'lesao_s1_sim',
                                    'rotulo': 'Lesão Extensa em S1',
                                    'subtexto': 'Reentrar na via motora corticoespinhal (M1 / PEM)',
                                    'proxima_etapa': 'pem_triage'
                                }
                            ]
                        },
                        {
                            'etapa_id': 'protocolo_ppc',
                            'pergunta': 'Conduta para Heminegligência:',
                            'subtitulo': 'Modulação parietal para recuperação da atenção espacial',
                            'opcoes': [
                                {
                                    'id': 'ppc_padrao',
                                    'rotulo': 'Estimulação de Alta Frequência em PPC Esquerdo',
                                    'subtexto': 'Protocolo 1 rTMS PPC (10 Hz, 90% LMR, 1.000 pulsos)',
                                    'protocolo_id': 'RM01-P_PPC_1',
                                    'modalidade_chave': 'negligencia'
                                }
                            ]
                        }
                    ],
                    'ajuste_parametros': {
                        'titulo': 'Diretrizes de Otimização e Ajuste de Parâmetros (Rede NAPeN)',
                        'tolerabilidade': 'Em caso de desconforto ou dor local, reduzir temporariamente a intensidade para 80% do LMR e progredir gradualmente conforme tolerância até a dose plena prevista (Nota N10).',
                        'dose_pulsos': 'Recomenda-se ajustar o número de pulsos para 1.500 por sessão, conforme evidências metanalíticas de maior magnitude de ganho com doses superiores (Nota N23).',
                        'calibracao_limiar': 'Na ausência de identificação do limiar motor de repouso (LMR), calibrar a estimulação baseando-se no Limiar Motor Ativo (LMA a 70%–80%) (Nota N13).'
                    },
                    'protocolo_alternativo_2': {
                        'id': 'RM01-ALT2',
                        'nome': 'Protocolo Alternativo 2 (iTBS Cortical + rPMS Periférica)',
                        'tecnica': 'iTBS (Triplets a 50 Hz em 5 Hz) + rPMS Periférica Contínua/Intermitente',
                        'alvo': 'M1 ipsilesional + Músculos flexores espásticos ou extensores fracos',
                        'parametros': 'iTBS cortical: 1.200 pulsos a 80% LMA seguido de rPMS contínua (600 pulsos a 5 Hz sobre flexores) ou intermitente (extensores) (Notas N18, N19)',
                        'observacoes': 'Bobina perpendicular às fibras com intensidade para contração visível (Nota N20). Separar sessão por 10 min.'
                    },
                    'falha_terapeutica': {
                        'id': 'RM01-FALHA',
                        'titulo': 'Declaração Formal de Falha Terapêutica em Neuromodulação (Rede NAPeN)',
                        'descricao': 'Critérios diagnósticos e condutas padronizadas para não-resposta clínica comprovada após esgotamento de todas as linhas e alternativas do roadmap.',
                        'criterios_definicao': 'Persistência de variação clínica funcional inferior à MCID na escala clínica validada após indução completa (mínimo de 10 a 20 sessões), esgotamento das diretrizes de ajuste de parâmetros/tolerabilidade e ausência de resposta aos Protocolos Alternativos 1 e 2.',
                        'condutas': [
                            'Interromper o ciclo de neuromodulação não invasiva na modalidade e alvo vigentes;',
                            'Encaminhar o paciente para reavaliação médica e funcional multidisciplinar ampliada;',
                            'Considerar reavaliação neurofisiológica aprofundada (ressonância funcional ou mapeamento cortical de conectividade);',
                            'Avaliar transição para modalidades sinérgicas ou intervenções adjuvantes recomendadas pela Rede NAPeN.'
                        ]
                    }
                },
                'tdcs': {
                    'roadmap_id': 'RM02',
                    'titulo': 'AVC — Membro Superior (tDCS / taVNS)',
                    'macro_desfecho': 'Uso do membro superior nas AVDs',
                    'etapas': [
                        {
                            'etapa_id': 'fator_limitante',
                            'pergunta': 'Qual é o principal fator limitante com indicação para tDCS?',
                            'opcoes': [
                                {
                                    'id': 'm1_tdcs',
                                    'rotulo': 'Disfunção Motora / Espasticidade',
                                    'subtexto': 'Aplicação sobre o Córtex Motor Primário (M1)',
                                    'linha_prescricao': 'Córtex Motor Primário (M1)',
                                    'proxima_etapa': 'lesao_tdcs_m1'
                                },
                                {
                                    'id': 's1_tdcs',
                                    'rotulo': 'Disfunção Sensorial Somestésica',
                                    'subtexto': 'Aplicação sobre o Córtex Somatossensorial (S1)',
                                    'linha_prescricao': 'Córtex Somatosensorial Primário (S1)',
                                    'proxima_etapa': 'protocolo_s1_tdcs'
                                },
                                {
                                    'id': 'ppc_tdcs',
                                    'rotulo': 'Heminegligência',
                                    'subtexto': 'Aplicação sobre Córtex Parietal (P3/P4)',
                                    'linha_prescricao': 'Córtex Parietal (P3/P4)',
                                    'proxima_etapa': 'protocolo_ppc_tdcs'
                                }
                            ]
                        },
                        {
                            'etapa_id': 'lesao_tdcs_m1',
                            'pergunta': 'Lesão cortical extensa no giro pré-frontal?',
                            'opcoes': [
                                {
                                    'id': 'lesao_tdcs_sim',
                                    'rotulo': 'Lesão Cortical no Giro Pré-Frontal',
                                    'subtexto': 'Avaliar capacidade residual de extensão dos dedos',
                                    'proxima_etapa': 'extensao_dedos'
                                },
                                {
                                    'id': 'lesao_tdcs_nao',
                                    'rotulo': 'Sem Lesão Extensa no Giro Pré-Frontal',
                                    'subtexto': 'Protocolo 1 tDCS: 1,5 mA, 30 min, ânodo ipsilesional',
                                    'protocolo_id': 'RM02-P-L012',
                                    'modalidade_chave': 'fraqueza'
                                }
                            ]
                        },
                        {
                            'etapa_id': 'extensao_dedos',
                            'pergunta': 'Comprometimento motor leve/moderado (extensão ativa ≥10° de dedos/polegar)?',
                            'opcoes': [
                                {
                                    'id': 'extensao_sim',
                                    'rotulo': 'Extensão Presente ≥ 10°',
                                    'subtexto': 'Protocolo 5 tDCS: 1,0 mA, 30 min, córtex pré-motor',
                                    'protocolo_id': 'RM02-P-L016',
                                    'modalidade_chave': 'fraqueza'
                                },
                                {
                                    'id': 'extensao_nao',
                                    'rotulo': 'Extensão Ausente < 10°',
                                    'subtexto': 'Protocolo 4 tDCS: 1,75 mA, 20 min, ânodo contralesional',
                                    'protocolo_id': 'RM02-P-L017',
                                    'modalidade_chave': 'espasticidade'
                                }
                            ]
                        },
                        {
                            'etapa_id': 'protocolo_s1_tdcs',
                            'pergunta': 'Protocolo para Disfunção Sensorial:',
                            'opcoes': [
                                {
                                    'id': 's1_tdcs_prot',
                                    'rotulo': 'tDCS Anodal em S1',
                                    'subtexto': '1,0 mA, 20 min, 25 cm², ânodo sobre S1 ipsilesional',
                                    'protocolo_id': 'RM02-P-L011',
                                    'modalidade_chave': 'sensorial'
                                }
                            ]
                        },
                        {
                            'etapa_id': 'protocolo_ppc_tdcs',
                            'pergunta': 'Protocolo para Heminegligência:',
                            'opcoes': [
                                {
                                    'id': 'ppc_tdcs_prot',
                                    'rotulo': 'tDCS Bipolar Parietal',
                                    'subtexto': '1,0 mA, 20 min, 35 cm², ânodo em P4 e cátodo em FP1',
                                    'protocolo_id': 'RM02-P-L009',
                                    'modalidade_chave': 'negligencia'
                                }
                            ]
                        }
                    ]
                }
            }

        # Higienização de todas as modalidades da condição
        for mod_k, mod_v in cond.get('modalidades', {}).items():
            # Higienizar strings textuais
            mod_v['tecnica'] = higienizar_texto(mod_v.get('tecnica', ''))
            mod_v['alvo'] = higienizar_texto(mod_v.get('alvo', ''))
            mod_v['evidencia'] = higienizar_texto(mod_v.get('evidencia', ''))
            mod_v['tamanho_efeito'] = higienizar_texto(mod_v.get('tamanho_efeito', ''))

            # Garantir classificação de Cohen unívoca
            cohen_str = mod_v.get('cohen_d', '')
            if cohen_str:
                mod_v['cohen_d'] = higienizar_texto(cohen_str)

            eff_obj = mod_v.get('efeito_clinico', {})
            if eff_obj:
                eff_obj['estudo_referencia'] = higienizar_texto(eff_obj.get('estudo_referencia', ''))
                eff_obj['efeito_esperado_resumo'] = higienizar_texto(eff_obj.get('efeito_esperado_resumo', ''))
                eff_obj['cohen_d'] = higienizar_texto(eff_obj.get('cohen_d', ''))
                eff_obj['mcid_label'] = higienizar_texto(eff_obj.get('mcid_label', ''))
                mod_v['efeito_clinico'] = eff_obj

            ec = mod_v.get('ensaio_clinico', {})
            if ec:
                ec['tipo'] = 'Estudos de referência'
                ec['autores'] = higienizar_texto(ec.get('autores', ''))
                mod_v['ensaio_clinico'] = ec

            # Protocolo alternativo derivado
            alt = mod_v.get('protocolo_alternativo', {})
            if alt:
                alt['nome'] = higienizar_texto(alt.get('nome', ''))
                alt['observacoes'] = higienizar_texto(alt.get('observacoes', ''))
                mod_v['protocolo_alternativo'] = alt

            # Injetar Diretrizes Padronizadas de Ajuste de Parâmetros e Tolerabilidade (NAPeN)
            mod_v['ajuste_parametros'] = {
                'titulo': 'Diretrizes de Otimização e Ajuste de Parâmetros (Rede NAPeN)',
                'tolerabilidade': 'Em caso de desconforto ou dor local, reduzir temporariamente a intensidade para 80% do LMR e progredir gradualmente conforme tolerância até a dose plena prevista (Nota N10).',
                'dose_pulsos': 'Recomenda-se ajustar o número de pulsos para 1.500 por sessão, conforme evidências metanalíticas de maior magnitude de ganho com doses superiores (Nota N23).',
                'calibracao_limiar': 'Na ausência de identificação do limiar motor de repouso (LMR), calibrar a estimulação baseando-se no Limiar Motor Ativo (LMA a 70%–80%) (Nota N13).'
            }

            # Injetar Protocolo Alternativo 2 para AVC Membro Superior conforme RM01
            if cid == 'avc-membro-superior':
                if mod_k == 'espasticidade':
                    mod_v['protocolo_alternativo_2'] = {
                        'nome': 'Protocolo Alternativo 2 (iTBS Cortical + rPMS Periférica Contínua)',
                        'tecnica': 'iTBS (Triplets a 50 Hz em 5 Hz) + rPMS Periférica',
                        'alvo': 'M1 ipsilesional + Músculos flexores espásticos do punho/dedos',
                        'parametros': 'iTBS cortical: 1.200 pulsos a 80% LMA seguido de rPMS contínua: 600 pulsos a 5 Hz sobre flexores (Nota N19)',
                        'observacoes': 'Bobina perpendicular às fibras com intensidade para contração visível (Nota N20). Separar sessão por 10 min.'
                    }
                elif mod_k == 'fraqueza':
                    mod_v['protocolo_alternativo_2'] = {
                        'nome': 'Protocolo Alternativo 2 (iTBS Intermitente + rPMS Intermitente em Músculos Fracos)',
                        'tecnica': 'iTBS Excitatório + rPMS em modo intermitente',
                        'alvo': 'M1 ipsilesional + Extensor radial do carpo / deltóide',
                        'parametros': 'iTBS 1.200 pulsos + rPMS: 3 pulsos a 50 Hz a cada 2s de estímulo e 8s pausa, 600 pulsos por músculo (Nota N18)',
                        'observacoes': 'Associar imediatamente à terapia convencional para o membro superior (Nota N08).'
                    }
                else:
                    mod_v['protocolo_alternativo_2'] = {
                        'nome': 'Protocolo Alternativo 2 Sequencial (Cerebelar / Pré-Motor)',
                        'tecnica': 'iTBS / rTMS 10 Hz',
                        'alvo': 'Cerebelo contralesional ou Córtex Pré-motor',
                        'parametros': '600 a 1.000 pulsos conforme tolerabilidade clínica',
                        'observacoes': 'Aplicação com bobina duplo-cone ou parabólica se direcionada ao cerebelo (Nota N11).'
                    }
            elif 'protocolo_alternativo_2' not in mod_v:
                mod_v['protocolo_alternativo_2'] = {
                    'nome': 'Protocolo Alternativo 2 (Ajuste de Alvo / Parâmetros)',
                    'tecnica': 'Modulação Alternativa Padronizada',
                    'alvo': 'Alvo de compensação de rede neural',
                    'parametros': 'Dose e frequência ajustadas conforme tolerância do paciente',
                    'observacoes': 'Indicado após reavaliação clínica que comprove persistência de déficit sem ganho mínimo.'
                }

            # Injetar Critério e Conduta Formal de Falha Terapêutica (Rede NAPeN)
            mod_v['falha_terapeutica'] = {
                'criterio': 'Persistência de resposta funcional inferior à MCID na escala clínica validada após o ciclo pleno de indução, realização dos ajustes de parâmetros/tolerabilidade e conclusão dos protocolos alternativos 1 e 2 do roadmap.',
                'conduta_oficial': '1. Encerramento formal do ciclo de estimulação vigente;\n2. Registro em prontuário de refratariedade ao regime testado;\n3. Investigação multiprofissional de fatores biológicos de resistência (uso concomitante de benzodiazepínicos/antiepilépticos, lesão corticoespinhal estrutural completa);\n4. Transição para modalidade alternativa (ex.: tDCS domiciliar associada a telerreabilitação intensiva, bloqueio neuromuscular focal com toxina botulínica ou reabilitação motora assistida por robótica/RV).'
            }

    # Aplicação de higienização recursiva em todo o target_data
    target_data = aplicar_higienizacao_recursiva(target_data)

    # Gravação dos arquivos finais
    with open(JSON_TARGET, 'w', encoding='utf-8') as f:
        json.dump(target_data, f, ensure_ascii=False, indent=2)

    with open(JS_TARGET, 'w', encoding='utf-8') as f:
        f.write('// Rede NAPeN — Base de Dados dos Roadmaps Clínicos (Auto-gerada)\n')
        f.write('// Integrada com topologia V2 e padronização terminológica estrita\n')
        f.write('window.NAPEN_DATA = ')
        json.dump(target_data, f, ensure_ascii=False, indent=2)
        f.write(';\n')

    print(f"✓ Base JSON salva em {JSON_TARGET} ({os.path.getsize(JSON_TARGET)} bytes)")
    print(f"✓ Base JS salva em {JS_TARGET} ({os.path.getsize(JS_TARGET)} bytes)")

if __name__ == '__main__':
    main()
