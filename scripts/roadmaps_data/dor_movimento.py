"""Official clinical decision trees, protocols, and contextual observations for Dor Neuropatica (RM05), Ataxia Cerebelar (RM16), and Doenca de Parkinson (RM17)."""

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

# Verified references directly matching RM05, RM16, RM17 PDFs
REF_DUARTE_MOREIRA_2025 = make_ref(
    "Duarte-Moreira, R. J., et al.", 2025,
    "Evidence-Based Umbrella Review of Non-Invasive Neuromodulation in Chronic Neuropathic Pain",
    "European Journal of Pain", "10.1002/ejp.4786", tipo="Metanálise de referência",
)
REF_JIANG_2022 = make_ref(
    "Jiang, X., et al.", 2022,
    "Effects of repetitive transcranial magnetic stimulation on neuropathic pain: A systematic review and meta-analysis",
    "Neuroscience & Biobehavioral Reviews", "10.1016/j.neubiorev.2021.11.037", tipo="Metanálise de referência",
)
REF_PACHECO_BARRIOS_2020 = make_ref(
    "Pacheco-Barrios, K., et al.", 2020,
    "Neuromodulation Techniques in Phantom Limb Pain: A Systematic Review and Meta-analysis",
    "Pain Medicine", "10.1093/pm/pnaa039", tipo="Metanálise de referência",
)
REF_UYGUR_2023 = make_ref(
    "Uygur-Kucukseymen, E., et al.", 2023,
    "Non-invasive brain stimulation on clinical symptoms in multiple sclerosis patients: A systematic review and meta-analysis",
    "Multiple Sclerosis and Related Disorders", "10.1016/j.msard.2023.104927", tipo="Metanálise de referência",
)
REF_KHEDR_2015 = make_ref(
    "Khedr, E. M., et al.", 2015,
    "Repetitive transcranial magnetic stimulation in neuropathic pain secondary to malignancy: a randomized clinical trial",
    "European Journal of Pain", "10.1002/ejp.576", tipo="Ensaio clínico de referência",
)
REF_LEFAUCHEUR_2008 = make_ref(
    "Lefaucheur, J. P., et al.", 2008,
    "Motor cortex rTMS in chronic neuropathic pain: pain relief is associated with thermal sensory perception improvement",
    "Journal of Neurology, Neurosurgery & Psychiatry", "10.1136/jnnp.2007.135327", tipo="Ensaio clínico de referência",
)
REF_ATTAL_2016 = make_ref(
    "Attal, N., et al.", 2016,
    "Repetitive transcranial magnetic stimulation and transcranial direct-current stimulation in neuropathic pain due to radiculopathy: a randomized sham-controlled comparative study",
    "Pain", "10.1097/j.pain.0000000000000510", tipo="Ensaio clínico de referência",
)
REF_BONIFACIO_2022 = make_ref(
    "Bonifácio de Assis, E. D., et al.", 2022,
    "Effects of rTMS and tDCS on neuropathic pain after brachial plexus injury: a randomized placebo-controlled pilot study",
    "Scientific Reports", "10.1038/s41598-022-05254-3", tipo="Ensaio clínico de referência",
)
REF_KIKKERT_2019 = make_ref(
    "Kikkert, S., et al.", 2019,
    "Neural basis of induced phantom limb pain relief",
    "Annals of Neurology", "10.1002/ana.25371", tipo="Ensaio clínico de referência",
)
REF_MORI_2010 = make_ref(
    "Mori, F., et al.", 2010,
    "Effects of anodal transcranial direct current stimulation on chronic neuropathic pain in patients with multiple sclerosis",
    "The Journal of Pain", "10.1016/j.jpain.2009.08.011", tipo="Ensaio clínico de referência",
)
REF_HODAJ_2023 = make_ref(
    "Hodaj, H., et al.", 2023,
    "Long-term analgesic effect of trans-spinal direct current stimulation compared to non-invasive motor cortex stimulation in complex regional pain syndrome",
    "Brain Communications", "10.1093/braincomms/fcad191", tipo="Ensaio clínico de referência",
)

# RM16 Ataxia
REF_MATSUGI_2024 = make_ref(
    "Matsugi, A., et al.", 2024,
    "Effectiveness of non-invasive cerebellar stimulation on ataxia: a systematic review and meta-analysis",
    "Movement Disorders Clinical Practice", "10.1002/mdc3.14205", tipo="Metanálise de referência",
)
REF_YIN_2023 = make_ref(
    "Yin, L., et al.", 2023,
    "Effects of non-invasive cerebellar stimulation on balance and gait in patients with ataxia: a meta-analysis",
    "Frontiers in Neurology", "10.3389/fneur.2023.1177746", tipo="Metanálise de referência",
)
REF_BALZAN_2022 = make_ref(
    "Balzan, P., et al.", 2022,
    "Non-invasive brain stimulation for treating neurogenic dysarthria: A systematic review",
    "Annals of Physical and Rehabilitation Medicine", "10.1016/j.rehab.2021.101580", tipo="Metanálise de referência",
)
REF_BENUSSI_2021 = make_ref(
    "Benussi, A., et al.", 2021,
    "Motor and cognitive outcomes of cerebello-spinal stimulation in neurodegenerative ataxia",
    "Brain", "10.1093/brain/awab157", tipo="Ensaio clínico de referência",
)
REF_FRANCA_2020 = make_ref(
    "França, C., et al.", 2020,
    "Effects of cerebellar transcranial magnetic stimulation on ataxias: A randomized trial",
    "Parkinsonism & Related Disorders", "10.1016/j.parkreldis.2020.09.001", tipo="Ensaio clínico de referência",
)
REF_SHI_2023 = make_ref(
    "Shi, Y., et al.", 2023,
    "Efficacy of cerebellar transcranial magnetic stimulation in spinocerebellar ataxia type 3: a randomized, single-blinded, controlled trial",
    "Journal of Neurology", "10.1007/s00415-023-11848-2", tipo="Ensaio clínico de referência",
)
REF_SIKANDAR_2023 = make_ref(
    "Sikandar, A., et al.", 2023,
    "Short-term efficacy of repetitive transcranial magnetic stimulation in SCA3: A prospective, randomized, double-blind, sham-controlled study",
    "Parkinsonism & Related Disorders", "10.1016/j.parkreldis.2022.105236", tipo="Ensaio clínico de referência",
)
REF_LIBRI_2024 = make_ref(
    "Libri, I., et al.", 2024,
    "Comparing Cerebellar tDCS and Cerebellar tACS in Neurodegenerative Ataxias Using Wearable Sensors: A Randomized, Double-Blind, Sham-Controlled, Triple-Crossover Trial",
    "The Cerebellum", "10.1007/s12311-023-01578-6", tipo="Ensaio clínico de referência",
)
REF_CURY_2019 = make_ref(
    "Cury, R. G., et al.", 2019,
    "Effects of dentate nucleus stimulation in spinocerebellar ataxia type 3",
    "Parkinsonism & Related Disorders", "10.1016/j.parkreldis.2019.01.013", tipo="Ensaio clínico de referência",
)

# RM17 Parkinson
REF_LI_2022_PD = make_ref(
    "Li, R., et al.", 2022,
    "Effects of Repetitive Transcranial Magnetic Stimulation on Motor Symptoms in Parkinson's Disease: A Meta-Analysis",
    "Neurorehabilitation and Neural Repair", "10.1177/15459683221095034", tipo="Metanálise de referência",
)
REF_XIE_2020_PD = make_ref(
    "Xie, Y. J., et al.", 2020,
    "Effect of Repetitive Transcranial Magnetic Stimulation on Gait and Freezing of Gait in Parkinson Disease: A Systematic Review and Meta-analysis",
    "Archives of Physical Medicine and Rehabilitation", "10.1016/j.apmr.2019.07.013", tipo="Metanálise de referência",
)
REF_ZHANG_2022_PD = make_ref(
    "Zhang, W., et al.", 2022,
    "Efficacy of repetitive transcranial magnetic stimulation in Parkinson's disease: A systematic review and meta-analysis of randomised controlled trials",
    "eClinicalMedicine", "10.1016/j.eclinm.2022.101589", tipo="Metanálise de referência",
)
REF_CHEN_2025_PD = make_ref(
    "Chen, Y., et al.", 2025,
    "Effects of non-invasive brain stimulation over the supplementary motor area on motor function in Parkinson's disease: A systematic review and meta-analysis",
    "Brain Stimulation", "10.1016/j.brs.2024.12.005", tipo="Metanálise de referência",
)
REF_BRYS_2016 = make_ref(
    "Brys, M., et al.", 2016,
    "Multifocal repetitive TMS for motor and mood symptoms of Parkinson disease: A randomized trial",
    "Neurology", "10.1212/WNL.0000000000003279", tipo="Ensaio clínico de referência",
)
REF_KHEDR_2019 = make_ref(
    "Khedr, E. M., et al.", 2019,
    "The Effect of 20 Hz versus 1 Hz Repetitive Transcranial Magnetic Stimulation on Motor Dysfunction in Parkinson's Disease: Which Is More Beneficial?",
    "Journal of Parkinson's Disease", "10.3233/JPD-181540", tipo="Ensaio clínico de referência",
)
REF_YOKOE_2018 = make_ref(
    "Yokoe, M., et al.", 2018,
    "The optimal stimulation site for high-frequency repetitive transcranial magnetic stimulation in Parkinson's disease: A double-blind crossover pilot study",
    "Journal of Clinical Neuroscience", "10.1016/j.jocn.2017.09.023", tipo="Ensaio clínico de referência",
)
REF_AFTANAS_2020 = make_ref(
    "Aftanas, L. I., et al.", 2020,
    "Clinical and neurophysiological effects of dual-target high-frequency rTMS over the primary motor and prefrontal cortex in Parkinson's disease",
    "Zhurnal Nevrologii i Psikhiatrii imeni S.S. Korsakova", "10.17116/jnevro202012005129", tipo="Ensaio clínico de referência",
)
REF_MI_2019 = make_ref(
    "Mi, T. M., et al.", 2019,
    "High-frequency rTMS over the supplementary motor area improves freezing of gait in Parkinson's disease: a randomized controlled trial",
    "Parkinsonism & Related Disorders", "10.1016/j.parkreldis.2019.10.009", tipo="Ensaio clínico de referência",
)
REF_KHEDR_2006 = make_ref(
    "Khedr, E. M., et al.", 2006,
    "Effect of daily repetitive transcranial magnetic stimulation on motor performance in Parkinson's disease",
    "Movement Disorders", "10.1002/mds.21089", tipo="Ensaio clínico de referência",
)


def _tol(o, a, f):
    return {"orientacao_tolerabilidade": o, "ajuste_seguranca": a, "fatores_moduladores": f}


def _audit(nivel, resumo, just, sinais, grade, forca, dom, tol):
    return {
        "amstar2_nivel": nivel, "amstar2_resumo": resumo, "amstar2_justificativa": just,
        "amstar2_sinais": sinais, "grade_certeza": grade, "grade_forca": forca,
        "grade_dominios": dom, "tolerabilidade": tol,
    }


