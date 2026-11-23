/**
 * Rede NAPeN — Motor de Prescrição Clínica e Árvore de Decisão
 * Gerencia a lógica de Fator Limitante, parâmetros de indução, diretrizes internacionais ABNT,
 * seleção de múltiplas escalas clínicas (ex: BBS e SARA), modo EAM (0, 1, 1+, 2, 3, 4),
 * cálculo automatizado de resposta e ativação de protocolos alternativos.
 */

class DecisionEngine {
  constructor(data) {
    this.data = data;
    this.activeConditionId = null;
    this.activeModalityType = 'rtms'; // 'rtms' | 'tdcs'
    this.pathChoices = {}; // { [etapaId]: optionId }
    this.primaryFactorId = null; // Fator limitante principal (sintoma clínico inicial)
    this.activeFactorId = null; // Chave de prescrição resolvida no percurso da árvore
    this.activeScaleId = null;
    this.activeOutcome = null; // 'success' | 'warning' | 'danger' | null
    this.entryMode = 'new'; // 'new' | 'returning'
    this.continuingStage = 'primary'; // 'primary' | 'evaluation' | 'alt1' | 'alt2' | 'failure'
    this.activeCalcStage = 'primary'; // 'primary' | 'alt1' | 'alt2' | ... (protocolo avaliado na calculadora)
    this.tolerabilityStatus = 'boa'; // 'boa' | 'leve' | 'intolerante' | 'grave'
  }

  getCondition(conditionId) {
    return this.data.condicoes.find(c => c.id === conditionId);
  }

  setCondition(conditionId, options = {}) {
    this.activeConditionId = conditionId;
    const cond = this.getCondition(conditionId);
    const supported = (cond && cond.modalidades_suportadas) || [];
    const requestedMod = options.modalityType;
    const trees = (cond && cond.arvore_algoritmo) || {};
    let resolvedMod = requestedMod && (trees[requestedMod] || supported.some(m => m.id === requestedMod))
      ? requestedMod
      : (supported[0]?.id || Object.keys(trees)[0] || 'rtms');

    this.activeModalityType = resolvedMod;
    this.pathChoices = {};
    this.entryMode = options.preserveEntryMode
      ? (options.entryMode || this.entryMode || 'new')
      : (options.entryMode || 'new');
    this.continuingStage = this.entryMode === 'returning'
      ? (options.continuingStage || 'evaluation')
      : 'primary';
    this.activeCalcStage = /^alt\d+$/.test(this.continuingStage) ? this.continuingStage : 'primary';
    this.tolerabilityStatus = 'boa';

    if (cond && cond.fatores_limitantes && cond.fatores_limitantes.length > 0) {
      this.primaryFactorId = cond.fatores_limitantes[0].id;
      this.activeFactorId = cond.fatores_limitantes[0].id;
    } else {
      this.primaryFactorId = null;
      this.activeFactorId = null;
    }
    this.activeScaleId = null;
    this.activeOutcome = null;

    const tree = this.getActiveTree();
    if (tree && tree.etapas && tree.etapas.length > 0) {
      const firstEtapa = tree.etapas[0];
      if (firstEtapa.opcoes && firstEtapa.opcoes.length > 0) {
        this.setPathChoice(firstEtapa.etapa_id, firstEtapa.opcoes[0].id);
      }
    }
  }

  setModalityType(type) {
    const cond = this.getCondition(this.activeConditionId);
    const trees = (cond && cond.arvore_algoritmo) || {};
    const supported = (cond && cond.modalidades_suportadas) || [];
    this.activeModalityType = trees[type]
      ? type
      : (supported[0]?.id || Object.keys(trees)[0] || type);
    this.pathChoices = {};
    this.activeScaleId = null;
    this.activeOutcome = null;
    this.activeCalcStage = 'primary';
    const tree = this.getActiveTree();
    if (tree && tree.etapas && tree.etapas.length > 0) {
      const firstEtapa = tree.etapas[0];
      if (firstEtapa.opcoes && firstEtapa.opcoes.length > 0) {
        this.setPathChoice(firstEtapa.etapa_id, firstEtapa.opcoes[0].id);
      }
    }
  }

  getActiveTree() {
    if (!this.activeConditionId) return null;
    const cond = this.getCondition(this.activeConditionId);
    if (!cond || !cond.arvore_algoritmo) return null;
    if (cond.arvore_algoritmo[this.activeModalityType]) {
      return cond.arvore_algoritmo[this.activeModalityType];
    }
    const keys = Object.keys(cond.arvore_algoritmo);
    return keys.length > 0 ? cond.arvore_algoritmo[keys[0]] : null;
  }

  _reconcileTreePath(tree) {
    if (!tree || !Array.isArray(tree.etapas) || tree.etapas.length === 0) return;
    const stepMap = {};
    tree.etapas.forEach(s => {
      stepMap[s.etapa_id] = s;
    });

    const activeStepIds = new Set();
    const visited = new Set();
    let currStep = tree.etapas[0];

    while (currStep && !visited.has(currStep.etapa_id)) {
      visited.add(currStep.etapa_id);
      activeStepIds.add(currStep.etapa_id);
      const opts = currStep.opcoes || [];
      if (opts.length === 0) break;

      const curChoice = this.pathChoices[currStep.etapa_id];
      const chosenOpt = opts.find(o => o.id === curChoice) || opts[0];
      this.pathChoices[currStep.etapa_id] = chosenOpt.id;

      if (currStep.etapa_id === 'fator_limitante') {
        const directTarget = chosenOpt.modalidade_chave || chosenOpt.protocolo_alvo;
        this.primaryFactorId = directTarget || chosenOpt.id;
      }

      const targetLeaf = chosenOpt.modalidade_chave || chosenOpt.protocolo_alvo;
      if (targetLeaf) {
        this.activeFactorId = targetLeaf;
        break;
      }
      if (chosenOpt.proxima_etapa && stepMap[chosenOpt.proxima_etapa]) {
        currStep = stepMap[chosenOpt.proxima_etapa];
      } else {
        break;
      }
    }

    // Prune orphan choices from sibling branches
    Object.keys(this.pathChoices).forEach(sid => {
      if (!activeStepIds.has(sid)) {
        delete this.pathChoices[sid];
      }
    });
  }

