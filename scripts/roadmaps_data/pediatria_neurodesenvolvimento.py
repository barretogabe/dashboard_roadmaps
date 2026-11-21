"""Official clinical decision trees, protocols, and contextual observations for Paralisia Cerebral (RM14) and Transtorno do Espectro Autista (RM15)."""

from scripts.roadmaps_data import (
    ADVERSE_BANK_URL,
    DIR_IFCN_RTMS_2020,
    DIR_IFCN_TDCS_2017,
    make_chain_step,
    make_mod,
    make_obs,
    make_ref,
    make_scale,
)

# RM14 Paralisia Cerebral
REF_ZHONG_2025_PC = make_ref("Zhong, M., et al.", 2025, "Safety and effectiveness of non-invasive brain stimulation on mobility and balance function in children with cerebral palsy: a systematic review and meta-analysis", "Journal of NeuroEngineering and Rehabilitation", "10.1186/s12984-025-01619-7", tipo="Metanálise de referência")
REF_ZHANG_2025_PC_MS = make_ref("Zhang, Y., et al.", 2025, "Non-invasive brain stimulation for upper extremity dysfunction in children with cerebral palsy: a systematic review and meta-analysis", "Translational Pediatrics", "10.21037/tp-24-488", tipo="Metanálise de referência")
REF_SALEEM_2019_PC = make_ref("Saleem, G. T., et al.", 2019, "Transcranial Direct Current Stimulation in Pediatric Motor Disorders: A Systematic Review and Meta-analysis", "Archives of Physical Medicine and Rehabilitation", "10.1016/j.apmr.2018.10.011", tipo="Metanálise de referência")
REF_GRECCO_2014_PC = make_ref("Grecco, L. A. C., et al.", 2014, "Transcranial direct current stimulation during treadmill training in children with cerebral palsy: a randomized controlled double-blind clinical trial", "Research in Developmental Disabilities", "10.1016/j.ridd.2014.07.030", tipo="Ensaio clínico de referência")
REF_GUPTA_2023_PC = make_ref("Gupta, J., et al.", 2023, "Brain Stimulation and Constraint Induced Movement Therapy in Children With Unilateral Cerebral Palsy: A Randomized Controlled Trial", "Neurorehabilitation and Neural Repair", "10.1177/15459683231174222", tipo="Ensaio clínico de referência")
REF_WAQAS_2025_PC = make_ref("Waqas, S., et al.", 2025, "Conjunct effects of transcranial direct current stimulation with mirror therapy on motor control and muscle performance in spastic quadriplegic cerebral palsy children: A randomized clinical trial", "Journal of Multidisciplinary Healthcare", "10.2147/JMDH.S506784", tipo="Ensaio clínico de referência")
REF_DUARTE_2014_PC = make_ref("Duarte, N. A. G., et al.", 2014, "Effect of transcranial direct current stimulation combined with gait and mobility training on functionality in children with cerebral palsy: A double-blind randomized controlled trial", "BMC Pediatrics", "10.1186/1471-2431-14-225", tipo="Ensaio clínico de referência")
REF_DADASHI_2019_PC = make_ref("Dadashi, F., et al.", 2019, "The Effects of Repetitive Transcranial Magnetic Stimulation (rTMS) on Balance Control in Children with Cerebral Palsy", "Annual International Conference of the IEEE EMBS", "10.1109/EMBC.2019.8857361", tipo="Ensaio clínico de referência")
REF_GRECCO_2017_PC = make_ref("Grecco, L. A., et al.", 2017, "Cerebellar transcranial direct current stimulation in children with ataxic cerebral palsy: A sham-controlled, crossover, pilot study", "Developmental Neurorehabilitation", "10.3109/17518423.2016.1139639", tipo="Ensaio clínico de referência")
REF_YOUNG_2014_PC = make_ref("Young, S. J., et al.", 2014, "Cathodal transcranial direct current stimulation in children with dystonia: a sham-controlled study", "Journal of Child Neurology", "10.1177/0883073813492385", tipo="Ensaio clínico de referência")

# RM15 Transtorno do Espectro Autista
REF_LIU_2023_TEA = make_ref("Liu, A., et al.", 2023, "Non-invasive brain stimulation for patient with autism: a systematic review and meta-analysis", "Frontiers in Psychiatry", "10.3389/fpsyt.2023.1147327", tipo="Metanálise de referência")
REF_CHEN_2024_TEA = make_ref("Chen, Y. B., et al.", 2024, "A network meta-analysis of non-invasive brain stimulation interventions for autism spectrum disorder: Evidence from randomized controlled trials", "Neuroscience & Biobehavioral Reviews", "10.1016/j.neubiorev.2024.105807", tipo="Metanálise de referência")
REF_SOKHADZE_2018_TEA = make_ref("Sokhadze, E. M., et al.", 2018, "Exploratory Study of rTMS Neuromodulation Effects on Electrocortical Functional Measures of Performance in an Oddball Test and Behavioral Symptoms in Autism", "Frontiers in Systems Neuroscience", "10.3389/fnsys.2018.00020", tipo="Ensaio clínico de referência")
REF_AMATACHAYA_2015_TEA = make_ref("Amatachaya, A., et al.", 2015, "The short-term effects of transcranial direct current stimulation on electroencephalography in children with autism: a randomized crossover controlled trial", "Behavioural Neurology", "10.1155/2015/928631", tipo="Ensaio clínico de referência")
REF_SOKHADZE_2014_TEA = make_ref("Sokhadze, E. M., et al.", 2014, "rTMS neuromodulation improves electrocortical functional measures of information processing and behavioral responses in autism", "Frontiers in Systems Neuroscience", "10.3389/fnsys.2014.00134", tipo="Ensaio clínico de referência")
REF_AUVICHAYAPAT_2023_TEA = make_ref("Auvichayapat, P., et al.", 2023, "Long-term effects of transcranial direct current stimulation in the treatment of autism spectrum disorder: A randomized controlled trial", "Developmental Medicine & Child Neurology", "10.1111/dmcn.15457", tipo="Ensaio clínico de referência")
REF_AYDIN_2025_TEA = make_ref("Aydin, A., & Yildirim, A.", 2025, "Assessing the impact of Transcranial Direct Current Stimulation (tDCS) over the dorsolateral prefrontal cortex on social communication in children and adolescents with Autism Spectrum Disorder (ASD)", "Research in Developmental Disabilities", "10.1016/j.ridd.2025.104958", tipo="Ensaio clínico de referência")


def _tol(o, a, f):
    return {"orientacao_tolerabilidade": o, "ajuste_seguranca": a, "fatores_moduladores": f}


def _audit(nivel, resumo, just, sinais, grade, forca, dom, tol):
    return {
        "amstar2_nivel": nivel, "amstar2_resumo": resumo, "amstar2_justificativa": just,
        "amstar2_sinais": sinais, "grade_certeza": grade, "grade_forca": forca,
        "grade_dominios": dom, "tolerabilidade": tol,
    }