def _build_dor_neuropatica():
    cid = "dor-neuropatica"
    tags = {
        "coordenadas_10_20": ["C3", "C4", "Fp2", "M1", "SII", "C4-C5", "L1-L2"],
        "alvos_anatomicos": [
            "Córtex Motor Primário (M1)", "Córtex Somatossensorial Secundário (SII — 2 cm posterior a M1)",
            "Medula Espinal (tsDCS C4-C5 / L1-L2)", "Tronco Nervoso / Ponto Motor (rPMS)",
        ],
        "sinonimos_en": ["pain", "neuropathic pain", "chronic pain", "phantom limb pain", "multiple sclerosis pain", "allodynia", "radiculopathy"],
        "sintomas_pt": ["dor", "dor neuropática", "queimação", "choque", "dor fantasma", "esclerose múltipla", "alodinia", "hiperalgesia", "hiperpatia"],
        "escalas": ["EVA", "VAS", "NRS", "NPSI", "BPI"],
        "tecnicas": ["rTMS", "HF-rTMS", "tDCS", "tsDCS", "rPMS", "Estimulação Elétrica Periférica"],
    }
    tol_dor = _tol(
        "Em rTMS, posicionar bobina em figura de 8 com cabo virado para trás e angulado a 45 graus com o plano sagital. Na alodinia mecânica, preferir rPMS (sem encostar a bobina na pele).",
        "Manter avaliação de alterações sensoriais (alodinia, hiperalgesia, hiperpatia), sono, humor e qualidade de vida.",
        "Avaliar consolidação analgésica nas semanas subsequentes ao término da indução e considerar manutenção quando houver resposta sustentada.",
    )

    scale_eva = make_scale("eva", "Escala Visual Analógica / Numérica de Dor (EVA / NRS)", "EVA / NRS", "reducao", "Redução ≥ 20% da intensidade da dor após 5 sessões", 0.62, placeholder="Ex: 7.5", min_val=0, max_val=10, mcid_valor=2.0, mcid_label="-20% a -2,0 pts na EVA")
    scale_npsi = make_scale("npsi", "Inventário de Sintomas de Dor Neuropática (NPSI)", "NPSI", "reducao", "Redução ≥ 20% a 32% nos sintomas neuropáticos e alodinia", 0.56, placeholder="Ex: 42", min_val=0, max_val=100, mcid_valor=10.0, mcid_label="-20% a -32% no NPSI")
    scale_bpi = make_scale("bpi", "Inventário Breve de Dor (BPI — Multidimensional)", "BPI", "reducao", "Redução da interferência da dor em sono, humor e atividade geral", 0.54, placeholder="Ex: 6.0", min_val=0, max_val=10, mcid_valor=1.5, mcid_label="-1,5 pt no BPI")

    step_p3 = make_chain_step(2, "RM05-P3", "HF-rTMS 10 Hz M1 (3.000 pulsos)", "HF-rTMS 10 Hz — M1 C3 3.000 pulsos (Attal et al., 2016)", "HF-rTMS (10 Hz)", "C3 (M1), figura em 8 (cabo para trás a 45° do plano sagital)", "10 Hz | 80% LMR | 3.000 pulsos | 30 trens | 20 s IIT", sessoes="3 a 10 sessões", efeito_esperado="-32%±48% no NPSI após 3 sessões consecutivas", referencia="Attal et al. (2016) · DOI: 10.1097/j.pain.0000000000000510")
    step_p4 = make_chain_step(3, "RM05-P4", "tDCS Anódica C3/Fp2", "tDCS Anódica — C3 / Fp2 (Bonifácio de Assis et al., 2022)", "tDCS Anódica", "Ânodo C3 + Cátodo Fp2 (eletrodos 5 × 7 cm)", "2,0 mA | 20 min", sessoes="5 sessões consecutivas", efeito_esperado="-27%±81% intensidade da dor em lesão de plexo braquial", referencia="Bonifácio de Assis et al. (2022) · DOI: 10.1038/s41598-022-05254-3")
    step_sii = make_chain_step(4, "RM05-ALT-SII", "HF-rTMS 10 Hz — SII (Pontilhado)", "HF-rTMS 10 Hz — Córtex Somatossensorial Secundário SII (Lindholm et al., 2015)", "HF-rTMS (10 Hz)", "Córtex Somatossensorial Secundário (SII — 2 cm posterior a M1)", "10 Hz | 90% LMR | 1.000 pulsos | trens de 50 pulsos | 10 s IIT", sessoes="7 sessões consecutivas", efeito_esperado="-38% NRS em dor neuropática resistente (orofacial)", referencia="Lindholm et al. (2015) · DOI: 10.1097/j.pain.0000000000000175", linha_fluxograma="pontilhada", fase_etapa="ajustes")
    step_tsdcs = make_chain_step(2, "RM05-ALT-TSDCS", "tsDCS Medular (Pontilhado)", "tsDCS Medular — C4-C5 / L1-L2 (Hodaj et al., 2023)", "tsDCS Medular", "MMSS: ânodo C4–C5, cátodo 8 cm abaixo | MMII: ânodo L1–L2, cátodo 8 cm abaixo (5 × 7 cm)", "2,0 mA | 20 minutos", sessoes="5 sessões consecutivas", efeito_esperado="Redução de 2 pontos na escala de dor", referencia="Hodaj et al. (2023) · DOI: 10.1093/braincomms/fcad191", linha_fluxograma="pontilhada", fase_etapa="ajustes")

    adj_dor = {"titulo": "Ajustes, Orientação da Bobina e Abordagens Adjuvantes (Dor Neuropática)", "tolerabilidade": "Bobina em figura de 8 com cabo virado para trás a 45° do plano sagital; em alodinia mecânica, preferir rPMS (sem encostar a bobina na pele).", "dose_pulsos": "Adjuvantes opcionais a qualquer momento: Estimulação Elétrica Periférica (50 Hz, 200 µs, nível sensorial, 30 min) ou rPMS (4 Hz, 3.000 p, 15 trens, 1 s IIT, sem dor sobre tronco/ponto motor).", "calibracao_limiar": "Melhoras frequentemente se consolidam nas semanas após o fim da indução; considerar manutenção para efeito analgésico sustentado."}
    falha_dor = {"criterio": "Redução da intensidade da dor < 20% na EVA em 5 sessões SEM melhora multidimensional associada após percorrer toda a sequência de protocolos e a seção de ajustes.", "conduta_oficial": "1. Verificar redução < 20% na EVA aos 5 dias E avaliar alterações sensoriais (alodinia, hiperalgesia, hiperpatia), sono, humor e BPI;\n2. Associar adjuvantes periféricos (rPMS/PEP);\n3. Consolidar protocolos de manutenção caso analgesia tardia ocorra."}
    sa_dor = {"quando_reavaliar": "Redução < 20% na EVA em 5 sessões configura resposta insatisfatória (verificar também alodinia, hiperalgesia, hiperpatia, sono e humor) e acompanhar consolidação nas semanas pós-indução.", "ajuste_dose": "Escalonar carga de pulsos (2.000 p para 3.000 p), migrar para tDCS / SII / tsDCS na sequência ou associar rPMS/PEP conforme perfil sensorial.", "regra_interrupcao": "Manter manutenção se efeito analgésico sustentado; avançar de protocolo se redução < 20% na EVA sem ganho sensorial, de sono ou humor."}

    modalidades = {
        "geral": make_mod(
            protocolo_id="RM05-P1", tecnica="HF-rTMS 20 Hz — Córtex Motor Primário (C3)", modalidade_sigla="rTMS 20 Hz M1",
            alvo="Córtex Motor Primário (C3) — bobina em figura de 8 (45° cabo para trás)", frequencia="20 Hz", intensidade="80% LMR",
            pulsos_duracao="2.000 pulsos | 10 trens | 30 s IIT", sessoes="10 sessões consecutivas",
            escala_recomendada="EVA / NRS / NPSI / BPI", meta_melhora="Redução ≥ 20% na EVA em 5 sessões (-36%±76% na intensidade da dor)",
            tamanho_efeito=0.62, evidencia="Nível A — Umbrella Review Duarte-Moreira 2025 / Jiang 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível A (Lefaucheur et al., 2020 · Duarte-Moreira et al., 2025)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_KHEDR_2015, meta_analise=REF_DUARTE_MOREIRA_2025,
            mcid_valor=2.0, mcid_label="-20% a -2,0 pts na EVA", cohen_d_valor=0.62, cohen_d_interp="Moderado",
            estudo_referencia="Khedr et al. (2015)", efeito_resumo="Redução da intensidade da dor em 36%±76% após 10 sessões",
            escalas_detalhadas=[scale_eva, scale_npsi, scale_bpi],
            cadeia_sequencial=[
                make_chain_step(1, "RM05-P1", "HF-rTMS 20 Hz M1 (Primeira Linha)", "HF-rTMS 20 Hz — Córtex Motor Primário C3 (Khedr et al., 2015)", "HF-rTMS (20 Hz)", "C3 (M1), figura em 8 (cabo 45° para trás)", "20 Hz | 80% LMR | 2.000 pulsos | 10 trens | 30 s IIT", sessoes="10 sessões", efeito_esperado="-36%±76% na intensidade da dor", referencia="Khedr et al. (2015) · DOI: 10.1002/ejp.576"),
                step_p3, step_p4, step_sii,
            ],
            ajuste_parametros=adj_dor, falha_terapeutica=falha_dor, sessoes_ajuste=sa_dor,
            notas_clinicas="Avaliar alodinia, hiperalgesia, hiperpatia, sono e humor além da intensidade bruta da dor na EVA.",
            audit_meta=_audit("Alta", "Umbrella Review (Duarte-Moreira et al., 2025) + Metanálise (Jiang et al., 2022).", "Síntese de alta qualidade metodológica para dor neuropática crônica em M1.", ["Umbrella Review", "Risco de viés"], "Alta", "Forte", "Nível A para rTMS de alta frequência em M1 contralateral à dor.", tol_dor),
        ),
        "dor_geral_p2": make_mod(
            protocolo_id="RM05-P2", tecnica="HF-rTMS 10 Hz — Córtex Motor Primário (C3)", modalidade_sigla="rTMS 10 Hz M1",
            alvo="Córtex Motor Primário (C3) — bobina em figura de 8 (45° cabo para trás)", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="2.000 pulsos | 60 trens | 25 s IIT", sessoes="5 a 10 sessões consecutivas",
            escala_recomendada="EVA / NRS / NPSI / BPI", meta_melhora="Redução ≥ 20% na EVA (-24%±6% na intensidade da dor)",
            tamanho_efeito=0.60, evidencia="Nível A — IFCN 2020 / Jiang 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível A (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_LEFAUCHEUR_2008, meta_analise=REF_JIANG_2022,
            mcid_valor=2.0, mcid_label="-20% a -2,0 pts na EVA", cohen_d_valor=0.60, cohen_d_interp="Moderado",
            estudo_referencia="Lefaucheur et al. (2008)", efeito_resumo="-24%±6% na intensidade da dor em dor neuropática central e periférica",
            escalas_detalhadas=[scale_eva, scale_npsi, scale_bpi],
            cadeia_sequencial=[
                make_chain_step(1, "RM05-P2", "HF-rTMS 10 Hz M1 (Primeira Linha)", "HF-rTMS 10 Hz — Córtex Motor Primário C3 (Lefaucheur et al., 2008)", "HF-rTMS (10 Hz)", "C3 (M1), figura em 8 (cabo 45° para trás)", "10 Hz | 90% LMR | 2.000 pulsos | 60 trens | 25 s IIT", sessoes="5–10 sessões", efeito_esperado="-24%±6% na dor central/periférica", referencia="Lefaucheur et al. (2008) · DOI: 10.1136/jnnp.2007.135327"),
                step_p3, step_p4, step_sii,
            ],
            ajuste_parametros=adj_dor, falha_terapeutica=falha_dor, sessoes_ajuste=sa_dor,
            notas_clinicas="Opção inicial de 10 Hz em M1 equivalente em eficácia clínica para dor neuropática central e periférica.",
            audit_meta=_audit("Moderada", "Metanálise (Jiang et al., 2022) para rTMS em dor neuropática.", "Análise sistemática com avaliação de viés e heterogeneidade.", ["Risco de viés"], "Alta", "Forte", "Regime clássico de 10 Hz / 2.000 pulsos em M1.", tol_dor),
        ),
        "dor_fantasma": make_mod(
            protocolo_id="RM05-FANT", tecnica="tDCS Anódica — C3 / Fp2 (Dor Fantasma)", modalidade_sigla="tDCS M1",
            alvo="Ânodo em C3 e Cátodo em Fp2 (eletrodos 5 × 7 cm)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min (eletrodos 5 × 7 cm)", sessoes="6 sessões consecutivas",
            escala_recomendada="EVA / NRS / BPI", meta_melhora="-29,5%±25% na dor após 6 sessões",
            tamanho_efeito=0.58, evidencia="Nível B — Metanálise Pacheco-Barrios 2020", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017 · Pacheco-Barrios et al., 2020)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_KIKKERT_2019, meta_analise=REF_PACHECO_BARRIOS_2020,
            mcid_valor=2.0, mcid_label="-20% na EVA", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Kikkert et al. (2019)", efeito_resumo="Redução de 29,5%±25% após 6 sessões em membro fantasma",
            escalas_detalhadas=[scale_eva, scale_bpi, scale_npsi],
            cadeia_sequencial=[
                make_chain_step(1, "RM05-FANT-P1", "tDCS Anódica C3/Fp2 (Dor Fantasma)", "tDCS Anódica — C3/Fp2 em Dor Fantasma (Kikkert et al., 2019)", "tDCS Anódica", "Ânodo C3 + Cátodo Fp2 (5 × 7 cm)", "2,0 mA | 20 min", sessoes="6 sessões", efeito_esperado="-29,5%±25% dor fantasma", referencia="Kikkert et al. (2019) · DOI: 10.1002/ana.25371", fase_etapa="inicial"),
                make_chain_step(2, "RM05-P2", "HF-rTMS 10 Hz M1 (2.000 p)", "HF-rTMS 10 Hz — C3 2.000 pulsos (Lefaucheur et al., 2008)", "HF-rTMS (10 Hz)", "C3 M1", "10 Hz | 90% LMR | 2.000 p", sessoes="5–10 sessões", efeito_esperado="-24%±6% na dor", referencia="Lefaucheur et al. (2008) · DOI: 10.1136/jnnp.2007.135327", fase_etapa="sequencia"),
                make_chain_step(3, "RM05-P3", "HF-rTMS 10 Hz M1 (3.000 pulsos)", "HF-rTMS 10 Hz — M1 C3 3.000 pulsos (Attal et al., 2016)", "HF-rTMS (10 Hz)", "C3 (M1), figura em 8 (cabo para trás a 45° do plano sagital)", "10 Hz | 80% LMR | 3.000 pulsos | 30 trens | 20 s IIT", sessoes="3 a 10 sessões", efeito_esperado="-32%±48% no NPSI após 3 sessões consecutivas", referencia="Attal et al. (2016) · DOI: 10.1097/j.pain.0000000000000510", fase_etapa="sequencia"),
            ],
            ajuste_parametros=adj_dor, falha_terapeutica=falha_dor, sessoes_ajuste=sa_dor,
            notas_clinicas="Em dor de membro fantasma, inicia-se com tDCS cortical pela boa tolerabilidade inicial antes de escalonar para rTMS em M1 (2.000 p e 3.000 p).",
            audit_meta=_audit("Moderada", "Metanálise dedicada à dor do membro fantasma (Pacheco-Barrios et al., 2020).", "Sinal consistente para tDCS anódica M1.", ["Risco de viés"], "Moderada", "Condicional", "Boa tolerabilidade inicial antes de rTMS.", tol_dor),
            mod_tipo="tdcs",
        ),
        "espinhal": make_mod(
            protocolo_id="RM05-EM", tecnica="tDCS Anódica — C3 / Fp2 (Esclerose Múltipla)", modalidade_sigla="tDCS M1",
            alvo="Ânodo em C3 + Cátodo em Fp2 (eletrodos 5 × 7 cm)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min (eletrodos 5 × 7 cm)", sessoes="5 sessões consecutivas (EM Remitente-Recorrente)",
            escala_recomendada="EVA / NRS / BPI", meta_melhora="-45,5%±11% na dor após 5 sessões",
            tamanho_efeito=0.55, evidencia="Nível B — Metanálise Esclerose Múltipla Uygur 2023", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_MORI_2010, meta_analise=REF_UYGUR_2023,
            mcid_valor=2.0, mcid_label="-20% a -2,0 pts na dor", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Mori et al. (2010)", efeito_resumo="Redução de 45,5%±11% na dor na Esclerose Múltipla em remissão",
            escalas_detalhadas=[scale_eva, scale_bpi, scale_npsi],
            cadeia_sequencial=[
                make_chain_step(1, "RM05-EM-P1", "tDCS Anódica C3/Fp2 (Esclerose Múltipla)", "tDCS Anódica — C3/Fp2 em EM (Mori et al., 2010)", "tDCS Anódica", "Ânodo C3 + Cátodo Fp2 (5 × 7 cm)", "2,0 mA | 20 min", sessoes="5 sessões consecutivas", efeito_esperado="-45,5%±11% na dor crônica em EM", referencia="Mori et al. (2010) · DOI: 10.1016/j.jpain.2009.08.011"),
                step_tsdcs,
            ],
            ajuste_parametros=adj_dor, falha_terapeutica=falha_dor, sessoes_ajuste=sa_dor,
            notas_clinicas="Em Esclerose Múltipla sem resposta à tDCS cortical, a etapa de ajustes utiliza tsDCS medular com montagem específica para MMSS (C4-C5) ou MMII (L1-L2).",
            audit_meta=_audit("Moderada", "Metanálise NIBS em Esclerose Múltipla (Uygur-Kucukseymen et al., 2023).", "Resultados consistentes em dor crônica associada à EM.", ["Risco de viés"], "Moderada", "Condicional", "Sequência direta para tsDCS medular em caso de resposta insatisfatória.", tol_dor),
            mod_tipo="tdcs",
        ),
    }

    arvore = {
        "roadmap_id": "RM05",
        "titulo_fluxograma": "Neuromodulação Não Invasiva na Dor Neuropática",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante clínico?",
                "subtitulo": "Indicação geral: Controle da dor neuropática — Local de aplicação em Córtex Motor Primário.",
                "opcoes": [{"id": "intensidade_dor", "rotulo": "Intensidade da dor", "criterio": "EVA / NRS / NPSI / BPI", "descricao": "Selecionar indicação específica da dor neuropática.", "proxima_etapa": "indicacao_especifica"}],
            },
            "indicacao_especifica": {
                "pergunta": "Qual é a indicação clínica específica da dor neuropática?",
                "subtitulo": "Selecione o quadro clínico predominante para definir a parametrização inicial.",
                "opcoes": [
                    {"id": "dor_geral", "rotulo": "Dor neuropática em geral", "criterio": "Duarte-Moreira et al., 2025 / Jiang 2022", "descricao": "Escolher entre regime inicial de 20 Hz (Khedr 2015) ou 10 Hz (Lefaucheur 2008).", "proxima_etapa": "dor_geral_inicial"},
                    {"id": "dor_fantasma", "rotulo": "Dor fantasma", "criterio": "Amputação de membro", "descricao": "Inicia com tDCS anódica C3/Fp2 (Kikkert et al., 2019).", "protocolo_alvo": "dor_fantasma"},
                    {"id": "dor_em", "rotulo": "Dor na Esclerose Múltipla", "criterio": "EM Remitente-Recorrente", "descricao": "Inicia com tDCS anódica C3/Fp2 (Mori et al., 2010).", "protocolo_alvo": "espinhal"},
                ],
            },
            "dor_geral_inicial": {
                "pergunta": "Qual regime inicial de rTMS M1 deseja selecionar para Dor Neuropática em Geral?",
                "subtitulo": "Os dois regimes iniciais em M1 possuem indicação paralela e convergem na sequência pós-indução.",
                "opcoes": [
                    {"id": "dor_p1_20hz", "rotulo": "HF-rTMS 20 Hz — 80% LMR, 2.000 pulsos (10 trens)", "criterio": "Khedr et al. (2015)", "descricao": "-36%±76% dor após 10 sessões.", "protocolo_alvo": "geral"},
                    {"id": "dor_p2_10hz", "rotulo": "HF-rTMS 10 Hz — 90% LMR, 2.000 pulsos (60 trens)", "criterio": "Lefaucheur et al. (2008)", "descricao": "-24%±6% dor central/periférica.", "protocolo_alvo": "dor_geral_p2"},
                ],
            },
        },
        "ajuste_parametros": adj_dor,
        "protocolo_alternativo": {
            "nome": "HF-rTMS 10 Hz SII (Lindholm et al., 2015) — Seção de Ajustes",
            "tecnica": "HF-rTMS (10 Hz)", "alvo": "SII (2 cm posteriores a M1)", "parametros": "10 Hz | 90% LMR | 1.000 pulsos | trens de 50 p | 10 s IIT",
            "observacoes": "-38% NRS em dor orofacial resistente após 7 sessões.",
        },
        "protocolo_alternativo_2": {
            "nome": "tsDCS Medular (Hodaj et al., 2023) / Adjuvantes rPMS-PEP — Seção de Ajustes",
            "tecnica": "tsDCS / rPMS / PEP", "alvo": "MMSS: C4–C5; MMII: L1–L2 (+ tronco nervoso em rPMS)",
            "parametros": "tsDCS 2 mA 20 min | rPMS 4 Hz 3.000p 15 trens 1 s IIT | PEP 50 Hz 200 µs 30 min",
            "observacoes": "Em alodinia mecânica, preferir rPMS por não necessitar contato da bobina com a pele algógena.",
        },
        "falha_terapeutica": {
            "id": "RM05-FALHA", "titulo": "Falha Terapêutica em Dor Neuropática",
            "criterios_definicao": "Redução < 20% na EVA em 5 sessões e ausência de resposta sensorial, sono, humor ou BPI após protocolos sequenciais e seção de ajustes.",
            "descricao": "Considerar melhora multidimensional além da intensidade bruta e consolidação tardia pós-indução.",
            "condutas": ["Associar abordagens periféricas (rPMS 4 Hz ou PEP 50 Hz).", "Considerar SII (10 Hz) ou tsDCS conforme topografia."],
        },
    }

    obs_dor = [
        make_obs("RM05-BOBINA-45", "Nos protocolos envolvendo rTMS, a bobina em formato de 8 deve estar com o cabo virado para trás e angulado a 45 graus com o plano sagital.", "alvo", categoria="anatomia", protocolo_ids=["geral", "dor_geral_p2"], estagios=["primary", "alt1"], modalidades_tipo=["rtms"]),
        make_obs("RM05-ALODINIA-RPMS", "Na presença de alodinia mecânica, a associação com rPMS é preferível, pois não há necessidade de encostar a bobina diretamente na pele dolorosa.", "alvo", categoria="clinica"),
        make_obs("RM05-ADJUVANTES", "Abordagens adjuvantes opcionais (PEP ou rPMS) podem ser associadas simultânea ou subsequentemente a qualquer momento em caso de analgesia parcial.", "sessoes", categoria="parametros"),
        make_obs("RM05-DESFECHOS-MULTIDIM", "É possível que o paciente não reduza a intensidade bruta da dor, mas apresente melhora em alterações sensoriais (alodinia, hiperalgesia, hiperpatia), grau de sofrimento, qualidade de vida, sono e humor.", "scale", categoria="avaliacao"),
        make_obs("RM05-BANCO-EA", "Em caso de efeitos adversos, relatá-los no Banco de Efeitos Adversos NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN"),
    ]

    return {
        "id": cid, "condicao": "Dor Neuropática Crônica", "eixo": "Dor Crônica & Neuropática",
        "roadmap_id": "RM05", "svg_file": "RM05.svg",
        "fatores_limitantes": [
            {"id": "intensidade_dor", "nome": "Intensidade da dor", "instrumento_sugerido": "EVA / NRS / NPSI / BPI", "descricao": "Dor neuropática periférica, central, fantasma ou associada à esclerose múltipla."},
        ],
        "arvore_algoritmo": arvore, "observacoes_contextuais": obs_dor, "modalidades": modalidades, "tags_busca": tags,
    }