  _findPathToTarget(tree, targetKey) {
    if (!tree || !Array.isArray(tree.etapas) || tree.etapas.length === 0) return null;
    const stepMap = {};
    tree.etapas.forEach(s => {
      stepMap[s.etapa_id] = s;
    });

    const dfs = (stepId, acc, visited) => {
      if (visited.has(stepId)) return null;
      const step = stepMap[stepId];
      if (!step) return null;
      visited.add(stepId);
      for (const opt of (step.opcoes || [])) {
        const nextAcc = { ...acc, [stepId]: opt.id };
        const leaf = opt.modalidade_chave || opt.protocolo_alvo;
        if (leaf === targetKey || (stepId === 'fator_limitante' && opt.id === targetKey && !leaf)) {
          return nextAcc;
        }
        if (opt.proxima_etapa) {
          const found = dfs(opt.proxima_etapa, nextAcc, new Set(visited));
          if (found) return found;
        }
      }
      return null;
    };

    return dfs(tree.etapas[0].etapa_id, {}, new Set());
  }

  setPathChoice(stepId, optionId) {
    this.pathChoices[stepId] = optionId;
    this.activeScaleId = null;
    this.activeOutcome = null;

    const tree = this.getActiveTree();
    if (tree) {
      this._reconcileTreePath(tree);
    }
  }

  getPathChoice(stepId) {
    return this.pathChoices[stepId] || null;
  }

  setFactor(factorId, isPrimary = true) {
    if (isPrimary) {
      this.primaryFactorId = factorId;
    }
    this.activeFactorId = factorId;
    this.activeScaleId = null;
    this.activeOutcome = null;

    const tree = this.getActiveTree();
    if (tree && Array.isArray(tree.etapas) && tree.etapas.length > 0) {
      const rootStep = tree.etapas[0];
      const rootOpt = (rootStep.opcoes || []).find(o => o.id === factorId || o.modalidade_chave === factorId);
      if (isPrimary && rootOpt) {
        this.pathChoices = { [rootStep.etapa_id]: rootOpt.id };
        this._reconcileTreePath(tree);
      } else {
        const path = this._findPathToTarget(tree, factorId);
        if (path) {
          this.pathChoices = path;
          this._reconcileTreePath(tree);
        }
      }
    }
  }

  getProtocolChain() {
    const m = this.getActiveModality();
    const chain = (m && Array.isArray(m.cadeia_sequencial)) ? m.cadeia_sequencial : [];
    return chain.map((step, idx) => ({
      ...step,
      ordem: step.ordem || (idx + 1),
      fase_etapa: idx === 0
        ? 'inicial'
        : ((step.fase_etapa === 'ajustes' || /ajustes/i.test(step.etapa_rotulo || '') || /ajustes/i.test(step.linha_fluxograma || '')) ? 'ajustes' : 'sequencia'),
      stageKey: idx === 0 ? 'primary' : `alt${idx}`
    }));
  }

  getContextualObservations(filter = {}) {
    const cond = this.getCondition(this.activeConditionId);
    const list = (cond && Array.isArray(cond.observacoes_contextuais)) ? cond.observacoes_contextuais : [];
    if (list.length === 0) return [];

    const m = this.getActiveModality();
    const modType = this.activeModalityType || 'rtms';
    const leafModType = (m && m.mod_tipo) || '';
    const activeProtId = filter.protocoloId || this.activeFactorId;
    const activeStage = filter.stage || 'primary';
    const rawTol = filter.tolerability || this.tolerabilityStatus || 'boa';
    const tolAliases = rawTol === 'leve'
      ? ['leve', 'desconforto_leve']
      : [rawTol];
    const selectedOptionValues = new Set(Object.values(this.pathChoices || {}));
    if (filter.optionId) selectedOptionValues.add(filter.optionId);

    return list.filter(obs => {
      if (filter.slot && obs.slot !== filter.slot) return false;
      const g = obs.gatilho || {};

      if (Array.isArray(g.modalidades_tipo) && g.modalidades_tipo.length > 0) {
        const modOk = g.modalidades_tipo.some(mt => mt === modType || mt === leafModType);
        if (!modOk) return false;
      }

      if (Array.isArray(g.protocolo_ids) && g.protocolo_ids.length > 0) {
        if (!activeProtId || !g.protocolo_ids.includes(activeProtId)) return false;
      }

      if (Array.isArray(g.etapa_ids) && g.etapa_ids.length > 0) {
        if (filter.etapaId) {
          if (!g.etapa_ids.includes(filter.etapaId)) return false;
        } else {
          const activeEtapaIds = Object.keys(this.pathChoices || {});
          if (!g.etapa_ids.some(eid => activeEtapaIds.includes(eid))) return false;
        }
      }

      if (Array.isArray(g.opcao_ids) && g.opcao_ids.length > 0) {
        const optOk = g.opcao_ids.some(oid => selectedOptionValues.has(oid));
        if (!optOk) return false;
      }

      if (Array.isArray(g.estagios) && g.estagios.length > 0) {
        if (!g.estagios.includes(activeStage)) return false;
      }

      if (Array.isArray(g.tolerabilidades) && g.tolerabilidades.length > 0) {
        if (!g.tolerabilidades.some(t => tolAliases.includes(t))) return false;
      }

      return true;
    });
  }

  setActiveScale(scaleId) {
    this.activeScaleId = scaleId;
  }

