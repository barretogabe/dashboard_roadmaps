#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Enriquecimento de Tags de Busca, Sistema 10-20 e Sinônimos em Inglês
Adiciona o campo 'tags_busca' estruturado para cada condição clínica no JSON,
garantindo indexação neuroanatômica e semântica completa.
"""

import json
import os

TAGS_MAP = {
    "avc-membro-superior": {
        "coordenadas_10_20": ["C3", "C4", "M1"],
        "alvos_anatomicos": ["Córtex Motor Primário", "M1", "Área Motora da Mão", "Representação Corticomotora do Membro Superior"],
        "sinonimos_en": ["stroke", "spasticity", "upper extremity", "upper limb", "hand motor function", "hemiparesis", "arm recovery", "motor impairment"],
        "sintomas_pt": ["paralisia", "hemiparesia", "membro superior", "braço", "mão", "preensão", "destreza", "espasticidade", "tônus"],
        "escalas": ["FMA-UE", "Fugl-Meyer", "EAM", "Ashworth", "9HPT"],
        "tecnicas": ["rTMS", "HF-rTMS", "LF-rTMS", "iTBS", "cTBS", "tDCS", "tDCS Anódica", "tDCS Catódica"]
    },
    "avc-mobilidade": {
        "coordenadas_10_20": ["Cz", "C3", "C4", "M1 Perna"],
        "alvos_anatomicos": ["Área Motora Suplementar (SMA)", "M1 Área de Membro Inferior", "Vértice Craniano (Cz)"],
        "sinonimos_en": ["stroke", "spasticity", "gait", "mobility", "walking speed", "balance", "falls risk", "lower limb", "locomotion"],
        "sintomas_pt": ["marcha", "mobilidade", "equilíbrio", "quedas", "passo", "velocidade de caminhada", "deambulação"],
        "escalas": ["BBS", "Berg", "TUG", "TC10m", "10MWT", "EAM"],
        "tecnicas": ["rTMS", "HF-rTMS", "iTBS", "tDCS", "tDCS Anódica"]
    },
    "avc-afasia": {
        "coordenadas_10_20": ["F7", "F5", "F3", "T3", "CP6", "T4"],
        "alvos_anatomicos": ["Área de Broca", "Giro Frontal Inferior", "Área de Wernicke", "Giro Temporal Superior"],
        "sinonimos_en": ["stroke", "aphasia", "broca aphasia", "non-fluent aphasia", "language rehabilitation", "naming deficit", "anomia"],
        "sintomas_pt": ["afasia", "linguagem", "fala", "anomia", "dificuldade de nomeação", "compreensão oral", "expressão verbal"],
        "escalas": ["BNT", "Boston Naming Test", "WAB", "WAB-R", "Token"],
        "tecnicas": ["LF-rTMS", "HF-rTMS", "iTBS", "tDCS Anódica", "tDCS Catódica"]
    },
    "avc-disfagia": {
        "coordenadas_10_20": ["C3", "C4", "M1 Deglutição"],
        "alvos_anatomicos": ["Córtex Motor da Deglutição", "Representação Cortical Faríngea", "Área Faríngea Bilateral"],
        "sinonimos_en": ["stroke", "dysphagia", "swallowing disorder", "aspiration", "pharyngeal cortex"],
        "sintomas_pt": ["disfagia", "deglutição", "engasgo", "aspiração", "alimentação oral", "sonda enteral"],
        "escalas": ["FOIS", "DOSS", "FEDSS"],
        "tecnicas": ["HF-rTMS", "tDCS Anódica", "PES"]
    },
    "doenca-parkinson": {
        "coordenadas_10_20": ["C3", "C4", "Cz", "F3", "M1", "SMA", "DLPFC"],
        "alvos_anatomicos": ["Córtex Motor Primário (M1)", "Área Motora Suplementar (SMA)", "Córtex Pré-Frontal Dorsolateral (DLPFC)"],
        "sinonimos_en": ["parkinson", "parkinson's disease", "pd", "freezing of gait", "fog", "bradykinesia", "rigidity", "tremor", "motor symptoms"],
        "sintomas_pt": ["parkinson", "rigidez", "tremor", "bradicinesia", "congelamento da marcha", "fog", "hesitação", "instabilidade"],
        "escalas": ["MDS-UPDRS-III", "UPDRS", "FOGQ", "TUG", "TC10m"],
        "tecnicas": ["HF-rTMS", "iTBS", "tDCS Anódica"]
    },
    "depressao-maior": {
        "coordenadas_10_20": ["F3", "F4", "DLPFC"],
        "alvos_anatomicos": ["Córtex Pré-Frontal Dorsolateral Esquerdo (DLPFC Esquerdo)", "DLPFC Direito"],
        "sinonimos_en": ["depression", "major depressive disorder", "mdd", "treatment-resistant depression", "saint protocol", "anhedonia"],
        "sintomas_pt": ["depressão", "tristeza", "anedonia", "desânimo", "culpa", "insônia", "fadiga", "humor deprimido"],
        "escalas": ["HAM-D 17", "HDRS", "MADRS", "BDI"],
        "tecnicas": ["HF-rTMS 10Hz", "iTBS", "Protocolo SAINT / Stanford", "LF-rTMS 1Hz", "tDCS Anódica"]
    },
    "ansiedade-generalizada": {
        "coordenadas_10_20": ["F4", "F3", "DLPFC"],
        "alvos_anatomicos": ["Córtex Pré-Frontal Dorsolateral Direito (DLPFC Direito)"],
        "sinonimos_en": ["anxiety", "generalized anxiety disorder", "gad", "panic", "worry", "hyperarousal"],
        "sintomas_pt": ["ansiedade", "tag", "tensão", "preocupação", "nervosismo", "apreensão", "medo", "insônia"],
        "escalas": ["HAM-A", "HAMA", "BAI", "GAD-7"],
        "tecnicas": ["LF-rTMS 1Hz", "tDCS Catódica", "iTBS"]
    },
    "tept": {
        "coordenadas_10_20": ["F4", "F3", "DLPFC"],
        "alvos_anatomicos": ["Córtex Pré-Frontal Dorsolateral Direito (DLPFC Direito)", "DLPFC Bilateral"],
        "sinonimos_en": ["ptsd", "posttraumatic stress disorder", "trauma", "flashback", "hyperarousal", "nightmares"],
        "sintomas_pt": ["estresse pós-traumático", "tept", "trauma", "flashbacks", "pesadelos", "hipervigilância", "esquiva"],
        "escalas": ["PCL-5", "CAPS-5", "HAM-A"],
        "tecnicas": ["LF-rTMS 1Hz", "HF-rTMS", "tDCS Anódica / Catódica"]
    },
    "dor-neuropatica": {
        "coordenadas_10_20": ["C3", "C4", "M1"],
        "alvos_anatomicos": ["Córtex Motor Primário (M1)", "Representação Somatotópica da Área Dolorosa em M1"],
        "sinonimos_en": ["pain", "neuropathic pain", "chronic pain", "thalamic pain", "central pain", "fibromyalgia", "allodynia"],
        "sintomas_pt": ["dor", "dor neuropática", "queimação", "choque", "formigamento", "alodínia", "fibromialgia", "analgesia"],
        "escalas": ["EVA", "VAS", "DN4", "LANSS"],
        "tecnicas": ["HF-rTMS 10Hz", "HF-rTMS 20Hz", "tDCS Anódica M1"]
    },
    "ataxia-cerebelar": {
        "coordenadas_10_20": ["Inion", "Cerebelo", "Vermis"],
        "alvos_anatomicos": ["Córtex Cerebelar Bilateral", "Hemisférios Cerebelares", "Vermis Cerebelar"],
        "sinonimos_en": ["ataxia", "spinocerebellar ataxia", "sca", "cerebellar ataxia", "incoordination", "dysmetria", "cerebellum"],
        "sintomas_pt": ["ataxia", "incoordenação", "dismetria", "desequilíbrio", "disdiadococinesia", "disartria", "marcha ébria"],
        "escalas": ["SARA", "BBS", "Berg", "9HPT", "ICARS"],
        "tecnicas": ["tDCS Anódica Cerebelar", "rTMS Cerebelar", "iTBS"]
    },
    "paralisia-cerebral": {
        "coordenadas_10_20": ["C3", "C4", "M1"],
        "alvos_anatomicos": ["Córtex Motor Primário (M1)", "Hemisfério Mais Acometido em M1"],
        "sinonimos_en": ["cerebral palsy", "cp", "spastic diplegia", "hemiplegic cp", "pediatric motor rehabilitation"],
        "sintomas_pt": ["paralisia cerebral", "pc", "diparesia", "hemiparesia espástica", "função motora", "criança", "pediatria"],
        "escalas": ["GMFM", "GMFM-66", "GMFM-88", "EAM", "Ashworth"],
        "tecnicas": ["tDCS Anódica M1", "rTMS"]
    },
    "transtorno-espectro-autista": {
        "coordenadas_10_20": ["F3", "F4", "DLPFC"],
        "alvos_anatomicos": ["Córtex Pré-Frontal Dorsolateral (DLPFC)", "DLPFC Bilateral"],
        "sinonimos_en": ["autism", "autism spectrum disorder", "asd", "social communication", "repetitive behavior", "irritability"],
        "sintomas_pt": ["autismo", "tea", "irritabilidade", "agressividade", "comunicação social", "estereotipias", "interação"],
        "escalas": ["ABC", "ABC-I", "SRS-2", "ATEC"],
        "tecnicas": ["LF-rTMS 1Hz", "tDCS Anódica DLPFC", "iTBS"]
    },
    "alzheimer-ccl": {
        "coordenadas_10_20": ["F3", "F4", "Precúneo", "DLPFC"],
        "alvos_anatomicos": ["Córtex Pré-Frontal Dorsolateral (DLPFC)", "DLPFC Bilateral", "Precúneo"],
        "sinonimos_en": ["alzheimer", "alzheimer's disease", "ad", "mild cognitive impairment", "mci", "dementia", "memory deficit", "cognition"],
        "sintomas_pt": ["alzheimer", "demência", "ccl", "declínio cognitivo", "memória", "esquecimento", "orientação"],
        "escalas": ["MEEM", "MMSE", "ADAS-Cog", "NPI"],
        "tecnicas": ["HF-rTMS 20Hz", "iTBS", "tACS 40Hz Gamma", "tDCS Anódica DLPFC"]
    }
}

def enrich():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'data', 'napen_roadmaps_data.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for c in data['condicoes']:
        cid = c['id']
        if cid in TAGS_MAP:
            c['tags_busca'] = TAGS_MAP[cid]
            
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Base de dados enriquecida com tags_busca completas: {json_path}")
    
    # Executa atualizar_base.py para manter sincronia
    from atualizar_base import sincronizar_arquivos
    sincronizar_arquivos(data, base_dir)

if __name__ == '__main__':
    enrich()
