"""Official clinical decision trees, protocols, and contextual observations for AVC roadmaps (RM01-RM04, RM06-RM09)."""

from scripts.roadmaps_data import (
    ADVERSE_BANK_URL,
    DIR_IFCN_RTMS_2020,
    DIR_IFCN_TDCS_2017,
    DIR_ROSSI_2009,
    PEM_GUIDE_DOI,
    PEM_GUIDE_LABEL,
    make_chain_step,
    make_mod,
    make_obs,
    make_ref,
    make_scale,
)

# Verified primary trials and meta-analyses strictly matching PDF citations (RM01-RM04, RM06-RM09)
REF_ANTONINO_2025 = make_ref(
    "Antonino, G. B., et al.",
    2025,
    "The impact of the number of sessions and stimulation parameters on repetitive transcranial magnetic stimulation efficacy for post-stroke upper extremity recovery: A systematic review and meta-analysis",
    "Clinical Rehabilitation",
    "10.1177/02692155251328945",
    tipo="Metanálise de referência",
)
REF_FAN_2022 = make_ref(
    "Fan, J., et al.",
    2022,
    "The effectiveness and safety of repetitive transcranial magnetic stimulation on spasticity after upper motor neuron injury: A systematic review and meta-analysis",
    "Frontiers in Neural Circuits",
    "10.3389/fncir.2022.973561",
    tipo="Metanálise de referência",
)
REF_CHEN_2023 = make_ref(
    "Chen, G., et al.",
    2023,
    "Non-invasive brain stimulation effectively improves post-stroke sensory impairment: a systematic review and meta-analysis",
    "Journal of Neural Transmission",
    "10.1007/s00702-023-02674-x",
    tipo="Metanálise de referência",
)
REF_FAN_2017 = make_ref(
    "Fan, J., et al.",
    2017,
    "Efficacy of Noninvasive Brain Stimulation on Unilateral Neglect After Stroke: A Systematic Review and Meta-analysis",
    "American Journal of Physical Medicine & Rehabilitation",
    "10.1097/PHM.0000000000000834",
    tipo="Metanálise de referência",
)
REF_ZHU_2025 = make_ref(
    "Zhu, Y., et al.",
    2025,
    "Effects of Cerebellar Transcranial Magnetic Stimulation on the Motor Function of Patients With Stroke: A Systematic Review and Meta-Analysis",
    "Brain and Behavior",
    "10.1002/brb3.70471",
    tipo="Metanálise de referência",
)
REF_JIA_2025 = make_ref(
    "Jia, S., et al.",
    2025,
    "Therapeutic efficacy of repetitive transcranial magnetic stimulation on gait and limb balance function in patients with lower limb dysfunction post-cerebral infarction: a systematic review and meta-analysis",
    "BMC Neurology",
    "10.1186/s12883-025-04112-9",
    tipo="Metanálise de referência",
)
REF_ZENG_2024 = make_ref(
    "Zeng, Y., et al.",
    2024,
    "Efficacy of Cerebellar Transcranial Magnetic Stimulation for Post-stroke Balance and Limb Motor Function Impairments: Meta-analyses of Random Controlled Trials and Resting-State fMRI Studies",
    "The Cerebellum",
    "10.1007/s12311-024-01660-7",
    tipo="Metanálise de referência",
)
REF_SU_2025 = make_ref(
    "Su, X., et al.",
    2025,
    "The Effect of Intermittent Theta Burst Stimulation for Post-Stroke Lower Limb Motor Recovery: A Systematic Review and Meta-Analysis",
    "NeuroRehabilitation",
    "10.1177/10538135241304991",
    tipo="Metanálise de referência",
)
REF_LIU_2024 = make_ref(
    "Liu, Y., et al.",
    2024,
    "Effects of Cerebellar Repetitive Transcranial Magnetic Stimulation in the Treatment of Post-Stroke Dysphagia: A Meta-Analysis and Systematic Review of Randomized Controlled Trials",
    "European Neurology",
    "10.1159/000538130",
    tipo="Metanálise de referência",
)
REF_HAN_2024_DYSP = make_ref(
    "Han, D., et al.",
    2024,
    "Evidence for Intermittent Theta Burst Transcranial Magnetic Stimulation for Dysphagia after Stroke: A Systematic Review and Meta-analysis",
    "Dysphagia",
    "10.1007/s00455-024-10729-8",
    tipo="Metanálise de referência",
)
REF_WEN_2022 = make_ref(
    "Wen, X., et al.",
    2022,
    "The Effectiveness of Repetitive Transcranial Magnetic Stimulation for Post-stroke Dysphagia: A Systematic Review and Meta-Analysis",
    "Frontiers in Human Neuroscience",
    "10.3389/fnhum.2022.841781",
    tipo="Metanálise de referência",
)
REF_DING_2022 = make_ref(
    "Ding, X., et al.",
    2022,
    "Comparative efficacy of non-invasive brain stimulation for post-stroke aphasia: A network meta-analysis and meta-regression of moderators",
    "Neuroscience & Biobehavioral Reviews",
    "10.1016/j.neubiorev.2022.104804",
    tipo="Metanálise de referência",
)
REF_HAN_2024_AF = make_ref(
    "Han, C., et al.",
    2024,
    "The effectiveness and safety of noninvasive brain stimulation technology combined with speech training on aphasia after stroke: A systematic review and meta-analysis",
    "Medicine",
    "10.1097/MD.0000000000036880",
    tipo="Metanálise de referência",
)
REF_BIOU_2019 = make_ref(
    "Biou, E., et al.",
    2019,
    "Transcranial direct current stimulation in post-stroke aphasia rehabilitation: A systematic review",
    "Annals of Physical and Rehabilitation Medicine",
    "10.1016/j.rehab.2019.01.003",
    tipo="Metanálise de referência",
)

# Verified RCTs directly extracted from official PDFs
REF_GUO_2016 = make_ref(
    "Guo, Z., et al.", 2016,
    "Ipsilesional High Frequency Repetitive Transcranial Magnetic Stimulation Add-On Therapy Improved Diffusion Parameters of Stroke Patients with Motor Dysfunction: A Preliminary DTI Study",
    "Neural Plasticity", "10.1155/2016/6238575", tipo="Ensaio clínico de referência",
)
REF_LONG_2018 = make_ref(
    "Long, H., et al.", 2018,
    "Effects of combining high- and low-frequency repetitive transcranial magnetic stimulation on upper limb hemiparesis in the early phase of stroke",
    "Restorative Neurology and Neuroscience", "10.3233/RNN-170733", tipo="Ensaio clínico de referência",
)
REF_ZHENG_2015 = make_ref(
    "Zheng, C., et al.", 2015,
    "Effect of combined low-frequency repetitive transcranial magnetic stimulation and virtual reality training on upper limb function in subacute stroke: A double-blind randomized controlled trial",
    "Journal of Huazhong University of Science and Technology [Medical Sciences]", "10.1007/s11596-015-1419-0", tipo="Ensaio clínico de referência",
)
REF_WANG_2022 = make_ref(
    "Wang, L., et al.", 2022,
    "Effects of corticospinal tract integrity on upper limb motor function recovery in stroke patients treated with repetitive transcranial magnetic stimulation",
    "Journal of Integrative Neuroscience", "10.31083/j.jin2102050", tipo="Ensaio clínico de referência",
)
REF_ZANONA_2022 = make_ref(
    "de Freitas Zanona, A., et al.", 2022,
    "Somatosensory Cortex Repetitive Transcranial Magnetic Stimulation and Associative Sensory Stimulation of Peripheral Nerves Could Assist Motor and Sensory Recovery After Stroke",
    "Frontiers in Human Neuroscience", "10.3389/fnhum.2022.860965", tipo="Ensaio clínico de referência",
)
REF_KIM_2013 = make_ref(
    "Kim, B. R., et al.", 2013,
    "Effect of high- and low-frequency repetitive transcranial magnetic stimulation on visuospatial neglect in patients with acute stroke: a double-blind, sham-controlled trial",
    "Archives of Physical Medicine and Rehabilitation", "10.1016/j.apmr.2012.12.016", tipo="Ensaio clínico de referência",
)
REF_CHEN_2021 = make_ref(
    "Chen, Y., et al.", 2021,
    "Cerebellar intermittent theta-burst stimulation reduces upper limb spasticity after subacute stroke: a randomized controlled trial",
    "Frontiers in Neural Circuits", "10.3389/fncir.2021.655502", tipo="Ensaio clínico de referência",
)
REF_KASHOO_2022 = make_ref(
    "Kashoo, F., et al.", 2022,
    "Effect of Transcranial Direct Current Stimulation Augmented with Motor Imagery and Upper-Limb Functional Training for Upper-Limb Stroke Rehabilitation: A Prospective Randomized Controlled Trial",
    "International Journal of Environmental Research and Public Health", "10.3390/ijerph192215199", tipo="Ensaio clínico de referência",
)
REF_KOH_2017 = make_ref(
    "Koh, C. L., et al.", 2017,
    "Effects of Transcranial Direct Current Stimulation With Sensory Modulation on Stroke Motor Rehabilitation: A Randomized Controlled Trial",
    "Archives of Physical Medicine and Rehabilitation", "10.1016/j.apmr.2017.05.025", tipo="Ensaio clínico de referência",
)
REF_KLOMJAI_2022 = make_ref(
    "Klomjai, W., et al.", 2022,
    "Anodal tDCS of contralesional hemisphere modulates ipsilateral control of spinal motor networks targeting the paretic arm post-stroke",
    "Clinical Neurophysiology", "10.1016/j.clinph.2021.12.016", tipo="Ensaio clínico de referência",
)
REF_CUNNINGHAM_2015 = make_ref(
    "Cunningham, D. A., et al.", 2015,
    "Stimulation targeting higher motor areas in stroke rehabilitation: A proof-of-concept, randomized, double-blinded placebo-controlled study of effectiveness and underlying mechanisms",
    "Restorative Neurology and Neuroscience", "10.3233/RNN-150574", tipo="Ensaio clínico de referência",
)
REF_KOO_2018 = make_ref(
    "Koo, W. R., et al.", 2018,
    "Effects of Anodal Transcranial Direct Current Stimulation on Somatosensory Recovery After Stroke: A Randomized Controlled Trial",
    "American Journal of Physical Medicine & Rehabilitation", "10.1097/PHM.0000000000000910", tipo="Ensaio clínico de referência",
)
REF_BANG_2015 = make_ref(
    "Bang, D. H., & Bong, S. Y.", 2015,
    "Effect of combination of transcranial direct current stimulation and feedback training on visuospatial neglect in patients with subacute stroke: a pilot randomized controlled trial",
    "Journal of Physical Therapy Science", "10.1589/jpts.27.2759", tipo="Ensaio clínico de referência",
)
REF_KOCH_2019 = make_ref(
    "Koch, G., et al.", 2019,
    "Effect of Cerebellar Stimulation on Gait and Balance Recovery in Patients With Hemiparetic Stroke: A Randomized Clinical Trial",
    "JAMA Neurology", "10.1001/jamaneurol.2018.3639", tipo="Ensaio clínico de referência",
)
REF_WANG_2024_MOB = make_ref(
    "Wang, R., et al.", 2024,
    "Repetitive Transcranial Magnetic Stimulation Coupled With Visual-Feedback Cycling Exercise Improves Walking Ability and Walking Stability After Stroke: A Randomized Pilot Study",
    "Neural Plasticity", "10.1155/np/8737366", tipo="Ensaio clínico de referência",
)
REF_ZHANG_2024_MOB = make_ref(
    "Zhang, Y., et al.", 2024,
    "Effectiveness of repetitive transcranial magnetic stimulation combined with intelligent Gait-Adaptability Training in improving lower limb function and brain symmetry after subacute stroke: a preliminary study",
    "Journal of Stroke and Cerebrovascular Diseases", "10.1016/j.jstrokecerebrovasdis.2024.107961", tipo="Ensaio clínico de referência",
)
REF_DANZL_2013 = make_ref(
    "Danzl, M. M., et al.", 2013,
    "Brain stimulation paired with novel locomotor training with robotic gait orthosis in chronic stroke: a feasibility study",
    "NeuroRehabilitation", "10.3233/NRE-130929", tipo="Ensaio clínico de referência",
)
REF_TAI_2023 = make_ref(
    "Tai, J., et al.", 2023,
    "Theta-burst transcranial magnetic stimulation for dysphagia patients during recovery stage of stroke: a randomized controlled trial",
    "European Journal of Physical and Rehabilitation Medicine", "10.23736/S1973-9087.23.08023-1", tipo="Ensaio clínico de referência",
)
REF_ZHONG_2021 = make_ref(
    "Zhong, L., et al.", 2021,
    "Repetitive transcranial magnetic stimulation at different sites for dysphagia after stroke: a randomized, observer-blind clinical trial",
    "Frontiers in Neurology", "10.3389/fneur.2021.625683", tipo="Ensaio clínico de referência",
)
REF_DONG_2022 = make_ref(
    "Dong, L., et al.", 2022,
    "High-Frequency Cerebellar rTMS Improves the Swallowing Function of Patients with Dysphagia after Brainstem Stroke",
    "Neural Plasticity", "10.1155/2022/6259693", tipo="Ensaio clínico de referência",
)
REF_WANG_2023_DYSP = make_ref(
    "Wang, Z., et al.", 2023,
    "Efficacy of Transcranial Direct Current Stimulation Combined with Conventional Swallowing Rehabilitation Training on Post-stroke Dysphagia",
    "Dysphagia", "10.1007/s00455-023-10581-2", tipo="Ensaio clínico de referência",
)
REF_SAWAN_2020 = make_ref(
    "Sawan, S. A. E., et al.", 2020,
    "Transcranial direct current stimulation (tDCS): its effect on improving dysphagia in stroke patients",
    "The Egyptian Journal of Neurology, Psychiatry and Neurosurgery", "10.1186/s41983-020-00246-4", tipo="Ensaio clínico de referência",
)
REF_REN_2019 = make_ref(
    "Ren, C., et al.", 2019,
    "The Effect of rTMS over the Different Targets on Language Recovery in Stroke Patients with Global Aphasia: A Randomized Sham-Controlled Study",
    "BioMed Research International", "10.1155/2019/4589056", tipo="Ensaio clínico de referência",
)
REF_ZHAO_2021 = make_ref(
    "Zhao, Q., et al.", 2021,
    "Effect of Anodic Transcranial Direct Current Stimulation Combined With Speech Language Therapy on Nonfluent Poststroke Aphasia",
    "Neuromodulation: Technology at the Neural Interface", "10.1111/ner.13337", tipo="Ensaio clínico de referência",
)
REF_FIORI_2013 = make_ref(
    "Fiori, V., et al.", 2013,
    "tDCS stimulation segregates words in the brain: evidence from aphasia",
    "Frontiers in Human Neuroscience", "10.3389/fnhum.2013.00269", tipo="Ensaio clínico de referência",
)
REF_MEINZER_2016 = make_ref(
    "Meinzer, M., et al.", 2016,
    "Electrical stimulation of the motor cortex enhances treatment outcome in post-stroke aphasia",
    "Brain", "10.1093/brain/aww002", tipo="Ensaio clínico de referência",
)


def _tol_profile(orientacao, ajuste, fatores):
    return {
        "orientacao_tolerabilidade": orientacao,
        "ajuste_seguranca": ajuste,
        "fatores_moduladores": fatores,
    }


def _audit(amstar_nivel, amstar_resumo, amstar_just, amstar_sinais, grade_certeza, grade_forca, grade_dom, tol):
    return {
        "amstar2_nivel": amstar_nivel,
        "amstar2_resumo": amstar_resumo,
        "amstar2_justificativa": amstar_just,
        "amstar2_sinais": amstar_sinais,
        "grade_certeza": grade_certeza,
        "grade_forca": grade_forca,
        "grade_dominios": grade_dom,
        "tolerabilidade": tol,
    }


def _sessoes_aj(quando, ajuste, regra):
    return {"quando_reavaliar": quando, "ajuste_dose": ajuste, "regra_interrupcao": regra}


def _falha_mod(criterio, conduta):
    return {"criterio": criterio, "conduta_oficial": conduta}


def _avc_shared_observations(prefix, device_noun, therapy_domain, mod_tipo, session_rule_txt, reeval_txt, dotted_protocols):
    """Generates exact PDF-aligned contextual observations without repeating rules shown in Tolerance/Monitoring panels."""
    obs = [
        make_obs(
            f"{prefix}-DOR-PRE",
            f"Se a dor (neuropática ou nociceptiva) for o fator limitante principal em {therapy_domain}, seguir o protocolo clínico de Dor Neuropática Crônica, evitando apenas posicionar {device_noun} sobre a área cortical lesada.",
            "pre", categoria="redirecionamento", modalidades_tipo=[mod_tipo],
            acao_condicao_id="dor-neuropatica", acao_rotulo="Abrir Protocolo de Dor Neuropática Crônica", severidade="warning",
        ),
        make_obs(
            f"{prefix}-MULTIPROTOCOLO-TEC",
            "Evite aplicar múltiplos protocolos simultaneamente, exceto quando sua combinação já tiver sido previamente validada por estudos científicos.",
            "tec", categoria="clinica", modalidades_tipo=[mod_tipo], estagios=["primary"],
        ),
        make_obs(
            f"{prefix}-BANCO-EA",
            "Registrar eventos adversos e parâmetros de segurança no Banco de Efeitos Adversos da Rede NAPeN.",
            "tol", categoria="seguranca", modalidades_tipo=[mod_tipo],
            referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN",
        ),
    ]
    if dotted_protocols:
        obs.append(
            make_obs(
                f"{prefix}-PONTILHADO-TEC",
                "Protocolo com linha pontilhada no fluxograma: proveniente de estudo clínico individual ainda não consolidado por metanálises.",
                "tec", categoria="evidencia", modalidades_tipo=[mod_tipo],
                protocolo_ids=dotted_protocols, estagios=["primary", "alt1", "alt2"],
            )
        )
    return obs