def _build_pc():
    cid = "paralisia-cerebral"
    tags = {
        "coordenadas_10_20": ["C3", "C4", "Cz", "Fp1", "Fp2", "Inion", "Cerebelo Medial"],
        "alvos_anatomicos": ["Córtex Motor Primário (M1)", "Vértice Craniano (Cz)", "Região Cerebelar Medial (1 cm abaixo do ínion)"],
        "sinonimos_en": ["cerebral palsy", "spastic diplegia", "hemiplegic cerebral palsy", "tetraplegia", "pediatric motor rehabilitation"],
        "sintomas_pt": ["paralisia cerebral", "diparesia espástica", "hemiparesia espástica", "tetraparesia", "ataxia", "distonia", "marcha", "controle postural"],
        "escalas": ["GMFM-88", "6MWT", "10MWT", "PDMS-FM", "BBT", "QUEST", "FMA", "PBS"],
        "tecnicas": ["tDCS", "rTMS", "rTMS Priming 6Hz+1Hz"],
    }
    tol_pc = _tol(
        "Rampa tDCS recomendada: 10 segundos (subida/descida), ajustável às sensibilidades sensoriais pediátricas. Monitorar irritabilidade, cefaleia, fadiga e desconforto local.",
        "PAUSA IMEDIATA diante de qualquer sintoma neurológico agudo (confusão, alteração de consciência, sinais motores abruptos).",
        "Não aplicar com fontanelas abertas ou alterações craniofaciais (micro/macro/plagiocefalia); aguardar 3 a 4 meses entre ciclos.",
    )

    scale_gmfm = make_scale("gmfm_88", "Gross Motor Function Measure (GMFM-88 Dimensões D/E + 6MWT)", "GMFM-88 / 6MWT", "aumento", "Ganho ≥ 5,0% na GMFM-88 (e evolução na velocidade/distância de marcha no 6MWT)", 0.58, placeholder="Ex: 52", min_val=0, max_val=100, mcid_valor=5.0, mcid_label="+5,0% GMFM-88 / +25% marcha")
    scale_manip = make_scale("pdms_bbt_quest", "Destreza e Função Manual (PDMS-FM / BBT / QUEST / FMA)", "PDMS-FM / BBT / QUEST", "aumento", "Ganho ≥ 11,7% na QUEST ou 14,1% no BBT (e evolução clínica em PDMS-FM / FMA-MS)", 0.56, placeholder="Ex: 38", min_val=0, max_val=100, mcid_valor=5.0, mcid_label="+11,7% QUEST / +14,1% BBT")
    scale_pbs = make_scale("pbs_estab", "Pediatric Balance Scale (PBS / Mini-BESTest / Estabilometria)", "PBS / Mini-BESTest", "aumento", "Diparesia: +11,9% PBS e -27,6% oscilação ML | Hemiparesia: até 63% equilíbrio estático", 0.55, placeholder="Ex: 32", min_val=0, max_val=56, mcid_valor=3.6, mcid_label="+11,9% na PBS")

    adj_pc = {"titulo": "Segurança Pediátrica, Limite de 25 Sessões e Treinamento Ativo", "tolerabilidade": "Rampa tDCS recomendada de 10 s (ajustável a sensibilidades sensoriais); pausar imediatamente se sintoma neurológico agudo.", "dose_pulsos": "5 a 20 sessões (10 para tDCS, até 20 rTMS, 1×/dia; máximo ≤ 25 sessões totais incluindo desmame). Proibido protocolo acelerado (> 1 sessão/dia); respeitar intervalo mínimo de 3–4 meses entre ciclos.", "calibracao_limiar": "Associar treinamento ativo (esteira, contensão induzida) simultâneo ou imediatamente após a estimulação (priming)."}
    falha_pc = {"criterio": "Ausência de resposta clínica observável após 5 sessões quanto ao objetivo motor principal E sem benefícios secundários (sono, atenção, regulação emocional).", "conduta_oficial": "1. Verificar estabilidade clínica/EEG e maturação cortical;\n2. Evitar áreas alternativas não validadas em falha (literatura prioriza M1);\n3. Extrapolação cautelosa apenas sob critérios estritos de segurança, idade mínima e maturação cortical."}
    sa_pc = {"quando_reavaliar": "Reavaliar após 5 sessões quanto à função motora principal e benefícios secundários (sono, atenção, regulação emocional); aguardar 3–4 meses entre ciclos repetidos.", "ajuste_dose": "Manter treinamento motor/funcional ativo combinado durante ou logo após cada sessão.", "regra_interrupcao": "Pausa imediata em qualquer sintoma neurológico agudo."}

    modalidades = {
        "deficits_motores": make_mod(
            protocolo_id="RM14-LOC-DIP", tecnica="tDCS Anódica — C3/C4 Lesado + Supraorbital (Locomoção)", modalidade_sigla="tDCS Locomoção",
            alvo="Ânodo C3 ou C4 lesado + Cátodo supraorbital contralateral (25 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min (eletrodos 25 cm²; rampa 10 s)", sessoes="10 sessões (1×/dia)",
            escala_recomendada="GMFM-88 (D/E) / 6MWT / 10MWT / TUG / FMS", meta_melhora="+125% veloc. marcha, +100,6% 6MWT e +34,1% GMFM-E",
            tamanho_efeito=0.58, evidencia="Nível B — Metanálise Zhong 2025 / Grecco 2014", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Zhong et al., 2025 · Saleem et al., 2019)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_GRECCO_2014_PC, meta_analise=REF_ZHONG_2025_PC,
            mcid_valor=5.0, mcid_label="+27–34% GMFM / +100% 6MWT", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Grecco et al. (2014/2015) / Radwan et al. (2023)", efeito_resumo="+125% velocidade marcha e +34,1% GMFM-E após 10 sessões em esteira/RV",
            escalas_detalhadas=[scale_gmfm],
            cadeia_sequencial=[
                make_chain_step(1, "RM14-LOC-P1", "tDCS C3/C4 Lesado (Locomotora)", "tDCS Anódica — C3/C4 Lesado + Supraorbital (Grecco et al., 2014/2015)", "tDCS Anódica", "Ânodo C3 ou C4 lesado + Cátodo supraorbital contra (25 cm²)", "1,0 mA | 20 min | rampa 10 s", sessoes="10 sessões (1×/dia)", efeito_esperado="+125% veloc. marcha; +100,6% 6MWT; +34,1% GMFM-E", referencia="Grecco et al. (2014/2015) · DOI: 10.1016/j.ridd.2014.07.030"),
                make_chain_step(2, "RM14-LOC-P2", "tDCS Cz / Ínion (Locomotora)", "tDCS Anódica — Cz / Ínion (Radwan et al., 2023)", "tDCS Anódica", "Ânodo Cz + Cátodo Ínion (25 cm²)", "1,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="+45,8% veloc. marcha e +38,5% passada", referencia="Radwan et al. (2023) · DOI: 10.3390/children10020222"),
            ],
            ajuste_parametros=adj_pc, falha_terapeutica=falha_pc, sessoes_ajuste=sa_pc,
            notas_clinicas="GMFCS/MACS I–III e faixa etária típica 6–12 anos concentram a evidência mais robusta.",
            audit_meta=_audit("Baixa", "Metanálise mobilidade e equilíbrio na PC (Zhong et al., 2025).", "Benefício consistente quando combinada a treino locomotor em esteira.", ["Metanálise Pediátrica"], "Moderada", "Condicional", "Associar treinamento ativo durante ou logo após a sessão.", tol_pc),
            mod_tipo="tdcs",
        ),
        "pc_manip_hemi": make_mod(
            protocolo_id="RM14-MANIP-HEMI", tecnica="rTMS Sequencial 10 Hz Lesado + 1 Hz Não Lesado", modalidade_sigla="rTMS MS PC",
            alvo="M1 C3/C4 lesado (10 Hz) e não lesado (1 Hz), bobina figura em 8", frequencia="10 Hz lesado + 1 Hz não lesado", intensidade="90% LMR",
            pulsos_duracao="1.600 p (80×2s, 13s) + 960 p (80×12s, 3s)", sessoes="20 sessões (1×/dia)",
            escala_recomendada="PDMS-FM / BBT / QUEST / AHA / ABILHAND-Kids / 9HPT", meta_melhora="+49,7% na PDMS-FM e +31,4% na FMFM",
            tamanho_efeito=0.56, evidencia="Nível B — Zhang 2025 / Gupta 2023", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Zhang et al., 2025 · Metelski et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_GUPTA_2023_PC, meta_analise=REF_ZHANG_2025_PC_MS,
            mcid_valor=5.0, mcid_label="+11,7% QUEST / +14,1% BBT", cohen_d_valor=0.56, cohen_d_interp="Moderado",
            estudo_referencia="Ye 2019 / He 2022 / Gupta 2023", efeito_resumo="+49,7% PDMS-FM (rTMS sequencial), +14,1% BBT (tDCS) e +11,7% QUEST (priming)",
            escalas_detalhadas=[scale_manip],
            cadeia_sequencial=[
                make_chain_step(1, "RM14-MANIP-P1", "rTMS 10 Hz Lesado + 1 Hz Não Lesado", "rTMS Sequencial — 10 Hz Lesado + 1 Hz Não Lesado (Ye et al., 2019)", "rTMS Sequencial", "C3/C4 lesado (10 Hz) + C4/C3 não lesado (1 Hz), bobina figura em 8", "90% LMR | 1.600 p (80×2s, 13s) + 960 p (80×12s, 3s)", sessoes="20 sessões", efeito_esperado="+49,7% PDMS-FM e +31,4% FMFM", referencia="Ye et al. (2019) · Chinese Journal of Rehabilitation Medicine, 11:1368-1370", fase_etapa="inicial"),
                make_chain_step(2, "RM14-MANIP-P2", "tDCS 1,5 mA C3/C4 (Opção Paralela OU Pós-Ye 2019)", "tDCS Anódica — 1,5 mA C3/C4 + Supraorbital (He et al., 2022)", "tDCS Anódica", "Ânodo C3/C4 lesado + Cátodo supraorbital contra (25 cm²)", "1,5 mA | 20 min", sessoes="5 sessões", efeito_esperado="+14,1% BBT após 5 sessões", referencia="He et al. (2022) · Frontiers in Behavioral Neuroscience, 16:925122", fase_etapa="sequencia", observacoes="Opção paralela (OU) ao protocolo de rTMS Priming (Gupta et al., 2023) após resposta insatisfatória à rTMS sequencial; preferível quando há menor tolerância à rTMS ou faixa pré-escolar."),
                make_chain_step(3, "RM14-MANIP-P3", "rTMS Priming 6 Hz + 1 Hz Contralesional (Opção Paralela OU)", "rTMS Priming — 6 Hz + 1 Hz Contralesional (Gupta et al., 2023)", "rTMS Priming", "C3 ou C4 contralesional (bobina figura em 8)", "6 Hz (600 p) + 1 Hz (600 p) | 90% LMR | 20 min", sessoes="10 sessões", efeito_esperado="+11,7% QUEST com terapia de contensão induzida", referencia="Gupta et al. (2023) · DOI: 10.1177/15459683231174222", fase_etapa="sequencia", observacoes="Opção paralela (OU) à tDCS anódica (He et al., 2022) após resposta insatisfatória à rTMS sequencial, especialmente associada à terapia de contensão induzida."),
            ],
            ajuste_parametros=adj_pc, falha_terapeutica=falha_pc, sessoes_ajuste=sa_pc,
            notas_clinicas="Associar terapia de contensão induzida ou treino bimanual imediatamente após estimulação (priming).",
            audit_meta=_audit("Moderada", "Metanálise em função de membro superior na PC (Zhang et al., 2025).", "Opções complementares entre rTMS sequencial, tDCS e rTMS priming.", ["Risco de viés"], "Moderada", "Condicional", "Inclui opção de priming com terapia de contensão induzida.", tol_pc),
        ),
        "pc_manip_tetra": make_mod(
            protocolo_id="RM14-MANIP-TETRA", tecnica="tDCS Anódica Bilateral — C3/C4 (15 min/hemisfério)", modalidade_sigla="tDCS Bilateral",
            alvo="Ânodo C3 ou C4 lesado + Supraorbital contralateral (25 cm²)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="15 min por hemisfério (30 min total, eletrodos 25 cm²)", sessoes="10 sessões associadas à terapia espelho/funcional",
            escala_recomendada="FMA — Membros Superiores / BBT / QUEST", meta_melhora="+142,6% na pontuação FMA-Membros Superiores (DP 12,6%) após 10 sessões",
            tamanho_efeito=0.58, evidencia="Nível B — Waqas et al. 2025 / Zhang 2025", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Zhang et al., 2025)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_WAQAS_2025_PC, meta_analise=REF_ZHANG_2025_PC_MS,
            mcid_valor=5.0, mcid_label="+142,6% na FMA-MS", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Waqas et al. (2025)", efeito_resumo="Aumento de 142,6% na FMA-MS em 10 sessões",
            escalas_detalhadas=[scale_manip],
            cadeia_sequencial=[make_chain_step(1, "RM14-TETRA-P1", "tDCS Bilateral 2 mA (15 min/hemisfério)", "tDCS Bilateral — C3/C4 15 min/hemisfério (Waqas et al., 2025)", "tDCS Bilateral Sequencial", "C3 ou C4 + Supraorbital contralateral (25 cm²)", "2,0 mA | 15 min por hemisfério (30 min total)", sessoes="10 sessões", efeito_esperado="+142,6% FMA-MS", referencia="Waqas et al. (2025) · DOI: 10.2147/JMDH.S506784")],
            ajuste_parametros=adj_pc, falha_terapeutica=falha_pc, sessoes_ajuste=sa_pc,
            notas_clinicas="Monitorar aceitação sensorial nos dois hemisférios durante aplicação bilateral.",
            audit_meta=_audit("Moderada", "Metanálise membro superior na PC (Zhang et al., 2025).", "ECR recente em tetraparesia espástica (Waqas et al., 2025).", ["ECR 2025"], "Baixa", "Condicional", "Combinar com terapia funcional ativa.", tol_pc),
            mod_tipo="tdcs",
        ),
        "pc_estab_dip": make_mod(
            protocolo_id="RM14-EST-DIP", tecnica="tDCS Anódica — C3/C4 Lesado (Controle Postural)", modalidade_sigla="tDCS Postural",
            alvo="Ânodo C3/C4 lesado + Cátodo supraorbital contralateral (25 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min (eletrodos 25 cm²)", sessoes="10 sessões com treino de equilíbrio/marcha",
            escala_recomendada="PBS / Mini-BESTest / FRT / Estabilometria", meta_melhora="+11,9% na PBS e -24,7% a -29,6% na oscilação postural",
            tamanho_efeito=0.55, evidencia="Nível B — Zhong 2025 / Duarte 2014", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Zhong et al., 2025)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_DUARTE_2014_PC, meta_analise=REF_ZHONG_2025_PC,
            mcid_valor=3.6, mcid_label="+11,9% na PBS", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Duarte et al. (2014)", efeito_resumo="+11,9% na PBS e redução de ~27% na oscilação estabilométrica",
            escalas_detalhadas=[scale_pbs],
            cadeia_sequencial=[make_chain_step(1, "RM14-EST-DIP-P1", "tDCS 1 mA C3/C4 (Estab. Diparesia)", "tDCS Anódica — C3/C4 Controle Postural (Duarte et al., 2014)", "tDCS Anódica", "Ânodo C3/C4 + Cátodo supraorbital contra (25 cm²)", "1,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="+11,9% PBS e redução da oscilação do centro de pressão", referencia="Duarte et al. (2014) · DOI: 10.1186/1471-2431-14-225")],
            ajuste_parametros=adj_pc, falha_terapeutica=falha_pc, sessoes_ajuste=sa_pc,
            notas_clinicas="Usar PBS ou Mini-BESTest na rotina clínica quando estabilometria não disponível.",
            audit_meta=_audit("Baixa", "Metanálise mobilidade e equilíbrio na PC (Zhong et al., 2025).", "Ensaio duplo-cego com controle postural.", ["ECR duplo-cego"], "Moderada", "Condicional", "Associar treino de equilíbrio funcional.", tol_pc),
            mod_tipo="tdcs",
        ),
        "pc_estab_hemi": make_mod(
            protocolo_id="RM14-EST-HEMI", tecnica="LF-rTMS 1 Hz — C3/C4 Contralesional", modalidade_sigla="LF-rTMS Postural",
            alvo="C3 ou C4 (hemisfério contralesional — bobina figura em 8)", frequencia="1 Hz", intensidade="100% LMR",
            pulsos_duracao="1.200 pulsos (20 trens × 60 pulsos, 30 s IIT) | 20 min", sessoes="12 sessões",
            escala_recomendada="PBS / Mini-BESTest / Estabilometria", meta_melhora="Melhora de até 63% no equilíbrio estático após 12 sessões",
            tamanho_efeito=0.52, evidencia="Nível B/C — Dadashi 2019 / Saleem 2019", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Zhong et al., 2025)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_DADASHI_2019_PC, meta_analise=REF_SALEEM_2019_PC,
            mcid_valor=3.6, mcid_label="Melhora de equilíbrio estático (PBS)", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Dadashi et al. (2019)", efeito_resumo="Até 63% de melhora na oscilação do centro de pressão após 12 sessões",
            escalas_detalhadas=[scale_pbs],
            cadeia_sequencial=[make_chain_step(1, "RM14-EST-HEMI-P1", "rTMS 1 Hz C3/C4 Contralesional", "LF-rTMS 1 Hz — C3/C4 Contralesional (Dadashi et al., 2019)", "LF-rTMS (1 Hz)", "C3 ou C4 contralesional", "1 Hz | 100% LMR | 1.200 pulsos (20×60p, 30s IIT)", sessoes="12 sessões", efeito_esperado="Melhora de até 63% no equilíbrio estático", referencia="Dadashi et al. (2019) · DOI: 10.1109/EMBC.2019.8857361")],
            ajuste_parametros=adj_pc, falha_terapeutica=falha_pc, sessoes_ajuste=sa_pc,
            notas_clinicas="Triar epilepsia com EEG antes de aplicar rTMS em crianças.",
            audit_meta=_audit("Moderada", "Revisão pediátrica (Saleem et al., 2019 · Zhong et al., 2025).", "Evidência em controle postural para hemiparesia.", ["Pequena amostra"], "Baixa", "Condicional", "Respeitar idade ≥ 3–6 anos e triagem EEG.", tol_pc),
        ),
        "pc_ataxia": make_mod(
            protocolo_id="RM14-ATAXIA", tecnica="tDCS Cerebelar Medial 1 mA (Exploratório)", modalidade_sigla="tDCS Cerebelo (Exploratório)",
            alvo="Ânodo região cerebelar medial (1 cm abaixo do ínion) + cátodo supraorbital central (35 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min (eletrodos 35 cm²)", sessoes="10 sessões",
            escala_recomendada="PBS / Mini-BESTest / Estabilometria", meta_melhora="-23,6% oscilação ML e -20,4% AP de olhos fechados após 10 sessões",
            tamanho_efeito=0.45, evidencia="Nível C — Evidência exploratória (Grecco 2017)", linha_fluxograma="pontilhada",
            diretriz_internacional="Exploratório (Grecco et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_GRECCO_2017_PC, meta_analise=REF_SALEEM_2019_PC,
            mcid_valor=3.6, mcid_label="-20% a -24% na oscilação postural", cohen_d_valor=0.45, cohen_d_interp="Pequeno",
            estudo_referencia="Grecco et al. (2017)", efeito_resumo="Redução de 23,6% ML e 20,4% AP com olhos fechados",
            escalas_detalhadas=[scale_pbs],
            cadeia_sequencial=[make_chain_step(1, "RM14-ATAX-P1", "tDCS Cerebelar Medial (Exploratório)", "tDCS Cerebelar Medial (Grecco et al., 2017)", "tDCS Cerebelar (Exploratório)", "1 cm abaixo do ínion + supraorbital central (35 cm²)", "1,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="-23,6% ML / -20,4% AP", referencia="Grecco et al. (2017) · DOI: 10.3109/17518423.2016.1139639", linha_fluxograma="pontilhada")],
            ajuste_parametros=adj_pc, falha_terapeutica=falha_pc, sessoes_ajuste=sa_pc,
            notas_clinicas="Outras apresentações clínicas possuem evidência limitada; usar critérios individualizados.",
            audit_meta=_audit("Moderada", "Revisão pediátrica (Saleem et al., 2019).", "Estudo piloto crossover em PC atáxica.", ["Evidência exploratória"], "Muito Baixa", "Condicional", "Quadro exploratório tracejado.", tol_pc),
            mod_tipo="tdcs",
        ),
        "pc_distonia": make_mod(
            protocolo_id="RM14-DISTONIA", tecnica="tDCS Catódica Fracionada — C3/C4 Contralateral (Exploratório)", modalidade_sigla="tDCS Catódica (Exploratório)",
            alvo="Cátodo C3/C4 contralateral à mão mais afetada + Ânodo frontal oposto (35 cm²)", frequencia="Contínua fracionada", intensidade="1,0 mA",
            pulsos_duracao="9 min + pausa 20 min + 9 min (eletrodos 35 cm²)", sessoes="2 sessões",
            escala_recomendada="Observação clínica / Overflow eletromiográfico / PDMS-FM", meta_melhora="Redução de 1,5% da contração máxima no overflow contralateral (IC 95%: -2,2% a -0,7%)",
            tamanho_efeito=0.40, evidencia="Nível C — Evidência exploratória (Young 2014)", linha_fluxograma="pontilhada",
            diretriz_internacional="Exploratório (Young et al., 2014)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_YOUNG_2014_PC, meta_analise=REF_SALEEM_2019_PC,
            mcid_valor=1.5, mcid_label="-1,5% no overflow contralateral", cohen_d_valor=0.40, cohen_d_interp="Pequeno",
            estudo_referencia="Young et al. (2014)", efeito_resumo="Redução significativa da atividade de overflow contralateral",
            escalas_detalhadas=[scale_manip],
            cadeia_sequencial=[make_chain_step(1, "RM14-DIST-P1", "tDCS Catódica Fracionada (Exploratório)", "tDCS Catódica Fracionada (Young et al., 2014)", "tDCS Catódica (Exploratório)", "C3/C4 contralateral + região frontal oposta (35 cm²)", "1,0 mA | 9 min + 20 min pausa + 9 min", sessoes="2 sessões", efeito_esperado="-1,5% contração máxima de overflow", referencia="Young et al. (2014) · DOI: 10.1177/0883073813492385", linha_fluxograma="pontilhada")],
            ajuste_parametros=adj_pc, falha_terapeutica=falha_pc, sessoes_ajuste=sa_pc,
            notas_clinicas="Evidência limitada para distonia; aplicar apenas sob critérios clínicos estritos.",
            audit_meta=_audit("Moderada", "Revisão pediátrica (Saleem et al., 2019).", "Estudo controlado em distonia infantil.", ["Evidência exploratória"], "Muito Baixa", "Condicional", "Quadro exploratório em movimentos involuntários.", tol_pc),
            mod_tipo="tdcs",
        ),
    }

    arvore = {
        "roadmap_id": "RM14",
        "titulo_fluxograma": "Árvore de Decisão — Déficits Motores na Paralisia Cerebral",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é a habilidade motora prioritária / apresentação clínica na Paralisia Cerebral?",
                "subtitulo": "Evidência mais robusta concentra-se em PC espástica (GMFCS/MACS I–III) e idade 6–12 anos (extensões ≥ 3 a 28 anos).",
                "opcoes": [
                    {"id": "pc_locomotor", "rotulo": "Habilidades Locomotoras: Marcha / Mobilidade", "criterio": "GMFM-88 D/E, 6MWT, 10MWT, TUG, FMS", "descricao": "Diparesia Espástica -> tDCS C3/C4 lesado.", "proxima_etapa": "topo_locomotor"},
                    {"id": "pc_manipulativo", "rotulo": "Habilidades Manipulativas: Função motora fina / Bimanual / Espasticidade", "criterio": "BBT, PDMS-FM, FMFM, QUEST, FMA, EAM", "descricao": "Hemiparesia vs Tetraparesia Espástica.", "proxima_etapa": "topo_manipulativo"},
                    {"id": "pc_estabilizador", "rotulo": "Habilidades Estabilizadoras: Controle Postural", "criterio": "PBS, Mini-BESTest, FRT, Estabilometria", "descricao": "Diparesia vs Hemiparesia Espástica.", "proxima_etapa": "topo_estabilizador"},
                    {"id": "pc_outras", "rotulo": "Outras Apresentações Clínicas (Ataxia / Distonia — Evidência Exploratória)", "criterio": "Evidência limitada — usar cautela", "descricao": "Ataxia cerebelar ou movimentos involuntários / Distonia.", "proxima_etapa": "topo_outras"},
                ],
            },
            "topo_locomotor": {
                "pergunta": "Confirme a distribuição topográfica (Habilidades Locomotoras):",
                "subtitulo": "Córtex motor primário (M1).",
                "opcoes": [{"id": "loc_dip", "rotulo": "Diparesia Espástica", "criterio": "tDCS anódica C3/C4 lesado", "descricao": "+125% velocidade marcha e +34,1% GMFM-E.", "protocolo_alvo": "deficits_motores"}],
            },
            "topo_manipulativo": {
                "pergunta": "Qual é a distribuição topográfica (Habilidades Manipulativas)?",
                "subtitulo": "Córtex motor primário (M1).",
                "opcoes": [
                    {"id": "manip_hemi", "rotulo": "Hemiparesia Espástica", "criterio": "rTMS 10Hz+1Hz (opções sequenciais: tDCS / Priming)", "descricao": "+49,7% na PDMS-FM (Ye et al., 2019).", "protocolo_alvo": "pc_manip_hemi"},
                    {"id": "manip_tetra", "rotulo": "Tetraparesia Espástica", "criterio": "tDCS 2 mA bilateral (15 min/hemisfério)", "descricao": "+142,6% na FMA-MS (Waqas et al., 2025).", "protocolo_alvo": "pc_manip_tetra"},
                ],
            },
            "topo_estabilizador": {
                "pergunta": "Qual é a distribuição topográfica (Habilidades Estabilizadoras)?",
                "subtitulo": "Córtex motor primário (M1).",
                "opcoes": [
                    {"id": "est_dip", "rotulo": "Diparesia Espástica", "criterio": "tDCS 1 mA C3/C4", "descricao": "+11,9% na PBS e redução de oscilação postural.", "protocolo_alvo": "pc_estab_dip"},
                    {"id": "est_hemi", "rotulo": "Hemiparesia Espástica", "criterio": "rTMS 1 Hz C3/C4 contralesional", "descricao": "Até 63% de melhora no equilíbrio estático.", "protocolo_alvo": "pc_estab_hemi"},
                ],
            },
            "topo_outras": {
                "pergunta": "Qual apresentação exploratória deseja consultar?",
                "subtitulo": "Evidência limitada (estudos observacionais / crossover piloto); usar critérios individualizados.",
                "opcoes": [
                    {"id": "outras_ataxia", "rotulo": "Ataxia (Controle postural cerebelar)", "criterio": "tDCS 1 cm abaixo do ínion (1 mA, 20 min)", "descricao": "-23,6% oscilação ML (Grecco et al., 2017).", "protocolo_alvo": "pc_ataxia"},
                    {"id": "outras_distonia", "rotulo": "Distonia (Controle de movimentos involuntários)", "criterio": "tDCS catódica C3/C4 fracionada (9+20+9 min)", "descricao": "-1,5% overflow contralateral (Young et al., 2014).", "protocolo_alvo": "pc_distonia"},
                ],
            },
        },
        "ajuste_parametros": adj_pc,
        "protocolo_alternativo": {"nome": "tDCS Cz/Ínion ou rTMS Priming 6Hz+1Hz — Sequência", "tecnica": "tDCS / rTMS Priming", "alvo": "Cz/Ínion ou M1 contralesional", "parametros": "tDCS 1 mA 20 min ou Priming 6 Hz (600p) + 1 Hz (600p)", "observacoes": "Associar obrigatoriamente treinamento ativo funcional."},
        "protocolo_alternativo_2": {"nome": "Critério Pediátrico — Intervalo 3–4 Meses entre Ciclos (≤ 25 Sessões)", "tecnica": "Segurança Pediátrica", "alvo": "M1 prioritário (sem áreas alternativas na falha)", "parametros": "Máximo ≤ 25 sessões incluindo desmame; nunca > 1×/dia", "observacoes": "Extrapolação na falha apenas sob estritos critérios de segurança e maturação cortical."},
        "falha_terapeutica": {"id": "RM14-FALHA", "titulo": "Falha Terapêutica na Paralisia Cerebral", "criterios_definicao": "Critérios após 5 sessões sem resposta motora nem secundária (sono, atenção, regulação emocional) e ausência de resposta nos protocolos do ramo.", "descricao": "Literatura atual prioriza M1 e não contempla alvos alternativos na falha; considerar extrapolação cautelosa apenas se condições neurobiológicas semelhantes.", "condutas": ["Verificar se houve benefício secundário (sono, atenção, regulação emocional) em 5 sessões.", "Respeitar intervalo mínimo de 3–4 meses antes de eventual reindução em novo platô."]},
    }

    obs_pc = [
        make_obs("RM14-PRE-FONTANELA", "CRITÉRIO DE SEGURANÇA PEDIÁTRICA: não aplicar neuromodulação em crianças com fontanelas abertas ou alterações craniofaciais (microcefalia, macrocefalia, plagiocefalia) (Guillen et al., 2023). Realizar triagem neurológica e psiquiátrica prévia com EEG nos casos de epilepsia, crises febris ou uso de psicofármacos em dose estável (Allen et al., 2017).", "pre", categoria="seguranca", severidade="warning"),
        make_obs("RM14-STEP-ESP", "Crianças com PC espástica (hemiparética/diparética, GMFCS/MACS I–III) entre 6 e 12 anos (extensões ≥ 3 a 28 anos) concentram a evidência mais robusta. Outras apresentações (ataxia/distonia) têm evidência exploratória e a literatura prioriza M1 sem áreas alternativas validadas na falha.", "step", categoria="evidencia", etapa_ids=["fator_limitante", "topo_outras"]),
        make_obs("RM14-EXPLORATORIO-TEC", "Evidência exploratória (estudos piloto/observacionais): aplicar com cautela e critérios clínicos individualizados.", "tec", categoria="evidencia", protocolo_ids=["pc_ataxia", "pc_distonia"]),
        make_obs("RM14-SES-TREINO", "Acompanhar obrigatoriamente treinamento ativo (esteira, contensão induzida ou treino bimanual) simultâneo ou imediatamente após a estimulação (priming).", "sessoes", categoria="clinica", severidade="warning"),
        make_obs("RM14-PAUSA-AGUDA-TOL", "Monitoramento contínuo de irritabilidade, cefaleia, fadiga e desconforto local. Registrar eventos no Banco de Efeitos Adversos NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN", severidade="warning"),
        make_obs("RM14-FALHA-CAUTELA-STAGE", "Em falha terapêutica, extrapolação para protocolos indiretos só pode ocorrer respeitando idade mínima, maturação cortical e rigoroso monitoramento de segurança e tolerabilidade.", "stage", categoria="seguranca", estagios=["failure"]),
    ]

    return {
        "id": cid, "condicao": "Paralisia Cerebral", "eixo": "Neurodesenvolvimento",
        "roadmap_id": "RM14", "svg_file": "RM14.svg",
        "fatores_limitantes": [
            {"id": "deficits_motores", "nome": "Habilidades Locomotoras: Marcha e Mobilidade", "instrumento_sugerido": "GMFM-88 D/E / 6MWT / 10MWT", "descricao": "Velocidade, cadência e distância na diparesia espástica."},
            {"id": "pc_manip_hemi", "nome": "Habilidades Manipulativas: Função motora fina / Bimanual / Espasticidade", "instrumento_sugerido": "PDMS-FM / BBT / QUEST / FMA", "descricao": "Destreza e função de membro superior (hemiparesia/tetraparesia)."},
            {"id": "pc_estab_dip", "nome": "Habilidades Estabilizadoras: Controle Postural", "instrumento_sugerido": "PBS / Mini-BESTest / FRT", "descricao": "Equilíbrio estático e dinâmico."},
            {"id": "pc_ataxia", "nome": "Outras Apresentações Clínicas: Ataxia ou Distonia", "instrumento_sugerido": "PBS / Avaliação Funcional", "descricao": "Protocolos exploratórios para ataxia e distonia."},
        ],
        "arvore_algoritmo": arvore, "observacoes_contextuais": obs_pc, "modalidades": modalidades, "tags_busca": tags,
    }


