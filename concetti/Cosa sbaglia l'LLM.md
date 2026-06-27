---
title: Cosa sbaglia l'LLM
type: concetto
status: stabile
tags: [concetto, llm]
---

| Rischio | Sintomo | Rimedio |
|---|---|---|
| Errori aritmetici silenziosi | Ti dà un numero di ROAS o CAC con sicurezza assoluta | Sempre [[Code interpreter - quando e come|code interpreter]] per i calcoli |
| Inventare dati mancanti | Riempie i buchi con "stime ragionevoli" non dichiarate | Chiedi esplicitamente: "se il dato non c'è, dimmelo" |
| Conclusioni senza evidenza | "Il canale X non funziona" senza citare un numero | Chiedi sempre l'evidenza specifica prima della conclusione |
| Ottimismo non richiesto | Ti dice che "i risultati sono incoraggianti" anche quando non lo sono | Chiedi: "dimmi cosa c'è che non va, non solo cosa va bene" |
| Confondere correlazione e causalità | "Il ROAS cala quando la spesa sale → la spesa fa calare il ROAS" | Distingui esplicitamente: "questa è una correlazione, non una causa" |
