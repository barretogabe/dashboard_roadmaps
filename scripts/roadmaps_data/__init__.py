#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construtores compartilhados para os 18 Roadmaps Oficiais da Rede NAPeN (RM01–RM18).
Mantém esquema único compatível com DecisionEngine, Biblioteca de Evidências,
Calculadora Dual, Modo Continuidade e Sistema de 10 Slots Contextuais.
"""

PEM_GUIDE_DOI = 'https://doi.org/10.17267/2965-3738bis.2023.e5097'
PEM_GUIDE_SHORT = '10.17267/2965-3738bis.2023.e5097'
PEM_GUIDE_LABEL = (
    'Ver guia prático para testar a presença de PEM '
    '(Albuquerque et al., 2023 · DOI: 10.17267/2965-3738bis.2023.e5097)'
)
ADVERSE_BANK_URL = 'https://www.neuromodulation-net.com/banco-efeitos-adversos-napen'

DIR_IFCN_RTMS_2020 = {
    'nome': 'Lefaucheur et al., 2020 (IFCN)',
    'autores': 'Lefaucheur et al.',
    'ano': 2020,
    'periodico': 'Clinical Neurophysiology, 131(2), 474–528',
    'doi': '10.1016/j.clinph.2019.11.002',
    'url_doi': 'https://doi.org/10.1016/j.clinph.2019.11.002',
    'citacao_completa': 'Lefaucheur, J. P., et al. (2020). Clin Neurophysiol, 131(2), 474–528.'
}

DIR_IFCN_TDCS_2017 = {
    'nome': 'Lefaucheur et al., 2017 (IFCN)',
    'autores': 'Lefaucheur et al.',
    'ano': 2017,
    'periodico': 'Clinical Neurophysiology, 128(1), 56–92',
    'doi': '10.1016/j.clinph.2016.10.087',
    'url_doi': 'https://doi.org/10.1016/j.clinph.2016.10.087',
    'citacao_completa': 'Lefaucheur, J. P., et al. (2017). Clin Neurophysiol, 128(1), 56–92.'
}

DIR_ROSSI_2009 = {
    'nome': 'Rossi et al., 2009 / Consensus Safety TMS',
    'autores': 'Rossi et al.',
    'ano': 2009,
    'periodico': 'Clinical Neurophysiology, 120(12), 2008–2039',
    'doi': '10.1016/j.clinph.2009.08.016',
    'url_doi': 'https://doi.org/10.1016/j.clinph.2009.08.016',
    'citacao_completa': 'Rossi, S., et al. (2009). Clin Neurophysiol, 120(12), 2008–2039.'
}


def make_ref(autores, ano, titulo, periodico, doi, url_doi=None, tipo='Ensaio clínico de referência', citacao_completa=None):
    clean_doi = (doi or '').replace('https://doi.org/', '').replace('http://dx.doi.org/', '').strip()
    full_url = url_doi or (f'https://doi.org/{clean_doi}' if clean_doi else '')
    return {
        'autores': autores,
        'ano': ano,
        'titulo': titulo,
        'periodico': periodico,
        'doi': clean_doi,
        'url_doi': full_url,
        'tipo': tipo,
        'citacao_completa': citacao_completa or f'{autores} ({ano}). {periodico}.'
    }


def make_scale(
    scale_id,
    nome,
    sigla,
    direcao_melhora,
    meta_texto,
    tamanho_efeito,
    *,
    tipo='continua',
    placeholder='Ex: 20',
    min_val=0,
    max_val=None,
    mcid_valor=None,
    mcid_label=None,
    privativo_psicologo=False
):
    obj = {
        'id': scale_id,
        'nome': nome,
        'sigla': sigla,
        'tipo': tipo,
        'placeholder': placeholder,
        'direcao_melhora': direcao_melhora,
        'meta_texto': meta_texto,
        'tamanho_efeito': tamanho_efeito
    }
    if min_val is not None:
        obj['min'] = min_val
    if max_val is not None:
        obj['max'] = max_val
    if mcid_valor is not None:
        obj['mcid_valor'] = mcid_valor
    if mcid_label:
        obj['mcid_label'] = mcid_label
    if privativo_psicologo:
        obj['privativo_psicologo'] = True
    return obj


def make_obs(
    obs_id,
    texto,
    slot,
    *,
    categoria='clinica',
    etapa_ids=None,
    opcao_ids=None,
    protocolo_ids=None,
    modalidades_tipo=None,
    estagios=None,
    tolerabilidades=None,
    referencia_doi=None,
    referencia_rotulo=None,
    acao_condicao_id=None,
    acao_rotulo=None,
    severidade='info'
):
    """
    Constrói observação contextual declarativa com gatilho explícito.
    Slots suportados:
      - 'pre'         : SLOT-PRE (#preTriagemObservationsSlot — pré-triagem/elegibilidade/redirecionamento)
      - 'step'        : SLOT-STEP (dentro do card de decisão ativo no fluxo em cascata)
      - 'tec'         : SLOT-P1-TEC (sob Técnica Recomendada)
      - 'alvo'        : SLOT-P2-ALVO (sob Alvo Anatômico & Coordenadas)
      - 'intensidade' : SLOT-P3-INT (sob Frequência & Intensidade)
      - 'sessoes'     : SLOT-P4-SES (sob Dose e Regime de Aplicação / Sessões)
      - 'scale'       : SLOT-SCALE (sob Instrumento de Avaliação e na Calculadora)
      - 'reeval'      : SLOT-REEVAL (#monitoringReeval — janela e critério de resposta insatisfatória)
      - 'tol'         : SLOT-TOL (#tolerabilityContextNote e #monitoringStopRule)
      - 'stage'       : SLOT-STAGE (#branchResultPanel e #continuingStageFocusSlot)
    """
    item = {
        'id': obs_id,
        'texto': texto,
        'slot': slot,
        'categoria': categoria,
        'severidade': severidade,
        'gatilho': {}
    }
    if etapa_ids:
        item['gatilho']['etapa_ids'] = etapa_ids
    if opcao_ids:
        item['gatilho']['opcao_ids'] = opcao_ids
    if protocolo_ids:
        item['gatilho']['protocolo_ids'] = protocolo_ids
    if modalidades_tipo:
        item['gatilho']['modalidades_tipo'] = modalidades_tipo
    if estagios:
        item['gatilho']['estagios'] = estagios
    if tolerabilidades:
        item['gatilho']['tolerabilidades'] = tolerabilidades
    if referencia_doi:
        item['referencia_doi'] = referencia_doi
    if referencia_rotulo:
        item['referencia_rotulo'] = referencia_rotulo
    if acao_condicao_id:
        item['acao_condicao_id'] = acao_condicao_id
    if acao_rotulo:
        item['acao_rotulo'] = acao_rotulo
    return item


def make_chain_step(
    ordem,
    step_id,
    etapa_rotulo,
    nome,
    tecnica,
    alvo,
    parametros,
    *,
    sessoes='',
    efeito_esperado='',
    referencia='',
    linha_fluxograma='solida',
    observacoes='',
    fase_etapa=None
):
    resolved_fase = fase_etapa
    if not resolved_fase:
        combined = f'{etapa_rotulo} {nome}'.lower()
        if 'ajuste' in combined or 'seção de ajustes' in combined or 'quadro de ajustes' in combined:
            resolved_fase = 'ajustes'
        elif ordem == 1:
            resolved_fase = 'inicial'
        else:
            resolved_fase = 'sequencia'
    return {
        'ordem': ordem,
        'id': step_id,
        'etapa_rotulo': etapa_rotulo,
        'nome': nome,
        'tecnica': tecnica,
        'alvo': alvo,
        'parametros': parametros,
        'sessoes': sessoes,
        'efeito_esperado': efeito_esperado,
        'referencia': referencia,
        'linha_fluxograma': linha_fluxograma,
        'observacoes': observacoes,
        'fase_etapa': resolved_fase
    }


def make_mod(
    *,
    protocolo_id,
    tecnica,
    modalidade_sigla,
    alvo,
    frequencia,
    intensidade,
    pulsos_duracao,
    sessoes,
    escala_recomendada,
    meta_melhora,
    tamanho_efeito,
    evidencia,
    linha_fluxograma,
    diretriz_internacional,
    diretriz_ref,
    artigo_referencia,
    meta_analise,
    mcid_valor,
    mcid_label,
    cohen_d_valor,
    cohen_d_interp,
    estudo_referencia,
    efeito_resumo,
    escalas_detalhadas,
    cadeia_sequencial,
    ajuste_parametros,
    falha_terapeutica,
    notas_clinicas,
    sessoes_ajuste,
    contraindicacoes=None,
    ic_min=None,
    ic_max=None,
    audit_meta=None,
    mod_tipo='rtms',
    escalas_por_fator=None
):
    normalized_chain = []
    for idx, step in enumerate(cadeia_sequencial or [], start=1):
        s = dict(step)
        s['ordem'] = idx
        if idx == 1:
            s['fase_etapa'] = 'inicial'
        elif s.get('fase_etapa') != 'ajustes':
            s['fase_etapa'] = 'sequencia'
        normalized_chain.append(s)

    alt1_step = normalized_chain[1] if len(normalized_chain) > 1 else None
    alt2_step = normalized_chain[2] if len(normalized_chain) > 2 else None

    if alt1_step:
        prot_alt1 = {
            'id': alt1_step['id'],
            'nome': alt1_step['nome'],
            'tecnica': alt1_step['tecnica'],
            'alvo': alt1_step['alvo'],
            'parametros': f"{alt1_step['parametros']}{(' · ' + alt1_step['sessoes']) if alt1_step.get('sessoes') else ''}",
            'linha_fluxograma': alt1_step.get('linha_fluxograma', 'solida'),
            'efeito_esperado': alt1_step.get('efeito_esperado', ''),
            'referencia': alt1_step.get('referencia', ''),
            'fase_etapa': alt1_step.get('fase_etapa', 'sequencia'),
            'observacoes': alt1_step.get('observacoes') or 'Transição sequencial indicada pelo algoritmo clínico diante de resposta insatisfatória ou intolerância.'
        }
    else:
        prot_alt1 = {
            'nome': 'Protocolo Único do Ramo (Sem Sequencial Direto)',
            'tecnica': 'Ajuste de Tolerabilidade / Reavaliação Multiprofissional',
            'alvo': alvo,
            'parametros': 'Otimização gradual dentro da margem de segurança antes de declarar encerramento do ciclo.',
            'linha_fluxograma': linha_fluxograma,
            'fase_etapa': 'ajustes',
            'observacoes': 'O fluxo clínico não prevê troca sequencial adicional neste ramo específico.'
        }

    if alt2_step:
        prot_alt2 = {
            'id': alt2_step['id'],
            'nome': alt2_step['nome'],
            'tecnica': alt2_step['tecnica'],
            'alvo': alt2_step['alvo'],
            'parametros': f"{alt2_step['parametros']}{(' · ' + alt2_step['sessoes']) if alt2_step.get('sessoes') else ''}",
            'linha_fluxograma': alt2_step.get('linha_fluxograma', 'solida'),
            'efeito_esperado': alt2_step.get('efeito_esperado', ''),
            'referencia': alt2_step.get('referencia', ''),
            'fase_etapa': alt2_step.get('fase_etapa', 'ajustes'),
            'observacoes': alt2_step.get('observacoes') or 'Passo sequencial subsequente previsto no fluxograma antes da caracterização de falha terapêutica.'
        }
    else:
        prot_alt2 = {
            'nome': 'Reavaliação Direta Pré-Falha',
            'tecnica': 'Consolidação Clínica ou Transição p/ Falha Terapêutica',
            'alvo': alvo,
            'parametros': 'Conferir adesão, medicações interferentes (benzodiazepínicos) e terapia concomitante.',
            'linha_fluxograma': linha_fluxograma,
            'fase_etapa': 'ajustes',
            'observacoes': 'Se não houver resposta após as tentativas indicadas neste ramo, caracteriza-se falha terapêutica.'
        }

    efeito_obj = {
        'cohen_d_esperado': cohen_d_valor,
        'interpretacao_cohen': cohen_d_interp,
        'mcid_valor': mcid_valor,
        'mcid_label': mcid_label,
        'efeito_esperado_resumo': efeito_resumo,
        'estudo_referencia': estudo_referencia,
        'cohen_d': f"d ≈ {cohen_d_valor:.2f} ({cohen_d_interp})"
    }
    if ic_min is not None:
        efeito_obj['ic_min'] = ic_min
    if ic_max is not None:
        efeito_obj['ic_max'] = ic_max

    mod = {
        'protocolo_id': protocolo_id,
        'mod_tipo': mod_tipo,
        'tecnica': tecnica,
        'modalidade_sigla': modalidade_sigla,
        'alvo': alvo,
        'frequencia': frequencia,
        'intensidade': intensidade,
        'pulsos_duracao': pulsos_duracao,
        'sessoes': sessoes,
        'escala_recomendada': escala_recomendada,
        'meta_melhora': meta_melhora,
        'tamanho_efeito': tamanho_efeito,
        'evidencia': evidencia,
        'linha_fluxograma': linha_fluxograma,
        'diretriz_internacional': diretriz_internacional,
        'diretriz_ref': diretriz_ref,
        'artigo_referencia': artigo_referencia,
        'ensaio_clinico': dict(artigo_referencia),
        'meta_analise': meta_analise,
        'escalas_detalhadas': escalas_detalhadas,
        'cohen_d': efeito_obj['cohen_d'],
        'mcid_valor': mcid_valor,
        'mcid_label': mcid_label,
        'efeito_clinico': efeito_obj,
        'ajuste_parametros': ajuste_parametros,
        'protocolo_alternativo': prot_alt1,
        'protocolo_alternativo_2': prot_alt2,
        'cadeia_sequencial': normalized_chain,
        'falha_terapeutica': falha_terapeutica,
        'sessoes_ajuste': sessoes_ajuste,
        'contraindicacoes': contraindicacoes or [
            'Implantes metálicos ferromagnéticos intracranianos ou próximos à área de estimulação',
            'Histórico de epilepsia / crises convulsivas não controladas',
            'Implantes cocleares ou dispositivos eletrônicos intracranianos'
        ],
        'notas_clinicas': notas_clinicas
    }
    if escalas_por_fator:
        mod['escalas_por_fator'] = escalas_por_fator
    if audit_meta:
        mod['audit_meta'] = audit_meta
    return mod
