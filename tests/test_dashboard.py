#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Suíte de Testes Automatizados da Plataforma de Prescrição Clínica
Valida integridade do cabeçalho estrito, menu com hover dropdown,
ausência de ícones/redes desnecessários, e fluxo de seleção sob demanda.
"""

import os
import json
import subprocess
import tempfile
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
        self.assertIn('Protocolos e Algoritmos de Decisão Terapêutica Baseados em Evidências', html)

        # Botão Exclusivo do Portal da Rede NAPeN
        self.assertIn('Retornar ao Portal da Rede NAPeN', html)

        # Itens do Menu na Barra Turquesa Oficial (SEM emojis e SEM ?)
        self.assertIn('PRESCRIÇÃO INTERATIVA', html)
        self.assertIn('BIBLIOTECA DE EVIDÊNCIAS', html)
        self.assertNotIn('BIBLIOTECA DE EVIDÊNCIAS & METANÁLISES', html)
        self.assertIn('COMO OS PROTOCOLOS CLÍNICOS FORAM DESENVOLVIDOS', html)
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

        self.assertIn('9,1%', sara['meta_texto'])
        self.assertNotIn('11,77%', sara['meta_texto'])
        self.assertIsInstance(sara['tamanho_efeito'], (int, float))

        self.assertIn('11,77%', bbs['meta_texto'])
        self.assertNotIn('14,8%', bbs['meta_texto'])
        self.assertIsInstance(bbs['tamanho_efeito'], (int, float))

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

    def test_11_calculator_fast_track_removed_from_navbar(self):
        """Verifica Opção A: remoção da aba Calculadora da navbar (centralização na homepage) mantendo estilos de destaque."""
        html_file = os.path.join(BASE_DIR, 'index.html')
        css_file = os.path.join(BASE_DIR, 'css', 'styles.css')
        app_js = os.path.join(BASE_DIR, 'js', 'app.js')

        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
        self.assertIn('id="navItemPrescription"', html)
        self.assertIn('id="dropdownConditionsList"', html)
        self.assertNotIn('id="navItemCalc"', html)
        self.assertNotIn('id="tabBtnCalc"', html)
        self.assertNotIn('id="dropdownCalcList"', html)
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

        with open(app_js, 'r', encoding='utf-8') as f:
            js = f.read()
        self.assertNotIn('function populateCalcDropdown()', js)
        self.assertNotIn('function navigateToCalculator(', js)
        self.assertNotIn('function toggleCalcDropdown()', js)
        self.assertNotIn('tabBtnCalc.addEventListener', js)
        self.assertIn('shortcut-to-calc', html + js)
        self.assertIn('id="btnScrollToTolGuide"', html)
        self.assertIn('scrollToTolerabilityGuide', js)
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
        self.assertEqual(fraqueza['efeito_clinico']['mcid_valor'], 5.0)
        self.assertIn('Guo', fraqueza['efeito_clinico']['estudo_referencia'])
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

        # 2. Ausência completa de "btnOutcomeWarning", "btnOutcomeAdjust" e "Ajuste de Parâmetros" nos botões
        self.assertNotIn('id="btnOutcomeWarning"', html)
        self.assertNotIn('id="btnOutcomeAdjust"', html)
        self.assertNotIn('data-home-stage="adjustment"', html)
        self.assertNotIn('<span>Ajuste de Parâmetros</span>', html)
        self.assertIn('id="btnOutcomeSuccess"', html)
        self.assertIn('id="btnOutcomeDanger"', html)
        self.assertIn('id="tolerabilityDoseGuidePanel"', html)

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
        self.assertIn('Protocolos e Algoritmos de Decisão Terapêutica Baseados em Evidências. Versão 2025-2026.', html)
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
        engine_js = os.path.join(BASE_DIR, 'js', 'decision-engine.js')
        with open(app_js, 'r', encoding='utf-8') as f:
            js = f.read()
        with open(engine_js, 'r', encoding='utf-8') as f:
            eng = f.read()
        self.assertNotIn('⚙', js)
        self.assertNotIn('⚠️', js)
        self.assertNotIn('🎯', js)
        self.assertIn("therapeuticStage: 'primary'", js)
        self.assertIn('switchTherapeuticStage', js)
        self.assertIn('closeDropdown', js)
        self.assertNotIn('closeCalcDropdown', js)
        self.assertIn("getPrescriptionForStage('failure')", js)
        self.assertNotIn("getPrescriptionForStage('adjustment')", js)
        self.assertIn('scrollToTolerabilityGuide', js)
        self.assertIn('falha_terapeutica', eng)
        self.assertIn('ajuste_parametros', eng)

        # 4. JSON - Topologia completa do RM01 (AVC rTMS)
        avc = next(c for c in data['condicoes'] if c['id'] == 'avc-membro-superior')
        rtms = avc['arvore_algoritmo']['rtms']
        self.assertIn('ajuste_parametros', rtms)
        self.assertIn('protocolo_alternativo_2', rtms)
        self.assertIn('falha_terapeutica', rtms)

        falha = rtms['falha_terapeutica']
        self.assertEqual(falha['id'], 'RM01-FALHA')
        self.assertIn('ausência de resposta clínica', falha.get('criterios_definicao', '').lower())
        self.assertTrue(len(falha.get('descricao', '')) > 20)
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
        """Valida diferenciação dos caminhos sem PEM no RM01: Wang 2022 (M1 contralesional) vs Guo 2016 (M1 ipsilesional)."""
        json_path = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        avc = next(c for c in data['condicoes'] if c['id'] == 'avc-membro-superior')
        mods = avc['modalidades']

        # Caminho sem PEM com lesão cortical extensa no giro pré-frontal - M1 Contralesional (Wang et al., 2022)
        self.assertIn('sem_pem', mods)
        self.assertIn('CONTRALESIONAL', mods['sem_pem']['alvo'].upper())
        self.assertIn('Wang', mods['sem_pem']['artigo_referencia']['autores'])

        # Caminho sem PEM sem lesão extensa no giro pré-frontal - M1 Ipsilesional (Guo et al., 2016)
        self.assertIn('sem_pem_ipsilesional', mods)
        self.assertIn('IPSILESIONAL', mods['sem_pem_ipsilesional']['alvo'].upper())
        self.assertIn('Guo', mods['sem_pem_ipsilesional']['artigo_referencia']['autores'])

        # Protocolos devem ser clinicamente distintos
        self.assertNotEqual(mods['sem_pem']['alvo'], mods['sem_pem_ipsilesional']['alvo'])
        self.assertNotEqual(mods['sem_pem']['tecnica'], mods['sem_pem_ipsilesional']['tecnica'])

        # Validação na árvore topológica
        tree = avc['arvore_algoritmo']['rtms']
        lesao_step = next(s for s in tree['etapas'] if s['etapa_id'] == 'lesao_m1')
        opt_sim = next(o for o in lesao_step['opcoes'] if o['id'] == 'lesao_prefrontal_sim')
        opt_nao = next(o for o in lesao_step['opcoes'] if o['id'] == 'lesao_prefrontal_nao')

        self.assertEqual(opt_sim['modalidade_chave'], 'sem_pem')
        self.assertEqual(opt_nao['modalidade_chave'], 'sem_pem_ipsilesional')

    def test_17_continuity_shortcut_elements(self):
        """Valida o atalho de continuidade clínica ('O paciente já realizou algum protocolo?') na UI e no motor."""
        html_path = os.path.join(BASE_DIR, 'index.html')
        app_path = os.path.join(BASE_DIR, 'js', 'app.js')
        engine_path = os.path.join(BASE_DIR, 'js', 'decision-engine.js')
        css_path = os.path.join(BASE_DIR, 'css', 'styles.css')

        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        with open(app_path, 'r', encoding='utf-8') as f:
            app_js = f.read()
        with open(engine_path, 'r', encoding='utf-8') as f:
            engine_js = f.read()
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()

        self.assertIn('O paciente já realizou ou iniciou algum protocolo para alguma condição presente nesta plataforma?', html)
        self.assertIn('id="homeContinuityPanel"', html)
        self.assertIn('id="btnHomeEntryNew"', html)
        self.assertIn('id="btnHomeEntryReturning"', html)
        self.assertIn('id="homeContinuityQuickPanel"', html)
        self.assertIn('id="homeContCondition"', html)
        self.assertIn('id="homeContProtocol"', html)
        self.assertIn('id="btnSwitchToContinuing"', html)
        self.assertIn('id="continuityEntryBar"', html)
        self.assertIn('id="continuityCompactBar"', html)
        self.assertIn('id="continuingStageFocusSlot"', html)

        # Pergunta deve estar dentro da homepage (#searchHeroPanel), antes de #algorithmActiveContainer
        self.assertLess(
            html.index('O paciente já realizou ou iniciou algum protocolo para alguma condição presente nesta plataforma?'),
            html.index('id="algorithmActiveContainer"'),
            'A pergunta inicial de continuidade deve ficar na homepage (#searchHeroPanel)'
        )
        # Sem pergunta binária duplicada dentro da tela interna da condição
        self.assertNotIn('id="btnEntryNew"', html)
        self.assertNotIn('id="btnEntryReturning"', html)

        self.assertIn('setEntryMode', engine_js)
        self.assertIn('getPrescriptionForStage', engine_js)
        self.assertIn('renderContinuingFocusSlot', app_js)
        self.assertIn('renderHomeContinuityPanel', app_js)
        self.assertIn('.home-continuity-panel', css)
        self.assertIn('.continuing-focus-slot', css)

        # Sem balões/pílulas elipsoides nos novos controles
        new_css_block = css[css.index('.home-continuity-panel'):]
        self.assertNotIn('9999px', new_css_block)
        self.assertIn('.evidence-tag-grade', new_css_block)
        self.assertIn('.btn-tolerability', new_css_block)

    def test_18_clinical_response_tolerability_matrix(self):
        """Valida critérios multidimensionais (escore + tolerabilidade + Guia Estratégico + Banco NAPeN) no HTML e via JavaScriptCore."""
        import subprocess

        html_path = os.path.join(BASE_DIR, 'index.html')
        engine_path = os.path.join(BASE_DIR, 'js', 'decision-engine.js')
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        with open(engine_path, 'r', encoding='utf-8') as f:
            engine_js = f.read()

        self.assertIn('id="tolerabilityOptionsGrid"', html)
        self.assertNotIn('id="btnOutcomeAdjust"', html)
        self.assertIn('id="tolerabilityDoseGuidePanel"', html)
        self.assertIn('id="tolGuideTolerance"', html)
        self.assertIn('id="tolGuideDose"', html)
        self.assertIn('id="tolGuideCalibration"', html)
        self.assertIn('Critério Individual de Resposta Insatisfatória', html)
        self.assertIn('evaluateClinicalResponse', engine_js)
        self.assertIn('https://www.neuromodulation-net.com/banco-efeitos-adversos-napen', engine_js)

        jsc_bin = '/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc'
        if os.path.exists(jsc_bin):
            sim_code = """
            var eng = new DecisionEngine(window.NAPEN_DATA);
            eng.setCondition('doenca-parkinson', { preserveEntryMode: true, entryMode: 'returning', continuingStage: 'alt1' });
            if (eng.entryMode !== 'returning' || eng.continuingStage !== 'alt1') {
              throw new Error('Falha ao preservar entryMode/continuingStage vindo da homepage');
            }

            eng.setCondition('avc-membro-superior');
            eng.setFactor('fraqueza');

            // 1. Continuidade (sem etapa sintética 'adjustment')
            eng.setEntryMode('returning', 'alt1');
            var alt1 = eng.getPrescriptionForStage('alt1');
            if (!alt1 || alt1.stage !== 'alt1') throw new Error('Falha em getPrescriptionForStage(alt1)');
            eng.setContinuingStage('failure');
            var failStage = eng.getPrescriptionForStage('failure');
            if (!failStage || failStage.stage !== 'failure') throw new Error('Falha em getPrescriptionForStage(failure)');
            if (eng.getPrescriptionForStage('adjustment') !== null) {
              throw new Error('Etapa sintética adjustment deveria retornar null');
            }
            eng.setEntryMode('new');

            // 2. Evidência GRADE & AMSTAR 2 carregada
            var eq = eng.getEvidenceQuality();
            if (!eq.grade || !eq.amstar2 || eq.grade.status_homologacao.indexOf('homologação') === -1) {
              throw new Error('Metadados GRADE/AMSTAR 2 ausentes ou sem marcador de homologação');
            }

            // 3. Evento adverso grave sobrepõe MCID atingida
            var deltaOk = { isSuccess: true, mcidMet: true, isImproved: true, delta: 8, percentFormatted: '+40%', mcidLabel: '>= 6,6' };
            var rGrave = eng.evaluateClinicalResponse(deltaOk, 'grave');
            if (rGrave.recommendationType !== 'adverse_halt' || rGrave.recommendedStage !== 'failure' || !rGrave.needsAdverseReport) {
              throw new Error('Evento grave não sobrepôs sucesso numérico: ' + JSON.stringify(rGrave));
            }

            // 4. MCID atingida + intolerância aponta para guia estratégico de tolerabilidade (warning_tol)
            var rIntol = eng.evaluateClinicalResponse(deltaOk, 'intolerante');
            if (rIntol.recommendationType !== 'warning_tol' || rIntol.scrollGuideTarget !== 'tolerabilityDoseGuidePanel') {
              throw new Error('Intolerância com MCID não retornou warning_tol/tolerabilityDoseGuidePanel: ' + JSON.stringify(rIntol));
            }

            // 5. Melhora parcial (< MCID) + boa tolerabilidade avança diretamente ao próximo protocolo (alt1, depois alt2)
            var deltaPartial = { isSuccess: true, mcidMet: false, isImproved: true, delta: 3, percentFormatted: '+15%', mcidLabel: '>= 6,6' };
            var rPartial = eng.evaluateClinicalResponse(deltaPartial, 'boa');
            if (rPartial.recommendationType !== 'danger' || rPartial.recommendedStage !== 'alt1') {
              throw new Error('Melhora parcial (< MCID) não avançou diretamente para alt1: ' + JSON.stringify(rPartial));
            }
            eng.setEntryMode('returning', 'alt1');
            var rAltNext = eng.evaluateClinicalResponse(deltaPartial, 'boa');
            if (rAltNext.recommendationType !== 'danger' || rAltNext.recommendedStage !== 'alt2') {
              throw new Error('Melhora parcial (< MCID) em alt1 não avançou para alt2: ' + JSON.stringify(rAltNext));
            }

            // 6. Cadeia de protocolo único com < MCID avança diretamente para failure
            eng.setCondition('paralisia-cerebral');
            eng.setFactor('pc_estab_dip');
            var rSingleFail = eng.evaluateClinicalResponse(deltaPartial, 'boa');
            if (rSingleFail.recommendationType !== 'danger' || rSingleFail.recommendedStage !== 'failure') {
              throw new Error('Cadeia única com < MCID não avançou diretamente para failure: ' + JSON.stringify(rSingleFail));
            }

            print('JSC_SIM_OK');
            """
            res = subprocess.run(
                [jsc_bin, '-e', 'var window = {};', 'js/data.js', 'js/decision-engine.js', '-e', sim_code],
                cwd=BASE_DIR,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(res.returncode, 0, f"Erro no jsc: {res.stderr}\n{res.stdout}")
            self.assertIn('JSC_SIM_OK', res.stdout)

    def test_19_grade_and_amstar2_metadata(self):
        """Valida presença de GRADE, AMSTAR 2 em todas as 78 modalidades/subprotocolos e remoção de DOIs legados inválidos."""
        json_path = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
        html_path = os.path.join(BASE_DIR, 'index.html')
        app_path = os.path.join(BASE_DIR, 'js', 'app.js')

        with open(json_path, 'r', encoding='utf-8') as f:
            raw_json = f.read()
            data = json.loads(raw_json)
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        with open(app_path, 'r', encoding='utf-8') as f:
            app_js = f.read()

        # Seção 4 Metodológica e badges na interface
        self.assertIn('id="metodologia-grade-amstar"', html)
        self.assertIn('id="evidenceGradeBadge"', html)
        self.assertIn('id="evidenceAmstarBadge"', html)
        self.assertIn('AMSTAR 2:', app_js)
        self.assertIn('GRADE:', app_js)

        # Remoção definitiva de DOIs legados quebrados/fictícios
        invalid_dois = [
            '10.3389/fneur.2019.00633',
            '10.1186/s12984-023-01208-1',
            '10.1016/j.arr.2023.101952',
            '10.1177/02692155211070862',
            '10.1002/mds.28472',
        ]
        for bad_doi in invalid_dois:
            self.assertNotIn(bad_doi, raw_json, f"DOI legado inválido ainda presente no JSON: {bad_doi}")

        total_mods = 0
        for c in data['condicoes']:
            for k, m in c.get('modalidades', {}).items():
                total_mods += 1
                grade = m.get('grade')
                amstar2 = (m.get('meta_analise') or {}).get('amstar2')
                self.assertIsNotNone(grade, f"GRADE ausente em {c['id']}::{k}")
                self.assertIsNotNone(amstar2, f"AMSTAR 2 ausente em {c['id']}::{k}")
                self.assertIn(grade.get('certeza'), ['Alta', 'Moderada', 'Baixa', 'Muito Baixa'])
                self.assertIn(amstar2.get('nivel'), ['Alta', 'Moderada', 'Baixa', 'Criticamente Baixa'])
                self.assertIn('homologação', grade.get('status_homologacao', '').lower())
                self.assertIn('homologação', amstar2.get('status_homologacao', '').lower())
                self.assertIn('tolerabilidade_roadmap', m)
                self.assertIn('titulo', m.get('meta_analise', {}))

        self.assertEqual(total_mods, 78)

    def test_20_full_18_roadmaps_trees_and_contextual_observations(self):
        """Valida integralmente as 13 condições (18 roadmaps / 77 protocolos), 10 slots cirúrgicos, 52 escalas e execução real em JavaScriptCore."""
        json_path = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
        scale_path = os.path.join(BASE_DIR, 'data', 'escalas_guia_clinico.json')
        html_path = os.path.join(BASE_DIR, 'index.html')
        app_path = os.path.join(BASE_DIR, 'js', 'app.js')
        engine_path = os.path.join(BASE_DIR, 'js', 'decision-engine.js')

        with open(json_path, 'r', encoding='utf-8') as f:
            raw_json = f.read()
        data = json.loads(raw_json)

        with open(scale_path, 'r', encoding='utf-8') as f:
            scales = json.load(f)
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        with open(app_path, 'r', encoding='utf-8') as f:
            app_js = f.read()
        with open(engine_path, 'r', encoding='utf-8') as f:
            engine_js = f.read()

        # 1. Cobertura completa das 13 condições e dos 10 slots contextuais
        self.assertEqual(len(data['condicoes']), 13)
        all_slots = set()
        for c in data['condicoes']:
            trees = c.get('arvore_algoritmo', {})
            self.assertTrue(len(trees) >= 1, f"Sem árvore em {c['id']}")
            for mkey, tree in trees.items():
                etapas = tree.get('etapas', [])
                self.assertTrue(len(etapas) >= 1, f"Árvore vazia em {c['id']}::{mkey}")
                self.assertEqual(etapas[0]['etapa_id'], 'fator_limitante')
            for obs in c.get('observacoes_contextuais', []):
                all_slots.add(obs['slot'])

        expected_slots = {'pre', 'step', 'tec', 'alvo', 'intensidade', 'sessoes', 'scale', 'reeval', 'tol', 'stage'}
        self.assertEqual(all_slots, expected_slots)

        # 2. Slots cirúrgicos e DOI oficial do guia PEM no HTML e app.js
        for dom_id in [
            'preTriagemObservationsSlot', 'prescObsTecnica', 'prescObsAlvo',
            'prescObsIntensidade', 'prescObsSessoes', 'prescObsEscala', 'evidencePemGuide'
        ]:
            self.assertIn(f'id="{dom_id}"', html)
            self.assertIn(dom_id, app_js)

        pem_doi = '10.17267/2965-3738bis.2023.e5097'
        self.assertIn(pem_doi, html)
        self.assertIn(pem_doi, raw_json)

        # 3. 52 escalas oficiais, UPDRS-III ON e restrição privativa de psicólogos
        self.assertEqual(len(scales), 52)
        updrs_str = json.dumps(scales['updrs_iii'], ensure_ascii=False)
        self.assertIn('estado ON', updrs_str)
        self.assertNotIn('estado OFF', updrs_str)
        for priv_key in ['d2_psico', 'wais_digitos', 'teste_trilhas']:
            self.assertTrue(scales[priv_key].get('uso_privativo_psicologo'), f"Flag ausente em {priv_key}")
        self.assertIn('uso_privativo_psicologo', app_js)
        self.assertIn('Lei nº 4.119/1962', app_js)

        # 4. Proibição estrita de siglas redundantes e jargões banidos
        for c in data['condicoes']:
            for sigla in ['(AVC)', '(TAG)', '(TEPT)', '(PC)', '(TEA)', '(CCL)', '(Transtorno Depressivo Maior)']:
                self.assertNotIn(sigla, c['condicao'])
            for fl in c.get('fatores_limitantes', []):
                for bad_scale in ['(TUG', '(SARA', '(9HPT', '(HAM-A']:
                    self.assertNotIn(bad_scale, fl['label'])

        for token in ['posologia', 'beira do leito', 'seminal', 'moderado a grande']:
            self.assertNotIn(token, raw_json.lower())
            self.assertNotIn(token, app_js.lower())
            self.assertNotIn(token, engine_js.lower())

        # 5. Execução comportamental real do motor e carga completa no JavaScriptCore
        jsc_bin = '/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc'
        if os.path.exists(jsc_bin):
            js_test_script = r'''
var window = {
  addEventListener: function(){},
  scrollTo: function(){},
  pageYOffset: 0,
  location: { hash: '' },
  NAPEN_SCALE_GUIDE: null,
  NAPEN_DATA: null
};
var _listeners = {};
function makeEl() {
  return {
    style: {},
    value: '',
    textContent: '',
    innerHTML: '',
    options: [],
    selectedIndex: 0,
    classList: { add: function(){}, remove: function(){}, toggle: function(){}, contains: function(){ return false; } },
    setAttribute: function(){},
    getAttribute: function(){ return null; },
    addEventListener: function(){},
    appendChild: function(){},
    querySelector: function(){ return null; },
    querySelectorAll: function(){ return []; },
    closest: function(){ return null; },
    getBoundingClientRect: function(){ return { top: 0 }; }
  };
}
var document = {
  addEventListener: function(ev, fn) { _listeners[ev] = _listeners[ev] || []; _listeners[ev].push(fn); },
  getElementById: function() { return makeEl(); },
  querySelector: function() { return makeEl(); },
  querySelectorAll: function() { return []; },
  createElement: function() { return makeEl(); }
};

load('js/data.js');
load('js/scale-guide-data.js');
load('js/decision-engine.js');
load('js/app.js');

if (_listeners['DOMContentLoaded']) {
  _listeners['DOMContentLoaded'].forEach(function(fn) { fn(); });
}

var eng = new DecisionEngine(window.NAPEN_DATA);
function assert(cond, msg) {
  if (!cond) throw new Error('JSC ASSERT FAILED: ' + msg);
}

// A. RM01: PEM sim vs PEM não (RM01-PEM-DOI & RM01-N05-CONTRALESIONAL)
eng.setCondition('avc-membro-superior', { modalityType: 'rtms' });
eng.setPathChoice('fator_limitante', 'espasticidade');
eng.setPathChoice('pem_triage', 'pem_sim');
var stepPemSim = eng.getContextualObservations({ slot: 'step', etapaId: 'pem_triage', optionId: 'pem_sim' });
assert(stepPemSim.some(function(o){ return o.id === 'RM01-PEM-DOI'; }), 'RM01-PEM-DOI missing in pem_sim');
assert(!stepPemSim.some(function(o){ return o.id === 'RM01-N05-CONTRALESIONAL'; }), 'RM01-N05 must NOT fire in pem_sim');

eng.setPathChoice('pem_triage', 'pem_nao');
var stepPemNao = eng.getContextualObservations({ slot: 'step', etapaId: 'pem_triage', optionId: 'pem_nao' });
assert(stepPemNao.some(function(o){ return o.id === 'RM01-N05-CONTRALESIONAL'; }), 'RM01-N05 must fire in pem_nao');

// B. Multi-step chains (> 2 protocolos): Afasia RM09 e Disfagia RM07
eng.setCondition('avc-afasia', { modalityType: 'rtms' });
assert(eng.getProtocolChain().length >= 5, 'RM09 chain < 5');
assert(eng.getPrescriptionForStage('alt3') !== null, 'RM09 alt3 null');
eng.setCondition('avc-disfagia', { modalityType: 'rtms' });
assert(eng.getProtocolChain().length >= 4, 'RM07 default chain < 4');
eng.setFactor('rtms_cortical_extensa', false);
assert(eng.getProtocolChain().length >= 6, 'RM07 rtms_cortical_extensa chain < 6');
assert(eng.getPrescriptionForStage('alt4') !== null, 'RM07 alt4 null');

// C. Dor neuropática (RM05): bobina 45° apenas em rTMS ('dor_geral') + corte <20% EVA
eng.setCondition('dor-neuropatica');
eng.setPathChoice('indicacao_especifica', 'dor_geral');
var obsDorRtms = eng.getContextualObservations({});
assert(obsDorRtms.some(function(o){ return o.id === 'RM05-BOBINA-45'; }), 'RM05-BOBINA-45 missing in rTMS');
var mDor = eng.getActiveModality();
var sEva = eng.getActiveScale();
var deltaDor15 = eng.calculateDelta(10, 8.5, sEva, mDor);
var evalDor15 = eng.evaluateClinicalResponse(deltaDor15, 'boa');
assert(evalDor15.recommendationType !== 'success', 'RM05 <20% EVA should not be success');

eng.setPathChoice('indicacao_especifica', 'dor_fantasma');
var obsDorTdcs = eng.getContextualObservations({});
assert(!obsDorTdcs.some(function(o){ return o.id === 'RM05-BOBINA-45'; }), 'RM05-BOBINA-45 leaked into tDCS');

// D. TEPT (RM18): corte <25% CAPS/PCL-5
eng.setCondition('tept');
var mTept = eng.getActiveModality();
var sPcl = eng.getActiveScale();
var deltaTept15 = eng.calculateDelta(60, 51, sPcl, mTept);
var evalTept15 = eng.evaluateClinicalResponse(deltaTept15, 'boa');
assert(evalTept15.recommendationType !== 'success', 'RM18 <25% must not be success');

// E. Todas as 52 escalas presentes no NAPEN_SCALE_GUIDE
assert(Object.keys(window.NAPEN_SCALE_GUIDE).length === 52, 'Expected 52 scales in JS guide');
print('JSC_SUITE_OK');
'''
            with tempfile.NamedTemporaryFile('w', suffix='.js', encoding='utf-8', delete=False) as tf:
                tf.write(js_test_script)
                tmp_js = tf.name
            try:
                proc = subprocess.run(
                    [jsc_bin, tmp_js],
                    cwd=BASE_DIR,
                    capture_output=True,
                    text=True,
                    timeout=15
                )
                self.assertEqual(proc.returncode, 0, f"JSC error: {proc.stderr}\n{proc.stdout}")
                self.assertIn('JSC_SUITE_OK', proc.stdout)
            finally:
                if os.path.exists(tmp_js):
                    os.remove(tmp_js)

    def test_21_comprehensive_18_roadmaps_audit(self):
        """Auditoria integral pós-revisão: zero códigos visíveis, higiene de tolerabilidade, fidelidade RM01-RM18 e Guia de Tolerabilidade."""
        import re
        import subprocess
        import tempfile

        code_pat = re.compile(r'\bRM\d{2}\b|\bNota N\d+|\bNota [IVX]+\b|\bConsidera[çc][ãa]o [IVX]+\b|nota PDF|\bRef\.\s*\[?\d', re.I)
        therapy_pat = re.compile(r'fisioterap|fonoterap|terapia de reabilita|treino motor|exerc[íi]cio', re.I)
        tech_keys = {'id', 'roadmap_id', 'svg_file', 'protocolo_id', 'redirecionar_para_protocolo'}

        def scan_codes(obj, path=''):
            hits = []
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k in tech_keys:
                        continue
                    p = f'{path}.{k}' if path else k
                    if isinstance(v, str) and code_pat.search(v):
                        hits.append((p, v[:120]))
                    else:
                        hits.extend(scan_codes(v, p))
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    hits.extend(scan_codes(item, f'{path}[{i}]'))
            return hits

        def scan_therapy_in_tol(obj, path=''):
            hits = []
            if isinstance(obj, dict):
                for k, v in obj.items():
                    p = f'{path}.{k}' if path else k
                    if isinstance(v, str):
                        if k == 'tolerabilidade_roadmap' and therapy_pat.search(v):
                            hits.append((p, v[:120]))
                        elif k == 'tolerabilidade' and 'ajuste_parametros' in p and therapy_pat.search(v):
                            hits.append((p, v[:120]))
                        elif k == 'texto' and obj.get('slot') == 'tol' and therapy_pat.search(v):
                            hits.append((p, v[:120]))
                    else:
                        hits.extend(scan_therapy_in_tol(v, p))
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    hits.extend(scan_therapy_in_tol(item, f'{path}[{i}]'))
            return hits

        for rel in ['data/napen_roadmaps_data.json', 'data/grade_amstar_audit.json', 'data/escalas_guia_clinico.json']:
            with open(os.path.join(BASE_DIR, rel), 'r', encoding='utf-8') as f:
                payload = json.load(f)
            self.assertEqual(scan_codes(payload, rel), [], f"Códigos internos visíveis encontrados em {rel}")
            self.assertEqual(scan_therapy_in_tol(payload, rel), [], f"Fisioterapia/terapia encontrada no campo tolerabilidade de {rel}")

        with open(os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json'), 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 1. Nomes oficiais dos fatores limitantes do AVC Membro Superior
        avc_ms = next(c for c in data['condicoes'] if c['id'] == 'avc-membro-superior')
        factor_names = [f['nome'] for f in avc_ms['fatores_limitantes']]
        for expected in ['Perda de sinergia', 'Espasticidade', 'Fraqueza muscular', 'Disfunção motora', 'Disfunção sensorial', 'Heminegligência']:
            self.assertIn(expected, factor_names)

        # 2. PC Distonia = 2 sessões e TEA Comunicação Protocolo 2 tDCS Bifrontal (Zemestani)
        pc = next(c for c in data['condicoes'] if c['id'] == 'paralisia-cerebral')
        self.assertIn('2 sessões', pc['modalidades']['pc_distonia']['sessoes'])
        tea = next(c for c in data['condicoes'] if c['id'] == 'transtorno-espectro-autista')
        tea_alt = tea['modalidades']['tea_comunicacao'].get('protocolo_alternativo') or {}
        self.assertTrue('F3' in tea_alt.get('alvo', '') and 'Zemestani' in tea_alt.get('referencia', ''))

        # 3. Verificação CSS/HTML do painel plano
        with open(os.path.join(BASE_DIR, 'css', 'styles.css'), 'r', encoding='utf-8') as f:
            css = f.read()
        self.assertIn('.tolerability-guide-panel', css)
        self.assertIn('.tol-guide-grid', css)

        # 4. Verificação dinâmica via JavaScriptCore (RM01 PEM+ FMA>35 vs FMA<=35, Depressão Acelerado, Alzheimer, Guia 3 colunas)
        jsc_bin = '/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc'
        if os.path.exists(jsc_bin):
            with open(os.path.join(BASE_DIR, 'js', 'data.js'), 'r', encoding='utf-8') as f:
                data_js = f.read()
            with open(os.path.join(BASE_DIR, 'js', 'decision-engine.js'), 'r', encoding='utf-8') as f:
                engine_js = f.read()

            audit_js = f"""
