---
title: Meridian - [[Non è un MMM|MMM]] open source di Google
type: fonte
status: ingerita
tags: [fonte, budget, mmm]
source: https://github.com/google/meridian
---

**Cos'è.** Il Marketing Mix Model open source di Google, scritto in Python, basato su inferenza causale bayesiana. Annunciato a marzo 2024 e reso disponibile a tutti tra gennaio e febbraio 2025; sostituisce il vecchio LightweightMMM.

**Cosa fa.** Stima l'impatto incrementale dei canali (online e offline) modellando adstock e rendimenti decrescenti — cioè le curve di [[La saturazione|saturazione]]. Si calibra con i risultati di esperimenti di [[Efficienza vs incrementalità|incrementalità]] usati come *prior*, e può usare il volume di query Google come variabile di controllo. Produce ottimizzazione del budget e scenario planning. Da febbraio 2026 ha uno *Scenario Planner* no-code che non richiede Python.

**Limiti.** Lavora a livello di canale, non di campagna; richiede un data scientist, una GPU e 2-3 anni di dati puliti. Trasparente ma non plug-and-play.

**Perché è qui.** È il riferimento serio per [[Non è un MMM]] e per [[La saturazione]]: il modello statistico che fa davvero quello che in aula approssimiamo a parole.
