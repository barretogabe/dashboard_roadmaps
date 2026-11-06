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
        self.assertIn('BIBLIOTECA DE EVIDÊNCIAS', html)
        self.assertNotIn('BIBLIOTECA DE EVIDÊNCIAS & METANÁLISES', html)
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

        # Versão Editorial Integrada no Subtítulo
        self.assertIn('Versão 2025-2026.', html)

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

        # Colunas de Evidência Científica na Biblioteca de Evidências
        self.assertIn('Ensaio Clínico de Referência', html)
        self.assertIn('Metanálise de Suporte', html)

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

        # 6. Nomenclatura atualizada: 'Estudos de referência', 'Resultado Esperado na Literatura' e dissociação de desfecho clínico alvo
        self.assertIn('Tamanho de Efeito Esperado (d de Cohen)', html)
        self.assertIn('Resultado Esperado na Literatura (IC 95%)', html)
        self.assertIn('Desfecho Clínico / Foco Funcional Alvo', html)
        self.assertIn('Instrumento de Avaliação:', html)
        self.assertIn('Estudos de referência', html)
        self.assertNotIn('Tamanho de Efeito Reportado:', html)
        self.assertNotIn('Ensaio Clínico Randomizado de Referência', html)

    def test_13_algoritmo_estratificacao_e_dissociacao_desfechos(self):
        """Verifica a estratificação real por PEM no AVC, ausência de 'Ajuste de Parâmetros' e dissociação estrita desfecho vs escala."""
        html_file = os.path.join(BASE_DIR, 'index.html')
        css_file = os.path.join(BASE_DIR, 'css', 'styles.css')
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')
        engine_js = os.path.join(BASE_DIR, 'js', 'decision-engine.js')
        json_file = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')

        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Painel de Triagem Neurofisiológica (PEM)
        self.assertIn('id="pemTriagePanel"', html)
        self.assertIn('id="btnPemSim"', html)
        self.assertIn('id="btnPemNao"', html)
        self.assertIn('Estratificação Neurofisiológica: Integridade Corticoespinhal', html)

        # 2. Ausência completa de "btnOutcomeWarning" e "Ajuste de Parâmetros" nos botões
        self.assertNotIn('id="btnOutcomeWarning"', html)
        self.assertNotIn('<span>Ajuste de Parâmetros</span>', html)
        self.assertIn('id="btnOutcomeSuccess"', html)
        self.assertIn('id="btnOutcomeDanger"', html)

        # 3. Dissociação explícita: Desfecho Clínico Alvo vs. Instrumento vs. Meta MCID
        self.assertIn('id="prescDesfechoNome"', html)
        self.assertIn('id="prescEscala"', html)
        self.assertIn('id="prescMeta"', html)

        # 4. Verificação no JSON da modalidade sem_pem (Protocolo 4 do RM01)
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        avc = next(c for c in data['condicoes'] if c['id'] == 'avc-membro-superior')
        self.assertIn('sem_pem', avc['modalidades'])
        sem_pem_mod = avc['modalidades']['sem_pem']
        self.assertIn('Protocolo 4', sem_pem_mod['tecnica'])
        self.assertEqual(sem_pem_mod['mcid_valor'], 3.7)

        # 5. CSS dos componentes
        with open(css_file, 'r', encoding='utf-8') as f:
            css = f.read()
        self.assertIn('.pem-triage-panel', css)
        self.assertIn('.btn-pem-choice', css)
        self.assertIn('.scale-panel-kicker', css)
        self.assertIn('.scale-target-outcome', css)
        self.assertIn('.scale-instrument-label', css)

        # 6. JS: ausência de listener para btnOutcomeWarning
        with open(app_js, 'r', encoding='utf-8') as f:
            js = f.read()
        self.assertNotIn('btnOutcomeWarning.addEventListener', js)
        self.assertIn('state.pemStatus', js)
        self.assertIn('prescDesfechoNome', js)

    def test_14_cascata_algoritmo_e_modalidades_v2(self):
        """Valida a árvore de decisão em cascata progressiva, suporte a rTMS/tDCS e higienização dos roadmaps."""
        html_file = os.path.join(BASE_DIR, 'index.html')
        css_file = os.path.join(BASE_DIR, 'css', 'styles.css')
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')
        engine_js = os.path.join(BASE_DIR, 'js', 'decision-engine.js')
        json_file = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')

        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
        with open(css_file, 'r', encoding='utf-8') as f:
            css = f.read()
        with open(app_js, 'r', encoding='utf-8') as f:
            js = f.read()
        with open(engine_js, 'r', encoding='utf-8') as f:
            engine_code = f.read()
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 1. Elementos no HTML
        self.assertIn('id="modalitySelectorBar"', html)
        self.assertIn('id="modalityPillsGroup"', html)
        self.assertIn('id="cascadingFlowContainer"', html)
        self.assertIn('id="prescAlvo"', html)
        self.assertIn('Montserrat', html)
        self.assertIn('Rua Almirante Tamandaré', html)
        self.assertIn('rede.napenm@gmail.com', html)
        self.assertIn('PEM Presente — Trato Corticoespinhal Preservado', html)
        self.assertIn('PEM Ausente — Integridade Corticoespinhal Não Preservada', html)

        # 2. Classes de Estilo no CSS
        self.assertIn('.modality-selector-bar', css)
        self.assertIn('.btn-modality-pill', css)
        self.assertIn('.cascading-flow-container', css)
        self.assertIn('.cascading-step-card', css)
        self.assertIn('.cascading-connector-line', css)
        self.assertIn('.cascading-active-path-summary', css)
        self.assertIn('Montserrat', css)

        # 3. Métodos no DecisionEngine
        self.assertIn('setModalityType', engine_code)
        self.assertIn('getActiveTree', engine_code)
        self.assertIn('setPathChoice', engine_code)
        self.assertIn('getPathChoice', engine_code)

        # 4. Funções no app.js
        self.assertIn('renderModalitySelector', js)
        self.assertIn('renderCascadingFlow', js)
        self.assertIn('prescAlvo', js)

        # 5. Estrutura de dados da árvore e suporte rTMS/tDCS no JSON
        avc = next(c for c in data['condicoes'] if c['id'] == 'avc-membro-superior')
        self.assertIn('modalidades_suportadas', avc)
        mods = [m['id'] for m in avc['modalidades_suportadas']]
        self.assertIn('rtms', mods)
        self.assertIn('tdcs', mods)

        self.assertIn('arvore_algoritmo', avc)
        self.assertIn('rtms', avc['arvore_algoritmo'])
        self.assertIn('tdcs', avc['arvore_algoritmo'])

        rtms_tree = avc['arvore_algoritmo']['rtms']
        self.assertEqual(rtms_tree['roadmap_id'], 'RM01')
        etapas_ids = [e['etapa_id'] for e in rtms_tree['etapas']]
        self.assertIn('fator_limitante', etapas_ids)
        self.assertIn('pem_triage', etapas_ids)
        self.assertIn('gravidade_fma', etapas_ids)
        self.assertIn('lesao_m1', etapas_ids)
        self.assertIn('lesao_s1', etapas_ids)

        tdcs_tree = avc['arvore_algoritmo']['tdcs']
        self.assertEqual(tdcs_tree['roadmap_id'], 'RM02')
        tdcs_etapas = [e['etapa_id'] for e in tdcs_tree['etapas']]
        self.assertIn('fator_limitante', tdcs_etapas)
        self.assertIn('lesao_tdcs_m1', tdcs_etapas)
        self.assertIn('extensao_dedos', tdcs_etapas)

        # 6. Rigor terminológico estrito: sem 'seminal', sem 'moderado a grande', e sem '(sim)'/ '(não)' redundantes no PEM
        for filepath in [html_file, css_file, app_js, engine_js, json_file]:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().lower()
            self.assertNotIn('seminal', content, f"Termo 'seminal' encontrado indevidamente em {filepath}")
            self.assertNotIn('moderado a grande', content, f"Termo 'moderado a grande' encontrado indevidamente em {filepath}")
        
        # Validação da ausência de PEM com (SIM)/(NÃO)
        self.assertNotIn('pem presente (sim)', html.lower())
        self.assertNotIn('pem ausente (não)', html.lower())

        # 7. Validação de ausência de pseudo-fatores limitantes (PEM é teste de estratificação, não queixa funcional)
        avc_fatores_ids = [f['id'] for f in avc['fatores_limitantes']]
        self.assertNotIn('sem_pem', avc_fatores_ids)
        for f in avc['fatores_limitantes']:
            self.assertNotIn('baixa integridade corticoespinhal', f['label'].lower())
            self.assertNotIn('sem pem', f['label'].lower())

    def test_15_ui_refinement_anti_ai_and_therapeutic_cascade(self):
        """Verifica as correções visuais anti-IA, badges institucionais e o algoritmo terapêutico completo."""
        html_file = os.path.join(BASE_DIR, 'index.html')
        css_file = os.path.join(BASE_DIR, 'css', 'styles.css')
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')
        json_file = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')

        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
        with open(css_file, 'r', encoding='utf-8') as f:
            css = f.read()
        with open(app_js, 'r', encoding='utf-8') as f:
            js = f.read()
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 1. Versão Editorial no Hero e ausência de caixas artificiais
        self.assertIn('Roadmaps e Algoritmos de Decisão Terapêutica Baseados em Evidências. Versão 2025-2026.', html)
        self.assertNotIn('hero-version-badge', html)
        self.assertNotIn('footer-version-tag', html)
        self.assertNotIn('menu turquesa acima', html.lower())

        # 2. Design Anti-IA, tokens refinados e ausência de molduras externas nos dropdowns
        self.assertIn('--radius-pill: 4px;', css)
        self.assertNotIn('.hero-version-badge', css)
        self.assertIn('.dropdown-submenu .axis-arrow-icon', css)
        self.assertIn('.adjustment-step-card', css)
        self.assertIn('.failure-therapeutic-card', css)
        self.assertIn('.btn-evidence-goto', css)
        self.assertIn('border: none !important;', css)
        self.assertIn('1pt solid', css)

        # 3. JavaScript - Pipeline completa sem ícones de IA
        self.assertNotIn('⚙', js)
        self.assertNotIn('⚠️', js)
        self.assertNotIn('🎯', js)
        self.assertIn("therapeuticStage: 'primary'", js)
        self.assertIn('switchTherapeuticStage', js)
        self.assertIn('closeDropdown', js)
        self.assertIn('closeCalcDropdown', js)
        self.assertIn('falha_terapeutica', js)
        self.assertIn('ajuste_parametros', js)

        # 4. JSON - Topologia completa do RM01 (AVC rTMS)
        avc = next(c for c in data['condicoes'] if c['id'] == 'avc-membro-superior')
        rtms = avc['arvore_algoritmo']['rtms']
        self.assertIn('ajuste_parametros', rtms)
        self.assertIn('protocolo_alternativo_2', rtms)
        self.assertIn('falha_terapeutica', rtms)

        falha = rtms['falha_terapeutica']
        self.assertEqual(falha['id'], 'RM01-FALHA')
        self.assertIn('critérios', falha.get('descricao', '').lower() or falha.get('criterios_definicao', '').lower())
        self.assertIn('condutas', falha)
        self.assertTrue(len(falha['condutas']) >= 3)

        # 5. Título Estrito da Biblioteca de Evidências e Higienização de Siglas
        self.assertIn('Biblioteca de Evidências', html)
        self.assertNotIn('Biblioteca de Evidências & Metanálises', html)
        self.assertNotIn('Tabela de Bolso', html)

        for cond in data['condicoes']:
            self.assertNotIn('(AVC)', cond['condicao'])
            self.assertNotIn('(Transtorno Depressivo Maior)', cond['condicao'])
            self.assertNotIn('(PC)', cond['condicao'])
            self.assertNotIn('(TEA)', cond['condicao'])
            self.assertNotIn('(CCL)', cond['condicao'])

        # 6. Extinção de Cards e Otimização de Margens Laterais no CSS
        self.assertIn('.pocket-table-container {\n  background-color: transparent;\n  border: none;\n  border-radius: 0;\n  overflow-x: auto;\n  box-shadow: none;\n  width: 100%;', css)
        self.assertIn('.pocket-table th {\n  background-color: var(--napen-teal-dark);\n  color: #FFFFFF;\n  font-weight: 700;\n  padding: 12px 14px;\n  text-align: left;\n  white-space: normal;', css)

    def test_16_lesao_prefrontal_distinct_protocols(self):
        """Valida diferenciação dos Protocolos 4 (Cerebelar) e 5 (Pré-motor) em Lesão Pré-Frontal."""
        json_path = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        avc = next(c for c in data['condicoes'] if c['id'] == 'avc-membro-superior')
        mods = avc['modalidades']

        # Protocolo 4 - Cerebelar
        self.assertIn('sem_pem_cerebelar', mods)
        self.assertIn('Cerebelar', mods['sem_pem_cerebelar']['alvo'])
        self.assertIn('Wang', mods['sem_pem_cerebelar']['artigo_referencia']['autores'])

        # Protocolo 5 - Pré-Motor
        self.assertIn('sem_pem_premotor', mods)
        self.assertIn('Pré-Motor', mods['sem_pem_premotor']['alvo'])
        self.assertIn('Lefaucheur', mods['sem_pem_premotor']['artigo_referencia']['autores'])

        # Protocolos devem ser clinicamente distintos
        self.assertNotEqual(mods['sem_pem_cerebelar']['alvo'], mods['sem_pem_premotor']['alvo'])
        self.assertNotEqual(mods['sem_pem_cerebelar']['tecnica'], mods['sem_pem_premotor']['tecnica'])

        # Validação na árvore topológica
        tree = avc['arvore_algoritmo']['rtms']
        lesao_step = next(s for s in tree['etapas'] if s['etapa_id'] == 'lesao_m1')
        opt_sim = next(o for o in lesao_step['opcoes'] if o['id'] == 'lesao_prefrontal_sim')
        opt_nao = next(o for o in lesao_step['opcoes'] if o['id'] == 'lesao_prefrontal_nao')

        self.assertEqual(opt_sim['modalidade_chave'], 'sem_pem_cerebelar')
        self.assertEqual(opt_nao['modalidade_chave'], 'sem_pem_premotor')

if __name__ == '__main__':
    unittest.main()