var window = {{}};
{data_js}
{engine_js}
function assert(cond, msg) {{ if (!cond) throw new Error(msg); }}
var eng = new DecisionEngine(window.NAPEN_DATA);

// RM01: PEM Presente + FMA > 35 + rTMS -> 3 protocolos (10 Hz -> 1 Hz+10 Hz -> iTBS+rPMS 10min)
eng.setCondition('avc-membro-superior', {{ modalityType: 'rtms' }});
eng.setFactor('fraqueza', false);
eng.setPathChoice('pem_triage', 'pem_sim');
eng.setPathChoice('gravidade_fma', 'fma_maior_35');
var m1 = eng.getActiveModality();
assert(m1.id === 'fraqueza' || eng.activeFactorId === 'fraqueza', 'Expected fraqueza, got ' + eng.activeFactorId);
assert(m1.frequencia.indexOf('10 Hz') !== -1 && m1.pulsos_duracao.indexOf('1.500') !== -1, 'P1 freq/pulsos mismatch: ' + m1.frequencia + ' / ' + m1.pulsos_duracao);
var chain35 = eng.getProtocolChain();
assert(chain35.length === 3, 'Expected 3-step chain for FMA>35, got ' + chain35.length);
var alt2 = eng.getPrescriptionForStage('alt2');
assert(alt2 && alt2.parametros.indexOf('10 minutos') !== -1, 'Expected alt2 10 minutos iTBS+rPMS');
var guide = eng.getTolerabilityGuidance();
assert(guide.tituloGuia && guide.orientacaoGeral && guide.dosePulsos && guide.calibracaoLimiar && guide.criterioInsatisfatoria, 'Incomplete guide object');

