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
    pemStatus: 'sim' // 'sim' | 'nao'
  };

  const eamState = {
    base: null,
    post: null
  };

  // Elementos de Navegação da Barra Turquesa
  const navItemPrescription = document.getElementById('navItemPrescription');
  const navItemCalc = document.getElementById('navItemCalc');
  const navItemPocket = document.getElementById('navItemPocket');
  const navItemMethod = document.getElementById('navItemMethod');

  const tabBtnPrescription = document.getElementById('tabBtnPrescription');
  const tabBtnCalc = document.getElementById('tabBtnCalc');
  const tabBtnPocket = document.getElementById('tabBtnPocket');
  const tabBtnMethod = document.getElementById('tabBtnMethod');

  const dropdownConditionsList = document.getElementById('dropdownConditionsList');
  const dropdownCalcList = document.getElementById('dropdownCalcList');

  // Painéis das Abas
  const panePrescription = document.getElementById('panePrescription');
  const panePocket = document.getElementById('panePocket');
  const paneMethod = document.getElementById('paneMethod');

  // Elementos da Prescrição Interativa
  const searchHeroPanel = document.getElementById('searchHeroPanel');
  const algorithmActiveContainer = document.getElementById('algorithmActiveContainer');
  const btnClearSelection = document.getElementById('btnClearSelection');

  const globalSearchInput = document.getElementById('globalSearchInput');
  const searchPlaceholderMarquee = document.getElementById('searchPlaceholderMarquee');
  const searchClearBtn = document.getElementById('searchClearBtn');
  const searchResultsDropdown = document.getElementById('searchResultsDropdown');

  // Elementos do Algoritmo Clínico
  const algoCondEixo = document.getElementById('algoCondEixo');
  const algoCondTitle = document.getElementById('algoCondTitle');
  const node1QuestionText = document.getElementById('node1QuestionText');
  const node1OptionsList = document.getElementById('node1OptionsList');

  const prescTecnica = document.getElementById('prescTecnica');
  const prescModalidade = document.getElementById('prescModalidade');
  const prescAlvo = document.getElementById('prescAlvo');
  const prescFrequencia = document.getElementById('prescFrequencia');
  const prescIntensidade = document.getElementById('prescIntensidade');
  const prescPulsos = document.getElementById('prescPulsos');
  const prescSessoes = document.getElementById('prescSessoes');
  const prescDesfechoNome = document.getElementById('prescDesfechoNome');
  const prescEscala = document.getElementById('prescEscala');
  const prescEfeito = document.getElementById('prescEfeito');
  const prescMeta = document.getElementById('prescMeta');
  const guidelineBadgeText = document.getElementById('guidelineBadgeText');

  // Painel de Triagem Neurofisiológica (PEM)
  const pemTriagePanel = document.getElementById('pemTriagePanel');
  const btnPemSim = document.getElementById('btnPemSim');
  const btnPemNao = document.getElementById('btnPemNao');

  // Botões de Desfecho Oficial da Rede NAPeN
  const btnOutcomeSuccess = document.getElementById('btnOutcomeSuccess');
  const btnOutcomeDanger = document.getElementById('btnOutcomeDanger');
  const branchResultPanel = document.getElementById('branchResultPanel');

  // Evidência Científica e Referências Formais
  const evidenceReferencePanel = document.getElementById('evidenceReferencePanel');
  const evidenceCitationText = document.getElementById('evidenceCitationText');
  const evidenceDoiLink = document.getElementById('evidenceDoiLink');
  const evidenceDoiText = document.getElementById('evidenceDoiText');
  const evidenceGuidelineText = document.getElementById('evidenceGuidelineText');
  const evidenceGuidelineDoiLink = document.getElementById('evidenceGuidelineDoiLink');
  const evidenceGuidelineDoiText = document.getElementById('evidenceGuidelineDoiText');

  // Calculadora Dual (Clínica & Comparador de Efeito)
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
  const cardDeltaPoints = document.getElementById('cardDeltaPoints');
  const calcDeltaPoints = document.getElementById('calcDeltaPoints');
  const cardDeltaPercent = document.getElementById('cardDeltaPercent');
  const calcDeltaPercent = document.getElementById('calcDeltaPercent');
  const cardMcidBadge = document.getElementById('cardMcidBadge');
  const calcMcidBadge = document.getElementById('calcMcidBadge');
  const calcStudyRef = document.getElementById('calcStudyRef');
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

  // Elementos do Painel de Monitoramento Clínico
  const monitoringReeval = document.getElementById('monitoringReeval');
  const monitoringDoseAdjust = document.getElementById('monitoringDoseAdjust');
  const monitoringStopRule = document.getElementById('monitoringStopRule');
  const monitoringNotesText = document.getElementById('monitoringNotesText');

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
      dropdownConditionsList.classList.add('dropdown-force-closed');
      setTimeout(() => {
        dropdownConditionsList.classList.remove('dropdown-force-closed');
      }, 300);
    }
  }

  function openDropdown() {
    closeCalcDropdown();
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

  function closeCalcDropdown() {
    if (navItemCalc) {
      navItemCalc.classList.remove('dropdown-open');
    }
    if (dropdownCalcList) {
      dropdownCalcList.querySelectorAll('.dropdown-item-has-submenu').forEach(item => {
        item.classList.remove('submenu-open');
      });
      dropdownCalcList.classList.add('dropdown-force-closed');
      setTimeout(() => {
        dropdownCalcList.classList.remove('dropdown-force-closed');
      }, 300);
    }
  }

  function openCalcDropdown() {
    closeDropdown();
    if (navItemCalc) {
      navItemCalc.classList.add('dropdown-open');
    }
  }

  function toggleCalcDropdown() {
    if (!navItemCalc) return;
    if (navItemCalc.classList.contains('dropdown-open')) {
      closeCalcDropdown();
    } else {
      openCalcDropdown();
    }
  }

  function closeAllDropdowns() {
    closeDropdown();
    closeCalcDropdown();
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
  // 1b. Popula Dropdown da Calculadora de Resposta Clínica (3 Níveis em Cascata)
  // Eixo ➔ Condição / Foco ➔ Desfechos & Escala Direta
  // ==========================================================================
  function navigateToCalculator(conditionId, factorId, scaleId) {
    // 1. Alterna para a visualização de prescrição/algoritmo
    switchTab('prescription');

    // 2. Abre a condição selecionada
    openConditionAlgorithm(conditionId);

    // 3. Define o fator limitante (medida) específico
    if (factorId) {
      engine.setFactor(factorId);
      const cond = engine.getCondition(conditionId);
      renderNode1Options(cond);
    }

    // 4. Se houver escala específica selecionada (ex: SARA ou BBS)
    if (scaleId) {
      engine.setActiveScale(scaleId);
    }

    // 5. Atualiza display e calculadora
    updatePrescriptionDisplay();

    // 6. Rola suavemente até o início EXATO da calculadora (com respiro abaixo do cabeçalho)
    setTimeout(() => {
      if (dualCalcContainer) {
        const headerEl = document.querySelector('.site-header');
        const headerHeight = headerEl ? headerEl.offsetHeight : 140;
        const rect = dualCalcContainer.getBoundingClientRect();
        const targetScrollY = window.pageYOffset + rect.top - headerHeight - 16;

        window.scrollTo({
          top: Math.max(0, targetScrollY),
          behavior: 'smooth'
        });

        dualCalcContainer.classList.add('calc-highlight-pulse');
        setTimeout(() => {
          dualCalcContainer.classList.remove('calc-highlight-pulse');
        }, 2500);
      }
    }, 180);

    // 8. Fecha os menus dropdowns
    closeAllDropdowns();
  }

  function populateCalcDropdown() {
    if (!dropdownCalcList) return;
    dropdownCalcList.innerHTML = '';

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

      // Alterna submenu (2º Nível) no clique
      aAxis.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const wasOpen = liAxis.classList.contains('submenu-open');
        dropdownCalcList.querySelectorAll('.dropdown-item-has-submenu').forEach(item => {
          item.classList.remove('submenu-open');
        });
        if (!wasOpen) {
          liAxis.classList.add('submenu-open');
        }
      });

      // Abre submenu no hover no desktop
      liAxis.addEventListener('mouseenter', () => {
        dropdownCalcList.querySelectorAll('.dropdown-item-has-submenu').forEach(item => {
          if (item !== liAxis) item.classList.remove('submenu-open');
        });
        liAxis.classList.add('submenu-open');
      });

      // Submenu do 2º Nível (Condições / Focos do Eixo)
      const ulSub = document.createElement('ul');
      ulSub.className = 'dropdown-submenu';

      conditionsInAxis.forEach(c => {
        const liCond = document.createElement('li');
        liCond.className = 'dropdown-item-napen dropdown-item-has-subsubmenu';

        const aCond = document.createElement('a');
        aCond.className = 'dropdown-sublink-napen dropdown-sublink-has-subsubmenu';
        aCond.href = '#';

        // Título limpo da condição (remove prefixos redundantes)
        let cleanTitle = c.condicao;
        if (axisName === 'Acidente Vascular Cerebral' || axisName === 'Doenças Cerebrovasculares (AVC)') {
          cleanTitle = cleanTitle.replace(/^Acidente Vascular Cerebral\s*(\(AVC\))?\s*—\s*/i, '');
        }

        aCond.innerHTML = `
          <span class="dropdown-sublink-title">${cleanTitle}</span>
          <span class="axis-arrow-icon" style="font-size: 0.95rem; font-weight: 700; margin-left: 10px; color: var(--napen-teal-bar); transition: transform 0.25s ease; display: inline-block;">›</span>
        `;

        // Submenu do 3º Nível (Desfechos e Escalas Diretas)
        const ulSubSub = document.createElement('ul');
        ulSubSub.className = 'dropdown-subsubmenu';

        const factors = c.fatores_limitantes || [];
        factors.forEach(f => {
          const m = c.modalidades ? c.modalidades[f.id] : null;
          if (!m) return;

          const measureTitle = f.label.split('(')[0].trim();

          // Se houver múltiplas escalas detalhadas (ex: SARA e BBS nas Ataxias)
          if (m.escalas_detalhadas && m.escalas_detalhadas.length > 1) {
            m.escalas_detalhadas.forEach(sc => {
              const liMeasure = document.createElement('li');
              const aMeasure = document.createElement('a');
              aMeasure.className = 'dropdown-sublink-napen';
              aMeasure.href = '#';
              const scaleName = sc.nome_escala || sc.id.toUpperCase();
              aMeasure.innerHTML = `
                <span class="dropdown-sublink-title">${measureTitle}</span>
                <span class="dropdown-sublink-sub" style="color: var(--napen-teal-dark); font-weight: 600;">${scaleName}</span>
              `;
              aMeasure.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                navigateToCalculator(c.id, f.id, sc.id);
              });
              liMeasure.appendChild(aMeasure);
              ulSubSub.appendChild(liMeasure);
            });
          } else {
            const liMeasure = document.createElement('li');
            const aMeasure = document.createElement('a');
            aMeasure.className = 'dropdown-sublink-napen';
            aMeasure.href = '#';
            const scaleName = m.escala_recomendada || 'Escala de Avaliação Clínica';
            aMeasure.innerHTML = `
              <span class="dropdown-sublink-title">${measureTitle}</span>
              <span class="dropdown-sublink-sub" style="color: var(--napen-teal-dark); font-weight: 600;">${scaleName}</span>
            `;
            aMeasure.addEventListener('click', (e) => {
              e.preventDefault();
              e.stopPropagation();
              navigateToCalculator(c.id, f.id, null);
            });
            liMeasure.appendChild(aMeasure);
            ulSubSub.appendChild(liMeasure);
          }
        });

        // Alterna o 3º nível no clique (mobile e touch)
        aCond.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          const wasOpen = liCond.classList.contains('subsubmenu-open');
          ulSub.querySelectorAll('.dropdown-item-has-subsubmenu').forEach(item => {
            item.classList.remove('subsubmenu-open');
          });
          if (!wasOpen) {
            liCond.classList.add('subsubmenu-open');
            const subRect = ulSubSub.getBoundingClientRect();
            if (subRect.right > window.innerWidth - 10) {
              ulSubSub.classList.add('open-left');
            } else {
              ulSubSub.classList.remove('open-left');
            }
          }
        });

        // Hover suave no desktop
        liCond.addEventListener('mouseenter', () => {
          ulSub.querySelectorAll('.dropdown-item-has-subsubmenu').forEach(item => {
            if (item !== liCond) item.classList.remove('subsubmenu-open');
          });
          liCond.classList.add('subsubmenu-open');
          const subRect = ulSubSub.getBoundingClientRect();
          if (subRect.right > window.innerWidth - 10) {
            ulSubSub.classList.add('open-left');
          } else {
            ulSubSub.classList.remove('open-left');
          }
        });

        liCond.appendChild(aCond);
        liCond.appendChild(ulSubSub);
        ulSub.appendChild(liCond);
      });

      liAxis.appendChild(aAxis);
      liAxis.appendChild(ulSub);
      dropdownCalcList.appendChild(liAxis);
    });
  }

  // ==========================================================================
  // 2. Abertura do Algoritmo Clínico Sob Demanda
  // ==========================================================================
  function openConditionAlgorithm(conditionId) {
    state.selectedConditionId = conditionId;
    engine.setCondition(conditionId);

    const cond = engine.getCondition(conditionId);
    if (!cond) return;

    if (algoCondEixo) algoCondEixo.textContent = cond.eixo;
    if (algoCondTitle) algoCondTitle.textContent = cond.condicao;
    if (node1QuestionText) {
      node1QuestionText.textContent = cond.no1_pergunta || 'Qual é o principal fator limitante ou foco de ganho terapêutico?';
    }

    // Gerenciamento da Estratificação Neurofisiológica (PEM no MS para AVC)
    if (conditionId === 'avc-membro-superior') {
      if (pemTriagePanel) pemTriagePanel.style.display = 'flex';
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

    renderNode1Options(cond);
    updatePrescriptionDisplay();
  }

  function clearSelectedCondition() {
    state.selectedConditionId = null;
    if (algorithmActiveContainer) algorithmActiveContainer.classList.remove('visible');
    if (searchHeroPanel) searchHeroPanel.style.display = 'flex';

    document.querySelectorAll('.dropdown-sublink-napen').forEach(link => {
      link.classList.remove('active-item');
    });

    window.scrollTo({ top: 120, behavior: 'smooth' });
  }

  if (btnClearSelection) {
    btnClearSelection.addEventListener('click', clearSelectedCondition);
  }

  // ==========================================================================
  // 3. Renderiza Pills do Fator Limitante Principal
  // ==========================================================================
  function renderNode1Options(cond) {
    if (!node1OptionsList) return;
    node1OptionsList.innerHTML = '';

    let factors = cond.fatores_limitantes || [];
    if (cond.id === 'avc-membro-superior') {
      if (state.pemStatus === 'nao') {
        factors = factors.filter(f => f.triagem_pem === 'nao');
      } else {
        factors = factors.filter(f => f.triagem_pem !== 'nao');
      }
    }

    if (!factors.some(f => f.id === engine.activeFactorId) && factors.length > 0) {
      engine.setFactor(factors[0].id);
    }

    factors.forEach(f => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = `pill-factor-btn ${engine.activeFactorId === f.id ? 'active' : ''}`;
      btn.textContent = f.label;

      btn.addEventListener('click', () => {
        engine.setFactor(f.id);
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

    const scales = m.escalas_detalhadas || [];

    // 1. Seletor de Múltiplas Escalas (Tabs)
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

    const studyName = effObj.estudo_referencia || m?.ensaio_clinico?.autores || 'Estudos de referência';
    const studyDetail = effObj.estudo_detalhe ? ` (${effObj.estudo_detalhe})` : '';
    if (calcStudyRef) {
      calcStudyRef.textContent = `${studyName}${studyDetail}`;
    }

    if (calcStudyCohen) {
      calcStudyCohen.textContent = effObj.cohen_d || 'd ≈ 0.65 (Efeito Moderado)';
    }

    if (calcStudyMcid) {
      calcStudyMcid.textContent = effObj.mcid_label || activeScale?.meta_texto || m.meta_melhora || 'Ganho clínico relevante';
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
      calcComparisonFeedback.textContent = 'Ao informar os escores, o sistema analisará se o ganho clínico individual é compatível com o intervalo de confiança dos estudos de referência e se superou a MCID da escala.';
    }

    // Reseta desfecho ao alternar escala ou fator
    engine.setOutcome(null);
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
  // 5. Atualiza Prescrição Primária, Diretrizes e Monitoramento do Ciclo
  // ==========================================================================
  function updatePrescriptionDisplay() {
    const m = engine.getActiveModality();
    if (!m) return;

    if (prescTecnica) prescTecnica.textContent = m.tecnica || '—';
    if (prescModalidade) prescModalidade.textContent = `Modalidade: ${m.modalidade_sigla || 'NIBS'}`;
    if (prescAlvo) prescAlvo.textContent = m.alvo || '—';
    if (prescFrequencia) prescFrequencia.textContent = m.frequencia || '—';
    if (prescIntensidade) prescIntensidade.textContent = `Intensidade: ${m.intensidade || 'Conforme limiar motor/sensorial'}`;
    if (prescPulsos) prescPulsos.textContent = m.pulsos_duracao || '—';
    if (prescSessoes) prescSessoes.textContent = `Dose e Sessões: ${m.sessoes || '—'}`;
    
    // Dissociação Conceitual NAPeN: Desfecho Clínico Alvo vs. Instrumento de Avaliação
    const cond = engine.getCondition(engine.activeConditionId);
    const activeFactor = cond?.fatores_limitantes?.find(f => f.id === engine.activeFactorId);
    if (prescDesfechoNome) {
      prescDesfechoNome.textContent = activeFactor ? activeFactor.label : (cond ? cond.condicao : 'Desfecho Clínico Alvo');
    }

    const activeScale = engine.getActiveScale() || (m.escalas_detalhadas && m.escalas_detalhadas.length > 0 ? m.escalas_detalhadas[0] : null);
    if (prescEscala) prescEscala.textContent = activeScale?.nome || m.escala_recomendada || 'Escala Clínica Validada';
    if (prescEfeito) prescEfeito.textContent = activeScale?.tamanho_efeito || m.tamanho_efeito || 'Eficácia demonstrada em ensaios controlados randomizados.';
    if (prescMeta) prescMeta.textContent = activeScale?.meta_texto || m.meta_melhora || 'Melhora clinicamente relevante conforme protocolo.';

    // Diretriz Internacional Oficial em Padrão ABNT
    const gInfo = engine.getFormattedGuideline();
    if (guidelineBadgeText) {
      if (gInfo && gInfo.url) {
        guidelineBadgeText.innerHTML = `
          <span><strong>${gInfo.recomendacao}</strong> — ${gInfo.autores || 'IFCN'} (${gInfo.ano || 'Consenso'})</span>
          <a href="${gInfo.url}" target="_blank" rel="noopener noreferrer" style="color: var(--napen-teal-dark); text-decoration: underline; margin-left: 6px; font-weight: 600;" title="Acessar diretriz oficial via DOI">
            ${gInfo.doi ? `DOI: ${gInfo.doi} ↗` : 'Acessar Diretriz ↗'}
          </a>
        `;
      } else {
        guidelineBadgeText.textContent = gInfo?.text || 'Recomendação Consensual NAPeN';
      }
    }

    // Painel de Evidências: Estudos de referência vs. Diretriz Internacional
    if (m.artigo_referencia) {
      if (evidenceCitationText) {
        evidenceCitationText.innerHTML = `<strong>${m.artigo_referencia.citacao_completa || m.artigo_referencia.autores}</strong> — <em>"${m.artigo_referencia.titulo || ''}"</em> (${m.artigo_referencia.revista || ''})`;
      }
      if (evidenceDoiLink) {
        evidenceDoiLink.href = m.artigo_referencia.url_doi || '#';
      }
      if (evidenceDoiText) {
        evidenceDoiText.textContent = m.artigo_referencia.doi ? `DOI: ${m.artigo_referencia.doi}` : 'Acessar Artigo Oficial';
      }
    }

    if (evidenceGuidelineText) {
      evidenceGuidelineText.innerHTML = `<strong>${gInfo.recomendacao}</strong> — Diretriz Internacional IFCN / Consenso (${gInfo.autores || 'IFCN'}, ${gInfo.ano || '2020'}).`;
    }
    if (evidenceGuidelineDoiLink) {
      evidenceGuidelineDoiLink.href = gInfo.url || '#';
    }
    if (evidenceGuidelineDoiText) {
      evidenceGuidelineDoiText.textContent = gInfo.doi ? `DOI: ${gInfo.doi}` : 'Acessar Diretriz Oficial';
    }



    // Monitoramento Clínico e Regras de Reavaliação
    const sa = m.sessoes_ajuste || {};
    if (monitoringReeval) {
      monitoringReeval.textContent = sa.quando_reavaliar || 'Reavaliar pontuação na escala clínica após 5 a 10 sessões de indução.';
    }
    if (monitoringDoseAdjust) {
      monitoringDoseAdjust.textContent = sa.ajuste_dose || 'Se resposta parcial, estender ciclo em +5 sessões diárias e recalibrar o Limiar Motor de Repouso (LMR).';
    }
    if (monitoringStopRule) {
      monitoringStopRule.textContent = sa.regra_interrupcao || 'Interromper o ciclo de indução e migrar para o Protocolo Alternativo se não houver ganho clínico mínimo após 2 ajustes sucessivos.';
    }
    if (monitoringNotesText) {
      monitoringNotesText.textContent = m.notas_clinicas || 'A estimulação deve ser associada a intervenção motora ou comportamental imediata com metas funcionais bem delineadas.';
    }

    if (stepNode3) stepNode3.classList.add('completed');

    // Inicializa a calculadora com a escala ativa correspondente
    renderCalculatorForActiveScale();
  }

  // ==========================================================================
  // 6. Assistente de Resposta Clínica (Sem Emojis, Badges Clínicos Sóbrios)
  // ==========================================================================
  // 6. Atualiza Assistente de Resposta Clínica (Pós-Indução)
  // ==========================================================================
  function updateOutcomeDisplay() {
    const outcome = engine.activeOutcome;
    const m = engine.getActiveModality();

    if (btnOutcomeSuccess) btnOutcomeSuccess.classList.toggle('active', outcome === 'success');
    if (btnOutcomeDanger) btnOutcomeDanger.classList.toggle('active', outcome === 'danger');

    if (!outcome) {
      branchResultPanel.className = 'branch-result-panel';
      branchResultPanel.innerHTML = '';
      if (stepNode4) stepNode4.classList.remove('completed', 'current');
      return;
    }

    if (stepNode4) stepNode4.classList.add('current');

    if (outcome === 'success') {
      branchResultPanel.className = 'branch-result-panel success visible';
      branchResultPanel.innerHTML = `
        <div style="font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
          <span class="outcome-bullet status-success"></span>
          [Resposta Clínica Satisfatória Alcançada]
        </div>
        <div style="color: var(--status-success-text); line-height: 1.55;">
          Paciente atingiu ou superou a meta terapêutica estabelecida no protocolo (${m?.escala_recomendada || 'escala clínica'}).
          <br><strong>Conduta Oficial do Roadmap NAPeN:</strong> Manter o protocolo primário até consolidação do ganho clínico e iniciar transição para manutenção periódica (redução gradual da frequência para 1 sessão por semana ou quinzenal, mantendo terapia multiprofissional concomitante e reavaliações periódicas).
        </div>
      `;
    } else if (outcome === 'danger') {
      branchResultPanel.className = 'branch-result-panel danger visible';
      const alt = m?.protocolo_alternativo;

      let altContent = '';
      if (alt) {
        altContent = `
          <div class="alternative-protocol-box">
            <div class="alt-title-line">
              <span style="color: var(--napen-teal-dark); font-weight: 700;">➔</span>
              ${alt.nome || 'Protocolo Alternativo Sequencial (Próxima Etapa da Árvore NAPeN)'}
            </div>
            <div><strong>Técnica:</strong> ${alt.tecnica || '—'}</div>
            <div><strong>Alvo Anatômico:</strong> ${alt.alvo || '—'}</div>
            <div><strong>Parâmetros:</strong> ${alt.parametros || '—'}</div>
            <div class="alt-clinical-notes">
              <strong>Observações Clínicas e Cuidados do Roadmap:</strong> ${alt.observacoes || 'Transição indicada conforme algoritmo sequencial original da Rede NAPeN.'}
            </div>
          </div>
        `;
      } else {
        altContent = `
          <div class="alternative-protocol-box">
            <div>Consulte o comitê clínico interdisciplinar para reestratificação diagnóstica.</div>
          </div>
        `;
      }

      branchResultPanel.innerHTML = `
        <div style="font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
          <span class="outcome-bullet status-danger"></span>
          [Resposta Insatisfatória — Transição para Protocolo Alternativo]
        </div>
        <div style="line-height: 1.55;">
          Paciente não atingiu o benefício terapêutico mínimo na escala recomendada após o ciclo de indução (sem melhora quantitativa ou qualitativa).
          Seguindo o algoritmo clínico sequencial oficial da Rede NAPeN:
        </div>
        ${altContent}
        <div style="margin-top: 12px; font-size: 0.84rem; color: #7F1D1D; background: rgba(239, 68, 68, 0.08); padding: 10px 14px; border-radius: var(--radius-sm); border: 1px dashed #FCA5A5; line-height: 1.5;">
          <strong>Critério de Falha Terapêutica dos Roadmaps NAPeN:</strong> Configura-se quando o paciente não apresenta nenhum tipo de resposta mesmo após os protocolos alternativos do roadmap. Nesses casos, encerra-se a rota atual de estimulação e encaminha-se para reavaliação clínica e equipe interdisciplinar.
        </div>
      `;
    }
  }

  // Interação manual com os botões de desfecho
  if (btnOutcomeSuccess) {
    btnOutcomeSuccess.addEventListener('click', () => {
      engine.toggleOutcome('success');
      updateOutcomeDisplay();
    });
  }

  if (btnOutcomeDanger) {
    btnOutcomeDanger.addEventListener('click', () => {
      engine.toggleOutcome('danger');
      updateOutcomeDisplay();
    });
  }

  // ==========================================================================
  // 7. Calculadora Dual & Automatismo de Seleção de Desfecho
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

    if (!res.isSuccess) {
      if (calcDeltaPoints) calcDeltaPoints.textContent = 'Δ = —';
      if (calcDeltaPercent) calcDeltaPercent.textContent = '— %';
      if (calcMcidBadge) {
        calcMcidBadge.textContent = 'Aguardando dados';
        calcMcidBadge.className = 'calc-metric-val calc-mcid-status';
      }
      if (cardDeltaPoints) cardDeltaPoints.className = 'calc-metric-card';
      if (cardDeltaPercent) cardDeltaPercent.className = 'calc-metric-card';
      if (cardMcidBadge) cardMcidBadge.className = 'calc-metric-card';

      if (calcGoalFeedback) {
        calcGoalFeedback.textContent = `Meta do protocolo: ${activeScale?.meta_texto || m?.meta_melhora || 'Insira os escores para verificar o desfecho.'}`;
      }
      if (calcComparisonFeedback) {
        calcComparisonFeedback.textContent = 'Ao informar os escores, o sistema analisará se o ganho clínico individual é compatível com o intervalo de confiança dos estudos de referência e se superou a MCID da escala.';
      }
      return;
    }

    // Atualização dos 3 Cards de Métricas Individuais
    if (calcDeltaPoints) calcDeltaPoints.textContent = res.deltaPointsFormatted || `Δ = ${res.delta}`;
    if (calcDeltaPercent) calcDeltaPercent.textContent = res.percentFormatted || `${res.percent}%`;
    
    if (calcMcidBadge) {
      if (res.mcidMet) {
        calcMcidBadge.textContent = 'MCID Atingida';
      } else if (res.isImproved) {
        calcMcidBadge.textContent = 'Abaixo da MCID';
      } else {
        calcMcidBadge.textContent = 'Não Atingida';
      }
    }

    const statusClass = res.outcomeRecommended === 'success' ? 'success' : 'danger';
    if (cardDeltaPoints) cardDeltaPoints.className = `calc-metric-card ${statusClass}`;
    if (cardDeltaPercent) cardDeltaPercent.className = `calc-metric-card ${statusClass}`;
    if (cardMcidBadge) cardMcidBadge.className = `calc-metric-card ${statusClass}`;

    // Automatismo: Seleciona e abre automaticamente o desfecho clínico
    engine.setOutcome(res.outcomeRecommended);
    updateOutcomeDisplay();

    // Feedback Clínico e Conduta Oficial dos Roadmaps da Rede NAPeN
    if (calcGoalFeedback) {
      if (res.outcomeRecommended === 'success') {
        calcGoalFeedback.innerHTML = `<strong>[Meta Terapêutica Alcançada (≥ MCID)]</strong> O paciente atingiu ou superou o limiar de relevância clínica da escala (${res.mcidLabel || activeScale?.meta_texto || m?.meta_melhora}). Conduta oficial de consolidação e manutenção periódica ativada automaticamente abaixo.`;
      } else {
        calcGoalFeedback.innerHTML = `<strong>[Resposta Insatisfatória (< MCID)]</strong> A evolução clínica na escala permaneceu aquém da meta do protocolo (${res.mcidLabel || activeScale?.meta_texto || m?.meta_melhora}). Transição para o Protocolo Alternativo da árvore sequencial ativada automaticamente abaixo.`;
      }
    }

    // Diagnóstico Comparativo Dinâmico com Ensaio Clínico de Referência
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
    if (str.includes('fugl') || str.includes('fma')) return 'fma_ue';
    if (str.includes('berg') || str.includes('bbs')) return 'bbs';
    if (str.includes('sara')) return 'sara';
    if (str.includes('hamd') || str.includes('ham-d') || str.includes('hdrs') || str.includes('madrs')) return 'ham_d';
    if (str.includes('hama') || str.includes('ham-a')) return 'ham_a';
    if (str.includes('pcl') || str.includes('tept')) return 'pcl_5';
    if (str.includes('eva') || str.includes('vas')) return 'eva';
    if (str.includes('dn4')) return 'dn4';
    if (str.includes('tug') || str.includes('timed up')) return 'tug';
    if (str.includes('fog') || str.includes('freezing')) return 'fogq';
    if (str.includes('updrs') || str.includes('mds')) return 'updrs_iii';
    if (str.includes('meem') || str.includes('mmse') || str.includes('mental')) return 'meem';
    if (str.includes('adas')) return 'adas_cog';
    if (str.includes('boston') || str.includes('bnt')) return 'bnt';
    if (str.includes('wab')) return 'wab_r';
    if (str.includes('fois') || str.includes('doss') || str.includes('fedss')) return 'fois';
    if (str.includes('gmfm')) return 'gmfm';
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
    if (scaleGuideDominio) scaleGuideDominio.textContent = scale.dominio;
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
      scaleGuideDoiLink.href = scale.link_artigo || '#';
      scaleGuideDoiLink.textContent = `Acessar Artigo Original (${scale.doi ? 'DOI: ' + scale.doi : 'Link Oficial'}) ↗`;
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
      const scaleToOpen = activeScale?.sigla || activeScale?.id || activeMod?.escala_recomendada;
      openScaleGuide(scaleToOpen);
    });
  }

  if (btnOpenScaleGuideCalc) {
    btnOpenScaleGuideCalc.addEventListener('click', () => {
      const activeScale = engine.getActiveScale();
      const activeMod = engine.getActiveModality();
      const scaleToOpen = activeScale?.sigla || activeScale?.id || activeMod?.escala_recomendada;
      openScaleGuide(scaleToOpen);
    });
  }

  const btnOpenScaleGuidePresc = document.getElementById('btnOpenScaleGuidePresc');
  if (btnOpenScaleGuidePresc) {
    btnOpenScaleGuidePresc.addEventListener('click', () => {
      const activeScale = engine.getActiveScale();
      const activeMod = engine.getActiveModality();
      const scaleToOpen = activeScale?.sigla || activeScale?.id || activeMod?.escala_recomendada;
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
            ${matchReason ? `<div class="search-res-match-tag">🎯 ${matchReason}</div>` : ''}
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
  // 9. Matriz de Protocolos e Parâmetros (Tabela)
  // ==========================================================================
  function renderPocketTable() {
    if (!pocketTableBody) return;
    pocketTableBody.innerHTML = '';

    data.condicoes.forEach(c => {
      const factors = c.fatores_limitantes || [];
      factors.forEach(f => {
        const m = c.modalidades ? c.modalidades[f.id] : null;
        if (!m) return;

        const ensaio = m.ensaio_clinico || m.artigo_referencia;
        const meta = m.meta_analise;

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <strong style="color: var(--napen-navy);">${c.condicao}</strong>
            <div style="font-size: 0.75rem; color: var(--text-faint);">${c.eixo}</div>
          </td>
          <td><span style="background: var(--napen-teal-soft); color: var(--napen-teal-dark); padding: 3px 8px; border-radius: 4px; font-weight: 600; font-size: 0.78rem;">${f.label}</span></td>
          <td><strong>${m.tecnica || '—'}</strong></td>
          <td>${m.alvo || '—'}</td>
          <td>
            <div>${m.frequencia || '—'}</div>
            <div style="font-size: 0.78rem; color: var(--text-muted);">${m.intensidade || '—'}</div>
          </td>
          <td>
            <div>${m.pulsos_duracao || '—'}</div>
            <div style="font-size: 0.78rem; color: var(--text-muted);">${m.sessoes || '—'}</div>
          </td>
          <td><span class="scale-badge-pill" style="font-size: 0.75rem;">${m.escala_recomendada || '—'}</span></td>
          <td>
            <span style="font-weight: 700; color: var(--napen-teal-dark); font-size: 0.8rem;">
              ${m.diretriz_internacional || 'Recomendação Consensual NAPeN'}
            </span>
          </td>
          <td>
            <div style="display: flex; flex-direction: column; gap: 6px; min-width: 175px;">
              ${ensaio ? `
                <div style="font-size: 0.78rem;">
                  <span style="font-weight: 700; color: var(--napen-navy); display: block; font-size: 0.70rem; text-transform: uppercase; letter-spacing: 0.03em;">Estudos de referência:</span>
                  ${ensaio.url_doi ? `
                    <a href="${ensaio.url_doi}" target="_blank" rel="noopener noreferrer" style="color: var(--napen-teal-dark); font-weight: 600; text-decoration: underline; font-size: 0.78rem;" title="${ensaio.titulo || ''}">
                      ${ensaio.autores} (${ensaio.ano}) ↗
                    </a>
                  ` : `<span style="color: var(--text-muted); font-size: 0.75rem;">${ensaio.autores || '—'}</span>`}
                </div>
              ` : '<span style="color: var(--text-faint); font-size: 0.75rem;">—</span>'}
              ${meta ? `
                <div style="font-size: 0.78rem; border-top: 1px dashed var(--border-subtle); padding-top: 4px;">
                  <span style="font-weight: 700; color: var(--text-muted); display: block; font-size: 0.70rem; text-transform: uppercase; letter-spacing: 0.03em;">Metanálise de Suporte:</span>
                  ${meta.url_doi ? `
                    <a href="${meta.url_doi}" target="_blank" rel="noopener noreferrer" style="color: var(--text-muted); font-weight: 600; text-decoration: underline; font-size: 0.78rem;" title="${meta.titulo || ''}">
                      ${meta.autores} (${meta.ano}) ↗
                    </a>
                  ` : `<span style="color: var(--text-muted); font-size: 0.75rem;">${meta.autores || '—'}</span>`}
                </div>
              ` : ''}
            </div>
          </td>
        `;
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
    if (navItemCalc) navItemCalc.classList.toggle('active', false);
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
      closeCalcDropdown();
      switchTab('prescription');
      toggleDropdown();
    });
  }

  if (tabBtnCalc) {
    tabBtnCalc.addEventListener('click', (e) => {
      e.stopPropagation();
      closeDropdown();
      toggleCalcDropdown();
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
      closeCalcDropdown();
      openDropdown();
    });
    navItemPrescription.addEventListener('mouseleave', () => {
      closeDropdown();
    });
  }

  // Hover suave no desktop para o menu da Calculadora de Resposta Clínica
  if (navItemCalc) {
    navItemCalc.addEventListener('mouseenter', () => {
      closeDropdown();
      openCalcDropdown();
    });
    navItemCalc.addEventListener('mouseleave', () => {
      closeCalcDropdown();
    });
  }

  // Fechar dropdowns ao clicar fora ou teclar ESC
  document.addEventListener('click', (e) => {
    if (navItemPrescription && !navItemPrescription.contains(e.target)) {
      closeDropdown();
    }
    if (navItemCalc && !navItemCalc.contains(e.target)) {
      closeCalcDropdown();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllDropdowns();
    }
  });

  // Inicialização
  populateDropdownMenu();
  populateCalcDropdown();
  renderPocketTable();
});