def _build_avc_ms():
    cid = "avc-membro-superior"
    tags = {
        "siglas": ["AVC", "AVE", "MS", "MMSS", "M1", "S1", "PPC", "PEM", "LMR", "LMA", "SCT", "BIT"],
        "coordenadas_10_20": ["C3", "C4", "M1", "P3", "P4", "F5", "CP3", "CP4"],
        "alvos_anatomicos": [
            "Córtex Motor Primário", "M1", "Área Motora da Mão",
            "Representação Corticomotora do Membro Superior",
            "Córtex Somatossensorial Primário (S1)", "Córtex Parietal Posterior (PPC)", "Cerebelo",
        ],
        "sinonimos_en": [
            "stroke", "spasticity", "upper extremity", "upper limb",
            "hand motor function", "hemiparesis", "arm recovery", "motor impairment", "unilateral spatial neglect", "star cancellation test",
        ],
        "sintomas_pt": [
            "paralisia", "hemiparesia", "membro superior", "braço", "mão", "preensão",
            "destreza", "espasticidade", "tônus", "perda de sinergia",
            "disfunção motora", "disfunção sensorial", "heminegligência",
        ],
        "escalas": ["FMA-UE", "Fugl-Meyer", "EAM", "Ashworth", "MRC", "MAL-Brazil", "Cancelamento de Estrelas", "Star Cancellation", "BIT"],
        "tecnicas": ["rTMS", "HF-rTMS", "LF-rTMS", "iTBS", "cTBS", "rPMS", "tDCS", "taVNS"],
    }

    tol_rtms = _tol_profile(
        "Em caso de desconforto com a bobina, reduzir inicialmente a intensidade e progredir gradualmente conforme a tolerância do paciente até o valor previsto no protocolo.",
        "Na ausência de identificação do Limiar Motor de Repouso (LMR), calibrar pelo Limiar Motor Ativo (LMA); na ausência de PEM no hemisfério lesionado, testar o hemisfério contralesional para confirmar inervação e excluir limitação técnica.",
        "Qualidade do sono, medicações em uso (não interromper terapias medicamentosas), integridade do trato corticoespinhal e fase pós-AVC (efeito mais pronunciado de 1 a 6 meses).",
    )
    tol_tdcs = _tol_profile(
        "Monitorar formigamento, eritema cutâneo e cefaleia sob os eletrodos (25–35 cm²); hidratar uniformemente as esponjas com solução salina e inspecionar a pele a cada sessão.",
        "Quando bem tolerado em protocolos tDCS compatíveis, titular progressivamente para 2 mA e 30 minutos conforme conforto cutâneo e tolerabilidade.",
        "Estado medicamentoso estável (não suspender medicações), fase subaguda (1–6 meses) e grau de comprometimento motor (quadros leves respondem melhor).",
    )

    step_p1 = make_chain_step(
        1, "RM01-P1", "Protocolo Inicial — HF-rTMS M1 Ipsilesional", "HF-rTMS (10 Hz) — M1 Ipsilesional (Guo et al., 2016)",
        "rTMS Excitatória (10 Hz) — M1 Ipsilesional", "Córtex Motor Primário (M1) — hemisfério ipsilesional (hotspot via PEM)",
        "10 Hz | 90% LMR | 1.500 pulsos (30 trens de 50 pulsos, 25 s de intervalo)",
        sessoes="10 sessões diárias associadas à fisioterapia e terapia ocupacional",
        efeito_esperado="+23,3 pts na FMA-UE (IC 95%: -3,5 a 50,0) e ganho nas AVDs (MAL-Brazil)",
        referencia="Guo et al. (2016) · DOI: 10.1155/2016/6238575",
        fase_etapa="inicial",
    )
    step_p2 = make_chain_step(
        2, "RM01-P2", "Próximo Protocolo — rTMS Bilateral Sequencial", "rTMS Bilateral (1 Hz Contralesional + 10 Hz Ipsilesional — Long et al., 2018)",
        "rTMS Bilateral (1 Hz contralesional seguido de 10 Hz ipsilesional)", "M1 contralesional (1 Hz) seguido de M1 ipsilesional (10 Hz)",
        "1 Hz, 90% LMR, 1.000 pulsos no hemisfério contralesional seguido de 10 Hz, 90% LMR, 1.000 pulsos (10 s trens, 50 s de intervalo) no hemisfério ipsilesional",
        sessoes="15 sessões diárias associadas à fisioterapia e terapia ocupacional",
        efeito_esperado="+6,6 pts na FMA-UE (IC 95%: 4,1 a 9,1) após 15 sessões diárias",
        referencia="Long et al. (2018) · DOI: 10.3233/RNN-170733",
        fase_etapa="sequencia",
    )
    step_p2_inicial = make_chain_step(
        1, "RM01-P2", "Protocolo Inicial — rTMS Bilateral Sequencial", "rTMS Bilateral (1 Hz Contralesional + 10 Hz Ipsilesional — Long et al., 2018)",
        "rTMS Bilateral (1 Hz contralesional seguido de 10 Hz ipsilesional)", "M1 contralesional (1 Hz) seguido de M1 ipsilesional (10 Hz)",
        "1 Hz, 90% LMR, 1.000 pulsos no hemisfério contralesional seguido de 10 Hz, 90% LMR, 1.000 pulsos (10 s trens, 50 s de intervalo) no hemisfério ipsilesional",
        sessoes="15 sessões diárias associadas à fisioterapia e terapia ocupacional",
        efeito_esperado="+6,6 pts na FMA-UE (IC 95%: 4,1 a 9,1) após 15 sessões diárias",
        referencia="Long et al. (2018) · DOI: 10.3233/RNN-170733",
        fase_etapa="inicial",
    )
    step_p3_seq = make_chain_step(
        2, "RM01-P3", "Próximo Protocolo — LF-rTMS M1 Contralesional", "LF-rTMS (1 Hz) — M1 Contralesional (Zheng et al., 2015)",
        "rTMS Inibitória (1 Hz) — M1 Contralesional", "Córtex Motor Primário (M1) — hemisfério contralesional",
        "1 Hz | 90% LMR | 1.800 pulsos | 30 min contínuos",
        sessoes="24 sessões associadas à reabilitação motora", efeito_esperado="+13,2 pts na FMA-UE (IC 95%: 3,6 a 22,7)",
        referencia="Zheng et al. (2015) · DOI: 10.1007/s11596-015-1419-0", linha_fluxograma="solida",
        fase_etapa="sequencia",
        observacoes="Indicado após resposta insatisfatória ao protocolo bilateral em comprometimento moderado a grave (FMA-UE ≤ 35 pts).",
    )
    step_p4 = make_chain_step(
        1, "RM01-P4", "Protocolo Inicial (Linha Pontilhada) — HF-rTMS M1 Contralesional", "HF-rTMS (10 Hz) — M1 Contralesional (Wang et al., 2022)",
        "rTMS Excitatória (10 Hz) — M1 Contralesional", "M1 contralesional (hemisfério não lesionado poupado)",
        "10 Hz | 100% LMR | 1.000 pulsos (100 trens de 10 pulsos, 10 s de intervalo)",
        sessoes="21 sessões diárias", efeito_esperado="+3,7 pts na FMA-UE (IC 95%: 2,4 a 5,0)",
        referencia="Wang et al. (2022) · DOI: 10.31083/j.jin2102050", linha_fluxograma="pontilhada",
        fase_etapa="inicial",
        observacoes="Confirmar ausência de PEM no hemisfério contralesional para descartar limitação técnica antes de concluir integridade não preservada.",
    )
    step_p5 = make_chain_step(
        1, "RM01-P5", "Protocolo Inicial (PEM Ausente) — HF-rTMS M1 Ipsilesional", "HF-rTMS (10 Hz) — M1 Ipsilesional sem PEM (Guo et al., 2016)",
        "rTMS Excitatória (10 Hz) — M1 Ipsilesional", "M1 ipsilesional (hemisfério lesionado)",
        "10 Hz | 90% LMR (ou calibrar pelo LMA se LMR ausente) | 1.500 pulsos (30 trens de 50 pulsos, 25 s de intervalo)",
        sessoes="10 sessões diárias associadas à terapia convencional", efeito_esperado="+23,3 pts na FMA-UE (IC 95%: -3,5 a 50,0)",
        referencia="Guo et al. (2016) · DOI: 10.1155/2016/6238575",
        fase_etapa="inicial",
    )
    step_p5_seq = make_chain_step(
        2, "RM01-P5-SEQ", "Próximo Protocolo — HF-rTMS M1 Ipsilesional", "HF-rTMS (10 Hz) — M1 Ipsilesional (Guo et al., 2016)",
        "rTMS Excitatória (10 Hz) — M1 Ipsilesional", "Córtex Motor Primário (M1) — hemisfério ipsilesional",
        "10 Hz | 90% LMR (ou calibrar pelo LMA se LMR ausente) | 1.500 pulsos (30 trens de 50 pulsos, 25 s de intervalo)",
        sessoes="10 sessões diárias associadas à terapia convencional", efeito_esperado="+23,3 pts na FMA-UE (IC 95%: -3,5 a 50,0)",
        referencia="Guo et al. (2016) · DOI: 10.1155/2016/6238575",
        fase_etapa="sequencia",
    )
    step_p6 = make_chain_step(
        3, "RM01-P6", "Escalonamento Combinado (Linha Pontilhada) — cTBS + Cerebelo", "cTBS Contralesional + HF-rTMS Cerebelar Contralesional (Kim et al., 2025)",
        "cTBS M1 Contralesional + HF-rTMS Cerebelar Contralesional", "M1 contralesional + Cerebelo contralesional (3 cm lateral ao ínion)",
        "cTBS (3 pulsos a 50 Hz repetidos a cada 200 ms / 5 Hz, 40 s contínuos, 600 pulsos, 70% LMR) contralesional seguido por rTMS cerebelar (10 Hz, 100% LMR, 1.000 pulsos, 20 trens de 50 pulsos, 25 s de intervalo) a 3 cm lateral ao ínion contralesional",
        sessoes="10 sessões diárias", efeito_esperado="+12,5 pts na FMA-UE (IC 95%: 9,9 a 21,1)",
        referencia="Kim et al. (2025) · DOI: 10.3390/jcm14072315", linha_fluxograma="pontilhada",
        fase_etapa="sequencia",
    )
    step_p6_s1 = make_chain_step(
        4, "RM01-P6", "Escalonamento Combinado (Linha Pontilhada) — cTBS + Cerebelo", "cTBS Contralesional + HF-rTMS Cerebelar Contralesional (Kim et al., 2025)",
        "cTBS M1 Contralesional + HF-rTMS Cerebelar Contralesional", "M1 contralesional + Cerebelo contralesional (3 cm lateral ao ínion)",
        "cTBS (3 pulsos a 50 Hz repetidos a cada 200 ms / 5 Hz, 40 s contínuos, 600 pulsos, 70% LMR) contralesional seguido por rTMS cerebelar (10 Hz, 100% LMR, 1.000 pulsos, 20 trens de 50 pulsos, 25 s de intervalo) a 3 cm lateral ao ínion contralesional",
        sessoes="10 sessões diárias", efeito_esperado="+12,5 pts na FMA-UE (IC 95%: 9,9 a 21,1)",
        referencia="Kim et al. (2025) · DOI: 10.3390/jcm14072315", linha_fluxograma="pontilhada",
        fase_etapa="sequencia",
    )
    step_alt1 = make_chain_step(
        3, "RM01-ALT1", "Seção de Ajustes — iTBS M1 + rPMS (Linha Pontilhada)", "iTBS M1 + rPMS no Sulco do Nervo Radial (Chang et al., 2024)",
        "iTBS M1 + rPMS no Sulco do Nervo Radial", "M1 ipsilesional (iTBS) seguido de sulco do nervo radial no úmero (rPMS — extensor radial do carpo)",
        "iTBS: 3 pulsos a 50 Hz repetidos a cada 200 ms (5 Hz), 2 s estímulo e 8 s pausa, 80% LMA ou 70% LMR, 1.200 pulsos · Intervalo de 10 minutos · rPMS: sulco do nervo radial no úmero, 3 pulsos a 50 Hz repetidos a 5 Hz, 2 s estímulo e 8 s pausa, 600 pulsos na intensidade para contração do extensor radial do carpo",
        sessoes="10 sessões diárias combinadas à fisioterapia convencional", efeito_esperado="+8,8 pts na FMA-UE (IC 95%: -7,4 a 25,0)",
        referencia="Chang et al. (2024) · DOI: 10.1186/s12984-024-01486-8", linha_fluxograma="pontilhada",
        fase_etapa="ajustes",
        observacoes="A sessão de iTBS deve ser separada por exatamente 10 minutos da rPMS; posicionar a bobina perpendicularmente às fibras musculares gerando contração visível.",
    )
    step_alt2 = make_chain_step(
        2, "RM01-ALT2", "Seção de Ajustes — iTBS Cerebelar (Linha Pontilhada)", "iTBS Cerebelar Ipsilesional (Chen et al., 2021)",
        "iTBS Cerebelar Ipsilesional", "Cerebelo ipsilesional (3 cm lateral ao ínion — bobina parabólica ou duplo cone)",
        "iTBS: 3 pulsos a 50 Hz repetidos a cada 200 ms (5 Hz), 2 s estímulo e 8 s pausa, 600 pulsos por sessão, 80% LMA, a 3 cm lateral ao ínion no hemisfério cerebelar ipsilesional",
        sessoes="10 sessões diárias combinadas à fisioterapia convencional", efeito_esperado="-1,0 pt na EAM para flexores de punho (IC 95%: 0,5 a 1,5)",
        referencia="Chen et al. (2021) · DOI: 10.3389/fncir.2021.655502", linha_fluxograma="pontilhada",
        fase_etapa="ajustes",
        observacoes="Etapa da seção de Ajustes após HF-rTMS M1 contralesional em pacientes sem PEM e com lesão pré-frontal extensa.",
    )

    scale_fma = make_scale(
        "fma_ue", "Fugl-Meyer Assessment — Extremidade Superior", "FMA-UE", "aumento",
        "+5,0 pontos na FMA-UE (Diferença Mínima Clinicamente Importante)",
        0.55, placeholder="Ex: 38", min_val=0, max_val=66, mcid_valor=5.0, mcid_label="+5,0 pontos na FMA-UE",
    )
    scale_fma_p4 = make_scale(
        "fma_ue", "Fugl-Meyer Assessment — Extremidade Superior", "FMA-UE", "aumento",
        "+3,7 pontos na FMA-UE (IC 95%: 2,4 a 5,0 — Wang et al., 2022)",
        0.48, placeholder="Ex: 22", min_val=0, max_val=66, mcid_valor=3.7, mcid_label="+3,7 pontos na FMA-UE",
    )
    scale_eam = make_scale(
        "eam", "Escala de Ashworth Modificada (EAM)", "EAM", "reducao",
        "Redução ≥ 1,0 ponto no escore de tônus muscular",
        0.52, tipo="ordinal_eam", placeholder="Ex: 2.0", min_val=0, max_val=4, mcid_valor=1.0, mcid_label="-1,0 ponto na EAM",
    )
    scale_fma_sens = make_scale(
        "fma_ue_sens", "FMA-UE — Subescala Sensorial (Seção II)", "FMA-UE Sensorial", "aumento",
        "+3,4 pontos na subescala sensorial da FMA-UE (IC 95%: 2,1 a 4,6 — Zanona et al., 2022)",
        0.56, placeholder="Ex: 6", min_val=0, max_val=12, mcid_valor=3.4, mcid_label="+3,4 pontos sensoriais",
    )
    scale_star_cancel_rtms = make_scale(
        "star_cancellation", "Teste de Cancelamento de Estrelas (BIT — Star Cancellation Test)", "Cancelamento de Estrelas", "aumento",
        "Aumento esperado de +10,4 pontos (IC 95%: 8,0 a 12,7) após 10 sessões diárias (corte satisfatório ≥ +8,0 pontos)",
        0.54, placeholder="Ex: 32", min_val=0, max_val=54, mcid_valor=8.0,
        mcid_label="≥ +8,0 pontos (limite inferior do IC 95%: 8,0–12,7 · média +10,4 pts)",
    )
    scale_star_cancel_tdcs = make_scale(
        "star_cancellation", "Teste de Cancelamento de Estrelas (BIT — Star Cancellation Test)", "Cancelamento de Estrelas", "aumento",
        "Aumento ≥ +5,0 estrelas (0–54) no Teste de Cancelamento de Estrelas (ou ≥ +7,0 pontos na etapa catódica P3/Cz — Yi et al., 2016)",
        0.50, placeholder="Ex: 32", min_val=0, max_val=54, mcid_valor=5.0,
        mcid_label="≥ +5,0 estrelas no Cancelamento de Estrelas (0–54)",
    )

    motor_scales_map = {
        "fraqueza": ["fma_ue"],
        "perda_sinergia": ["fma_ue"],
        "disfuncao_motora": ["fma_ue"],
        "espasticidade": ["eam"],
        "sensorial": ["fma_ue_sens"],
    }

    adj_rtms = {
        "titulo": "Ajustes de Tolerabilidade, Dose e Calibração em rTMS (Membro Superior)",
        "tolerabilidade": "Se houver desconforto com a bobina, reduzir inicialmente a intensidade e progredir gradualmente conforme a tolerância do paciente até o valor previsto no protocolo.",
        "dose_pulsos": "Nos protocolos excitatórios de rTMS (10 Hz) que utilizam 1.000 pulsos, recomenda-se ajustar para 1.500 pulsos por sessão visando maior efeito terapêutico; ciclos com mais de 15 sessões elevam o tamanho de efeito.",
        "calibracao_limiar": "Na ausência de identificação do LMR, calibrar pelo Limiar Motor Ativo (LMA). Para cerebelo, utilizar bobinas parabólicas ou duplo cone.",
    }
    adj_tdcs = {
        "titulo": "Ajustes de Tolerabilidade e Densidade em tDCS (Membro Superior)",
        "tolerabilidade": "Hidratar uniformemente as esponjas (25–35 cm²) com solução salina, inspecionar a pele a cada sessão e ajustar rampa caso haja desconforto cutâneo.",
        "dose_pulsos": "Titular protocolos tDCS para 2 mA e 30 minutos quando tolerado, pela maior densidade de corrente e duração; ciclos > 15 sessões simultâneos à terapia funcional geram maior efeito.",
        "calibracao_limiar": "Não requer PEM/LMR; pacientes com comprometimentos motores leves tendem a ser mais responsivos à tDCS.",
    }
    falha_rtms_mod = _falha_mod(
        "Ausência de resposta clínica mesmo após percorrer os protocolos sequenciais e a seção de Ajustes desta rota.",
        "1. Conferir calibração de LMR/LMA, checagem contralesional do PEM e adesão às terapias convencionais;\n2. Garantir conclusão da sequência terapêutica e dos Ajustes no Assistente Pós-Indução;\n3. Considerar transição para estimulação elétrica transcraniana (tDCS/taVNS) ou investigar dor neuropática/nociceptiva como fator limitante principal.",
    )
    falha_tdcs_mod = _falha_mod(
        "Ausência de resposta clínica após conclusão da sequência tDCS otimizada (2 mA, 30 min) e da seção de Ajustes.",
        "1. Otimizar densidade 2 mA e 30 min simultânea à tarefa motora ou sensorial;\n2. Concluir os protocolos da seção de Ajustes indicados na rota;\n3. Considerar transição para estimulação magnética (rTMS/iTBS) caso não haja contraindicações ou seguir o fluxo de Dor Neuropática Crônica se dor limitante.",
    )
    sa_rtms = _sessoes_aj(
        "Avaliar evolução clínica após 5 sessões com o protocolo indicado e adesão confirmada; ausência de melhora (quantitativa ou qualitativa) nos fatores limitantes indica resposta insatisfatória.",
        "",
        "Ao atingir platô funcional sustentado, interromper o ciclo intensivo e iniciar redução gradual da frequência das sessões.",
    )
    sa_tdcs = _sessoes_aj(
        "Avaliar evolução clínica após 5 sessões simultâneas à terapia convencional; ausência de melhora (quantitativa ou qualitativa) nos fatores limitantes indica resposta insatisfatória.",
        "",
        "Ao atingir platô funcional sustentado, interromper o ciclo intensivo e iniciar redução gradual da frequência das sessões.",
    )

    modalidades = {
        "fraqueza": make_mod(
            protocolo_id="RM01-P1", tecnica="HF-rTMS (10 Hz) — M1 Ipsilesional (Guo et al., 2016)", modalidade_sigla="rTMS / HF-rTMS",
            alvo="Córtex Motor Primário (M1) — hemisfério ipsilesional (hotspot via PEM)", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="1.500 pulsos (30 trens de 50 pulsos, 25 s de intervalo)", sessoes="10 sessões diárias associadas à fisioterapia e terapia ocupacional",
            escala_recomendada="FMA-UE / MRC / EAM / MAL-Brazil (conforme fator limitante)", meta_melhora="+5,0 pontos na FMA-UE (MCID)",
            tamanho_efeito=0.55, evidencia="Nível A — Eficácia definida (IFCN 2020 · 35 ECRs Antonino 2025)", linha_fluxograma="solida",
            diretriz_internacional="Nível A (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_GUO_2016, meta_analise=REF_ANTONINO_2025,
            mcid_valor=5.0, mcid_label="+5,0 pontos na FMA-UE", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Guo et al. (2016)", efeito_resumo="+23,3 pts FMA-UE (IC 95%: -3,5 a 50,0)",
            escalas_detalhadas=[scale_fma, scale_eam, scale_fma_sens], escalas_por_fator=motor_scales_map,
            cadeia_sequencial=[step_p1, step_p2, step_alt1],
            ajuste_parametros=adj_rtms, falha_terapeutica=falha_rtms_mod, sessoes_ajuste=sa_rtms,
            notas_clinicas="Efeito mais pronunciado na fase subaguda (1 a 6 meses). Associar terapias convencionais direcionadas ao membro superior e à área estimulada; não interromper medicações em uso.",
            audit_meta=_audit("Moderada", "Revisão sistemática com 6 bases, avaliação PEDro e metanálise dose-resposta via curva ROC (35 ECRs, n=897).", "Busca abrangente em 6 bases e curva ROC dose-resposta em ≥ 15 sessões.", ["Avaliação PEDro", "Curva ROC"], "Alta", "Forte", "Nível A (Lefaucheur et al., 2020) e 35 ECRs (Antonino et al., 2025) na presença de PEM.", tol_rtms),
        ),
        "perda_sinergia": make_mod(
            protocolo_id="RM01-P1-SIN", tecnica="HF-rTMS (10 Hz) — M1 Ipsilesional (Guo et al., 2016)", modalidade_sigla="rTMS / HF-rTMS",
            alvo="Córtex Motor Primário (M1) — hemisfério ipsilesional (Foco em FMA-UE Seção III)", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="1.500 pulsos (30 trens de 50 pulsos, 25 s de intervalo)", sessoes="10 sessões diárias associadas à fisioterapia e terapia ocupacional",
            escala_recomendada="FMA-UE Seção III (36 pts) + MAL-Brazil", meta_melhora="+5,0 pontos na FMA-UE (MCID)",
            tamanho_efeito=0.55, evidencia="Nível A — Eficácia definida (IFCN 2020)", linha_fluxograma="solida",
            diretriz_internacional="Nível A (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_GUO_2016, meta_analise=REF_ANTONINO_2025,
            mcid_valor=5.0, mcid_label="+5,0 pontos na FMA-UE", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Guo et al. (2016)", efeito_resumo="+23,3 pts na FMA-UE global",
            escalas_detalhadas=[scale_fma], cadeia_sequencial=[step_p1, step_p2, step_alt1],
            ajuste_parametros=adj_rtms, falha_terapeutica=falha_rtms_mod, sessoes_ajuste=sa_rtms,
            notas_clinicas="Perda de sinergia avaliada pela Seção III da FMA-UE (36 pts). Associar terapias convencionais direcionadas ao membro superior; não interromper medicações.",
            audit_meta=_audit("Moderada", "Metanálise dose-resposta com 35 ECRs (Antonino et al., 2025).", "Consistente com efeito motor global de HF-rTMS.", ["Avaliação PEDro"], "Alta", "Forte", "Evidência sólida quando PEM presente.", tol_rtms),
        ),
        "espasticidade": make_mod(
            protocolo_id="RM01-ESP", tecnica="HF-rTMS (10 Hz) — M1 Ipsilesional (Guo et al., 2016)", modalidade_sigla="rTMS / HF-rTMS",
            alvo="Córtex Motor Primário (M1) — hemisfério ipsilesional", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="1.500 pulsos (30 trens de 50 pulsos, 25 s de intervalo)", sessoes="10 sessões diárias associadas à fisioterapia e terapia ocupacional",
            escala_recomendada="Escala de Ashworth Modificada (EAM)", meta_melhora="-1,0 ponto na EAM",
            tamanho_efeito=0.52, evidencia="Nível B — Evidência moderada (Fan et al., 2022)", linha_fluxograma="solida",
            diretriz_internacional="Nível A/B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_GUO_2016, meta_analise=REF_FAN_2022,
            mcid_valor=1.0, mcid_label="-1,0 ponto na EAM", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Guo et al. (2016) / Fan et al. (2022)", efeito_resumo="Redução de tônus espástico (≥ 1 grau EAM) e ganho motor associado",
            escalas_detalhadas=[scale_eam], cadeia_sequencial=[step_p1, step_p2, step_alt1],
            ajuste_parametros=adj_rtms, falha_terapeutica=falha_rtms_mod, sessoes_ajuste=sa_rtms,
            notas_clinicas="Efeito mais pronunciado na fase subaguda (1–6 meses). Na etapa de Ajustes com rPMS, adotar modo contínuo para músculos espásticos; não interromper medicações.",
            audit_meta=_audit("Moderada", "Revisão sistemática em 8 bases, risco de viés em duplicata e GRADE relatado (42 ECRs, n=2.108).", "Busca em 8 bases e GRADE relatado (Fan et al., 2022).", ["Risco de viés", "Heterogeneidade", "GRADE"], "Moderada", "Condicional", "Heterogeneidade moderada entre alvos corticais e cerebelares.", tol_rtms),
        ),
        "disfuncao_motora": make_mod(
            protocolo_id="RM01-DMOT", tecnica="HF-rTMS (10 Hz) — M1 Ipsilesional (Guo et al., 2016)", modalidade_sigla="rTMS / HF-rTMS",
            alvo="Córtex Motor Primário (M1) — hemisfério ipsilesional", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="1.500 pulsos (30 trens de 50 pulsos, 25 s de intervalo)", sessoes="10 sessões diárias associadas à fisioterapia e terapia ocupacional",
            escala_recomendada="FMA-UE Seções III-IV (66 pts) + MAL-Brazil", meta_melhora="+5,0 pontos na FMA-UE (MCID)",
            tamanho_efeito=0.55, evidencia="Nível A — Eficácia definida (IFCN 2020)", linha_fluxograma="solida",
            diretriz_internacional="Nível A (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_GUO_2016, meta_analise=REF_ANTONINO_2025,
            mcid_valor=5.0, mcid_label="+5,0 pontos na FMA-UE", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Guo et al. (2016)", efeito_resumo="+23,3 pts na FMA-UE",
            escalas_detalhadas=[scale_fma], cadeia_sequencial=[step_p1, step_p2, step_alt1],
            ajuste_parametros=adj_rtms, falha_terapeutica=falha_rtms_mod, sessoes_ajuste=sa_rtms,
            notas_clinicas="Avaliar FMA-UE (> 35 pts como ponto de corte) e desempenho funcional nas AVDs via MAL-Brazil; associar fisioterapia/TO.",
            audit_meta=_audit("Moderada", "Metanálise dose-resposta com 35 ECRs.", "Consistente para recuperação motora global pós-AVC.", ["Avaliação PEDro"], "Alta", "Forte", "Nível A com PEM positivo.", tol_rtms),
        ),
        "rtms_m1_grave": make_mod(
            protocolo_id="RM01-P2", tecnica="rTMS Bilateral (1 Hz Contralesional + 10 Hz Ipsilesional — Long et al., 2018)", modalidade_sigla="rTMS Bilateral",
            alvo="M1 contralesional (1 Hz) seguido de M1 ipsilesional (10 Hz)", frequencia="1 Hz (contra) + 10 Hz (ipsi)", intensidade="90% LMR",
            pulsos_duracao="1.000 pulsos (1 Hz) + 1.000 pulsos (10 Hz, 10 s trens, 50 s de intervalo)", sessoes="15 sessões diárias associadas à fisioterapia e terapia ocupacional",
            escala_recomendada="FMA-UE (≤ 35 pts) + MAL-Brazil", meta_melhora="+5,0 pontos na FMA-UE (MCID)",
            tamanho_efeito=0.50, evidencia="Nível B — Eficácia provável (Long et al., 2018)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_LONG_2018, meta_analise=REF_ANTONINO_2025,
            mcid_valor=5.0, mcid_label="+5,0 pontos na FMA-UE", cohen_d_valor=0.50, cohen_d_interp="Moderado",
            estudo_referencia="Long et al. (2018)", efeito_resumo="+6,6 pts FMA-UE (IC 95%: 4,1 a 9,1) após 15 sessões",
            escalas_detalhadas=[scale_fma, scale_eam, scale_fma_sens], escalas_por_fator=motor_scales_map,
            cadeia_sequencial=[step_p2_inicial, step_p3_seq, step_alt1],
            ajuste_parametros=adj_rtms, falha_terapeutica=falha_rtms_mod, sessoes_ajuste=sa_rtms,
            notas_clinicas="Indicado inicialmente para comprometimento moderado a grave (FMA-UE ≤ 35 pts). Associar terapias convencionais direcionadas ao membro superior e não interromper medicações.",
            audit_meta=_audit("Moderada", "Metanálise dose-resposta (Antonino et al., 2025).", "Inclui subgrupos de comprometimento moderado-grave.", ["Avaliação PEDro"], "Moderada", "Condicional", "Necessita ≥ 15 sessões em déficit motor moderado-grave.", tol_rtms),
        ),
        "sem_pem": make_mod(
            protocolo_id="RM01-P4", tecnica="HF-rTMS (10 Hz) — M1 Contralesional (Wang et al., 2022)", modalidade_sigla="rTMS (Pontilhado)",
            alvo="M1 CONTRALESIONAL (lesão cortical extensa no giro pré-frontal sem PEM)", frequencia="10 Hz", intensidade="100% LMR",
            pulsos_duracao="1.000 pulsos (100 trens × 10 pulsos, 10 s intervalo)", sessoes="21 sessões diárias associadas à reabilitação motora",
            escala_recomendada="FMA-UE (Fugl-Meyer) + MAL-Brazil", meta_melhora="+3,7 pts na FMA-UE (IC 95%: 2,4 a 5,0)",
            tamanho_efeito=0.48, evidencia="Nível C — Evidência exploratória (Quadro pontilhado)", linha_fluxograma="pontilhada",
            diretriz_internacional="Nível B/C (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_WANG_2022, meta_analise=REF_ZHU_2025,
            mcid_valor=3.7, mcid_label="+3,7 pontos na FMA-UE", cohen_d_valor=0.48, cohen_d_interp="Moderado",
            estudo_referencia="Wang et al. (2022)", efeito_resumo="+3,7 pts na FMA-UE (IC 95%: 2,4 a 5,0)",
            escalas_detalhadas=[scale_fma_p4, scale_eam, scale_fma_sens], escalas_por_fator=motor_scales_map,
            cadeia_sequencial=[step_p4, step_alt2],
            ajuste_parametros=adj_rtms, falha_terapeutica=falha_rtms_mod, sessoes_ajuste=sa_rtms,
            notas_clinicas="Confirmar ausência de PEM no hemisfério contralesional para excluir falha técnica antes de adotar estimulação contralesional; associar reabilitação motora e manter medicações.",
            audit_meta=_audit("Moderada", "Revisão sistemática de vias motoras alternativas (Zhu et al., 2025).", "Evidência específica em ausência de PEM e lesão pré-frontal extensa.", ["Risco de viés"], "Baixa", "Condicional", "Quadro pontilhado (Wang et al., 2022): modula hemisfério contralesional poupado.", tol_rtms),
        ),
        "sem_pem_ipsilesional": make_mod(
            protocolo_id="RM01-P5", tecnica="HF-rTMS (10 Hz) — M1 Ipsilesional sem PEM (Guo et al., 2016)", modalidade_sigla="rTMS",
            alvo="M1 IPSILESIONAL (sem lesão cortical extensa no giro pré-frontal)", frequencia="10 Hz", intensidade="90% LMR (ou LMA quando LMR ausente)",
            pulsos_duracao="1.500 pulsos (30 trens de 50 pulsos, 25 s de intervalo)", sessoes="10 sessões diárias associadas à terapia convencional",
            escala_recomendada="FMA-UE (Fugl-Meyer) + MAL-Brazil", meta_melhora="+5,0 pontos na FMA-UE (MCID)",
            tamanho_efeito=0.52, evidencia="Nível B — Evidência clínica favorável", linha_fluxograma="solida",
            diretriz_internacional="Nível A/B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_GUO_2016, meta_analise=REF_ANTONINO_2025,
            mcid_valor=5.0, mcid_label="+5,0 pontos na FMA-UE", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Guo et al. (2016)", efeito_resumo="+23,3 pts na FMA-UE",
            escalas_detalhadas=[scale_fma, scale_eam, scale_fma_sens], escalas_por_fator=motor_scales_map,
            cadeia_sequencial=[step_p5, step_p2, step_p6],
            ajuste_parametros=adj_rtms, falha_terapeutica=falha_rtms_mod, sessoes_ajuste=sa_rtms,
            notas_clinicas="Na ausência de LMR identificável, calibrar intensidade utilizando o Limiar Motor Ativo (LMA); manter terapias convencionais associadas.",
            audit_meta=_audit("Moderada", "Metanálise dose-resposta em rTMS pós-AVC (Antonino et al., 2025).", "Córtex pré-frontal poupado permite estimulação ipsilesional em M1.", ["Avaliação PEDro"], "Moderada", "Condicional", "Calibração por LMA quando LMR não captado.", tol_rtms),
        ),
        "sensorial": make_mod(
            protocolo_id="RM01-S1", tecnica="HF-rTMS (10 Hz) — Córtex Somatossensorial Primário (Zanona et al., 2022)", modalidade_sigla="rTMS S1",
            alvo="S1 — hemisfério ipsilesional (3 cm posterior a M1/C3-C4 via PEM)", frequencia="10 Hz", intensidade="120% LMR",
            pulsos_duracao="1.500 pulsos (30 trens de 50 pulsos, 30 s de intervalo)", sessoes="10 sessões diárias com estimulação sensorial associada",
            escala_recomendada="FMA-UE Subescala Sensorial (Seção II — 12 pts)", meta_melhora="+3,4 pts na FMA-UE sensorial (IC 95%: 2,1 a 4,6)",
            tamanho_efeito=0.56, evidencia="Nível B — Evidência clínica favorável (Zanona et al., 2022)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_ZANONA_2022, meta_analise=REF_CHEN_2023,
            mcid_valor=3.4, mcid_label="+3,4 pontos sensoriais", cohen_d_valor=0.56, cohen_d_interp="Moderado",
            estudo_referencia="Zanona et al. (2022)", efeito_resumo="+3,4 pts na subescala sensorial FMA-UE",
            escalas_detalhadas=[scale_fma_sens],
            cadeia_sequencial=[
                make_chain_step(1, "RM01-PS1-1", "Protocolo Inicial — HF-rTMS S1", "HF-rTMS (10 Hz) — S1 Ipsilesional (Zanona et al., 2022)", "rTMS Excitatória (10 Hz)", "S1 ipsilesional — 3 cm posterior a M1 (C3/C4 via PEM)", "10 Hz | 120% LMR | 1.500 pulsos (30 trens × 50 pulsos, 30 s intervalo)", sessoes="10 sessões diárias", efeito_esperado="+3,4 pts subescala sensorial FMA-UE (IC 95%: 2,1 a 4,6)", referencia="Zanona et al. (2022) · DOI: 10.3389/fnhum.2022.860965", fase_etapa="inicial"),
                step_p5_seq,
                step_p2,
                step_p6_s1,
            ],
            ajuste_parametros=adj_rtms, falha_terapeutica=falha_rtms_mod, sessoes_ajuste=sa_rtms,
            notas_clinicas="Associar à estimulação somatossensorial periférica ou treino sensitivo; se lesão cortical extensa no giro pós-frontal, redirecionar diretamente ao ramo motor M1 ipsilesional.",
            audit_meta=_audit("Moderada", "Metanálise em déficits sensoriais pós-AVC (Chen et al., 2023).", "Risco de viés e heterogeneidade avaliados.", ["Risco de viés", "Heterogeneidade"], "Moderada", "Condicional", "S1 3 cm posterior ao hotspot motor mostra ganho sensorial consistente.", tol_rtms),
        ),
        "negligencia": make_mod(
            protocolo_id="RM01-PPC", tecnica="HF-rTMS (10 Hz) — Córtex Parietal Posterior Ipsilesional (Kim et al., 2013)", modalidade_sigla="rTMS PPC",
            alvo="Córtex Parietal Posterior (PPC) — P3/P4 ipsilesional", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="1.000 pulsos (20 trens de 50 pulsos, 55 s de intervalo)", sessoes="10 sessões diárias associadas à varredura visual",
            escala_recomendada="Teste de Cancelamento de Estrelas (BIT — 0 a 54)", meta_melhora="Aumento de 10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias",
            tamanho_efeito=0.54, evidencia="Nível B — Eficácia clínica em heminegligência", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_KIM_2013, meta_analise=REF_FAN_2017,
            mcid_valor=8.0, mcid_label="≥ +8,0 pontos (IC 95%: 8,0 a 12,7 · média +10,4 pts)", cohen_d_valor=0.54, cohen_d_interp="Moderado",
            estudo_referencia="Kim et al. (2013)", efeito_resumo="Aumento de 10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
            ic_min=8.0, ic_max=12.7,
            escalas_detalhadas=[scale_star_cancel_rtms],
            cadeia_sequencial=[
                make_chain_step(
                    1, "RM01-PPC-1", "Protocolo Inicial — HF-rTMS PPC Ipsilesional", "HF-rTMS (10 Hz) — PPC P3/P4 Ipsilesional (Kim et al., 2013)",
                    "rTMS Excitatória (10 Hz)", "P3/P4 ipsilesional", "10 Hz | 90% LMR | 1.000 pulsos (20 trens de 50 pulsos, 55 s de intervalo)",
                    sessoes="10 sessões diárias",
                    efeito_esperado="Aumento de 10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
                    referencia="Kim et al. (2013) · DOI: 10.1016/j.apmr.2012.12.016", fase_etapa="inicial",
                    calc_meta={
                        "mcid_valor": 8.0,
                        "mcid_label": "≥ +8,0 pontos (limite inferior do IC 95%: 8,0–12,7 · média +10,4 pts)",
                        "meta_texto": "Aumento esperado de +10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias",
                        "ic_min": 8.0,
                        "ic_max": 12.7,
                        "estudo_referencia": "Kim et al. (2013) — HF-rTMS 10 Hz P3/P4 Ipsilesional",
                        "efeito_esperado_resumo": "Aumento de 10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
                    },
                ),
                make_chain_step(
                    2, "RM01-PPC-2", "Próximo Protocolo — LF-rTMS PPC Contralesional", "LF-rTMS (1 Hz) — PPC P3/P4 Contralesional (Kim et al., 2013)",
                    "rTMS Inibitória (1 Hz)", "P3/P4 contralesional", "1 Hz | 90% LMR | 1.200 pulsos",
                    sessoes="10 sessões diárias",
                    efeito_esperado="Aumento de 16,4 pontos (IC 95%: 13,0 a 20,0) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
                    referencia="Kim et al. (2013) · DOI: 10.1016/j.apmr.2012.12.016", fase_etapa="sequencia",
                    calc_meta={
                        "mcid_valor": 13.0,
                        "mcid_label": "≥ +13,0 pontos (limite inferior do IC 95%: 13,0–20,0 · média +16,4 pts)",
                        "meta_texto": "Aumento esperado de +16,4 pontos (IC 95%: 13,0 a 20,0) no teste de cancelamento de estrelas após 10 sessões diárias",
                        "ic_min": 13.0,
                        "ic_max": 20.0,
                        "estudo_referencia": "Kim et al. (2013) — LF-rTMS 1 Hz P3/P4 Contralesional",
                        "efeito_esperado_resumo": "Aumento de 16,4 pontos (IC 95%: 13,0 a 20,0) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
                    },
                ),
                make_chain_step(
                    3, "RM01-ALT3", "Seção de Ajustes — iTBS F5 (Linha Pontilhada)", "iTBS DLPFC Esquerdo F5 (Cao et al., 2016)",
                    "iTBS DLPFC Esquerdo", "F5 (entre F3 e F7) — Córtex pré-frontal dorsolateral esquerdo",
                    "iTBS: 2 sessões separadas por 15 min, 3 pulsos a 50 Hz repetidos a 200 ms (5 Hz), 2 s estímulo e 8 s pausa, 600 pulsos, 80% LMR",
                    sessoes="10 dias de tratamento",
                    efeito_esperado="+37% no teste de cancelamento de estrelas após 10 dias de tratamento",
                    referencia="Cao et al. (2016) · DOI: 10.1097/WNR.0000000000000689", linha_fluxograma="pontilhada", fase_etapa="ajustes",
                    calc_meta={
                        "mcid_valor": 37.0,
                        "mcid_label": "≥ +37% no teste de cancelamento de estrelas (Cao et al., 2016)",
                        "meta_texto": "Aumento esperado ≥ +37% no teste de cancelamento de estrelas após 10 dias de tratamento",
                        "is_percent": True,
                        "estudo_referencia": "Cao et al. (2016) — iTBS DLPFC Esquerdo (F5)",
                        "efeito_esperado_resumo": "Aumento de +37% no teste de cancelamento de estrelas após 10 dias de tratamento",
                    },
                ),
            ],
            ajuste_parametros=adj_rtms, falha_terapeutica=falha_rtms_mod, sessoes_ajuste=sa_rtms,
            notas_clinicas="Associar à terapia de varredura visual e feedback espacial; manter terapias medicamentosas em uso.",
            audit_meta=_audit("Moderada", "Metanálise em heminegligência unilateral pós-AVC (Fan et al., 2017).", "ECRs duplo-cegos consistentes no PPC.", ["Risco de viés"], "Moderada", "Condicional", "Evidência moderada para reequilíbrio parietal.", tol_rtms),
        ),
        # --- RM02 tDCS / taVNS leaves ---
        "tdcs_m1_pf_nao": make_mod(
            protocolo_id="RM02-P1", tecnica="tDCS Anódica — M1 Ipsilesional (Kashoo et al., 2022)", modalidade_sigla="tDCS",
            alvo="Ânodo C3/C4 ipsilesional + Cátodo Fp1/Fp2 contralesional (35 cm²)", frequencia="Contínua", intensidade="1,5 mA",
            pulsos_duracao="30 min (eletrodos 35 cm²)", sessoes="15 a 20 sessões simultâneas à terapia motora",
            escala_recomendada="FMA-UE / EAM (conforme fator limitante)", meta_melhora="+5,0 pontos na FMA-UE (MCID)",
            tamanho_efeito=0.52, evidencia="Nível B — Eficácia provável (IFCN tDCS 2017)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_KASHOO_2022, meta_analise=REF_ANTONINO_2025,
            mcid_valor=5.0, mcid_label="+5,0 pontos na FMA-UE", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Kashoo et al. (2022)", efeito_resumo="+7,6 pts na FMA-UE após 15–20 sessões",
            escalas_detalhadas=[scale_fma, scale_eam, scale_fma_sens], escalas_por_fator=motor_scales_map,
            cadeia_sequencial=[
                make_chain_step(1, "RM02-P1", "Protocolo Inicial — tDCS Anódica M1 Ipsilesional", "tDCS Anódica M1 Ipsilesional (Kashoo et al., 2022)", "tDCS Anódica", "Ânodo C3/C4 ipsi + Cátodo Fp1/Fp2 contra (35 cm²)", "1,5 mA | 30 min", sessoes="15–20 sessões simultâneas à terapia", efeito_esperado="+7,6 pts FMA-UE", referencia="Kashoo et al. (2022) · DOI: 10.3390/ijerph192215199", fase_etapa="inicial"),
                make_chain_step(2, "RM02-P2", "Próximo Protocolo — tDCS Bilateral M1", "tDCS Bilateral M1 (Koh et al., 2017)", "tDCS Bihemisférica", "Ânodo C3/C4 ipsi + Cátodo C3/C4 contra (25 cm²)", "1,5 mA | 30 min", sessoes="15–20 sessões", efeito_esperado="+6,0 pts FMA-UE", referencia="Koh et al. (2017) · DOI: 10.1016/j.apmr.2017.05.025", fase_etapa="sequencia"),
                make_chain_step(3, "RM02-P3", "Próximo Protocolo — tDCS Catódica M1 Contralesional", "tDCS Catódica M1 Contralesional (Yao et al., 2020)", "tDCS Catódica", "Cátodo C3/C4 contra + Ânodo supraorbital ipsi (35 cm²)", "2,0 mA | 20 min", sessoes="15–20 sessões", efeito_esperado="+10,1 pts FMA-UE", referencia="Yao et al. (2020) · DOI: 10.1186/s12984-020-00699-x", fase_etapa="sequencia"),
                make_chain_step(4, "RM02-ALT1", "Seção de Ajustes — tDCS Cerebelar Contralesional (Linha Pontilhada)", "tDCS Cerebelar Contralesional (Gong et al., 2023)", "tDCS Cerebelar", "Cerebelo contralesional (3 cm lateral ao ínion, 35 cm²)", "2,0 mA | 20 min", sessoes="15 sessões", efeito_esperado="+10,7 pts FMA-UE", referencia="Gong et al. (2023) · DOI: 10.3389/fneur.2023.1044333", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
                make_chain_step(5, "RM02-ALT2", "Seção de Ajustes — taVNS Auricular (Linha Pontilhada)", "taVNS Auricular Esquerda (Wang et al., 2024)", "taVNS", "Concha da orelha esquerda", "500 µs | 25 Hz | limiar até 10 mA | 60 min", sessoes="15 sessões", efeito_esperado="+10,6 pts FMA-UE", referencia="Wang et al. (2024) · DOI: 10.3389/fnins.2024.1346634", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
            ],
            ajuste_parametros=adj_tdcs, falha_terapeutica=falha_tdcs_mod, sessoes_ajuste=sa_tdcs,
            notas_clinicas="Aplicar simultaneamente à terapia funcional do membro superior para maior efeito; não suspender medicações em uso.",
            audit_meta=_audit("Moderada", "Revisão e diretriz IFCN tDCS (2017).", "Parâmetros otimizados com 2 mA e 30 min simultâneos.", ["IFCN tDCS"], "Moderada", "Condicional", "Pacientes leves apresentam maior resposta à tDCS.", tol_tdcs),
            mod_tipo="tdcs",
        ),
        "tdcs_m1_pf_sim_ext_nao": make_mod(
            protocolo_id="RM02-P4", tecnica="tDCS Anódica — M1 Contralesional (Klomjai et al., 2022)", modalidade_sigla="tDCS (Pontilhado)",
            alvo="Ânodo C3/C4 CONTRALESIONAL + Cátodo Fp1/Fp2 ipsilesional (35 cm²)", frequencia="Contínua", intensidade="1,75 mA",
            pulsos_duracao="20 min (eletrodos 35 cm²) | extensão < 10°", sessoes="15 a 20 sessões simultâneas à terapia",
            escala_recomendada="FMA-UE / EAM (conforme fator limitante)", meta_melhora="+5,0 pontos na FMA-UE (MCID)",
            tamanho_efeito=0.46, evidencia="Nível C — Ensaio exploratório (Pontilhado)", linha_fluxograma="pontilhada",
            diretriz_internacional="Nível B/C (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_KLOMJAI_2022, meta_analise=REF_ZHU_2025,
            mcid_valor=5.0, mcid_label="+5,0 pontos na FMA-UE", cohen_d_valor=0.46, cohen_d_interp="Pequeno",
            estudo_referencia="Klomjai et al. (2022)", efeito_resumo="Facilitação das vias ipsilaterais em lesão grave",
            escalas_detalhadas=[scale_fma, scale_eam, scale_fma_sens], escalas_por_fator=motor_scales_map,
            cadeia_sequencial=[
                make_chain_step(1, "RM02-P4", "Protocolo Inicial (Linha Pontilhada) — tDCS M1 Contralesional", "tDCS Anódica M1 Contralesional (Klomjai et al., 2022)", "tDCS Anódica Contralesional", "Ânodo C3/C4 contralesional + Cátodo Fp1/Fp2 ipsi", "1,75 mA | 20 min | 35 cm²", sessoes="15–20 sessões", efeito_esperado="Modulação espinhal ipsilateral na ausência de extensão ≥ 10°", referencia="Klomjai et al. (2022) · DOI: 10.1016/j.clinph.2021.12.016", linha_fluxograma="pontilhada", fase_etapa="inicial"),
                make_chain_step(2, "RM02-ALT1", "Seção de Ajustes — tDCS Cerebelar Contralesional (Linha Pontilhada)", "tDCS Cerebelar Contralesional (Gong et al., 2023)", "tDCS Cerebelar", "Cerebelo contralesional (3 cm lateral ao ínion)", "2,0 mA | 20 min | 35 cm²", sessoes="15 sessões", efeito_esperado="+10,7 pts FMA-UE", referencia="Gong et al. (2023) · DOI: 10.3389/fneur.2023.1044333", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
                make_chain_step(3, "RM02-ALT2", "Seção de Ajustes — taVNS Auricular (Linha Pontilhada)", "taVNS Auricular Esquerda (Wang et al., 2024)", "taVNS Auricular", "Concha da orelha esquerda", "500 µs | 25 Hz | 60 min", sessoes="15 sessões", efeito_esperado="+10,6 pts FMA-UE", referencia="Wang et al. (2024) · DOI: 10.3389/fnins.2024.1346634", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
            ],
            ajuste_parametros=adj_tdcs, falha_terapeutica=falha_tdcs_mod, sessoes_ajuste=sa_tdcs,
            notas_clinicas="Indicado quando há lesão pré-frontal sem extensão ativa mínima de 10°. Aplicar simultaneamente à terapia motora.",
            audit_meta=_audit("Moderada", "Vias motoras alternativas pós-AVC (Zhu et al., 2025).", "Ensaio único exploratório (pontilhado).", ["Quadro pontilhado"], "Baixa", "Condicional", "Indicado quando ausência de extensão ativa ≥ 10°.", tol_tdcs),
            mod_tipo="tdcs",
        ),
        "tdcs_m1_pf_sim_ext_sim": make_mod(
            protocolo_id="RM02-P5", tecnica="tDCS Anódica — Córtex Pré-Motor Ipsilesional (Cunningham et al., 2015)", modalidade_sigla="tDCS (Pontilhado)",
            alvo="Córtex Pré-Motor ipsilesional (2,5 cm anterior a C3/C4, 35 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="30 min (eletrodos 35 cm²) | extensão ≥ 10° presente", sessoes="15 a 20 sessões simultâneas à terapia",
            escala_recomendada="FMA-UE / EAM (conforme fator limitante)", meta_melhora="+5,0 pontos na FMA-UE (MCID)",
            tamanho_efeito=0.50, evidencia="Nível C — Ensaio exploratório (Pontilhado)", linha_fluxograma="pontilhada",
            diretriz_internacional="Nível B/C (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_CUNNINGHAM_2015, meta_analise=REF_ANTONINO_2025,
            mcid_valor=5.0, mcid_label="+5,0 pontos na FMA-UE", cohen_d_valor=0.50, cohen_d_interp="Moderado",
            estudo_referencia="Cunningham et al. (2015)", efeito_resumo="+6,8 pts na FMA-UE",
            escalas_detalhadas=[scale_fma, scale_eam, scale_fma_sens], escalas_por_fator=motor_scales_map,
            cadeia_sequencial=[
                make_chain_step(1, "RM02-P5", "Protocolo Inicial (Linha Pontilhada) — tDCS Pré-Motora Ipsilesional", "tDCS Pré-Motora Ipsilesional (Cunningham et al., 2015)", "tDCS Pré-Motora", "2,5 cm anterior a C3/C4 ipsilesional (35 cm²)", "1,0 mA | 30 min", sessoes="15–20 sessões", efeito_esperado="+6,8 pts FMA-UE", referencia="Cunningham et al. (2015) · DOI: 10.3233/RNN-150574", linha_fluxograma="pontilhada", fase_etapa="inicial"),
                make_chain_step(2, "RM02-P3", "Próximo Protocolo — tDCS Catódica M1 Contralesional", "tDCS Catódica M1 Contralesional (Yao et al., 2020)", "tDCS Catódica", "Cátodo C3/C4 contralesional", "2,0 mA | 20 min", sessoes="15–20 sessões", efeito_esperado="+10,1 pts FMA-UE", referencia="Yao et al. (2020) · DOI: 10.1186/s12984-020-00699-x", fase_etapa="sequencia"),
                make_chain_step(3, "RM02-ALT1", "Seção de Ajustes — tDCS Cerebelar Contralesional (Linha Pontilhada)", "tDCS Cerebelar Contralesional (Gong et al., 2023)", "tDCS Cerebelar", "Cerebelo contralesional (3 cm lateral ao ínion)", "2,0 mA | 20 min | 35 cm²", sessoes="20 sessões", efeito_esperado="+10,7 pts FMA-UE", referencia="Gong et al. (2023) · DOI: 10.3389/fneur.2023.1044333", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
                make_chain_step(4, "RM02-ALT2", "Seção de Ajustes — taVNS Auricular (Linha Pontilhada)", "taVNS Auricular Esquerda (Wang et al., 2024)", "taVNS Auricular", "Concha auricular esquerda", "500 µs | 25 Hz | 30 s ON/OFF | até 10 mA | 60 min", sessoes="20 sessões", efeito_esperado="+10,6 pts FMA-UE", referencia="Wang et al. (2024) · DOI: 10.3389/fnins.2024.1346634", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
            ],
            ajuste_parametros=adj_tdcs, falha_terapeutica=falha_tdcs_mod, sessoes_ajuste=sa_tdcs,
            notas_clinicas="Indicado em lesão pré-frontal com extensão ativa preservada (≥ 10°); aplicar simultaneamente ao treino funcional.",
            audit_meta=_audit("Moderada", "Evidência em estimulação pré-motora.", "Reservado a pacientes com extensão mínima preservada (≥ 10°).", ["Quadro pontilhado"], "Baixa", "Condicional", "Pacientes leves apresentam resposta superior à tDCS.", tol_tdcs),
            mod_tipo="tdcs",
        ),
        "tdcs_sensorial_s1": make_mod(
            protocolo_id="RM02-S1", tecnica="tDCS Anódica — S1 CP3/CP4 Ipsilesional (Koo et al., 2018)", modalidade_sigla="tDCS S1",
            alvo="Ânodo CP3/CP4 ipsilesional + Cátodo Fp2/Fp1 (25 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min (eletrodos 25 cm²)", sessoes="10 sessões associadas à estimulação sensorial",
            escala_recomendada="FMA-UE Subescala Sensorial (Seção II)", meta_melhora="+3,4 pontos sensoriais / +4,5 pts rNSA",
            tamanho_efeito=0.54, evidencia="Nível B — Evidência em recuperação sensorial (Chen 2023)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_KOO_2018, meta_analise=REF_CHEN_2023,
            mcid_valor=3.4, mcid_label="+3,4 pontos sensoriais", cohen_d_valor=0.54, cohen_d_interp="Moderado",
            estudo_referencia="Koo et al. (2018)", efeito_resumo="+4,5 pts na rNSA após 10 sessões",
            escalas_detalhadas=[scale_fma_sens],
            cadeia_sequencial=[
                make_chain_step(1, "RM02-PS1-1", "Protocolo Inicial — tDCS Anódica S1 CP3/CP4", "tDCS Anódica S1 CP3/CP4 (Koo et al., 2018)", "tDCS S1", "CP3/CP4 ipsilesional + Fp2/Fp1 (25 cm²)", "1,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="+4,5 pts rNSA", referencia="Koo et al. (2018) · DOI: 10.1097/PHM.0000000000000910", fase_etapa="inicial"),
                make_chain_step(2, "RM02-PS1-2", "Próximo Protocolo (Linha Pontilhada) — tDCS Dual S1", "tDCS Dual S1 Bilateral (Chong et al., 2024)", "tDCS Bilateral S1", "2 cm posterior a C3/C4 bilateral (25 cm²)", "2,0 mA | 20 min", sessoes="20 sessões", efeito_esperado="+11,1 pts FMA-UE", referencia="Chong et al. (2024) · DOI: 10.1111/cns.14530", linha_fluxograma="pontilhada", fase_etapa="sequencia"),
                make_chain_step(3, "RM02-ALT2", "Seção de Ajustes — taVNS Auricular (Linha Pontilhada)", "taVNS Auricular Esquerda (Wang et al., 2024)", "taVNS", "Concha da orelha esquerda", "500 µs | 25 Hz | limiar até 10 mA | 60 min", sessoes="15 sessões", efeito_esperado="+10,6 pts FMA-UE", referencia="Wang et al. (2024) · DOI: 10.3389/fnins.2024.1346634", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
            ],
            ajuste_parametros=adj_tdcs, falha_terapeutica=falha_tdcs_mod, sessoes_ajuste=sa_tdcs,
            notas_clinicas="Associar à estimulação sensorial periférica ou treino tátil discriminativo; após o protocolo dual S1 sem resposta, seguir para a Seção de Ajustes com taVNS auricular antes de concluir falha terapêutica.",
            audit_meta=_audit("Moderada", "Metanálise sensorial (Chen et al., 2023).", "Consistência favorável em estimulação somatossensorial.", ["Risco de viés"], "Moderada", "Condicional", "Titular corrente para 2 mA e 30 min.", tol_tdcs),
            mod_tipo="tdcs",
        ),
        "tdcs_negligencia": make_mod(
            protocolo_id="RM02-PPC", tecnica="tDCS Anódica — Córtex Parietal Posterior P4/P3 (Bang et al., 2015)", modalidade_sigla="tDCS PPC",
            alvo="Ânodo P4 + Cátodo P3 no Córtex Parietal Posterior (35 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min (eletrodos 35 cm²)", sessoes="15 sessões combinadas a feedback visual",
            escala_recomendada="Teste de Cancelamento de Estrelas (BIT — 0 a 54)", meta_melhora="Ganho ≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (Bang et al., 2015: -6,0 mm bissecção)",
            tamanho_efeito=0.50, evidencia="Nível B — Eficácia clínica (Fan et al., 2017)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_BANG_2015, meta_analise=REF_FAN_2017,
            mcid_valor=5.0, mcid_label="≥ +5,0 estrelas no Cancelamento de Estrelas (0–54)", cohen_d_valor=0.50, cohen_d_interp="Moderado",
            estudo_referencia="Bang et al. (2015)", efeito_resumo="-6,0 mm na bissecção de linhas após 15 sessões (acompanhamento quantitativo pelo Teste de Cancelamento de Estrelas)",
            escalas_detalhadas=[scale_star_cancel_tdcs],
            cadeia_sequencial=[
                make_chain_step(
                    1, "RM02-PPC-1", "Protocolo Inicial — tDCS Anódica P4 / P3", "tDCS Anódica P4 / Cátodo P3 (Bang et al., 2015)",
                    "tDCS PPC", "Ânodo P4 + Cátodo P3 (35 cm²)", "1,0 mA | 20 min", sessoes="15 sessões",
                    efeito_esperado="-6,0 mm bissecção de linhas após 15 sessões", referencia="Bang et al. (2015) · DOI: 10.1589/jpts.27.2759", fase_etapa="inicial",
                    calc_meta={
                        "mcid_valor": 5.0,
                        "mcid_label": "≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (0–54)",
                        "meta_texto": "Ganho ≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (Bang et al., 2015: -6,0 mm bissecção)",
                        "estudo_referencia": "Bang et al. (2015) — tDCS Anódica P4 / Cátodo P3",
                        "efeito_esperado_resumo": "-6,0 mm na bissecção de linhas após 15 sessões (avaliação na calculadora pelo Teste de Cancelamento de Estrelas)",
                    },
                ),
                make_chain_step(
                    2, "RM02-PPC-2", "Próximo Protocolo — tDCS P6 / FP1", "tDCS Anódica P6 / Cátodo FP1 (Làdavas et al., 2015)",
                    "tDCS PPC", "Ânodo P6 + Cátodo FP1 (35 cm²)", "2,0 mA | 20 min", sessoes="10 sessões",
                    efeito_esperado="+19 pts na bateria BIT", referencia="Làdavas et al. (2015) · DOI: 10.3233/RNN-140464", fase_etapa="sequencia",
                    calc_meta={
                        "mcid_valor": 5.0,
                        "mcid_label": "≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (BIT)",
                        "meta_texto": "Ganho ≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (Làdavas et al., 2015: +19 pts BIT)",
                        "estudo_referencia": "Làdavas et al. (2015) — tDCS Anódica P6 / Cátodo FP1",
                        "efeito_esperado_resumo": "+19 pontos na bateria BIT após 10 sessões",
                    },
                ),
                make_chain_step(
                    3, "RM02-PPC-3", "Próximo Protocolo (Linha Pontilhada) — tDCS Catódica P3 / Cz", "tDCS Catódica P3 / Ânodo Cz (Yi et al., 2016)",
                    "tDCS Catódica PPC", "Cátodo P3 + Ânodo Cz (25 cm²)", "2,0 mA | 30 min", sessoes="15 sessões",
                    efeito_esperado="+7,0 pontos no teste de cancelamento de estrelas", referencia="Yi et al. (2016) · DOI: 10.5535/arm.2016.40.2.223", linha_fluxograma="pontilhada", fase_etapa="sequencia",
                    calc_meta={
                        "mcid_valor": 7.0,
                        "mcid_label": "≥ +7,0 pontos no Teste de Cancelamento de Estrelas (Yi et al., 2016)",
                        "meta_texto": "Aumento esperado de +7,0 pontos no Teste de Cancelamento de Estrelas após 15 sessões",
                        "estudo_referencia": "Yi et al. (2016) — tDCS Catódica P3 / Ânodo Cz",
                        "efeito_esperado_resumo": "Aumento de +7,0 pontos no teste de cancelamento de estrelas após 15 sessões",
                    },
                ),
            ],
            ajuste_parametros=adj_tdcs, falha_terapeutica=falha_tdcs_mod, sessoes_ajuste=sa_tdcs,
            notas_clinicas="Aplicar simultaneamente a treino visuoespacial e feedback visual.",
            audit_meta=_audit("Moderada", "Metanálise heminegligência (Fan et al., 2017).", "Simultaneidade ao treino visuoespacial potencializa resposta.", ["Risco de viés"], "Moderada", "Condicional", "Reequilíbrio parietal inter-hemisférico.", tol_tdcs),
            mod_tipo="tdcs",
        ),
    }

    arvore_rtms = {
        "roadmap_id": "RM01",
        "titulo_fluxograma": "AVC Membro Superior — rTMS / iTBS / rPMS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante do uso do membro superior nas AVDs (MAL-Brazil)?",
                "subtitulo": "Selecione o principal fator limitante conforme a avaliação funcional.",
                "opcoes": [
                    {"id": "perda_sinergia", "rotulo": "Perda de sinergia", "criterio": "FMA-UE Seção III (36 pts)", "descricao": "Comprometimento de sinergias flexoras e extensoras.", "proxima_etapa": "pem_triage"},
                    {"id": "espasticidade", "rotulo": "Espasticidade", "criterio": "Escala de Ashworth Modificada (EAM)", "descricao": "Hipertonia espástica limitando alcance e preensão.", "proxima_etapa": "pem_triage"},
                    {"id": "fraqueza", "rotulo": "Fraqueza muscular", "criterio": "Escala MRC (Medical Research Council)", "descricao": "Paresia proximal ou distal de membro superior.", "proxima_etapa": "pem_triage"},
                    {"id": "disfuncao_motora", "rotulo": "Disfunção motora", "criterio": "FMA-UE Seções III-IV (66 pts)", "descricao": "Déficit global de coordenação e controle motor.", "proxima_etapa": "pem_triage"},
                    {"id": "sensorial", "rotulo": "Disfunção sensorial", "criterio": "FMA-UE Seção II (12 pts)", "descricao": "Hipoestesia ou déficit proprioceptivo no membro afetado.", "proxima_etapa": "alvo_sensorial"},
                    {"id": "negligencia", "rotulo": "Heminegligência", "criterio": "Teste de Cancelamento de Estrelas (BIT)", "descricao": "Desatenção espacial unilateral para o hemicorpo afetado.", "protocolo_alvo": "negligencia"},
                ],
            },
            "alvo_sensorial": {
                "pergunta": "Qual é o alvo cortical indicado para a disfunção sensorial?",
                "subtitulo": "A disfunção sensorial pode seguir pelo Córtex Motor Primário (M1) ou diretamente pelo Córtex Somatossensorial Primário (S1).",
                "opcoes": [
                    {"id": "sensorial_m1", "rotulo": "Córtex Motor Primário (M1)", "criterio": "Rota motora-sensorial", "descricao": "Avaliar integridade corticoespinhal via PEM.", "proxima_etapa": "pem_triage"},
                    {"id": "sensorial_s1", "rotulo": "Córtex Somatossensorial Primário (S1)", "criterio": "3 cm posterior a C3/C4 (via PEM)", "descricao": "Estimulação direta de S1 guiada pelo hotspot motor.", "proxima_etapa": "lesao_s1"},
                ],
            },
            "pem_triage": {
                "pergunta": "Há presença de Potencial Evocado Motor (PEM) no membro superior afetado?",
                "subtitulo": "A presença de PEM confirma integridade corticoespinhal e orienta a escolha em M1.",
                "opcoes": [
                    {"id": "pem_sim", "rotulo": "SIM — PEM Presente", "criterio": "Resposta motora evocada presente no lado afetado", "descricao": "Seguir para estratificação pela FMA-UE (> 35 pts).", "proxima_etapa": "gravidade_fma"},
                    {"id": "pem_nao", "rotulo": "NÃO — PEM Ausente", "criterio": "Sem resposta motora evocada no lado afetado", "descricao": "Confirmar PEM contralesional antes de avaliar lesão pré-frontal.", "proxima_etapa": "lesao_m1"},
                ],
            },
            "gravidade_fma": {
                "pergunta": "O paciente apresenta comprometimento motor leve (> 35 pontos na FMA-UE)?",
                "subtitulo": "Ponto de corte de gravidade motora em M1 com PEM presente.",
                "opcoes": [
                    {"id": "fma_maior_35", "rotulo": "SIM — FMA-UE > 35 pts", "criterio": "Comprometimento motor leve", "descricao": "Inicia por HF-rTMS 10 Hz M1 ipsilesional (Guo et al., 2016).", "protocolo_alvo": "fraqueza"},
                    {"id": "fma_menor_35", "rotulo": "NÃO — FMA-UE ≤ 35 pts", "criterio": "Comprometimento moderado a grave", "descricao": "Inicia pelo protocolo rTMS Bilateral M1 (1 Hz contralesional + 10 Hz ipsilesional, Long et al., 2018).", "protocolo_alvo": "rtms_m1_grave"},
                ],
            },
            "lesao_m1": {
                "pergunta": "Há lesão cortical extensa no giro pré-frontal?",
                "subtitulo": "Critério neuroanatômico em M1 quando PEM está ausente.",
                "opcoes": [
                    {"id": "lesao_prefrontal_sim", "rotulo": "SIM — Lesão pré-frontal extensa", "criterio": "Neuroimagem confirma extensa lesão pré-frontal", "descricao": "Inicia por HF-rTMS 10 Hz em M1 CONTRALESIONAL (Wang et al., 2022).", "protocolo_alvo": "sem_pem"},
                    {"id": "lesao_prefrontal_nao", "rotulo": "NÃO — Sem lesão pré-frontal extensa", "criterio": "Córtex pré-frontal/motor poupado", "descricao": "Inicia por HF-rTMS 10 Hz em M1 IPSILESIONAL (Guo et al., 2016).", "protocolo_alvo": "sem_pem_ipsilesional"},
                ],
            },
            "lesao_s1": {
                "pergunta": "Há lesão cortical extensa no giro pós-frontal?",
                "subtitulo": "Define entre estimulação direta de S1 ou redirecionamento direto para o ramo M1 ipsilesional.",
                "opcoes": [
                    {"id": "lesao_pos_nao", "rotulo": "NÃO — Sem lesão pós-frontal extensa", "criterio": "S1 viável", "descricao": "HF-rTMS 10 Hz a 120% LMR, 3 cm posterior a M1 (Zanona et al., 2022).", "protocolo_alvo": "sensorial"},
                    {"id": "lesao_pos_sim", "rotulo": "SIM — Lesão pós-frontal extensa", "criterio": "S1 comprometido — rota M1 ipsilesional", "descricao": "Inicia diretamente por HF-rTMS 10 Hz em M1 ipsilesional (Guo et al., 2016) com escalonamento para Bilateral e cTBS + Cerebelo.", "protocolo_alvo": "sem_pem_ipsilesional"},
                ],
            },
        },
        "ajuste_parametros": adj_rtms,
        "protocolo_alternativo": {
            "nome": "Seção de Ajustes (Linha Pontilhada) — iTBS M1 + rPMS no Sulco do Nervo Radial (Chang et al., 2024)",
            "tecnica": "iTBS M1 + rPMS Periférica", "alvo": "M1 ipsilesional + sulco do nervo radial no úmero (extensor radial do carpo)",
            "parametros": "iTBS (80% LMA ou 70% LMR, 1.200 pulsos) seguido após 10 min por rPMS (sulco do nervo radial, 3 pulsos 50 Hz / 5 Hz, 2 s ON / 8 s OFF, 600 pulsos)",
            "observacoes": "A sessão de iTBS é separada por 10 minutos da rPMS; bobina perpendicular ao músculo com contração visível.",
        },
        "protocolo_alternativo_2": {
            "nome": "Seção de Ajustes (Linha Pontilhada) — iTBS Cerebelar Ipsilesional (Chen et al., 2021)",
            "tecnica": "iTBS Cerebelar", "alvo": "Cerebelo ipsilesional (3 cm lateral ao ínion)",
            "parametros": "iTBS 600 pulsos | 80% LMA | bobina parabólica ou duplo cone",
            "observacoes": "Etapa da seção de Ajustes após HF-rTMS contralesional em pacientes sem PEM e com lesão pré-frontal extensa.",
        },
        "falha_terapeutica": {
            "id": "RM01-FALHA",
            "titulo": "Critérios de Falha Terapêutica em rTMS Pós-AVC (Membro Superior)",
            "criterios_definicao": "Ausência de resposta clínica mesmo após percorrer os protocolos sequenciais e o quadro de Ajustes indicado para a rota.",
            "descricao": "Reavaliar adesão às terapias convencionais associadas e confirmar exclusão técnica contralesional antes de concluir falha.",
            "condutas": [
                "Reavaliar integridade estrutural, medicações sedativas e adequação da terapia motora/ocupacional associada.",
                "Considerar a modalidade tDCS / taVNS para Membro Superior caso ainda não utilizada.",
                "Se dor neuropática ou nociceptiva for o obstáculo predominante, seguir o fluxo de Dor Neuropática Crônica.",
            ],
        },
    }

    arvore_tdcs = {
        "roadmap_id": "RM02",
        "titulo_fluxograma": "AVC Membro Superior — tDCS / taVNS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante do membro superior nas AVDs (tDCS)?",
                "subtitulo": "Selecione o fator limitante predominante para estimulação elétrica.",
                "opcoes": [
                    {"id": "disfuncao_motora", "rotulo": "Disfunção motora", "criterio": "FMA-UE Seções III-IV", "descricao": "Comprometimento motor em M1.", "proxima_etapa": "lesao_tdcs_m1"},
                    {"id": "espasticidade", "rotulo": "Espasticidade", "criterio": "EAM", "descricao": "Hipertonia em membro superior.", "proxima_etapa": "lesao_tdcs_m1"},
                    {"id": "sensorial", "rotulo": "Disfunção sensorial", "criterio": "FMA-UE Seção II", "descricao": "Déficit somatossensorial.", "proxima_etapa": "alvo_sensorial_tdcs"},
                    {"id": "negligencia", "rotulo": "Heminegligência", "criterio": "Teste de Cancelamento de Estrelas (BIT)", "descricao": "Rota para Córtex Parietal Posterior (P3/P4).", "protocolo_alvo": "tdcs_negligencia"},
                ],
            },
            "alvo_sensorial_tdcs": {
                "pergunta": "Qual alvo cortical utilizar para Disfunção Sensorial na tDCS?",
                "subtitulo": "Escolha entre M1 e S1 conforme avaliação funcional.",
                "opcoes": [
                    {"id": "tdcs_sens_m1", "rotulo": "Córtex Motor Primário (M1)", "criterio": "Avaliar lesão pré-frontal", "descricao": "Segue fluxograma motor M1.", "proxima_etapa": "lesao_tdcs_m1"},
                    {"id": "tdcs_sens_s1", "rotulo": "Córtex Somatossensorial (S1 — CP3/CP4)", "criterio": "CP3/CP4 ipsilesional", "descricao": "Protocolos S1 tDCS.", "protocolo_alvo": "tdcs_sensorial_s1"},
                ],
            },
            "lesao_tdcs_m1": {
                "pergunta": "Há lesão cortical no giro pré-frontal?",
                "subtitulo": "Decisão anatômica em M1 para posicionamento anódico.",
                "opcoes": [
                    {"id": "tdcs_pf_nao", "rotulo": "NÃO — Sem lesão pré-frontal", "criterio": "Córtex motor/pré-motor íntegro", "descricao": "Inicia por tDCS anódica M1 ipsilesional (Kashoo et al., 2022).", "protocolo_alvo": "tdcs_m1_pf_nao"},
                    {"id": "tdcs_pf_sim", "rotulo": "SIM — Lesão pré-frontal", "criterio": "Avaliar extensão mínima de dedos/punho", "descricao": "Triagem motora de 10 graus.", "proxima_etapa": "extensao_dedos"},
                ],
            },
            "extensao_dedos": {
                "pergunta": "O paciente apresenta comprometimento motor leve/moderado (extensão ativa ≥ 10° de polegar, dedos e punho)?",
                "subtitulo": "Critério funcional de triagem motora para tDCS.",
                "opcoes": [
                    {"id": "ext_nao", "rotulo": "NÃO — Extensão < 10°", "criterio": "Grave", "descricao": "Inicia por tDCS anódica contralesional (Klomjai et al., 2022).", "protocolo_alvo": "tdcs_m1_pf_sim_ext_nao"},
                    {"id": "ext_sim", "rotulo": "SIM — Extensão ≥ 10°", "criterio": "Leve / Moderado", "descricao": "Inicia por tDCS anódica pré-motora ipsilesional (Cunningham et al., 2015).", "protocolo_alvo": "tdcs_m1_pf_sim_ext_sim"},
                ],
            },
        },
        "ajuste_parametros": adj_tdcs,
        "protocolo_alternativo": {
            "nome": "Seção de Ajustes (Linha Pontilhada) — tDCS Cerebelar Contralesional (Gong et al., 2023)",
            "tecnica": "tDCS Cerebelar", "alvo": "Cerebelo contralesional (3 cm lateral ao ínion, 35 cm²)", "parametros": "2,0 mA | 20 min (titular para 30 min)",
            "observacoes": "Quadro pontilhado (+10,7 pts FMA-UE).",
        },
        "protocolo_alternativo_2": {
            "nome": "Seção de Ajustes (Linha Pontilhada) — taVNS Auricular (Wang et al., 2024)",
            "tecnica": "taVNS Auricular", "alvo": "Concha da orelha esquerda", "parametros": "500 µs | 25 Hz | 30 s ON / 30 s OFF | até 10 mA | 60 min",
            "observacoes": "Quadro pontilhado (+10,6 pts FMA-UE).",
        },
        "falha_terapeutica": {
            "id": "RM02-FALHA",
            "titulo": "Critérios de Falha Terapêutica em tDCS Pós-AVC (Membro Superior)",
            "criterios_definicao": "Ausência de resposta funcional relevante após ciclo com parâmetros otimizados (2 mA, 30 min, > 15 sessões simultâneas à terapia) e conclusão da seção de Ajustes.",
            "descricao": "Reavaliar resposta em todos os domínios após 5 sessões e completar etapas previstas.",
            "condutas": [
                "Considerar transição para rTMS/iTBS para Membro Superior caso não haja contraindicação magnética.",
                "Investigar dor neuropática ou nociceptiva oculta como fator limitante e seguir o fluxo de Dor Neuropática Crônica se necessário.",
            ],
        },
    }

    obs_rtms = _avc_shared_observations(
        "RM01", "a bobina", "membro superior", "rtms", "", "", ["sem_pem"],
    ) + [
        make_obs(
            "RM01-PEM-DOI",
            "Como testar o Potencial Evocado Motor (PEM) e procedimento técnico padronizado.",
            "step", categoria="clinica", etapa_ids=["pem_triage"], modalidades_tipo=["rtms"],
            referencia_doi=PEM_GUIDE_DOI, referencia_rotulo=PEM_GUIDE_LABEL,
        ),
        make_obs(
            "RM01-N05-CONTRALESIONAL",
            "Na ausência de PEM no hemisfério lesionado, testar o hemisfério contralesional para confirmar inervação ipsilesional e excluir limitação técnica do equipamento.",
            "step", categoria="neurofisiologia", etapa_ids=["pem_triage", "lesao_m1"], opcao_ids=["pem_nao"],
            modalidades_tipo=["rtms"], referencia_doi=PEM_GUIDE_DOI, referencia_rotulo=PEM_GUIDE_LABEL, severidade="warning",
        ),
        make_obs(
            "RM01-N22-S1-3CM",
            "Regra de Aplicação: para estimular S1, aplicar a bobina 3 cm posterior ao córtex motor primário, preferencialmente identificado pelo PEM.",
            "alvo", categoria="anatomia", protocolo_ids=["sensorial"], modalidades_tipo=["rtms"],
            referencia_doi=PEM_GUIDE_DOI, referencia_rotulo=PEM_GUIDE_LABEL,
        ),
        make_obs(
            "RM01-N11-CEREBELO-PEM",
            "Bobinas parabólicas e duplo cone são as mais indicadas para a estimulação profunda do cerebelo.",
            "stage", categoria="equipamento", protocolo_ids=["sem_pem"],
            estagios=["alt1"], modalidades_tipo=["rtms"],
        ),
        make_obs(
            "RM01-N11-CEREBELO-IPSI",
            "Bobinas parabólicas e duplo cone são as mais indicadas para a estimulação profunda do cerebelo.",
            "stage", categoria="equipamento", protocolo_ids=["sem_pem_ipsilesional"],
            estagios=["alt2"], modalidades_tipo=["rtms"],
        ),
        make_obs(
            "RM01-N11-CEREBELO-S1",
            "Bobinas parabólicas e duplo cone são as mais indicadas para a estimulação profunda do cerebelo.",
            "stage", categoria="equipamento", protocolo_ids=["sensorial"],
            estagios=["alt3"], modalidades_tipo=["rtms"],
        ),
        make_obs(
            "RM01-RPMS-REGRAS",
            "Regras operacionais de rPMS: em músculos fracos (deltoide, extensores do punho, pronador redondo) usar modo intermitente (3 pulsos a 50 Hz repetidos a 5 Hz, 2 s ON / 8 s OFF, 600 pulsos por músculo); em músculos espásticos (flexores do punho, bíceps braquial, peitoral maior) usar modo contínuo (600 pulsos sem pausas); posicionar bobina perpendicular às fibras gerando contração visível.",
            "stage", categoria="parametros", protocolo_ids=["fraqueza", "perda_sinergia", "espasticidade", "disfuncao_motora", "rtms_m1_grave"],
            estagios=["alt2"], modalidades_tipo=["rtms"],
        ),
        make_obs(
            "RM01-MRC-FORCA",
            "Medida de desfecho recomendada para força muscular focal: Medical Research Council (MRC, graus 0–5); para acompanhamento longitudinal comparável aos ensaios clínicos de referência do protocolo (Guo et al., 2016; Long et al., 2018), utilizar em conjunto a FMA-UE (MCID +5,0 pontos).",
            "scale", categoria="avaliacao", opcao_ids=["fraqueza"], modalidades_tipo=["rtms"],
        ),
    ]

    obs_tdcs = _avc_shared_observations(
        "RM02", "o eletrodo", "membro superior", "tdcs", "", "", ["tdcs_m1_pf_sim_ext_nao", "tdcs_m1_pf_sim_ext_sim"],
    ) + [
        make_obs(
            "RM02-LEVES-RESP",
            "Pacientes com comprometimento motor leve (ex.: extensão ativa ≥ 10° de punho/dedos) tendem a ser mais responsivos à tDCS.",
            "step", categoria="prognostico", etapa_ids=["extensao_dedos"], opcao_ids=["ext_sim"], modalidades_tipo=["tdcs"],
        ),
    ]

    return {
        "id": cid,
        "condicao": "Acidente Vascular Cerebral — Membro Superior",
        "eixo": "Doenças Cerebrovasculares",
        "roadmap_id": "RM01",
        "svg_file": "RM01.svg",
        "fatores_limitantes": [
            {"id": "perda_sinergia", "nome": "Perda de sinergia", "instrumento_sugerido": "FMA-UE Seção III (36 pts)", "descricao": "Comprometimento de sinergias motoras no membro superior."},
            {"id": "espasticidade", "nome": "Espasticidade", "instrumento_sugerido": "Escala de Ashworth Modificada", "descricao": "Aumento do tônus velocidade-dependente."},
            {"id": "fraqueza", "nome": "Fraqueza muscular", "instrumento_sugerido": "Escala MRC", "descricao": "Déficit de força no membro parético."},
            {"id": "disfuncao_motora", "nome": "Disfunção motora", "instrumento_sugerido": "FMA-UE Seção III-IV (66 pts)", "descricao": "Comprometimento motor global do membro superior."},
            {"id": "sensorial", "nome": "Disfunção sensorial", "instrumento_sugerido": "FMA-UE Seção II (12 pts)", "descricao": "Alteração tátil ou proprioceptiva (M1 ou S1)."},
            {"id": "negligencia", "nome": "Heminegligência", "instrumento_sugerido": "Teste de Cancelamento de Estrelas (BIT)", "descricao": "Heminegligência espacial unilateral (PPC)."},
        ],
        "arvore_algoritmo": arvore_rtms,
        "arvores_por_modalidade": {"rtms": arvore_rtms, "tdcs": arvore_tdcs},
        "observacoes_contextuais": obs_rtms + obs_tdcs,
        "modalidades": modalidades,
        "tags_busca": tags,
    }


def _build_avc_mobilidade():
    cid = "avc-mobilidade"
    tags = {
        "siglas": ["AVC", "AVE", "MI", "MMII", "M1", "S1", "PPC", "BBS", "TC10m", "10MWT", "FMA-LE", "SCT", "BIT"],
        "coordenadas_10_20": ["Cz", "C3", "C4", "P3", "P4", "F5", "CP3", "CP4"],
        "alvos_anatomicos": ["Cerebelo", "Córtex Motor Primário (M1)", "Vértice Craniano (Cz)", "Córtex Somatossensorial Primário (S1)", "Córtex Parietal Posterior (PPC)"],
        "sinonimos_en": ["stroke", "gait", "mobility", "walking speed", "balance", "falls risk", "lower limb", "locomotion", "star cancellation test"],
        "sintomas_pt": ["marcha", "mobilidade", "equilíbrio", "quedas", "passo", "velocidade de caminhada", "deambulação", "membros inferiores", "heminegligência"],
        "escalas": ["BBS", "Berg", "Mini-BESTest", "10MWT", "TC10m", "FMA-LE", "DGI", "Cancelamento de Estrelas", "Star Cancellation", "BIT"],
        "tecnicas": ["rTMS", "iTBS", "rPMS", "tDCS", "taVNS"],
    }
    tol_mob_rtms = _tol_profile(
        "A intensidade do estimulador pode ser reduzida inicialmente em caso de desconforto e ajustada progressivamente conforme a tolerância do paciente até o valor previsto.",
        "Usar bobina circular ou parabólica para M1 MMII e parabólica/duplo cone no cerebelo; na ausência de PEM no hemisfério lesionado, definir o LMR pelo hemisfério não lesionado.",
        "Medicações em uso (não interromper terapias medicamentosas) e ciclos com 10 ou mais sessões para maior tamanho de efeito.",
    )
    tol_mob_tdcs = _tol_profile(
        "Monitorar desconforto cutâneo e hidratar uniformemente as esponjas; em caso de incômodo facial na montagem cerebelar, deslocar o cátodo do músculo bucinador para o músculo deltoide direito.",
        "Quando tolerado em protocolos tDCS compatíveis, titular para 2 mA e 30 minutos simultaneamente à tarefa locomotora.",
        "Cuidados cutâneos padrão, manutenção das medicações e ciclos > 15 sessões.",
    )

    scale_bbs = make_scale("bbs", "Escala de Equilíbrio de Berg (BBS)", "BBS", "aumento", "+5,0 pontos na Escala de Equilíbrio de Berg (MCID)", 0.58, placeholder="Ex: 38", min_val=0, max_val=56, mcid_valor=5.0, mcid_label="+5,0 pontos na BBS")
    scale_10mwt = make_scale("tc10m", "Teste de Caminhada de 10 Metros (TC10m / 10MWT)", "TC10m / 10MWT", "reducao", "Redução ≥ 1,5 s no tempo de caminhada (10MWT)", 0.50, placeholder="Ex: 18.0", min_val=1, max_val=120, mcid_valor=1.5, mcid_label="-1,5 s no TC10m")
    scale_fma_le = make_scale("fma_le", "Fugl-Meyer — Membro Inferior (FMA-LE)", "FMA-LE", "aumento", "+4,0 pontos na FMA-LE (ganho funcional de membro inferior)", 0.52, placeholder="Ex: 20", min_val=0, max_val=34, mcid_valor=4.0, mcid_label="+4,0 pontos FMA-LE")
    scale_star_cancel_rtms = make_scale(
        "star_cancellation", "Teste de Cancelamento de Estrelas (BIT — Star Cancellation Test)", "Cancelamento de Estrelas", "aumento",
        "Aumento esperado de +10,4 pontos (IC 95%: 8,0 a 12,7) após 10 sessões diárias (corte satisfatório ≥ +8,0 pontos)",
        0.54, placeholder="Ex: 32", min_val=0, max_val=54, mcid_valor=8.0,
        mcid_label="≥ +8,0 pontos (limite inferior do IC 95%: 8,0–12,7 · média +10,4 pts)",
    )
    scale_star_cancel_tdcs = make_scale(
        "star_cancellation", "Teste de Cancelamento de Estrelas (BIT — Star Cancellation Test)", "Cancelamento de Estrelas", "aumento",
        "Aumento ≥ +5,0 estrelas (0–54) no Teste de Cancelamento de Estrelas (ou ≥ +7,0 pontos na etapa catódica P3/Cz — Yi et al., 2016)",
        0.50, placeholder="Ex: 32", min_val=0, max_val=54, mcid_valor=5.0,
        mcid_label="≥ +5,0 estrelas no Cancelamento de Estrelas (0–54)",
    )

    mob_scales_map = {
        "equilibrio": ["bbs"],
        "equilibrio_tdcs": ["bbs"],
        "velocidade_marcha": ["tc10m"],
        "marcha_tdcs": ["tc10m"],
        "disfuncao_motora_mi": ["fma_le"],
        "fraqueza_tdcs": ["fma_le"],
        "sensorial_mi": ["fma_le"],
        "sensorial_tdcs_mi": ["fma_le"],
    }

    step_cer_p1 = make_chain_step(1, "RM03-CER-P1", "Protocolo Inicial — iTBS Cerebelar Contralateral", "iTBS Cerebelar Contralateral ao Lesionado (Koch et al., 2019)", "iTBS Cerebelar", "Hemisfério cerebelar contralateral ao hemisfério lesionado (bobina parabólica ou duplo cone)", "iTBS (2 sessões separadas por 5 min): 3 pulsos a 50 Hz repetidos a cada 200 ms (5 Hz), 2 s estímulo e 8 s pausa | 80% LMA | 1.200 pulsos", sessoes="15 sessões associadas à fisioterapia", efeito_esperado="+8,9 pts na Escala de Berg (BBS)", referencia="Koch et al. (2019) · DOI: 10.1001/jamaneurol.2018.3639", linha_fluxograma="solida", fase_etapa="inicial")
    step_cer_p2 = make_chain_step(2, "RM03-CER-P2", "Próximo Protocolo — LF-rTMS Cerebelar 1 Hz", "LF-rTMS Cerebelar Contralateral 1 Hz (Im et al., 2022)", "rTMS Inibitória (1 Hz)", "Hemisfério cerebelar contralateral ao lesionado (2 cm abaixo e 2 cm lateral ao ínion; bobina parabólica/duplo cone)", "1 Hz | 90% LMR | 900 pulsos", sessoes="10 sessões diárias associadas à fisioterapia", efeito_esperado="-4,4 s no Teste de Caminhada de 10 Metros (10MWT)", referencia="Im et al. (2022) · DOI: 10.5535/arm.22058", linha_fluxograma="solida", fase_etapa="sequencia")
    step_rpms_mob = make_chain_step(3, "RM03-ALT1", "Seção de Ajustes — rPMS Músculo Tibial Anterior (Linha Pontilhada)", "rPMS no Músculo Tibial Anterior e Músculos da Marcha (Beaulieu et al., 2015)", "rPMS Periférica", "Ventre do músculo tibial anterior afetado e demais músculos com déficit na marcha", "42% da saída máxima do estimulador | 2 s ON / 8 s OFF | 600 pulsos | 190 s (modo contínuo para músculos espásticos)", sessoes="Associar sempre a um protocolo de rTMS/TBS", efeito_esperado="+7,8° em dorsiflexão ativa do tornozelo", referencia="Beaulieu et al. (2015) · DOI: 10.1179/1074935714Z.0000000032", linha_fluxograma="pontilhada", fase_etapa="ajustes")
    step_m1_chr = make_chain_step(1, "RM03-M1-P1", "Protocolo Inicial — HF-rTMS 10 Hz M1 Tibial Anterior", "HF-rTMS 10 Hz M1 Tibial Anterior (Wang et al., 2024)", "HF-rTMS (10 Hz)", "Hotspot do músculo tibial anterior no hemisfério lesionado (via PEM ou Cz se PEM ausente; bobina circular/parabólica)", "10 Hz | 100% LMR | 2.000 pulsos (40 trens de 5 s com 35 s de intervalo)", sessoes="10 sessões associadas a ciclismo com feedback visual", efeito_esperado="+3,0 pts na FMA-LE após 10 sessões", referencia="Wang et al. (2024) · DOI: 10.1155/np/8737366", linha_fluxograma="solida", fase_etapa="inicial")
    step_m1_chr_seq = make_chain_step(2, "RM03-M1-P1-SEQ", "Próximo Protocolo — HF-rTMS 10 Hz M1 Tibial Anterior", "HF-rTMS 10 Hz M1 Tibial Anterior (Wang et al., 2024)", "HF-rTMS (10 Hz)", "Hotspot do músculo tibial anterior no hemisfério lesionado (via PEM ou Cz se PEM ausente; bobina circular/parabólica)", "10 Hz | 100% LMR | 2.000 pulsos (40 trens de 5 s com 35 s de intervalo)", sessoes="10 sessões associadas ao treino motor de MMII", efeito_esperado="+3,0 pts na FMA-LE após 10 sessões", referencia="Wang et al. (2024) · DOI: 10.1155/np/8737366", linha_fluxograma="solida", fase_etapa="sequencia")
    step_m1_acu = make_chain_step(2, "RM03-M1-P2", "Próximo Protocolo — LF-rTMS 1 Hz M1 Não Lesionado", "LF-rTMS 1 Hz M1 Não Lesionado (Zhang et al., 2024)", "LF-rTMS (1 Hz)", "Hotspot do tibial anterior no hemisfério não lesionado (via PEM ou Cz)", "1 Hz | 90% LMR | 1.000 pulsos", sessoes="20 sessões associadas ao treino de marcha", efeito_esperado="-0,3 s no TC10m e melhora de equilíbrio/simetria", referencia="Zhang et al. (2024) · DOI: 10.1016/j.jstrokecerebrovasdis.2024.107961", linha_fluxograma="solida", fase_etapa="sequencia")
    step_m1_acu_init = make_chain_step(1, "RM03-M1-P2", "Protocolo Inicial — LF-rTMS 1 Hz M1 Não Lesionado", "LF-rTMS 1 Hz M1 Não Lesionado (Zhang et al., 2024)", "LF-rTMS (1 Hz)", "Hotspot do tibial anterior no hemisfério não lesionado (via PEM ou Cz)", "1 Hz | 90% LMR | 1.000 pulsos", sessoes="20 sessões associadas ao treino de marcha", efeito_esperado="-0,3 s no TC10m e melhora de equilíbrio/simetria", referencia="Zhang et al. (2024) · DOI: 10.1016/j.jstrokecerebrovasdis.2024.107961", linha_fluxograma="solida", fase_etapa="inicial")

    adj_mob_rtms = {"titulo": "Ajustes de Tolerabilidade, Distribuição de Trens e Calibração (Mobilidade)", "tolerabilidade": "Reduzir inicialmente a intensidade em caso de desconforto e progredir gradualmente até a meta; na ausência de PEM MMII, definir LMR pelo lado não lesionado.", "dose_pulsos": "Ciclos com ≥ 10 sessões apresentam maior tamanho de efeito; em HF-rTMS M1 MMII, distribuir os 2.000 pulsos em 40 trens de 5 s com 35 s de intervalo visando maior segurança.", "calibracao_limiar": "Hotspot pelo PEM em pulso único; na ausência de PEM usar Cz. M1 MMII: bobina circular ou parabólica; Cerebelo: parabólica ou duplo cone."}
    adj_mob_tdcs = {"titulo": "Ajustes de Densidade e Montagem Alternativa em tDCS (Mobilidade)", "tolerabilidade": "Em desconforto facial na montagem cerebelar, deslocar o cátodo do músculo bucinador para o músculo deltoide direito.", "dose_pulsos": "Titular para 2 mA e 30 minutos quando tolerado; manter ciclos > 15 sessões simultâneos à terapia motora para maior efeito.", "calibracao_limiar": "Pacientes mais leves respondem melhor; estimulação simultânea à terapia potencializa o ganho funcional."}
    falha_mob_rtms = _falha_mod("Ausência de melhora clínica após 5 sessões com adesão confirmada e conclusão da sequência e seção de Ajustes.", "1. Revisar alvo anatômico (Cerebelo vs. M1 MMII) e calibração contralesional;\n2. Considerar modalidade tDCS / taVNS em Mobilidade Funcional;\n3. Se a dor limitar a mobilidade funcional, seguir o fluxo de Dor Neuropática Crônica.")
    falha_mob_tdcs = _falha_mod("Ausência de resposta funcional após conclusão dos protocolos otimizados (2 mA, 30 min) e da seção de Ajustes.", "1. Otimizar simultaneidade ao treino locomotor e titular 2 mA / 30 min;\n2. Considerar modalidade rTMS/iTBS em Mobilidade Funcional;\n3. Se dor limitar a marcha, seguir o fluxo de Dor Neuropática Crônica.")
    sa_mob_rtms = _sessoes_aj("Avaliar evolução clínica após 5 sessões com o protocolo indicado e adesão confirmada; ausência de melhora nos fatores limitantes indica resposta insatisfatória.", "", "Ao atingir platô funcional sustentado, interromper o ciclo intensivo e iniciar redução gradual da frequência.")
    sa_mob_tdcs = _sessoes_aj("Avaliar evolução clínica após 5 sessões simultâneas à terapia convencional; ausência de melhora indica resposta insatisfatória.", "", "Ao atingir platô funcional sustentado, interromper o ciclo intensivo e iniciar manutenção com redução gradual da frequência.")

    modalidades = {
        "equilibrio": make_mod(
            protocolo_id="RM03-CER", tecnica="iTBS Cerebelar Contralateral ao Lesionado (Koch et al., 2019)", modalidade_sigla="iTBS Cerebelar",
            alvo="Hemisfério cerebelar contralateral ao lesionado (bobina parabólica ou duplo cone)", frequencia="iTBS (50 Hz / 5 Hz)", intensidade="80% LMA",
            pulsos_duracao="1.200 pulsos (2 sessões separadas por 5 min; 2 s estímulo e 8 s pausa)", sessoes="15 sessões associadas à fisioterapia para equilíbrio e marcha",
            escala_recomendada="Escala de Berg (BBS) / TC10m / FMA-LE", meta_melhora="+5,0 pontos na BBS (+8,9 pts no estudo de referência)",
            tamanho_efeito=0.58, evidencia="Nível B — Evidência clínica favorável (Koch 2019 · Zeng 2024)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_KOCH_2019, meta_analise=REF_ZENG_2024,
            mcid_valor=5.0, mcid_label="+5,0 pontos na BBS", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Koch et al. (2019)", efeito_resumo="+8,9 pts na Escala de Equilíbrio de Berg (BBS)",
            escalas_detalhadas=[scale_bbs, scale_10mwt, scale_fma_le], escalas_por_fator=mob_scales_map,
            cadeia_sequencial=[step_cer_p1, step_cer_p2, step_rpms_mob],
            ajuste_parametros=adj_mob_rtms, falha_terapeutica=falha_mob_rtms, sessoes_ajuste=sa_mob_rtms,
            notas_clinicas="Rota cerebelar recebe pacientes priorizando Cerebelo ou redirecionados de M1 por lesão cortical extensa no giro pré-frontal. Associar fisioterapia direcionada; não suspender medicações.",
            audit_meta=_audit("Moderada", "Metanálise cerebelar em marcha e equilíbrio (Zeng et al., 2024).", "Evidência favorável para modulação cerebelar em equilíbrio e marcha.", ["Risco de viés"], "Moderada", "Condicional", "Reavaliação clínica seriada após 5 sessões com fisioterapia associada.", tol_mob_rtms),
        ),
        "velocidade_marcha": make_mod(
            protocolo_id="RM03-M1-CHR", tecnica="HF-rTMS (10 Hz) — M1 Tibial Anterior (Wang et al., 2024)", modalidade_sigla="HF-rTMS M1 MMII",
            alvo="Hotspot do músculo tibial anterior no hemisfério lesionado (via PEM ou Cz; bobina circular/parabólica)", frequencia="10 Hz", intensidade="100% LMR",
            pulsos_duracao="2.000 pulsos (40 trens de 5 s com 35 s de intervalo)", sessoes="10 sessões associadas a terapias para mobilidade e marcha",
            escala_recomendada="TC10m / BBS / FMA-LE (conforme fator limitante)", meta_melhora="-1,5 s no TC10m (+3,0 pts FMA-LE)",
            tamanho_efeito=0.50, evidencia="Nível B — Evidência clínica favorável (Jia 2025: ≥10 sessões)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_WANG_2024_MOB, meta_analise=REF_JIA_2025,
            mcid_valor=1.5, mcid_label="-1,5 s no TC10m", cohen_d_valor=0.50, cohen_d_interp="Moderado",
            estudo_referencia="Wang et al. (2024)", efeito_resumo="+3,0 pts na FMA-LE e estabilidade de marcha pós-AVC",
            escalas_detalhadas=[scale_10mwt, scale_bbs, scale_fma_le], escalas_por_fator=mob_scales_map,
            cadeia_sequencial=[step_m1_chr, step_m1_acu, step_rpms_mob],
            ajuste_parametros=adj_mob_rtms, falha_terapeutica=falha_mob_rtms, sessoes_ajuste=sa_mob_rtms,
            notas_clinicas="Indicado em lesão subaguda/crônica (> 1 mês) sem lesão pré-frontal extensa. Associar à fisioterapia direcionada à marcha; não interromper medicações.",
            audit_meta=_audit("Moderada", "Metanálise (Jia et al., 2025) em marcha/equilíbrio com ≥ 10 sessões.", "Análise por subgrupos de dose de sessões.", ["Subgrupo ≥10 sessões"], "Moderada", "Condicional", "Usar bobina circular ou parabólica para representação de MMII.", tol_mob_rtms),
        ),
        "rtms_m1_aguda": make_mod(
            protocolo_id="RM03-M1-ACU", tecnica="LF-rTMS (1 Hz) — M1 Não Lesionado em Fase Aguda (Zhang et al., 2024)", modalidade_sigla="LF-rTMS Aguda",
            alvo="Hotspot do tibial anterior no hemisfério não lesionado (via PEM ou Cz)", frequencia="1 Hz", intensidade="90% LMR",
            pulsos_duracao="1.000 pulsos | Fase aguda (≤ 1 mês)", sessoes="20 sessões associadas ao treino de marcha",
            escala_recomendada="FMA-LE / BBS / TC10m (conforme fator limitante)", meta_melhora="-0,3 s no TC10m / simetria precoce",
            tamanho_efeito=0.52, evidencia="Nível B — Evidência clínica favorável em fase aguda (Zhang 2024)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_ZHANG_2024_MOB, meta_analise=REF_SU_2025,
            mcid_valor=4.0, mcid_label="+4,0 pontos FMA-LE", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Zhang et al. (2024)", efeito_resumo="Melhora em marcha e simetria na fase aguda",
            escalas_detalhadas=[scale_fma_le, scale_bbs, scale_10mwt], escalas_por_fator=mob_scales_map,
            cadeia_sequencial=[step_m1_acu_init, step_m1_chr_seq, step_rpms_mob],
            ajuste_parametros=adj_mob_rtms, falha_terapeutica=falha_mob_rtms, sessoes_ajuste=sa_mob_rtms,
            notas_clinicas="Indicado em lesão aguda (≤ 1 mês) sem lesão cortical extensa pré-frontal. Associar treino de marcha convencional.",
            audit_meta=_audit("Moderada", "Metanálise iTBS/rTMS em MMII pós-AVC (Su et al., 2025).", "Heterogeneidade moderada em ensaios de fase aguda.", ["Heterogeneidade"], "Moderada", "Condicional", "Indicado em lesão aguda ≤ 1 mês com progressão sequencial para HF-rTMS M1 se resposta insatisfatória.", tol_mob_rtms),
        ),
        "rtms_ppc_mob": make_mod(
            protocolo_id="RM03-PPC", tecnica="HF-rTMS (10 Hz) — Córtex Parietal Posterior Ipsilesional (Kim et al., 2013)", modalidade_sigla="rTMS PPC",
            alvo="Córtex Parietal Posterior (P3/P4) ipsilesional", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="1.000 pulsos (20 trens × 50 pulsos, 55 s IIT)", sessoes="10 sessões diárias",
            escala_recomendada="Teste de Cancelamento de Estrelas (BIT — 0 a 54)", meta_melhora="Aumento de 10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias",
            tamanho_efeito=0.54, evidencia="Nível B — Quadro sólido em Mobilidade", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_KIM_2013, meta_analise=REF_FAN_2017,
            mcid_valor=8.0, mcid_label="≥ +8,0 pontos (IC 95%: 8,0 a 12,7 · média +10,4 pts)", cohen_d_valor=0.54, cohen_d_interp="Moderado",
            estudo_referencia="Kim et al. (2013)", efeito_resumo="Aumento de 10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
            ic_min=8.0, ic_max=12.7,
            escalas_detalhadas=[scale_star_cancel_rtms],
            cadeia_sequencial=[
                make_chain_step(
                    1, "RM03-PPC-1", "Protocolo Inicial — HF-rTMS PPC Ipsilesional", "HF-rTMS (10 Hz) — P3/P4 Ipsilesional (Kim et al., 2013)",
                    "HF-rTMS", "P3/P4 ipsilesional", "10 Hz | 90% LMR | 1.000 pulsos (20 trens × 50 p, 55 s IIT)",
                    sessoes="10 sessões diárias",
                    efeito_esperado="Aumento de 10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
                    referencia="Kim et al. (2013) · DOI: 10.1016/j.apmr.2012.12.016", fase_etapa="inicial",
                    calc_meta={
                        "mcid_valor": 8.0,
                        "mcid_label": "≥ +8,0 pontos (limite inferior do IC 95%: 8,0–12,7 · média +10,4 pts)",
                        "meta_texto": "Aumento esperado de +10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias",
                        "ic_min": 8.0,
                        "ic_max": 12.7,
                        "estudo_referencia": "Kim et al. (2013) — HF-rTMS 10 Hz P3/P4 Ipsilesional",
                        "efeito_esperado_resumo": "Aumento de 10,4 pontos (IC 95%: 8,0 a 12,7) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
                    },
                ),
                make_chain_step(
                    2, "RM03-PPC-2", "Próximo Protocolo — LF-rTMS PPC Contralesional", "LF-rTMS (1 Hz) — P3/P4 Contralesional (Kim et al., 2013)",
                    "LF-rTMS", "P3/P4 contralesional", "1 Hz | 90% LMR | 1.200 pulsos",
                    sessoes="10 sessões diárias",
                    efeito_esperado="Aumento de 16,4 pontos (IC 95%: 13,0 a 20,0) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
                    referencia="Kim et al. (2013) · DOI: 10.1016/j.apmr.2012.12.016", fase_etapa="sequencia",
                    calc_meta={
                        "mcid_valor": 13.0,
                        "mcid_label": "≥ +13,0 pontos (limite inferior do IC 95%: 13,0–20,0 · média +16,4 pts)",
                        "meta_texto": "Aumento esperado de +16,4 pontos (IC 95%: 13,0 a 20,0) no teste de cancelamento de estrelas após 10 sessões diárias",
                        "ic_min": 13.0,
                        "ic_max": 20.0,
                        "estudo_referencia": "Kim et al. (2013) — LF-rTMS 1 Hz P3/P4 Contralesional",
                        "efeito_esperado_resumo": "Aumento de 16,4 pontos (IC 95%: 13,0 a 20,0) no teste de cancelamento de estrelas após 10 sessões diárias em pacientes em fase aguda com lesões corticais ou subcorticais",
                    },
                ),
                make_chain_step(
                    3, "RM03-ALT2", "Seção de Ajustes — iTBS F5 (Linha Pontilhada)", "iTBS F5 DLPFC Esquerdo (Cao et al., 2016)",
                    "iTBS", "F5 (entre F3 e F7) — Córtex pré-frontal dorsolateral esquerdo",
                    "iTBS: 2 sessões separadas por 15 min | 3 pulsos a 50 Hz / 5 Hz (2 s ON, 8 s OFF) | 600 pulsos | 80% LMR",
                    sessoes="10 dias",
                    efeito_esperado="+37% no teste de cancelamento de estrelas após 10 dias de tratamento",
                    referencia="Cao et al. (2016) · DOI: 10.1097/WNR.0000000000000689", linha_fluxograma="pontilhada", fase_etapa="ajustes",
                    calc_meta={
                        "mcid_valor": 37.0,
                        "mcid_label": "≥ +37% no teste de cancelamento de estrelas (Cao et al., 2016)",
                        "meta_texto": "Aumento esperado ≥ +37% no teste de cancelamento de estrelas após 10 dias de tratamento",
                        "is_percent": True,
                        "estudo_referencia": "Cao et al. (2016) — iTBS DLPFC Esquerdo (F5)",
                        "efeito_esperado_resumo": "Aumento de +37% no teste de cancelamento de estrelas após 10 dias de tratamento",
                    },
                ),
            ],
            ajuste_parametros=adj_mob_rtms, falha_terapeutica=falha_mob_rtms, sessoes_ajuste=sa_mob_rtms,
            notas_clinicas="Indicado na heminegligência unilateral afetando a mobilidade; associar terapia de varredura visual.",
            audit_meta=_audit("Moderada", "Metanálise heminegligência (Fan et al., 2017).", "Evidência sólida em modulação parietal.", ["Risco de viés"], "Moderada", "Condicional", "Reequilíbrio inter-hemisférico em heminegligência.", tol_mob_rtms),
        ),
        "tdcs_m1_mob": make_mod(
            protocolo_id="RM04-M1", tecnica="tDCS Anódica — M1 MMII Vértice Cz (Danzl et al., 2013)", modalidade_sigla="tDCS MMII",
            alvo="Ânodo Cz (25 cm²) + Cátodo supraorbital contralateral (35 cm²)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min (eletrodos 25/35 cm²)", sessoes="12 a 20 sessões simultâneas ao treino locomotor",
            escala_recomendada="BBS / TC10m / FMA-LE (conforme fator limitante)", meta_melhora="+5,0 pontos na BBS / +0,5 pt FAC",
            tamanho_efeito=0.55, evidencia="Nível B — Eficácia provável (IFCN tDCS)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_DANZL_2013, meta_analise=REF_JIA_2025,
            mcid_valor=5.0, mcid_label="+5,0 pontos na BBS", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Danzl et al. (2013)", efeito_resumo="Ganho funcional locomotor (+0,5 pt FAC com órtese robótica)",
            escalas_detalhadas=[scale_bbs, scale_10mwt, scale_fma_le], escalas_por_fator=mob_scales_map,
            cadeia_sequencial=[
                make_chain_step(1, "RM04-P1", "Protocolo Inicial — tDCS Anódica Cz", "tDCS Anódica Cz M1 MMII (Danzl et al., 2013)", "tDCS Anódica", "Ânodo Cz (25 cm²) + Cátodo supraorbital (35 cm²)", "2,0 mA | 20 min", sessoes="12 a 20 sessões", efeito_esperado="+0,5 pt FAC com órtese robótica", referencia="Danzl et al. (2013) · DOI: 10.3233/NRE-130929", fase_etapa="inicial"),
                make_chain_step(2, "RM04-P2", "Próximo Protocolo — tDCS Anódica C3/C4 Ipsilesional", "tDCS Anódica C3/C4 Ipsilesional (Wang et al., 2024)", "tDCS Anódica", "Ânodo C3/C4 ipsilesional + Cátodo supraorbital contralesional (25 cm²)", "2,0 mA | 20 min", sessoes="20 sessões com fisioterapia padrão", efeito_esperado="+11,06 pts na BBS", referencia="Wang et al. (2024) · DOI: 10.2340/jrm.v56.40348", fase_etapa="sequencia"),
                make_chain_step(3, "RM04-ALT1", "Seção de Ajustes — tDCS Cerebelar (Linha Pontilhada)", "tDCS Cerebelar Cátodo Bucinador ou Deltoide D (Qurat-Ul-Ain et al., 2023)", "tDCS Cerebelar", "Ânodo cerebelo 2 cm abaixo do ínion (15 cm²) + Cátodo músculo bucinador ou deltoide direito", "2,0 mA | 20 min", sessoes="1 a >15 sessões", efeito_esperado="+4,64 pts na BBS", referencia="Qurat-Ul-Ain et al. (2023) · DOI: 10.1080/07853890.2023.2252439", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
                make_chain_step(4, "RM04-ALT2", "Seção de Ajustes — taVNS + tDCS (Linha Pontilhada)", "taVNS Tragus E + tDCS C3/C4 (Wang et al., 2024)", "taVNS + tDCS", "Tragus orelha esquerda (taVNS) seguido de C3/C4 ipsilesional (tDCS)", "taVNS (200 µs, 25 Hz, 30 s ON/OFF, abaixo dor, 30 min) seguido de tDCS (2 mA, 30 min)", sessoes="20 sessões com fisioterapia padrão", efeito_esperado="+16,24 pts na BBS", referencia="Wang et al. (2024) · DOI: 10.2340/jrm.v56.40348", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
            ],
            ajuste_parametros=adj_mob_tdcs, falha_terapeutica=falha_mob_tdcs, sessoes_ajuste=sa_mob_tdcs,
            notas_clinicas="Aplicar simultaneamente ao treino locomotor/equilíbrio; não interromper medicações em uso.",
            audit_meta=_audit("Moderada", "Revisão em estimulação elétrica para marcha.", "Combinação simultânea ao treino locomotor potencializa ganho.", ["IFCN tDCS"], "Moderada", "Condicional", "Alternativa no deltoide direito reduz desconforto facial.", tol_mob_tdcs),
            mod_tipo="tdcs",
        ),
        "tdcs_s1_mob": make_mod(
            protocolo_id="RM04-S1", tecnica="tDCS Anódica — S1 CP3/CP4 Ipsilesional (Koo et al., 2018)", modalidade_sigla="tDCS S1",
            alvo="Ânodo CP3/CP4 ipsilesional + Cátodo Fp1/Fp2 contralesional (25 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min (eletrodos 25 cm²)", sessoes="10 sessões associadas à fisioterapia",
            escala_recomendada="FMA-LE Sensorial + rNSA", meta_melhora="+4,5 pts rNSA / +4,0 pts FMA-LE",
            tamanho_efeito=0.52, evidencia="Nível B — Recuperação sensorial MMII", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_KOO_2018, meta_analise=REF_CHEN_2023,
            mcid_valor=4.0, mcid_label="+4,0 pontos FMA-LE", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Koo et al. (2018)", efeito_resumo="+4,5 pts na rNSA após 10 sessões",
            escalas_detalhadas=[scale_fma_le],
            cadeia_sequencial=[
                make_chain_step(1, "RM04-S1-P1", "Protocolo Inicial — tDCS Anódica S1 CP3/CP4", "tDCS Anódica S1 CP3/CP4 (Koo et al., 2018)", "tDCS S1", "Ânodo CP3/CP4 ipsilesional + Cátodo Fp1/Fp2 contralesional (25 cm²)", "1,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="+4,5 rNSA", referencia="Koo et al. (2018) · DOI: 10.1097/PHM.0000000000000910", fase_etapa="inicial"),
                make_chain_step(2, "RM04-ALT3", "Seção de Ajustes — tDCS M1 C3/C4 Sensorial (Linha Pontilhada)", "tDCS Anódica C3/C4 para Função Sensorial (Bornheim et al., 2020)", "tDCS M1", "Ânodo C3/C4 lesado + Cátodo Fp1/Fp2 contralesional (25 cm²)", "1,0 mA (titular para 2,0 mA) | 20 min (titular para 30 min)", sessoes="20 sessões combinadas a fisioterapia e TO", efeito_esperado="+8 pts na subescala sensorial FMA", referencia="Bornheim et al. (2020) · DOI: 10.1016/j.brs.2019.10.019", linha_fluxograma="pontilhada", fase_etapa="ajustes"),
            ],
            ajuste_parametros=adj_mob_tdcs, falha_terapeutica=falha_mob_tdcs, sessoes_ajuste=sa_mob_tdcs,
            notas_clinicas="Associar à estimulação sensorial plantar/proprioceptiva; na seção de Ajustes utiliza C3/C4 lesado.",
            audit_meta=_audit("Moderada", "Metanálise sensorial pós-AVC (Chen et al., 2023).", "Indicado na disfunção sensorial do membro inferior.", ["Risco de viés"], "Moderada", "Condicional", "C3/C4 sensorial compõe a seção de Ajustes pontilhada.", tol_mob_tdcs),
            mod_tipo="tdcs",
        ),
        "tdcs_ppc_mob": make_mod(
            protocolo_id="RM04-PPC", tecnica="tDCS Anódica — Córtex Parietal Posterior P4/P3 (Bang et al., 2015)", modalidade_sigla="tDCS PPC",
            alvo="Ânodo P4 + Cátodo P3 no Córtex Parietal Posterior (35 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min (eletrodos 35 cm²)", sessoes="15 sessões associadas à varredura visual",
            escala_recomendada="Teste de Cancelamento de Estrelas (BIT — 0 a 54)", meta_melhora="Ganho ≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (Bang et al., 2015: -6,0 mm bissecção)",
            tamanho_efeito=0.50, evidencia="Nível B — Eficácia clínica (Fan 2017)", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_BANG_2015, meta_analise=REF_FAN_2017,
            mcid_valor=5.0, mcid_label="≥ +5,0 estrelas no Cancelamento de Estrelas (0–54)", cohen_d_valor=0.50, cohen_d_interp="Moderado",
            estudo_referencia="Bang et al. (2015)", efeito_resumo="-6,0 mm na bissecção de linhas após 15 sessões (acompanhamento quantitativo pelo Teste de Cancelamento de Estrelas)",
            escalas_detalhadas=[scale_star_cancel_tdcs],
            cadeia_sequencial=[
                make_chain_step(
                    1, "RM04-PPC-1", "Protocolo Inicial — tDCS P4/P3", "tDCS Anódica P4 / Cátodo P3 (Bang et al., 2015)",
                    "tDCS PPC", "Ânodo P4 + Cátodo P3 (35 cm²)", "1,0 mA | 20 min", sessoes="15 sessões",
                    efeito_esperado="-6,0 mm bissecção de linhas após 15 sessões", referencia="Bang et al. (2015) · DOI: 10.1589/jpts.27.2759", fase_etapa="inicial",
                    calc_meta={
                        "mcid_valor": 5.0,
                        "mcid_label": "≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (0–54)",
                        "meta_texto": "Ganho ≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (Bang et al., 2015: -6,0 mm bissecção)",
                        "estudo_referencia": "Bang et al. (2015) — tDCS Anódica P4 / Cátodo P3",
                        "efeito_esperado_resumo": "-6,0 mm na bissecção de linhas após 15 sessões (avaliação na calculadora pelo Teste de Cancelamento de Estrelas)",
                    },
                ),
                make_chain_step(
                    2, "RM04-PPC-2", "Próximo Protocolo — tDCS P6/FP1", "tDCS Anódica P6 / Cátodo FP1 (Làdavas et al., 2015)",
                    "tDCS PPC", "Ânodo P6 + Cátodo FP1 (35 cm²)", "2,0 mA | 20 min", sessoes="10 sessões",
                    efeito_esperado="+19 pts na bateria BIT", referencia="Làdavas et al. (2015) · DOI: 10.3233/RNN-140464", fase_etapa="sequencia",
                    calc_meta={
                        "mcid_valor": 5.0,
                        "mcid_label": "≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (BIT)",
                        "meta_texto": "Ganho ≥ +5,0 estrelas no Teste de Cancelamento de Estrelas (Làdavas et al., 2015: +19 pts BIT)",
                        "estudo_referencia": "Làdavas et al. (2015) — tDCS Anódica P6 / Cátodo FP1",
                        "efeito_esperado_resumo": "+19 pontos na bateria BIT após 10 sessões",
                    },
                ),
                make_chain_step(
                    3, "RM04-PPC-3", "Próximo Protocolo (Linha Pontilhada) — tDCS Catódica P3 / Cz", "tDCS Catódica P3 / Ânodo Cz (Yi et al., 2016)",
                    "tDCS Catódica PPC", "Cátodo P3 + Ânodo Cz (25 cm²)", "2,0 mA | 30 min", sessoes="15 sessões",
                    efeito_esperado="+7,0 pontos no teste de cancelamento de estrelas", referencia="Yi et al. (2016) · DOI: 10.5535/arm.2016.40.2.223", linha_fluxograma="pontilhada", fase_etapa="sequencia",
                    calc_meta={
                        "mcid_valor": 7.0,
                        "mcid_label": "≥ +7,0 pontos no Teste de Cancelamento de Estrelas (Yi et al., 2016)",
                        "meta_texto": "Aumento esperado de +7,0 pontos no Teste de Cancelamento de Estrelas após 15 sessões",
                        "estudo_referencia": "Yi et al. (2016) — tDCS Catódica P3 / Ânodo Cz",
                        "efeito_esperado_resumo": "Aumento de +7,0 pontos no teste de cancelamento de estrelas após 15 sessões",
                    },
                ),
            ],
            ajuste_parametros=adj_mob_tdcs, falha_terapeutica=falha_mob_tdcs, sessoes_ajuste=sa_mob_tdcs,
            notas_clinicas="Combinar varredura visual em ortostatismo e marcha.",
            audit_meta=_audit("Moderada", "Metanálise heminegligência (Fan et al., 2017).", "Protocolos PPC alinhados para heminegligência em mobilidade.", ["Risco de viés"], "Moderada", "Condicional", "Treino simultâneo amplia efeito.", tol_mob_tdcs),
            mod_tipo="tdcs",
        ),
    }

    arvore_rtms = {
        "roadmap_id": "RM03",
        "titulo_fluxograma": "AVC Mobilidade Funcional — rTMS / iTBS / rPMS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante da mobilidade e marcha pós-AVC?",
                "subtitulo": "Selecione o fator limitante predominante para mobilidade funcional.",
                "opcoes": [
                    {"id": "equilibrio", "rotulo": "Déficit de equilíbrio", "criterio": "BBS / Mini-BESTest", "descricao": "Instabilidade postural e risco de quedas.", "proxima_etapa": "alvo_mobilidade"},
                    {"id": "disfuncao_motora_mi", "rotulo": "Disfunção motora dos membros inferiores", "criterio": "FMA-LE (34 pts)", "descricao": "Comprometimento motor de MMII.", "proxima_etapa": "alvo_mobilidade"},
                    {"id": "velocidade_marcha", "rotulo": "Alteração na Marcha", "criterio": "TC10m / 10MWT", "descricao": "Redução de velocidade e cadência.", "proxima_etapa": "alvo_mobilidade"},
                    {"id": "negligencia", "rotulo": "Heminegligência", "criterio": "Teste de Cancelamento de Estrelas (BIT)", "descricao": "Desatenção espacial afetando a marcha.", "protocolo_alvo": "rtms_ppc_mob"},
                ],
            },
            "alvo_mobilidade": {
                "pergunta": "Qual alvo cortical/cerebelar deseja priorizar inicialmente?",
                "subtitulo": "Os três fatores motores podem seguir diretamente para o Cerebelo ou para o Córtex Motor Primário (M1).",
                "opcoes": [
                    {"id": "mob_cerebelo", "rotulo": "Cerebelo", "criterio": "Bobina parabólica ou duplo cone", "descricao": "Inicia por iTBS cerebelar contralateral (Koch et al., 2019).", "protocolo_alvo": "equilibrio"},
                    {"id": "mob_m1", "rotulo": "Córtex Motor Primário (M1)", "criterio": "Hotspot PEM ou Cz", "descricao": "Verificar extensão cortical no giro pré-frontal.", "proxima_etapa": "lesao_pf_mob"},
                ],
            },
            "lesao_pf_mob": {
                "pergunta": "Há lesão cortical extensa no giro pré-frontal?",
                "subtitulo": "Critério neuroanatômico de redirecionamento de M1 para Cerebelo.",
                "opcoes": [
                    {"id": "mob_pf_sim", "rotulo": "SIM — Lesão pré-frontal extensa", "criterio": "Redireciona para rota cerebelar", "descricao": "Segue diretamente para iTBS cerebelar contralateral (Koch et al., 2019).", "protocolo_alvo": "equilibrio"},
                    {"id": "mob_pf_nao", "rotulo": "NÃO — Sem lesão pré-frontal extensa", "criterio": "M1 viável", "descricao": "Verificar tempo de evolução da lesão (≤ 1 mês).", "proxima_etapa": "fase_aguda_mob"},
                ],
            },
            "fase_aguda_mob": {
                "pergunta": "Trata-se de lesão aguda (≤ 1 mês)?",
                "subtitulo": "Define o protocolo inicial entre M1 contralesional (aguda) e M1 ipsilesional (> 1 mês).",
                "opcoes": [
                    {"id": "mob_aguda_sim", "rotulo": "SIM — Lesão aguda (≤ 1 mês)", "criterio": "≤ 1 mês pós-AVC", "descricao": "Inicia por LF-rTMS 1 Hz no M1 não lesionado (Zhang et al., 2024).", "protocolo_alvo": "rtms_m1_aguda"},
                    {"id": "mob_aguda_nao", "rotulo": "NÃO — Subaguda ou Crônica (> 1 mês)", "criterio": "> 1 mês pós-AVC", "descricao": "Inicia por HF-rTMS 10 Hz M1 tibial anterior (Wang et al., 2024).", "protocolo_alvo": "velocidade_marcha"},
                ],
            },
        },
        "ajuste_parametros": adj_mob_rtms,
        "protocolo_alternativo": {
            "nome": "Seção de Ajustes — rPMS em Tibial Anterior / Músculos da Marcha (Beaulieu et al., 2015)",
            "tecnica": "rPMS Periférica", "alvo": "Ventre do músculo tibial anterior afetado e demais músculos da marcha com déficit",
            "parametros": "42% saída máxima | 2 s ON / 8 s OFF | 600 pulsos | 190 s (intermitente p/ fraqueza; contínuo p/ espasticidade)",
            "observacoes": "Bobina perpendicular gerando contração visível (+7,8° dorsiflexão). Associar sempre rPMS a rTMS/TBS.",
        },
        "protocolo_alternativo_2": {
            "nome": "Seção de Ajustes — iTBS F5 em Heminegligência (Cao et al., 2016)",
            "tecnica": "iTBS Frontal", "alvo": "F5 (entre F3 e F7) — Córtex pré-frontal dorsolateral esquerdo", "parametros": "2 sessões/dia (15 min intervalo) | 600 pulsos | 80% LMR",
            "observacoes": "Etapa de Ajustes para heminegligência refratária à neuromodulação parietal.",
        },
        "falha_terapeutica": {
            "id": "RM03-FALHA", "titulo": "Falha Terapêutica em rTMS Mobilidade",
            "criterios_definicao": "Ausência de resposta clínica mesmo após percorrer os protocolos sequenciais e a seção de Ajustes com rPMS.",
            "descricao": "Reavaliar resposta após 5 sessões antes de avançar na cadeia.",
            "condutas": ["Alternar entre Cerebelo e M1 conforme neuroimagem.", "Considerar tDCS / taVNS para Mobilidade Funcional.", "Se dor limitar a marcha, seguir o fluxo de Dor Neuropática Crônica."],
        },
    }

    arvore_tdcs = {
        "roadmap_id": "RM04",
        "titulo_fluxograma": "AVC Mobilidade Funcional — tDCS / taVNS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante na mobilidade pós-AVC (tDCS)?",
                "subtitulo": "Selecione o fator limitante predominante para estimulação elétrica em mobilidade.",
                "opcoes": [
                    {"id": "marcha_tdcs", "rotulo": "Alteração da Marcha", "criterio": "TC10m / TUG", "descricao": "Inicia por tDCS anódica M1 MMII em Cz.", "protocolo_alvo": "tdcs_m1_mob"},
                    {"id": "fraqueza_tdcs", "rotulo": "Fraqueza muscular", "criterio": "MRC / FMA-LE", "descricao": "Inicia por tDCS anódica M1 MMII em Cz.", "protocolo_alvo": "tdcs_m1_mob"},
                    {"id": "equilibrio_tdcs", "rotulo": "Déficit de Equilíbrio", "criterio": "BBS / Mini-BESTest", "descricao": "Inicia por tDCS anódica M1 MMII em Cz.", "protocolo_alvo": "tdcs_m1_mob"},
                    {"id": "sensorial_tdcs_mi", "rotulo": "Disfunção sensorial do membro inferior", "criterio": "FMA-LE Sensorial", "descricao": "Inicia por tDCS anódica em S1 (CP3/CP4).", "protocolo_alvo": "tdcs_s1_mob"},
                    {"id": "negligencia_tdcs_mi", "rotulo": "Heminegligência", "criterio": "Teste de Cancelamento de Estrelas (BIT)", "descricao": "Inicia por tDCS Parietal Posterior (P4/P3).", "protocolo_alvo": "tdcs_ppc_mob"},
                ],
            },
        },
        "ajuste_parametros": adj_mob_tdcs,
        "protocolo_alternativo": {
            "nome": "Seção de Ajustes (Linha Pontilhada) — tDCS Cerebelar (Qurat-Ul-Ain et al., 2023)",
            "tecnica": "tDCS Cerebelar", "alvo": "Cerebelo (15 cm²) + Cátodo no bucinador ou deltoide direito", "parametros": "2,0 mA | 20 min",
            "observacoes": "+4,64 pts na BBS. Permite cátodo no deltoide direito em caso de desconforto facial.",
        },
        "protocolo_alternativo_2": {
            "nome": "Seção de Ajustes (Linha Pontilhada) — taVNS + tDCS (Wang et al., 2024)",
            "tecnica": "taVNS + tDCS", "alvo": "Tragus esquerdo + C3/C4", "parametros": "taVNS (30 min) seguido de tDCS 2,0 mA (30 min)",
            "observacoes": "+16,24 pts na BBS em ensaio combinado.",
        },
        "falha_terapeutica": {
            "id": "RM04-FALHA", "titulo": "Falha Terapêutica em tDCS Mobilidade",
            "criterios_definicao": "Ausência de resposta funcional relevante após ciclo otimizado (2 mA, 30 min, > 15 sessões simultâneas à terapia) e seção de Ajustes.",
            "descricao": "Reavaliar resposta em todos os fatores após 5 sessões.",
            "condutas": ["Considerar modalidade rTMS/iTBS cerebelar ou M1 em Mobilidade Funcional.", "Se dor for o limitante primário, seguir o fluxo de Dor Neuropática Crônica."],
        },
    }

    obs_rtms = _avc_shared_observations(
        "RM03", "a bobina", "mobilidade funcional", "rtms", "", "", [],
    ) + [
        make_obs("RM03-HOTSPOT-CZ", "Regra de Aplicação: estimular M1 no hotspot via PEM por TMS de pulso único. Na ausência de PEM em MMII, usar Cz como referência e definir LMR pelo hemisfério não lesionado.", "step", categoria="neurofisiologia", etapa_ids=["alvo_mobilidade", "fase_aguda_mob"], modalidades_tipo=["rtms"], referencia_doi=PEM_GUIDE_DOI, referencia_rotulo=PEM_GUIDE_LABEL),
        make_obs("RM03-BOBINA-MMII", "Bobinas circulares ou parabólicas são mais adequadas para estimular a representação profunda dos membros inferiores em M1.", "alvo", categoria="equipamento", protocolo_ids=["velocidade_marcha", "rtms_m1_aguda"], modalidades_tipo=["rtms"]),
        make_obs("RM03-BOBINA-CEREB", "Bobinas parabólicas e duplo cone são mais indicadas para estimulação do cerebelo.", "alvo", categoria="equipamento", protocolo_ids=["equilibrio"], modalidades_tipo=["rtms"]),
        make_obs("RM03-RPMS-MARCHA", "Abrangência Muscular (rPMS na marcha): músculos fracos (tibial anterior, transverso abdominal, multífidos) = modo intermitente (3 p 50 Hz / 5 Hz, 2 s ON / 8 s OFF, 600 p); músculos espásticos (isquiotibiais, adutores de quadril) = modo contínuo (600 p sem pausas). Bobina perpendicular com contração visível.", "stage", categoria="parametros", protocolo_ids=["equilibrio", "velocidade_marcha", "rtms_m1_aguda"], estagios=["alt2"], modalidades_tipo=["rtms"]),
    ]

    obs_tdcs = _avc_shared_observations(
        "RM04", "o eletrodo", "mobilidade funcional", "tdcs", "", "", [],
    ) + [
        make_obs("RM04-DELTOIDE", "Regra de Aplicação: na montagem cerebelar, o cátodo originalmente no músculo bucinador pode ser posicionado sobre o músculo deltoide direito em caso de desconforto facial.", "stage", categoria="anatomia", protocolo_ids=["tdcs_m1_mob"], estagios=["alt2"], modalidades_tipo=["tdcs"]),
    ]

    return {
        "id": cid, "condicao": "Acidente Vascular Cerebral — Mobilidade e Marcha", "eixo": "Doenças Cerebrovasculares",
        "roadmap_id": "RM03", "svg_file": "RM03.svg",
        "fatores_limitantes": [
            {"id": "equilibrio", "nome": "Déficit de equilíbrio", "instrumento_sugerido": "BBS / Mini-BESTest", "descricao": "Instabilidade postural e risco de quedas."},
            {"id": "disfuncao_motora_mi", "nome": "Disfunção motora dos membros inferiores", "instrumento_sugerido": "FMA-LE (34 pts)", "descricao": "Comprometimento motor em membros inferiores."},
            {"id": "velocidade_marcha", "nome": "Alteração na Marcha", "instrumento_sugerido": "TC10m / 10MWT", "descricao": "Redução de velocidade e cadência da marcha."},
            {"id": "sensorial_mi", "nome": "Disfunção sensorial do membro inferior", "instrumento_sugerido": "FMA-LE Sensorial (tDCS)", "descricao": "Déficit somatossensorial plantar/proprioceptivo."},
            {"id": "negligencia", "nome": "Heminegligência", "instrumento_sugerido": "Teste de Cancelamento de Estrelas (BIT)", "descricao": "Heminegligência espacial impactando deslocamento."},
        ],
        "arvore_algoritmo": arvore_rtms, "arvores_por_modalidade": {"rtms": arvore_rtms, "tdcs": arvore_tdcs},
        "observacoes_contextuais": obs_rtms + obs_tdcs, "modalidades": modalidades, "tags_busca": tags,
    }


def _build_avc_disfagia():
    cid = "avc-disfagia"
    tags = {
        "siglas": ["AVC", "AVE", "FOIS", "DOSS", "MASA", "SSA", "PAS"],
        "coordenadas_10_20": ["M1 Suprahioideo", "C5", "C6", "CP5", "CP6", "Cerebelo"],
        "alvos_anatomicos": ["Córtex Motor da Deglutição (2–4 cm à frente de Cz)", "Cerebelo Unilateral", "Cerebelo Bilateral", "tAVNS"],
        "sinonimos_en": ["stroke", "dysphagia", "swallowing disorder", "aspiration", "pharyngeal cortex"],
        "sintomas_pt": ["disfagia", "deglutição", "engasgo", "aspiração", "alimentação oral", "sonda enteral", "consistências"],
        "escalas": ["FOIS", "DOSS", "MASA", "SSA"], "tecnicas": ["rTMS", "iTBS", "cTBS", "tDCS", "tAVNS"],
    }
    tol_disf = _tol_profile(
        "Avaliar contraindicações: presença de implantes metálicos no cérebro, histórico de convulsões não controladas e implantes cocleares.",
        "Protocolos Theta-Burst (iTBS/cTBS) requerem menos tempo de sessão e menor intensidade vs. rTMS tradicional; monitorar tolerabilidade local.",
        "Avaliar extensão cortical/subcortical, déficit cognitivo ou de linguagem associado e fase aguda/subaguda (1–6 meses).",
    )
    scale_fois = make_scale("fois", "Functional Oral Intake Scale (FOIS)", "FOIS", "aumento", "Ganho ≥ 1 nível funcional de via oral em TODAS as consistências alimentares avaliadas", 0.65, placeholder="Ex: 3", min_val=1, max_val=7, mcid_valor=1.0, mcid_label="+1 nível na FOIS")
    scale_doss = make_scale("doss", "Dysphagia Outcome and Severity Scale (DOSS)", "DOSS", "aumento", "Evolução ≥ 1 nível de gravidade clínica da deglutição", 0.58, placeholder="Ex: 3", min_val=1, max_val=7, mcid_valor=1.0, mcid_label="+1 nível na DOSS")

    step_alt_a = make_chain_step(7, "RM07-ALTA", "Seção de Ajustes — iTBS Faríngea C6 Direita (Linha Pontilhada)", "iTBS — Córtex Motor Faríngeo C6 Direito (Cosentino et al., 2020)", "iTBS Faríngea", "Córtex motor faríngeo do hemisfério direito (C6)", "iTBS: 3 pulsos a 50 Hz durante 200 ms, 2 s de trem repetido a cada 10 s por 20× (200 s) | 600 pulsos | 70% LMR", sessoes="5 sessões (1×/dia, 5 dias/semana, 1 semana)", efeito_esperado="Melhora de 2 pontos na escala DOSS com efeito persistente", referencia="Cosentino et al. (2020) · DOI: 10.1111/nmo.13791", linha_fluxograma="pontilhada", fase_etapa="ajustes")
    step_alt_b = make_chain_step(8, "RM07-ALTB", "Seção de Ajustes — Estímulo Vagal tAVNS (Linha Pontilhada)", "tAVNS — Ramo Auricular do Nervo Vago (Wang et al., 2023)", "tAVNS Auricular", "Ramo auricular do nervo vago (fase aguda do AVC)", "Intensidade ajustada conforme tolerância | 30 minutos", sessoes="2 vezes ao dia, 5 dias por semana, por 3 semanas", efeito_esperado="Melhora estatisticamente significativa nas escalas clínicas e PAS com efeito persistente", referencia="Wang et al. (2023) · DOI: 10.1007/s00415-022-11465-5", linha_fluxograma="pontilhada", fase_etapa="ajustes")
    step_disf_p3 = make_chain_step(3, "RM07-P3", "HF-rTMS 5 Hz — M1 Suprahioideo Não Lesado", "HF-rTMS 5 Hz — M1 Suprahioideo Não Lesado (Zhong et al., 2021)", "HF-rTMS (5 Hz)", "M1 suprahioideo não lesado", "5 Hz | 110% LMR | 1.800 pulsos", sessoes="10 sessões (1×/dia, 5 dias/sem, 2 semanas)", efeito_esperado="Drive corticobulbar compensatório", referencia="Zhong et al. (2021) · DOI: 10.3389/fneur.2021.625683", linha_fluxograma="solida", fase_etapa="sequencia")
    step_disf_p4 = make_chain_step(4, "RM07-P4", "cTBS — M1 Suprahioideo Não Lesado", "cTBS — M1 Suprahioideo Não Lesado (Tai et al., 2023)", "cTBS", "M1 suprahioideo não lesado", "cTBS: 3 pulsos a 50 Hz (200 ms), 40 s contínuos | 600 pulsos | 80% LMR", sessoes="20 sessões (1×/dia, 5 dias/sem, 4 semanas)", efeito_esperado="Melhora de 17,28% na SSA e 66,67% na PAS", referencia="Tai et al. (2023) · DOI: 10.23736/S1973-9087.23.08023-1", linha_fluxograma="solida", fase_etapa="sequencia")
    step_disf_p5 = make_chain_step(5, "RM07-P5", "LF-rTMS 1 Hz — M1 Suprahioideo Não Lesado", "LF-rTMS 1 Hz — M1 Suprahioideo Não Lesado (Lim et al., 2014)", "LF-rTMS (1 Hz)", "M1 não lesado", "1 Hz | 100% LMR | 1.200 pulsos", sessoes="10 sessões (1×/dia, 5 dias/sem, 2 semanas)", efeito_esperado="Melhora em FDS para líquido ralo (-2,54) e PAS", referencia="Lim et al. (2014) · DOI: 10.5535/arm.2014.38.5.592", linha_fluxograma="solida", fase_etapa="sequencia")
    step_p9_bi = make_chain_step(6, "RM07-P9", "iTBS — Cerebelo Bilateral Faríngeo", "iTBS — Cerebelo Bilateral Faríngeo (Rao et al., 2022)", "iTBS Cerebelar Bilateral", "Representação motora faríngea no cerebelo bilateral (2,4 cm abaixo do ínion e 4,3 cm lateralmente)", "iTBS: 3 pulsos a 50 Hz repetidos a 5 Hz | 100% LMR | 2 s trem a cada 10 s (190 s total) | 600 pulsos em cada hemisfério cerebelar", sessoes="10 sessões (1×/dia, 5 dias/sem, 2 semanas)", efeito_esperado="-0,72 FEDSS, +1,42 PAS, +4,44 SSA e +1,28 FOIS", referencia="Rao et al. (2022) · DOI: 10.1177/15459683221092995", linha_fluxograma="solida", fase_etapa="sequencia")

    adj_disf_rtms = {"titulo": "Ajustes, Tolerabilidade e Coordenadas Anatômicas (Disfagia)", "tolerabilidade": "Respeitar contraindicações (implantes metálicos/cocleares, convulsões não controladas). Em desconforto local, considerar redução gradual dentro da faixa tolerável.", "dose_pulsos": "Ciclos mais frequentes de 5 ou 10 sessões ao longo de 1 ou 2 semanas, associados à terapia fonoaudiológica especializada.", "calibracao_limiar": "M1 suprahioideo: 2–4 cm à frente de Cz e 4–6 cm lateral; Cerebelo unilateral: 1–2 cm abaixo do ínion e 3–4 cm lateral; Cerebelo bilateral faríngeo: 2,4 cm abaixo do ínion e 4,3 cm lateral."}
    adj_disf_tdcs = {"titulo": "Ajustes de Corrente e Segurança em tDCS (Disfagia)", "tolerabilidade": "Atenção máxima a implantes cocleares, metálicos intracranianos e convulsões não controladas; hidratar eletrodos (5×5 cm ou 3×5/4×4 cm) uniformemente.", "dose_pulsos": "Otimização de Dose: na tDCS unilateral inicial (C5/C6), considerar 1,4 mA por 20 minutos (Xie et al., 2023) a critério profissional. Ciclos mais frequentes de 5 ou 10 sessões em 1–2 semanas.", "calibracao_limiar": "Acompanhamento conjunto com fonoaudiólogo especializado em disfagia."}
    falha_disf = _falha_mod("Ausência de qualquer resposta clínica em até 5 dias após avaliar TODAS as consistências alimentares (líquido, pastoso e sólido) e percorrer os protocolos indicados.", "1. Avaliar individualmente a deglutição para todas as consistências alimentares (líquido, pastoso e sólido);\n2. Realizar avaliação clínica, escalas (FOIS/DOSS/SSA) e videodeglutograma pré/pós;\n3. Considerar transição entre rTMS/TBS e tDCS/tAVNS para Disfagia pós-AVC.")
    sa_disf = _sessoes_aj("Ausência de qualquer resposta em até 5 dias (avaliar OBRIGATORIAMENTE líquido, pastoso e sólido antes de declarar resposta insatisfatória).", "Manter associação obrigatória com terapia fonoaudiológica convencional especializada em disfagia durante todo o ciclo.", "Interromper em via oral segura e estável ou avançar na sequência de protocolos até ajustes e falha terapêutica.")

    modalidades = {
        "orofaringea": make_mod(
            protocolo_id="RM07-P1", tecnica="iTBS — M1 Suprahioideo Lesado", modalidade_sigla="iTBS",
            alvo="M1 suprahioideo do hemisfério LESADO (2–4 cm à frente de Cz e 4–6 cm lateralmente)", frequencia="iTBS (50 Hz / 5 Hz)", intensidade="80% LMR",
            pulsos_duracao="600 pulsos | 200 s (2 s trem a cada 120 s)", sessoes="20 sessões (1×/dia, 5 dias/sem, 4 semanas)",
            escala_recomendada="FOIS / DOSS / SSA / MASA (+ Videodeglutograma)", meta_melhora="Ganho ≥ 1 nível na FOIS avaliando todas as consistências",
            tamanho_efeito=0.65, evidencia="Nível B — Metanálise Han 2024 / Wen 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_TAI_2023, meta_analise=REF_HAN_2024_DYSP,
            mcid_valor=1.0, mcid_label="+1 nível na FOIS", cohen_d_valor=0.65, cohen_d_interp="Moderado",
            estudo_referencia="Tai et al. (2023)", efeito_resumo="Melhora de 22% na SSA, 16,15% OMFS e 80% na PAS",
            escalas_detalhadas=[scale_fois, scale_doss],
            cadeia_sequencial=[
                make_chain_step(1, "RM07-P1", "iTBS Hemisfério Lesado", "iTBS — M1 Suprahioideo Lesado (Tai et al., 2023)", "iTBS", "M1 suprahioideo lesado (2–4 cm frente Cz, 4–6 cm lateral)", "iTBS: 3 pulsos a 50 Hz (200 ms), 2 s trem a cada 120 s (200 s total) | 600 pulsos | 80% LMR", sessoes="20 sessões (1×/dia, 5 dias/sem, 4 semanas)", efeito_esperado="Melhora de 22% na SSA, 16,15% OMFS e 80% PAS", referencia="Tai et al. (2023) · DOI: 10.23736/S1973-9087.23.08023-1"),
                make_chain_step(2, "RM07-P2", "5 Hz M1 Lesado", "HF-rTMS 5 Hz — M1 Suprahioideo Lesado (Zhong et al., 2021)", "HF-rTMS (5 Hz)", "M1 suprahioideo lesado", "5 Hz | 110% LMR | 1.800 pulsos", sessoes="10 sessões (1×/dia, 5 dias/sem, 2 semanas)", efeito_esperado="Melhora em FEDSS, PAS, SSA e GUSS (+23,54% SSA)", referencia="Zhong et al. (2021) · DOI: 10.3389/fneur.2021.625683"),
                step_disf_p3, step_disf_p4, step_disf_p5, step_p9_bi, step_alt_a, step_alt_b,
            ],
            ajuste_parametros=adj_disf_rtms, falha_terapeutica=falha_disf, sessoes_ajuste=sa_disf,
            notas_clinicas="Em lesão cortical não extensa, prioriza-se a estimulação excitatória direta do M1 suprahioideo lesado; em resposta insatisfatória, escalona-se para o hemisfério não lesado e cerebelo bilateral antes da seção de Ajustes.",
            audit_meta=_audit("Moderada", "Metanálise iTBS disfagia pós-AVC (Han et al., 2024).", "Seleção e risco de viés em duplicata.", ["Risco de viés"], "Moderada", "Condicional", "Forte consistência em 5–10 sessões com fonoterapia especializada.", tol_disf),
        ),
        "rtms_cortical_extensa": make_mod(
            protocolo_id="RM07-P3", tecnica="HF-rTMS 5 Hz — M1 Suprahioideo Não Lesado", modalidade_sigla="HF-rTMS (5 Hz)",
            alvo="M1 suprahioideo do hemisfério NÃO LESADO (lesão cortical extensa)", frequencia="5 Hz", intensidade="110% LMR",
            pulsos_duracao="1.800 pulsos", sessoes="10 sessões (1×/dia, 5 dias/sem, 2 semanas)",
            escala_recomendada="FOIS / DOSS / Videodeglutograma", meta_melhora="Recrutamento corticobulbar bilateral",
            tamanho_efeito=0.58, evidencia="Nível B — Wen 2022 / Zhong 2021", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_ZHONG_2021, meta_analise=REF_WEN_2022,
            mcid_valor=1.0, mcid_label="+1 nível na FOIS", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Zhong et al. (2021)", efeito_resumo="Drive corticobulbar bilateral pelo hemisfério preservado",
            escalas_detalhadas=[scale_fois, scale_doss],
            cadeia_sequencial=[
                step_disf_p3, step_disf_p4, step_disf_p5, step_p9_bi, step_alt_a, step_alt_b,
            ],
            ajuste_parametros=adj_disf_rtms, falha_terapeutica=falha_disf, sessoes_ajuste=sa_disf,
            notas_clinicas="A estimulação unilateral do hemisfério não lesado ativa projeções corticobulbares bilaterais quando a extensão da lesão impede estimulação ipsilesional.",
            audit_meta=_audit("Moderada", "Metanálise disfagia (Wen et al., 2022).", "Indicado quando lesão cortical impede estimulação direta.", ["Risco de viés"], "Moderada", "Condicional", "Drive corticobulbar compensatório.", tol_disf),
        ),
        "tempo_transito": make_mod(
            protocolo_id="RM07-P6", tecnica="HF-rTMS 5 Hz — Cerebelo Unilateral", modalidade_sigla="rTMS Cerebelo Uni",
            alvo="Cerebelo unilateral (1–2 cm abaixo do ínion e 3–4 cm lateralmente)", frequencia="5 Hz", intensidade="110% LMR",
            pulsos_duracao="1.800 pulsos", sessoes="10 sessões (1×/dia, 5 dias/sem, 2 semanas)",
            escala_recomendada="FOIS / DOSS / Videodeglutograma", meta_melhora="+39,25% na PAS / ganho em fase faríngea",
            tamanho_efeito=0.60, evidencia="Nível B — Metanálise Cerebelar Liu 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_ZHONG_2021, meta_analise=REF_LIU_2024,
            mcid_valor=1.0, mcid_label="+1 nível na FOIS", cohen_d_valor=0.60, cohen_d_interp="Moderado",
            estudo_referencia="Zhong et al. (2021)", efeito_resumo="Melhora na fase faríngea (+39,25% PAS no cerebelo)",
            escalas_detalhadas=[scale_fois, scale_doss],
            cadeia_sequencial=[
                make_chain_step(1, "RM07-P6", "5 Hz Cerebelo Unilateral", "HF-rTMS 5 Hz — Cerebelo Unilateral (Zhong et al., 2021)", "HF-rTMS Cerebelar (5 Hz)", "Cerebelo unilateral (1–2 cm abaixo do ínion e 3–4 cm lateralmente)", "5 Hz | 110% LMR | 1.800 pulsos", sessoes="10 sessões (1×/dia, 5 dias/sem, 2 semanas)", efeito_esperado="Melhora de 39,25% na PAS em cerebelo", referencia="Zhong et al. (2021) · DOI: 10.3389/fneur.2021.625683"),
                make_chain_step(2, "RM07-P7", "10 Hz Cerebelo Contralesional", "HF-rTMS 10 Hz — Cerebelo Contralesional (Wilkinson et al., 2025)", "HF-rTMS Cerebelar (10 Hz)", "Hemisfério cerebelar contralesional (1–2 cm abaixo do ínion e 3–4 cm lateral)", "10 Hz | 90% LMR | 250 pulsos", sessoes="10 sessões (2×/dia, 5 dias/sem, 1 semana)", efeito_esperado="Aumento de 2,53 pts na Escala FOIS (IC 95%: 0,28 a 4,78)", referencia="Wilkinson et al. (2025) · DOI: 10.1007/s12311-025-01823-0", linha_fluxograma="solida"),
                step_p9_bi, step_alt_a, step_alt_b,
            ],
            ajuste_parametros=adj_disf_rtms, falha_terapeutica=falha_disf, sessoes_ajuste=sa_disf,
            notas_clinicas="Opção cerebelar unilateral para lesão cortical com foco na modulação da fase faríngea.",
            audit_meta=_audit("Moderada", "Metanálise cerebelar em disfagia pós-AVC (Liu et al., 2024).", "Avaliação sistemática específica para alvos cerebelares.", ["Risco de viés"], "Moderada", "Condicional", "Alvo cerebelar alternativo em disfagia cortical.", tol_disf),
        ),
        "rtms_tronco": make_mod(
            protocolo_id="RM07-P8", tecnica="HF-rTMS 10 Hz — Cerebelo Bilateral (Dong et al., 2022)", modalidade_sigla="rTMS Tronco",
            alvo="Cerebelo bilateral faríngeo (2,4 cm abaixo do ínion e 4,3 cm lateralmente)", frequencia="10 Hz", intensidade="80% LMR",
            pulsos_duracao="250 pulsos (1 s estímulo e 9 s intervalo; total 190 s)", sessoes="10 sessões (1×/dia, 5 dias/sem, 2 semanas)",
            escala_recomendada="FOIS / DOSS / SSA", meta_melhora="Recuperação em disfagia de tronco encefálico",
            tamanho_efeito=0.55, evidencia="Nível B — Metanálise Cerebelar Liu 2024 / Dong 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_DONG_2022, meta_analise=REF_LIU_2024,
            mcid_valor=1.0, mcid_label="+1 nível na FOIS", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Dong et al. (2022)", efeito_resumo="Melhora em PAS e FDS pós-AVC de tronco encefálico",
            escalas_detalhadas=[scale_fois, scale_doss],
            cadeia_sequencial=[
                make_chain_step(1, "RM07-P8", "10 Hz Cerebelo Bilateral (Tronco Encefálico)", "HF-rTMS 10 Hz — Cerebelo Bilateral (Dong et al., 2022)", "HF-rTMS Cerebelar Bilateral", "Cerebelo bilateral (2,4 cm abaixo do ínion e 4,3 cm lateralmente)", "10 Hz | 80% LMR | 250 pulsos (1 s estímulo e 9 s intervalo; total 190 s)", sessoes="10 sessões (1×/dia, 5 dias/sem, 2 semanas)", efeito_esperado="Melhora superior em PAS e FDS vs unilateral em AVC de tronco", referencia="Dong et al. (2022) · DOI: 10.1155/2022/6259693", linha_fluxograma="solida"),
                step_p9_bi, step_alt_a, step_alt_b,
            ],
            ajuste_parametros=adj_disf_rtms, falha_terapeutica=falha_disf, sessoes_ajuste=sa_disf,
            notas_clinicas="Indicação específica para disfagia por lesão de tronco encefálico com estimulação cerebelar faríngea bilateral.",
            audit_meta=_audit("Moderada", "Metanálise cerebelar disfagia (Liu et al., 2024).", "Indicada quando lesão é de tronco encefálico.", ["Risco de viés"], "Moderada", "Condicional", "Estimulação bilateral cerebelar superior à unilateral em AVC de tronco.", tol_disf),
        ),
        "tdcs_disf_uni": make_mod(
            protocolo_id="RM06-P1", tecnica="tDCS Anódica — C5/C6 + Ombro Direito", modalidade_sigla="tDCS Disfagia",
            alvo="Ânodo em M1 faríngeo C5/C6 + Cátodo em ombro direito (5×5 cm)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min", sessoes="10 sessões (2 semanas)",
            escala_recomendada="FOIS / DOSS / SSA / MASA (+ Videodeglutograma)", meta_melhora="Ganho ≥ 1 nível na FOIS em todas as consistências",
            tamanho_efeito=0.58, evidencia="Nível B — Metanálise Han 2024 / Wang 2023", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_WANG_2023_DYSP, meta_analise=REF_HAN_2024_DYSP,
            mcid_valor=1.0, mcid_label="+1 nível na FOIS", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Wang et al. (2023)", efeito_resumo="Melhora de SSA, PAS, oxigenação e remoção de gastrostomia",
            escalas_detalhadas=[scale_fois, scale_doss],
            cadeia_sequencial=[
                make_chain_step(1, "RM06-P1", "tDCS C5/C6 + Ombro Direito", "tDCS Anódica — C5/C6 + Ombro Direito (Wang et al., 2023)", "tDCS Anódica", "Ânodo C5/C6 + Cátodo ombro direito (5×5 cm)", "1,0 mA (opcional 1,4 mA conforme Xie et al., 2023) | 20 min", sessoes="10 sessões (2 semanas)", efeito_esperado="Redução em SSA e PAS + marcadores infecciosos/nutricionais", referencia="Wang et al. (2023) · DOI: 10.1007/s00455-023-10581-2"),
                make_chain_step(2, "RM06-P2", "tDCS C5/C6 2 mA (30 min)", "tDCS Anódica — M1 Faríngeo C5/C6 2 mA (Kumar et al., 2011)", "tDCS Anódica", "Ânodo M1 faríngeo C5/C6 (3×5 cm) + Cátodo supraorbitário contralateral (5×6 cm)", "2,0 mA | 30 min", sessoes="10 sessões", efeito_esperado="Ganho de 2,6 pontos na Escala DOSS", referencia="Kumar et al. (2011) · DOI: 10.1161/STROKEAHA.110.602128"),
                make_chain_step(3, "RM06-P3", "tDCS Giro Supramarginal CP5/CP6", "tDCS Anódica — Giro Supramarginal CP5/CP6 (Farpour et al., 2023)", "tDCS Anódica", "Ânodo CP5/CP6 (4×4 cm) + Cátodo supraorbital contralateral (4×6 cm)", "2,0 mA | 20 min", sessoes="5 a 10 sessões", efeito_esperado="27,6% retiradas de gastrostomia e ganho MASA", referencia="Farpour et al. (2023) · DOI: 10.18502/cjn.v22i3.13793", linha_fluxograma="solida"),
            ],
            ajuste_parametros=adj_disf_tdcs, falha_terapeutica=falha_disf, sessoes_ajuste=sa_disf,
            notas_clinicas="Em lesão unilateral, a estimulação anódica sobre M1 faríngeo com fonoterapia precoce favorece desmame de via alternativa de alimentação.",
            audit_meta=_audit("Moderada", "Revisão e diretriz tDCS em disfagia.", "Preditores favoráveis com menor NIHSS e estimulação precoce.", ["IFCN tDCS"], "Moderada", "Condicional", "Xie et al. (2023) sugerem 1,4 mA / 20 min como otimização clínica.", tol_disf),
            mod_tipo="tdcs",
        ),
        "tdcs_disf_bi": make_mod(
            protocolo_id="RM06-P4", tecnica="tDCS Sequencial Bihemisférica — M1 Faríngeo C5/C6", modalidade_sigla="tDCS Bilateral",
            alvo="Ânodo C5/C6 + Cátodo supraorbitário contralateral (5d dominante + 5d não dominante)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="30 min", sessoes="10 sessões em 2 semanas (5d dominante + 5d não dominante)",
            escala_recomendada="FOIS / DOSS / Videodeglutograma", meta_melhora="+5 pts DOSS / -70% aspiração",
            tamanho_efeito=0.52, evidencia="Nível B/C — Sawan 2020 / Wen 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_SAWAN_2020, meta_analise=REF_WEN_2022,
            mcid_valor=1.0, mcid_label="+1 nível na FOIS", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Sawan et al. (2020)", efeito_resumo="Ganho funcional de 5 pts na DOSS e redução de 70% de aspiração",
            escalas_detalhadas=[scale_fois, scale_doss],
            cadeia_sequencial=[
                make_chain_step(1, "RM06-P4", "tDCS Sequencial Bilateral (5d + 5d)", "tDCS Sequencial — 5d Dominante + 5d Não Dominante (Sawan et al., 2020)", "tDCS Sequencial Bilateral", "Ânodo C5/C6 + Cátodo supraorbitário contralateral (5d dom + 5d não dom)", "2,0 mA | 30 min", sessoes="10 sessões (2 semanas)", efeito_esperado="+5 pontos DOSS e redução de 70% na aspiração", referencia="Sawan et al. (2020) · DOI: 10.1186/s41983-020-00246-4"),
                make_chain_step(2, "RM06-ALTA", "Seção de Ajustes — tDCS Bihemisférica Simultânea", "tDCS Bihemisférica Simultânea (Ahn et al., 2017)", "tDCS Bilateral", "Ânodos em córtex faríngeo bilateral + cátodos supraorbitários contralaterais (5×5 cm)", "1,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="+0,62 pts na escala DOSS", referencia="Ahn et al. (2017) · DOI: 10.2340/16501977-2170", linha_fluxograma="solida", fase_etapa="ajustes"),
                step_alt_b,
            ],
            ajuste_parametros=adj_disf_tdcs, falha_terapeutica=falha_disf, sessoes_ajuste=sa_disf,
            notas_clinicas="Alternar hemisférios (5d dominante na 1ª semana + 5d não dominante na 2ª semana) em lesões bilaterais.",
            audit_meta=_audit("Moderada", "Metanálise disfagia pós-AVC (Wen et al., 2022).", "Preditores clínicos Sawan et al. (2020).", ["Risco de viés"], "Baixa", "Condicional", "Alternar hemisférios antes da etapa de ajustes e tAVNS.", tol_disf),
            mod_tipo="tdcs",
        ),
    }

    arvore_rtms = {
        "roadmap_id": "RM07",
        "titulo_fluxograma": "AVC Disfagia Neurogênica — rTMS / iTBS / cTBS / tAVNS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é a gravidade e natureza da Disfagia pós-AVC (TMS)?",
                "subtitulo": "Avalie se a lesão envolve componentes corticais/subcorticais e se há alteração cognitiva ou de linguagem associada.",
                "opcoes": [{"id": "orofaringea", "rotulo": "Gravidade da Disfagia Orofaríngea", "criterio": "FOIS / DOSS / MASA / SSA", "descricao": "Seguir para topografia da lesão.", "proxima_etapa": "topografia_lesao"}],
            },
            "topografia_lesao": {
                "pergunta": "Qual é a localização predominante da lesão em neuroimagem?",
                "subtitulo": "Define a bifurcação entre Lesão Cortical e Lesão de Tronco Encefálico.",
                "opcoes": [
                    {"id": "lesao_cortical", "rotulo": "Lesão Cortical", "criterio": "Hemisférica cortical / subcortical", "descricao": "Avaliar extensão cortical e viabilidade de M1 suprahioideo ou Cerebelo.", "proxima_etapa": "lesao_extensa_disf"},
                    {"id": "lesao_tronco", "rotulo": "Lesão de Tronco Encefálico", "criterio": "Bulbar / Pontina", "descricao": "Encaminha para estimulação cerebelar bilateral faríngea (10 Hz Dong 2022).", "protocolo_alvo": "rtms_tronco"},
                ],
            },
            "lesao_extensa_disf": {
                "pergunta": "Trata-se de lesão cortical extensa (considerando escolha do hemisfério)?",
                "subtitulo": "Selecione Não (hemisfério lesado), Sim (não lesado) ou a rota cerebelar unilateral.",
                "opcoes": [
                    {"id": "disf_ext_nao", "rotulo": "NÃO — Lesão Cortical Não Extensa", "criterio": "M1 suprahioideo lesado preservado", "descricao": "Inicia com iTBS em M1 suprahioideo do hemisfério lesado (Tai et al., 2023).", "protocolo_alvo": "orofaringea"},
                    {"id": "disf_ext_sim", "rotulo": "SIM — Lesão Cortical Extensa", "criterio": "Estimular hemisfério não lesado", "descricao": "Inicia com HF-rTMS 5 Hz em M1 suprahioideo do hemisfério não lesado (Zhong et al., 2021).", "protocolo_alvo": "rtms_cortical_extensa"},
                    {"id": "disf_cerebelo_ou", "rotulo": "OU — Rota Cerebelar Unilateral", "criterio": "Opção cerebelar", "descricao": "Inicia com HF-rTMS 5 Hz em cerebelo unilateral (Zhong et al., 2021).", "protocolo_alvo": "tempo_transito"},
                ],
            },
        },
        "ajuste_parametros": adj_disf_rtms,
        "protocolo_alternativo": {
            "nome": "iTBS Faríngea C6 Direita (Cosentino et al., 2020) — Seção de Ajustes",
            "tecnica": "iTBS", "alvo": "Representação cortical faríngea (C6 direita)", "parametros": "600 pulsos | 70% LMR | 5 sessões",
            "observacoes": "Estudo clínico fora de metanálises consolidadas (+2 pts DOSS).",
        },
        "protocolo_alternativo_2": {
            "nome": "tAVNS Auricular (Wang et al., 2023) — Seção de Ajustes",
            "tecnica": "tAVNS", "alvo": "Nervos vagais auriculares (fase aguda)", "parametros": "Intensidade conforme tolerância | 30 min (2×/dia, 5 d/sem, 3 sem)",
            "observacoes": "Estímulo vagal periférico não invasivo antes da falha terapêutica.",
        },
        "falha_terapeutica": {
            "id": "RM07-FALHA", "titulo": "Falha Terapêutica em rTMS Disfagia",
            "criterios_definicao": "Ausência de resposta em até 5 dias após avaliar TODAS as consistências alimentares (líquido, pastoso e sólido) e percorrer as alternativas previstas.",
            "descricao": "Documentar com escalas clínicas (FOIS/DOSS/SSA) e avaliação instrumental (videodeglutograma) pré e pós.",
            "condutas": ["Verificar se cada consistência alimentar foi testada isoladamente.", "Considerar transição para tDCS / tAVNS em Disfagia pós-AVC ou manejo fonoaudiológico compensatório."],
        },
    }

    arvore_tdcs = {
        "roadmap_id": "RM06",
        "titulo_fluxograma": "AVC Disfagia Neurogênica — tDCS / tAVNS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é a lateralidade da lesão na Disfagia pós-AVC (tDCS)?",
                "subtitulo": "Estimulação unilateral também pode aumentar o drive corticobulbar bilateral.",
                "opcoes": [
                    {"id": "disf_tdcs_uni", "rotulo": "Lesão Unilateral", "criterio": "FOIS / DOSS + Lateralidade unilateral", "descricao": "Inicia com tDCS anódica M1 faríngeo C5/C6 + ombro direito (Wang et al., 2023).", "protocolo_alvo": "tdcs_disf_uni"},
                    {"id": "disf_tdcs_bi", "rotulo": "Lesão Bilateral", "criterio": "Acometimento bihemisférico", "descricao": "Inicia com tDCS sequencial bilateral 5d dominante + 5d não dominante (Sawan et al., 2020).", "protocolo_alvo": "tdcs_disf_bi"},
                ],
            },
        },
        "ajuste_parametros": adj_disf_tdcs,
        "protocolo_alternativo": {
            "nome": "tDCS Bihemisférica Simultânea (Ahn et al., 2017) — Seção de Ajustes",
            "tecnica": "tDCS Bilateral", "alvo": "Representação faríngea bilateral", "parametros": "1,0 mA | 20 min | eletrodos 5×5 cm",
            "observacoes": "Opção bihemisférica simultânea em lesão bilateral.",
        },
        "protocolo_alternativo_2": {
            "nome": "tAVNS Auricular (Wang et al., 2023) — Seção de Ajustes",
            "tecnica": "tAVNS", "alvo": "Ramo auricular do nervo vago (fase aguda)", "parametros": "Intensidade conforme tolerância | 30 min (2×/dia, 5 d/sem, 3 sem)",
            "observacoes": "Estímulo vagal auricular antes da falha terapêutica.",
        },
        "falha_terapeutica": {
            "id": "RM06-FALHA", "titulo": "Falha Terapêutica em tDCS Disfagia",
            "criterios_definicao": "Ausência de resposta em até 5 dias após testar TODAS as consistências alimentares (líquido, pastoso e sólido).",
            "descricao": "Documentar avaliações clínicas e instrumentais pré e pós.",
            "condutas": ["Testar cada consistência alimentar antes de considerar falha.", "Considerar transição para rTMS/iTBS em Disfagia pós-AVC."],
        },
    }

    obs_disf = [
        make_obs("RM07-PRE-TRIAGEM", "Atenção às contraindicações (implantes metálicos cerebrais, histórico de convulsões não controladas e implantes cocleares). Avaliar se a lesão envolve componentes corticais/subcorticais e se há alteração cognitiva ou de linguagem associada. Melhores resultados na fase aguda/subaguda (1–6 meses).", "pre", categoria="seguranca", severidade="warning"),
        make_obs("RM07-STEP-HEMISF", "Na escolha do hemisfério, considerar o tamanho da lesão cortical. A estimulação unilateral pode aumentar o drive corticobulbar bilateral; menor NIHSS e estimulação precoce são preditores positivos (Sawan et al., 2020).", "step", categoria="clinica", etapa_ids=["lesao_extensa_disf", "fator_limitante"]),
        make_obs("RM07-TBS-VANTAGEM", "Theta-Burst (TBS: iTBS/cTBS) apresenta vantagem operacional de requerer menos tempo de sessão e menor intensidade para atingir os mesmos efeitos clínicos vs. rTMS convencional.", "tec", categoria="clinica", protocolo_ids=["orofaringea", "rtms_cortical_extensa", "tempo_transito", "rtms_tronco"], modalidades_tipo=["rtms"]),
        make_obs("RM07-COORD-SUPRA", "Coordenada anatômica suprahioidea: 2–4 cm à frente de Cz e 4–6 cm lateralmente.", "alvo", categoria="anatomia", protocolo_ids=["orofaringea", "rtms_cortical_extensa"], modalidades_tipo=["rtms"]),
        make_obs("RM07-COORD-CER-UNI", "Coordenada anatômica cerebelo unilateral: 1–2 cm abaixo do ínion e 3–4 cm lateralmente.", "alvo", categoria="anatomia", protocolo_ids=["tempo_transito"], modalidades_tipo=["rtms"]),
        make_obs("RM07-COORD-CER-BI", "Coordenada anatômica cerebelo bilateral faríngeo: 2,4 cm abaixo do ínion e 4,3 cm lateralmente.", "alvo", categoria="anatomia", protocolo_ids=["rtms_tronco"], estagios=["primary"], modalidades_tipo=["rtms"]),
        make_obs("RM07-EXAMES-SCALE", "Recomenda-se realizar avaliações clínicas, escalas (FOIS/DOSS) e exames instrumentais (videodeglutograma) pré e pós-intervenção.", "scale", categoria="avaliacao"),
    ]

    return {
        "id": cid, "condicao": "Acidente Vascular Cerebral — Disfagia Orofaríngea", "eixo": "Doenças Cerebrovasculares",
        "roadmap_id": "RM07", "svg_file": "RM07.svg",
        "fatores_limitantes": [
            {"id": "orofaringea", "nome": "Gravidade da Disfagia Orofaríngea", "instrumento_sugerido": "FOIS / DOSS / MASA / SSA", "descricao": "Risco de aspiração, penetração laríngea e restrição de via oral."},
        ],
        "arvore_algoritmo": arvore_rtms, "arvores_por_modalidade": {"rtms": arvore_rtms, "tdcs": arvore_tdcs},
        "observacoes_contextuais": obs_disf, "modalidades": modalidades, "tags_busca": tags,
    }


