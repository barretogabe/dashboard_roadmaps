/**
 * Rede NAPeN — Base de Dados de Guias Clínicos de Aplicação de Escalas
 * Exportação automática para uso pelo front-end.
 */
window.NAPEN_SCALE_GUIDE = {
  "eam": {
    "id": "eam",
    "sigla": "EAM",
    "nome": "Escala de Ashworth Modificada",
    "nome_en": "Modified Ashworth Scale (MAS)",
    "dominio": "Espasticidade e Resistência Passiva ao Movimento",
    "tempo_aplicacao": "3 a 5 minutos por grupo muscular",
    "publico_alvo": "Pacientes com hipertonia espástica após Acidente Vascular Cerebral, Paralisia Cerebral, Traumatismo Cranioencefálico ou Lesão Medular.",
    "materiais": "Maca de exame neurológico confortável, goniômetro articular (opcional para mensuração de ângulo de parada).",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Posicionamento e Relaxamento Inicial",
        "descricao": "Posicione o paciente em decúbito dorsal confortável e relaxado. O membro a ser testado deve estar totalmente desprovido de restrições de vestimenta e apoiado adequadamente."
      },
      {
        "passo": 2,
        "titulo": "Instrução ao Paciente",
        "descricao": "Oriente o paciente: 'Vou movimentar seu braço/perna. Por favor, mantenha-se relaxado, não tente me ajudar nem resista ao movimento voluntariamente'."
      },
      {
        "passo": 3,
        "titulo": "Movimento Passivo Lento de Reconhecimento",
        "descricao": "Realize uma movimentação passiva lenta através de toda a amplitude de movimento articular (ADM) disponível para avaliar a amplitude livre de dor e a presença de contraturas articulares fixas."
      },
      {
        "passo": 4,
        "titulo": "Manobra de Estiramento Rápido Padronizada",
        "descricao": "Mova a articulação da posição de flexão máxima para a extensão máxima (ou vice-versa para flexores) na velocidade padronizada de aproximadamente 1 segundo para percorrer todo o arco de movimento articular (estiramento fásico dependente de velocidade)."
      },
      {
        "passo": 5,
        "titulo": "Classificação Imediata da Resistência",
        "descricao": "Gradue a resistência muscular percebida durante o estiramento rápido de acordo com os critérios padronizados de 0 a 4."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0",
        "descricao": "Sem aumento do tônus muscular (resistência fisiológica normal)."
      },
      {
        "grau": "1",
        "descricao": "Leve aumento do tônus muscular, manifestado por uma sensação de travamento (catch) transitório e soltura (release), ou por resistência mínima no final da amplitude de movimento articular."
      },
      {
        "grau": "1+",
        "descricao": "Leve aumento do tônus muscular, manifestado por um travamento (catch) súbito seguido de resistência mínima durante o restante (em menos da metade) da amplitude de movimento articular restante."
      },
      {
        "grau": "2",
        "descricao": "Aumento mais pronunciado do tônus muscular durante a maior parte da amplitude de movimento, mas o segmento afetado é movimentado com facilidade pelo examinador."
      },
      {
        "grau": "3",
        "descricao": "Aumento considerável do tônus muscular; a movimentação passiva torna-se difícil e com resistência importante."
      },
      {
        "grau": "4",
        "descricao": "Segmento acometido apresenta rigidez severa em flexão ou extensão (movimento passivo praticamente nulo sem força extrema)."
      }
    ],
    "interpretacao_clinica": "Na neuromodulação cerebral não invasiva (rTMS e tDCS), a resposta terapêutica satisfatória é definida pela redução de pelo menos 1 nível ordinal na EAM (ex: de 2 para 1, ou de 1+ para 0). A regressão da espasticidade facilita ganhos funcionais secundários e reduz a dor espástica.",
    "mcid": "Redução de pelo menos 1 ponto ordinal na escala (Diferença Clinicamente Importante Mínima).",
    "referencia_abnt": "Bohannon, R. W., & Smith, M. B. (1987). Interrater reliability of a modified Ashworth scale of muscle spasticity. Physical Therapy, 67(2), 206-207.",
    "doi": "10.1093/ptj/67.2.206",
    "link_artigo": "https://doi.org/10.1093/ptj/67.2.206",
    "validacao_brasil": "Oberg, T. D., et al. (2005). Estudo da confiabilidade interexaminadores da Escala Modificada de Ashworth. Revista Neurociências, 13(3), 114-118."
  },
  "fma_ue": {
    "id": "fma_ue",
    "sigla": "FMA-UE",
    "nome": "Escala Fugl-Meyer de Avaliação Motora (Membro Superior)",
    "nome_en": "Fugl-Meyer Assessment of Motor Recovery after Stroke (Upper Extremity)",
    "dominio": "Função Motora e Recuperação de Membro Superior",
    "tempo_aplicacao": "25 a 35 minutos",
    "publico_alvo": "Pacientes hemiparéticos em recuperação de Acidente Vascular Cerebral em todas as fases clínicas (aguda, subaguda e crônica).",
    "materiais": "Cadeira padrão sem braços, mesa ajustável, martelo de reflexos, goniômetro, bola pequena de tênis, lata cilíndrica, folha de papel, cronômetro e lápis.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Preparação e Avaliação dos Reflexos Profundos",
        "descricao": "Avalie os reflexos bicipital e tricipital do membro parético com martelo de percussão (0 = sem reflexo, 2 = reflexo presente)."
      },
      {
        "passo": 2,
        "titulo": "Avaliação das Sinergias Flexora e Extensora Básicas",
        "descricao": "Solicite que o paciente realize as sinergias motoras estereotipadas (retração e elevação escapular, abdução/rotação externa do ombro, flexão do cotovelo, supinação; seguidas pela sinergia extensora: adução/rotação interna, extensão do cotovelo, pronação)."
      },
      {
        "passo": 3,
        "titulo": "Movimentos Mistos e Fora de Sinergia",
        "descricao": "Avalie movimentos fracionados: mão na coluna lombar, flexão do ombro a 90° com cotovelo estendido, pronação/supinação com cotovelos a 90° e depois a 0°."
      },
      {
        "passo": 4,
        "titulo": "Avaliação Específica de Punho e Mão",
        "descricao": "Avalie estabilidade do punho em dorsiflexão com cotovelo fletido e estendido; avalie os 5 tipos de preensão manual (gancho, cilíndrica, esférica, pinça com polpa do indicador e pinça lateral)."
      },
      {
        "passo": 5,
        "titulo": "Coordenação, Dismetria e Velocidade",
        "descricao": "Teste índice-nariz rápido repetido 5 vezes; registre dismetria, tremor cinético e tempo cronometrado em comparação com o membro não parético."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 pontos",
        "descricao": "O paciente não consegue realizar a atividade motora solicitada."
      },
      {
        "grau": "1 ponto",
        "descricao": "O paciente realiza a tarefa apenas de forma incompleta ou parcial."
      },
      {
        "grau": "2 pontos",
        "descricao": "O paciente realiza a tarefa de forma completa e harmoniosa."
      },
      {
        "grau": "Escore Total Motor",
        "descricao": "Pontuação máxima de 66 pontos. Classificação: < 28 grave comprometimento; 28 a 50 moderado comprometimento; > 50 leve comprometimento."
      }
    ],
    "interpretacao_clinica": "Em ensaios de neuromodulação não invasiva, a melhora na FMA-UE correlaciona-se diretamente com plasticidade corticomotora (MEP facilitado e redução de inibição inter-hemisférica).",
    "mcid": "Grave/Moderado: ganho de 4.25 a 7.25 pontos; Crônico: ganho de 5.25 pontos (Page et al., 2012).",
    "referencia_abnt": "Fugl-Meyer, A. R., Jääskö, L., Leyman, I., Olsson, S., & Steglind, S. (1975). The post-stroke hemiplegic patient. 1. A method for evaluation of physical performance. Scandinavian Journal of Rehabilitation Medicine, 7(1), 13-31.",
    "doi": "10.2340/1650197771331",
    "link_artigo": "https://doi.org/10.2340/1650197771331",
    "validacao_brasil": "Maki, T., Quagliato, E. M., Cacho, E. W., Paz, L. P., Nascimento, N. H., & Inoue, M. M. (2006). Estudo de confiabilidade da aplicação da escala de Fugl-Meyer no Brasil. Revista Brasileira de Fisioterapia, 10(2), 177-183."
  },
  "bbs": {
    "id": "bbs",
    "sigla": "BBS",
    "nome": "Escala de Equilíbrio de Berg",
    "nome_en": "Berg Balance Scale (BBS)",
    "dominio": "Equilíbrio Estático e Dinâmico, Risco de Quedas",
    "tempo_aplicacao": "15 a 20 minutos",
    "publico_alvo": "Pacientes com sequelas motoras de AVC, Ataxias Espinocerebelares, Doença de Parkinson e idosos com risco de instabilidade postural.",
    "materiais": "Cronômetro, régua de alcance (métrica de 30 cm fixada na parede), duas cadeiras de altura padrão (uma com braços e uma sem braços), degrau/banco de 15 a 20 cm e calçados habituais.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Tarefas de Transferência e Permanência Sentada",
        "descricao": "Avalie transição de sentado para em pé, permanência de pé sem apoio, sentar sem apoio com pés no chão e permanência em pé para sentado."
      },
      {
        "passo": 2,
        "titulo": "Tarefas com Redução de Base de Suporte",
        "descricao": "Avalie equilíbrio de pé com olhos fechados (10 segundos), de pé com pés juntos unidos (1 minuto) e de pé em apoio unipodal (10 segundos em cada perna)."
      },
      {
        "passo": 3,
        "titulo": "Tarefas Dinâmicas com Deslocamento de Centro de Massa",
        "descricao": "Alcance anterior com braço estendido (sem dar passo), pegar objeto colocado no chão à frente dos pés e virar o tronco para olhar para trás sobre os ombros."
      },
      {
        "passo": 4,
        "titulo": "Tarefas Rotacionais e de Marcha",
        "descricao": "Giro completo de 360 graus para cada lado em menos de 4 segundos e colocação alternada dos pés sobre um degrau padrão de forma ritmada."
      },
      {
        "passo": 5,
        "titulo": "Posição em Tandem (Pé Imediatamente à Frente do Outro)",
        "descricao": "Colocar um pé imediatamente à frente do outro em linha reta e manter sem apoio por 30 segundos."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 a 4 pontos por item",
        "descricao": "Cada uma das 14 tarefas funcionais é pontuada de 0 (incapaz) a 4 (realiza de forma independente e com segurança dentro do tempo estabelecido)."
      },
      {
        "grau": "Escore Total Máximo",
        "descricao": "56 pontos possíveis."
      },
      {
        "grau": "Pontos de Corte",
        "descricao": "0 a 20: alto risco de quedas (cadeirante); 21 a 40: risco moderado de quedas (deambulação com auxílio); 41 a 56: baixo risco de quedas (deambulação independente)."
      }
    ],
    "interpretacao_clinica": "Na neuromodulação de ataxias ou AVC (alvo Cerebelo ou SMA/M1), um incremento >= 4 a 5 pontos na BBS representa ganho funcional clinicamente significativo na autonomia ambulatorial do paciente.",
    "mcid": "Ganho de 4 a 5 pontos (Stevenson, 2001; Hiengkaew et al., 2012).",
    "referencia_abnt": "Berg, K. O., Wood-Dauphinee, S. L., Williams, J. I., & Maki, B. (1992). Measuring balance in the elderly: validation of an instrument. Canadian Journal of Public Health, 83(Suppl 2), S7-11.",
    "doi": "10.1007/bf03404285",
    "link_artigo": "https://pubmed.ncbi.nlm.nih.gov/1468055/",
    "validacao_brasil": "Miyamoto, S. T., Lombardi Junior, I., Berg, K. O., Ramos, L. R., & Natour, J. (2004). Brazilian version of the Berg balance scale. Brazilian Journal of Medical and Biological Research, 37(9), 1411-1421."
  },
  "sara": {
    "id": "sara",
    "sigla": "SARA",
    "nome": "Scale for the Assessment and Rating of Ataxia",
    "nome_en": "Scale for the Assessment and Rating of Ataxia (SARA)",
    "dominio": "Gravidade da Ataxia Cerebelar e Coordenação Motora",
    "tempo_aplicacao": "10 a 15 minutos",
    "publico_alvo": "Pacientes com Ataxias Espinocerebelares (SCAs), Ataxia de Friedreich, Ataxia pós-AVC ou lesões cerebelares.",
    "materiais": "Cadeira sem braços, corredor livre para marcha de 10 metros, maca para teste deitados e cronômetro.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Avaliação da Marcha (Item 1, 0 a 8)",
        "descricao": "Peça ao paciente para caminhar por 10 metros, virar e retornar. Observe instabilidade, alargamento de base, desvios e necessidade de auxílio."
      },
      {
        "passo": 2,
        "titulo": "Postura Estática de Pé (Item 2, 0 a 6)",
        "descricao": "Avalie permanência de pé em posição natural, com pés juntos e em tandem, com olhos abertos e fechados por até 10 segundos."
      },
      {
        "passo": 3,
        "titulo": "Postura Sentada (Item 3, 0 a 4)",
        "descricao": "Avalie postura sentada na borda da cama sem encosto com braços cruzados sobre o peito."
      },
      {
        "passo": 4,
        "titulo": "Fala e Articulação (Item 4, 0 a 6)",
        "descricao": "Avalie disartria cerebelar durante fala espontânea padronizada e repetição da frase: 'O rato roeu a roupa do rei de Roma'."
      },
      {
        "passo": 5,
        "titulo": "Dedo-Nariz e Perseguição Rápida (Itens 5 e 6, 0 a 4 cada)",
        "descricao": "Avalie dismetria e tremor de intenção na manobra índice-nariz e seguimento do dedo do examinador em movimentos rápidos com cada braço."
      },
      {
        "passo": 6,
        "titulo": "Diadococinesia e Calcanhar-Joelho (Itens 7 e 8, 0 a 4 cada)",
        "descricao": "Avalie movimentos rápidos de pronação/supinação da mão e o deslizamento do calcanhar ao longo da tíbia oposta em decúbito dorsal."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 pontos",
        "descricao": "Sem sinais de ataxia (normal)."
      },
      {
        "grau": "1 a 10 pontos",
        "descricao": "Ataxia leve (deambulação independente, coordenação levemente preservada)."
      },
      {
        "grau": "11 a 20 pontos",
        "descricao": "Ataxia moderada (marcha com dispositivo ou apoio unilateral)."
      },
      {
        "grau": "21 a 30 pontos",
        "descricao": "Ataxia severa (cadeirante ou deambulação com assistência de duas pessoas)."
      },
      {
        "grau": "31 a 40 pontos",
        "descricao": "Ataxia gravíssima / dependência completa."
      }
    ],
    "interpretacao_clinica": "Em ensaios de estimulação cerebelar com tDCS anódica ou rTMS excitatória (ex: Benussi et al., 2018), uma redução de >= 1.5 a 2.0 pontos na SARA é considerada uma melhora clínica significativa e relevante.",
    "mcid": "Redução de 1.5 pontos (D'Abreu et al., 2010; Subramony et al., 2021).",
    "referencia_abnt": "Schmitz-Hübsch, T., du Montcel, S. T., Baliko, L., Berciano, J., Boesch, S., Depondt, C., ... & Klockgether, T. (2006). Scale for the assessment and rating of ataxia: development of a new clinical scale. Neurology, 66(11), 1717-1720.",
    "doi": "10.1212/01.wnl.0000219042.60538.92",
    "link_artigo": "https://doi.org/10.1212/01.wnl.0000219042.60538.92",
    "validacao_brasil": "Braga-Neto, P., Godeiro-Junior, C., Dutra, L. A., Pedroso, J. L., & Barsottini, O. G. (2010). Translation and validation into Brazilian Portuguese of the Scale for the Assessment and Rating of Ataxia (SARA). Arquivos de Neuro-Psiquiatria, 68(2), 228-230."
  },
  "ham_d": {
    "id": "ham_d",
    "sigla": "HAM-D 17",
    "nome": "Escala Hamilton de Avaliação da Depressão (17 itens)",
    "nome_en": "Hamilton Depression Rating Scale (HDRS-17)",
    "dominio": "Gravidade da Sintomatologia Depressiva",
    "tempo_aplicacao": "15 a 20 minutos",
    "publico_alvo": "Pacientes adultos com Transtorno Depressivo Maior (TDM) unipolar resistente ou refratário a tratamento medicamentoso.",
    "materiais": "Entrevista clínica semiestruturada com manual e folha de registro.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Entrevista Clínica Semiestruturada Padronizada",
        "descricao": "Conduza a entrevista cobrindo o período dos últimos 7 dias. Formule as perguntas de forma neutra e investigue a intensidade e a frequência de cada sintoma."
      },
      {
        "passo": 2,
        "titulo": "Avaliação dos Sintomas Afetivos e Ideação Suicida",
        "descricao": "Investigue humor deprimido, sentimentos de culpa e ideação suicida (0 = ausente; 4 = tentativas ativas de suicídio)."
      },
      {
        "passo": 3,
        "titulo": "Avaliação dos Distúrbios do Sono (Insônia)",
        "descricao": "Pontue separadamente: insônia inicial (dificuldade de adormecer), insônia intermediária (despertar no meio da noite) e insônia terminal (despertar precoce)."
      },
      {
        "passo": 4,
        "titulo": "Avaliação de Trabalho, Atividades e Lentificação Psicomotora",
        "descricao": "Examine perda de interesse, fadiga incapacitante, lentidão do pensamento e agitação psicomotora observável."
      },
      {
        "passo": 5,
        "titulo": "Sintomas Somáticos, Ansiedade e Sintomas Sexuais",
        "descricao": "Investigue ansiedade psíquica e somática, sintomas gastrointestinais, sintomas somáticos gerais e perda de libido/peso."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 a 7 pontos",
        "descricao": "Sem depressão / Eutimia ou Remissão Clínica."
      },
      {
        "grau": "8 a 13 pontos",
        "descricao": "Depressão Leve."
      },
      {
        "grau": "14 a 18 pontos",
        "descricao": "Depressão Moderada."
      },
      {
        "grau": "19 a 22 pontos",
        "descricao": "Depressão Severa."
      },
      {
        "grau": ">= 23 pontos",
        "descricao": "Depressão Muito Severa."
      }
    ],
    "interpretacao_clinica": "Na estimulação do DLPFC esquerdo por rTMS de alta frequência (10 Hz) ou iTBS (protocolo SAINT/Stanford), a Resposta Clínica é definida por redução >= 50% no escore inicial, e a Remissão Clínica por escore final <= 7.",
    "mcid": "Redução mínima de 3 pontos no escore total (Kirsch et al., 2008; NICE Guidelines).",
    "referencia_abnt": "Hamilton, M. (1960). A rating scale for depression. Journal of Neurology, Neurosurgery, and Psychiatry, 23(1), 56-62.",
    "doi": "10.1136/jnnp.23.1.56",
    "link_artigo": "https://doi.org/10.1136/jnnp.23.1.56",
    "validacao_brasil": "Moreno, R. A., & Moreno, D. H. (1998). Escalas de avaliação para depressão de Hamilton (HAM-D) e Montgomery-Åsberg (MADRS). Revista de Psiquiatria Clínica, 25(5), 262-272."
  },
  "ham_a": {
    "id": "ham_a",
    "sigla": "HAM-A",
    "nome": "Escala Hamilton de Avaliação da Ansiedade",
    "nome_en": "Hamilton Anxiety Rating Scale (HAMA)",
    "dominio": "Gravidade dos Sintomas de Ansiedade Psíquica e Somática",
    "tempo_aplicacao": "10 a 15 minutos",
    "publico_alvo": "Pacientes com Transtorno de Ansiedade Generalizada (TAG), pânico ou ansiedade comórbida.",
    "materiais": "Roteiro semiestruturado de 14 itens e formulário de pontuação.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Exploração dos 14 Itens Sintomatológicos",
        "descricao": "Avalie os 14 grupos de sintomas: humor ansioso, tensão, medos, insônia, dificuldades cognitivas, humor deprimido, sintomas somáticos musculares, sintomas sensoriais, cardiovasculares, respiratórios, gastrointestinais, geniturinários, autonômicos e comportamento na entrevista."
      },
      {
        "passo": 2,
        "titulo": "Pontuação em Escala Likert de 5 Níveis",
        "descricao": "Gradue cada item de 0 (ausente) a 4 (muito grave / incapacitante)."
      },
      {
        "passo": 3,
        "titulo": "Cálculo e Diferenciação Subescalar",
        "descricao": "Some o escore total (0 a 56) e analise o balanço entre Ansiedade Psíquica (itens 1 a 6 e 14) e Ansiedade Somática (itens 7 a 13)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "< 17 pontos",
        "descricao": "Ansiedade leve ou subclínica."
      },
      {
        "grau": "18 a 24 pontos",
        "descricao": "Ansiedade leve a moderada."
      },
      {
        "grau": "25 a 30 pontos",
        "descricao": "Ansiedade moderada a grave."
      },
      {
        "grau": "> 30 pontos",
        "descricao": "Ansiedade muito grave."
      }
    ],
    "interpretacao_clinica": "Na estimulação inibitória (1 Hz) no DLPFC direito para TAG, uma redução de >= 50% na HAM-A consolida resposta terapêutica clínica robusta.",
    "mcid": "Redução de 4 a 5 pontos no escore total.",
    "referencia_abnt": "Hamilton, M. (1959). The assessment of anxiety states by rating. British Journal of Medical Psychology, 32(1), 50-55.",
    "doi": "10.1111/j.2044-8341.1959.tb00467.x",
    "link_artigo": "https://doi.org/10.1111/j.2044-8341.1959.tb00467.x",
    "validacao_brasil": "Freire, M. A., et al. (2014). Propriedades psicométricas das versões brasileiras das escalas de ansiedade de Hamilton e Beck. Revista Brasileira de Psiquiatria."
  },
  "pcl_5": {
    "id": "pcl_5",
    "sigla": "PCL-5",
    "nome": "Posttraumatic Stress Disorder Checklist (DSM-5)",
    "nome_en": "PCL-5 for DSM-5",
    "dominio": "Sintomas de Transtorno de Estresse Pós-Traumático (TEPT)",
    "tempo_aplicacao": "5 a 10 minutos (autoaplicável)",
    "publico_alvo": "Indivíduos expostos a eventos traumáticos com sintomas intrusivos, esquiva ou hiperestimulação.",
    "materiais": "Questionário autoaplicável de 20 itens com instruções padronizadas.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Orientação e Contexto Temporal",
        "descricao": "Instrua o paciente a considerar as reações e desconfortos experimentados durante o último mês em decorrência do evento traumático mais estressante vivenciado."
      },
      {
        "passo": 2,
        "titulo": "Preenchimento dos 20 Itens",
        "descricao": "O paciente responde a cada item indicando o quanto foi incomodado: 0 = 'De modo nenhum', 1 = 'Um pouco', 2 = 'Moderadamente', 3 = 'Muito', 4 = 'Extremamente'."
      },
      {
        "passo": 3,
        "titulo": "Avaliação dos 4 Clusters do DSM-5",
        "descricao": "Cluster B: Intrusão (itens 1-5); Cluster C: Esquiva (itens 6-7); Cluster D: Alterações cognitivas e humor (itens 8-14); Cluster E: Reatividade e hipervigilância (itens 15-20)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "Escore Total (0 a 80)",
        "descricao": "Soma de todos os 20 itens."
      },
      {
        "grau": "Ponto de Corte Provisório",
        "descricao": "Pontuação >= 31 a 33 sugere diagnóstico provável de TEPT."
      },
      {
        "grau": "Regra de Resposta",
        "descricao": "Redução de 5 a 10 pontos indica melhora confiável; redução de 10 a 20 pontos indica melhora clinicamente significativa (National Center for PTSD)."
      }
    ],
    "interpretacao_clinica": "Na estimulação do DLPFC direito em 1 Hz ou estimulação bilateral em TEPT, o objetivo clínico é desativar a hiper-reatividade amigdalar com queda sustentada no cluster E e redução >= 10 pontos no escore global.",
    "mcid": "Redução de 10 pontos no escore total (Marx et al., 2022).",
    "referencia_abnt": "Blevins, C. A., Weathers, F. W., Davis, M. T., Witte, T. K., & Domino, J. L. (2015). The Posttraumatic Stress Disorder Checklist for DSM-5 (PCL-5): development and initial psychometric evaluation. Journal of Traumatic Stress, 28(6), 489-498.",
    "doi": "10.1002/jts.22059",
    "link_artigo": "https://doi.org/10.1002/jts.22059",
    "validacao_brasil": "Pereira-Lima, K., Loureiro, S. R., Crippa, J. A. S., & Hallak, J. E. (2019). Psychometric properties of the Brazilian version of the Posttraumatic Stress Disorder Checklist for DSM-5 (PCL-5). Journal of Affective Disorders, 256, 442-449."
  },
  "eva": {
    "id": "eva",
    "sigla": "EVA",
    "nome": "Escala Visual Analógica de Dor",
    "nome_en": "Visual Analogue Scale (VAS Pain)",
    "dominio": "Intensidade Subjetiva da Dor",
    "tempo_aplicacao": "1 minuto",
    "publico_alvo": "Pacientes com Dor Neuropática Crônica, Fibromialgia, Dor pós-AVC (Síndrome Talamica) ou Síndrome Dolorosa Miofascial.",
    "materiais": "Régua analógica de 100 mm (10 cm) com âncoras verbais nas extremidades ou régua deslizante milimetrada.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Instrução Padronizada ao Paciente",
        "descricao": "Apresente a régua de 10 cm e oriente: 'Esta linha representa a intensidade da sua dor. A ponta esquerda representa AUSÊNCIA TOTAL DE DOR e a ponta direita representa A PIOR DOR IMAGINÁVEL. Marque com um risco o ponto exato da sua dor neste momento (ou nas últimas 24 horas)'."
      },
      {
        "passo": 2,
        "titulo": "Mensuração em Milímetros ou Centímetros",
        "descricao": "Com uma régua graduada, meça a distância do extremo esquerdo (zero) até o ponto marcado pelo paciente em centímetros (0 a 10) ou milímetros (0 a 100)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 a 2.9 cm",
        "descricao": "Dor leve ou tolerável."
      },
      {
        "grau": "3.0 a 6.9 cm",
        "descricao": "Dor moderada (interfere em atividades cotidianas)."
      },
      {
        "grau": "7.0 a 10.0 cm",
        "descricao": "Dor severa / intolerável."
      }
    ],
    "interpretacao_clinica": "Em ensaios de estimulação de M1 com rTMS de 10 Hz ou 20 Hz (e tDCS anódica) para dor crônica, o critério de resposta clínica satisfatória padrão é a redução de pelo menos 30% ou >= 2.0 cm na EVA.",
    "mcid": "Redução absoluta de 2.0 cm ou alívio de 30% a 50% (Farrar et al., 2001; IMMPACT recommendations).",
    "referencia_abnt": "Huskisson, E. C. (1974). Measurement of pain. The Lancet, 304(7889), 1127-1131.",
    "doi": "10.1016/S0140-6736(74)90884-8",
    "link_artigo": "https://doi.org/10.1016/S0140-6736(74)90884-8",
    "validacao_brasil": "Martinez, J. E., Grassi, D. C., & Marques, L. G. (2011). Validação da versão em português da escala visual analógica e de faces. Revista Brasileira de Reumatologia, 51(4), 299-305."
  },
  "dn4": {
    "id": "dn4",
    "sigla": "DN4",
    "nome": "Questionário de Dor Neuropática (DN4)",
    "nome_en": "Douleur Neuropathique 4 Questions (DN4)",
    "dominio": "Caracterização e Triagem de Dor Neuropática",
    "tempo_aplicacao": "3 a 5 minutos",
    "publico_alvo": "Pacientes com suspeita de dor de origem somatossensorial (neuralgia do trigêmeo, dor pós-AVC, radiculopatias, polineuropatia diabética).",
    "materiais": "Chumaço de algodão (para hipoestesia ao toque), agulha descartável romba (hipoestesia à picada), pincel macio (alodínia mecânica dinâmica).",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Questão 1: Características da Dor (Sintomas)",
        "descricao": "Pergunte se a dor apresenta: 1. Queimação; 2. Sensação de frio doloroso; 3. Choques elétricos."
      },
      {
        "passo": 2,
        "titulo": "Questão 2: Sintomas Associados na Mesma Região",
        "descricao": "Pergunte se no local da dor há: 4. Formigamento; 5. Picadas/agulhadas; 6. Dormência; 7. Coceira."
      },
      {
        "passo": 3,
        "titulo": "Questões 3 e 4: Exame Físico Sensitivo Comparativo",
        "descricao": "Teste no local da dor comparando com área homóloga contralateral sadia: 8. Hipoestesia ao toque (algodão); 9. Hipoestesia à picada (agulha romba); 10. Alodínia mecânica dinâmica (pincel suave causando dor)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 a 10 pontos",
        "descricao": "Cada resposta 'Sim' pontua 1 ponto."
      },
      {
        "grau": "Ponto de Corte >= 4 pontos",
        "descricao": "Sensibilidade de 83% e especificidade de 90% para identificação de dor neuropática."
      }
    ],
    "interpretacao_clinica": "O escore >= 4 no DN4 confirma a indicação de neuromodulação em M1 (Córtex Motor Primário) para analgesia mediada pela modulação das vias tálamo-corticais e sistema descendente inibitório da dor.",
    "mcid": "Redução do componente disestésico e queda do escore abaixo do ponto de corte 4.",
    "referencia_abnt": "Bouhassira, D., Attal, N., Alchaar, H., Boureau, F., Brochet, B., Bruxelle, J., ... & Vicaut, E. (2005). Comparison of pain syndromes associated with nervous or somatic lesions and development of a new neuropathic pain diagnostic questionnaire (DN4). Pain, 114(1-2), 29-36.",
    "doi": "10.1016/j.pain.2004.12.010",
    "link_artigo": "https://doi.org/10.1016/j.pain.2004.12.010",
    "validacao_brasil": "Santos, J. G., et al. (2010). Translation and validation of the Douleur Neuropathique 4 questions (DN4) questionnaire into Brazilian Portuguese. Arquivos de Neuro-Psiquiatria, 68(4), 540-544."
  },
  "tug": {
    "id": "tug",
    "sigla": "TUG",
    "nome": "Timed Up and Go Test",
    "nome_en": "Timed Up and Go Test (TUG)",
    "dominio": "Mobilidade Funcional, Velocidade da Marcha e Risco de Quedas",
    "tempo_aplicacao": "3 minutos",
    "publico_alvo": "Pacientes com sequelas de AVC, Doença de Parkinson, Ataxias e idosos em reabilitação.",
    "materiais": "Cadeira com altura de assento padrão (aproximadamente 46 cm) com braços, fita adesiva para demarcar 3 metros no chão e cronômetro.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Posicionamento Inicial do Paciente",
        "descricao": "Paciente sentado com as costas totalmente apoiadas no encosto da cadeira e braços repousados sobre os apoios."
      },
      {
        "passo": 2,
        "titulo": "Comando Verbal Padronizado",
        "descricao": "Instrua: 'Ao meu comando 'Vá', levante-se da cadeira, caminhe em passo confortável e seguro até a linha demarcada a 3 metros, dê a volta, retorne até a cadeira e sente-se novamente apoiando as costas'."
      },
      {
        "passo": 3,
        "titulo": "Acionamento e Parada do Cronômetro",
        "descricao": "Inicie a contagem no momento em que o paciente iniciar o movimento de levantar da cadeira; pare o cronômetro no momento exato em que o quadril toca o assento e as costas encostam no encosto."
      },
      {
        "passo": 4,
        "titulo": "Ensaio e Teste Oficial",
        "descricao": "Realize uma tentativa de familiarização não pontuada, seguida de 2 testes oficiais cronometrados, registrando o menor tempo ou a média."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "< 10 segundos",
        "descricao": "Mobilidade preservada e totalmente independente."
      },
      {
        "grau": "10 a 20 segundos",
        "descricao": "Independência na maioria das atividades diárias; fragilidade leve."
      },
      {
        "grau": "> 20 segundos",
        "descricao": "Mobilidade restrita; alto risco de quedas e necessidade de dispositivo de auxílio."
      }
    ],
    "interpretacao_clinica": "Na estimulação da Área Motora Suplementar (SMA / Cz) ou M1 para marcha pós-AVC ou Parkinson, a redução de pelo menos 2 a 3 segundos no TUG reflete melhora substancial na coordenação locomotora.",
    "mcid": "Redução de 2.9 a 3.4 segundos pós-AVC (Flansbjer et al., 2005).",
    "referencia_abnt": "Podsiadlo, D., & Richardson, S. (1991). The timed 'Up & Go': a test of basic functional mobility for frail elderly persons. Journal of the American Geriatrics Society, 39(2), 142-148.",
    "doi": "10.1111/j.1532-5415.1991.tb01616.x",
    "link_artigo": "https://doi.org/10.1111/j.1532-5415.1991.tb01616.x",
    "validacao_brasil": "Alexandre, T. S., Corona, L. P., Brito, T. R. P., & Duarte, Y. A. O. (2012). Similarities and differences in the performance of the Timed Up and Go test in frail elderly. Revista Brasileira de Fisioterapia, 16(5), 415-421."
  },
  "fogq": {
    "id": "fogq",
    "sigla": "FOGQ",
    "nome": "Freezing of Gait Questionnaire",
    "nome_en": "Freezing of Gait Questionnaire (FOGQ)",
    "dominio": "Congelamento da Marcha na Doença de Parkinson",
    "tempo_aplicacao": "5 minutos",
    "publico_alvo": "Pacientes com Doença de Parkinson idiopática que relatam episódios súbitos de bloqueio motor (pés 'colados ao chão').",
    "materiais": "Questionário estruturado com 6 itens.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Definição do Sintoma com o Paciente",
        "descricao": "Explique o fenômeno de congelamento: 'Sensação de que seus pés estão grudados ou colados no chão, apesar da sua intenção de continuar caminhando'."
      },
      {
        "passo": 2,
        "titulo": "Preenchimento dos Itens 1 e 2 (Marcha Geral)",
        "descricao": "Item 1: Severidade do distúrbio de marcha em geral (0 a 4). Item 2: Impacto na vida diária e independência (0 a 4)."
      },
      {
        "passo": 3,
        "titulo": "Preenchimento dos Itens 3 a 6 (Episódios de FOG)",
        "descricao": "Item 3: Frequência dos congelamentos (0 = nunca a 4 = várias vezes por hora); Item 4: Duração do episódio mais longo (0 a 4); Item 5: Hesitação ao iniciar a marcha (0 a 4); Item 6: Congelamento ao fazer curvas (0 a 4)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 a 24 pontos",
        "descricao": "Pontuação máxima de 24 pontos. Quanto maior a pontuação, maior a gravidade e o impacto do congelamento."
      },
      {
        "grau": "Ponto de Corte Diagnóstico",
        "descricao": "Presença de escore > 0 nos itens 3 a 6 confirma a presença de congelamento clínico ativo."
      }
    ],
    "interpretacao_clinica": "Na estimulação da Área Motora Suplementar (SMA / Cz) com rTMS de alta frequência (10 Hz), a redução de pelo menos 2 a 3 pontos no FOGQ reflete desconexão de redes locomotoras subcorticais e desbloqueio do início da marcha.",
    "mcid": "Redução mínima de 3 pontos no escore total.",
    "referencia_abnt": "Giladi, N., Shabtai, H., Simon, E. S., Biran, S., Tal, J., & Yao, S. C. (2000). Construction of questionnaire for evaluation of freezing of gait in Parkinson's disease. Parkinsonism & Related Disorders, 6(3), 165-170.",
    "doi": "10.1016/S1353-8020(99)00062-0",
    "link_artigo": "https://doi.org/10.1016/S1353-8020(99)00062-0",
    "validacao_brasil": "Baggio, J. A., Curtarelli, M. B., Freire, G. R. S., Coutinho, R., & Tumas, V. (2012). Translation and validation of the Freezing of Gait Questionnaire into Brazilian Portuguese. Parkinsonism & Related Disorders, 18(6), 701-705."
  },
  "updrs_iii": {
    "id": "updrs_iii",
    "sigla": "MDS-UPDRS-III",
    "nome": "MDS-UPDRS Parte III (Exame Motor)",
    "nome_en": "MDS-UPDRS Part III (Motor Examination)",
    "dominio": "Sinais Motores da Doença de Parkinson",
    "tempo_aplicacao": "15 a 25 minutos",
    "publico_alvo": "Pacientes com Doença de Parkinson em acompanhamento e avaliação de resposta a terapias farmacológicas e neuromodulatórias.",
    "materiais": "Cadeira padrão, espaço livre para deambulação de 10 metros e cronômetro.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Definição do Estado Clínico (ON vs OFF)",
        "descricao": "Registre se a avaliação está sendo realizada em estado OFF (sem medicação dopaminérgica há pelo menos 12 horas) ou em estado ON medicamentoso."
      },
      {
        "passo": 2,
        "titulo": "Avaliação de Fala, Expressão Facial e Rigidez",
        "descricao": "Avalie a hipomimia, volume/prosódia da fala e realize a mobilização passiva de punho, cotovelo, joelho e tornozelo para avaliar rigidez em roda denteada (0 a 4)."
      },
      {
        "passo": 3,
        "titulo": "Avaliação de Bradicinesia de Extremidades",
        "descricao": "Teste batimento repetido de dedos (finger tapping), abertura/fechamento rápido da mão, pronação/supinação do antebraço e batimento do calcanhar no solo (10 repetições amplas e rápidas)."
      },
      {
        "passo": 4,
        "titulo": "Levantar da Cadeira, Marcha e Congelamento",
        "descricao": "Avalie capacidade de levantar da cadeira com braços cruzados, amplitude de passos na marcha, balanço de membros superiores e presença de hesitação."
      },
      {
        "passo": 5,
        "titulo": "Teste de Puxão (Pull Test / Estabilidade Postural) e Tremor",
        "descricao": "Realize o teste de retropulsão postural súbita nos ombros do paciente; avalie tremor de repouso, postural e cinético nas 4 extremidades."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 a 132 pontos",
        "descricao": "Cada um dos 33 itens/subitens motores é pontuado de 0 (normal) a 4 (severo)."
      },
      {
        "grau": "MCID",
        "descricao": "Redução de pelo menos 3.25 a 4.5 pontos para melhora clinicamente importante no estado OFF (Horváth et al., 2015)."
      }
    ],
    "interpretacao_clinica": "Na estimulação de M1 ou DLPFC na Doença de Parkinson, a redução no MDS-UPDRS-III indica melhora objetiva da bradicinesia e rigidez.",
    "mcid": "Redução de 3.25 a 4.5 pontos no escore total (Shulman et al., 2010).",
    "referencia_abnt": "Goetz, C. G., Tilley, B. C., Shaftman, S. R., Stebbins, G. T., Fahn, S., Martinez-Martin, P., ... & LaPelle, N. (2008). Movement Disorder Society-sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS): scale presentation and clinimetric testing results. Movement Disorders, 23(15), 2129-2170.",
    "doi": "10.1002/mds.22340",
    "link_artigo": "https://doi.org/10.1002/mds.22340",
    "validacao_brasil": "Godeiro-Junior, C., et al. (2011). Portuguese version of the Movement Disorder Society-Unified Parkinson's Disease Rating Scale. Arquivos de Neuro-Psiquiatria, 69(4), 587-591."
  },
  "meem": {
    "id": "meem",
    "sigla": "MEEM",
    "nome": "Mini-Exame do Estado Mental",
    "nome_en": "Mini-Mental State Examination (MMSE)",
    "dominio": "Rastreio e Monitoramento Cognitivo Global",
    "tempo_aplicacao": "8 a 10 minutos",
    "publico_alvo": "Pacientes com Queixa Cognitiva Subjetiva, Comprometimento Cognitivo Leve (CCL) e Demências (Alzheimer, Vascular).",
    "materiais": "Protocolo impresso do MEEM, relógio de pulso, caneta, folha de papel em branco e desenho impresso de pentágonos sobrepostos.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Orientação Temporal (5 pontos) e Espacial (5 pontos)",
        "descricao": "Pergunte: ano, estação do ano, mês, dia do mês e dia da semana. Pergunte: país, estado, cidade, local em que estamos (hospital/clínica) e andar/sala."
      },
      {
        "passo": 2,
        "titulo": "Memória Imediata / Registro (3 pontos)",
        "descricao": "Diga 3 palavras não relacionadas (ex: GELO, FLOR, CARRO) com clareza (1 segundo por palavra) e peça ao paciente para repeti-las. Repita até 5 vezes se necessário para aprendizado."
      },
      {
        "passo": 3,
        "titulo": "Atenção e Cálculo (5 pontos)",
        "descricao": "Peça para subtrair sucessivamente 7 a partir de 100 por 5 vezes (100 - 7 = 93, 86, 79, 72, 65). Se o paciente for incapaz de calcular, soletre a palavra M-U-N-D-O de trás para frente (O-D-N-U-M)."
      },
      {
        "passo": 4,
        "titulo": "Memória de Evocação Tardia (3 pontos)",
        "descricao": "Peça ao paciente para recordar as 3 palavras mencionadas anteriormente."
      },
      {
        "passo": 5,
        "titulo": "Linguagem e Praxia (9 pontos)",
        "descricao": "Nomear relógio e caneta (2 pts); repetir 'Nem aqui, nem ali, nem lá' (1 pt); executar comando verbal de 3 estágios (1 folha de papel: pegue com mão direita, dobre ao meio, ponha no chão - 3 pts); ler e executar 'FECHE OS OLHOS' (1 pt); escrever uma frase completa com sujeito e predicado (1 pt); copiar desenho dos pentágonos interligados (1 pt)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "Pontuação Máxima",
        "descricao": "30 pontos possíveis."
      },
      {
        "grau": "Pontos de Corte Brasileiros (Brucki et al., 2003)",
        "descricao": "Analfabetos: 20 pontos; 1 a 4 anos de escolaridade: 25 pontos; 5 a 8 anos: 26.5 pontos; 9 a 11 anos: 28 pontos; > 11 anos: 29 pontos."
      }
    ],
    "interpretacao_clinica": "Na estimulação do DLPFC esquerdo com alta frequência ou gamma (40 Hz tACS / rTMS) em Alzheimer/CCL, um ganho >= 2 pontos ou a estabilização longitudinal indica desaceleração do declínio cognitivo.",
    "mcid": "Variação de 1.4 a 2.0 pontos (Howard et al., 2011).",
    "referencia_abnt": "Folstein, M. F., Folstein, S. E., & McHugh, P. R. (1975). 'Mini-mental state': a practical method for grading the cognitive state of patients for the clinician. Journal of Psychiatric Research, 12(3), 189-198.",
    "doi": "10.1016/0022-3956(75)90026-6",
    "link_artigo": "https://doi.org/10.1016/0022-3956(75)90026-6",
    "validacao_brasil": "Brucki, S. M. D., Nitrini, R., Caramelli, P., Bertolucci, P. H. F., & Okamoto, I. H. (2003). Sugestões para o uso do mini-exame do estado mental no Brasil. Arquivos de Neuro-Psiquiatria, 61(3B), 777-781."
  },
  "adas_cog": {
    "id": "adas_cog",
    "sigla": "ADAS-Cog",
    "nome": "Alzheimer's Disease Assessment Scale - Cognitive Subscale",
    "nome_en": "ADAS-Cog (11-item Cognitive Subscale)",
    "dominio": "Desempenho Cognitivo e Progressão na Demência de Alzheimer",
    "tempo_aplicacao": "30 a 45 minutos",
    "publico_alvo": "Pacientes com Doença de Alzheimer em fase leve a moderada em ensaios clínicos.",
    "materiais": "Cartões de estímulo com palavras, objetos reais cotidianos, folhas de desenho estruturadas e protocolo ADAS.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Memória Verbal: Evocação e Reconhecimento de Palavras",
        "descricao": "Teste de aprendizado de lista de 10 palavras em 3 tentativas sucessivas e teste de reconhecimento com palavras distratoras."
      },
      {
        "passo": 2,
        "titulo": "Linguagem e Nomeação de Objetos",
        "descricao": "Nomear objetos reais de baixa e alta frequência e nomear os próprios dedos da mão."
      },
      {
        "passo": 3,
        "titulo": "Comandos e Praxia Ideatória",
        "descricao": "Execução de comandos de 1 a 5 estágios e manuseio simulado de envio de correspondência (dobrar papel, colocar no envelope, selar)."
      },
      {
        "passo": 4,
        "titulo": "Praxia Construcional e Orientação",
        "descricao": "Cópia de figuras geométricas (círculo, dois retângulos sobrepostos, losango, cubo) e avaliação detalhada da orientação têmporo-espacial."
      },
      {
        "passo": 5,
        "titulo": "Avaliação Clínica pelo Examinador",
        "descricao": "Classificação da dificuldade de encontrar palavras na fala espontânea, compreensão da linguagem falada e lembrança das instruções do teste."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 a 70 pontos",
        "descricao": "Pontuação baseada no número de erros cometidos (0 = sem erros / cognitivamente intacto; 70 = comprometimento cognitivo extremo)."
      }
    ],
    "interpretacao_clinica": "Em ensaios de neuromodulação em Alzheimer (DLPFC ou Precúneo), uma redução de pelo menos 3 a 4 pontos no escore ADAS-Cog reflete ganho cognitivo relevante.",
    "mcid": "Redução de 3.1 a 4.0 pontos (Schrag et al., 2012; FDA Guideline for AD trials).",
    "referencia_abnt": "Rosen, W. G., Mohs, R. C., & Davis, K. L. (1984). A new rating scale for Alzheimer's disease. American Journal of Psychiatry, 141(11), 1356-1364.",
    "doi": "10.1176/ajp.141.11.1356",
    "link_artigo": "https://doi.org/10.1176/ajp.141.11.1356",
    "validacao_brasil": "Schultz, R. R., Siviero, M. O., & Bertolucci, P. H. F. (2001). The Brazilian version of the Alzheimer's disease assessment scale-cognitive subscale (ADAS-Cog) in the diagnosis of mild to moderate Alzheimer's disease. Arquivos de Neuro-Psiquiatria, 59(3B), 707-711."
  },
  "bnt": {
    "id": "bnt",
    "sigla": "BNT",
    "nome": "Teste de Nomeação de Boston",
    "nome_en": "Boston Naming Test (BNT)",
    "dominio": "Acesso Lexical e Nomeação Visual por Confrontação",
    "tempo_aplicacao": "10 a 15 minutos",
    "publico_alvo": "Pacientes com Afasia pós-AVC, Afasia Progressiva Primária ou Demência de Alzheimer.",
    "materiais": "Caderno de figuras do BNT (60 pranchas em preto e branco ordenadas por frequência) e folha de registro padronizada.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Apresentação da Figura",
        "descricao": "Apresente cada prancha individualmente por até 20 segundos e pergunte: 'Qual é o nome disto?'."
      },
      {
        "passo": 2,
        "titulo": "Fornecimento de Pista Semântica Padronizada",
        "descricao": "Se houver erro de percepção visual ou ausência de resposta, forneça a pista semântica categórica oficial (ex: 'É uma fruta')."
      },
      {
        "passo": 3,
        "titulo": "Fornecimento de Pista Fonêmica",
        "descricao": "Se o paciente ainda não nomear após a pista semântica, forneça o som da primeira sílaba do nome (ex: 'A-ba...'). Registre se houve acerto após pista fonêmica (não pontua no escore espontâneo)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "Escore Espontâneo",
        "descricao": "Total de acertos corretos espontâneos (0 a 60 pontos)."
      },
      {
        "grau": "Normas Brasileiras (Mansur et al., 2006)",
        "descricao": "Média de acertos em adultos saudáveis com alta escolaridade é de 53 a 57 pontos; em baixa escolaridade de 44 a 49 pontos."
      }
    ],
    "interpretacao_clinica": "Na estimulação da Área de Broca (Giro Frontal Inferior esquerdo com anódica ou iTBS, ou inibição de Broca homóloga direita em afasia não fluente), um aumento >= 4 a 6 acertos no BNT demonstra facilitação do acesso ao léxico fonológico.",
    "mcid": "Ganho de 3 a 5 pontos no escore espontâneo.",
    "referencia_abnt": "Kaplan, E., Goodglass, H., & Weintraub, S. (1983). The Boston Naming Test. Philadelphia: Lea & Febiger.",
    "doi": "10.1037/t27741-000",
    "link_artigo": "https://doi.org/10.1037/t27741-000",
    "validacao_brasil": "Mansur, L. L., Radanovic, M., Araújo, G. C., Taquemori, L. Y., & Greco, L. L. (2006). Teste de nomeação de Boston: desempenho de uma população de São Paulo. Pró-Fono Revista de Atualização Científica, 18(1), 13-20."
  },
  "wab_r": {
    "id": "wab_r",
    "sigla": "WAB-R",
    "nome": "Western Aphasia Battery - Revised",
    "nome_en": "Western Aphasia Battery - Revised (WAB-R)",
    "dominio": "Gravidade da Afasia e Quociente de Afasia (AQ)",
    "tempo_aplicacao": "30 a 45 minutos",
    "publico_alvo": "Pacientes com transtornos de linguagem decorrentes de Acidente Vascular Cerebral.",
    "materiais": "Protocolo de teste WAB-R, pranchas visuais (foto de piquenique), objetos reais cotidianos e cronômetro.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Fala Espontânea (20 pontos)",
        "descricao": "Respostas a 6 perguntas biográficas e descrição oral detalhada da prancha do piquenique (avaliação de conteúdo informativo de 0 a 10 e fluência de 0 a 10)."
      },
      {
        "passo": 2,
        "titulo": "Compreensão Auditiva (200 pontos brutos)",
        "descricao": "Perguntas de Sim/Não, reconhecimento auditivo de palavras por apontamento e execução sequencial de ordens verbais."
      },
      {
        "passo": 3,
        "titulo": "Repetição (100 pontos brutos)",
        "descricao": "Repetição de palavras monossílabas até frases complexas de alta extensão."
      },
      {
        "passo": 4,
        "titulo": "Nomeação e Fluência por Categoria (100 pontos brutos)",
        "descricao": "Nomeação de objetos por confrontação, fluência de animais em 1 minuto, complementação de frases e respostas a perguntas rápidas."
      },
      {
        "passo": 5,
        "titulo": "Cálculo do Quociente de Afasia (AQ)",
        "descricao": "Fórmula: AQ = [Fala espontânea (20) + Compreensão/10 (10) + Repetição/10 (10) + Nomeação/10 (10)] x 2 (escore total de 0 a 100)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "Quociente de Afasia (AQ)",
        "descricao": "Ponto de corte: AQ < 93.8 confirma a presença de afasia clínica."
      },
      {
        "grau": "Classificação",
        "descricao": "0 a 25: Afasia muito grave/global; 26 a 50: Afasia grave; 51 a 75: Afasia moderada; 76 a 93.8: Afasia leve."
      }
    ],
    "interpretacao_clinica": "Em estudos de neuromodulação em afasia crônica, um ganho no AQ >= 5.0 pontos representa melhora funcional comunicativa diária significativa.",
    "mcid": "Ganho de 5.0 pontos no AQ (Katz et al., 2000).",
    "referencia_abnt": "Kertesz, A. (2006). Western Aphasia Battery-Revised (WAB-R). San Antonio, TX: PsychCorp.",
    "doi": "10.1037/t15159-000",
    "link_artigo": "https://doi.org/10.1037/t15159-000",
    "validacao_brasil": "Ferreira, V. M., et al. (2018). Adaptação transcultural e aplicabilidade da Western Aphasia Battery-Revised no Brasil. CoDAS, 30(2), e20170068."
  },
  "fois": {
    "id": "fois",
    "sigla": "FOIS",
    "nome": "Functional Oral Intake Scale",
    "nome_en": "Functional Oral Intake Scale (FOIS)",
    "dominio": "Nível Funcional de Ingestão e Dieta Oral na Disfagia",
    "tempo_aplicacao": "3 minutos",
    "publico_alvo": "Pacientes com disfagia orofaríngea neurogênica pós-AVC ou pós-intubação orotraqueal.",
    "materiais": "Registro da prescrição dietética e entrevista com equipe de enfermagem/fonoaudiologia.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Verificação da Via de Alimentação",
        "descricao": "Identifique se o paciente recebe nutrição por via enteral exclusiva (sonda nasoenteral, gastrostomia) ou por via oral."
      },
      {
        "passo": 2,
        "titulo": "Caracterização das Consistências Alimentares Seguras",
        "descricao": "Para pacientes em via oral, determine se a dieta é restrita a uma única consistência (líquido espessado, pastoso), se exige preparo especial compensatório ou se é dieta livre."
      },
      {
        "passo": 3,
        "titulo": "Classificação no Escore de 1 a 7",
        "descricao": "Selecione o nível que melhor representa o padrão alimentar do paciente no momento atual."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "Nível 1",
        "descricao": "Nada por via oral (alimentação por sonda enteral exclusiva)."
      },
      {
        "grau": "Nível 2",
        "descricao": "Dependente de via alternativa com mínima ingestão oral de alimentos/líquidos (treinamento fonoaudiológico)."
      },
      {
        "grau": "Nível 3",
        "descricao": "Dependente de via alternativa com alimentação consistente de alimento ou líquido por via oral."
      },
      {
        "grau": "Nível 4",
        "descricao": "Via oral total de consistência única (ex: apenas purês pastosos ou líquidos espessados)."
      },
      {
        "grau": "Nível 5",
        "descricao": "Via oral total com múltiplas consistências, mas exigindo preparo especial ou compensações."
      },
      {
        "grau": "Nível 6",
        "descricao": "Via oral total com múltiplas consistências sem preparo especial, mas com restrições alimentares específicas."
      },
      {
        "grau": "Nível 7",
        "descricao": "Via oral total sem quaisquer restrições alimentares (dieta normal irrestrita)."
      }
    ],
    "interpretacao_clinica": "Na estimulação do córtex motor de deglutição (área da faringe/laringe) pós-AVC, a progressão de pelo menos 1 a 2 níveis na FOIS indica transição segura para retirada da sonda enteral.",
    "mcid": "Evolução de pelo menos 1 nível na escala (Crary et al., 2005).",
    "referencia_abnt": "Crary, M. A., Mann, G. D., & Groher, M. E. (2005). Initial psychometric assessment of a functional oral intake scale for dysphagia in stroke patients. Archives of Physical Medicine and Rehabilitation, 86(8), 1516-1520.",
    "doi": "10.1016/j.apmr.2004.11.049",
    "link_artigo": "https://doi.org/10.1016/j.apmr.2004.11.049",
    "validacao_brasil": "Furkim, A. M., & Sacco, A. B. F. (2008). Eficácia da fonoterapia em disfagia neurogênica usando a escala FOIS. Revista CEFAC, 10(4), 503-512."
  },
  "gmfm": {
    "id": "gmfm",
    "sigla": "GMFM",
    "nome": "Gross Motor Function Measure",
    "nome_en": "Gross Motor Function Measure (GMFM-66 / GMFM-88)",
    "dominio": "Função Motora Grossa na Paralisia Cerebral",
    "tempo_aplicacao": "30 a 45 minutos",
    "publico_alvo": "Crianças e adolescentes com Paralisia Cerebral (todos os níveis GMFCS).",
    "materiais": "Colchonete de fisioterapia, banco pequeno, degraus, brinquedos para motivação e formulário GMFM.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Dimensão A: Deitar e Rolar",
        "descricao": "Avalie controle cervical, rolamento de supino para prono e sustentação de cabeça."
      },
      {
        "passo": 2,
        "titulo": "Dimensão B: Sentar",
        "descricao": "Avalie manutenção de sentar com apoio e sem apoio no chão e no banco com pés apoiados."
      },
      {
        "passo": 3,
        "titulo": "Dimensão C: Engatinhar e Ajoelhar",
        "descricao": "Avalie postura de quatro apoios, engatinhar e permanência de joelhos."
      },
      {
        "passo": 4,
        "titulo": "Dimensão D: De Pé",
        "descricao": "Avalie transição de sentado para de pé e manutenção estática de pé."
      },
      {
        "passo": 5,
        "titulo": "Dimensão E: Andar, Correr e Pular",
        "descricao": "Avalie marcha independente, subir e descer degraus e saltos."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 pontos",
        "descricao": "Não inicia a tarefa motora."
      },
      {
        "grau": "1 ponto",
        "descricao": "Inicia a tarefa motora (< 10% de conclusão)."
      },
      {
        "grau": "2 pontos",
        "descricao": "Completa parcialmente a tarefa motora (10% a 99%)."
      },
      {
        "grau": "3 pontos",
        "descricao": "Completa a tarefa com êxito (100%)."
      }
    ],
    "interpretacao_clinica": "Na estimulação transcraniana por corrente contínua (tDCS) combinada com treino motor intensivo na paralisia cerebral, ganhos percentuais de 3% a 5% no GMFM representam avanços funcionais cruciais na autonomia locomotora da criança.",
    "mcid": "Ganho percentual de 3.7% no GMFM-66 (Wang et al., 2017).",
    "referencia_abnt": "Russell, D. J., Rosenbaum, P. L., Cadman, D. T., Gowland, C., Hardy, S., & Jarvis, S. (1989). The gross motor function measure: a means to evaluate the effects of physical therapy. Developmental Medicine & Child Neurology, 31(3), 341-352.",
    "doi": "10.1111/j.1469-8749.1989.tb04003.x",
    "link_artigo": "https://doi.org/10.1111/j.1469-8749.1989.tb04003.x",
    "validacao_brasil": "Campos, A. C., et al. (2008). Tradução e adaptação transcultural da Gross Motor Function Measure para a língua portuguesa. Revista Brasileira de Fisioterapia, 12(1), 56-63."
  },
  "abc": {
    "id": "abc",
    "sigla": "ABC",
    "nome": "Aberrant Behavior Checklist (Irritabilidade / Agitação)",
    "nome_en": "Aberrant Behavior Checklist - Irritability Subscale (ABC-I)",
    "dominio": "Comportamentos Desafiadores e Irritabilidade no TEA",
    "tempo_aplicacao": "10 a 15 minutos (respondido por pais/cuidadores)",
    "publico_alvo": "Crianças e adolescentes com Transtorno do Espectro Autista e deficiência intelectual.",
    "materiais": "Questionário estruturado com 58 itens (subescala de Irritabilidade com 15 itens).",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Instrução ao Cuidador Principal",
        "descricao": "Solicite ao pai, mãe ou cuidador que avalie o comportamento da criança nas últimas 4 semanas."
      },
      {
        "passo": 2,
        "titulo": "Pontuação em Escala de Gravidade",
        "descricao": "Cada comportamento é graduado de 0 (não é problema) a 3 (problema grave de intensidade severa)."
      },
      {
        "passo": 3,
        "titulo": "Foco na Subescala de Irritabilidade",
        "descricao": "A subescala de Irritabilidade/Agitação (itens que cobrem agressividade, autolesão, crises de raiva e gritos) varia de 0 a 45 pontos."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "0 a 45 pontos (ABC-I)",
        "descricao": "Pontuação somatória direta dos 15 itens da subescala de Irritabilidade."
      },
      {
        "grau": "Critério de Resposta em Ensaios",
        "descricao": "Redução >= 25% a 30% no escore inicial reflete resposta clínica favorável em protocolos clínicos de neuromodulação."
      }
    ],
    "interpretacao_clinica": "Na estimulação do DLPFC esquerdo ou bilateral com tDCS / rTMS no TEA, a diminuição dos escores da subescala de irritabilidade reflete melhora na autorregulação emocional e redução de crises comportamentais.",
    "mcid": "Redução mínima de 5 a 6 pontos ou queda de 25% no escore da subescala.",
    "referencia_abnt": "Aman, M. G., Singh, N. N., Stewart, A. W., & Field, C. J. (1985). The aberrant behavior checklist: a rating scale for the assessment of treatment effects. American Journal of Mental Deficiency, 89(5), 485-491.",
    "doi": "10.1037/t10453-000",
    "link_artigo": "https://pubmed.ncbi.nlm.nih.gov/3993694/",
    "validacao_brasil": "Schmidt, C., et al. (2015). Propriedades psicométricas da versão brasileira da Aberrant Behavior Checklist em transtornos do espectro autista. Trends in Psychiatry and Psychotherapy, 37(1), 42-48."
  },
  "srs_2": {
    "id": "srs_2",
    "sigla": "SRS-2",
    "nome": "Social Responsiveness Scale - 2",
    "nome_en": "Social Responsiveness Scale, Second Edition (SRS-2)",
    "dominio": "Comunicação e Responsividade Social no Espectro Autista",
    "tempo_aplicacao": "15 a 20 minutos (respondido por pais/professores)",
    "publico_alvo": "Crianças e adolescentes com suspeita ou diagnóstico de TEA.",
    "materiais": "Questionário padronizado de 65 itens.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Preenchimento dos 65 Itens pelo Cuidador",
        "descricao": "Cada item é pontuado em escala Likert de 1 ('Não é verdadeiro') a 4 ('Quase sempre verdadeiro')."
      },
      {
        "passo": 2,
        "titulo": "Cálculo dos Escores Brutos e Conversão em Escore T",
        "descricao": "Gera pontuações nas subescalas: Consciência Social, Cognição Social, Comunicação Social, Motivação Social e Maneirismos Restritos/Repetitivos."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "Escore T <= 59",
        "descricao": "Dentro dos limites normais / neurotípico."
      },
      {
        "grau": "Escore T 60 a 65",
        "descricao": "Comprometimento leve a moderado em reciprocidade social."
      },
      {
        "grau": "Escore T 66 a 75",
        "descricao": "Comprometimento severo / fortemente indicativo de TEA clínico."
      },
      {
        "grau": "Escore T >= 76",
        "descricao": "Comprometimento muito severo."
      }
    ],
    "interpretacao_clinica": "Na estimulação do DLPFC ou junção temporoparietal em indivíduos com TEA, a redução no Escore T reflete ganhos na habilidade de decodificação de pistas sociais e reciprocidade comunicativa.",
    "mcid": "Redução de 5 pontos no Escore T padronizado.",
    "referencia_abnt": "Constantino, J. N., & Gruber, C. P. (2012). Social Responsiveness Scale, Second Edition (SRS-2). Torrance, CA: Western Psychological Services.",
    "doi": "10.1037/t15140-000",
    "link_artigo": "https://www.wpspublish.com/srs-2-social-responsiveness-scale-second-edition",
    "validacao_brasil": "Fernandes, F. D. M., et al. (2018). Adaptação e validação transcultural da Social Responsiveness Scale 2 (SRS-2) no Brasil. Jornal da Sociedade Brasileira de Fonoaudiologia."
  },
  "npi": {
    "id": "npi",
    "sigla": "NPI",
    "nome": "Inventário Neuropsiquiátrico",
    "nome_en": "Neuropsychiatric Inventory (NPI)",
    "dominio": "Sintomas Comportamentais e Psicológicos nas Demências (BPSD)",
    "tempo_aplicacao": "15 a 20 minutos",
    "publico_alvo": "Pacientes com Doença de Alzheimer, Demência Vascular ou Demência Frontotemporal com sintomas comportamentais.",
    "materiais": "Entrevista clínica estruturada com o cuidador principal.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Investigação dos 12 Domínios Comportamentais",
        "descricao": "Delírios, Alucinações, Agitação/Agressão, Depressão/Disforia, Ansiedade, Euforia, Apatia/Indiferença, Desinibição, Irritabilidade/Labilidade, Comportamento motor aberrante, Sono/comportamento noturno e Apetite/alterações alimentares."
      },
      {
        "passo": 2,
        "titulo": "Graduação de Frequência e Gravidade",
        "descricao": "Para cada domínio presente: Frequência (1 = ocasional a 4 = muito frequente) e Gravidade (1 = leve a 3 = severa). O escore do domínio é o produto Frequência x Gravidade (1 a 12)."
      },
      {
        "passo": 3,
        "titulo": "Avaliação do Desgaste do Cuidador",
        "descricao": "Avalie o estresse emocional gerado em cada domínio de 0 (nenhum) a 5 (extremo)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "Escore Total (0 a 144)",
        "descricao": "Soma dos 12 domínios (Frequência x Gravidade)."
      },
      {
        "grau": "Desgaste do Cuidador (0 a 60)",
        "descricao": "Soma do estresse percebido pelo cuidador."
      }
    ],
    "interpretacao_clinica": "Em ensaios de estimulação pré-frontal para controle de apatia ou agitação em demências, uma redução de pelo menos 4 a 8 pontos no NPI representa alívio expressivo da carga de sintomas.",
    "mcid": "Redução mínima de 4 pontos no escore total (Kaufer et al., 2000).",
    "referencia_abnt": "Cummings, J. L., Mega, M., Gray, K., Rosenberg-Thompson, S., Carusi, D. A., & Gornbein, J. (1994). The Neuropsychiatric Inventory: comprehensive assessment of psychopathology in dementia. Neurology, 44(12), 2308-2314.",
    "doi": "10.1212/wnl.44.12.2308",
    "link_artigo": "https://doi.org/10.1212/wnl.44.12.2308",
    "validacao_brasil": "Camozzato, A. L., Kochhann, R., Simeoni, C., Konrath, C. A., Franz, A. P., Carvalho, A., & Chaves, M. L. (2008). Reliability of the Brazilian Portuguese version of the Neuropsychiatric Inventory (NPI) for caregivers of patients with dementia. International Psychogeriatrics, 20(3), 577-584."
  },
  "tc10m": {
    "id": "tc10m",
    "sigla": "TC10m",
    "nome": "Teste de Caminhada de 10 Metros",
    "nome_en": "10-Meter Walk Test (10MWT)",
    "dominio": "Velocidade da Marcha Funcional (m/s)",
    "tempo_aplicacao": "3 a 5 minutos",
    "publico_alvo": "Pacientes com sequelas de AVC, Doença de Parkinson, Lesão Medular e Ataxias.",
    "materiais": "Pista reta e plana de 14 metros, fita métrica, fita adesiva de demarcação e cronômetro.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Demarcação da Pista de Marcha",
        "descricao": "Demarque 14 metros: os primeiros 2 metros para aceleração, os 10 metros centrais para cronometragem e os últimos 2 metros para desaceleração."
      },
      {
        "passo": 2,
        "titulo": "Comando Verbal Padronizado",
        "descricao": "Oriente: 'Caminhe em sua velocidade confortável e segura (ou em velocidade máxima) até passar da linha final'."
      },
      {
        "passo": 3,
        "titulo": "Cronometragem dos 10 Metros Centrais",
        "descricao": "Inicie o cronômetro no momento em que o primeiro pé cruzar a marca de 2 metros; pare o cronômetro no momento em que o primeiro pé cruzar a marca de 12 metros."
      },
      {
        "passo": 4,
        "titulo": "Cálculo da Velocidade da Marcha",
        "descricao": "Calcule a velocidade em metros por segundo: Velocidade (m/s) = 10 / Tempo registrado (segundos)."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "< 0.4 m/s",
        "descricao": "Deambulador exclusivamente domiciliar restrito."
      },
      {
        "grau": "0.4 a 0.8 m/s",
        "descricao": "Deambulador comunitário limitado (necessita de auxílio em calçadas/rua)."
      },
      {
        "grau": "> 0.8 m/s",
        "descricao": "Deambulador comunitário pleno e independente."
      }
    ],
    "interpretacao_clinica": "Na estimulação da Área Motora Suplementar (SMA / Cz) ou M1 de membros inferiores pós-AVC, um incremento de 0.10 a 0.16 m/s é o limiar de melhora clinicamente importante.",
    "mcid": "Aumento de 0.10 a 0.16 m/s (Perera et al., 2006; Tilson et al., 2010).",
    "referencia_abnt": "Perry, J., Garrett, M., Gronley, J. K., & Mulroy, S. J. (1995). Classification of walking handicap in the stroke population. Stroke, 26(6), 982-989.",
    "doi": "10.1161/01.str.26.6.982",
    "link_artigo": "https://doi.org/10.1161/01.str.26.6.982",
    "validacao_brasil": "Medeiros, C. S., et al. (2016). Confiabilidade teste-reteste do teste de caminhada de 10 metros em hemiparéticos crônicos. Revista Fisioterapia e Pesquisa."
  },
  "peg9": {
    "id": "peg9",
    "sigla": "9HPT",
    "nome": "Nine-Hole Peg Test",
    "nome_en": "Nine-Hole Peg Test (9HPT)",
    "dominio": "Destreza Motora Fina Manual",
    "tempo_aplicacao": "3 a 5 minutos",
    "publico_alvo": "Pacientes com Ataxia Espinocerebelar, Doença de Parkinson, Esclerose Múltipla e AVC.",
    "materiais": "Prancha de madeira ou plástico com 9 orifícios cilíndricos, 9 pinos e cronômetro.",
    "procedimento_passo_a_passo": [
      {
        "passo": 1,
        "titulo": "Posicionamento da Prancha",
        "descricao": "Coloque a prancha alinhada à linha média do paciente, com o recipiente de pinos do lado da mão a ser testada."
      },
      {
        "passo": 2,
        "titulo": "Instrução de Execução Rápida",
        "descricao": "Instrua: 'Pegue os pinos um a um o mais rápido possível e coloque-os nos buracos; assim que todos estiverem colocados, retire-os um a um e coloque-os de volta no recipiente'."
      },
      {
        "passo": 3,
        "titulo": "Cronometragem",
        "descricao": "Inicie o cronômetro no momento em que o paciente tocar no primeiro pino; pare quando o último pino for depositado no recipiente. Teste mão dominante e mão não dominante."
      }
    ],
    "criterios_pontuacao": [
      {
        "grau": "Tempo em Segundos",
        "descricao": "Registrado para cada mão individualmente."
      },
      {
        "grau": "Valores Normativos",
        "descricao": "Adultos saudáveis completam o teste em aproximadamente 18 a 22 segundos."
      }
    ],
    "interpretacao_clinica": "Em ataxias cerebelares ou AVC, a redução de pelo menos 20% no tempo de execução ou uma redução de 3 a 5 segundos representa ganho de coordenação motora fina.",
    "mcid": "Redução de 20% no tempo em segundos (Earhart et al., 2011).",
    "referencia_abnt": "Mathiowetz, V., Weber, K., Kashman, N., & Volland, G. (1985). Adult norms for the Nine Hole Peg Test of finger dexterity. The Occupational Therapy Journal of Research, 5(1), 24-38.",
    "doi": "10.1177/153944928500500102",
    "link_artigo": "https://doi.org/10.1177/153944928500500102",
    "validacao_brasil": "Oxford Grice, K., et al. (2003); Normas brasileiras em Oliveira, C. S., et al. (2012)."
  }
};