  getScalesForCurrentPath() {
    const m = this.getActiveModality();
    if (!m || !Array.isArray(m.escalas_detalhadas) || m.escalas_detalhadas.length === 0) return [];
    const all = m.escalas_detalhadas;
    const map = m.escalas_por_fator;
    const rootChoice = this.pathChoices?.fator_limitante || this.getPathChoice('fator_limitante');
    const factorIds = [rootChoice, this.primaryFactorId, this.activeFactorId].filter(Boolean);
    if (map && typeof map === 'object') {
      for (const fid of factorIds) {
        const allowed = map[fid];
        if (Array.isArray(allowed) && allowed.length > 0) {
          const filtered = all.filter(s => allowed.includes(s.id));
          if (filtered.length > 0) return filtered;
        }
      }
    }
    const pf = rootChoice || this.primaryFactorId || '';
    if (pf === 'perda_sinergia') {
      const fmaOnly = all.filter(s => s.id !== 'eam' && !/ashworth|\beam\b/i.test(s.nome || ''));
      if (fmaOnly.length > 0) return fmaOnly;
    } else if (pf === 'espasticidade') {
      const eamOnly = all.filter(s => s.id === 'eam' || /ashworth|\beam\b/i.test(s.nome || ''));
      if (eamOnly.length > 0) return eamOnly;
    } else if (pf === 'dor') {
      const dorOnly = all.filter(s => s.id === 'eva' || /\beva\b|\bvas\b|\bdor\b/i.test(s.nome || ''));
      if (dorOnly.length > 0) return dorOnly;
    }
    return all;
  }

  getActiveScale() {
    const allowedScales = this.getScalesForCurrentPath();
    if (allowedScales.length === 0) return null;
    if (this.activeScaleId) {
      const found = allowedScales.find(s => s.id === this.activeScaleId);
      if (found) return found;
    }
    return allowedScales[0];
  }

  setOutcome(outcomeType) {
    this.activeOutcome = outcomeType;
  }

  toggleOutcome(outcomeType) {
    if (this.activeOutcome === outcomeType) {
      this.activeOutcome = null;
    } else {
      this.activeOutcome = outcomeType;
    }
  }

  getActiveModality() {
    if (!this.activeConditionId) return null;
    const cond = this.getCondition(this.activeConditionId);
    if (!cond || !cond.modalidades) return null;

    if (this.activeFactorId && cond.modalidades[this.activeFactorId]) {
      return cond.modalidades[this.activeFactorId];
    }

    if (this.primaryFactorId && cond.modalidades[this.primaryFactorId]) {
      return cond.modalidades[this.primaryFactorId];
    }

    const firstKey = Object.keys(cond.modalidades)[0];
    return cond.modalidades[firstKey] || null;
  }

  getFormattedGuideline() {
    const m = this.getActiveModality();
    if (!m) {
      return {
        text: 'Recomendação Consensual NAPeN',
        recomendacao: 'Consenso NAPeN',
        autores: null,
        ano: null,
        doi: null,
        url: null,
        isIfcnLefaucheur: false,
        fonteTipo: 'Consenso Clínico NAPeN'
      };
    }

    const rec = m.diretriz_internacional || 'Consenso Clínico Internacional';
    const isIfcnLefaucheur = /lefaucheur|ifcn/i.test(rec);
    const meta = m.meta_analise;
    const ref = isIfcnLefaucheur
      ? (m.diretriz_ref || null)
      : (meta && meta.url_doi ? meta : null);

    if (ref && ref.url_doi) {
      return {
        text: `${rec} — ${ref.autores || 'Referência'} (${ref.ano || ''})`,
        recomendacao: rec,
        autores: ref.autores || (isIfcnLefaucheur ? 'Lefaucheur et al. (IFCN)' : null),
        ano: ref.ano || null,
        doi: ref.doi || null,
        url: ref.url_doi,
        citacao: ref.citacao_completa || null,
        isIfcnLefaucheur,
        fonteTipo: isIfcnLefaucheur
          ? 'Diretriz Internacional IFCN (Lefaucheur et al.)'
          : 'Revisão Sistemática / Síntese Clínica para o Desfecho (sem gradação IFCN direta)'
      };
    }

    return {
      text: rec,
      recomendacao: rec,
      autores: null,
      ano: null,
      doi: null,
      url: null,
      isIfcnLefaucheur,
      fonteTipo: isIfcnLefaucheur
        ? 'Diretriz Internacional IFCN (Lefaucheur et al.)'
        : 'Evidência Clínica Exploratória / Síntese para o Desfecho'
    };
  }

  setActiveCalcStage(stage) {
    const str = String(stage || 'primary');
    if (str === 'primary' || /^alt\d+$/.test(str)) {
      this.activeCalcStage = str;
    } else {
      this.activeCalcStage = 'primary';
    }
  }

  getCalculatorStageContext(stageKey = null) {
    const chain = this.getProtocolChain();
    const rawStage = stageKey || this.activeCalcStage || 'primary';
    const normalized = rawStage === 'evaluation' || rawStage === 'failure' ? 'primary' : rawStage;
    const step = chain.find(s => s.stageKey === normalized) || chain[0] || null;
    return {
      stageKey: step?.stageKey || 'primary',
      step,
      calcMeta: (step && step.calc_meta) ? step.calc_meta : null
    };
  }

