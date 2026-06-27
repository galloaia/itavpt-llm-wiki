---
title: Prompt - Diagnosi e analisi performance
type: prompt
status: stabile
tags: [prompt, diagnosi]
---

*(Sessione 1 — performance/attribuzione, economics, creative)*

**Pulizia con resa esplicita delle anomalie**
```
Pulisci [DATASET]. Prima di analizzare, elenca OGNI anomalia: outlier numerici,
valori mancanti, duplicati, nomenclatura incoerente, formati data non standard.
Per ognuna scrivi come l'hai corretta. Non imputare nulla senza segnalarlo.
```
Perché funziona: forza il modello a far emergere i problemi invece di analizzarci sopra in silenzio. Senza questo, anomalie come valori negativi o duplicati passano inosservate nei totali aggregati.

**Ground truth in codice, poi LLM come interprete**
```
Questi sono i numeri verificati calcolati in codice: [TABELLA].
Leggi [FILE] per il dettaglio ma NON ricalcolare a memoria.
Usa solo questi valori come ancore e interpretali.
```
Perché funziona: separa il calcolo (deterministico, va fatto in codice) dall'interpretazione (compito dell'LLM). Elimina le metriche allucinate o stimate "a occhio" leggendo il file.

**Red team avversariale su ogni claim forte**
```
Sei un red team ostile esperto di analytics. Prova a DEMOLIRE questo claim:
[CLAIM] con evidenza [NUMERI]. Cerca: correlazione spacciata per causalità,
numeri imprecisi, variabili confondenti (stagionalità, mix, eventi esogeni),
over-claim quantitativi. Se regge dillo. Se no, dammi la riformulazione
che resta vera ma non è attaccabile.
```
Perché funziona: trasforma affermazioni sexy ma fragili in affermazioni difendibili. Funziona anche solo cambiando ruolo nella stessa chat, senza bisogno di un secondo strumento.

**Classificazione per funzione, non per canale/etichetta superficiale**
```
Non classificare [GLI ELEMENTI] per [CATEGORIA OVVIA, es. canale/piattaforma].
Classificali per FUNZIONE: [FUNZIONE A, es. crea domanda nuova] vs
[FUNZIONE B, es. cattura domanda esistente]. Poi calcola quota di
[RISORSA, es. budget] vs quota di [RISULTATO, es. ricavi] per ciascun gruppo.
```
Perché funziona: la categoria "ovvia" (canale, nome, tipo) spesso nasconde il vero driver. Riclassificare per funzione rende visibili gli squilibri (es. una piccola quota di risorsa che si prende una quota sproporzionata di risultato).

**Analisi multi-lente con output strutturato**
```
Analizza [DATI] da [N] angoli indipendenti in parallelo. Ogni lente restituisce:
titolo, evidenza numerica, interpretazione, forza, attaccabilità.
Schema: [SCHEMA JSON].
```
Perché funziona: forzare uno schema — incluso un campo esplicito di "attaccabilità" — alza la qualità delle interpretazioni e riduce la retorica non supportata dai dati.

**Domanda guida aperta invece di una lista di metriche**
```
[CONTESTO]. Come [RUOLO/TEAM] ci occupiamo di [AREA].
Domanda guida: [DOMANDA APERTA, non una metrica da calcolare].
[Una frase su perché la domanda conta e qual è il sospetto da verificare].
```
Perché funziona: una domanda aperta lascia al modello la libertà di scegliere la fonte di verità tra dati sovrapposti e di proporre segmentazioni non richieste esplicitamente. Una richiesta rigida ("calcola la metrica X") spesso non fa emergere la scoperta più interessante.

**Spiegazione del processo richiesta post-hoc**
```
Spiegaci come hai svolto i passaggi. Quali domande ti sei posto?
Quali metriche hai estratto? Come hai pulito e segmentato il dato?
Procedi step by step.
```
Perché funziona: chiesto DOPO aver visto il risultato, con domande puntuali (non "spiegami tutto"), forza risposte verificabili con codice ri-eseguito — non un riassunto a memoria che potrebbe non corrispondere a quanto effettivamente calcolato.

**Sintesi finale ancorata alla domanda originale**
```
Indicaci in maniera sintetica la risposta alla domanda guida ([RIPETI LA DOMANDA]).
```
Perché funziona: ripetere la domanda guida originale nel prompt di chiusura ancora la sintesi a ciò che serve davvero al destinatario, evitando che derivi verso dettagli tecnici intermedi. Attenzione però: può anche spingere verso una sintesi troppo netta — vedi nota su quantificazione delle cause più sotto.

**Prompt intermedio per un secondo tool, con struttura esplicita**
```
Creaci un prompt per [TOOL]. Struttura richiesta: [N] slide/sezioni,
contenuto di ciascuna, tono, istruzioni su [DETTAGLI ES. grafici], formato output.
```
Perché funziona: specificare la struttura desiderata, invece di chiedere genericamente "fai un prompt per X", produce un artefatto effettivamente riutilizzabile — e permette di rivedere le istruzioni prima che vengano eseguite da un sistema meno controllabile.

**Analisi integrata di più materiali (dati + contesto + asset visivi)**
```
Sei un consulente di [DOMINIO]. Hai a disposizione: [DATASET con metriche],
[DOCUMENTO DI CONTESTO, es. brand/posizionamento], [ASSET, es. creative/immagini].
Obiettivo: [DOMANDA].
Analizza seguendo questi passaggi: 1) distingui [METRICA TIPO A] da [METRICA TIPO B];
2) classifica ogni elemento in una matrice [DIMENSIONE 1]/[DIMENSIONE 2];
3) leggi [ASPETTI QUALITATIVI];
4) identifica pattern ricorrenti;
5) valuta la coerenza con [CONTESTO/POSIZIONAMENTO];
6) restituisci tabella, insight e raccomandazioni.
```
Perché funziona: obbliga il modello a non fermarsi alle metriche e a collegare dato quantitativo, contesto qualitativo e asset visivi — l'errore più comune è trattare questi tre livelli separatamente.

**Framing esplicito del criterio interpretativo, prima dell'analisi**
```
[Spiega in una frase perché la metrica più ovvia non basta — es: "i numeri senza
le immagini sono incompleti, le immagini senza i numeri sono estetica"].
Il vostro lavoro è tenerli insieme.
```
Perché funziona: definire il criterio interpretativo prima di iniziare impedisce che una metrica facile da leggere (es. [[CPM e CTR bassi non bastano|CTR]], click) venga trattata come autosufficiente quando non lo è.

**Verifica puntuale sugli asset reali dopo la prima analisi**
```
Ecco gli asset reali utilizzati ([IMMAGINI/FILE]). Verifica che ciò che
hai scritto sopra sia corretto.
```
Perché funziona: introduce un controllo qualitativo sui materiali reali e corregge interpretazioni basate solo su nomi o metadati invece che sul contenuto effettivo. Più efficace di chiedere subito tutto insieme, perché isola dove il modello ha dedotto invece di osservare.

**Conversione in deliverable operativo per un terzo**
```
Rendi [OUTPUT] un [FORMATO, es. Excel/slide] che devo passare a [DESTINATARIO].
```
Perché funziona: trasforma l'analisi in un artefatto riutilizzabile con classificazione, soglie, sintesi e legenda — non solo una risposta in chat.

---
