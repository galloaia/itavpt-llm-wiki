---
title: Code interpreter - quando e come
type: concetto
status: stabile
tags: [concetto, llm]
aliases: ["code interpreter"]
---

**Usalo per:** calcoli aggregati (somme, medie, ROAS, CAC), grafici, pivot, join tra tabelle, anomaly detection, curve di tendenza.

**Come attivarlo in modo efficace:**
- Carica i CSV separatamente, non in un unico paste di testo.
- Dopo il caricamento, chiedi prima una preview (`head()` + `describe()`) per verificare che i dati siano stati letti bene.
- Se il modello fa un calcolo senza mostrare il codice, chiedilo: "mostrami il codice che hai usato per questo numero".

---
