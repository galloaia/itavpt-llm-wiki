---
title: Prompt - Data viz e storytelling
type: prompt
status: stabile
tags: [prompt, storytelling]
---

*(Sessione 2 — comunicare la stessa diagnosi a CEO/CFO, Head of Marketing, Adv Specialist)*

**Persona e vincoli del destinatario dichiarati a monte**
```
Costruisci [N] slide per [PERSONA: ruolo, cosa decide, quanta attenzione ha].
Vietato il gergo: niente [TERMINI TECNICI], traduci tutto in [unità che il
destinatario capisce, es. soldi e clienti]. Una sola tesi, la più difendibile.
Struttura: messaggio iniziale, [N] grafici con titoli già conclusivi, una raccomandazione.
```
Perché funziona: dichiarare destinatario e suoi limiti prima di chiedere le slide cambia l'output più di qualsiasi correzione successiva. Senza, il modello produce un'estetica generica e usa il gergo del mittente, non quello del lettore.

**Colore per direzione del dato, non per sentiment**
```
Il colore segue la DIREZIONE del dato, non il sentiment della metrica:
peggioramento = rosso sempre, anche se la metrica suona "positiva"
([es. clienti che tornano che calano = rosso, non verde]).
```
Perché funziona: lasciato libero, il modello colora per come "suona" la metrica (numero alto = verde) e finisce per dipingere di verde una perdita. La regola esplicita lega il colore alla direzione — l'unica cosa che il destinatario legge a colpo d'occhio.

**Un grafico = una domanda del destinatario**
```
Ogni grafico deve rispondere a UNA domanda precisa di [destinatario].
Se un grafico non risponde a nessuna sua domanda, taglialo — anche se è corretto.
```
Perché funziona: separa "vero" da "utile a lui". Elimina i grafici tecnicamente giusti ma orfani di domanda, che fanno solo perdere il lettore. (In aula il destinatario lo conferma a vista: un grafico solo rafforzativo, che non aggiunge una risposta, viene scartato.)

**Reazioni verbatim del pubblico invece di "miglioralo"**
```
Questi sono i commenti di chi ha visto la bozza: [TRASCRIZIONE VERBATIM].
Correggi di conseguenza.
```
Perché funziona: il modello si auto-corregge molto meglio dalle frasi reali del pubblico che da un generico "miglioralo" — le reazioni verbatim contengono il punto esatto in cui il messaggio non passa.

**Ragionamento prima dell'artefatto visivo**
```
Non generare ancora [OUTPUT]. Prima spiegami il ragionamento per costruire
[OBIETTIVO], sapendo che il destinatario è [RUOLO] e il contesto è [SITUAZIONE].
```
Perché funziona: validare la struttura argomentativa prima di costruire qualsiasi slide riduce le iterazioni — gli output successivi poggiano su un ragionamento già approvato invece di essere rifatti da capo.

**Correzione esplicita del frame presentatore / destinatario**
```
Attenzione: noi non siamo [RUOLO], dobbiamo PRESENTARE i risultati a [RUOLO].
Questo cambia: [tono, visibilità del metodo, action point come indicazioni non come ordini].
```
Perché funziona: il modello non inferisce il punto di vista del presentatore dal brief — se dici "presenta all'HOM" assume di ESSERE l'HOM. Dichiarare chi parla, chi ascolta e cosa cambia è l'unico modo per spostare il frame.

**Talking points a tre livelli, con l'obiezione pericolosa**
```
Per ogni slide dammi: cosa dico per primo / il filo logico /
la domanda difficile con la risposta già pronta.
Per la domanda difficile scegli l'obiezione più PERICOLOSA per la tesi, non la più probabile.
```
Perché funziona: la struttura a tre livelli è usabile in sala senza rielaborazione, e chiedere l'obiezione "più pericolosa" fa emergere quella che suona tecnica e ragionevole ([es. "potrebbe essere stagionale?"]) invece di quella ovvia.

**Regole di formato in negativo per tool esterni**
```
FORMATO (vincolante): [lista di cose VIETATE, es. zero bullet, max 1 riga per slide].
Poi il contenuto slide per slide, con schema IDENTICO per tutte le slide.
```
Perché funziona: i generatori esterni (tipo NotebookLM) tendono a riempire; un divieto esplicito blocca l'aggiunta meglio di una descrizione positiva. Lo schema identico per ogni slide evita che il tool salti l'ultima perché formattata diversamente.

**Filtro sulle leve del destinatario operativo**
```
Presentazione per [DESTINATARIO OPERATIVO]. La domanda che si fa: "[DOMANDA PRATICA]".
Cosa deve decidere: [DECISIONI ATTESE]. Cosa NON è nella sua leva: [FUORI SCOPE, es. logistica/prodotto/CX].
Prima di procedere, chiedimi cosa ti serve.
```
Perché funziona: obbliga il modello a filtrare l'analisi sulla leva reale dell'interlocutore (budget/canali/creative/cap/test) ed escludere ciò che non può toccare — trasforma una diagnosi in un set di decisioni.

**Sfida sui grafici prima di generarli**
```
Perché consigli questi grafici? Ce ne sono di più adatti a [destinatario]?
```
Perché funziona: sposta il modello da una proposta descrittiva ("ecco i grafici corretti") a una decisionale ("ecco cosa tagliare, spostare, testare"). Il primo set è quasi sempre diagnostico; il secondo, dopo challenge, diventa operativo.

**Spiegazione della slide come se parlasse al destinatario**
```
Spiegami il grafico di pagina [N] come se lo stessi spiegando a [destinatario finale].
```
Perché funziona: fa emergere ambiguità invisibili nella prima versione — etichette arrotondate, messaggi impliciti, la differenza tra metrica apparente e decisione operativa — prima che la slide arrivi davanti a chi decide.

**Panel di bozze di narrazione + sintesi**
```
Genera [N] versioni della narrazione da angoli diversi ([ANGOLO A], [ANGOLO B], [ANGOLO C]).
Giudicale contro [VINCOLI / tesi da difendere] e sintetizza la migliore.
```
Perché funziona: quando la parte rischiosa è il framing e non il dato, esplorare angoli alternativi in parallelo e poi sceglierne uno motivato blocca la narrazione su una tesi difendibile invece che sulla prima che esce.

**Verifica della resa nel browser a ogni iterazione**
```
Dopo ogni modifica apri la pagina nel browser, controlla overflow, altezze,
colori, line-break, e mostrami uno screenshot prima di dichiararla finita.
```
Perché funziona: il codice "corretto" può rendere male (slide in overflow, titoli spezzati, colori sbagliati) e te ne accorgi solo guardando l'output reale a dimensione di proiezione, non leggendo il codice.
