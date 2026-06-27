---
title: Le tre fonti
type: concetto
status: stabile
tags: [concetto, attribuzione]
aliases: ["tre fonti"]
---

| Fonte | Cosa misura | Bias principale |
|---|---|---|
| **Piattaforma** (Google Ads, Meta, TikTok…) | Conversioni attribuite dalla piattaforma stessa | Sovrastima: ogni piattaforma conta le sue |
| **Analytics** ([[GA4 è un campione, non la verità|GA4]], ecc.) | Sessioni, eventi e conversioni tracciati sul sito | Sottostima: cookie, ITP, adblocker, bug di tracking |
| **Backend / CRM** | Ordini reali dal gestionale | La verità sulle vendite, ma non sa quale canale le ha generate |

**Come riconciliarle:**
- Non cercare un numero "giusto" unico: non esiste.
- Usa il backend come ancora (gli ordini ci sono o non ci sono).
- Il gap piattaforma/analytics segnala problemi di attribuzione o tracking.
- Il gap analytics/backend segnala problemi tecnici specifici (cookie, device, browser).
- Dichiara sempre da quale fonte viene ogni numero in un report.
