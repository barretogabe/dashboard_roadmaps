#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Atualização Integral do Guia Clínico de Escalas (RM01–RM18)
Corrige UPDRS-III para estado ON, registra nota brasileira da HAM-A (RM11),
adiciona todas as escalas oficiais faltantes dos 18 PDFs e sinaliza reserva legal
(*Uso privativo de psicólogos) em D2, WAIS-IV Dígitos e Teste de Trilhas.
"""

import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
JSON_PATH = os.path.join(BASE_DIR, 'data', 'escalas_guia_clinico.json')
JS_PATH = os.path.join(BASE_DIR, 'js', 'scale-guide-data.js')


def _scale(
    scale_id, sigla, nome, nome_en, dominio, tempo, publico, materiais,
    passos, criterios, interpretacao, mcid, ref_abnt, validacao_brasil,
    doi='', privativo_psicologo=False
):
    obj = {
        'id': scale_id,
        'sigla': sigla,
        'nome': nome,
        'nome_en': nome_en,
        'dominio': dominio,
        'tempo_aplicacao': tempo,
        'publico_alvo': publico,
        'materiais': materiais,
        'procedimento_passo_a_passo': [
            {'passo': idx + 1, 'titulo': t, 'descricao': d}
            for idx, (t, d) in enumerate(passos)
        ],
        'criterios_pontuacao': [{'grau': g, 'descricao': d} for g, d in criterios],
        'interpretacao_clinica': interpretacao,
        'mcid': mcid,
        'referencia_abnt': ref_abnt,
        'doi': doi,
        'link_artigo': f'https://doi.org/{doi}' if doi else '',
        'validacao_brasil': validacao_brasil,
    }
    if privativo_psicologo:
        obj['uso_privativo_psicologo'] = True
        obj['nota_uso_privativo'] = 'Uso privativo de psicólogos no Brasil (CFP/SATEPSI).'
    return obj


NEW_SCALES = {
    'mal_brazil': _scale(
        'mal_brazil', 'MAL-Brazil', 'Motor Activity Log — Versão Brasileira (MAL-Brazil)', 'Motor Activity Log (MAL)',
        'Uso Real do Membro Superior Parético nas AVDs', '10 a 15 minutos',
        'Pacientes pós-AVC em reabilitação do membro superior.',
        'Formulário estruturado com 30 atividades cotidianas e cartões de escalas de Quantidade (QOM) e Qualidade (AOU) de uso (0 a 5).',
        [
            ('Entrevista Estruturada por Tarefa', 'Investigar quanto (AOU) e quão bem (QOM) o paciente utilizou espontaneamente o membro parético em 30 tarefas cotidianas.'),
            ('Pontuação Dupla (0 a 5)', 'Atribuir escores de 0 (não usa) a 5 (como antes do AVC), evitando superestimação pelo examinador.'),
            ('Cálculo das Médias', 'Calcular média das tarefas aplicáveis para Quantidade e Qualidade de Movimento.'),
        ],
        [('0 a 5 pontos (média)', 'Pontuação média de uso espontâneo e qualidade funcional nas AVDs.')],
        'Instrumento central de desfecho nas atividades de vida diária para reabilitação do membro superior pós-AVC.',
        'Ganho médio ≥ 0,5 a 1,0 ponto nas subescalas AOU/QOM.',
        'Saliba, V. A., et al. (2011). Adaptação transcultural e análise das propriedades psicométricas da versão brasileira do instrumento Motor Activity Log. Revista Panamericana de Salud Pública, 30(3), 262-271.',
        'Validada para português brasileiro por Saliba et al. (2011).',
        doi='10.1590/S1020-49892011000900011',
    ),
    'catherine_bergego': _scale(
        'catherine_bergego', 'CBS', 'Escala Catherine Bergego', 'Catherine Bergego Scale (CBS)',
        'Heminegligência Espacial Unilateral em AVDs', '10 minutos (observação)',
        'Pacientes pós-AVC com suspeita de heminegligência espacial unilateral.',
        'Checklist observacional de 10 situações funcionais cotidianas (higiene, vestuário, alimentação, deslocamento).',
        [
            ('Observação Ecológica em 10 Domínios', 'Observar negligência lateral em autocuidado, leitura espacial, atenção ao hemicorpo e colisões em deslocamento.'),
            ('Graduação de Gravidade (0 a 3 por item)', 'Pontuar 0 (sem negligência), 1 (leve), 2 (moderada) ou 3 (grave).'),
            ('Índice de Anosognosia', 'Comparar escore do avaliador com autoavaliação do paciente para mensurar consciência do déficit.'),
        ],
        [('0 pontos', 'Sem heminegligência observável.'), ('1–10 / 11–20 / 21–30', 'Negligência leve, moderada ou grave.')],
        'Avalia impacto ecológico da heminegligência após estimulação parietal posterior (P3/P4) ou frontal (F5).',
        'Redução ≥ 3 pontos no escore total observacional.',
        'Azouvi, P., et al. (2003). Behavioral assessment of unilateral neglect: study of the psychometric properties of the Catherine Bergego Scale. Arch Phys Med Rehabil, 84(1), 51-57.',
        'Amplamente adotada na clínica brasileira de neuroreabilitação em conjunto com testes de cancelamento.',
        doi='10.1053/apmr.2003.50062',
    ),
    'fma_le': _scale(
        'fma_le', 'FMA-LE', 'Escala de Fugl-Meyer — Extremidade Inferior', 'Fugl-Meyer Assessment Lower Extremity (FMA-LE)',
        'Recuperação Motora e Sensorial do Membro Inferior', '15 a 20 minutos',
        'Pacientes pós-AVC avaliados para mobilidade e função motora de membros inferiores.',
        'Martelo de reflexos e maca de avaliação neurológica.',
        [
            ('Avaliação Reflexa e Sinérgica', 'Testar reflexos aquileu/patelar e sinergias flexora e extensora de quadril, joelho e tornozelo.'),
            ('Coordenação e Velocidade', 'Executar teste calcanhar-joelho bilateralmente comparando velocidade e dismetria.'),
            ('Subescala Sensorial', 'Avaliar sensibilidade tátil e proprioceptiva em quadril, joelho, tornozelo e hálux.'),
        ],
        [('0 a 34 pontos (Motor MMII)', 'Pontuação motora máxima da extremidade inferior.')],
        'Quantifica controle motor seletivo e ganhos somatossensoriais de MMII após M1, cerebelo ou S1.',
        'Ganho mínimo de 4 a 6 pontos no escore motor da extremidade inferior.',
        'Fugl-Meyer, A. R., et al. (1975). The post-stroke hemiplegic patient. Scand J Rehabil Med, 7(1), 13-31.',
        'Versão brasileira validada por Maki et al. (2006).',
    ),
    'npsi': _scale(
        'npsi', 'NPSI', 'Inventário de Sintomas de Dor Neuropática', 'Neuropathic Pain Symptom Inventory (NPSI)',
        'Dimensões Qualitativas da Dor Neuropática e Alodinia', '5 a 8 minutos',
        'Pacientes com dor neuropática crônica em acompanhamento clínico.',
        'Questionário de 12 itens (10 descritores 0–10 + 2 itens temporais).',
        [
            ('Avaliação dos Descritores', 'Pontuar de 0 a 10 dor em queimação, aperto/pressão, choque elétrico, pontada/agulhada e evocada (escovação/pressão/frio).'),
            ('Soma das 5 Dimensões', 'Agrupar queimação espontânea, dor profunda, paroxística, evocada e parestesia/disestesia (0–100).'),
        ],
        [('0 a 100 pontos', 'Maior pontuação indica maior gravidade neuropática; subescores captam resposta em alodinia mesmo sem queda da EVA.')],
        'Essencial na dor neuropática para detectar melhora em alodinia, hiperalgesia ou hiperpatia quando a intensidade bruta da dor pouco oscila.',
        'Redução ≥ 20% a 32% no escore total após sessões seriadas.',
        'Bouhassira, D., et al. (2004). Development and validation of the Neuropathic Pain Symptom Inventory. Pain, 108(3), 248-257.',
        'Validado em português brasileiro por de Andrade et al. (2011).',
        doi='10.1016/j.pain.2003.12.024',
    ),
    'bpi': _scale(
        'bpi', 'BPI', 'Inventário Breve de Dor', 'Brief Pain Inventory (BPI)',
        'Instrumento Multidimensional de Intensidade e Interferência da Dor', '5 a 10 minutos',
        'Pacientes com dor crônica neuropática ou oncológica.',
        'Formulário com diagrama corporal, escalas 0–10 de intensidade e 7 itens de interferência (sono, humor, trabalho, relações).',
        [
            ('Mapa Corporal e Intensidade', 'Registrar localização da dor e piores/menores/médias intensidades nas últimas 24h.'),
            ('Interferência Funcional e Emocional', 'Avaliar de 0 a 10 o impacto em atividade geral, humor, locomoção, sono e prazer de viver.'),
        ],
        [('0 a 10 pontos (média)', 'Subescores de Severidade e de Interferência na qualidade de vida, sono e humor.')],
        'Recomendado na dor neuropática como instrumento multidimensional para captar ganhos em sono, humor e sofrimento.',
        'Redução ≥ 1,0 a 1,5 ponto na média de interferência.',
        'Cleeland, C. S., & Ryan, K. M. (1994). Pain assessment: global use of the Brief Pain Inventory. Ann Acad Med Singapore, 23(2), 129-138.',
        'Validado em português brasileiro por Ferreira et al. (2011).',
    ),
    'ssa': _scale(
        'ssa', 'SSA', 'Standardized Swallowing Assessment', 'Standardized Swallowing Assessment (SSA)',
        'Triagem Clínica Padronizada da Deglutição', '10 minutos',
        'Pacientes pós-AVC com disfagia neurogênica.',
        'Copo graduado de água, colher de chá e estetoscópio clínico.',
        [
            ('Pré-Requisitos Clínicos', 'Checar nível de alerta, controle postural de tronco/cabeça e reflexo de tosse voluntária.'),
            ('Teste de Água por Etapas', 'Ofertar 3 colheres de chá de água e, se seguro, meio copo d’água observando tosse, engasgo ou voz molhada.'),
        ],
        [('18 a 46 pontos (variações clínicas)', 'Quanto menor a pontuação, mais segura e próxima do normal encontra-se a deglutição.')],
        'Usada junto à avaliação fonoaudiológica por consistência alimentar antes de classificar resposta aos 5 dias.',
        'Redução significativa do escore combinada à progressão por consistências.',
        'Perry, L. (2001). Screening swallowing function of patients with acute stroke. Part one: Identification, implementation and initial evaluation of a screening tool for use by nurses. J Clin Nurs, 10(4), 463-473.',
        'Aplicar exclusivamente com acompanhamento fonoaudiológico especializado em disfagia.',
        doi='10.1046/j.1365-2702.2001.00501.x',
    ),
    'doss': _scale(
        'doss', 'DOSS', 'Dysphagia Outcome and Severity Scale', 'Dysphagia Outcome and Severity Scale (DOSS)',
        'Gravidade Clínica e Independência Funcional da Deglutição', '5 a 10 minutos (pós-avaliação)',
        'Pacientes com disfagia orofaríngea pós-AVC.',
        'Registro clínico e/ou videodeglutograma com testagem de múltiplas consistências alimentares.',
        [
            ('Testar Todas as Consistências', 'Avaliar líquidos ralos, néctar, pastosos e sólidos observando retenção, penetração e aspiração.'),
            ('Classificação nos 7 Níveis', 'Graduar de 7 (deglutição normal) a 1 (disfagia grave — nada por via oral).'),
        ],
        [('Nível 6–7', 'Deglutição normal ou dentro dos limites funcionais.'), ('Nível 3–5', 'Disfagia leve a moderada com restrição de consistências.'), ('Nível 1–2', 'Disfagia moderada-grave a grave (risco aspirativo).')],
        'Fundamental antes de declarar falha nos primeiros 5 dias: avaliar resposta em CADA consistência alimentar.',
        'Progressão ≥ 1 nível na DOSS.',
        "O'Neil, K. H., et al. (1999). The Dysphagia Outcome and Severity Scale. Dysphagia, 14(3), 139-145.",
        'Utilizada rotineiramente em conjunto com FOIS e videodeglutograma.',
        doi='10.1007/PL00009595',
    ),
    'masa': _scale(
        'masa', 'MASA', 'Mann Assessment of Swallowing Ability', 'Mann Assessment of Swallowing Ability (MASA)',
        'Avaliação Clínica Multidimensional da Deglutição', '15 minutos',
        'Pacientes com disfagia pós-AVC.',
        'Protocolo clínico estruturado com 24 itens motores orofaríngeos e função craniana.',
        [
            ('Exame Motor e Craniano Oral', 'Avaliar alerta, respiração, vedamento labial, língua, elevação laríngea e reflexo faríngeo.'),
            ('Somatória de 200 Pontos', 'Pontuar os 24 domínios para quantificar risco de disfagia e aspiração.'),
        ],
        [('178–200', 'Sem disfagia significativa.'), ('< 178 / < 168', 'Disfagia leve a moderada/grave.')],
        'Instrumento clínico quantitativo sensível para acompanhamento pré e pós-intervenção fonoaudiológica.',
        'Aumento ≥ 10 pontos com progressão de consistência segura.',
        'Mann, G. (2002). MASA: The Mann Assessment of Swallowing Ability. Singular/Thomson Learning.',
        'Conduzir por fonoaudiólogo especializado em disfagia.',
        doi='10.1016/j.jstrokecerebrovasdis.2009.03.007',
    ),
    'mtl_brasil': _scale(
        'mtl_brasil', 'MTL-Brasil', 'Bateria Montreal-Toulouse de Avaliação da Linguagem', 'Montreal-Toulouse Language Assessment Battery (MTL-BR)',
        'Avaliação Abrangente de Expressão e Compreensão na Afasia (Recomendação Brasil)', '30 a 45 minutos (ou subtestes por microdesfecho)',
        'Pacientes brasileiros com afasia pós-AVC de expressão ou compreensão.',
        'Manual e cadernos de estímulos validados da Bateria MTL-Brasil.',
        [
            ('Seleção dos Subtestes por Microdesfecho', 'Aplicar subtestes correspondentes ao sintoma limitante (discurso espontâneo, nomeação/anomia, repetição ou compreensão oral).'),
            ('Comparação com Normas Brasileiras', 'Interpretar escores ajustados por faixa etária e escolaridade brasileira.'),
        ],
        [('Escore por subteste', 'Valores abaixo dos pontos de corte normativos de idade e escolaridade indicam déficit específico.')],
        'Adaptação Clínica (Brasil): substitui as baterias internacionais dos ensaios originais na prática clínica nacional.',
        'Melhora mensurável nos microdesfechos-alvo após 5 a 15 sessões combinadas à fonoterapia.',
        'Parente, M. A. M. P., Fonseca, R. P., Pagliarin, K. C., et al. (2016). Bateria Montreal-Toulouse de Avaliação da Linguagem (MTL-Brasil). Vetor Editora.',
        'Adaptada e normatizada para a população brasileira (Parente, Fonseca, Pagliarin et al.).',
        doi='10.3109/02687038.2014.919315',
    ),
    'token_test': _scale(
        'token_test', 'Token Test', 'Token Test (Compreensão Verbal)', 'Token Test',
        'Compreensão Auditiva e Sintática', '10 a 15 minutos',
        'Pacientes com afasia de compreensão pós-AVC.',
        '20 fichas geométricas em 2 formas, 2 tamanhos e 5 cores padronizadas.',
        [
            ('Comandos Crescentes', 'Solicitar manipulação das fichas em 5 ou 6 partes de complexidade linguística progressiva.'),
            ('Registro de Acertos', 'Pontuar acertos em comandos simples e relacionais.'),
        ],
        [('0 a 36 pontos (versão reduzida)', 'Escore mais elevado representa melhor compreensão verbal.')],
        'Complementa a MTL-Brasil na quantificação da compreensão sintática auditiva.',
        'Aumento ≥ 3 pontos na compreensão verbal.',
        'De Renzi, E., & Faglioni, P. (1978). Normative data and screening power of a shortened version of the Token Test. Cortex, 14(1), 41-49.',
        'Versão reduzida normatizada e utilizada na prática fonoaudiológica e neuropsicológica no Brasil.',
    ),
    'hdrs_21': _scale(
        'hdrs_21', 'HDRS-21', 'Escala de Depressão de Hamilton — 21 Itens', 'Hamilton Depression Rating Scale — 21 items (HDRS-21)',
        'Gravidade Clínica da Depressão Maior', '15 a 20 minutos',
        'Pacientes com depressão moderada a grave em avaliação para TMS.',
        'Roteiro clínico semiestruturado de 21 itens.',
        [
            ('Entrevista Semiestruturada', 'Avaliar humor deprimido, culpa, ideação suicida, insônia, retardo/agitação, ansiedade e sintomas somáticos/variação diurna.'),
            ('Limiares Clínicos', 'HDRS-21 ≥ 18 define depressão moderada a grave elegível ao tratamento.'),
        ],
        [('≥ 18 pontos', 'Critério clínico de entrada (depressão moderada a grave).'), ('≤ 7 pontos', 'Remissão clínica.')],
        'Em depressão resistente, espera-se redução média de 55% (DP 16,4%) na HDRS-21 com HF-rTMS 10 Hz em F3.',
        'Redução ≥ 50% do escore basal.',
        'Hamilton, M. (1960). A rating scale for depression. J Neurol Neurosurg Psychiatry, 23(1), 56-62.',
        'Versão brasileira adaptada por Moreno & Moreno (1998).',
        doi='10.1136/jnnp.23.1.56',
    ),
    'madrs': _scale(
        'madrs', 'MADRS', 'Escala de Depressão de Montgomery-Asberg', 'Montgomery-Asberg Depression Rating Scale (MADRS)',
        'Sensibilidade à Mudança Terapêutica na Depressão', '15 minutos',
        'Pacientes com depressão moderada a grave em regimes convencionais e acelerados.',
        'Guia de entrevista clínica com 10 itens pontuados de 0 a 6.',
        [
            ('Avaliação dos 10 Domínios', 'Investigar tristeza aparente/relatada, tensão interna, redução do sono/apetite, concentração, lassidão, incapacidade de sentir e pessimismo.'),
            ('Critério de Gravidade', 'MADRS ≥ 20 indica quadro moderado a grave para indicação terapêutica.'),
        ],
        [('≥ 20 pontos', 'Depressão moderada a grave.'), ('≤ 10 pontos', 'Remissão sintomática.')],
        'O regime acelerado SNT (Stanford) espera redução média de 52,5% na MADRS.',
        'Redução ≥ 50% do escore basal.',
        'Montgomery, S. A., & Asberg, M. (1979). A new depression scale designed to be sensitive to change. Br J Psychiatry, 134, 382-389.',
        'Quilty et al. (2013) · Crosswalk HRSD/MADRS (Chen et al., 2025).',
        doi='10.1002/mpr.1388',
    ),
    'bai': _scale(
        'bai', 'BAI', 'Inventário de Ansiedade de Beck', 'Beck Anxiety Inventory (BAI)',
        'Sintomas Somáticos e Subjetivos de Ansiedade (Validado no Brasil)', '5 a 10 minutos',
        'Pacientes com Transtorno de Ansiedade Generalizada acompanhados por TMS.',
        'Questionário autoaplicável de 21 itens (escala 0–3).',
        [
            ('Aplicação Conjunta à HAM-A', 'Aplicar em conjunto à HAM-A (que não é validada no Brasil).'),
            ('Somatória de 0 a 63', 'Graduar ansiedade mínima (0–10), leve (11–19), moderada (20–30) ou grave (31–63).'),
        ],
        [('20–30 / 31–63 pontos', 'Ansiedade moderada a grave.')],
        'Instrumento validado no Brasil recomendado para suprir ausência de validação nacional da HAM-A.',
        'Redução ≥ 25% a 50% do escore basal.',
        'Beck, A. T., et al. (1988). An inventory for measuring clinical anxiety: psychometric properties. J Consult Clin Psychol, 56(6), 893-897.',
        'Validada para a população brasileira (Cunha, 2001).',
    ),
    'gad_7': _scale(
        'gad_7', 'GAD-7', 'Generalized Anxiety Disorder 7', 'Generalized Anxiety Disorder 7-item Scale (GAD-7)',
        'Rastreio e Gravidade do Transtorno de Ansiedade Generalizada', '3 a 5 minutos',
        'Pacientes com TAG em acompanhamento por TMS.',
        'Questionário de 7 itens referentes às últimas 2 semanas (0–21).',
        [
            ('Pontuação dos 7 Itens', 'Avaliar preocupação excessiva, inquietação, dificuldade de relaxar e irritabilidade (0–3 cada).'),
            ('Uso Conjunto à HAM-A', 'Recomendada como métrica validada complementar à HAM-A no Brasil.'),
        ],
        [('≥ 10 / ≥ 15 pontos', 'Ansiedade moderada (10–14) ou grave (15–21).')],
        'Alta sensibilidade à mudança ao longo de 10–25 sessões de rTMS/cTBS em F4 ou P4.',
        'Redução ≥ 4 pontos ou queda para faixa < 10 pontos.',
        'Spitzer, R. L., et al. (2006). A brief measure for assessing generalized anxiety disorder: the GAD-7. Arch Intern Med, 166(10), 1092-1097.',
        'Validada para português brasileiro (Moreno et al., 2016).',
        doi='10.1001/archinte.166.10.1092',
    ),
    'dass_21': _scale(
        'dass_21', 'DASS-21', 'Escala de Depressão, Ansiedade e Estresse — 21 Itens', 'Depression, Anxiety and Stress Scale (DASS-21)',
        'Triagem Integrada de Ansiedade, Depressão e Estresse no Brasil', '5 a 10 minutos',
        'Pacientes com TAG e sintomas depressivos associados.',
        'Questionário autoaplicável de 21 itens (7 por subescala; multiplicar soma por 2).',
        [
            ('Cálculo das 3 Subescalas', 'Calcular separadamente Depressão, Ansiedade e Estresse multiplicando cada soma por 2.'),
            ('Uso Conjunto à HAM-A', 'Recomendada em conjunto com a HAM-A para monitorar ansiedade e depressão comórbida no Brasil.'),
        ],
        [('Ansiedade ≥ 10 / ≥ 15', 'Faixas moderada e grave na subescala de ansiedade.')],
        'Diferencia evolução da ansiedade versus depressão comórbida ao longo do tratamento.',
        'Mudança para faixa clínica inferior (redução ≥ 25%–50%).',
        'Vignola, R. C. B., & Tucci, A. M. (2014). Adaptation and validation of the Depression, Anxiety and Stress Scale (DASS) to Brazilian Portuguese. J Affect Disord, 155, 104-109.',
        'Validada no Brasil por Vignola & Tucci (2014).',
        doi='10.1016/j.jad.2013.10.031',
    ),
    'moca': _scale(
        'moca', 'MoCA', 'Montreal Cognitive Assessment', 'Montreal Cognitive Assessment (MoCA)',
        'Rastreio Cognitivo Global no CCL e Doença de Alzheimer', '10 a 15 minutos',
        'Pacientes com Declínio Cognitivo Leve (CCL) ou Doença de Alzheimer inicial.',
        'Formulário MoCA e cronômetro.',
        [
            ('Avaliação de 8 Domínios', 'Testar função visuoespacial/executiva, nomeação, atenção, linguagem, abstração, evocação tardia e orientação.'),
            ('Ajuste de Escolaridade', 'Adicionar 1 ponto se escolaridade ≤ 12 anos (conforme manual oficial).'),
        ],
        [('≥ 26 pontos', 'Faixa de normalidade (pontos de corte brasileiros ajustados por escolaridade).')],
        'Mais sensível que o MMSE para detecção e acompanhamento no Declínio Cognitivo Leve.',
        'Aumento ≥ 2 pontos ou estabilização do declínio cognitivo.',
        'Nasreddine, Z. S., et al. (2005). The Montreal Cognitive Assessment, MoCA: a brief screening tool for mild cognitive impairment. J Am Geriatr Soc, 53(4), 695-699.',
        'Validada no Brasil por Memória et al. (2013).',
        doi='10.1111/j.1532-5415.2005.53221.x',
    ),
    'cornell': _scale(
        'cornell', 'Cornell', 'Escala de Depressão de Cornell na Demência', 'Cornell Scale for Depression in Dementia (CSDD)',
        'Sintomas Depressivos em Pacientes com Demência / Alzheimer', '15 a 20 minutos (paciente + cuidador)',
        'Pacientes com Doença de Alzheimer com apatia, humor deprimido ou sintomas neuropsiquiátricos.',
        'Entrevista dupla (cuidador + paciente) com 19 itens graduados de 0 a 2.',
        [
            ('Entrevista Integrada com Cuidador', 'Coletar sinais relacionados ao humor, perturbações comportamentais, sinais físicos, funções cíclicas e distúrbios ideacionais.'),
            ('Reconciliação de Escores', 'Pontuar cada item (0–2) considerando observação direta e relato do cuidador.'),
        ],
        [('> 10 pontos', 'Provável depressão maior associada à demência.')],
        'A estimulação temporoparietal bilateral de tDCS obteve melhora média de 43,3% na Escala de Cornell após 10 sessões.',
        'Redução ≥ 30% a 43% no escore total.',
        'Alexopoulos, G. S., et al. (1988). Cornell Scale for Depression in Dementia. Biol Psychiatry, 23(3), 271-284.',
        'Validada no Brasil por Carthery-Goulart et al. (2007).',
        doi='10.1016/0006-3223(88)90038-8',
    ),
    'd2_psico': _scale(
        'd2_psico', 'D2', 'Teste de Atenção Concentrada (D2) — Uso Privativo de Psicólogos', 'd2 Test of Attention',
        'Atenção Concentrada e Velocidade de Processamento (Uso Privativo de Psicólogos)', '5 a 8 minutos',
        'Pacientes com CCL ou Alzheimer em protocolo pré-frontal — aplicação exclusiva por psicólogo.',
        'Caderno padronizado do Teste D2 e cronômetro (fornecimento restrito a psicólogos inscritos no CRP).',
        [
            ('Reserva Legal (Lei nº 4.119/1962)', 'Confirmar que a aplicação e correção estão sendo conduzidas por psicólogo regularmente habilitado (SATEPSI/CFP).'),
            ('Rastreio Cronometrado (20 s/linha)', 'Solicitar marcação rápida dos estímulos-alvo ao longo das 14 linhas.'),
        ],
        [('Percentis normativos', 'Resultados líquidos (RL) interpretados segundo tabelas normativas brasileiras por idade/escolaridade.')],
        'Instrumento neuropsicológico de uso privativo de psicólogos.',
        'Melhora de percentil de atenção concentrada após ciclo em CPFDL.',
        'Brickenkamp, R. Teste D2 — Atenção Concentrada. Adaptação brasileira (SATEPSI / Vetor).',
        'Instrumento psicológico privativo aprovado para uso exclusivo de psicólogos no Brasil.',
        privativo_psicologo=True,
    ),
    'wais_digitos': _scale(
        'wais_digitos', 'WAIS-IV', 'WAIS-IV / WASI — Subteste Dígitos (Span) — Uso Privativo de Psicólogos', 'WAIS-IV / WASI Digit Span',
        'Atenção e Memória de Trabalho (Uso Privativo de Psicólogos)', '5 a 10 minutos',
        'Pacientes com Alzheimer ou CCL — aplicação exclusiva por psicólogo.',
        'Manual e protocolo de registro WAIS-IV ou WASI (uso restrito a psicólogos).',
        [
            ('Reserva Profissional (Lei nº 4.119/1962)', 'Aplicação privativa de psicólogos; profissionais não psicólogos devem utilizar testes não privativos alternativos (ex.: N-back).'),
            ('Ordem Direta, Inversa e Sequencial', 'Aplicar séries numéricas crescentes até critério de interrupção do manual.'),
        ],
        [('Escore Ponderado', 'Interpretação segundo normas brasileiras padronizadas do manual WAIS-IV.')],
        'Medida padronizada de atenção e memória de trabalho (uso privativo de psicólogos).',
        'Aumento ≥ 1 ponto ponderado no subteste Dígitos.',
        'Nascimento, E. (2004/2015). Adaptação e padronização brasileira da Escala de Inteligência Wechsler para Adultos (WAIS). Casa do Psicólogo / Pearson.',
        'Instrumento privativo de psicólogos regulamentado no Brasil (CFP/SATEPSI).',
        privativo_psicologo=True,
    ),
    'teste_trilhas': _scale(
        'teste_trilhas', 'Trilhas', 'Teste de Trilhas (Partes A e B) — Uso Privativo de Psicólogos', 'Trail Making Test / Teste de Trilhas',
        'Função Executiva e Flexibilidade Cognitiva (Uso Privativo de Psicólogos)', '5 a 10 minutos',
        'Pacientes com Alzheimer ou CCL — atenção à restrição profissional conforme versão SATEPSI.',
        'Folhas padronizadas de estímulos numéricos e alfanuméricos e cronômetro.',
        [
            ('Restrição Profissional (Lei nº 4.119/1962)', 'O Teste de Trilhas possui aplicação privativa de psicólogos regularmente habilitados (CFP/SATEPSI).'),
            ('Sequência e Alternância', 'Mensurar tempo de execução e erros nas conexões sequenciais e alternadas.'),
        ],
        [('Escore padrão / Tempo (s)', 'Menor tempo e ausência de erros de alternância indicam melhor função executiva.')],
        'Em não-psicólogos, priorizar alternativas não privativas como Go/No-Go, BDEFS ou Torre de Hanói.',
        'Redução no tempo de execução da Parte B / flexibilidade executiva.',
        'Montiel, J. M., & Seabra, A. G. (2012). Teste de Trilhas (Partes A e B). Memnon / Avaliação Neuropsicológica.',
        'Instrumento de uso privativo de psicólogos no Brasil.',
        privativo_psicologo=True,
    ),
    'pdms_fm': _scale(
        'pdms_fm', 'PDMS-FM', 'Peabody Developmental Motor Scales — Fine Motor', 'PDMS-FM',
        'Desenvolvimento Motor Fino na Paralisia Cerebral', '20 a 30 minutos',
        'Crianças com Paralisia Cerebral hemiparética espástica.',
        'Kit padronizado PDMS-2 (blocos, pinos, papel, tesoura).',
        [
            ('Subtestes Preensão e Integração Visuomotora', 'Aplicar itens adequados à idade motora da criança até alcançar teto.'),
            ('Conversão em Escore Bruto e Quociente', 'Registrar pontos em cada subteste de motricidade fina.'),
        ],
        [('Percentil / Escore Padrão', 'Quantifica melhora em manipulação fina (séries clínicas de rTMS sequencial relatam +49,7%).')],
        'Escala de referência nas Habilidades Manipulativas da Paralisia Cerebral.',
        'Aumento relevante na pontuação bruta e quociente motor fino.',
        'Folio, M. R., & Fewell, R. R. (2000). Peabody Developmental Motor Scales (2nd ed.). Pro-Ed.',
        'Instrumento internacional utilizado em reabilitação pediátrica no Brasil.',
    ),
    'quest': _scale(
        'quest', 'QUEST', 'Quality of Upper Extremity Skills Test', 'Quality of Upper Extremity Skills Test (QUEST)',
        'Qualidade do Movimento dos Membros Superiores na Paralisia Cerebral', '25 a 35 minutos',
        'Crianças com Paralisia Cerebral espástica.',
        'Cubos, bola pequena, folha de papel, lápis e formulário QUEST.',
        [
            ('4 Domínios de Qualidade Motora', 'Avaliar movimentos dissociados, preensão, descarga de peso e extensão protetora.'),
            ('Escore Percentual Global', 'Converter pontuações padronizadas para índice percentual (0 a 100%).'),
        ],
        [('0 a 100%', 'Quanto maior o percentual, melhor a qualidade dissociada do membro superior.')],
        'rTMS Priming 6 Hz + 1 Hz contralesional (Gupta et al., 2023) apresentou melhora de 11,7% no escore QUEST após 10 sessões.',
        'Ganho ≥ 4,9 a 11,7 pontos percentuais.',
        'DeMatteo, C., et al. (1993). The reliability and validity of the Quality of Upper Extremity Skills Test. Phys Occup Ther Pediatr, 13(2), 1-18.',
        'Instrumento padrão-ouro na avaliação qualitativa bimanual em Paralisia Cerebral.',
        doi='10.1080/J006v13n02_01',
    ),
    'bbt': _scale(
        'bbt', 'BBT', 'Box and Block Test', 'Box and Block Test (BBT)',
        'Destreza Manual Grosseira Unilateral', '5 minutos',
        'Crianças com Paralisia Cerebral e adultos com ataxia cerebelar.',
        'Caixa bipartida padronizada com 150 blocos de madeira (2,5 cm) e cronômetro de 60 s.',
        [
            ('Treino de 15 Segundos', 'Permitir familiarização rápida com a tarefa de transpor blocos além da divisória central.'),
            ('Contagem em 60 Segundos', 'Contar quantos blocos atravessam a divisória em 1 minuto para cada mão.'),
        ],
        [('Blocos / minuto', 'Maior número de blocos transferidos indica maior destreza manual.')],
        'tDCS anódica C3/C4 na hemiparesia pediátrica relata aumento de 14,1% na pontuação do BBT após 5 sessões.',
        'Aumento ≥ 5,5 blocos/minuto (~14% em pediatria).',
        'Mathiowetz, V., et al. (1985). Adult norms for the Box and Block Test of manual dexterity. Am J Occup Ther, 39(6), 386-391.',
        'Instrumento amplamente validado e normatizado na terapia ocupacional brasileira.',
        doi='10.5014/ajot.39.6.386',
    ),
    'pbs': _scale(
        'pbs', 'PBS', 'Pediatric Balance Scale', 'Pediatric Balance Scale (PBS)',
        'Equilíbrio Funcional Pediátrico em Tarefas do Dia a Dia', '15 a 20 minutos',
        'Crianças com Paralisia Cerebral em avaliação de habilidades estabilizadoras.',
        'Banco sem encosto ajustável, escada de um degrau, fita métrica e cronômetro.',
        [
            ('14 Tarefas Funcionais Adaptadas', 'Testar transições sentado-em pé, apoio unipodal, giro 360°, degraus e alcance anterior (0–4 por item).'),
            ('Escore Total (0–56)', 'Registrar o total funcional e observar segurança postural.'),
        ],
        [('0 a 56 pontos', 'Maior pontuação indica melhor controle postural funcional.')],
        'Em Habilidades Estabilizadoras na Diparesia Espástica, tDCS C3/C4 gerou +11,9% na PBS após 10 sessões.',
        'Aumento ≥ 3,6 pontos (~10%–12% em pediatria).',
        'Franjoine, M. R., et al. (2003). Pediatric Balance Scale: a modified version of the Berg Balance Scale for the school-age child with mild to moderate motor impairment. Pediatr Phys Ther, 15(2), 114-128.',
        'Versão brasileira validada por Ries et al. (2012).',
        doi='10.1097/01.PEP.0000068117.48023.18',
    ),
    'rbs_r': _scale(
        'rbs_r', 'RBS-R', 'Repetitive Behavior Scale-Revised', 'Repetitive Behavior Scale-Revised (RBS-R)',
        'Comportamentos Repetitivos, Estereotipias e Compulsões no TEA', '10 a 15 minutos',
        'Crianças, adolescentes e adultos com TEA em protocolo comportamental/repetitivo.',
        'Escala de 43 itens preenchida por cuidadores em escala Likert 0–3.',
        [
            ('6 Subescalas Clínicas', 'Avaliar comportamento estereotipado, autolesivo, compulsivo, ritualístico, insistência na mesmice e interesses restritos.'),
            ('Monitoramento Pré e Pós', 'Aplicar no início e após 10–18 sessões de rTMS/HD-tDCS.'),
        ],
        [('0 a 129 pontos', 'Redução do escore total ou da subescala Compulsive indica melhora clínica.')],
        'LF-rTMS 1 Hz pré-frontal no TEA obteve ~35% de redução na RBS-R; HD-tDCS CP5/CP6 reduziu 21,9% em Compulsive Behavior.',
        'Redução ≥ 20% a 35% na RBS-R.',
        'Bodfish, J. W., et al. (2000). Varieties of repetitive behavior in autism: comparisons to mental retardation. J Autism Dev Disord, 30(3), 237-243.',
        'Traduzida e utilizada em serviços brasileiros de neurodesenvolvimento e TEA.',
        doi='10.1023/A:1005596502855',
    ),
    'atec': _scale(
        'atec', 'ATEC', 'Autism Treatment Evaluation Checklist', 'Autism Treatment Evaluation Checklist (ATEC)',
        'Regulação Multidimensional no Transtorno do Espectro Autista', '10 minutos',
        'Indivíduos com TEA acompanhados ao longo de ciclos de rTMS ou tDCS.',
        'Questionário de 77 itens dividido em 4 subescalas (Fala/Linguagem, Sociabilidade, Consciência Sensorial/Cognitiva e Saúde/Comportamento).',
        [
            ('Preenchimento por Cuidadores/Clínico', 'Pontuar os 4 domínios multidimensionalmente antes e após o ciclo.'),
            ('Subescala Sociabilidade / Saúde', 'Avaliar evolução tanto no escore global quanto nos subdomínios de Sociabilidade e Problemas Comportamentais.'),
        ],
        [('0 a 179 pontos', 'Pontuações menores indicam menor gravidade sintomática e melhor adaptação.')],
        'tDCS anódica F3 + deltoide D reduziu 12,5% no total ATEC e tDCS bilateral FC1/FC2 reduziu 23,5% em Sociabilidade.',
        'Redução ≥ 12% a 23% no total ou domínio-alvo da ATEC.',
        'Rimland, B., & Edelson, S. M. (1999). Autism Treatment Evaluation Checklist (ATEC). Autism Research Institute.',
        'Amplamente empregada em estudos clínicos e seguimento longitudinal no Brasil.',
        doi='10.3390/children5020025',
    ),
    'icars': _scale(
        'icars', 'ICARS', 'International Cooperative Ataxia Rating Scale', 'International Cooperative Ataxia Rating Scale (ICARS)',
        'Gravidade da Ataxia em Postura/Marcha, Funções Cinéticas, Fala e Oculomotricidade', '15 a 20 minutos',
        'Pacientes com ataxia cerebelar degenerativa ou adquirida.',
        'Roteiro clínico de 19 itens dividido em 4 subescalas (0–100 pontos).',
        [
            ('Avaliação dos 4 Subgrupos', 'Testar marcha/postura, decomposição cinética de MMSS/MMII, disartria atáxica e motricidade ocular.'),
            ('Subitens de Disartria', 'Utilizar subitens específicos de fala na presença de queixa associada de disartria atáxica.'),
        ],
        [('0 a 100 pontos', 'Maior escore indica maior gravidade atáxica.')],
        'csDCS cerebelo-espinal (Benussi et al., 2021) reduziu ICARS de 46,9 para 33,7 (-13,2 pts / ~28%).',
        'Redução ≥ 3,5 a 5 pontos na ICARS.',
        'Trouillas, P., et al. (1997). International Cooperative Ataxia Rating Scale for pharmacological assessment of the cerebellar syndrome. J Neurol Sci, 145(2), 205-211.',
        'Referência internacional utilizada em conjunto com a escala SARA.',
        doi='10.1016/s0022-510x(96)00231-6',
    ),
    'nfog_q': _scale(
        'nfog_q', 'NFOG-Q', 'New Freezing of Gait Questionnaire (Versão Atualizada)', 'New Freezing of Gait Questionnaire (NFOG-Q)',
        'Frequência e Impacto Funcional do Congelamento da Marcha', '5 a 8 minutos',
        'Pacientes com Doença de Parkinson apresentando episódios de freezing.',
        'Questionário de 9 itens (com apoio visual opcional) avaliando frequência, duração e limitação cotidiana.',
        [
            ('Triagem Inicial do Episódio', 'Confirmar ocorrência de freezing no último mês.'),
            ('Quantificação de Gravidade e Impacto', 'Pontuar frequência, duração dos piores episódios de hesitação inicial/em giros e interferência nas AVDs (0–28).'),
        ],
        [('0 a 28 pontos', 'Quanto menor o escore após 10 sessões, maior redução do congelamento.')],
        'Reduções esperadas na FOGQ/NFOG-Q: 9,24% (AMS, Mi et al., 2019), 15,59%–21,32% (M1 contralateral ao dimídio mais comprometido, Song et al., 2024) e 23,02% (M1+tsMS T10-T12, Wang et al., 2024).',
        'Redução ≥ 15% a 23% no escore total.',
        'Nieuwboer, A., et al. (2009). Reliability of the new freezing of gait questionnaire: agreement between patients with Parkinson\'s disease and their carers. Gait & Posture, 30(4), 459-463.',
        'Versão atualizada adotada na prática clínica especializada em Doença de Parkinson.',
        doi='10.1016/j.gaitpost.2009.07.108',
    ),
    'caps': _scale(
        'caps', 'CAPS', 'Clinician-Administered PTSD Scale', 'Clinician-Administered PTSD Scale (CAPS-5)',
        'Diagnóstico e Gravidade Clínica do TEPT por Entrevista Estruturada', '30 a 45 minutos',
        'Pacientes com diagnóstico ou suspeita clínica de TEPT (Critério inicial: CAPS ≥ 13).',
        'Entrevista clínica estruturada de 30 itens avaliando frequência e intensidade dos 20 sintomas DSM-5 + impacto funcional.',
        [
            ('Triagem de Entrada (CAPS ≥ 13)', 'Confirmar presença clínica dos critérios diagnósticos de TEPT segundo o DSM-5.'),
            ('Critério de Resposta Insatisfatória (< 25%)', 'Considerar resposta insatisfatória redução < 25% na CAPS ou PCL-5 ao término do protocolo.'),
        ],
        [('≥ 13 pontos', 'Limiar clínico de inclusão sintomática no TEPT; meta de redução ≥ 25%.')],
        'Resultados < 25% na CAPS ou PCL-5 indicam reavaliação diagnóstica, comorbidades (borderline, substâncias) e contexto social.',
        'Redução ≥ 25% do escore basal ao fim do protocolo.',
        'Weathers, F. W., et al. (2018). The Clinician-Administered PTSD Scale for DSM-5 (CAPS-5): Development and initial psychometric evaluation in military veterans. Psychol Assess, 30(3), 383-395.',
        'Padrão-ouro clínico em português brasileiro para acompanhamento de TEPT.',
        doi='10.1037/pas0000486',
    ),
}


def main():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Padronizar updrs_iii para estado "ON" (Zhang et al., 2022)
    if 'updrs_iii' in data:
        u = data['updrs_iii']
        u['sigla'] = 'MDS-UPDRS-III (ON)'
        u['nome'] = 'MDS-UPDRS Parte III (Exame Motor no Estado ON)'
        u['procedimento_passo_a_passo'][0] = {
            'passo': 1,
            'titulo': 'Padronização no Estado Clínico ON',
            'descricao': 'Recomenda-se aplicar TODOS os protocolos de Doença de Parkinson no estado "ON" da medicação dopaminérgica (efeito ótimo da levodopa), garantindo reprodutibilidade entre as reavaliações semanais.'
        }
        u['criterios_pontuacao'] = [
            {'grau': '0 a 132 pontos', 'descricao': 'Cada um dos 33 itens motores é pontuado de 0 (normal) a 4 (severo) no estado ON.'},
            {'grau': 'MCID (Estado ON)', 'descricao': 'Redução ≥ 3,25 a 4,5 pontos ou -15% a -25% no estado ON após 10 a 20 sessões.'}
        ]
        u['interpretacao_clinica'] = (
            'Conforme evidência clínica de referência (Zhang et al., 2022), aplicar sempre no estado "ON". Redução na MDS-UPDRS-III reflete melhora de bradicinesia e rigidez.'
        )

    # 2. Alinhar HAM-A à recomendação brasileira
    if 'ham_a' in data:
        data['ham_a']['validacao_brasil'] = (
            'Recomenda-se usar em conjunto BAI, GAD-7 ou DASS-21, pois a HAM-A não possui validação psicométrica para populações brasileiras.'
        )

    # 3. Adicionar novas escalas oficiais
    for k, v in NEW_SCALES.items():
        data[k] = v

    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open(JS_PATH, 'w', encoding='utf-8') as f:
        f.write('/**\n')
        f.write(' * Rede NAPeN — Base de Dados de Guias Clínicos de Aplicação de Escalas\n')
        f.write(' * Exportação automática alinhada às diretrizes clínicas da Rede NAPeN.\n')
        f.write(' */\n')
        f.write('window.NAPEN_SCALE_GUIDE = ')
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(';\n')

    print(f'✓ Guia de Escalas atualizado com sucesso: {len(data)} escalas em {JSON_PATH} e {JS_PATH}')


if __name__ == '__main__':
    main()
