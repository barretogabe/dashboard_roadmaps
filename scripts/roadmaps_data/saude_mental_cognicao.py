"""Official clinical decision trees, protocols, and contextual observations for Depressao (RM10), TAG (RM11), Alzheimer/CCL (RM12-RM13), and TEPT (RM18)."""

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

# RM10 Depressao Maior
REF_HSU_2024 = make_ref("Hsu, T. W., et al.", 2024, "The dose-effect relationship of six stimulation parameters with rTMS over left DLPFC on treatment-resistant depression: A systematic review and meta-analysis", "Neuroscience & Biobehavioral Reviews", "10.1016/j.neubiorev.2024.105704", tipo="Metanálise de referência")
REF_KISHI_2024 = make_ref("Kishi, T., et al.", 2024, "Theta burst stimulation for depression: a systematic review and network and pairwise meta-analysis", "Molecular Psychiatry", "10.1038/s41380-024-02630-5", tipo="Metanálise de referência")
REF_LI_2021_DEP = make_ref("Li, H., et al.", 2021, "Comparative efficacy and acceptability of neuromodulation procedures in the treatment of treatment-resistant depression: a network meta-analysis of randomized controlled trials", "Journal of Affective Disorders", "10.1016/j.jad.2021.03.019", tipo="Metanálise de referência")
REF_SHI_2024_DEP = make_ref("Shi, R., et al.", 2024, "Short-term and long-term efficacy of accelerated transcranial magnetic stimulation for depression: a systematic review and meta-analysis", "BMC Psychiatry", "10.1186/s12888-024-05545-1", tipo="Metanálise de referência")
REF_SPAMPINATO_2013 = make_ref("Spampinato, C., et al.", 2013, "Transcranial magnetic stimulation in the assessment of motor cortex excitability and treatment of drug-resistant major depression", "IEEE Transactions on Neural Systems and Rehabilitation Engineering", "10.1109/TNSRE.2013.2256432", tipo="Ensaio clínico de referência")
REF_BLUMBERGER_2016 = make_ref("Blumberger, D. M., et al.", 2016, "Unilateral and bilateral MRI-targeted repetitive transcranial magnetic stimulation for treatment-resistant depression: a randomized controlled study", "Journal of Psychiatry & Neuroscience", "10.1503/jpn.150265", tipo="Ensaio clínico de referência")
REF_RAMOS_2025_TTT = make_ref("Ramos, M. R. F., et al.", 2025, "Accelerated Theta-Burst Stimulation for Treatment-Resistant Depression: A Randomized Clinical Trial", "JAMA Psychiatry", "10.1001/jamapsychiatry.2025.0013", tipo="Ensaio clínico de referência")
REF_COLE_2020_SNT = make_ref("Cole, E. J., et al.", 2020, "Stanford Accelerated Intelligent Neuromodulation Therapy for Treatment-Resistant Depression", "American Journal of Psychiatry", "10.1176/appi.ajp.2019.19070720", tipo="Ensaio clínico de referência")

# RM11 TAG
REF_CIRILLO_2019 = make_ref("Cirillo, P., et al.", 2019, "Transcranial magnetic stimulation in anxiety and trauma-related disorders: A systematic review and meta-analysis", "Brain and Behavior", "10.1002/brb3.1284", tipo="Metanálise de referência")
REF_LI_2022_TAG = make_ref("Li, X., et al.", 2022, "Clinical effects of continuous theta burst stimulation for generalized anxiety disorder and a mechanism involving alpha oscillations: a randomized controlled trial", "Journal of Psychiatry & Neuroscience", "10.1503/jpn.210134", tipo="Ensaio clínico de referência")
REF_HUANG_2018_TAG = make_ref("Huang, Z., et al.", 2018, "Repetitive transcranial magnetic stimulation of the right parietal cortex for comorbid generalized anxiety disorder and insomnia: A randomized, double-blind, sham-controlled pilot study", "Brain Stimulation", "10.1016/j.brs.2018.05.016", tipo="Ensaio clínico de referência")
REF_DILKOV_2017_TAG = make_ref("Dilkov, D., et al.", 2017, "Repetitive transcranial magnetic stimulation of the right dorsal lateral prefrontal cortex in the treatment of generalized anxiety disorder: A randomized, double-blind sham controlled clinical trial", "Progress in Neuro-Psychopharmacology and Biological Psychiatry", "10.1016/j.pnpbp.2017.05.018", tipo="Ensaio clínico de referência")
REF_CLARKE_2019_TAG = make_ref("Clarke, E., et al.", 2019, "Efficacy of repetitive transcranial magnetic stimulation in the treatment of depression with comorbid anxiety disorders", "Journal of Affective Disorders", "10.1016/j.jad.2019.03.085", tipo="Ensaio clínico de referência")

# RM12 / RM13 Alzheimer e CCL
REF_YANG_2024_AD = make_ref("Yang, T., et al.", 2024, "The cognitive effect of non-invasive brain stimulation combined with cognitive training in Alzheimer's disease and mild cognitive impairment: a systematic review and meta-analysis", "Alzheimer's Research & Therapy", "10.1186/s13195-024-01505-9", tipo="Metanálise de referência")
REF_XIU_2024_AD = make_ref("Xiu, H., et al.", 2024, "High-frequency repetitive transcranial magnetic stimulation (HF-rTMS) on global cognitive function of elderly in mild to moderate Alzheimer's disease: a systematic review and meta-analysis", "Neurological Sciences", "10.1007/s10072-023-07072-5", tipo="Metanálise de referência")
REF_JIN_2024_AD = make_ref("Jin, Y., et al.", 2024, "Efficacy and safety of neuromodulation for apathy in patients with Alzheimer's disease: A systematic review and meta-analysis of randomized controlled trials", "Journal of Psychiatric Research", "10.1016/j.jpsychires.2024.01.016", tipo="Metanálise de referência")
REF_MENARDI_2022_AD = make_ref("Menardi, A., et al.", 2022, "Transcranial magnetic stimulation treatment in Alzheimer's disease: a meta-analysis of its efficacy as a function of protocol characteristics and degree of personalization", "Journal of Neurology", "10.1007/s00415-022-11236-2", tipo="Metanálise de referência")
REF_ANDRADE_2024_AD = make_ref("Andrade, S. M., et al.", 2024, "Effect of transcranial direct current stimulation and transcranial magnetic stimulation on the cognitive function of individuals with Alzheimer's disease: a systematic review with meta-analysis and meta-regression", "Neurological Research", "10.1080/01616412.2024.2321779", tipo="Metanálise de referência")
REF_TAO_2022_AD = make_ref("Tao, Y., et al.", 2022, "Repetitive Transcranial Magnetic Stimulation Decreases Serum Amyloid-beta and Increases Ectodomain of p75 Neurotrophin Receptor in Patients with Alzheimer's Disease", "Journal of Integrative Neuroscience", "10.31083/j.jin2105140", tipo="Ensaio clínico de referência")
REF_PADALA_2020_AD = make_ref("Padala, P. R., et al.", 2020, "Neuromodulation for Apathy in Alzheimer's Disease: A Double-Blind, Randomized, Sham-Controlled Pilot Study", "Journal of Alzheimer's Disease", "10.3233/JAD-200640", tipo="Ensaio clínico de referência")
REF_WEI_2022_AD = make_ref("Wei, L., et al.", 2022, "Parietal-hippocampal rTMS improves cognitive function in Alzheimer's disease and increases dynamic functional connectivity of default mode network", "Psychiatry Research", "10.1016/j.psychres.2022.114721", tipo="Ensaio clínico de referência")
REF_MARRA_2015_CCL = make_ref("Drumond Marra, H. L., et al.", 2015, "Transcranial Magnetic Stimulation to Address Mild Cognitive Impairment in the Elderly: A Randomized Controlled Study", "Behavioural Neurology", "10.1155/2015/287843", tipo="Ensaio clínico de referência")
REF_KOCH_2022_AD = make_ref("Koch, G., et al.", 2022, "Precuneus magnetic stimulation for Alzheimer's disease: a randomized, sham-controlled trial", "Brain", "10.1093/brain/awac285", tipo="Ensaio clínico de referência")
REF_KHEDR_2014_AD_TDCS = make_ref("Khedr, E. M., et al.", 2014, "A double-blind randomized clinical trial on the efficacy of cortical direct current stimulation for the treatment of Alzheimer's disease", "Frontiers in Aging Neuroscience", "10.3389/fnagi.2014.00275", tipo="Ensaio clínico de referência")
REF_SATORRES_2022_CCL = make_ref("Satorres, E., et al.", 2022, "Home-based transcranial direct current stimulation in mild neurocognitive disorder due to possible Alzheimer's disease: A randomised, single-blind, controlled-placebo study", "Frontiers in Psychology", "10.3389/fpsyg.2022.1071737", tipo="Ensaio clínico de referência")
REF_LU_2019_TDCS = make_ref("Lu, H., et al.", 2019, "Randomized controlled trial of tDCS on cognition in 201 seniors with mild neurocognitive disorder", "Annals of Clinical and Translational Neurology", "10.1002/acn3.50823", tipo="Ensaio clínico de referência")
REF_KHEDR_2019_AD_TDCS = make_ref("Khedr, E. M., et al.", 2019, "Therapeutic Role of Transcranial Direct Current Stimulation in Alzheimer Disease Patients: Double-Blind, Placebo-Controlled Clinical Trial", "Neurorehabilitation and Neural Repair", "10.1177/1545968319840285", tipo="Ensaio clínico de referência")
REF_ANDRADE_2022_AD = make_ref("Andrade, S. M., et al.", 2022, "Effects of multisite anodal transcranial direct current stimulation combined with cognitive stimulation in patients with Alzheimer's disease and its neurophysiological correlates: A double-blind randomized clinical trial", "Neurophysiologie Clinique", "10.1016/j.neucli.2022.02.003", tipo="Ensaio clínico de referência")

# RM18 TEPT
REF_LIU_2024_TEPT = make_ref("Liu, H., et al.", 2024, "Neuromodulation treatments for post-traumatic stress disorder: a systematic review and network meta-analysis covering efficacy, acceptability, and follow-up effects", "Journal of Anxiety Disorders", "10.1016/j.janxdis.2024.102912", tipo="Metanálise de referência")
REF_MCGIRR_2021_TEPT = make_ref("McGirr, A., et al.", 2021, "Deconstructing systematic reviews on repetitive transcranial magnetic stimulation (rTMS) for posttraumatic stress disorder", "Canadian Journal of Psychiatry", "10.1177/0706743720982432", tipo="Metanálise de referência")
REF_BOGGIO_2010_TEPT = make_ref("Boggio, P. S., et al.", 2010, "Noninvasive brain stimulation with high-frequency and low-intensity repetitive transcranial magnetic stimulation treatment for posttraumatic stress disorder", "The Journal of Clinical Psychiatry", "10.4088/JCP.08m04638blu", tipo="Ensaio clínico de referência")
REF_KOZEL_2019_TEPT = make_ref("Kozel, F. A., et al.", 2019, "One hertz versus ten hertz repetitive TMS treatment of PTSD: A randomized clinical trial", "Psychiatry Research", "10.1016/j.psychres.2019.01.004", tipo="Ensaio clínico de referência")
REF_AHMADIZADEH_2018 = make_ref("Ahmadizadeh, M. J., & Rezaei, M.", 2018, "Unilateral right and bilateral dorsolateral prefrontal cortex transcranial magnetic stimulation in treatment post-traumatic stress disorder: a randomized controlled study", "Brain Research Bulletin", "10.1016/j.brainresbul.2018.06.001", tipo="Ensaio clínico de referência")
REF_PHILIP_2019_TEPT = make_ref("Philip, N. S., et al.", 2019, "Theta-burst transcranial magnetic stimulation for posttraumatic stress disorder", "American Journal of Psychiatry", "10.1176/appi.ajp.2019.18101160", tipo="Ensaio clínico de referência")
REF_WATTS_2012_TEPT = make_ref("Watts, B. V., et al.", 2012, "A sham controlled study of repetitive transcranial magnetic stimulation for posttraumatic stress disorder", "Brain Stimulation", "10.1016/j.brs.2011.02.002", tipo="Ensaio clínico de referência")


def _tol(o, a, f):
    return {"orientacao_tolerabilidade": o, "ajuste_seguranca": a, "fatores_moduladores": f}


def _audit(nivel, resumo, just, sinais, grade, forca, dom, tol):
    return {
        "amstar2_nivel": nivel, "amstar2_resumo": resumo, "amstar2_justificativa": just,
        "amstar2_sinais": sinais, "grade_certeza": grade, "grade_forca": forca,
        "grade_dominios": dom, "tolerabilidade": tol,
    }


