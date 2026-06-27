# FILO STUDIO — WIKI (compilata dal vault)

> Generato da compile.py. Non modificare a mano: la sorgente sono le note del vault.



# Istruzioni e meta


## Istruzioni operative

> Questa sezione è rivolta all'LLM. Se stai leggendo questo come studente: non serve che la conosca a memoria — è il "manuale di comportamento" che il modello seguirà automaticamente.

### Durante una sessione di lavoro (USO)

Quando ricevi questa wiki come contesto, il tuo ruolo è quello di un **analista senior con memoria persistente**. Significa:

1. **Applica i framework di sezione 1-3 senza che ti vengano ri-spiegati.** Se l'utente ti dà un CSV di dati advertising, sai già che ci sono almeno tre fonti, che i ROAS di piattaforma sovrastimano, e che il primo passo è la data quality.
2. **Usa il caso Filo (sezione 4) come riferimento condiviso.** Se l'utente dice "come nel caso di Filo", sai di cosa parla.
3. **Proponi prompt dalla Prompt Library (sezione 5)** quando noti che l'utente sta cercando di fare qualcosa che quella library copre già.
4. **Non inventare numeri su Filo.** I dati del caso sono nei file CSV/Excel collegati — se non li hai in contesto, dillo.

### Alla fine di una sessione (CONTRIBUTO AL DIARIO)

Quando l'utente ti chiede di generare il contributo per la wiki, segui questo comportamento:

- **Scrivi nel formato del Diario (sezione 8)** — usa esattamente la struttura del template, con il prefisso greppabile `## [DATA] S[N] | [TEAM] |`.
- **Non modificare le sezioni 1-7.** Il contenuto metodologico lo aggiorna solo Riccardo Sozzi. Tu scrivi *solo* nella sezione 8.
- **Sii onesto su cosa non ha funzionato.** Il diario vale solo se include gli errori e i limiti, non solo i successi.
- **Mantieni le entry specifiche.** "L'LLM ha sbagliato la metrica" è inutile. "L'LLM ha calcolato il ROAS usando ricavi di piattaforma invece di GA4, gonfiando del 40%" è utile.

### Aggiornamento metodologico (solo Riccardo)

Se emerge in sessione qualcosa che cambia un principio delle sezioni 1-3 (es. una nuova euristica, un errore sistematico mai documentato), Riccardo lo integra direttamente. Non farlo in autonomia.


---


## Template diario

```
## [YYYY-MM-DD] S[N] | [TEAM A/B/C] | [ANGOLO: performance/economics/creative]

**Messaggio principale trovato**
[Una frase sola — la tesi che regge tutto]

**Prompt che hanno funzionato**
- [Struttura riutilizzabile con [PLACEHOLDER] al posto dei dettagli specifici] — ⭐[1-5] — perché ha funzionato
- ...

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- [Cosa hai chiesto] → [cosa ha risposto di sbagliato] → [come hai corretto]
- ...

**Best practice scoperte**
- [Concreta, non generica — es: "quando dai un CSV con valori mancanti, specifica nel prompt come vuoi che il modello li gestisca"]
- ...

**Metodi di analisi applicati**
- [Metodo]: [cosa hai calcolato, con quale logica, a cosa serviva]
- ...

**Cosa il modello ha sbagliato o inventato**
- [Errore specifico con esempio — es: "ha proposto causalità agenzia→calo Meta senza verificare il trend preesistente"]
- ...

**L'insight più importante della sessione**
[Una frase sola — non una cosa che ha detto il modello, una cosa che hai capito tu usando il modello]
```

---



# Concetti


## Automazione vs agente

Se puoi scriverlo come regole fisse (se X allora Y) è un'**automazione**; se serve interpretare e scegliere tra sfumature è un **agente**. Default anti-hype: a parità di risultato vince la cosa più semplice.


## Brand search ad alto ROAS

Un ottimo ROAS sulla brand search non è una campagna che funziona: **intercetta domanda già esistente** (harvest), non ne crea di nuova. ROAS alto, incrementalità quasi nulla.


## Budget allocation - le domande giuste