def _build_ataxia():
    cid = "ataxia-cerebelar"
    tags = {
        "coordenadas_10_20": ["Inion", "Cerebelo", "Vermis", "Núcleo Denteado", "T11", "C3", "C4", "Fp1", "Fp2"],
        "alvos_anatomicos": ["Córtex Cerebelar Global", "Vérmis Cerebelar (1 cm abaixo do ínion)", "Hemisférios Cerebelares (1 cm abaixo, 3 cm laterais)", "Núcleo Denteado", "Medula Espinal T11 (8 × 6 cm)"],
        "sinonimos_en": ["ataxia", "spinocerebellar ataxia", "sca", "cerebellar ataxia", "incoordination", "dysmetria", "dysarthria"],
        "sintomas_pt": ["ataxia", "incoordenação", "dismetria", "desequilíbrio", "destreza manual", "mobilidade funcional", "disartria atáxica"],
        "escalas": ["SARA", "ICARS", "BBS", "Mini-BESTest", "TC10m", "TUG", "9HPT", "V-RQOL", "DDK"],
        "tecnicas": ["csDCS", "ctDCS", "iTBS Cerebelar", "rTMS Núcleo Denteado", "cbTMS"],
    }
    tol_ax = _tol(
        "Atentar para eventos adversos durante e após a estimulação e para o efeito terapêutico reduzido na presença de certas medicações (ex.: benzodiazepínicos).",
        "Em estimulação medular T11 (csDCS), usar eletrodo de 8 × 6 cm (48 cm²). Em núcleo denteado, utilizar obrigatoriamente neuronavegação.",
        "Avaliar qualidade da resposta semanalmente combinando escala do pré-teste e auto-relato do paciente.",
    )

    scale_sara = make_scale("sara", "Scale for the Assessment and Rating of Ataxia (SARA)", "SARA", "reducao", "Redução ≥ 1,5 pt ou -9,1% a -25% na SARA", 0.60, placeholder="Ex: 17.5", min_val=0, max_val=40, mcid_valor=1.5, mcid_label="-1,5 pt ou -9,1% a -25% na SARA")
    scale_icars = make_scale("icars", "International Cooperative Ataxia Rating Scale (ICARS)", "ICARS", "reducao", "Redução ≥ 3,5 pts (-13,2 pts a -4,27 pts em séries clínicas) na ICARS", 0.69, placeholder="Ex: 42", min_val=0, max_val=100, mcid_valor=3.5, mcid_label="-3,5 pts na ICARS")
    scale_bbs = make_scale("bbs", "Escala de Equilíbrio de Berg (BBS) / BESTest", "BBS", "aumento", "Melhora ≥ 4,0 pts ou +11,77% na BBS", 0.58, placeholder="Ex: 34", min_val=0, max_val=56, mcid_valor=4.0, mcid_label="+11,77% na BBS")
    scale_9hpt = make_scale("nine_hpt", "Nine-Hole Peg Test (9HPT) / Box and Blocks Test", "9HPT", "reducao", "Melhora ≥ 12,83% no tempo do 9HPT", 0.50, placeholder="Ex: 38.0", min_val=5, max_val=300, mcid_valor=3.0, mcid_label="-12,83% no tempo do 9HPT")
    scale_tc10 = make_scale("tc10m", "Teste de Caminhada de 10 Metros (TC10m) / TUG", "TC10m / TUG", "reducao", "Mobilidade funcional: melhora de 31,11% no TC10m e -1,2 s (8,7%) no TUG", 0.55, placeholder="Ex: 14.0", min_val=2, max_val=120, mcid_valor=1.2, mcid_label="-8,7% TUG / -31,1% TC10m")

    def _ax_cs(ordem, fase="inicial"):
        rotulo = "Seção de Ajustes — csDCS Cerebelo-Espinal (T11 / Cerebelo Global)" if fase == "ajustes" else "csDCS (Cátodo T11 / Ânodo Cerebelo)"
        return make_chain_step(ordem, "RM16-CSDCS", rotulo, "csDCS Cerebelo-Espinal (Benussi et al., 2018/2021)", "csDCS", "Ânodo cerebelo global (2 cm abaixo ínion) + Cátodo T11 (eletrodo 8 × 6 cm = 48 cm²)", "2,0 mA | 20 min", sessoes="10 a 20 sessões", efeito_esperado="-4,8 pts (~25% SARA) e ~28% ICARS mantidos até 6 meses", referencia="Benussi et al. (2021) · DOI: 10.1093/brain/awab157", linha_fluxograma="solida", fase_etapa=fase)

    def _ax_ct(ordem, fase="sequencia"):
        rotulo = "Seção de Ajustes — ctDCS Cerebelo / Deltoide Direito" if fase == "ajustes" else "ctDCS Cerebelo / Deltoide Direito"
        return make_chain_step(ordem, "RM16-CTDCS", rotulo, "ctDCS Cerebelar (Libri et al., 2024)", "ctDCS", "Ânodo cerebelo global + Cátodo músculo deltoide direito", "2,0 mA | 20 min", sessoes="10 a 20 sessões", efeito_esperado="-0,6 pts SARA (4,4%) / Severidade: -1,92 pts (14,8% SARA)", referencia="Libri et al. (2024) · DOI: 10.1007/s12311-023-01578-6", linha_fluxograma="solida", fase_etapa=fase)

    def _ax_itbs(ordem, fase="sequencia"):
        return make_chain_step(ordem, "RM16-ITBS", "iTBS Hemisférios Cerebelares", "iTBS — Hemisférios Cerebelares (Shiga et al., 2002; Shi et al., 2023)", "iTBS Cerebelar", "Hemisférios cerebelares (1 cm abaixo do ínion e 3 cm laterais)", "600 pulsos/hemisfério (10 triplets/trem, 60 trens) | 90% LMR", sessoes="10 a 20 sessões", efeito_esperado="Melhora cinética na SARA/ICARS e 9HPT", referencia="Shiga et al. (2002) · Shi et al. (2023) · DOI: 10.1007/s00415-023-11848-2", linha_fluxograma="solida", fase_etapa=fase)

    def _ax_dent(ordem):
        return make_chain_step(ordem, "RM16-DENT", "Próximo Protocolo (Linha Pontilhada) — LF-rTMS 1 Hz Núcleo Denteado", "LF-rTMS 1 Hz — Núcleo Denteado com Neuronavegação (Cury et al., 2019)", "LF-rTMS (1 Hz — Experimental)", "Núcleo denteado (3 cm lateral e 1 cm inferior ao ínion, requer neuronavegação)", "1 Hz | 1.200 pulsos | 90% LMR", sessoes="10 a 20 sessões", efeito_esperado="-3,5 pts SARA (PGIC 5)", referencia="Cury et al. (2019) · DOI: 10.1016/j.parkreldis.2019.01.013", linha_fluxograma="pontilhada", fase_etapa="sequencia")

    def _ax_m1(ordem):
        return make_chain_step(ordem, "RM16-P5", "Seção de Ajustes — ctDCS M1 Área Alternativa (C3/C4)", "ctDCS M1 — C3/C4 + FP1/FP2 (Barretto et al., 2019)", "ctDCS M1 (Área Alternativa)", "Ânodo C3 e C4 (M1) + Cátodo FP1 ou FP2 contralateral", "2,0 mA | 20 min", sessoes="10 a 20 sessões", efeito_esperado="-3,5 pts SARA (22,4%; d=1,09) e +14,21 s posturografia", referencia="Barretto et al. (2019)", linha_fluxograma="solida", fase_etapa="ajustes")

    adj_ax = {"titulo": "Ajustes de Tolerabilidade, Coordenadas e Dose em Ataxia Cerebelar", "tolerabilidade": "Monitorar eventos adversos durante e após a estimulação; checar benzodiazepínicos que tendem a diminuir os efeitos terapêuticos.", "dose_pulsos": "Tem sido observada maior quantidade de sessões do que as 10 habituais — optar por estender o ciclo para 10 a 20 sessões. Eletrodo medular T11 mede 8 × 6 cm (48 cm²).", "calibracao_limiar": "Vérmis: 1 cm abaixo do ínion; Hemisférios cerebelares: 1 cm abaixo e 3 cm laterais; Núcleo denteado: requer obrigatoriamente neuronavegação."}
    falha_ax = {"criterio": "Sem mudança de pontuação nas escalas utilizadas como pré-teste após 1 semana e auto-relato negativo, após percorrer tDCS, rotas rTMS e seção de ajustes.", "conduta_oficial": "1. Verificar uso de benzodiazepínicos e aderência à terapia associada à função-alvo;\n2. Confirmar aumento do ciclo para 10 a 20 sessões;\n3. Escalonar sequencialmente de tDCS para iTBS/rTMS cerebelar ou área alternativa C3/C4 / deltoide direito."}
    sa_ax = {"quando_reavaliar": "De uma semana para a outra: sem mudança nas escalas de pré-teste para o microdesfecho + auto-relato negativo configura resposta insuficiente.", "ajuste_dose": "Associar treino ativo direcionado à função desejada mantendo o paciente em fadiga leve-moderada.", "regra_interrupcao": "Se não houver mudança em 1 semana, avançar diretamente para o próximo protocolo na sequência."}

    modalidades = {
        "severidade_motora": make_mod(
            protocolo_id="RM16-SEV", tecnica="csDCS Cerebelo-Espinal — T11 / Cerebelo Global (Benussi et al., 2021)", modalidade_sigla="csDCS",
            alvo="Ânodo cerebelo global (2 cm abaixo ínion) + Cátodo T11 (8 × 6 cm = 48 cm²)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min | T11 eletrodo 48 cm² (8 × 6 cm)", sessoes="10 a 20 sessões associadas à função desejada",
            escala_recomendada="SARA / ICARS (+ auto-relato semanal)", meta_melhora="-4,8 pts (~25% SARA) e ~28% ICARS",
            tamanho_efeito=0.60, evidencia="Nível B — Metanálise Matsugi 2024 / Benussi 2021", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Matsugi et al., 2024)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_BENUSSI_2021, meta_analise=REF_MATSUGI_2024,
            mcid_valor=1.5, mcid_label="-14,8% a -25% na SARA", cohen_d_valor=0.60, cohen_d_interp="Moderado",
            estudo_referencia="Benussi et al. (2021) / Libri et al. (2024)", efeito_resumo="Redução média de 4,8 pts (~25%) na SARA mantida até 6 meses",
            escalas_detalhadas=[scale_sara, scale_icars],
            escalas_por_fator={"severidade_motora": ["sara", "icars"]},
            cadeia_sequencial=[
                _ax_cs(1, "inicial"),
                _ax_ct(2, "sequencia"),
                _ax_itbs(3, "sequencia"),
                _ax_dent(4),
                _ax_m1(5),
            ],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Em caso de resposta insatisfatória à tDCS (csDCS/ctDCS), avançar no Assistente Pós-Indução para iTBS cerebelar, LF-rTMS núcleo denteado (neuronavegação) e área alternativa M1 (C3/C4); manter exercícios motores em fadiga leve-moderada.",
            audit_meta=_audit("Moderada", "Metanálise cerebelar em ataxia (Matsugi et al., 2024).", "Consistência de csDCS, ctDCS e escalonamento para iTBS/rTMS sobre escores SARA/ICARS.", ["Risco de viés"], "Moderada", "Condicional", "csDCS reduz SARA em ~25% mantido até 6 meses; ctDCS reduz ~14,8%; escalona para iTBS, núcleo denteado e M1.", tol_ax),
            mod_tipo="tdcs",
        ),
        "destreza_manual": make_mod(
            protocolo_id="RM16-DEST", tecnica="csDCS Cerebelo-Espinal — T11 / Cerebelo Global (Benussi et al., 2021)", modalidade_sigla="csDCS",
            alvo="Ânodo cerebelo global (2 cm abaixo ínion) + Cátodo T11 (8 × 6 cm)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min | eletrodo espinal T11 (8 × 6 cm)", sessoes="10 a 20 sessões com treino de destreza",
            escala_recomendada="9HPT / Box and Blocks / Purdue / Jebsen Taylor", meta_melhora="Melhora de 12,83% no 9HPT",
            tamanho_efeito=0.50, evidencia="Nível B — Benussi 2021 / Libri 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Matsugi et al., 2024)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_LIBRI_2024, meta_analise=REF_MATSUGI_2024,
            mcid_valor=3.0, mcid_label="-12,83% no tempo do 9HPT", cohen_d_valor=0.50, cohen_d_interp="Moderado",
            estudo_referencia="Benussi et al. (2021) / Libri et al. (2024)", efeito_resumo="+12,83% de melhora no 9HPT (d=0,50)",
            escalas_detalhadas=[scale_9hpt],
            escalas_por_fator={"destreza_manual": ["nine_hpt"]},
            cadeia_sequencial=[
                _ax_cs(1, "inicial"),
                _ax_ct(2, "ajustes"),
            ],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Associar tarefas de destreza manual ao nível de fadiga leve-moderado.",
            audit_meta=_audit("Moderada", "Metanálise ataxia (Matsugi et al., 2024).", "Consistente em destreza fina.", ["Risco de viés"], "Moderada", "Condicional", "Combinar com treino manual direcionado.", tol_ax),
            mod_tipo="tdcs",
        ),
        "mobilidade_funcional": make_mod(
            protocolo_id="RM16-MOB", tecnica="cbTMS 1 Hz Bobina Circular (Sikandar et al., 2023)", modalidade_sigla="cbTMS 1 Hz",
            alvo="Hemisfério D, Vérmis e Hemisfério E", frequencia="1 Hz", intensidade="90% LMR",
            pulsos_duracao="10 pulsos/área (5 anti-horário + 5 horário, IIT 6 s)", sessoes="10 a 20 sessões",
            escala_recomendada="TC10m / TC8m / TC6min / TUG", meta_melhora="Melhora de 31,11% no TC10m e -1,2 s (8,7%) no TUG",
            tamanho_efeito=0.55, evidencia="Nível B — Sikandar 2023 / Yin 2023 / csDCS", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Yin et al., 2023)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_SIKANDAR_2023, meta_analise=REF_YIN_2023,
            mcid_valor=1.2, mcid_label="-1,2 s (-8,7%) TUG / -31,1% TC10m", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Sikandar et al. (2023) / Benussi et al. (2021)", efeito_resumo="31,11% no TC10m e -1,2 s (8,7%) no TUG",
            escalas_detalhadas=[scale_tc10],
            escalas_por_fator={"mobilidade_funcional": ["tc10m"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM16-MOB-P1", "Protocolo Inicial — cbTMS 1 Hz Bobina Circular", "cbTMS 1 Hz Bobina Circular — 10 pulsos/área (Sikandar et al., 2023)", "cbTMS (Bobina Circular)", "Hemisfério D, Vérmis e Hemisfério E", "5 pulsos anti-horários + 5 horários, IIT 6 s | 1 Hz | 90% LMR", sessoes="10 a 20 sessões", efeito_esperado="+31,11% TC10m e -8,7% TUG", referencia="Sikandar et al. (2023) · DOI: 10.1016/j.parkreldis.2022.105236", linha_fluxograma="solida", fase_etapa="inicial"),
                _ax_cs(2, "sequencia"),
                _ax_ct(3, "ajustes"),
            ],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Ramo inicial com bobina circular sobre hemisférios cerebelares e vérmis; associar treino de marcha em fadiga leve-moderada.",
            audit_meta=_audit("Moderada", "Metanálise marcha/equilíbrio em ataxia (Yin et al., 2023).", "Resultados consistentes em TC10m e TUG.", ["Risco de viés"], "Moderada", "Condicional", "Associar treino de marcha em fadiga leve-moderada.", tol_ax),
        ),
        "equilibrio": make_mod(
            protocolo_id="RM16-EQ", tecnica="cbTMS 1 Hz — Hemisférios Cerebelares (França et al., 2020)", modalidade_sigla="cbTMS 1 Hz",
            alvo="Hemisférios cerebelares bilateral (2 cm abaixo do ínion; 1 cm abaixo/3 cm lateral)", frequencia="1 Hz", intensidade="100% LMR",
            pulsos_duracao="900 p/hemisfério (1.800 pulsos/sessão)", sessoes="10 a 20 sessões associadas a treino de equilíbrio",
            escala_recomendada="BBS / BESTest / Mini-BESTest", meta_melhora="Melhora de +11,77% na BBS e 9,1% na SARA (SMD 0,70)",
            tamanho_efeito=0.70, evidencia="Nível B — França 2020 / Yin 2023", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Yin et al., 2023)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_FRANCA_2020, meta_analise=REF_YIN_2023,
            mcid_valor=4.0, mcid_label="+11,77% na BBS", cohen_d_valor=0.70, cohen_d_interp="Moderado",
            estudo_referencia="França et al. (2020) / Benussi et al. (2021)", efeito_resumo="SARA reduziu de 17,5 para 15,9 (9,1%; SMD 0,70) e +11,77% na BBS",
            escalas_detalhadas=[scale_bbs],
            escalas_por_fator={"equilibrio": ["bbs"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM16-EQ-P1", "Protocolo Inicial — cbTMS 1 Hz Hemisférios Cerebelares", "cbTMS 1 Hz — Hemisférios Cerebelares 1.800 p (França et al., 2020)", "cbTMS (1 Hz)", "Hemisférios cerebelares (900 p / 900 p)", "1 Hz | 100% LMR | 1.800 pulsos/sessão", sessoes="10 a 20 sessões", efeito_esperado="SARA 17,5 -> 15,9 (9,1%; SMD 0,70)", referencia="França et al. (2020) · DOI: 10.1016/j.parkreldis.2020.09.001", linha_fluxograma="solida", fase_etapa="inicial"),
                _ax_cs(2, "ajustes"),
            ],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Conduzir exercícios de equilíbrio associados em nível de fadiga leve-moderado.",
            audit_meta=_audit("Moderada", "Metanálise equilíbrio em ataxia (Yin et al., 2023).", "Efeito clínico na BBS e SARA.", ["Risco de viés"], "Moderada", "Condicional", "Reavaliar semanalmente via pré-teste e auto-relato.", tol_ax),
        ),
        "disartria": make_mod(
            protocolo_id="RM16-DIS", tecnica="ctDCS Cerebelo Global + Deltoide Direito (Libri et al., 2024)", modalidade_sigla="ctDCS Cerebelar",
            alvo="Cerebelo global (2 cm abaixo do ínion) + cátodo no deltoide direito", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min", sessoes="10 a 20 sessões associadas à fonoterapia da fala",
            escala_recomendada="Subitens disartria SARA/ICARS + DDK + V-RQOL", meta_melhora="Benefício indicativo nos subitens de disartria e inteligibilidade",
            tamanho_efeito=0.45, evidencia="Nível C — Evidência emergente para disartria atáxica (Balzan 2022)", linha_fluxograma="solida",
            diretriz_internacional="Exploratório (Balzan et al., 2022)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_LIBRI_2024, meta_analise=REF_BALZAN_2022,
            mcid_valor=1.0, mcid_label="Melhora perceptivo-acústica / DDK", cohen_d_valor=0.45, cohen_d_interp="Pequeno",
            estudo_referencia="Libri et al. (2024) / Zhu et al. (2023)", efeito_resumo="Indicativo de benefício na fala com evidência clínica emergente",
            escalas_detalhadas=[scale_sara, scale_icars],
            escalas_por_fator={"disartria": ["sara", "icars"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM16-DIS-P1", "Protocolo Inicial — ctDCS Cerebelo / Deltoide Direito", "ctDCS Cerebelo Global + Deltoide Direito (Libri et al., 2024)", "ctDCS", "Cerebelo global (2 cm abaixo ínion) + cátodo deltoide D", "2,0 mA | 20 min", sessoes="10 a 20 sessões", efeito_esperado="Melhora em escores motores e fala", referencia="Libri et al. (2024) · DOI: 10.1007/s12311-023-01578-6", linha_fluxograma="solida", fase_etapa="inicial"),
                make_chain_step(2, "RM16-DIS-P2", "Próximo Protocolo (Linha Pontilhada) — cTBS Hemisfério Cerebelar Direito", "cTBS — Hemisfério Cerebelar Direito (Zhu et al., 2023)", "cTBS Cerebelar", "1 cm abaixo e 3 cm à direita do ínion", "50 Hz intra-burst (3 p), 5 Hz inter-burst | 600 p | 40 s | 80% AMT", sessoes="10 a 20 sessões", efeito_esperado="Estímulo exploratório à disartria atáxica", referencia="Zhu et al. (2023) · DOI: 10.3389/fnagi.2023.1215330", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
            ],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Ramo voltado à queixa associada de disartria atáxica; associar fonoterapia e acompanhar evolução perceptivo-acústica.",
            audit_meta=_audit("Moderada", "Revisão sistemática neurogenic dysarthria (Balzan et al., 2022).", "Ainda requer ensaios mais robustos para consolidação.", ["Evidência exploratória"], "Muito Baixa", "Condicional", "Sub-ramo de disartria com cTBS cerebelar direito em linha pontilhada.", tol_ax),
            mod_tipo="tdcs",
        ),
    }

    arvore = {
        "roadmap_id": "RM16",
        "titulo_fluxograma": "Ataxia Cerebelar — tDCS e rTMS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante clínico na Ataxia Cerebelar?",
                "subtitulo": "Selecione o fator limitante predominante para definir a rota terapêutica.",
                "opcoes": [
                    {"id": "severidade_motora", "rotulo": "Severidade da ataxia", "criterio": "SARA / ICARS", "descricao": "Inicia com csDCS cerebelo-espinal (Benussi et al., 2021) com escalonamento sequencial até M1.", "protocolo_alvo": "severidade_motora"},
                    {"id": "destreza_manual", "rotulo": "Destreza manual", "criterio": "9HPT / Box and Blocks / Purdue", "descricao": "Inicia com csDCS cerebelo-espinal (Benussi et al., 2021).", "protocolo_alvo": "destreza_manual"},
                    {"id": "mobilidade_funcional", "rotulo": "Mobilidade funcional", "criterio": "TC10m / TC8m / TC6min / TUG", "descricao": "Inicia com cbTMS circular (Sikandar et al., 2023).", "protocolo_alvo": "mobilidade_funcional"},
                    {"id": "equilibrio", "rotulo": "Equilíbrio", "criterio": "BBS / BESTest / Mini-BESTest", "descricao": "Inicia com cbTMS 1 Hz em hemisférios cerebelares (França et al., 2020).", "protocolo_alvo": "equilibrio"},
                    {"id": "disartria", "rotulo": "Disartria atáxica (meu paciente se queixa da disartria)", "criterio": "Subitens disartria SARA/ICARS, DDK, V-RQOL", "descricao": "Inicia com ctDCS cerebelar (Libri et al., 2024).", "protocolo_alvo": "disartria"},
                ],
            },
        },
        "ajuste_parametros": adj_ax,
        "protocolo_alternativo": {
            "nome": "LF-rTMS 1 Hz Núcleo Denteado (Cury et al., 2019) — Linha Pontilhada",
            "tecnica": "LF-rTMS (1 Hz — Neuronavegação)", "alvo": "Núcleo denteado (3 cm lateral e 1 cm inferior ao ínion)",
            "parametros": "1 Hz | 1.200 pulsos | 90% LMR", "observacoes": "Quadro tracejado; exige neuronavegação (-3,5 pts SARA).",
        },
        "protocolo_alternativo_2": {
            "nome": "Seção de Ajustes — ctDCS M1 C3/C4 Área Alternativa (Barretto et al., 2019)",
            "tecnica": "ctDCS M1", "alvo": "Ânodo C3 e C4 + Cátodo FP1/FP2 contralateral",
            "parametros": "2,0 mA | 20 min", "observacoes": "Área alternativa em M1 (-3,5 pts SARA / 22,4%, +14,21 s equilíbrio).",
        },
        "falha_terapeutica": {
            "id": "RM16-FALHA", "titulo": "Falha Terapêutica em Ataxia Cerebelar",
            "criterios_definicao": "Critérios de resposta insuficiente semanal mantidos após percorrer tDCS, rotas cerebelares de rTMS e áreas alternativas (M1 C3/C4).",
            "descricao": "Documentar ausência de mudança no pré-teste semanal e no auto-relato do paciente.",
            "condutas": ["Verificar uso de benzodiazepínicos.", "Ajustar fadiga da terapia motora associada (nível leve-moderado).", "Considerar extensão de sessões entre 10 e 20."],
        },
    }

    obs_ax = [
        make_obs("RM16-COORD-VERMIS", "Coordenada anatômica vérmis cerebelar: considerar 1 cm abaixo do ínion.", "alvo", categoria="anatomia", protocolo_ids=["severidade_motora", "destreza_manual", "mobilidade_funcional"]),
        make_obs("RM16-COORD-HEMISF", "Coordenada anatômica hemisférios cerebelares: considerar 1 cm abaixo do ínion e 3 cm laterais.", "alvo", categoria="anatomia", protocolo_ids=["equilibrio", "severidade_motora"]),
        make_obs("RM16-COORD-DENTEADO", "Núcleo denteado: requer obrigatoriamente utilização de neuronavegação (3 cm lateral e 1 cm inferior ao ínion).", "alvo", categoria="equipamento", protocolo_ids=["severidade_motora"], estagios=["alt2", "alt3"], severidade="warning"),
        make_obs("RM16-ELETRODO-T11", "Dimensão do eletrodo espinal (csDCS T11): usar eletrodo de 8 × 6 cm (48 cm²).", "alvo", categoria="equipamento", protocolo_ids=["severidade_motora", "destreza_manual", "mobilidade_funcional", "equilibrio"]),
        make_obs("RM16-FADIGA-TERAPIA", "Associar a estimulação à função que se deseja adquirir (motor/cognitivo); considerar realizar exercícios que mantenham o paciente no nível de fadiga leve-moderado.", "sessoes", categoria="clinica"),
        make_obs("RM16-TRACEJADO-EXP", "Protocolos em linha tracejada são experimentais (evidência ainda não validada por metanálises); opções para disartria atáxica ainda carecem de estudos mais robustos.", "stage", categoria="evidencia", protocolo_ids=["severidade_motora", "disartria"], estagios=["alt1", "alt2", "alt3"]),
        make_obs("RM16-BENZO-TEC", "Fique atento à presença de medicações que possam influenciar os efeitos da neuromodulação (ex.: benzodiazepínicos tendem a diminuir os efeitos terapêuticos).", "tec", categoria="clinica"),
        make_obs("RM16-AUTO-RELATO-SCALE", "Considerar o auto-relato do paciente em conjunto com a mudança objetiva nas escalas semanais.", "scale", categoria="avaliacao"),
        make_obs("RM16-TOL-EA", "Monitorar efeitos adversos durante e após a estimulação e registrar no Banco de Efeitos Adversos NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN"),
    ]

    return {
        "id": cid, "condicao": "Ataxia Cerebelar", "eixo": "Distúrbios do Movimento",
        "roadmap_id": "RM16", "svg_file": "RM16.svg",
        "fatores_limitantes": [
            {"id": "severidade_motora", "nome": "Severidade da ataxia", "instrumento_sugerido": "SARA / ICARS", "descricao": "Comprometimento atáxico global (csDCS/ctDCS, iTBS/rTMS cerebelar e área alternativa M1)."},
            {"id": "destreza_manual", "nome": "Destreza manual", "instrumento_sugerido": "Nine-Hole Peg / Box and Blocks", "descricao": "Dismetria e incoordenação fina de membros superiores."},
            {"id": "mobilidade_funcional", "nome": "Mobilidade funcional", "instrumento_sugerido": "TC10m / TC8m / TC6min", "descricao": "Velocidade e segurança na deambulação."},
            {"id": "equilibrio", "nome": "Equilíbrio", "instrumento_sugerido": "BBS / BESTest / Mini-BESTest", "descricao": "Ataxia troncular e instabilidade postural."},
            {"id": "disartria", "nome": "Disartria atáxica (queixa associada)", "instrumento_sugerido": "Subitens Disartria SARA/ICARS / V-RQOL", "descricao": "Ramo voltado à queixa de fala com cTBS cerebelar direito em linha pontilhada."},
        ],
        "arvore_algoritmo": arvore, "observacoes_contextuais": obs_ax, "modalidades": modalidades, "tags_busca": tags,
    }


