---
title: S2 - Data storytelling per audience
type: sessione
status: completa
tags: [sessione]
session: S2
---

## [2026-06-18] S2 | TEAM A | ANGOLO: storytelling per CEO/CFO

**Messaggio principale trovato**
Il dato non cambia, ma la verità va ricostruita da zero per ogni interlocutore: per un CEO la slide giusta non è la più precisa, è quella che risponde alla sua unica domanda senza fargli leggere un grafico — e quasi tutto il lavoro è togliere ciò che è corretto ma a lui non serve.

**Prompt che hanno funzionato**
- "Costruisci [N] slide per [PERSONA: ruolo, cosa decide, quanta attenzione ha]. Vietato il gergo: niente [TERMINI TECNICI], traduci tutto in [unità che capisce]. Una sola tesi, la più difendibile. Struttura: messaggio, 3 grafici con titoli conclusivi, raccomandazione." — ⭐5 — dichiarare destinatario e suoi limiti a monte cambia tutto l'output, più di qualsiasi correzione dopo
- "Il colore segue la DIREZIONE del dato, non il sentiment della metrica: peggioramento = rosso sempre, anche se la metrica suona 'buona' ([clienti che tornano che calano = rosso])." — ⭐5 — senza questa riga il modello colora per come "suona" il numero
- "Questi sono i commenti di chi ha visto la bozza: [TRASCRIZIONE VERBATIM]. Correggi di conseguenza." — ⭐5 — si auto-corregge molto meglio dalle reazioni reali del pubblico che da un "miglioralo"
- "Ogni grafico risponde a UNA domanda precisa di [persona]. Se non risponde a nessuna, taglialo, anche se è corretto." — ⭐5 — elimina grafici tecnicamente giusti ma inutili al destinatario
- "Genera [N] versioni della narrazione da angoli diversi ([A], [B], [C]). Giudicale contro [vincoli]. Sintetizza la migliore." — ⭐4 — utile quando il rischio è il framing, non il dato
- "Dopo ogni modifica apri nel browser, controlla overflow/colori/line-break, mostrami lo screenshot prima di dichiararlo fatto." — ⭐4 — intercetta rese che il codice da solo non rivela

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- "Fai una presentazione executive d'impatto, bella" → titoli enormi in grassetto, spezzati su più righe, non presentabili → corretto vincolando lo stile (calmo, editoriale, titoli misurati, molto spazio bianco)
- Grafico senza dichiarare la domanda del destinatario → ha tenuto il divario dichiarato/reale (1x→2,8x), corretto ma orfano di domanda (già bocciato dal docente) → legare ogni grafico a una domanda, tagliare gli orfani
- Ordine scelto dal modello → ha aperto col grafico spesa/efficienza, inquadrando di fatto il problema come "di budget", contro la tesi strutturale → grafico-risultato in fondo, aprire con la causa
- Colori scelti dal modello → crollo dei clienti di ritorno colorato in verde → regole colore esplicite
- Feedback ambiguo sul tipo di grafico ("resa per euro" vs "spesa vs vendite") → avanti-e-indietro seguendo letteralmente ogni messaggio → decidere noi il grafico prima, istruzioni univoche

**Best practice scoperte**
- Definisci la persona e cosa NON può sentire prima di chiedere le slide — vale più di ogni correzione dopo
- Regole colore per direzione, non per sentiment: mai verde su una perdita
- Lega ogni grafico a una domanda del destinatario e taglia gli orfani, anche se corretti
- Passa le reazioni verbatim di chi guarda, non un "miglioralo"
- Verifica sempre nel browser, a dimensione di proiezione (overflow, line-break, colori)