def _build_tea():
    cid = "transtorno-espectro-autista"
    tags = {
        "coordenadas_10_20": ["F3", "F4", "Fp1", "Fp2", "FC1", "FC2", "CP5", "CP6", "Cerebelo Direito"],
        "alvos_anatomicos": ["CPFDL (F3/F4)", "Junção Temporoparietal Bilateral (CP5/CP6 HD-tDCS)", "Bilateral Motor/Pré-Frontal (FC1/FC2)", "Cerebelo Direito"],
        "sinonimos_en": ["autism", "autism spectrum disorder", "asd", "irritability", "repetitive behavior", "social interaction", "social communication"],
        "sintomas_pt": ["autismo", "déficits comportamentais", "irritabilidade", "hiperatividade", "comportamentos repetitivos", "estereotipias", "déficits sociais", "déficits em comunicação"],
        "escalas": ["ATEC", "ABC", "RBS-R", "SRS-2", "FER", "GARS-2", "VABS", "CGI"],
        "tecnicas": ["rTMS 1Hz", "tDCS", "HD-tDCS CP5/CP6"],
    }
    tol_tea = _tol(
        "VIGILÂNCIA ATÉ 24H PÓS-SESSÃO (Gupta & Adnan, 2018): observar fala excessiva, agitação psicomotora, insônia, euforia, impulsividade ou irritabilidade acentuada.",
        "Condutas escalonadas na intensificação de sintomas: (1) espaçar sessões (2–3×/sem); (2) reduzir intensidade/duração ou trocar alvo; (3) suspender se risco de hipomania/descompensação.",
        "Monitorar aceitação tátil e auditiva durante posicionamento de eletrodos/bobina em crianças com hipersensibilidade.",
    )

    scale_abc = make_scale("abc_irrit", "Autism Behavior Checklist (ABC) / Irritabilidade e Hiperatividade", "ABC / ATEC / CBCL", "reducao", "Redução ≥ 40% na Irritabilidade e Hiperatividade na ABC", 0.56, placeholder="Ex: 26", min_val=0, max_val=158, mcid_valor=5.0, mcid_label="-40% na Irritabilidade ABC")
    scale_rbs = make_scale("rbs_r", "Repetitive Behavior Scale-Revised (RBS-R)", "RBS-R / GARS", "reducao", "Redução ≥ 22% a 35% no escore da RBS-R", 0.54, placeholder="Ex: 34", min_val=0, max_val=129, mcid_valor=6.0, mcid_label="-22% a -35% na RBS-R")
    scale_srs = make_scale("srs_2", "Social Responsiveness Scale (SRS-2) / FER / ATEC Sociabilidade", "SRS-2 / ATEC / FER", "reducao", "Redução ≥ 24% na SRS-2 ou ganho em reconhecimento emocional e sociabilidade", 0.55, placeholder="Ex: 82", min_val=0, max_val=195, mcid_valor=10.0, mcid_label="-24% SRS-2 / +69,6% FER")

    adj_tea = {"titulo": "Vigilância 24h, Condutas Escalonadas e Proibição Acelerada", "tolerabilidade": "Vigilância até 24h pós-sessão (Gupta & Adnan, 2018): observar fala excessiva, agitação, insônia, euforia, impulsividade ou irritabilidade. Condutas escalonadas: (1) espaçar sessões (ex.: 5×/sem para 2–3×/sem); (2) reduzir mA/% LMR ou trocar alvo; (3) suspender definitivamente se risco de hipomania/descompensação.", "dose_pulsos": "Ciclo de 5 a 20 sessões (tDCS 5×/sem; rTMS 1–2×/sem; máximo ≤ 20 sessões). Protocolos acelerados (> 1 sessão/dia) são contraindicados em crianças; aguardar 3–4 meses entre ciclos.", "calibracao_limiar": "Iniciar neuromodulação somente com psicofármacos em dose estável, mantendo o esquema basal sem alterações durante o ciclo."}
    falha_tea = {"criterio": "Ausência de resposta após 5 sessões quanto ao objetivo principal E sem benefícios secundários (sono, atenção, regulação emocional) após sequência de protocolos e mudanças de alvo.", "conduta_oficial": "1. Conferir aceitação tátil/auditiva e estabilidade de psicofármacos;\n2. Seguir escada de 3 condutas caso haja intensificação de sintomas nas 24h;\n3. Na falha, considerar extrapolação cautelosa apenas respeitando idade, maturação cortical e equipe interdisciplinar."}
    sa_tea = {"quando_reavaliar": "Realizar avaliação cognitiva breve pré e pós-ciclo e reavaliar após 5 sessões quanto à resposta clínica principal e benefícios secundários (sono, atenção, regulação emocional).", "ajuste_dose": "Associar obrigatoriamente tarefas sociais, de atenção ou linguagem durante/logo após a estimulação (priming).", "regra_interrupcao": "Suspender definitivamente se sinais de hipomania ou descompensação psiquiátrica."}

    def _tea_rtms_step(ordem):
        return make_chain_step(ordem, "RM15-COMP-P1", "rTMS 1 Hz Rotação F3/F4/Bilateral (Crianças Maiores / Adultos)", "LF-rTMS 1 Hz — Rotação F3, F4 e Bilateral (Sokhadze et al., 2018)", "LF-rTMS (1 Hz)", "Rotação F3, F4 e Bilateral (1 alvo a cada 6 sessões)", "1 Hz | 90% LMR | 180 p/sessão (9 trens × 20 p)", sessoes="18 sessões (1–2×/sem)", efeito_esperado="-43,3% Irritabilidade e -41% Hiperatividade na ABC", referencia="Sokhadze et al. (2018) · DOI: 10.3389/fnsys.2018.00020")

    def _tea_tdcs_step(ordem):
        return make_chain_step(ordem, "RM15-COMP-P2", "tDCS Anódica F3 + Deltoide Direito (Preferencial ≤ 5–6 anos)", "tDCS Anódica — F3 + Deltoide Direito (Amatachaya et al., 2015)", "tDCS Anódica", "Ânodo F3 + Cátodo deltoide direito (35 cm²)", "1,0 mA | 20 min", sessoes="10 sessões (5×/sem)", efeito_esperado="-40% a -43,3% Irritabilidade e -37,8% a -41% Hiperatividade ABC", referencia="Amatachaya et al. (2015) · DOI: 10.1155/2015/928631")

    modalidades = {
        "comportamental": make_mod(
            protocolo_id="RM15-COMP-TDCS", tecnica="tDCS Anódica — F3 + Deltoide Direito (≤ 5–6 anos)", modalidade_sigla="tDCS F3 Infantil",
            alvo="Ânodo F3 + Cátodo deltoide direito (35 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min (35 cm²)", sessoes="10 sessões (5×/sem)",
            escala_recomendada="ABC / ATEC (Saúde e Problemas Comportamentais) / CBCL / Conners", meta_melhora="-40% a -43,3% Irritabilidade e -37,8% a -41% Hiperatividade na ABC",
            tamanho_efeito=0.56, evidencia="Nível B/C — Metanálise Liu 2023 / Chen 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B/C (Liu et al., 2023 · Fregni et al., 2021)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_AMATACHAYA_2015_TEA, meta_analise=REF_LIU_2023_TEA,
            mcid_valor=5.0, mcid_label="-40% na Irritabilidade ABC", cohen_d_valor=0.56, cohen_d_interp="Moderado",
            estudo_referencia="Amatachaya et al. (2015) / Qiu et al. (2021)", efeito_resumo="Redução de 40%–43,3% na Irritabilidade e 37,8%–41% na Hiperatividade ABC",
            escalas_detalhadas=[scale_abc],
            escalas_por_fator={"comportamental": ["abc_irrit"]},
            cadeia_sequencial=[_tea_tdcs_step(1), _tea_rtms_step(2)],
            ajuste_parametros=adj_tea, falha_terapeutica=falha_tea, sessoes_ajuste=sa_tea,
            notas_clinicas="Neuromodulação NÃO é terapia de 1ª linha no TEA; tDCS é preferível em crianças menores (≤ 5–6 anos) pela melhor tolerabilidade.",
            audit_meta=_audit("Moderada", "Metanálise NIBS no TEA (Liu et al., 2023 · Chen et al., 2024).", "Maior parte dos estudos em QI > 80; triagem psiquiátrica/neurológica e vigilância 24h obrigatórias.", ["Heterogeneidade pediátrica"], "Baixa", "Condicional", "Associar tarefas comportamentais/sociais.", tol_tea),
            mod_tipo="tdcs",
        ),
        "tea_comp_rtms": make_mod(
            protocolo_id="RM15-COMP-RTMS", tecnica="LF-rTMS 1 Hz — Rotação F3, F4 e Bilateral", modalidade_sigla="rTMS 1Hz TEA",
            alvo="Rotação de alvo: F3, F4 e Bilateral (1 alvo a cada 6 sessões, bobina figura em 8)", frequencia="1 Hz", intensidade="90% LMR",
            pulsos_duracao="180 pulsos/sessão (9 trens × 20 pulsos)", sessoes="18 sessões (1–2×/sem predominante)",
            escala_recomendada="ABC / ATEC / CBCL / Conners", meta_melhora="-43,3% Irritabilidade e -41% Hiperatividade na ABC após 18 sessões",
            tamanho_efeito=0.58, evidencia="Nível B/C — Sokhadze 2018 / Liu 2023", linha_fluxograma="solida",
            diretriz_internacional="Nível B/C (Liu et al., 2023)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_SOKHADZE_2018_TEA, meta_analise=REF_LIU_2023_TEA,
            mcid_valor=5.0, mcid_label="-43,3% Irritabilidade ABC", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Sokhadze et al. (2018)", efeito_resumo="Redução de 43,3% em Irritabilidade e 41% em Hiperatividade após 18 sessões",
            escalas_detalhadas=[scale_abc],
            escalas_por_fator={"comportamental": ["abc_irrit"]},
            cadeia_sequencial=[_tea_rtms_step(1), _tea_tdcs_step(2)],
            ajuste_parametros=adj_tea, falha_terapeutica=falha_tea, sessoes_ajuste=sa_tea,
            notas_clinicas="Neuromodulação NÃO é terapia de 1ª linha no TEA; LF-rTMS é preferível para crianças maiores, adolescentes e adultos.",
            audit_meta=_audit("Moderada", "Metanálise TEA (Liu et al., 2023).", "Rotação progressiva F3, F4 e Bilateral a cada 6 sessões.", ["Risco de viés"], "Baixa", "Condicional", "Vigilância de 24h obrigatória para agitação/hipomania.", tol_tea),
        ),
        "tea_repetitivos": make_mod(
            protocolo_id="RM15-REP", tecnica="LF-rTMS 1 Hz — F3 (CPFDL Esquerdo)", modalidade_sigla="rTMS F3 Repetitivos",
            alvo="F3 (CPFDL esquerdo)", frequencia="1 Hz", intensidade="90% LMR",
            pulsos_duracao="180 pulsos/sessão (9 trens × 20 p, 20–30 s IIT)", sessoes="18 sessões (1–2×/sem)",
            escala_recomendada="RBS-R / GARS / Observação clínica estruturada", meta_melhora="~35% de redução na RBS-R (78% respondedores)",
            tamanho_efeito=0.54, evidencia="Nível B/C — Chen 2024 / Sokhadze 2014 (HD-tDCS exploratório)", linha_fluxograma="solida",
            diretriz_internacional="Nível B/C (Chen et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_SOKHADZE_2014_TEA, meta_analise=REF_CHEN_2024_TEA,
            mcid_valor=6.0, mcid_label="-35% escore total RBS-R", cohen_d_valor=0.54, cohen_d_interp="Moderado",
            estudo_referencia="Sokhadze et al. (2014/2018) / Luckhardt et al. (2025)", efeito_resumo="~35% de redução na RBS-R em 78% dos pacientes após 18 sessões",
            escalas_detalhadas=[scale_rbs],
            escalas_por_fator={"tea_repetitivos": ["rbs_r"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM15-REP-P1", "LF-rTMS 1 Hz F3 (Comportamentos Repetitivos)", "LF-rTMS 1 Hz — F3 (Sokhadze et al., 2014)", "LF-rTMS (1 Hz)", "F3 (CPFDL esquerdo)", "1 Hz | 90% LMR | 180 pulsos (9×20p, 20–30 s IIT)", sessoes="18 sessões (1–2×/sem)", efeito_esperado="-35% RBS-R (78% com melhora clínica)", referencia="Sokhadze et al. (2014) · DOI: 10.3389/fnsys.2014.00134"),
                _tea_rtms_step(2),
                make_chain_step(3, "RM15-REP-P3", "HD-tDCS Anódica Bilateral CP5/CP6 (Mudança de Alvo Exploratória)", "HD-tDCS Multicanal — CP5/CP6 (Luckhardt et al., 2025)", "HD-tDCS Multicanal (Exploratório)", "Junção temporoparietal bilateral (CP5/CP6)", "2,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="Melhora de 21,9% em Compulsive Behavior na RBS-R", referencia="Luckhardt et al. (2025) · DOI: 10.1002/aur.3057", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
            ],
            ajuste_parametros=adj_tea, falha_terapeutica=falha_tea, sessoes_ajuste=sa_tea,
            notas_clinicas="Na ausência de resposta às montagens frontais (F3/F4), a seção de ajustes indica mudança de alvo exploratória para HD-tDCS CP5/CP6.",
            audit_meta=_audit("Moderada", "Metanálise em rede no TEA (Chen et al., 2024).", "Consistência de 1 Hz F3 em comportamentos repetitivos e estereotipias.", ["Análise em rede"], "Baixa", "Condicional", "Mudança para CP5/CP6 tem nível exploratório.", tol_tea),
        ),
        "social": make_mod(
            protocolo_id="RM15-SOC", tecnica="tDCS Anódica — F3 + Deltoide Direito (Déficits Sociais)", modalidade_sigla="tDCS F3 Social",
            alvo="Ânodo F3 + Cátodo deltoide direito (35 cm²)", frequencia="Contínua", intensidade="1,0 a 2,0 mA",
            pulsos_duracao="20 min (eletrodo 35 cm²)", sessoes="10 a 20 sessões associadas a treino de habilidades sociais",
            escala_recomendada="SRS-2 / ATEC (Sociabilidade) / FER / VABS / GARS-2", meta_melhora="+69,6% FER e +12,5% na subescala de sociabilidade ATEC",
            tamanho_efeito=0.55, evidencia="Nível B/C — Metanálise Chen 2024 / Auvichayapat 2023", linha_fluxograma="solida",
            diretriz_internacional="Nível B/C (Chen et al., 2024 · García-González et al., 2021)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_AUVICHAYAPAT_2023_TEA, meta_analise=REF_CHEN_2024_TEA,
            mcid_valor=10.0, mcid_label="+69,6% FER / -24,3% SRS-2", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Auvichayapat et al. (2023)", efeito_resumo="Cadeia progressiva de montagens frontais até mudança de alvo para cerebelo direito",
            escalas_detalhadas=[scale_srs],
            escalas_por_fator={"social": ["srs_2"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM15-SOC-P1", "tDCS F3 + Deltoide Direito", "tDCS Anódica — F3 + Deltoide Direito (Auvichayapat et al., 2023)", "tDCS Anódica", "Ânodo F3 + Cátodo deltoide D (35 cm²)", "1–2 mA | 20 min", sessoes="10–20 sessões", efeito_esperado="+69,6% FER e +12,5% ATEC", referencia="Auvichayapat et al. (2023) · DOI: 10.1111/dmcn.15457"),
                make_chain_step(2, "RM15-SOC-P2", "tDCS Bifrontal F3 / F4", "tDCS Bifrontal — Ânodo F3 + Cátodo F4 (Zemestani et al., 2022)", "tDCS Bifrontal", "Ânodo F3 + Cátodo F4 (25 cm²)", "1,5 mA | 15 min", sessoes="10 sessões", efeito_esperado="+30,8% ToM e +11,6% GARS-2", referencia="Zemestani et al. (2022) · DOI: 10.1002/aur.2803"),
                make_chain_step(3, "RM15-SOC-P3", "tDCS Pré-Frontal Cátodo F3 + Ânodo Fp2", "tDCS Pré-Frontal — Cátodo F3 + Ânodo Fp2 (Han et al., 2022)", "tDCS Pré-Frontal", "Cátodo F3 + Ânodo Fp2 (25 cm²)", "1,5 mA | 20 min", sessoes="10 sessões", efeito_esperado="-24,3% SRS-2 e +31,5% reconhecimento emocional", referencia="Han et al. (2022) · DOI: 10.1016/j.brs.2022.02.004"),
                make_chain_step(4, "RM15-SOC-P4", "tDCS Bilateral FC1 / FC2", "tDCS Bilateral — Ânodos FC1/FC2 + Cátodos Fp1/Fp2 (Hadoush et al., 2020)", "tDCS Bilateral", "Ânodos FC1/FC2 + Cátodos Fp1/Fp2 (8 cm²)", "1,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="-23,5% ATEC Sociability", referencia="Hadoush et al. (2020) · DOI: 10.1002/aur.2290"),
                make_chain_step(5, "RM15-SOC-P5", "tDCS Cerebelo Direito + Ânodo F3 (Mudança de Alvo Exploratória)", "tDCS Cerebelar — Cátodo Cerebelo D + Ânodo F3 (D'Urso et al., 2021)", "tDCS Cerebelar (Exploratório)", "Cátodo cerebelo direito + Ânodo F3 (25 cm²)", "1,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="-35% Lethargy/Social Withdrawal na ABC", referencia="D'Urso et al. (2021) · DOI: 10.3390/jcm11010143", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
            ],
            ajuste_parametros=adj_tea, falha_terapeutica=falha_tea, sessoes_ajuste=sa_tea,
            notas_clinicas="Após falha das montagens frontais e motoras (F3/F4 e FC1/FC2), a seção de ajustes indica mudança de alvo exploratória para cerebelo direito.",
            audit_meta=_audit("Moderada", "Metanálise em rede no TEA (Chen et al., 2024).", "Cadeia progressiva bem definida até mudança para cerebelo D.", ["Análise em rede"], "Baixa", "Condicional", "Associar treino de habilidades sociais (priming).", tol_tea),
            mod_tipo="tdcs",
        ),
        "tea_comunicacao": make_mod(
            protocolo_id="RM15-COM", tecnica="tDCS Anódica — F3 / Fp2 Comunicação (Exploratório)", modalidade_sigla="tDCS Comunicação (Exploratório)",
            alvo="Ânodo F3 + Cátodo Fp2", frequencia="Contínua", intensidade="1,5 a 1,8 mA",
            pulsos_duracao="30 min", sessoes="20 sessões",
            escala_recomendada="SRS-2 (Subescalas Comunicação Verbal e Não Verbal) / GARS-2", meta_melhora="+25,0% a 28,6% na comunicação (SRS-2) após 20 sessões",
            tamanho_efeito=0.46, evidencia="Nível C — Evidência exploratória (Aydin & Yildirim, 2025)", linha_fluxograma="pontilhada",
            diretriz_internacional="Exploratório (Aydin & Yildirim, 2025)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_AYDIN_2025_TEA, meta_analise=REF_CHEN_2024_TEA,
            mcid_valor=10.0, mcid_label="+25–28,6% comunicação SRS-2", cohen_d_valor=0.46, cohen_d_interp="Pequeno",
            estudo_referencia="Aydin & Yildirim (2025)", efeito_resumo="Melhora de 25%–28,6% nas subescalas de comunicação verbal e não verbal da SRS-2",
            escalas_detalhadas=[scale_srs],
            escalas_por_fator={"tea_comunicacao": ["srs_2"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM15-COM-P1", "tDCS F3 / Fp2 Comunicação (Exploratório)", "tDCS Anódica — F3 / Fp2 Comunicação (Aydin & Yildirim, 2025)", "tDCS Anódica (Exploratória)", "Ânodo F3 + Cátodo Fp2", "1,5 a 1,8 mA | 30 min", sessoes="20 sessões", efeito_esperado="25,0% a 28,6% comunicação na SRS-2", referencia="Aydin & Yildirim (2025) · DOI: 10.1016/j.ridd.2025.104958", linha_fluxograma="pontilhada", fase_etapa="inicial"),
            ],
            ajuste_parametros=adj_tea, falha_terapeutica=falha_tea, sessoes_ajuste=sa_tea,
            notas_clinicas="Classificado em 'Outros desfechos — Evidência exploratória' com protocolo único de tDCS anódica F3/Fp2; em ausência de resposta após o ciclo, caracteriza-se falha terapêutica.",
            audit_meta=_audit("Moderada", "Metanálise em rede no TEA (Chen et al., 2024).", "Ensaio recente de comunicação em tDCS F3/Fp2 (protocolo único exploratório).", ["Evidência exploratória"], "Muito Baixa", "Condicional", "Associar tarefas estruturadas de linguagem.", tol_tea),
            mod_tipo="tdcs",
        ),
    }

    arvore = {
        "roadmap_id": "RM15",
        "titulo_fluxograma": "Árvore de Decisão — Regulação Multidimensional no Transtorno do Espectro Autista",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante na Regulação Multidimensional?",
                "subtitulo": "A neuromodulação NÃO é terapia de primeira linha; considerar nível de suporte (DSM-5), DI, QI (> 80 na maioria dos estudos) e comorbidades.",
                "opcoes": [
                    {"id": "comportamental", "rotulo": "Déficits Comportamentais (Irritabilidade, Hiperatividade, Impulsividade)", "criterio": "ABC / ATEC (Saúde e Problemas Comportamentais) / CBCL / Conners", "descricao": "Escolha de modalidade guiada pela idade.", "proxima_etapa": "idade_modalidade_tea"},
                    {"id": "tea_repetitivos", "rotulo": "Comportamentos Repetitivos (Estereotipias, Compulsões, Resistência à mudança)", "criterio": "RBS-R / GARS", "descricao": "Inicia com LF-rTMS 1 Hz em F3 (Sokhadze et al., 2014).", "protocolo_alvo": "tea_repetitivos"},
                    {"id": "social", "rotulo": "Déficits Sociais (Reciprocidade social, Contato visual, Engajamento)", "criterio": "SRS-2 / ATEC Sociabilidade / FER / VABS", "descricao": "Inicia com tDCS anódica F3 + deltoide direito (Auvichayapat et al., 2023).", "protocolo_alvo": "social"},
                    {"id": "tea_comunicacao", "rotulo": "Déficits em Comunicação (Outros desfechos — Evidência Exploratória)", "criterio": "SRS-2 Subescalas Comunicação", "descricao": "Inicia com tDCS F3/Fp2 1,5–1,8 mA (Aydin & Yildirim, 2025).", "protocolo_alvo": "tea_comunicacao"},
                ],
            },
            "idade_modalidade_tea": {
                "pergunta": "Qual faixa etária e modalidade está indicada para Déficits Comportamentais?",
                "subtitulo": "Recomendação clínica: tDCS em crianças menores (≤ 5–6 anos) pela tolerabilidade/segurança; rTMS em crianças maiores, adolescentes e adultos.",
                "opcoes": [
                    {"id": "tea_menor_tdcs", "rotulo": "Criança menor (≤ 5–6 anos) — tDCS Anódica F3", "criterio": "Melhor tolerabilidade e segurança nesta faixa etária", "descricao": "tDCS 1 mA, 20 min, ânodo F3 / cátodo deltoide direito.", "protocolo_alvo": "comportamental"},
                    {"id": "tea_maior_rtms", "rotulo": "Criança maior (> 6 anos), Adolescente ou Adulto — rTMS 1 Hz", "criterio": "90% LMR | rotação F3, F4 e Bilateral a cada 6 sessões", "descricao": "Inicia com rTMS 1 Hz (180 pulsos/sessão).", "protocolo_alvo": "tea_comp_rtms"},
                ],
            },
        },
        "ajuste_parametros": adj_tea,
        "protocolo_alternativo": {"nome": "Mudança de Alvo (Exploratória) — HD-tDCS CP5/CP6 ou tDCS Cerebelo D", "tecnica": "HD-tDCS / tDCS Cerebelar", "alvo": "CP5/CP6 ou Cerebelo direito", "parametros": "HD-tDCS CP5/CP6 2 mA 20 min ou Cerebelo D 1 mA 20 min", "observacoes": "Evidência exploratória para falha em CPFDL."},
        "protocolo_alternativo_2": {"nome": "Vigilância 24h & Condutas Escalonadas — Manejo de Tolerabilidade TEA", "tecnica": "Manejo de Tolerabilidade TEA", "alvo": "Seguimento pós-sessão até 24h", "parametros": "Espaçar para 2–3×/sem; reduzir mA/%LMR/trens; suspender se hipomania", "observacoes": "Monitorar fala excessiva, agitação, insônia, euforia, impulsividade e irritabilidade por 24h."},
        "falha_terapeutica": {"id": "RM15-FALHA", "titulo": "Falha Terapêutica no Transtorno do Espectro Autista", "criterios_definicao": "Critérios após 5 sessões sem resposta cognitiva/comportamental principal nem secundária (sono, atenção, regulação emocional) e conclusão das mudanças de alvo.", "descricao": "Respeitar intervalo de 3–4 meses entre ciclos; considerar extrapolação cautelosa apenas sob critérios de segurança, idade e maturação cortical.", "condutas": ["Seguir 3 condutas escalonadas em qualquer intensificação de sintomas nas 24h.", "Reavaliar comorbidades e epilepsia com neurologista/psiquiatra."]},
    }

    obs_tea = [
        make_obs("RM15-PRE-NAO-PRIMEIRA-LINHA", "ELEGIBILIDADE E TRIAGEM INTEGRAL: a neuromodulação NÃO é terapia de 1ª linha no TEA. A maioria dos estudos inclui QI > 80 (alto funcionamento / leve-moderado); considerar nível de suporte (DSM-5), DI e comorbidades. Não aplicar com fontanelas abertas ou alterações craniofaciais (Guillen et al., 2023). Realizar triagem psiquiátrica/neurológica/comportamental; em epilepsia, avaliar com neurologista/EEG e, se as crises forem o limitante principal, priorizar protocolo direcionado à epilepsia (Hawas et al., 2025).", "pre", categoria="seguranca", severidade="warning"),
        make_obs("RM15-IDADE-MODALIDADE-STEP", "FAIXA ETÁRIA POR MODALIDADE: recomenda-se preferencialmente tDCS em crianças menores (≤ 5–6 anos) pela melhor tolerabilidade e segurança, e rTMS em crianças maiores, adolescentes e adultos.", "step", categoria="clinica", etapa_ids=["idade_modalidade_tea", "fator_limitante"]),
        make_obs("RM15-EXPLORATORIO-TEC", "Evidência exploratória (estudos observacionais/relatos): mudança de alvo para junção temporoparietal CP5/CP6 ou cerebelo D e o ramo Déficits em Comunicação.", "tec", categoria="evidencia", protocolo_ids=["tea_comunicacao", "tea_repetitivos", "social"], estagios=["primary", "alt1", "alt2"]),
        make_obs("RM15-VIGILANCIA-24H-TOL", "Monitorar aceitação tátil e auditiva durante posicionamento de eletrodos/bobina em crianças com hipersensibilidade e registrar eventos adversos no Banco NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN", severidade="warning"),
    ]

    return {
        "id": cid, "condicao": "Transtorno do Espectro Autista", "eixo": "Neurodesenvolvimento",
        "roadmap_id": "RM15", "svg_file": "RM15.svg",
        "fatores_limitantes": [
            {"id": "comportamental", "nome": "Déficits Comportamentais (Irritabilidade, Hiperatividade, Impulsividade)", "instrumento_sugerido": "ABC / ATEC / CBCL / Conners", "descricao": "Escolha tDCS (≤ 5–6 anos) vs rTMS (> 6 anos)."},
            {"id": "tea_repetitivos", "nome": "Comportamentos Repetitivos (Estereotipias, Compulsões)", "instrumento_sugerido": "RBS-R / GARS", "descricao": "rTMS CPFDL e mudança exploratória HD-tDCS CP5/CP6."},
            {"id": "social", "nome": "Déficits Sociais (Reciprocidade, Contato Visual, Engajamento)", "instrumento_sugerido": "SRS-2 / ATEC Sociabilidade / FER", "descricao": "Cadeia tDCS frontoparietal até cerebelo direito."},
            {"id": "tea_comunicacao", "nome": "Déficits em Comunicação (Outros desfechos — Exploratório)", "instrumento_sugerido": "SRS-2 Comunicação", "descricao": "tDCS anódica F3/Fp2 (Aydin & Yildirim, 2025)."},
        ],
        "arvore_algoritmo": arvore, "observacoes_contextuais": obs_tea, "modalidades": modalidades, "tags_busca": tags,
    }


def build_pediatria_neurodesenvolvimento_conditions():
    """Returns Paralisia Cerebral (RM14) and Transtorno do Espectro Autista (RM15)."""
    return [_build_pc(), _build_tea()]
