# Arquitetura de Web App Estático Moderno (Zero-Build)

Para a plataforma interativa dos Roadmaps NAPeN, decidimos utilizar uma arquitetura estática moderna baseada em HTML5 semântico, CSS com tokens de design e Vanilla JavaScript (ES6+) modular, sem etapas de compilação ou dependências de bundlers (Node/Webpack/Vite).

A decisão prioriza portabilidade total e facilidade de distribuição: a aplicação pode ser executada instantaneamente a partir de qualquer diretório local, compartilhada via Google Drive entre os membros dos Grupos de Trabalho ou hospedada gratuitamente (GitHub Pages/Vercel) e incorporada por iframe no portal da NAPeN, sem impor barreiras de ambiente de desenvolvimento a pesquisadores e clínicos.
