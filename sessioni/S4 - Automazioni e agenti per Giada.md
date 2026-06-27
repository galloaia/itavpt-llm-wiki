---
title: S4 - Automazioni e agenti per [[Giada Ferri|Giada]]
type: sessione
status: completa
tags: [sessione]
session: S4
---

## [2026-06-25] S4 | TEAM A | ANGOLO: progettare partendo dal fallimento (role-play + red-team)

**Messaggio principale trovato**
Il test giusto di un agente non è se funziona quando lo guardi, ma scoprire dove sbaglia quando NON lo guardi: facendolo recitare e osservando dove mente in silenzio, [[HITL (human-in-the-loop)|HITL]] e [[Guardrail]] si scrivono quasi da soli — la fiducia si progetta a partire dal fallimento, non dal successo.

**Prompt che hanno funzionato**
- "Recita l'aiutante [X] su un caso concreto: produci l'output reale che genereresti, poi auto-criticati spietato. Dove sbagli IN SILENZIO per giorni senza che [utente] se ne accorga? Da quel fallimento deriva HITL e il guardrail." — ⭐5 — trasforma HITL e guardrail da invenzioni plausibili a cose derivate da un fallimento osservato; è il metodo del brief, eseguito davvero invece che descritto
- "Sei [utente scettico]: attacca questo design con le TUE paure precise ([paura A], [paura B]). Di' se sopravvive così o cosa aggiungere perché tu ti fidi." — ⭐5 — le paure specifiche fanno cadere i design fragili prima della plenaria; un "critica genericamente" non avrebbe trovato l'[[Errore silenzioso]]
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
- Red-team con persona-stakeholder (le due paure di Giada + la linea di [[Chiara Donadoni|Chiara]])
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

## [2026-06-25] S4 | TEAM B | ANGOLO: progettare partendo dall'output (e l'[[Orchestratore]])

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
- Design per destinatari diversi: il Reporter produce una lettura numerica per [[Luca Bellini|Luca]] e una di coerenza brand per Chiara

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