// RM01: FMA <= 35 rota pontilhada -> rtms_m1_grave_p3 (rPMS + rTMS Excitatória)
eng.setPathChoice('gravidade_fma', 'fma_menor_35');
eng.setPathChoice('rota_fma_menor_35', 'fma35_rota_pontilhada');
assert(eng.activeFactorId === 'rtms_m1_grave_p3', 'Expected rtms_m1_grave_p3, got ' + eng.activeFactorId);

// Depressão Acelerado -> 2 steps [TTT, SNT]
eng.setCondition('depressao-maior', {{ modalityType: 'rtms' }});
eng.setPathChoice('demanda_tempo', 'acelerado');
assert(eng.activeFactorId === 'tempo_reduzido', 'Expected tempo_reduzido');
assert(eng.getProtocolChain().length === 2, 'Expected 2 steps for Depressao Acelerado');

// Alzheimer rTMS Parietal/Temporal e tDCS Temporoparietal chains
eng.setCondition('alzheimer-ccl', {{ modalityType: 'rtms' }});
eng.setPathChoice('fator_limitante', 'ad_parietal');
assert(eng.getProtocolChain().length >= 2, 'Expected Alzheimer rTMS Parietal/Temporal chain >= 2');
eng.setModalityType('tdcs');
eng.setPathChoice('fator_limitante', 'tdcs_tp');
assert(eng.getProtocolChain().length >= 2, 'Expected Alzheimer tDCS Temporoparietal chain >= 2');

