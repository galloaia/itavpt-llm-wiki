---
title: S3 - Allocazione budget e analisi prescrittiva
type: sessione
status: completa
tags: [sessione]
session: S3
---

## [2026-06-23] S3 | TEAM A | ANGOLO: rendimento marginale ([[La saturazione|saturazione]]) + red team degli stakeholder

**Messaggio principale trovato**
Un modello genera dieci scenari plausibili in un minuto — ed è l'opposto di una previsione. Il valore non è esplorare più opzioni: è scegliere UNA, ripararci il modello economico rotto, e dire onestamente dove finisce il dato e comincia l'ipotesi.

**Prompt che hanno funzionato**
- "Calcola in codice il rendimento marginale per canale (Δconversioni ÷ Δspesa) e l'economia della retention. Usa SOLO questi numeri verificati, non stimare a memoria." — ⭐5 — l'LLM da solo confonde saturazione e ROAS medio; ancorarlo al marginale calcolato in codice tiene la diagnosi onesta
- "Per ogni canale dimmi se l'euro che sto per spendere rende ancora come i primi, o già meno. Voglio il ritorno sul PROSSIMO euro, non il ROAS medio." — ⭐5 — sblocca la verità che un canale può avere ottimo ritorno medio e pessimo ritorno marginale (harvest ROAS 9 ma [[Efficienza vs incrementalità|incrementalità]] zero)
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
- Allocazione dei 120k tra adv/post-vendita/corriere/agenzia/mix canali → stima economica necessariamente parziale (costi di corriere, customer care, audit agenzia non nel [[Dataset Filo|dataset]]) → esplicitare dove la previsione smette di essere calcolo e diventa ipotesi gestionale
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
- Distinzione ROAS piattaforma vs ROAS backend: il divario crescente rende il [[ROAS di piattaforma vs valore reale|ROAS dichiarato]] una metrica non sufficiente
- Classificazione dei canali per funzione: [[Brand search ad alto ROAS|Brand Search]] e Retargeting = harvest, [[PMax è una black box|PMax]] = [[La budget simulation di Google come black box|black box]], TikTok = non scalabile, Meta = solo su creatività controllate
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

> Nota: cross-examination dal vivo (docente nei panni di [[Luca Bellini|Luca]] e [[Chiara Donadoni|Chiara]]). 2 team.

**La connessione più forte: due metodi indipendenti convergono sullo stesso numero.**
Team A è arrivato al rendimento marginale per canale via calcolo in codice; Team B via scenari qualitativi vincolati dalle mail di Luca e Chiara. Confrontati live, i due piani si sono rivelati quasi identici: circa **65-72k€ su esperienza/post-acquisto** (corriere, resi, customer care) e **40-48k€ su media controllato**, contro un riferimento del docente di 80/40. Strade diverse, stessa conclusione — il modello economico del secchio rotto non è un'opinione, è una conseguenza dei numeri.

**La cross-examination dal vivo ha fatto emergere il movimento più importante della serata, indipendentemente nei due team.**
Sfidato in diretta — *"dopo 90 giorni che cosa stiamo ridando a Luca?"* — Team A ha dovuto rendere esplicito ciò che il loro stesso scenario implicava ma non dicevano: i 120.000€ non tornano come ricavo nel trimestre. Quello che si restituisce a Luca è uno **spostamento di KPI** — le metriche rotte (repeat rate, NPS, tempi di consegna) che ricominciano a risalire — non un numero di fatturato. Team B aveva scritto la stessa cosa, indipendentemente, come messaggio finale del proprio scenario: *"non promettiamo che i 120k tornino interamente in 90 giorni. Promettiamo di smettere di spenderli dove il dato dice che il prossimo euro rende meno."* Stesso movimento, due voci: l'allocazione onesta non vende un ritorno, vende la fine dello spreco.

**Il principio del corso ha tenuto anche qui.**
*"I 120.000€ che il CEO dà non diventano 121.000 — sono un investimento, e i KPI rotti che risalgono sono il segnale che la strada è quella giusta."* È lo stesso [[First-instinct-is-wrong]] delle altre sessioni, spostato sul budget: il primo istinto del modello è presentare un ritorno calcolato; il lavoro vero è dire dove il calcolo finisce e dove comincia la fiducia nella direzione.

**Il filo dei quattro tipi continua a tenere.**
S1 non fidarti del primo dato → S2 inquadra per chi riceve → S3 prevedi onesto, dichiara dove il calcolo diventa ipotesi, e l'allocazione resta una scelta umana, non un output del modello → S4 (visto in anticipo) automatizza la fatica, tieni il giudizio.

---