  calculateDelta(valBaseRaw, valPostRaw, scaleObj = null, modality = null, stageKey = null) {
    const scale = scaleObj || this.getActiveScale();
    const m = modality || this.getActiveModality();
    const stageCtx = this.getCalculatorStageContext(stageKey);
    const cm = stageCtx?.calcMeta || null;

    // 1. Caso especial: Escala de Ashworth Modificada (EAM) com graus 0, 1, 1+, 2, 3, 4
    if (scale && scale.tipo === 'ordinal_eam') {
      if (valBaseRaw === null || valBaseRaw === undefined || valBaseRaw === '' ||
          valPostRaw === null || valPostRaw === undefined || valPostRaw === '') {
        return { text: 'Selecione os graus inicial e pós-tratamento', isSuccess: false };
      }

      const eamMap = { '0': 0, '1': 1, '1+': 1.5, '2': 2, '3': 3, '4': 4 };
      const strBase = String(valBaseRaw).trim();
      const strPost = String(valPostRaw).trim();

      if (!(strBase in eamMap) || !(strPost in eamMap)) {
        return { text: 'Grau da EAM inválido', isSuccess: false };
      }

      const numBase = eamMap[strBase];
      const numPost = eamMap[strPost];

      const deltaLevels = numPost - numBase;
      const isImproved = deltaLevels < 0;

      let percent = 0;
      if (numBase > 0) {
        percent = ((numBase - numPost) / numBase) * 100;
      }
      percent = Math.max(0, Math.min(100, percent));

      const deltaPointsFormatted = deltaLevels === 0 ? 'Δ = 0 níveis' : (deltaLevels < 0 ? `Δ = ${deltaLevels} níveis` : `Δ = +${deltaLevels} níveis`);
      const percentFormatted = `${isImproved ? '-' : '+'}${percent.toFixed(1)}% de tônus`;

      const deltaText = deltaLevels === 0
        ? 'Δ = 0 níveis (Tônus inalterado)'
        : deltaLevels < 0
          ? `Δ = ${deltaLevels} níveis (Redução de ${percent.toFixed(1)}%)`
          : `Δ = +${deltaLevels} níveis (Aumento de tônus / Piora)`;

      const goalMet = deltaLevels <= -1; // Meta formal e MCID dos roadmaps: redução ≥ 1 nível
      const mcidMet = goalMet;
      const outcomeRecommended = goalMet ? 'success' : 'danger';

      const eff = m?.efeito_clinico || {};
      const estudo = cm?.estudo_referencia || eff.estudo_referencia || 'o ensaio clínico de referência do protocolo';
      const esperado = cm?.efeito_esperado_resumo || eff.efeito_esperado_resumo || m?.tamanho_efeito || 'Diminuição de 1 nível na EAM';

      let comparativeFeedback = '';
      if (outcomeRecommended === 'success') {
        comparativeFeedback = `<strong>[Resposta Clínica Satisfatória Alcançada]</strong> A redução de ${Math.abs(deltaLevels)} nível(is) no tônus muscular atingiu a MCID da escala (redução ≥ 1 grau) em concordância com o ensaio clínico de referência do protocolo (${estudo}). <strong>Conduta Oficial NAPeN:</strong> Manter protocolo para consolidação motora e transição para manutenção periódica.`;
      } else {
        comparativeFeedback = `<strong>[Resposta Clínica Insatisfatória (< MCID)]</strong> A variação de tônus permaneceu aquém da MCID da escala (redução ≥ 1 grau na EAM). <strong>Conduta Oficial NAPeN:</strong> Avançar para o próximo protocolo da sequência clínica no Assistente de Resposta Pós-Indução. Se persistir sem resposta após os protocolos seguintes e ajustes, caracteriza-se Falha Terapêutica.`;
      }

      return {
        text: deltaText,
        isSuccess: true,
        delta: deltaLevels,
        deltaPointsFormatted,
        percent: parseFloat(percent.toFixed(1)),
        percentFormatted,
        isImproved,
        goalMet,
        mcidMet,
        mcidLabel: 'Redução ≥ 1 grau na EAM',
        outcomeRecommended,
        isOrdinal: true,
        gradeFrom: strBase,
        gradeTo: strPost,
        stageKey: stageCtx.stageKey,
        studyRef: estudo,
        expectedSummary: esperado,
        comparativeFeedback
      };
    }

    // 2. Escala Contínua
    const valBase = parseFloat(valBaseRaw);
    const valPost = parseFloat(valPostRaw);

    if (isNaN(valBase) || isNaN(valPost)) {
      return { text: 'Informe ambos os valores', isSuccess: false };
    }

    const delta = valPost - valBase;
    const meta = cm?.meta_texto || scale?.meta_texto || m?.meta_melhora || '';
    const isReduction = scale ? scale.direcao_melhora === 'reducao' : (/redução|queda|diminuição|alívio/i.test(meta));

    const isImproved = isReduction ? delta < 0 : delta > 0;
    let percentChange = 0;
    if (valBase !== 0) {
      percentChange = isReduction
        ? ((valBase - valPost) / Math.abs(valBase)) * 100
        : ((valPost - valBase) / Math.abs(valBase)) * 100;
    }

    const sign = delta > 0 ? '+' : '';
    const deltaPointsFormatted = `Δ = ${sign}${delta.toFixed(1)} pts`;
    const percentFormatted = `${percentChange >= 0 ? '+' : ''}${percentChange.toFixed(1)}%`;

    let textDisplay = '';
    if (isReduction && valPost === 0 && valBase > 0) {
      textDisplay = `Δ = ${delta.toFixed(1)} pts (Remissão clínica completa — Escore 0)`;
    } else {
      textDisplay = `Δ = ${sign}${delta.toFixed(1)} pts (${percentFormatted})`;
    }

    // Avaliação de MCID / Limiar do estudo (sensível ao protocolo da sequência em uso)
    const eff = m?.efeito_clinico || {};
    const mcidVal = cm?.mcid_valor ?? scale?.mcid_valor ?? eff.mcid_valor ?? m?.mcid_valor ?? ((scale?.id === 'fma_ue' || scale?.id === 'fma-ue' || /fma/i.test(scale?.nome || '')) ? 5.0 : 30.0);
    const mcidLabel = cm?.mcid_label || scale?.mcid_label || eff.mcid_label || m?.mcid_label || `Meta clínica: ${meta}`;
    const isPercentMcid = (cm && typeof cm.is_percent === 'boolean')
      ? cm.is_percent
      : (/%/.test(mcidLabel) && !/IC\s*95%|ponto|pt|estrela/i.test(mcidLabel)) || (!/ponto|pt|estrela|grau|seg|s\b|m\/s/i.test(mcidLabel) && (mcidVal === 30.0 || mcidVal === 50.0));

    let mcidMet = false;
    const changeMagnitude = Math.abs(delta);
    
    // Se o corte for percentual (ex: 30%, 37%, 50%)
    if (isPercentMcid) {
      mcidMet = isImproved && percentChange >= mcidVal;
    } else {
      // Se for em pontos absolutos (ex: 5.0 FMA-UE, 8.0 / 13.0 Cancelamento de Estrelas)
      mcidMet = isImproved && changeMagnitude >= mcidVal;
    }

    // Compatibilidade com Intervalo de Confiança do Estudo (IC 95%)
    const icMin = cm?.ic_min ?? eff.ic_min;
    const icMax = cm?.ic_max ?? eff.ic_max;
    let withinCI = false;
    if (icMin !== undefined && icMax !== undefined && icMin !== null && icMax !== null) {
      const metricToCheck = isPercentMcid ? percentChange : changeMagnitude;
      withinCI = isImproved && metricToCheck >= icMin && metricToCheck <= icMax;
    }

    let goalMet = mcidMet;
    if (!goalMet && !cm) {
      if (/30%/i.test(meta)) goalMet = isImproved && percentChange >= 30;
      else if (/50%/i.test(meta)) goalMet = isImproved && percentChange >= 50;
      else if (/5[,.]0/i.test(meta) && /fma|bbs/i.test(`${scale?.id || ''} ${scale?.nome || ''}`)) goalMet = isImproved && changeMagnitude >= 5.0;
      else if (scale?.mcid_valor == null && eff.mcid_valor == null && isImproved && percentChange >= 25) goalMet = true;
    }

    const outcomeRecommended = goalMet ? 'success' : 'danger';

    const stageStep = stageCtx?.step || null;
    const estudo = cm?.estudo_referencia
      || (stageStep && stageStep.stageKey !== 'primary' && stageStep.referencia ? stageStep.referencia.split('·')[0].trim() : null)
      || eff.estudo_referencia
      || m?.ensaio_clinico?.autores
      || 'o ensaio clínico de referência do protocolo';
    const esperadoResumo = cm?.efeito_esperado_resumo
      || (stageStep && stageStep.stageKey !== 'primary' && stageStep.efeito_esperado ? stageStep.efeito_esperado : null)
      || eff.efeito_esperado_resumo
      || m?.tamanho_efeito
      || 'efeito clinicamente relevante';

    let comparativeFeedback = '';
    if (outcomeRecommended === 'success') {
      const ciSuffix = (icMin != null && icMax != null)
        ? ` (compatível com o IC 95% de ${icMin} a ${icMax} do protocolo em uso)`
        : '';
      comparativeFeedback = `<strong>[Resposta Clínica Satisfatória Alcançada]</strong> O ganho individual de <strong>${sign}${changeMagnitude.toFixed(1)} pontos (${percentFormatted})</strong> atingiu o critério clínico esperado (${mcidLabel})${ciSuffix}, alinhado ao estudo de referência (<em>${estudo}</em>: ${esperadoResumo}). <strong>Conduta Oficial NAPeN:</strong> Prosseguir para consolidação e manutenção periódica com redução gradual das sessões.`;
    } else {
      comparativeFeedback = `<strong>[Resposta Clínica Insatisfatória]</strong> A variação individual de <strong>${sign}${delta.toFixed(1)} pontos (${percentFormatted})</strong> não atingiu o limiar esperado para o protocolo em uso (${mcidLabel} · <em>${estudo}</em>). <strong>Conduta Oficial NAPeN:</strong> Avançar para o próximo protocolo da sequência clínica no Assistente de Resposta Pós-Indução. Caso persista sem melhora após os protocolos seguintes e ajustes, caracteriza-se Falha Terapêutica formal.`;
    }

    return {
      text: textDisplay,
      isSuccess: true,
      delta,
      deltaPointsFormatted,
      percent: parseFloat(percentChange.toFixed(1)),
      percentFormatted,
      isImproved,
      mcidMet,
      mcidLabel,
      withinCI,
      icMin: icMin ?? null,
      icMax: icMax ?? null,
      goalMet,
      outcomeRecommended,
      metaText: meta,
      stageKey: stageCtx.stageKey,
      studyRef: estudo,
      expectedSummary: esperadoResumo,
      comparativeFeedback
    };
  }

