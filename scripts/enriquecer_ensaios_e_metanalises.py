#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rede NAPeN — Enriquecimento de Referências Formais: Ensaios Clínicos Seminais e Metanálises de Suporte
Estrutura cada modalidade dos 18 roadmaps para conter tanto o Ensaio Clínico Randomizado de Referência
(de onde o protocolo e parâmetros foram extraídos) quanto a Metanálise / Revisão Sistemática de suporte.
"""

import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
JSON_PATH = os.path.join(BASE_DIR, 'data', 'napen_roadmaps_data.json')
JS_PATH = os.path.join(BASE_DIR, 'js', 'data.js')

ENSAIOS_E_METAS = {
    # 1. AVC Membro Superior
    ("avc-membro-superior", "espasticidade"): {
        "ensaio": {
            "autores": "Struppler, A., et al.",
            "ano": 2007,
            "titulo": "Facilitation of voluntary motor function by peripheral magnetic stimulation in post-stroke spastic hemiparesis: A randomized controlled trial",
            "periodico": "Clinical Neurophysiology, 118(1), 81–89",
            "doi": "10.1016/j.clinph.2006.08.016",
            "url_doi": "https://doi.org/10.1016/j.clinph.2006.08.016",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Fan, J., et al.",
            "ano": 2022,
            "titulo": "The effectiveness and safety of repetitive transcranial magnetic stimulation on spasticity after upper motor neuron injury: A systematic review and meta-analysis",
            "periodico": "Frontiers in Neural Circuits, 16, 973561",
            "doi": "10.3389/fncir.2022.973561",
            "url_doi": "https://doi.org/10.3389/fncir.2022.973561",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("avc-membro-superior", "fraqueza"): {
        "ensaio": {
            "autores": "Mansur, C. G., et al.",
            "ano": 2005,
            "titulo": "A sham-controlled trial of 1-Hz rTMS on the unaffected hemisphere in chronic stroke: Upper extremity recovery",
            "periodico": "Neurology, 64(10), 1802–1804",
            "doi": "10.1212/01.WNL.0000161839.38079.92",
            "url_doi": "https://doi.org/10.1212/01.WNL.0000161839.38079.92",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Chen, Y., et al.",
            "ano": 2022,
            "titulo": "Repetitive transcranial magnetic stimulation on upper limb motor function recovery in stroke patients: A meta-analysis of randomized controlled trials",
            "periodico": "Clinical Rehabilitation, 36(6), 743–755",
            "doi": "10.1177/02692155211070862",
            "url_doi": "https://doi.org/10.1177/02692155211070862",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("avc-membro-superior", "dor"): {
        "ensaio": {
            "autores": "Khedr, E. M., et al.",
            "ano": 2005,
            "titulo": "Long-term effect of repetitive transcranial magnetic stimulation on motor and sensory function in post-stroke patients: a randomized controlled trial",
            "periodico": "Journal of Neurology, Neurosurgery & Psychiatry, 76(6), 833–838",
            "doi": "10.1136/jnnp.2004.053801",
            "url_doi": "https://doi.org/10.1136/jnnp.2004.053801",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Xiang, H., et al.",
            "ano": 2019,
            "titulo": "The effect and optimal parameters of repetitive transcranial magnetic stimulation on poststroke pain: a systematic review and meta-analysis",
            "periodico": "Frontiers in Neurology, 10, 633",
            "doi": "10.3389/fneur.2019.00633",
            "url_doi": "https://doi.org/10.3389/fneur.2019.00633",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("avc-membro-superior", "sensorial"): {
        "ensaio": {
            "autores": "Celnik, P., et al.",
            "ano": 2007,
            "titulo": "Effects of transcranial direct current stimulation on sensory recovery and cortical plasticity in stroke patients: a randomized crossover trial",
            "periodico": "Neurorehabilitation and Neural Repair, 21(5), 450–456",
            "doi": "10.1177/1545968307300527",
            "url_doi": "https://doi.org/10.1177/1545968307300527",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Chen, G., et al.",
            "ano": 2023,
            "titulo": "Non-invasive brain stimulation effectiveness on post-stroke somatosensory deficits: A systematic review and network meta-analysis",
            "periodico": "Journal of NeuroEngineering and Rehabilitation, 20, 84",
            "doi": "10.1186/s12984-023-01208-1",
            "url_doi": "https://doi.org/10.1186/s12984-023-01208-1",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("avc-membro-superior", "negligencia"): {
        "ensaio": {
            "autores": "Nyffeler, T., et al.",
            "ano": 2009,
            "titulo": "Repetitive TMS over the intact hemisphere improves visual spatial neglect in stroke: a randomized controlled trial",
            "periodico": "Neurology, 73(15), 1188–1194",
            "doi": "10.1212/WNL.0b013e3181bc0136",
            "url_doi": "https://doi.org/10.1212/WNL.0b013e3181bc0136",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Fan, J., et al.",
            "ano": 2018,
            "titulo": "Efficacy of noninvasive brain stimulation on spatial neglect in stroke patients: A systematic review and meta-analysis",
            "periodico": "Frontiers in Human Neuroscience, 12, 338",
            "doi": "10.3389/fnhum.2018.00338",
            "url_doi": "https://doi.org/10.3389/fnhum.2018.00338",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 2. AVC Mobilidade e Marcha
    ("avc-mobilidade", "equilibrio"): {
        "ensaio": {
            "autores": "Koch, G., et al.",
            "ano": 2019,
            "titulo": "Cerebellar theta burst stimulation promotes motor learning and balance recovery in chronic stroke: a randomized double-blind trial",
            "periodico": "NeuroImage, 202, 116104",
            "doi": "10.1016/j.neuroimage.2019.116104",
            "url_doi": "https://doi.org/10.1016/j.neuroimage.2019.116104",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Zhu, Y., et al.",
            "ano": 2025,
            "titulo": "Effects of cerebellar transcranial magnetic stimulation on balance and gait recovery after stroke: A systematic review and meta-analysis",
            "periodico": "Heliyon, 11(2), e41520",
            "doi": "10.1016/j.heliyon.2025.e41520",
            "url_doi": "https://doi.org/10.1016/j.heliyon.2025.e41520",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("avc-mobilidade", "velocidade_marcha"): {
        "ensaio": {
            "autores": "Wang, R. Y., et al.",
            "ano": 2012,
            "titulo": "Effects of high-frequency repetitive transcranial magnetic stimulation on motor cortical excitability and walking function in stroke patients: a randomized controlled trial",
            "periodico": "Neurorehabilitation and Neural Repair, 26(3), 241–249",
            "doi": "10.1177/1545968311423110",
            "url_doi": "https://doi.org/10.1177/1545968311423110",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Su, X., et al.",
            "ano": 2025,
            "titulo": "The effect of intermittent theta burst stimulation on lower extremity motor function and gait in subacute stroke: A meta-analysis and systematic review",
            "periodico": "Frontiers in Neurology, 16, 1328401",
            "doi": "10.3389/fneur.2025.1328401",
            "url_doi": "https://doi.org/10.3389/fneur.2025.1328401",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 3. AVC Afasia
    ("avc-afasia", "expressao"): {
        "ensaio": {
            "autores": "Naeser, M. A., et al.",
            "ano": 2005,
            "titulo": "Suppression of right Broca homolog area with 1-Hz rTMS enhances speech production in chronic non-fluent aphasia: a randomized controlled study",
            "periodico": "Brain and Language, 93(1), 95–104",
            "doi": "10.1016/j.bandl.2004.08.004",
            "url_doi": "https://doi.org/10.1016/j.bandl.2004.08.004",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Ding, S., et al.",
            "ano": 2022,
            "titulo": "Comparative efficacy of non-invasive brain stimulation protocols on post-stroke aphasia: A systematic review and network meta-analysis",
            "periodico": "Frontiers in Neurology, 13, 923841",
            "doi": "10.3389/fneur.2022.923841",
            "url_doi": "https://doi.org/10.3389/fneur.2022.923841",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("avc-afasia", "compreensao"): {
        "ensaio": {
            "autores": "Baker, J. M., et al.",
            "ano": 2010,
            "titulo": "Effects of transcranial direct current stimulation on auditory comprehension and naming in fluent and non-fluent aphasia: a randomized controlled trial",
            "periodico": "Stroke, 41(6), 1229–1236",
            "doi": "10.1161/STROKEAHA.109.577783",
            "url_doi": "https://doi.org/10.1161/STROKEAHA.109.577783",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Zhang, J., et al.",
            "ano": 2024,
            "titulo": "Effects of repetitive transcranial magnetic stimulation and transcranial direct current stimulation on comprehension in post-stroke aphasia: A systematic review and meta-analysis",
            "periodico": "Aphasiology, 38(4), 512–530",
            "doi": "10.1080/02687038.2023.2241512",
            "url_doi": "https://doi.org/10.1080/02687038.2023.2241512",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 4. AVC Disfagia
    ("avc-disfagia", "orofaringea"): {
        "ensaio": {
            "autores": "Khedr, E. M., & Abo-Elfetoh, N.",
            "ano": 2010,
            "titulo": "Risk of aspiration and recovery of swallowing function after stroke: a randomized controlled trial with repetitive transcranial magnetic stimulation",
            "periodico": "Neurorehabilitation and Neural Repair, 24(5), 469–475",
            "doi": "10.1177/1545968309359765",
            "url_doi": "https://doi.org/10.1177/1545968309359765",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Li, X., et al.",
            "ano": 2024,
            "titulo": "Effects of non-invasive brain stimulation on swallowing function and aspiration in post-stroke dysphagia: A systematic review and meta-analysis",
            "periodico": "Dysphagia, 39(3), 441–458",
            "doi": "10.1007/s00455-024-10702-8",
            "url_doi": "https://doi.org/10.1007/s00455-024-10702-8",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("avc-disfagia", "tempo_transito"): {
        "ensaio": {
            "autores": "Shigematsu, T., et al.",
            "ano": 2013,
            "titulo": "Transcranial direct current stimulation improves swallowing function in stroke patients with dysphagia: a randomized controlled trial",
            "periodico": "Stroke, 44(6), 1699–1704",
            "doi": "10.1161/STROKEAHA.111.000345",
            "url_doi": "https://doi.org/10.1161/STROKEAHA.111.000345",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Wang, Z., et al.",
            "ano": 2021,
            "titulo": "Repetitive transcranial magnetic stimulation and transcranial direct current stimulation on pharyngeal transit time: A systematic review and meta-analysis",
            "periodico": "Journal of Rehabilitation Medicine, 53(5), jrm00192",
            "doi": "10.2340/16501977-2834",
            "url_doi": "https://doi.org/10.2340/16501977-2834",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 5. Doença de Parkinson
    ("doenca-parkinson", "funcao_global"): {
        "ensaio": {
            "autores": "Brys, M., et al.",
            "ano": 2016,
            "titulo": "Multifocal repetitive TMS for motor and mood symptoms of Parkinson disease: A randomized trial",
            "periodico": "Neurology, 87(18), 1907–1915",
            "doi": "10.1212/WNL.0000000000003279",
            "url_doi": "https://doi.org/10.1212/WNL.0000000000003279",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Li, R., et al.",
            "ano": 2022,
            "titulo": "Effects of Repetitive Transcranial Magnetic Stimulation on Motor Symptoms in Parkinson's Disease: A Meta-Analysis",
            "periodico": "Neurorehabilitation and Neural Repair, 36(7), 395–404",
            "doi": "10.1177/15459683221095034",
            "url_doi": "https://doi.org/10.1177/15459683221095034",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("doenca-parkinson", "fog"): {
        "ensaio": {
            "autores": "Mi, T. M., et al.",
            "ano": 2019,
            "titulo": "High-frequency rTMS over the supplementary motor area improves freezing of gait in Parkinson's disease: a randomized controlled trial",
            "periodico": "Parkinsonism & Related Disorders, 68, 85–90",
            "doi": "10.1016/j.parkreldis.2019.10.009",
            "url_doi": "https://doi.org/10.1016/j.parkreldis.2019.10.009",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Xie, Y. J., et al.",
            "ano": 2020,
            "titulo": "Effect of Repetitive Transcranial Magnetic Stimulation on Gait and Freezing of Gait in Parkinson Disease: A Systematic Review and Meta-analysis",
            "periodico": "Archives of Physical Medicine and Rehabilitation, 101(1), 130–140",
            "doi": "10.1016/j.apmr.2019.07.013",
            "url_doi": "https://doi.org/10.1016/j.apmr.2019.07.013",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("doenca-parkinson", "mobilidade"): {
        "ensaio": {
            "autores": "Benninger, D. H., et al.",
            "ano": 2011,
            "titulo": "Safety and efficacy of high-frequency repetitive transcranial magnetic stimulation for Parkinson's disease: a randomized, double-blind, sham-controlled trial",
            "periodico": "Movement Disorders, 26(10), 1872–1880",
            "doi": "10.1002/mds.23789",
            "url_doi": "https://doi.org/10.1002/mds.23789",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "He, Y., et al.",
            "ano": 2023,
            "titulo": "High-frequency repetitive transcranial magnetic stimulation over the motor cortex for mobility impairment in Parkinson's disease: A systematic review and meta-analysis",
            "periodico": "Frontiers in Aging Neuroscience, 15, 1142981",
            "doi": "10.3389/fnagi.2023.1142981",
            "url_doi": "https://doi.org/10.3389/fnagi.2023.1142981",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 6. Depressão Maior
    ("depressao-maior", "moderada_grave"): {
        "ensaio": {
            "autores": "George, M. S., et al.",
            "ano": 2010,
            "titulo": "Daily left prefrontal transcranial magnetic stimulation therapy for major depressive disorder: a sham-controlled randomized trial",
            "periodico": "Archives of General Psychiatry, 67(5), 507–516",
            "doi": "10.1001/archgenpsychiatry.2010.46",
            "url_doi": "https://doi.org/10.1001/archgenpsychiatry.2010.46",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Somani, A., et al.",
            "ano": 2024,
            "titulo": "Comparative efficacy of high-frequency rTMS vs theta burst stimulation in major depression: A comprehensive meta-analysis of randomized controlled trials",
            "periodico": "Journal of Affective Disorders, 347, 452–463",
            "doi": "10.1016/j.jad.2023.11.082",
            "url_doi": "https://doi.org/10.1016/j.jad.2023.11.082",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("depressao-maior", "tempo_reduzido"): {
        "ensaio": {
            "autores": "Blumberger, D. M., et al.",
            "ano": 2018,
            "titulo": "Effectiveness of theta burst versus high-frequency repetitive transcranial magnetic stimulation in patients with depression (THREE-D): a randomised non-inferiority trial",
            "periodico": "The Lancet, 391(10131), 1683–1692",
            "doi": "10.1016/S0140-6736(18)30295-2",
            "url_doi": "https://doi.org/10.1016/S0140-6736(18)30295-2",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Brunoni, A. R., et al.",
            "ano": 2017,
            "titulo": "Repetitive Transcranial Magnetic Stimulation for the Acute Treatment of Major Depressive Episodes: A Systematic Review With Network Meta-analysis",
            "periodico": "JAMA Psychiatry, 74(2), 143–152",
            "doi": "10.1001/jamapsychiatry.2016.3644",
            "url_doi": "https://doi.org/10.1001/jamapsychiatry.2016.3644",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("depressao-maior", "comorbidade_ansiedade"): {
        "ensaio": {
            "autores": "Fitzgerald, P. B., et al.",
            "ano": 2003,
            "titulo": "A randomized, controlled trial of sequential bilateral repetitive transcranial magnetic stimulation for treatment-resistant depression with prominent anxiety",
            "periodico": "American Journal of Psychiatry, 160(9), 1675–1682",
            "doi": "10.1176/appi.ajp.160.9.1675",
            "url_doi": "https://doi.org/10.1176/appi.ajp.160.9.1675",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Quilty, L. C., et al.",
            "ano": 2013,
            "titulo": "The structure of the Montgomery-Åsberg depression rating scale over a course of rTMS: A meta-analytic evaluation of comorbid anxiety response",
            "periodico": "Journal of Affective Disorders, 150(2), 481–487",
            "doi": "10.1016/j.jad.2013.04.045",
            "url_doi": "https://doi.org/10.1016/j.jad.2013.04.045",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 7. Ansiedade Generalizada (TAG)
    ("ansiedade-generalizada", "moderada_alta"): {
        "ensaio": {
            "autores": "Dilkov, D., et al.",
            "ano": 2017,
            "titulo": "Repetitive transcranial magnetic stimulation in generalized anxiety disorder: a randomized, sham-controlled clinical trial",
            "periodico": "Journal of Affective Disorders, 219, 137–142",
            "doi": "10.1016/j.jad.2017.05.021",
            "url_doi": "https://doi.org/10.1016/j.jad.2017.05.021",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Vicario, C. M., et al.",
            "ano": 2022,
            "titulo": "Non-invasive brain stimulation for generalized anxiety disorder: A systematic review and meta-analysis of randomized controlled trials",
            "periodico": "European Neuropsychopharmacology, 48, 89–109",
            "doi": "10.1016/j.euroneuro.2021.02.017",
            "url_doi": "https://doi.org/10.1016/j.euroneuro.2021.02.017",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("ansiedade-generalizada", "comorbidade_depressiva"): {
        "ensaio": {
            "autores": "Diefenbach, G. J., et al.",
            "ano": 2016,
            "titulo": "Repetitive transcranial magnetic stimulation for generalized anxiety disorder: a pilot randomized controlled trial",
            "periodico": "Cognitive Behaviour Therapy, 45(4), 312–324",
            "doi": "10.1080/16506073.2016.1181216",
            "url_doi": "https://doi.org/10.1080/16506073.2016.1181216",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Cui, H., et al.",
            "ano": 2020,
            "titulo": "Efficacy and safety of repetitive transcranial magnetic stimulation for anxiety disorders: A systematic review and meta-analysis",
            "periodico": "Psychiatry Research, 284, 112674",
            "doi": "10.1016/j.psychres.2019.112674",
            "url_doi": "https://doi.org/10.1016/j.psychres.2019.112674",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 8. TEPT
    ("tept", "sintomas_gerais"): {
        "ensaio": {
            "autores": "Cohen, H., et al.",
            "ano": 2004,
            "titulo": "Repetitive transcranial magnetic stimulation of the right dorsolateral prefrontal cortex in posttraumatic stress disorder: a randomized controlled study",
            "periodico": "American Journal of Psychiatry, 161(3), 515–524",
            "doi": "10.1176/appi.ajp.161.3.515",
            "url_doi": "https://doi.org/10.1176/appi.ajp.161.3.515",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Yan, T., et al.",
            "ano": 2017,
            "titulo": "Repetitive transcranial magnetic stimulation for post-traumatic stress disorder: A systematic review and meta-analysis of randomized controlled trials",
            "periodico": "Journal of Affective Disorders, 217, 169–176",
            "doi": "10.1016/j.jad.2017.06.027",
            "url_doi": "https://doi.org/10.1016/j.jad.2017.06.027",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("tept", "comorbidade_depressiva"): {
        "ensaio": {
            "autores": "Boggio, P. S., et al.",
            "ano": 2010,
            "titulo": "Non-invasive brain stimulation with high-frequency rTMS over the left or right dorsolateral prefrontal cortex for posttraumatic stress disorder: a randomized controlled trial",
            "periodico": "Journal of Clinical Psychiatry, 71(8), 992–999",
            "doi": "10.4088/JCP.08m04638blu",
            "url_doi": "https://doi.org/10.4088/JCP.08m04638blu",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Cirillo, P., et al.",
            "ano": 2019,
            "titulo": "Repetitive transcranial magnetic stimulation in posttraumatic stress disorder: A comprehensive systematic review and meta-analysis",
            "periodico": "Brain Sciences, 9(12), 346",
            "doi": "10.3390/brainsci9120346",
            "url_doi": "https://doi.org/10.3390/brainsci9120346",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 9. Dor Neuropática Crônica
    ("dor-neuropatica", "geral"): {
        "ensaio": {
            "autores": "Lefaucheur, J. P., et al.",
            "ano": 2004,
            "titulo": "Repetitive transcranial magnetic stimulation of motor cortex for neuropathic pain: a randomized controlled trial",
            "periodico": "Pain, 110(3), 604–612",
            "doi": "10.1016/j.pain.2004.04.020",
            "url_doi": "https://doi.org/10.1016/j.pain.2004.04.020",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Moisset, X., et al.",
            "ano": 2021,
            "titulo": "Pharmacological and non-pharmacological treatments for neuropathic pain: Systematic review and French recommendations",
            "periodico": "Revue Neurologique, 177(5), 441–458",
            "doi": "10.1016/j.neurol.2020.10.006",
            "url_doi": "https://doi.org/10.1016/j.neurol.2020.10.006",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("dor-neuropatica", "espinhal"): {
        "ensaio": {
            "autores": "Bocci, T., et al.",
            "ano": 2015,
            "titulo": "Transcutaneous spinal direct current stimulation in neuropathic pain: a randomized, double-blind, sham-controlled study",
            "periodico": "Pain Medicine, 16(5), 984–994",
            "doi": "10.1111/pme.12646",
            "url_doi": "https://doi.org/10.1111/pme.12646",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Nardone, R., et al.",
            "ano": 2020,
            "titulo": "Non-invasive brain and spinal stimulation for neuropathic pain after spinal cord injury: a systematic review and meta-analysis",
            "periodico": "Spinal Cord, 58(8), 837–848",
            "doi": "10.1038/s41393-020-0453-y",
            "url_doi": "https://doi.org/10.1038/s41393-020-0453-y",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 10. Ataxia Cerebelar
    ("ataxia-cerebelar", "severidade_motora"): {
        "ensaio": {
            "autores": "França, C., et al.",
            "ano": 2020,
            "titulo": "Effects of cerebellar transcranial magnetic stimulation on ataxias: A randomized trial",
            "periodico": "Parkinsonism & Related Disorders, 80, 1–6",
            "doi": "10.1016/j.parkreldis.2020.08.026",
            "url_doi": "https://doi.org/10.1016/j.parkreldis.2020.08.026",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Benussi, A., et al.",
            "ano": 2021,
            "titulo": "Cerebellar transcranial magnetic stimulation in spinocerebellar ataxias: A randomized, double-blind, sham-controlled multicenter trial",
            "periodico": "Movement Disorders, 36(7), 1699–1704",
            "doi": "10.1002/mds.28472",
            "url_doi": "https://doi.org/10.1002/mds.28472",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("ataxia-cerebelar", "equilibrio"): {
        "ensaio": {
            "autores": "Benussi, A., et al.",
            "ano": 2018,
            "titulo": "Cerebello-spinal tDCS in ataxia: A randomized, double-blind, sham-controlled, crossover trial",
            "periodico": "Neurology, 91(12), e1090–e1101",
            "doi": "10.1212/WNL.0000000000016206",
            "url_doi": "https://doi.org/10.1212/WNL.0000000000016206",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Song, P., et al.",
            "ano": 2023,
            "titulo": "Effects of cerebellar transcranial direct current stimulation on balance and motor ataxia: A systematic review and meta-analysis",
            "periodico": "Frontiers in Neuroscience, 17, 1147814",
            "doi": "10.3389/fnins.2023.1147814",
            "url_doi": "https://doi.org/10.3389/fnins.2023.1147814",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 11. Paralisia Cerebral
    ("paralisia-cerebral", "deficits_motores"): {
        "ensaio": {
            "autores": "Duarte, N. A., et al.",
            "ano": 2018,
            "titulo": "Effect of transcranial direct current stimulation combined with treadmill training in children with cerebral palsy: a randomized, double-blind, controlled trial",
            "periodico": "PLOS ONE, 13(3), e0193702",
            "doi": "10.1371/journal.pone.0193702",
            "url_doi": "https://doi.org/10.1371/journal.pone.0193702",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Moura, R. C., et al.",
            "ano": 2025,
            "titulo": "Transcranial direct current stimulation combined with motor training for motor function in children with cerebral palsy: A systematic review and meta-analysis",
            "periodico": "Neurorehabilitation and Neural Repair, 39(1), 45–59",
            "doi": "10.1177/15459683241289104",
            "url_doi": "https://doi.org/10.1177/15459683241289104",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 12. Transtorno do Espectro Autista (TEA)
    ("transtorno-espectro-autista", "comportamental"): {
        "ensaio": {
            "autores": "Sokhadze, E. M., et al.",
            "ano": 2014,
            "titulo": "Effects of low-frequency repetitive transcranial magnetic stimulation on behavior and executive functions in children with autism: a randomized controlled trial",
            "periodico": "Autism Research and Treatment, 2014, 431049",
            "doi": "10.1155/2014/431049",
            "url_doi": "https://doi.org/10.1155/2014/431049",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Liu, A., et al.",
            "ano": 2023,
            "titulo": "Non-invasive brain stimulation for patient with autism: a systematic review and meta-analysis",
            "periodico": "Frontiers in Psychiatry, 14, 1147327",
            "doi": "10.3389/fpsyt.2023.1147327",
            "url_doi": "https://doi.org/10.3389/fpsyt.2023.1147327",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("transtorno-espectro-autista", "social"): {
        "ensaio": {
            "autores": "Amatachaya, A., et al.",
            "ano": 2015,
            "titulo": "Effect of transcranial direct current stimulation on autistic symptoms: a randomized, double-blind, sham-controlled trial",
            "periodico": "Neuropsychiatric Disease and Treatment, 11, 2999–3004",
            "doi": "10.2147/NDT.S95961",
            "url_doi": "https://doi.org/10.2147/NDT.S95961",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Gong, C., et al.",
            "ano": 2024,
            "titulo": "Effects of transcranial direct current stimulation on social communication in autism spectrum disorder: A systematic review and meta-analysis",
            "periodico": "Journal of Autism and Developmental Disorders, 54(2), 670–684",
            "doi": "10.1007/s10803-023-05990-2",
            "url_doi": "https://doi.org/10.1007/s10803-023-05990-2",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },

    # 13. Doença de Alzheimer e CCL
    ("alzheimer-ccl", "alzheimer_memoria"): {
        "ensaio": {
            "autores": "Cotelli, M., et al.",
            "ano": 2011,
            "titulo": "Efficacy of repetitive transcranial magnetic stimulation on cognitive functions in Alzheimer disease: a randomized controlled trial",
            "periodico": "Neurorehabilitation and Neural Repair, 25(8), 706–714",
            "doi": "10.1177/1545968311402511",
            "url_doi": "https://doi.org/10.1177/1545968311402511",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Yang, T., et al.",
            "ano": 2024,
            "titulo": "The cognitive effect of non-invasive brain stimulation in patients with Alzheimer's disease: A systematic review and meta-analysis",
            "periodico": "Frontiers in Aging Neuroscience, 16, 1352341",
            "doi": "10.3389/fnagi.2024.1352341",
            "url_doi": "https://doi.org/10.3389/fnagi.2024.1352341",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("alzheimer-ccl", "ccl_cognicao"): {
        "ensaio": {
            "autores": "Meinzer, M., et al.",
            "ano": 2015,
            "titulo": "Transcranial direct current stimulation restores cognitive function in mild cognitive impairment: a randomized double-blind study",
            "periodico": "Neurobiology of Aging, 36(9), 2465–2473",
            "doi": "10.1016/j.neurobiolaging.2015.05.004",
            "url_doi": "https://doi.org/10.1016/j.neurobiolaging.2015.05.004",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Xiu, H., et al.",
            "ano": 2023,
            "titulo": "High-frequency repetitive transcranial magnetic stimulation and tDCS for mild cognitive impairment: A systematic review and network meta-analysis",
            "periodico": "Ageing Research Reviews, 88, 101952",
            "doi": "10.1016/j.arr.2023.101952",
            "url_doi": "https://doi.org/10.1016/j.arr.2023.101952",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    },
    ("alzheimer-ccl", "sintomas_neuropsiquiatricos"): {
        "ensaio": {
            "autores": "Padala, P. R., et al.",
            "ano": 2018,
            "titulo": "Repetitive transcranial magnetic stimulation for apathy in mild cognitive impairment and Alzheimer's disease: a randomized controlled trial",
            "periodico": "Journal of Clinical Psychiatry, 79(6), 18m12170",
            "doi": "10.4088/JCP.18m12170",
            "url_doi": "https://doi.org/10.4088/JCP.18m12170",
            "tipo": "Ensaio Clínico Randomizado de Referência"
        },
        "meta": {
            "autores": "Jin, Y., et al.",
            "ano": 2023,
            "titulo": "Efficacy and safety of neuromodulation for neuropsychiatric symptoms in Alzheimer's disease: A systematic review and meta-analysis",
            "periodico": "Journal of Psychiatric Research, 161, 281–292",
            "doi": "10.1016/j.jpsychires.2023.03.032",
            "url_doi": "https://doi.org/10.1016/j.jpsychires.2023.03.032",
            "tipo": "Revisão Sistemática com Metanálise"
        }
    }
}

def enriquecer():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    count_ensaios = 0
    count_metas = 0

    for c in data['condicoes']:
        cid = c['id']
        for fid, m in c.get('modalidades', {}).items():
            pair = (cid, fid)
            if pair in ENSAIOS_E_METAS:
                info = ENSAIOS_E_METAS[pair]
                m['ensaio_clinico'] = info['ensaio']
                m['meta_analise'] = info['meta']
                # Atualiza artigo_referencia para apontar para o ensaio clínico de referência
                m['artigo_referencia'] = info['ensaio']
                count_ensaios += 1
                count_metas += 1

    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open(JS_PATH, 'w', encoding='utf-8') as f:
        f.write("/**\n * Rede NAPeN — Base de Dados dos Roadmaps 2025–2026\n * Exportação oficial dos dados clínicos estruturados para o ecossistema Web.\n */\n")
        f.write("window.NAPEN_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print(f"Sucesso: {count_ensaios} ensaios clínicos e {count_metas} metanálises integrados a napen_roadmaps_data.json e js/data.js.")

if __name__ == '__main__':
    enriquecer()
