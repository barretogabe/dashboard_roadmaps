/**
 * Rede NAPeN — Aplicação Principal da Plataforma Interativa de Prescrição
 * Standalone: Navegação oficial na barra turquesa com dropdown no hover,
 * seleção sob demanda (via dropdown ou busca instantânea), seletor de escalas múltiplas (ex: BBS/SARA),
 * modo híbrido para EAM (graus 0 a 4 + percentual), automatismo de desfechos clínicos e rigor acadêmico ABNT.
 */

document.addEventListener('DOMContentLoaded', () => {
  const data = window.NAPEN_DATA || window.NAPEN_ROADMAPS_DATA;
  if (!data || !data.condicoes) {
    console.error('Base de dados da Rede NAPeN não encontrada.');
    return;
  }

  const engine = new DecisionEngine(data);

  // Estado da Aplicação
  const state = {
    activeTab: 'prescription', // 'prescription' | 'pocket' | 'method'
    searchQuery: '',
    selectedConditionId: null,
    pemStatus: 'sim', // 'sim' | 'nao'
    therapeuticStage: 'primary', // 'primary' | 'alt1' | 'alt2' | 'failure'
    homeEntryMode: 'new', // 'new' | 'returning'
    homeSelectedConditionId: null,
    homeSelectedModality: 'rtms'
  };

  const eamState = {
    base: null,
    post: null
  };

  // Elementos de Navegação da Barra Turquesa
  const navItemPrescription = document.getElementById('navItemPrescription');
  const navItemPocket = document.getElementById('navItemPocket');
  const navItemMethod = document.getElementById('navItemMethod');

  const tabBtnPrescription = document.getElementById('tabBtnPrescription');
  const tabBtnPocket = document.getElementById('tabBtnPocket');
  const tabBtnMethod = document.getElementById('tabBtnMethod');

  const dropdownConditionsList = document.getElementById('dropdownConditionsList');

  // Painéis das Abas
  const panePrescription = document.getElementById('panePrescription');
  const panePocket = document.getElementById('panePocket');
  const paneMethod = document.getElementById('paneMethod');

  // Elementos da Prescrição Interativa & Triagem Inicial na Homepage
  const searchHeroPanel = document.getElementById('searchHeroPanel');
  const homeContinuityPanel = document.getElementById('homeContinuityPanel');
  const btnHomeEntryNew = document.getElementById('btnHomeEntryNew');
  const btnHomeEntryReturning = document.getElementById('btnHomeEntryReturning');
  const homeContinuityQuickPanel = document.getElementById('homeContinuityQuickPanel');
  const homeContCondition = document.getElementById('homeContCondition');
  const homeContModalityWrap = document.getElementById('homeContModalityWrap');
  const homeContModality = document.getElementById('homeContModality');
  const homeContProtocol = document.getElementById('homeContProtocol');
  const homeContStoppedProtocol = document.getElementById('homeContStoppedProtocol');
  const homeContStageShortcuts = document.getElementById('homeContStageShortcuts');

  const algorithmActiveContainer = document.getElementById('algorithmActiveContainer');
  const btnClearSelection = document.getElementById('btnClearSelection');
  const btnSwitchToContinuing = document.getElementById('btnSwitchToContinuing');

  const globalSearchInput = document.getElementById('globalSearchInput');
  const searchPlaceholderMarquee = document.getElementById('searchPlaceholderMarquee');
  const searchClearBtn = document.getElementById('searchClearBtn');
  const searchResultsDropdown = document.getElementById('searchResultsDropdown');

  // Elementos do Algoritmo Clínico
  const algoCondEixo = document.getElementById('algoCondEixo');
  const algoCondTitle = document.getElementById('algoCondTitle');
  const node1QuestionText = document.getElementById('node1QuestionText');
  const node1OptionsList = document.getElementById('node1OptionsList');

  // Barra de Continuidade Clínica Interna (Etapa 0 quando em modo retorno)
  const continuityEntryBar = document.getElementById('continuityEntryBar');
  const continuityCompactBar = document.getElementById('continuityCompactBar');
  const continuityInlineContext = document.getElementById('continuityInlineContext');
  const continuingStageFocusSlot = document.getElementById('continuingStageFocusSlot');
  const prescriptionDetailsCard = document.getElementById('prescriptionDetailsCard');

  // Seletores da Nova Cascata e Modalidades V2
  const modalitySelectorBar = document.getElementById('modalitySelectorBar');
  const modalityPillsGroup = document.getElementById('modalityPillsGroup');
  const preTriagemObservationsSlot = document.getElementById('preTriagemObservationsSlot');
  const cascadingFlowContainer = document.getElementById('cascadingFlowContainer');

  const prescTecnica = document.getElementById('prescTecnica');
  const prescModalidade = document.getElementById('prescModalidade');
  const prescAlvo = document.getElementById('prescAlvo');
  const prescFrequencia = document.getElementById('prescFrequencia');
  const prescIntensidade = document.getElementById('prescIntensidade');
  const prescPulsos = document.getElementById('prescPulsos');
  const prescSessoes = document.getElementById('prescSessoes');
  const prescObsTecnica = document.getElementById('prescObsTecnica');
  const prescObsAlvo = document.getElementById('prescObsAlvo');
  const prescObsIntensidade = document.getElementById('prescObsIntensidade');
  const prescObsSessoes = document.getElementById('prescObsSessoes');
  const prescObsEscala = document.getElementById('prescObsEscala');
  const prescDesfechoNome = document.getElementById('prescDesfechoNome');
  const prescDesfechoGradeBadge = document.getElementById('prescDesfechoGradeBadge');
  const prescLinhaPrescricao = document.getElementById('prescLinhaPrescricao');
  const prescEscala = document.getElementById('prescEscala');
  const prescEfeito = document.getElementById('prescEfeito');
  const prescMeta = document.getElementById('prescMeta');
  const guidelineBadgeText = document.getElementById('guidelineBadgeText');

  // Painel de Triagem Neurofisiológica (PEM)
  const pemTriagePanel = document.getElementById('pemTriagePanel');
  const btnPemSim = document.getElementById('btnPemSim');
  const btnPemNao = document.getElementById('btnPemNao');

  // Botões de Desfecho Oficial da Rede NAPeN
  const responseAssistantPanel = document.getElementById('responseAssistantPanel');
  const btnOutcomeSuccess = document.getElementById('btnOutcomeSuccess');
  const btnOutcomeDanger = document.getElementById('btnOutcomeDanger');
  const assistantSequenceTrail = document.getElementById('assistantSequenceTrail');
  const branchResultPanel = document.getElementById('branchResultPanel');

  // Evidência Científica e Referências Formais (+ AMSTAR 2 / GRADE)
  const evidenceReferencePanel = document.getElementById('evidenceReferencePanel');
  const evidenceSummaryGradeBadge = document.getElementById('evidenceSummaryGradeBadge');
  const evidenceSummaryAmstarBadge = document.getElementById('evidenceSummaryAmstarBadge');
  const btnScrollToEvidence = document.getElementById('btnScrollToEvidence');
  const evidenceCitationText = document.getElementById('evidenceCitationText');
  const evidenceDoiLink = document.getElementById('evidenceDoiLink');
  const evidenceDoiText = document.getElementById('evidenceDoiText');
  const evidenceMetaBlock = document.getElementById('evidenceMetaBlock');
  const evidenceMetaCitationText = document.getElementById('evidenceMetaCitationText');
  const evidenceMetaDoiLink = document.getElementById('evidenceMetaDoiLink');
  const evidenceMetaDoiText = document.getElementById('evidenceMetaDoiText');
  const evidenceAmstarBadge = document.getElementById('evidenceAmstarBadge');
  const evidenceAmstarRationale = document.getElementById('evidenceAmstarRationale');
  const evidenceGradeBadge = document.getElementById('evidenceGradeBadge');
  const evidenceGradeRationale = document.getElementById('evidenceGradeRationale');
  const evidenceGuidelineText = document.getElementById('evidenceGuidelineText');
  const evidenceGuidelineDoiLink = document.getElementById('evidenceGuidelineDoiLink');
  const evidenceGuidelineDoiText = document.getElementById('evidenceGuidelineDoiText');
  const evidencePemGuide = document.getElementById('evidencePemGuide');

  // Calculadora Dual (Clínica & Comparador de Efeito + Tolerabilidade)
  const dualCalcContainer = document.getElementById('dualCalcContainer');
  const calcScaleTabs = document.getElementById('calcScaleTabs');
  const calcEamBox = document.getElementById('calcEamBox');
  const eamGroupBase = document.getElementById('eamGroupBase');
  const eamGroupPost = document.getElementById('eamGroupPost');
  const calcContinuousInputsRow = document.getElementById('calcContinuousInputsRow');
  const calcValBaseLabel = document.getElementById('calcValBaseLabel');
  const calcValPostLabel = document.getElementById('calcValPostLabel');
  const calcValBase = document.getElementById('calcValBase');
  const calcValPost = document.getElementById('calcValPost');
  const tolerabilityOptionsGrid = document.getElementById('tolerabilityOptionsGrid');
  const tolerabilityContextNote = document.getElementById('tolerabilityContextNote');
  const cardDeltaPoints = document.getElementById('cardDeltaPoints');
  const calcDeltaPoints = document.getElementById('calcDeltaPoints');
  const cardDeltaPercent = document.getElementById('cardDeltaPercent');
  const calcDeltaPercent = document.getElementById('calcDeltaPercent');
  const cardMcidBadge = document.getElementById('cardMcidBadge');
  const calcMcidBadge = document.getElementById('calcMcidBadge');
  const calcStudyRef = document.getElementById('calcStudyRef');
  const calcGradeBadge = document.getElementById('calcGradeBadge');
  const calcAmstarBadge = document.getElementById('calcAmstarBadge');
  const calcStudyCohen = document.getElementById('calcStudyCohen');
  const calcStudyMcid = document.getElementById('calcStudyMcid');
  const calcGoalFeedback = document.getElementById('calcGoalFeedback');
  const calcRoadmapEffectText = document.getElementById('calcRoadmapEffectText');
  const calcComparisonFeedback = document.getElementById('calcComparisonFeedback');
  const linkComoEfeitoCalculado = document.getElementById('linkComoEfeitoCalculado');

  // Tabela de Bolso
  const pocketTableBody = document.getElementById('pocketTableBody');

  // Stepper Visual
  const stepNode3 = document.getElementById('stepNode3');
  const stepNode4 = document.getElementById('stepNode4');

  // Elementos do Painel de Monitoramento Clínico & Guia Estratégico de Tolerabilidade/Dose
  const monitoringReeval = document.getElementById('monitoringReeval');
  const monitoringCriterion = document.getElementById('monitoringCriterion');
  const monitoringStopRule = document.getElementById('monitoringStopRule');
  const monitoringNotesText = document.getElementById('monitoringNotesText');
  const tolerabilityDoseGuidePanel = document.getElementById('tolerabilityDoseGuidePanel');
  const tolGuideTitle = document.getElementById('tolGuideTitle');
  const tolGuideBankLink = document.getElementById('tolGuideBankLink');
  const tolGuideTolerance = document.getElementById('tolGuideTolerance');
  const tolGuideDose = document.getElementById('tolGuideDose');
  const tolGuideCalibration = document.getElementById('tolGuideCalibration');
  const btnScrollToTolGuide = document.getElementById('btnScrollToTolGuide');

  // Widget de Idioma Retrátil Oficial (Mimetização Estrita do Portal Rede NAPeN)
  const langDropdownWrapper = document.getElementById('langDropdownWrapper');
  const langCapsuleBtn = document.getElementById('langCapsuleBtn');
  const langMenuExpanded = document.getElementById('langMenuExpanded');
  const langTierActive = document.getElementById('langTierActive');
  const langTierOption = document.getElementById('langTierOption');
  const capsuleFlag = document.getElementById('capsuleFlag');
  const capsuleLangText = document.getElementById('capsuleLangText');
  const tierActiveFlag = document.getElementById('tierActiveFlag');
  const tierActiveText = document.getElementById('tierActiveText');
  const tierOptionFlag = document.getElementById('tierOptionFlag');
  const tierOptionText = document.getElementById('tierOptionText');

  // Elementos do Guia Clínico Operacional de Aplicação de Escalas (Drawer)
  const btnOpenScaleGuideMain = document.getElementById('btnOpenScaleGuideMain');
  const btnOpenScaleGuideCalc = document.getElementById('btnOpenScaleGuideCalc');
  const btnScaleGuideUseInCalc = document.getElementById('btnScaleGuideUseInCalc');
  const scaleGuideBackdrop = document.getElementById('scaleGuideBackdrop');
  const scaleGuideDrawer = document.getElementById('scaleGuideDrawer');
  const scaleGuideCloseBtn = document.getElementById('scaleGuideCloseBtn');

  const scaleGuideSigla = document.getElementById('scaleGuideSigla');
  const scaleGuideTempo = document.getElementById('scaleGuideTempo');
  const scaleGuideTitle = document.getElementById('scaleGuideTitle');
  const scaleGuideDominio = document.getElementById('scaleGuideDominio');
  const scaleGuidePublico = document.getElementById('scaleGuidePublico');
  const scaleGuideMateriais = document.getElementById('scaleGuideMateriais');
  const scaleGuideStepsList = document.getElementById('scaleGuideStepsList');
  const scaleGuideScoresTable = document.getElementById('scaleGuideScoresTable');
  const scaleGuideMcidText = document.getElementById('scaleGuideMcidText');
  const scaleGuideInterpretacaoText = document.getElementById('scaleGuideInterpretacaoText');
  const scaleGuideRefAbnt = document.getElementById('scaleGuideRefAbnt');
  const scaleGuideDoiLink = document.getElementById('scaleGuideDoiLink');
  const scaleGuideValidacaoBrasil = document.getElementById('scaleGuideValidacaoBrasil');

  // ==========================================================================
  // 1. Popula Dropdown de Condições na Barra Turquesa (2 Níveis em Cascata)
  // ==========================================================================
  function closeDropdown() {
    if (navItemPrescription) {
      navItemPrescription.classList.remove('dropdown-open');
    }
    if (dropdownConditionsList) {
      dropdownConditionsList.querySelectorAll('.dropdown-item-has-submenu').forEach(item => {
        item.classList.remove('submenu-open');
      });
      dropdownConditionsList.querySelectorAll('.dropdown-item-has-subsubmenu').forEach(item => {
        item.classList.remove('subsubmenu-open');
      });
      dropdownConditionsList.querySelectorAll('.open-left').forEach(item => {
        item.classList.remove('open-left');
      });
      dropdownConditionsList.classList.add('dropdown-force-closed');
      setTimeout(() => {
        dropdownConditionsList.classList.remove('dropdown-force-closed');
      }, 300);
    }
  }

  function openDropdown() {
    if (navItemPrescription) {
      navItemPrescription.classList.add('dropdown-open');
    }
  }

  function toggleDropdown() {
    if (!navItemPrescription) return;
    if (navItemPrescription.classList.contains('dropdown-open')) {
      closeDropdown();
    } else {
      openDropdown();
    }
  }

  function closeAllDropdowns() {
    closeDropdown();
  }

  function populateDropdownMenu() {
    if (!dropdownConditionsList) return;
    dropdownConditionsList.innerHTML = '';

    const axesOrder = [
      'Acidente Vascular Cerebral',
      'Distúrbios do Movimento',
      'Psiquiatria & Saúde Mental',
      'Dor Crônica & Neuropática',
      'Neurodesenvolvimento',
      'Cognição & Demências'
    ];

    const axesMap = {};
    axesOrder.forEach(axis => { axesMap[axis] = []; });

    data.condicoes.forEach(c => {
      let axis = c.eixo || 'Outros';
      if (axis.includes('Cerebrovasculares') || axis.includes('AVC')) {
        axis = 'Acidente Vascular Cerebral';
      }
      if (!axesMap[axis]) axesMap[axis] = [];
      axesMap[axis].push(c);
    });

    axesOrder.forEach(axisName => {
      const conditionsInAxis = axesMap[axisName] || [];
      if (conditionsInAxis.length === 0) return;

      // Item do 1º Nível (Eixo Clínico)
      const liAxis = document.createElement('li');
      liAxis.className = 'dropdown-item-napen dropdown-item-has-submenu';

      const aAxis = document.createElement('a');
      aAxis.className = 'dropdown-link-napen';
      aAxis.href = '#';
      aAxis.innerHTML = `
        <span>${axisName}</span>
        <span class="axis-arrow-icon" style="font-size: 0.95rem; font-weight: 700; margin-left: 12px; color: var(--napen-teal-bar); transition: transform 0.25s ease; display: inline-block;">›</span>
      `;

      // Alterna submenu no clique (mobile, tablet e desktop)
      aAxis.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const wasOpen = liAxis.classList.contains('submenu-open');
        dropdownConditionsList.querySelectorAll('.dropdown-item-has-submenu').forEach(item => {
          item.classList.remove('submenu-open');
        });
        if (!wasOpen) {
          liAxis.classList.add('submenu-open');
        }
      });

      // Abre submenu suave no hover em desktop
      liAxis.addEventListener('mouseenter', () => {
        dropdownConditionsList.querySelectorAll('.dropdown-item-has-submenu').forEach(item => {
          if (item !== liAxis) item.classList.remove('submenu-open');
        });
        liAxis.classList.add('submenu-open');
      });

      // Submenu do 2º Nível (Condições e Focos Específicos)
      const ulSub = document.createElement('ul');
      ulSub.className = 'dropdown-submenu';

      conditionsInAxis.forEach(c => {
        const liCond = document.createElement('li');
        const aCond = document.createElement('a');
        aCond.className = 'dropdown-sublink-napen';
        aCond.href = '#';

        // Evita redundância de nome: remove prefixo do eixo no submenu
        let cleanTitle = c.condicao;
        if (axisName === 'Acidente Vascular Cerebral' || axisName === 'Doenças Cerebrovasculares (AVC)') {
          cleanTitle = cleanTitle.replace(/^Acidente Vascular Cerebral\s*(\(AVC\))?\s*—\s*/i, '');
        }

        // Resumo dos focos clínicos da condição
        const factorsSummary = (c.fatores_limitantes || [])
          .map(f => f.label.split('(')[0].trim())
          .slice(0, 3)
          .join(' • ');

        aCond.innerHTML = `
          <span class="dropdown-sublink-title">${cleanTitle}</span>
          <span class="dropdown-sublink-sub">${factorsSummary}</span>
        `;

        aCond.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          switchTab('prescription');
          openConditionAlgorithm(c.id);
          closeDropdown();
        });

        liCond.appendChild(aCond);
        ulSub.appendChild(liCond);
      });

      liAxis.appendChild(aAxis);
      liAxis.appendChild(ulSub);
      dropdownConditionsList.appendChild(liAxis);
    });
  }

  // ==========================================================================
  // 2. Abertura do Algoritmo Clínico Sob Demanda
  // ==========================================================================
  // ==========================================================================
  // 2. Abertura do Algoritmo Clínico Sob Demanda & Cascata dos Roadmaps
  // ==========================================================================
  function openConditionAlgorithm(conditionId, opts = {}) {
    state.selectedConditionId = conditionId;

    const targetEntryMode = opts.forceEntryMode
      || (state.homeEntryMode === 'returning' ? 'returning' : 'new');
    const targetStage = opts.continuingStage
      || (targetEntryMode === 'returning' ? 'evaluation' : 'primary');

    engine.setCondition(conditionId, {
      preserveEntryMode: true,
      entryMode: targetEntryMode,
      modalityType: opts.modalityType || 'rtms',
      continuingStage: targetStage
    });

    const cond = engine.getCondition(conditionId);
    if (!cond) return;

    if (opts.factorKey) {
      const pKey = opts.primaryKey || opts.factorKey;
      engine.setFactor(pKey, true);
      if (opts.factorKey !== pKey) {
        engine.setFactor(opts.factorKey, false);
      }
    }

    if (targetEntryMode === 'returning' && targetStage !== 'evaluation' && targetStage !== 'primary') {
      state.therapeuticStage = targetStage;
      engine.setOutcome('danger');
    } else {
      state.therapeuticStage = 'primary';
    }

    if (algoCondEixo) algoCondEixo.textContent = cond.eixo;
    if (algoCondTitle) algoCondTitle.textContent = cond.condicao;
    if (node1QuestionText) {
      node1QuestionText.textContent = cond.no1_pergunta || 'Qual é o principal fator limitante ou desfecho clínico prioritário?';
    }

    // Gerenciamento de compatibilidade da Estratificação Neurofisiológica (PEM no MS para AVC)
    if (conditionId === 'avc-membro-superior') {
      if (pemTriagePanel) pemTriagePanel.style.display = 'none'; // Agora integrado visualmente na cascata fluida
      state.pemStatus = 'sim';
      if (btnPemSim) btnPemSim.classList.add('active');
      if (btnPemNao) btnPemNao.classList.remove('active');
    } else {
      if (pemTriagePanel) pemTriagePanel.style.display = 'none';
      state.pemStatus = 'sim';
    }

    document.querySelectorAll('.dropdown-sublink-napen').forEach(link => {
      const cleanName = cond.condicao.replace(/^Acidente Vascular Cerebral\s*(\(AVC\))?\s*—\s*/i, '');
      const isCurrent = link.textContent.includes(cond.condicao) || link.textContent.includes(cleanName);
      link.classList.toggle('active-item', isCurrent);
    });

    if (searchHeroPanel) searchHeroPanel.style.display = 'none';
    if (algorithmActiveContainer) algorithmActiveContainer.classList.add('visible');

    if (searchResultsDropdown) searchResultsDropdown.classList.remove('visible');
    if (globalSearchInput) globalSearchInput.value = '';
    if (searchClearBtn) searchClearBtn.classList.remove('visible');

    window.scrollTo({ top: 180, behavior: 'smooth' });

    renderContinuityBar(cond);
    renderModalitySelector(cond);
    renderCascadingFlow(cond);
    renderNode1Options(cond);
    renderTolerabilityUI();
    updatePrescriptionDisplay();
    if (state.therapeuticStage !== 'primary') {
      updateOutcomeDisplay();
    }
  }

  function clearSelectedCondition() {
    state.selectedConditionId = null;
    if (algorithmActiveContainer) algorithmActiveContainer.classList.remove('visible');
    if (searchHeroPanel) searchHeroPanel.style.display = 'flex';
    if (typeof renderHomeContinuityPanel === 'function') renderHomeContinuityPanel();

    document.querySelectorAll('.dropdown-sublink-napen').forEach(link => {
      link.classList.remove('active-item');
    });

    window.scrollTo({ top: 120, behavior: 'smooth' });
  }

  if (btnClearSelection) {
    btnClearSelection.addEventListener('click', clearSelectedCondition);
  }

  // ==========================================================================
  // 2a. Helpers Compartilhados de Observações Contextuais & Árvore Dinâmica
  // ==========================================================================
  function escHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function formatObservationTextHtml(rawText) {
    const match = String(rawText || '').match(
      /^(Otimização de Dose|Regra de Aplicação|Ajuste de Segurança|Adaptação Clínica(?:\s*\([^)]+\))?|Abrangência Muscular(?:\s*\([^)]+\))?|Reserva Legal(?:\s*\([^)]+\))?):\s*(.+)$/i
    );
    if (!match) return escHtml(rawText);
    return `<span class="obs-semantic-tag">${escHtml(match[1])}</span>${escHtml(match[2])}`;
  }

  function buildObservationsHtml(obsList, opts = {}) {
    if (!Array.isArray(obsList) || obsList.length === 0) return '';
    const seen = new Set();
    const items = [];
    obsList.forEach(obs => {
      const key = obs.id || obs.texto;
      if (!obs || !obs.texto || seen.has(key)) return;
      seen.add(key);

      const sev = String(obs.severidade || 'info').toLowerCase();
      const sevCls = sev === 'danger' || sev === 'critical' || sev === 'alerta'
        ? 'obs-sev-danger'
        : (sev === 'warning' || sev === 'atencao' || sev === 'alert' ? 'obs-sev-warning' : 'obs-sev-info');

      const doiUrl = obs.referencia_doi
        ? (obs.referencia_doi.startsWith('http') ? obs.referencia_doi : `https://doi.org/${obs.referencia_doi}`)
        : '';
      const doiHtml = doiUrl
        ? `<div class="obs-action-row"><a href="${escHtml(doiUrl)}" target="_blank" rel="noopener noreferrer" class="obs-action-link">${escHtml(obs.referencia_rotulo || 'Consultar referência oficial')} ↗</a></div>`
        : '';

      const redirectHtml = obs.acao_condicao_id
        ? `<div class="obs-action-row"><button type="button" class="obs-redirect-btn" data-obs-redirect-cond="${escHtml(obs.acao_condicao_id)}">${escHtml(obs.acao_rotulo || 'Abrir Protocolo Recomendado')} ➔</button></div>`
        : '';

      items.push(`
        <div class="obs-contextual-item ${sevCls}${opts.compact ? ' obs-compact' : ''}">
          <div class="obs-contextual-text">${formatObservationTextHtml(obs.texto)}</div>
          ${doiHtml}${redirectHtml}
        </div>
      `);
    });

    if (items.length === 0) return '';
    return `<div class="obs-contextual-list${opts.compact ? ' obs-compact' : ''}">${items.join('')}</div>`;
  }

  function bindObsRedirectButtons(rootEl) {
    if (!rootEl) return;
    rootEl.querySelectorAll('[data-obs-redirect-cond]').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetCondId = btn.getAttribute('data-obs-redirect-cond');
        if (targetCondId) {
          switchTab('prescription');
          openConditionAlgorithm(targetCondId, { forceEntryMode: 'new' });
        }
      });
    });
  }

  function renderObservationsSlot(containerEl, obsList, opts = {}) {
    if (!containerEl) return;
    const html = buildObservationsHtml(obsList, opts);
    if (!html) {
      containerEl.innerHTML = '';
      containerEl.style.display = 'none';
      return;
    }
    containerEl.innerHTML = html;
    containerEl.style.display = 'block';
    bindObsRedirectButtons(containerEl);
  }

  function collectTreeProtocolLeaves(tree) {
    if (!tree || !Array.isArray(tree.etapas) || tree.etapas.length === 0) return [];
    const stepMap = {};
    tree.etapas.forEach(s => {
      stepMap[s.etapa_id] = s;
    });

    const leaves = [];
    const seenKeys = new Set();

    function walk(stepId, rootOptId, crumbs, visited) {
      if (!stepId || visited.has(stepId)) return;
      const step = stepMap[stepId];
      if (!step) return;
      visited.add(stepId);

      (step.opcoes || []).forEach(opt => {
        const nextRoot = rootOptId || opt.id;
        const cleanRotulo = String(opt.rotulo || '').trim();
        const nextCrumbs = cleanRotulo ? [...crumbs, cleanRotulo] : [...crumbs];
        const targetKey = opt.modalidade_chave || opt.protocolo_alvo;
        if (targetKey && !seenKeys.has(targetKey)) {
          seenKeys.add(targetKey);
          leaves.push({
            key: targetKey,
            primary: nextRoot,
            crumbs: nextCrumbs,
            opt
          });
        }
        if (opt.proxima_etapa) {
          walk(opt.proxima_etapa, nextRoot, nextCrumbs, new Set(visited));
        }
      });
    }

    walk(tree.etapas[0].etapa_id, null, [], new Set());
    return leaves;
  }

  function resolveModalityForFactor(cond, factorId) {
    if (!cond) return null;
    if (cond.modalidades && cond.modalidades[factorId]) return cond.modalidades[factorId];
    const trees = Object.values(cond.arvore_algoritmo || {});
    for (const tree of trees) {
      const leaves = collectTreeProtocolLeaves(tree);
      const match = leaves.find(l => l.primary === factorId || l.key === factorId);
      if (match && cond.modalidades?.[match.key]) return cond.modalidades[match.key];
    }
    const allMods = Object.values(cond.modalidades || {});
    return allMods.length > 0 ? allMods[0] : null;
  }

  function formatDottedIndicator(linhaFluxograma) {
    if (linhaFluxograma !== 'pontilhada') return '';
    return '<span class="protocol-dotted-flag" title="Quadrado pontilhado no fluxograma oficial NAPeN: protocolo cujo nível de evidência científica ainda não foi validado por metanálises">Borda pontilhada · Evidência ainda não validada por metanálises</span>';
  }

  // ==========================================================================
  // 2b. Triagem de Continuidade Clínica (Homepage + Barra Compacta Interna)
  // ==========================================================================
  function getContinuityProtocolOptions(cond, modalityOverride = null) {
    if (!cond) return [];
    const trees = cond.arvore_algoritmo || {};
    const modType = modalityOverride || engine.activeModalityType || 'rtms';
    const tree = trees[modType] || Object.values(trees)[0];

    if (tree) {
      const leaves = collectTreeProtocolLeaves(tree);
      if (leaves.length > 0) {
        return leaves.map(leaf => {
          const m = cond.modalidades?.[leaf.key];
          const pathSummary = leaf.crumbs.map(c => c.split('(')[0].trim()).filter(Boolean).join(' › ');
          const techName = m?.tecnica ? ` — ${m.tecnica}` : '';
          const dottedTag = m?.linha_fluxograma === 'pontilhada' ? ' [Linha pontilhada]' : '';
          return {
            key: leaf.key,
            primary: leaf.primary,
            label: `${pathSummary}${techName}${dottedTag}`
          };
        });
      }
    }

    return (cond.fatores_limitantes || []).map(f => ({
      key: f.id,
      primary: f.id,
      label: f.label
    }));
  }

  function scrollToCalculatorHighlight() {
    setTimeout(() => {
      if (!dualCalcContainer) return;
      const headerEl = document.querySelector('.site-header');
      const headerHeight = headerEl ? headerEl.offsetHeight : 140;
      const rect = dualCalcContainer.getBoundingClientRect();
      const targetScrollY = window.pageYOffset + rect.top - headerHeight - 16;
      window.scrollTo({ top: Math.max(0, targetScrollY), behavior: 'smooth' });
      dualCalcContainer.classList.add('calc-highlight-pulse');
      setTimeout(() => dualCalcContainer.classList.remove('calc-highlight-pulse'), 2500);
    }, 100);
  }

  function scrollToResponseAssistantHighlight() {
    setTimeout(() => {
      if (!responseAssistantPanel) return;
      const headerEl = document.querySelector('.site-header');
      const headerHeight = headerEl ? headerEl.offsetHeight : 140;
      const rect = responseAssistantPanel.getBoundingClientRect();
      const targetScrollY = window.pageYOffset + rect.top - headerHeight - 16;
      window.scrollTo({ top: Math.max(0, targetScrollY), behavior: 'smooth' });
      responseAssistantPanel.classList.add('calc-highlight-pulse');
      setTimeout(() => responseAssistantPanel.classList.remove('calc-highlight-pulse'), 2500);
    }, 120);
  }

  function getDynamicAltStagesForActiveModality() {
    const m = engine.getActiveModality();
    const chain = engine.getProtocolChain();
    const altSteps = chain.filter(s => s.stageKey !== 'primary');
    if (altSteps.length > 0) {
      return altSteps.map((s) => {
        const isAj = s.fase_etapa === 'ajustes';
        const isDot = s.linha_fluxograma === 'pontilhada';
        const shortLabel = isAj ? 'Seção de Ajustes' : (isDot ? 'Linha Pontilhada' : 'Próximo Protocolo');
        return {
          stageKey: s.stageKey,
          faseEtapa: s.fase_etapa || (isAj ? 'ajustes' : 'sequencia'),
          linhaFluxograma: s.linha_fluxograma || '',
          shortLabel,
          nome: s.nome || shortLabel,
          etapaRotulo: s.etapa_rotulo || shortLabel
        };
      });
    }
    if (chain.length > 0) {
      return [];
    }
    const fallback = [];
    if (m?.protocolo_alternativo && !String(m.protocolo_alternativo.nome || '').includes('Protocolo Único')) {
      fallback.push({
        stageKey: 'alt1',
        faseEtapa: 'sequencia',
        linhaFluxograma: m.protocolo_alternativo.linha_fluxograma || '',
        shortLabel: 'Próximo Protocolo',
        nome: m.protocolo_alternativo.nome || 'Próximo Protocolo na Sequência',
        etapaRotulo: 'Próximo Protocolo na Sequência'
      });
    }
    if (m?.protocolo_alternativo_2 && !String(m.protocolo_alternativo_2.nome || '').includes('Protocolo Único')) {
      fallback.push({
        stageKey: 'alt2',
        faseEtapa: 'ajustes',
        linhaFluxograma: m.protocolo_alternativo_2.linha_fluxograma || '',
        shortLabel: 'Seção de Ajustes',
        nome: m.protocolo_alternativo_2.nome || 'Seção de Ajustes',
        etapaRotulo: 'Seção de Ajustes'
      });
    }
    return fallback;
  }

  function renderContinuingFocusSlot(cond) {
    if (!continuingStageFocusSlot) return;
    if (engine.entryMode !== 'returning' || engine.continuingStage === 'evaluation' || engine.continuingStage === 'primary') {
      continuingStageFocusSlot.style.display = 'none';
      continuingStageFocusSlot.innerHTML = '';
      continuingStageFocusSlot.className = 'continuing-focus-slot';
      return;
    }

    const stage = engine.continuingStage;
    const stageData = engine.getPrescriptionForStage(stage);
    if (!stageData) return;

    continuingStageFocusSlot.style.display = 'flex';
    continuingStageFocusSlot.className = `continuing-focus-slot stage-${stage}`;
    continuingStageFocusSlot.innerHTML = `
      <div class="continuing-focus-header">
        <div>
          <span class="continuing-focus-kicker">Acompanhamento Direto · Assistente de Resposta Clínica (Pós-Indução)</span>
          <h3 class="continuing-focus-title">${escHtml(stageData.titulo)}</h3>
        </div>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
          <button type="button" class="btn-step-action primary" id="btnTopJumpAssistant">Ver Protocolo no Assistente ↓</button>
          <button type="button" class="btn-reopen-triage" id="btnReopenFullTriage">Reabrir triagem diagnóstica completa</button>
        </div>
      </div>
    `;

    document.getElementById('btnTopJumpAssistant')?.addEventListener('click', scrollToResponseAssistantHighlight);
    document.getElementById('btnReopenFullTriage')?.addEventListener('click', () => {
      engine.setEntryMode('new');
      state.therapeuticStage = 'primary';
      engine.setOutcome(null);
      renderContinuityBar(cond);
      renderModalitySelector(cond);
      renderCascadingFlow(cond);
      renderNode1Options(cond);
      renderTolerabilityUI();
      updatePrescriptionDisplay();
      updateOutcomeDisplay();
    });
  }

  function selectContinuityStage(cond, stage) {
    engine.setEntryMode('returning', stage);
    if (stage === 'evaluation') {
      state.therapeuticStage = 'primary';
      renderContinuityBar(cond);
      updatePrescriptionDisplay();
      scrollToCalculatorHighlight();
    } else {
      state.therapeuticStage = stage;
      engine.setOutcome('danger');
      renderContinuityBar(cond);
      updatePrescriptionDisplay();
      updateOutcomeDisplay();
      scrollToResponseAssistantHighlight();
    }
  }

  function renderContinuityBar(cond) {
    if (!cond) return;
    const isReturning = engine.entryMode === 'returning';

    if (btnSwitchToContinuing) {
      btnSwitchToContinuing.style.display = isReturning ? 'none' : 'inline-flex';
    }

    if (!continuityEntryBar) return;

    if (!isReturning) {
      continuityEntryBar.style.display = 'none';
      if (continuityInlineContext) continuityInlineContext.innerHTML = '';
      renderContinuingFocusSlot(cond);
      return;
    }

    continuityEntryBar.style.display = 'flex';
    if (continuityCompactBar) continuityCompactBar.style.display = 'block';
    if (!continuityInlineContext) return;

    const mods = cond.modalidades_suportadas || [];
    const modSelectHtml = mods.length > 1
      ? `<label class="continuity-inline-label" for="contSelectModality">Modalidade:</label>
         <select id="contSelectModality" class="continuity-inline-select">
           ${mods.map(m => `<option value="${m.id}" ${engine.activeModalityType === m.id ? 'selected' : ''}>${m.id.toUpperCase()}</option>`).join('')}
         </select>`
      : '';

    const protOptions = getContinuityProtocolOptions(cond);
    const activeProtKey = engine.activeFactorId || engine.primaryFactorId;
    const protSelectHtml = `
      <label class="continuity-inline-label" for="contSelectProtocol">Desfecho / Árvore Clínica:</label>
      <select id="contSelectProtocol" class="continuity-inline-select">
        ${protOptions.map(o => `<option value="${o.key}" data-primary="${o.primary}" ${activeProtKey === o.key ? 'selected' : ''}>${escHtml(o.label)}</option>`).join('')}
      </select>
    `;

    const curStage = engine.continuingStage || 'evaluation';
    const altStages = getDynamicAltStagesForActiveModality();
    const altBtnsHtml = altStages.map(a => `
      <button type="button" class="btn-stage-shortcut ${a.faseEtapa === 'ajustes' ? 'stage-adjust' : ''} ${curStage === a.stageKey ? 'active' : ''}" data-stage="${a.stageKey}" title="${escHtml(a.nome)}">${escHtml(a.faseEtapa === 'ajustes' ? `Ajustes: ${a.nome}` : a.nome)}</button>
    `).join('');

    continuityInlineContext.innerHTML = `
      <div class="continuity-context-fields">
        ${modSelectHtml}
        ${protSelectHtml}
      </div>
      <div class="continuity-stage-shortcuts">
        <span class="continuity-inline-label">Ir no Assistente Pós-Indução:</span>
        <button type="button" class="btn-stage-shortcut ${curStage === 'evaluation' ? 'active' : ''}" data-stage="evaluation">Avaliar Resposta (Calculadora)</button>
        ${altBtnsHtml}
        <button type="button" class="btn-stage-shortcut stage-danger ${curStage === 'failure' ? 'active' : ''}" data-stage="failure">Falha Terapêutica (Encerramento)</button>
        <button type="button" class="btn-reopen-triage" id="btnReopenFullTriageBar">Voltar à triagem inicial</button>
      </div>
    `;

    const selMod = document.getElementById('contSelectModality');
    if (selMod) {
      selMod.addEventListener('change', (e) => {
        engine.setModalityType(e.target.value);
        renderContinuityBar(cond);
        renderNode1Options(cond);
        renderTolerabilityUI();
        updatePrescriptionDisplay();
        if (state.therapeuticStage !== 'primary') updateOutcomeDisplay();
      });
    }

    const selProt = document.getElementById('contSelectProtocol');
    if (selProt) {
      selProt.addEventListener('change', (e) => {
        const selectedOpt = e.target.options[e.target.selectedIndex];
        const key = selectedOpt.value;
        const primaryKey = selectedOpt.getAttribute('data-primary') || key;
        engine.setFactor(primaryKey, true);
        if (key !== primaryKey) {
          engine.setFactor(key, false);
        }
        renderContinuityBar(cond);
        renderNode1Options(cond);
        renderTolerabilityUI();
        updatePrescriptionDisplay();
        if (state.therapeuticStage !== 'primary') updateOutcomeDisplay();
      });
    }

    continuityInlineContext.querySelectorAll('.btn-stage-shortcut').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetStage = btn.getAttribute('data-stage');
        selectContinuityStage(cond, targetStage);
      });
    });

    document.getElementById('btnReopenFullTriageBar')?.addEventListener('click', () => {
      engine.setEntryMode('new');
      state.therapeuticStage = 'primary';
      engine.setOutcome(null);
      renderContinuityBar(cond);
      renderModalitySelector(cond);
      renderCascadingFlow(cond);
      renderNode1Options(cond);
      renderTolerabilityUI();
      updatePrescriptionDisplay();
      updateOutcomeDisplay();
    });

    renderContinuingFocusSlot(cond);
  }

  function populateHomeContinuityConditions() {
    if (!homeContCondition || !data?.condicoes?.length) return;
    homeContCondition.innerHTML = '';

    const groups = new Map();
    data.condicoes.forEach(c => {
      const axis = c.eixo || 'Condições Clínicas';
      if (!groups.has(axis)) groups.set(axis, []);
      groups.get(axis).push(c);
    });

    groups.forEach((conds, axisName) => {
      const og = document.createElement('optgroup');
      og.label = axisName;
      conds.forEach(c => {
        const opt = document.createElement('option');
        opt.value = c.id;
        opt.textContent = c.condicao;
        og.appendChild(opt);
      });
      homeContCondition.appendChild(og);
    });

    if (!state.homeSelectedConditionId || !engine.getCondition(state.homeSelectedConditionId)) {
      state.homeSelectedConditionId = data.condicoes[0].id;
    }
    homeContCondition.value = state.homeSelectedConditionId;
  }

  function getHomeModalityForSelection(cond) {
    if (!cond) return null;
    const selectedProtOpt = homeContProtocol && homeContProtocol.options[homeContProtocol.selectedIndex];
    const protOptions = getContinuityProtocolOptions(cond, state.homeSelectedModality);
    const factorKey = (selectedProtOpt && selectedProtOpt.value) || protOptions[0]?.key || null;
    return (factorKey && cond.modalidades?.[factorKey]) || Object.values(cond.modalidades || {})[0] || null;
  }

  function getStoppedChainForHomeModality(mod) {
    if (!mod) return [];
    const chain = Array.isArray(mod.cadeia_sequencial) ? mod.cadeia_sequencial : [];
    if (chain.length > 0) {
      return chain.map((step, idx) => ({
        stageKey: idx === 0 ? 'primary' : `alt${idx}`,
        nome: step.nome || step.tecnica || mod.tecnica || 'Protocolo Clínico',
        faseEtapa: idx === 0
          ? 'inicial'
          : ((step.fase_etapa === 'ajustes' || /ajustes/i.test(step.etapa_rotulo || '')) ? 'ajustes' : 'sequencia'),
        linhaFluxograma: step.linha_fluxograma || mod.linha_fluxograma || ''
      }));
    }
    const items = [{
      stageKey: 'primary',
      nome: mod.tecnica || 'Protocolo Inicial',
      faseEtapa: 'inicial',
      linhaFluxograma: mod.linha_fluxograma || ''
    }];
    if (mod.protocolo_alternativo && !String(mod.protocolo_alternativo.nome || '').includes('Protocolo Único')) {
      items.push({
        stageKey: 'alt1',
        nome: mod.protocolo_alternativo.nome || 'Próximo Protocolo na Sequência',
        faseEtapa: 'sequencia',
        linhaFluxograma: mod.protocolo_alternativo.linha_fluxograma || ''
      });
    }
    if (mod.protocolo_alternativo_2 && !String(mod.protocolo_alternativo_2.nome || '').includes('Protocolo Único')) {
      items.push({
        stageKey: 'alt2',
        nome: mod.protocolo_alternativo_2.nome || 'Seção de Ajustes',
        faseEtapa: 'ajustes',
        linhaFluxograma: mod.protocolo_alternativo_2.linha_fluxograma || ''
      });
    }
    return items;
  }

  function populateHomeStoppedProtocols(cond) {
    if (!homeContStoppedProtocol || !cond) return;
    const mod = getHomeModalityForSelection(cond);
    const steps = getStoppedChainForHomeModality(mod);
    const prevVal = homeContStoppedProtocol.value;
    homeContStoppedProtocol.innerHTML = steps.map((step, idx) => {
      const tag = idx === 0
        ? 'Protocolo Inicial'
        : (step.faseEtapa === 'ajustes'
          ? 'Seção de Ajustes'
          : (step.linhaFluxograma === 'pontilhada' ? 'Linha Pontilhada' : 'Na Sequência'));
      return `<option value="${escHtml(step.stageKey)}">[${tag}] ${escHtml(step.nome)}</option>`;
    }).join('');
    if (steps.some(s => s.stageKey === prevVal)) {
      homeContStoppedProtocol.value = prevVal;
    } else if (steps.length > 0) {
      homeContStoppedProtocol.value = steps[0].stageKey;
    }
  }

  function renderHomeContinuityStageButtons(cond) {
    if (!homeContStageShortcuts || !cond) return;
    const mod = getHomeModalityForSelection(cond);
    const steps = getStoppedChainForHomeModality(mod);
    const stoppedStage = (homeContStoppedProtocol && homeContStoppedProtocol.value) || 'primary';
    const stoppedIdx = Math.max(0, steps.findIndex(s => s.stageKey === stoppedStage));
    const hasNext = stoppedIdx + 1 < steps.length;
    const nextStep = hasNext ? steps[stoppedIdx + 1] : null;
    const isUnique = steps.length <= 1;

    let nextBtnHtml = '';
    if (nextStep) {
      const isAj = nextStep.faseEtapa === 'ajustes';
      const prefix = isAj ? 'Ir para Seção de Ajustes: ' : 'Avançar para ';
      nextBtnHtml = `<button type="button" class="btn-stage-shortcut stage-danger" data-home-stage="${escHtml(nextStep.stageKey)}">Resposta Insatisfatória ➔ ${prefix}${escHtml(nextStep.nome)}</button>`;
    } else if (isUnique) {
      nextBtnHtml = `<button type="button" class="btn-stage-shortcut stage-danger" data-home-stage="failure">Sem Resposta ao Protocolo Único ➔ Falha Terapêutica / Encerramento</button>`;
    } else {
      nextBtnHtml = `<button type="button" class="btn-stage-shortcut stage-danger" data-home-stage="failure">Sem Resposta após Sequência e Ajustes ➔ Falha Terapêutica</button>`;
    }

    homeContStageShortcuts.innerHTML = `
      ${nextBtnHtml}
      <button type="button" class="btn-stage-shortcut" data-home-stage="evaluation">Avaliar Resposta do Protocolo (Calculadora)</button>
    `;
  }

  function renderHomeContinuityPanel() {
    if (!homeContinuityPanel) return;
    const isReturning = state.homeEntryMode === 'returning';

    if (btnHomeEntryNew) btnHomeEntryNew.classList.toggle('active', !isReturning);
    if (btnHomeEntryReturning) btnHomeEntryReturning.classList.toggle('active', isReturning);

    if (!homeContinuityQuickPanel) return;
    if (!isReturning) {
      homeContinuityQuickPanel.style.display = 'none';
      return;
    }

    homeContinuityQuickPanel.style.display = 'flex';
    const condId = state.homeSelectedConditionId || data?.condicoes?.[0]?.id;
    const cond = engine.getCondition(condId);
    if (!cond) return;

    if (homeContCondition && homeContCondition.value !== cond.id) {
      homeContCondition.value = cond.id;
    }

    const mods = cond.modalidades_suportadas || [];
    const hasSelectedMod = mods.some(m => m.id === state.homeSelectedModality);
    if (!hasSelectedMod) {
      state.homeSelectedModality = mods[0]?.id || 'rtms';
    }

    if (homeContModalityWrap && homeContModality) {
      if (mods.length > 1) {
        homeContModalityWrap.style.display = 'flex';
        homeContModality.innerHTML = mods
          .map(m => `<option value="${m.id}" ${state.homeSelectedModality === m.id ? 'selected' : ''}>${m.id.toUpperCase()}</option>`)
          .join('');
      } else {
        homeContModalityWrap.style.display = 'none';
      }
    }

    if (homeContProtocol) {
      const protOptions = getContinuityProtocolOptions(cond, state.homeSelectedModality);
      homeContProtocol.innerHTML = protOptions
        .map(o => `<option value="${o.key}" data-primary="${o.primary}">${escHtml(o.label)}</option>`)
        .join('');
    }
    populateHomeStoppedProtocols(cond);
    renderHomeContinuityStageButtons(cond);
  }

  if (btnHomeEntryNew) {
    btnHomeEntryNew.addEventListener('click', () => {
      state.homeEntryMode = 'new';
      renderHomeContinuityPanel();
    });
  }

  if (btnHomeEntryReturning) {
    btnHomeEntryReturning.addEventListener('click', () => {
      state.homeEntryMode = 'returning';
      renderHomeContinuityPanel();
    });
  }

  if (homeContCondition) {
    homeContCondition.addEventListener('change', (e) => {
      state.homeSelectedConditionId = e.target.value;
      state.homeSelectedModality = 'rtms';
      if (homeContStoppedProtocol) homeContStoppedProtocol.value = '';
      renderHomeContinuityPanel();
    });
  }

  if (homeContModality) {
    homeContModality.addEventListener('change', (e) => {
      state.homeSelectedModality = e.target.value;
      if (homeContStoppedProtocol) homeContStoppedProtocol.value = '';
      renderHomeContinuityPanel();
    });
  }

  if (homeContProtocol) {
    homeContProtocol.addEventListener('change', () => {
      const condId = (homeContCondition && homeContCondition.value) || state.homeSelectedConditionId;
      const cond = engine.getCondition(condId);
      if (homeContStoppedProtocol) homeContStoppedProtocol.value = '';
      populateHomeStoppedProtocols(cond);
      renderHomeContinuityStageButtons(cond);
    });
  }

  if (homeContStoppedProtocol) {
    homeContStoppedProtocol.addEventListener('change', () => {
      const condId = (homeContCondition && homeContCondition.value) || state.homeSelectedConditionId;
      renderHomeContinuityStageButtons(engine.getCondition(condId));
    });
  }

  if (homeContStageShortcuts) {
    homeContStageShortcuts.addEventListener('click', (e) => {
      const btn = e.target.closest('[data-home-stage]');
      if (!btn) return;
      const targetStage = btn.getAttribute('data-home-stage');
      const condId = (homeContCondition && homeContCondition.value) || state.homeSelectedConditionId;
      if (!condId) return;

      const selectedProtOpt = homeContProtocol && homeContProtocol.options[homeContProtocol.selectedIndex];
      const factorKey = selectedProtOpt ? selectedProtOpt.value : null;
      const primaryKey = selectedProtOpt ? (selectedProtOpt.getAttribute('data-primary') || factorKey) : factorKey;

      state.homeEntryMode = 'returning';
      openConditionAlgorithm(condId, {
        forceEntryMode: 'returning',
        modalityType: state.homeSelectedModality || 'rtms',
        factorKey,
        primaryKey,
        continuingStage: targetStage
      });

      if (targetStage === 'evaluation') {
        scrollToCalculatorHighlight();
      } else {
        scrollToResponseAssistantHighlight();
      }
    });
  }

  if (btnSwitchToContinuing) {
    btnSwitchToContinuing.addEventListener('click', () => {
      const cond = engine.getCondition(state.selectedConditionId);
      if (!cond) return;
      engine.setEntryMode('returning', 'evaluation');
      renderContinuityBar(cond);
      renderModalitySelector(cond);
      renderCascadingFlow(cond);
      updatePrescriptionDisplay();
    });
  }

  // ==========================================================================
  // 3a. Seletor de Modalidade Terapêutica (rTMS vs. tDCS)
  // ==========================================================================
  function renderModalitySelector(cond) {
    if (!modalitySelectorBar || !modalityPillsGroup) return;

    if (engine.entryMode === 'returning') {
      modalitySelectorBar.style.display = 'none';
      return;
    }

    const mods = cond.modalidades_suportadas || [];
    if (mods.length <= 1) {
      modalitySelectorBar.style.display = 'none';
      modalityPillsGroup.innerHTML = '';
      return;
    }

    modalitySelectorBar.style.display = 'flex';
    modalityPillsGroup.innerHTML = '';

    mods.forEach(m => {
      const btn = document.createElement('button');
      btn.type = 'button';
      const isActive = engine.activeModalityType === m.id;
      btn.className = `btn-modality-pill ${isActive ? 'active' : ''}`;
      btn.textContent = m.nome;

      btn.addEventListener('click', () => {
        engine.setModalityType(m.id);
        renderModalitySelector(cond);
        renderCascadingFlow(cond);
        renderNode1Options(cond);
        updatePrescriptionDisplay();
      });

      modalityPillsGroup.appendChild(btn);
    });
  }

  // ==========================================================================
  // 3b. Árvore de Decisão Algorítmica em Cascata Progressiva (100% Dinâmica)
  // Conecta sequencialmente: Fator Limitante ➔ Sub-nós do Roadmap ➔ Protocolo
  // ==========================================================================
  function renderCascadingFlow(cond) {
    if (!cascadingFlowContainer) return;
    if (engine.entryMode === 'returning') {
      renderObservationsSlot(preTriagemObservationsSlot, []);
      cascadingFlowContainer.style.display = 'none';
      cascadingFlowContainer.innerHTML = '';
      return;
    }
    cascadingFlowContainer.innerHTML = '';
    cascadingFlowContainer.style.display = 'flex';

    const node1Panel = document.getElementById('node1Panel');
    if (node1Panel) node1Panel.style.display = 'none';

    // Slot PRE-TRIAGEM (redirecionamentos transversais, exclusões e avisos pré-avaliação)
    const preObs = engine.getContextualObservations({ slot: 'pre' });
    renderObservationsSlot(preTriagemObservationsSlot, preObs);

    let currentStepNum = 0;
    const trailCrumbs = [];
    const seenStepObsIds = new Set();

    const tree = engine.getActiveTree();
    if (tree && Array.isArray(tree.etapas) && tree.etapas.length > 0) {
      const stepMap = {};
      tree.etapas.forEach(s => {
        stepMap[s.etapa_id] = s;
      });

      const visitedSteps = new Set();
      let nextStepId = tree.etapas[0].etapa_id;

      while (nextStepId && !visitedSteps.has(nextStepId)) {
        const step = stepMap[nextStepId];
        if (!step || !Array.isArray(step.opcoes) || step.opcoes.length === 0) break;
        visitedSteps.add(nextStepId);

        currentStepNum += 1;

        if (currentStepNum > 1) {
          const connectorSub = document.createElement('div');
          connectorSub.className = 'cascading-connector-line';
          cascadingFlowContainer.appendChild(connectorSub);
        }

        const stepCard = document.createElement('div');
        stepCard.className = 'cascading-step-card active-step';

        let currentChoiceId = engine.getPathChoice(step.etapa_id);
        if (!currentChoiceId || !step.opcoes.some(o => o.id === currentChoiceId)) {
          currentChoiceId = step.opcoes[0].id;
          engine.setPathChoice(step.etapa_id, currentChoiceId);
        }

        const isRootStep = step.etapa_id === 'fator_limitante' || currentStepNum === 1;
        const stepQuestion = isRootStep
          ? (step.pergunta || cond.no1_pergunta || 'Qual é o principal fator limitante ou queixa funcional do paciente?')
          : (step.pergunta || 'Selecione a estratificação clínica do protocolo:');
        const stepSubtitle = step.subtitulo
          || (isRootStep ? 'A seleção do fator limitante direciona o desfecho clínico, a escala de avaliação e a linha de prescrição.' : '');

        const stepHeader = document.createElement('div');
        stepHeader.className = 'cascading-step-header';
        stepHeader.innerHTML = `
          <span class="cascading-step-badge">Etapa ${currentStepNum}</span>
          <div class="cascading-step-title-box">
            <h4 class="cascading-step-question">${escHtml(stepQuestion)}</h4>
            ${stepSubtitle ? `<span class="cascading-step-subtext">${escHtml(stepSubtitle)}</span>` : ''}
          </div>
        `;
        stepCard.appendChild(stepHeader);

        const stepOptsRow = document.createElement('div');
        stepOptsRow.className = 'cascading-options-row';

        step.opcoes.forEach(opt => {
          const btnOpt = document.createElement('button');
          btnOpt.type = 'button';
          const isOptActive = currentChoiceId === opt.id;
          const targetLeafKey = opt.modalidade_chave || opt.protocolo_alvo;
          const targetLeafMod = targetLeafKey ? cond.modalidades?.[targetLeafKey] : null;
          const isDottedOpt = opt.linha_fluxograma === 'pontilhada' || targetLeafMod?.linha_fluxograma === 'pontilhada';

          btnOpt.className = `btn-cascade-choice ${isOptActive ? 'active' : ''} ${isDottedOpt ? 'btn-cascade-dotted' : ''}`.trim();

          const subtextoFinal = opt.subtexto || (isDottedOpt ? 'Linha pontilhada · Conduta exploratória' : '');
          btnOpt.innerHTML = `
            <span>${escHtml(opt.rotulo)}</span>
            ${subtextoFinal ? `<span class="btn-cascade-sub">${escHtml(subtextoFinal)}</span>` : ''}
          `;

          btnOpt.addEventListener('click', () => {
            engine.setPathChoice(step.etapa_id, opt.id);

            if (opt.id === 'pem_sim') {
              state.pemStatus = 'sim';
              if (btnPemSim) btnPemSim.classList.add('active');
              if (btnPemNao) btnPemNao.classList.remove('active');
            } else if (opt.id === 'pem_nao') {
              state.pemStatus = 'nao';
              if (btnPemNao) btnPemNao.classList.add('active');
              if (btnPemSim) btnPemSim.classList.remove('active');
            }

            if (targetLeafKey) {
              engine.setFactor(targetLeafKey, false);
            }

            renderCascadingFlow(cond);
            renderNode1Options(cond);
            updatePrescriptionDisplay();
          });

          stepOptsRow.appendChild(btnOpt);
        });

        stepCard.appendChild(stepOptsRow);

        // Observações inline da Etapa (SLOT-STEP), incluindo guia PEM e notas condicionais
        const rawStepObs = engine.getContextualObservations({
          slot: 'step',
          etapaId: step.etapa_id,
          optionId: currentChoiceId
        }).filter(o => {
          const k = o.id || o.texto;
          if (seenStepObsIds.has(k)) return false;
          seenStepObsIds.add(k);
          return true;
        });

        if (rawStepObs.length > 0) {
          const stepObsEl = document.createElement('div');
          stepObsEl.className = 'step-inline-obs-slot';
          stepObsEl.innerHTML = buildObservationsHtml(rawStepObs, { compact: true });
          stepCard.appendChild(stepObsEl);
          bindObsRedirectButtons(stepObsEl);
        }

        cascadingFlowContainer.appendChild(stepCard);

        const chosenOpt = step.opcoes.find(o => o.id === currentChoiceId) || step.opcoes[0];
        if (chosenOpt) {
          const crumbText = String(chosenOpt.rotulo || '').split('(')[0].trim();
          if (crumbText) trailCrumbs.push(crumbText);

          if (currentStepNum === 1) {
            const mods = cond.modalidades_suportadas || [];
            const activeModObj = mods.find(m => m.id === engine.activeModalityType) || mods[0];
            if (activeModObj) {
              trailCrumbs.push(activeModObj.id === 'integrado' ? 'rTMS + tDCS' : activeModObj.id.toUpperCase());
            }
          }

          nextStepId = chosenOpt.proxima_etapa || null;
        } else {
          nextStepId = null;
        }
      }
    } else {
      // Fallback defensivo se alguma condição não possuir arvore_algoritmo
      currentStepNum += 1;
      const step1Card = document.createElement('div');
      step1Card.className = 'cascading-step-card active-step';
      const factors = cond.fatores_limitantes || [];
      const activeFactorObj = factors.find(f => f.id === (engine.primaryFactorId || engine.activeFactorId)) || factors[0];
      if (activeFactorObj) trailCrumbs.push((activeFactorObj.label || activeFactorObj.nome || '').split('(')[0].trim());
      step1Card.innerHTML = `
        <div class="cascading-step-header">
          <span class="cascading-step-badge">Etapa 1</span>
          <div class="cascading-step-title-box">
            <h4 class="cascading-step-question">${escHtml(cond.no1_pergunta || 'Principal fator limitante')}</h4>
          </div>
        </div>
      `;
      const row = document.createElement('div');
      row.className = 'cascading-options-row';
      factors.forEach(f => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `btn-cascade-choice ${(engine.primaryFactorId || engine.activeFactorId) === f.id ? 'active' : ''}`;
        btn.innerHTML = `<span>${escHtml(f.label || f.nome || '')}</span>`;
        btn.addEventListener('click', () => {
          engine.setFactor(f.id, true);
          renderCascadingFlow(cond);
          renderNode1Options(cond);
          updatePrescriptionDisplay();
        });
        row.appendChild(btn);
      });
      step1Card.appendChild(row);
      cascadingFlowContainer.appendChild(step1Card);
    }

    // ------------------------------------------------------------------------
    // Painel Resumo do Percurso Clínico Selecionado
    // ------------------------------------------------------------------------
    if (trailCrumbs.length > 0) {
      const summaryBox = document.createElement('div');
      summaryBox.className = 'cascading-active-path-summary';
      const m = engine.getActiveModality();
      const protName = m?.tecnica || 'Protocolo Primário Recomendado';
      const dottedBanner = formatDottedIndicator(m?.linha_fluxograma);

      summaryBox.innerHTML = `
        <div style="display: flex; flex-direction: column; gap: 4px;">
          <span class="cascading-path-label">Percurso Clínico Selecionado:</span>
          <div class="cascading-path-trail">
            ${trailCrumbs.map((c, i) => `
              <span class="cascading-path-crumb">${escHtml(c)}</span>
              ${i < trailCrumbs.length - 1 ? '<span class="cascading-path-arrow">➔</span>' : ''}
            `).join('')}
          </div>
          ${dottedBanner ? `<div style="margin-top: 4px;">${dottedBanner}</div>` : ''}
        </div>
        <div class="cascading-path-protocol-badge">
          ${escHtml(protName)}
        </div>
      `;
      cascadingFlowContainer.appendChild(summaryBox);
    }
  }

  // ==========================================================================
  // 3c. Renderiza Pills do Fator Limitante Principal (Sincronização)
  // ==========================================================================
  function renderNode1Options(cond) {
    if (!node1OptionsList) return;
    node1OptionsList.innerHTML = '';

    const tree = engine.getActiveTree();
    const rootOpts = tree?.etapas?.[0]?.opcoes;
    const factors = (Array.isArray(rootOpts) && rootOpts.length > 0)
      ? rootOpts.map(o => ({ id: o.id, label: o.rotulo }))
      : (cond.fatores_limitantes || []);

    const activeRootChoice = tree?.etapas?.[0] ? engine.getPathChoice(tree.etapas[0].etapa_id) : null;
    const currentFactor = activeRootChoice || engine.primaryFactorId || engine.activeFactorId;

    if (!factors.some(f => f.id === currentFactor) && factors.length > 0) {
      engine.setFactor(factors[0].id, true);
    }

    factors.forEach(f => {
      const btn = document.createElement('button');
      btn.type = 'button';
      const isActive = (activeRootChoice || engine.primaryFactorId || engine.activeFactorId) === f.id;
      btn.className = `pill-factor-btn ${isActive ? 'active' : ''}`;
      btn.textContent = f.label;

      btn.addEventListener('click', () => {
        engine.setFactor(f.id, true);
        renderCascadingFlow(cond);
        renderNode1Options(cond);
        updatePrescriptionDisplay();
      });

      node1OptionsList.appendChild(btn);
    });
  }

  // Listeners dos Botões de Triagem Neurofisiológica (PEM)
  if (btnPemSim) {
    btnPemSim.addEventListener('click', () => {
      state.pemStatus = 'sim';
      btnPemSim.classList.add('active');
      if (btnPemNao) btnPemNao.classList.remove('active');
      const cond = engine.getCondition(state.selectedConditionId);
      if (cond) {
        renderNode1Options(cond);
        updatePrescriptionDisplay();
      }
    });
  }

  if (btnPemNao) {
    btnPemNao.addEventListener('click', () => {
      state.pemStatus = 'nao';
      btnPemNao.classList.add('active');
      if (btnPemSim) btnPemSim.classList.remove('active');
      const cond = engine.getCondition(state.selectedConditionId);
      if (cond) {
        renderNode1Options(cond);
        updatePrescriptionDisplay();
      }
    });
  }


  // ==========================================================================
  // 4. Renderiza Calculadora para a Escala Ativa (Suporte a Múltiplas Escalas e EAM)
  // ==========================================================================
  function renderCalculatorForActiveScale() {
    const m = engine.getActiveModality();
    if (!m) return;

    const scales = engine.getScalesForCurrentPath();

    // 1. Seletor de Múltiplas Escalas (Exibido apenas quando o desfecho selecionado possui mais de um instrumento)
    if (calcScaleTabs) {
      if (scales.length > 1) {
        calcScaleTabs.innerHTML = '';
        calcScaleTabs.style.display = 'flex';

        scales.forEach(s => {
          const tabBtn = document.createElement('button');
          tabBtn.type = 'button';
          const isActive = engine.getActiveScale()?.id === s.id;
          tabBtn.className = `calc-scale-tab-btn ${isActive ? 'active' : ''}`;
          tabBtn.textContent = `Avaliar com ${s.sigla || s.nome}`;

          tabBtn.addEventListener('click', () => {
            engine.setActiveScale(s.id);
            renderCalculatorForActiveScale();
          });

          calcScaleTabs.appendChild(tabBtn);
        });
      } else {
        calcScaleTabs.style.display = 'none';
        calcScaleTabs.innerHTML = '';
      }
    }

    const activeScale = engine.getActiveScale() || (scales.length > 0 ? scales[0] : null);

    // 2. Sincronização em tempo real do tamanho de efeito e meta com a escala selecionada
    const effObj = m?.efeito_clinico || {};
    const eff = activeScale?.tamanho_efeito || effObj.efeito_esperado_resumo || m.tamanho_efeito || 'Eficácia demonstrada em ensaios controlados randomizados.';
    const meta = activeScale?.meta_texto || m.meta_melhora || 'Melhora clinicamente relevante conforme protocolo.';
    const escNome = activeScale?.nome || m.escala_recomendada || 'Escala Clínica Validada';

    // 2. Sincronização em tempo real do estudo de referência, efeito e MCID da literatura
    if (calcRoadmapEffectText) calcRoadmapEffectText.textContent = eff;
    if (prescEfeito) prescEfeito.textContent = eff;
    if (prescMeta) prescMeta.textContent = meta;
    if (prescEscala) prescEscala.textContent = escNome;

    const studyName = effObj.estudo_referencia || m?.ensaio_clinico?.autores || 'Ensaio clínico do protocolo';
    const studyDetail = effObj.estudo_detalhe ? ` (${effObj.estudo_detalhe})` : '';
    if (calcStudyRef) {
      calcStudyRef.textContent = `${studyName}${studyDetail}`;
    }

    if (calcStudyCohen) {
      calcStudyCohen.textContent = effObj.cohen_d || 'd ≈ 0.65 (Efeito Moderado)';
    }

    if (calcStudyMcid) {
      calcStudyMcid.textContent = activeScale?.mcid_label || effObj.mcid_label || activeScale?.meta_texto || m.meta_melhora || 'Ganho clínico relevante';
    }

    // 3. Alternância entre Modo EAM (Graus 0 a 4) e Modo Contínuo
    if (activeScale && activeScale.tipo === 'ordinal_eam') {
      if (calcEamBox) calcEamBox.style.display = 'flex';
      if (calcContinuousInputsRow) calcContinuousInputsRow.style.display = 'none';

      // Reseta seleção visual dos botões EAM
      eamState.base = null;
      eamState.post = null;
      if (eamGroupBase) eamGroupBase.querySelectorAll('.btn-eam').forEach(b => b.classList.remove('active'));
      if (eamGroupPost) eamGroupPost.querySelectorAll('.btn-eam').forEach(b => b.classList.remove('active'));

      if (calcGoalFeedback) {
        calcGoalFeedback.textContent = `Meta do protocolo: ${activeScale.meta_texto}`;
      }
    } else {
      if (calcEamBox) calcEamBox.style.display = 'none';
      if (calcContinuousInputsRow) calcContinuousInputsRow.style.display = 'grid';

      if (calcValBaseLabel) {
        calcValBaseLabel.textContent = `Escore Inicial (${activeScale?.sigla || 'Pré-Tratamento'})`;
      }
      if (calcValPostLabel) {
        calcValPostLabel.textContent = `Escore Pós-Tratamento (${activeScale?.sigla || 'Pós-Tratamento'})`;
      }
      if (calcValBase) {
        calcValBase.value = '';
        calcValBase.placeholder = activeScale?.placeholder || 'Ex: 24';
      }
      if (calcValPost) {
        calcValPost.value = '';
        calcValPost.placeholder = activeScale?.placeholder || 'Ex: 12';
      }
      if (calcGoalFeedback) {
        calcGoalFeedback.textContent = `Meta do protocolo: ${activeScale?.meta_texto || m.meta_melhora || 'Melhora clinicamente relevante.'}`;
      }
    }

    // Reseta cartões de métricas individuais
    if (calcDeltaPoints) calcDeltaPoints.textContent = 'Δ = —';
    if (calcDeltaPercent) calcDeltaPercent.textContent = '— %';
    if (calcMcidBadge) {
      calcMcidBadge.textContent = 'Aguardando escores';
      calcMcidBadge.className = 'calc-metric-val calc-mcid-status';
    }
    if (cardDeltaPoints) cardDeltaPoints.className = 'calc-metric-card';
    if (cardDeltaPercent) cardDeltaPercent.className = 'calc-metric-card';
    if (cardMcidBadge) cardMcidBadge.className = 'calc-metric-card';

    if (calcComparisonFeedback) {
      calcComparisonFeedback.textContent = 'Ao informar os escores, o sistema analisará se o ganho clínico individual é compatível com o intervalo de confiança do ensaio clínico de referência do protocolo e se superou a MCID da escala.';
    }

    // Reseta desfecho ao alternar escala/fator, preservando quando em salto direto de continuidade para etapa sequencial/Ajustes/Falha
    const keepReturningOutcome = engine.entryMode === 'returning'
      && state.therapeuticStage
      && state.therapeuticStage !== 'primary'
      && state.therapeuticStage !== 'evaluation';
    if (!keepReturningOutcome) {
      engine.setOutcome(null);
    }
    updateOutcomeDisplay();
  }

  // Configuração dos Botões de Graus da EAM
  if (eamGroupBase) {
    eamGroupBase.querySelectorAll('.btn-eam').forEach(btn => {
      btn.addEventListener('click', () => {
        eamGroupBase.querySelectorAll('.btn-eam').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        eamState.base = btn.getAttribute('data-val');
        handleScoreComputation();
      });
    });
  }

  if (eamGroupPost) {
    eamGroupPost.querySelectorAll('.btn-eam').forEach(btn => {
      btn.addEventListener('click', () => {
        eamGroupPost.querySelectorAll('.btn-eam').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        eamState.post = btn.getAttribute('data-val');
        handleScoreComputation();
      });
    });
  }

  // ==========================================================================
  // 4b. Helpers de Qualidade Metodológica (AMSTAR 2 / GRADE) & Tolerabilidade
  // ==========================================================================
  function getQualityLevelClass(levelStr) {
    if (!levelStr) return '';
    const v = String(levelStr).toLowerCase();
    if (v.includes('critica')) return 'level-critica';
    if (v.includes('muito baixa')) return 'level-muito-baixa';
    if (v.includes('alta')) return 'level-alta';
    if (v.includes('moderad')) return 'level-moderada';
    if (v.includes('baixa')) return 'level-baixa';
    return '';
  }

  function renderEvidenceQualityDisplays(m) {
    const eq = engine.getEvidenceQuality();
    const amstar = eq.amstar2;
    const grade = eq.grade;
    const meta = m?.meta_analise;

    // 1. Metanálise de Suporte + AMSTAR 2
    if (evidenceMetaBlock) {
      if (meta) {
        evidenceMetaBlock.style.display = 'block';
        if (evidenceMetaCitationText) {
          const per = meta.periodico || meta.revista || '';
          const perFmt = per ? ` (${per})` : '';
          evidenceMetaCitationText.innerHTML = `<strong>${meta.autores || 'Revisão Sistemática'} (${meta.ano || ''})</strong> — <em>"${meta.titulo || 'Revisão Sistemática e Metanálise de Suporte'}"</em>${perFmt}`;
        }
        if (evidenceMetaDoiLink) {
          const urlMeta = meta.url_doi || (meta.doi ? (meta.doi.startsWith('http') ? meta.doi : `https://doi.org/${meta.doi}`) : '#');
          evidenceMetaDoiLink.href = urlMeta;
        }
        if (evidenceMetaDoiText) {
          evidenceMetaDoiText.textContent = meta.doi ? `DOI: ${meta.doi.replace('https://doi.org/', '')}` : 'Acessar Metanálise';
        }
        if (evidenceAmstarBadge) {
          const level = amstar?.nivel || 'Avaliação Pendente GT';
          evidenceAmstarBadge.textContent = `AMSTAR 2: ${level} · Em homologação GT`;
          evidenceAmstarBadge.className = `evidence-tag-amstar ${getQualityLevelClass(level)}`;
        }
        if (evidenceAmstarRationale) {
          evidenceAmstarRationale.textContent = amstar?.justificativa_preliminar || 'Instrumento AMSTAR 2 aplicado à qualidade metodológica da revisão sistemática de suporte.';
        }
      } else {
        evidenceMetaBlock.style.display = 'none';
      }
    }

    // 2. Certeza da Evidência por Desfecho (GRADE)
    const gradeCerteza = grade?.certeza || 'Moderada';
    const gradeSimbolos = grade?.simbolos || '⊕⊕⊕◯';
    const gradeForca = grade?.forca_recomendacao || 'Condicional';
    const gradeCls = getQualityLevelClass(gradeCerteza);

    if (evidenceGradeBadge) {
      evidenceGradeBadge.textContent = `GRADE (Desfecho): ${gradeCerteza} (${gradeSimbolos}) · Rec. ${gradeForca} · Em homologação GT`;
      evidenceGradeBadge.className = `evidence-tag-grade ${gradeCls}`;
    }
    if (evidenceGradeRationale) {
      evidenceGradeRationale.textContent = grade?.observacao_dominios || 'Avaliação preliminar da certeza da evidência por desfecho (risco de viés, inconsistência, evidência indireta e imprecisão).';
    }

    // 3. Espelho compacto no Desfecho, na Coluna 2 da Calculadora e no cabeçalho recolhível de Evidências
    const amstarLevel = amstar?.nivel || 'Pendente GT';
    const amstarCls = getQualityLevelClass(amstarLevel);

    if (prescDesfechoGradeBadge) {
      prescDesfechoGradeBadge.textContent = `GRADE (Desfecho): ${gradeCerteza} (${gradeSimbolos}) · Rec. ${gradeForca}`;
      prescDesfechoGradeBadge.className = `evidence-tag-grade ${gradeCls}`;
    }
    if (calcGradeBadge) {
      calcGradeBadge.textContent = `GRADE (Desfecho): ${gradeCerteza} (${gradeSimbolos}) · Rec. ${gradeForca}`;
      calcGradeBadge.className = `evidence-tag-grade ${gradeCls}`;
    }
    if (calcAmstarBadge) {
      calcAmstarBadge.textContent = `AMSTAR 2 (Metanálise): ${amstarLevel}`;
      calcAmstarBadge.className = `evidence-tag-amstar ${amstarCls}`;
    }
    if (evidenceSummaryGradeBadge) {
      evidenceSummaryGradeBadge.textContent = `GRADE (Desfecho): ${gradeCerteza} (${gradeSimbolos})`;
      evidenceSummaryGradeBadge.className = `evidence-tag-grade ${gradeCls}`;
    }
    if (evidenceSummaryAmstarBadge) {
      evidenceSummaryAmstarBadge.textContent = `AMSTAR 2: ${amstarLevel}`;
      evidenceSummaryAmstarBadge.className = `evidence-tag-amstar ${amstarCls}`;
    }
  }

  function renderTolerabilityUI() {
    if (!tolerabilityOptionsGrid) return;
    const tol = engine.tolerabilityStatus || 'boa';
    tolerabilityOptionsGrid.querySelectorAll('.btn-tolerability').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-tol') === tol);
    });

    if (!tolerabilityContextNote) return;
    const guidance = engine.getTolerabilityGuidance();
    const tolObs = engine.getContextualObservations({ slot: 'tol' });
    const tolObsHtml = buildObservationsHtml(tolObs, { compact: true });

    let baseGuidanceHtml = '';
    let noteClass = 'tolerability-context-note';

    if (tol === 'leve') {
      baseGuidanceHtml = `
        <div><strong>Orientação de Manejo (Desconforto Leve):</strong> ${escHtml(guidance.orientacaoGeral)}</div>
        <div style="color: var(--text-muted); margin-top: 2px;">${escHtml(guidance.fatoresModuladores)}</div>
      `;
    } else if (tol === 'intolerante') {
      noteClass = 'tolerability-context-note tol-warning';
      baseGuidanceHtml = `
        <div><strong>Conduta de Tolerabilidade (Intolerância Moderada):</strong> ${escHtml(guidance.ajusteDoseSugerido)}</div>
        <div><a href="${escHtml(guidance.adverseBankUrl)}" target="_blank" rel="noopener noreferrer" class="adverse-bank-link">Registrar evento no Banco de Efeitos Adversos NAPeN ↗</a></div>
      `;
    } else if (tol === 'grave') {
      noteClass = 'tolerability-context-note tol-danger';
      baseGuidanceHtml = `
        <div><strong>Alerta de Segurança:</strong> Suspender imediatamente a sessão/protocolo e proceder à avaliação médica. <strong>Registro obrigatório:</strong>
        <a href="${escHtml(guidance.adverseBankUrl)}" target="_blank" rel="noopener noreferrer" class="adverse-bank-link">Acessar Banco de Efeitos Adversos da Rede NAPeN ↗</a></div>
      `;
    }

    if (!baseGuidanceHtml && !tolObsHtml) {
      tolerabilityContextNote.style.display = 'none';
      tolerabilityContextNote.innerHTML = '';
      tolerabilityContextNote.className = 'tolerability-context-note';
      return;
    }

    if (tol === 'boa' && tolObs.some(o => String(o.severidade).toLowerCase() === 'danger')) {
      noteClass = 'tolerability-context-note tol-danger';
    } else if (tol === 'boa' && tolObs.some(o => String(o.severidade).toLowerCase() === 'warning')) {
      noteClass = 'tolerability-context-note tol-warning';
    }

    tolerabilityContextNote.style.display = 'block';
    tolerabilityContextNote.className = noteClass;
    tolerabilityContextNote.innerHTML = `${baseGuidanceHtml}${tolObsHtml ? `<div style="${baseGuidanceHtml ? 'margin-top: 8px;' : ''}">${tolObsHtml}</div>` : ''}`;
    bindObsRedirectButtons(tolerabilityContextNote);
  }

  if (tolerabilityOptionsGrid) {
    tolerabilityOptionsGrid.querySelectorAll('.btn-tolerability').forEach(btn => {
      btn.addEventListener('click', () => {
        const tol = btn.getAttribute('data-tol') || 'boa';
        engine.setTolerabilityStatus(tol);
        renderTolerabilityUI();
        handleScoreComputation();
      });
    });
  }

  // ==========================================================================
  // 5. Atualiza Prescrição Primária, Diretrizes e Monitoramento do Ciclo
  // ==========================================================================
  function updatePrescriptionDisplay() {
    const m = engine.getActiveModality();
    if (!m) return;

    const cond = engine.getCondition(engine.activeConditionId);
    const dottedHtml = formatDottedIndicator(m.linha_fluxograma);

    if (prescTecnica) prescTecnica.textContent = m.tecnica || '—';
    if (prescModalidade) {
      prescModalidade.innerHTML = `Modalidade: ${escHtml(m.modalidade_sigla || 'NIBS')}${dottedHtml ? `<div style="margin-top: 4px;">${dottedHtml}</div>` : ''}`;
    }
    if (prescAlvo) prescAlvo.textContent = m.alvo || '—';
    if (prescFrequencia) prescFrequencia.textContent = m.frequencia || '—';
    if (prescIntensidade) prescIntensidade.textContent = `Intensidade: ${m.intensidade || 'Conforme limiar motor/sensorial'}`;
    if (prescPulsos) prescPulsos.textContent = m.pulsos_duracao || '—';
    if (prescSessoes) prescSessoes.textContent = `Dose e Sessões: ${m.sessoes || '—'}`;

    // Observações cirúrgicas nos slots dos parâmetros (otimização de carga/intensidade consolidada no Guia de Tolerabilidade & Dose)
    renderObservationsSlot(prescObsTecnica, engine.getContextualObservations({ slot: 'tec', stage: state.therapeuticStage }), { compact: true });
    renderObservationsSlot(prescObsAlvo, engine.getContextualObservations({ slot: 'alvo', stage: state.therapeuticStage }), { compact: true });
    renderObservationsSlot(prescObsIntensidade, [], { compact: true });
    renderObservationsSlot(prescObsSessoes, engine.getContextualObservations({ slot: 'sessoes', stage: state.therapeuticStage }), { compact: true });

    // Dissociação Conceitual NAPeN: Desfecho Clínico Alvo vs. Instrumento de Avaliação
    const tree = engine.getActiveTree();
    const rootOpts = tree?.etapas?.[0]?.opcoes || [];
    const activeRootChoice = tree?.etapas?.[0] ? engine.getPathChoice(tree.etapas[0].etapa_id) : null;
    const chosenRootOpt = rootOpts.find(o => o.id === activeRootChoice);
    const activeFactor = cond?.fatores_limitantes?.find(f => f.id === (engine.primaryFactorId || engine.activeFactorId))
      || (cond?.fatores_limitantes ? cond.fatores_limitantes[0] : null);
    if (prescDesfechoNome) {
      prescDesfechoNome.textContent = chosenRootOpt?.rotulo || activeFactor?.nome || activeFactor?.label || m.titulo_curto || cond?.condicao || '—';
    }
    const activeScale = engine.getActiveScale() || (m.escalas_detalhadas && m.escalas_detalhadas.length > 0 ? m.escalas_detalhadas[0] : null);
    if (prescEscala) prescEscala.textContent = activeScale?.nome || m.escala_recomendada || '—';
    if (prescEfeito) prescEfeito.textContent = activeScale?.tamanho_efeito || m.tamanho_efeito || 'Eficácia demonstrada em ensaios controlados randomizados.';
    if (prescMeta) prescMeta.textContent = activeScale?.meta_texto || m.meta_melhora || 'Melhora clinicamente relevante conforme protocolo.';
    renderObservationsSlot(prescObsEscala, engine.getContextualObservations({ slot: 'scale', stage: state.therapeuticStage }), { compact: true });

    // Nível de Evidência em Diretriz Oficial (Guideline) ou Síntese Clínica — sem misturar GRADE
    const gInfo = engine.getFormattedGuideline();
    const fonteCurta = gInfo.isIfcnLefaucheur
      ? `${gInfo.autores || 'Lefaucheur et al.'} (${gInfo.ano || '2020'})`
      : (gInfo.autores ? `Síntese: ${gInfo.autores} (${gInfo.ano || 'Ref.'})` : 'Síntese / Consenso clínico');
    if (guidelineBadgeText) {
      if (gInfo && gInfo.url) {
        guidelineBadgeText.innerHTML = `
          <span><strong>${escHtml(gInfo.recomendacao)}</strong> — ${escHtml(fonteCurta)}</span>
          <a href="${escHtml(gInfo.url)}" target="_blank" rel="noopener noreferrer" style="color: var(--napen-teal-dark); text-decoration: underline; margin-left: 6px; font-weight: 600;" title="${gInfo.isIfcnLefaucheur ? 'Acessar diretriz oficial IFCN via DOI' : 'Acessar revisão / síntese de suporte via DOI'}">
            ${gInfo.doi ? `DOI: ${escHtml(gInfo.doi)} ↗` : 'Acessar Referência ↗'}
          </a>
        `;
      } else {
        guidelineBadgeText.textContent = gInfo?.text || 'Recomendação Consensual NAPeN';
      }
    }

    // Painel de Evidências: Ensaio clínico de referência do protocolo, Metanálise (AMSTAR 2), Nível em Guideline, GRADE (Desfecho) e Guia PEM
    if (m.artigo_referencia) {
      if (evidenceCitationText) {
        const periodicalText = m.artigo_referencia.periodico || m.artigo_referencia.revista || '';
        const periodicalFormatted = periodicalText ? ` (${escHtml(periodicalText)})` : '';
        evidenceCitationText.innerHTML = `<strong>${escHtml(m.artigo_referencia.citacao_completa || m.artigo_referencia.autores)}</strong> — <em>"${escHtml(m.artigo_referencia.titulo || '')}"</em>${periodicalFormatted}`;
      }
      if (evidenceDoiLink) {
        const fullDoiUrl = m.artigo_referencia.url_doi || (m.artigo_referencia.doi ? (m.artigo_referencia.doi.startsWith('http') ? m.artigo_referencia.doi : `https://doi.org/${m.artigo_referencia.doi}`) : '#');
        evidenceDoiLink.href = fullDoiUrl;
      }
      if (evidenceDoiText) {
        evidenceDoiText.textContent = m.artigo_referencia.doi ? `DOI: ${m.artigo_referencia.doi.replace('https://doi.org/', '')}` : 'Acessar Artigo Oficial';
      }
    }

    const guidelineSourceLabel = document.getElementById('evidenceGuidelineSourceLabel');
    if (guidelineSourceLabel) {
      guidelineSourceLabel.textContent = gInfo.isIfcnLefaucheur
        ? 'Guideline (IFCN):'
        : 'Revisão / Síntese de Suporte:';
    }
    if (evidenceGuidelineText) {
      evidenceGuidelineText.innerHTML = gInfo.isIfcnLefaucheur
        ? `<strong>${escHtml(gInfo.recomendacao)}</strong> — Nível de evidência segundo a Diretriz Internacional IFCN (${escHtml(gInfo.autores || 'Lefaucheur et al.')}, ${escHtml(gInfo.ano || '2020')}).`
        : `<strong>${escHtml(gInfo.recomendacao)}</strong> — Nível de evidência clínica segundo revisão sistemática / síntese de suporte (${gInfo.autores ? `${escHtml(gInfo.autores)}, ${escHtml(gInfo.ano || '')}` : 'estudos clínicos selecionados'}), sem gradação direta em Guideline IFCN.`;
    }
    if (evidenceGuidelineDoiLink) {
      const fullGuideUrl = gInfo.url || (gInfo.doi ? (gInfo.doi.startsWith('http') ? gInfo.doi : `https://doi.org/${gInfo.doi}`) : '#');
      evidenceGuidelineDoiLink.href = fullGuideUrl;
    }
    if (evidenceGuidelineDoiText) {
      evidenceGuidelineDoiText.textContent = gInfo.doi
        ? `DOI: ${gInfo.doi.replace('https://doi.org/', '')}`
        : (gInfo.isIfcnLefaucheur ? 'Acessar Diretriz IFCN' : 'Acessar Revisão de Suporte');
    }

    if (evidencePemGuide) {
      const showPemGuide = Boolean(
        cond
        && (cond.id === 'avc-membro-superior' || cond.id === 'avc-mobilidade')
        && (engine.activeModalityType === 'rtms' || m.mod_tipo === 'rtms')
      );
      evidencePemGuide.style.display = showPemGuide ? 'block' : 'none';
    }

    renderEvidenceQualityDisplays(m);

    // Monitoramento Clínico e Regras de Reavaliação (3 cartões não sobrepostos)
    const sa = m.sessoes_ajuste || {};
    if (monitoringReeval) {
      monitoringReeval.textContent = sa.quando_reavaliar || 'Avaliar evolução clínica após 5 a 10 sessões de indução; ausência de melhora indica resposta insatisfatória.';
    }
    if (monitoringCriterion) {
      monitoringCriterion.textContent = sa.regra_interrupcao || 'Ao atingir platô funcional sustentado, interromper o ciclo intensivo e iniciar redução gradual da frequência das sessões.';
    }
    if (monitoringStopRule) {
      monitoringStopRule.textContent = m.falha_terapeutica?.criterio || 'Caracteriza-se falha terapêutica ao concluir toda a sequência prevista (incluindo a Seção de Ajustes) sem alcançar a MCID na escala clínica.';
    }
    if (monitoringNotesText) {
      monitoringNotesText.innerHTML = formatObservationTextHtml(
        m.notas_clinicas || 'A estimulação deve ser associada a intervenção motora ou comportamental imediata com metas funcionais bem delineadas.'
      );
    }

    // Guia Estratégico de Tolerabilidade & Dose (Painel Plano Integrado)
    renderTolerabilityDoseGuide(m, sa);

    if (stepNode3) stepNode3.classList.add('completed');

    // Atualiza nota contextual de tolerabilidade (SLOT-TOL) do protocolo ativo
    renderTolerabilityUI();

    // Atualiza foco de continuidade caso esteja ativo
    if (engine.entryMode === 'returning' && cond) {
      renderContinuingFocusSlot(cond);
    }

    // Inicializa a calculadora com a escala ativa correspondente
    renderCalculatorForActiveScale();
  }

  function renderTolerabilityDoseGuide(m, sa) {
    if (!tolerabilityDoseGuidePanel) return;
    const tolGuide = engine.getTolerabilityGuidance();
    if (tolGuideTitle) {
      tolGuideTitle.textContent = tolGuide.tituloGuia || 'Guia Estratégico de Tolerabilidade & Dose';
    }
    if (tolGuideBankLink && tolGuide.adverseBankUrl) {
      tolGuideBankLink.href = tolGuide.adverseBankUrl;
    }

    if (tolGuideTolerance) {
      const tolTexts = [];
      [tolGuide.orientacaoGeral, tolGuide.ajusteDoseSugerido].forEach(txt => {
        if (!txt) return;
        const norm = String(txt).trim();
        if (norm && !tolTexts.some(prev => prev.includes(norm) || norm.includes(prev))) {
          tolTexts.push(norm);
        }
      });
      tolGuideTolerance.innerHTML = tolTexts
        .map((t, idx) => `<p${idx > 0 ? ' class="tol-guide-col-note"' : ''}>${formatObservationTextHtml(t)}</p>`)
        .join('');
    }

    if (tolGuideDose) {
      const doseMain = (tolGuide.dosePulsos || '').trim();
      tolGuideDose.innerHTML = doseMain ? `<p>${formatObservationTextHtml(doseMain)}</p>` : '';
    }

    if (tolGuideCalibration) {
      const calibMain = (tolGuide.calibracaoLimiar || '').trim();
      const modFactors = (tolGuide.fatoresModuladores || '').trim();
      tolGuideCalibration.innerHTML = `
        ${calibMain ? `<p>${escHtml(calibMain)}</p>` : ''}
        ${modFactors ? `<div class="tol-guide-col-note"><strong>Fatores Moduladores:</strong> ${escHtml(modFactors)}</div>` : ''}
      `;
    }
  }

  function scrollToTolerabilityGuide() {
    if (!tolerabilityDoseGuidePanel) return;
    const headerEl = document.querySelector('.site-header');
    const headerHeight = headerEl ? headerEl.offsetHeight : 140;
    const rect = tolerabilityDoseGuidePanel.getBoundingClientRect();
    const targetScrollY = window.pageYOffset + rect.top - headerHeight - 16;
    window.scrollTo({ top: Math.max(0, targetScrollY), behavior: 'smooth' });
    tolerabilityDoseGuidePanel.classList.add('tol-guide-highlight-pulse');
    setTimeout(() => {
      tolerabilityDoseGuidePanel.classList.remove('tol-guide-highlight-pulse');
    }, 2500);
  }

  // ==========================================================================
  // 6. Assistente de Resposta Clínica (Integrado à Tolerabilidade & Esteira Completa)
  // ==========================================================================
  function updateOutcomeDisplay() {
    const outcome = engine.activeOutcome;
    const m = engine.getActiveModality();
    const guidance = engine.getTolerabilityGuidance();
    const tol = engine.tolerabilityStatus || 'boa';

    if (btnOutcomeSuccess) btnOutcomeSuccess.classList.toggle('active', outcome === 'success');
    if (btnOutcomeDanger) btnOutcomeDanger.classList.toggle('active', outcome === 'danger');

    if (!outcome) {
      if (assistantSequenceTrail) {
        assistantSequenceTrail.style.display = 'none';
        assistantSequenceTrail.innerHTML = '';
      }
      branchResultPanel.className = 'branch-result-panel';
      branchResultPanel.innerHTML = '';
      if (stepNode4) stepNode4.classList.remove('completed', 'current');
      return;
    }

    if (stepNode4) stepNode4.classList.add('current');

    // Estado 1: Resposta Clínica Satisfatória
    if (outcome === 'success') {
      if (assistantSequenceTrail) {
        assistantSequenceTrail.style.display = 'none';
        assistantSequenceTrail.innerHTML = '';
      }
      branchResultPanel.className = 'branch-result-panel success visible';
      const tolNoteHtml = tol === 'leve'
        ? `<div style="margin-top: 8px; padding-top: 8px; border-top: 1px dashed rgba(6,95,70,0.25);"><strong>Manejo de Desconforto Leve:</strong> ${escHtml(guidance.orientacaoGeral)}</div>`
        : '';
      const stageObsHtml = buildObservationsHtml(engine.getContextualObservations({ slot: 'stage', stage: 'primary' }), { compact: true });
      branchResultPanel.innerHTML = `
        <div style="font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
          <span class="outcome-bullet status-success"></span>
          [Resposta Clínica Satisfatória Alcançada]
        </div>
        <div style="color: var(--status-success-text); line-height: 1.55;">
          Paciente atingiu ou superou a meta terapêutica estabelecida no protocolo (${escHtml(m?.escala_recomendada || 'escala clínica')}) com tolerabilidade adequada.
          <br><strong>Conduta Clínica NAPeN:</strong> Manter o protocolo primário até consolidação do ganho clínico e iniciar transição para manutenção periódica (redução gradual da frequência para 1 sessão por semana ou quinzenal, mantendo terapia multiprofissional concomitante e reavaliações periódicas).
          ${tolNoteHtml}
        </div>
        ${stageObsHtml}
      `;
      bindObsRedirectButtons(branchResultPanel);
      return;
    }

    // Estado Especial de Segurança: Evento Adverso Grave
    if (tol === 'grave' && outcome === 'danger') {
      if (assistantSequenceTrail) {
        assistantSequenceTrail.style.display = 'none';
        assistantSequenceTrail.innerHTML = '';
      }
      branchResultPanel.className = 'branch-result-panel danger visible';
      branchResultPanel.innerHTML = `
        <div class="failure-therapeutic-card" style="margin-top: 0;">
          <div class="failure-head">
            <span class="failure-badge">Segurança do Paciente</span>
            <span class="failure-title">Suspensão Imediata por Evento Adverso Grave / Contraindicação</span>
          </div>
          <div class="failure-description">
            Ocorrência de evento adverso grave ou contraindicação superveniente exige interrupção imediata da estimulação vigente, sobrepondo-se a qualquer pontuação numérica da escala.
          </div>
          <div class="failure-conduct-box">
            <div class="failure-conduct-title">Protocolo de Conduta Segura NAPeN:</div>
            <div style="line-height: 1.55;">
              1. Suspender imediatamente a sessão e o ciclo terapêutico atual;<br>
              2. Realizar avaliação médica/neurológica presencial para estabilização clínica;<br>
              3. Revisar medicações, histórico convulsivo, implantes e adesão ao checklist pré-sessão;<br>
              4. <a href="${escHtml(guidance.adverseBankUrl)}" target="_blank" rel="noopener noreferrer" class="adverse-bank-link">Registrar formalmente a ocorrência no Banco de Efeitos Adversos da Rede NAPeN ↗</a>
            </div>
          </div>
        </div>
      `;
      return;
    }

    // Estado 2: Progressão Sequencial Pós-Resposta Insatisfatória (Protocolos -> Seção de Ajustes -> Falha Terapêutica)
    branchResultPanel.className = 'branch-result-panel danger visible';

    const altStages = getDynamicAltStagesForActiveModality();
    const curStage = state.therapeuticStage || 'primary';
    const stageObsHtml = buildObservationsHtml(engine.getContextualObservations({ slot: 'stage', stage: curStage }), { compact: true });

    if (assistantSequenceTrail) {
      const chips = [];
      const activeIdxInAlt = curStage === 'failure'
        ? altStages.length
        : altStages.findIndex(s => s.stageKey === curStage);

      if (altStages.length > 0) {
        altStages.forEach((step, idx) => {
          const isCompleted = activeIdxInAlt > idx;
          const isCurrent = activeIdxInAlt === idx;
          const isAj = step.faseEtapa === 'ajustes';
          const isDot = step.linhaFluxograma === 'pontilhada';
          const prefix = isAj ? 'Seção de Ajustes' : (isDot ? 'Linha Pontilhada' : 'Na Sequência');
          const cls = [
            'seq-trail-chip',
            isCompleted ? 'completed' : '',
            isCurrent ? 'active' : '',
            isAj ? 'ajustes' : '',
            isDot ? 'dotted' : ''
          ].filter(Boolean).join(' ');
          chips.push(`<button type="button" class="${cls}" data-trail-stage="${escHtml(step.stageKey)}" title="${escHtml(step.nome)}">${escHtml(prefix)}: ${escHtml(step.nome)}</button>`);
          chips.push('<span class="seq-trail-arrow" aria-hidden="true">➔</span>');
        });
      }
      chips.push(`<button type="button" class="seq-trail-chip failure ${curStage === 'failure' ? 'active' : ''}" data-trail-stage="failure">Falha Terapêutica</button>`);
      assistantSequenceTrail.style.display = 'flex';
      assistantSequenceTrail.innerHTML = chips.join('');
    }

    let stageHtml = '';

    if (curStage === 'primary') {
      const firstAlt = altStages[0];
      const nextStepIsAjustes = firstAlt?.faseEtapa === 'ajustes';
      stageHtml = `
        <div style="font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
          <span class="outcome-bullet status-danger"></span>
          [Resposta Insatisfatória no Protocolo Inicial]
        </div>
        <div style="line-height: 1.55; margin-bottom: 12px;">
          Paciente não atingiu o benefício terapêutico mínimo após a janela clínica esperada.
          Caso necessário revisar conforto ou calibração de dose do ciclo vigente antes da transição, consulte o <a href="#tolerabilityDoseGuidePanel" class="adverse-bank-link js-scroll-tol-guide">Guia de Tolerabilidade, Limiar &amp; Dose ↑</a>.
        </div>
        ${stageObsHtml}
        <div class="adjustment-actions-row">
          ${firstAlt
            ? `<button type="button" class="btn-step-action primary" id="btnGoAlt1" data-target-stage="${firstAlt.stageKey}">Resposta Insatisfatória ➔ ${nextStepIsAjustes ? 'Ir para Seção de Ajustes: ' : 'Avançar para '}${escHtml(firstAlt.nome)}</button>`
            : `<button type="button" class="btn-step-action danger" id="btnGoFailure" data-target-stage="failure">Sem Resposta no Protocolo Único ➔ Conduta de Encerramento</button>`}
        </div>
      `;
    } else if (curStage.startsWith('alt')) {
      const altData = engine.getPrescriptionForStage(curStage);
      const curIdx = altStages.findIndex(a => a.stageKey === curStage);
      const prevStage = curIdx > 0 ? altStages[curIdx - 1] : null;
      const nextAlt = (curIdx >= 0 && curIdx + 1 < altStages.length) ? altStages[curIdx + 1] : null;
      const dottedHtml = formatDottedIndicator(altData?.linhaFluxograma);
      const prevBtnId = prevStage ? (prevStage.stageKey === 'alt1' ? 'btnGoAlt1' : `btnGo${prevStage.stageKey}`) : 'btnBackPrimary';
      const nextBtnId = nextAlt ? (nextAlt.stageKey === 'alt2' ? 'btnGoAlt2' : `btnGo${nextAlt.stageKey}`) : 'btnGoFailure';
      const isCurAjustes = altData?.faseEtapa === 'ajustes' || altStages[curIdx]?.faseEtapa === 'ajustes';
      const isCurDotted = altData?.linhaFluxograma === 'pontilhada' || altStages[curIdx]?.linhaFluxograma === 'pontilhada';
      const badgeColor = isCurAjustes ? '#B45309' : 'var(--napen-teal-dark)';
      const boxCls = [
        'alternative-protocol-box',
        isCurAjustes ? 'is-ajustes' : '',
        isCurDotted ? 'is-dotted' : ''
      ].filter(Boolean).join(' ');
      const rationaleTitle = isCurAjustes && isCurDotted
        ? 'Seção de Ajustes · Borda Pontilhada'
        : (isCurAjustes ? 'Seção de Ajustes' : 'Borda Pontilhada');
      const rationaleText = altData?.motivoAjuste
        || 'Protocolos com borda pontilhada e opções da Seção de Ajustes indicam condutas cujo nível de evidência científica ainda não foi validado por metanálises (base científica exploratória respaldada em ensaios clínicos individuais).';
      const ajustesRationaleHtml = (isCurAjustes || isCurDotted)
        ? `<div class="ajustes-evidence-rationale"><strong>Motivo da classificação (${rationaleTitle}):</strong> ${escHtml(rationaleText)}</div>`
        : '';

      stageHtml = `
        <div class="${boxCls}" style="margin-top: 6px;">
          <div class="alt-title-line" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <span><strong>${escHtml(altData?.badge || altStages[curIdx]?.shortLabel || 'Próximo Protocolo na Sequência')}:</strong> ${escHtml(altData?.titulo || 'Protocolo Subsequente')}</span>
            <span class="failure-badge" style="background-color: ${badgeColor};">${escHtml(altStages[curIdx]?.shortLabel || 'Na Sequência')}</span>
          </div>
          ${dottedHtml ? `<div style="margin-top: 6px;">${dottedHtml}</div>` : ''}
          ${ajustesRationaleHtml}
          <div style="margin-top: 6px;"><strong>Técnica:</strong> ${escHtml(altData?.tecnica || '—')}</div>
          <div><strong>Alvo Anatômico:</strong> ${escHtml(altData?.alvo || '—')}</div>
          <div><strong>Parâmetros:</strong> ${escHtml(altData?.parametros || '—')}</div>
          ${altData?.efeitoEsperado ? `<div><strong>Efeito Esperado:</strong> ${escHtml(altData.efeitoEsperado)}</div>` : ''}
          ${altData?.referencia ? `<div><strong>Referência:</strong> ${escHtml(altData.referencia)}</div>` : ''}
          <div class="alt-clinical-notes" style="margin-top: 8px;">
            <strong>Observações Clínicas:</strong> ${formatObservationTextHtml(altData?.observacoes || 'Transição sequencial indicada conforme a árvore de decisão clínica.')}
          </div>
          ${stageObsHtml}
          <div class="adjustment-actions-row" style="margin-top: 14px;">
            <button type="button" class="btn-step-action secondary" id="${prevBtnId}" data-target-stage="${prevStage ? prevStage.stageKey : 'primary'}">
              ${prevStage ? `← ${escHtml(prevStage.nome)}` : '← Rever Protocolo Inicial'}
            </button>
            ${nextAlt
              ? `<button type="button" class="btn-step-action primary" id="${nextBtnId}" data-target-stage="${nextAlt.stageKey}">Sem Resposta neste Protocolo ➔ ${nextAlt.faseEtapa === 'ajustes' ? 'Seção de Ajustes: ' : 'Avançar para '}${escHtml(nextAlt.nome)}</button>`
              : `<button type="button" class="btn-step-action danger" id="${nextBtnId}" data-target-stage="failure">Sem Resposta após Sequência e Ajustes ➔ Indicar Falha Terapêutica</button>`}
          </div>
        </div>
      `;
    } else if (curStage === 'failure') {
      const failData = engine.getPrescriptionForStage('failure');
      const conductList = (failData?.condutas || []).map(c => `<li>${escHtml(c)}</li>`).join('');
      const lastAlt = altStages.length > 0 ? altStages[altStages.length - 1] : null;
      stageHtml = `
        <div class="failure-therapeutic-card">
          <div class="failure-head">
            <span class="failure-badge">Falha Terapêutica</span>
            <span class="failure-title">${escHtml(failData?.titulo || 'Falha Terapêutica / Encerramento da Sequência NAPeN')}</span>
          </div>
          <div class="failure-description">
            ${escHtml(failData?.criterio || 'Paciente concluiu o ciclo inicial, os protocolos subsequentes e a seção de ajustes sem apresentar resposta clínica mínima relevante.')}
          </div>
          <div class="failure-conduct-box">
            <div class="failure-conduct-title">Conduta Clínica Sistematizada da Rede NAPeN:</div>
            <ul style="margin: 4px 0 0 18px; line-height: 1.55;">${conductList}</ul>
          </div>
          ${stageObsHtml}
          <div class="adjustment-actions-row" style="margin-top: 14px;">
            ${lastAlt ? `<button type="button" class="btn-step-action secondary" data-target-stage="${lastAlt.stageKey}">← Retornar a ${escHtml(lastAlt.nome)}</button>` : ''}
            <button type="button" class="btn-step-action secondary" id="btnBackPrimary" data-target-stage="primary">
              ← Retornar ao Protocolo Inicial
            </button>
          </div>
        </div>
      `;
    }

    branchResultPanel.innerHTML = stageHtml;
    bindObsRedirectButtons(branchResultPanel);

    branchResultPanel.querySelectorAll('.js-scroll-tol-guide').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        scrollToTolerabilityGuide();
      });
    });

    function switchTherapeuticStage(stage) {
      state.therapeuticStage = stage;
      engine.setOutcome('danger');
      if (engine.entryMode === 'returning') {
        engine.setContinuingStage(stage);
      }
      updateOutcomeDisplay();
    }

    branchResultPanel.querySelectorAll('[data-target-stage]').forEach(btn => {
      btn.addEventListener('click', () => {
        const nextStage = btn.getAttribute('data-target-stage');
        if (nextStage) switchTherapeuticStage(nextStage);
      });
    });

    if (assistantSequenceTrail) {
      assistantSequenceTrail.querySelectorAll('[data-trail-stage]').forEach(chip => {
        chip.addEventListener('click', () => {
          const nextStage = chip.getAttribute('data-trail-stage');
          if (nextStage) switchTherapeuticStage(nextStage);
        });
      });
    }
  }

  // Interação manual com os botões de desfecho
  if (btnOutcomeSuccess) {
    btnOutcomeSuccess.addEventListener('click', () => {
      state.therapeuticStage = 'primary';
      if (assistantSequenceTrail) {
        assistantSequenceTrail.style.display = 'none';
        assistantSequenceTrail.innerHTML = '';
      }
      engine.toggleOutcome('success');
      updateOutcomeDisplay();
    });
  }

  if (btnOutcomeDanger) {
    btnOutcomeDanger.addEventListener('click', () => {
      if (engine.activeOutcome === 'danger') {
        state.therapeuticStage = 'primary';
        engine.setOutcome(null);
        if (assistantSequenceTrail) {
          assistantSequenceTrail.style.display = 'none';
          assistantSequenceTrail.innerHTML = '';
        }
      } else if (engine.tolerabilityStatus === 'grave') {
        state.therapeuticStage = 'primary';
        engine.setOutcome('danger');
      } else {
        const altStages = getDynamicAltStagesForActiveModality();
        state.therapeuticStage = altStages[0]?.stageKey || 'failure';
        engine.setOutcome('danger');
      }
      updateOutcomeDisplay();
    });
  }

  // ==========================================================================
  // 7. Calculadora Dual Multidimensional (Escore + Tolerabilidade) & Automatismo
  // ==========================================================================
  function handleScoreComputation() {
    const m = engine.getActiveModality();
    const activeScale = engine.getActiveScale();

    let valBaseRaw, valPostRaw;
    if (activeScale && activeScale.tipo === 'ordinal_eam') {
      valBaseRaw = eamState.base;
      valPostRaw = eamState.post;
    } else {
      valBaseRaw = calcValBase?.value;
      valPostRaw = calcValPost?.value;
    }

    const res = engine.calculateDelta(valBaseRaw, valPostRaw, activeScale, m);
    const evalMatrix = engine.evaluateClinicalResponse(res, engine.tolerabilityStatus);

    const bindCalcGuideLinks = () => {
      if (!calcGoalFeedback) return;
      calcGoalFeedback.querySelectorAll('.js-scroll-tol-guide').forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          scrollToTolerabilityGuide();
        });
      });
    };

    if (!res.isSuccess) {
      if (calcDeltaPoints) calcDeltaPoints.textContent = 'Δ = —';
      if (calcDeltaPercent) calcDeltaPercent.textContent = '— %';
      if (calcMcidBadge) {
        calcMcidBadge.textContent = evalMatrix.recommendationType === 'pending' ? 'Aguardando dados' : evalMatrix.badgeLabel;
        calcMcidBadge.className = 'calc-metric-val calc-mcid-status';
      }
      const noScoreCls = evalMatrix.recommendationType === 'adverse_halt' ? 'danger' : (evalMatrix.recommendationType === 'warning_tol' ? 'warning' : '');
      if (cardDeltaPoints) cardDeltaPoints.className = 'calc-metric-card';
      if (cardDeltaPercent) cardDeltaPercent.className = 'calc-metric-card';
      if (cardMcidBadge) cardMcidBadge.className = `calc-metric-card ${noScoreCls}`.trim();

      if (calcGoalFeedback) {
        if (evalMatrix.recommendationType === 'adverse_halt' || evalMatrix.recommendationType === 'warning_tol') {
          const tolGuideAnchor = evalMatrix.recommendationType === 'warning_tol'
            ? ' <a href="#tolerabilityDoseGuidePanel" class="adverse-bank-link js-scroll-tol-guide">Ver Ajustes de Tolerabilidade &amp; Dose ↑</a>'
            : '';
          const bankHtml = evalMatrix.needsAdverseReport
            ? ` <a href="${evalMatrix.adverseBankUrl}" target="_blank" rel="noopener noreferrer" class="adverse-bank-link">Registrar no Banco de Efeitos Adversos NAPeN ↗</a>`
            : '';
          calcGoalFeedback.innerHTML = `${evalMatrix.summaryHtml}${tolGuideAnchor}${bankHtml}`;
          bindCalcGuideLinks();
        } else {
          calcGoalFeedback.textContent = `Meta do protocolo: ${activeScale?.meta_texto || m?.meta_melhora || 'Insira os escores e selecione a tolerabilidade para verificar o desfecho.'}`;
        }
      }
      if (calcComparisonFeedback) {
        calcComparisonFeedback.innerHTML = evalMatrix.recommendationType === 'pending'
          ? 'Ao informar os escores e a tolerabilidade, o sistema analisará a compatibilidade clínica com a MCID, com o ensaio clínico de referência do protocolo e com a segurança terapêutica.'
          : evalMatrix.summaryHtml;
      }

      if (evalMatrix.recommendationType === 'adverse_halt') {
        state.therapeuticStage = 'primary';
        engine.setOutcome('danger');
        updateOutcomeDisplay();
      } else if (evalMatrix.recommendationType === 'warning_tol') {
        state.therapeuticStage = 'primary';
        engine.setOutcome(null);
        updateOutcomeDisplay();
      }
      return;
    }

    // Atualização dos 3 Cards de Métricas Individuais
    if (calcDeltaPoints) calcDeltaPoints.textContent = res.deltaPointsFormatted || `Δ = ${res.delta}`;
    if (calcDeltaPercent) calcDeltaPercent.textContent = res.percentFormatted || `${res.percent}%`;

    if (calcMcidBadge) {
      if (evalMatrix.recommendationType === 'adverse_halt') {
        calcMcidBadge.textContent = 'Suspensão (EA Grave)';
      } else if (res.mcidMet) {
        calcMcidBadge.textContent = evalMatrix.recommendationType === 'warning_tol' ? 'MCID (Ver Tolerabilidade)' : 'MCID Atingida';
      } else if (res.isImproved) {
        calcMcidBadge.textContent = 'Parcial (< MCID)';
      } else {
        calcMcidBadge.textContent = 'Não Atingida';
      }
    }

    let statusClass = 'danger';
    if (evalMatrix.recommendationType === 'success') statusClass = 'success';
    else if (evalMatrix.recommendationType === 'warning_tol') statusClass = 'warning';

    if (cardDeltaPoints) cardDeltaPoints.className = `calc-metric-card ${statusClass}`;
    if (cardDeltaPercent) cardDeltaPercent.className = `calc-metric-card ${statusClass}`;
    if (cardMcidBadge) cardMcidBadge.className = `calc-metric-card ${statusClass}`;

    // Automatismo multidimensional: resposta satisfatória consolida; resposta insatisfatória avança diretamente ao próximo protocolo
    if (evalMatrix.recommendationType === 'success') {
      state.therapeuticStage = 'primary';
      engine.setOutcome('success');
    } else if (evalMatrix.recommendationType === 'warning_tol') {
      state.therapeuticStage = 'primary';
      engine.setOutcome(null);
    } else if (evalMatrix.recommendationType === 'adverse_halt') {
      state.therapeuticStage = 'primary';
      engine.setOutcome('danger');
    } else {
      const altStages = getDynamicAltStagesForActiveModality();
      state.therapeuticStage = evalMatrix.recommendedStage || altStages[0]?.stageKey || 'failure';
      engine.setOutcome('danger');
    }
    updateOutcomeDisplay();

    // Feedback Clínico Integrado (Escore + Tolerabilidade)
    if (calcGoalFeedback) {
      const tolGuideAnchor = evalMatrix.recommendationType === 'warning_tol'
        ? ' <a href="#tolerabilityDoseGuidePanel" class="adverse-bank-link js-scroll-tol-guide">Ver Ajustes de Tolerabilidade &amp; Dose ↑</a>'
        : '';
      const bankLink = evalMatrix.needsAdverseReport
        ? ` <a href="${evalMatrix.adverseBankUrl}" target="_blank" rel="noopener noreferrer" class="adverse-bank-link">Registrar evento no Banco de Efeitos Adversos NAPeN ↗</a>`
        : '';
      calcGoalFeedback.innerHTML = `${evalMatrix.summaryHtml}${tolGuideAnchor}${bankLink}`;
      bindCalcGuideLinks();
    }

    // Diagnóstico Comparativo Dinâmico
    if (calcComparisonFeedback) {
      calcComparisonFeedback.innerHTML = res.comparativeFeedback;
    }
  }

  if (calcValBase && calcValPost) {
    calcValBase.addEventListener('input', handleScoreComputation);
    calcValPost.addEventListener('input', handleScoreComputation);
  }

  if (linkComoEfeitoCalculado) {
    linkComoEfeitoCalculado.addEventListener('click', (e) => {
      e.preventDefault();
      switchTab('method');
      const target = document.getElementById('metodologia-calculo-efeito');
      if (target) {
        setTimeout(() => {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 120);
      }
    });
  }

  // ==========================================================================
  // 8. Seletor de Idioma Oficial (Mimetização Rede NAPeN) & Notificações
  // ==========================================================================
  function showToast(message) {
    let toast = document.getElementById('napenToastNotification');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'napenToastNotification';
      toast.style.cssText = `
        position: fixed;
        bottom: 24px;
        right: 24px;
        background: var(--napen-navy);
        color: #FFFFFF;
        padding: 10px 18px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(0,0,0,0.25);
        z-index: 2000;
        opacity: 0;
        transform: translateY(10px);
        transition: all 0.25s ease;
        pointer-events: none;
      `;
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.style.opacity = '1';
    toast.style.transform = 'translateY(0)';
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
    }, 3200);
  }

  // ==========================================================================
  // Widget de Idioma Retrátil Oficial (Mimetização Estrita do Portal Rede NAPeN)
  // ==========================================================================
  const FLAG_BR_SVG = `<svg viewBox="0 0 32 32" width="20" height="20">
    <clipPath id="br-flag-c"><circle cx="16" cy="16" r="16"/></clipPath>
    <g clip-path="url(#br-flag-c)">
      <rect width="32" height="32" fill="#009b3a"/>
      <polygon points="16,5 29,16 16,27 3,16" fill="#fedf00"/>
      <circle cx="16" cy="16" r="6.8" fill="#002776"/>
      <path d="M 9.8,16.8 A 7,7 0 0,0 22.2,15.2" stroke="#ffffff" stroke-width="1.2" fill="none"/>
    </g>
  </svg>`;

  const FLAG_US_SVG = `<svg viewBox="0 0 32 32" width="20" height="20">
    <clipPath id="us-flag-t"><circle cx="16" cy="16" r="16"/></clipPath>
    <g clip-path="url(#us-flag-t)">
      <rect width="32" height="32" fill="#b22234"/>
      <rect y="2.46" width="32" height="2.46" fill="#ffffff"/>
      <rect y="7.38" width="32" height="2.46" fill="#ffffff"/>
      <rect y="12.30" width="32" height="2.46" fill="#ffffff"/>
      <rect y="17.23" width="32" height="2.46" fill="#ffffff"/>
      <rect y="22.15" width="32" height="2.46" fill="#ffffff"/>
      <rect y="27.07" width="32" height="2.46" fill="#ffffff"/>
      <rect width="14" height="17.23" fill="#3c3b6e"/>
      <circle cx="4" cy="4" r="0.9" fill="#ffffff"/><circle cx="10" cy="4" r="0.9" fill="#ffffff"/>
      <circle cx="7" cy="7.5" r="0.9" fill="#ffffff"/>
      <circle cx="4" cy="11" r="0.9" fill="#ffffff"/><circle cx="10" cy="11" r="0.9" fill="#ffffff"/>
      <circle cx="7" cy="14" r="0.9" fill="#ffffff"/>
    </g>
  </svg>`;

  let currentLang = 'pt';

  function updateLangSwitcherUI() {
    if (currentLang === 'pt') {
      if (capsuleFlag) capsuleFlag.innerHTML = FLAG_BR_SVG;
      if (capsuleLangText) capsuleLangText.textContent = 'PT';
      if (tierActiveFlag) tierActiveFlag.innerHTML = FLAG_BR_SVG;
      if (tierActiveText) tierActiveText.textContent = 'PT';
      if (tierOptionFlag) tierOptionFlag.innerHTML = FLAG_US_SVG;
      if (tierOptionText) tierOptionText.textContent = 'EN';
    } else {
      if (capsuleFlag) capsuleFlag.innerHTML = FLAG_US_SVG;
      if (capsuleLangText) capsuleLangText.textContent = 'EN';
      if (tierActiveFlag) tierActiveFlag.innerHTML = FLAG_US_SVG;
      if (tierActiveText) tierActiveText.textContent = 'EN';
      if (tierOptionFlag) tierOptionFlag.innerHTML = FLAG_BR_SVG;
      if (tierOptionText) tierOptionText.textContent = 'PT';
    }
  }

  function openLangDropdown() {
    if (langMenuExpanded) langMenuExpanded.classList.add('open');
    if (langCapsuleBtn) langCapsuleBtn.style.visibility = 'hidden';
  }

  function closeLangDropdown() {
    if (langMenuExpanded) langMenuExpanded.classList.remove('open');
    if (langCapsuleBtn) langCapsuleBtn.style.visibility = 'visible';
  }

  if (langCapsuleBtn) {
    langCapsuleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      openLangDropdown();
    });
  }

  if (langTierActive) {
    langTierActive.addEventListener('click', (e) => {
      e.stopPropagation();
      closeLangDropdown();
    });
  }

  if (langTierOption) {
    langTierOption.addEventListener('click', (e) => {
      e.stopPropagation();
      currentLang = currentLang === 'pt' ? 'en' : 'pt';
      updateLangSwitcherUI();
      closeLangDropdown();
      showToast(currentLang === 'en' ? 'English version currently under development.' : 'Idioma português selecionado.');
    });
  }

  document.addEventListener('click', (e) => {
    if (langDropdownWrapper && !langDropdownWrapper.contains(e.target)) {
      closeLangDropdown();
    }
  });

  // ==========================================================================
  // 9. Guia Clínico Operacional de Aplicação de Escalas (Slide-Over Drawer)
  // ==========================================================================
  function resolveScaleKey(rawScaleStr) {
    if (!rawScaleStr) return 'eam';
    const str = String(rawScaleStr).toLowerCase();
    if (str.includes('ashworth') || str.includes('eam')) return 'eam';
    if (str.includes('fma-le') || str.includes('membro inferior') && str.includes('fugl')) return 'fma_le';
    if (str.includes('fugl') || str.includes('fma')) return 'fma_ue';
    if (str.includes('mal-brazil') || str.includes('mal ') || str.includes('motor activity log')) return 'mal_brazil';
    if (str.includes('bergego')) return 'catherine_bergego';
    if (str.includes('berg') || str.includes('bbs')) return 'bbs';
    if (str.includes('icars')) return 'icars';
    if (str.includes('sara')) return 'sara';
    if (str.includes('madrs') || str.includes('montgomery')) return 'madrs';
    if (str.includes('hdrs-21') || str.includes('hdrs 21')) return 'hdrs_21';
    if (str.includes('hamd') || str.includes('ham-d') || str.includes('hdrs')) return 'ham_d';
    if (str.includes('gad-7') || str.includes('gad 7')) return 'gad_7';
    if (str.includes('dass-21') || str.includes('dass 21') || str.includes('dass')) return 'dass_21';
    if (str.includes('bai') || str.includes('beck anxiety')) return 'bai';
    if (str.includes('hama') || str.includes('ham-a')) return 'ham_a';
    if (str.includes('pcl')) return 'pcl_5';
    if (str.includes('caps')) return 'caps';
    if (str.includes('bpi') || str.includes('brief pain')) return 'bpi';
    if (str.includes('npsi')) return 'npsi';
    if (str.includes('eva') || str.includes('vas')) return 'eva';
    if (str.includes('dn4')) return 'dn4';
    if (str.includes('tug') || str.includes('timed up')) return 'tug';
    if (str.includes('nfog')) return 'nfog_q';
    if (str.includes('fog') || str.includes('freezing')) return 'fogq';
    if (str.includes('updrs') || str.includes('mds')) return 'updrs_iii';
    if (str.includes('moca') || str.includes('montreal')) return 'moca';
    if (str.includes('cornell') || str.includes('csdd')) return 'cornell';
    if (str.includes('meem') || str.includes('mmse') || str.includes('mental')) return 'meem';
    if (str.includes('adas')) return 'adas_cog';
    if (str.includes('trilhas') || str.includes('trail') || str.includes('tmt')) return 'teste_trilhas';
    if (str.includes('wais') || str.includes('dígitos') || str.includes('digitos')) return 'wais_digitos';
    if (str.includes('d2')) return 'd2_psico';
    if (str.includes('boston') || str.includes('bnt')) return 'bnt';
    if (str.includes('mtl')) return 'mtl_brasil';
    if (str.includes('token')) return 'token_test';
    if (str.includes('wab')) return 'wab_r';
    if (str.includes('doss')) return 'doss';
    if (str.includes('masa')) return 'masa';
    if (str.includes('ssa')) return 'ssa';
    if (str.includes('fois') || str.includes('fedss')) return 'fois';
    if (str.includes('pdms')) return 'pdms_fm';
    if (str.includes('quest')) return 'quest';
    if (str.includes('box') || str.includes('bbt')) return 'bbt';
    if (str.includes('pediatric balance') || str.includes('pbs')) return 'pbs';
    if (str.includes('gmfm')) return 'gmfm';
    if (str.includes('rbs')) return 'rbs_r';
    if (str.includes('atec')) return 'atec';
    if (str.includes('abc')) return 'abc';
    if (str.includes('srs')) return 'srs_2';
    if (str.includes('npi')) return 'npi';
    if (str.includes('10m') || str.includes('tc10') || str.includes('10mwt')) return 'tc10m';
    if (str.includes('9hpt') || str.includes('peg') || str.includes('pinos')) return 'peg9';
    return 'eam';
  }

  function openScaleGuide(scaleKeyOrRawName) {
    const guideData = window.NAPEN_SCALE_GUIDE || {};
    const key = guideData[scaleKeyOrRawName] ? scaleKeyOrRawName : resolveScaleKey(scaleKeyOrRawName);
    const scale = guideData[key] || guideData['eam'];
    if (!scale) return;

    if (scaleGuideSigla) scaleGuideSigla.textContent = scale.sigla;
    if (scaleGuideTempo) scaleGuideTempo.textContent = `⏱ ${scale.tempo_aplicacao || '5 a 10 min'}`;
    if (scaleGuideTitle) scaleGuideTitle.textContent = scale.nome;
    if (scaleGuideDominio) {
      scaleGuideDominio.textContent = scale.uso_privativo_psicologo
        ? `${scale.dominio} · Uso privativo de psicólogos (Lei nº 4.119/1962)`
        : scale.dominio;
    }
    if (scaleGuidePublico) scaleGuidePublico.textContent = scale.publico_alvo;
    if (scaleGuideMateriais) scaleGuideMateriais.textContent = scale.materiais;

    // 1. Passo a Passo
    if (scaleGuideStepsList) {
      scaleGuideStepsList.innerHTML = '';
      (scale.procedimento_passo_a_passo || []).forEach(step => {
        const li = document.createElement('li');
        li.className = 'scale-step-item';
        li.innerHTML = `
          <div class="scale-step-item-title">${step.passo}. ${step.titulo}</div>
          <div class="scale-step-item-desc">${step.descricao}</div>
        `;
        scaleGuideStepsList.appendChild(li);
      });
    }

    // 2. Pontuação e Graus
    if (scaleGuideScoresTable) {
      scaleGuideScoresTable.innerHTML = '';
      (scale.criterios_pontuacao || []).forEach(crit => {
        const row = document.createElement('div');
        row.className = 'scale-score-row';
        row.innerHTML = `
          <span class="scale-score-grau">${crit.grau}</span>
          <span class="scale-score-desc">${crit.descricao}</span>
        `;
        scaleGuideScoresTable.appendChild(row);
      });
    }

    if (scaleGuideMcidText) scaleGuideMcidText.textContent = scale.mcid || 'Consulte a literatura de referência.';
    if (scaleGuideInterpretacaoText) scaleGuideInterpretacaoText.textContent = scale.interpretacao_clinica || '';
    if (scaleGuideRefAbnt) scaleGuideRefAbnt.textContent = scale.referencia_abnt || '';
    if (scaleGuideDoiLink) {
      const hasLink = Boolean(scale.doi || (scale.link_artigo && scale.link_artigo !== '#'));
      if (hasLink) {
        scaleGuideDoiLink.style.display = 'inline-flex';
        scaleGuideDoiLink.href = scale.link_artigo || (scale.doi ? `https://doi.org/${scale.doi}` : '#');
        scaleGuideDoiLink.textContent = `Acessar Artigo Original (${scale.doi ? 'DOI: ' + scale.doi : 'Link Oficial'}) ↗`;
      } else {
        scaleGuideDoiLink.style.display = 'none';
        scaleGuideDoiLink.href = '#';
      }
    }
    if (scaleGuideValidacaoBrasil) scaleGuideValidacaoBrasil.textContent = scale.validacao_brasil || 'Adaptação e normas psicométricas disponíveis em língua portuguesa.';

    // Aba inicial: Passo a Passo
    document.querySelectorAll('.scale-tab-btn').forEach((b, idx) => b.classList.toggle('active', idx === 0));
    document.getElementById('scaleTabPassos')?.classList.add('active');
    document.getElementById('scaleTabPontuacao')?.classList.remove('active');
    document.getElementById('scaleTabValidacao')?.classList.remove('active');

    if (scaleGuideBackdrop) scaleGuideBackdrop.classList.add('visible');
    if (scaleGuideDrawer) scaleGuideDrawer.classList.add('visible');
  }

  function closeScaleGuide() {
    if (scaleGuideBackdrop) scaleGuideBackdrop.classList.remove('visible');
    if (scaleGuideDrawer) scaleGuideDrawer.classList.remove('visible');
  }

  if (scaleGuideCloseBtn) scaleGuideCloseBtn.addEventListener('click', closeScaleGuide);
  if (scaleGuideBackdrop) scaleGuideBackdrop.addEventListener('click', closeScaleGuide);

  document.querySelectorAll('.scale-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const tabKey = btn.getAttribute('data-tab');
      document.querySelectorAll('.scale-tab-btn').forEach(b => b.classList.toggle('active', b === btn));
      document.getElementById('scaleTabPassos')?.classList.toggle('active', tabKey === 'passos');
      document.getElementById('scaleTabPontuacao')?.classList.toggle('active', tabKey === 'pontuacao');
      document.getElementById('scaleTabValidacao')?.classList.toggle('active', tabKey === 'validacao');
    });
  });

  if (btnOpenScaleGuideMain) {
    btnOpenScaleGuideMain.addEventListener('click', () => {
      const activeMod = engine.getActiveModality();
      const activeScale = engine.getActiveScale();
      const scaleToOpen = activeScale?.scale_key || activeScale?.sigla || activeScale?.id || activeMod?.escala_recomendada;
      openScaleGuide(scaleToOpen);
    });
  }

  if (btnOpenScaleGuideCalc) {
    btnOpenScaleGuideCalc.addEventListener('click', () => {
      const activeScale = engine.getActiveScale();
      const activeMod = engine.getActiveModality();
      const scaleToOpen = activeScale?.scale_key || activeScale?.sigla || activeScale?.id || activeMod?.escala_recomendada;
      openScaleGuide(scaleToOpen);
    });
  }

  const btnOpenScaleGuidePresc = document.getElementById('btnOpenScaleGuidePresc');
  if (btnOpenScaleGuidePresc) {
    btnOpenScaleGuidePresc.addEventListener('click', () => {
      const activeScale = engine.getActiveScale();
      const activeMod = engine.getActiveModality();
      const scaleToOpen = activeScale?.scale_key || activeScale?.sigla || activeScale?.id || activeMod?.escala_recomendada;
      openScaleGuide(scaleToOpen);
    });
  }

  const btnScrollToCalc = document.getElementById('btnScrollToCalc');
  if (btnScrollToCalc) {
    btnScrollToCalc.addEventListener('click', (e) => {
      e.preventDefault();
      if (dualCalcContainer) {
        const headerEl = document.querySelector('.site-header');
        const headerHeight = headerEl ? headerEl.offsetHeight : 140;
        const rect = dualCalcContainer.getBoundingClientRect();
        const targetScrollY = window.pageYOffset + rect.top - headerHeight - 16;
        window.scrollTo({ top: targetScrollY, behavior: 'smooth' });
      }
    });
  }

  const tolAnchorBtn = typeof btnScrollToTolGuide !== 'undefined' && btnScrollToTolGuide ? btnScrollToTolGuide : document.getElementById('btnScrollToTolGuide');
  if (tolAnchorBtn) {
    tolAnchorBtn.addEventListener('click', (e) => {
      e.preventDefault();
      scrollToTolerabilityGuide();
    });
  }

  const evidenceAnchorBtn = typeof btnScrollToEvidence !== 'undefined' && btnScrollToEvidence ? btnScrollToEvidence : document.getElementById('btnScrollToEvidence');
  if (evidenceAnchorBtn) {
    evidenceAnchorBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const panel = typeof evidenceReferencePanel !== 'undefined' && evidenceReferencePanel ? evidenceReferencePanel : document.getElementById('evidenceReferencePanel');
      if (!panel) return;
      panel.open = true;
      const headerEl = document.querySelector('.site-header');
      const headerHeight = headerEl ? headerEl.offsetHeight : 140;
      const rect = panel.getBoundingClientRect();
      const targetScrollY = window.pageYOffset + rect.top - headerHeight - 16;
      window.scrollTo({ top: Math.max(0, targetScrollY), behavior: 'smooth' });
    });
  }

  if (btnScaleGuideUseInCalc) {
    btnScaleGuideUseInCalc.addEventListener('click', () => {
      closeScaleGuide();
      if (dualCalcContainer) {
        const headerEl = document.querySelector('.site-header');
        const headerHeight = headerEl ? headerEl.offsetHeight : 140;
        const rect = dualCalcContainer.getBoundingClientRect();
        const targetScrollY = window.pageYOffset + rect.top - headerHeight - 16;
        window.scrollTo({ top: targetScrollY, behavior: 'smooth' });
      }
    });
  }

  // ==========================================================================
  // 10. Busca Instantânea com Cruzamento Neuroanatômico (10-20 & Sinônimos)
  // ==========================================================================
  let searchDebounce = null;

  if (globalSearchInput) {
    globalSearchInput.addEventListener('focus', () => {
      if (searchPlaceholderMarquee) searchPlaceholderMarquee.classList.add('hidden');
    });

    globalSearchInput.addEventListener('blur', () => {
      if (searchPlaceholderMarquee && !globalSearchInput.value.trim()) {
        searchPlaceholderMarquee.classList.remove('hidden');
      }
    });

    globalSearchInput.addEventListener('input', (e) => {
      const val = e.target.value.trim();
      if (searchPlaceholderMarquee) {
        searchPlaceholderMarquee.classList.toggle('hidden', !!val);
      }
      clearTimeout(searchDebounce);
      searchDebounce = setTimeout(() => {
        const q = e.target.value.toLowerCase().trim();
        state.searchQuery = q;

        if (searchClearBtn) {
          searchClearBtn.classList.toggle('visible', !!q);
        }

        if (!q) {
          searchResultsDropdown.classList.remove('visible');
          searchResultsDropdown.innerHTML = '';
          return;
        }

      const matchesWithReason = [];

      data.condicoes.forEach(c => {
        let matched = false;
        let matchReason = '';

        const cTitle = (c.condicao || '').toLowerCase();
        const cEixo = (c.eixo || '').toLowerCase();
        const tags = c.tags_busca || {};

        // 1. Nome ou eixo principal
        if (cTitle.includes(q) || cEixo.includes(q)) {
          matched = true;
        }

        // 2. Coordenadas do Sistema 10-20 (ex: C3, C4, Cz, F3, F4, Broca)
        if (!matched && tags.coordenadas_10_20) {
          const foundCoord = tags.coordenadas_10_20.find(coord => coord.toLowerCase() === q || coord.toLowerCase().startsWith(q));
          if (foundCoord) {
            matched = true;
            matchReason = `Sistema 10-20: ${foundCoord} ➔ ${c.modalidades ? Object.values(c.modalidades)[0]?.alvo || 'M1' : ''}`;
          }
        }

        // 3. Alvos Anatômicos
        if (!matched && tags.alvos_anatomicos) {
          const foundAlvo = tags.alvos_anatomicos.find(a => a.toLowerCase().includes(q));
          if (foundAlvo) {
            matched = true;
            matchReason = `Alvo Anatômico: ${foundAlvo}`;
          }
        }

        // 4. Sinônimos em Inglês (stroke, depression, anxiety, pain, etc.)
        if (!matched && tags.sinonimos_en) {
          const foundEn = tags.sinonimos_en.find(s => s.toLowerCase().includes(q) || q.includes(s.toLowerCase()));
          if (foundEn) {
            matched = true;
            matchReason = `Sinônimo em Inglês (${foundEn})`;
          }
        }

        // 5. Escalas Clínicas (EAM, FMA, BBS, SARA, HAM-D, etc.)
        if (!matched && tags.escalas) {
          const foundScale = tags.escalas.find(s => s.toLowerCase().includes(q) || q.includes(s.toLowerCase()));
          if (foundScale) {
            matched = true;
            matchReason = `Escala Clínica: ${foundScale}`;
          }
        }

        // 6. Sintomas em Português
        if (!matched && tags.sintomas_pt) {
          const foundSymptom = tags.sintomas_pt.find(s => s.toLowerCase().includes(q));
          if (foundSymptom) {
            matched = true;
            matchReason = `Sintoma: ${foundSymptom}`;
          }
        }

        // 7. Modalidades, técnicas e alvos
        if (!matched) {
          Object.values(c.modalidades || {}).forEach(m => {
            if ((m.tecnica || '').toLowerCase().includes(q)) {
              matched = true;
              matchReason = `Técnica: ${m.tecnica}`;
            } else if ((m.alvo || '').toLowerCase().includes(q)) {
              matched = true;
              matchReason = `Alvo: ${m.alvo}`;
            } else if ((m.escala_recomendada || '').toLowerCase().includes(q)) {
              matched = true;
              matchReason = `Escala: ${m.escala_recomendada}`;
            }
          });
        }

        // 8. Fatores limitantes
        if (!matched) {
          const foundFactor = (c.fatores_limitantes || []).find(f => f.label.toLowerCase().includes(q));
          if (foundFactor) {
            matched = true;
            matchReason = `Fator: ${foundFactor.label}`;
          }
        }

        if (matched) {
          matchesWithReason.push({ condition: c, matchReason });
        }
      });

      if (matchesWithReason.length === 0) {
        searchResultsDropdown.innerHTML = `
          <div style="padding: 14px 18px; color: var(--text-muted); font-size: 0.88rem;">
            Nenhuma condição encontrada para "<strong>${e.target.value}</strong>".
          </div>
        `;
        searchResultsDropdown.classList.add('visible');
        return;
      }

      searchResultsDropdown.innerHTML = '';
      matchesWithReason.forEach(({ condition: c, matchReason }) => {
        const item = document.createElement('div');
        item.className = 'search-result-item';
        item.innerHTML = `
          <div>
            <div class="search-res-title">${c.condicao}</div>
            <div class="search-res-eixo">${c.eixo}</div>
            ${matchReason ? `<div class="search-res-match-tag">${matchReason}</div>` : ''}
          </div>
          <span style="color: var(--napen-teal-dark); font-weight: 700; font-size: 0.95rem;">➔</span>
        `;

        item.addEventListener('click', () => {
          openConditionAlgorithm(c.id);
        });

        searchResultsDropdown.appendChild(item);
      });

      searchResultsDropdown.classList.add('visible');
    }, 120);
  });
}

  if (searchClearBtn) {
    searchClearBtn.addEventListener('click', () => {
      globalSearchInput.value = '';
      state.searchQuery = '';
      if (searchPlaceholderMarquee) searchPlaceholderMarquee.classList.remove('hidden');
      searchClearBtn.classList.remove('visible');
      searchResultsDropdown.classList.remove('visible');
    });
  }

  // Fecha dropdown de busca ao clicar fora
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.search-box-wrap')) {
      if (searchResultsDropdown) searchResultsDropdown.classList.remove('visible');
    }
  });

  // ==========================================================================
  // ==========================================================================
  // 9. Biblioteca de Evidências & Metanálises (Repositório Científico)
  // ==========================================================================
  function renderPocketTable() {
    if (!pocketTableBody) return;
    pocketTableBody.innerHTML = '';

    const escAttr = (val) => String(val || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

    data.condicoes.forEach(c => {
      const factors = c.fatores_limitantes || [];
      factors.forEach(f => {
        const m = resolveModalityForFactor(c, f.id);
        if (!m) return;

        const ensaio = m.ensaio_clinico || m.artigo_referencia;
        const meta = m.meta_analise;
        const amstar = meta ? (meta.amstar2 || m.amstar2) : m.amstar2;
        const grade = m.grade;

        let condLabel = c.condicao.replace(/\s*\([A-Z0-9]+\)/g, '');
        let eixoLabel = (c.eixo || '').replace(/\s*\([A-Z0-9]+\)/g, '');
        if (condLabel.startsWith(eixoLabel + ' — ')) {
          condLabel = condLabel.replace(eixoLabel + ' — ', '');
        }

        const recStr = m.diretriz_internacional || 'Recomendação Consensual NAPeN';
        const isIfcnLefaucheur = /lefaucheur|ifcn/i.test(recStr);
        const guideRef = isIfcnLefaucheur ? (m.diretriz_ref || null) : (meta && meta.url_doi ? meta : null);
        const fonteRecLabel = isIfcnLefaucheur
          ? 'Guideline IFCN — apenas Nível de Evidência'
          : 'Síntese / Metanálise Clínica (sem gradação IFCN direta)';
        const protLabel = m.tecnica || m.modalidade_sigla || 'Protocolo de 1ª Linha';
        const hasMultipleRoutes = (Array.isArray(c.modalidades_suportadas) && c.modalidades_suportadas.length > 1)
          || (Array.isArray(m.cadeia_sequencial) && m.cadeia_sequencial.length > 1);
        const altRouteHint = hasMultipleRoutes
          ? '<div class="pocket-alt-route-hint">1ª linha padrão do desfecho · ver outras rotas no algoritmo</div>'
          : '';

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <strong style="color: var(--napen-navy); font-size: 0.90rem;">${escHtml(condLabel)}</strong>
            <div style="font-size: 0.75rem; color: var(--text-faint); margin-top: 2px;">${escHtml(eixoLabel)}</div>
          </td>
          <td>
            <span style="background: var(--napen-teal-soft); color: var(--napen-teal-dark); padding: 4px 9px; border-radius: 3px; font-weight: 600; font-size: 0.78rem; display: inline-block;">
              ${escHtml(f.label || f.nome || '')}
            </span>
            ${grade ? `
              <div style="margin-top: 8px;">
                <div class="pocket-cell-kicker">GRADE deste desfecho:</div>
                <span class="evidence-tag-grade ${getQualityLevelClass(grade.certeza)}" title="${escAttr(grade.observacao_dominios)}">
                  GRADE: ${escHtml(grade.certeza)} (${escHtml(grade.simbolos)}) · Rec. ${escHtml(grade.forca_recomendacao)}
                </span>
                <div style="font-size: 0.70rem; color: var(--text-faint); margin-top: 3px;">
                  ${escHtml(grade.status_homologacao || 'Avaliação preliminar — Em homologação GT')}
                </div>
              </div>
            ` : ''}
          </td>
          <td>
            <div class="pocket-cell-kicker">Nível de evidência (${isIfcnLefaucheur ? 'Guideline' : 'Síntese'}):</div>
            <div style="font-weight: 700; color: var(--napen-teal-dark); font-size: 0.82rem; line-height: 1.35;">
              ${escHtml(recStr)}
            </div>
            <div class="pocket-source-note">${escHtml(fonteRecLabel)}</div>
            ${guideRef && guideRef.url_doi ? `
              <a href="${escHtml(guideRef.url_doi)}" target="_blank" rel="noopener noreferrer" style="color: var(--napen-teal-dark); font-weight: 700; text-decoration: underline; font-size: 0.75rem; display: inline-block; margin-top: 4px;">
                ${escHtml(guideRef.autores || 'Referência')} (${escHtml(guideRef.ano || '')}) · DOI ↗
              </a>
            ` : ''}
          </td>
          <td>
            <div class="pocket-cell-kicker">Protocolo sugerido (1ª linha):</div>
            <div class="pocket-protocol-tag">${escHtml(protLabel)}</div>
            ${ensaio ? `
              <div class="pocket-cell-kicker" style="margin-top: 6px;">Ensaio clínico que embasa este protocolo:</div>
              <div style="font-size: 0.80rem; line-height: 1.4;">
                <div style="font-weight: 700; color: var(--text-main);">${escHtml(ensaio.autores)} (${escHtml(ensaio.ano)})</div>
                <div style="font-size: 0.74rem; color: var(--text-muted); margin-top: 2px;">${escHtml(ensaio.titulo || '')}</div>
                ${ensaio.url_doi ? `
                  <a href="${escHtml(ensaio.url_doi)}" target="_blank" rel="noopener noreferrer" style="color: var(--napen-teal-dark); font-weight: 700; text-decoration: underline; font-size: 0.76rem; display: inline-block; margin-top: 4px;">
                    Acessar Ensaio do Protocolo via DOI ↗
                  </a>
                ` : ''}
                ${altRouteHint}
              </div>
            ` : '<span style="color: var(--text-faint); font-size: 0.75rem;">—</span>'}
          </td>
          <td>
            ${meta ? `
              <div style="font-size: 0.80rem; line-height: 1.4;">
                <div style="font-weight: 700; color: var(--text-muted);">${escHtml(meta.autores)} (${escHtml(meta.ano)})</div>
                <div style="font-size: 0.74rem; color: var(--text-muted); margin-top: 2px;">${escHtml(meta.titulo || '')}</div>
                ${amstar ? `
                  <div style="margin-top: 6px;">
                    <span class="evidence-tag-amstar ${getQualityLevelClass(amstar.nivel)}" title="${escAttr(amstar.justificativa_preliminar)}">
                      AMSTAR 2: ${escHtml(amstar.nivel)}
                    </span>
                    <div style="font-size: 0.70rem; color: var(--text-faint); margin-top: 3px;">
                      ${escHtml(amstar.status_homologacao || 'Avaliação preliminar — Em homologação GT')}
                    </div>
                  </div>
                ` : ''}
                ${meta.url_doi ? `
                  <a href="${escHtml(meta.url_doi)}" target="_blank" rel="noopener noreferrer" style="color: var(--napen-teal-dark); font-weight: 700; text-decoration: underline; font-size: 0.76rem; display: inline-block; margin-top: 4px;">
                    Acessar Metanálise via DOI ↗
                  </a>
                ` : ''}
              </div>
            ` : '<span style="color: var(--text-faint); font-size: 0.75rem;">—</span>'}
          </td>
          <td style="text-align: center; vertical-align: middle;">
            <button type="button" class="btn-evidence-goto" data-condition-id="${escHtml(c.id)}" data-factor-id="${escHtml(f.id)}">
              Prescrever no Algoritmo ➔
            </button>
          </td>
        `;

        const btnGoto = tr.querySelector('.btn-evidence-goto');
        if (btnGoto) {
          btnGoto.addEventListener('click', () => {
            switchTab('prescription');
            openConditionAlgorithm(c.id, { forceEntryMode: 'new' });
            if (f.id) {
              engine.setFactor(f.id);
              if (typeof renderContinuityBar === 'function') renderContinuityBar(c);
              if (typeof renderCascadingFlow === 'function') renderCascadingFlow(c);
              if (typeof renderNode1Options === 'function') renderNode1Options(c);
              if (typeof updatePrescriptionDisplay === 'function') updatePrescriptionDisplay();
              if (typeof updateOutcomeDisplay === 'function') updateOutcomeDisplay();
            }
          });
        }

        pocketTableBody.appendChild(tr);
      });
    });
  }

  // ==========================================================================
  // 10. Gestão de Abas da Barra Turquesa Oficial
  // ==========================================================================
  function switchTab(tabKey) {
    state.activeTab = tabKey;

    navItemPrescription.classList.toggle('active', tabKey === 'prescription');
    navItemPocket.classList.toggle('active', tabKey === 'pocket');
    navItemMethod.classList.toggle('active', tabKey === 'method');

    panePrescription.style.display = tabKey === 'prescription' ? 'flex' : 'none';
    panePocket.style.display = tabKey === 'pocket' ? 'block' : 'none';
    paneMethod.style.display = tabKey === 'method' ? 'block' : 'none';

    window.scrollTo({ top: 120, behavior: 'smooth' });
  }

  if (tabBtnPrescription) {
    tabBtnPrescription.addEventListener('click', (e) => {
      e.stopPropagation();
      switchTab('prescription');
      toggleDropdown();
    });
  }

  if (tabBtnPocket) {
    tabBtnPocket.addEventListener('click', () => {
      closeAllDropdowns();
      switchTab('pocket');
    });
  }

  if (tabBtnMethod) {
    tabBtnMethod.addEventListener('click', () => {
      closeAllDropdowns();
      switchTab('method');
    });
  }

  // Hover suave no desktop para o menu de Prescrição Interativa
  if (navItemPrescription) {
    navItemPrescription.addEventListener('mouseenter', () => {
      openDropdown();
    });
    navItemPrescription.addEventListener('mouseleave', () => {
      closeDropdown();
    });
  }

  // Fechar dropdowns ao clicar fora ou teclar ESC
  document.addEventListener('click', (e) => {
    if (navItemPrescription && !navItemPrescription.contains(e.target)) {
      closeDropdown();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllDropdowns();
    }
  });

  // Inicialização
  populateDropdownMenu();
  populateHomeContinuityConditions();
  renderHomeContinuityPanel();
  renderPocketTable();
});