def _build_parkinson():
    cid = "doenca-parkinson"
    tags = {
        "coordenadas_10_20": ["M1", "AMS (3 cm anterior)", "3 cm à frente de Cz", "F3 (DLPFC)", "T3 (tsMS)", "C7 (tsMS)", "T10-T12 (tsMS)"],
        "alvos_anatomicos": ["Área Motora Primária (M1)", "Área Motora Suplementar (AMS)", "Córtex Pré-Frontal Dorsolateral (DLPFC F3)", "Estimulação Trans-Espinal (tsMS T3/C7/T10-T12)"],
        "sinonimos_en": ["parkinson", "parkinson's disease", "pd", "freezing of gait", "fog", "bradykinesia", "rigidity", "levodopa-induced dyskinesia"],
        "sintomas_pt": ["parkinson", "função motora", "freezing of gait", "congelamento da marcha", "mobilidade funcional", "bradicinesia", "rigidez", "discinesia"],
        "escalas": ["MDS-UPDRS-III (Estado ON)", "NFOG-Q", "TUG", "TC6min"],
        "tecnicas": ["rTMS", "HF-rTMS", "LF-rTMS", "iTBS", "tsMS"],
    }
    tol_pd = _tol(
        "Cefaleia é o efeito adverso mais frequente durante/após estimulação; atenção a contraindicações (implantes metálicos e epilepsia não controlada).",
        "Em protocolos combinados cervicais (M1 + tsMS nível C7), aplicar intensidade reduzida a 50% da saída máxima do estimulador no nível C7.",
        "Fenótipo rígido-acinético apresenta melhor prognóstico; benzodiazepínicos diminuem os efeitos terapêuticos. Se discinesia por levodopa ou freezing, priorizar protocolos voltados a esses sintomas.",
    )

    scale_updrs_on = make_scale("updrs_iii_on", "MDS-UPDRS Seção III (Estado ON)", "MDS-UPDRS III (ON)", "reducao", "Redução ≥ 3,5 pts ou -15,1% a -57,7% na UPDRS-III no estado ON", 0.56, placeholder="Ex: 28", min_val=0, max_val=132, mcid_valor=3.5, mcid_label="-3,5 pts (-15% a -25%) na UPDRS-III (Estado ON)")
    scale_nfog = make_scale("nfog_q", "New Freezing of Gait Questionnaire (NFOG-Q)", "NFOG-Q", "reducao", "Redução ≥ 3,0 pts ou -15% a -23% no NFOG-Q", 0.54, placeholder="Ex: 16", min_val=0, max_val=28, mcid_valor=3.0, mcid_label="-15% a -23% no NFOG-Q")
    scale_tug_pd = make_scale("tug_pd", "Timed Up and Go Test (TUG / TUG dupla tarefa) e TC6min", "TUG / TC6min", "reducao", "Melhora ≥ 12,5% a 19,3% no tempo do TUG / velocidade da marcha", 0.55, placeholder="Ex: 18.0", min_val=3, max_val=120, mcid_valor=2.5, mcid_label="-12,5% a -19,3% no TUG")

    def _pd_step(ordem, pid, rotulo, nome, tec, alvo, params, sessoes, efeito, ref, linha="solida", fase="sequencia", obs=""):
        return make_chain_step(
            ordem, pid, rotulo, nome, tec, alvo, params,
            sessoes=sessoes, efeito_esperado=efeito, referencia=ref,
            linha_fluxograma=linha, fase_etapa=fase, observacoes=obs,
        )

    def _s_brys(ordem, fase="inicial"):
        return _pd_step(ordem, "RM17-P1", "M1 10 Hz Bilateral (Brys et al., 2016)", "HF-rTMS 10 Hz — M1 Hotspot Mão Bilateral (Brys et al., 2016)", "HF-rTMS (10 Hz)", "M1 hotspot mão bilateral (bobina figura em 8)", "10 Hz | 90% LMR | 1.000 p/área (40 p × 25 trens, 20 s IIT)", "10 a 20 sessões", "-15,10% UPDRS-III mantido por 30 dias", "Brys et al. (2016) · DOI: 10.1212/WNL.0000000000003279", "solida", fase)

    def _s_khedr19(ordem, fase="sequencia"):
        return _pd_step(ordem, "RM17-P2", "M1 20 Hz Bilateral (Khedr et al., 2019)", "HF-rTMS 20 Hz — M1 Hotspot Mão Bilateral (Khedr et al., 2019)", "HF-rTMS (20 Hz)", "M1 hotspot mão bilateral (bobina figura em 8)", "20 Hz | 90% LMR | 2.000 p/área (100 p × 20 trens, 25 s IIT, 5 min entre áreas)", "10 a 20 sessões", "-25,18% UPDRS-III pós e -22,83% em 30 dias", "Khedr et al. (2019) · DOI: 10.3233/JPD-181540", "solida", fase)

    def _s_yokoe(ordem, fase="sequencia"):
        return _pd_step(ordem, "RM17-P3", "AMS 10 Hz Bilateral (Yokoe et al., 2018)", "HF-rTMS 10 Hz — AMS Anterior ao Hotspot da Mão (Yokoe et al., 2018)", "HF-rTMS AMS (10 Hz)", "3 cm anterior ao hotspot da mão bilateral (bobina figura em 8 / circular)", "10 Hz | 100% LMR | 1.000 p/área (100 p × 10 trens, 20 s IIT)", "10 a 20 sessões", "-1,90 pts UPDRS-III após 3 sessões", "Yokoe et al. (2018) · DOI: 10.1016/j.jocn.2017.09.023", "solida", fase)

    def _s_mi(ordem, fase="sequencia"):
        return _pd_step(ordem, "RM17-P5", "AMS 10 Hz Abdutor do Hálux / Cz (Mi et al., 2019)", "HF-rTMS 10 Hz — AMS 3 cm à Frente do Abdutor do Hálux (Mi et al., 2019)", "HF-rTMS AMS (10 Hz)", "3 cm à frente do hotspot do abdutor do hálux (se ausente, 3 cm à frente de Cz; bobina circular)", "10 Hz | 90% LMR | 1.000 p/área (50 p × 20 trens, 55 s IIT)", "10 a 20 sessões", "-9,24% a -12,5% FOGQ e -7,6% a -14,98% UPDRS-III", "Mi et al. (2019) · DOI: 10.1016/j.parkreldis.2019.10.009", "solida", fase)

    def _s_aftanas(ordem, fase="sequencia"):
        return _pd_step(ordem, "RM17-P4", "Dual F3 10 Hz + M1 Tibial Anterior Bilateral (Aftanas et al., 2020)", "HF-rTMS Dual 10 Hz — F3 + M1 Tibial Anterior Bilateral (Aftanas et al., 2020)", "HF-rTMS Dual (DLPFC + M1)", "F3 (DLPFC) + M1 hotspot tibial anterior bilateral (bobina duplo cone)", "F3: 10 Hz 3.000 p (110% LMR) + M1: 10 Hz 2.000 p/área (100% LMR)", "20 sessões", "-57,69% UPDRS-III pós-20 sessões (-41,45% após 4 semanas)", "Aftanas et al. (2020) · DOI: 10.17116/jnevro202012005129", "solida", fase)

    def _s_song(ordem, fase="sequencia"):
        return _pd_step(ordem, "RM17-P6", "M1 Contralateral ao Lado Mais Comprometido (Song et al., 2024)", "HF-rTMS 10 Hz — M1 Contralateral ao Dimídio Mais Afetado (Song et al., 2024)", "HF-rTMS (10 Hz)", "M1 hotspot mão contralateral ao lado mais comprometido", "10 Hz | 90% LMR | 1.000 p/área (50 p × 20 trens, 55 s IIT)", "10 a 20 sessões", "-15,59% a -21,32% FOGQ e -12,41% TUG", "Song et al. (2024) · DOI: 10.3389/fnagi.2024.1354455", "solida", fase, obs="Regra de Aplicação: iniciar obrigatoriamente pelo hemisfério contralateral ao lado mais comprometido do paciente.")

    def _s_khedr06(ordem, fase="inicial"):
        return _pd_step(ordem, "RM17-P8", "M1 Hotspot Membro Inferior + Mão Bilateral (Khedr et al., 2006)", "HF-rTMS 10 Hz — M1 MI + Mão Bilateral (Khedr et al., 2006)", "HF-rTMS (10 Hz)", "M1 membro inferior + mão bilateral (bobina circular/8)", "10 Hz | 100% LMR | 1.000 p/área (50 p × 20 trens, 50 s IIT)", "6 a 15 sessões", "-12,54% velocidade da caminhada", "Khedr et al. (2006) · DOI: 10.1002/mds.21089", "solida", fase)

    def _s_menezes(ordem):
        return _pd_step(ordem, "RM17-P9", "Seção de Ajustes — tsMS iTBS Nível T3 (Linha Pontilhada)", "tsMS iTBS — Coluna Torácica T3 (Menezes et al., 2024)", "tsMS iTBS (Exploratório)", "Coluna torácica nível T3", "iTBS 5 Hz / 50 Hz | 1.200 pulsos (20 triplets × 20 trens, 8 s IIT) | 100% LMR", "5 a 10 sessões", "-19,26% no TUG após 5 sessões", "Menezes et al. (2024) · DOI: 10.1002/mds.29776", "pontilhada", "ajustes")

    def _s_khedr25(ordem):
        return _pd_step(ordem, "RM17-P10", "Seção de Ajustes — Dual M1 + tsMS Nível C7 (Linha Pontilhada)", "rTMS M1 + tsMS Nível C7 com Ajuste de Segurança (Khedr et al., 2025)", "rTMS + tsMS (Ajuste de Segurança)", "M1 1º interósseo dorsal bilat + tsMS C7", "M1 20 Hz 2.000 p/área 80% LMR + tsMS C7 10 Hz 1.500 p a 50% saída", "10 sessões", "-32 s no TUG logo após 10 sessões (-35 s em 1 mês)", "Khedr et al. (2025) · DOI: 10.1177/15459683241300547", "pontilhada", "ajustes", obs="Ajuste de Segurança: parâmetros reduzidos a 50% da saída máxima do estimulador no nível C7 para proteção do paciente.")

    def _s_wang24(ordem):
        return _pd_step(ordem, "RM17-P7", "Seção de Ajustes — M1 Tibial Anterior + tsMS T10-T12 (Linha Pontilhada)", "LF-rTMS 1 Hz M1 + tsMS T10-T12 (Wang et al., 2024)", "LF-rTMS + tsMS (1 Hz — Exploratório)", "M1 tibial ant. bilateral + tsMS nível T10-T12 (duplo cone)", "1 Hz | 120% LMR 800 p M1 + 1 Hz 1.500 p tsMS p/ contração MMII", "10 sessões", "-23,02% FOGQ pós-sessões", "Wang et al. (2024) · DOI: 10.1038/s41531-024-00792-1", "pontilhada", "ajustes")

    adj_pd = {"titulo": "Ajustes de Bobina, Pulsos e Segurança — Parkinson", "tolerabilidade": "Cefaleia é o efeito adverso mais frequente durante/após a estimulação; checar contraindicações (implantes metálicos e epilepsia não controlada).", "dose_pulsos": "Quanto maior a quantidade de pulsos (2.000–7.000 pulsos), maiores e mais duradouros os efeitos clínicos. Tem sido observada maior eficácia estendendo ciclos de 10 para 10 a 20 sessões. Ajuste de Segurança: na estimulação combinada M1 + tsMS nível C7, utilizar 50% da saída máxima do estimulador no nível C7.", "calibracao_limiar": "Iniciar M1 unilateral pelo hemisfério oposto ao dimídio mais comprometido; usar 3 cm à frente de Cz quando o hotspot do abdutor do hálux não for identificado e adotar bobina circular em MMII e AMS."}
    falha_pd = {"criterio": "Sem mudança nas escalas pré-teste após 1 semana OU piora dos sintomas motores (bradicinesia e tremores mais evidentes, aumento na frequência de freezing) após percorrer os protocolos previstos e a seção de Ajustes.", "conduta_oficial": "1. Conferir aderência ao estado 'ON' dopaminérgico durante todas as sessões;\n2. Checar interferência de benzodiazepínicos;\n3. Priorizar protocolos específicos caso haja freezing of gait ou discinesia induzida por levodopa."}
    sa_pd = {"quando_reavaliar": "Se em 1 semana o paciente não teve mudança de pontuação nas escalas de pré-teste OU apresentou piora motora (bradicinesia, tremores, freezing), seguir para o próximo protocolo.", "ajuste_dose": "Associar treino funcional motor/marcha ao objetivo clínico e progredir a carga total de pulsos quando bem tolerado.", "regra_interrupcao": "Se houver piora motora ou ausência de mudança em 1 semana, seguir diretamente na sequência; platô sustentado indica manutenção."}

    modalidades = {
        "funcao_global": make_mod(
            protocolo_id="RM17-M1", tecnica="HF-rTMS 10 Hz — M1 Bilateral (Brys et al., 2016)", modalidade_sigla="rTMS M1 Bilateral",
            alvo="M1 hotspot da mão bilateral (bobina figura em 8)", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="1.000 p/área (40 p × 25 trens, 20 s IIT)", sessoes="10 a 20 sessões",
            escala_recomendada="MDS-UPDRS III (Estado ON)", meta_melhora="-15,10% na UPDRS-III mantido por 30 dias",
            tamanho_efeito=0.56, evidencia="Nível B — Metanálises Li 2022 / Zhang 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020 · Zhang et al., 2022)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_BRYS_2016, meta_analise=REF_LI_2022_PD,
            mcid_valor=3.5, mcid_label="-3,5 pts UPDRS-III (Estado ON)", cohen_d_valor=0.56, cohen_d_interp="Moderado",
            estudo_referencia="Brys et al. (2016) / Khedr et al. (2019)", efeito_resumo="Redução de 15,1% a 25,18% na UPDRS-III mantida por 30 dias",
            escalas_detalhadas=[scale_updrs_on],
            escalas_por_fator={"dp_funcao_motora": ["updrs_iii_on"], "funcao_global": ["updrs_iii_on"]},
            cadeia_sequencial=[
                _s_brys(1, "inicial"),
                _s_khedr19(2, "sequencia"),
                _s_yokoe(3, "sequencia"),
                _s_mi(4, "sequencia"),
                _s_aftanas(5, "sequencia"),
                _s_khedr25(6),
                _s_wang24(7),
            ],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Aplicar TODOS os protocolos no estado 'ON' da medicação dopaminérgica. Pacientes com fenótipo rígido-acinético apresentam melhor prognóstico.",
            audit_meta=_audit("Moderada", "Metanálise de rTMS em sintomas motores da Doença de Parkinson (Li et al., 2022 / Zhang et al., 2022).", "Avaliação por alvos motores e estado dopaminérgico ON.", ["Risco de viés"], "Moderada", "Condicional", "Base consolidada por metanálise para M1 bilateral no estado ON.", tol_pd),
        ),
        "dp_ams": make_mod(
            protocolo_id="RM17-AMS", tecnica="HF-rTMS 10 Hz — Área Motora Suplementar (Yokoe et al., 2018)", modalidade_sigla="rTMS AMS",
            alvo="3 cm anterior ao hotspot da mão bilateral (bobina figura em 8 / circular)", frequencia="10 Hz", intensidade="100% LMR",
            pulsos_duracao="1.000 p/área (100 p × 10 trens, 20 s IIT)", sessoes="10 a 20 sessões",
            escala_recomendada="MDS-UPDRS III (Estado ON)", meta_melhora="-1,90 pts a -14,98% na UPDRS-III",
            tamanho_efeito=0.52, evidencia="Nível B — Metanálise AMS Chen 2025", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Chen et al., 2025)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_YOKOE_2018, meta_analise=REF_CHEN_2025_PD,
            mcid_valor=3.5, mcid_label="-3,5 pts UPDRS-III (ON)", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Yokoe et al. (2018) / Mi et al. (2019)", efeito_resumo="Melhora motora global e axial na Área Motora Suplementar",
            escalas_detalhadas=[scale_updrs_on],
            escalas_por_fator={"dp_funcao_motora": ["updrs_iii_on"], "funcao_global": ["updrs_iii_on"]},
            cadeia_sequencial=[
                _s_yokoe(1, "inicial"),
                _s_mi(2, "sequencia"),
                _s_aftanas(3, "sequencia"),
                _s_khedr25(4),
                _s_wang24(5),
            ],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Aplicar TODOS os protocolos no estado 'ON' da medicação dopaminérgica. Benzodiazepínicos tendem a diminuir os efeitos terapêuticos.",
            audit_meta=_audit("Moderada", "Metanálise dedicada à Área Motora Suplementar em Parkinson (Chen et al., 2025).", "Benefício consistente em sintomas axiais e bradicinesia.", ["Subgrupo AMS"], "Moderada", "Condicional", "Usar 3 cm à frente de Cz quando hotspot do abdutor do hálux ausente.", tol_pd),
        ),
        "dp_dlpfc": make_mod(
            protocolo_id="RM17-P4", tecnica="HF-rTMS Dual 10 Hz — F3 (DLPFC) + M1 Tibial Anterior Bilateral (Aftanas et al., 2020)", modalidade_sigla="rTMS Dual DLPFC+M1",
            alvo="F3 (DLPFC) + M1 hotspot tibial anterior bilateral (bobina duplo cone)", frequencia="10 Hz", intensidade="110% LMR (F3) + 100% LMR (M1)",
            pulsos_duracao="3.000 p (F3) + 2.000 p/área (M1)", sessoes="20 sessões",
            escala_recomendada="MDS-UPDRS III (Estado ON)", meta_melhora="-57,69% UPDRS-III pós-20 sessões (-41,45% após 4 sem)",
            tamanho_efeito=0.62, evidencia="Nível B — Quadro sólido Dual DLPFC+M1 (Aftanas 2020 · Zhang 2022)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Zhang et al., 2022)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_AFTANAS_2020, meta_analise=REF_ZHANG_2022_PD,
            mcid_valor=3.5, mcid_label="-3,5 pts UPDRS-III (ON)", cohen_d_valor=0.62, cohen_d_interp="Moderado",
            estudo_referencia="Aftanas et al. (2020)", efeito_resumo="Redução de 57,69% na UPDRS-III após 20 sessões (bobina duplo cone)",
            escalas_detalhadas=[scale_updrs_on],
            escalas_por_fator={"dp_funcao_motora": ["updrs_iii_on"], "funcao_global": ["updrs_iii_on"]},
            cadeia_sequencial=[
                _s_aftanas(1, "inicial"),
                _s_khedr25(2),
                _s_wang24(3),
            ],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Aplicar TODOS os protocolos no estado 'ON' da medicação dopaminérgica. Protocolo dual com bobina duplo cone e alta carga de pulsos.",
            audit_meta=_audit("Moderada", "Metanálise geral DP (Zhang et al., 2022).", "Protocolo dual F3+M1 com bobina duplo cone e alta carga de pulsos.", ["Alta carga de pulsos"], "Moderada", "Condicional", "Alta carga de pulsos (5.000–7.000 p); escalona para tsMS C7 e T10-T12 em Ajustes.", tol_pd),
        ),
        "fog": make_mod(
            protocolo_id="RM17-FOG", tecnica="HF-rTMS 10 Hz — AMS Abdutor do Hálux / Cz (Mi et al., 2019)", modalidade_sigla="rTMS AMS (FOG)",
            alvo="3 cm à frente do hotspot do abdutor do hálux (se ausente, 3 cm à frente de Cz; bobina circular)", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="1.000 p/área (50 p × 20 trens, 55 s IIT)", sessoes="10 a 20 sessões",
            escala_recomendada="NFOG-Q", meta_melhora="-9,24% a -23,02% no NFOG-Q",
            tamanho_efeito=0.54, evidencia="Nível B — Metanálise Freezing Xie 2020 / Mi 2019", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Xie et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_MI_2019, meta_analise=REF_XIE_2020_PD,
            mcid_valor=3.0, mcid_label="-15% a -23% no NFOG-Q", cohen_d_valor=0.54, cohen_d_interp="Moderado",
            estudo_referencia="Mi et al. (2019) / Song et al. (2024)", efeito_resumo="Redução progressiva do freezing of gait",
            escalas_detalhadas=[scale_nfog],
            escalas_por_fator={"fog": ["nfog_q"]},
            cadeia_sequencial=[
                _s_mi(1, "inicial"),
                _s_song(2, "sequencia"),
                _s_wang24(3),
            ],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Aplicar TODOS os protocolos no estado 'ON' da medicação dopaminérgica. Priorizar esta rota na presença de freezing of gait ou discinesia induzida por levodopa.",
            audit_meta=_audit("Moderada", "Metanálise rTMS em Freezing of Gait (Xie et al., 2020).", "Alinhada com Mi 2019 (AMS) e Song 2024 (M1 contralateral).", ["Risco de viés"], "Moderada", "Condicional", "Iniciar M1 pelo hemisfério contralateral ao dimídio mais comprometido.", tol_pd),
        ),
        "mobilidade": make_mod(
            protocolo_id="RM17-MOB", tecnica="HF-rTMS 10 Hz — M1 Membro Inferior + Mão Bilateral (Khedr et al., 2006)", modalidade_sigla="rTMS M1 Marcha",
            alvo="M1 membro inferior + mão bilateral (bobina circular / figura em 8)", frequencia="10 Hz", intensidade="100% LMR",
            pulsos_duracao="1.000 p/área (50 p × 20 trens, 50 s IIT)", sessoes="6 a 15 sessões",
            escala_recomendada="TUG / TUG dupla tarefa / TC6min", meta_melhora="-12,54% velocidade da caminhada a -19,26% no TUG",
            tamanho_efeito=0.55, evidencia="Nível B — Zhang 2022 / Xie 2020 (tsMS T3/C7/T10-T12 em Ajustes)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Zhang et al., 2022)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_KHEDR_2006, meta_analise=REF_ZHANG_2022_PD,
            mcid_valor=2.5, mcid_label="-12,5% a -19,3% no TUG", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Khedr et al. (2006) / Menezes et al. (2024)", efeito_resumo="-12,54% velocidade da marcha e -19,26% a -32 s no TUG",
            escalas_detalhadas=[scale_tug_pd],
            escalas_por_fator={"mobilidade": ["tug_pd"]},
            cadeia_sequencial=[
                _s_khedr06(1, "inicial"),
                _s_menezes(2),
                _s_khedr25(3),
                _s_wang24(4),
            ],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Aplicar TODOS os protocolos no estado 'ON' da medicação dopaminérgica. Na seção de Ajustes (tsMS nível C7), aplicar intensidade reduzida a 50% da saída máxima do estimulador.",
            audit_meta=_audit("Moderada", "Metanálise DP (Zhang et al., 2022) + ensaios recentes tsMS.", "Cadeia escalonada diretamente para tsMS T3, C7 (ajuste de segurança) e T10-T12.", ["Risco de viés"], "Moderada", "Condicional", "M1 sólido; tsMS T3, C7 e T10-T12 são opções exploratórias da seção de Ajustes.", tol_pd),
        ),
    }

    arvore = {
        "roadmap_id": "RM17",
        "titulo_fluxograma": "Árvore de Decisão — Doença de Parkinson: Sintomas Motores e rTMS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante na Doença de Parkinson?",
                "subtitulo": "Selecione o fator limitante predominante (Função Motora vs. Mobilidade).",
                "opcoes": [
                    {"id": "dp_funcao_motora", "rotulo": "Função Motora", "criterio": "MDS-UPDRS Seção III (Estado ON)", "descricao": "Escolha do alvo cortical motor.", "proxima_etapa": "alvo_funcao_motora"},
                    {"id": "dp_mobilidade", "rotulo": "Mobilidade (FOG / Marcha)", "criterio": "NFOG-Q / TUG / TC6min", "descricao": "Selecionar subtipo predominante de mobilidade.", "proxima_etapa": "subtipo_mobilidade"},
                ],
            },
            "alvo_funcao_motora": {
                "pergunta": "Qual é o alvo cortical inicial em Função Motora?",
                "subtitulo": "Três rotas de estimulação disponíveis: M1, AMS ou DLPFC.",
                "opcoes": [
                    {"id": "dp_m1", "rotulo": "Área Motora Primária (M1)", "criterio": "Base consolidada por metanálises", "descricao": "Inicia com HF-rTMS 10 Hz M1 bilateral (Brys et al., 2016).", "protocolo_alvo": "funcao_global"},
                    {"id": "dp_ams", "rotulo": "Área Motora Suplementar (AMS)", "criterio": "3 cm anterior ao hotspot mão / 3 cm Cz", "descricao": "Inicia com HF-rTMS 10 Hz AMS bilateral (Yokoe et al., 2018).", "protocolo_alvo": "dp_ams"},
                    {"id": "dp_dlpfc", "rotulo": "Córtex Pré-Frontal Dorsolateral (DLPFC)", "criterio": "Protocolo Dual F3 + M1 tibial anterior", "descricao": "Inicia com HF-rTMS Dual F3 10 Hz + M1 tibial anterior (Aftanas et al., 2020).", "protocolo_alvo": "dp_dlpfc"},
                ],
            },
            "subtipo_mobilidade": {
                "pergunta": "Qual é a limitação predominante na Mobilidade?",
                "subtitulo": "Bifurcação entre Freezing of Gait e Mobilidade Funcional/Marcha.",
                "opcoes": [
                    {"id": "fog", "rotulo": "Freezing of Gait", "criterio": "NFOG-Q (AMS / M1 contralateral / tsMS)", "descricao": "Inicia com HF-rTMS 10 Hz em AMS (Mi et al., 2019).", "protocolo_alvo": "fog"},
                    {"id": "mobilidade", "rotulo": "Mobilidade Funcional e Desempenho de Marcha", "criterio": "TUG / TUG dupla tarefa / TC6min", "descricao": "Inicia com HF-rTMS 10 Hz M1 MI+Mão bilateral (Khedr et al., 2006).", "protocolo_alvo": "mobilidade"},
                ],
            },
        },
        "ajuste_parametros": adj_pd,
        "protocolo_alternativo": {
            "nome": "Seção de Ajustes — tsMS iTBS Nível T3 (Menezes et al., 2024)",
            "tecnica": "tsMS iTBS", "alvo": "Coluna torácica nível T3", "parametros": "iTBS 5 Hz/50 Hz | 1.200 pulsos | 100% LMR",
            "observacoes": "-19,26% no TUG após 5 sessões.",
        },
        "protocolo_alternativo_2": {
            "nome": "Seção de Ajustes — Dual M1 + tsMS Nível C7 (Khedr et al., 2025)",
            "tecnica": "rTMS + tsMS", "alvo": "M1 1º interósseo dorsal + C7",
            "parametros": "M1 20 Hz 80% LMR + tsMS C7 10 Hz 50% saída estimulador",
            "observacoes": "Ajuste de Segurança: intensidade reduzida a 50% da saída máxima em C7 (-32 s no TUG).",
        },
        "falha_terapeutica": {
            "id": "RM17-FALHA", "titulo": "Falha Terapêutica em Doença de Parkinson",
            "criterios_definicao": "Sem alteração no pré-teste semanal ou piora dos sintomas motores (bradicinesia, tremores mais evidentes, aumento de freezing) após cadeia completa.",
            "descricao": "Conferir aderência ao estado ON dopaminérgico, medicações e escalonamento prévio.",
            "condutas": ["Conferir realização integral no estado ON.", "Revisar interações medicamentosas (benzodiazepínicos).", "Priorizar protocolo específico para discinesia/freezing quando presentes."],
        },
    }

    obs_pd = [
        make_obs("RM17-PRE-CONTRA", "Checar contraindicações absolutas (implantes metálicos na área de estimulação e epilepsia não controlada). Pacientes com fenótipo rígido-acinético têm melhor prognóstico; se houver discinesia induzida por levodopa ou freezing, priorizar protocolos voltados a esses sintomas.", "pre", categoria="clinica", severidade="warning"),
        make_obs("RM17-EXPLORATORIO-TEC", "Protocolos com borda pontilhada e opções da Seção de Ajustes (tsMS T3, C7 e T10-T12) representam base científica exploratória cujo nível de evidência ainda não foi validado por metanálises.", "stage", categoria="evidencia", protocolo_ids=["funcao_global", "dp_ams", "dp_dlpfc", "fog", "mobilidade"], estagios=["alt1", "alt2", "alt3", "alt4", "alt5", "alt6"]),
        make_obs("RM17-CONTRALAT-STAR", "Regra de Aplicação: iniciar a estimulação em M1 pelo hemisfério CONTRALATERAL ao lado mais comprometido do paciente.", "alvo", categoria="anatomia", protocolo_ids=["fog"]),
        make_obs("RM17-CZ-HASH", "Regra de Aplicação: caso não seja possível localizar o hotspot do abdutor do hálux na AMS, considerar 3 cm à frente de Cz. Utilizar bobina circular para áreas motoras de MMII e AMS.", "alvo", categoria="anatomia", protocolo_ids=["funcao_global", "dp_ams", "fog", "mobilidade"]),
        make_obs("RM17-CEFALEIA-TOL", "Cefaleia é o efeito adverso mais frequente durante/após a estimulação. Registrar ocorrências no Banco de Efeitos Adversos NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN"),
    ]

    return {
        "id": cid, "condicao": "Doença de Parkinson — Sintomas Motores e Marcha", "eixo": "Distúrbios do Movimento",
        "roadmap_id": "RM17", "svg_file": "RM17.svg",
        "fatores_limitantes": [
            {"id": "funcao_global", "nome": "Função Motora", "instrumento_sugerido": "MDS-UPDRS Seção III (Estado ON)", "descricao": "Bradicinesia, rigidez e função motora global em M1, AMS ou DLPFC."},
            {"id": "fog", "nome": "Freezing of Gait", "instrumento_sugerido": "NFOG-Q (versão atualizada)", "descricao": "Congelamento da marcha com protocolos em AMS, M1 contralateral e tsMS T10-T12."},
            {"id": "mobilidade", "nome": "Mobilidade Funcional e Desempenho de Marcha", "instrumento_sugerido": "Timed Up and Go / TC6min", "descricao": "Velocidade e estabilidade de marcha (M1 bilateral e tsMS T3, C7 e T10-T12)."},
        ],
        "arvore_algoritmo": arvore, "observacoes_contextuais": obs_pd, "modalidades": modalidades, "tags_busca": tags,
    }


def build_dor_movimento_conditions():
    """Returns Dor Neuropatica (RM05), Ataxia Cerebelar (RM16), and Doenca de Parkinson (RM17)."""
    return [_build_dor_neuropatica(), _build_ataxia(), _build_parkinson()]
