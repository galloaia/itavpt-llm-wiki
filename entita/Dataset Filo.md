---
title: Dataset Filo
type: entita
status: stabile
tags: [entità, caso, dati]
aliases: ["dataset"]
---

> Rappresenta il funnel digitale DTC, non il fatturato totale.

**Due formati, stesso contenuto.** L’Excel raccoglie tutto in un unico file con 7 fogli (incluso un foglio Leggimi). I CSV sono gli stessi dati separati, più comodi da caricare direttamente nell’LLM.

| File | Cosa contiene | Da ricordare |
|---|---|---|
| `filo_ads_dataset.xlsx` | **Master file** — tutti i fogli in uno (Campagne, [[GA4 è un campione, non la verità|GA4]], Vendite, Ops, Creative, Daily Q4) | Inizia dal foglio Leggimi |
| `filo_ads_campagne_mensili.csv` | Performance per campagna, dichiarate dalle piattaforme | ⚠️ Contiene errori di data quality: va pulito prima di analizzare |
| `filo_ga4_canali_device_mensili.csv` | Sessioni e conversioni per canale × device | Attenzione al breakdown per device (gap Safari mobile) |
| `filo_vendite_backend_mensili.csv` | Ordini reali, nuovi vs ritorno, repeat rate | Fonte di verità |
| `filo_ops_esperienza_mensili.csv` | Consegna, resi, NPS, ticket | Il lato post-acquisto |
| `filo_creative_metadata.csv` | Metadata creative: hook, formato, [[CPM e CTR bassi non bastano|CTR]] iniziale/finale, CVR, file immagine | Confronta con le immagini nella cartella `creative/` |
| `filo_ads_giornaliero_q4_2025.csv` | Dettaglio giornaliero Q4 2025 | Per il drill-down ultimi 3 mesi |
| `filo_budget_test_settimanale_q1_2026.csv` | **(S3)** 13 settimane di test budget: spesa→conversioni a livelli diversi per canale | Da qui si inferiscono le curve di [[La saturazione|saturazione]] |
| `filo_budget_attuale_mensile.csv` | **(S3)** Allocazione budget di partenza (9.000 €/mese), sub-ottimale | È il punto da migliorare con il simulatore |

---