print('JSC_AUDIT_21_OK');
"""
            with tempfile.NamedTemporaryFile('w', suffix='.js', encoding='utf-8', delete=False) as tf:
                tf.write(audit_js)
                tmp_js = tf.name
            try:
                proc = subprocess.run([jsc_bin, tmp_js], cwd=BASE_DIR, capture_output=True, text=True, timeout=15)
                self.assertEqual(proc.returncode, 0, f"JSC error: {proc.stderr}\n{proc.stdout}")
                self.assertIn('JSC_AUDIT_21_OK', proc.stdout)
            finally:
                if os.path.exists(tmp_js):
                    os.remove(tmp_js)

    def test_22_wayfinder_solutions_1_to_4(self):
        """Valida Soluções 1–4 do Wayfinder: evidências recolhíveis ao fim, zero menções a roadmap/nota, fluxo de 2 botões e zero marcadores (#/*/**/&)."""
        import re
        import subprocess
        import tempfile

        html_path = os.path.join(BASE_DIR, 'index.html')
        css_path = os.path.join(BASE_DIR, 'css', 'styles.css')
        app_path = os.path.join(BASE_DIR, 'js', 'app.js')

        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
        with open(app_path, 'r', encoding='utf-8') as f:
            app_js = f.read()

        # Solução 1: <details id="evidenceReferencePanel"> fechado por padrão, APÓS #responseAssistantPanel, com atalho na calculadora
        self.assertIn('<details class="evidence-reference-panel" id="evidenceReferencePanel">', html)
        self.assertIn('id="btnScrollToEvidence"', html)
        self.assertIn('id="evidenceSummaryGradeBadge"', html)
        self.assertIn('id="evidenceSummaryAmstarBadge"', html)
        self.assertLess(
            html.index('id="responseAssistantPanel"'),
            html.index('id="evidenceReferencePanel"'),
            'evidenceReferencePanel deve encerrar #prescriptionDetailsCard após #responseAssistantPanel'
        )
        self.assertLess(
            html.index('id="btnScrollToEvidence"'),
            html.index('id="responseAssistantPanel"'),
            'Link #btnScrollToEvidence deve ficar na Calculadora antes do Assistente Pós-Indução'
        )

        # Solução 2: Zero menções visíveis a roadmap / nota no HTML (ignorando IDs técnicos calcRoadmapEffectText)
        visible_html = re.sub(r'<script.*?</script>', '', html, flags=re.S)
        visible_html = re.sub(r'<!--.*?-->', '', visible_html, flags=re.S)
        visible_text = re.sub(r'<[^>]+>', ' ', visible_html)
        self.assertIsNone(
            re.search(r'\broadmaps?\b|\bRM\d{2}\b|\bNota\b\s*(?:N\d+|Institucional|de transpar)', visible_text, re.I),
            'Não deve haver menções visíveis a roadmap, RMxx ou Nota na interface HTML'
        )

        # Solução 4: Zero marcadores (# / * / ** / (&) / Marcador () no HTML visível e nos 3 JSONs + CSS semântico
        self.assertIn('2. Otimização de Dose, Pulsos &amp; Duração', html)
        self.assertNotIn('2. Dose, Pulsos &amp; Marcadores', html)
        self.assertIn('.obs-semantic-tag', css)
        self.assertNotIn('*Uso privativo', app_js)

        skip_keys = {'id', 'roadmap_id', 'svg_file', 'protocolo_id', 'tolerabilidade_roadmap',
                     'step_id', 'tol_key', 'chave', 'proxima_etapa', 'protocolo_alvo',
                     'etapa_ids', 'protocolo_ids', 'estagios', 'modalidades_tipo',
                     'tolerabilidades', 'referencia_doi', 'guideline_doi', 'url', 'doi'}
        sym_pat = re.compile(r'(\*|#|\(&\)|Marcador\s*\(|\broadmaps?\b|\bnota\b)', re.I)

        def scan_sym(obj, path=''):
            hits = []
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k in skip_keys:
                        continue
                    p = f'{path}.{k}' if path else k
                    if isinstance(v, str) and sym_pat.search(v):
                        hits.append((p, v[:120]))
                    else:
                        hits.extend(scan_sym(v, p))
            elif isinstance(obj, list):
                for idx, item in enumerate(obj):
                    hits.extend(scan_sym(item, f'{path}[{idx}]'))
            return hits

        for rel in ['data/napen_roadmaps_data.json', 'data/grade_amstar_audit.json', 'data/escalas_guia_clinico.json']:
            with open(os.path.join(BASE_DIR, rel), 'r', encoding='utf-8') as f:
                payload = json.load(f)
            self.assertEqual(scan_sym(payload, rel), [], f'Marcadores residuais (#/*/**/&/roadmap/nota) em {rel}')

        # Solução 3: Continuidade dinâmica de 2 botões na homepage e barras internas via JSC
        self.assertIn('Conduta após o protocolo selecionado:', html)
        self.assertIn('Cenário do paciente:', app_js)
        self.assertIn('renderHomeContinuityStageButtons', app_js)

        jsc_bin = '/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc'
        if os.path.exists(jsc_bin):
            with open(os.path.join(BASE_DIR, 'js', 'data.js'), 'r', encoding='utf-8') as f:
                data_js = f.read()
            with open(os.path.join(BASE_DIR, 'js', 'scale-guide-data.js'), 'r', encoding='utf-8') as f:
                sg_js = f.read()
            with open(os.path.join(BASE_DIR, 'js', 'decision-engine.js'), 'r', encoding='utf-8') as f:
                engine_js = f.read()

            dom_ids = sorted(set(re.findall(r'id="([^"]+)"', html)))
            dom_probe = f"""
var window = {{ pageYOffset: 0, scrollTo: function(){{}} }};
var _els = {{}};
function makeEl(id) {{
  var classes = new Set();
  var _inner = '';
  var el = {{
    id: id, value: '', textContent: '', href: '', open: false,
    style: {{}}, options: [], selectedIndex: 0, children: [],
    classList: {{ add: function(c){{classes.add(c);}}, remove: function(c){{classes.delete(c);}}, toggle: function(c,f){{f?classes.add(c):classes.delete(c);}}, contains: function(c){{return classes.has(c);}} }},
    listeners: {{}},
    addEventListener: function(ev, fn){{ (this.listeners[ev]=this.listeners[ev]||[]).push(fn); }},
    appendChild: function(c){{
      this.children.push(c);
      if (this.tagName === 'SELECT' && c && c.tagName === 'OPTGROUP') {{
        (c.children || []).forEach(function(o){{ el.options.push(o); }});
      }} else if (this.tagName === 'SELECT' && c && c.tagName === 'OPTION') {{
        this.options.push(c);
      }}
    }},
    querySelector: function(){{ return makeEl(''); }},
    querySelectorAll: function(){{ return []; }},
    getAttribute: function(k){{ return this['data-' + k] || ''; }},
    setAttribute: function(k, v){{ this['data-' + k] = v; }},
    closest: function(){{ return null; }},
    getBoundingClientRect: function(){{ return {{ top: 100 }}; }}
  }};
  Object.defineProperty(el, 'innerHTML', {{
    get: function(){{ return _inner; }},
    set: function(val){{
      _inner = String(val || '');
      if (this.tagName === 'SELECT') {{
        this.options = [];
        var re = /<option[^>]*value="([^"]*)"[^>]*>/g, m;
        while ((m = re.exec(_inner)) !== null) {{
          this.options.push({{ value: m[1] }});
        }}
        this.selectedIndex = 0;
      }}
    }}
  }});
  return el;
}}
{json.dumps(dom_ids)}.forEach(function(id){{ _els[id] = makeEl(id); }});
_els['homeContCondition'].tagName = 'SELECT';
_els['homeContProtocol'].tagName = 'SELECT';
_els['homeContModality'].tagName = 'SELECT';
var document = {{
  _cbs: {{}},
  addEventListener: function(ev, fn){{ if (ev === 'DOMContentLoaded') this._cbs.ready = fn; else (this._cbs[ev]=this._cbs[ev]||[]).push(fn); }},
  getElementById: function(id){{ if (!_els[id]) _els[id] = makeEl(id); return _els[id]; }},
  createElement: function(tag){{ var e = makeEl(''); e.tagName = tag.toUpperCase(); return e; }},
  querySelector: function(sel){{ return makeEl(sel); }},
  querySelectorAll: function(){{ return []; }}
}};
{data_js}
{sg_js}
{engine_js}
{app_js}
if (document._cbs.ready) document._cbs.ready();
// Simula clique em 'Sim — Já realizou ou iniciou'
_els['btnHomeEntryReturning'].listeners['click'][0]();
var htmlMulti = _els['homeContStageShortcuts'].innerHTML;
if (htmlMulti.indexOf('data-home-stage="evaluation"') === -1 || htmlMulti.indexOf('data-home-stage="alt1"') === -1) {{
  throw new Error('Esperado 2 botoes (evaluation + alt1) para AVC MS, obtido: ' + htmlMulti);
}}
// Muda para Paralisia Cerebral (pc_distonia = protocolo unico sem alt)
_els['homeContCondition'].value = 'paralisia-cerebral';
_els['homeContCondition'].listeners['change'][0]({{ target: _els['homeContCondition'] }});
var singleIdx = -1;
for (var i = 0; i < _els['homeContProtocol'].options.length; i++) {{
  if (_els['homeContProtocol'].options[i].value === 'pc_distonia') {{ singleIdx = i; break; }}
}}
if (singleIdx === -1) throw new Error('pc_distonia nao encontrado no select');
_els['homeContProtocol'].selectedIndex = singleIdx;
_els['homeContProtocol'].value = 'pc_distonia';
_els['homeContProtocol'].listeners['change'][0]({{ target: _els['homeContProtocol'] }});
var htmlSingle = _els['homeContStageShortcuts'].innerHTML;
if (htmlSingle.indexOf('data-home-stage="failure"') === -1 || htmlSingle.indexOf('Protocolo Único') === -1) {{
  throw new Error('Esperado botao unico failure para pc_distonia, obtido: ' + htmlSingle);
}}
// Simula clique em #btnScrollToEvidence abrindo <details>
_els['evidenceReferencePanel'].open = false;
_els['btnScrollToEvidence'].listeners['click'][0]({{ preventDefault: function(){{}} }});
if (_els['evidenceReferencePanel'].open !== true) {{
  throw new Error('#btnScrollToEvidence deve abrir details#evidenceReferencePanel');
}}
print('JSC_WAYFINDER_22_OK');
"""
            with tempfile.NamedTemporaryFile('w', suffix='.js', encoding='utf-8', delete=False) as tf:
                tf.write(dom_probe)
                tmp_js = tf.name
            try:
                proc = subprocess.run([jsc_bin, tmp_js], cwd=BASE_DIR, capture_output=True, text=True, timeout=15)
                self.assertEqual(proc.returncode, 0, f"JSC error: {proc.stderr}\n{proc.stdout}")
                self.assertIn('JSC_WAYFINDER_22_OK', proc.stdout)
            finally:
                if os.path.exists(tmp_js):
                    os.remove(tmp_js)


if __name__ == '__main__':
    unittest.main()



