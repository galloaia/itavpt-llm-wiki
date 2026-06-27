---
title: Come usare l'LLM per costruire il simulatore
type: concetto
status: stabile
tags: [concetto, budget, llm]
---

**Inferire le curve dai dati:**
```
Ho questi punti spesa→conversioni per canale [incolla dati di test].
Per ogni canale, stima una curva di saturazione del tipo conv = Vmax·spesa/(spesa+K).
Dammi Vmax e K stimati, e dimmi quanto è affidabile il fit (quanti punti, quanta dispersione).
Segnala i canali dove i dati non bastano a stimare la curva con sicurezza.
```

**Costruire l'ottimizzatore:**
```
Date queste curve [Vmax, K per canale] e un budget totale di [X],
costruisci un modello che alloca il budget massimizzando le conversioni totali,
spostando budget finché il ritorno marginale dei canali si pareggia.
Aggiungi vincoli: min [X] e max [Y] per canale.
Mostra l'allocazione risultante, le conversioni stimate, e il confronto con l'allocazione attuale.
```

**Stress test delle assunzioni:**
```
Questo è il mio simulatore di allocazione [descrivi].
Fai l'avvocato del diavolo: quali assunzioni sono più fragili?
Cosa succede al risultato se la curva del canale [X] è sbagliata del 20%?
Quali vincoli del mondo reale non sto considerando?
```

**Errori da documentare nel diario:**
- L'allocazione ottima dice "tutto su un canale"? → manca [[La saturazione]] nel modello
- Stai trattando un ROAS alto come sempre buono? → controlla l'[[Efficienza vs incrementalità|incrementalità]]
- Il modello raccomanda l'ineseguibile (azzera un canale overnight)? → aggiungi vincoli
- Hai presentato il numero senza le assunzioni? → è una [[La budget simulation di Google come black box|black box]], esattamente ciò che volevi evitare


---
