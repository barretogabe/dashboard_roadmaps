"""
Script de consolidação da base de dados dos Roadmaps NAPeN.
Unifica as 26 linhas legadas parametrizadas com os dados dos 18 roadmaps da base relacional,
ancorando as métricas nas escalas recomendadas, laços condicionais e protocolos alternativos.
"""
import os, json, csv

real = os.path.realpath('Dashboard NAPeN - Roadmaps 2026-2027')
trans_dir = os.path.join(real, 'Dados dos roadmaps transcritos')
relational_json = os.path.join(trans_dir, 'NAPeN_Base_Relacional_JSON_2026-11-03.json')
atlas_dir = os.path.join(trans_dir, 'NAPeN_Roadmaps_Atlas_Digital_COMPLETO')
legado_csv = os.path.join(atlas_dir, 'csv', 'legado.csv')

# Load relational json
with open(relational_json, 'r', encoding='utf-8') as f:
    rel_data = json.load(f)

# Extract audit and reference tables
roadmaps_meta = {r[0]: {'condicao': r[1], 'foco': r[2], 'tecnica': r[3]} for r in rel_data['tables'][1]['rows']}
audit_map = {r[0]: {'ocr': r[6], 'status_conexoes': r[7], 'revisao': r[8], 'pendencias': r[11]} for r in rel_data['tables'][14]['rows']}

