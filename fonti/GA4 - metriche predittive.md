---
title: [[GA4 è un campione, non la verità|GA4]] - metriche predittive
type: fonte
status: ingerita
tags: [fonte, predittiva, ga4]
source: https://support.google.com/analytics/answer/9846734
---

**Cosa sono.** Tre metriche di machine learning calcolate da GA4 sui dati di prima parte, senza cookie di terza parte:
- **Purchase probability** — probabilità che un utente attivo acquisti nei prossimi 7 giorni.
- **Churn probability** — probabilità che un utente attivo non torni nei prossimi 7 giorni.
- **Predicted revenue** — ricavo atteso nei prossimi 28 giorni dagli utenti attivi.

**A cosa servono.** Alimentano le *predictive audience* (es. "probabili acquirenti a 7 giorni", "probabili top spender a 28 giorni"), esportabili verso Google Ads e DV360 per il retargeting.

**Prerequisiti (rigidi).** Evento purchase con value e currency; nelle ultime 4 settimane, su una finestra di 7 giorni, almeno 1.000 utenti di ritorno che hanno innescato la condizione e almeno 1.000 che non l'hanno fatta; qualità del modello sostenuta nel tempo. Sotto soglia, GA4 smette di aggiornarle.

**Perché è qui.** È l'entry-level dell'analisi predittiva citato in aula — vedi [[Le tre prediction da non confondere]] e [[pLTV in una formula]].
