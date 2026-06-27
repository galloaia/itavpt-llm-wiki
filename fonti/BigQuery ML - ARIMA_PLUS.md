---
title: BigQuery ML - ARIMA_PLUS
type: fonte
status: ingerita
tags: [fonte, predittiva]
source: https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series
---

**Cos'è.** Un modello di forecasting di serie storiche dentro BigQuery, addestrabile in puro SQL (`CREATE MODEL ... OPTIONS(MODEL_TYPE='ARIMA_PLUS', HORIZON=90)`).

**Cosa fa.** Gestisce automaticamente trend, stagionalità, festività e anomalie, con selezione automatica del modello (auto.ARIMA). Le previsioni si leggono con `ML.FORECAST` (con orizzonte e intervallo di confidenza). È univariato; la variante `ARIMA_PLUS_XREG` aggiunge regressori esterni (multivariato). La più recente `AI.FORECAST` usa il modello fondazionale TimesFM senza addestrare nulla. Scala fino a milioni di serie.

**Perché è qui.** È il modo "in-warehouse" di fare le previsioni di ricavo/domanda che in [[Le tre prediction da non confondere|S3]] trattiamo concettualmente — niente Python, solo SQL sul dato già in BigQuery.