  /**
   * Alterna entre primeira indicação ('new') e paciente já em protocolo ('returning').
   */
  setEntryMode(mode, stage = null) {
    this.entryMode = mode === 'returning' ? 'returning' : 'new';
    if (this.entryMode === 'new') {
      this.continuingStage = 'primary';
      this.activeCalcStage = 'primary';
    } else {
      this.continuingStage = stage || (this.continuingStage === 'primary' ? 'evaluation' : this.continuingStage);
      this.activeCalcStage = /^alt\d+$/.test(this.continuingStage) ? this.continuingStage : 'primary';
    }
  }

  setContinuingStage(stage) {
    const str = String(stage || '');
    if (['primary', 'evaluation', 'failure'].includes(str) || /^alt\d+$/.test(str)) {
      this.continuingStage = str;
    } else {
      this.continuingStage = 'evaluation';
    }
    if (str === 'primary' || /^alt\d+$/.test(str)) {
      this.activeCalcStage = str;
    }
  }

  getNextStageFrom(stage = this.continuingStage) {
    const chain = this.getProtocolChain();
    if (!chain || chain.length === 0 || stage === 'failure') {
      return { nextStage: 'failure', nextStep: null, nextIndex: -1, isFailure: true };
    }
    const baseStage = stage === 'evaluation' ? 'primary' : (stage || 'primary');
    const idx = chain.findIndex(s => s.stageKey === baseStage);
    const currentIdx = idx >= 0 ? idx : 0;
    const nextIdx = currentIdx + 1;
    if (nextIdx < chain.length) {
      return {
        nextStage: chain[nextIdx].stageKey,
        nextStep: chain[nextIdx],
        nextIndex: nextIdx,
        isFailure: false
      };
    }
    return { nextStage: 'failure', nextStep: null, nextIndex: -1, isFailure: true };
  }

  setTolerabilityStatus(tol) {
    const valid = ['boa', 'leve', 'intolerante', 'grave'];
    this.tolerabilityStatus = valid.includes(tol) ? tol : 'boa';
  }