# Canonical conditions definition
conditions = [
    {
        "id": "avc-membro-superior",
        "condicao": "Acidente Vascular Cerebral (AVC) — Membro Superior",
        "eixo": "Doenças Cerebrovasculares (AVC)",
        "roadmap_id": "RM01",
        "svg_file": "RM01.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Versão consolidada a partir de ensaios clínicos randomizados e metanálises de recuperação motora pós-AVC.",
        "no1_pergunta": "Qual é o principal fator limitante do membro superior?",
        "fatores_limitantes": [
            {"id": "espasticidade", "label": "Espasticidade (Flexores de punho/cotovelo)"},
            {"id": "fraqueza", "label": "Fraqueza Muscular (Músculos fracos)"},
            {"id": "dor", "label": "Dor Limitante no Membro Superior"},
            {"id": "sensorial", "label": "Déficit Sensorial Somatossensorial"},
            {"id": "negligencia", "label": "Heminegligência Visuoespacial"}
        ],
        "modalidades": {
            "espasticidade": {
                "tecnica": "rPMS (Estimulação Magnética Periférica)",
                "modalidade_sigla": "rPMS",
                "alvo": "Nervo periférico / Músculos flexores espásticos (punho/cotovelo)",
                "frequencia": "50 Hz contínuo (repetição 5 Hz)",
                "intensidade": "Intensidade suficiente para induzir contração muscular visível sem dor",
                "pulsos_duracao": "600 pulsos por grupo muscular (modo contínuo sem pausas)",
                "sessoes": "10 a 15 sessões diárias associadas à fisioterapia cinesioterapêutica",
                "escala_recomendada": "Escala de Ashworth Modificada (EAM)",
                "meta_melhora": "Redução de pelo menos 1 nível na EAM para flexores de punho e dedos",
                "tamanho_efeito": "Diminuição de 1 ponto (IC 95% 0,5 a 1,5) na EAM após 10 sessões combinadas com terapia motora",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível B (Eficácia Provável na redução de hipertonia)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo 1 (rTMS Inibitória Contralesional)",
                    "tecnica": "rTMS 1 Hz",
                    "alvo": "Córtex Motor Primário (M1) contralesional (hemisfério não afetado)",
                    "parametros": "1 Hz, 90% a 100% do LMR, 1.200 pulsos contínuos (20 min)",
                    "observacoes": "Indicado quando persistir hiper-reatividade e inibição inter-hemisférica anômala. Reavaliação semanal da excitabilidade cortical."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar após o 5º dia consecutivo de estimulação motora.",
                    "ajuste_dose": "Se resposta parcial, recalibrar o ponto de aplicação periférico ou titular tempo de trem para 800 pulsos.",
                    "regra_interrupcao": "Interromper o ciclo de indução se após 2 ajustes sucessivos não for observada variação na amplitude articular ou EAM."
                },
                "contraindicacoes": ["Implantes metálicos na área de estimulação", "Trombose venosa profunda no membro", "Fratura óssea instável recente"],
                "notas_clinicas": "A estimulação magnética periférica contínua reduz a hipertonia e facilita o ganho funcional nas sessões de terapia ocupacional subsequentes."
            },
            "fraqueza": {
                "tecnica": "rPMS Intermitente + rTMS Excitatória",
                "modalidade_sigla": "rPMS / rTMS",
                "alvo": "M1 ipsilesional (área do punho/mão) e musculatura extensora do membro",
                "frequencia": "50 Hz (trens intermitentes de 2s com 8s de pausa)",
                "intensidade": "80% a 90% do LMR na rTMS / contração motora na rPMS",
                "pulsos_duracao": "600 pulsos por músculo (extensores do punho e deltoide)",
                "sessoes": "10 a 20 sessões diárias, aplicando cinesioterapia imediatamente após",
                "escala_recomendada": "Escala Fugl-Meyer de Avaliação Motora (FMA-UE)",
                "meta_melhora": "Ganho clinicamente importante ≥ 6,6 pontos na FMA-UE",
                "tamanho_efeito": "Aumento de 6,6 a 23,3 pontos (IC 95% 4,1 a 9,1) na escala FMA-UE após 10–15 sessões",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível A (Eficácia Estabelecida na fase subaguda 2 semanas a 6 meses)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo 2 (iTBS Intermitente Acelerado)",
                    "tecnica": "iTBS (Theta Burst Intermitente)",
                    "alvo": "M1 ipsilesional (representação da mão)",
                    "parametros": "iTBS 50 Hz em tripletos a 5 Hz, 600 pulsos (3 min), 70% a 80% do LMR",
                    "observacoes": "Opção com alta eficiência de tempo para pacientes com fadiga motora rápida. Pode ser repetido 2x/dia com intervalo de 15 min."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar pontuação na FMA-UE ao final de 10 sessões.",
                    "ajuste_dose": "Recalibrar o Limiar Motor de Repouso (LMR) no hemisfério lesado antes de cada ajuste de intensidade.",
                    "regra_interrupcao": "Interromper se houver ausência completa de resposta após 10 sessões associadas ao treino de tarefas motoras."
                },
                "contraindicacoes": ["Clips metálicos de aneurisma", "Implante coclear", "Histórico de crises epilépticas pós-AVC não controladas"],
                "notas_clinicas": "A fase ideal para resposta máxima situa-se entre 1 e 6 meses após o ictus isquêmico ou hemorrágico."
            },
            "dor": {
                "tecnica": "rTMS Excitatória (Alta Frequência)",
                "modalidade_sigla": "rTMS",
                "alvo": "Córtex Motor Primário (M1) contralateral à dor (área não infartada)",
                "frequencia": "10 Hz a 20 Hz",
                "intensidade": "80% a 90% do LMR",
                "pulsos_duracao": "2.000 a 3.000 pulsos totais por sessão (trens de 5s / intervalo 25s)",
                "sessoes": "10 a 15 sessões iniciais diárias; manutenção quinzenal ou mensal",
                "escala_recomendada": "Escala Visual Analógica de Dor (EVA) e DN4",
                "meta_melhora": "Redução ≥ 30% na intensidade da dor na escala EVA",
                "tamanho_efeito": "Redução média de 24% a 36% na escala EVA de dor crônica pós-AVC",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível A (Eficácia Estabelecida para dor central pós-AVC)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Anodal sobre M1)",
                    "tecnica": "tDCS (Corrente Contínua)",
                    "alvo": "Ânodo sobre M1 contralateral à dor / Cátodo supraorbitário contralateral",
                    "parametros": "2.0 mA, 20 minutos, eletrodos de 35 cm² embebidos em solução salina",
                    "observacoes": "Opção com excelente tolerabilidade, indicada caso o paciente apresente desconforto ou cefaleia induzida pela rTMS."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Avaliar após a 5ª e 10ª sessão com diário de dor.",
                    "ajuste_dose": "Ajustar intensidade em 5% acima do LMR se dor não reduzir pelo menos 1 ponto na EVA.",
                    "regra_interrupcao": "Se após 10 sessões não houver alívio de dor, considerar refratariedade e investigar síndrome dolorosa miofascial concomitante."
                },
                "contraindicacoes": ["Placas cranianas metálicas próximas à bobina", "Marca-passo cardíaco"],
                "notas_clinicas": "A estimulação do córtex motor induz alívio da dor talâmica e central por vias talamocorticais descendentes."
            },
            "sensorial": {
                "tecnica": "tDCS Bi-hemisférica / rTMS Sensorial",
                "modalidade_sigla": "tDCS",
                "alvo": "Córtex Somatossensorial Primário (S1)",
                "frequencia": "Corrente Contínua (tDCS) ou 10 Hz (rTMS)",
                "intensidade": "2.0 mA (tDCS) ou 90% LMR (rTMS)",
                "pulsos_duracao": "20 minutos por sessão",
                "sessoes": "10 sessões combinadas com estimulação tátil e proprioceptiva",
                "escala_recomendada": "Revised Nottingham Sensory Assessment (rNSA)",
                "meta_melhora": "Ganho significativo no escore rNSA tátil e proprioceptivo",
                "tamanho_efeito": "Aumento médio de 4,5 pontos (IC 95% 2,5 a 6,5) na rNSA após 10 sessões",
                "evidencia": "Emergente (Estudos Controlados sem meta-análise definitiva)",
                "linha_fluxograma": "pontilhada",
                "diretriz_internacional": "Consenso NAPeN: Nível C / Estudo de intervenção",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (Estimulação Periférica Sensorial Pareada)",
                    "tecnica": "rPMS / TENS em baixa intensidade",
                    "alvo": "Dermátomos e nervos periféricos do antebraço",
                    "parametros": "Estimulação sensorial pareada com treino discriminativo de textura",
                    "observacoes": "Aplicar durante tarefas ativas de reconhecimento cego de objetos (estereognosia)."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Avaliar na 10ª sessão.",
                    "ajuste_dose": "Modificar posição dos eletrodos em 1 cm caso haja dormência excessiva sob o eletrodo.",
                    "regra_interrupcao": "Interromper se ausência de resposta somatossensorial após 10 sessões."
                },
                "contraindicacoes": ["Lesões de pele no couro cabeludo", "Implantes intracranianos"],
                "notas_clinicas": "O ganho sensorial frequentemente destrava o uso funcional da mão parética na vida diária."
            },
            "negligencia": {
                "tecnica": "tDCS Parietal / rTMS Posterior",
                "modalidade_sigla": "tDCS",
                "alvo": "Córtex Parietal Posterior (P4/P3 ou P6/FP1)",
                "frequencia": "Corrente contínua (tDCS)",
                "intensidade": "1.0 a 2.0 mA",
                "pulsos_duracao": "20 a 30 minutos",
                "sessoes": "10 sessões diárias combinadas com treino de exploração visual",
                "escala_recomendada": "Behavioural Inattention Test (BIT) / Teste de Cancelamento de Estrelas",
                "meta_melhora": "Ganho clinicamente significativo no teste BIT e cancelamento de linhas",
                "tamanho_efeito": "Aumento de até 19 pontos no BIT e melhora de 10,4 a 16,4 pontos no cancelamento de estrelas",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível B (Eficácia Provável na negligência hemiespacial)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (cTBS Inibitório no Córtex Parietal Esquerdo)",
                    "tecnica": "cTBS Contínuo",
                    "alvo": "P3 (Córtex Parietal Esquerdo não afetado)",
                    "parametros": "600 pulsos contínuos (40s), 80% do LMR",
                    "observacoes": "Restaura o equilíbrio de atenção inter-hemisférica inibindo o hemisfério esquerdo hiperativo."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Ao término da 5ª sessão com o teste de bissecção de linhas.",
                    "ajuste_dose": "Associar biofeedback visual e prismas ópticos se evolução for lenta.",
                    "regra_interrupcao": "Interromper se não houver melhora na exploração hemiespacial em 10 dias."
                },
                "contraindicacoes": ["Metal no crânio", "Crises convulsivas ativas"],
                "notas_clinicas": "A correção da heminegligência é mandatória antes de iniciar treino intensivo de marcha por segurança."
            }
        }
    },
    {
        "id": "avc-mobilidade",
        "condicao": "Acidente Vascular Cerebral (AVC) — Mobilidade e Marcha",
        "eixo": "Doenças Cerebrovasculares (AVC)",
        "roadmap_id": "RM03",
        "svg_file": "RM03.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Diretrizes baseadas em ensaios com avaliação de marcha e equilíbrio estático/dinâmico.",
        "no1_pergunta": "Qual é a principal limitação funcional de mobilidade?",
        "fatores_limitantes": [
            {"id": "equilibrio", "label": "Equilíbrio Estático e Dinâmico (Instabilidade / Quedas)"},
            {"id": "velocidade_marcha", "label": "Velocidade da Marcha / Cadência Lenta"}
        ],
        "modalidades": {
            "equilibrio": {
                "tecnica": "rTMS / iTBS sobre M1 Bilateral ou Cerebelo",
                "modalidade_sigla": "rTMS (iTBS)",
                "alvo": "M1 (representação do membro inferior / tronco) ou Córtex Pré-frontal (F5)",
                "frequencia": "50 Hz iTBS (ou 10 Hz convencional)",
                "intensidade": "80% do LMR",
                "pulsos_duracao": "600 a 1.200 pulsos totais por sessão",
                "sessoes": "10 a 20 sessões (2x ao dia com intervalo de 15 min ou 1x/dia)",
                "escala_recomendada": "Escala de Equilíbrio de Berg (BBS)",
                "meta_melhora": "Aumento clinicamente relevante na pontuação BBS",
                "tamanho_efeito": "Aumento médio de 8,9 a 11,06 pontos na Escala de Berg após 10 a 20 sessões",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur: Nível B / Consenso NAPeN",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Anodal sobre M1 Membro Inferior)",
                    "tecnica": "tDCS 2 mA",
                    "alvo": "Cz ou M1 da perna lesada",
                    "parametros": "2.0 mA, 20 minutos, com treino de equilíbrio em plataforma",
                    "observacoes": "Facilita o aprendizado motor com baixo custo e boa tolerabilidade."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar semanalmente com o teste Berg.",
                    "ajuste_dose": "Ajustar alinhamento da bobina dupla em D (cone de foco profundo) para atingir M1 de membros inferiores.",
                    "regra_interrupcao": "Interromper indução quando não houver melhora clínica quantitativa após 10 sessões."
                },
                "contraindicacoes": ["Implantes metálicos cranianos", "Hipotensão postural grave"],
                "notas_clinicas": "Sempre aplicar a estimulação imediatamente antes da sessão de fisioterapia neurofuncional."
            },
            "velocidade_marcha": {
                "tecnica": "rTMS de Alta Frequência / iTBS",
                "modalidade_sigla": "rTMS",
                "alvo": "M1 lesado (área da perna) / Córtex Motor Primário",
                "frequencia": "10 Hz excitatória",
                "intensidade": "90% a 100% LMR",
                "pulsos_duracao": "1.500 a 2.000 pulsos",
                "sessoes": "10 a 15 sessões diárias",
                "escala_recomendada": "Teste de Caminhada de 10 Metros (TC10m)",
                "meta_melhora": "Redução clinicamente significativa no tempo do TC10m",
                "tamanho_efeito": "Redução média de 4,4 segundos (IC 95% -8,22 a 17,16) no tempo de caminhada de 10 metros",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Consenso NAPeN / Metanálises 2023",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (rPMS em Tríceps Sural / Tibial Anterior)",
                    "tecnica": "rPMS Periférico",
                    "alvo": "Nervo fibular comum e ventre do tibial anterior",
                    "parametros": "20 Hz, contração visível durante treino de dorsiflexão",
                    "observacoes": "Indicado especificamente para pé caído ou déficit de desobstrução do solo durante a fase de balanço da marcha."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar com cronômetro a cada 5 sessões.",
                    "ajuste_dose": "Aumentar número de pulsos de 1.500 para 2.000 se tolerado.",
                    "regra_interrupcao": "Se persistir sem resposta após ajustes, direcionar foco para fortalecimento com órteses."
                },
                "contraindicacoes": ["Instabilidade cardiovascular aguda", "Uso de próteses metálicas no membro"],
                "notas_clinicas": "Recomenda-se associar treino de marcha em esteira com suporte de peso parcial quando disponível."
            }
        }
    },
    {
        "id": "avc-afasia",
        "condicao": "Acidente Vascular Cerebral (AVC) — Afasia de Expressão e Compreensão",
        "eixo": "Doenças Cerebrovasculares (AVC)",
        "roadmap_id": "RM09",
        "svg_file": "RM09.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Baseado em metanálise Frontiers in Neurology 2024 e ensaios com terapia fonoaudiológica combinada.",
        "no1_pergunta": "Qual é o foco predominante da alteração de linguagem?",
        "fatores_limitantes": [
            {"id": "expressao", "label": "Afasia Não-Fluente / Expressão e Nomeação"},
            {"id": "compreensao", "label": "Afasia Fluente / Compreensão e Wernicke"}
        ],
        "modalidades": {
            "expressao": {
                "tecnica": "rTMS Inibitória Contralesional ou tDCS Anodal",
                "modalidade_sigla": "rTMS / tDCS",
                "alvo": "Giro Frontal Inferior direito (Área de Broca homologa / CP6 / F8)",
                "frequencia": "1 Hz inibitória",
                "intensidade": "80% a 90% do LMR",
                "pulsos_duracao": "1.200 pulsos (20 min)",
                "sessoes": "15 a 20 sessões, com terapia de linguagem iniciando imediatamente após",
                "escala_recomendada": "Teste de Nomeação de Boston (BNT) e Fluência Verbal",
                "meta_melhora": "Ganho substancial na nomeação de substantivos e itens treinados",
                "tamanho_efeito": "Aumento estatisticamente significativo na precisão de nomeação e velocidade de evocação lexical pós-estimulação",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível A (Eficácia Estabelecida na afasia não fluente pós-AVC)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Dual Bihemisférica)",
                    "tecnica": "tDCS",
                    "alvo": "Ânodo sobre F5 (Broca esquerda lesada) / Cátodo sobre F6 (direita)",
                    "parametros": "2.0 mA, 20 minutos durante sessão fonoaudiológica",
                    "observacoes": "Potencializa simultaneamente a facilitação peri-lesional e a desinibição contralesional."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar ao final da 10ª sessão.",
                    "ajuste_dose": "Se resposta modesta, testar localização precisa via neuronavigação ou 10-20 estendido.",
                    "regra_interrupcao": "Interromper ciclo de indução se ausência completa de resposta após 15 sessões."
                },
                "contraindicacoes": ["Implantes cranianos metálicos", "Afasia global severa com perda completa de compreensão (ajustar expectativas)"],
                "notas_clinicas": "A inibição da área homóloga direita visa romper a interferência inibitória anômala sobre o hemisfério esquerdo remanescente."
            },
            "compreensao": {
                "tecnica": "tDCS Anodal / rTMS Temporoparietal",
                "modalidade_sigla": "tDCS",
                "alvo": "Córtex Temporoparietal Esquerdo (Área de Wernicke / T3)",
                "frequencia": "Corrente contínua",
                "intensidade": "2.0 mA",
                "pulsos_duracao": "20 minutos",
                "sessoes": "10 a 15 sessões diárias",
                "escala_recomendada": "Western Aphasia Battery (WAB) / Teste Token",
                "meta_melhora": "Melhora na compreensão auditiva e associação semântica de objetos",
                "tamanho_efeito": "Melhora demonstrada em acurácia de compreensão de frases complexas",
                "evidencia": "Emergente (Estudos controlados em expansão)",
                "linha_fluxograma": "pontilhada",
                "diretriz_internacional": "Consenso NAPeN: Nível C",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (rTMS em Baixa Frequência Contralateral)",
                    "tecnica": "rTMS 1 Hz",
                    "alvo": "Córtex Temporoparietal Direito",
                    "parametros": "1 Hz, 90% LMR, 1.200 pulsos",
                    "observacoes": "Reduz hiperativação homóloga contralateral."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar na 10ª sessão.",
                    "ajuste_dose": "Associar tarefas de discriminação fonêmica durante a passagem da corrente.",
                    "regra_interrupcao": "Interromper se ausência de evolução perceptiva após 12 sessões."
                },
                "contraindicacoes": ["Metal no crânio", "Crises epilépticas"],
                "notas_clinicas": "Necessita de estabilidade hemodinâmica prévia e cooperação para os testes de compreensão."
            }
        }
    },
    {
        "id": "avc-disfagia",
        "condicao": "Acidente Vascular Cerebral (AVC) — Disfagia Orofaríngea",
        "eixo": "Doenças Cerebrovasculares (AVC)",
        "roadmap_id": "RM07",
        "svg_file": "RM07.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Respaldo em metanálises recentes de reabilitação da deglutição pós-AVC (2023).",
        "no1_pergunta": "Qual é a gravidade e o foco da alteração de deglutição?",
        "fatores_limitantes": [
            {"id": "orofaringea", "label": "Disfagia Orofaríngea Aguda/Subaguda (Risco de Broncoaspiração)"},
            {"id": "tempo_transito", "label": "Atraso no Tempo de Trânsito Oral e Faríngeo"}
        ],
        "modalidades": {
            "orofaringea": {
                "tecnica": "rTMS de Alta Frequência / iTBS ou tDCS",
                "modalidade_sigla": "rTMS / tDCS",
                "alvo": "Córtex Motor Faríngeo (representação da deglutição C5/C6 ou córtex motor esofágico bilateral)",
                "frequencia": "5 Hz ou 50 Hz (iTBS) para rTMS / Anodal no tDCS",
                "intensidade": "110% do LMR (5 Hz) ou 70% LMR (iTBS) / 2.0 mA (tDCS)",
                "pulsos_duracao": "1.800 pulsos (5 Hz) ou 600 pulsos (iTBS) / 20 min (tDCS)",
                "sessoes": "5 a 10 sessões (1ª semana hemisfério dominante, 2ª semana hemisfério contralateral)",
                "escala_recomendada": "Functional Oral Intake Scale (FOIS) e Escala DOSS",
                "meta_melhora": "Evolução na escala FOIS com liberação segura de consistências orais",
                "tamanho_efeito": "Aumento médio de 2,53 pontos na Escala FOIS (IC 95% 0,28 a 4,78) e ganho de 5 pontos na Escala DOSS (melhora de 70,8%)",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível B (Eficácia Provável na disfagia pós-AVC)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (Estimulação Vagal Não Invasiva - taVNS)",
                    "tecnica": "taVNS (Vago Auricular)",
                    "alvo": "Concha e trago da orelha esquerda",
                    "parametros": "25 Hz, intensidade sensorial confortável, 30 min, 2x/dia, 5 dias/semana",
                    "observacoes": "Especialmente viável na fase aguda hospitalar à beira do leito, com melhora no tônus autonômico e deglutição."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliação fonoaudiológica após 5 dias de estimulação.",
                    "ajuste_dose": "Se ausência de resposta, alternar hemisfério de estimulação de dominante para não lesado.",
                    "regra_interrupcao": "Considera-se resposta insatisfatória a ausência de melhora na escala FOIS em até 5 dias."
                },
                "contraindicacoes": ["Broncopneumonia aspirativa aguda em curso", "Traqueostomia descompensada", "Implantes metálicos cervicais/cefálicos"],
                "notas_clinicas": "A terapia fonoaudiológica com biofeedback deve ser iniciada imediatamente após o término da sessão de estimulação."
            },
            "tempo_transito": {
                "tecnica": "tDCS Anodal sobre Córtex Faríngeo",
                "modalidade_sigla": "tDCS",
                "alvo": "Córtex motor faríngeo ipsilesional / supraorbitário contralateral",
                "frequencia": "Corrente contínua",
                "intensidade": "1.5 a 2.0 mA",
                "pulsos_duracao": "20 minutos",
                "sessoes": "5 a 10 sessões diárias",
                "escala_recomendada": "Fiberoptic Endoscopic Dysphagia Severity Scale (FEDSS) e DOSS",
                "meta_melhora": "Redução no tempo de trânsito oral e faríngeo à videoendoscopia",
                "tamanho_efeito": "Redução de 0,72 pontos na FEDSS e aceleração de até 46% no tempo de trânsito oral",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Consenso NAPeN / Metanálise 2023",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (Estimulação de Hemisfério Não Afetado)",
                    "tecnica": "tDCS Anodal Contralesional",
                    "alvo": "Córtex motor faríngeo do hemisfério íntegro",
                    "parametros": "2 mA, 20 min com treino de deglutição de saliva e pastoso",
                    "observacoes": "Recruta a representação faríngea compensatória no hemisfério preservado."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "No 5º dia de protocolo.",
                    "ajuste_dose": "Ajustar consistência dos bolos alimentares nos treinos conforme escala FOIS.",
                    "regra_interrupcao": "Interromper se estagnação sem ganho deglutitório após 10 dias."
                },
                "contraindicacoes": ["Marca-passo cardíaco", "Lesões cutâneas na fronte"],
                "notas_clinicas": "Sempre monitorar saturação de O2 e ausculta cervical durante as sessões de treino com alimento."
            }
        }
    },
    {
        "id": "doenca-parkinson",
        "condicao": "Doença de Parkinson — Sintomas Motores e Marcha",
        "eixo": "Distúrbios do Movimento",
        "roadmap_id": "RM17",
        "svg_file": "RM17.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Metanálises JAMA Neurology e ensaios com avaliação UPDRS-III em estado OFF medicação.",
        "no1_pergunta": "Qual é a principal queixa ou fator limitante motor?",
        "fatores_limitantes": [
            {"id": "funcao_global", "label": "Sintomas Motores Globais (Rigidez / Bradicinesia)"},
            {"id": "fog", "label": "Freezing of Gait (Congelamento da Marcha)"},
            {"id": "mobilidade", "label": "Mobilidade Funcional / Risco de Quedas (TUG)"}
        ],
        "modalidades": {
            "funcao_global": {
                "tecnica": "rTMS de Alta Frequência Bilateral",
                "modalidade_sigla": "rTMS",
                "alvo": "Córtex Motor Primário (M1 Bilateral) e/ou Córtex Pré-frontal (F3)",
                "frequencia": "10 Hz excitatória",
                "intensidade": "90% a 110% do LMR",
                "pulsos_duracao": "2.000 a 7.000 pulsos totais por sessão",
                "sessoes": "10 a 20 sessões diárias (2 a 4 semanas consecutivas)",
                "escala_recomendada": "MDS-UPDRS Parte III (Escala de Avaliação Motora no estado OFF)",
                "meta_melhora": "Redução clinicamente significativa na pontuação motora UPDRS-III",
                "tamanho_efeito": "Redução média de 15% a 57,69% na pontuação da UPDRS-III (SMD = 0,51 em metanálise JAMA)",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível B (Eficácia Provável nos sintomas motores de membros)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Anodal sobre M1 / DLPFC)",
                    "tecnica": "tDCS",
                    "alvo": "Ânodo M1 bilateral / Cátodo supraorbitário",
                    "parametros": "2.0 mA, 20 minutos, 10 sessões",
                    "observacoes": "Única opção de neuromodulação não invasiva permitida para pacientes com marcapasso DBS implantado (onde rTMS é contraindicada absoluta)."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar a cada 1 semana com a UPDRS-III.",
                    "ajuste_dose": "Se piora de sintomas motores ou estagnação após 1 semana, recalibrar o LMR e checar horário da medicação dopaminérgica.",
                    "regra_interrupcao": "Interromper se ausência de mudança na escala pré-teste após 2 semanas completas com 10 sessões."
                },
                "contraindicacoes": ["DBS (Estimulação Cerebral Profunda implantada — contraindicação absoluta para rTMS)", "Crises epilépticas", "Discinesias graves no pico de dose"],
                "notas_clinicas": "Aplicar a estimulação preferencialmente na transição entre fases da medicação para avaliar ganho funcional sustentado."
            },
            "fog": {
                "tecnica": "rTMS de Alta Frequência sobre Área Motora Suplementar (AMS)",
                "modalidade_sigla": "rTMS",
                "alvo": "Área Motora Suplementar (AMS / SMA) e M1",
                "frequencia": "Altas frequências (10 Hz a 20 Hz)",
                "intensidade": "100% do LMR",
                "pulsos_duracao": "2.000 a 3.000 pulsos",
                "sessoes": "10 a 15 sessões diárias",
                "escala_recomendada": "Freezing of Gait Questionnaire (FOGQ)",
                "meta_melhora": "Redução na frequência e duração dos episódios de congelamento",
                "tamanho_efeito": "Redução de 9,2% a 23,0% na pontuação do questionário FOGQ e diminuição de episódios de travamento",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Consenso NAPeN / Diretriz Lefaucheur",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (Estimulação Espinhal tsMS nível T10-T12)",
                    "tecnica": "tsMS (Estimulação Magnética Transespinhal)",
                    "alvo": "Nível toracolombar T10-T12",
                    "parametros": "1 Hz, 1.500 pulsos por área",
                    "observacoes": "Ativa geradores centrais de padrão de marcha espinhais para destravar o ritmo locomotor."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Semanalmente.",
                    "ajuste_dose": "Ajustar alinhamento sobre a linha média da SMA.",
                    "regra_interrupcao": "Interromper se congelamento não sofrer variação após 10 sessões."
                },
                "contraindicacoes": ["DBS", "Implantes de coluna"],
                "notas_clinicas": "Associar pistas auditivas e visuais rítmicas durante os treinos locomotores pós-estímulo."
            },
            "mobilidade": {
                "tecnica": "rTMS / tDCS sobre Córtex Motor",
                "modalidade_sigla": "rTMS / tDCS",
                "alvo": "M1 (área de pernas) e CPFDL",
                "frequencia": "10 Hz",
                "intensidade": "100% LMR",
                "pulsos_duracao": "2.000 pulsos",
                "sessoes": "10 a 15 sessões",
                "escala_recomendada": "Timed Up and Go (TUG)",
                "meta_melhora": "Redução clinicamente significativa no tempo de execução do TUG",
                "tamanho_efeito": "Redução no teste TUG em até 32 segundos e aumento médio de 12,5% na velocidade da marcha",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur Nível B",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Pré-frontal F3/F4)",
                    "tecnica": "tDCS",
                    "alvo": "DLPFC bilateral (dupla tarefa motora-cognitiva)",
                    "parametros": "2.0 mA, 20 min com treino de dupla tarefa",
                    "observacoes": "Melhora a atenção executiva durante a marcha e reduz risco de quedas distrativas."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Avaliar após a 5ª e 10ª sessão.",
                    "ajuste_dose": "Monitorar queixas de fadiga ou cefaleia após a sessão.",
                    "regra_interrupcao": "Interromper se ausência de ganho no TUG."
                },
                "contraindicacoes": ["DBS", "Hipotensão postural descompensada"],
                "notas_clinicas": "Protocolo com elevado impacto na prevenção secundária de fraturas por queda."
            }
        }
    },
    {
        "id": "depressao-maior",
        "condicao": "Depressão Maior (Transtorno Depressivo Maior)",
        "eixo": "Psiquiatria & Saúde Mental",
        "roadmap_id": "RM10",
        "svg_file": "RM10.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Diretrizes de maior volume de evidências e aprovações regulatórias na neuromodulação (FDA / ANVISA / CFM).",
        "no1_pergunta": "Qual é a demanda clínica prioritária do quadro depressivo?",
        "fatores_limitantes": [
            {"id": "moderada_grave", "label": "Sintomas Moderados a Graves (Protocolo Padrão Alta Frequência)"},
            {"id": "tempo_reduzido", "label": "Demanda por Tempo Reduzido (Protocolo iTBS Acelerado)"},
            {"id": "comorbidade_ansiedade", "label": "Depressão com Comorbidade Ansiosa Relevante"}
        ],
        "modalidades": {
            "moderada_grave": {
                "tecnica": "rTMS de Alta Frequência Esquerda",
                "modalidade_sigla": "rTMS",
                "alvo": "Córtex Pré-Frontal Dorsolateral Esquerdo (F3 / DLPFC)",
                "frequencia": "10 Hz excitatória",
                "intensidade": "120% do LMR",
                "pulsos_duracao": "3.000 pulsos por sessão (trens de 4s / pausa de 26s)",
                "sessoes": "20 a 30 sessões diárias (4 a 6 semanas consecutivas)",
                "escala_recomendada": "HAMD-17 / HDRS-21 ou MADRS",
                "meta_melhora": "Redução ≥ 50% na escala HAMD (critério de resposta clínica da NAPeN) ou escore ≤ 7 (remissão)",
                "tamanho_efeito": "Redução média de ~55% no HDRS-21 e 52% na MADRS; taxa de resposta típica de 50–60%",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível A (Eficácia Definitivamente Estabelecida / FDA 2008)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (Estimulação Bilateral F3 Alta + F4 Baixa)",
                    "tecnica": "rTMS Bilateral Sequencial",
                    "alvo": "F3 (10 Hz excitatório) seguido de F4 (1 Hz inibitório)",
                    "parametros": "10 Hz F3 (1.500p) + 1 Hz F4 (1.200p), 110% a 120% LMR",
                    "observacoes": "Indicado se resposta parcial após 15 sessões ou se houver componente ansioso/insônia associado."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar na 10ª, 15ª e 20ª sessão com a escala HAMD.",
                    "ajuste_dose": "Titular de 100% para 120% do LMR nos primeiros 3 dias para mitigar desconforto no couro cabeludo.",
                    "regra_interrupcao": "Se redução na HAMD for < 20% após 15 sessões com adesão confirmada, transicionar para protocolo bilateral ou iTBS."
                },
                "contraindicacoes": ["Implantes metálicos cranianos", "Histórico de crises convulsivas", "Transtorno Bipolar em viragem maníaca"],
                "notas_clinicas": "Recomenda-se manter estabilidade dos psicofármacos durante o ciclo de indução."
            },
            "tempo_reduzido": {
                "tecnica": "iTBS (Intermittent Theta Burst Stimulation)",
                "modalidade_sigla": "iTBS",
                "alvo": "Córtex Pré-Frontal Dorsolateral Esquerdo (F3)",
                "frequencia": "50 Hz em tripletos repetidos a 5 Hz",
                "intensidade": "80% a 120% do LMR",
                "pulsos_duracao": "600 a 1.800 pulsos (duração de apenas 3 minutos por sessão)",
                "sessoes": "20 a 30 sessões (pode ser aplicado em formato acelerado 3 a 5 sessões/dia)",
                "escala_recomendada": "HAMD-17",
                "meta_melhora": "Redução ≥ 50% na pontuação HAMD-17",
                "tamanho_efeito": "Redução de 54,7% na HAMD-17 (equivalência comprovada ao protocolo 10 Hz convencional de 37 min)",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível A (Eficácia Estabelecida / FDA 2018)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (rTMS 10 Hz Padrão)",
                    "tecnica": "rTMS 10 Hz convencional",
                    "alvo": "F3 (3.000 pulsos)",
                    "parametros": "10 Hz, 120% LMR, 30 min",
                    "observacoes": "Indicado se o paciente relatar dor cutânea intolerável aos pulsos concentrados do theta burst."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Avaliar semanalmente.",
                    "ajuste_dose": "Espaçar intervalos entre sessões no protocolo acelerado (mínimo de 50 minutos entre trens).",
                    "regra_interrupcao": "Interromper se ausência de resposta após ciclo completo de 30 sessões."
                },
                "contraindicacoes": ["Metal no crânio", "Epilepsia ativa"],
                "notas_clinicas": "O protocolo iTBS revolucionou a adesão por reduzir o tempo de sessão de 37 minutos para apenas 3 minutos."
            },
            "comorbidade_ansiedade": {
                "tecnica": "rTMS Inibitória Direita ou Bilateral",
                "modalidade_sigla": "rTMS",
                "alvo": "Córtex Pré-Frontal Dorsolateral Direito (F4 / DLPFC Direito)",
                "frequencia": "1 Hz inibitória (ou sequencial bilateral)",
                "intensidade": "110% a 120% do LMR",
                "pulsos_duracao": "1.200 a 1.500 pulsos contínuos",
                "sessoes": "15 a 20 sessões diárias",
                "escala_recomendada": "HAMD-17 + Escala de Ansiedade de Hamilton (HAM-A)",
                "meta_melhora": "Redução combinada nas escalas de depressão e ansiedade",
                "tamanho_efeito": "Redução média de 32% a 45% nos escores de ansiedade comórbida associada ao alívio do humor",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur: Nível B / Consenso NAPeN",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (cTBS Contínuo sobre F4)",
                    "tecnica": "cTBS",
                    "alvo": "F4 (DLPFC direito)",
                    "parametros": "600 pulsos (40s contínuos)",
                    "observacoes": "Inibe a hiperativação da amígdala e o circuito do estresse."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Na 10ª sessão.",
                    "ajuste_dose": "Aumentar tempo de estimulação para 1.500 pulsos se ansiedade residual permanecer.",
                    "regra_interrupcao": "Interromper se ausência de redução de sintomas em 15 sessões."
                },
                "contraindicacoes": ["Metal no crânio", "Crises epilépticas"],
                "notas_clinicas": "A inibição de F4 apresenta menor risco de cefaleia e menor desconforto acústico em relação à alta frequência esquerda."
            }
        }
    },
    {
        "id": "ansiedade-generalizada",
        "condicao": "Transtorno de Ansiedade Generalizada (TAG)",
        "eixo": "Psiquiatria & Saúde Mental",
        "roadmap_id": "RM11",
        "svg_file": "RM11.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Ensaios controlados com rTMS de baixa frequência e TBS em córtex pré-frontal direito.",
        "no1_pergunta": "Qual é a gravidade e o perfil da ansiedade?",
        "fatores_limitantes": [
            {"id": "moderada_alta", "label": "Ansiedade Moderada a Alta (HAM-A > 14)"},
            {"id": "comorbidade_depressiva", "label": "Ansiedade com Comorbidade Depressiva"}
        ],
        "modalidades": {
            "moderada_alta": {
                "tecnica": "rTMS de Baixa Frequência Direita / cTBS",
                "modalidade_sigla": "rTMS",
                "alvo": "Córtex Pré-Frontal Dorsolateral Direito (F4) ou Parietal Direito (P4)",
                "frequencia": "1 Hz inibitória (ou 20 Hz / cTBS 600 pulsos)",
                "intensidade": "100% a 110% do LMR",
                "pulsos_duracao": "600 a 1.200 pulsos por sessão",
                "sessoes": "10 a 20 sessões (5 sessões/semana por 2 a 4 semanas, com desmame progressivo)",
                "escala_recomendada": "Escala Hamilton de Nível de Ansiedade (HAM-A)",
                "meta_melhora": "Redução clínica clinicamente relevante no escore HAM-A",
                "tamanho_efeito": "Redução média de 45% (1 Hz) a 86% (20 Hz) na escala HAM-A ao término do ciclo",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível B (Eficácia Provável no TAG)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (cTBS Direita sobre F4)",
                    "tecnica": "cTBS",
                    "alvo": "F4",
                    "parametros": "600 pulsos, priorizando tolerabilidade e segurança",
                    "observacoes": "Reduz hipervigilância autonômica em pacientes sensíveis a estímulos prolongados."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar semanalmente com a HAM-A e escala de sono PSQI.",
                    "ajuste_dose": "Reduzir gradualmente para 3 a 2 sessões por semana antes de finalizar o protocolo (esquema de desmame).",
                    "regra_interrupcao": "Interromper se ausência de resposta após 15 sessões com adesão plena."
                },
                "contraindicacoes": ["Implantes metálicos", "Epilepsia ativa"],
                "notas_clinicas": "Recomenda-se associar medidas de higiene do sono devido à melhora no índice de Pittsburgh (PSQI)."
            },
            "comorbidade_depressiva": {
                "tecnica": "rTMS Bilateral Sequencial (F3 + F4)",
                "modalidade_sigla": "rTMS",
                "alvo": "F3 (DLPFC esquerdo) + F4 (DLPFC direito)",
                "frequencia": "10 Hz (F3) / 1 Hz (F4)",
                "intensidade": "110% do LMR",
                "pulsos_duracao": "1.500 pulsos em F3 + 900 pulsos em F4",
                "sessoes": "15 a 20 sessões diárias",
                "escala_recomendada": "HAM-A e HAMD-17",
                "meta_melhora": "Redução concomitante de sintomas depressivos e ansiosos",
                "tamanho_efeito": "Redução de 32% na HAM-A acompanhada de estabilização do humor",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Consenso NAPeN: Nível B",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Anodal F3 / Cátodo F4)",
                    "tecnica": "tDCS",
                    "alvo": "Bilateral prefrontal",
                    "parametros": "2.0 mA, 20 min, 15 sessões",
                    "observacoes": "Promove equilíbrio inter-hemisférico frontocortical com perfil livre de dor."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Na 10ª sessão.",
                    "ajuste_dose": "Titular de acordo com resposta na pontuação composta de humor e ansiedade.",
                    "regra_interrupcao": "Interromper se ausência de melhora após 15 sessões."
                },
                "contraindicacoes": ["Metal no crânio", "Crises epilépticas"],
                "notas_clinicas": "O tratamento é considerado falho se não houver redução significativa após o ciclo de indução."
            }
        }
    },
    {
        "id": "tept",
        "condicao": "Transtorno de Estresse Pós-Traumático (TEPT)",
        "eixo": "Psiquiatria & Saúde Mental",
        "roadmap_id": "RM18",
        "svg_file": "RM18.svg",
        "status_auditoria": "Preliminar (OCR em revisão humana)",
        "nota_auditoria": "⚠️ Atenção: Roadmap transcrito a partir de imagem original; conferência clínica dos nós em andamento pelo GT de Diretrizes.",
        "no1_pergunta": "Qual é a queixa nuclear predominante do quadro de TEPT?",
        "fatores_limitantes": [
            {"id": "sintomas_gerais", "label": "Hiperarousal / Revivência e Intrusão"},
            {"id": "comorbidade_depressiva", "label": "TEPT com Comorbidade Depressiva Relevante"}
        ],
        "modalidades": {
            "sintomas_gerais": {
                "tecnica": "rTMS / TBS sobre Córtex Pré-Frontal Direito",
                "modalidade_sigla": "rTMS / TBS",
                "alvo": "Córtex Pré-Frontal Dorsolateral Direito (F4)",
                "frequencia": "20 Hz / 10 Hz ou TBS",
                "intensidade": "80% a 100% do LMR",
                "pulsos_duracao": "600 a 2.400 pulsos",
                "sessoes": "10 a 15 sessões diárias",
                "escala_recomendada": "PCL-5 (Posttraumatic Stress Disorder Checklist)",
                "meta_melhora": "Redução expressiva na pontuação total da PCL-5",
                "tamanho_efeito": "Redução de 29,9% a 52,0% na PCL-5 e alívio de sintomas de hipervigilância",
                "evidencia": "Emergente (Estudos clínicos controlados sem meta-análise definitiva)",
                "linha_fluxograma": "pontilhada",
                "diretriz_internacional": "Lefaucheur: Nível B (Eficácia Provável em rTMS direita)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (rTMS Inibitória 1 Hz)",
                    "tecnica": "rTMS 1 Hz",
                    "alvo": "F4 (DLPFC direito)",
                    "parametros": "1 Hz, 80% LMR, 400 a 1.200 pulsos",
                    "observacoes": "Diminui hiperativação autonômica e reatividade ao estresse."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar na 10ª sessão.",
                    "ajuste_dose": "Associar terapia cognitivo-comportamental focada no trauma imediatamente após o estímulo.",
                    "regra_interrupcao": "Interromper se ausência de redução de intrusão após 15 sessões."
                },
                "contraindicacoes": ["Metal no crânio", "Ideação suicida aguda descompensada", "Psicose ativa"],
                "notas_clinicas": "A estimulação facilita a extinção do medo condicionado quando associada à terapia de exposição."
            },
            "comorbidade_depressiva": {
                "tecnica": "rTMS 1 Hz ou Bilateral",
                "modalidade_sigla": "rTMS",
                "alvo": "F4 ou bilateral F3/F4",
                "frequencia": "1 Hz",
                "intensidade": "80% LMR",
                "pulsos_duracao": "400 a 1.200 pulsos",
                "sessoes": "10 a 20 sessões",
                "escala_recomendada": "PCL-5 e HAMD-17",
                "meta_melhora": "Redução concomitante de reatividade ao estresse e humor deprimido",
                "tamanho_efeito": "Redução média de 25,0% na PCL acompanhada de melhora nos escores depressivos",
                "evidencia": "Emergente (Estudos em revisão)",
                "linha_fluxograma": "pontilhada",
                "diretriz_internacional": "Consenso NAPeN: Nível C",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Pré-frontal)",
                    "tecnica": "tDCS",
                    "alvo": "F3 ânodo / F4 cátodo",
                    "parametros": "2 mA, 20 min",
                    "observacoes": "Facilita o controle inibitório sobre memórias aversivas."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Avaliar na 10ª sessão.",
                    "ajuste_dose": "Ajustar dose conforme tolerabilidade psicológica durante o estímulo.",
                    "regra_interrupcao": "Interromper se estagnação após 15 sessões."
                },
                "contraindicacoes": ["Metal no crânio", "Crises convulsivas"],
                "notas_clinicas": "Monitorar possíveis sintomas dissociativos durante as primeiras sessões."
            }
        }
    },
    {
        "id": "dor-neuropatica",
        "condicao": "Dor Neuropática Crônica",
        "eixo": "Dor Crônica & Neuropática",
        "roadmap_id": "RM05",
        "svg_file": "RM05.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Diretrizes com respaldo nos consensos de Lefaucheur et al. e revisões Cochrane de dor crônica.",
        "no1_pergunta": "Qual é a topografia e a origem da dor neuropática?",
        "fatores_limitantes": [
            {"id": "geral", "label": "Dor Neuropática Geral / Central / Pós-AVC / Radiculopatia"},
            {"id": "espinhal", "label": "Dor Neuropática Espinhal / Medular"}
        ],
        "modalidades": {
            "geral": {
                "tecnica": "rTMS de Alta Frequência sobre M1",
                "modalidade_sigla": "rTMS",
                "alvo": "C3 ou M1 contralateral à dor (área motora somatotópica)",
                "frequencia": "10 Hz a 20 Hz",
                "intensidade": "80% a 90% do LMR",
                "pulsos_duracao": "2.000 a 3.000 pulsos totais por sessão",
                "sessoes": "10 ou mais sessões diárias (fase de indução), seguidas de manutenção",
                "escala_recomendada": "Escala Visual Analógica de Dor (EVA) e DN4",
                "meta_melhora": "Redução clinicamente significativa ≥ 30% na escala EVA de dor",
                "tamanho_efeito": "Redução média de 24% a 36% na escala EVA; possível melhora precoce em alodinia e hiperalgesia",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível A (Eficácia Definitivamente Estabelecida para dor neuropática crônica)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Anodal sobre M1)",
                    "tecnica": "tDCS",
                    "alvo": "Ânodo sobre M1 contralateral à dor / Cátodo supraorbitário",
                    "parametros": "2.0 mA, 20 minutos, 10 a 20 sessões",
                    "observacoes": "Excelente opção para pacientes que necessitam de intervenção contínua e boa tolerabilidade."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Avaliar após a 5ª e 10ª sessão.",
                    "ajuste_dose": "É possível que os pacientes não melhorem na intensidade pura da dor, mas melhorem em alterações sensoriais como alodinia e hiperalgesia. Avaliar ambos.",
                    "regra_interrupcao": "Interromper se ausência de alteração após 10 sessões."
                },
                "contraindicacoes": ["Placas cranianas metálicas próximas", "Marca-passo cardíaco"],
                "notas_clinicas": "A estimulação do córtex motor ativa mecanismos inibitórios endógenos opióides e vias talamocorticais descendentes."
            },
            "espinhal": {
                "tecnica": "tsDCS (Estimulação Espinhal Transcutânea por Corrente Contínua)",
                "modalidade_sigla": "tsDCS",
                "alvo": "Medula espinhal (nível C4-C5 cervical ou L1-L2 lombar)",
                "frequencia": "Corrente contínua",
                "intensidade": "2.0 mA",
                "pulsos_duracao": "20 minutos",
                "sessoes": "5 ou mais sessões",
                "escala_recomendada": "Escala Visual Analógica (EVA)",
                "meta_melhora": "Alívio da dor radicular e lombar/cervical",
                "tamanho_efeito": "Redução média de até 20% nos escores de dor radicular crônica",
                "evidencia": "Emergente (Estudos pilotos e observacionais)",
                "linha_fluxograma": "pontilhada",
                "diretriz_internacional": "Consenso NAPeN: Nível C",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (rTMS sobre M1 correspondente)",
                    "tecnica": "rTMS 10 Hz",
                    "alvo": "M1 cortical representativo da área do membro acometido",
                    "parametros": "10 Hz, 85% LMR, 2.000 pulsos",
                    "observacoes": "Modulação ascendente do controle inibitório da dor."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "No 5º dia de estimulação.",
                    "ajuste_dose": "Verificar impedância e contato dos eletrodos sobre o processo espinhoso.",
                    "regra_interrupcao": "Interromper se ausência de alívio após 10 dias."
                },
                "contraindicacoes": ["Implantes metálicos de fixação vertebral no segmento estimulado", "Gestação"],
                "notas_clinicas": "Modalidade inovadora em expansão com excelente perfil de segurança."
            }
        }
    },
    {
        "id": "ataxia-cerebelar",
        "condicao": "Ataxia Cerebelar",
        "eixo": "Distúrbios do Movimento",
        "roadmap_id": "RM16",
        "svg_file": "RM16.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Estudos randomizados com estimulação magnética e elétrica cerebelar.",
        "no1_pergunta": "Qual é a manifestação atáxica primária a ser reabilitada?",
        "fatores_limitantes": [
            {"id": "severidade_motora", "label": "Severidade Motora / Destreza Manual (9HPT)"},
            {"id": "equilibrio", "label": "Equilíbrio e Marcha Atáxica (SARA / BBS)"}
        ],
        "modalidades": {
            "severidade_motora": {
                "tecnica": "rTMS Cerebelar (cbTMS)",
                "modalidade_sigla": "rTMS (cbTMS)",
                "alvo": "Hemisférios cerebelares ou Vérmis cerebelar",
                "frequencia": "1 Hz inibitória (ou alta frequência excitatória)",
                "intensidade": "100% do LMR",
                "pulsos_duracao": "1.800 pulsos totais por sessão",
                "sessoes": "10 a 20 sessões diárias",
                "escala_recomendada": "Scale for Assessment and Rating of Ataxia (SARA) e 9-Hole Peg Test (9HPT)",
                "meta_melhora": "Redução clinicamente perceptível na pontuação SARA",
                "tamanho_efeito": "Redução média de 25% na SARA, redução de 28% no ICARS e melhora de 12,83% no 9HPT",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur: Nível B / Consenso NAPeN",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (ctDCS Cerebelar)",
                    "tecnica": "tDCS Cerebelar",
                    "alvo": "Ânodo cerebelar bilateral / Cátodo em bucinador",
                    "parametros": "2.0 mA, 20 minutos, 10 sessões",
                    "observacoes": "Alternativa de alta comodidade para estabilização de tônus e coordenação fina."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar a cada 1 semana para verificar resposta terapêutica.",
                    "ajuste_dose": "De uma semana para a outra se o paciente não teve mudança de pontuação nas escalas pré-teste para o microdesfecho, realizar sessão de ajuste na terapia motora associada.",
                    "regra_interrupcao": "Interromper se estagnação sem melhora após 2 semanas consecutivas."
                },
                "contraindicacoes": ["Clips de aneurisma na fossa posterior", "Implantes metálicos occipitais"],
                "notas_clinicas": "A terapia motora associada deve estar relacionada com o desfecho. Evitar fadiga excessiva do paciente atáxico."
            },
            "equilibrio": {
                "tecnica": "tDCS Cerebelar (ctDCS)",
                "modalidade_sigla": "tDCS (ctDCS)",
                "alvo": "Cerebelo (linha média 2 cm abaixo do ínion)",
                "frequencia": "Corrente contínua",
                "intensidade": "2.0 mA",
                "pulsos_duracao": "20 minutos",
                "sessoes": "10 sessões associadas a treino de equilíbrio em plataforma",
                "escala_recomendada": "Berg Balance Scale (BBS) e SARA",
                "meta_melhora": "Melhora no equilíbrio estático e tempo de caminhada de 10 metros",
                "tamanho_efeito": "Melhora de 14,8% na escala SARA, aumento de 11,77% na BBS e ganho de 31,11% no teste de 10 metros",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível B",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (cbTMS de Alta Frequência)",
                    "tecnica": "rTMS 10 Hz",
                    "alvo": "Vérmis cerebelar",
                    "parametros": "10 Hz, 90% LMR, 1.500 pulsos",
                    "observacoes": "Facilitação das vias dentatorrubrotalamocorticais."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Semanalmente.",
                    "ajuste_dose": "Ajustar exercícios motores para nível de fadiga leve a moderado.",
                    "regra_interrupcao": "Interromper se não houver ganho funcional em 10 sessões."
                },
                "contraindicacoes": ["Metal no crânio", "Lesões cutâneas na nuca"],
                "notas_clinicas": "Medicamentos como benzodiazepínicos tendem a diminuir os efeitos terapêuticos da estimulação."
            }
        }
    },
    {
        "id": "paralisia-cerebral",
        "condicao": "Paralisia Cerebral (PC)",
        "eixo": "Neurodesenvolvimento",
        "roadmap_id": "RM14",
        "svg_file": "RM14.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Diretrizes com ensaios clínicos pediátricos em crianças e adolescentes com PC espástica.",
        "no1_pergunta": "Qual é a distribuição topográfica e motora predominante?",
        "fatores_limitantes": [
            {"id": "deficits_motores", "label": "Déficits Motores / Hemiparesia Espástica (Controle Motor e Equilíbrio)"}
        ],
        "modalidades": {
            "deficits_motores": {
                "tecnica": "rTMS / tDCS sobre Córtex Motor",
                "modalidade_sigla": "rTMS / tDCS",
                "alvo": "M1 lesado (C3/C4) ou M1 não lesado",
                "frequencia": "10 Hz (no hemisfério lesado) ou 1 Hz (no não lesado) / Anodal no tDCS",
                "intensidade": "90% do LMR (rTMS) / 1.0 a 1.5 mA conforme faixa etária (tDCS)",
                "pulsos_duracao": "1.600 pulsos (10 Hz) ou 960 pulsos (1 Hz) / 20 min (tDCS)",
                "sessoes": "10 a 20 sessões combinadas com fisioterapia intensiva",
                "escala_recomendada": "Gross Motor Function Measure (GMFM) e Escala de Ashworth Modificada",
                "meta_melhora": "Ganho observável na função motora grossa e redução da espasticidade",
                "tamanho_efeito": "Melhora de até 63% no equilíbrio e ganho funcional motor observável nas tarefas ativas",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Consenso NAPeN: Nível B",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Bihemisférica com Rampa Suave)",
                    "tecnica": "tDCS",
                    "alvo": "M1 lesado (ânodo) / M1 contralesional (cátodo)",
                    "parametros": "1.0 mA a 1.5 mA com rampa de subida/descida de 10s, 20 minutos",
                    "observacoes": "Adaptação pediátrica com alta tolerabilidade e redução de desconforto sensorial."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar na 5ª sessão de neuromodulação.",
                    "ajuste_dose": "Considera-se resposta insatisfatória a ausência de resposta clínica observável após 5 sessões, seja motora ou em indicadores secundários (sono, atenção, regulação emocional).",
                    "regra_interrupcao": "Respeitar intervalo de 3 a 4 meses entre ciclos repetidos para consolidação neuroplástica."
                },
                "contraindicacoes": ["Epilepsia refratária ativa não controlada", "Válvula de derivação ventriculoperitoneal com componente magnético próximo à bobina"],
                "notas_clinicas": "Recomenda-se realizar a aplicação concomitante ou imediatamente antes de terapia motora com metas bem definidas."
            }
        }
    },
    {
        "id": "transtorno-espectro-autista",
        "condicao": "Transtorno do Espectro Autista (TEA)",
        "eixo": "Neurodesenvolvimento",
        "roadmap_id": "RM15",
        "svg_file": "RM15.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Respaldo em metanálises recentes de ensaios controlados em TEA (Frontiers / ScienceDirect).",
        "no1_pergunta": "Qual é a dimensão clínica prioritária do paciente?",
        "fatores_limitantes": [
            {"id": "comportamental", "label": "Déficits Comportamentais (Irritabilidade, Rigidez, Hiperatividade)"},
            {"id": "social", "label": "Déficits Sociais e Comunicação (Teoria da Mente, Reconhecimento Facial)"}
        ],
        "modalidades": {
            "comportamental": {
                "tecnica": "rTMS de Baixa Frequência / tDCS",
                "modalidade_sigla": "rTMS / tDCS",
                "alvo": "Córtex Pré-Frontal Dorsolateral Esquerdo ou Bilateral (F3/F4)",
                "frequencia": "1 Hz inibitória (rTMS) ou estimulação catódica",
                "intensidade": "80% a 90% do LMR / 1.0 a 1.5 mA no tDCS",
                "pulsos_duracao": "1.200 pulsos / 20 minutos",
                "sessoes": "10 a 20 sessões (1 a 2x/semana ou diárias conforme tolerância sensorial)",
                "escala_recomendada": "Aberrant Behavior Checklist (ABC) — Subescala de Irritabilidade",
                "meta_melhora": "Redução clinicamente relevante na irritabilidade e estereotipias",
                "tamanho_efeito": "Redução média de 43,3% na pontuação do domínio Irritabilidade do questionário ABC",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Consenso NAPeN: Nível B",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS de Baixa Intensidade com Acomodação Sensorial)",
                    "tecnica": "tDCS",
                    "alvo": "F3/F4",
                    "parametros": "1 mA, 15–20 min com dessensibilização progressiva",
                    "observacoes": "Indicado para crianças com hipersensibilidade tátil ou auditiva à bobina magnética."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Reavaliar na 5ª sessão clínica.",
                    "ajuste_dose": "Considerar resposta insatisfatória a ausência de resposta observável após 5 sessões (cognitiva, qualidade do sono ou autorregulação).",
                    "regra_interrupcao": "Não ultrapassar 20 sessões no ciclo completo de indução. Intervalo de 3 a 4 meses antes de reindução."
                },
                "contraindicacoes": ["Epilepsia com descargas paroxísticas frequentes no EEG", "Implantes cocleares ou metálicos"],
                "notas_clinicas": "Manter esquema medicamentoso estável durante todo o ciclo para não mascarar a resposta à estimulação."
            },
            "social": {
                "tecnica": "rTMS / tDCS sobre Córtex Pré-Frontal ou TPJ",
                "modalidade_sigla": "rTMS / tDCS",
                "alvo": "Junção Temporoparietal (TPJ) ou CPFDL",
                "frequencia": "10 Hz excitatória ou tDCS Anodal",
                "intensidade": "90% LMR / 1.5 mA",
                "pulsos_duracao": "1.200 a 1.800 pulsos / 20 min",
                "sessoes": "10 a 20 sessões associadas a treino de habilidades sociais",
                "escala_recomendada": "Social Responsiveness Scale-2 (SRS-2) e ATEC",
                "meta_melhora": "Evolução nas tarefas de reconhecimento facial e cognição social",
                "tamanho_efeito": "Melhora de 69,6% no reconhecimento facial, aumento de 30,8% em Teoria da Mente e redução de 24,3% no escore SRS-2",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Consenso NAPeN / Metanálise 2024",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (Estimulação Vagal taVNS para Regulação Autonômica)",
                    "tecnica": "taVNS",
                    "alvo": "Trago auricular esquerdo",
                    "parametros": "25 Hz, intensidade sublimiar, 30 min",
                    "observacoes": "Modula reatividade autonômica, ansiedade e sintomas gastrointestinais comórbidos."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Após 5 sessões.",
                    "ajuste_dose": "Adaptar estímulo com reforço visual positivo para engajamento.",
                    "regra_interrupcao": "Interromper se agitação psicomotora persistente."
                },
                "contraindicacoes": ["Crises epilépticas", "Rejeição sensorial intransponível"],
                "notas_clinicas": "Indivíduos com nível de suporte 1 e 2 apresentam maior volume de dados reportados na literatura."
            }
        }
    },
    {
        "id": "alzheimer-ccl",
        "condicao": "Doença de Alzheimer e Declínio Cognitivo Leve (CCL)",
        "eixo": "Cognição & Demências",
        "roadmap_id": "RM12",
        "svg_file": "RM12.svg",
        "status_auditoria": "Consolidado (Meta-análise)",
        "nota_auditoria": "Metanálises recentes de estimulação combinada com treino cognitivo computadorizado (2024).",
        "no1_pergunta": "Qual é o estágio diagnóstico do paciente?",
        "fatores_limitantes": [
            {"id": "alzheimer_memoria", "label": "Doença de Alzheimer Leve a Moderada (Memória / Cognição Global)"},
            {"id": "ccl_cognicao", "label": "Declínio Cognitivo Leve — CCL (Memória Episódica)"},
            {"id": "sintomas_neuropsiquiatricos", "label": "Sintomas Neuropsiquiátricos (Apatia / Agitação)"}
        ],
        "modalidades": {
            "alzheimer_memoria": {
                "tecnica": "rTMS de Alta Frequência ou tDCS Anodal",
                "modalidade_sigla": "rTMS / tDCS",
                "alvo": "F3 (DLPFC Esquerdo) e/ou P3 (Parietal Esquerdo)",
                "frequencia": "20 Hz (F3) / 10 Hz (P3) ou corrente contínua",
                "intensidade": "100% LMR em F3 / 90% LMR em P3 / 2.0 mA no tDCS",
                "pulsos_duracao": "1.760 a 3.000 pulsos / 20–25 min no tDCS",
                "sessoes": "20 a 30 sessões diárias combinadas com tarefas de estimulação cognitiva",
                "escala_recomendada": "ADAS-cog e Mini-Exame do Estado Mental (MEEM)",
                "meta_melhora": "Estabilização ou melhora mensurável nos domínios de memória e orientação",
                "tamanho_efeito": "Melhora média de 32,64% na escala ADAS-cog e ganho de 9,0% a 21,9% no MEEM sustentados por até 3 meses",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Lefaucheur / IFCN: Nível B (Eficácia Provável na cognição global do Alzheimer leve)",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (tDCS Temporoparietal Bilateral)",
                    "tecnica": "tDCS",
                    "alvo": "T3 e P3 (ânodo) / supraorbitário (cátodo)",
                    "parametros": "2 mA, 25 min, a cada 10 dias reavaliação",
                    "observacoes": "Estimula circuitos temporais mediais cruciais para a consolidação de memória."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "A cada 10 sessões com o MEEM.",
                    "ajuste_dose": "O uso de benzodiazepínicos pode diminuir o efeito do tratamento. Monitorar comorbidades de sono.",
                    "regra_interrupcao": "Interromper se declínio acelerado com perda de capacidade de engajamento no treino."
                },
                "contraindicacoes": ["Metal no crânio", "Demência em fase avançada sem canal de comunicação"],
                "notas_clinicas": "A combinação com treino cognitivo imediato é indispensável para a indução de plasticidade sináptica duradoura."
            },
            "ccl_cognicao": {
                "tecnica": "tDCS Anodal sobre CPFDL",
                "modalidade_sigla": "tDCS",
                "alvo": "F3 (Córtex Pré-Frontal Dorsolateral Esquerdo)",
                "frequencia": "Corrente contínua",
                "intensidade": "2.0 mA",
                "pulsos_duracao": "20 minutos",
                "sessoes": "10 a 20 sessões",
                "escala_recomendada": "MEEM e Rivermead Behavioural Memory Test",
                "meta_melhora": "Ganho percentual significativo na recordação tardia e atenção executiva",
                "tamanho_efeito": "Melhora de 9,12% no MEEM e aumento médio de 29% na retenção de memória episódica",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Consenso NAPeN: Nível B",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (rTMS em Alta Frequência F3/P3)",
                    "tecnica": "rTMS 20 Hz",
                    "alvo": "F3",
                    "parametros": "20 Hz, 100% LMR, 2.000 pulsos",
                    "observacoes": "Facilitação direta da rede de modo padrão (DMN) e controle executivo."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Na 10ª sessão.",
                    "ajuste_dose": "Ajustar complexidade dos exercícios cognitivos conforme evolução.",
                    "regra_interrupcao": "Interromper se ausência de resposta após 15 sessões."
                },
                "contraindicacoes": ["Metal no crânio", "Crises epilépticas"],
                "notas_clinicas": "Intervenção preventiva precoce com potencial de retardar a conversão para demência estabelecida."
            },
            "sintomas_neuropsiquiatricos": {
                "tecnica": "tDCS / rTMS sobre Córtex Temporoparietal",
                "modalidade_sigla": "tDCS / rTMS",
                "alvo": "Córtex temporoparietal ou F3",
                "frequencia": "Anodal 2 mA ou 10 Hz excitatória",
                "intensidade": "2.0 mA / 90% LMR",
                "pulsos_duracao": "20 min",
                "sessoes": "10 sessões",
                "escala_recomendada": "Inventário Neuropsiquiátrico (NPI) e Escala de Depressão de Cornell",
                "meta_melhora": "Alívio expressivo da apatia e sintomas depressivos associados à demência",
                "tamanho_efeito": "Melhora de 60,9% no NPI e redução média de 43,3% na Escala de Cornell após 10 sessões",
                "evidencia": "Consolidada (Respaldo em Meta-análise)",
                "linha_fluxograma": "solida",
                "diretriz_internacional": "Consenso NAPeN: Nível B",
                "protocolo_alternativo": {
                    "nome": "Protocolo Alternativo (rTMS F3/F4 Bilateral)",
                    "tecnica": "rTMS",
                    "alvo": "F3 (alta) + F4 (baixa)",
                    "parametros": "10 Hz F3 + 1 Hz F4",
                    "observacoes": "Modulação de circuitos afetivos fronto-límbicos."
                },
                "sessoes_ajuste": {
                    "quando_reavaliar": "Na 5ª e 10ª sessão.",
                    "ajuste_dose": "Verificar se alterações de sono estão contribuindo para agitação vespertina.",
                    "regra_interrupcao": "Interromper se agitação piorar com o estímulo."
                },
                "contraindicacoes": ["Metal no crânio", "Delírios persecutórios agudos"],
                "notas_clinicas": "Excelente recurso não farmacológico para reduzir a sobrecarga dos cuidadores."
            }
        }
    }
]