def _build_depressao():
    cid = "depressao-maior"
    tags = {
        "siglas": ["TDM", "DM", "MDD", "DRT", "TRD", "CPFDL", "DLPFC", "HDRS", "MADRS", "TTT", "SNT", "SAINT"],
        "coordenadas_10_20": ["F3", "F4", "DLPFC"],
        "alvos_anatomicos": ["Córtex Pré-Frontal Dorsolateral Esquerdo (DLPFC Esquerdo — F3)", "Córtex Pré-Frontal Dorsolateral Direito (F4)"],
        "sinonimos_en": ["depression", "major depressive disorder", "mdd", "treatment-resistant depression", "saint", "snt", "ttt"],
        "sintomas_pt": ["depressão", "tristeza persistente", "perda de interesse", "anedonia", "distúrbios do sono", "tempo reduzido"],
        "escalas": ["HDRS-21", "HDRS-17", "MADRS"],
        "tecnicas": ["rTMS", "HF-rTMS 10Hz", "rTMS Bilateral", "iTBS", "LF-rTMS 1Hz F4", "TTT", "SNT"],
    }
    tol_dep = _tol(
        "Reduzir a intensidade (em % do LMR) se houver intolerância do paciente nos primeiros trens de estimulação.",
        "Frequência é parâmetro chave; a curva dose-resposta atinge platô entre 4.000 e 5.000 pulsos por sessão.",
        "Acompanhar resposta até a 3ª–4ª semana e programar reavaliação estruturada após 3 meses da indução.",
    )

    scale_hdrs21 = make_scale("hdrs_21", "Escala de Depressão de Hamilton — 21 itens (HDRS-21)", "HDRS-21", "reducao", "Redução média ≥ 50% a 55% (ou ≥ 7 pts) na HDRS-21", 0.72, placeholder="Ex: 24", min_val=0, max_val=62, mcid_valor=7.0, mcid_label="-50% ou -7 pts na HDRS-21")
    scale_hdrs17 = make_scale("hdrs_17", "Escala de Depressão de Hamilton — 17 itens (HDRS-17)", "HDRS-17", "reducao", "Redução ≥ 6 pts (ou ≥ 50%) na HDRS-17", 0.70, placeholder="Ex: 21", min_val=0, max_val=52, mcid_valor=6.0, mcid_label="-6 pts ou -50% na HDRS-17")
    scale_madrs = make_scale("madrs", "Escala de Depressão de Montgomery-Asberg (MADRS)", "MADRS", "reducao", "Redução média de 52,5% na MADRS em protocolo acelerado SNT (Cole et al., 2020)", 0.75, placeholder="Ex: 28", min_val=0, max_val=60, mcid_valor=10.0, mcid_label="-52,5% na MADRS")

    def _dep_f3_step(ordem):
        return make_chain_step(ordem, "RM10-P1", "HF-rTMS 10 Hz — F3 Convencional", "HF-rTMS 10 Hz — F3 Esquerdo (Spampinato et al., 2013)", "HF-rTMS (10 Hz)", "F3 (CPFDL esquerdo)", "10 Hz | 120% LMR | 3.000 pulsos (40 p/trem, 26\" IIT)", sessoes="20 sessões (1×/dia)", efeito_esperado="Redução de 55% na HDRS-21 (DP 16,4%)", referencia="Spampinato et al. (2013) · DOI: 10.1109/TNSRE.2013.2256432")

    def _dep_bilat_step(ordem):
        return make_chain_step(ordem, "RM10-P2", "rTMS Bilateral Sequencial (F4 1 Hz + F3 10 Hz)", "rTMS Bilateral Sequencial — F4 + F3 (Blumberger et al., 2016)", "rTMS Bilateral", "F4 (1 Hz) seguido de F3 (10 Hz)", "F4: 1 Hz 120% LMR (100p × 6 trens = 600 p) + F3: 10 Hz 120% LMR (30p × 50 trens, 30\" IIT = 1.500 p)", sessoes="15 sessões (1×/dia)", efeito_esperado="Redução de 6,8±7,2 pontos na HDRS-17", referencia="Blumberger et al. (2016) · DOI: 10.1503/jpn.150265", observacoes="Metanálises sugerem superioridade ou equivalência da estimulação bilateral frente à alta frequência esquerda.")

    step_conv_p3 = make_chain_step(3, "RM10-P3", "iTBS F3 (1.800 pulsos)", "iTBS — F3 Esquerdo 1.800 pulsos (Li et al., 2021)", "iTBS (50 Hz)", "F3 (CPFDL esquerdo)", "iTBS 50 Hz | 80% LMR | 30 p/trem, 10\" IIT | 1.800 pulsos", sessoes="10 sessões (1×/dia)", efeito_esperado="Redução de 24% na HDRS-17 (DP 39,1%)", referencia="Li et al. (2021) · DOI: 10.1177/24705470211006855", fase_etapa="sequencia")
    step_conv_p4 = make_chain_step(4, "RM10-P4", "LF-rTMS 1 Hz — F4 (Direito)", "LF-rTMS 1 Hz — F4 Direito (Miron et al., 2021)", "LF-rTMS (1 Hz)", "F4 (CPFDL direito)", "1 Hz | 120% LMR | 1.200 pulsos", sessoes="15 sessões", efeito_esperado="Redução de 38,2% na HDRS-17", referencia="Miron et al. (2021) · DOI: 10.1177/20451253211042696", observacoes="Embora efetivo, é menos utilizado na prática clínica brasileira.", linha_fluxograma="solida", fase_etapa="sequencia")
    step_acc_ttt = make_chain_step(1, "RM10-TTT", "iTBS Acelerado — TTT (Craniometria, 3×/dia)", "iTBS Acelerado TTT — Triple TBS (Ramos et al., 2025)", "iTBS Acelerado (3×/dia)", "F3 por craniometria", "50 Hz | 8\" IIT | 100% LMR | 1.200 p/sessão · 3 sessões/dia (pausa 30 min)", sessoes="45 sessões em 15 dias (5d/sem)", efeito_esperado="Redução de 54,7% na HAMD-17 (DP 9,2%)", referencia="Ramos et al. (2025) · DOI: 10.1001/jamapsychiatry.2025.0013", observacoes="Maior viabilidade prática (craniometria, 3×/dia); estudo ainda não replicado.", fase_etapa="inicial")
    step_acc_snt = make_chain_step(2, "RM10-SNT", "iTBS Acelerado — SNT (Neuronavegação, 10×/dia)", "iTBS Acelerado SNT — Stanford (Cole et al., 2020)", "iTBS Acelerado (10×/dia)", "F3 por neuronavegação funcional", "50 Hz | 8\" IIT | 90% LMR | 1.800 p/sessão · 10 sessões/dia (pausa 50 min)", sessoes="50 sessões em 5 dias consecutivos", efeito_esperado="Redução de 52,5% na MADRS", referencia="Cole et al. (2020) · DOI: 10.1176/appi.ajp.2019.19070720", observacoes="A neuronavegação e o número elevado de sessões diárias dificultam a implementação.", fase_etapa="sequencia")

    adj_dep = {"titulo": "Ajustes de Intensidade, Dose e Tempo de Indução", "tolerabilidade": "Reduzir a intensidade (% do LMR) se houver intolerância do paciente nos trens iniciais.", "dose_pulsos": "Frequência é parâmetro chave, seguido por intensidade (Hsu et al., 2024). Curva dose-resposta atinge platô em 4.000–5.000 pulsos/sessão (Sabé et al., 2024).", "calibracao_limiar": "A estimulação magnética transcraniana é mais eficiente quando associada ao tratamento medicamentoso (Tao et al., 2024)."}
    falha_dep = {"criterio": "Resposta ao final do protocolo menor que o tamanho de efeito previsto após percorrer toda a sequência convencional ou acelerada.", "conduta_oficial": "1. Revisar adesão medicamentosa concomitante;\n2. Escalonar de unilateral F3 para bilateral F4+F3, iTBS F3 ou LF-rTMS F4;\n3. Avaliar regime acelerado (TTT/SNT) caso haja disponibilidade clínica."}
    sa_dep = {"quando_reavaliar": "Melhora sintomática tem pico entre a 3ª e a 4ª semanas e pode decair após 3 meses — programar reavaliação estruturada com HDRS/MADRS após 3 meses da indução.", "ajuste_dose": "Avaliar associação farmacológica otimizada e escalonamento sequencial conforme resposta ao final do ciclo.", "regra_interrupcao": "Se resposta final abaixo do tamanho de efeito previsto para o protocolo, avançar para a etapa seguinte."}

    modalidades = {
        "moderada_grave": make_mod(
            protocolo_id="RM10-CONV", tecnica="HF-rTMS 10 Hz — F3 (CPFDL Esquerdo)", modalidade_sigla="rTMS F3 10 Hz",
            alvo="F3 (Córtex Pré-Frontal Dorsolateral Esquerdo)", frequencia="10 Hz", intensidade="120% LMR",
            pulsos_duracao="3.000 pulsos (40 pulsos/trem, 26\" intervalo)", sessoes="20 sessões (1 sessão por dia)",
            escala_recomendada="HDRS-21 / HDRS-17 / MADRS", meta_melhora="Redução de 55% na HDRS-21",
            tamanho_efeito=0.72, evidencia="Nível A — Consenso NNDC/IFCN 2025 e Metanálises 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível A (Trapp et al., 2025 · Lefaucheur et al., 2020)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_SPAMPINATO_2013, meta_analise=REF_HSU_2024,
            mcid_valor=7.0, mcid_label="-50% ou -7 pts HDRS", cohen_d_valor=0.72, cohen_d_interp="Grande",
            estudo_referencia="Spampinato et al. (2013) / Blumberger et al. (2016)", efeito_resumo="Redução média de 55% na HDRS-21 após 20 sessões",
            escalas_detalhadas=[scale_hdrs21, scale_hdrs17, scale_madrs],
            cadeia_sequencial=[_dep_f3_step(1), _dep_bilat_step(2), step_conv_p3, step_conv_p4],
            ajuste_parametros=adj_dep, falha_terapeutica=falha_dep, sessoes_ajuste=sa_dep,
            notas_clinicas="Associar ao tratamento medicamentoso otimizado; pacientes refratários seguem para estimulação bilateral sequencial ou iTBS.",
            audit_meta=_audit("Alta", "Metanálise dose-resposta em 6 parâmetros (Hsu et al., 2024) e consenso NNDC/IFCN (Trapp et al., 2025).", "Frequência, intensidade e platô de 4–5 mil pulsos definidos com alta consistência.", ["Dose-resposta", "Consenso 2025"], "Alta", "Forte", "Nível A consolidado para depressão moderada a grave resistente.", tol_dep),
        ),
        "tempo_reduzido": make_mod(
            protocolo_id="RM10-ACC", tecnica="iTBS Acelerado TTT — Craniometria (3 sessões/dia)", modalidade_sigla="iTBS Acelerado",
            alvo="F3 (CPFDL Esquerdo por craniometria)", frequencia="iTBS (50 Hz)", intensidade="100% LMR",
            pulsos_duracao="1.200 pulsos/sessão · 3 sessões/dia (pausa 30 min, 8\" IIT)", sessoes="45 sessões em 15 dias (5 dias/semana)",
            escala_recomendada="HDRS-17 / MADRS", meta_melhora="Redução de 54,7% na HAMD-17",
            tamanho_efeito=0.75, evidencia="Nível A/B — Ramos et al. 2025 (JAMA Psych) · Cole 2020 · Kishi 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B/A emergente (Trapp et al., 2025 · Shi et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_RAMOS_2025_TTT, meta_analise=REF_SHI_2024_DEP,
            mcid_valor=6.0, mcid_label="-52,5% MADRS / -54,7% HAMD-17", cohen_d_valor=0.75, cohen_d_interp="Grande",
            estudo_referencia="Ramos et al. (2025) / Cole et al. (2020)", efeito_resumo="Remissão rápida em 5 a 15 dias (-54,7% HAMD-17 com TTT)",
            escalas_detalhadas=[scale_hdrs17, scale_madrs, scale_hdrs21],
            cadeia_sequencial=[step_acc_ttt, step_acc_snt],
            ajuste_parametros=adj_dep, falha_terapeutica=falha_dep, sessoes_ajuste=sa_dep,
            notas_clinicas="TTT tem maior viabilidade prática (craniometria, estudo ainda não replicado); SNT exige neuronavegação funcional.",
            audit_meta=_audit("Moderada", "Metanálise iTBS acelerada (Shi et al., 2024; Kishi et al., 2024) e ECR JAMA Psychiatry (Ramos et al., 2025).", "Alta eficácia de curto prazo quando há demanda logística por tempo reduzido.", ["ECR 2025", "Metanálise 2024"], "Moderada", "Condicional", "Escolha entre TTT (craniometria) e SNT (neuronavegação) conforme infraestrutura.", tol_dep),
        ),
    }

    arvore = {
        "roadmap_id": "RM10",
        "titulo_fluxograma": "Árvore de Decisão — Estimulação Magnética Transcraniana para Depressão",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante na Depressão Maior?",
                "subtitulo": "Alvo: Córtex pré-frontal dorsolateral (Trapp et al., 2025).",
                "opcoes": [{"id": "sintomas_dep", "rotulo": "Sintomas de depressão moderada a grave (HDRS-21 ≥ 18 ou MADRS ≥ 20)", "criterio": "Tristeza persistente, perda de interesse e distúrbios do sono", "descricao": "Avaliar demanda por sessão de menor duração.", "proxima_etapa": "demanda_tempo"}],
            },
            "demanda_tempo": {
                "pergunta": "Há demanda por sessão de menor duração?",
                "subtitulo": "Avaliar magnitude dos sintomas depressivos e disponibilidade do paciente e da clínica para múltiplas sessões diárias.",
                "opcoes": [
                    {"id": "convencional", "rotulo": "NÃO — Regime Convencional (1 sessão por dia)", "criterio": "Inicia com HF-rTMS 10 Hz em F3 (Spampinato et al., 2013)", "descricao": "Maior respaldo longitudinal com sessões diárias únicas.", "protocolo_alvo": "moderada_grave"},
                    {"id": "acelerado", "rotulo": "SIM — Regime Acelerado (> 1 sessão por dia)", "criterio": "Inicia com iTBS acelerado TTT por craniometria (Ramos et al., 2025)", "descricao": "Indução intensiva em 5 a 15 dias.", "protocolo_alvo": "tempo_reduzido"},
                ],
            },
        },
        "ajuste_parametros": adj_dep,
        "protocolo_alternativo": {"nome": "rTMS Bilateral Sequencial F4 + F3 (Blumberger et al., 2016) — Sequência", "tecnica": "rTMS Bilateral", "alvo": "F4 + F3", "parametros": "F4 1 Hz 600p + F3 10 Hz 1.500p | 15 sessões", "observacoes": "Superior ou equivalente à estimulação unilateral esquerda."},
        "protocolo_alternativo_2": {"nome": "LF-rTMS 1 Hz F4 Direito (Miron et al., 2021) — Sequência", "tecnica": "LF-rTMS", "alvo": "F4", "parametros": "1 Hz | 1.200 pulsos | 15 sessões", "observacoes": "F4 1 Hz é efetivo, porém menos utilizado na prática clínica brasileira."},
        "falha_terapeutica": {"id": "RM10-FALHA", "titulo": "Falha Terapêutica em Depressão", "criterios_definicao": "Critérios de resposta final inferior ao tamanho de efeito previsto após cadeia convencional ou acelerada.", "descricao": "Reavaliar adesão farmacológica, platô de pulsos (4–5 mil/sessão) e programar reavaliação após 3 meses.", "condutas": ["Otimizar medicação antidepressiva em conjunto.", "Transicionar para regime bilateral ou iTBS acelerado (TTT/SNT)."]},
    }

    obs_dep = [
        make_obs("RM10-MAGNITUDE-STEP", "Regra de Aplicação: avaliar a magnitude dos sintomas depressivos e a disponibilidade do paciente e da clínica para realizar múltiplas sessões diárias.", "step", categoria="clinica", etapa_ids=["demanda_tempo"]),
        make_obs("RM10-BILAT-TEC", "Metanálises sugerem que a rTMS bilateral sequencial (F4 1 Hz + F3 10 Hz) é superior ou ao menos equivalente à alta frequência esquerda. LF-rTMS 1 Hz em F4, embora efetiva, é menos utilizada na prática clínica brasileira.", "tec", categoria="evidencia", protocolo_ids=["moderada_grave"]),
        make_obs("RM10-ACC-TEC", "TTT possui maior viabilidade prática por número de sessões/pausa e uso de craniometria (estudo ainda não replicado). SNT exige neuronavegação funcional e 10 sessões diárias, o que dificulta a implementação.", "tec", categoria="clinica", protocolo_ids=["tempo_reduzido"]),
        make_obs("RM10-MED-IX", "A TMS é mais eficiente quando associada ao tratamento medicamentoso (Tao et al., 2024).", "tec", categoria="clinica"),
        make_obs("RM10-BANCO-EA", "Registrar eventos adversos conforme protocolo de segurança e Banco NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN"),
    ]

    return {
        "id": cid, "condicao": "Depressão Maior", "eixo": "Psiquiatria & Saúde Mental",
        "roadmap_id": "RM10", "svg_file": "RM10.svg",
        "fatores_limitantes": [{"id": "moderada_grave", "nome": "Sintomas de depressão moderada a grave", "instrumento_sugerido": "HDRS-21 ≥ 18 ou MADRS ≥ 20", "descricao": "Tristeza persistente, perda de interesse e distúrbios do sono."}],
        "arvore_algoritmo": arvore, "observacoes_contextuais": obs_dep, "modalidades": modalidades, "tags_busca": tags,
    }


