# Plataforma Interativa de Prescrição Clínica em Neuromodulação Não Invasiva
### Rede NAPeN — Roadmaps de Prescrição Baseada em Evidências 2026–2027

[![Test Suite](https://img.shields.io/badge/tests-11%20passing-brightgreen.svg)](#testes-automatizados)
[![JavaScript](https://img.shields.io/badge/ES6+-Vanilla%20JS-yellow.svg)](#arquitetura-e-stack)
[![Rede NAPeN](https://img.shields.io/badge/Rede%20NAPeN-Official%20Roadmaps-0099A1.svg)](https://www.neuromodulation-net.com/)

Plataforma interativa para apoio à tomada de decisão clínica em Neuromodulação Não Invasiva (Estimulação Magnética Transcraniana — **TMS** e Estimulação Transcraniana por Corrente Contínua — **tDCS**).

Baseada rigorosamente nos **Roadmaps Clínicos 2026–2027 da Rede NAPeN** (*National Advanced Pharmacotherapy & Neuromodulation Network*), abrangendo 13 condições neurológicas, psiquiátricas e de reabilitação motora.

---

## Funcionalidades Principais

1. **Prescrição Interativa Passo a Passo**:
   - **Passo 1 — Definição do Fator Limitante / Desfecho Primário**: Seleção do objetivo funcional (espasticidade, motricidade, marcha, deglutição, sintomas depressivos, etc.).
   - **Passo 2 — Escolha da Modalidade Terapêutica**: TMS (HF-rTMS, LF-rTMS, iTBS) vs. tDCS (anodal, catodal, bihemisférica), com níveis de evidência GRADE e alertas de segurança.
   - **Passo 3 — Matriz de Parâmetros e Alvos Neuroanatômicos**: Frequência, intensidade (% LMR), localização no Sistema Internacional 10-20 (C3, C4, F3, F4, etc.), eletrodos e dosimetria.
   - **Passo 4 — Calculadora Dual de Resposta Clínica**: Avaliação pré e pós-tratamento com cálculo automático de variação percentual, comparação com a Diferença Clínica Minimamente Importante (**MCID**) e árvore decisória de conduta clínica (*Manter*, *Ajustar Parâmetros* ou *Migrar de Protocolo*).

2. **Calculadora de Resposta Clínica (Fast-Track de Reavaliação)**:
   - Acesso direto via menu superior em cascata de 3 níveis:
     - **1º Nível (Eixos Clínicos)**: *Acidente Vascular Cerebral*, *Distúrbios do Movimento*, *Psiquiatria & Saúde Mental*, *Dor Crônica*, *Neurodesenvolvimento*, *Cognição*.
     - **2º Nível (Foco Clínico / Diagnóstico)**: Ex: *Membro Superior*, *Mobilidade e Marcha*, *Afasia*, *Disfagia*.
     - **3º Nível (Desfecho & Escala)**: Ex: *Espasticidade* ➔ *Escala de Ashworth Modificada (EAM)*; *Equilíbrio* ➔ *Escala SARA* / *Berg (BBS)*.
   - Rolagem inteligente que posiciona a visualização no início da calculadora com realce visual.

3. **Guia Clínico de Aplicação de Escalas**:
   - Modal lateral com orientações práticas, tempo estimado, instruções passo a passo, tabela de pontuação e links diretos para acesso e download das escalas padronizadas.

4. **Busca Semântica & Tags Neuroanatômicas 10-20**:
   - Localização rápida de protocolos digitando condições clínicas, sintomas ou alvos cerebrais (ex: *C3, C4, F3, DLPFC, M1, cerebelo, espasticidade, marcha*).

5. **Design e Identidade Visual Rede NAPeN**:
   - Tipografia oficial, design tokens, barra turquesa com logos oficiais em SVG e seletor de idiomas (Português / Inglês).

---

## Arquitetura e Stack

A plataforma foi desenvolvida com foco em **zero dependências externas pesadas**, garantindo máxima velocidade, portabilidade clínica e funcionamento offline:

- **HTML5 Semântico**: Estrutura acessível com suporte a leitores de tela e atalhos de navegação.
- **CSS3 Moderno**: Variáveis CSS (Design Tokens oficiais da Rede NAPeN), Flexbox/Grid responsivo e animações em 60fps.
- **JavaScript (ES6+)**: Vanilla JS modular, isolado e orientado a eventos sem frameworks pesados.
- **Base de Dados Clínica**: `data/roadmaps_napen.json` e `js/data.js` espelhando integralmente a literatura e os parâmetros dos roadmaps.

### Estrutura de Arquivos

```text
├── index.html                # Aplicação SPA principal
├── css/
│   └── styles.css            # Folha de estilos e Design Tokens
├── js/
│   ├── app.js                # Lógica de controle, navegação e calculadora
│   └── data.js               # Exportação dos dados dos 13 roadmaps clínicos
├── data/
│   └── roadmaps_napen.json   # Base de dados clínica estruturada em JSON
├── assets/                   # Logos oficiais da Rede NAPeN (vetores SVG)
├── tests/
│   └── test_dashboard.py     # Suíte de testes unitários automatizados (Python unittest)
└── .gitignore                # Regras de exclusão Git
```

---

## Como Executar Localmente

### Opção 1: Diretamente no Navegador
Basta abrir o arquivo `index.html` em qualquer navegador web moderno (Google Chrome, Firefox, Safari ou Edge).

### Opção 2: Servidor Local (Recomendado)
Para rodar com um servidor HTTP leve:

```bash
# Clone o repositório
git clone https://github.com/barretogabe/dashboard_roadmaps.git
cd dashboard_roadmaps

# Inicie o servidor local via Python 3
python3 -m http.server 8000
```

Abra em seu navegador: `http://localhost:8000`

---

## Testes Automatizados

O projeto conta com uma suíte de testes unitários que valida a integridade clínica, visual e arquitetural:

```bash
python3 -m unittest -v tests/test_dashboard.py
```

### O que os testes verificam:
- `test_01_json_data_integrity`: Validação estrutural de todos os 13 roadmaps clínicos e parâmetros.
- `test_02_js_data_export`: Conformidade da exportação de dados para o client-side.
- `test_03_brand_assets_present`: Verificação dos logotipos oficiais da Rede NAPeN.
- `test_04_html_structure_and_napen_branding`: Integridade do layout, títulos e cabeçalho.
- `test_05_css_tokens_and_hover_effects`: Paleta oficial (#0099A1, #001A33), contrastes e responsividade.
- `test_06_js_classes_and_syntax`: Verificação de sintaxe e ausência de erros de script.
- `test_07_scale_guide_and_language_switcher`: Drawer do Guia de Escalas e seletor PT/EN.
- `test_08_neuroanatomical_search_tags`: Indexação de alvos 10-20 e termos bilíngues.
- `test_09_granular_scale_effects_and_synchronization`: Tamanhos de efeito e sincronização multiescala.
- `test_10_interactive_dropdown_and_menu_navigation`: Funcionamento dos menus em cascata por clique e hover.
- `test_11_calculator_fast_track_dropdown`: Navegação direta e layout horizontal das setas no 2º nível.

---

## Publicação no GitHub Pages

Para disponibilizar a plataforma online com link direto para outros desenvolvedores e profissionais de saúde:

1. Acesse o repositório no GitHub: `https://github.com/barretogabe/dashboard_roadmaps`.
2. Vá em **Settings** > **Pages**.
3. Na seção **Build and deployment**:
   - **Source**: `Deploy from a branch`.
   - **Branch**: `main` / pasta `/ (root)`.
4. Clique em **Save**.
5. Em instantes, a plataforma estará acessível publicamente em:
   `https://barretogabe.github.io/dashboard_roadmaps/`

---

## Licença e Atribuição

Desenvolvido para a **Rede NAPeN — National Advanced Pharmacotherapy & Neuromodulation Network**.
Todos os direitos reservados aos respectivos autores dos Roadmaps Clínicos 2026–2027.
Website Oficial: [www.neuromodulation-net.com](https://www.neuromodulation-net.com/)
