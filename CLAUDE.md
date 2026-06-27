# CLAUDE.md — istruzioni operative per Claude Code

Questo repository è la **wiki Filo Studio** in forma di vault Obsidian: una cartella di note markdown atomiche. La sorgente di verità sono le singole note, NON un file unico.

## Struttura
- `concetti/` — nozioni teoriche atomiche (una per file), incluse le voci di glossario
- `sessioni/` — il diario, una nota per sessione (S1–S4)
- `prompt/` — la libreria prompt, una nota per area d'uso
- `entita/` — brand, dataset, personaggi del caso
- `fonti/` — fonti esterne sintetizzate (Meridian, Robyn, GA4 predittivo, Performance Planner, ARIMA_PLUS, Karpathy, HITL)
- `_meta/` — istruzioni e template

I collegamenti usano la sintassi `[[Titolo nota]]` (wikilink Obsidian).

## Aggiornare dopo una sessione
1. Crea/aggiorna la nota in `sessioni/` seguendo `_meta/Template diario.md`.
2. Generalizza i prompt nuovi nelle note di `prompt/`.
3. Nozioni nuove → note in `concetti/`, collegate con `[[ ]]`.
4. Mantieni il frontmatter (`type`, `status`, `tags`).

## File unico per altri LLM
`python3 compile.py` concatena il vault in `FILO_WIKI_COMPILED.md` (ordine: meta → concetti → entità → prompt → sessioni → fonti). È l'artefatto da incollare in un GPT Knowledge / Gemini Gem; il vault resta la sorgente.