**Metodi di analisi applicati**
- Struttura a 5 slide: messaggio (tesi) → 3 grafici (sintomo / falla / causa) → raccomandazione — forza la sottrazione
- Before/after a piccoli multipli (4 pannelli): consegne, resi, soddisfazione, riacquisto prima/dopo l'evento
- Resa per euro con linea di pareggio: ROAS blended tradotto in "per ogni euro speso quanto torna" (3,20€→1,60€), riferimento al pareggio a 1€ — rende leggibile un concetto tecnico senza nominarlo
- Scomposizione ricavi nuovi vs ritorno: due serie sullo stesso grafico, il calo viene dal cliente che non torna
- Spesa vs vendite reali, colore per direzione: "direzioni opposte" a colpo d'occhio
- Mapping causale su timeline ancorato a un evento datato (cambio corriere), tenendo l'onestà che il declino precedeva

**Cosa il modello ha sbagliato o inventato**
- Default estetico "bold da poster" con titoli spezzati, inadatto a una presentazione
- Colore per sentiment: perdita di clienti colorata in verde
- Framing che tradiva la tesi: aprendo con la spesa rischiava di far concludere "è un problema di budget", l'opposto della tesi strutturale
- Ha tenuto un grafico già scartato (il divario 1x→2,8x) ricomparso in una versione
- Compiacenza sul feedback: esegue alla lettera l'ultimo messaggio anche quando contraddice il precedente
- Stime presentate come fatti (eredità S1): estrapolazioni date come numeri certi, da marcare come ipotesi

**L'insight più importante della sessione**
Per un CEO la slide giusta non è la più precisa ma quella che risponde alla sua unica domanda, e quasi tutto il lavoro è togliere ciò che è corretto ma non serve a lui.

---

## [2026-06-18] S2 | TEAM B | ANGOLO: storytelling per Head of Marketing

**Messaggio principale trovato**
La stessa diagnosi cambia completamente di struttura a seconda di chi la presenta e a chi — e il modello non lo sa finché non glielo dici, perché assume di ESSERE il destinatario invece di parlarGLI.

**Prompt che hanno funzionato**
- "Non generare ancora [OUTPUT]. Prima spiegami il ragionamento per costruire [OBIETTIVO], sapendo che il destinatario è [RUOLO] e il contesto è [SITUAZIONE]." — ⭐5 — valida la struttura argomentativa prima di qualsiasi artefatto, gli output successivi richiedono meno iterazioni
- "Attenzione: noi non siamo [RUOLO], dobbiamo presentare i risultati a [RUOLO]. Questo cambia [tono, visibilità del metodo, action point come indicazioni non ordini]." — ⭐5 — riformulare chi parla e chi ascolta produce un cambio strutturale, non solo di tono
- "FORMATO (vincolante): [lista di cose VIETATE]. Poi il contenuto slide per slide con schema identico per tutte." — ⭐4 — i tool tipo NotebookLM riempiono; bloccare l'aggiunta funziona meglio del descrivere cosa mettere
- "Per ogni slide: cosa dico per primo / il filo logico / la domanda difficile con risposta già pronta." — ⭐5 — la struttura a tre livelli è usabile in sala senza rielaborazione; chiedere "la domanda difficile" fa emergere le obiezioni pericolose, non le ovvie
- "[CITA LA FRASE ESATTA]. Spiegami questa frase." poi "In breve." — ⭐5 — isolare una frase produce il meccanismo causale (saldo retention vs risparmio corriere) meglio dei talking points generali; il follow-up "in breve" dà la versione usabile in sala

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- Presentazione senza dichiarare il punto di vista del presentatore → slide come se l'Head of Marketing fosse il presentatore (titoli assertivi, action point come ordini, nessun metodo o fonte) → correzione esplicita del frame con le tre implicazioni pratiche
- Prima versione del prompt NotebookLM troppo lunga → slide 5 non generata (il tool legge le istruzioni finali come fine del contenuto) → tolto il meta-testo, regole di formato in cima vincolanti e negative, schema identico per tutte
- Slide 5 con domande aperte → coerenti con la logica analitica ma deboli come chiusura, lasciano la sala senza passo successivo → sostituite con tre action point su orizzonti distinti (Subito / Entro 60gg / Strutturale)

