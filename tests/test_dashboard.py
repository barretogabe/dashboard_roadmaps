#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Suíte de Testes Automatizados da Plataforma de Prescrição Clínica
Valida integridade do cabeçalho estrito, menu com hover dropdown,
ausência de ícones/redes desnecessários, e fluxo de seleção sob demanda.
"""

import os
import json
import unittest

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class TestRedeNAPeNPrescriptionPlatform(unittest.TestCase):

    def test_01_json_data_integrity(self):
        """Verifica a integridade da base JSON clínica."""
        json_path = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
        self.assertTrue(os.path.exists(json_path), f"JSON ausente: {json_path}")

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.assertEqual(data.get('versao'), '2025-2026')
        self.assertIn('Rede NAPeN', data.get('instituicao', ''))
        self.assertGreaterEqual(len(data.get('condicoes', [])), 10)

        for c in data['condicoes']:
            self.assertIn('id', c)
            self.assertIn('condicao', c)
            self.assertIn('eixo', c)
            self.assertTrue(len(c.get('fatores_limitantes', [])) > 0)
            
            # Garante que não há acrônimos de testes entre parênteses nos rótulos de sintomas
            for f in c.get('fatores_limitantes', []):
                self.assertNotIn('(TUG)', f['label'])
                self.assertNotIn('(HAM-A', f['label'])
                self.assertNotIn('(9HPT)', f['label'])
                self.assertNotIn('(SARA', f['label'])

            modalidades = c.get('modalidades', {})
            self.assertTrue(len(modalidades) > 0)
            for k, m in modalidades.items():
                self.assertIn('tecnica', m)
                self.assertIn('alvo', m)
                self.assertIn('frequencia', m)
                self.assertIn('pulsos_duracao', m)
                self.assertIn('sessoes', m)
                self.assertIn('escala_recomendada', m)
                self.assertIn('meta_melhora', m)
                self.assertIn('tamanho_efeito', m)
                self.assertIn('artigo_referencia', m)
                self.assertIn('url_doi', m['artigo_referencia'])
                self.assertIn('ensaio_clinico', m)
                self.assertIn('url_doi', m['ensaio_clinico'])
                self.assertIn('meta_analise', m)
                self.assertIn('url_doi', m['meta_analise'])
                self.assertIn('diretriz_ref', m)
                self.assertIn('url_doi', m['diretriz_ref'])
                self.assertIn('protocolo_alternativo', m)
                alt = m['protocolo_alternativo']
                self.assertIn('nome', alt)
                self.assertIn('observacoes', alt)

    def test_02_js_data_export(self):
        """Verifica se js/data.js exporta window.NAPEN_DATA corretamente."""
        js_data_path = os.path.join(BASE_DIR, 'js', 'data.js')
        self.assertTrue(os.path.exists(js_data_path))

        with open(js_data_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('window.NAPEN_DATA =', content)
        self.assertIn('"versao": "2025-2026"', content)

    def test_03_brand_assets_present(self):
        """Verifica presença dos logos oficiais da Rede NAPeN."""
        logo_dir = os.path.join(BASE_DIR, 'assets', 'logos')
        h_logo = os.path.join(logo_dir, 'napen_logo_horizontal.png')
        icon_logo = os.path.join(logo_dir, 'napen_logo_icon.png')

        self.assertTrue(os.path.exists(h_logo))
        self.assertTrue(os.path.exists(icon_logo))

    def test_04_html_structure_and_napen_branding(self):
        """Verifica a estrutura de index.html, títulos, cabeçalho oficial e ausência de elementos rejeitados."""
        html_path = os.path.join(BASE_DIR, 'index.html')
        self.assertTrue(os.path.exists(html_path))

        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Título e Subtítulo atualizados
        self.assertIn('Plataforma Interativa de Prescrição Clínica em Neuromodulação Não Invasiva', html)
        self.assertIn('Roadmaps e Algoritmos de Decisão Terapêutica Baseados em Evidências', html)

        # Botão Exclusivo do Portal da Rede NAPeN
        self.assertIn('Retornar ao Portal da Rede NAPeN', html)

        # Itens do Menu na Barra Turquesa Oficial (SEM emojis e SEM ?)
        self.assertIn('PRESCRIÇÃO INTERATIVA', html)
        self.assertIn('MATRIZ DE PROTOCOLOS E PARÂMETROS', html)
        self.assertIn('COMO OS ROADMAPS DE INDICAÇÃO FORAM DESENVOLVIDOS', html)
        # Ausência expressa de ponto de interrogação no título da metodologia e navegação
        self.assertNotIn('como os roadmaps de indicação foram desenvolvidos?', html.lower())
        self.assertNotIn('como os roadmaps são feitos?', html.lower())

        # Dropdown no hover da barra turquesa
        self.assertIn('dropdown-menu-napen', html)
        self.assertIn('dropdownConditionsList', html)

        # Ausência expressa dos botões rejeitados
        self.assertNotIn('lang-selector-pill', html)
        self.assertNotIn('instagram', html.lower())
        self.assertNotIn('youtube', html.lower())
        self.assertNotIn('🇧🇷 pt', html.lower())

        # Versão no Rodapé
        self.assertIn('Versão: 2025–2026', html)

        # Ausência de termos banidos e jargões técnicos
        self.assertNotIn('posologia', html.lower())
        self.assertNotIn('exibindo 13 de 13', html.lower())
        self.assertNotIn('rm01', html.lower())
        self.assertNotIn('rm02', html.lower())
        self.assertNotIn('nó 1', html.lower()) # Substituído por Fator Limitante Principal

        # Ausência expressa de ícones de ECG / batimentos cardíacos
        self.assertNotIn('22 12 18 12 15 21 9 3 6 12 2 12', html)

        # Painel de Evidência Científica com DOI
        self.assertIn('evidenceReferencePanel', html)
        self.assertIn('evidenceCitationText', html)
        self.assertIn('evidenceDoiLink', html)
        self.assertIn('evidenceGuidelineText', html)
        self.assertIn('evidenceGuidelineDoiLink', html)

        # Calculadora Dual (Resposta Clínica & Comparador de Efeito)
        self.assertIn('dualCalcContainer', html)
        self.assertIn('calcValBase', html)
        self.assertIn('calcValPost', html)
        self.assertIn('calcRoadmapEffectText', html)
        self.assertIn('metodologia-calculo-efeito', html)

        # Seletor de Escalas Múltiplas e Painel Especial da EAM
        self.assertIn('calcScaleTabs', html)
        self.assertIn('calcEamBox', html)
        self.assertIn('btn-eam', html)

        # Ausência expressa de emojis (bolinhas coloridas) e termos informais
        self.assertNotIn('🟢', html)
        self.assertNotIn('🟡', html)
        self.assertNotIn('🔴', html)
        self.assertNotIn('beira do leito', html.lower())
        self.assertNotIn('beira leito', html.lower())

        # Coluna de Evidência Científica (Estudos de referência & Metanálise) na Matriz de Parâmetros
        self.assertIn('Evidência Científica (Estudos de referência & Metanálise)', html)

        # Letreiro Rolante de Dicas da Barra de Busca
        self.assertIn('searchPlaceholderMarquee', html)
        self.assertIn('marquee-track', html)

        # Presença do painel de monitoramento clínico e reavaliação
        self.assertIn('monitoring-rules-panel', html)
        self.assertIn('monitoringReeval', html)

    def test_05_css_tokens_and_hover_effects(self):
        """Verifica cores oficiais, dimensões de logo, centralização e transições de hover no stylesheet."""
        css_path = os.path.join(BASE_DIR, 'css', 'styles.css')
        self.assertTrue(os.path.exists(css_path))

        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()

        # Cores extraídas do site da NAPeN
        self.assertIn('#18C1C0', css) # Turquesa da barra
        self.assertIn('#0A6A6E', css) # Teal escuro no hover/ativo
        self.assertIn('#2C3070', css) # Deep Navy

        # Centralização da barra turquesa
        self.assertIn('justify-content: center;', css)

        # Proporção visual idêntica ao site NAPeN (Header 140px, Logo 112px)
        self.assertIn('height: 140px;', css)
        self.assertIn('height: 112px;', css)

        # Estilos dos novos componentes
        self.assertIn('evidence-reference-panel', css)
        self.assertIn('dual-calc-container', css)
        self.assertIn('calc-metric-pill', css)
        self.assertIn('calc-scale-tabs', css)
        self.assertIn('calc-eam-box', css)
        self.assertIn('btn-eam', css)
        self.assertIn('outcome-bullet', css)

        # Transição e submenus em cascata (2 níveis)
        self.assertIn('0.4s', css)
        self.assertIn('dropdown-menu-napen', css)
        self.assertIn('dropdown-submenu', css)

    def test_06_js_classes_and_syntax(self):
        """Verifica a integridade dos scripts ES6."""
        engine_js = os.path.join(BASE_DIR, 'js', 'decision-engine.js')
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')

        self.assertTrue(os.path.exists(engine_js))
        self.assertTrue(os.path.exists(app_js))

        with open(engine_js, 'r', encoding='utf-8') as f:
            e_code = f.read()
        self.assertIn('class DecisionEngine', e_code)
        self.assertIn('getFormattedGuideline', e_code)
        self.assertIn('calculateDelta', e_code)
        self.assertIn('setActiveScale', e_code)

        with open(app_js, 'r', encoding='utf-8') as f:
            a_code = f.read()
        self.assertIn('openConditionAlgorithm', a_code)
        self.assertIn('populateDropdownMenu', a_code)
        self.assertIn('handleScoreComputation', a_code)
        self.assertIn('renderCalculatorForActiveScale', a_code)
        self.assertIn('linkComoEfeitoCalculado', a_code)

        # Ausência de emojis e termos informais no JavaScript
        self.assertNotIn('🟢', a_code)
        self.assertNotIn('🟡', a_code)
        self.assertNotIn('🔴', a_code)
        self.assertNotIn('beira do leito', a_code.lower())
        self.assertNotIn('beira leito', a_code.lower())

        # Validação estrita de sintaxe JS via JavaScriptCore (jsc)
        jsc_bin = '/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc'
        if os.path.exists(jsc_bin):
            import subprocess
            data_js = os.path.join(BASE_DIR, 'js', 'data.js')
            scale_js = os.path.join(BASE_DIR, 'js', 'scale-guide-data.js')
            cmd = [
                jsc_bin,
                '-e', 'var window=this, document={addEventListener:function(){}, getElementById:function(){return {addEventListener:function(){}, classList:{add:function(){},remove:function(){},toggle:function(){}}};}};' ,
                data_js, scale_js, engine_js, app_js
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, f"Erro de compilação ou sintaxe JS: {res.stderr}")

    def test_07_scale_guide_and_language_switcher(self):
        """Verifica a presença e integridade do guia de aplicação de escalas e seletor de idiomas PT/EN."""
        scale_json = os.path.join(BASE_DIR, 'data', 'escalas_guia_clinico.json')
        scale_js = os.path.join(BASE_DIR, 'js', 'scale-guide-data.js')
        html_file = os.path.join(BASE_DIR, 'index.html')
        css_file = os.path.join(BASE_DIR, 'css', 'styles.css')
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')

        self.assertTrue(os.path.exists(scale_json))
        self.assertTrue(os.path.exists(scale_js))

        with open(scale_json, 'r', encoding='utf-8') as f:
            scales = json.load(f)
        
        # Deve cobrir as principais escalas clínicas dos roadmaps
        self.assertIn('eam', scales)
        self.assertIn('fma_ue', scales)
        self.assertIn('bbs', scales)
        self.assertIn('sara', scales)
        self.assertIn('ham_d', scales)
        self.assertIn('ham_a', scales)
        self.assertIn('pcl_5', scales)
        self.assertIn('eva', scales)
        self.assertIn('dn4', scales)
        self.assertIn('tug', scales)

        # Cada escala deve possuir procedimentos passo a passo, MCID e ABNT
        for k, sc in scales.items():
            self.assertTrue(len(sc.get('procedimento_passo_a_passo', [])) > 0, f"Escala {k} sem passos")
            self.assertIn('mcid', sc, f"Escala {k} sem MCID")
            self.assertIn('referencia_abnt', sc, f"Escala {k} sem referência ABNT")

        # HTML: Seletor de idioma retrátil oficial e Drawer do Guia Clínico
        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
        self.assertIn('langDropdownWrapper', html)
        self.assertIn('langCapsuleBtn', html)
        self.assertIn('langMenuExpanded', html)
        self.assertIn('scaleGuideDrawer', html)
        self.assertIn('btnOpenScaleGuideCalc', html)
        # Ausência da primeira ocorrência (ao lado da escala) e das dicas em botões conforme pedido
        self.assertNotIn('btnOpenScaleGuideMain', html)
        self.assertNotIn('searchQuickHints', html)

        # CSS: Estilos do seletor retrátil e drawer
        with open(css_file, 'r', encoding='utf-8') as f:
            css = f.read()
        self.assertIn('.lang-dropdown-wrapper', css)
        self.assertIn('.lang-capsule-btn', css)
        self.assertIn('.lang-menu-expanded', css)
        self.assertIn('.scale-guide-drawer', css)

        # JS: Funções do guia e do seletor retrátil
        with open(app_js, 'r', encoding='utf-8') as f:
            js = f.read()
        self.assertIn('openScaleGuide', js)
        self.assertIn('closeScaleGuide', js)
        self.assertIn('resolveScaleKey', js)
        self.assertIn('langCapsuleBtn', js)
        self.assertIn('langMenuExpanded', js)

    def test_08_neuroanatomical_search_tags(self):
        """Verifica se todas as condições possuem indexação neuroanatômica 10-20 e sinônimos em inglês."""
        json_file = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for c in data['condicoes']:
            cid = c['id']
            tags = c.get('tags_busca')
            self.assertIsNotNone(tags, f"Condição '{cid}' não possui tags_busca")
            self.assertTrue(len(tags.get('coordenadas_10_20', [])) > 0, f"Condição '{cid}' sem coordenadas 10-20")
            self.assertTrue(len(tags.get('sinonimos_en', [])) > 0, f"Condição '{cid}' sem sinônimos em inglês")
            self.assertTrue(len(tags.get('alvos_anatomicos', [])) > 0, f"Condição '{cid}' sem alvos anatômicos")

    def test_09_granular_scale_effects_and_synchronization(self):
        """Verifica se cada escala clínica em modalidades multiescala possui tamanho de efeito isolado."""
        json_file = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Verifica Ataxias (ataxia-cerebelar, equilíbrio): SARA e BBS devem ter tamanhos de efeito distintos e isolados
        atax = next(c for c in data['condicoes'] if c['id'] == 'ataxia-cerebelar')
        f_eq = atax['modalidades']['equilibrio']
        scales_atax = f_eq.get('escalas_detalhadas', [])
        self.assertEqual(len(scales_atax), 2)
        sara = next(s for s in scales_atax if s['id'] == 'sara')
        bbs = next(s for s in scales_atax if s['id'] == 'bbs')

        self.assertIn('14,8%', sara['tamanho_efeito'])
        self.assertNotIn('11,77%', sara['tamanho_efeito'])

        self.assertIn('11,77%', bbs['tamanho_efeito'])
        self.assertNotIn('14,8%', bbs['tamanho_efeito'])

        # Verifica integridade no app.js: sincronização dinâmica de tamanho de efeito e meta
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')
        with open(app_js, 'r', encoding='utf-8') as f:
            js = f.read()
        self.assertIn('activeScale?.tamanho_efeito', js)
        self.assertIn('calcRoadmapEffectText.textContent = eff', js)
        self.assertIn('prescEfeito.textContent = eff', js)

    def test_10_interactive_dropdown_and_menu_navigation(self):
        """Verifica se os menus e submenus possuem suporte a clique e abertura interativa garantidos."""
        html_file = os.path.join(BASE_DIR, 'index.html')
        css_file = os.path.join(BASE_DIR, 'css', 'styles.css')
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')

        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
        self.assertIn('id="navItemPrescription"', html)
        self.assertIn('id="tabBtnPrescription"', html)
        self.assertIn('id="dropdownConditionsList"', html)
        self.assertIn('id="tabBtnPocket"', html)
        self.assertIn('id="tabBtnMethod"', html)

        with open(css_file, 'r', encoding='utf-8') as f:
            css = f.read()
        self.assertIn('.nav-item.has-dropdown.dropdown-open .dropdown-menu-napen', css)
        self.assertIn('.dropdown-item-has-submenu.submenu-open > .dropdown-submenu', css)
        self.assertIn('.dropdown-item-has-submenu.submenu-open .axis-arrow-icon', css)
        # Na media query <= 992px, container não pode ter overflow-x: auto (que cortaria o dropdown)
        self.assertIn('overflow: visible;', css)

        with open(app_js, 'r', encoding='utf-8') as f:
            js = f.read()
        self.assertIn('function toggleDropdown()', js)
        self.assertIn('function closeDropdown()', js)
        self.assertIn('function openDropdown()', js)
        self.assertIn('tabBtnPrescription.addEventListener(\'click\'', js)
        self.assertIn('submenu-open', js)
        self.assertIn('dropdown-open', js)

    def test_11_calculator_fast_track_dropdown(self):
        """Verifica a nova aba da Calculadora de Resposta Clínica e navegação direta para o desfecho."""
        html_file = os.path.join(BASE_DIR, 'index.html')
        css_file = os.path.join(BASE_DIR, 'css', 'styles.css')
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')

        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
        self.assertIn('id="navItemCalc"', html)
        self.assertIn('id="tabBtnCalc"', html)
        self.assertIn('CALCULADORA DE RESPOSTA CLÍNICA', html)
        self.assertIn('id="dropdownCalcList"', html)
        self.assertNotIn('id="calcFastTrackBadge"', html)
        self.assertNotIn('Reavaliação Direta de Desfecho', html)
        self.assertNotIn('id="calcDeltaBadge"', html)

        with open(css_file, 'r', encoding='utf-8') as f:
            css = f.read()
        self.assertIn('.calc-highlight-pulse', css)
        self.assertIn('.calc-study-label', css)
        self.assertIn('calcPulseHighlight', css)
        self.assertIn('.dropdown-subsubmenu', css)
        self.assertIn('.dropdown-item-has-subsubmenu', css)
        self.assertIn('.dropdown-sublink-has-subsubmenu', css)
        self.assertIn('.dropdown-item-has-subsubmenu:hover > .dropdown-sublink-napen .axis-arrow-icon', css)

        with open(app_js, 'r', encoding='utf-8') as f:
            js = f.read()
        self.assertIn('function populateCalcDropdown()', js)
        self.assertIn('function navigateToCalculator(', js)
        self.assertIn('function toggleCalcDropdown()', js)
        self.assertIn('tabBtnCalc.addEventListener(\'click\'', js)
        self.assertIn('dropdown-subsubmenu', js)
        self.assertIn('dropdown-sublink-has-subsubmenu', js)
        self.assertIn('Acidente Vascular Cerebral', js)
        self.assertIn('targetScrollY', js)
        # Ausência de passos e textos redundantes
        self.assertNotIn('1. Selecione o Roadmap', js)
        self.assertNotIn('Escala sugerida:', js)

    def test_12_calculator_mcid_and_cohen_d_evidence(self):
        """Verifica a nova estrutura de MCID, estimativa de Cohen's d e ausência do termo seminal."""
        html_file = os.path.join(BASE_DIR, 'index.html')
        css_file = os.path.join(BASE_DIR, 'css', 'styles.css')
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')
        engine_js = os.path.join(BASE_DIR, 'js', 'decision-engine.js')
        json_file = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')

        # 1. Ausência completa da palavra "seminal"
        for filepath in [html_file, app_js, engine_js, json_file]:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().lower()
            self.assertNotIn('seminal', content, f"Termo 'seminal' encontrado indevidamente em {filepath}")

        # 2. Presença dos novos cards e elementos no HTML
        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
        self.assertIn('id="calcDeltaPoints"', html)
        self.assertIn('id="calcDeltaPercent"', html)
        self.assertIn('id="calcMcidBadge"', html)
        self.assertIn('id="calcStudyRef"', html)
        self.assertIn('id="calcStudyCohen"', html)
        self.assertIn('id="calcStudyMcid"', html)
        self.assertIn('id="calcComparisonBox"', html)

        # 3. Presença das classes no CSS
        with open(css_file, 'r', encoding='utf-8') as f:
            css = f.read()
        self.assertIn('.calc-metrics-dashboard', css)
        self.assertIn('.calc-metric-card', css)
        self.assertIn('.calc-study-reference-row', css)
        self.assertIn('.calc-evidence-metrics-grid', css)
        self.assertIn('.calc-dynamic-comparison-card', css)

        # 4. Estrutura de dados enriquecida com MCID e Cohen's d no JSON
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        avc = next(c for c in data['condicoes'] if c['id'] == 'avc-membro-superior')
        fraqueza = avc['modalidades']['fraqueza']
        self.assertIn('efeito_clinico', fraqueza)
        self.assertEqual(fraqueza['efeito_clinico']['mcid_valor'], 6.6)
        self.assertIn('Zheng', fraqueza['efeito_clinico']['estudo_referencia'])
        self.assertIn('cohen_d', fraqueza)
        self.assertIn('mcid_valor', fraqueza)

        # 5. Rigor estatístico na classificação de Cohen (ausência de classificações ambíguas)
        for filepath in [html_file, app_js, engine_js, json_file]:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().lower()
            self.assertNotIn('moderado a grande', content, f"Termo híbrido ambíguo 'moderado a grande' encontrado em {filepath}")

        # 6. Nomenclatura atualizada: 'Estudos de referência', 'Resultado Esperado na Literatura' e 'Desfecho Funcional & Meta do Ciclo'
        self.assertIn('Tamanho de Efeito Esperado (d de Cohen)', html)
        self.assertIn('Resultado Esperado na Literatura (IC 95%)', html)
        self.assertIn('Desfecho Funcional & Meta do Ciclo', html)
        self.assertIn('Estudos de referência', html)
        self.assertNotIn('Tamanho de Efeito Reportado:', html)
        self.assertNotIn('Ensaio Clínico Randomizado de Referência', html)

if __name__ == '__main__':
    unittest.main()