  /**
   * Retorna as recomendações clínicas específicas de tolerabilidade, dose e calibração dos protocolos NAPeN.
   */
  getTolerabilityGuidance() {
    const cond = this.getCondition(this.activeConditionId);
    const m = this.getActiveModality();
    const tree = this.getActiveTree();
    const tolMeta = (m && m.tolerabilidade_roadmap) || (cond && cond.tolerabilidade_roadmap) || {};
    const aj = (m && m.ajuste_parametros) || (tree && tree.ajuste_parametros) || {};
    const sa = (m && m.sessoes_ajuste) || {};
    const isTdcs = this.activeModalityType === 'tdcs' || (m?.modalidade_sigla || '').toUpperCase().includes('TDCS');

    const defaultSpecific = isTdcs
      ? 'Verificar hidratação adequada das esponjas e integridade cutânea antes da aplicação; adotar rampa de subida e descida de 10 a 30 segundos para conforto sensorial.'
      : 'Em caso de desconforto ou cefaleia local pela bobina, reduzir temporariamente a intensidade para 80% do LMR e progredir gradualmente até a meta prevista; monitorar sono, medicações (benzodiazepínicos/antiepilépticos) e jejum.';

    return {
      adverseBankUrl: 'https://www.neuromodulation-net.com/banco-efeitos-adversos-napen',
      tituloGuia: aj.titulo || 'Ajustes de Tolerabilidade, Dose e Calibração',
      orientacaoGeral: tolMeta.orientacao_tolerabilidade || aj.tolerabilidade || defaultSpecific,
      ajusteDoseSugerido: tolMeta.ajuste_seguranca || aj.tolerabilidade || defaultSpecific,
      dosePulsos: aj.dose_pulsos || sa.ajuste_dose || 'Seguir rigorosamente a faixa de pulsos, duração e espaçamento de sessões estabelecida no protocolo.',
      calibracaoLimiar: aj.calibracao_limiar || (isTdcs
        ? 'Ajustar rampa de subida/descida e área dos eletrodos conforme sensibilidade cutânea e faixa etária.'
        : 'Quando o LMR não for identificável em repouso, calibrar entre 70%–80% do LMA conforme critério clínico do protocolo.'),
      fatoresModuladores: tolMeta.fatores_moduladores || 'Avaliar qualidade do sono, alimentação prévia e medicações que modulam excitabilidade cortical.',
      criterioInsatisfatoria: sa.regra_interrupcao || sa.quando_reavaliar || 'Reavaliar na janela do protocolo; resposta clínica abaixo da MCID ou dos critérios individuais avança diretamente ao próximo protocolo.'
    };
  }

  /**
   * Retorna metadados estruturados de GRADE e AMSTAR 2 da modalidade/protocolo ativo.
   */
  getEvidenceQuality() {
    const m = this.getActiveModality();
    if (!m) {
      return { amstar2: null, grade: null, hasAuditData: false };
    }
    const metaRef = m.meta_analise || {};
    const amstar2 = metaRef.amstar2 || m.amstar2 || null;
    const grade = m.grade || null;
    return {
      amstar2,
      grade,
      hasAuditData: Boolean(amstar2 || grade)
    };
  }

  /**
   * Retorna os dados clínicos estruturados para o estágio em foco no fluxo de continuidade.
   */
  getPrescriptionForStage(stage) {
    const m = this.getActiveModality();
    const tree = this.getActiveTree();
    if (!m || stage === 'adjustment') return null;

    const AJUSTES_DOTTED_RATIONALE =
      'Protocolos com borda pontilhada e opções da Seção de Ajustes indicam condutas cujo nível de evidência científica ainda não foi validado por metanálises (base científica exploratória respaldada em ensaios clínicos individuais).';

    if (stage && stage.startsWith('alt')) {
      const chain = this.getProtocolChain();
      const matched = chain.find(s => s.stageKey === stage);
      if (matched) {
        const fase = matched.fase_etapa || 'sequencia';
        const linha = matched.linha_fluxograma || 'solida';
        const needsRationale = fase === 'ajustes' || linha === 'pontilhada';
        const badge = fase === 'ajustes'
          ? 'Seção de Ajustes — Opção Clínica'
          : (linha === 'pontilhada'
              ? 'Próximo Protocolo na Sequência (Linha Pontilhada)'
              : 'Próximo Protocolo na Sequência');
        return {
          stage,
          badge,
          faseEtapa: fase,
          ordem: matched.ordem,
          titulo: matched.nome || matched.etapa_rotulo || 'Próximo Protocolo na Sequência',
          tecnica: matched.tecnica || '—',
          alvo: matched.alvo || '—',
          parametros: `${matched.parametros || '—'}${matched.sessoes ? ` · ${matched.sessoes}` : ''}`,
          sessoes: matched.sessoes || '',
          linhaFluxograma: linha,
          motivoAjuste: needsRationale ? AJUSTES_DOTTED_RATIONALE : '',
          efeitoEsperado: matched.efeito_esperado || '',
          referencia: matched.referencia || '',
          observacoes: matched.observacoes || (fase === 'ajustes'
            ? 'Opção prevista na Seção de Ajustes após ausência de resposta aos protocolos principais da sequência.'
            : 'Próxima etapa prevista pelas setas do fluxograma diante de resposta clínica insatisfatória.'),
          referenciaPrimaria: `${m.tecnica || 'Protocolo Inicial'} (${m.alvo || '—'})`
        };
      }

      if (stage === 'alt1') {
        const alt1 = m.protocolo_alternativo || {};
        const fase1 = alt1.fase_etapa || 'sequencia';
        const linha1 = alt1.linha_fluxograma || 'solida';
        return {
          stage: 'alt1',
          badge: fase1 === 'ajustes' ? 'Seção de Ajustes — Opção Clínica' : 'Próximo Protocolo na Sequência',
          faseEtapa: fase1,
          titulo: alt1.nome || 'Próximo Protocolo na Sequência',
          tecnica: alt1.tecnica || '—',
          alvo: alt1.alvo || '—',
          parametros: alt1.parametros || '—',
          linhaFluxograma: linha1,
          motivoAjuste: (fase1 === 'ajustes' || linha1 === 'pontilhada') ? AJUSTES_DOTTED_RATIONALE : '',
          observacoes: alt1.observacoes || 'Transição sequencial indicada diante de ausência de resposta ou intolerância.',
          referenciaPrimaria: `${m.tecnica || 'Protocolo Inicial'} (${m.alvo || '—'})`
        };
      }

      if (stage === 'alt2') {
        const alt2 = (tree && tree.protocolo_alternativo_2) || m.protocolo_alternativo_2 || {};
        const fase2 = alt2.fase_etapa || 'ajustes';
        const linha2 = alt2.linha_fluxograma || 'solida';
        return {
          stage: 'alt2',
          badge: 'Seção de Ajustes — Opção Clínica',
          faseEtapa: fase2,
          titulo: alt2.nome || 'Seção de Ajustes',
          tecnica: alt2.tecnica || '—',
          alvo: alt2.alvo || '—',
          parametros: alt2.parametros || '—',
          linhaFluxograma: linha2,
          motivoAjuste: (fase2 === 'ajustes' || linha2 === 'pontilhada') ? AJUSTES_DOTTED_RATIONALE : '',
          observacoes: alt2.observacoes || 'Etapa de ajustes prévia à caracterização de falha terapêutica formal.',
          referenciaPrimaria: `${m.tecnica || 'Protocolo Inicial'} (${m.alvo || '—'})`
        };
      }
    }

    if (stage === 'failure') {
      const falha = (tree && tree.falha_terapeutica) || m.falha_terapeutica || {};
      return {
        stage: 'failure',
        badge: 'Falha Terapêutica Formal',
        faseEtapa: 'falha',
        titulo: falha.titulo || 'Critérios e Condutas na Falha Terapêutica Formal (Rede NAPeN)',
        criterio: falha.criterios_definicao || falha.criterio || 'Persistência de resposta clínica inferior à MCID após indução completa e conclusão da sequência e ajustes.',
        condutas: Array.isArray(falha.condutas)
          ? falha.condutas
          : String(falha.conduta_oficial || '1. Encerramento formal do ciclo vigente;\n2. Investigação de fatores de resistência;\n3. Encaminhamento interdisciplinar.').split('\n'),
        referenciaPrimaria: `${m.tecnica || 'Protocolo Inicial'} (${m.alvo || '—'})`
      };
    }

    const primaryLinha = m.linha_fluxograma || 'solida';
    return {
      stage: 'primary',
      badge: 'Protocolo Inicial Indicado',
      faseEtapa: 'inicial',
      titulo: m.tecnica || 'Prescrição Terapêutica Inicial',
      tecnica: m.tecnica,
      alvo: m.alvo,
      frequencia: m.frequencia,
      intensidade: m.intensidade,
      pulsos_duracao: m.pulsos_duracao,
      sessoes: m.sessoes,
      linhaFluxograma: primaryLinha,
      motivoAjuste: primaryLinha === 'pontilhada' ? AJUSTES_DOTTED_RATIONALE : ''
    };
  }