**Best practice scoperte**
- Prima di generare qualsiasi artefatto, far esplicitare e validare il ragionamento — gli output costruiti su un ragionamento approvato richiedono meno iterazioni
- Quando il destinatario cambia, dire esplicitamente cosa cambia in formato e tono: il modello tiene il frame precedente finché non lo contraddici
- Per tool esterni, schema identico per ogni sezione — se la slide 5 ha schema diverso, il tool può non processarla
- Istruzioni di formato in negativo ("zero bullet point") più efficaci di quelle in positivo ("layout pulito"): non lasciano spazio di interpretazione
- Chiedere le obiezioni più pericolose per la diagnosi, non le più probabili ("potrebbe essere stagionale?" è più pericolosa di "il CAC è alto?")

**Metodi di analisi applicati**
- Struttura argomentativa a 5 livelli: affermazione falsificabile → prova principale → prova di rinforzo indipendente → confutazione anticipata dell'alternativa → conseguenza pratica
- Segmentazione del destinatario per posizione, non per ruolo: chi presenta vs chi riceve cambia titoli, tono, visibilità del metodo, formulazione degli action point
- Test della domanda difficile: per ogni slide, l'obiezione che mina la diagnosi se non hai la risposta pronta — preparata prima, sistematicamente
- Saldo economico impostato ma non chiuso: quantificata la propria metà del conto (perdita retention 15.300€/mese) e indicato dove sta l'altra metà (risparmio corriere, in Operations), senza inventare il numero mancante
- Semplificazione iterativa del prompt per tool esterni: quattro versioni in sessione (v2→v5)

**Cosa il modello ha sbagliato o inventato**
- Frame del destinatario mantenuto: con "presenta all'Head of Marketing" ha assunto che il team FOSSE l'HOM — errore nella struttura della comunicazione, non nei numeri; emerso solo quando il team ha esplicitato la distinzione
- Slide 5 con domande invece di azioni: ha applicato la logica dell'analisi dove serviva la logica della comunicazione
- Prompt NotebookLM sovradimensionato: non distingue da solo "informazioni per me" da "istruzioni per il tool", e il tool ha messo il meta-testo dentro le slide

**L'insight più importante della sessione**
Il modello non inferisce il punto di vista del presentatore dal brief — va dichiarato esplicitamente chi parla e chi ascolta, altrimenti eredita il frame sbagliato e produce slide assertive al posto di documentate.

---

## [2026-06-18] S2 | TEAM C | ANGOLO: storytelling per Adv/Performance Specialist

**Messaggio principale trovato**
Un Performance Specialist non ha bisogno della diagnosi completa: ha bisogno della traduzione del dato in priorità di budget, cap e test — con una metrica che spieghi perché ogni leva viene toccata.

**Prompt che hanno funzionato**
- "Presentazione per [DESTINATARIO OPERATIVO]. La domanda che si fa: '[DOMANDA PRATICA]'. Cosa deve decidere: [DECISIONI ATTESE]. Cosa NON è nella sua leva: [FUORI SCOPE]. Struttura: [SLIDE]. Prima di procedere chiedimi cosa ti serve." — ⭐5 — filtra l'analisi sulla leva reale dell'interlocutore (budget/canali/creative/cap/test), esclude logistica/prodotto/CX
- "Perché consigli questi grafici? Ce ne sono di più adatti a [destinatario]?" — ⭐5 — sposta il modello da proposta descrittiva a decisionale ("cosa tagliare / spostare / testare")
- "Ipotizziamo lo stesso budget e riallocalo. Procedi con le slide." — ⭐4 — trasforma l'analisi in simulazione operativa; il vincolo impedisce il rifugio "aumentare il budget sui canali migliori"
- "Spiegami il grafico di pagina [N]." — ⭐5 — fa emergere ambiguità non visibili nella prima versione: etichette da correggere, messaggi impliciti, differenza tra metrica apparente e decisione
- "Sulla base di queste spiegazioni, rigenera la presentazione più esplicita, che non generi ambiguità." — ⭐4 — usa le spiegazioni come materiale di revisione, non come commento separato: la chiave di lettura entra dentro le slide

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- Richiesta iniziale sui grafici → corretti sul piano diagnostico ma non orientati all'azione ("budget vs ricavi harvest" spiega il problema ma non dice quanto spostare e da dove) → riformulati in grafici operativi (riallocazione attuale vs consigliata, matrice [[CPM e CTR bassi non bastano|CTR]]/CVR, quota budget vs quota ricavi)
- Prima versione della presentazione → usabile ma richiedeva spiegazione orale (perché una metrica alta non implica più budget) → spiegazioni puntuali pag. 2/3/4, poi rigenerata
- Grafico harvest → etichette arrotondate illeggibili invece di percentuali → chiarito che il punto non è "harvest non funziona" ma "harvest sotto cap perché intercetta domanda già esistente"
- Raccomandazione TikTok → rischio di lettura troppo netta (spegnere) → formulata come "ridurre a test cap", non spegnere: tiene il canale aperto a nuovi test ma ne impedisce lo scaling su vanity metric