def _build_tag():
    cid = "ansiedade-generalizada"
    tags = {
        "siglas": ["TAG", "GAD", "CPFDL", "DLPFC", "HAM-A", "BAI", "GAD-7", "DASS-21", "PSQI"],
        "coordenadas_10_20": ["F4", "F3", "P4", "DLPFC Direito"],
        "alvos_anatomicos": ["Córtex Pré-Frontal Dorsolateral Direito (F4)", "Córtex Parietal Direito (P4)", "Bilateral F3+F4"],
        "sinonimos_en": ["anxiety", "generalized anxiety disorder", "gad", "insomnia", "worry"],
        "sintomas_pt": ["ansiedade generalizada", "tensão", "preocupação", "insônia", "ansiedade"],
        "escalas": ["HAM-A", "BAI", "GAD-7", "DASS-21", "HDRS", "PSQI"],
        "tecnicas": ["LF-rTMS 1Hz F4", "cTBS F4", "LF-rTMS 1Hz P4", "HF-rTMS 20Hz F4", "rTMS Bilateral F3+F4"],
    }
    tol_tag = _tol(
        "Em cTBS em F4 no TAG optou-se por 600 pulsos priorizando segurança clínica. A estimulação a 20 Hz em F4 excede a diretriz de segurança e registrou 1 crise tônico-clônica.",
        "Protocolos iniciam com 5 sessões/semana por 2–4 semanas (10 a 25 sessões totais) com desmame gradual para 3–2 sessões/semana antes de encerrar.",
        "Como a HAM-A não é validada no Brasil, associar BAI, GAD-7 ou DASS-21; falha = ausência de melhora após 5 tentativas com diferentes protocolos.",
    )

    scale_gad7 = make_scale("gad_7", "Transtorno de Ansiedade Generalizada — GAD-7 (Validação Brasil + HAM-A)", "GAD-7 / BAI / HAM-A", "reducao", "Redução ≥ 4 pts na GAD-7 (ou -44% a -50% na HAM-A)", 0.65, placeholder="Ex: 16", min_val=0, max_val=21, mcid_valor=4.0, mcid_label="-4 pts GAD-7 / -45% HAM-A")
    scale_psqi = make_scale("psqi", "Índice de Qualidade do Sono de Pittsburgh (PSQI — Alvo P4 Parietal)", "PSQI", "reducao", "Melhora significativa dos sintomas de insônia comorbida (Huang et al., 2018)", 0.55, placeholder="Ex: 12", min_val=0, max_val=21, mcid_valor=3.0, mcid_label="-3 pts no PSQI")

    def _tag_f4_1hz_step(ordem):
        return make_chain_step(ordem, "RM11-P1", "LF-rTMS 1 Hz — F4 (Replicado em 2 ECRs)", "LF-rTMS 1 Hz — F4 Direito (Li et al., 2022)", "LF-rTMS (1 Hz)", "F4 (CPFDL direito)", "1 Hz | 100% LMR | 24 trens × 50 pulsos (total 1.200 p)", sessoes="10–25 sessões (desmame 3–2×/sem)", efeito_esperado="Redução de 45% na HAM-A (DP 22%)", referencia="Li et al. (2022) · DOI: 10.1503/jpn.210134", observacoes="Bom tamanho de efeito, replicado em 2 outros ensaios clínicos randomizados.")

    def _tag_bilat_step(ordem, fase="ajustes"):
        return make_chain_step(ordem, "RM11-ALT", "Seção de Ajustes — Bilateral F3 10 Hz + F4 1 Hz (Comorbidade Depressiva)", "rTMS Bilateral Sequencial — F3 + F4 (Clarke et al., 2019)", "rTMS Bilateral Sequencial", "F3 (10 Hz) + F4 (1 Hz)", "F3: 10 Hz 110% LMR (1.500 p) + F4: 1 Hz 110% LMR (900 p)", sessoes="10 a 25 sessões", efeito_esperado="Redução de 32% na HAM-A (DP 42%)", referencia="Clarke et al. (2019) · DOI: 10.1016/j.jad.2019.03.085", observacoes="Originalmente testado em depressão com comorbidade de transtorno de ansiedade.", fase_etapa=fase)

    step_p4_f4_20 = make_chain_step(3, "RM11-P4", "HF-rTMS 20 Hz F4 (Alerta de Segurança)", "HF-rTMS 20 Hz — F4 Direito (Dilkov et al., 2017)", "HF-rTMS (20 Hz)", "F4 (CPFDL direito)", "20 Hz | 110% LMR | 20 trens | 600 pulsos total (excede diretriz de segurança)", sessoes="10 a 25 sessões (com desmame 3–2×/sem)", efeito_esperado="Redução de 86% na HAM-A (DP 20%)", referencia="Dilkov et al. (2017) · DOI: 10.1016/j.pnpbp.2017.05.018", linha_fluxograma="solida", observacoes="Alerta de segurança: aplica mais pulsos do que o recomendado por diretrizes de segurança e apresentou 1 caso relatado de crise tônico-clônica no estudo.", fase_etapa="sequencia")

    adj_tag = {"titulo": "Segurança em cTBS/20 Hz, Desmame e Escalas Brasileiras", "tolerabilidade": "ALERTA DE SEGURANÇA: estimulação a 20 Hz em F4 (Dilkov et al., 2017) excede pulsos recomendados e registrou 1 caso de crise tônico-clônica.", "dose_pulsos": "No TAG, optou-se por limitar cTBS em F4 a 600 pulsos priorizando segurança clínica frente a 1.800 p. Total de 10–25 sessões (5×/sem por 2–4 sem com desmame gradual para 3–2×/semana).", "calibracao_limiar": "Associar BAI, GAD-7 ou DASS-21 junto à HAM-A (não validada para populações brasileiras)."}
    falha_tag = {"criterio": "Ausência de melhora após 5 tentativas com diferentes protocolos de TMS.", "conduta_oficial": "1. Verificar comorbidade depressiva (Bilateral F3+F4 na seção de Ajustes) ou insônia (P4 Parietal Direito);\n2. Aplicar esquema completo de desmame;\n3. Encerrar após 5 tentativas distintas sem resposta."}
    sa_tag = {"quando_reavaliar": "Avaliar BAI/GAD-7/DASS-21 + HAM-A (e PSQI apenas na rota parietal P4 com insônia) ao longo das 2–4 semanas (10–25 sessões); considerar falha apenas após 5 tentativas distintas sem resposta.", "ajuste_dose": "Realizar desmame gradual para 3–2 sessões/semana antes de encerrar.", "regra_interrupcao": "Falha terapêutica configurada somente após 5 tentativas com diferentes protocolos sem resposta."}

    modalidades = {
        "moderada_alta": make_mod(
            protocolo_id="RM11-F4", tecnica="LF-rTMS 1 Hz — F4 (CPFDL Direito)", modalidade_sigla="LF-rTMS 1 Hz F4",
            alvo="F4 (Córtex Pré-Frontal Dorsolateral Direito)", frequencia="1 Hz", intensidade="100% LMR",
            pulsos_duracao="1.200 pulsos (24 trens × 50 pulsos)", sessoes="10 a 25 sessões (5×/sem com desmame 3–2×/sem)",
            escala_recomendada="BAI / GAD-7 / DASS-21 (junto à HAM-A)", meta_melhora="-45% na HAM-A (replicado em 2 ECRs)",
            tamanho_efeito=0.65, evidencia="Nível B/C — Cirillo 2019 / Li 2022", linha_fluxograma="solida",
            diretriz_internacional="Nível B/C (Lefaucheur et al., 2020 · Cirillo et al., 2019)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_LI_2022_TAG, meta_analise=REF_CIRILLO_2019,
            mcid_valor=4.0, mcid_label="-4 pts GAD-7 / -45% HAM-A", cohen_d_valor=0.65, cohen_d_interp="Moderado",
            estudo_referencia="Li et al. (2022)", efeito_resumo="Redução média de 45% na HAM-A com LF-rTMS 1 Hz em F4 (replicado em 2 ECRs)",
            escalas_detalhadas=[scale_gad7],
            escalas_por_fator={"moderada_alta": ["gad_7"]},
            cadeia_sequencial=[
                _tag_f4_1hz_step(1),
                make_chain_step(2, "RM11-P2", "cTBS F4 (600 pulsos segurança)", "cTBS — F4 Direito 600 pulsos (Li et al., 2022)", "cTBS", "F4 (CPFDL direito)", "100% LMR | 1 trem | 600 pulsos | 40 s", sessoes="10–25 sessões (desmame 3–2×/sem)", efeito_esperado="Redução de 50% na HAM-A (DP 23%)", referencia="Li et al. (2022) · DOI: 10.1503/jpn.210134", observacoes="Sessões curtas (40 s); optou-se por 600 pulsos priorizando segurança clínica frente a 1.800 pulsos (ainda sem replicação).", fase_etapa="sequencia"),
                step_p4_f4_20, _tag_bilat_step(4, "ajustes"),
            ],
            ajuste_parametros=adj_tag, falha_terapeutica=falha_tag, sessoes_ajuste=sa_tag,
            notas_clinicas="Usar BAI, GAD-7 ou DASS-21 em conjunto à HAM-A; aguardar até 5 tentativas distintas antes de concluir falha terapêutica.",
            audit_meta=_audit("Baixa", "Metanálise em ansiedade e trauma (Cirillo et al., 2019).", "Replicação existente apenas para 1 Hz F4; cTBS 600p e 20 Hz F4 ainda limitados.", ["Poucos ECRs"], "Baixa", "Condicional", "cTBS limitado a 600 pulsos por segurança; 20 Hz F4 requer vigilância convulsiva.", tol_tag),
        ),
        "tag_parietal_p4": make_mod(
            protocolo_id="RM11-P3", tecnica="LF-rTMS 1 Hz — Córtex Parietal Direito (P4)", modalidade_sigla="LF-rTMS P4",
            alvo="Córtex Parietal Direito (P4)", frequencia="1 Hz", intensidade="100% LMR",
            pulsos_duracao="1.500 pulsos (3 trens × 500 p, 10 min ISI)", sessoes="10 a 25 sessões (5×/sem + desmame 3–2×/sem)",
            escala_recomendada="BAI / GAD-7 / HAM-A + PSQI (Insônia)", meta_melhora="Redução de 44% na HAM-A + melhora em insônia (PSQI)",
            tamanho_efeito=0.60, evidencia="Nível C — Huang et al. 2018 (não replicado)", linha_fluxograma="solida",
            diretriz_internacional="Nível C (Huang et al., 2018)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_HUANG_2018_TAG, meta_analise=REF_CIRILLO_2019,
            mcid_valor=3.0, mcid_label="-44% HAM-A / -3 pts PSQI", cohen_d_valor=0.60, cohen_d_interp="Moderado",
            estudo_referencia="Huang et al. (2018)", efeito_resumo="Redução de 44% HAM-A e melhora dos sintomas de insônia comorbida",
            escalas_detalhadas=[scale_gad7, scale_psqi],
            escalas_por_fator={"moderada_alta": ["gad_7", "psqi"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM11-P3", "LF-rTMS 1 Hz — P4 Parietal Direito", "LF-rTMS 1 Hz — Córtex Parietal Direito P4 (Huang et al., 2018)", "LF-rTMS (1 Hz)", "P4 (Córtex Parietal Direito)", "1 Hz | 100% LMR | 3 trens × 500 p | 10 min ISI | 1.500 pulsos", sessoes="10–25 sessões", efeito_esperado="Redução de 44% HAM-A + melhora em insônia (PSQI)", referencia="Huang et al. (2018) · DOI: 10.1016/j.brs.2018.05.016", observacoes="Também promove melhora nos sintomas de insônia comorbida; achados ainda não replicados.", fase_etapa="inicial"),
                _tag_bilat_step(2, "ajustes"),
            ],
            ajuste_parametros=adj_tag, falha_terapeutica=falha_tag, sessoes_ajuste=sa_tag,
            notas_clinicas="Preferencial quando há queixa proeminente de insônia comorbida (avaliar PSQI em conjunto).",
            audit_meta=_audit("Baixa", "Metanálise transtornos de ansiedade (Cirillo et al., 2019).", "Estudo piloto duplo-cego em P4 para TAG + insônia.", ["Estudo único"], "Baixa", "Condicional", "Benefício adicional na qualidade do sono (insônia comorbida).", tol_tag),
        ),
    }

    arvore = {
        "roadmap_id": "RM11",
        "titulo_fluxograma": "Árvore de Decisão — Estimulação Magnética Transcraniana para TAG",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante clínico no TAG?",
                "subtitulo": "Como a HAM-A não é validada no Brasil, associar BAI, GAD-7 ou DASS-21.",
                "opcoes": [{"id": "ansiedade_mod_alta", "rotulo": "Moderado a alto nível de ansiedade (HAM-A > 14), sem ou baixa depressão", "criterio": "HAM-A > 14 + BAI / GAD-7 / DASS-21", "descricao": "Escolha do alvo cortical inicial.", "proxima_etapa": "alvo_tag"}],
            },
            "alvo_tag": {
                "pergunta": "Qual alvo cortical inicial deseja selecionar?",
                "subtitulo": "Escolha entre a rota frontal direita (F4) e a rota parietal direita (P4 para comorbidade com insônia); o protocolo bilateral F3+F4 integra a Seção de Ajustes.",
                "opcoes": [
                    {"id": "tag_f4", "rotulo": "Córtex Pré-Frontal Dorsolateral Direito (F4)", "criterio": "Inicia com LF-rTMS 1 Hz em F4 (Li et al., 2022)", "descricao": "Rota principal em ansiedade generalizada.", "protocolo_alvo": "moderada_alta"},
                    {"id": "tag_p4", "rotulo": "Córtex Parietal Direito (P4)", "criterio": "LF-rTMS 1 Hz em P4 (melhora também insônia — PSQI)", "descricao": "Indicado especialmente quando há sintomas de insônia comorbida.", "protocolo_alvo": "tag_parietal_p4"},
                ],
            },
        },
        "ajuste_parametros": adj_tag,
        "protocolo_alternativo": {"nome": "HF-rTMS 20 Hz F4 (Dilkov et al., 2017 — Alerta de Segurança) — Sequência", "tecnica": "HF-rTMS (20 Hz)", "alvo": "F4", "parametros": "20 Hz | 110% LMR | 20 trens", "observacoes": "ALERTA DE SEGURANÇA: excede pulsos seguros e registrou 1 crise tônico-clônica."},
        "protocolo_alternativo_2": {"nome": "Seção de Ajustes — rTMS Bilateral F3 10 Hz + F4 1 Hz (Clarke et al., 2019)", "tecnica": "rTMS Bilateral", "alvo": "F3 + F4", "parametros": "1.500 p F3 + 900 p F4", "observacoes": "Testado originalmente em depressão com ansiedade comorbida (-32% HAM-A)."},
        "falha_terapeutica": {"id": "RM11-FALHA", "titulo": "Falha Terapêutica no TAG", "criterios_definicao": "Ausência de melhora após 5 tentativas com diferentes protocolos de TMS.", "descricao": "Documentar tentativas em F4, cTBS, P4 e F3+F4 com desmame completo.", "condutas": ["Completar até 5 tentativas distintas de protocolos antes de declarar falha.", "Avaliar psicoterapia associada e estabilidade farmacológica."],
        },
    }

    obs_tag = [
        make_obs("RM11-ESCALA-BR", "Instrumentos no Brasil: como a HAM-A não é validada para populações brasileiras, recomenda-se usar em conjunto BAI (Inventário de Ansiedade de Beck), GAD-7 ou DASS-21 (+ PSQI apenas no alvo P4 com insônia).", "scale", categoria="avaliacao", severidade="warning"),
        make_obs("RM11-CONS-I-II", "LF-rTMS 1 Hz F4 apresenta bom tamanho de efeito e foi replicada em 2 outros ECRs. cTBS F4 (600 p) apresenta um dos melhores tamanhos de efeito e sessões curtas (40 s), mas ainda não foi replicada.", "tec", categoria="evidencia", protocolo_ids=["moderada_alta"]),
        make_obs("RM11-CONS-III", "LF-rTMS 1 Hz em Córtex Parietal Direito (P4) mostrou bom efeito na ansiedade e melhora em sintomas de insônia (avaliar PSQI); dados ainda não replicados.", "tec", categoria="clinica", protocolo_ids=["tag_parietal_p4"]),
        make_obs("RM11-BANCO-EA", "Monitorar e registrar efeitos adversos no Banco NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN"),
    ]

    return {
        "id": cid, "condicao": "Transtorno de Ansiedade Generalizada", "eixo": "Psiquiatria & Saúde Mental",
        "roadmap_id": "RM11", "svg_file": "RM11.svg",
        "fatores_limitantes": [{"id": "moderada_alta", "nome": "Moderado a alto nível de ansiedade, sem ou baixa depressão", "instrumento_sugerido": "HAM-A > 14 + BAI / GAD-7 / DASS-21", "descricao": "Ansiedade generalizada com ou sem insônia e depressão leve."}],
        "arvore_algoritmo": arvore, "observacoes_contextuais": obs_tag, "modalidades": modalidades, "tags_busca": tags,
    }


