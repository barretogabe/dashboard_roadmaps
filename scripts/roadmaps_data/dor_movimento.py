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
        "Manter avaliação de alterações sensoriais (alodinia, hiperalgesia, hiperpatia), sono, humor e qualidade de vida, pois a analgesia pode consolidar nas semanas pós-indução.",
        "Redução < 20% na EVA em 5 sessões define resposta insatisfatória. Associar estimulação elétrica ou magnética periférica de forma segura quando indicado.",
    )

    scale_eva = make_scale("eva", "Escala Visual Analógica / Numérica de Dor (EVA / NRS)", "EVA / NRS", "reducao", "Redução ≥ 20% da intensidade da dor após 5 sessões (P1: -36%±76%; P2: -24%±6%; EM: -45,5%; DF: -29,5%)", 0.62, placeholder="Ex: 7.5", min_val=0, max_val=10, mcid_valor=2.0, mcid_label="-20% a -2,0 pts na EVA")
    scale_npsi = make_scale("npsi", "Inventário de Sintomas de Dor Neuropática (NPSI)", "NPSI", "reducao", "Redução de sintomas neuropáticos e alodinia (P3: -32%±48% NPSI após 3 sessões)", 0.56, placeholder="Ex: 42", min_val=0, max_val=100, mcid_valor=10.0, mcid_label="-20% a -32% no NPSI")
    scale_bpi = make_scale("bpi", "Inventário Breve de Dor (BPI — Multidimensional)", "BPI", "reducao", "Redução da interferência da dor em sono, humor e atividade geral", 0.54, placeholder="Ex: 6.0", min_val=0, max_val=10, mcid_valor=1.5, mcid_label="-1,5 pt no BPI")

    step_p3 = make_chain_step(2, "RM05-P3", "Protocolo 3 (rTMS M1 3.000 pulsos)", "Protocolo 3 — rTMS C3 10 Hz 3.000 pulsos (Attal et al., 2016)", "HF-rTMS (10 Hz)", "C3 (M1), figura em 8 (cabo para trás a 45° do plano sagital)", "10 Hz | 80% LMR | 3.000 pulsos | 30 trens | 20 s IIT", sessoes="3 a 10 sessões", efeito_esperado="-32%±48% no NPSI após 3 sessões consecutivas", referencia="Attal et al. (2016) · DOI: 10.1097/j.pain.0000000000000510")
    step_p4 = make_chain_step(3, "RM05-P4", "Protocolo 4 (tDCS C3/Fp2)", "Protocolo 4 — tDCS Anódica C3/Fp2 (Bonifácio de Assis et al., 2022)", "tDCS Anódica", "Ânodo C3 + Cátodo Fp2 (eletrodos 5 × 7 cm)", "2,0 mA | 20 min", sessoes="5 sessões consecutivas", efeito_esperado="-27%±81% intensidade da dor em lesão de plexo braquial", referencia="Bonifácio de Assis et al. (2022) · DOI: 10.1038/s41598-022-05254-3")
    step_sii = make_chain_step(4, "RM05-ALT-SII", "Protocolo Alternativo rTMS — SII", "Protocolo Alternativo — rTMS SII (2 cm posteriores a M1)", "HF-rTMS (10 Hz)", "Córtex Somatossensorial Secundário (SII — 2 cm posterior a M1)", "10 Hz | 90% LMR | 1.000 pulsos | trens de 50 pulsos | 10 s IIT", sessoes="7 sessões consecutivas", efeito_esperado="-38% NRS em dor neuropática resistente (orofacial)", referencia="Lindholm et al. (2015) · DOI: 10.1097/j.pain.0000000000000175")
    step_tsdcs = make_chain_step(2, "RM05-ALT-TSDCS", "Protocolo Alternativo — tsDCS", "Protocolo Alternativo — tsDCS Medular (Hodaj et al., 2023)", "tsDCS Medular", "MMSS: ânodo C4–C5, cátodo 8 cm abaixo | MMII: ânodo L1–L2, cátodo 8 cm abaixo (5 × 7 cm)", "2,0 mA | 20 minutos", sessoes="5 sessões consecutivas", efeito_esperado="Redução de 2 pontos na escala de dor", referencia="Hodaj et al. (2023) · DOI: 10.1093/braincomms/fcad191")

    adj_dor = {"titulo": "Ajustes, Orientação da Bobina e Abordagens Adjuvantes (Dor Neuropática)", "tolerabilidade": "Bobina em figura de 8 com cabo virado para trás a 45° do plano sagital; em alodinia mecânica, preferir rPMS (sem encostar a bobina na pele).", "dose_pulsos": "Adjuvantes a qualquer momento: Estimulação Elétrica Periférica (50 Hz, 200 µs, nível sensorial, 30 min) ou rPMS (4 Hz, 3.000 p, 15 trens, 1 s IIT).", "calibracao_limiar": "Melhoras frequentemente se consolidam nas semanas após o fim da indução; considerar manutenção para efeito analgésico sustentado."}
    falha_dor = {"criterio": "Redução da intensidade da dor < 20% na EVA em 5 sessões SEM melhora multidimensional associada após percorrer P1/P2 ➔ P3 ➔ P4/SII ou tsDCS.", "conduta_oficial": "1. Verificar redução < 20% na EVA aos 5 dias E avaliar alterações sensoriais (alodinia, hiperalgesia, hiperpatia), sono, humor e BPI;\n2. Associar adjuvantes periféricos (rPMS/PEP);\n3. Consolidar protocolos de manutenção caso analgesia tardia ocorra."}
    sa_dor = {"quando_reavaliar": "Redução < 20% na EVA em 5 sessões configura resposta insatisfatória (verificar também alodinia, hiperalgesia, sono e humor) e nas semanas após fim da indução.", "ajuste_dose": "Escalonar pulsos (2.000 p -> 3.000 p) ou mudar para tDCS/SII/tsDCS e associar rPMS/PEP quando indicado.", "regra_interrupcao": "Manter manutenção se efeito analgésico sustentado; avançar de protocolo se < 20% na EVA sem ganho sensorial, de sono ou humor."}

    modalidades = {
        "geral": make_mod(
            protocolo_id="RM05-P1", tecnica="Protocolo 1 — rTMS 20 Hz C3 (2.000 pulsos) -> 10 Hz 3.000 p -> tDCS -> SII", modalidade_sigla="rTMS 20 Hz M1",
            alvo="Córtex Motor Primário (C3) — bobina em figura de 8 (45° cabo para trás)", frequencia="20 Hz", intensidade="80% LMR",
            pulsos_duracao="2.000 pulsos | 10 trens | 30 s IIT", sessoes="5 a 10 sessões consecutivas (+ manutenção se necessário)",
            escala_recomendada="EVA / NRS / NPSI / BPI", meta_melhora="Redução ≥ 20% na EVA em 5 sessões (P1: -36%±76%)",
            tamanho_efeito=0.62, evidencia="Nível A — Umbrella Review Duarte-Moreira 2025 / Jiang 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível A (Lefaucheur et al., 2020 · Duarte-Moreira et al., 2025)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_KHEDR_2015, meta_analise=REF_DUARTE_MOREIRA_2025,
            mcid_valor=2.0, mcid_label="-20% a -2,0 pts na EVA", cohen_d_valor=0.62, cohen_d_interp="Moderado",
            estudo_referencia="Khedr et al. (2015)", efeito_resumo="Redução da intensidade da dor em 36%±76% após 10 sessões",
            escalas_detalhadas=[scale_eva, scale_npsi, scale_bpi],
            cadeia_sequencial=[
                make_chain_step(1, "RM05-P1", "Protocolo 1 (Primeira Linha Opção A)", "Protocolo 1 — HF-rTMS 20 Hz C3", "HF-rTMS (20 Hz)", "C3 (M1), figura em 8 (cabo 45° para trás)", "20 Hz | 80% LMR | 2.000 pulsos | 10 trens | 30 s IIT", sessoes="10 sessões", efeito_esperado="-36%±76% na intensidade da dor", referencia="Khedr et al. (2015) · DOI: 10.1002/ejp.576"),
                step_p3, step_p4, step_sii,
            ],
            ajuste_parametros=adj_dor, falha_terapeutica=falha_dor, sessoes_ajuste=sa_dor,
            notas_clinicas="Avaliar alodinia, hiperalgesia, hiperpatia, sono e humor além da intensidade bruta da EVA.",
            audit_meta=_audit("Alta", "Umbrella Review (Duarte-Moreira et al., 2025) + Metanálise (Jiang et al., 2022).", "Síntese de alta qualidade metodológica para dor neuropática crônica em M1.", ["Umbrella Review", "Risco de viés"], "Alta", "Forte", "Nível A para rTMS de alta frequência em M1 contralateral à dor.", tol_dor),
        ),
        "dor_geral_p2": make_mod(
            protocolo_id="RM05-P2", tecnica="Protocolo 2 — rTMS 10 Hz C3 (90% LMR, 60 trens) -> P3 -> tDCS -> SII", modalidade_sigla="rTMS 10 Hz M1",
            alvo="Córtex Motor Primário (C3) — figura em 8 (cabo 45° para trás)", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="2.000 pulsos | 60 trens | 25 s IIT", sessoes="5 a 10 sessões consecutivas",
            escala_recomendada="EVA / NRS / NPSI / BPI", meta_melhora="-24%±6% na intensidade da dor (Lefaucheur 2008)",
            tamanho_efeito=0.60, evidencia="Nível A — IFCN 2020 / Jiang 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível A (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_LEFAUCHEUR_2008, meta_analise=REF_JIANG_2022,
            mcid_valor=2.0, mcid_label="-20% a -2,0 pts na EVA", cohen_d_valor=0.60, cohen_d_interp="Moderado",
            estudo_referencia="Lefaucheur et al. (2008)", efeito_resumo="-24%±6% na intensidade da dor após sessão única/inicial",
            escalas_detalhadas=[scale_eva, scale_npsi, scale_bpi],
            cadeia_sequencial=[
                make_chain_step(1, "RM05-P2", "Protocolo 2 (Primeira Linha Opção B)", "Protocolo 2 — HF-rTMS 10 Hz C3 (90% LMR)", "HF-rTMS (10 Hz)", "C3 (M1), figura em 8 (cabo 45° para trás)", "10 Hz | 90% LMR | 2.000 pulsos | 60 trens | 25 s IIT", sessoes="5–10 sessões", efeito_esperado="-24%±6% na dor central/periférica", referencia="Lefaucheur et al. (2008) · DOI: 10.1136/jnnp.2007.135327"),
                step_p3, step_p4, step_sii,
            ],
            ajuste_parametros=adj_dor, falha_terapeutica=falha_dor, sessoes_ajuste=sa_dor,
            notas_clinicas="Opção inicial equivalente ao Protocolo 1 em dor neuropática central e/ou periférica.",
            audit_meta=_audit("Moderada", "Metanálise (Jiang et al., 2022) para rTMS em dor neuropática.", "Análise sistemática com avaliação de viés e heterogeneidade.", ["Risco de viés"], "Alta", "Forte", "Protocolo clássico de 10 Hz / 2.000 pulsos em M1.", tol_dor),
        ),
        "dor_fantasma": make_mod(
            protocolo_id="RM05-FANT", tecnica="tDCS Anódica C3/Fp2 (Kikkert 2019) -> rTMS P2 -> P3 -> SII", modalidade_sigla="tDCS -> rTMS M1",
            alvo="Ânodo em C3 e Cátodo em Fp2 (eletrodos 5 × 7 cm)", frequencia="Contínua (tDCS)", intensidade="2,0 mA",
            pulsos_duracao="20 min (5 × 7 cm)", sessoes="6 sessões consecutivas (escalonar p/ rTMS P2/P3 se sem resposta)",
            escala_recomendada="EVA / NRS / BPI", meta_melhora="-29,5%±25% na dor após 6 sessões",
            tamanho_efeito=0.58, evidencia="Nível B — Metanálise Pacheco-Barrios 2020", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017 · Pacheco-Barrios et al., 2020)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_KIKKERT_2019, meta_analise=REF_PACHECO_BARRIOS_2020,
            mcid_valor=2.0, mcid_label="-20% na EVA", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Kikkert et al. (2019)", efeito_resumo="Redução de 29,5%±25% após 6 sessões em membro fantasma",
            escalas_detalhadas=[scale_eva, scale_bpi, scale_npsi],
            cadeia_sequencial=[
                make_chain_step(1, "RM05-FANT-P1", "Protocolo 1 Dor Fantasma", "Protocolo 1 — tDCS C3/Fp2 (Kikkert et al., 2019)", "tDCS Anódica", "Ânodo C3 + Cátodo Fp2 (5 × 7 cm)", "2,0 mA | 20 min", sessoes="6 sessões", efeito_esperado="-29,5%±25% dor fantasma", referencia="Kikkert et al. (2019) · DOI: 10.1002/ana.25371"),
                make_chain_step(2, "RM05-P2", "Protocolo 2 rTMS M1", "Protocolo 2 — rTMS C3 10 Hz 2.000 p", "HF-rTMS", "C3 M1", "10 Hz | 90% LMR | 2.000 p", sessoes="5–10 sessões", efeito_esperado="-24%±6% na dor", referencia="Lefaucheur et al. (2008) · DOI: 10.1136/jnnp.2007.135327"),
                step_p3, step_sii,
            ],
            ajuste_parametros=adj_dor, falha_terapeutica=falha_dor, sessoes_ajuste=sa_dor,
            notas_clinicas="Se resposta insatisfatória após tDCS em membro fantasma, escalonar para rTMS Protocolos 2 e 3 e SII.",
            audit_meta=_audit("Moderada", "Metanálise dedicada à dor do membro fantasma (Pacheco-Barrios et al., 2020).", "Sinal consistente para tDCS anódica M1.", ["Risco de viés"], "Moderada", "Condicional", "Boa tolerabilidade inicial antes de rTMS.", tol_dor),
            mod_tipo="tdcs",
        ),
        "espinhal": make_mod(
            protocolo_id="RM05-EM", tecnica="tDCS Anódica C3/Fp2 (Mori 2010) -> tsDCS Medular C4-C5 / L1-L2 (Hodaj 2023)", modalidade_sigla="tDCS -> tsDCS",
            alvo="Ânodo C3 / Fp2 (P1) -> tsDCS Medular C4-C5 (MMSS) ou L1-L2 (MMII)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min (eletrodos 5 × 7 cm)", sessoes="5 sessões consecutivas (EM Remitente-Recorrente)",
            escala_recomendada="EVA / NRS / BPI", meta_melhora="-45,5%±11% na dor após 5 sessões (P1); -2 pts escala dor (tsDCS)",
            tamanho_efeito=0.55, evidencia="Nível B — Metanálise Esclerose Múltipla Uygur 2023", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_MORI_2010, meta_analise=REF_UYGUR_2023,
            mcid_valor=2.0, mcid_label="-20% a -2,0 pts na dor", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Mori et al. (2010)", efeito_resumo="Redução de 45,5%±11% na dor na Esclerose Múltipla em remissão",
            escalas_detalhadas=[scale_eva, scale_bpi, scale_npsi],
            cadeia_sequencial=[
                make_chain_step(1, "RM05-EM-P1", "Protocolo 1 Esclerose Múltipla", "Protocolo 1 — tDCS Anódica C3/Fp2 (Mori et al., 2010)", "tDCS Anódica", "Ânodo C3 + Cátodo Fp2 (5 × 7 cm)", "2,0 mA | 20 min", sessoes="5 sessões consecutivas", efeito_esperado="-45,5%±11% na dor crônica em EM", referencia="Mori et al. (2010) · DOI: 10.1016/j.jpain.2009.08.011"),
                step_tsdcs,
            ],
            ajuste_parametros=adj_dor, falha_terapeutica=falha_dor, sessoes_ajuste=sa_dor,
            notas_clinicas="Protocolo alternativo tsDCS (Hodaj 2023) varia montagem entre MMSS (C4-C5) e MMII (L1-L2).",
            audit_meta=_audit("Moderada", "Metanálise NIBS em Esclerose Múltipla (Uygur-Kucukseymen et al., 2023).", "Resultados consistentes em dor crônica associada à EM.", ["Risco de viés"], "Moderada", "Condicional", "Sequência direta tDCS -> tsDCS medular.", tol_dor),
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
                "subtitulo": "Selecione o quadro clínico predominante para definir o protocolo inicial.",
                "opcoes": [
                    {"id": "dor_geral", "rotulo": "Dor neuropática em geral", "criterio": "Duarte-Moreira et al., 2025 / Jiang 2022", "descricao": "Escolher entre Protocolo 1 (20 Hz) e Protocolo 2 (10 Hz).", "proxima_etapa": "dor_geral_inicial"},
                    {"id": "dor_fantasma", "rotulo": "Dor fantasma", "criterio": "Amputação de membro", "descricao": "Protocolo 1 (tDCS C3/Fp2, Kikkert 2019) -> P2 -> P3 -> SII.", "protocolo_alvo": "dor_fantasma"},
                    {"id": "dor_em", "rotulo": "Dor na Esclerose Múltipla", "criterio": "EM Remitente-Recorrente", "descricao": "Protocolo 1 (tDCS C3/Fp2, Mori 2010) -> Alt tsDCS (Hodaj 2023).", "protocolo_alvo": "espinhal"},
                ],
            },
            "dor_geral_inicial": {
                "pergunta": "Qual regime inicial de rTMS M1 deseja selecionar para Dor Neuropática em Geral?",
                "subtitulo": "Protocolo 1 (20 Hz) e Protocolo 2 (10 Hz) têm indicação inicial paralela e convergem ao Protocolo 3.",
                "opcoes": [
                    {"id": "dor_p1_20hz", "rotulo": "Protocolo 1 — 20 Hz, 80% LMR, 2.000 pulsos (10 trens)", "criterio": "Khedr et al. (2015)", "descricao": "-36%±76% dor após 10 sessões.", "protocolo_alvo": "geral"},
                    {"id": "dor_p2_10hz", "rotulo": "Protocolo 2 — 10 Hz, 90% LMR, 2.000 pulsos (60 trens)", "criterio": "Lefaucheur et al. (2008)", "descricao": "-24%±6% dor central/periférica.", "protocolo_alvo": "dor_geral_p2"},
                ],
            },
        },
        "ajuste_parametros": adj_dor,
        "protocolo_alternativo": {
            "nome": "Protocolo Alternativo — rTMS SII (Lindholm et al., 2015)",
            "tecnica": "HF-rTMS (10 Hz)", "alvo": "SII (2 cm posteriores a M1)", "parametros": "10 Hz | 90% LMR | 1.000 pulsos | trens de 50 p | 10 s IIT",
            "observacoes": "-38% NRS em dor orofacial resistente após 7 sessões.",
        },
        "protocolo_alternativo_2": {
            "nome": "Protocolo Alternativo — tsDCS Medular (Hodaj et al., 2023) / Adjuvantes rPMS-PEP",
            "tecnica": "tsDCS / rPMS / PEP", "alvo": "MMSS: C4–C5; MMII: L1–L2 (+ tronco nervoso em rPMS)",
            "parametros": "tsDCS 2 mA 20 min | rPMS 4 Hz 3.000p 15 trens 1 s IIT | PEP 50 Hz 200 µs 30 min",
            "observacoes": "Em alodinia mecânica, preferir rPMS por não necessitar contato da bobina com a pele algógena.",
        },
        "falha_terapeutica": {
            "id": "RM05-FALHA", "titulo": "Falha Terapêutica em Dor Neuropática",
            "criterios_definicao": "Redução < 20% na EVA em 5 sessões e ausência de resposta sensorial, sono, humor ou BPI após protocolos sequenciais e alternativos.",
            "descricao": "Considerar melhora multidimensional além da intensidade bruta e consolidação tardia pós-indução.",
            "condutas": ["Associar abordagens periféricas (rPMS 4 Hz ou PEP 50 Hz).", "Considerar SII (10 Hz) ou tsDCS conforme topografia."],
        },
    }

    obs_dor = [
        make_obs("RM05-BOBINA-45", "Nos protocolos envolvendo rTMS, a bobina em formato de 8 deve estar com o cabo virado para trás e angulada a 45 graus com o plano sagital.", "alvo", categoria="anatomia", protocolo_ids=["geral", "dor_geral_p2"], estagios=["primary", "alt1"], modalidades_tipo=["rtms"]),
        make_obs("RM05-ALODINIA-RPMS", "Na presença de alodinia mecânica, a associação com rPMS é preferível, pois não há necessidade de encostar a bobina diretamente na pele dolorosa.", "alvo", categoria="clinica"),
        make_obs("RM05-ADJUVANTES", "Abordagens adjuvantes opcionais (simultâneas ou subsequentes, a qualquer momento; baixa evidência, porém seguras): Estimulação Elétrica Periférica (50 Hz, 200 µs, nível sensorial, 30 min) ou rPMS (4 Hz, 3.000 pulsos, 15 trens, 1 s IIT — pequenas contrações sem dor sobre tronco/ponto motor).", "sessoes", categoria="parametros"),
        make_obs("RM05-ADJUVANTES-STAGE", "Associar rPMS (4 Hz, 3.000 pulsos, sem dor) ou Estimulação Elétrica Periférica (50 Hz, 200 µs, 30 min) se analgesia central parcial ou alodinia mecânica.", "stage", categoria="parametros", estagios=["alt1", "alt2"]),
        make_obs("RM05-POS-INDUCAO", "Os ensaios clínicos demonstram que os pacientes podem apresentar melhora nas semanas subsequentes ao término da indução; protocolos de manutenção podem ser úteis para sustentar o efeito analgésico.", "reeval", categoria="prognostico"),
        make_obs("RM05-REEVAL-20EVA", "REGRA CRÍTICA DE REAVALIAÇÃO: redução da intensidade da dor menor que 20% na EVA em 5 sessões configura Resposta Clínica Insatisfatória.", "reeval", categoria="reavaliacao", severidade="warning"),
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
        "Em estimulação medular T11 (csDCS), usar eletrodo de 8 × 6 cm (48 cm²). Em núcleo denteado, utilizar obrigatoriamente neuronavegação; para estimular vérmis considerar 1 cm abaixo do ínion e para hemisférios cerebelares 1 cm abaixo e 3 cm laterais.",
        "Qualidade da resposta em avaliação semanal + auto-relato do paciente; uso de benzodiazepínicos e extensão de ciclos para 10 a 20 sessões.",
    )

    scale_sara = make_scale("sara", "Scale for the Assessment and Rating of Ataxia (SARA)", "SARA", "reducao", "P1 csDCS: -4,8 pts (~25% SARA) | P2 Severidade: -1,92±1,50 pts (14,8% SARA) | P1 Equilíbrio: -1,6 pts (9,1% SARA)", 0.60, placeholder="Ex: 17.5", min_val=0, max_val=40, mcid_valor=1.5, mcid_label="-1,5 pt ou -9,1% a -25% na SARA")
    scale_icars = make_scale("icars", "International Cooperative Ataxia Rating Scale (ICARS)", "ICARS", "reducao", "P1 csDCS: -13,2 pts (~28% ICARS) | P2: -4,27±3,43 pts", 0.69, placeholder="Ex: 42", min_val=0, max_val=100, mcid_valor=3.5, mcid_label="-3,5 pts na ICARS")
    scale_bbs = make_scale("bbs", "Escala de Equilíbrio de Berg (BBS) / BESTest", "BBS", "aumento", "Equilíbrio P2 csDCS: melhora média de 11,77% na BBS", 0.58, placeholder="Ex: 34", min_val=0, max_val=56, mcid_valor=4.0, mcid_label="+11,77% na BBS")
    scale_9hpt = make_scale("nine_hpt", "Nine-Hole Peg Test (9HPT) / Box and Blocks Test", "9HPT", "reducao", "Destreza P1 csDCS: melhora de 12,83% no 9HPT", 0.50, placeholder="Ex: 38.0", min_val=5, max_val=300, mcid_valor=3.0, mcid_label="-12,83% no tempo do 9HPT")
    scale_tc10 = make_scale("tc10m", "Teste de Caminhada de 10 Metros (TC10m) / TUG", "TC10m / TUG", "reducao", "Mobilidade funcional: melhora de 31,11% no TC10m e -1,2 s (8,7%) no TUG", 0.55, placeholder="Ex: 14.0", min_val=2, max_val=120, mcid_valor=1.2, mcid_label="-8,7% TUG / -31,1% TC10m")

    step_cs = make_chain_step(1, "RM16-CSDCS", "csDCS (Cátodo T11 / Ânodo Cerebelo)", "csDCS Cerebelo-Espinal (Benussi et al., 2018/2021)", "csDCS", "Ânodo cerebelo global (2 cm abaixo ínion) + Cátodo T11 (eletrodo 8 × 6 cm = 48 cm²)", "2,0 mA | 20 min", sessoes="10 a 20 sessões", efeito_esperado="-4,8 pts (~25% SARA) e ~28% ICARS mantidos até 6 meses", referencia="Benussi et al. (2021) · DOI: 10.1093/brain/awab157")
    step_ct = make_chain_step(2, "RM16-CTDCS", "ctDCS Cerebelo / Deltoide Direito", "ctDCS Cerebelar (Libri et al., 2024)", "ctDCS", "Ânodo cerebelo global + Cátodo músculo deltoide direito", "2,0 mA | 20 min", sessoes="10 a 20 sessões", efeito_esperado="-0,6 pts SARA (4,4%) / Severidade P2: -1,92 pts (14,8% SARA)", referencia="Libri et al. (2024) · DOI: 10.1007/s12311-023-01578-6")
    step_itbs = make_chain_step(1, "RM16-ITBS", "Protocolo 3 (rTMS — iTBS Cerebelar)", "Protocolo 3 — iTBS Hemisférios Cerebelares", "iTBS Cerebelar", "Hemisférios cerebelares (1 cm abaixo do ínion e 3 cm laterais)", "600 pulsos/hemisfério (10 triplets/trem, 60 trens) | 90% LMR", sessoes="10 a 20 sessões", efeito_esperado="Melhora cinética na SARA/ICARS e 9HPT", referencia="Shiga et al. (2002) · Shi et al. (2023) · DOI: 10.1007/s00415-023-11848-2")
    step_dent = make_chain_step(2, "RM16-DENT", "Protocolo 4 (Experimental — Núcleo Denteado)", "Protocolo 4 — rTMS 1 Hz Núcleo Denteado (Neuronavegação)", "LF-rTMS (1 Hz — Experimental)", "Núcleo denteado (3 cm lateral e 1 cm inferior ao ínion, requer neuronavegação)", "1 Hz | 1.200 pulsos | 90% LMR", sessoes="10 a 20 sessões", efeito_esperado="-3,5 pts SARA (PGIC 5)", referencia="Cury et al. (2019) · DOI: 10.1016/j.parkreldis.2019.01.013", linha_fluxograma="pontilhada")
    step_m1_ct = make_chain_step(3, "RM16-P5", "Protocolo 5 Área Alternativa (C3/C4)", "Protocolo 5 — ctDCS M1 (C3/C4) + FP1/FP2", "ctDCS M1 (Área Alternativa)", "Ânodo C3 e C4 (M1) + Cátodo FP1 ou FP2 contralateral", "2,0 mA | 20 min", sessoes="10 a 20 sessões", efeito_esperado="-3,5 pts SARA (22,4%; d=1,09) e +14,21 s posturografia", referencia="Barretto et al. (2019)", linha_fluxograma="solida")

    adj_ax = {"titulo": "Ajustes de Tolerabilidade, Coordenadas e Dose em Ataxia Cerebelar", "tolerabilidade": "Monitorar eventos adversos durante e após a estimulação; checar benzodiazepínicos que tendem a diminuir os efeitos terapêuticos.", "dose_pulsos": "Tem sido observada maior quantidade de sessões do que as 10 habituais — optar por aumentar para 10 a 20 sessões. Eletrodo medular T11 mede 8 × 6 cm (48 cm²).", "calibracao_limiar": "Vérmis: 1 cm abaixo do ínion; Hemisférios cerebelares: 1 cm abaixo e 3 cm laterais; Núcleo denteado: requer obrigatoriamente neuronavegação."}
    falha_ax = {"criterio": "Sem mudança de pontuação nas escalas utilizadas como pré-teste após 1 semana e auto-relato negativo, após percorrer tDCS, rotas rTMS e áreas alternativas.", "conduta_oficial": "1. Verificar uso de benzodiazepínicos e aderência à terapia associada à função-alvo;\n2. Confirmar aumento do ciclo para 10 a 20 sessões;\n3. Escalonar de tDCS para iTBS/rTMS cerebelar ou área alternativa C3/C4 / deltoide direito."}
    sa_ax = {"quando_reavaliar": "De uma semana para a outra: sem mudança nas escalas de pré-teste para o microdesfecho + auto-relato negativo configura resposta insuficiente.", "ajuste_dose": "Aumentar o número de sessões do paciente para 10 a 20 sessões associadas à função-alvo.", "regra_interrupcao": "Se não houver mudança em 1 semana, avançar diretamente para o próximo protocolo."}

    modalidades = {
        "severidade_motora": make_mod(
            protocolo_id="RM16-SEV", tecnica="csDCS (T11/Cerebelo) -> ctDCS (Cerebelo/Deltoide D)", modalidade_sigla="csDCS -> ctDCS",
            alvo="Cerebelo global (2 cm abaixo ínion) + cátodo T11 (8 × 6 cm)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min | T11 eletrodo 48 cm² (8 × 6 cm)", sessoes="10 a 20 sessões associadas à função desejada (fadiga leve-moderada)",
            escala_recomendada="SARA / ICARS (+ auto-relato semanal)", meta_melhora="P1: -4,8 pts SARA (25%) / P2: -1,92 pts SARA (14,8%)",
            tamanho_efeito=0.60, evidencia="Nível B — Metanálise Matsugi 2024 / Benussi 2021", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Matsugi et al., 2024)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_BENUSSI_2021, meta_analise=REF_MATSUGI_2024,
            mcid_valor=1.5, mcid_label="-14,8% a -25% na SARA", cohen_d_valor=0.60, cohen_d_interp="Moderado",
            estudo_referencia="Benussi et al. (2021) / Shi et al. (2023)", efeito_resumo="SARA -4,8 pts (P1) e -1,92±1,50 pts / 14,8% (P2 Severidade)",
            escalas_detalhadas=[scale_sara, scale_icars], cadeia_sequencial=[step_cs, step_ct, step_m1_ct],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Se já utilizou tDCS sem resposta, migrar diretamente ao ramo rTMS (iTBS cerebelar ➔ rTMS núcleo denteado ➔ ctDCS C3/C4); manter exercícios motores em fadiga leve-moderada.",
            audit_meta=_audit("Moderada", "Metanálise cerebelar em ataxia (Matsugi et al., 2024).", "Consistência de csDCS e ctDCS sobre escores SARA/ICARS.", ["Risco de viés"], "Moderada", "Condicional", "P1 reduz SARA em ~25% (mantido até 6 meses); P2 reduz 14,8%.", tol_ax),
            mod_tipo="tdcs",
        ),
        "ataxia_rtms_nao_resp": make_mod(
            protocolo_id="RM16-RTMS", tecnica="iTBS Hemisférios Cerebelares -> rTMS 1 Hz Núcleo Denteado (Neuronavegação) -> ctDCS M1", modalidade_sigla="iTBS / rTMS Cerebelar",
            alvo="Hemisférios cerebelares (P3) -> Núcleo Denteado com neuronavegação -> M1 C3/C4", frequencia="iTBS / 1 Hz", intensidade="90% LMR",
            pulsos_duracao="600 p/hemisfério (iTBS) -> 1.200 p (1 Hz)", sessoes="10 a 20 sessões associadas ao treino motor (fadiga leve-moderada)",
            escala_recomendada="SARA / ICARS / 9HPT", meta_melhora="P2/P3: -1,92 pts SARA (14,8%); Núcleo Denteado/M1: -3,5 pts SARA (22,4%)",
            tamanho_efeito=0.58, evidencia="Nível B/C — Shi 2023 / Cury 2019 (Núcleo Denteado experimental)", linha_fluxograma="pontilhada",
            diretriz_internacional="Nível B/C (Matsugi et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_SHI_2023, meta_analise=REF_MATSUGI_2024,
            mcid_valor=1.5, mcid_label="-1,92 a -3,5 pts na SARA", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Shi et al. (2023) / Cury et al. (2019)", efeito_resumo="Melhora em função cinética (14,8% SARA) e equilíbrio postural (22,4% SARA)",
            escalas_detalhadas=[scale_sara, scale_icars, scale_9hpt], cadeia_sequencial=[step_itbs, step_dent, step_m1_ct],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Ramo para não-respondedores à tDCS; Protocolo em núcleo denteado exige neuronavegação (indicação exploratória).",
            audit_meta=_audit("Moderada", "Metanálise cerebelar (Matsugi et al., 2024).", "Inclui ECRs em iTBS e rTMS cerebelar.", ["Risco de viés"], "Baixa", "Condicional", "Núcleo denteado é protocolo experimental tracejado.", tol_ax),
        ),
        "destreza_manual": make_mod(
            protocolo_id="RM16-DEST", tecnica="csDCS (T11/Cerebelo) -> ctDCS (Cerebelo/Deltoide D) / ctDCS M1", modalidade_sigla="csDCS -> ctDCS",
            alvo="Cerebelo (2 cm abaixo ínion) + T11 (8 × 6 cm)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min", sessoes="10 a 20 sessões com treino de destreza (fadiga leve-moderada)",
            escala_recomendada="9HPT / Box and Blocks / Purdue / Jebsen Taylor", meta_melhora="Melhora de 12,83% no 9HPT (P1) e -4,4% SARA (P2)",
            tamanho_efeito=0.50, evidencia="Nível B — Benussi 2021 / Libri 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Matsugi et al., 2024)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_LIBRI_2024, meta_analise=REF_MATSUGI_2024,
            mcid_valor=3.0, mcid_label="-12,83% no tempo do 9HPT", cohen_d_valor=0.50, cohen_d_interp="Moderado",
            estudo_referencia="Benussi et al. (2021) / Libri et al. (2024)", efeito_resumo="+12,83% de melhora no 9HPT e -0,6 pts na SARA (d=0,50)",
            escalas_detalhadas=[scale_9hpt, scale_sara], cadeia_sequencial=[step_cs, step_ct, step_m1_ct],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Associar tarefas de destreza manual ao nível de fadiga leve-moderado.",
            audit_meta=_audit("Moderada", "Metanálise ataxia (Matsugi et al., 2024).", "Consistente em destreza fina.", ["Risco de viés"], "Moderada", "Condicional", "Combinar com treino manual direcionado.", tol_ax),
            mod_tipo="tdcs",
        ),
        "mobilidade_funcional": make_mod(
            protocolo_id="RM16-MOB", tecnica="cbTMS Bobina Circular (1 Hz) -> csDCS (T11/Cerebelo) -> ctDCS M1", modalidade_sigla="cbTMS -> csDCS",
            alvo="Hemisfério D -> Vérmis -> Hemisfério E (cbTMS) / T11+Cerebelo (csDCS)", frequencia="1 Hz (cbTMS) / Contínua (csDCS)", intensidade="90% LMR / 2,0 mA",
            pulsos_duracao="10 pulsos/área (5 anti-horário + 5 horário, IIT 6 s) -> 20 min", sessoes="10 a 20 sessões",
            escala_recomendada="TC10m / TC8m / TC6min / TUG", meta_melhora="Melhora de 31,11% no TC10m e -1,2 s (8,7%) no TUG",
            tamanho_efeito=0.55, evidencia="Nível B/C — Protocolo 1 exploratório (Sikandar 2023) -> csDCS", linha_fluxograma="pontilhada",
            diretriz_internacional="Nível B (Yin et al., 2023)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_SIKANDAR_2023, meta_analise=REF_YIN_2023,
            mcid_valor=1.2, mcid_label="-1,2 s (-8,7%) TUG / -31,1% TC10m", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Sikandar et al. (2023) / Benussi et al. (2021)", efeito_resumo="31,11% no TC10m, -1,2 s (8,7%) no TUG e -0,6 pts SARA",
            escalas_detalhadas=[scale_tc10, scale_sara],
            cadeia_sequencial=[
                make_chain_step(1, "RM16-MOB-P1", "Protocolo 1 cbTMS Circular (Experimental)", "Protocolo 1 — cbTMS Bobina Circular (10 pulsos/área)", "cbTMS (Bobina Circular — Experimental)", "Hemisfério D -> Vérmis -> Hemisfério E", "5 pulsos anti-horários + 5 horários, IIT 6 s | 1 Hz | 90% LMR", sessoes="10 a 20 sessões", efeito_esperado="+31,11% TC10m e -8,7% TUG", referencia="Sikandar et al. (2023) · DOI: 10.1016/j.parkreldis.2022.105236", linha_fluxograma="pontilhada"),
                step_cs, step_m1_ct,
            ],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Protocolo 1 com bobina circular em indicação exploratória; segue csDCS e áreas alternativas.",
            audit_meta=_audit("Moderada", "Metanálise marcha/equilíbrio em ataxia (Yin et al., 2023).", "Resultados consistentes em TC10m e TUG.", ["Risco de viés"], "Moderada", "Condicional", "Associar treino de marcha em fadiga leve-moderada.", tol_ax),
        ),
        "equilibrio": make_mod(
            protocolo_id="RM16-EQ", tecnica="cbTMS 1 Hz Hemisférios Cerebelares (1.800 p) -> csDCS T11 / ctDCS Deltoide D", modalidade_sigla="cbTMS -> csDCS / ctDCS",
            alvo="Hemisférios cerebelares bilateral (2 cm abaixo do ínion; 1 cm abaixo/3 cm lateral)", frequencia="1 Hz (cbTMS) / Contínua (csDCS/ctDCS)", intensidade="100% LMR / 2,0 mA",
            pulsos_duracao="900 p/hemisfério (1.800 p/sessão) -> 20 min csDCS / ctDCS", sessoes="10 a 20 sessões associadas a treino de equilíbrio (fadiga leve-moderada)",
            escala_recomendada="SARA / BBS / BESTest / Mini-BESTest", meta_melhora="SARA 17,5->15,9 (9,1% · SMD 0,70) e +11,77% na BBS",
            tamanho_efeito=0.70, evidencia="Nível B — França 2020 / Yin 2023", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Yin et al., 2023)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_FRANCA_2020, meta_analise=REF_YIN_2023,
            mcid_valor=1.6, mcid_label="-1,6 pt (9,1%) SARA / +11,77% BBS", cohen_d_valor=0.70, cohen_d_interp="Moderado",
            estudo_referencia="França et al. (2020) / Benussi et al. (2021) / Libri et al. (2024)", efeito_resumo="SARA reduziu de 17,5 para 15,9 (9,1%; SMD 0,70); P2 +11,77% BBS",
            escalas_detalhadas=[scale_sara, scale_bbs],
            cadeia_sequencial=[
                make_chain_step(1, "RM16-EQ-P1", "Protocolo 1 cbTMS Equilíbrio", "Protocolo 1 — cbTMS Hemisférios Cerebelares (1.800 p)", "cbTMS (1 Hz)", "Hemisférios cerebelares (900 p / 900 p)", "1 Hz | 100% LMR | 1.800 pulsos/sessão", sessoes="10 a 20 sessões", efeito_esperado="SARA 17,5 -> 15,9 (9,1%; SMD 0,70)", referencia="França et al. (2020) · DOI: 10.1016/j.parkreldis.2020.09.001"),
                step_cs, step_ct,
            ],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Conduzir exercícios de equilíbrio associados em nível de fadiga leve-moderado; áreas alternativas incluem csDCS (T11/cerebelo) e ctDCS (cerebelo/deltoide D).",
            audit_meta=_audit("Moderada", "Metanálise equilíbrio em ataxia (Yin et al., 2023).", "Efeito clínico de 9,1% na SARA e 11,77% na BBS.", ["Risco de viés"], "Moderada", "Condicional", "Reavaliar semanalmente via pré-teste + auto-relato.", tol_ax),
        ),
        "disartria": make_mod(
            protocolo_id="RM16-DIS", tecnica="ctDCS Cerebelo/Deltoide D -> cbTMS cTBS Hemisfério Direito (Exploratório)", modalidade_sigla="ctDCS / cTBS (Exploratório)",
            alvo="Cerebelo global -> Hemisfério cerebelar D: 1 cm abaixo e 3 cm à direita do ínion (Exploratório)", frequencia="Contínua / cTBS (50 Hz intra, 5 Hz inter)", intensidade="2,0 mA / 80% AMT",
            pulsos_duracao="20 min (ctDCS) / cTBS 600 pulsos em 40 s (Exploratório)", sessoes="10 a 20 sessões associadas à fonoterapia da fala",
            escala_recomendada="Subitens disartria SARA/ICARS + DDK + V-RQOL", meta_melhora="Benefício indicativo nos subitens de disartria e inteligibilidade",
            tamanho_efeito=0.45, evidencia="Nível C — Opções experimentais (ainda requer mais estudos)", linha_fluxograma="pontilhada",
            diretriz_internacional="Exploratório (Balzan et al., 2022)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_LIBRI_2024, meta_analise=REF_BALZAN_2022,
            mcid_valor=1.0, mcid_label="Melhora perceptivo-acústica / DDK", cohen_d_valor=0.45, cohen_d_interp="Pequeno",
            estudo_referencia="Libri et al. (2024) / Zhu et al. (2023)", efeito_resumo="Indicativo de benefício na fala com evidência experimental",
            escalas_detalhadas=[scale_sara, scale_icars],
            cadeia_sequencial=[
                make_chain_step(1, "RM16-DIS-P1", "Área 1 — ctDCS Disartria", "Protocolo 1 — ctDCS Cerebelo/Deltoide D", "ctDCS", "Cerebelo global (2 cm abaixo ínion) + cátodo deltoide D", "2,0 mA | 20 min", sessoes="10 a 20 sessões", efeito_esperado="Melhora em escores motores e fala", referencia="Libri et al. (2024) · DOI: 10.1007/s12311-023-01578-6"),
                make_chain_step(2, "RM16-DIS-P2", "Área Alternativa 2 — cTBS Cerebelo D (Experimental)", "Protocolo 2 — cTBS Hemisfério Cerebelar Direito", "cTBS Cerebelar", "1 cm abaixo e 3 cm à direita do ínion", "50 Hz intra-burst (3 p), 5 Hz inter-burst | 600 p | 40 s | 80% AMT", sessoes="10 a 20 sessões", efeito_esperado="Estímulo experimental à disartria atáxica", referencia="Zhu et al. (2023) · DOI: 10.3389/fnagi.2023.1215330", linha_fluxograma="pontilhada"),
            ],
            ajuste_parametros=adj_ax, falha_terapeutica=falha_ax, sessoes_ajuste=sa_ax,
            notas_clinicas="Opções experimentais para queixa associada de disartria atáxica; associar fonoterapia.",
            audit_meta=_audit("Moderada", "Revisão sistemática neurogenic dysarthria (Balzan et al., 2022).", "Ainda requer ensaios mais robustos para consolidação.", ["Evidência exploratória"], "Muito Baixa", "Condicional", "Sub-ramo experimental tracejado (disartria atáxica).", tol_ax),
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
                    {"id": "severidade_motora", "rotulo": "Severidade da ataxia", "criterio": "SARA / ICARS", "descricao": "Avaliar se paciente já utilizou tDCS sem resposta.", "proxima_etapa": "ataxia_prev_tdcs"},
                    {"id": "destreza_manual", "rotulo": "Destreza manual", "criterio": "9HPT / Box and Blocks / Purdue", "descricao": "csDCS (P1) -> ctDCS (P2) -> ctDCS M1.", "protocolo_alvo": "destreza_manual"},
                    {"id": "mobilidade_funcional", "rotulo": "Mobilidade funcional", "criterio": "TC10m / TC8m / TC6min / TUG", "descricao": "cbTMS circular exploratório (P1) -> csDCS (P2) -> ctDCS M1.", "protocolo_alvo": "mobilidade_funcional"},
                    {"id": "equilibrio", "rotulo": "Equilíbrio", "criterio": "BBS / BESTest / Mini-BESTest", "descricao": "cbTMS 1 Hz (P1: -9,1% SARA) -> csDCS / ctDCS.", "protocolo_alvo": "equilibrio"},
                    {"id": "disartria", "rotulo": "Disartria atáxica (meu paciente se queixa da disartria)", "criterio": "Subitens disartria SARA/ICARS, DDK, V-RQOL", "descricao": "Rota exploratória (ctDCS -> cTBS hemisfério direito).", "protocolo_alvo": "disartria"},
                ],
            },
            "ataxia_prev_tdcs": {
                "pergunta": "Já utilizei tDCS, porém meu paciente não foi responsivo a essa técnica?",
                "subtitulo": "Bifurcação explícita dentro de Severidade da ataxia.",
                "opcoes": [
                    {"id": "ataxia_tdcs_nao", "rotulo": "NÃO — Iniciar com tDCS (csDCS -> ctDCS)", "criterio": "Primeira linha em Severidade", "descricao": "P1 csDCS T11/cerebelo (-25% SARA) -> P2 ctDCS (-14,8% SARA).", "protocolo_alvo": "severidade_motora"},
                    {"id": "ataxia_tdcs_sim", "rotulo": "SIM — Sem resposta à tDCS (Escalonar p/ rTMS / M1)", "criterio": "Segunda linha / Área alternativa", "descricao": "iTBS hemisférios cerebelares -> Núcleo denteado (Neuronavegação) -> ctDCS M1 C3/C4.", "protocolo_alvo": "ataxia_rtms_nao_resp"},
                ],
            },
        },
        "ajuste_parametros": adj_ax,
        "protocolo_alternativo": {
            "nome": "Protocolo 4 (Experimental) — rTMS Núcleo Denteado (Cury et al., 2019)",
            "tecnica": "LF-rTMS (1 Hz — Neuronavegação)", "alvo": "Núcleo denteado (3 cm lateral e 1 cm inferior ao ínion)",
            "parametros": "1 Hz | 1.200 pulsos | 90% LMR", "observacoes": "Quadro tracejado; exige neuronavegação (-3,5 pts SARA).",
        },
        "protocolo_alternativo_2": {
            "nome": "Protocolo 5 Área Alternativa — ctDCS M1 C3/C4 (Barretto et al., 2019)",
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
        make_obs("RM16-COORD-HEMISF", "Coordenada anatômica hemisférios cerebelares: considerar 1 cm abaixo do ínion e 3 cm laterais.", "alvo", categoria="anatomia", protocolo_ids=["equilibrio", "ataxia_rtms_nao_resp"]),
        make_obs("RM16-COORD-DENTEADO", "Núcleo denteado (Protocolo 4): requer obrigatoriamente utilização de neuronavegação (3 cm lateral e 1 cm inferior ao ínion).", "alvo", categoria="equipamento", protocolo_ids=["ataxia_rtms_nao_resp"], estagios=["primary", "alt1"], severidade="warning"),
        make_obs("RM16-ELETRODO-T11", "Dimensão do eletrodo espinal (csDCS T11): usar eletrodo de 8 × 6 cm (48 cm²).", "alvo", categoria="equipamento", protocolo_ids=["severidade_motora", "destreza_manual", "mobilidade_funcional", "equilibrio"]),
        make_obs("RM16-SESSOES-10-20", "Tem sido observada maior quantidade de sessões do que as 10 habituais — opte por aumentar o número de sessões do paciente (10 a 20 sessões).", "sessoes", categoria="parametros"),
        make_obs("RM16-FADIGA-TERAPIA", "Associar a estimulação à função que se deseja adquirir (motor/cognitivo); considerar realizar exercícios que mantenham o paciente no nível de fadiga leve-moderado.", "sessoes", categoria="clinica"),
        make_obs("RM16-TRACEJADO-EXP", "Protocolos em linha tracejada são experimentais; opções para disartria atáxica ainda carecem de estudos mais robustos.", "tec", categoria="evidencia", protocolo_ids=["ataxia_rtms_nao_resp", "mobilidade_funcional", "disartria"]),
        make_obs("RM16-BENZO-TEC", "Fique atento à presença de medicações que possam influenciar os efeitos da neuromodulação (ex.: benzodiazepínicos tendem a diminuir os efeitos terapêuticos).", "tec", categoria="clinica"),
        make_obs("RM16-REEVAL-SEMANAL", "Reavaliar a cada 1 semana. Resposta insuficiente: ausência de mudança de pontuação nas escalas utilizadas como pré-teste para o microdesfecho de uma semana para a outra + auto-relato do paciente.", "reeval", categoria="reavaliacao"),
        make_obs("RM16-AUTO-RELATO-SCALE", "Considerar o auto-relato do paciente em conjunto com a mudança objetiva nas escalas semanais.", "scale", categoria="avaliacao"),
        make_obs("RM16-TOL-EA", "Monitorar efeitos adversos durante e após a estimulação e registrar no Banco de Efeitos Adversos NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN"),
    ]

    return {
        "id": cid, "condicao": "Ataxia Cerebelar", "eixo": "Distúrbios do Movimento",
        "roadmap_id": "RM16", "svg_file": "RM16.svg",
        "fatores_limitantes": [
            {"id": "severidade_motora", "nome": "Severidade da ataxia", "instrumento_sugerido": "SARA / ICARS", "descricao": "Comprometimento atáxico global (csDCS/ctDCS e iTBS/rTMS se não responsivo)."},
            {"id": "destreza_manual", "nome": "Destreza manual", "instrumento_sugerido": "Nine-Hole Peg / Box and Blocks", "descricao": "Dismetria e incoordenação fina de membros superiores."},
            {"id": "mobilidade_funcional", "nome": "Mobilidade funcional", "instrumento_sugerido": "TC10m / TC8m / TC6min", "descricao": "Velocidade e segurança na deambulação."},
            {"id": "equilibrio", "nome": "Equilíbrio", "instrumento_sugerido": "BBS / BESTest / Mini-BESTest", "descricao": "Ataxia troncular e instabilidade postural."},
            {"id": "disartria", "nome": "Disartria atáxica (queixa associada)", "instrumento_sugerido": "Subitens Disartria SARA/ICARS / V-RQOL", "descricao": "Ramo experimental tracejado em queixa de fala."},
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
        "Aplicar sempre no estado 'ON' da medicação dopaminérgica. Ajuste de Segurança: no Protocolo 10 (Dual M1 + tsMS nível C7), aplicar a 50% da saída máxima no nível C7.",
        "Fenótipo rígido-acinético apresenta melhor prognóstico; benzodiazepínicos diminuem os efeitos terapêuticos. Se discinesia por levodopa ou freezing, priorizar protocolos voltados a esses sintomas.",
    )

    scale_updrs_on = make_scale("updrs_iii_on", "MDS-UPDRS Seção III (Estado ON)", "MDS-UPDRS III (ON)", "reducao", "Redução ≥ 3,5 pts ou -15,1% a -57,7% na UPDRS-III no estado ON", 0.56, placeholder="Ex: 28", min_val=0, max_val=132, mcid_valor=3.5, mcid_label="-3,5 pts (-15% a -25%) na UPDRS-III (Estado ON)")
    scale_nfog = make_scale("nfog_q", "New Freezing of Gait Questionnaire (NFOG-Q)", "NFOG-Q", "reducao", "P5: -9,24% a -12,5% FOGQ | P6: -15,59% a -21,32% FOGQ | P7: -23,02% FOGQ", 0.54, placeholder="Ex: 16", min_val=0, max_val=28, mcid_valor=3.0, mcid_label="-15% a -23% no NFOG-Q")
    scale_tug_pd = make_scale("tug_pd", "Timed Up and Go Test (TUG / TUG dupla tarefa) e TC6min", "TUG / TC6min", "reducao", "P8: -12,54% veloc. marcha | P9: -19,26% TUG | P10: -32 s no TUG", 0.55, placeholder="Ex: 18.0", min_val=3, max_val=120, mcid_valor=2.5, mcid_label="-12,5% a -19,3% no TUG")

    step_p1 = make_chain_step(1, "RM17-P1", "Protocolo 1 M1", "Protocolo 1 — M1 10 Hz Bilateral (Brys et al., 2016)", "HF-rTMS (10 Hz)", "M1 hotspot mão bilateral (bobina figura em 8)", "10 Hz | 90% LMR | 1.000 p/área (40 p × 25 trens, 20 s IIT)", sessoes="10 a 20 sessões (estado ON)", efeito_esperado="-15,10% UPDRS-III mantido por 30 dias", referencia="Brys et al. (2016) · DOI: 10.1212/WNL.0000000000003279")
    step_p2 = make_chain_step(2, "RM17-P2", "Protocolo 2 M1", "Protocolo 2 — M1 20 Hz Bilateral (Khedr et al., 2019)", "HF-rTMS (20 Hz)", "M1 hotspot mão bilateral (bobina figura em 8)", "20 Hz | 90% LMR | 2.000 p/área (100 p × 20 trens, 25 s IIT, 5 min entre áreas)", sessoes="10 a 20 sessões (estado ON)", efeito_esperado="-25,18% UPDRS-III pós e -22,83% em 30 dias", referencia="Khedr et al. (2019) · DOI: 10.3233/JPD-181540")
    step_p3 = make_chain_step(1, "RM17-P3", "Protocolo 3 AMS", "Protocolo 3 — AMS 10 Hz Bilateral (Yokoe et al., 2018)", "HF-rTMS AMS (10 Hz)", "3 cm anterior ao hotspot da mão bilateral (bobina figura em 8 / circular)", "10 Hz | 100% LMR | 1.000 p/área (100 p × 10 trens, 20 s IIT)", sessoes="10 a 20 sessões", efeito_esperado="-1,90 pts UPDRS-III após 3 sessões", referencia="Yokoe et al. (2018) · DOI: 10.1016/j.jocn.2017.09.023")
    step_p5 = make_chain_step(1, "RM17-P5", "Protocolo 5 AMS (Abdutor do Hálux / Cz)", "Protocolo 5 — AMS 3 cm à frente do Abdutor do Hálux (Mi et al., 2019)", "HF-rTMS AMS (10 Hz)", "3 cm à frente do hotspot do abdutor do hálux (se ausente, 3 cm à frente de Cz; bobina circular)", "10 Hz | 90% LMR | 1.000 p/área (50 p × 20 trens, 55 s IIT)", sessoes="10 a 20 sessões", efeito_esperado="-9,24% a -12,5% FOGQ e -7,6% a -14,98% UPDRS-III", referencia="Mi et al. (2019) · DOI: 10.1016/j.parkreldis.2019.10.009")

    adj_pd = {"titulo": "Ajustes Estado ON, Bobina Circular, Pulsos e Segurança — Parkinson", "tolerabilidade": "Aplicar sempre no estado 'ON' da medicação dopaminérgica. Cefaleia é o efeito adverso mais frequente durante/após a estimulação.", "dose_pulsos": "Quanto maior a quantidade de pulsos (2.000–7.000 pulsos), maiores e mais duradouros os efeitos no estado 'ON'. Realizar 10 a 20 sessões. Ajuste de Segurança: no Protocolo 10 (M1 + tsMS nível C7), utilizar 50% da saída máxima no nível C7.", "calibracao_limiar": "Regra de Aplicação: iniciar M1 contralateral (Protocolo 6) pelo hemisfério oposto ao dimídio mais comprometido; usar 3 cm à frente de Cz quando o hotspot do abdutor do hálux não for identificado e adotar bobina circular em MMII e AMS."}
    falha_pd = {"criterio": "Sem mudança nas escalas pré-teste após 1 semana OU piora dos sintomas motores (bradicinesia e tremores mais evidentes, aumento na frequência de freezing) após percorrer os protocolos previstos.", "conduta_oficial": "1. Conferir aderência ao estado 'ON' dopaminérgico;\n2. Checar interferência de benzodiazepínicos;\n3. Priorizar protocolos específicos caso haja freezing of gait ou discinesia induzida por levodopa."}
    sa_pd = {"quando_reavaliar": "Se em 1 semana o paciente não teve mudança de pontuação nas escalas utilizadas como pré-teste OU apresentou piora motora (bradicinesia, tremores, freezing), seguir para o próximo protocolo.", "ajuste_dose": "Progredir dose total de pulsos (2.000–7.000 p no estado 'ON') e sessões (10 a 20 sessões).", "regra_interrupcao": "Se houver piora motora ou ausência de mudança em 1 semana, seguir diretamente para o próximo protocolo."}

    modalidades = {
        "funcao_global": make_mod(
            protocolo_id="RM17-M1", tecnica="M1 10 Hz Bilateral (P1) -> M1 20 Hz Bilateral (P2)", modalidade_sigla="rTMS M1 Bilateral",
            alvo="M1 hotspot da mão bilateral (bobina figura em 8)", frequencia="10 Hz (P1) -> 20 Hz (P2)", intensidade="90% LMR",
            pulsos_duracao="1.000 p/área (P1) -> 2.000 p/área + 5 min pausa entre áreas (P2)", sessoes="10 a 20 sessões no estado ON",
            escala_recomendada="MDS-UPDRS III (Estado ON)", meta_melhora="-15,10% (P1) a -25,18% (P2) na UPDRS-III",
            tamanho_efeito=0.56, evidencia="Nível B — Metanálises Li 2022 / Zhang 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020 · Zhang et al., 2022)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_BRYS_2016, meta_analise=REF_LI_2022_PD,
            mcid_valor=3.5, mcid_label="-3,5 pts UPDRS-III (Estado ON)", cohen_d_valor=0.56, cohen_d_interp="Moderado",
            estudo_referencia="Brys et al. (2016) / Khedr et al. (2019)", efeito_resumo="Redução de 15,1% a 25,18% na UPDRS-III mantida por 30 dias",
            escalas_detalhadas=[scale_updrs_on], cadeia_sequencial=[step_p1, step_p2],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Aplicar obrigatoriamente no estado ON; pacientes rígido-acinéticos têm melhor prognóstico.",
            audit_meta=_audit("Moderada", "Metanálise de rTMS em sintomas motores da Doença de Parkinson (Li et al., 2022 / Zhang et al., 2022).", "Avaliação por alvos motores e estado dopaminérgico ON.", ["Risco de viés"], "Moderada", "Condicional", "Base consolidada por metanálise para M1 bilateral no estado ON.", tol_pd),
        ),
        "dp_ams": make_mod(
            protocolo_id="RM17-AMS", tecnica="AMS 10 Hz Bilateral (Anterior ao hotspot da mão -> Abdutor do Hálux)", modalidade_sigla="rTMS AMS",
            alvo="AMS: 3 cm anterior ao hotspot da mão -> 3 cm à frente do abdutor do hálux (ou 3 cm à frente de Cz)", frequencia="10 Hz", intensidade="90–100% LMR",
            pulsos_duracao="1.000 pulsos por área", sessoes="10 a 20 sessões no estado ON",
            escala_recomendada="MDS-UPDRS III (Estado ON) + NFOG-Q", meta_melhora="-1,90 pts UPDRS-III (Protocolo 3) / -14,98% UPDRS-III (Protocolo 5)",
            tamanho_efeito=0.52, evidencia="Nível B — Metanálise AMS Chen 2025", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Chen et al., 2025)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_YOKOE_2018, meta_analise=REF_CHEN_2025_PD,
            mcid_valor=3.5, mcid_label="-3,5 pts UPDRS-III (ON)", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Yokoe et al. (2018) / Mi et al. (2019)", efeito_resumo="Melhora motora global e axial na Área Motora Suplementar",
            escalas_detalhadas=[scale_updrs_on, scale_nfog], cadeia_sequencial=[step_p3, step_p5],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Recomenda-se bobina circular para Área Motora Suplementar e membros inferiores; usar 3 cm à frente de Cz se o hotspot do abdutor do hálux estiver ausente.",
            audit_meta=_audit("Moderada", "Metanálise dedicada à Área Motora Suplementar em Parkinson (Chen et al., 2025).", "Benefício consistente em sintomas axiais e bradicinesia.", ["Subgrupo AMS"], "Moderada", "Condicional", "Usar 3 cm à frente de Cz quando hotspot ausente.", tol_pd),
        ),
        "dp_dlpfc": make_mod(
            protocolo_id="RM17-P4", tecnica="Protocolo 4 (Exploratório) — Dual F3 10 Hz (3.000 p) + M1 Tibial Anterior Bilateral (2.000 p)", modalidade_sigla="rTMS Dual DLPFC+M1",
            alvo="F3 (DLPFC) + M1 hotspot tibial anterior bilateral (bobina duplo cone)", frequencia="10 Hz", intensidade="110% LMR (F3) + 100% LMR (M1)",
            pulsos_duracao="3.000 p (F3) + 2.000 p/área (M1) — faixa alta 2.000–7.000 pulsos", sessoes="20 sessões no estado ON",
            escala_recomendada="MDS-UPDRS III (Estado ON)", meta_melhora="-57,69% UPDRS-III pós-20 sessões (-41,45% após 4 sem)",
            tamanho_efeito=0.62, evidencia="Nível C — Base científica exploratória (Aftanas 2020)", linha_fluxograma="pontilhada",
            diretriz_internacional="Exploratório (Aftanas et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_AFTANAS_2020, meta_analise=REF_ZHANG_2022_PD,
            mcid_valor=3.5, mcid_label="-3,5 pts UPDRS-III (ON)", cohen_d_valor=0.62, cohen_d_interp="Moderado",
            estudo_referencia="Aftanas et al. (2020)", efeito_resumo="Redução de 57,69% na UPDRS-III após 20 sessões (bobina duplo cone)",
            escalas_detalhadas=[scale_updrs_on],
            cadeia_sequencial=[
                make_chain_step(1, "RM17-P4", "Protocolo 4 Dual (Exploratório)", "Protocolo 4 — F3 10 Hz + M1 Tibial Anterior Bilateral", "HF-rTMS Dual", "F3 + M1 tibial anterior bilateral (duplo cone)", "F3: 10 Hz 3.000 p (110% LMR) + M1: 10 Hz 2.000 p/área (100% LMR)", sessoes="20 sessões", efeito_esperado="-57,69% UPDRS-III pós-ciclo", referencia="Aftanas et al. (2020) · DOI: 10.17116/jnevro202012005129", linha_fluxograma="pontilhada"),
            ],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Protocolo exploratório tracejado de alta carga de pulsos (bobina duplo cone).",
            audit_meta=_audit("Moderada", "Metanálise geral DP (Zhang et al., 2022).", "Protocolo dual F3+M1 com duplo cone oriundo de ensaio individual.", ["Quadro exploratório"], "Baixa", "Condicional", "Alta carga de pulsos (5.000–7.000 p) no estado ON.", tol_pd),
        ),
        "fog": make_mod(
            protocolo_id="RM17-FOG", tecnica="AMS P5 -> M1 Contralateral P6 -> M1 + tsMS T10-T12 P7 (Exploratório)", modalidade_sigla="rTMS / tsMS FOG",
            alvo="AMS (3 cm à frente abdutor hálux/Cz) -> M1 mão contralateral ao lado mais afetado -> M1 tibial ant. + tsMS T10-T12", frequencia="10 Hz (P5/P6) / 1 Hz (P7)", intensidade="90% LMR (P5/P6) / 120% LMR + tsMS (P7)",
            pulsos_duracao="1.000 p/área (P5/P6) / 800 p M1 + 1.500 p tsMS T10-T12 (P7)", sessoes="10 a 20 sessões no estado ON",
            escala_recomendada="NFOG-Q + MDS-UPDRS III (Estado ON) + TUG", meta_melhora="P5: -9,24% FOGQ | P6: -21,32% FOGQ | P7: -23,02% FOGQ",
            tamanho_efeito=0.54, evidencia="Nível B — Metanálise Freezing Xie 2020 / Mi 2019", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Xie et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_MI_2019, meta_analise=REF_XIE_2020_PD,
            mcid_valor=3.0, mcid_label="-15% a -23% no NFOG-Q", cohen_d_valor=0.54, cohen_d_interp="Moderado",
            estudo_referencia="Mi et al. (2019) / Song et al. (2024)", efeito_resumo="Redução progressiva do freezing of gait e melhora do TUG",
            escalas_detalhadas=[scale_nfog, scale_updrs_on, scale_tug_pd],
            cadeia_sequencial=[
                step_p5,
                make_chain_step(2, "RM17-P6", "Protocolo 6 M1 Contralateral", "Protocolo 6 — M1 Contralateral ao Lado Mais Comprometido", "HF-rTMS (10 Hz)", "M1 hotspot mão contralateral ao lado mais comprometido", "10 Hz | 90% LMR | 1.000 p/área (50 p × 20 trens, 55 s IIT)", sessoes="10 a 20 sessões", efeito_esperado="-15,59% a -21,32% FOGQ e -12,41% TUG", referencia="Song et al. (2024) · DOI: 10.3389/fnagi.2024.1354455", observacoes="Regra de Aplicação: iniciar obrigatoriamente pelo hemisfério contralateral ao lado mais comprometido do paciente."),
                make_chain_step(3, "RM17-P7", "Protocolo 7 M1 + tsMS T10-T12 (Exploratório)", "Protocolo 7 — M1 Tibial Anterior + tsMS T10-T12", "LF-rTMS + tsMS (1 Hz — Exploratório)", "M1 tibial ant. bilateral + tsMS nível T10-T12 (duplo cone)", "1 Hz | 120% LMR 800 p M1 + 1 Hz 1.500 p tsMS p/ contração MMII", sessoes="10 sessões", efeito_esperado="-23,02% FOGQ pós-sessões", referencia="Wang et al. (2024) · DOI: 10.1038/s41531-024-00792-1", linha_fluxograma="pontilhada"),
            ],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Priorizar se o paciente apresentar freezing of gait ou discinesia induzida por levodopa; no Protocolo 6 iniciar pelo hemisfério contralateral ao dimídio mais comprometido.",
            audit_meta=_audit("Moderada", "Metanálise rTMS em Freezing of Gait (Xie et al., 2020).", "Alinhada com Mi 2019 (AMS) e Song 2024 (M1 contralateral).", ["Risco de viés"], "Moderada", "Condicional", "P6 inicia pelo lado contralateral ao dimídio mais comprometido.", tol_pd),
        ),
        "mobilidade": make_mod(
            protocolo_id="RM17-MOB", tecnica="M1 MMII+Mão P8 -> AMS P5 -> tsMS T3 P9 -> Dual M1+tsMS C7 P10 (Ajuste de Segurança)", modalidade_sigla="rTMS / tsMS Marcha",
            alvo="M1 MI+Mão (P8) -> AMS (P5) -> tsMS T3 (P9) -> Dual M1 + tsMS C7 (P10)", frequencia="10 Hz / iTBS T3 / 20 Hz + 10 Hz", intensidade="80–100% LMR + 50% saída em C7",
            pulsos_duracao="1.000 p (P8/P5) -> 1.200 p iTBS (T3) -> 2.000 p + 1.500 p tsMS C7", sessoes="10 a 20 sessões no estado ON",
            escala_recomendada="TUG / TUG dupla tarefa + TC6min + MDS-UPDRS III (Estado ON)", meta_melhora="P8: -12,54% marcha | P9: -19,26% TUG | P10: -32 s TUG",
            tamanho_efeito=0.55, evidencia="Nível B — Zhang 2022 / Xie 2020 (tsMS T3/C7 exploratórios)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Zhang et al., 2022)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_KHEDR_2006, meta_analise=REF_ZHANG_2022_PD,
            mcid_valor=2.5, mcid_label="-12,5% a -19,3% no TUG", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Khedr et al. (2006) / Menezes et al. (2024)", efeito_resumo="-12,54% marcha (P8), -19,26% TUG (P9) e -32 s TUG (Dual M1+tsMS C7)",
            escalas_detalhadas=[scale_tug_pd, scale_updrs_on],
            cadeia_sequencial=[
                make_chain_step(1, "RM17-P8", "Protocolo 8 M1 MI+Mão", "Protocolo 8 — M1 Hotspot MI + Mão Bilateral", "HF-rTMS (10 Hz)", "M1 membro inferior + mão bilateral (bobina circular/8)", "10 Hz | 100% LMR | 1.000 p/área (50 p × 20 trens, 50 s IIT)", sessoes="6 a 15 sessões", efeito_esperado="-12,54% velocidade da caminhada", referencia="Khedr et al. (2006) · DOI: 10.1002/mds.21089"),
                step_p5,
                make_chain_step(3, "RM17-P9", "Protocolo 9 tsMS T3 (Exploratório)", "Protocolo 9 — tsMS iTBS Nível T3", "tsMS iTBS (Exploratório)", "Coluna torácica nível T3", "iTBS 5 Hz / 50 Hz | 1.200 pulsos (20 triplets × 20 trens, 8 s IIT) | 100% LMR", sessoes="5 a 10 sessões", efeito_esperado="-19,26% no TUG após 5 sessões", referencia="Menezes et al. (2024) · DOI: 10.1002/mds.29776", linha_fluxograma="pontilhada"),
                make_chain_step(4, "RM17-P10", "Protocolo 10 M1 + tsMS C7 (Ajuste de Segurança)", "Protocolo 10 — Dual M1 + tsMS Nível C7", "rTMS + tsMS (Ajuste de Segurança)", "M1 1º interósseo dorsal bilat + tsMS C7", "M1 20 Hz 2.000 p/área 80% LMR + tsMS C7 10 Hz 1.500 p a 50% saída", sessoes="10 sessões", efeito_esperado="-32 s no TUG logo após 10 sessões (-35 s em 1 mês)", referencia="Khedr et al. (2025) · DOI: 10.1177/15459683241300547", linha_fluxograma="pontilhada", observacoes="Ajuste de Segurança: parâmetros reduzidos a 50% da saída máxima do estimulador no nível C7 para proteção do paciente."),
            ],
            ajuste_parametros=adj_pd, falha_terapeutica=falha_pd, sessoes_ajuste=sa_pd,
            notas_clinicas="Ajuste de Segurança: no Protocolo 10 (Dual M1 + tsMS nível C7), aplicar intensidade de 50% da saída máxima do estimulador em C7.",
            audit_meta=_audit("Moderada", "Metanálise DP (Zhang et al., 2022) + ensaios recentes tsMS.", "Cadeia escalonada até tsMS T3 e C7 (com ajuste de segurança).", ["Risco de viés"], "Moderada", "Condicional", "P8 sólido; tsMS T3/C7 são exploratórios.", tol_pd),
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
                    {"id": "dp_m1", "rotulo": "Área Motora Primária (M1)", "criterio": "Base consolidada por metanálises", "descricao": "Protocolo 1 (10 Hz) -> Protocolo 2 (20 Hz).", "protocolo_alvo": "funcao_global"},
                    {"id": "dp_ams", "rotulo": "Área Motora Suplementar (AMS)", "criterio": "3 cm anterior ao hotspot mão / 3 cm Cz", "descricao": "Protocolo 3 -> Protocolo 5 (Abdutor Hálux / Cz).", "protocolo_alvo": "dp_ams"},
                    {"id": "dp_dlpfc", "rotulo": "Córtex Pré-Frontal Dorsolateral (DLPFC)", "criterio": "Base científica exploratória", "descricao": "Protocolo 4 (F3 10 Hz + M1 tibial anterior duplo cone).", "protocolo_alvo": "dp_dlpfc"},
                ],
            },
            "subtipo_mobilidade": {
                "pergunta": "Qual é a limitação predominante na Mobilidade?",
                "subtitulo": "Bifurcação entre Freezing of Gait e Mobilidade Funcional/Marcha.",
                "opcoes": [
                    {"id": "fog", "rotulo": "Freezing of Gait", "criterio": "NFOG-Q (AMS / M1 contralateral / tsMS)", "descricao": "AMS (P5) -> M1 contralateral ao lado afetado (P6) -> M1 + tsMS T10-T12 (P7).", "protocolo_alvo": "fog"},
                    {"id": "mobilidade", "rotulo": "Mobilidade Funcional e Desempenho de Marcha", "criterio": "TUG / TUG dupla tarefa / TC6min", "descricao": "M1 MI+Mão (P8) -> AMS (P5) -> tsMS T3 (P9) -> Dual M1 + tsMS C7 (P10).", "protocolo_alvo": "mobilidade"},
                ],
            },
        },
        "ajuste_parametros": adj_pd,
        "protocolo_alternativo": {
            "nome": "Protocolo 9 (Exploratório) — tsMS iTBS T3 (Menezes et al., 2024)",
            "tecnica": "tsMS iTBS", "alvo": "Coluna torácica nível T3", "parametros": "iTBS 5 Hz/50 Hz | 1.200 pulsos | 100% LMR",
            "observacoes": "-19,26% no TUG após 5 sessões.",
        },
        "protocolo_alternativo_2": {
            "nome": "Protocolo 10 (Exploratório) — Dual M1 + tsMS C7 (Khedr et al., 2025)",
            "tecnica": "rTMS + tsMS", "alvo": "M1 1º interósseo dorsal + C7",
            "parametros": "M1 20 Hz 80% LMR + tsMS C7 10 Hz 50% saída estimulador",
            "observacoes": "Ajuste de Segurança: intensidade reduzida a 50% da saída máxima em C7 (-32 s no TUG).",
        },
        "falha_terapeutica": {
            "id": "RM17-FALHA", "titulo": "Falha Terapêutica em Doença de Parkinson",
            "criterios_definicao": "Sem alteração no pré-teste semanal ou piora dos sintomas motores (bradicinesia, tremores mais evidentes, aumento de freezing) após cadeia completa.",
            "descricao": "Conferir estado ON dopaminérgico, medicações e escalonamento prévio.",
            "condutas": ["Conferir realização integral no estado ON.", "Revisar interações medicamentosas (benzodiazepínicos).", "Priorizar protocolo específico para discinesia/freezing quando presentes."],
        },
    }

    obs_pd = [
        make_obs("RM17-PRE-CONTRA", "Checar contraindicações absolutas (implantes metálicos na área de estimulação e epilepsia não controlada). Pacientes com fenótipo rígido-acinético têm melhor prognóstico; se houver discinesia induzida por levodopa ou freezing, priorizar protocolos voltados a esses sintomas.", "pre", categoria="clinica", severidade="warning"),
        make_obs("RM17-ON-STATE-TEC", "Recomenda-se aplicar TODOS os protocolos sugeridos no estado 'ON' da medicação dopaminérgica (Zhang et al., 2022). Atenção a benzodiazepínicos (reduzem efeito).", "tec", categoria="clinica"),
        make_obs("RM17-EXPLORATORIO-TEC", "Base científica exploratória (ensaios clínicos): Protocolos 4, 7, 9 e 10 ainda não consolidados por metanálise.", "tec", categoria="evidencia", protocolo_ids=["dp_dlpfc", "fog", "mobilidade"], estagios=["primary", "alt1", "alt2"]),
        make_obs("RM17-CONTRALAT-STAR", "Regra de Aplicação: iniciar o Protocolo 6 pelo hemisfério CONTRALATERAL ao lado mais comprometido do paciente.", "alvo", categoria="anatomia", protocolo_ids=["fog"]),
        make_obs("RM17-CZ-HASH", "Regra de Aplicação: caso não seja possível localizar o hotspot do abdutor do hálux na AMS, considerar 3 cm à frente de Cz. Utilizar bobina circular para áreas motoras do MMII e AMS.", "alvo", categoria="anatomia", protocolo_ids=["dp_ams", "fog", "mobilidade"]),
        make_obs("RM17-AMP-SEGURANCA", "Ajuste de Segurança: no Protocolo 10 (M1 + tsMS nível C7), aplicar a 50% da saída máxima do estimulador no nível C7. Otimização de Dose: quanto maior a carga de pulsos (2.000–7.000 pulsos no estado ON), maiores e mais duradouros os efeitos.", "intensidade", categoria="seguranca", protocolo_ids=["mobilidade", "dp_dlpfc"], estagios=["primary", "alt2"], severidade="warning"),
        make_obs("RM17-SESSOES-10-20", "Tem sido observada maior quantidade de sessões do que as 10 habituais — aumentar para 10 a 20 sessões associadas à função motora/marcha desejada.", "sessoes", categoria="parametros"),
        make_obs("RM17-ON-SCALE", "Avaliar a MDS-UPDRS Seção III sempre no estado 'ON' da medicação, em conjunto com NFOG-Q (versão atualizada) e TUG / TC6min.", "scale", categoria="avaliacao"),
        make_obs("RM17-REEVAL-SEMANAL", "Reavaliar a cada 1 semana -> melhora crescente: manter protocolo; platô: indicar manutenção. Insuficiente: ausência de mudança no pré-teste em 1 semana OU piora motora (bradicinesia, tremores mais evidentes, mais episódios de freezing) -> seguir para próximo protocolo.", "reeval", categoria="reavaliacao", severidade="warning"),
        make_obs("RM17-CEFALEIA-TOL", "Cefaleia é o efeito adverso mais frequente durante/após a estimulação. Registrar ocorrências no Banco de Efeitos Adversos NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN"),
    ]

    return {
        "id": cid, "condicao": "Doença de Parkinson — Sintomas Motores e Marcha", "eixo": "Distúrbios do Movimento",
        "roadmap_id": "RM17", "svg_file": "RM17.svg",
        "fatores_limitantes": [
            {"id": "funcao_global", "nome": "Função Motora", "instrumento_sugerido": "MDS-UPDRS Seção III (Estado ON)", "descricao": "Bradicinesia, rigidez e função motora global em M1, AMS ou DLPFC."},
            {"id": "fog", "nome": "Freezing of Gait", "instrumento_sugerido": "NFOG-Q (versão atualizada)", "descricao": "Congelamento da marcha com protocolos em AMS, M1 contralateral e tsMS T10-T12."},
            {"id": "mobilidade", "nome": "Mobilidade Funcional e Desempenho de Marcha", "instrumento_sugerido": "Timed Up and Go / TC6min", "descricao": "Velocidade e estabilidade de marcha (M1, AMS e tsMS T3/C7)."},
        ],
        "arvore_algoritmo": arvore, "observacoes_contextuais": obs_pd, "modalidades": modalidades, "tags_busca": tags,
    }


def build_dor_movimento_conditions():
    """Returns Dor Neuropatica (RM05), Ataxia Cerebelar (RM16), and Doenca de Parkinson (RM17)."""
    return [_build_dor_neuropatica(), _build_ataxia(), _build_parkinson()]
