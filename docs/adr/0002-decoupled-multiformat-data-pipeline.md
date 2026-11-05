# Pipeline de Dados Desacoplado e Ingestão Multiformato

Decidimos separar estritamente a camada de visualização da camada de dados (`data/napen_roadmaps_data.json` / `js/data.js`), acoplada a um pipeline de ingestão agnóstico capaz de normalizar entradas em Excel (.xlsx), Word (.docx), CSV e JSON.

Como a revisão das diretrizes no ciclo 2026–2027 será conduzida por múltiplos GTs temáticos com diferentes perfis de familiaridade técnica, a plataforma não deve exigir formatação manual em código. Um script utilitário e validador de integridade converterá os arquivos entregues pelos pesquisadores diretamente para o formato canônico da aplicação.