def _build_alzheimer():
    cid = "alzheimer-ccl"
    tags = {
        "siglas": ["DA", "AD", "CCL", "MCI", "CPFDL", "DLPFC", "MMSE", "MEEM", "MoCA", "ADAS", "NPI", "DAS", "TAVEC"],
        "coordenadas_10_20": ["F3", "F4", "P3", "P4", "T5", "T6", "T3", "Precuneus", "Cerebelo"],
        "alvos_anatomicos": ["CPFDL (F3/F4)", "Córtex Parietal e Temporal (P3/P4, T5/T6)", "Precúneo", "Cerebelo Bilateral", "Córtex Temporoparietal (T3-P3/T4-P4)"],
        "sinonimos_en": ["alzheimer", "alzheimer's disease", "mild cognitive impairment", "mci", "dementia", "apathy", "sundowning"],
        "sintomas_pt": ["alzheimer", "declínio cognitivo leve", "cognição global", "memória", "atenção", "apatia", "função executiva", "sintomas neuropsiquiátricos"],
        "escalas": ["MMSE", "MoCA", "ADAS-Cog", "NPI", "Cornell", "DAS", "D2", "WAIS-IV", "Teste de Trilhas", "TAVEC"],
        "tecnicas": ["rTMS", "HF-rTMS 10Hz/20Hz", "tDCS", "tDCS Multissítio"],
    }
    tol_ad = _tol(
        "Em quadros confusionais ou alterações do sono durante a rTMS, reduzir o número de pulsos pela metade. Observar agitação, confusão e humor (atenção se linguagem prejudicada).",
        "Pacientes com dificuldade de locomoção ou histórico de convulsão podem ser beneficiados pela tDCS. Nunca posicionar eletrodos sobre lesões teciduais.",
        "Evitar fim do dia em pacientes com Sundowning; não alterar medicações basais; benzodiazepínicos diminuem efeito terapêutico.",
    )

    scale_mmse = make_scale("mmse", "Mini Mental State Exam (MMSE) / MoCA", "MMSE / MoCA", "aumento", "Ganho ≥ 2,0 pts (ou +4,4% a +21,9%) no MMSE", 0.58, placeholder="Ex: 21", min_val=0, max_val=30, mcid_valor=2.0, mcid_label="+2,0 pts ou +4,4% a +21,9% MMSE")
    scale_adas = make_scale("adas_cog", "Alzheimer's Disease Assessment Scale — ADAS-Cog", "ADAS-Cog", "reducao", "Melhora ≥ 3,0 pts (ou -20,6% a -32,6%) na ADAS-Cog", 0.62, placeholder="Ex: 22", min_val=0, max_val=70, mcid_valor=3.0, mcid_label="-3,0 pts ou -20,6% ADAS-Cog")
    scale_npi = make_scale("npi", "Neuropsychiatric Inventory (NPI) / Cornell / DAS", "NPI / Cornell", "reducao", "Redução ≥ 4,0 pts (-43% a -61% em NPI/Cornell ou -22,4% na AES-C)", 0.56, placeholder="Ex: 18", min_val=0, max_val=144, mcid_valor=4.0, mcid_label="-4,0 pts ou -43% a -61% NPI/Cornell")
    scale_psico = make_scale("rbmt_d2_tmt", "Baterias Cognitivas (RBMT / D2 / WAIS-IV Dígitos / Trilhas / TAVEC — Uso Privativo de Psicólogos)", "Cognitivo (Uso Privativo Psicólogos)", "aumento", "D2, WAIS-IV Dígitos, Teste de Trilhas e TAVEC possuem uso privativo de psicólogos no Brasil", 0.52, placeholder="Ex: 14", min_val=0, max_val=100, mcid_valor=2.0, mcid_label="+8,3% RBMT / +29% memória", privativo_psicologo=True)

    def _ad_pt_steps(start_ordem):
        return [
            make_chain_step(start_ordem, "RM12-PT-P1", "HF-rTMS 10 Hz — Parietal P3 (Transição Cortical)", "HF-rTMS 10 Hz — Córtex Parietal P3 (Wei et al., 2022)", "HF-rTMS (10 Hz)", "P3 (Córtex Parietal)", "10 Hz | 90% LMR | 880 pulsos (40 p × 22 trens, 20 s IIT)", sessoes="10 sessões", efeito_esperado="Melhora de +9,04% no MMSE", referencia="Wei et al. (2022) · DOI: 10.1016/j.psychres.2022.114721", observacoes="Antes de migrar para alvos exploratórios (cerebelo/precúneo), pode-se utilizar a rota em córtex parietal e temporal."),
            make_chain_step(start_ordem + 1, "RM12-PT-P2", "HF-rTMS 20 Hz — Multissítio P3/P4 e T5/T6 (3 áreas/sessão)", "HF-rTMS 20 Hz — Multissítio Parietal/Temporal (Zhao et al., 2017)", "HF-rTMS (20 Hz)", "P3/P4 e T5/T6 (selecionar 3 áreas corticais por sessão)", "20 Hz | 100–110% LMR | 4.000 p distribuídos entre 3 áreas/sessão", sessoes="30 sessões", efeito_esperado="Melhora de ~9% no MMSE após 30 sessões", referencia="Zhao et al. (2017) · Oncotarget 8:33864"),
        ]

    def _ad_rtms_cer(ordem):
        return make_chain_step(ordem, "RM12-ALT1", "HF-rTMS 5 Hz — Cerebelo Bilateral (Exploratório)", "HF-rTMS 5 Hz — Cerebelo Bilateral (Yao et al., 2022)", "HF-rTMS Cerebelo (Exploratório)", "Cerebelo bilateral (1 cm inferior e 3 cm lateral ao ínion)", "5 Hz | 2.000 pulsos (20 pulsos/trem)", sessoes="20 sessões", efeito_esperado="Melhora de 20% no MMSE após 20 sessões (DP 50%)", referencia="Yao et al. (2022) · DOI: 10.1016/j.brs.2022.06.004", linha_fluxograma="pontilhada", fase_etapa="ajustes")

    def _ad_rtms_prec(ordem):
        return make_chain_step(ordem, "RM12-ALT2", "HF-rTMS 20 Hz — Precúneo (Exploratório)", "HF-rTMS 20 Hz — Precúneo (Koch et al., 2022)", "HF-rTMS Precuneus (Exploratório)", "Precúneo", "20 Hz | 1.600 pulsos (40 p/trem, 28 s IIT) | 100% LMR", sessoes="32 sessões", efeito_esperado="Melhora de 1,16 pontos na ADAS-cog após 32 sessões", referencia="Koch et al. (2022) · DOI: 10.1093/brain/awac285", linha_fluxograma="pontilhada", fase_etapa="ajustes")

    def _ad_tp_steps(start_ordem):
        return [
            make_chain_step(start_ordem, "RM13-TP-P1", "tDCS Anódica Temporal — T3 + Deltoide Direito (Transição)", "tDCS Anódica Temporal — T3 + Deltoide Direito (Lu et al., 2019)", "tDCS Anódica Temporal", "Ânodo T3 (35 cm²) + Cátodo deltoide direito (35 cm²)", "2,0 mA | 20 min", sessoes="20 sessões", efeito_esperado="+60,9% no NPI até 3 meses", referencia="Lu et al. (2019) · DOI: 10.1002/acn3.50823", observacoes="Antes de migrar para alvos exploratórios (cerebelo/multissítio), pode-se utilizar a rota temporoparietal."),
            make_chain_step(start_ordem + 1, "RM13-TP-P2", "tDCS Bilateral Temporoparietal — T3-P3 e T4-P4", "tDCS Bilateral Temporoparietal — T3-P3 e T4-P4 (Khedr et al., 2019)", "tDCS Bilateral Temporoparietal", "T3-P3 e T4-P4 (35 cm²) + Cátodo deltoide D", "2,0 mA | 20 min em cada área (com 5 min de pausa)", sessoes="10 sessões", efeito_esperado="Melhora de +43,3% na Escala de Cornell", referencia="Khedr et al. (2019) · DOI: 10.1177/1545968319840285"),
        ]

    def _ad_tdcs_cer(ordem):
        return make_chain_step(ordem, "RM13-ALT1", "tDCS Cerebelo Direito + Nomeação (Exploratório)", "tDCS Cerebelar — Cerebelo Direito + Terapia Computadorizada (Kim et al., 2024)", "tDCS Cerebelar (Exploratório)", "Cerebelo direito (35 cm²) + neutro ombro/braço", "2,0 mA | 20 min seguidos de 25 min de terapia computadorizada", sessoes="45 sessões (3×/sem)", efeito_esperado="30–60% na QDC da ASHA-FACS", referencia="Kim et al. (2024) · DOI: 10.1080/02687038.2024.2328874", linha_fluxograma="pontilhada", fase_etapa="ajustes")

    def _ad_tdcs_multi(ordem):
        return make_chain_step(ordem, "RM13-ALT2", "tDCS Multissítio 6 Regiões (Exploratório)", "tDCS Multissítio 6 Regiões — F3/P4/P5 e F5/CP5/F4 (Andrade et al., 2022)", "tDCS Multissítio (Exploratório)", "Alternado por sessão: F3/P4/P5 e F5/CP5/F4 (25 cm²) + Cátodo supraorbital (35 cm²)", "2,0 mA | 10 min em cada área", sessoes="24 sessões (3×/sem)", efeito_esperado="Melhora de 20,6% no ADAS-cog após 24 sessões (DP 4,7%)", referencia="Andrade et al. (2022) · DOI: 10.1016/j.neucli.2022.02.003", linha_fluxograma="pontilhada", fase_etapa="ajustes")

    adj_ad = {"titulo": "Tolerabilidade Confusional, Sundowning e Desmame Gradual", "tolerabilidade": "Em casos de quadros confusionais ou alterações do sono durante a rTMS, reduzir o número de pulsos pela metade; coletar comportamento pós-sessão (agitação, confusão, humor).", "dose_pulsos": "Reavaliar a cada 10 sessões; ao atingir platô, iniciar desmame gradual (3× -> 2× -> 1×/sem -> quinzenal -> mensal). Pacientes com comprometimento leve/moderado têm melhor resposta.", "calibracao_limiar": "Pacientes com comprometimento mais grave podem requerer regime de 10 Hz / 3.000 pulsos em F3; em multissítio parieto-temporal selecionar 3 áreas corticais por sessão."}
    falha_ad = {"criterio": "Paciente/familiar/cuidador não percebeu nem relatou nenhum benefício direto ou indireto (comportamento, discurso, sono) em até 10 sessões após percorrer a sequência e seção de ajustes.", "conduta_oficial": "1. Conferir checklist pré-sessão (sono, dieta/jejum, medicações, agitação);\n2. Discutir evolução vs flutuação cognitiva típica com cuidadores;\n3. Considerar transição entre rTMS e tDCS ou encerramento seguro."}
    sa_ad = {"quando_reavaliar": "Reavaliar a cada 10 sessões junto ao familiar/cuidador quanto a ganhos diretos e indiretos (comportamento, discurso, sono).", "ajuste_dose": "Realizar atividades cognitivas dirigidas durante a estimulação; manter esquema medicamentoso estável e checar checklist diário pré-sessão.", "regra_interrupcao": "Se paciente/familiar/cuidador não perceber benefício direto ou indireto em até 10 sessões, avançar para o próximo protocolo."}

    modalidades = {
        "alzheimer_memoria": make_mod(
            protocolo_id="RM12-AD-CPFDL", tecnica="HF-rTMS 20 Hz — F3 (CPFDL Esquerdo)", modalidade_sigla="rTMS AD CPFDL",
            alvo="F3 (Córtex Pré-Frontal Dorsolateral Esquerdo)", frequencia="20 Hz", intensidade="100% LMR",
            pulsos_duracao="1.760 pulsos (40 pulsos × 44 trens, 25 s IIT)", sessoes="30 sessões (+ atividades cognitivas dirigidas)",
            escala_recomendada="MMSE / MoCA / ADAS-Cog + Barthel", meta_melhora="Melhora de 32,64% na ADAS-Cog",
            tamanho_efeito=0.62, evidencia="Nível B — Metanálise Xiu 2024 / Yang 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Xiu et al., 2024 · Menardi et al., 2022)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_TAO_2022_AD, meta_analise=REF_XIU_2024_AD,
            mcid_valor=3.0, mcid_label="+4,4% MMSE / -32,6% ADAS-Cog", cohen_d_valor=0.62, cohen_d_interp="Moderado",
            estudo_referencia="Tao et al. (2022) / Padala et al. (2020)", efeito_resumo="Melhora em ADAS-Cog (32,64%) com regime inicial de 20 Hz em F3",
            escalas_detalhadas=[scale_mmse, scale_adas, scale_psico],
            escalas_por_fator={"alzheimer_memoria": ["mmse", "adas_cog", "rbmt_d2_tmt"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM12-AD-P1", "HF-rTMS 20 Hz F3 (Alzheimer)", "HF-rTMS 20 Hz — F3 CPFDL (Tao et al., 2022)", "HF-rTMS (20 Hz)", "F3 (CPFDL esquerdo)", "20 Hz | 100% LMR | 1.760 p (40 p × 44 trens, 25 s IIT)", sessoes="30 sessões", efeito_esperado="Melhora de 32,64% na ADAS-cog", referencia="Tao et al. (2022) · DOI: 10.31083/j.jin2105140"),
                make_chain_step(2, "RM12-AD-P2", "HF-rTMS 10 Hz F3 3.000 p (Pacientes Mais Graves)", "HF-rTMS 10 Hz — F3 3.000 pulsos (Padala et al., 2020)", "HF-rTMS (10 Hz)", "F3 (CPFDL esquerdo)", "10 Hz | 120% LMR | 3.000 pulsos (indicado para pacientes mais graves)", sessoes="20 sessões", efeito_esperado="Melhora de 4,36% no MMSE", referencia="Padala et al. (2020) · DOI: 10.3233/JAD-200640"),
                *_ad_pt_steps(3), _ad_rtms_cer(5), _ad_rtms_prec(6),
            ],
            ajuste_parametros=adj_ad, falha_terapeutica=falha_ad, sessoes_ajuste=sa_ad,
            notas_clinicas="Em pacientes mais graves pode-se utilizar 10 Hz / 3.000 pulsos; pacientes com 'Sundowning' devem evitar sessões no fim do dia.",
            audit_meta=_audit("Moderada", "Metanálise HF-rTMS na Doença de Alzheimer (Xiu et al., 2024).", "Seleção e risco de viés relatados; melhor resposta em estágio leve-moderado.", ["Risco de viés"], "Moderada", "Condicional", "Associar treinamento cognitivo dirigido durante a estimulação.", tol_ad),
        ),
        "ccl_cognicao": make_mod(
            protocolo_id="RM12-CCL", tecnica="HF-rTMS 10 Hz — F3 (Declínio Cognitivo Leve)", modalidade_sigla="rTMS CCL F3",
            alvo="F3 (Córtex Pré-Frontal Dorsolateral Esquerdo)", frequencia="10 Hz", intensidade="110% LMR",
            pulsos_duracao="2.000 pulsos (50 pulsos × 40 trens, 25 s IIT)", sessoes="10 sessões com tarefas cognitivas",
            escala_recomendada="MoCA / MMSE / RBMT / RBANS / D2 / WAIS-IV (Privativos: Psicólogos)", meta_melhora="+8,28% RBMT pós-ciclo (+9,58% em 1 mês)",
            tamanho_efeito=0.60, evidencia="Nível B — Metanálise Yang 2024 / Marra 2015", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Yang et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_MARRA_2015_CCL, meta_analise=REF_YANG_2024_AD,
            mcid_valor=2.0, mcid_label="+8,3% RBMT / +37,3% CVLT", cohen_d_valor=0.60, cohen_d_interp="Moderado",
            estudo_referencia="Drumond Marra et al. (2015)", efeito_resumo="Melhora sustentada de memória operacional/episódica no CCL",
            escalas_detalhadas=[scale_mmse, scale_psico],
            escalas_por_fator={"alzheimer_memoria": ["mmse", "rbmt_d2_tmt"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM12-CCL-P1", "HF-rTMS 10 Hz F3 (CCL)", "HF-rTMS 10 Hz — F3 no CCL (Marra et al., 2015)", "HF-rTMS (10 Hz)", "F3", "10 Hz | 110% LMR | 2.000 p (50p × 40 trens, 25s IIT)", sessoes="10 sessões", efeito_esperado="+8,28% RBMT pós e +9,58% 1 mês follow-up", referencia="Marra et al. (2015) · DOI: 10.1155/2015/287843"),
                make_chain_step(2, "RM12-CCL-P2", "HF-rTMS Bilateral F3 + F4 (CCL)", "HF-rTMS Bilateral 10 Hz — F3 + F4 (Esposito et al., 2022)", "HF-rTMS Bilateral", "F3 e F4 bilateral", "10 Hz | 80% LMR | 2.000 p/área (100p × 20 trens, 25s IIT)", sessoes="20 sessões", efeito_esperado="+7,14% RBANS", referencia="Esposito et al. (2022) · DOI: 10.3390/biomedicines10050994"),
                make_chain_step(3, "RM12-CCL-P3", "HF-rTMS Dual F3 + Precúneo (CCL)", "HF-rTMS Dual 10 Hz — F3 + Precúneo (Zhang et al., 2022)", "HF-rTMS Dual", "F3 (1.200 p) + Precúneo (800 p)", "10 Hz | 120% LMR | 10p/trem | 10 s IIT", sessoes="20 sessões", efeito_esperado="+18,29% imediato e +37,33% CVLT", referencia="Zhang et al. (2022) · DOI: 10.3389/fphys.2022.1066290"),
                _ad_rtms_cer(4), _ad_rtms_prec(5),
            ],
            ajuste_parametros=adj_ad, falha_terapeutica=falha_ad, sessoes_ajuste=sa_ad,
            notas_clinicas="Reserva Legal: D2, WAIS-IV Dígitos e Teste de Trilhas têm uso privativo de psicólogos; pacientes com 'Sundowning' devem evitar fim do dia.",
            audit_meta=_audit("Moderada", "Metanálise NIBS + treino cognitivo (Yang et al., 2024).", "Forte sinergia entre estimulação pré-frontal/precúneo e treino cognitivo.", ["Treino cognitivo"], "Moderada", "Condicional", "Pacientes em estágio CCL obtêm melhor preservação funcional.", tol_ad),
        ),
        "rtms_parietal_temporal": make_mod(
            protocolo_id="RM12-PT", tecnica="HF-rTMS 10 Hz — Córtex Parietal Esquerdo (P3)", modalidade_sigla="rTMS Parietal P3",
            alvo="P3 (Córtex Parietal Esquerdo)", frequencia="10 Hz", intensidade="90% LMR",
            pulsos_duracao="880 pulsos (40 pulsos × 22 trens, 20 s IIT)", sessoes="10 sessões",
            escala_recomendada="MMSE / MoCA", meta_melhora="Melhora de +9,04% no MMSE",
            tamanho_efeito=0.58, evidencia="Nível B — Menardi 2022 / Wei 2022 / Zhao 2017", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Menardi et al., 2022)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_WEI_2022_AD, meta_analise=REF_MENARDI_2022_AD,
            mcid_valor=2.0, mcid_label="+9% no MMSE", cohen_d_valor=0.58, cohen_d_interp="Moderado",
            estudo_referencia="Wei et al. (2022)", efeito_resumo="Melhora de +9,04% no MMSE com conectividade parieto-hipocampal",
            escalas_detalhadas=[scale_mmse, scale_adas],
            escalas_por_fator={"rtms_parietal_temporal": ["mmse", "adas_cog"]},
            cadeia_sequencial=[*_ad_pt_steps(1), _ad_rtms_cer(3), _ad_rtms_prec(4)],
            ajuste_parametros=adj_ad, falha_terapeutica=falha_ad, sessoes_ajuste=sa_ad,
            notas_clinicas="Em progressão multissítio (P3/P4 e T5/T6), selecionar 3 áreas corticais por sessão; evitar fim do dia em pacientes com 'Sundowning'.",
            audit_meta=_audit("Moderada", "Metanálise de personalização de alvos na DA (Menardi et al., 2022).", "Foco em cognição global via rede de modo padrão parieto-temporal.", ["Personalização"], "Moderada", "Condicional", "Pode ser selecionado diretamente ou após resposta insuficiente em CPFDL.", tol_ad),
        ),
        "rm12_apatia_executiva": make_mod(
            protocolo_id="RM12-APATIA", tecnica="HF-rTMS 10 Hz — F3 para Apatia, Função Executiva e Atenção (Padala et al., 2020)", modalidade_sigla="rTMS F3 Apatia",
            alvo="F3 (Córtex Pré-Frontal Dorsolateral Esquerdo)", frequencia="10 Hz", intensidade="120% LMR",
            pulsos_duracao="3.000 pulsos (75 pulsos/trem, 40 trens, 26 s intervalo)", sessoes="20 sessões",
            escala_recomendada="DAS / AES-C / Cornell / BDEFS / Trilhas / D2 / WAIS-IV (Privativos: Psicólogos)", meta_melhora="Melhora de +22,4% na Apathy Evaluation Scale (AES-C) após 20 sessões",
            tamanho_efeito=0.56, evidencia="Nível B — Metanálise Apatia Jin 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Jin et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_PADALA_2020_AD, meta_analise=REF_JIN_2024_AD,
            mcid_valor=3.0, mcid_label="-22,4% na AES-C (Apatia)", cohen_d_valor=0.56, cohen_d_interp="Moderado",
            estudo_referencia="Padala et al. (2020)", efeito_resumo="-22,4% na escala de apatia após 20 sessões",
            escalas_detalhadas=[scale_npi, scale_psico],
            escalas_por_fator={"rm12_apatia_executiva": ["npi", "rbmt_d2_tmt"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM12-AP-P1", "HF-rTMS 10 Hz F3 (Apatia / Executiva)", "HF-rTMS 10 Hz — F3 Apatia/Executiva (Padala et al., 2020)", "HF-rTMS (10 Hz)", "F3 (CPFDL esquerdo)", "10 Hz | 120% LMR | 3.000 pulsos (75 pulsos/trem, 40 trens, 26 s intervalo)", sessoes="20 sessões", efeito_esperado="Melhora de 22,4% na AES-C", referencia="Padala et al. (2020) · DOI: 10.3233/JAD-200640", fase_etapa="inicial"),
                _ad_rtms_cer(2), _ad_rtms_prec(3),
            ],
            ajuste_parametros=adj_ad, falha_terapeutica=falha_ad, sessoes_ajuste=sa_ad,
            notas_clinicas="Reserva Legal: Teste de Trilhas, D2 e WAIS-IV Dígitos são de uso privativo de psicólogos; evitar fim do dia em 'Sundowning'.",
            audit_meta=_audit("Moderada", "Metanálise de neuromodulação para apatia na DA (Jin et al., 2024).", "Evidência crescente para apatia pré-frontal esquerda.", ["Risco de viés"], "Moderada", "Condicional", "Direciona Apatia, Função Executiva e Atenção para F3.", tol_ad),
        ),
        "tdcs_ad_cpfdl": make_mod(
            protocolo_id="RM13-AD", tecnica="tDCS Anódica — F3 (Alzheimer Leve: 25 min)", modalidade_sigla="tDCS AD Leve",
            alvo="Ânodo F3 (24 cm²) + Cátodo supraorbital direito (100 cm²)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="25 min (evitar áreas com lesões teciduais)", sessoes="10 sessões",
            escala_recomendada="MMSE / MoCA / TAVEC / Trilhas (Privativos: Psicólogos)", meta_melhora="+21,9% no MMSE até 3 meses (DP 8,79%)",
            tamanho_efeito=0.52, evidencia="Nível B — Andrade 2024 / Khedr 2014", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Lefaucheur et al., 2017 · Andrade et al., 2024)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_KHEDR_2014_AD_TDCS, meta_analise=REF_ANDRADE_2024_AD,
            mcid_valor=2.0, mcid_label="+21,9% no MMSE", cohen_d_valor=0.52, cohen_d_interp="Moderado",
            estudo_referencia="Khedr et al. (2014)", efeito_resumo="+21,9% no MMSE sustentado até 3 meses",
            escalas_detalhadas=[scale_mmse, scale_psico],
            escalas_por_fator={"alzheimer_memoria": ["mmse", "rbmt_d2_tmt"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM13-AD-P1", "tDCS Anódica F3 (Alzheimer Leve)", "tDCS Anódica — F3 24 cm² + Fp2 100 cm² (Khedr et al., 2014)", "tDCS Anódica", "Ânodo F3 + Cátodo Fp2", "2,0 mA | 25 min", sessoes="10 sessões", efeito_esperado="+21,9% MMSE até 3 meses", referencia="Khedr et al. (2014) · DOI: 10.3389/fnagi.2014.00275", fase_etapa="inicial"),
                *_ad_tp_steps(2), _ad_tdcs_cer(4), _ad_tdcs_multi(5),
            ],
            ajuste_parametros=adj_ad, falha_terapeutica=falha_ad, sessoes_ajuste=sa_ad,
            notas_clinicas="O tamanho de efeito da tDCS é geralmente menor que o da rTMS na Doença de Alzheimer; evitar posicionar eletrodos sobre lesões teciduais.",
            audit_meta=_audit("Moderada", "Metanálise tDCS vs rTMS na DA (Andrade et al., 2024).", "Útil especialmente em dificuldade de locomoção ou histórico de convulsões.", ["Metarregressão"], "Moderada", "Condicional", "Efeito tDCS menor que rTMS na DA, porém alta segurança.", tol_ad),
            mod_tipo="tdcs",
        ),
        "tdcs_ccl_cpfdl": make_mod(
            protocolo_id="RM13-CCL", tecnica="tDCS Anódica — F3 (CCL / Alzheimer: 20 min)", modalidade_sigla="tDCS CCL",
            alvo="Ânodo F3 (25 cm²) + Cátodo supraorbital direito (25 cm²)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min", sessoes="10 sessões",
            escala_recomendada="MMSE / MoCA / TAVEC (Uso Privativo de Psicólogos)", meta_melhora="+9,12% MMSE e +29,01% em memória imediata",
            tamanho_efeito=0.50, evidencia="Nível B — Satorres 2022 / Yang 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Yang et al., 2024)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_SATORRES_2022_CCL, meta_analise=REF_YANG_2024_AD,
            mcid_valor=2.0, mcid_label="+9,1% MMSE / +29% Memória", cohen_d_valor=0.50, cohen_d_interp="Moderado",
            estudo_referencia="Satorres et al. (2022)", efeito_resumo="+9,12% MMSE e +27,22% aprendizagem em 10 sessões",
            escalas_detalhadas=[scale_mmse, scale_psico],
            escalas_por_fator={"alzheimer_memoria": ["mmse", "rbmt_d2_tmt"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM13-CCL-P1", "tDCS Anódica F3 (CCL / Alzheimer)", "tDCS Anódica — F3 / Supraorbital D (Satorres et al., 2022)", "tDCS Anódica", "Ânodo F3 + Cátodo Fp2 (25 cm²)", "2,0 mA | 20 min", sessoes="10 sessões", efeito_esperado="+9,12% MMSE e +29,01% memória", referencia="Satorres et al. (2022) · DOI: 10.3389/fpsyg.2022.1071737", fase_etapa="inicial"),
                _ad_tdcs_cer(2), _ad_tdcs_multi(3),
            ],
            ajuste_parametros=adj_ad, falha_terapeutica=falha_ad, sessoes_ajuste=sa_ad,
            notas_clinicas="Alternativa em dificuldade de locomoção ou histórico convulsivo; não posicionar eletrodos sobre lesões teciduais.",
            audit_meta=_audit("Moderada", "Metanálise NIBS + treino cognitivo (Yang et al., 2024).", "Montagem estruturada para CCL em 10 sessões.", ["Treino cognitivo"], "Moderada", "Condicional", "Combinar com estimulação cognitiva durante a sessão.", tol_ad),
            mod_tipo="tdcs",
        ),
        "sintomas_neuropsiquiatricos": make_mod(
            protocolo_id="RM13-TP", tecnica="tDCS Anódica Temporal — T3 + Deltoide Direito", modalidade_sigla="tDCS Temporoparietal",
            alvo="Ânodo T3 (35 cm²) + Cátodo deltoide direito (35 cm²)", frequencia="Contínua", intensidade="2,0 mA",
            pulsos_duracao="20 min", sessoes="20 sessões",
            escala_recomendada="NPI (Pacientes mais graves) + Escala de Depressão de Cornell + WAIS/WASI", meta_melhora="Melhora de +60,9% no NPI até 3 meses",
            tamanho_efeito=0.56, evidencia="Nível B — Jin 2024 / Andrade 2024 / Khedr 2019", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Andrade et al., 2024)", diretriz_ref=DIR_IFCN_TDCS_2017,
            artigo_referencia=REF_LU_2019_TDCS, meta_analise=REF_JIN_2024_AD,
            mcid_valor=4.0, mcid_label="-60,9% NPI / -43,3% Cornell", cohen_d_valor=0.56, cohen_d_interp="Moderado",
            estudo_referencia="Lu et al. (2019) / Khedr et al. (2019)", efeito_resumo="Melhora em sintomas neuropsiquiátricos (60,9% NPI) sustentada por 3 meses",
            escalas_detalhadas=[scale_npi, scale_psico],
            escalas_por_fator={"sintomas_neuropsiquiatricos": ["npi", "rbmt_d2_tmt"]},
            cadeia_sequencial=[
                make_chain_step(1, "RM13-TP-P1", "tDCS T3 Neuropsiquiátricos", "tDCS Anódica Temporal — T3 + Deltoide D (Lu et al., 2019)", "tDCS Anódica Temporal", "T3 (35 cm²) + Deltoide direito (35 cm²)", "2,0 mA | 20 min", sessoes="20 sessões", efeito_esperado="Melhora de 60,9% no NPI até 3 meses", referencia="Lu et al. (2019) · DOI: 10.1002/acn3.50823"),
                make_chain_step(2, "RM13-TP-P2", "tDCS Bilateral T3-P3 e T4-P4 (Depressão/Cognição)", "tDCS Bilateral — T3-P3 e T4-P4 (Khedr et al., 2019)", "tDCS Bilateral Temporoparietal", "T3-P3 e T4-P4 (35 cm²) + Deltoide D", "2,0 mA | 20 min cada área (5 min pausa)", sessoes="10 sessões", efeito_esperado="Melhora de 43,3% na Escala de Cornell", referencia="Khedr et al. (2019) · DOI: 10.1177/1545968319840285"),
                _ad_tdcs_cer(3), _ad_tdcs_multi(4),
            ],
            ajuste_parametros=adj_ad, falha_terapeutica=falha_ad, sessoes_ajuste=sa_ad,
            notas_clinicas="Monitorar agitação, confusão, humor e sono após cada sessão; evitar horário de 'Sundowning'.",
            audit_meta=_audit("Moderada", "Metanálise em sintomas neuropsiquiátricos/apatia na DA (Jin et al., 2024).", "Forte impacto sobre sintomas comportamentais e humor.", ["Risco de viés"], "Moderada", "Condicional", "Temporoparietal indicado para NPI e depressão na DA.", tol_ad),
            mod_tipo="tdcs",
        ),
    }

    arvore_rtms = {
        "roadmap_id": "RM12",
        "titulo_fluxograma": "Árvore de Decisão — Uso da rTMS para a Doença de Alzheimer e CCL",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante cognitivo/comportamental (rTMS)?",
                "subtitulo": "Uso exclusivo para diagnóstico médico confirmado após avaliação neuropsicológica prévia.",
                "opcoes": [
                    {"id": "ad_cpfdl_grupo", "rotulo": "Função cognitiva global / Desempenho nas AVDs / Atenção / Memória (CPFDL)", "criterio": "MMSE / MoCA / Barthel / D2 / WAIS-IV / WMT", "descricao": "Rota CPFDL (escolher diagnóstico CCL vs Alzheimer).", "proxima_etapa": "diagnostico_rtms_cpfdl"},
                    {"id": "ad_parietal", "rotulo": "Função cognitiva global (Rota Córtex Parietal e Temporal)", "criterio": "Inicia com HF-rTMS 10 Hz em P3 (Wei et al., 2022)", "descricao": "Rota dedicada ao córtex parietal e temporal na Doença de Alzheimer.", "protocolo_alvo": "rtms_parietal_temporal"},
                    {"id": "ad_apatia_exec", "rotulo": "Apatia / Função executiva / Atenção (CPFDL Esquerdo)", "criterio": "DAS / Cornell / Trilhas / BDEFS / D2", "descricao": "Inicia com HF-rTMS 10 Hz em F3 — 3.000 pulsos, 120% LMR (Padala et al., 2020).", "protocolo_alvo": "rm12_apatia_executiva"},
                ],
            },
            "diagnostico_rtms_cpfdl": {
                "pergunta": "Qual é o diagnóstico do seu paciente?",
                "subtitulo": "Estratificação entre CCL/Alzheimer inicial e Doença de Alzheimer estabelecida.",
                "opcoes": [
                    {"id": "diag_ccl_ad", "rotulo": "Declínio Cognitivo Leve / Alzheimer inicial", "criterio": "RBMT / RBANS / CVLT", "descricao": "Inicia com HF-rTMS 10 Hz em F3 (Marra et al., 2015).", "protocolo_alvo": "ccl_cognicao"},
                    {"id": "diag_ad", "rotulo": "Doença de Alzheimer", "criterio": "ADAS-Cog / MMSE", "descricao": "Inicia com HF-rTMS 20 Hz em F3 (Tao et al., 2022).", "protocolo_alvo": "alzheimer_memoria"},
                ],
            },
        },
        "ajuste_parametros": adj_ad,
        "protocolo_alternativo": {"nome": "HF-rTMS 5 Hz Cerebelo Bilateral (Yao et al., 2022) — Seção de Ajustes", "tecnica": "HF-rTMS Cerebelo", "alvo": "1 cm inferior e 3 cm lateral ao ínion", "parametros": "5 Hz | 2.000 p | 20 sessões", "observacoes": "+20% MMSE (exploratório)."},
        "protocolo_alternativo_2": {"nome": "HF-rTMS 20 Hz Precúneo (Koch et al., 2022) — Seção de Ajustes", "tecnica": "HF-rTMS Precuneus", "alvo": "Precúneo", "parametros": "20 Hz | 1.600 p | 100% LMR | 32 sessões", "observacoes": "+1,16 pts ADAS-Cog (exploratório)."},
        "falha_terapeutica": {"id": "RM12-FALHA", "titulo": "Falha Terapêutica em Alzheimer/CCL (rTMS)", "criterios_definicao": "Critérios em até 10 sessões: paciente/familiar/cuidador não percebeu nenhum benefício direto ou indireto (comportamento, discurso, sono).", "descricao": "Documentar ausência de benefício clínico após Parietal/Temporal, Cerebelo e Precúneo.", "condutas": ["Considerar tDCS se intolerância, dificuldade de locomoção ou histórico convulsivo.", "Manter estimulação cognitiva multidisciplinar."]},
    }

    arvore_tdcs = {
        "roadmap_id": "RM13",
        "titulo_fluxograma": "Árvore de Decisão — Uso da tDCS para a Doença de Alzheimer e CCL",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é o principal fator limitante na avaliação (tDCS)?",
                "subtitulo": "Análise comparativa: o tamanho de efeito da tDCS é geralmente menor que o da rTMS na Doença de Alzheimer.",
                "opcoes": [
                    {"id": "tdcs_cpfdl", "rotulo": "Função cognitiva global / Memória / Função executiva / Atenção / Aprendizagem", "criterio": "CPFDL Esquerdo (MMSE/MoCA/Trilhas/TAVEC)", "descricao": "Escolher diagnóstico: Alzheimer leve vs CCL.", "proxima_etapa": "diagnostico_tdcs_cpfdl"},
                    {"id": "tdcs_tp", "rotulo": "Memória de trabalho / Sintomas neuropsiquiátricos / Depressão", "criterio": "Córtex Temporoparietal (NPI / Cornell / WAIS)", "descricao": "Inicia com tDCS anódica em T3 + deltoide direito (Lu et al., 2019).", "protocolo_alvo": "sintomas_neuropsiquiatricos"},
                ],
            },
            "diagnostico_tdcs_cpfdl": {
                "pergunta": "Qual é o diagnóstico do paciente (tDCS CPFDL)?",
                "subtitulo": "Define área do eletrodo e duração (25 min vs 20 min).",
                "opcoes": [
                    {"id": "tdcs_ad_leve", "rotulo": "Doença de Alzheimer leve", "criterio": "24 cm² F3 / 100 cm² Fp2 · 25 min", "descricao": "+21,9% MMSE até 3 meses (Khedr et al., 2014).", "protocolo_alvo": "tdcs_ad_cpfdl"},
                    {"id": "tdcs_ccl", "rotulo": "CCL / Alzheimer", "criterio": "25 cm² F3 / 25 cm² Fp2 · 20 min", "descricao": "+9,12% MMSE / +29% memória (Satorres et al., 2022).", "protocolo_alvo": "tdcs_ccl_cpfdl"},
                ],
            },
        },
        "ajuste_parametros": adj_ad,
        "protocolo_alternativo": {"nome": "tDCS Cerebelo Direito + Nomeação (Kim et al., 2024) — Seção de Ajustes", "tecnica": "tDCS Cerebelar", "alvo": "Cerebelo direito (35 cm²) + neutro", "parametros": "2 mA | 20 min + 25 min nomeação | 45 sessões", "observacoes": "30–60% QDC ASHA-FACS (exploratório)."},
        "protocolo_alternativo_2": {"nome": "tDCS Multissítio 6 Regiões (Andrade et al., 2022) — Seção de Ajustes", "tecnica": "tDCS Multissítio", "alvo": "Alternado F3/P4/P5 e F5/CP5/F4", "parametros": "2 mA | 10 min/área | 24 sessões", "observacoes": "+20,6% ADAS-cog (exploratório)."},
        "falha_terapeutica": {"id": "RM13-FALHA", "titulo": "Falha Terapêutica tDCS em Alzheimer/CCL", "criterios_definicao": "Critérios sem benefício direto ou indireto (familiar/cuidador) em até 10 sessões após percorrer alternativas.", "descricao": "Considerar migração para rTMS salvo contraindicações.", "condutas": ["Verificar se locomoção e ausência de histórico convulsivo permitem transição para rTMS."]},
    }

    obs_ad = [
        make_obs("RM12-PRE-DIAG", "ANTES DE INICIAR: uso exclusivo para pacientes com diagnóstico médico confirmado. Realizar avaliação neuropsicológica prévia para guiar o alvo e discutir o caso com cuidadores/equipe (evolução real vs flutuação cognitiva). Checar contraindicações (implantes metálicos); pacientes com dificuldade de locomoção ou histórico convulsivo beneficiam-se de tDCS.", "pre", categoria="seguranca", severidade="warning"),
        make_obs("RM12-PSICO-SCALE", "RESERVA LEGAL (Uso Privativo de Psicólogos — Lei nº 4.119/1962): D2 (Atenção Concentrada), WAIS-IV/WASI Dígitos, Teste de Trilhas e TAVEC são instrumentos privativos de psicólogos no Brasil. Usar MMSE/MoCA/NPI também para acompanhar pacientes mais graves.", "scale", categoria="avaliacao", severidade="warning"),
        make_obs("RM12-BENZO-TEC", "Uso de benzodiazepínicos diminui o efeito do tratamento; não alterar medicações em uso durante o ciclo. Pacientes com comprometimento leve/moderado têm melhor resposta.", "tec", categoria="clinica"),
        make_obs("RM13-MENOR-EFEITO-TEC", "Análise comparativa: o tamanho de efeito da tDCS é geralmente menor que o da rTMS no tratamento cognitivo da Doença de Alzheimer.", "tec", categoria="evidencia", modalidades_tipo=["tdcs"]),
        make_obs("RM12-3AREAS-ALVO", "Regra de Aplicação: na etapa multissítio parieto-temporal (P3/P4, T5/T6), selecionar e estimular 3 áreas corticais por sessão.", "alvo", categoria="anatomia", protocolo_ids=["rtms_parietal_temporal"], modalidades_tipo=["rtms"]),
        make_obs("RM13-LESAO-TECIDUAL-ALVO", "Na tDCS para Doença de Alzheimer/CCL, não posicionar eletrodos sobre áreas com lesões teciduais.", "alvo", categoria="seguranca", modalidades_tipo=["tdcs"], severidade="warning"),
        make_obs("RM12-CHECKLIST-SESSAO", "CHECKLIST DIÁRIO PRÉ-SESSÃO: (1) Qualidade do sono na noite anterior; (2) Medicamentos ingeridos; (3) Alimentação/jejum prolongado; (4) Notícia/evento de agitação no dia.", "sessoes", categoria="clinica"),
        make_obs("RM12-TOL-COMPORTAMENTO", "Coletar comportamento pós-sessão (especialmente em pacientes com linguagem prejudicada) e registrar eventos adversos no Banco NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN"),
    ]

    return {
        "id": cid, "condicao": "Doença de Alzheimer e Declínio Cognitivo Leve", "eixo": "Cognição & Demências",
        "roadmap_id": "RM12", "svg_file": "RM12.svg",
        "fatores_limitantes": [
            {"id": "alzheimer_memoria", "nome": "Função cognitiva global / Memória / AVDs (CPFDL)", "instrumento_sugerido": "MMSE / MoCA / ADAS-Cog / Barthel", "descricao": "Declínio cognitivo em CCL ou Doença de Alzheimer via CPFDL."},
            {"id": "rtms_parietal_temporal", "nome": "Função cognitiva global (Córtex Parietal e Temporal)", "instrumento_sugerido": "MMSE / MoCA", "descricao": "Rota parieto-temporal para Doença de Alzheimer."},
            {"id": "rm12_apatia_executiva", "nome": "Apatia / Função executiva / Atenção", "instrumento_sugerido": "DAS / Cornell / Trilhas / D2 / WAIS-IV", "descricao": "Apatia, disfunção executiva e atenção via F3."},
            {"id": "sintomas_neuropsiquiatricos", "nome": "Sintomas neuropsiquiátricos / Depressão (tDCS Temporoparietal)", "instrumento_sugerido": "NPI / Cornell", "descricao": "Sintomas neuropsiquiátricos e humor na DA."},
        ],
        "arvore_algoritmo": arvore_rtms, "arvores_por_modalidade": {"rtms": arvore_rtms, "tdcs": arvore_tdcs},
        "observacoes_contextuais": obs_ad, "modalidades": modalidades, "tags_busca": tags,
    }