Prima di spostare un euro, rispondi a queste (nell'ordine):

1. *Su quale canale/campagna ho evidenza di incrementalità reale, anche approssimativa?*
2. *Dove il ROAS sta decadendo nel tempo? (saturazione, fatica creativa, targeting esaurito)*
3. *Quali campagne stanno crescendo solo perché "rubano" attribuzioni ad altri? (brand, PMax, retargeting)*
4. *Ho un problema di tracciamento che mi fa prendere decisioni su numeri bucati?*
5. *Qual è l'orizzonte temporale? (ottimizzare il ROAS mensile e ottimizzare il LTV del cliente sono cose diverse)*

**Cosa NON è un'allocazione di budget:**
- Spostare spesa sul canale col ROAS più alto senza verificare l'incrementalità.
- Tagliare un canale perché "non converte" senza controllare il suo ruolo nel funnel.
- Ottimizzare il CAC senza guardare il repeat rate / LTV.

---


## Budget senza test di incrementalità

Aumentare il budget su ciò che "funziona" senza un test di incrementalità ottimizza **l'attribuzione, non le vendite reali**. È il modo più comune di buttare soldi sentendosi data-driven. Vedi Efficienza vs incrementalità.


## CPM e CTR bassi non bastano

CPM e CTR bassi non fanno una buona campagna: traffico economico che **non converte costa, non fa risparmiare**. La metrica di vanità nasconde la mancanza di valore.


## Cinque regole operative dello storytelling

**1. La forma segue la domanda**
Non "quale grafico mi piace" ma "quale domanda voglio che il lettore si faccia".
- Trend nel tempo → linee
- Confronto categorie → barre (ordinate per valore, non alfabeticamente)
- Proporzione → barre se le fette sono più di tre
- Relazione tra variabili → scatter
- Se non sai quale: barre.

**2. Togli prima di aggiungere**
Ogni elemento che rimane deve guadagnarsi il posto.
Candidati alla rimozione: griglia (se le etichette bastano), bordo del grafico, legenda (se puoi etichettare direttamente), titolo dell'asse (se è ovvio), colori di sfondo.

**3. Il colore per significato, non per decorazione**
Una regola sola: usa il colore per attirare l'attenzione su *una cosa sola*. Tutto il resto: grigio.
Stesso colore = stessa categoria, sempre, in tutti i grafici della stessa presentazione.

**4. Il primo e l'ultimo si ricordano**
Il messaggio più importante va in apertura come *tesi* (non come anticipazione).
La raccomandazione va in chiusura.
Il mezzo è per le prove.

**5. Un messaggio per visual**
Un grafico che racconta tre cose non racconta nessuna. Se hai bisogno di tre messaggi: tre grafici.


## Code interpreter - quando e come

**Usalo per:** calcoli aggregati (somme, medie, ROAS, CAC), grafici, pivot, join tra tabelle, anomaly detection, curve di tendenza.

**Come attivarlo in modo efficace:**
- Carica i CSV separatamente, non in un unico paste di testo.
- Dopo il caricamento, chiedi prima una preview (`head()` + `describe()`) per verificare che i dati siano stati letti bene.
- Se il modello fa un calcolo senza mostrare il codice, chiedilo: "mostrami il codice che hai usato per questo numero".

---


## Come usare l'LLM per costruire il simulatore

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
- L'allocazione ottima dice "tutto su un canale"? → manca La saturazione nel modello
- Stai trattando un ROAS alto come sempre buono? → controlla l'incrementalità
- Il modello raccomanda l'ineseguibile (azzera un canale overnight)? → aggiungi vincoli
- Hai presentato il numero senza le assunzioni? → è una black box, esattamente ciò che volevi evitare


---


## Come usare l'LLM per il data storytelling

**Prompt per adattare per audience:**


**Prompt per trovare il confronto giusto:**


**Prompt per de-cluttering del grafico:**


**Errori da documentare nel diario:**
- Hai costruito i grafici prima di scrivere il messaggio? → riparti dalla frase
- Il titolo del grafico descrive i dati invece di concludere? → cambialo
- Hai usato più di due colori con significato distinto? → semplifica
- La raccomandazione inizia con "bisogna" o "occorre"? → rendila concreta e attribuita


---


## Cosa fa bene l'LLM sui dati

- Trovare pattern e anomalie in serie temporali lunghe
- Generare ipotesi su cause di un calo/crescita
- Scrivere la sintesi in linguaggio di business (per il CMO che non legge le tabelle)
- Costruire un simulatore "what-if" su ipotesi dichiarate
- Confrontare scenari alternativi di allocazione
- Identificare coerenze e incoerenze tra fonti
- Proporre visualizzazioni per un messaggio specifico


## Cosa sbaglia l'LLM

| Rischio | Sintomo | Rimedio |
|---|---|---|
| Errori aritmetici silenziosi | Ti dà un numero di ROAS o CAC con sicurezza assoluta | Sempre code interpreter per i calcoli |
| Inventare dati mancanti | Riempie i buchi con "stime ragionevoli" non dichiarate | Chiedi esplicitamente: "se il dato non c'è, dimmelo" |
| Conclusioni senza evidenza | "Il canale X non funziona" senza citare un numero | Chiedi sempre l'evidenza specifica prima della conclusione |
| Ottimismo non richiesto | Ti dice che "i risultati sono incoraggianti" anche quando non lo sono | Chiedi: "dimmi cosa c'è che non va, non solo cosa va bene" |
| Confondere correlazione e causalità | "Il ROAS cala quando la spesa sale → la spesa fa calare il ROAS" | Distingui esplicitamente: "questa è una correlazione, non una causa" |


## Efficienza vs incrementalità

È la distinzione più importante nell'advertising data — e la più ignorata.

**Efficienza** = quanto ROAS/CPA riporta la piattaforma. Facile da misurare, facile da ottimizzare, facile da gonfiare. Una campagna brand search ha ROAS 15x: stai misurando domanda che sarebbe arrivata comunque.

**Incrementalità** = quanto *in più* hai venduto *grazie a* quella campagna rispetto a non averla attivata. Difficile da misurare (richiede test), ma è l'unico numero che conta per le decisioni di budget.

**Segnali di bassa incrementalità nel dato storico (non definitivi, ma da alzare bandiera rossa):**
- ROAS altissimo e piatto indipendentemente dalla spesa → brand / retargeting
- ROAS che sale mentre tutto il resto cala → cannibalizzazione (es. PMax)
- Conversioni concentrate su utenti già in pipeline → retargeting su demand esistente
- Risultati "troppo buoni" su un canale che non scala → black box o overclaim


## Errore silenzioso

Quando un agente sbaglia senza farsi accorgere: il fallimento più pericoloso. Da qui si derivano HITL e guardrail — la fiducia si progetta a partire dal fallimento, non dal successo.


## First-instinct-is-wrong

Il modello dà una risposta plausibile e troppo sicura finché non dichiari il vincolo. Pattern ricorrente del corso: in S1 sbaglia sul dato, in S2 sul destinatario, in S3 sul confine calcolo/ipotesi, in S4 sulla linea automazione/agente.


## Framework Chi-Cosa-Tono

| Domanda | Cosa determina | Errore tipico |
|---------|---------------|---------------|
| **Chi?** | Il livello di dettaglio, il linguaggio, le leve che ha in mano | Dire "il management" — troppo vago per scrivere una storia tagliente |
| **Cosa?** | Il messaggio unico. Non tre insight: uno. | Mettere tutto per non sbagliare nulla — e perdere il lettore |
| **Tono?** | Urgenza, registro, quantità di contesto necessario | Usare lo stesso tono per un alert e per un report mensile |


## GA4 è un campione, non la verità

GA4 non è la verità assoluta: è un **campione tracciato con buchi noti** (ITP, restrizioni cookie, browser specifici). Va letto insieme alle altre fonti — vedi Le tre fonti.


## Guardrail

Ciò che il sistema non deve fare MAI, nemmeno quando va tutto bene. Se non sai dire cosa non deve mai fare, il flusso è ancora troppo vago.


## HITL (human-in-the-loop)

Il punto in cui l'umano decide, prima di ogni azione irreversibile o di giudizio. Si individua a partire dal fallimento più pericoloso del flusso. Vedi anche la fonte sui pattern HITL.


## Il contratto col modello

**Non inventa numeri.** Se un valore non è nei dati caricati, lo dichiara. Mai stime spacciate per fatti.

**Sui calcoli usa il code interpreter.** Somme, medie, percentuali, ROAS, CAC: sempre calcolati con codice. Il modello fa errori aritmetici a mente in modo silenzioso e sicuro di sé.

**Tre piani, sempre separati:**
1. *Evidenza* — "nei dati risulta che…" (fatto, con numero e fonte)
2. *Interpretazione* — "questo suggerisce che…" (ipotesi difendibile)
3. *Azione* — "quindi farei…" (raccomandazione)

**Conosce i limiti delle fonti.** I dati piattaforma sovrastimano (ognuno conta le sue conversioni). Analytics traccia parzialmente. Il CRM/backend è la verità sugli ordini. Quando le fonti divergono, lo segnala invece di sceglierne una.

**Risponde a una domanda di business, non produce tabelle.** Una tabella da sola non è un'analisi.

---


## Il numero senza contesto è rumore

Un ROAS di 3,2 è un buon risultato? Dipende. Rispetto a cosa?

| Tipo di confronto | Quando usarlo | Attenzione |
|---|---|---|
| **Vs target/obiettivo** | Più azionabile — il gap è la domanda del management | Il target era realistico? |
| **Vs periodo precedente** | Isola la tendenza | Stagionalità: BF vs ottobre non si confrontano |
| **Vs benchmark di mercato** | Potente — differenzia "siamo peggiorati" da "siamo sotto mercato" | Difficile da ottenere, facile da gonfiare |
| **Vs altra dimensione** | Diagnostico — isola la variabile che spiega | Attenzione alle variabili confondenti |

**Regola:** ogni grafico ha un confronto implicito. Renderlo esplicito è già metà del lavoro di storytelling.


## Il principio fondante dello storytelling

Un'analisi che non arriva a chi decide non esiste. Il problema dei report non è quasi mai la qualità del dato — è che nessuno li ha pensati per un lettore specifico. Il cervello umano non elabora dati: percepisce pattern, accorcia, completa, dimentica. Progettare per questo non è estetica, è efficacia.

**Il test della frase:** prima di costruire qualsiasi grafico, scrivi:
> *"[Chi] deve capire che [cosa] per poter [decidere/fare cosa]."*

Se non riesci a scriverla, non hai ancora la storia. Se riesci, hai già la struttura.


## La budget simulation di Google come black box

Lo slider "spendi X → ottieni Y" di Google Ads è comodo e opaco: non dichiara assunzioni, range di validità, dipendenza dalle creative. Ricostruire il simulatore a mano non serve a fare meglio di Google — serve a **capire quali variabili Google nasconde**, così sai quando fidarti e quando no.


## La catena Obiettivo-KPI-Metrica-Evento

Prima di toccare un dato, si costruisce questa catena. Senza, si analizzano le cose sbagliate.

```
Obiettivo di business
    └── KPI (max 2-3, con soglia e azione collegata)
            └── Metrica (come si calcola, da quale fonte)
                    └── Evento/parametro sul sito (cosa deve essere tracciato)
```

**Regola:** un KPI senza soglia numerica e senza un'azione collegata è solo un numero. "ROAS" non è un KPI. "ROAS < 3x → rivedi l'allocazione di quel canale" è un KPI.

**Errore comune:** partire dai dati disponibili invece che dall'obiettivo. Porta a ottimizzare la metrica sbagliata.


## La saturazione

Ogni canale ha **rendimento decrescente**: i primi euro prendono la domanda più calda, gli euro successivi rendono meno. Il CPA marginale sale con la spesa.

```
conversioni ≈ Vmax × spesa / (spesa + K)
  Vmax = tetto di conversioni catturabili dal canale
  K    = spesa a cui raggiungi metà del Vmax (K basso = satura presto)
```

**Conseguenza pratica:** senza saturazione, un simulatore dice sempre "tutto sul canale col ROAS più alto" — sbagliato, perché quel canale satura e il ROAS crolla. La domanda giusta non è "qual è il canale migliore" ma **"fino a che punto questo canale rende, prima che convenga spostare l'euro successivo altrove?"**. L'allocazione ottima si raggiunge quando il *ritorno marginale* dei canali si pareggia.


## La struttura del deliverable

*(da compilare)*


## Le tre fonti

| Fonte | Cosa misura | Bias principale |
|---|---|---|
| **Piattaforma** (Google Ads, Meta, TikTok…) | Conversioni attribuite dalla piattaforma stessa | Sovrastima: ogni piattaforma conta le sue |
| **Analytics** (GA4, ecc.) | Sessioni, eventi e conversioni tracciati sul sito | Sottostima: cookie, ITP, adblocker, bug di tracking |
| **Backend / CRM** | Ordini reali dal gestionale | La verità sulle vendite, ma non sa quale canale le ha generate |

**Come riconciliarle:**
- Non cercare un numero "giusto" unico: non esiste.
- Usa il backend come ancora (gli ordini ci sono o non ci sono).
- Il gap piattaforma/analytics segnala problemi di attribuzione o tracking.
- Il gap analytics/backend segnala problemi tecnici specifici (cookie, device, browser).
- Dichiara sempre da quale fonte viene ogni numero in un report.


## Le tre prediction da non confondere

"Fare prediction" nel marketing significa almeno tre cose diverse. Prima di costruire qualsiasi cosa, stabilisci quale:

| Tipo | Domanda | Strumento tipico | Sbaglia quando |
|---|---|---|---|
| **Per-utente** | Questo utente comprerà / spenderà quanto? | pLTV, predictive audience GA4 | Il mondo cambia e il modello non lo sa |
| **Per-decisione** | Se sposto budget da A a B, cosa succede? | Budget simulation (Google Ads), simulatore proprio | Ignora La saturazione |
| **Per-andamento** | Dove sarà il fatturato a settembre? | Forecasting, trend+stagionalità | Estrapola troppo lontano |


## Le variabili di un simulatore di allocazione

| Variabile | Perché serve | Trappola se la ignori |
|---|---|---|
| CPA/ROAS attuale per canale | Punto di partenza | — |
| **Curva di saturazione** | Cattura il rendimento decrescente | "Metti tutto sul canale top" |
| Incrementalità | Quanto sarebbe successo comunque | Sovra-investi su Brand/retargeting |
| Vincoli min/max | Realismo operativo | Raccomandi l'ineseguibile |
| Lag temporale | Il budget di oggi non converte tutto oggi | Stime troppo precise |
| Fatica creativa | Un canale satura perché la creative si brucia | Confondi saturazione di pubblico e di creative |


## Mental models e euristiche

*Principi che si confermano sul campo. Iniziati dal framework, integrati dall'esperienza su casi reali.*

- **"Il ROAS più alto è spesso il meno incrementale."** Brand search, retargeting, PMax: ottimi numeri, bassa prova di causalità.
- **"Se un canale 'migliora' mentre tutto il resto peggiora, guarda se sta cannibalizzando."**
- **"Il CAC che sale è quasi sempre un sintomo, non una causa."** La causa può essere nella retention, nel prodotto, nella qualità dei lead, nel tracciamento.
- **"Un problema di tracciamento camuffato da problema di performance."** Prima di tagliare un canale, verifica che il dato sia pulito.
> *[continua a crescere — aggiungi qui i principi che si confermano durante il corso e dopo]*

---


## Non è un MMM

Quello che costruisci è un **simulatore di allocazione basato sull'efficienza osservata dei canali**: trasparente, a scatola aperta, parte dalle metriche di piattaforma.

L'**MMM (Marketing Mix Model)** è un'altra cosa: stima l'incrementalità *reale* di ogni canale (anche offline e brand) su tutta la domanda, via regressione su serie storiche, gestendo adstock/carryover/baseline. Risponde a una domanda causale più ambiziosa: *quanto vale davvero ogni euro al netto di quello che sarebbe successo comunque?*

Frase da tenere a mente: *"Un simulatore di allocazione non è un MMM. È lo strumento giusto quando hai i dati di piattaforma e vuoi ridistribuire. L'MMM è il gradino dopo, per quando l'attribuzione deterministica non basta più."*


## Orchestratore

Un livello di regia sopra più agenti: raccoglie gli output, elimina il rumore, ordina per priorità e consegna un solo punto di attenzione. L'anti-dashboard.


## PMax è una black box

Un PMax ad alto ROAS non è di per sé un segnale positivo: finché non sai cosa contiene, è una **black box** che può cannibalizzare brand e retargeting. Vedi La budget simulation di Google come black box.


## ROAS di piattaforma vs valore reale

Il ROAS dichiarato dalle piattaforme **sovrastima per costruzione**: ogni piattaforma si auto-attribuisce conversioni che sarebbero avvenute comunque. Il ROAS di piattaforma non è il valore incrementale generato. Vedi Le tre fonti ed Efficienza vs incrementalità.


## Struttura di un buon prompt di analisi

```
CONTESTO: [chi è il cliente, qual è il periodo, qual è la fonte dati]
DOMANDA: [domanda di business specifica — non "analizza questo", ma "perché X è calato?"]
VINCOLO: [cosa NON deve fare — es. "non fare ipotesi su dati che non hai"]
OUTPUT: [formato che ti serve — es. "una diagnosi in 3 frasi + il grafico che la supporta"]
```


## Tre audience tipo nel digital advertising

**CEO / CFO** — domanda: *"È un problema strutturale o lo risolviamo con un cambio di budget?"*
- Tempo di attenzione: 90 secondi
- Non vuole: metriche di campagna (CPM, CTR, CPC)
- Vuole: una tesi e una decisione prendibile
- Messaggio efficace: conclusione prima, prove dopo

**Head of Marketing / Brand Manager** — domanda: *"Qual è la causa vera e come la dimostro?"*
- Ha bisogno di argomenti, non solo conclusioni
- Legge i numeri ma deve difenderli davanti a chi non li legge
- Messaggio efficace: diagnosi causale + prova da almeno due fonti

**Performance / Adv Specialist** — domanda: *"Cosa faccio lunedì mattina?"*
- Vuole leve concrete e priorità esplicite
- Non può agire su logistica o brand — può agire su budget e creative
- Messaggio efficace: tre azioni specifiche in ordine di priorità


## pLTV in una formula

```
pLTV ≈ P(acquisto) × valore medio ordine × numero atteso di acquisti
```

Ogni pezzo è stimato dai dati storici: il modello cerca utenti passati simili e proietta. **Assunto nascosto: il futuro somiglia al passato.** Un modello pLTV addestrato su dati pre-rottura (es. pre-cambio corriere) continua a promettere clienti di valore mentre la realtà è già cambiata. La predizione vale quanto l'assunto che la regge.



# Il caso Filo Studio


## Chiara Donadoni

Co-founder creativa di Filo Studio. Custodisce il brand: niente sconti, coerenza dell'identità. La sua nota è il vincolo di brand costante.


## Dataset Filo

> Rappresenta il funnel digitale DTC, non il fatturato totale.

**Due formati, stesso contenuto.** L’Excel raccoglie tutto in un unico file con 7 fogli (incluso un foglio Leggimi). I CSV sono gli stessi dati separati, più comodi da caricare direttamente nell’LLM.

| File | Cosa contiene | Da ricordare |
|---|---|---|
| `filo_ads_dataset.xlsx` | **Master file** — tutti i fogli in uno (Campagne, GA4, Vendite, Ops, Creative, Daily Q4) | Inizia dal foglio Leggimi |
| `filo_ads_campagne_mensili.csv` | Performance per campagna, dichiarate dalle piattaforme | ⚠️ Contiene errori di data quality: va pulito prima di analizzare |
| `filo_ga4_canali_device_mensili.csv` | Sessioni e conversioni per canale × device | Attenzione al breakdown per device (gap Safari mobile) |
| `filo_vendite_backend_mensili.csv` | Ordini reali, nuovi vs ritorno, repeat rate | Fonte di verità |
| `filo_ops_esperienza_mensili.csv` | Consegna, resi, NPS, ticket | Il lato post-acquisto |
| `filo_creative_metadata.csv` | Metadata creative: hook, formato, CTR iniziale/finale, CVR, file immagine | Confronta con le immagini nella cartella `creative/` |
| `filo_ads_giornaliero_q4_2025.csv` | Dettaglio giornaliero Q4 2025 | Per il drill-down ultimi 3 mesi |
| `filo_budget_test_settimanale_q1_2026.csv` | **(S3)** 13 settimane di test budget: spesa→conversioni a livelli diversi per canale | Da qui si inferiscono le curve di saturazione |
| `filo_budget_attuale_mensile.csv` | **(S3)** Allocazione budget di partenza (9.000 €/mese), sub-ottimale | È il punto da migliorare con il simulatore |

---


## Filo Studio

E-commerce di abbigliamento lifestyle (basics e capsule, cotone organico e lino), Milano, dal 2018. Due ex designer di Zara. Posizionamento: "moda italiana onesta". Payoff: *Vestiti fatti per durare. Non per sembrare.* Target: donne 25–40, nord Italia, urbane. AOV 54€ e in calo. Canali: e-commerce 70%, Amazon 15%, pop-up stagionali 15%.

**I tre interlocutori:** Luca (co-founder, vuole risposte semplici, non legge i report), Giulia (Head of Marketing, brava sul brand, a disagio coi numeri), Marco (Customer Service Lead, sa tutto dei clienti uno per uno, non riesce a scalare quella conoscenza).

**Il problema dichiarato:** *"Abbiamo aumentato la spesa adv ma i ricavi non crescono e il CAC è quasi triplicato. Dove sono andati i soldi?"*

**Il segnale che non c'è nei dati adv ma va cercato:** i commenti NPS negativi parlano quasi solo di tempi di spedizione e difficoltà nei resi — non del prodotto. Possibile che il problema sia a valle della vendita, non nelle campagne.


## Giada Ferri

Adv Specialist di Filo Studio, rimasta sola a gestire l'advertising. Scettica e scottata, con due paure precise: un'altra dashboard da controllare, e l'errore silenzioso che non vede. Protagonista di S4.


## Luca Bellini

CEO e co-founder di Filo Studio. Voce dei numeri e della pressione del board (orizzonte 90 giorni). Nelle esercitazioni è il committente che chiede "quanti soldi tornano, e quando".



# Prompt library


## Prompt - Anomaly detection e qualità del dato

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


## Prompt - Data viz e storytelling

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


## Prompt - Diagnosi e analisi performance

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
Perché funziona: definire il criterio interpretativo prima di iniziare impedisce che una metrica facile da leggere (es. CTR, click) venga trattata come autosufficiente quando non lo è.

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


## Prompt - Progettazione agente

Prompt generalizzati emersi in Sessione 4 (progettazione di automazioni e agenti). Sostituire i [PLACEHOLDER] con il caso reale.

**Role-play + auto-audit del fallimento silenzioso** ⭐ *(il metodo-cardine: deriva HITL e Guardrail dal fallimento osservato, non a tavolino)*
> Recita l'aiutante [NOME/RUOLO] su un caso concreto di [CONTESTO]: produci l'output reale che genereresti, poi auto-criticati spietato. Dove sbagli IN SILENZIO per giorni senza che [UTENTE] se ne accorga? Da quel fallimento deriva dove deve decidere l'umano (HITL) e il limite che non superi mai (guardrail).

**Stakeholder avversario con paure nominate** ⭐ *(fa cadere i design fragili prima della plenaria; le paure specifiche trovano ciò che "critica genericamente" non trova)*
> Sei [UTENTE]: scettico, scottato. Attacca questo design con le TUE paure precise ([PAURA 1], [PAURA 2]). Di' se sopravvive così o cosa aggiungere perché tu ti fidi.

**"Giudizio o ricetta" come domanda di routing** ⭐ *(tiene l'AI all'ultimo miglio, impedisce di gonfiare tutto ad agente)*
> Per ogni pezzo del flusso: richiede giudizio o è una ricetta? Se è una ricetta, fanne un'automazione (più affidabile, più economica). L'agente solo dove serve capire e scegliere tra sfumature.

**Critico di conformità contro il brief** ⭐ *(trova campi mancanti, gergo non spiegato, soglie messe come numeri magici)*
> Confronta questo design contro [BRIEF] e [VINCOLI/NOTA UTENTE] ed elenca SOLO i gap: campi mancanti, gergo non spiegato, soglie arbitrarie non giustificate.

**Mostra, non dire (simula con artefatti reali)** ⭐ *(lo stop sul punto umano diventa la dimostrazione della tesi)*
> Non spiegare a parole cosa fa l'agente: simulalo passo per passo con gli artefatti veri (la card di notifica, la tabella, il report), e fermati esattamente dove decide l'umano.

**Output-centric: "cosa riceve l'utente, e dove?"** ⭐ *(sposta da "cosa fa l'aiutante" a flussi concreti e usabili)*
> Specificami quali sono gli output di ogni agente e automazione e in che modo arrivano a [UTENTE] (canale e formato: alert, foglio, documento, memo, digest).

**Scoperta del componente nascosto** ⭐ *(un output ricorrente che coordina più flussi è un componente da progettare, non un formato di consegna)*
> Questo [OUTPUT RICORRENTE] non è anche lui un agente o un'automazione da progettare? Se ha logiche, frequenza, priorità, guardrail e canale, trattalo come un aiutante.

**Blocco del livello: logiche, non implementazione** *(impedisce al modello di costruire workflow reali quando serve solo il disegno)*
> Progettate le logiche degli aiutanti: cosa serve, come dovrebbe funzionare, dove resta [UTENTE], qual è il guardrail. Non costruite niente di funzionante. Obiettivo finale: presentazione.

---


## Prompt - Simulazione e scenari budget

Prompt generalizzati emersi in Sessione 3 (allocazione budget, analisi prescrittiva). Sostituire i [PLACEHOLDER] con il caso reale.

**Marginale, non medio (la regola-cardine)** ⭐ *(sblocca la verità che un canale può avere ottimo ritorno medio e pessimo ritorno marginale)*
> Per ogni canale dimmi se l'euro che sto per spendere rende ancora come i primi, o già meno. Voglio il ritorno sul PROSSIMO euro, non il ROAS medio.

**Numero in codice, poi LLM come interprete** ⭐ *(l'LLM da solo confonde saturazione e ROAS medio; ancoralo al calcolo)*
> Calcola in codice il rendimento marginale per [CANALE/SEGMENTO] (Δoutput ÷ Δinput) usando SOLO questi numeri verificati. Non stimare a memoria.

**Definizione del problema decisionale come scenario, non ottimizzazione** ⭐ *(trasforma il task da "allocazione perfetta" a "decisione argomentata sotto vincoli")*
> [STAKEHOLDER] ha stanziato [BUDGET] in [ORIZZONTE TEMPORALE]. Vaglia [IPOTESI 1], [IPOTESI 2], [IPOTESI 3], [IPOTESI 4]. L'obiettivo non è un'allocazione perfetta, ma uno scenario difendibile: ecco cosa prevediamo succeda, ecco perché abbiamo scartato l'altra, ecco dove la previsione diventa ipotesi.

**Stakeholder come red team** ⭐ *(il piano che sopravvive a tutti i decisori in conflitto è quello da portare in plenaria)*
> Sei [STAKEHOLDER]. Prova a demolire questo piano con le tue domande dure ([PREOCCUPAZIONE 1] / [PREOCCUPAZIONE 2]). Per ogni obiezione dai la risposta difendibile.

**N scenari paralleli ancorati ai dati, poi giudice** *(esplora lo spazio invece di affezionarsi al primo split — solo se ogni scenario è ancorato a numeri reali)*
> Simula [N] split diversi di [RISORSA] (es. retention-heavy, acquisizione-heavy, mix...), ognuno proiettato su [ORIZZONTE] coi numeri veri e scorato. Poi rankali e scegli il bilanciamento migliore.

**Risultati prima della narrativa** ⭐ *(separa analisi e storytelling, riduce il rischio di output convincente ma non difendibile)*
> Prima fornisci i risultati dell'analisi. Solo dopo costruiamo la presentazione per [DESTINATARIO].

**Editing chirurgico su artefatto già prodotto** ⭐ *(più efficace di un generico "rendila migliore")*
> Rifai [ARTEFATTO] con questa struttura: [sequenza esatta, cosa tenere invariato, cosa sintetizzare, cosa aggiungere].

**Passaggio di comprensione finale** *(la prima stesura del modello è quasi sempre gergale)*
> Questa frase non si capisce: [INCOLLA]. Riscrivila per chi non è del mestiere, senza gergo.



# Diario delle sessioni


## S1 - Analisi descrittiva e diagnostica

## [2026-06-16] S1 | TEAM A | ANGOLO: performance e attribuzione

**Messaggio principale trovato**
Il canale più redditizio di Filo non era in nessuna piattaforma — era il cliente che torna; lo si trova solo smettendo di fidarsi del ROAS dichiarato e confrontando tre misurazioni indipendenti della stessa vendita.

**Prompt che hanno funzionato**
- "Pulisci [DATASET]. Elenca OGNI anomalia (outlier, mancanti, duplicati, nomenclatura, date). Per ognuna scrivi come l'hai corretta. Non imputare senza segnalarlo." — ⭐5 — ha forzato 12 anomalie a galla invece di analizzarci sopra
- "Questi sono i numeri verificati in codice: [TABELLA]. Leggi il CSV per il dettaglio ma NON ricalcolare a memoria. Usa solo questi valori come ancore." — ⭐5 — separa calcolo deterministico da interpretazione, elimina metriche allucinate
- "Sei un red team ostile esperto di analytics. DEMOLISCI questo claim: [CLAIM] con evidenza [NUMERI]. Cerca correlazione-per-causalità, variabili confondenti, over-claim. Se regge dillo, se no riformula in modo non attaccabile." — ⭐5 — il pattern singolo più utile della sessione
- "Non classificare le campagne per canale. Classificale per FUNZIONE: domanda nuova (prospecting) vs domanda esistente (brand/retargeting). Calcola quota budget vs quota ricavi per gruppo." — ⭐4 — ha reso visibile che il 12% del budget (harvest) si prendeva il 36% dei ricavi
- "Analizza da [N] angoli indipendenti in parallelo. Ogni lente restituisce: titolo, evidenza, interpretazione, forza, ATTACCABILITÀ. Schema: [JSON]." — ⭐4 — il campo "attaccabilità" forzato nello schema alza la qualità e riduce la retorica

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- Analisi su dataset parziale (solo foglio campagne) → diagnosi plausibile ma di livello sbagliato (media mix invece di retention) → corretto recuperando tutti i 6 fogli: la causa radice è cambiata
- Far aggregare i numeri all'LLM leggendo il CSV direttamente → "spesa media 16k→31k" erano primo/ultimo mese, non la media (19,1k→24,3k) → corretto: ogni aggregato va calcolato in codice
- "Perché è successo?" senza vincoli → narrazione mono-causale compiacente → corretto obbligando a validare ogni ipotesi contro i dati e mappare gli eventi documentati prima di concludere
- Stima impatto riallocazione TikTok→DPA: estrapolazione lineare che ignora il pool finito di retargeting → corretto tenendo la direzione, togliendo il numero assoluto

**Best practice scoperte**
- CSV sporco: dichiara nel prompt come gestire i buchi (segnala/ignora/imputa) — altrimenti il modello sceglie da solo o salta righe in silenzio
- Non lasciare aggregare i numeri all'LLM: calcola in codice, salva come "ground truth", passa come ancore
- Verifica di avere TUTTE le fonti prima di chiedere il "perché": con dati parziali la diagnosi è plausibile e sbagliata di livello
- Red team separato per ogni claim forte, anche solo cambiando ruolo nella stessa chat
- Correlazione alta non basta: chiedi sempre meccanismo + sequenza temporale + evento documentato prima di chiamarla causa

**Metodi di analisi applicati**
- Pulizia dati: 12 anomalie segnalate e corrette prima dell'analisi
- Confronto 2024 vs 2025 per canale/campagna su ROAS, CPA, CPC, CTR
- Bucketing per funzione (harvest/mid/create/vanity): quota budget vs quota ricavi
- Triangolazione: ricavi piattaforma vs GA4 vs backend — rapporto piattaforma/backend cresciuto da 1,0x a 2,8x
- Ritorno marginale della spesa: Δspesa vs Δconversioni — marginale negativo trovato (+68k spesa → −335 conversioni)
- Scomposizione nuovi vs ritorno: il cliente di ritorno spiega il 70% del crollo ricavi (−184k)
- Correlazioni di Pearson 24 mesi: repeat~NPS (+0,98), repeat~resi (−0,92), ROAS reale~repeat (+0,95)
- Mapping causale su timeline eventi (cambio agenzia, cambio corriere, +5% prezzi, Black Friday)

**Cosa il modello ha sbagliato o inventato**
- Diagnosi di livello sbagliato su dati parziali (media/attribuzione invece di retention) — errore di gerarchia causale, non di calcolo
- "Le piattaforme gonfiano/mentono" — formulazione troppo forte, poi corretta in sovra-attribuzione strutturale (finestre 28gg, sistemi non integrati): metà del gap è modello di attribuzione, non frode
- Causalità del cambio corriere presentata come causa unica del crollo retention — i dati mostrano che il calo era già in corso da gennaio 2024, il corriere ha aggravato, non creato
- Estrapolazione lineare sulla riallocazione TikTok→DPA che ignora il pool finito
- Outlier di dicembre (margine −22%, Black Friday) rischiava di essere letto come regime medio

**L'insight più importante della sessione**
Il canale più redditizio di Filo non era in nessuna piattaforma — era il cliente che torna, trovato solo confrontando tre misurazioni indipendenti della stessa vendita invece di fidarsi del ROAS dichiarato.

---

## [2026-06-16] S1 | TEAM B | ANGOLO: economics (CAC & retention)

**Messaggio principale trovato**
Acquisiamo in modo sempre meno sostenibile e chi acquisiamo torna sempre meno — ma il salto netto di giugno 2025 (cambio corriere) spiega solo l'ultimo terzo del problema: il 62% del calo di repeat rate era già avvenuto prima, in un declino lento dal 2024 le cui cause non sono isolate nei dati.

**Prompt che hanno funzionato**
- "[CONTESTO]. Come [TEAM] ci occupiamo di [AREA]. Domanda guida: [APERTA, non una metrica]. [perché conta e qual è il sospetto da verificare]." — ⭐5 — la domanda aperta ("acquisiamo in modo sostenibile, e chi acquisiamo resta?") ha lasciato al modello la libertà di scegliere la fonte di verità e proporre la segmentazione pre/post evento non richiesta esplicitamente
- "Spiegaci come hai svolto i passaggi. Quali domande ti sei posto? Quali metriche hai estratto? Come hai pulito e segmentato? Step by step." — ⭐5 — chiesto POST-HOC, con domande puntuali, forza risposte verificabili con codice ri-eseguito
- "Indicaci in maniera sintetica la risposta alla domanda guida ([RIPETI LA DOMANDA])." — ⭐4 — ripetere la domanda originale ancora la sintesi a ciò che serve al CEO, ma ha sovra-semplificato l'attribuzione causale (vedi errori)
- "Creaci un prompt per [TOOL]. Struttura: [N slide], contenuto di ciascuna, tono, istruzioni sui grafici, formato output." — ⭐5 — specificare slide-per-slide produce un artefatto riutilizzabile, non un meta-prompt generico

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- Nessun rifiuto tecnico vero. Il problema è stato un'auto-correzione insufficiente: la sintesi "in una frase" ha attribuito il crollo retention al cambio corriere in modo più netto di quanto i dati supportassero isolatamente
- Lezione esplicita: "prima di sintetizzare in una frase, quantifica quanto della variazione totale è spiegato dal fattore che stai per nominare come causa principale" — andava chiesto PRIMA, non scoperto dopo in revisione

**Best practice scoperte**
- Con più tab/fonti sovrapposte, specificare nel prompt qual è la fonte di verità o chiedere al modello di argomentare la scelta
- Se ci si aspettano dati sporchi, chiederlo esplicitamente nel prompt iniziale ("verifica anomalie e duplicati prima di aggregare") — qui sono stati trovati comunque, ma solo perché il modello ha scelto di ispezionare a fondo
- Quando si chiede una "causa", richiedere esplicitamente la quantificazione della quota di variazione spiegata — non solo la coincidenza temporale
- Per "spiega il processo" dopo un'analisi fatta, chiedere codice ri-eseguito che produce gli stessi numeri citati, non un riassunto a parole — rende falsificabile l'auto-racconto del modello
- Quando l'output alimenta un secondo tool, chiedere il prompt intermedio come artefatto a parte, da rivedere prima che venga eseguito da un sistema meno controllabile

**Metodi di analisi applicati**
- Riconciliazione tra fonti indipendenti: confronto spesa aggregata Campagne vs Vendite backend, mese per mese — ha scovato l'errore di segno sulla spesa TikTok di maggio 2025 (scostamento di 3.159€ = doppio di una riga negativa)
- Normalizzazione testuale dei nomi canale prima di aggregare
- Deduplicazione esatta su righe identiche (mese, canale, campagna)
- CAC a due livelli: blended (spesa totale/nuovi clienti totali) e per canale — il primo dà il quadro generale, il secondo scompone se il peggioramento è diffuso o concentrato
- Confronto pre/post evento: punto di rottura individuato cercando un salto netto e stabile (non un trend graduale) in giorni di consegna e NPS — giugno 2025
- Quota di variazione spiegata da un sotto-periodo: quanta parte del calo totale di repeat rate (−18 punti) sia avvenuta prima vs dopo il punto di rottura — fatto in revisione, non nell'analisi originale

**Cosa il modello ha sbagliato o inventato**
Non ha inventato numeri (tutti ricalcolati con pandas), ma ha commesso un errore di enfasi che è di fatto un errore analitico: nella sintesi, il cambio corriere di giugno 2025 è stato presentato come la spiegazione del crollo retention, mentre il 62% del calo totale (da 36% a 18%) era già avvenuto PRIMA, in un declino lento dal 2024 le cui cause non sono isolate nei dati. Il salto di giugno è reale e ben documentato, ma spiega solo l'ultimo terzo del fenomeno — non emerge leggendo la singola risposta, solo riconducendo la sintesi al dato grezzo.

**L'insight più importante della sessione**
Una correlazione temporale netta e ben visualizzabile tende a "mangiarsi" visivamente e narrativamente un problema più lento e meno fotogenico che la precede — il vero lavoro analitico non è trovare la causa più chiara, ma misurare quanto della variazione totale quella causa spiega davvero prima di darle il titolo della slide.

---

## [2026-06-16] S1 | TEAM C | ANGOLO: creative

**Messaggio principale trovato**
Una creatività efficace non è quella che genera più click, ma quella che rende immediatamente concreto il motivo per cui il prodotto vale l'acquisto.

**Prompt che hanno funzionato**
- "Sei un consulente di performance marketing e brand strategy. Hai dataset campagne, dossier brand, file creatività. Domanda: quali creatività vendono e quali fanno solo cliccare? [6 passaggi: distingui engagement da conversione → matrice visibilità/conversione → leggi formato/copy/composizione/tono → pattern → coerenza brand → tabella+insight+raccomandazioni]" — ⭐5 — obbliga a non fermarsi ai KPI e a collegare dato quantitativo, visual e posizionamento
- Framing esplicito del criterio interpretativo ("i numeri senza le immagini sono incompleti, le immagini senza i numeri sono estetica") — ⭐5 — ha impedito che il CTR venisse letto come metrica autosufficiente
- "Ecco le creatività reali utilizzate. Verifica che ciò che hai scritto sia corretto." — ⭐4 — controllo qualitativo sui visual reali dopo la prima analisi, ha corretto interpretazioni basate solo su nomi/metadati
- "Rendi la tabella un Excel che devo passare a un collega." — ⭐4 — trasforma l'analisi in deliverable riutilizzabile con classificazione, soglie, sintesi, legenda
- "Genera una presentazione con tutte queste considerazioni da esporre al Boss. Che formato mi consigli?" — ⭐4 — spinge il modello a cambiare registro da analisi estesa a sintesi executive

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- Recupero creatività da Google Drive → il modello non riesce a scaricare/leggere direttamente dalla cartella → corretto caricando le immagini direttamente in chat
- Prima analisi senza visual reali → la lettura visuale era dedotta da nomi e metadati, non dalle immagini → CR-002 letta come "macro tessuto" invece di "still life materico", corretta dopo il caricamento
- Slide comparative (5,6,7) con KPI non omogenei tra creatività → corretto standardizzando la griglia: CTR, CVR, CPA, ROAS stimato — nelle slide comparative i KPI devono restare costanti anche se il commento cambia
- ROAS stimato con AOV del brand invece di revenue reale per creatività → dichiarato esplicitamente come proxy direzionale, non metrica contabile

**Best practice scoperte**
- Caricare sempre dataset + dossier brand + creatività reali insieme: i nomi file non bastano a leggere il visual
- Separare esplicitamente metriche di engagement da metriche di conversione, altrimenti il modello sovrastima CTR/click/impression
- Specificare le categorie di classificazione PRIMA dell'analisi (matrice alta/bassa visibilità × alta/bassa conversione) per rendere l'output confrontabile
- Dopo la prima analisi, caricare i visual e chiedere una verifica puntuale: è il modo più rapido per individuare deduzioni fragili
- Nelle presentazioni per decisori, imporre una griglia KPI uniforme su ogni creatività

**Metodi di analisi applicati**
- Segmentazione engagement/conversione: CTR/impression/reach/frequenza separati da acquisti/CVR/CPA/revenue/ROAS
- Matrice visibilità/conversione a 4 quadranti: scalare / correggere / sospendere
- ROAS stimato con AOV (conversioni × ordine medio / spesa) come proxy in assenza di revenue puntuale
- Lettura visuale: formato, presenza prodotto/persone, composizione, tono emotivo, palette, copy, concretezza del messaggio
- Analisi di coerenza con posizionamento/target/promessa/valori/tono del brand
- Pattern recognition tra creatività che convertono vs che generano solo click
- Controllo executive: revisione del deliverable per omogeneità KPI nelle slide comparative

**Cosa il modello ha sbagliato o inventato**
Ha dedotto la lettura visuale senza le immagini reali (CR-002 letta come "macro tessuto", corretta in "still life materico" dopo verifica). Ha prodotto una prima presentazione con KPI non omogenei tra slide comparative — logica comprensibile ma forma debole. Ha usato un ROAS stimato (non reale) senza dichiararlo come proxy fino alla correzione. Ha tentato di lavorare su un link Drive senza poter recuperare i file. Ha trattato inizialmente creatività mancanti come parte del quadro completo, prima che venisse specificato di limitare la verifica alle sole creatività effettivamente visibili.

**L'insight più importante della sessione**
Una creatività efficace non è quella che genera più click, ma quella che rende immediatamente concreto il motivo per cui il prodotto vale l'acquisto.

---

## [2026-06-16] S1 | SINTESI DOCENTE | connessioni tra i team

> Nota: la cross-examination dal vivo non si è svolta per limiti di tempo. Questa sintesi ricostruisce a freddo le connessioni che sarebbero emerse, leggendo i tre output insieme — è il pezzo che normalmente il docente costruisce a voce in main room.

**La connessione più importante: A e B raccontano lo stesso fatto da due lati, e nessuno dei due da solo aveva la versione completa.**

Il Team A ha trovato che il cambio corriere "ha aggravato, non creato" il crollo della retention — il riacquisto calava già da gennaio 2024. Il Team B, indipendentemente, è arrivato alla stessa identica correzione per una strada diversa: ha quantificato che il 62% del calo di repeat rate era già avvenuto PRIMA di giugno 2025. Due team, due metodi (mapping causale su timeline eventi vs quota di variazione spiegata da un sotto-periodo), stessa conclusione corretta. Questo è il segnale più forte della sessione: quando due angoli indipendenti convergono sulla stessa correzione di una narrazione troppo netta, la correzione è probabilmente vera.

**Il pattern "First-instinct-is-wrong" si è ripetuto identico in tutti e tre i team — e in tre forme diverse:**
- A: la prima sintesi diceva "le piattaforme mentono" — poi corretta in sovra-attribuzione strutturale (metà del gap è modello di attribuzione, non frode)
- B: la prima sintesi attribuiva il crollo retention al corriere in modo netto — poi corretta quantificando che spiega solo l'ultimo terzo
- C: la prima lettura visuale (CR-002 "macro tessuto") era dedotta dai metadati senza guardare l'immagine reale — corretta dopo verifica visuale

In tutti e tre i casi l'errore non è stato un'allucinazione di numeri (i tre team lo segnalano esplicitamente: nessun numero inventato), ma un eccesso di sicurezza nella prima narrazione — risolto solo da un secondo passaggio esplicito di verifica/quantificazione. **Lezione trasversale per la wiki: la prima sintesi di un LLM è quasi sempre più netta di quanto i dati supportino. Il passaggio che la corregge va richiesto esplicitamente, non sperato.**

**Sul ROAS: A e C arrivano alla stessa diffidenza per ragioni complementari.**
A smonta il ROAS aggregato di piattaforma (sovra-attribuzione strutturale, finestre di attribuzione, sistemi non integrati). C smonta il ROAS per creatività (CR-005 sconto: CTR alto, ma è quello che A chiamerebbe "harvest" — domanda catturata non creata). Se si uniscono i due angoli: il ROAS è gonfiato sia a livello di canale sia a livello di creative, e per la stessa ragione di fondo — si misura quello che è facile attribuire, non quello che è incrementale.

**Quello che nessun team ha potuto vedere da solo:** il quadro completo richiede A (dove sembra andare bene ma non è incrementale), B (perché il cliente non torna, e da quando), e C (cosa nelle creative comunica valore vs cosa compra solo attenzione). Nessuno dei tre, isolato, arriva alla diagnosi: "stiamo spendendo di più su un mix che premia l'harvest non il prospecting, su creative che a volte vendono sconto invece che il prodotto, mentre il vero collo di bottiglia — il cliente che non torna — peggiora da più tempo di quanto chiunque pensi e non è riconducibile a un solo evento."

---


## S2 - Data storytelling per audience

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
- Richiesta iniziale sui grafici → corretti sul piano diagnostico ma non orientati all'azione ("budget vs ricavi harvest" spiega il problema ma non dice quanto spostare e da dove) → riformulati in grafici operativi (riallocazione attuale vs consigliata, matrice CTR/CVR, quota budget vs quota ricavi)
- Prima versione della presentazione → usabile ma richiedeva spiegazione orale (perché una metrica alta non implica più budget) → spiegazioni puntuali pag. 2/3/4, poi rigenerata
- Grafico harvest → etichette arrotondate illeggibili invece di percentuali → chiarito che il punto non è "harvest non funziona" ma "harvest sotto cap perché intercetta domanda già esistente"
- Raccomandazione TikTok → rischio di lettura troppo netta (spegnere) → formulata come "ridurre a test cap", non spegnere: tiene il canale aperto a nuovi test ma ne impedisce lo scaling su vanity metric

**Best practice scoperte**
- Per un destinatario operativo, definire subito le leve toccabili (budget/canali/creative/cap/test) ed escludere il fuori-scope (logistica, prodotto, CX)
- Chiedere quali grafici servono e perché prima di generarli: il primo set è descrittivo, il secondo (dopo challenge) decisionale
- Separare sempre metrica di attrazione e metrica di acquisto: CTR e CVR insieme, mai CTR da solo
- Quando un canale ha ROAS alto, chiedere se crea domanda o cattura domanda già esistente (Brand, Retargeting, PMax gonfiano la lettura)
- Far spiegare la slide come se parlasse al destinatario finale: fa emergere ambiguità grafiche e narrative prima della consegna

**Metodi di analisi applicati**
- Riallocazione a budget invariato: budget mensile costante e ridistribuito — raccomandazione attuabile senza chiedere nuovo investimento
- Cap operativo su harvest: Brand Search e Retargeting non eliminati ma messi sotto cap, per preservare la funzione di chiusura senza assorbire budget su ROAS apparente
- Matrice CTR/CVR per creatività: distinguere asset che generano attenzione da asset che generano traffico acquistabile
- Quota budget vs quota ricavi attribuiti per harvest (12% budget / 36% ricavi): mostra la sproporzione tra spesa e merito apparente
- Classificazione domanda creata (prospecting) vs catturata (brand/retargeting/harvest)

**Cosa il modello ha sbagliato o inventato**
- Grafici buoni per spiegare la diagnosi ma non abbastanza per guidare una decisione operativa immediata
- Ha rischiato di sovrainterpretare il ROAS come scalabilità, mentre era contaminato da sovra-attribuzione, domanda già esistente e black box PMax
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

In S1 il pattern "First-instinct-is-wrong" era sui dati: la prima sintesi del modello era sempre più netta di quanto i numeri reggessero. In S2 si ripete identico ma un livello sopra, sul destinatario: la prima risposta del modello assume il frame sbagliato (presentatore = destinatario), il primo grafico risponde alla domanda di nessuno, il primo colore segue il sentiment della metrica e non la direzione del dato. Stesso fallimento — un output plausibile e troppo sicuro — finché non si dichiara esplicitamente il vincolo. In S1 il vincolo era analitico, in S2 è comunicativo.

**La cross-examination dal vivo ha confermato l'errore di framing, team per team — e quasi sempre l'ha trovato il destinatario, non il team.**

- **Team A (CEO/CFO):** la slide che introduceva la spesa pubblicitaria ha "rotto" la tesi della retention in diretta. Da CEO: *"da questa chart capisco che ho speso male i soldi, ma prima mi stavi raccontando che è un problema di retention."* Piermatteo ha ammesso live: *"fa figurare come se le campagne non funzionassero invece che il cliente a non tornare."* È esattamente l'errore "framing che tradisce la tesi" che il team aveva documentato — ma a farlo emergere è stato il lettore, non l'autore. Stesso esito sulla didascalia "clienti persi = 70% del calo": il destinatario non l'ha capita ("è misleading"), e la conclusione è stata che il grafico spiega meglio della frase sotto — o lo spieghi davvero, o lo togli.

- **Team B (Head of Marketing):** il saldo economico impostato-ma-non-chiuso (15.300€/mese di retention vs risparmio corriere) ha retto al live, e anzi è stato stress-testato: 15.300 × 12 ≈ 180k/anno, un corriere non può plausibilmente costare 250k da una parte e 70k dall'altra, quindi il saldo pende verso il "tenere". Il punto debole è emerso su TikTok: il team lo metteva sullo stesso piano di Google sulla stessa metrica, senza pesare che TikTok costa ~5× e fa probabilmente awareness. La domanda giusta, emersa in aula (Piermatteo): *"quanto scende Google se togli TikTok?"*. La disciplina anti-overclaim di S1 ("aggrava, non causa") qui ritorna in forma comunicativa: "ridurre non spegnere" era la conclusione giusta, ma la *ragione* era ancora incompleta finché la cross-examination non l'ha aperta.

- **Team C (Adv Specialist):** il destinatario operativo ha rifiutato i grafici diagnostici in diretta. Sul grafico harvest 36%/12%: *"il ragionamento mi è chiaro, ma il grafico non mi sta dicendo questa cosa"* + *"perché dici a chi mette le mani sulle campagne di non guardare il ROAS? Digli cosa fare."* Dei tre grafici è sopravvissuta solo la riallocazione del budget (*"so cosa fare da domani veramente"*); harvest e matrice creative, giudicati misleading, sarebbero stati tagliati. La matrice CTR/CVR è cascata su un dettaglio che il team non poteva vedere da solo: era divisa per tipo di creatività ma la performance di una creatività dipende dal tipo di campagna in cui gira (una creatività retargeting può essere editoriale) — quindi posizionarla senza il canale "non funziona".

**Il lavoro che il modello non può fare da solo: un lettore ostile.**

Due grafici "corretti nel deck" sono caduti appena letti a freddo — la slide spesa di A, il grafico harvest di C. Entrambi tecnicamente giusti, entrambi rotti in sala. I due prompt che ci si avvicinano — "verifica nel browser" (A) e "spiega la slide al destinatario" (C) — sono buoni surrogati, ma il test vero è un lettore ostile, ed è la cross-examination. Il modello, lasciato solo, conferma; il destinatario, no.

**Quello che nessun team ha potuto vedere da solo:** la stessa diagnosi è diventata tre oggetti irriconoscibili per tre destinatari — prova che il framing è un secondo lavoro analitico, non packaging. E la cucitura dove il frame perde (la slide spesa, il grafico harvest, l'equivalenza TikTok/Google) la trova il destinatario, non chi ha costruito la slide. Per questo la slide va sempre testata contro chi la riceverà, non contro chi l'ha fatta.

---


## S3 - Allocazione budget e analisi prescrittiva

## [2026-06-23] S3 | TEAM A | ANGOLO: rendimento marginale (saturazione) + red team degli stakeholder

**Messaggio principale trovato**
Un modello genera dieci scenari plausibili in un minuto — ed è l'opposto di una previsione. Il valore non è esplorare più opzioni: è scegliere UNA, ripararci il modello economico rotto, e dire onestamente dove finisce il dato e comincia l'ipotesi.

**Prompt che hanno funzionato**
- "Calcola in codice il rendimento marginale per canale (Δconversioni ÷ Δspesa) e l'economia della retention. Usa SOLO questi numeri verificati, non stimare a memoria." — ⭐5 — l'LLM da solo confonde saturazione e ROAS medio; ancorarlo al marginale calcolato in codice tiene la diagnosi onesta
- "Per ogni canale dimmi se l'euro che sto per spendere rende ancora come i primi, o già meno. Voglio il ritorno sul PROSSIMO euro, non il ROAS medio." — ⭐5 — sblocca la verità che un canale può avere ottimo ritorno medio e pessimo ritorno marginale (harvest ROAS 9 ma incrementalità zero)
- "Sei [Luca/Chiara]. Prova a demolire questo piano con le tue domande dure ([incrementalità+timing] / [brand+sconti]). Per ogni obiezione dai la risposta difendibile." — ⭐5 — il piano che sopravvive a entrambi gli stakeholder in conflitto è quello che si porta in plenaria
- "Simula [N] split diversi del budget (retention-heavy, acquisizione-heavy, brand-only, mix...), ognuno proiettato sul trimestre coi numeri veri e scorato. Poi rankali e scegli il bilanciamento migliore." — ⭐4 — esplora lo spazio invece di affezionarsi al primo split; vale solo se ogni scenario è ancorato ai numeri
- "Questa frase non si capisce: [INCOLLA]. Riscrivila per chi non è del mestiere, senza gergo." — ⭐4 — il modello di default scrive "marginale / incrementale / 4 su 5"; con questo prompt diventa leggibile da chiunque

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- "Genera 8 scenari e dimmi il migliore" → output ricchi ma percepiti come speculazione, non previsione: numeri presentati come certi → restare dentro la richiesta del task — UNA scelta, legata al modello economico rotto, con i numeri marcati come stime e un test che li misura
- Primo piano sbilanciato sulla retention → ha quasi ignorato che anche l'acquisizione era in calo (clienti nuovi −21%, Meta rotto sulle creative) → rieseguire considerando entrambi i motori; il bilanciamento vincente li ripara entrambi
- Gergo nel deliverable ("4 euro su 5 fanno un lavoro vero", "torna vs circola" senza spiegazione, "rendimento marginale") → riscrittura in italiano semplice
- Gerarchia visiva ambigua nel diagramma: le due voci di sostegno (brand, test) sotto le due colonne sembravano appartenere una a un motore e una all'altro → etichetta esplicita "sostegno a entrambi i motori, una li alimenta una li misura"

**Best practice scoperte**
- Per allocare, calcola il rendimento del PROSSIMO euro in codice, non il medio: il medio nasconde la saturazione
- Stakeholder in conflitto = red team separati: trasforma ogni decisore in un agente che prova a rompere il piano, tieni la versione che regge a tutti
- Esplora con scenari paralleli MA ancorali ai dati: senza numeri veri ottieni speculazione plausibile, non previsione
- Dichiara il limite di affidabilità in cifre (qui: ~5k/mese per canale storico, 120k = 40k/mese supera lo storico): scrivi dove finisce il calcolo e comincia l'ipotesi, e finanzia un test invece di indovinare
- Fai sempre un passaggio di comprensione finale: reincolla le frasi dense e chiedi la versione per non esperti

**Metodi di analisi applicati**
- Rendimento marginale per canale: Δconversioni ÷ Δspesa per famiglia → CPA marginale (harvest €9 ma circola, mid €19 con margine, creative rotto, TikTok €62)
- Marginale di sistema: Δspesa totale vs Δconversioni → +68.300€ di spesa per −335 conversioni: il marginale aggregato è già negativo
- Classificazione torna / circola / perso: incrementale (retention a margine pieno + acquisizione vera) vs cattura di domanda esistente (harvest) vs perdita (TikTok)
- Limite di estrapolazione: spesa mensile massima storica per canale come soglia oltre cui la previsione è ipotesi
- Economia della retention: ricavi da clienti di ritorno persi per trimestre (≈ −46k) come leva a rendimento marginale più alto, perché €0 di ads e margine pieno
- Simulazione a scenari: 8 split del budget proiettati sul trimestre e scorati su incrementalità, timing, unit economics, doppio motore, brand, affidabilità

**Cosa il modello ha sbagliato o inventato**
- Stime spacciate per previsioni: i numeri della simulazione (retention recuperata, nuovi clienti, "79% torna") sono stime con range largo, presentate con sicurezza eccessiva
- Omissione di un motore: il primo piano ha sovra-pesato la retention e quasi ignorato il calo dell'acquisizione — lacuna colta dalla persona, non dal modello
- Default al gergo: spiega in automatico con "marginale / incrementale / 4 su 5", senza auto-controllo di comprensibilità
- Tendenza a sovra-produrre: più workflow e più scenari quando il task chiedeva una sola scelta difendibile in poche frasi

**L'insight più importante della sessione**
Il valore non è esplorare più opzioni ma scegliere una, riparare il modello economico rotto, e dire onestamente dove finisce il dato e comincia l'ipotesi — perché sul prossimo euro l'AI scalerebbe felicemente il canale dal ROAS medio più alto fino a sbattere, se non gli chiedi se quell'euro rende ancora.

---

## [2026-06-23] S3 | TEAM B | ANGOLO: scenario CEO-ready (decisione difendibile, non allocazione perfetta)

**Messaggio principale trovato**
Quando il problema è la retention, il budget per "far ripartire l'azienda" non va allocato dove il ROAS sembra più alto, ma dove si chiude la perdita che rende inutile continuare ad acquisire.

**Prompt che hanno funzionato**
- "Il CEO ha stanziato [BUDGET] in [ORIZZONTE]. Vaglia [IPOTESI 1-4]. L'obiettivo non è un'allocazione perfetta, ma uno scenario difendibile: ecco cosa prevediamo succeda, ecco perché abbiamo scartato l'altra, ecco dove la previsione diventa ipotesi." — ⭐5 — trasforma il task da "ottimizzazione budget" a "decisione argomentata sotto vincoli"; il modello confronta scenari, non solo distribuisce soldi
- "Allego le mail del CEO che autorizza la spesa con direttive, e della cofondatrice che chiede di non snaturare i principi fondatori." — ⭐5 — aggiunge un vincolo qualitativo alla lettura quantitativa: segnali entro 90 giorni senza crescita incoerente col brand
- "Prima forniscimi i risultati e poi vediamo una presentazione da presentare al CEO." — ⭐5 — separa analisi e storytelling; riduce il rischio di slide belle ma non difendibili
- "Abbiamo scelto lo scenario C. Crea una presentazione in PowerPoint." — ⭐4 — chiude la fase analitica e dà un vincolo netto alla produzione
- "Rifai la presentazione con questa struttura: [sequenza esatta slide per slide, cosa tenere, cosa sintetizzare, copertina]." — ⭐5 — corregge la sequenza narrativa senza riaprire l'analisi; editing strutturale su artefatto già prodotto

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- Allocazione dei 120k tra adv/post-vendita/corriere/agenzia/mix canali → stima economica necessariamente parziale (costi di corriere, customer care, audit agenzia non nel dataset) → esplicitare dove la previsione smette di essere calcolo e diventa ipotesi gestionale
- Valutazione ritorno media sui 120k → la cifra superava molte scale storiche osservate, niente previsione puntuale possibile → stima presentata come range, separando la parte fondata sui dati storici dall'extrapolazione
- Scenario post-acquisto-only → riconosciuto come più coerente con la diagnosi di retention, ma troppo lento per il vincolo dei 90 giorni → non scartato come "sbagliato" ma come incompleto rispetto alla pressione del CEO — permette di difendere lo scenario scelto come compromesso operativo
- Cambio agenzia → sconsigliato il cambio immediato, ma su logica operativa più che dato storico → trattato come opzione condizionata: non decisione immediata, ma esito possibile dopo audit e sprint con KPI
- Prima presentazione PowerPoint → completa ma sequenza non rispecchiava l'ordine voluto (confronto scenari → scelta → dettagli) → richiesta nuova struttura con istruzioni chirurgiche slide per slide

**Best practice scoperte**
- Quando il budget supera la scala storica osservata, chiedere sempre dove la previsione diventa extrapolazione: senza questo vincolo il modello presenta range troppo sicuri
- I vincoli qualitativi di brand vanno inseriti come vincoli decisionali, non come contesto descrittivo (niente sconti aggressivi, niente crescita incoerente, niente traffico comprato con creatività urlate)
- Imporre il confronto tra almeno due scenari scartati e uno scelto: il modello spiega bene la proposta selezionata ma omette perché le alternative non reggono
- Separare "risultati analitici" da "presentazione al CEO": prima si valuta la tenuta della scelta, solo dopo si costruisce la narrativa
- Dopo aver creato una presentazione, correggere con istruzioni chirurgiche (quali slide tenere, sintetizzare, quale copertina) — più efficace di un generico "rendila migliore"

**Metodi di analisi applicati**
- Analisi di scenario: ads-first, post-acquisto-only, mix — confronto su ritorno atteso, tempi, rischi, coerenza con i vincoli
- Vincolo temporale a 90 giorni: distingue interventi sani ma lenti da interventi utili nel breve periodo
- Rendimento marginale della spesa adv: dato storico di aumento spesa associato a calo conversioni, per evitare di scalare canali già saturi
- Distinzione ROAS piattaforma vs ROAS backend: il divario crescente rende il ROAS dichiarato una metrica non sufficiente
- Classificazione dei canali per funzione: Brand Search e Retargeting = harvest, PMax = black box, TikTok = non scalabile, Meta = solo su creatività controllate
- Analisi retention/post-acquisto: repeat rate, tempi di consegna, resi, ticket, NPS letti insieme, per dimostrare che la perdita clienti non si risolve solo con nuovo traffico
- Allocazione vincolata: i 120k distribuiti tra post-acquisto, corriere, media controllato, sprint creativo/agenzia
- Cap operativi: TikTok escluso dallo scaling, Retargeting e Brand Search sotto cap, PMax limitato a test controllato
- Separazione calcolo/ipotesi: la previsione a 90 giorni distinta tra dati storici solidi e ipotesi gestionali

**Cosa il modello ha sbagliato o inventato**
- Ha dovuto stimare costi di interventi non nel dataset (corriere, customer care, audit agenzia, sprint creativo): allocazioni manageriali plausibili, non valori da consuntivi
- Ha stimato range di ricavi incrementali a 90 giorni, ma il dataset non permetteva di calcolare con precisione il recupero di repeat rate da un miglioramento del post-acquisto: correlazione, non esperimento causale
- Ha rischiato di rendere lo scenario scelto troppo "equilibrato": il punto non era dividere equamente il budget, ma scegliere dove intervenire sul collo di bottiglia
- Ha trattato il cambio agenzia come scelta non immediata: valutazione operativa difendibile, ma non dimostrata dai dati (che indicavano problemi di canali/creative/attribuzione, non di agenzia)
- Prima presentazione: rischio che sembrasse ancora una riallocazione adv invece di centrare corriere, servizio clienti, retention, coerenza di brand

**L'insight più importante della sessione**
Quando il problema è la retention, il budget non va dove il ROAS sembra più alto, ma dove si chiude la perdita che rende inutile continuare ad acquisire.

---

## [2026-06-23] S3 | SINTESI DOCENTE | connessioni tra i team

> Nota: cross-examination dal vivo (docente nei panni di Luca e Chiara). 2 team.

**La connessione più forte: due metodi indipendenti convergono sullo stesso numero.**
Team A è arrivato al rendimento marginale per canale via calcolo in codice; Team B via scenari qualitativi vincolati dalle mail di Luca e Chiara. Confrontati live, i due piani si sono rivelati quasi identici: circa **65-72k€ su esperienza/post-acquisto** (corriere, resi, customer care) e **40-48k€ su media controllato**, contro un riferimento del docente di 80/40. Strade diverse, stessa conclusione — il modello economico del secchio rotto non è un'opinione, è una conseguenza dei numeri.

**La cross-examination dal vivo ha fatto emergere il movimento più importante della serata, indipendentemente nei due team.**
Sfidato in diretta — *"dopo 90 giorni che cosa stiamo ridando a Luca?"* — Team A ha dovuto rendere esplicito ciò che il loro stesso scenario implicava ma non dicevano: i 120.000€ non tornano come ricavo nel trimestre. Quello che si restituisce a Luca è uno **spostamento di KPI** — le metriche rotte (repeat rate, NPS, tempi di consegna) che ricominciano a risalire — non un numero di fatturato. Team B aveva scritto la stessa cosa, indipendentemente, come messaggio finale del proprio scenario: *"non promettiamo che i 120k tornino interamente in 90 giorni. Promettiamo di smettere di spenderli dove il dato dice che il prossimo euro rende meno."* Stesso movimento, due voci: l'allocazione onesta non vende un ritorno, vende la fine dello spreco.

**Il principio del corso ha tenuto anche qui.**
*"I 120.000€ che il CEO dà non diventano 121.000 — sono un investimento, e i KPI rotti che risalgono sono il segnale che la strada è quella giusta."* È lo stesso First-instinct-is-wrong delle altre sessioni, spostato sul budget: il primo istinto del modello è presentare un ritorno calcolato; il lavoro vero è dire dove il calcolo finisce e dove comincia la fiducia nella direzione.

**Il filo dei quattro tipi continua a tenere.**
S1 non fidarti del primo dato → S2 inquadra per chi riceve → S3 prevedi onesto, dichiara dove il calcolo diventa ipotesi, e l'allocazione resta una scelta umana, non un output del modello → S4 (visto in anticipo) automatizza la fatica, tieni il giudizio.

---


## S4 - Automazioni e agenti per Giada

## [2026-06-25] S4 | TEAM A | ANGOLO: progettare partendo dal fallimento (role-play + red-team)

**Messaggio principale trovato**
Il test giusto di un agente non è se funziona quando lo guardi, ma scoprire dove sbaglia quando NON lo guardi: facendolo recitare e osservando dove mente in silenzio, HITL e Guardrail si scrivono quasi da soli — la fiducia si progetta a partire dal fallimento, non dal successo.

**Prompt che hanno funzionato**
- "Recita l'aiutante [X] su un caso concreto: produci l'output reale che genereresti, poi auto-criticati spietato. Dove sbagli IN SILENZIO per giorni senza che [utente] se ne accorga? Da quel fallimento deriva HITL e il guardrail." — ⭐5 — trasforma HITL e guardrail da invenzioni plausibili a cose derivate da un fallimento osservato; è il metodo del brief, eseguito davvero invece che descritto
- "Sei [utente scettico]: attacca questo design con le TUE paure precise ([paura A], [paura B]). Di' se sopravvive così o cosa aggiungere perché tu ti fidi." — ⭐5 — le paure specifiche fanno cadere i design fragili prima della plenaria; un "critica genericamente" non avrebbe trovato l'Errore silenzioso
- "Per ogni pezzo del flusso: richiede giudizio o è una ricetta? Se è una ricetta, fanne un'automazione (più affidabile, più economica). L'agente solo dove serve capire e scegliere tra sfumature." — ⭐5 — tiene l'AI all'ultimo miglio e impedisce di gonfiare tutto ad agente
- "Per ogni aiutante: [role-play] e [red-team persona] in parallelo, poi sintesi, poi un critico che confronta il risultato contro il brief E i vincoli ed elenca SOLO i gap." — ⭐4 — il critico ha trovato gap reali: campi mancanti, gergo non spiegato, una soglia messa come numero magico
- "Non spiegare a parole cosa fa l'agente: simulalo passo per passo con gli artefatti veri (la card Slack, la tabella), e fermati dove decide l'umano." — ⭐4 — lo stop automatico sul punto HITL diventa la dimostrazione della tesi

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- "Inventa un modo per testare gli agenti" → ha proposto un backtest su dati storici, plausibile ma non il metodo prescritto (far recitare l'aiutante a un LLM) → rileggere il brief e usare il metodo prescritto, oltretutto migliore perché genera HITL e guardrail invece di solo validarli
- Default verso "agente / misto" → tendenza a etichettare ogni cosa come agente → Sentinella = automazione, con un solo velo di agente per scrivere l'anomalia in linguaggio umano, dichiarato esplicitamente
- Tipografia nel simulatore (accenti mancanti, em-dash nelle intestazioni) → passaggio dedicato di pulizia, verificato sul testo renderizzato
- Bug di rendering colto solo dalla verifica visiva: barre con `transform: scaleX` su uno span `display:inline` — il DOM riportava "rosso, 68%" ma a schermo le barre erano vuote → animazione su `width` e `display:block`

**Best practice scoperte**
- Per progettare un agente, fallo prima recitare su un caso concreto e chiedigli l'auto-audit dei fallimenti silenziosi: il punto dove mente senza farsi accorgere è dove vanno HITL e guardrail
- Decidi "ricetta o giudizio" PRIMA di scegliere lo strumento: dove basta una soglia, un'automazione è più affidabile ed economica
- Per convincere uno scettico, dagli voce come agente avversario con le sue paure esatte
- Per spiegare un sistema, simulalo con artefatti reali invece di descriverlo, e fallo fermare sul punto in cui decide l'umano: la pausa è il messaggio
- Verifica le UI nel browser, non solo nel DOM, e fai un passaggio tipografico dedicato

**Metodi di analisi applicati**
- Role-play dell'agente (prova del nove): far recitare ogni aiutante su un caso reale e osservare dove diventa inaffidabile, per derivare HITL e guardrail dal fallimento
- Classificazione automazione / agente / misto tramite "giudizio o ricetta"
- Mappatura HITL a partire dal fallimento più pericoloso del flusso
- Guardrail dedotto dal peggior fallimento silenzioso
- Red-team con persona-stakeholder (le due paure di Giada + la linea di Chiara)
- Critico di conformità contro brief e nota
- Difese contro l'errore silenzioso: heartbeat esterno (se l'agente tace, avvisa un altro), riconciliazione col gestionale, trend dello scarto invece del singolo giorno, ricontrollo a posteriori delle scelte

**Cosa il modello ha sbagliato o inventato**
- Ha inventato il metodo di test (backtest su storico) invece di leggere quello prescritto dal brief
- Ha tirato verso "agente" per default, contro la regola "non chiamare agente una regola"
- Ha ignorato vincoli tipografici già dichiarati finché non corretto
- Bug tecnico mascherato da DOM corretto: solo la verifica visiva l'ha trovato
- Tendenza a sovra-progettare: l'agente che fa tutto, la Sentinella che fa partire gli altri a cascata. La disciplina del NON aggiungere è venuta dal brief e dall'umano, non dal modello

**L'insight più importante della sessione**
La fiducia si progetta a partire dal fallimento, non dal successo: facendo recitare l'agente e osservando dove mente in silenzio, HITL e guardrail si scrivono quasi da soli.

---

## [2026-06-25] S4 | TEAM B | ANGOLO: progettare partendo dall'output (e l'Orchestratore)

**Messaggio principale trovato**
Una squadra digitale utile non è fatta da agenti più autonomi, ma da flussi più affidabili: pochi output, un solo punto di attenzione, decisioni lasciate all'umano.

**Prompt che hanno funzionato**
- "Progettate la squadra digitale: aiutanti, automazioni e agenti che tolgono il ripetitivo e sorvegliano dove [utente] non può guardare sempre, lasciandole il giudizio. Non costruite niente di funzionante: progettate le logiche." — ⭐5 — blocca subito il livello corretto: progettazione logica, non implementazione tecnica
- "Specificami quali sono gli output dei vari agenti e automazioni e in che modo arrivano a [utente]." — ⭐5 — sposta la progettazione da "cosa fa l'aiutante" a "cosa riceve l'utente": Slack alert, Sheet, Doc, memo, digest
- "Questo [output ricorrente] non è anche lui un agente o un'automazione da progettare?" — ⭐5 — individua una lacuna architetturale: un output che coordina più flussi non è un formato di consegna, è un componente
- "Allego i file del brief: usali come vincolo progettuale." — ⭐4 — niente agenti generici, ma aiutanti costruiti sui problemi reali dell'utente
- "Metti [il Digest] come caposquadra operativo, ma unisci le slide di ogni aiutante in una sola, con carattere più grande." — ⭐5 — corregge insieme contenuto (Digest come elemento architetturale) e forma (una slide per aiutante, leggibile)

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- Prima squadra digitale → il Digest era trattato come output trasversale, non come componente → promosso a "caposquadra operativo", automazione di orchestrazione che raccoglie gli output degli altri e consegna un solo punto di attenzione
- Output frammentati su troppi canali → regola "push, non dashboard": gli output arrivano in Slack/Doc/Sheet, ma il punto d'accesso quotidiano resta il Digest
- Prima PowerPoint troppo densa (corpo testo piccolo) → font più grande; ma la seconda versione frammentava troppo → struttura ibrida (font grande + una slide per aiutante)
- Classificazione del Digest non esplicitata → definito automazione di orchestrazione: può usare un LLM per rendere leggibile la sintesi, ma non interpreta liberamente e non decide

**Best practice scoperte**
- Chiedi sempre "cosa riceve l'utente, e dove?": senza, il modello descrive funzioni astratte, non flussi usabili
- Separa automazione e agente per tipo di lavoro: soglie e regole → automazione; interpretazione e adattamento del linguaggio → agente
- Ogni aiutante un guardrail esplicito; se non sai dire cosa non deve mai fare, il flusso è ancora troppo vago
- Non moltiplicare i punti di controllo: con cinque aiutanti serve un livello di regia che raccolga tutto (il Digest è il vero anti-dashboard)
- In revisione, distingui problema di contenuto da problema di leggibilità: alzare il font può richiedere una nuova architettura delle slide, non solo un ridimensionamento

**Metodi di analisi applicati**
- Mappatura della giornata di Giada (i punti di sofferenza: spesa, tracking, reporting, creative, decisioni media)
- Classificazione ricetta / giudizio per ogni compito
- Disegno HITL: dove resta l'utente (approvazione, scelta, validazione, invio)
- Definizione dei guardrail (non cambiare budget, non inviare report, non pubblicare creative, non correggere campagne live senza approvazione)
- Progettazione degli output in formati concreti (Slack alert/DM, Sheet, Doc, memo, digest)
- Prioritizzazione per affidabilità e impatto: prima le automazioni a regole, poi gli agenti interpretativi
- Orchestrazione tramite Digest: caposquadra che raccoglie gli output, elimina il rumore, ordina per priorità, consegna una sintesi giornaliera
- Design per destinatari diversi: il Reporter produce una lettura numerica per Luca e una di coerenza brand per Chiara

**Cosa il modello ha sbagliato o inventato**
- Ha trattato il Digest come semplice output trasversale, non come componente da progettare: errore architetturale, perché il Digest risponde al vincolo più importante di Giada (non aggiungere dashboard)
- Prima presentazione troppo densa, poi troppo frammentata: ha richiesto una correzione strutturale, non solo grafica
- Ha descritto alcuni agenti più intelligenti del necessario: il Planner Decisioni Media deve preparare opzioni, non consigliare una riallocazione come scelta autonoma
- Ha confuso output e componente: un output ricorrente che coordina più flussi, con logiche/frequenza/priorità/guardrail/canale, è un aiutante da progettare
- Ha ipotizzato uno stack (n8n, Slack, Sheets, Docs, Gmail, connettori Ads, LLM) plausibile per il disegno logico ma non verificato come stack realmente disponibile in azienda

**L'insight più importante della sessione**
Pochi output, un solo punto di attenzione, decisioni lasciate all'umano: l'affidabilità batte l'autonomia.

---

## [2026-06-25] S4 | SINTESI DOCENTE | connessioni tra i team

> Nota: cross-examination dal vivo (docente nei panni del prof e di Giada scettica). 2 team, e i 5 livelli previsti compressi a 3 dal vivo (monitoraggio, reporting, creatività) per far stare il confronto in plenaria.

**La connessione più importante: due strade opposte, stesso meta-insight.**
Team A è arrivato alla disciplina dal lato del **fallimento**: fai recitare l'agente, trova dove mente in silenzio, e da lì derivi HITL e guardrail (la fiducia si progetta a partire da dove si rompe). Team B ci è arrivato dal lato della **consegna**: cosa riceve Giada e dove → pochi output, un Digest/orchestratore come unico punto di attenzione (push, non dashboard). Due rotte, una sola conclusione: una squadra utile è fatta di **flussi affidabili + un punto di attenzione + giudizio umano**, non di agenti più autonomi.

**La cross-examination dal vivo ha confermato le due trappole.**
- *La linea automazione/agente è sottile, e si sbaglia per difetto.* La "Sentinella", presentata come automazione, è stata sfidata in diretta: *"come fa un'automazione a mandare un messaggio spiegato sui tre canali senza un LLM?"*. Il team ha ammesso che serve un velo di agente anche solo per scrivere il messaggio in linguaggio umano. È lo specchio della trappola anti-hype: non solo "non chiamare agente una regola", ma anche "un'automazione che deve scrivere in linguaggio umano ha già un velo di agente — dichiaralo".
- *Con tanti agenti serve un orchestratore sopra, non più dashboard.* L'orchestratore/Digest di Team B è stato elevato in diretta a risposta strutturale alla paura numero uno di Giada: un caposquadra che sorveglia tutti gli aiutanti, segnala problemi o dà un voto, e consegna un solo report. Esattamente l'anti-dashboard.

**Il principio che chiude l'arco ha tenuto dal vivo.**
*"Non esiste un agente che decide: gli aiutanti fanno chiarezza, Giada analizza a fondo e decide."* Il giudizio resta umano — è la stessa disciplina di S3 (l'allocazione è una scelta umana) trasportata nell'agentico: l'agente prepara, l'umano decide.

**Il filo dei quattro tipi si chiude.**
S1 non fidarti del primo dato → S2 inquadra per l'umano che riceve → S3 prevedi onesto e sappi dove indovini → S4 automatizza la fatica, tieni il giudizio. E l'orchestratore di Team B è letteralmente l'agente che "anticipa": sorveglia se tutto funziona e avvisa, mentre Giada lavora su altro.

---

*Ultimo aggiornamento: — · Mantenuta da Riccardo Sozzi · Format entry: `## [DATA] S[N] | [TEAM] |`*



# Fonti


## BigQuery ML - ARIMA_PLUS

**Cos'è.** Un modello di forecasting di serie storiche dentro BigQuery, addestrabile in puro SQL (`CREATE MODEL ... OPTIONS(MODEL_TYPE='ARIMA_PLUS', HORIZON=90)`).

**Cosa fa.** Gestisce automaticamente trend, stagionalità, festività e anomalie, con selezione automatica del modello (auto.ARIMA). Le previsioni si leggono con `ML.FORECAST` (con orizzonte e intervallo di confidenza). È univariato; la variante `ARIMA_PLUS_XREG` aggiunge regressori esterni (multivariato). La più recente `AI.FORECAST` usa il modello fondazionale TimesFM senza addestrare nulla. Scala fino a milioni di serie.

**Perché è qui.** È il modo "in-warehouse" di fare le previsioni di ricavo/domanda che in S3 trattiamo concettualmente — niente Python, solo SQL sul dato già in BigQuery.


## GA4 - metriche predittive

**Cosa sono.** Tre metriche di machine learning calcolate da GA4 sui dati di prima parte, senza cookie di terza parte:
- **Purchase probability** — probabilità che un utente attivo acquisti nei prossimi 7 giorni.
- **Churn probability** — probabilità che un utente attivo non torni nei prossimi 7 giorni.
- **Predicted revenue** — ricavo atteso nei prossimi 28 giorni dagli utenti attivi.

**A cosa servono.** Alimentano le *predictive audience* (es. "probabili acquirenti a 7 giorni", "probabili top spender a 28 giorni"), esportabili verso Google Ads e DV360 per il retargeting.

**Prerequisiti (rigidi).** Evento purchase con value e currency; nelle ultime 4 settimane, su una finestra di 7 giorni, almeno 1.000 utenti di ritorno che hanno innescato la condizione e almeno 1.000 che non l'hanno fatta; qualità del modello sostenuta nel tempo. Sotto soglia, GA4 smette di aggiornarle.

**Perché è qui.** È l'entry-level dell'analisi predittiva citato in aula — vedi Le tre prediction da non confondere e pLTV in una formula.


## HITL - human-in-the-loop

**Cos'è.** Un pattern di progettazione che inserisce il giudizio umano in punti critici di un flusso altrimenti automatico — vedi la nota-concetto HITL (human-in-the-loop).

**I tre pattern di approvazione.**
- *Pre-azione* — per azioni irreversibili: l'agente si ferma e aspetta l'ok prima di agire.
- *Post-azione* — per azioni reversibili ad alto volume: si agisce, l'umano rivede dopo.
- *Confidence-based* — si coinvolge l'umano solo quando la confidenza scende sotto una soglia.

**Il principio.** L'obiettivo non è la massima automazione né la massima sorveglianza, ma l'**automazione calibrata**: le azioni giuste procedono da sole, quelle giuste ricevono il giudizio umano. Un handoff tempestivo è segno di un sistema robusto, non di un fallimento — e ogni decisione del revisore diventa dato per ricalibrare. Implementato in framework come LangGraph, OpenAI Agents SDK, Microsoft Agent Framework, Mastra.

**Perché è qui.** È il backing di HITL (human-in-the-loop), Guardrail ed Errore silenzioso di S4.


## Karpathy - l'LLM come sistema operativo

**L'idea.** Andrej Karpathy propone l'analogia: l'LLM è un nuovo tipo di **sistema operativo**. I pesi del modello sono la CPU; la finestra di contesto è la **RAM** (limitata, volatile, costosa); gli strumenti sono le periferiche; il retrieval e i file sono il disco; l'agente è l'Orchestratore. Programmare in linguaggio naturale è il "Software 3.0".

**La conseguenza pratica.** Il *context engineering* è la disciplina di decidere cosa entra nella RAM e quando. È esattamente la ragione d'essere di questa wiki: la sorgente atomica è il "disco", e il file compilato (`compile.py` → `FILO_WIKI_COMPILED.md`) è ciò che si carica nella RAM dell'LLM quando serve tutto il contesto in un colpo.

**Perché è qui.** È il fondamento concettuale del pattern wiki-single-file e del design vault → compilazione adottato qui.


## Meridian - MMM open source di Google

**Cos'è.** Il Marketing Mix Model open source di Google, scritto in Python, basato su inferenza causale bayesiana. Annunciato a marzo 2024 e reso disponibile a tutti tra gennaio e febbraio 2025; sostituisce il vecchio LightweightMMM.

**Cosa fa.** Stima l'impatto incrementale dei canali (online e offline) modellando adstock e rendimenti decrescenti — cioè le curve di saturazione. Si calibra con i risultati di esperimenti di incrementalità usati come *prior*, e può usare il volume di query Google come variabile di controllo. Produce ottimizzazione del budget e scenario planning. Da febbraio 2026 ha uno *Scenario Planner* no-code che non richiede Python.

**Limiti.** Lavora a livello di canale, non di campagna; richiede un data scientist, una GPU e 2-3 anni di dati puliti. Trasparente ma non plug-and-play.

**Perché è qui.** È il riferimento serio per Non è un MMM e per La saturazione: il modello statistico che fa davvero quello che in aula approssimiamo a parole.


## Performance Planner - Google Ads

**Cos'è.** Lo strumento di forecast di Google Ads: modella come cambiamenti di budget e bid impattano clic, conversioni, CPA e ROAS.

**Come funziona.** Simula le aste rilevanti degli ultimi 7-10 giorni considerando miliardi di query, stagionalità, attività dei competitor e landing page; aggiorna circa ogni 24 ore e usa il machine learning per tarare i forecast, misurandone l'accuratezza a 1/7/30/90 giorni. Può proporre budget 0 per le campagne inefficienti.

**Limiti (il punto in aula).** Lavora **una campagna alla volta** e non modella gli effetti incrociati tra campagne; l'accuratezza cala sugli orizzonti lunghi e servono ~30 giorni di storico. È una *black box*: ragiona solo sui dati di Google Ads, non sul dato complessivo — i conti veri li fai tu. Vedi La budget simulation di Google come black box e Le variabili di un simulatore di allocazione.


## Robyn - MMM open source di Meta

**Cos'è.** Il Marketing Mix Model open source e semi-automatico di Meta, scritto in R.

**Cosa fa.** Usa la *ridge regression* per gestire la multicollinearità, gli algoritmi evolutivi di Nevergrad per l'ottimizzazione degli iperparametri, Prophet per la scomposizione delle serie storiche e l'ottimizzazione gradient-based per l'allocazione del budget. Stima adstock e curve di saturazione; si calibra con lift test ed esperimenti geo.

**Differenza con Meridian.** Robyn non è bayesiano e lavora a livello nazionale; Meridian è bayesiano e supporta il modeling geo-gerarchico. Due strade allo stesso fine.

**Perché è qui.** Seconda gamba di Non è un MMM: mostra che l'MMM moderno è un campo vivo, non una reliquia anni '70.
