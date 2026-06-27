---
title: Prompt - Progettazione agente
type: prompt
status: stabile
tags: [prompt, agenti]
---

Prompt generalizzati emersi in Sessione 4 (progettazione di automazioni e agenti). Sostituire i [PLACEHOLDER] con il caso reale.

**Role-play + auto-audit del fallimento silenzioso** ⭐ *(il metodo-cardine: deriva [[HITL (human-in-the-loop)|HITL]] e [[Guardrail]] dal fallimento osservato, non a tavolino)*
> Recita l'aiutante [NOME/RUOLO] su un caso concreto di [CONTESTO]: produci l'output reale che genereresti, poi auto-criticati spietato. Dove sbagli IN SILENZIO per giorni senza che [UTENTE] se ne accorga? Da quel fallimento deriva dove deve decidere l'umano (HITL) e il limite che non superi mai (guardrail).

**Stakeholder avversario con paure nominate** ⭐ *(fa cadere i design fragili prima della plenaria; le paure specifiche trovano ciò che "critica genericamente" non trova)*
> Sei [UTENTE]: scettico, scottato. Attacca questo design con le TUE paure precise ([PAURA 1], [PAURA 2]). Di' se sopravvive così o cosa aggiungere perché tu ti fidi.

**"Giudizio o ricetta" come domanda di routing** ⭐ *(tiene l'AI all'ultimo miglio, impedisce di gonfiare tutto ad agente)*
> Per ogni pezzo del flusso: richiede giudizio o è una ricetta? Se è una ricetta, fanne un'automazione (più affidabile, più economica). L'agente solo dove serve capire e scegliere tra sfumature.

**Critico di conformità contro il brief** ⭐ *(trova campi mancanti, gergo non spiegato, soglie messe come numeri magici)*
> Confronta questo design contro [BRIEF] e [VINCOLI/NOTA UTENTE] ed elenca SOLO i gap: campi mancanti, gergo non spiegato, soglie arbitrarie non giustificate.

**Mostra, non dire (simula con artefatti reali)** ⭐ *(lo stop sul punto umano diventa la dimostrazione della tesi)*
> Non spiegare a parole cosa fa l'agente: simulalo passo per passo con gli artefatti veri (la card di notifica, la tabella, il report), e fermati esattamente dove decide l'umano.

**Output-centric: "cosa riceve l'utente, e dove?"** ⭐ *(sposta da "cosa fa l'aiutante" a flussi concreti e usabili)*
> Specificami quali sono gli output di ogni agente e automazione e in che modo arrivano a [UTENTE] (canale e formato: alert, foglio, documento, memo, digest).

**Scoperta del componente nascosto** ⭐ *(un output ricorrente che coordina più flussi è un componente da progettare, non un formato di consegna)*
> Questo [OUTPUT RICORRENTE] non è anche lui un agente o un'automazione da progettare? Se ha logiche, frequenza, priorità, guardrail e canale, trattalo come un aiutante.

**Blocco del livello: logiche, non implementazione** *(impedisce al modello di costruire workflow reali quando serve solo il disegno)*
> Progettate le logiche degli aiutanti: cosa serve, come dovrebbe funzionare, dove resta [UTENTE], qual è il guardrail. Non costruite niente di funzionante. Obiettivo finale: presentazione.

---