def _build_tept():
    cid = "tept"
    tags = {
        "siglas": ["TEPT", "PTSD", "CPFDL", "DLPFC", "PCL-5", "CAPS", "EMDR", "TCC"],
        "coordenadas_10_20": ["F4", "F3", "r-CPFDL"],
        "alvos_anatomicos": ["Córtex Pré-Frontal Dorsolateral Direito (F4 — r-CPFDL)", "DLPFC Bilateral (F3 + F4)"],
        "sinonimos_en": ["ptsd", "posttraumatic stress disorder", "trauma", "hyperarousal", "nightmares"],
        "sintomas_pt": ["estresse pós-traumático", "tept", "trauma", "pesadelos", "flashbacks", "ideação suicida", "depressão associada"],
        "escalas": ["PCL-5", "CAPS"],
        "tecnicas": ["rTMS 20Hz F4", "rTMS 10Hz F4", "rTMS Bilateral F3+F4", "iTBS F4", "LF-rTMS 1Hz F4"],
    }
    tol_tept = _tol(
        "Reduzir intensidade da estimulação caso haja intolerância nos primeiros trens de pulso e aumentar a dose gradualmente.",
        "Em casos graves, ideação suicida ou risco de abandono, preferir estimulação bilateral F3+F4 (resposta rápida já a partir da 4ª sessão).",
        "Associar fortemente psicoterapias focadas no trauma (Exposição Prolongada, TCC Focada no Trauma, EMDR).",
    )

    scale_pcl5 = make_scale("pcl_5", "PTSD Checklist for DSM-5 (PCL-5)", "PCL-5", "reducao", "Redução ≥ 25% no escore do PCL-5 ao término do protocolo", 0.65, placeholder="Ex: 48", min_val=0, max_val=80, mcid_valor=10.0, mcid_label="-25% (-10 pts) no PCL-5")
    scale_caps = make_scale("caps", "Clinician-Administered PTSD Scale (CAPS)", "CAPS", "reducao", "Redução ≥ 25% na CAPS ao término do protocolo", 0.62, placeholder="Ex: 52", min_val=0, max_val=80, mcid_valor=12.0, mcid_label="-25% na CAPS")

    def _tept_p20_step(ordem):
        return make_chain_step(ordem, "RM18-P1", "HF-rTMS 20 Hz F4 Unilateral", "HF-rTMS 20 Hz — F4 Direito (Boggio et al., 2010)", "HF-rTMS (20 Hz)", "F4 (r-CPFDL)", "20 Hz | 100% LMR | TPS 2.400 (60 trens, 40 PPT, 28 s ITI) | 30 min", sessoes="10 sessões / 4 semanas (dias alternados)", efeito_esperado="Redução de 29,9% no PCL (DP 14,4%)", referencia="Boggio et al. (2010) · DOI: 10.4088/JCP.08m04638blu", observacoes="Melhora normalmente observada a partir da 5ª sessão em dias alternados.")

    def _tept_p10_step(ordem):
        return make_chain_step(ordem, "RM18-P2", "HF-rTMS 10 Hz F4 Unilateral", "HF-rTMS 10 Hz — F4 Direito (Kozel et al., 2019)", "HF-rTMS (10 Hz)", "F4 (r-CPFDL)", "10 Hz | 80% LMR | TPS 600 (30 trens, 20 PPT, 58 s ITI) | 20 min", sessoes="10 sessões / 2 semanas", efeito_esperado="Redução de 29,3% no PCL (DP 11,1%)", referencia="Kozel et al. (2019) · DOI: 10.1016/j.psychres.2019.01.004")

    adj_tept = {"titulo": "Ajuste de Tolerabilidade nos Primeiros Trens e Investigação Comórbida", "tolerabilidade": "Reduzir intensidade (% LMR) caso haja intolerância nos primeiros trens de pulso e subir a dose aos poucos.", "dose_pulsos": "Escalonar duração ou frequência conforme perfil clínico: bilateral F3+F4 em urgência (resposta na 4ª sessão) ou iTBS F4 para sessão rápida (9,5 min).", "calibracao_limiar": "Associar fortemente psicoterapias focadas no trauma (Exposição Prolongada, TCC Focada no Trauma, EMDR) para consolidação dos resultados."}
    falha_tept = {"criterio": "Resposta < 25% na CAPS ou PCL-5 ao término do protocolo.", "conduta_oficial": "1. Reavaliação diagnóstica e ajuste gradual de intensidade/alvo;\n2. Investigar transtorno de personalidade borderline e uso de substâncias;\n3. Avaliar sono inadequado, estressores contínuos e baixo suporte social."}
    sa_tept = {"quando_reavaliar": "Avaliar resposta (< 25% na CAPS ou PCL-5 configura resposta insatisfatória) ao término do protocolo (HF-rTMS unilateral a partir da 5ª sessão; bilateral a partir da 4ª sessão).", "ajuste_dose": "Se resposta < 25%, investigar comorbidades psiquiátricas (borderline, uso de substâncias) e contexto (sono inadequado, estressores contínuos, baixo suporte social).", "regra_interrupcao": "Se resposta < 25% CAPS/PCL-5 ao final do protocolo, progredir na sequência clínica ou realizar reavaliação diagnóstica."}

    modalidades = {
        "sintomas_gerais": make_mod(
            protocolo_id="RM18-P1", tecnica="HF-rTMS 20 Hz — F4 Unilateral Direito (r-CPFDL)", modalidade_sigla="rTMS 20 Hz F4",
            alvo="F4 — Córtex Pré-Frontal Dorsolateral Direito (r-CPFDL)", frequencia="20 Hz", intensidade="100% LMR",
            pulsos_duracao="TPS 2.400 (60 trens, 40 PPT, 28 s ITI) | 30 min", sessoes="10 sessões em 4 semanas (dias alternados)",
            escala_recomendada="PCL-5 (≥ 31) / CAPS (≥ 13)", meta_melhora="Redução ≥ 25% no PCL-5/CAPS (-29,9% pós-ciclo)",
            tamanho_efeito=0.65, evidencia="Nível B/A — Metanálise Liu 2024 / Cochrane Brown 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B/A (Liu et al., 2024 · Brown et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_BOGGIO_2010_TEPT, meta_analise=REF_LIU_2024_TEPT,
            mcid_valor=10.0, mcid_label="-25% (-10 pts) no PCL-5", cohen_d_valor=0.65, cohen_d_interp="Moderado",
            estudo_referencia="Boggio et al. (2010) / Kozel et al. (2019)", efeito_resumo="Redução de 29,9% no PCL-5 a partir da 5ª sessão em dias alternados",
            escalas_detalhadas=[scale_pcl5, scale_caps],
            cadeia_sequencial=[_tept_p20_step(1), _tept_p10_step(2)],
            ajuste_parametros=adj_tept, falha_terapeutica=falha_tept, sessoes_ajuste=sa_tept,
            notas_clinicas="Estimulação unilateral direita é tão eficaz quanto a bilateral e mais viável em rotina ambulatorial.",
            audit_meta=_audit("Moderada", "Metanálise em rede NIBS no TEPT (Liu et al., 2024) e Cochrane (Brown et al., 2024).", "Consistência favorável para F4 direito no TEPT.", ["Análise em rede", "Cochrane"], "Moderada", "Condicional", "Associar Exposição Prolongada, TCC Focada ou EMDR.", tol_tept),
        ),
        "tept_bilateral": make_mod(
            protocolo_id="RM18-P3", tecnica="HF-rTMS Bilateral 20 Hz — F3 + F4 (Gravidade / Risco / Abandono)", modalidade_sigla="rTMS Bilateral Grave",
            alvo="F3 e F4 (CPFDL Bilateral)", frequencia="20 Hz bilateral", intensidade="100% LMR",
            pulsos_duracao="1.200 p em F3 + 1.200 p em F4 (TPS: 2.400; 30 trens cada, 40 PPT, 28 s ITI)", sessoes="10 sessões em 4 semanas (resposta rápida a partir da 4ª sessão)",
            escala_recomendada="PCL-5 / CAPS", meta_melhora="-35,7% no PCL (DP 11,5%), resposta rápida já na 4ª sessão",
            tamanho_efeito=0.70, evidencia="Nível B — Ahmadizadeh 2018 / Liu 2024", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Liu et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_AHMADIZADEH_2018, meta_analise=REF_LIU_2024_TEPT,
            mcid_valor=10.0, mcid_label="-35,7% no PCL-5", cohen_d_valor=0.70, cohen_d_interp="Moderado",
            estudo_referencia="Ahmadizadeh & Rezaei (2018)", efeito_resumo="Resposta rápida já a partir da 4ª sessão em casos graves",
            escalas_detalhadas=[scale_pcl5, scale_caps],
            cadeia_sequencial=[
                make_chain_step(1, "RM18-P3", "HF-rTMS Bilateral 20 Hz F3 + F4", "HF-rTMS Bilateral 20 Hz — F3 e F4 (Ahmadizadeh & Rezaei, 2018)", "HF-rTMS Bilateral", "F3 + F4", "20 Hz | 100% LMR | 1.200 p F3 + 1.200 p F4 (30 min)", sessoes="10 sessões / 4 semanas", efeito_esperado="Redução de 35,7% no PCL desde a 4ª sessão", referencia="Ahmadizadeh & Rezaei (2018) · DOI: 10.1016/j.brainresbul.2018.06.001", fase_etapa="inicial"),
            ],
            ajuste_parametros=adj_tept, falha_terapeutica=falha_tept, sessoes_ajuste=sa_tept,
            notas_clinicas="Preferível diante de sintomas graves, ideação suicida ou risco de abandono.",
            audit_meta=_audit("Moderada", "Metanálise em rede no TEPT (Liu et al., 2024).", "Maior velocidade de resposta (4ª sessão).", ["Análise em rede"], "Moderada", "Condicional", "Indicado em urgência sintomática / risco de abandono.", tol_tept),
        ),
        "tept_itbs_f4": make_mod(
            protocolo_id="RM18-P4", tecnica="iTBS Excitatório — F4 (Sessão Rápida 9,5 min)", modalidade_sigla="iTBS F4",
            alvo="F4 (r-CPFDL)", frequencia="iTBS (50 Hz / 5 Hz)", intensidade="80% LMR",
            pulsos_duracao="1.800 pulsos | 20 trens | ITI 8 s (2 s ON / 8 s OFF) | 9,5 min/sessão", sessoes="15 sessões em 3 semanas",
            escala_recomendada="PCL-5 / CAPS", meta_melhora="Redução de 53,0% no PCL (DP 17,8%)",
            tamanho_efeito=0.72, evidencia="Nível B — Philip et al. 2019 / Yuan 2023", linha_fluxograma="solida",
            diretriz_internacional="Nível B (Liu et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_PHILIP_2019_TEPT, meta_analise=REF_LIU_2024_TEPT,
            mcid_valor=10.0, mcid_label="-53,0% no PCL-5", cohen_d_valor=0.72, cohen_d_interp="Grande",
            estudo_referencia="Philip et al. (2019)", efeito_resumo="Sessão rápida de 9,5 min com redução de 53% no PCL",
            escalas_detalhadas=[scale_pcl5, scale_caps],
            cadeia_sequencial=[
                make_chain_step(1, "RM18-P4", "iTBS F4 (Sessão Rápida 9,5 min)", "iTBS 1.800 pulsos — F4 Direito (Philip et al., 2019)", "iTBS", "F4 (r-CPFDL)", "50 Hz/5 Hz | 80% LMR | 1.800 pulsos | 9,5 min", sessoes="15 sessões / 3 semanas", efeito_esperado="Redução de 53,0% no PCL", referencia="Philip et al. (2019) · DOI: 10.1176/appi.ajp.2019.18101160", fase_etapa="inicial"),
            ],
            ajuste_parametros=adj_tept, falha_terapeutica=falha_tept, sessoes_ajuste=sa_tept,
            notas_clinicas="Sessão rápida (9,5 min) quando há demanda de tempo reduzido.",
            audit_meta=_audit("Moderada", "Metanálise NIBS TEPT (Liu et al., 2024).", "ECR duplo-cego controlado de iTBS F4.", ["Risco de viés"], "Moderada", "Condicional", "Sessão rápida em 9,5 min com boa aceitação.", tol_tept),
        ),
        "comorbidade_depressiva": make_mod(
            protocolo_id="RM18-P5", tecnica="LF-rTMS Inibitório 1 Hz — F4 (Depressão Associada)", modalidade_sigla="LF-rTMS 1Hz F4",
            alvo="F4 (r-CPFDL)", frequencia="1 Hz", intensidade="90% LMR",
            pulsos_duracao="400 pulsos/sessão (20 trens, 20 PPT, 40 s ITI) | 20 min", sessoes="10 sessões em 2 semanas",
            escala_recomendada="PCL-5 / CAPS + HDRS", meta_melhora="Redução de 25,0% no PCL (DP 9,8%) + melhora em sintomas depressivos",
            tamanho_efeito=0.55, evidencia="Nível B — Watts 2012 / McGirr 2021", linha_fluxograma="solida",
            diretriz_internacional="Nível B (McGirr et al., 2021 · Liu et al., 2024)", diretriz_ref=DIR_IFCN_RTMS_2020,
            artigo_referencia=REF_WATTS_2012_TEPT, meta_analise=REF_MCGIRR_2021_TEPT,
            mcid_valor=10.0, mcid_label="-25% no PCL / Melhora depressiva", cohen_d_valor=0.55, cohen_d_interp="Moderado",
            estudo_referencia="Watts et al. (2012)", efeito_resumo="Protocolo inibitório 1 Hz F4 com benefício significativo quando há depressão",
            escalas_detalhadas=[scale_pcl5, scale_caps],
            cadeia_sequencial=[
                make_chain_step(1, "RM18-P5", "LF-rTMS 1 Hz F4 Inibitório (Depressão Associada)", "LF-rTMS 1 Hz — F4 Direito (Watts et al., 2012)", "LF-rTMS (1 Hz)", "F4 (r-CPFDL)", "1 Hz | 90% LMR | 400 p (20 trens, 40 s ITI) | 20 min", sessoes="10 sessões / 2 semanas", efeito_esperado="Redução de 25,0% no PCL + melhora em depressão associada", referencia="Watts et al. (2012) · DOI: 10.1016/j.brs.2011.02.002", fase_etapa="inicial"),
            ],
            ajuste_parametros=adj_tept, falha_terapeutica=falha_tept, sessoes_ajuste=sa_tept,
            notas_clinicas="A estimulação inibitória a 1 Hz produziu melhoras significativas em pacientes com sintomas depressivos associados.",
            audit_meta=_audit("Moderada", "Revisão crítica de rTMS em TEPT (McGirr et al., 2021 · Liu et al., 2024).", "Indicado na presença de depressão associada.", ["Subgrupo depressão"], "Moderada", "Condicional", "Associar psicoterapia focada no trauma.", tol_tept),
        ),
    }

    arvore = {
        "roadmap_id": "RM18",
        "titulo_fluxograma": "Árvore de Decisão — Estimulação Magnética Transcraniana para TEPT",
        "etapa_inicial": "fator_limitante",
        "etapas": {
            "fator_limitante": {
                "pergunta": "Qual é a indicação e limiar clínico no TEPT?",
                "subtitulo": "Alvo: Córtex pré-frontal dorsolateral direito (r-CPFDL).",
                "opcoes": [{"id": "sintomas_tept", "rotulo": "Pessoas com sintomas de TEPT (PCL-5 ≥ 31 / CAPS ≥ 13)", "criterio": "PCL-5 ≥ 31 / CAPS ≥ 13", "descricao": "Iniciar triagem por comorbidade depressiva.", "proxima_etapa": "depressao_associada"}],
            },
            "depressao_associada": {
                "pergunta": "O paciente tem depressão associada?",
                "subtitulo": "O regime inibitório a 1 Hz em F4 produziu melhoras significativas em sintomas depressivos.",
                "opcoes": [
                    {"id": "tept_dep_sim", "rotulo": "SIM — Com depressão associada", "criterio": "LF-rTMS 1 Hz Inibitório F4 (Watts et al., 2012)", "descricao": "1 Hz F4, 90% LMR, 400 p, 10 sessões/2 semanas.", "protocolo_alvo": "comorbidade_depressiva"},
                    {"id": "tept_dep_nao", "rotulo": "NÃO — Sem depressão significativa associada", "criterio": "Avaliar demanda por sessão rápida", "descricao": "Verificar tempo disponível da sessão.", "proxima_etapa": "tempo_reduzido_tept"},
                ],
            },
            "tempo_reduzido_tept": {
                "pergunta": "Há demanda de tempo reduzido da sessão?",
                "subtitulo": "Opção pelo regime excitatório iTBS (9,5 min) quando necessário.",
                "opcoes": [
                    {"id": "tept_tempo_sim", "rotulo": "SIM — Demanda de sessão rápida (9,5 min)", "criterio": "iTBS F4 (Philip et al., 2019)", "descricao": "iTBS 1.800 pulsos, 80% LMR, 15 sessões/3 semanas.", "protocolo_alvo": "tept_itbs_f4"},
                    {"id": "tept_tempo_nao", "rotulo": "NÃO — Sessão convencional (20–30 min)", "criterio": "Avaliar gravidade e risco de abandono", "descricao": "Verificar presença de sintomas graves, ideação suicida ou risco de abandono.", "proxima_etapa": "gravidade_tept"},
                ],
            },
            "gravidade_tept": {
                "pergunta": "Observam-se sintomas graves, ideação suicida ou risco de abandono?",
                "subtitulo": "O regime bilateral F3+F4 pode ser preferível pela resposta rápida já a partir da 4ª sessão.",
                "opcoes": [
                    {"id": "tept_grave_sim", "rotulo": "SIM — Sintomas graves / Ideação suicida / Risco de abandono", "criterio": "HF-rTMS Bilateral F3 + F4 20 Hz (Ahmadizadeh & Rezaei, 2018)", "descricao": "20 Hz bilateral F3+F4, resposta rápida a partir da 4ª sessão.", "protocolo_alvo": "tept_bilateral"},
                    {"id": "tept_grave_nao", "rotulo": "NÃO — Quadro sem urgência suicida / abandono", "criterio": "HF-rTMS 20 Hz F4 Unilateral (Boggio et al., 2010)", "descricao": "Unilateral F4 (tão eficaz quanto bilateral e mais viável em rotina).", "protocolo_alvo": "sintomas_gerais"},
                ],
            },
        },
        "ajuste_parametros": adj_tept,
        "protocolo_alternativo": {"nome": "HF-rTMS 10 Hz F4 (Kozel et al., 2019) — Sequência", "tecnica": "HF-rTMS (10 Hz)", "alvo": "F4", "parametros": "10 Hz | 80% LMR | TPS 600 | 20 min | 10 sessões/2 sem", "observacoes": "Escalonamento imediato caso HF-rTMS 20 Hz F4 não apresente resposta."},
        "protocolo_alternativo_2": {"nome": "iTBS F4 ou LF-rTMS 1 Hz F4 Inibitório — Sequência", "tecnica": "iTBS / LF-rTMS", "alvo": "F4", "parametros": "iTBS 1.800 p (9,5 min) ou 1 Hz 400 p", "observacoes": "Ajustar intensidade gradualmente nos trens iniciais se intolerância."},
        "falha_terapeutica": {"id": "RM18-FALHA", "titulo": "Falha Terapêutica no TEPT", "criterios_definicao": "Resultados < 25% na CAPS ou PCL-5 ao término do protocolo.", "descricao": "Reavaliar diagnóstico, comorbidades (borderline, substâncias) e contexto (sono, estressores, suporte social).", "condutas": ["Investigar transtorno de personalidade borderline e uso de substâncias.", "Avaliar higiene do sono, estressores contínuos e baixo suporte social.", "Garantir psicoterapia focada no trauma (Exposição Prolongada, TCC, EMDR)."]},
    }

    obs_tept = [
        make_obs("RM18-CONSID-STEP", "Considere a logística e urgência clínica: bilateral F3+F4 responde já na 4ª sessão em casos graves/suicidas; iTBS F4 dura apenas 9,5 min; LF-rTMS 1 Hz é preferível se depressão associada; unilateral 20 Hz F4 é mais viável em rotina.", "step", categoria="clinica"),
        make_obs("RM18-CONSID-TEC", "Perfil de resposta: HF-rTMS 20 Hz unilateral F4 é tão eficaz quanto bilateral (melhora após 5ª sessão); bilateral F3+F4 responde já na 4ª sessão; iTBS F4 reduz duração para 9,5 min; LF-rTMS 1 Hz melhora sintomas depressivos associados.", "tec", categoria="clinica"),
        make_obs("RM18-PSICO-TRAUMA", "Para consolidação dos resultados, recomenda-se fortemente a associação da neuromodulação com psicoterapias ativas focadas no trauma (Terapia de Exposição Prolongada, TCC Focada no Trauma ou EMDR).", "sessoes", categoria="clinica", severidade="warning"),
        make_obs("RM18-BANCO-EA", "Seguir protocolo de segurança e registrar eventos adversos no Banco NAPeN.", "tol", categoria="seguranca", referencia_doi=ADVERSE_BANK_URL, referencia_rotulo="Acessar Banco de Efeitos Adversos NAPeN"),
    ]

    return {
        "id": cid, "condicao": "Transtorno de Estresse Pós-Traumático", "eixo": "Psiquiatria & Saúde Mental",
        "roadmap_id": "RM18", "svg_file": "RM18.svg",
        "fatores_limitantes": [{"id": "sintomas_gerais", "nome": "Pessoas com sintomas de TEPT", "instrumento_sugerido": "PCL-5 ≥ 31 ou CAPS ≥ 13", "descricao": "Sintomas pós-traumáticos estratificados por depressão, demanda de tempo e gravidade."}],
        "arvore_algoritmo": arvore, "observacoes_contextuais": obs_tept, "modalidades": modalidades, "tags_busca": tags,
    }


def build_saude_mental_cognicao_conditions():
    """Returns Depressao (RM10), TAG (RM11), Alzheimer/CCL (RM12-RM13), and TEPT (RM18)."""
    return [_build_depressao(), _build_tag(), _build_alzheimer(), _build_tept()]