def _build_avc_afasia():
    cid = "avc-afasia"
    tags = {
        "siglas": ["AVC", "AVE", "GFI", "MTL", "WAB", "BNT", "tsDCS"],
        "coordenadas_10_20": ["F5", "F6", "FC5", "FC6", "CP5", "CP6", "C3", "T3", "T4", "T10"],
        "alvos_anatomicos": ["Giro Frontal Inferior (Broca)", "Região Temporoparietal (Wernicke)", "M1 Esquerdo (C3)", "Cerebelo", "Medular Torácica (T10)"],
        "sinonimos_en": ["stroke", "aphasia", "broca aphasia", "non-fluent aphasia", "wernicke aphasia", "anomia", "language rehabilitation"],
        "sintomas_pt": ["afasia", "linguagem", "fala espontânea", "anomia", "repetição", "compreensão", "afasia de expressão", "afasia de compreensão"],
        "escalas": ["MTL-Brasil", "BNT", "WAB", "WAB-R", "Token Test"], "tecnicas": ["rTMS", "iTBS", "cTBS", "tDCS", "tsDCS Medular"],
    }
    tol_af = _tol_profile(
        "Realizar triagem de contraindicações (implantes metálicos cerebrais, implantes cocleares, histórico de convulsões não controladas e EEG/exames de imagem quando pertinentes) antes de iniciar protocolos excitatórios.",
        "Reduzir para 80% do LMR caso haja espasmo ou desconforto no músculo temporal durante estimulação à esquerda (F5 / CP5).",
        "Exames de imagem (RNM com tractografia, EEG, TC), dominância hemisférica (Inventário de Edimburgo) e presença de tecido viável remanescente.",
    )
    scale_mtl = make_scale("mtl_brasil", "Bateria Montreal-Toulouse — MTL-Brasil", "MTL-Brasil", "aumento", "Melhora em fluência, nomeação (anomia), repetição ou compreensão em 5 sessões (validada para o Brasil)", 0.58, placeholder="Ex: 52", min_val=0, max_val=100, mcid_valor=5.0, mcid_label="+5,0 pts na MTL-Brasil")
    scale_wab = make_scale("wab", "Western Aphasia Battery / Nomeação (BNT / Token Test)", "WAB / Token Test", "aumento", "Evolução em microdesfechos específicos de linguagem combinada à fonoterapia estruturada", 0.54, placeholder="Ex: 55", min_val=0, max_val=100, mcid_valor=5.0, mcid_label="+5,0 pontos no WAB-AQ")

    step_rtms_c3 = make_chain_step(4, "RM09-ALT1", "iTBS M1-E C3 (Pontilhado)", "iTBS — M1 Esquerdo C3 (Xu et al., 2021)", "iTBS (Pontilhado)", "C3 (Área Motora Primária esquerda)", "iTBS: 3 pulsos a 50 Hz repetidos a 5 Hz, 2 s estímulo e 8 s pausa | 80% LMR | 800 pulsos por sessão", sessoes="≥ 15 sessões", efeito_esperado="Melhora articulatória, fluência verbal e nomeação", referencia="Xu et al. (2021) · DOI: 10.3390/brainsci11111451", linha_fluxograma="pontilhada", fase_etapa="ajustes")
    step_rtms_cer = make_chain_step(5, "RM09-ALT2", "cTBS Cerebelo Lateral Direito (Pontilhado)", "cTBS — Cerebelar Lateral Direito (Zheng et al., 2022)", "cTBS Cerebelar (Pontilhado)", "Cerebelo lateral direito (3 cm à direita do vérmis e 1 cm inferior ao ínion)", "cTBS com rajadas de 3 pulsos a 50 Hz, 600 pulsos em 40 s | bobina em figura de 8 (7 cm) | 80% LMR", sessoes="≥ 15 sessões", efeito_esperado="Recuperação de palavras, nomeação e processamento semântico", referencia="Zheng et al. (2022) · DOI: 10.3389/fnagi.2022.909733", linha_fluxograma="pontilhada", fase_etapa="ajustes")
    step_tdcs_m1 = make_chain_step(3, "RM08-ALT1", "tDCS M1-E C3 (Pontilhado)", "tDCS Anódica — M1-E C3 (Meinzer et al., 2016)", "tDCS M1-E (Pontilhado)", "C3 (M1 esquerdo — ânodo 5×7 cm² + cátodo 10×10 cm² supraorbital D)", "1,0 mA | 20 min durante treino linguístico intensivo", sessoes="≥ 15 sessões (2×/dia, 4 d/sem, 2 sem)", efeito_esperado="Melhora na nomeação de material treinado e comunicação cotidiana", referencia="Meinzer et al. (2016) · DOI: 10.1093/brain/aww002", linha_fluxograma="pontilhada", fase_etapa="ajustes")
    step_tdcs_med = make_chain_step(4, "RM08-ALT2", "tsDCS Medular T10 (Pontilhado)", "tsDCS Medular — T10 (Marangolo et al., 2017)", "tsDCS Medular (Pontilhado)", "T10 (10ª vértebra torácica — ânodo 5×7 cm² abrangendo T9–T11 + cátodo 5×7 cm² deltoide D)", "2,0 mA | 20 min", sessoes="≥ 15 sessões", efeito_esperado="Melhora em nomeação de substantivos vs verbos", referencia="Marangolo et al. (2017) · DOI: 10.3389/fneur.2017.00400", linha_fluxograma="pontilhada", fase_etapa="ajustes")

    adj_af_rtms = {"titulo": "Ajustes Neuroanatômicos e Ordem Sequencial (Afasia)", "tolerabilidade": "Confirmar EEG e contraindicações antes de protocolos excitatórios à esquerda (F5 / CP5 / Dual).", "dose_pulsos": "Aplicar ciclos com ≥ 15 sessões para maior tamanho de efeito. Na estimulação bilateral de expressão (FC6+F6 / FC5+F5), realizar 1 Hz contralesional obrigatoriamente ANTES de 20 Hz lesional.", "calibracao_limiar": "Alta frequência à esquerda (F5 / CP5 / Dual F5+CP5) requer tecido viável remanescente documentado em RNM."}
    adj_af_tdcs = {"titulo": "Ajustes de Lateralidade e Montagens Simultâneas em tDCS (Afasia)", "tolerabilidade": "Em lesões extensas envolvendo múltiplas áreas nos exames de imagem, preferir inibição contralateral (CP6).", "dose_pulsos": "Aplicar ciclos com ≥ 15 sessões para maior tamanho de efeito; na estimulação dual em GFI (F5/F6), aplicar os eletrodos simultaneamente.", "calibracao_limiar": "Considerar extensão da lesão cortical e dominância hemisférica (Inventário de Edimburgo) ao escolher a montagem."}
    falha_af = _falha_mod("Ausência de resposta clínica em TODOS os microdesfechos avaliados após 5 sessões com protocolo indicado, adesão confirmada e fonoterapia estruturada.", "1. Verificar RNM/tractografia, tecido viável e dominância hemisférica (Inventário de Edimburgo);\n2. Ajustar estratégia hemisférica (excitação de tecido viável vs inibição contralateral);\n3. Considerar alternância entre rTMS/iTBS/cTBS e tDCS/tsDCS medular para Afasia pós-AVC.")
    sa_af = _sessoes_aj("Ausência de resposta clínica em TODOS os microdesfechos linguísticos após 5 sessões com protocolo indicado e adesão confirmada.", "Associar obrigatoriamente terapia fonoaudiológica estruturada direcionada ao microdesfecho de linguagem.", "Interromper ao atingir platô funcional linguístico sustentado.")

    modalidades = {
        "expressao": make_mod(
            protocolo_id="RM09-EXP", tecnica="LF-rTMS 1 Hz — F6 Contralesional (GFI)", modalidade_sigla="rTMS Afasia Expressão",
            alvo="F6 (Giro Frontal Inferior contralesional)", frequencia="1 Hz", intensidade="80% LMR",
            pulsos_duracao="1.000 pulsos (50 pulsos/trem, 20 trens, 10 s intervalo)", sessoes="≥ 15 sessões associadas à fonoterapia estruturada",
            escala_recomendada="MTL-Brasil / WAB / BNT", meta_melhora="Ganho em fala espontânea, anomia e repetição",
            tamanho_efeito=0.58, evidencia="Nível B — Metanálise em rede Ding 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_REN_2019, meta_analise=REF_DING_2022,
            mcid_valor=5.0, mcid_label="+5,0 pts na MTL-Brasil", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Ren et al. (2019)", efeito_resumo="+163,3% WAB-AQ, +362,9% fala espontânea e +144,2% repetição",
            escalas_detalhadas=[scale_mtl, scale_wab],
            cadeia_sequencial=[
                make_chain_step(1, "RM09-EXP-P1", "1 Hz F6 Contralesional (GFI)", "LF-rTMS 1 Hz — F6 Contralesional (Ren et al., 2019)", "LF-rTMS (1 Hz)", "F6 (GFI contralesional)", "1 Hz | 80% LMR | 1.000 pulsos (50 pulsos/trem, 20 trens, 10 s intervalo)", sessoes="≥ 15 sessões", efeito_esperado="+163,3% WAB, +362,9% fala espontânea", referencia="Ren et al. (2019) · DOI: 10.1155/2019/4589056"),
                make_chain_step(2, "RM09-EXP-P2", "10 Hz F5 Ipsilesional (GFI)", "HF-rTMS 10 Hz — F5 Ipsilesional (Liu et al., 2021)", "HF-rTMS (10 Hz)", "F5 (GFI esquerdo lesional — requer tecido viável)", "10 Hz | 90% LMR | 1.200 pulsos (60 pulsos/trem, 20 trens, 15 s intervalo)", sessoes="≥ 15 sessões", efeito_esperado="+282,9% ASRS com manutenção 1–2 meses", referencia="Liu et al. (2021) · DOI: 10.3969/j.issn.1001-568X.2021.05.0030"),
                make_chain_step(3, "RM09-EXP-P3", "Dual Sequencial (FC6+F6 seguido de FC5+F5)", "rTMS Bilateral Sequencial — FC6+F6 seguido de FC5+F5 (Khedr et al., 2014)", "rTMS Bilateral Sequencial", "2 cm caudal a F6 (FC6) e F6 seguido de 2 cm caudal a F5 (FC5) e F5", "1 Hz (1.000 p, 110% LMR: 500 FC6 + 500 F6) ANTES de 20 Hz (FC5 + F5)", sessoes="≥ 15 sessões", efeito_esperado="Melhora em fala espontânea e nomeação (WAB)", referencia="Khedr et al. (2014) · DOI: 10.1177/1545968314521009"),
                step_rtms_c3, step_rtms_cer,
            ],
            ajuste_parametros=adj_af_rtms, falha_terapeutica=falha_af, sessoes_ajuste=sa_af,
            notas_clinicas="Exames de imagem (RNM tractografia/TC) e Inventário de Edimburgo orientam a seleção do hemisfério antes de optar por estimulação excitatória ipsilesional.",
            audit_meta=_audit("Moderada", "Metanálise em rede NIBS para afasia (Ding et al., 2022).", "Comparação e metarregressão por moderadores clínicos.", ["Análise em rede", "Risco de viés"], "Moderada", "Condicional", "Base sólida para 1 Hz F6; F5 exige tecido viável.", tol_af),
        ),
        "compreensao": make_mod(
            protocolo_id="RM09-COMP", tecnica="LF-rTMS 1 Hz — CP6 Contralesional (Temporoparietal)", modalidade_sigla="rTMS Afasia Compreensão",
            alvo="CP6 (Região temporoparietal direita)", frequencia="1 Hz", intensidade="80% LMR",
            pulsos_duracao="1.200 pulsos (60 pulsos/trem, 20 trens, 10 s intervalo, 20 min)", sessoes="≥ 15 sessões associadas à fonoterapia estruturada",
            escala_recomendada="MTL-Brasil / Token Test / WAB", meta_melhora="Melhora em compreensão auditiva, nomeação e repetição",
            tamanho_efeito=0.55, evidencia="Nível B — Metanálise Han 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_REN_2019, meta_analise=REF_HAN_2024_AF,
            mcid_valor=5.0, mcid_label="+5,0 pts na MTL-Brasil", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Ren et al. (2019)", efeito_resumo="+130,3% compreensão WAB e +107,4% repetição",
            escalas_detalhadas=[scale_mtl, scale_wab],
            cadeia_sequencial=[
                make_chain_step(1, "RM09-COMP-P1", "1 Hz CP6 Contralesional (Temporoparietal)", "LF-rTMS 1 Hz — CP6 Contralesional (Ren et al., 2019)", "LF-rTMS (1 Hz)", "CP6 (Região temporoparietal direita)", "1 Hz | 80% LMR | 1.200 pulsos (60 pulsos/trem, 20 trens, 10 s intervalo, 20 min)", sessoes="≥ 15 sessões", efeito_esperado="+130,3% compreensão e +107,4% repetição na WAB", referencia="Ren et al. (2019) · DOI: 10.1155/2019/4589056"),
                make_chain_step(2, "RM09-COMP-P2", "10 Hz CP5 Ipsilesional (Temporoparietal)", "HF-rTMS 10 Hz — CP5 Ipsilesional (Ren et al., 2019)", "HF-rTMS (10 Hz)", "CP5 (com tecido viável remanescente)", "10 Hz | 80% LMR | 1.200 pulsos (60 pulsos/trem, 20 trens, 10 s intervalo, 20 min)", sessoes="≥ 15 sessões", efeito_esperado="Melhora em compreensão (130,3%), fala espontânea (66,5%) e repetição (107,4%) na WAB", referencia="Ren et al. (2019) · DOI: 10.1155/2019/4589056"),
                make_chain_step(3, "RM09-COMP-P3", "Dual 10 Hz F5 + CP5 Ipsilesional", "HF-rTMS Multissítio — Dual F5 + CP5 (Liu et al., 2021)", "HF-rTMS Multissítio", "F5 + CP5 ipsilesional", "10 Hz | 90% LMR | 1.200 pulsos (60 pulsos/trem, 20 trens, 10 s intervalo, 20 min)", sessoes="≥ 15 sessões", efeito_esperado="Apoio combinado frontal e temporal para fala e compreensão", referencia="Liu et al. (2021) · DOI: 10.3969/j.issn.1001-568X.2021.05.0030"),
                step_rtms_cer,
            ],
            ajuste_parametros=adj_af_rtms, falha_terapeutica=falha_af, sessoes_ajuste=sa_af,
            notas_clinicas="Na Afasia de Compreensão, após falha dos alvos temporoparietais e frontais, a seção de ajustes indica cTBS Cerebelar lateral direito.",
            audit_meta=_audit("Moderada", "Metanálise NIBS + terapia de linguagem (Han et al., 2024).", "Risco de viés avaliado; integração à fonoterapia.", ["Risco de viés"], "Moderada", "Condicional", "Considerar extensão da lesão antes de optar por HF-rTMS esquerda.", tol_af),
        ),
        "tdcs_expressao_gfi": make_mod(
            protocolo_id="RM08-GFI", tecnica="tDCS Anódica — F5 Esquerdo + Deltoide Direito", modalidade_sigla="tDCS GFI",
            alvo="Ânodo F5 esquerdo (10 cm²) + Cátodo sobre deltoide direito (10 cm²)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min", sessoes="20 sessões (4 semanas)",
            escala_recomendada="MTL-Brasil + WAB / BNT", meta_melhora="Ganho em nomeação, fala espontânea e precisão articulatória",
            tamanho_efeito=0.54, evidencia="Nível B — Revisão Sistemática Biou 2019", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_ZHAO_2021, meta_analise=REF_BIOU_2019,
            mcid_valor=5.0, mcid_label="+5,0 pts na MTL-Brasil", cohen_d_valor=0.54, cohen_d_interp="Moderado",
            estudo_referencia="Zhao et al. (2021)", efeito_resumo="Melhora em fluência, nomeação e repetição (WAB)",
            escalas_detalhadas=[scale_mtl, scale_wab],
            cadeia_sequencial=[
                make_chain_step(1, "RM08-GFI-P1", "tDCS Anódica F5 + Deltoide Direito", "tDCS Anódica — F5 + Deltoide Direito (Zhao et al., 2021)", "tDCS Anódica", "Ânodo F5 esquerdo (10 cm²) + Cátodo sobre deltoide direito (10 cm²)", "2,0 mA | 20 min", sessoes="20 sessões (4 semanas)", efeito_esperado="Melhora em nomeação, fluência e repetição na WAB", referencia="Zhao et al. (2021) · DOI: 10.1111/ner.13337"),
                make_chain_step(2, "RM08-GFI-P2", "tDCS Dual Simultânea F5 / F6", "tDCS Bilateral Simultânea — F5 / F6 (Marangolo et al., 2016)", "tDCS Bilateral Simultânea", "Ânodo F5 (5×7 cm²) + Cátodo F6 (5×7 cm²) — simultâneo", "2,0 mA | 20 min", sessoes="≥ 15 sessões", efeito_esperado="Recuperação articulatória e conectividade inter-hemisférica", referencia="Marangolo et al. (2016) · DOI: 10.1162/jocn_a_00927"),
                step_tdcs_m1, step_tdcs_med,
            ],
            ajuste_parametros=adj_af_tdcs, falha_terapeutica=falha_af, sessoes_ajuste=sa_af,
            notas_clinicas="Em lesões extensas envolvendo múltiplas áreas, preferir inibição contralateral (CP6/F6).",
            audit_meta=_audit("Moderada", "Revisão sistemática em tDCS na afasia pós-AVC (Biou et al., 2019).", "Detalhamento de montagens anódicas e duais simultâneas.", ["Revisão Sistemática"], "Moderada", "Condicional", "Considerar extensão de lesão para escolher lateralidade.", tol_af),
            mod_tipo="tdcs",
        ),
        "tdcs_compreensao_tp": make_mod(
            protocolo_id="RM08-TP", tecnica="tDCS Anódica Temporal — CP5 (Wernicke)", modalidade_sigla="tDCS Temporal",
            alvo="Ânodo CP5 (5×7 cm²) + Cátodo supraorbital contralateral (5×7 cm²)", frequencia="Contínua", intensidade="1,0 mA",
            pulsos_duracao="20 min", sessoes="15 sessões (5 d/sem, 3 sem)",
            escala_recomendada="MTL-Brasil + Token Test", meta_melhora="Melhora em compreensão auditiva e nomeação semântica",
            tamanho_efeito=0.52, evidencia="Nível B — Biou 2019 / Fiori 2013", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_FIORI_2013, meta_analise=REF_BIOU_2019,
            mcid_valor=5.0, mcid_label="+5,0 pts na MTL-Brasil", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Fiori et al. (2013)", efeito_resumo="Melhora em nomeação de substantivos e compreensão verbal",
            escalas_detalhadas=[scale_mtl, scale_wab],
            cadeia_sequencial=[
                make_chain_step(1, "RM08-TP-P1", "tDCS Anódica CP5 (Wernicke)", "tDCS Anódica Temporal — CP5 (Fiori et al., 2013)", "tDCS Anódica Temporal", "Ânodo CP5 (5×7 cm²) + Cátodo supraorbital contralateral (5×7 cm²)", "1,0 mA | 20 min", sessoes="15 sessões (5 d/sem, 3 sem)", efeito_esperado="Melhora na nomeação de substantivos", referencia="Fiori et al. (2013) · DOI: 10.3389/fnhum.2013.00269"),
                make_chain_step(2, "RM08-TP-P2", "tDCS Catódica CP6 Contralateral", "tDCS Catódica Contralateral — CP6 (You et al., 2011)", "tDCS Catódica Contralateral", "Cátodo CP6 (5×7 cm²) + Ânodo supraorbital E (5×7 cm²)", "2,0 mA | 30 min", sessoes="≥ 10–15 sessões", efeito_esperado="Melhora na compreensão verbal (WAB/Token)", referencia="You et al. (2011) · DOI: 10.1016/j.bandl.2011.05.002"),
                step_tdcs_med,
            ],
            ajuste_parametros=adj_af_tdcs, falha_terapeutica=falha_af, sessoes_ajuste=sa_af,
            notas_clinicas="Em lesões extensas esquerdas envolvendo múltiplas áreas, preferir montagem catódica contralateral (CP6).",
            audit_meta=_audit("Moderada", "Revisão sistemática tDCS na afasia (Biou et al., 2019).", "Diferencia estimulação esquerda vs inibição direita por imagem.", ["Revisão Sistemática"], "Moderada", "Condicional", "Montagem catódica contralateral em lesões extensas.", tol_af),
            mod_tipo="tdcs",
        ),
        "tdcs_cerebelo_anomia": make_mod(
            protocolo_id="RM08-CER", tecnica="tDCS Cerebelar Catódica — Cerebelo Direito (Sebastian et al., 2020)", modalidade_sigla="tDCS Cerebelar",
            alvo="Cátodo 1 cm abaixo e 4 cm lateral ao ínion (cerebelo D, 5×5 cm²) + Ânodo deltoide direito", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min", sessoes="15 sessões com treino simultâneo de nomeação",
            escala_recomendada="MTL-Brasil (Nomeação / Anomia)", meta_melhora="Ganho em nomeação e fluência fonêmica",
            tamanho_efeito=0.48, evidencia="Nível B/C — Alvo cerebelar para anomia (Sebastian et al., 2020)", linha_fluxograma="solida",
            diretriz_internacional="Nível B/C (Lefaucheur et al., 2017)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_MEINZER_2016, meta_analise=REF_BIOU_2019,
            mcid_valor=5.0, mcid_label="+5,0 pts na MTL-Brasil", cohen_d_valor=0.48, cohen_d_interp="Moderado",
            estudo_referencia="Sebastian et al. (2020) / Meinzer et al. (2016)", efeito_resumo="Melhora na nomeação de itens treinados/não treinados e geração de verbos",
            escalas_detalhadas=[scale_mtl, scale_wab],
            cadeia_sequencial=[
                make_chain_step(1, "RM08-CER-P1", "tDCS Cerebelar Catódica", "tDCS Cerebelar Catódica — Cerebelo Direito (Sebastian et al., 2020)", "tDCS Cerebelar Catódica", "Cátodo 1 cm abaixo e 4 cm lateral ao ínion (cerebelo D, 5×5 cm²) + Ânodo deltoide direito", "2,0 mA | 20 min", sessoes="15 sessões", efeito_esperado="Nomeação de itens treinados/não treinados e geração de verbos", referencia="Sebastian et al. (2020) · DOI: 10.1093/braincomms/fcaa179", linha_fluxograma="solida"),
                make_chain_step(2, "RM08-CER-P2", "tDCS Cerebelar Anódica", "tDCS Cerebelar Anódica — Rampa 15 s (Sebastian et al., 2020)", "tDCS Cerebelar Anódica", "Ânodo 1 cm abaixo e 4 cm lateral ao ínion (cerebelo D, 5×5 cm²) + Cátodo deltoide D", "2,0 mA | 20 min | rampa de subida e descida 15 s", sessoes="15 sessões", efeito_esperado="Melhora em fluência fonêmica e nomeação", referencia="Sebastian et al. (2020) · DOI: 10.1093/braincomms/fcaa179", linha_fluxograma="solida"),
                step_tdcs_m1, step_tdcs_med,
            ],
            ajuste_parametros=adj_af_tdcs, falha_terapeutica=falha_af, sessoes_ajuste=sa_af,
            notas_clinicas="Associar obrigatoriamente treino de nomeação estruturado; apenas a seção de Ajustes (M1-E C3 e Medular T10) possui borda tracejada/pontilhada.",
            audit_meta=_audit("Moderada", "Evidência cerebelar em anomia na afasia.", "Protocolo cerebelar catódico seguido de anódico antes da seção de Ajustes.", ["Ensaio controlado"], "Baixa", "Condicional", "Associar treino lexical estruturado.", tol_af),
            mod_tipo="tdcs",
        ),
    }

    arvore_rtms = {
        "roadmap_id": "RM09",
        "titulo_fluxograma": "AVC Afasia de Expressão e Compreensão — rTMS / iTBS / cTBS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual perfil e sintoma predominante na Afasia pós-AVC (rTMS)?",
                "subtitulo": "Basear escolha de hemisfério em exames de imagem (RNM com tractografia, EEG, TC) e dominância (Inventário de Edimburgo).",
                "opcoes": [
                    {"id": "exp_fala", "rotulo": "Afasia de Expressão — Redução da fala espontânea", "criterio": "Giro Frontal Inferior (GFI)", "descricao": "Inicia com LF-rTMS 1 Hz sobre F6 contralesional (Ren et al., 2019).", "protocolo_alvo": "expressao"},
                    {"id": "exp_anomia", "rotulo": "Afasia de Expressão — Anomia", "criterio": "GFI / Acesso lexical", "descricao": "Rota Giro Frontal Inferior.", "protocolo_alvo": "expressao"},
                    {"id": "exp_rep", "rotulo": "Afasia de Expressão — Repetição alterada", "criterio": "GFI / Fascículo arqueado anterior", "descricao": "Rota Giro Frontal Inferior.", "protocolo_alvo": "expressao"},
                    {"id": "comp_aud", "rotulo": "Afasia de Compreensão — Compreensão alterada", "criterio": "Região Temporoparietal", "descricao": "Inicia com LF-rTMS 1 Hz sobre CP6 contralesional (Ren et al., 2019).", "protocolo_alvo": "compreensao"},
                    {"id": "comp_anomia", "rotulo": "Afasia de Compreensão — Anomia", "criterio": "Região Temporoparietal", "descricao": "Rota temporoparietal.", "protocolo_alvo": "compreensao"},
                    {"id": "comp_rep", "rotulo": "Afasia de Compreensão — Repetição alterada", "criterio": "Região Temporoparietal", "descricao": "Rota temporoparietal.", "protocolo_alvo": "compreensao"},
                ],
            },
        },
        "ajuste_parametros": adj_af_rtms,
        "protocolo_alternativo": {
            "nome": "iTBS M1 Esquerdo C3 (Xu et al., 2021) — Seção de Ajustes",
            "tecnica": "iTBS", "alvo": "C3 (M1 esquerdo)", "parametros": "800 pulsos | 80% LMR (50 Hz / 5 Hz, 2 s ON / 8 s OFF)",
            "observacoes": "Opção na seção de ajustes para afasia de expressão não-fluente refratária.",
        },
        "protocolo_alternativo_2": {
            "nome": "cTBS Cerebelo Direito (Zheng et al., 2022) — Seção de Ajustes",
            "tecnica": "cTBS Cerebelar", "alvo": "Cerebelo lateral direito (3 cm à direita do vérmis, 1 cm abaixo do ínion)", "parametros": "600 pulsos em 40 s | bobina figura de 8 (7 cm) | 80% LMR",
            "observacoes": "Aplicável tanto após falha em expressão quanto diretamente após Dual F5+CP5 em compreensão.",
        },
        "falha_terapeutica": {
            "id": "RM09-FALHA", "titulo": "Falha Terapêutica em rTMS Afasia",
            "criterios_definicao": "Ausência de resposta clínica em TODOS os microdesfechos avaliados (MTL-Brasil) após 5 sessões com fonoterapia e conclusão das etapas previstas.",
            "descricao": "Reavaliar exames de imagem e dominância hemisférica.",
            "condutas": ["Verificar se tecido viável esquerdo ou lesão extensa justificam troca de hemisfério.", "Considerar transição para tDCS / tsDCS medular em Afasia pós-AVC."],
        },
    }

    arvore_tdcs = {
        "roadmap_id": "RM08",
        "titulo_fluxograma": "AVC Afasia de Expressão e Compreensão — tDCS / tsDCS",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual sintoma e perfil linguístico na Afasia pós-AVC (tDCS)?",
                "subtitulo": "Em Anomia, o fluxograma oferece escolha entre o alvo cortical principal (GFI/Temporal) e o Cerebelo.",
                "opcoes": [
                    {"id": "tdcs_exp_fala", "rotulo": "Afasia de Expressão — Redução da fala espontânea", "criterio": "Giro Frontal Inferior", "descricao": "Inicia com tDCS anódica F5 + deltoide direito (Zhao et al., 2021).", "protocolo_alvo": "tdcs_expressao_gfi"},
                    {"id": "tdcs_exp_rep", "rotulo": "Afasia de Expressão — Repetição alterada", "criterio": "Giro Frontal Inferior", "descricao": "Rota Giro Frontal Inferior.", "protocolo_alvo": "tdcs_expressao_gfi"},
                    {"id": "tdcs_exp_anomia", "rotulo": "Afasia de Expressão — Anomia", "criterio": "GFI ou Cerebelo", "descricao": "Escolher alvo cortical ou cerebelar.", "proxima_etapa": "anomia_alvo_exp"},
                    {"id": "tdcs_comp_aud", "rotulo": "Afasia de Compreensão — Compreensão alterada", "criterio": "Região Temporal", "descricao": "Inicia com tDCS anódica CP5 (Fiori et al., 2013).", "protocolo_alvo": "tdcs_compreensao_tp"},
                    {"id": "tdcs_comp_rep", "rotulo": "Afasia de Compreensão — Repetição alterada", "criterio": "Região Temporal", "descricao": "Rota Temporal.", "protocolo_alvo": "tdcs_compreensao_tp"},
                    {"id": "tdcs_comp_anomia", "rotulo": "Afasia de Compreensão — Anomia", "criterio": "Região Temporal ou Cerebelo", "descricao": "Escolher alvo temporal ou cerebelar.", "proxima_etapa": "anomia_alvo_comp"},
                ],
            },
            "anomia_alvo_exp": {
                "pergunta": "Qual alvo utilizar para Anomia (Afasia de Expressão)?",
                "subtitulo": "Bifurcação explícita para Anomia entre Giro Frontal Inferior e Cerebelo.",
                "opcoes": [
                    {"id": "anomia_gfi", "rotulo": "Giro Frontal Inferior (F5 / F6)", "criterio": "Rota principal", "descricao": "Inicia com tDCS anódica F5 + deltoide direito.", "protocolo_alvo": "tdcs_expressao_gfi"},
                    {"id": "anomia_cer_e", "rotulo": "Cerebelo", "criterio": "Catódica (seguida de anódica c/ rampa 15 s)", "descricao": "Inicia com tDCS cerebelar catódica (Sebastian et al., 2020).", "protocolo_alvo": "tdcs_cerebelo_anomia"},
                ],
            },
            "anomia_alvo_comp": {
                "pergunta": "Qual alvo utilizar para Anomia (Afasia de Compreensão)?",
                "subtitulo": "Bifurcação explícita para Anomia entre Região Temporal e Cerebelo.",
                "opcoes": [
                    {"id": "anomia_tp", "rotulo": "Região Temporal (CP5 / CP6)", "criterio": "Rota principal", "descricao": "Inicia com tDCS anódica CP5 (Wernicke).", "protocolo_alvo": "tdcs_compreensao_tp"},
                    {"id": "anomia_cer_c", "rotulo": "Cerebelo", "criterio": "Catódica (seguida de anódica c/ rampa 15 s)", "descricao": "Inicia com tDCS cerebelar catódica (Sebastian et al., 2020).", "protocolo_alvo": "tdcs_cerebelo_anomia"},
                ],
            },
        },
        "ajuste_parametros": adj_af_tdcs,
        "protocolo_alternativo": {
            "nome": "tDCS M1-E C3 (Meinzer et al., 2016) — Seção de Ajustes",
            "tecnica": "tDCS M1-E", "alvo": "C3 (M1 esquerdo, 5×7 cm² + supraorbital D 10×10 cm²)", "parametros": "1,0 mA | 20 min",
            "observacoes": "Opção auxiliar na seção de ajustes para nomeação e comunicação cotidiana.",
        },
        "protocolo_alternativo_2": {
            "nome": "tsDCS Medular T10 (Marangolo et al., 2017) — Seção de Ajustes",
            "tecnica": "tsDCS Medular", "alvo": "T10 torácica (T9–T11) + deltoide direito (5×7 cm²)", "parametros": "2,0 mA | 20 min",
            "observacoes": "Aplicável na seção de ajustes antes da falha terapêutica.",
        },
        "falha_terapeutica": {
            "id": "RM08-FALHA", "titulo": "Falha Terapêutica em tDCS Afasia",
            "criterios_definicao": "Ausência de resposta clínica em TODOS os microdesfechos na MTL-Brasil após 5 sessões combinadas à fonoterapia.",
            "descricao": "Documentar falha após percorrer etapas M1-E e tsDCS Medular na seção de ajustes.",
            "condutas": ["Considerar transição para rTMS/iTBS/cTBS conforme exames de imagem (RNM tractografia/TC)."],
        },
    }

    obs_af = [
        make_obs("RM09-PRE-IMAGEM", "Antes de iniciar qualquer protocolo de rTMS na afasia, basear a decisão em exames de imagem pertinentes (RNM com tractografia, EEG, TC), verificar dominância hemisférica (Inventário de Edimburgo) e checar contraindicações (implantes metálicos/cocleares, convulsões não controladas).", "pre", categoria="seguranca", modalidades_tipo=["rtms"], severidade="warning"),
        make_obs("RM08-PRE-MODERADORES", "Avaliar contraindicações e considerar que características clínicas individuais, parâmetros da tDCS e habilidades linguísticas basais moderam os efeitos terapêuticos.", "pre", categoria="clinica", modalidades_tipo=["tdcs"]),
        make_obs("RM09-TECIDO-VIAVEL", "A estimulação com alta frequência no hemisfério esquerdo (F5 10 Hz / CP5 10 Hz / Dual F5+CP5) é particularmente promissora em pacientes com tecido viável remanescente na imagem.", "alvo", categoria="anatomia", protocolo_ids=["expressao", "compreensao"], modalidades_tipo=["rtms"]),
        make_obs("RM09-DUAL-ORDEM", "Na estimulação bilateral sequencial de rTMS (FC6+F6 1 Hz seguido de FC5+F5 20 Hz), realizar obrigatoriamente a inibição contralesional (1 Hz) ANTES da estimulação lesional (20 Hz).", "stage", categoria="seguranca", protocolo_ids=["expressao"], estagios=["alt2"], modalidades_tipo=["rtms"], severidade="warning"),
        make_obs("RM08-DUAL-SIMULTANEO", "Na montagem dual bilateral de tDCS (F5/F6), considerar que a estimulação dos eletrodos ocorre de forma simultânea.", "stage", categoria="parametros", protocolo_ids=["tdcs_expressao_gfi"], estagios=["alt1"], modalidades_tipo=["tdcs"]),
        make_obs("RM08-LESAO-EXTENSA-INIB", "Na escolha do hemisfério, considerar o tamanho da lesão cortical: em lesões extensas envolvendo múltiplas áreas nos exames de imagem, recomenda-se a inibição do hemisfério contralateral (CP6).", "step", categoria="anatomia", etapa_ids=["fator_limitante"], modalidades_tipo=["tdcs", "rtms"]),
        make_obs("RM08-MTL-BRASIL", "Adaptação Clínica (Brasil): os artigos originais utilizam baterias internacionais de linguagem. No Brasil, recomenda-se a Bateria Montreal-Toulouse de Avaliação da Linguagem (MTL-Brasil), adaptada e validada para adultos e idosos.", "scale", categoria="avaliacao"),
        make_obs("RM09-SES-FONO", "Associar obrigatoriamente terapia fonoaudiológica estruturada conforme o microdesfecho de linguagem e a área estimulada.", "sessoes", categoria="clinica"),
    ]

    return {
        "id": cid, "condicao": "Acidente Vascular Cerebral — Afasia de Expressão e Compreensão", "eixo": "Doenças Cerebrovasculares",
        "roadmap_id": "RM09", "svg_file": "RM09.svg",
        "fatores_limitantes": [
            {"id": "expressao", "nome": "Afasia de Expressão (Redução da fala / Anomia / Repetição)", "instrumento_sugerido": "MTL-Brasil / WAB", "descricao": "Déficits expressivos direcionados ao Giro Frontal Inferior (F6/F5)."},
            {"id": "compreensao", "nome": "Afasia de Compreensão (Compreensão / Anomia / Repetição)", "instrumento_sugerido": "MTL-Brasil / Token Test", "descricao": "Déficits receptivos direcionados à Região Temporoparietal (CP6/CP5)."},
        ],
        "arvore_algoritmo": arvore_rtms, "arvores_por_modalidade": {"rtms": arvore_rtms, "tdcs": arvore_tdcs},
        "observacoes_contextuais": obs_af, "modalidades": modalidades, "tags_busca": tags,
    }


def build_avc_conditions():
    """Returns the 4 AVC clinical conditions built directly from official PDF protocols."""
    return [
        _build_avc_ms(),
        _build_avc_mobilidade(),
        _build_avc_disfagia(),
        _build_avc_afasia(),
    ]
