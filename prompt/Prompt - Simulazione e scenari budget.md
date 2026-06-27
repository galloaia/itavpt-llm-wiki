---
title: Prompt - Simulazione e scenari budget
type: prompt
status: stabile
tags: [prompt, budget]
---

Prompt generalizzati emersi in Sessione 3 (allocazione budget, analisi prescrittiva). Sostituire i [PLACEHOLDER] con il caso reale.

**Marginale, non medio (la regola-cardine)** ⭐ *(sblocca la verità che un canale può avere ottimo ritorno medio e pessimo ritorno marginale)*
> Per ogni canale dimmi se l'euro che sto per spendere rende ancora come i primi, o già meno. Voglio il ritorno sul PROSSIMO euro, non il ROAS medio.

**Numero in codice, poi LLM come interprete** ⭐ *(l'LLM da solo confonde [[La saturazione|saturazione]] e ROAS medio; ancoralo al calcolo)*
> Calcola in codice il rendimento marginale per [CANALE/SEGMENTO] (Δoutput ÷ Δinput) usando SOLO questi numeri verificati. Non stimare a memoria.

**Definizione del problema decisionale come scenario, non ottimizzazione** ⭐ *(trasforma il task da "allocazione perfetta" a "decisione argomentata sotto vincoli")*
> [STAKEHOLDER] ha stanziato [BUDGET] in [ORIZZONTE TEMPORALE]. Vaglia [IPOTESI 1], [IPOTESI 2], [IPOTESI 3], [IPOTESI 4]. L'obiettivo non è un'allocazione perfetta, ma uno scenario difendibile: ecco cosa prevediamo succeda, ecco perché abbiamo scartato l'altra, ecco dove la previsione diventa ipotesi.

**Stakeholder come red team** ⭐ *(il piano che sopravvive a tutti i decisori in conflitto è quello da portare in plenaria)*
> Sei [STAKEHOLDER]. Prova a demolire questo piano con le tue domande dure ([PREOCCUPAZIONE 1] / [PREOCCUPAZIONE 2]). Per ogni obiezione dai la risposta difendibile.

**N scenari paralleli ancorati ai dati, poi giudice** *(esplora lo spazio invece di affezionarsi al primo split — solo se ogni scenario è ancorato a numeri reali)*
> Simula [N] split diversi di [RISORSA] (es. retention-heavy, acquisizione-heavy, mix...), ognuno proiettato su [ORIZZONTE] coi numeri veri e scorato. Poi rankali e scegli il bilanciamento migliore.

**Risultati prima della narrativa** ⭐ *(separa analisi e storytelling, riduce il rischio di output convincente ma non difendibile)*
> Prima fornisci i risultati dell'analisi. Solo dopo costruiamo la presentazione per [DESTINATARIO].

**Editing chirurgico su artefatto già prodotto** ⭐ *(più efficace di un generico "rendila migliore")*
> Rifai [ARTEFATTO] con questa struttura: [sequenza esatta, cosa tenere invariato, cosa sintetizzare, cosa aggiungere].

**Passaggio di comprensione finale** *(la prima stesura del modello è quasi sempre gergale)*
> Questa frase non si capisce: [INCOLLA]. Riscrivila per chi non è del mestiere, senza gergo.
