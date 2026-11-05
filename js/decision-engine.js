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
    this.activeFactorId = null;
    this.activeScaleId = null;
    this.activeOutcome = null; // 'success' | 'warning' | 'danger' | null
  }

  getCondition(conditionId) {
    return this.data.condicoes.find(c => c.id === conditionId);
  }

  setCondition(conditionId) {
    this.activeConditionId = conditionId;
    const cond = this.getCondition(conditionId);
    if (cond && cond.fatores_limitantes && cond.fatores_limitantes.length > 0) {
      this.activeFactorId = cond.fatores_limitantes[0].id;
    } else {
      this.activeFactorId = null;
    }
    this.activeScaleId = null;
    this.activeOutcome = null;
  }

  setFactor(factorId) {
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

      const deltaText = deltaLevels === 0
        ? 'Δ = 0 níveis (Tônus inalterado)'
        : deltaLevels < 0
          ? `Δ = ${deltaLevels} níveis (Melhora de ${percent.toFixed(1)}%)`
          : `Δ = +${deltaLevels} níveis (Aumento de tônus / Piora)`;

      const goalMet = deltaLevels <= -1; // Meta formal dos roadmaps: redução ≥ 1 nível
      const outcomeRecommended = goalMet ? 'success' : (isImproved ? 'warning' : 'danger');

      return {
        text: deltaText,
        isSuccess: true,
        delta: deltaLevels,
        percent: parseFloat(percent.toFixed(1)),
        isImproved,
        goalMet,
        outcomeRecommended,
        isOrdinal: true,
        gradeFrom: strBase,
        gradeTo: strPost
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

    let textDisplay = '';
    if (isReduction && valPost === 0 && valBase > 0) {
      textDisplay = `Δ = ${delta.toFixed(1)} (Remissão clínica completa — Escore 0)`;
    } else {
      const sign = delta > 0 ? `+${delta.toFixed(1)}` : `${delta.toFixed(1)}`;
      textDisplay = `Δ = ${sign} (${percentChange >= 0 ? '+' : ''}${percentChange.toFixed(1)}%)`;
    }

    let goalMet = false;
    if (/30%/i.test(meta)) {
      goalMet = isImproved && percentChange >= 30;
    } else if (/50%/i.test(meta)) {
      goalMet = isImproved && percentChange >= 50;
    } else if (/6[,.]6/i.test(meta)) {
      goalMet = isImproved && delta >= 6.6;
    } else if (isImproved) {
      goalMet = true;
    }

    const outcomeRecommended = goalMet ? 'success' : (isImproved ? 'warning' : 'danger');

    return {
      text: textDisplay,
      isSuccess: true,
      delta,
      percent: parseFloat(percentChange.toFixed(1)),
      isImproved,
      goalMet,
      outcomeRecommended,
      metaText: meta
    };
  }
}

window.DecisionEngine = DecisionEngine;