  /**
   * Matriz multidimensional de decisão clínica pós-indução:
   * integra variação quantitativa da escala (MCID), critérios individuais da condição e tolerabilidade.
   * Sem resposta satisfatória pelos parâmetros individuais -> avança diretamente para o próximo protocolo da cadeia.
   */
  evaluateClinicalResponse(deltaResult = null, tolerabilityStatus = null) {
    const tol = tolerabilityStatus || this.tolerabilityStatus || 'boa';
    const guidance = this.getTolerabilityGuidance();
    const hasScores = Boolean(deltaResult && deltaResult.isSuccess);
    const activeMod = this.getActiveModality();
    const reevalObs = this.getContextualObservations({ slot: 'reeval' });
    const reevalRuleText = reevalObs.length > 0
      ? reevalObs[0].texto
      : (activeMod?.sessoes_ajuste?.quando_reavaliar || '');

    const evalBaseStage = deltaResult?.stageKey || (this.activeCalcStage && this.activeCalcStage !== 'primary' ? this.activeCalcStage : this.continuingStage);
    const { nextStage: nextProtocolStage, nextStep, isFailure } = this.getNextStageFrom(evalBaseStage);
    const nextProtocolLabel = nextStep
      ? (nextStep.nome || nextStep.etapa_rotulo || 'Próximo Protocolo na Sequência')
      : 'Falha Terapêutica Formal';

    // 1. Evento adverso grave ou contraindicação superveniente sobrepõe qualquer pontuação
    if (tol === 'grave') {
      return {
        recommendationType: 'adverse_halt',
        outcomeButton: 'danger',
        recommendedStage: 'failure',
        needsAdverseReport: true,
        adverseBankUrl: guidance.adverseBankUrl,
        badgeLabel: 'Suspensão Imediata & Registro de Evento Adverso',
        summaryHtml: `<strong>[Alerta de Segurança Clínica — Suspensão Recomendada]</strong> A ocorrência de evento adverso grave ou contraindicação superveniente sobrepõe-se à pontuação numérica da escala. <strong>Conduta Imediata NAPeN:</strong> Suspender imediatamente a aplicação vigente, realizar avaliação médica/neurológica presencial e registrar o evento no Banco de Efeitos Adversos da Rede NAPeN.`
      };
    }

    // Regras específicas de resposta insatisfatória (<20% EVA em dor neuropática · <25% CAPS/PCL-5 em TEPT)
    let roadmapSpecificCutoffNotMet = false;
    let roadmapSpecificReason = '';
    if (hasScores && this.activeConditionId === 'dor-neuropatica') {
      const reductionPct = deltaResult.isImproved ? Math.abs(deltaResult.percent) : 0;
      if (reductionPct < 20) {
        roadmapSpecificCutoffNotMet = true;
        roadmapSpecificReason = 'Critério individual de dor neuropática: redução na dor inferior a 20% na EVA em 5 sessões configura resposta insatisfatória (verificar também alodinia, hiperalgesia, sono e humor).';
      }
    } else if (hasScores && this.activeConditionId === 'tept') {
      const reductionPct = deltaResult.isImproved ? Math.abs(deltaResult.percent) : 0;
      if (reductionPct < 25) {
        roadmapSpecificCutoffNotMet = true;
        roadmapSpecificReason = 'Critério individual no TEPT: redução inferior a 25% na CAPS ou PCL-5 ao término do protocolo exige reavaliação diagnóstica, investigação de comorbidades e transição de protocolo.';
      }
    }

    // 2. Avaliação com escores numéricos preenchidos
    if (hasScores) {
      const eff = activeMod?.efeito_clinico || {};
      const estudo = deltaResult.studyRef || eff.estudo_referencia || activeMod?.ensaio_clinico?.autores || 'o ensaio clínico de referência do protocolo';
      const scoreSummary = deltaResult.isOrdinal
        ? `${Math.abs(deltaResult.delta)} nível(is) na EAM`
        : `${deltaResult.delta >= 0 ? '+' : ''}${deltaResult.delta.toFixed(1)} pts (${deltaResult.percentFormatted})`;

      // 2A. Meta atingida (incluindo ponto de corte percentual específico) + Boa/Leve tolerabilidade
      if (deltaResult.mcidMet && !roadmapSpecificCutoffNotMet && (tol === 'boa' || tol === 'leve')) {
        const tolSuffix = tol === 'leve'
          ? ` Observou-se apenas desconforto leve tolerável: ${guidance.orientacaoGeral}`
          : '';
        return {
          recommendationType: 'success',
          outcomeButton: 'success',
          recommendedStage: evalBaseStage === 'evaluation' ? 'primary' : evalBaseStage,
          needsAdverseReport: tol === 'leve',
          adverseBankUrl: guidance.adverseBankUrl,
          badgeLabel: tol === 'leve'
            ? 'Resposta Satisfatória (≥ MCID · Monitorar Desconforto Leve)'
            : 'Resposta Clínica Satisfatória Alcançada',
          summaryHtml: `<strong>[Resposta Clínica Satisfatória Alcançada]</strong> O paciente obteve variação de <strong>${scoreSummary}</strong>, atingindo o critério clínico (${deltaResult.mcidLabel}) em concordância com o estudo de referência (<em>${estudo}</em>), com perfil de segurança favorável. <strong>Conduta Oficial NAPeN:</strong> Manter protocolo até consolidação clínica e iniciar transição gradual para manutenção.${tolSuffix}`
        };
      }

      // 2B. Meta atingida, porém com intolerância moderada limitando conforto/adesão
      if (deltaResult.mcidMet && !roadmapSpecificCutoffNotMet && tol === 'intolerante') {
        return {
          recommendationType: 'warning_tol',
          outcomeButton: 'danger',
          recommendedStage: nextProtocolStage,
          scrollGuideTarget: 'tolerabilityDoseGuidePanel',
          needsAdverseReport: true,
          adverseBankUrl: guidance.adverseBankUrl,
          badgeLabel: 'MCID Atingida com Intolerância — Adequar Conforto ou Avançar',
          summaryHtml: `<strong>[Meta Numérica Atingida, mas Tolerabilidade Limita a Execução]</strong> Apesar do ganho de <strong>${scoreSummary}</strong> (≥ MCID), a intolerância moderada exige consultar os <strong>Ajustes de Tolerabilidade & Dose</strong> (${guidance.ajusteDoseSugerido}). Caso o desconforto persista após adequação, seguir diretamente para <strong>${nextProtocolLabel}</strong>.`
        };
      }

      // 2C / 2D. Resposta insatisfatória (< MCID ou abaixo do ponto de corte individual) -> Avançar diretamente ao próximo protocolo
      const partialNote = !roadmapSpecificCutoffNotMet && deltaResult.isImproved
        ? `Houve evolução parcial de <strong>${scoreSummary}</strong>, porém ainda inferior ao limiar mínimo de relevância clínica (${deltaResult.mcidLabel}).`
        : `A variação obtida (<strong>${scoreSummary}</strong>) não atingiu a meta clínica esperada (${deltaResult.mcidLabel}).`;
      const tolReason = tol === 'intolerante'
        ? ' Com intolerância moderada associada, não manter carga atual — priorizar transição direta ao próximo protocolo.'
        : (isFailure
            ? ' Todas as etapas da cadeia e seção de ajustes foram percorridas — caracteriza-se Falha Terapêutica formal.'
            : ' Caso persista resposta insatisfatória ao concluir toda a cadeia e os ajustes, caracteriza-se Falha Terapêutica formal.');
      const ruleContext = roadmapSpecificReason || (reevalRuleText ? ` Regra clínica: ${reevalRuleText}` : '');
      return {
        recommendationType: 'danger',
        outcomeButton: 'danger',
        recommendedStage: nextProtocolStage,
        needsAdverseReport: tol === 'intolerante',
        adverseBankUrl: guidance.adverseBankUrl,
        badgeLabel: tol === 'intolerante'
          ? `Resposta Insatisfatória + Intolerância — Avançar para ${nextProtocolLabel}`
          : `Resposta Insatisfatória (< MCID) — Avançar para ${nextProtocolLabel}`,
        summaryHtml: `<strong>[Resposta Clínica Insatisfatória]</strong> ${partialNote} ${ruleContext} <strong>Conduta Oficial NAPeN:</strong> Seguir diretamente para <strong>${nextProtocolLabel}</strong> na sequência clínica.${tolReason}`
      };
    }

    // 3. Avaliação sem escores numéricos preenchidos (decisão guiada por tolerabilidade)
    if (tol === 'intolerante') {
      return {
        recommendationType: 'warning_tol',
        outcomeButton: 'danger',
        recommendedStage: nextProtocolStage,
        scrollGuideTarget: 'tolerabilityDoseGuidePanel',
        needsAdverseReport: true,
        adverseBankUrl: guidance.adverseBankUrl,
        badgeLabel: 'Intolerância Moderada — Consultar Tolerabilidade ou Migrar',
        summaryHtml: `<strong>[Intolerância Moderada Reportada]</strong> Consulte as orientações de conforto no painel <strong>Ajustes de Tolerabilidade & Dose</strong> abaixo: ${guidance.ajusteDoseSugerido} Caso a intolerância persista após adequação, avance diretamente para <strong>${nextProtocolLabel}</strong>.`
      };
    }

    return {
      recommendationType: 'pending',
      outcomeButton: null,
      recommendedStage: null,
      needsAdverseReport: tol === 'leve',
      adverseBankUrl: guidance.adverseBankUrl,
      badgeLabel: tol === 'leve' ? 'Desconforto Leve Registrado' : 'Aguardando dados clínicos',
      summaryHtml: tol === 'leve'
        ? `<strong>[Desconforto Leve Tolerável]</strong> ${guidance.orientacaoGeral} Preencha os escores pré e pós-tratamento para integrar a resposta quantitativa.`
        : 'Insira os escores pré e pós-tratamento e confirme a tolerabilidade clínica para obter a conduta integrada do protocolo.'
    };
  }
}

window.DecisionEngine = DecisionEngine;
