---
title: Karpathy - l'LLM come sistema operativo
type: fonte
status: ingerita
tags: [fonte, llm]
source: https://www.decodingai.com/p/context-engineering-2025s-1-skill
---

**L'idea.** Andrej Karpathy propone l'analogia: l'LLM è un nuovo tipo di **sistema operativo**. I pesi del modello sono la CPU; la finestra di contesto è la **RAM** (limitata, volatile, costosa); gli strumenti sono le periferiche; il retrieval e i file sono il disco; l'agente è l'[[Orchestratore]]. Programmare in linguaggio naturale è il "Software 3.0".

**La conseguenza pratica.** Il *context engineering* è la disciplina di decidere cosa entra nella RAM e quando. È esattamente la ragione d'essere di questa wiki: la sorgente atomica è il "disco", e il file compilato (`compile.py` → `FILO_WIKI_COMPILED.md`) è ciò che si carica nella RAM dell'LLM quando serve tutto il contesto in un colpo.

**Perché è qui.** È il fondamento concettuale del pattern wiki-single-file e del design vault → compilazione adottato qui.
