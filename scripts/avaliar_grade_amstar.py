#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Auditoria Preliminar de Qualidade Metodológica (AMSTAR 2),
Certeza da Evidência (GRADE) e Diretrizes de Tolerabilidade por Roadmap (RM01–RM18).

Fontes auditáveis:
1. Metadados e resumos verificados nas bases OpenAlex / Europe PMC / Crossref (data/verified_metas_catalog.json).
2. Diretrizes de segurança e tolerabilidade extraídas dos Roadmaps oficiais RM01–RM18 da Rede NAPeN.
3. Diretrizes internacionais Lefaucheur et al. (2020 rTMS / 2017 tDCS) e consensos clínicos NAPeN.

Todas as classificações são explicitamente sinalizadas como:
  "Avaliação preliminar — Em homologação pelo GT NAPeN"
"""

import json
import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CATALOG_FILE = os.path.join(BASE_DIR, 'data', 'verified_metas_catalog.json')
ROADMAPS_FILE = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
OUT_AUDIT_FILE = os.path.join(BASE_DIR, 'data', 'grade_amstar_audit.json')

STATUS_HOMOLOGACAO = 'Avaliação preliminar — Em homologação pelo GT NAPeN'

GRADE_SYMBOLS = {
    'Alta': '⊕⊕⊕⊕',
    'Moderada': '⊕⊕⊕◯',
    'Baixa': '⊕⊕◯◯',
    'Muito Baixa': '⊕◯◯◯',
}

# Mapeamento verificado (condicao_id, fator_id) -> DOI verificado, perfil AMSTAR 2 preliminar,
# perfil GRADE por desfecho e diretrizes de tolerabilidade dos Roadmaps RM01–RM18.
PAIR_AUDIT_CONFIG = {
    ('avc-membro-superior', 'espasticidade'): {
        'doi': '10.3389/fncir.2022.973561',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca em 8 bases, seleção e avaliação de risco de viés em duplicata, e aplicação do GRADE descritas no artigo (42 ECRs, n=2.108). Verificação completa da lista de excluídos e financiamento primário em homologação pelo GT.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Risco de viés moderado e alta heterogeneidade clínica entre protocolos de rTMS em espasticidade pós-AVC (concordante com avaliação GRADE dos próprios autores em Fan et al., 2022).',
        },
        'tol_key': 'rm01_motor',
    },
    ('avc-membro-superior', 'fraqueza'): {
        'doi': '10.1177/02692155251328945',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Revisão sistemática com 6 bases, avaliação metodológica via escala PEDro e metanálise dose-resposta via curva ROC (35 ECRs, n=897). Verificação integral de itens não-críticos e protocolo prévio em homologação pelo GT.',
        },
        'grade': {
            'certeza': 'Alta',
            'forca': 'Forte',
            'dominios': 'Consistência robusta em 35 ECRs (Antonino et al., 2025) e Nível A internacional (Lefaucheur et al., 2020) para recuperação motora do membro superior na presença de potencial evocado motor (≥15 sessões, ≥1.000 pulsos/sessão).',
        },
        'tol_key': 'rm01_motor',
    },
    ('avc-membro-superior', 'dor'): {
        'doi': '10.3389/fnins.2024.1367649',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Adere às diretrizes PRISMA, registro PROSPERO CRD42024497530, busca em 6 bases, RoB 2 + escala PEDro e cálculo de I² (6 ECRs, n=288). Pendência de checagem do texto completo dos itens 7 e 10 pelo GT.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Amostra total reduzida (n=288 em 6 ECRs) com imprecisão estatística e inconsistência em seguimento superior a 6 meses na dor central pós-AVC.',
        },
        'tol_key': 'rm01_dor',
    },
    ('avc-membro-superior', 'sensorial'): {
        'doi': '10.1007/s00702-023-02674-x',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca sistemática em 6 bases sem restrição de idioma (14 ECRs, n=804) com subanálises por frequência, sítio e número de sessões; registro prévio e tabela detalhada de excluídos em checagem pelo GT.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Evidência de certeza moderada reportada pelos próprios autores (Chen et al., 2023), condicionada à execução de pelo menos 10 sessões e heterogeneidade de testes sensoriais.',
        },
        'tol_key': 'rm01_motor',
    },
    ('avc-membro-superior', 'negligencia'): {
        'doi': '10.1097/PHM.0000000000000834',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca abrangente (CENTRAL, Medline, Embase, Web of Knowledge) e avaliação sistemática de risco de viés em 11 ECRs; lista completa de excluídos e registro prévio em homologação pelo GT.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Tamanho amostral pequeno por subgrupo de técnica (rTMS vs. cTBS vs. tDCS) e risco de viés heterogêneo nos ensaios primários de heminegligência.',
        },
        'tol_key': 'rm01_motor',
    },
    ('avc-membro-superior', 'sem_pem'): {
        'doi': '10.1002/brb3.70471',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Registro PROSPERO CRD42024540604, busca em 6 bases, triagem em duplicata, Cochrane RoB 2 + escala PEDro e análise de sensibilidade (20 ECRs, n=812).',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Evidência indireta parcial para população sem potencial evocado motor no membro superior, com variabilidade entre fase subaguda e crônica e baixa certeza específica para ganho distal isolado.',
        },
        'tol_key': 'rm01_cerebelar',
    },
    ('avc-membro-superior', 'sem_pem_cerebelar'): {
        'doi': '10.1002/brb3.70471',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Registro PROSPERO CRD42024540604, busca em 6 bases, triagem independente em duplicata e avaliação via Cochrane RoB 2 e PEDro (20 ECRs, n=812).',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Certeza rebaixada por evidência indireta (ausência de estratificação universal por potencial evocado motor nos ensaios originais) e heterogeneidade clínica.',
        },
        'tol_key': 'rm01_cerebelar',
    },
    ('avc-membro-superior', 'sem_pem_premotor'): {
        'doi': '10.1177/02692155251328945',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca em 6 bases (PubMed, CINAHL, PEDro, LILACS, SciELO, Scopus), avaliação de viés via escala PEDro e metanálise de parâmetros (35 ECRs, n=897).',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Aplicação ao córtex pré-motor ou via alternativa diante de lesão extensa do giro pré-central apoia-se em racional neurofisiológico e subgrupos indiretos, justificando certeza preliminar baixa e recomendação condicional.',
        },
        'tol_key': 'rm01_motor',
    },
    ('avc-mobilidade', 'equilibrio'): {
        'doi': '10.1007/s12311-024-01660-7',
        'amstar2': {
            'nivel': 'Baixa',
            'justificativa': 'Metanálise multimodal (10 ECRs cerebelares + 18 estudos ALE fMRI) avaliada neste protocolo; resumo não detalha registro prévio em PROSPERO nem instrumento formal de risco de viés, requerendo checagem pelo GT (suplementada por Zhu et al., 2025).',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Convergência consistente na Escala de Equilíbrio de Berg entre Zeng et al. (2024) e Zhu et al. (2025, 20 ECRs), com ressalva por heterogeneidade entre parâmetros cerebelares.',
        },
        'tol_key': 'rm03_mobilidade',
    },
    ('avc-mobilidade', 'velocidade_marcha'): {
        'doi': '10.1177/10538135241304991',
        'amstar2': {
            'nivel': 'Baixa',
            'justificativa': 'Busca em 7 bases até maio/2024 com análises de subgrupo por sítio, dose e sessões; resumo não explicita ferramenta de risco de viés ou número PROSPERO, em verificação no texto completo pelo GT.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Efeito positivo em FMA-LE, equilíbrio e marcha com iTBS (≥1.200 pulsos, ≥15 sessões) em fase subaguda, porém sem efeito significativo em amplitude de potencial evocado motor e com necessidade de ECRs maiores.',
        },
        'tol_key': 'rm03_mobilidade',
    },
    ('avc-afasia', 'expressao'): {
        'doi': '10.1016/j.neubiorev.2022.104804',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Metanálise em rede bayesiana robusta e metarregressão incluindo 69 ECRs (n=1.670) incluída para afasia de expressão; verificação formal de registro prévio e tabela de risco de viés no texto completo em homologação pelo GT.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Consistência de LF-rTMS contralesional (giro frontal inferior direito) em 69 ECRs e alinhamento ao Nível B de Lefaucheur et al. (2020), com moderação por período terapêutico e número de sessões.',
        },
        'tol_key': 'rm08_afasia',
    },
    ('avc-afasia', 'compreensao'): {
        'doi': '10.1097/MD.0000000000036880',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca em 9 bases e 2 registros de ensaios clínicos, avaliação de risco de viés (RoB) e metanálise em rede associada à fonoterapia (17 ECRs, n=1.013) incluída para afasia de compreensão.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Melhora consistente nos subescores de compreensão auditiva e quociente de afasia (rTMS combinada a treino de fala) sem elevação de eventos adversos, embora com intervalos variáveis por tempo pós-AVC.',
        },
        'tol_key': 'rm09_afasia_rtms',
    },
    ('avc-disfagia', 'orofaringea'): {
        'doi': '10.1007/s00455-024-10729-8',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca em 8 bases bilíngues e aplicação explícita da ferramenta Cochrane Risk of Bias (9 estudos, n=567) incluída para disfagia orofaríngea; verificação de registro e viés de publicação pelo GT.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Os próprios autores destacam que o número reduzido de ECRs (n=567) e presença de risco de viés incerto em parte dos estudos limitam a força conclusiva da evidência.',
        },
        'tol_key': 'rm07_disfagia',
    },
    ('avc-disfagia', 'tempo_transito'): {
        'doi': '10.3389/fnhum.2022.841781',
        'amstar2': {
            'nivel': 'Baixa',
            'justificativa': 'Adere ao PRISMA com busca em 6 bases e cálculo de heterogeneidade I² (11 ECRs, n=463); resumo não descreve avaliação padronizada de risco de viés nem registro PROSPERO.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Amostra moderada-pequena (11 ECRs, n=463), dependência de associação com terapia tradicional de deglutição e variabilidade entre alvos ipsilesional e contralesional.',
        },
        'tol_key': 'rm07_disfagia',
    },
    ('doenca-parkinson', 'funcao_global'): {
        'doi': '10.1177/15459683221095034',
        'amstar2': {
            'nivel': 'Baixa',
            'justificativa': 'Metanálise de 32 ECRs sham-controlados incluída para Doença de Parkinson; busca restrita a 2 bases no resumo sem explicitação de risco de viés ou PROSPERO. Complementada pelo overview de Conte et al. (2025, 21 RS / 107 estudos).',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Concordância entre 32 ECRs em UPDRS-III e o overview recente de Conte et al. (2025), o qual classifica a certeza global como baixa a moderada pela heterogeneidade de alvos e estágio medicamentoso ON/OFF.',
        },
        'tol_key': 'rm17_parkinson',
    },
    ('doenca-parkinson', 'fog'): {
        'doi': '10.1016/j.apmr.2019.07.013',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca múltipla (MEDLINE, Embase, Cochrane), extração independente por 2 revisores e avaliação metodológica pela escala PEDro (14 ECRs, n=298) incluída para congelamento de marcha.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Benefício documentado em velocidade de marcha no estado ON a curto prazo, porém sem sustentação consistente a longo prazo ou diferença significativa isolada no questionário de congelamento de marcha (FOGQ) e TUG.',
        },
        'tol_key': 'rm17_parkinson_fog',
    },
    ('doenca-parkinson', 'mobilidade'): {
        'doi': '10.1016/j.eclinm.2022.101589',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Registro PROSPERO CRD42022329633, seleção por 2 investigadores independentes e baixa heterogeneidade documentada (I²=29% para função motora, 14 ECRs, n=469) incluída para mobilidade na Doença de Parkinson.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Baixa inconsistência (I²=29%) para ganho motor em HF-rTMS sobre M1/SMA em 12 ECRs motores (n=381), limitada pelo tamanho amostral modesto por protocolo de membro inferior.',
        },
        'tol_key': 'rm17_parkinson',
    },
    ('depressao-maior', 'moderada_grave'): {
        'doi': '10.1001/jamapsychiatry.2016.3644',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Registro PROSPERO CRD42015019855, busca em 4 bases, extração e avaliação de qualidade por 2 revisores em 81 ECRs (n=4.233) em NMA. Verificação de itens de financiamento e excluídos pelo GT.',
        },
        'grade': {
            'certeza': 'Alta',
            'forca': 'Forte',
            'dominios': 'Grande volume de ECRs sham-controlados (n=4.233) demonstrando superioridade consistente em taxa de resposta e aceitabilidade para rTMS HF F3, LF F4 e bilateral (Nível A em diretrizes internacionais).',
        },
        'tol_key': 'rm10_depressao',
    },
    ('depressao-maior', 'tempo_reduzido'): {
        'doi': '10.1038/s41380-024-02630-5',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Metanálise pareada e em rede de 23 ECRs (n=960) avaliando resposta, remissão, abandono, viragem maníaca e cefaleia/desconforto em protocolos TBS; verificação de registro e RoB pelo GT.',
        },
        'grade': {
            'certeza': 'Alta',
            'forca': 'Forte',
            'dominios': 'Consistência robusta entre 23 ECRs mostrando equivalência/superioridade de iTBS em L-DLPFC (F3) e cTBS+iTBS bilateral sobre sham com perfil favorável de aceitabilidade e aprovação regulatória (Nível A).',
        },
        'tol_key': 'rm10_depressao',
    },
    ('depressao-maior', 'comorbidade_ansiedade'): {
        'doi': '10.1016/j.jad.2021.03.019',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Metanálise em rede aderente à extensão PRISMA-NMA com 49 ECRs (n=2.941) comparando eficácia e aceitabilidade de rTMS bilateral, LF direita, HF esquerda e TBS em depressão resistente.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Forte evidência para depressão resistente em NMA (n=2.941), porém com evidência parcialmente indireta quanto ao desfecho ansioso comórbido específico (suplementada por curvas dose-resposta em Sabé et al., 2024).',
        },
        'tol_key': 'rm10_depressao',
    },
    ('ansiedade-generalizada', 'moderada_alta'): {
        'doi': '10.1093/ijnp/pyab077',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Adere às diretrizes PRISMA, avalia heterogeneidade (Q, I²=13,32%, τ²) e viés de publicação, com avaliação de risco de viés em 6 estudos (n=152); checagem de registro e texto completo pelo GT.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Tamanho amostral total pequeno (6 estudos, n=152; 97 ativos vs. 55 sham) exigindo cautela e novos ECRs multicêntricos, apesar da baixa heterogeneidade observada (I²=13,3%).',
        },
        'tol_key': 'rm11_ansiedade',
    },
    ('ansiedade-generalizada', 'comorbidade_depressiva'): {
        'doi': '10.1002/brb3.1284',
        'amstar2': {
            'nivel': 'Baixa',
            'justificativa': 'Segue PRISMA com busca em 3 bases (n=17 incluídos, sendo 4 em TAG e 9 em TEPT); resumo não relata ferramenta formal de risco de viés, registro prévio ou análise de viés de publicação.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Número muito reduzido de ensaios específicos em TAG com comorbidade depressiva, imprecisão dos intervalos de confiança e evidência mista entre alta e baixa frequência em DLPFC.',
        },
        'tol_key': 'rm11_ansiedade',
    },
    ('tept', 'sintomas_gerais'): {
        'doi': '10.1016/j.janxdis.2024.102912',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Revisão sistemática com NMA bayesiana de 21 ECRs (n=981) no TEPT avaliando 9 protocolos de neuromodulação no desfecho imediato, aceitabilidade e seguimento; verificação de registro e RoB pelo GT.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Significância clínica imediata consistente para HF-rTMS, iTBS e LF-rTMS (21 ECRs, n=981), porém rebaixada de Alta por perda de significância sustentada no follow-up tardio.',
        },
        'tol_key': 'rm18_tept',
    },
    ('tept', 'comorbidade_depressiva'): {
        'doi': '10.1177/0706743720982432',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Registro PROSPERO CRD42019134984, aderência ao PRISMA, triagem por 2 revisores independentes e busca em 4 bases (10 ECRs, n=421) incluída para TEPT.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Imprecisão em amostras menores (n=421 em 10 ECRs), ausência de diferença entre alvos ativos nas comparações diretas e heterogeneidade clínica nos sintomas depressivos comórbidos.',
        },
        'tol_key': 'rm18_tept',
    },
    ('dor-neuropatica', 'geral'): {
        'doi': '10.1002/14651858.cd008208.pub5',
        'amstar2': {
            'nivel': 'Alta',
            'justificativa': 'Revisão Sistemática Cochrane (O’Connell et al., 2018) com protocolo publicado a priori, triagem dupla, tabela detalhada de estudos excluídos, avaliação completa de RoB Cochrane e transparência de financiamento.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Forte',
            'dominios': 'Na dor neuropática crônica, rTMS de alta frequência sobre M1 reúne Nível A nas diretrizes Lefaucheur et al. (2020) e recomendações GRADE francesas (Moisset et al., 2020), com rebaixamento de Alta para Moderada por heterogeneidade e imprecisão nas análises Cochrane de dor crônica mista.',
        },
        'tol_key': 'rm05_dor',
    },
    ('dor-neuropatica', 'espinhal'): {
        'doi': '10.3389/fnins.2021.800560',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca em 8 bases seguindo o Cochrane Handbook com metanálise em rede (17 estudos, n=507) para dor neuropática após lesão medular; confirmação de registro prévio e viés de publicação pelo GT.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Ensaios de pequeno porte em dor por lesão medular (17 estudos, n=507), necessidade de ensaios multicêntricos duplo-cegos maiores apontada pelos autores e efeito reduzido no seguimento.',
        },
        'tol_key': 'rm05_dor',
    },
    ('ataxia-cerebelar', 'severidade_motora'): {
        'doi': '10.1002/mdc3.14205',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Registro PROSPERO CRD42023379192, busca em 4 bases (PubMed, Cochrane, CINAHL, PEDro), avaliação formal de RoB e aplicação do sistema GRADE pelos próprios autores (17 ECRs, n=661 SARA / n=606 ICARS).',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Os próprios autores (Matsugi et al., 2024) atribuíram baixa certeza pelo sistema GRADE devido a risco de viés sério nos ECRs incluídos e alta heterogeneidade estatística.',
        },
        'tol_key': 'rm16_ataxia',
    },
    ('ataxia-cerebelar', 'equilibrio'): {
        'doi': '10.3389/fneur.2023.1177746',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Registro PROSPERO CRD42022295726, busca em 4 bases e avaliação metodológica pela escala PEDro (8 estudos, n=278), incluindo síntese de eventos adversos.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Amostra total reduzida (8 estudos, n=278) e inconsistência entre alvos e frequências cerebelares; autores recomendam cautela até publicação de ECRs maiores.',
        },
        'tol_key': 'rm16_ataxia',
    },
    ('paralisia-cerebral', 'deficits_motores'): {
        'doi': '10.1186/s12984-025-01619-7',
        'amstar2': {
            'nivel': 'Baixa',
            'justificativa': 'Busca em 5 bases até abril/2024 com avaliação quantitativa de segurança e mobilidade em crianças de 3–14 anos (16 ECRs, n=346) na Paralisia Cerebral; registro PROSPERO e RoB detalhado em checagem pelo GT (além de Metelski et al., 2023 com GRADE).',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Evidência de certeza moderada para segurança e viabilidade em pediatria (Metelski et al., 2023; Zhong et al., 2025), porém certeza baixa/inconclusiva para equilíbrio isolado e heterogeneidade de idades e parâmetros motores.',
        },
        'tol_key': 'rm14_pc',
    },
    ('transtorno-espectro-autista', 'comportamental'): {
        'doi': '10.3389/fpsyt.2023.1147327',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca em 5 bases (22 estudos, n=829) no TEA, com análise crítica explícita de risco de viés e viés de publicação; verificação de registro prévio no texto completo pelo GT.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Risco de viés moderado a alto nos estudos primários (limitações de cegamento de participantes e avaliadores), viés de publicação significativo e ausência de seguimento contínuo prolongado.',
        },
        'tol_key': 'rm15_tea',
    },
    ('transtorno-espectro-autista', 'social'): {
        'doi': '10.1016/j.neubiorev.2024.105807',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Registro INPLASY202370003 e metanálise em rede bayesiana de 16 ECRs (n=709) no TEA, avaliando eficácia comparativa, taxas de abandono e eventos adversos graves.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Nenhum protocolo isolado demonstrou benefício robusto especificamente em comunicação social nesta NMA (16 ECRs, n=709), mantendo indicação condicional e não de primeira linha no TEA.',
        },
        'tol_key': 'rm15_tea',
    },
    ('alzheimer-ccl', 'alzheimer_memoria'): {
        'doi': '10.1007/s10072-023-07072-5',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Busca bilíngue em 10 bases (chinês e inglês) somente com ECRs e avaliação formal de qualidade metodológica (17 estudos, n=1.161) na Doença de Alzheimer.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Melhora consistente em cognição global no MEEM (17 ECRs, n=1.161) em Alzheimer leve a moderado, com ressalva pela variabilidade entre protocolos multissítio e necessidade de associar treino cognitivo.',
        },
        'tol_key': 'rm12_alzheimer',
    },
    ('alzheimer-ccl', 'ccl_cognicao'): {
        'doi': '10.1186/s13195-024-01505-9',
        'amstar2': {
            'nivel': 'Moderada',
            'justificativa': 'Segue PRISMA com busca em 5 bases e dupla avaliação de qualidade/risco de viés (escala PEDro média 7,9 + Cochrane RoB) em 15 estudos (n=685) no Declínio Cognitivo Leve e Doença de Alzheimer.',
        },
        'grade': {
            'certeza': 'Moderada',
            'forca': 'Condicional',
            'dominios': 'Consistência de efeito imediato e no follow-up quando rTMS/tDCS é combinada a treino cognitivo, com heterogeneidade moderada em subdomínios executivos no comprometimento cognitivo leve.',
        },
        'tol_key': 'rm13_alzheimer_tdcs',
    },
    ('alzheimer-ccl', 'sintomas_neuropsiquiatricos'): {
        'doi': '10.1016/j.jpsychires.2024.01.016',
        'amstar2': {
            'nivel': 'Baixa',
            'justificativa': 'Busca em 3 bases (CENTRAL, Embase, PubMed) incluindo 4 ECRs (n=89) para sintomas neuropsiquiátricos na demência; resumo não explicita instrumento de risco de viés nem registro PROSPERO.',
        },
        'grade': {
            'certeza': 'Baixa',
            'forca': 'Condicional',
            'dominios': 'Amostra total muito pequena (4 ECRs, n=89), ausência de significância global sem estratificação por intensidade (120% LMR) e necessidade de ECRs maiores para sintomas neuropsiquiátricos.',
        },
        'tol_key': 'rm12_alzheimer',
    },
}

TOLERABILITY_PROFILES = {
    'rm01_motor': {
        'orientacao_tolerabilidade': 'Reduzir temporariamente a intensidade para 80% do LMR em caso de desconforto ou cefaleia local pela bobina, progredindo gradualmente até a meta do protocolo.',
        'ajuste_seguranca': 'Se o Limiar Motor de Repouso (LMR) não for identificável, calibrar entre 70%–80% do Limiar Motor Ativo (LMA); ajustar o apoio e posicionamento confortável do membro e da bobina.',
        'fatores_moduladores': 'Qualidade do sono, alimentação prévia, uso de benzodiazepínicos/antiepilépticos e integridade do trato corticoespinhal.',
    },
    'rm01_dor': {
        'orientacao_tolerabilidade': 'Monitorar cefaleia tensional local ou exacerbação transitória da dor neuropática; titular intensidade em degraus a partir de 80% do LMR conforme tolerância individual.',
        'ajuste_seguranca': 'Considerar melhora qualitativa em alodinia, hiperalgesia, sono ou humor mesmo que o escore bruto de dor varie abaixo da MCID; evitar pressão excessiva da bobina sobre áreas hiperestésicas.',
        'fatores_moduladores': 'Presença de alodinia mecânica, medicações analgésicas centrais (gabapentinoides/antidepressivos) e distúrbios do sono.',
    },
    'rm01_cerebelar': {
        'orientacao_tolerabilidade': 'Em alvos cerebelares (2 cm abaixo e lateral ao ínion), vigiar contração muscular cervical, desconforto occipital ou tontura transitória.',
        'ajuste_seguranca': 'Ajustar angulação/contato da bobina duplo-cone ou parabólica e iniciar a 80% do LMR com progressão gradual nas sessões iniciais.',
        'fatores_moduladores': 'Rigidez cervical, uso de relaxantes musculares/benzodiazepínicos e tolerância à estimulação occipital.',
    },
    'rm03_mobilidade': {
        'orientacao_tolerabilidade': 'Ajustar a distribuição de pulsos nos trens e iniciar em intensidade submáxima tolerada caso ocorra desconforto occipital ou cervical.',
        'ajuste_seguranca': 'Na tDCS, verificar hidratação das esponjas, inspecionar a integridade cutânea sob os eletrodos e utilizar rampa de subida/descida de 10–30 segundos.',
        'fatores_moduladores': 'Fadiga de membros inferiores, espasticidade associada, risco de queda e uso de antiespásticos ou sedativos.',
    },
    'rm07_disfagia': {
        'orientacao_tolerabilidade': 'Monitorar desconforto cervical, contração facial ou de músculos milo-hióideos durante estimulação cortical/supra-hióidea; ajustar posição e intensidade conforme tolerância.',
        'ajuste_seguranca': 'Respeitar os critérios de segurança em neuromodulação, garantir estabilidade postural cervical e proteção de via aérea durante toda a aplicação.',
        'fatores_moduladores': 'Risco de broncoaspiração, estado clínico agudo/subagudo, fadiga bulbar e uso de fármacos sedativos.',
    },
    'rm08_afasia': {
        'orientacao_tolerabilidade': 'Garantir rampa de subida e descida de 15 segundos na tDCS e hidratação salina adequada em áreas periauriculares ou frontais; monitorar cefaleia ou formigamento.',
        'ajuste_seguranca': 'Pacientes com compreensão limitada requerem observação direta e contínua de sinais não-verbais de desconforto cutâneo, tontura ou cefaleia.',
        'fatores_moduladores': 'Integridade cutânea sob os eletrodos, fadiga linguística e estabilidade medicamentosa.',
    },
    'rm09_afasia_rtms': {
        'orientacao_tolerabilidade': 'Avaliar desconforto no escalpo em alvos frontotemporais (F5/F6/CP5/CP6) onde há maior proximidade do músculo temporal; reduzir para 80% do LMR se houver espasmo facial doloroso.',
        'ajuste_seguranca': 'Respeitar rigorosamente os intervalos entre trens (10–15 s) e titular a intensidade conforme conforto sobre o músculo temporal.',
        'fatores_moduladores': 'Contração do músculo temporal, sensibilidade local à bobina e horário de menor fadiga cognitiva.',
    },
    'rm10_depressao': {
        'orientacao_tolerabilidade': 'Reduzir temporariamente a intensidade se houver intolerância álgica ou cefaleia nos primeiros dias de estímulo sobre F3/F4, titulando progressivamente até 100%–120% do LMR.',
        'ajuste_seguranca': 'Monitorar padrão do sono, irritabilidade ou sintomas de viragem maníaca (especialmente em protocolos TBS/acelerados); rever uso concomitante de benzodiazepínicos que atenuam a resposta.',
        'fatores_moduladores': 'Uso de benzodiazepínicos/anticonvulsivantes, privação de sono, uso estável de antidepressivos e jejum prolongado.',
    },
    'rm11_ansiedade': {
        'orientacao_tolerabilidade': 'Priorizar segurança de dose (ex.: cTBS limitado a 600 pulsos para evitar sobrecarga ou risco convulsivo descrito com cargas altas); monitorar cefaleia ou ansiedade aguda.',
        'ajuste_seguranca': 'Realizar 5 sessões/semana por 2–4 semanas e considerar desmame gradual para 3 a 2 sessões/semana; reduzir intensidade nos primeiros dias se houver intolerância.',
        'fatores_moduladores': 'Limiar convulsivo, privação de sono, uso de benzodiazepínicos e agitação autonômica aguda.',
    },
    'rm12_alzheimer': {
        'orientacao_tolerabilidade': 'Verificar sono da noite anterior, alimentação/jejum, medicações e eventos geradores de agitação antes de cada sessão; ajustar horário caso haja fenômeno de Sundowning.',
        'ajuste_seguranca': 'Em pacientes com linguagem prejudicada, vigiar ativamente sinais não-verbais de desconforto, agitação psicomotora ou confusão mental; reduzir pulsos pela metade ou reavaliar a cada 10 sessões.',
        'fatores_moduladores': 'Fenômeno de Sundowning, uso de benzodiazepínicos (reduzem efeito terapêutico) e estabilidade clínica.',
    },
    'rm13_alzheimer_tdcs': {
        'orientacao_tolerabilidade': 'Nunca posicionar eletrodos sobre áreas com lesões teciduais; utilizar rampa suave (15–30 s) e checar sono, jejum e agitação pré-sessão.',
        'ajuste_seguranca': 'Reavaliar a cada 10 sessões; em platô após boa resposta, iniciar desmame gradual (3x, 2x, 1x/semana, quinzenal e mensal); interromper se houver confusão mental ou alteração súbita de humor.',
        'fatores_moduladores': 'Benzodiazepínicos, horário de aplicação (evitar fim do dia se Sundowning) e comprometimento leve vs. moderado.',
    },
    'rm14_pc': {
        'orientacao_tolerabilidade': 'Em população pediátrica, adotar rampa de subida e descida padrão de 10 segundos na tDCS (ajustável para maior conforto sensorial) e monitorar irritabilidade, cefaleia ou fadiga.',
        'ajuste_seguranca': 'Triagem neurológica e EEG prévios se histórico de epilepsia/crises febris; protocolos acelerados (>1 sessão/dia) são contraindicados em crianças. Respeitar limite de ≤25 sessões e intervalo de 3–4 meses entre ciclos.',
        'fatores_moduladores': 'Estabilidade de anticonvulsivantes/psicofármacos, hipersensibilidade tátil/auditiva e pausa imediata diante de qualquer sinal neurológico agudo.',
    },
    'rm15_tea': {
        'orientacao_tolerabilidade': 'Monitorar aceitação tátil e auditiva ao posicionamento da bobina ou eletrodos em crianças/adolescentes com hipersensibilidade sensorial e manter vigilância de 24h pós-sessão; preferir tDCS em menores de 5–6 anos.',
        'ajuste_seguranca': 'Protocolos acelerados são contraindicados na faixa pediátrica; não ultrapassar 20 sessões por ciclo nem alterar psicofármacos durante a indução. Aguardar 3–4 meses entre ciclos e escalonar redução/espaçamento se intensificação de sintomas.',
        'fatores_moduladores': 'Comorbidade epiléptica (exige EEG e estabilidade neurológica), hipersensibilidade sensorial e vigilância comportamental por 24 horas.',
    },
    'rm16_ataxia': {
        'orientacao_tolerabilidade': 'Vigiar desconforto cervical/occipital, tontura e nível de fadiga durante a estimulação cerebelar (adaptar ou pausar se fadiga acentuada).',
        'ajuste_seguranca': 'Reavaliar resposta semanalmente e checar interação com fármacos como benzodiazepínicos, que reduzem os efeitos da estimulação.',
        'fatores_moduladores': 'Uso de benzodiazepínicos/miorrelaxantes, fadiga cerebelar e posicionamento estável sobre hemisférios cerebelares.',
    },
    'rm17_parkinson': {
        'orientacao_tolerabilidade': 'Cefaleia é o efeito adverso mais frequente; aplicar os protocolos preferencialmente no estado medicamentoso ON e observar orientações de segurança (&) dos parâmetros.',
        'ajuste_seguranca': 'Utilizar bobina circular para alvos motores de membro inferior e área motora suplementar; reavaliar semanalmente e indicar ciclo de manutenção quando atingir platô.',
        'fatores_moduladores': 'Estado ON/OFF da levodopa, discinesia induzida por levodopa e uso de benzodiazepínicos.',
    },
    'rm17_parkinson_fog': {
        'orientacao_tolerabilidade': 'Aplicar sempre no estado medicamentoso ON para melhor resposta funcional de marcha e congelamento; monitorar cefaleia leve ou tontura pós-sessão.',
        'ajuste_seguranca': 'Priorizar protocolos específicos de congelamento/discinesia quando presentes e reavaliar semanalmente com testes funcionais padronizados.',
        'fatores_moduladores': 'Flutuações motoras de levodopa, risco de queda durante o congelamento de marcha e sedativos/benzodiazepínicos.',
    },
    'rm05_dor': {
        'orientacao_tolerabilidade': 'Na presença de alodinia mecânica, preferir ou associar rPMS periférica pois dispensa contato direto da bobina na pele. Reduzir inicialmente a intensidade se desconforto local.',
        'ajuste_seguranca': 'Considerar melhora em alterações sensoriais (alodinia, hiperalgesia, hiperpatia), sono e humor além da intensidade bruta na EVA.',
        'fatores_moduladores': 'Alodinia cutânea, uso de opioides/gabapentinoides/antidepressivos e qualidade do sono.',
    },
    'rm18_tept': {
        'orientacao_tolerabilidade': 'Reduzir a intensidade da estimulação caso haja intolerância nos primeiros dias e monitorar qualidade do sono, hipervigilância ou cefaleia após estimulação no DLPFC direito/medial.',
        'ajuste_seguranca': 'Aplicar checklist pré-sessão de segurança (rastreador de convulsão/medicamentos/sono) e evitar estímulos desencadeadores excessivos caso surja agitação aguda.',
        'fatores_moduladores': 'Qualidade do sono, psicofármacos concomitantes (benzodiazepínicos reduzem eficácia) e estabilidade clínica de sintomas dissociativos.',
    },
}


def detect_abstract_signals(abstract_text):
    text = (abstract_text or '').lower()
    signals = []
    if 'prisma' in text:
        signals.append('PRISMA')
    if 'prospero' in text or 'crd420' in text or 'inplasy' in text:
        signals.append('Protocolo registrado')
    if 'risk of bias' in text or 'rob ' in text or 'rob 2' in text or 'pedro' in text or 'cochrane' in text:
        signals.append('Avaliação de risco de viés')
    if 'i2' in text or 'i²' in text or 'i square' in text or 'heterogene' in text:
        signals.append('Análise de heterogeneidade')
    if 'publication bias' in text or 'funnel' in text or 'egger' in text:
        signals.append('Viés de publicação avaliado')
    if 'grade' in text or 'certainty' in text:
        signals.append('GRADE / Certeza relatados')
    return signals


def format_authors(raw_authors, fallback=''):
    if not raw_authors:
        return fallback
    return raw_authors


def _build_audit_entry_from_meta(cid, fator_id, m, catalog):
    meta = m.get('audit_meta') or {}
    ma = dict(m.get('meta_analise') or {})
    doi = ma.get('doi', '')
    paper = catalog.get(doi) if doi else None
    signals = detect_abstract_signals(paper.get('abstract', '')) if paper else list(meta.get('amstar2_sinais') or [])
    if not signals and meta.get('amstar2_sinais'):
        signals = list(meta['amstar2_sinais'])
    cert_name = meta.get('grade_certeza', 'Baixa')
    forca = meta.get('grade_forca', 'Condicional')
    resumo = meta.get('amstar2_resumo') or (
        ' · '.join(signals) if signals else 'Revisão sistemática com metanálise verificada via DOI'
    )
    return {
        'condicao_id': cid,
        'fator_id': fator_id,
        'meta_analise': {
            'autores': (
                format_authors(paper.get('authors'), ma.get('autores', ''))
                if paper
                else ma.get('autores', '')
            ),
            'ano': (paper.get('year') if paper else None) or ma.get('ano'),
            'titulo': (paper.get('title') if paper else None) or ma.get('titulo', ''),
            'periodico': (paper.get('journal') if paper else None) or ma.get('periodico', ''),
            'doi': doi,
            'url_doi': ma.get('url_doi') or (f'https://doi.org/{doi}' if doi else ''),
            'amstar2': {
                'instrumento': 'AMSTAR 2 (Shea et al., 2017 — Avaliação crítica de revisões sistemáticas)',
                'nivel': meta.get('amstar2_nivel', 'Moderada'),
                'resumo_criterio': resumo,
                'justificativa_preliminar': meta.get('amstar2_justificativa', resumo),
                'sinais_metodologicos': signals,
                'status_homologacao': STATUS_HOMOLOGACAO,
            },
        },
        'grade': {
            'certeza': cert_name,
            'simbolos': GRADE_SYMBOLS[cert_name],
            'forca_recomendacao': forca,
            'observacao_dominios': meta.get('grade_dominios', ''),
            'status_homologacao': STATUS_HOMOLOGACAO,
        },
        'tolerabilidade_roadmap': dict(meta.get('tolerabilidade') or {}),
    }


def main():
    with open(CATALOG_FILE, 'r', encoding='utf-8') as f:
        catalog = json.load(f)
    with open(ROADMAPS_FILE, 'r', encoding='utf-8') as f:
        roadmaps = json.load(f)

    audit_entries = {}
    missing_catalog = []
    unmapped_pairs = []

    for c in roadmaps.get('condicoes', []):
        cid = c['id']
        for fator_id, m in c.get('modalidades', {}).items():
            pair_key = f'{cid}::{fator_id}'
            if m.get('audit_meta'):
                entry = _build_audit_entry_from_meta(cid, fator_id, m, catalog)
            else:
                cfg = PAIR_AUDIT_CONFIG.get((cid, fator_id))
                if not cfg:
                    unmapped_pairs.append(pair_key)
                    continue
                doi = cfg['doi']
                paper = catalog.get(doi)
                if not paper:
                    missing_catalog.append(f'{pair_key} -> {doi}')
                    continue
                signals = detect_abstract_signals(paper.get('abstract', ''))
                amstar_cfg = cfg['amstar2']
                grade_cfg = cfg['grade']
                tol_cfg = TOLERABILITY_PROFILES[cfg['tol_key']]
                criterio_resumo = ' · '.join(signals) if signals else 'Revisão sistemática com metanálise verificada via DOI'
                cert_name = grade_cfg['certeza']
                entry = {
                    'condicao_id': cid,
                    'fator_id': fator_id,
                    'meta_analise': {
                        'autores': format_authors(paper.get('authors'), m.get('meta_analise', {}).get('autores', '')),
                        'ano': paper.get('year') or m.get('meta_analise', {}).get('ano'),
                        'titulo': paper.get('title'),
                        'periodico': paper.get('journal', ''),
                        'doi': doi,
                        'url_doi': f'https://doi.org/{doi}',
                        'amstar2': {
                            'instrumento': 'AMSTAR 2 (Shea et al., 2017 — Avaliação crítica de revisões sistemáticas)',
                            'nivel': amstar_cfg['nivel'],
                            'resumo_criterio': criterio_resumo,
                            'justificativa_preliminar': amstar_cfg['justificativa'],
                            'sinais_metodologicos': signals,
                            'status_homologacao': STATUS_HOMOLOGACAO,
                        },
                    },
                    'grade': {
                        'certeza': cert_name,
                        'simbolos': GRADE_SYMBOLS[cert_name],
                        'forca_recomendacao': grade_cfg['forca'],
                        'observacao_dominios': grade_cfg['dominios'],
                        'status_homologacao': STATUS_HOMOLOGACAO,
                    },
                    'tolerabilidade_roadmap': tol_cfg,
                }

            audit_entries[pair_key] = entry
            if isinstance(m.get('meta_analise'), dict):
                m['meta_analise']['amstar2'] = entry['meta_analise']['amstar2']
            m['grade'] = entry['grade']
            m['tolerabilidade_roadmap'] = entry['tolerabilidade_roadmap']

    if missing_catalog:
        raise RuntimeError(f'DOIs ausentes no catálogo verificado: {missing_catalog}')
    if unmapped_pairs:
        raise RuntimeError(f'Pares condição/fator sem mapeamento de auditoria: {unmapped_pairs}')

    output_payload = {
        'versao_auditoria': '2026-11-17-v2',
        'status_geral': STATUS_HOMOLOGACAO,
        'total_pares_auditados': len(audit_entries),
        'distribuicao_amstar2': {},
        'distribuicao_grade': {},
        'pares': audit_entries,
    }

    for entry in audit_entries.values():
        a_lvl = entry['meta_analise']['amstar2']['nivel']
        g_lvl = entry['grade']['certeza']
        output_payload['distribuicao_amstar2'][a_lvl] = output_payload['distribuicao_amstar2'].get(a_lvl, 0) + 1
        output_payload['distribuicao_grade'][g_lvl] = output_payload['distribuicao_grade'].get(g_lvl, 0) + 1

    with open(OUT_AUDIT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)

    with open(ROADMAPS_FILE, 'w', encoding='utf-8') as f:
        json.dump(roadmaps, f, ensure_ascii=False, indent=2)

    js_target = os.path.join(BASE_DIR, 'js', 'data.js')
    with open(js_target, 'w', encoding='utf-8') as f:
        f.write('// Rede NAPeN — Base de Dados dos Roadmaps Clínicos (Auto-gerada)\n')
        f.write('// Integrada com os 18 roadmaps oficiais (RM01-RM18) e auditoria GRADE/AMSTAR 2\n')
        f.write('window.NAPEN_DATA = ')
        json.dump(roadmaps, f, ensure_ascii=False, indent=2)
        f.write(';\n')

    print(f'✓ Auditoria GRADE & AMSTAR 2 salva em {OUT_AUDIT_FILE}')
    print(f'  Total de pares auditados: {len(audit_entries)}')
    print(f'  AMSTAR 2: {output_payload["distribuicao_amstar2"]}')
    print(f'  GRADE: {output_payload["distribuicao_grade"]}')


if __name__ == '__main__':
    main()
