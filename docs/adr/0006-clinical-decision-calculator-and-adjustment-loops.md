# Assistente Interativo de Reavaliação Clínica e Laços de Ajuste do Protocolo

Decidimos incorporar no dashboard um **Assistente Interativo de Reavaliação Clínica (Calculadora de Resposta & Próximo Passo)** e um bloco dedicado a **Sessões de Ajuste** em cada protocolo clínico.

## Contexto e Descoberta no Acervo
A análise dos roadmaps NAPeN revelou que a lógica condicional de reavaliação periódica por escala padronizada (e a consequente tomada de decisão em caso de resposta insatisfatória) **não é exclusiva do AVC**, estando presente também em:
- **AVC (RM01 a RM04, RM06 a RM09)**: Escalas FMA-UE, EAM, Nottingham Sensory e Teste de Cancelamento de Estrelas, com laço de resposta insatisfatória após 10 a 24 sessões.
- **Doença de Parkinson (RM17)**: Escalas UPDRS-III, TUG e FOGQ (reavaliação semanal; se estagnação ou piora, ativar protocolo de resgate).
- **Ataxia Cerebelar (RM16)**: Escalas SARA e ICARS (ajuste se não houver alteração de uma semana para outra).
- **Psiquiatria / Depressão & TAG (RM10 e RM11)**: Escalas HAMD-17, HDRS-21 e HAM-A (critério de resposta $\ge 50\%$ e remissão após 10–20 sessões).
- **Dor Neuropática (RM05)**: Escala EVA e testes sensoriais para alodinia/hiperalgesia.

## Decisão de Implementação
1. **Assistente de Avaliação nos Cartões**: O usuário insere a pontuação pré e pós-tratamento na escala do roadmap. O sistema calcula a variação e indica a conduta do fluxograma:
   - *Resposta Satisfatória*: Recomendação de continuidade ou protocolo de manutenção.
   - *Resposta Insatisfatória*: O sistema exibe o **Protocolo Alternativo / Próximo Passo**, detalhando os ajustes de alvo, modalidade (ex: rTMS ➔ tDCS/rPMS) ou parâmetros.
2. **Bloco de Sessões de Ajuste**: Todo protocolo terá uma área explícita descrevendo o momento da reavaliação, as manobras de ajuste de dose/montagem e o critério de interrupção do ciclo de indução.
