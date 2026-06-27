---
title: S1 - Analisi descrittiva e diagnostica
type: sessione
status: completa
tags: [sessione]
session: S1
---

## [2026-06-16] S1 | TEAM A | ANGOLO: performance e attribuzione

**Messaggio principale trovato**
Il canale più redditizio di Filo non era in nessuna piattaforma — era il cliente che torna; lo si trova solo smettendo di fidarsi del [[ROAS di piattaforma vs valore reale|ROAS dichiarato]] e confrontando tre misurazioni indipendenti della stessa vendita.

**Prompt che hanno funzionato**
- "Pulisci [DATASET]. Elenca OGNI anomalia (outlier, mancanti, duplicati, nomenclatura, date). Per ognuna scrivi come l'hai corretta. Non imputare senza segnalarlo." — ⭐5 — ha forzato 12 anomalie a galla invece di analizzarci sopra
- "Questi sono i numeri verificati in codice: [TABELLA]. Leggi il CSV per il dettaglio ma NON ricalcolare a memoria. Usa solo questi valori come ancore." — ⭐5 — separa calcolo deterministico da interpretazione, elimina metriche allucinate
- "Sei un red team ostile esperto di analytics. DEMOLISCI questo claim: [CLAIM] con evidenza [NUMERI]. Cerca correlazione-per-causalità, variabili confondenti, over-claim. Se regge dillo, se no riformula in modo non attaccabile." — ⭐5 — il pattern singolo più utile della sessione
- "Non classificare le campagne per canale. Classificale per FUNZIONE: domanda nuova (prospecting) vs domanda esistente (brand/retargeting). Calcola quota budget vs quota ricavi per gruppo." — ⭐4 — ha reso visibile che il 12% del budget (harvest) si prendeva il 36% dei ricavi
- "Analizza da [N] angoli indipendenti in parallelo. Ogni lente restituisce: titolo, evidenza, interpretazione, forza, ATTACCABILITÀ. Schema: [JSON]." — ⭐4 — il campo "attaccabilità" forzato nello schema alza la qualità e riduce la retorica

**Prompt che non hanno funzionato (o hanno richiesto correzioni)**
- Analisi su [[Dataset Filo|dataset]] parziale (solo foglio campagne) → diagnosi plausibile ma di livello sbagliato (media mix invece di retention) → corretto recuperando tutti i 6 fogli: la causa radice è cambiata
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
- Confronto 2024 vs 2025 per canale/campagna su ROAS, CPA, CPC, [[CPM e CTR bassi non bastano|CTR]]
- Bucketing per funzione (harvest/mid/create/vanity): quota budget vs quota ricavi
- Triangolazione: ricavi piattaforma vs [[GA4 è un campione, non la verità|GA4]] vs backend — rapporto piattaforma/backend cresciuto da 1,0x a 2,8x
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
Una correlazione temporale netta e ben visualizzabile tende a "mangiarsi" visivamente e narrativamente un problema più lento e meno fotogenico che la precede — il vero lavoro analitico non è trovare la causa più [[Chiara Donadoni|chiara]], ma misurare quanto della variazione totale quella causa spiega davvero prima di darle il titolo della slide.

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

**Il pattern "[[First-instinct-is-wrong]]" si è ripetuto identico in tutti e tre i team — e in tre forme diverse:**
- A: la prima sintesi diceva "le piattaforme mentono" — poi corretta in sovra-attribuzione strutturale (metà del gap è modello di attribuzione, non frode)
- B: la prima sintesi attribuiva il crollo retention al corriere in modo netto — poi corretta quantificando che spiega solo l'ultimo terzo
- C: la prima lettura visuale (CR-002 "macro tessuto") era dedotta dai metadati senza guardare l'immagine reale — corretta dopo verifica visuale

In tutti e tre i casi l'errore non è stato un'allucinazione di numeri (i tre team lo segnalano esplicitamente: nessun numero inventato), ma un eccesso di sicurezza nella prima narrazione — risolto solo da un secondo passaggio esplicito di verifica/quantificazione. **Lezione trasversale per la wiki: la prima sintesi di un LLM è quasi sempre più netta di quanto i dati supportino. Il passaggio che la corregge va richiesto esplicitamente, non sperato.**

**Sul ROAS: A e C arrivano alla stessa diffidenza per ragioni complementari.**
A smonta il ROAS aggregato di piattaforma (sovra-attribuzione strutturale, finestre di attribuzione, sistemi non integrati). C smonta il ROAS per creatività (CR-005 sconto: CTR alto, ma è quello che A chiamerebbe "harvest" — domanda catturata non creata). Se si uniscono i due angoli: il ROAS è gonfiato sia a livello di canale sia a livello di creative, e per la stessa ragione di fondo — si misura quello che è facile attribuire, non quello che è incrementale.

**Quello che nessun team ha potuto vedere da solo:** il quadro completo richiede A (dove sembra andare bene ma non è incrementale), B (perché il cliente non torna, e da quando), e C (cosa nelle creative comunica valore vs cosa compra solo attenzione). Nessuno dei tre, isolato, arriva alla diagnosi: "stiamo spendendo di più su un mix che premia l'harvest non il prospecting, su creative che a volte vendono sconto invece che il prodotto, mentre il vero collo di bottiglia — il cliente che non torna — peggiora da più tempo di quanto chiunque pensi e non è riconducibile a un solo evento."

---
