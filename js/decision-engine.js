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
    this.activeOutcome = null; // 'success' | 'danger' | null
  }

  getCondition(conditionId) {
    return this.data.condicoes.find(c => c.id === conditionId);
  }

  setCondition(conditionId) {
    this.activeConditionId = conditionId;
    this.activeModalityType = 'rtms';
    this.pathChoices = {};
    const cond = this.getCondition(conditionId);
    if (cond && cond.fatores_limitantes && cond.fatores_limitantes.length > 0) {
      this.primaryFactorId = cond.fatores_limitantes[0].id;
      this.activeFactorId = cond.fatores_limitantes[0].id;
    } else {
      this.primaryFactorId = null;
      this.activeFactorId = null;
    }
    this.activeScaleId = null;
    this.activeOutcome = null;

    // Inicializa escolhas padrão da árvore se disponível
    const tree = this.getActiveTree();
    if (tree && tree.etapas && tree.etapas.length > 0) {
      const firstEtapa = tree.etapas[0];
      if (firstEtapa.opcoes && firstEtapa.opcoes.length > 0) {
        this.setPathChoice(firstEtapa.etapa_id, firstEtapa.opcoes[0].id);
      }
    }
  }

  setModalityType(type) {
    this.activeModalityType = type;
    this.pathChoices = {};
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

  getActiveTree() {
    if (!this.activeConditionId) return null;
    const cond = this.getCondition(this.activeConditionId);
    if (!cond || !cond.arvore_algoritmo) return null;
    return cond.arvore_algoritmo[this.activeModalityType] || null;
  }

  setPathChoice(stepId, optionId) {
    this.pathChoices[stepId] = optionId;
    this.activeScaleId = null;
    this.activeOutcome = null;

    // Sincroniza activeFactorId com o passo escolhido
    const tree = this.getActiveTree();
    if (tree && tree.etapas) {
      const step = tree.etapas.find(s => s.etapa_id === stepId);
      if (step) {
        const opt = step.opcoes.find(o => o.id === optionId);
        if (opt && opt.modalidade_chave) {
          this.activeFactorId = opt.modalidade_chave;
        } else if (stepId === 'fator_limitante') {
          if (optionId.includes('m1')) {
            this.activeFactorId = 'espasticidade';
          } else if (optionId.includes('s1')) {
            this.activeFactorId = 'sensorial';
          } else if (optionId.includes('ppc')) {
            this.activeFactorId = 'negligencia';
          }
          this.primaryFactorId = this.activeFactorId;
        }
      }
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
  }

  setActiveScale(scaleId) {
    this.activeScaleId = scaleId;
  }

  getActiveScale() {
    const m = this.getActiveModality();
    if (!m || !m.escalas_detalhadas || m.escalas_detalhadas.length === 0) return null;
    if (this.activeScaleId) {
      const found = m.escalas_detalhadas.find(s => s.id === this.activeScaleId);
      if (found) return found;
    }
    return m.escalas_detalhadas[0];
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
        url: null
      };
    }

    const ref = m.diretriz_ref;
    const rec = m.diretriz_internacional || 'Consenso Clínico Internacional';

    if (ref && ref.url_doi) {
      return {
        text: `${rec} — ${ref.autores} (${ref.ano})`,
        recomendacao: rec,
        autores: ref.autores,
        ano: ref.ano,
        doi: ref.doi,
        url: ref.url_doi,
        citacao: ref.citacao_completa
      };
    }

    return {
      text: rec,
      recomendacao: rec,
      autores: null,
      ano: null,
      doi: null,
      url: null
    };
  }

  calculateDelta(valBaseRaw, valPostRaw, scaleObj = null, modality = null) {
    const scale = scaleObj || this.getActiveScale();
    const m = modality || this.getActiveModality();

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
      const estudo = eff.estudo_referencia || 'estudos de referência';
      const esperado = eff.efeito_esperado_resumo || m?.tamanho_efeito || 'Diminuição de 1 nível na EAM';

      let comparativeFeedback = '';
      if (outcomeRecommended === 'success') {
        comparativeFeedback = `<strong>[Resposta Clínica Satisfatória Alcançada]</strong> A redução de ${Math.abs(deltaLevels)} nível(is) no tônus muscular atingiu a MCID da escala (redução ≥ 1 grau) e é compatível com os estudos de referência (${estudo}). <strong>Conduta Oficial NAPeN:</strong> Manter protocolo para consolidação motora e transição para manutenção periódica.`;
      } else {
        comparativeFeedback = `<strong>[Resposta Clínica Insatisfatória (< MCID)]</strong> A variação de tônus permaneceu aquém da MCID da escala (redução ≥ 1 grau na EAM). <strong>Conduta Oficial NAPeN:</strong> Transição para o Protocolo Alternativo da árvore de decisão. Se persistir sem resposta após os protocolos alternativos, caracteriza-se Falha Terapêutica.`;
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
    const meta = scale?.meta_texto || m?.meta_melhora || '';
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

    // Avaliação de MCID (Minimal Clinically Important Difference)
    const eff = m?.efeito_clinico || {};
    const mcidVal = eff.mcid_valor || m?.mcid_valor || (scale?.id === 'fma-ue' || /fma/i.test(scale?.nome || '') ? 6.6 : 30.0);
    const mcidLabel = eff.mcid_label || m?.mcid_label || `Meta clínica: ${meta}`;

    let mcidMet = false;
    const changeMagnitude = Math.abs(delta);
    
    // Se a MCID for percentual (ex: 30%, 50%)
    if (/30%/i.test(mcidLabel) || mcidVal === 30.0 || mcidVal === 50.0) {
      mcidMet = isImproved && percentChange >= mcidVal;
    } else {
      // Se for em pontos absolutos (ex: 6.6 na FMA-UE, 5.0 na BBS, 1.5 na SARA)
      mcidMet = isImproved && changeMagnitude >= mcidVal;
    }

    // Compatibilidade com Intervalo de Confiança do Estudo (IC 95%)
    const icMin = eff.ic_min;
    const icMax = eff.ic_max;
    let withinCI = false;
    if (icMin !== undefined && icMax !== undefined && icMin !== null && icMax !== null) {
      const metricToCheck = (/30%/i.test(mcidLabel) || mcidVal === 30.0 || mcidVal === 50.0) ? percentChange : changeMagnitude;
      withinCI = metricToCheck >= icMin && metricToCheck <= icMax;
    }

    let goalMet = mcidMet;
    if (!goalMet) {
      if (/30%/i.test(meta)) goalMet = isImproved && percentChange >= 30;
      else if (/50%/i.test(meta)) goalMet = isImproved && percentChange >= 50;
      else if (/6[,.]6/i.test(meta)) goalMet = isImproved && changeMagnitude >= 6.6;
      else if (isImproved && percentChange >= 25) goalMet = true;
    }

    const outcomeRecommended = goalMet ? 'success' : 'danger';

    const estudo = eff.estudo_referencia || m?.ensaio_clinico?.autores || 'estudos de referência';
    const esperadoResumo = eff.efeito_esperado_resumo || m?.tamanho_efeito || 'efeito clinicamente relevante';

    let comparativeFeedback = '';
    if (outcomeRecommended === 'success') {
      comparativeFeedback = `<strong>[Resposta Clínica Satisfatória Alcançada]</strong> O ganho individual de <strong>${sign}${changeMagnitude.toFixed(1)} pontos (${percentFormatted})</strong> superou a MCID da escala (${mcidLabel}) e é compatível com os estudos de referência (<em>${estudo}</em>: ${esperadoResumo}). <strong>Conduta Oficial NAPeN:</strong> Prosseguir para o protocolo de consolidação e manutenção periódica com redução gradual das sessões.`;
    } else {
      comparativeFeedback = `<strong>[Resposta Clínica Insatisfatória (< MCID)]</strong> O ganho individual de <strong>${sign}${changeMagnitude.toFixed(1)} pontos (${percentFormatted})</strong> não atingiu o limiar mínimo de relevância clínica (${mcidLabel}). <strong>Conduta Oficial NAPeN:</strong> Transição para o Protocolo Alternativo da árvore de decisão. Caso persista sem melhora após os protocolos alternativos, caracteriza-se Falha Terapêutica formal.`;
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
      goalMet,
      outcomeRecommended,
      metaText: meta,
      comparativeFeedback
    };
  }
}

window.DecisionEngine = DecisionEngine;
