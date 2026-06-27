---
title: HITL - [[HITL (human-in-the-loop)|human-in-the-loop]]
type: fonte
status: ingerita
tags: [fonte, agenti]
source: https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo
---

**Cos'è.** Un pattern di progettazione che inserisce il giudizio umano in punti critici di un flusso altrimenti automatico — vedi la nota-concetto [[HITL (human-in-the-loop)]].

**I tre pattern di approvazione.**
- *Pre-azione* — per azioni irreversibili: l'agente si ferma e aspetta l'ok prima di agire.
- *Post-azione* — per azioni reversibili ad alto volume: si agisce, l'umano rivede dopo.
- *Confidence-based* — si coinvolge l'umano solo quando la confidenza scende sotto una soglia.

**Il principio.** L'obiettivo non è la massima automazione né la massima sorveglianza, ma l'**automazione calibrata**: le azioni giuste procedono da sole, quelle giuste ricevono il giudizio umano. Un handoff tempestivo è segno di un sistema robusto, non di un fallimento — e ogni decisione del revisore diventa dato per ricalibrare. Implementato in framework come LangGraph, OpenAI Agents SDK, Microsoft Agent Framework, Mastra.

**Perché è qui.** È il backing di [[HITL (human-in-the-loop)]], [[Guardrail]] ed [[Errore silenzioso]] di S4.