# Write JSON
out_json = 'data/napen_roadmaps_data.json'
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump({
        "versao": "2025-2026",
        "data_extracao": "2026-11-04",
        "instituicao": "Rede NAPeN — Rede de Núcleos de Assistência e Pesquisa em Neuromodulação",
        "url_oficial": "https://www.neuromodulation-net.com/",
        "total_condicoes": len(conditions),
        "condicoes": conditions
    }, f, indent=2, ensure_ascii=False)

# Write JS
out_js = 'js/data.js'
with open(out_js, 'w', encoding='utf-8') as f:
    f.write('// Base Canônica de Dados dos Roadmaps NAPeN — Versão 2025–2026\n')
    f.write('window.NAPEN_DATA = window.NAPEN_ROADMAPS_DATA = ')
    json.dump({
        "versao": "2025-2026",
        "data_extracao": "2026-11-04",
        "instituicao": "Rede NAPeN — Rede de Núcleos de Assistência e Pesquisa em Neuromodulação",
        "url_oficial": "https://www.neuromodulation-net.com/",
        "total_condicoes": len(conditions),
        "condicoes": conditions
    }, f, indent=2, ensure_ascii=False)
    f.write(';\n')

print(f'Sucesso! Gerados {out_json} ({os.path.getsize(out_json)} bytes) e {out_js} ({os.path.getsize(out_js)} bytes).')
