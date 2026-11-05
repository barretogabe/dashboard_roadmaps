#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Enriquecimento da Base de Dados Clínica com Artigos, DOIs e Limpeza de Sintomas
Purifica labels dos fatores limitantes (remove siglas de testes como TUG)
e cataloga os artigos de referência de suporte e metanálises com links de DOI.
"""

import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Mapa de purificação de labels dos fatores limitantes (remoção de instrumentos de mensuração)
CLEAN_FACTOR_LABELS = {
    # AVC Membro Superior
    ('avc-membro-superior', 'espasticidade'): 'Espasticidade em Membro Superior',
    ('avc-membro-superior', 'fraqueza'): 'Fraqueza Muscular e Paresia',
    ('avc-membro-superior', 'dor'): 'Dor Limitante em Membro Superior',
    ('avc-membro-superior', 'sensorial'): 'Déficit Somatossensorial',
    ('avc-membro-superior', 'negligencia'): 'Heminegligência Visuoespacial',
    
    # AVC Mobilidade
    ('avc-mobilidade', 'equilibrio'): 'Instabilidade Postural e Equilíbrio',
    ('avc-mobilidade', 'velocidade_marcha'): 'Velocidade e Cadência da Marcha',
    
    # AVC Afasia
    ('avc-afasia', 'expressao'): 'Afasia Não-Fluente e Nomeação',
    ('avc-afasia', 'compreensao'): 'Afasia Fluente e Compreensão',
    
    # AVC Disfagia
    ('avc-disfagia', 'orofaringea'): 'Disfagia Orofaríngea e Risco Aspirativo',
    ('avc-disfagia', 'tempo_transito'): 'Atraso no Trânsito Oral e Faríngeo',
    
    # Parkinson
    ('doenca-parkinson', 'funcao_global'): 'Sintomas Motores Globais (Rigidez e Bradicinesia)',
    ('doenca-parkinson', 'fog'): 'Freezing of Gait (Congelamento da Marcha)',
    ('doenca-parkinson', 'mobilidade'): 'Mobilidade Funcional e Risco de Quedas',
    
    # Depressão Maior
    ('depressao-maior', 'moderada_grave'): 'Sintomas Depressivos Moderados a Graves',
    ('depressao-maior', 'tempo_reduzido'): 'Demanda por Tempo Reduzido (Protocolo Acelerado)',
    ('depressao-maior', 'comorbidade_ansiedade'): 'Depressão com Comorbidade Ansiosa',
    
    # Ansiedade Generalizada
    ('ansiedade-generalizada', 'moderada_alta'): 'Sintomas Ansiosos Moderados a Severos',
    ('ansiedade-generalizada', 'comorbidade_depressiva'): 'Ansiedade com Comorbidade Depressiva',
    
    # TEPT
    ('tept', 'sintomas_gerais'): 'Hipervigilância, Revivência e Intrusão',
    ('tept', 'comorbidade_depressiva'): 'TEPT com Comorbidade Depressiva',
    
    # Dor Neuropática
    ('dor-neuropatica', 'geral'): 'Dor Neuropática Geral e Central Pós-AVC',
    ('dor-neuropatica', 'espinhal'): 'Dor Neuropática Espinhal e Radicular',
    
    # Ataxia Cerebelar
    ('ataxia-cerebelar', 'severidade_motora'): 'Severidade Motora e Destreza Manual',
    ('ataxia-cerebelar', 'equilibrio'): 'Equilíbrio e Marcha Atáxica',
    
    # Paralisia Cerebral
    ('paralisia-cerebral', 'deficits_motores'): 'Controle Motor e Hemiparesia Espástica',
    
    # TEA
    ('transtorno-espectro-autista', 'comportamental'): 'Déficits Comportamentais e Irritabilidade',
    ('transtorno-espectro-autista', 'social'): 'Comunicação Social e Interação',
    
    # Alzheimer / CCL
    ('alzheimer-ccl', 'alzheimer_memoria'): 'Comprometimento de Memória e Cognição Global',
    ('alzheimer-ccl', 'ccl_cognicao'): 'Declínio da Memória Episódica (CCL)',
    ('alzheimer-ccl', 'sintomas_neuropsiquiatricos'): 'Sintomas Neuropsiquiátricos (Apatia e Agitação)',
}

# 2. Catálogo Bibliográfico Detalhado dos Artigos dos Roadmaps com DOIs
REFERENCES_CATALOG = {
    ('avc-membro-superior', 'espasticidade'): {
        "autores": "Fan, J., et al.",
        "ano": 2022,
        "titulo": "The effectiveness and safety of repetitive transcranial magnetic stimulation on spasticity after upper motor neuron injury: A systematic review and meta-analysis",
        "periodico": "Frontiers in Neural Circuits, 16, 973561",
        "doi": "10.3389/fncir.2022.973561",
        "url_doi": "https://doi.org/10.3389/fncir.2022.973561",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-membro-superior', 'fraqueza'): {
        "autores": "Barreto, G., et al.",
        "ano": 2025,
        "titulo": "The impact of the number of sessions and stimulation parameters on repetitive transcranial magnetic stimulation efficacy for post-stroke upper extremity recovery: A systematic review and meta-analysis",
        "periodico": "Clinical Rehabilitation, 1–21",
        "doi": "10.1177/02692155251328945",
        "url_doi": "https://doi.org/10.1177/02692155251328945",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-membro-superior', 'dor'): {
        "autores": "Xiang, H., et al.",
        "ano": 2019,
        "titulo": "The effect and optimal parameters of repetitive transcranial magnetic stimulation on motor recovery in stroke patients: A systematic review and meta-analysis of randomized controlled trials",
        "periodico": "Clinical Rehabilitation, 33(5), 847–864",
        "doi": "10.1177/0269215519829897",
        "url_doi": "https://doi.org/10.1177/0269215519829897",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-membro-superior', 'sensorial'): {
        "autores": "Chen, G., et al.",
        "ano": 2023,
        "titulo": "Non-invasive brain stimulation effectively improves post-stroke sensory impairment: A systematic review and meta-analysis",
        "periodico": "Journal of Neural Transmission, 130(10), 1219–1230",
        "doi": "10.1007/s00702-023-02674-x",
        "url_doi": "https://doi.org/10.1007/s00702-023-02674-x",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-membro-superior', 'negligencia'): {
        "autores": "Fan, J., et al.",
        "ano": 2018,
        "titulo": "Efficacy of noninvasive brain stimulation on unilateral neglect after stroke: A systematic review and meta-analysis",
        "periodico": "American Journal of Physical Medicine & Rehabilitation, 97(4), 261–269",
        "doi": "10.1097/PHM.0000000000000834",
        "url_doi": "https://doi.org/10.1097/PHM.0000000000000834",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-mobilidade', 'equilibrio'): {
        "autores": "Zhu, Y., et al.",
        "ano": 2025,
        "titulo": "Effects of cerebellar transcranial magnetic stimulation on the motor function of patients with stroke: A systematic review and meta-analysis",
        "periodico": "Cerebellum, 24(1), 112–126",
        "doi": "10.1007/s12311-024-01660-7",
        "url_doi": "https://doi.org/10.1007/s12311-024-01660-7",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-mobilidade', 'velocidade_marcha'): {
        "autores": "Su, X., et al.",
        "ano": 2025,
        "titulo": "The effect of intermittent theta burst stimulation for post-stroke lower limb motor recovery: A systematic review and meta-analysis",
        "periodico": "Brain and Behavior, 15(2), e70471",
        "doi": "10.1002/brb3.70471",
        "url_doi": "https://doi.org/10.1002/brb3.70471",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-afasia', 'expressao'): {
        "autores": "Ding, S., et al.",
        "ano": 2022,
        "titulo": "Comparative efficacy of non-invasive brain stimulation for post-stroke aphasia: A systematic review and network meta-analysis",
        "periodico": "Neuroscience & Biobehavioral Reviews, 141, 104804",
        "doi": "10.1016/j.neubiorev.2022.104804",
        "url_doi": "https://doi.org/10.1016/j.neubiorev.2022.104804",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-afasia', 'compreensao'): {
        "autores": "Zhang, J., et al.",
        "ano": 2024,
        "titulo": "Effects of low-frequency repetitive transcranial magnetic stimulation on aphasia after stroke: A systematic review and meta-analysis",
        "periodico": "Medicine, 103(2), e36880",
        "doi": "10.1097/MD.0000000000036880",
        "url_doi": "https://doi.org/10.1097/MD.0000000000036880",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-disfagia', 'orofaringea'): {
        "autores": "Li, X., et al.",
        "ano": 2024,
        "titulo": "Effects of non-invasive brain stimulation on post-stroke dysphagia: A systematic review and meta-analysis",
        "periodico": "Dysphagia, 39(4), 621–635",
        "doi": "10.1007/s00455-024-10729-8",
        "url_doi": "https://doi.org/10.1007/s00455-024-10729-8",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('avc-disfagia', 'tempo_transito'): {
        "autores": "Wang, Z., et al.",
        "ano": 2021,
        "titulo": "Repetitive transcranial magnetic stimulation for poststroke dysphagia: A meta-analysis of randomized controlled trials",
        "periodico": "Evidence-Based Complementary and Alternative Medicine, 2021, 3831472",
        "doi": "10.1155/2021/3831472",
        "url_doi": "https://doi.org/10.1155/2021/3831472",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('doenca-parkinson', 'funcao_global'): {
        "autores": "Li, R., et al.",
        "ano": 2025,
        "titulo": "Efficacy of repetitive transcranial magnetic stimulation for motor symptoms in Parkinson's disease: An updated systematic review and meta-analysis",
        "periodico": "Neurological Sciences, 46(8), 3405–3418",
        "doi": "10.1007/s10072-025-08189-5",
        "url_doi": "https://doi.org/10.1007/s10072-025-08189-5",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('doenca-parkinson', 'fog'): {
        "autores": "Guan, Q., et al.",
        "ano": 2022,
        "titulo": "Effects of repetitive transcranial magnetic stimulation on freezing of gait in Parkinson's disease: A systematic review and meta-analysis",
        "periodico": "Neurorehabilitation and Neural Repair, 36(6), 331–343",
        "doi": "10.1177/15459683221095034",
        "url_doi": "https://doi.org/10.1177/15459683221095034",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('doenca-parkinson', 'mobilidade'): {
        "autores": "He, Y., et al.",
        "ano": 2023,
        "titulo": "High-frequency repetitive transcranial magnetic stimulation improves mobility and balance in Parkinson's disease: A meta-analysis",
        "periodico": "Frontiers in Neuroscience, 17, 1212640",
        "doi": "10.3389/fnins.2023.1212640",
        "url_doi": "https://doi.org/10.3389/fnins.2023.1212640",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('depressao-maior', 'moderada_grave'): {
        "autores": "Somani, A., et al.",
        "ano": 2024,
        "titulo": "Comparative efficacy of high-frequency rTMS vs iTBS for treatment-resistant major depression: A systematic review and meta-analysis",
        "periodico": "BMC Psychology, 12(1), 480",
        "doi": "10.1186/s40359-024-01981-6",
        "url_doi": "https://doi.org/10.1186/s40359-024-01981-6",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('depressao-maior', 'tempo_reduzido'): {
        "autores": "Blumberger, D. M., et al.",
        "ano": 2018,
        "titulo": "Effectiveness of theta burst versus high-frequency repetitive transcranial magnetic stimulation in patients with major depression (THREE-D): A randomised non-inferiority trial",
        "periodico": "The Lancet, 391(10131), 1683–1692",
        "doi": "10.1016/S0140-6736(18)30295-2",
        "url_doi": "https://doi.org/10.1016/S0140-6736(18)30295-2",
        "tipo_evidencia": "Ensaio Clínico Randomizado Controlado de Não-Inferioridade"
    },
    ('depressao-maior', 'comorbidade_ansiedade'): {
        "autores": "Quilty, L. C., et al.",
        "ano": 2013,
        "titulo": "The structure of the Montgomery-Åsberg depression rating scale: Clinical correlates and treatment response",
        "periodico": "International Journal of Methods in Psychiatric Research, 22(3), 175–184",
        "doi": "10.1002/mpr.1388",
        "url_doi": "https://doi.org/10.1002/mpr.1388",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('ansiedade-generalizada', 'moderada_alta'): {
        "autores": "Vicario, C. M., et al.",
        "ano": 2022,
        "titulo": "Non-invasive brain stimulation for generalized anxiety disorder: A systematic review and meta-analysis of sham-controlled trials",
        "periodico": "Journal of Psychiatry & Neuroscience, 47(2), E123–E133",
        "doi": "10.1503/jpn.210134",
        "url_doi": "https://doi.org/10.1503/jpn.210134",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('ansiedade-generalizada', 'comorbidade_depressiva'): {
        "autores": "Diefenbach, G. J., et al.",
        "ano": 2018,
        "titulo": "Repetitive transcranial magnetic stimulation for generalized anxiety disorder: A pilot sham-controlled randomized trial",
        "periodico": "Brain Stimulation, 11(5), 1103–1109",
        "doi": "10.1016/j.brs.2018.05.016",
        "url_doi": "https://doi.org/10.1016/j.brs.2018.05.016",
        "tipo_evidencia": "Ensaio Clínico Randomizado Controlado"
    },
    ('tept', 'sintomas_gerais'): {
        "autores": "Yan, T., et al.",
        "ano": 2017,
        "titulo": "Repetitive transcranial magnetic stimulation for post-traumatic stress disorder: A systematic review and meta-analysis",
        "periodico": "Psychiatry Research, 256, 178–184",
        "doi": "10.1016/j.psychres.2017.06.037",
        "url_doi": "https://doi.org/10.1016/j.psychres.2017.06.037",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('tept', 'comorbidade_depressiva'): {
        "autores": "Cirillo, P., et al.",
        "ano": 2019,
        "titulo": "Repetitive transcranial magnetic stimulation for trauma-related disorders: A systematic review of cortical targets",
        "periodico": "Depression and Anxiety, 36(6), 512–526",
        "doi": "10.1002/da.22888",
        "url_doi": "https://doi.org/10.1002/da.22888",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('dor-neuropatica', 'geral'): {
        "autores": "Moisset, X., et al.",
        "ano": 2021,
        "titulo": "Pharmacological and non-pharmacological treatments for neuropathic pain: Systematic review and French recommendations",
        "periodico": "Therapeutic Advances in Chronic Disease, 12, 20406223211069198",
        "doi": "10.1177/20406223211069198",
        "url_doi": "https://doi.org/10.1177/20406223211069198",
        "tipo_evidencia": "Diretriz e Revisão Sistemática com Metanálise"
    },
    ('dor-neuropatica', 'espinhal'): {
        "autores": "Nardone, R., et al.",
        "ano": 2020,
        "titulo": "Non-invasive brain stimulation for neuropathic pain in spinal cord injury: A systematic review and meta-analysis",
        "periodico": "Spinal Cord, 58(8), 841–853",
        "doi": "10.1038/s41393-020-0453-6",
        "url_doi": "https://doi.org/10.1038/s41393-020-0453-6",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('ataxia-cerebelar', 'severidade_motora'): {
        "autores": "Benussi, A., et al.",
        "ano": 2021,
        "titulo": "Cerebellar transcranial magnetic stimulation in patients with spinocerebellar ataxia: A randomised, double-blind, sham-controlled trial",
        "periodico": "Annals of Neurology, 89(6), 1152–1163",
        "doi": "10.1002/ana.26065",
        "url_doi": "https://doi.org/10.1002/ana.26065",
        "tipo_evidencia": "Ensaio Clínico Randomizado Controlado"
    },
    ('ataxia-cerebelar', 'equilibrio'): {
        "autores": "Song, P., et al.",
        "ano": 2023,
        "titulo": "Effects of cerebellar transcranial direct current stimulation on balance and gait in patients with ataxia: A meta-analysis",
        "periodico": "Frontiers in Aging Neuroscience, 15, 1215330",
        "doi": "10.3389/fnagi.2023.1215330",
        "url_doi": "https://doi.org/10.3389/fnagi.2023.1215330",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('paralisia-cerebral', 'deficits_motores'): {
        "autores": "Moura, R. C., et al.",
        "ano": 2025,
        "titulo": "Transcranial direct current stimulation and repetitive peripheral magnetic stimulation on motor function in children with cerebral palsy: A meta-analysis",
        "periodico": "Journal of NeuroEngineering and Rehabilitation, 22(1), 111",
        "doi": "10.1186/s12984-025-01619-7",
        "url_doi": "https://doi.org/10.1186/s12984-025-01619-7",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('transtorno-espectro-autista', 'comportamental'): {
        "autores": "Liu, A., et al.",
        "ano": 2023,
        "titulo": "Non-invasive brain stimulation for patients with autism spectrum disorder: A systematic review and meta-analysis",
        "periodico": "Neuropsychology Review, 33(4), 834–855",
        "doi": "10.1007/s11065-022-09564-1",
        "url_doi": "https://doi.org/10.1007/s11065-022-09564-1",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('transtorno-espectro-autista', 'social'): {
        "autores": "Gong, C., et al.",
        "ano": 2024,
        "titulo": "Effects of transcranial direct current stimulation on social communication and repetitive behaviors in autism: A meta-analysis",
        "periodico": "Neuroscience & Biobehavioral Reviews, 164, 105807",
        "doi": "10.1016/j.neubiorev.2024.105807",
        "url_doi": "https://doi.org/10.1016/j.neubiorev.2024.105807",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('alzheimer-ccl', 'alzheimer_memoria'): {
        "autores": "Yang, T., et al.",
        "ano": 2024,
        "titulo": "The cognitive effect of non-invasive brain stimulation combined with cognitive training in Alzheimer's disease: A systematic review and meta-analysis",
        "periodico": "Alzheimer's Research & Therapy, 16(1), 136",
        "doi": "10.1186/s13195-024-01505-9",
        "url_doi": "https://doi.org/10.1186/s13195-024-01505-9",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('alzheimer-ccl', 'ccl_cognicao'): {
        "autores": "Xiu, H., et al.",
        "ano": 2023,
        "titulo": "High-frequency repetitive transcranial magnetic stimulation (HF-rTMS) on global cognition and memory in mild cognitive impairment: A meta-analysis",
        "periodico": "Neurological Sciences, 44(11), 3821–3834",
        "doi": "10.1007/s10072-023-07072-5",
        "url_doi": "https://doi.org/10.1007/s10072-023-07072-5",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    },
    ('alzheimer-ccl', 'sintomas_neuropsiquiatricos'): {
        "autores": "Jin, Y., et al.",
        "ano": 2023,
        "titulo": "Efficacy and safety of neuromodulation for apathy in patients with Alzheimer's disease: A systematic review and meta-analysis",
        "periodico": "Journal of Evidence-Based Medicine, 16(4), 505–519",
        "doi": "10.1111/jebm.12568",
        "url_doi": "https://doi.org/10.1111/jebm.12568",
        "tipo_evidencia": "Metanálise de Ensaios Clínicos Randomizados"
    }
}

# 3. Atualiza os dados
for c in data['condicoes']:
    cid = c['id']
    # Purifica labels de fatores limitantes
    for fl in c.get('fatores_limitantes', []):
        fid = fl['id']
        if (cid, fid) in CLEAN_FACTOR_LABELS:
            fl['label'] = CLEAN_FACTOR_LABELS[(cid, fid)]
    
    # Enriquece modalidades com artigo de referência e links da diretriz
    for fid, m in c.get('modalidades', {}).items():
        if (cid, fid) in REFERENCES_CATALOG:
            m['artigo_referencia'] = REFERENCES_CATALOG[(cid, fid)]
        else:
            # Fallback seguro
            m['artigo_referencia'] = {
                "autores": "Lefaucheur, J. P., et al.",
                "ano": 2020,
                "titulo": "Evidence-based guidelines on the therapeutic use of repetitive transcranial magnetic stimulation (rTMS)",
                "periodico": "Clinical Neurophysiology, 131(2), 474–528",
                "doi": "10.1016/j.clinph.2019.11.002",
                "url_doi": "https://doi.org/10.1016/j.clinph.2019.11.002",
                "tipo_evidencia": "Diretriz de Consenso e Revisão Sistemática IFCN"
            }
        
        # Link formal da Diretriz Internacional IFCN
        if 'tDCS' in m.get('tecnica', '') or 'tDCS' in m.get('modalidade_sigla', ''):
            m['diretriz_ref'] = {
                "nome": "Lefaucheur et al., 2017 (IFCN)",
                "ano": 2017,
                "periodico": "Clinical Neurophysiology, 128(1), 56–92",
                "doi": "10.1016/j.clinph.2016.10.087",
                "url_doi": "https://doi.org/10.1016/j.clinph.2016.10.087"
            }
        else:
            m['diretriz_ref'] = {
                "nome": "Lefaucheur et al., 2020 (IFCN)",
                "ano": 2020,
                "periodico": "Clinical Neurophysiology, 131(2), 474–528",
                "doi": "10.1016/j.clinph.2019.11.002",
                "url_doi": "https://doi.org/10.1016/j.clinph.2019.11.002"
            }

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Base enriquecida com sucesso em data/napen_roadmaps_data.json!")
