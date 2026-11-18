"""Unified registry assembling all 13 official clinical conditions (RM01-RM18) for the Rede NAPeN dashboard."""

from scripts.roadmaps_data.avc import build_avc_conditions
from scripts.roadmaps_data.dor_movimento import build_dor_movimento_conditions
from scripts.roadmaps_data.pediatria_neurodesenvolvimento import (
    build_pediatria_neurodesenvolvimento_conditions,
)
from scripts.roadmaps_data.saude_mental_cognicao import (
    build_saude_mental_cognicao_conditions,
)

MOD_LABELS = {
    "rtms": "Estimulação Magnética (rTMS / iTBS / cTBS)",
    "tdcs": "Estimulação por Corrente Contínua (tDCS / taVNS)",
    "integrado": "Fluxograma Integrado (rTMS / tDCS / tsDCS)",
}

INTEGRATED_CONDITIONS = {
    "dor-neuropatica",
    "ataxia-cerebelar",
    "paralisia-cerebral",
    "transtorno-espectro-autista",
}


def _normalize_tree(tree, mods_map):
    """Converts dict-keyed etapas into canonical ordered list with etapa_id and modalidade_chave."""
    out = dict(tree)
    etapas_raw = tree.get("etapas")
    etapa_inicial = tree.get("etapa_inicial") or "fator_limitante"

    if isinstance(etapas_raw, dict):
        ordered_keys = []
        if etapa_inicial in etapas_raw:
            ordered_keys.append(etapa_inicial)
        for k in etapas_raw:
            if k not in ordered_keys:
                ordered_keys.append(k)
        etapas_list = []
        for k in ordered_keys:
            step = dict(etapas_raw[k])
            step["etapa_id"] = k
            norm_opts = []
            for opt in step.get("opcoes", []):
                nopt = dict(opt)
                if not nopt.get("subtexto") and nopt.get("criterio"):
                    nopt["subtexto"] = nopt["criterio"]
                alvo = nopt.get("modalidade_chave") or nopt.get("protocolo_alvo")
                if alvo:
                    nopt["modalidade_chave"] = alvo
                    nopt["protocolo_alvo"] = alvo
                    assert alvo in mods_map, f"Tree target '{alvo}' missing from modalidades"
                norm_opts.append(nopt)
            step["opcoes"] = norm_opts
            etapas_list.append(step)
        out["etapas"] = etapas_list

    return out


def _normalize_condition_contract(cond):
    """Normalizes factors, modalities_suportadas, and arvore_algoritmo across all 13 conditions."""
    mods_map = cond.get("modalidades") or {}

    # Ensure every fator_limitante exposes both 'label' and 'nome'
    norm_factors = []
    for f in cond.get("fatores_limitantes", []):
        nf = dict(f)
        nf["label"] = nf.get("label") or nf.get("nome") or f.get("id", "")
        nf["nome"] = nf.get("nome") or nf["label"]
        norm_factors.append(nf)
    cond["fatores_limitantes"] = norm_factors

    if "arvores_por_modalidade" in cond and isinstance(cond["arvores_por_modalidade"], dict):
        raw_trees = cond.pop("arvores_por_modalidade")
        cond["modalidades_suportadas"] = [
            {"id": m_id, "nome": MOD_LABELS.get(m_id, m_id.upper()), "label": MOD_LABELS.get(m_id, m_id.upper())}
            for m_id in raw_trees.keys()
        ]
        cond["arvore_algoritmo"] = {
            m_id: _normalize_tree(t, mods_map) for m_id, t in raw_trees.items()
        }
    else:
        single_tree = cond.get("arvore_algoritmo") or {}
        if "rtms" in single_tree or "integrado" in single_tree:
            raw_trees = single_tree
            cond["modalidades_suportadas"] = [
                {"id": m_id, "nome": MOD_LABELS.get(m_id, m_id.upper()), "label": MOD_LABELS.get(m_id, m_id.upper())}
                for m_id in raw_trees.keys()
            ]
            cond["arvore_algoritmo"] = {
                m_id: _normalize_tree(t, mods_map) for m_id, t in raw_trees.items()
            }
        else:
            m_id = "integrado" if cond["id"] in INTEGRATED_CONDITIONS else "rtms"
            cond["modalidades_suportadas"] = [
                {"id": m_id, "nome": MOD_LABELS[m_id], "label": MOD_LABELS[m_id]}
            ]
            cond["arvore_algoritmo"] = {m_id: _normalize_tree(single_tree, mods_map)}

    first_mod_id = cond["modalidades_suportadas"][0]["id"]
    first_tree = cond["arvore_algoritmo"].get(first_mod_id) or {}
    first_etapa = (first_tree.get("etapas") or [{}])[0]
    if first_etapa.get("pergunta") and not cond.get("no1_pergunta"):
        cond["no1_pergunta"] = first_etapa["pergunta"]

    return cond


def build_official_conditions(order_ids=None):
    """Builds and returns all 13 clinical conditions backed directly by official PDFs RM01-RM18."""
    by_id = {}
    for builder in (
        build_avc_conditions,
        build_dor_movimento_conditions,
        build_saude_mental_cognicao_conditions,
        build_pediatria_neurodesenvolvimento_conditions,
    ):
        for cond in builder():
            by_id[cond["id"]] = _normalize_condition_contract(cond)

    default_order = order_ids or [
        "avc-membro-superior",
        "avc-mobilidade",
        "avc-afasia",
        "avc-disfagia",
        "doenca-parkinson",
        "depressao-maior",
        "ansiedade-generalizada",
        "tept",
        "dor-neuropatica",
        "ataxia-cerebelar",
        "paralisia-cerebral",
        "transtorno-espectro-autista",
        "alzheimer-ccl",
    ]
    ordered = [by_id[cid] for cid in default_order if cid in by_id]
    remaining = [cond for cid, cond in by_id.items() if cid not in set(default_order)]
    return ordered + remaining
