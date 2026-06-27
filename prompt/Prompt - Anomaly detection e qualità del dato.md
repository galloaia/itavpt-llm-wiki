---
title: Prompt - Anomaly detection e qualità del dato
type: prompt
status: stabile
tags: [prompt, anomalie]
---

*(Sessione 1 — trasversale a tutti gli angoli)*

**Riconciliazione tra fonti indipendenti**
```
Confronta il totale di [METRICA] aggregato da [FONTE A] con il totale
riportato indipendentemente in [FONTE B], periodo per periodo.
Segnala ogni scostamento e proponi una spiegazione verificabile.
```
Perché funziona: gli scostamenti tra fonti indipendenti spesso puntano dritti a un errore specifico (es. un segno invertito, un doppio conteggio) che nei soli totali aggregati resterebbe invisibile.

**Normalizzazione testuale prima di aggregare**
```
Prima di qualsiasi aggregazione per [CATEGORIA, es. canale/cliente/prodotto],
controlla e correggi varianti di scrittura della stessa entità
(maiuscole/minuscole, spazi, abbreviazioni). Mostra le varianti trovate.
```
Perché funziona: senza questo step, la stessa entità scritta in modi diversi viene contata come entità separate, distorcendo ogni aggregazione successiva.

**Deduplicazione esplicita su colonne chiave**
```
Cerca righe duplicate o quasi-duplicate su [COLONNE CHIAVE].
Mostra le righe trovate prima di rimuoverle.
```
Perché funziona: un doppio conteggio involontario gonfia silenziosamente totali e medie; va reso visibile, non solo corretto in automatico.

---