**Best practice scoperte**
- Per un destinatario operativo, definire subito le leve toccabili (budget/canali/creative/cap/test) ed escludere il fuori-scope (logistica, prodotto, CX)
- Chiedere quali grafici servono e perché prima di generarli: il primo set è descrittivo, il secondo (dopo challenge) decisionale
- Separare sempre metrica di attrazione e metrica di acquisto: CTR e CVR insieme, mai CTR da solo
- Quando un canale ha ROAS alto, chiedere se crea domanda o cattura domanda già esistente (Brand, Retargeting, [[PMax è una black box|PMax]] gonfiano la lettura)
- Far spiegare la slide come se parlasse al destinatario finale: fa emergere ambiguità grafiche e narrative prima della consegna

**Metodi di analisi applicati**
- Riallocazione a budget invariato: budget mensile costante e ridistribuito — raccomandazione attuabile senza chiedere nuovo investimento
- Cap operativo su harvest: [[Brand search ad alto ROAS|Brand Search]] e Retargeting non eliminati ma messi sotto cap, per preservare la funzione di chiusura senza assorbire budget su ROAS apparente
- Matrice CTR/CVR per creatività: distinguere asset che generano attenzione da asset che generano traffico acquistabile
- Quota budget vs quota ricavi attribuiti per harvest (12% budget / 36% ricavi): mostra la sproporzione tra spesa e merito apparente
- Classificazione domanda creata (prospecting) vs catturata (brand/retargeting/harvest)

**Cosa il modello ha sbagliato o inventato**
- Grafici buoni per spiegare la diagnosi ma non abbastanza per guidare una decisione operativa immediata
- Ha rischiato di sovrainterpretare il ROAS come scalabilità, mentre era contaminato da sovra-attribuzione, domanda già esistente e [[La budget simulation di Google come black box|black box]] PMax
- Ha trattato CR-003 (PMax) e CR-009 (DPA retargeting) ad alta CVR come scalabili senza verifica
- Etichette del grafico harvest arrotondate in modo fuorviante (concetto corretto, forma ambigua)
- Formulazione troppo netta su TikTok (riduzione dello scaling ≠ spegnimento del canale)
- Spiegazioni lasciate fuori dalle slide invece che dentro: la prima versione richiedeva troppa interpretazione orale

**L'insight più importante della sessione**
A chi mette le mani sulle campagne non serve sapere che il ROAS inganna: serve sapere cosa spostare, cosa cappare e cosa testare da lunedì — la diagnosi è un mezzo, la leva è il deliverable.

---

## [2026-06-18] S2 | SINTESI DOCENTE | connessioni tra i team

> Nota: a differenza di S1, in questa sessione la cross-examination si è svolta dal vivo. Riccardo ha interpretato i tre destinatari (CEO/CFO, Head of Marketing, Adv Specialist) e ha attaccato le slide di ciascun team. Questa sintesi non è ricostruita a freddo — riporta cosa è successo in aula quando un lettore ostile ha letto le slide.

**La connessione più importante: tutti e tre i team scoprono indipendentemente lo stesso errore, ma spostato dai dati al framing.**

In S1 il pattern "[[First-instinct-is-wrong]]" era sui dati: la prima sintesi del modello era sempre più netta di quanto i numeri reggessero. In S2 si ripete identico ma un livello sopra, sul destinatario: la prima risposta del modello assume il frame sbagliato (presentatore = destinatario), il primo grafico risponde alla domanda di nessuno, il primo colore segue il sentiment della metrica e non la direzione del dato. Stesso fallimento — un output plausibile e troppo sicuro — finché non si dichiara esplicitamente il vincolo. In S1 il vincolo era analitico, in S2 è comunicativo.

**La cross-examination dal vivo ha confermato l'errore di framing, team per team — e quasi sempre l'ha trovato il destinatario, non il team.**

- **Team A (CEO/CFO):** la slide che introduceva la spesa pubblicitaria ha "rotto" la tesi della retention in diretta. Da CEO: *"da questa chart capisco che ho speso male i soldi, ma prima mi stavi raccontando che è un problema di retention."* Piermatteo ha ammesso live: *"fa figurare come se le campagne non funzionassero invece che il cliente a non tornare."* È esattamente l'errore "framing che tradisce la tesi" che il team aveva documentato — ma a farlo emergere è stato il lettore, non l'autore. Stesso esito sulla didascalia "clienti persi = 70% del calo": il destinatario non l'ha capita ("è misleading"), e la conclusione è stata che il grafico spiega meglio della frase sotto — o lo spieghi davvero, o lo togli.

- **Team B (Head of Marketing):** il saldo economico impostato-ma-non-chiuso (15.300€/mese di retention vs risparmio corriere) ha retto al live, e anzi è stato stress-testato: 15.300 × 12 ≈ 180k/anno, un corriere non può plausibilmente costare 250k da una parte e 70k dall'altra, quindi il saldo pende verso il "tenere". Il punto debole è emerso su TikTok: il team lo metteva sullo stesso piano di Google sulla stessa metrica, senza pesare che TikTok costa ~5× e fa probabilmente awareness. La domanda giusta, emersa in aula (Piermatteo): *"quanto scende Google se togli TikTok?"*. La disciplina anti-overclaim di S1 ("aggrava, non causa") qui ritorna in forma comunicativa: "ridurre non spegnere" era la conclusione giusta, ma la *ragione* era ancora incompleta finché la cross-examination non l'ha aperta.

- **Team C (Adv Specialist):** il destinatario operativo ha rifiutato i grafici diagnostici in diretta. Sul grafico harvest 36%/12%: *"il ragionamento mi è chiaro, ma il grafico non mi sta dicendo questa cosa"* + *"perché dici a chi mette le mani sulle campagne di non guardare il ROAS? Digli cosa fare."* Dei tre grafici è sopravvissuta solo la riallocazione del budget (*"so cosa fare da domani veramente"*); harvest e matrice creative, giudicati misleading, sarebbero stati tagliati. La matrice CTR/CVR è cascata su un dettaglio che il team non poteva vedere da solo: era divisa per tipo di creatività ma la performance di una creatività dipende dal tipo di campagna in cui gira (una creatività retargeting può essere editoriale) — quindi posizionarla senza il canale "non funziona".

**Il lavoro che il modello non può fare da solo: un lettore ostile.**

Due grafici "corretti nel deck" sono caduti appena letti a freddo — la slide spesa di A, il grafico harvest di C. Entrambi tecnicamente giusti, entrambi rotti in sala. I due prompt che ci si avvicinano — "verifica nel browser" (A) e "spiega la slide al destinatario" (C) — sono buoni surrogati, ma il test vero è un lettore ostile, ed è la cross-examination. Il modello, lasciato solo, conferma; il destinatario, no.

**Quello che nessun team ha potuto vedere da solo:** la stessa diagnosi è diventata tre oggetti irriconoscibili per tre destinatari — prova che il framing è un secondo lavoro analitico, non packaging. E la cucitura dove il frame perde (la slide spesa, il grafico harvest, l'equivalenza TikTok/Google) la trova il destinatario, non chi ha costruito la slide. Per questo la slide va sempre testata contro chi la riceverà, non contro chi l'ha fatta.

---
