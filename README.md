# Dizionari in Python: gestione del magazzino e listino prezzi

Kit didattico dimostrativo del laboratorio **Lab6 — Programmazione e coding guidate dalla AI, approccio responsabile**. È il repository che il formatore costruisce davanti ai corsisti, incontro dopo incontro, con la stessa struttura del loro kit.

**Classe:** terza SIA · **Durata:** 8 ore · **Prerequisiti:** variabili, `input` e `print`, costrutti di selezione (`if-elif-else`), cicli `for` e `while`, liste, funzioni con `return`.

## Obiettivi di apprendimento (osservabili)

Alla fine dell'UdA lo studente sa:
1. modellare dati economico-aziendali (es. anagrafica articoli, listino prezzi, giacenze di magazzino) mediante dizionari Python con tipi di chiavi e valori appropriati;
2. eseguire operazioni di lettura, inserimento, modifica e cancellazione di coppie chiave-valore, gestendo le chiavi inesistenti tramite operatore `in` e metodo `.get()`;
3. iterare su un dizionario utilizzando `.keys()`, `.values()` e `.items()` per estrarre aggregazioni e report (es. valore totale dell'inventario, articoli sottoscorta);
4. manipolare strutture dati combinate elementari (es. lista di dizionari per ordini clienti o dizionario con valori complessi);
5. individuare, isolare e correggere errori tipici di accesso e mutazione (`KeyError`, sovrascrittura accidentale, modifica della dimensione del dizionario durante un ciclo);
6. utilizzare un assistente IA come tutor di supporto e correttore nel rispetto del patto d'aula, documentando i prompt e sapendo spiegare e giustificare ogni riga di codice consegnata.

## Misconcezioni affrontate

- **Confusione tra indice numerico posizionale e chiave**: tentare di accedere a un dizionario con indici sequenziali (`d[0]`) pensando che funzioni come una lista o che le chiavi debbano essere numeriche ordinate;
- **Confusione tra chiave e valore**: tentare di ottenere la chiave passando il valore tra parentesi quadre (`d[valore]`), o cercare corrispondenze nei valori credendo di interrogare le chiavi;
- **`KeyError` inatteso**: dare per scontato che accedere a una chiave assente restituisca `None` o stringa vuota, omettendo l'operatore di appartenenza `in` o il fallback di `.get()`;
- **Sovrascrittura accidentale**: dimenticare che le chiavi sono univoche e che riassegnare `d[k] = nuovo_valore` sovrascrive il dato esistente anziché aggiungerne un duplicato;
- **Mutazione durante l'iterazione**: tentare di eliminare o inserire elementi (`del`, `.pop()`) all'interno di un ciclo che scorre il dizionario (`RuntimeError: dictionary changed size during iteration`);
- **Mancata comprensione dell'unpacking con `.items()`**: non cogliere che `.items()` restituisce una tupla `(chiave, valore)` e tentare di accedere ai valori come attributi o indici errati.

## Sequenza delle lezioni

| Lezione | Attività | Livello IA (0-4) | AI-proof / AI-powered | Materiali e agenti |
|---|---|---|---|---|
| 1 (1h) | Dal foglio di calcolo alla coppia chiave-valore: modellazione del listino prezzi e giacenze. Tracing alla lavagna e lettura guidata (PRIMM - Predict & Run) | 0 | AI-proof | Esercizio PRIMM 1 (Listino & Magazzino) |
| 2 (1h) | Accesso e aggiornamento sicuro: `in`, `.get()` e gestione delle scorte. Esercitazione individuale al calcolatore (PRIMM - Investigate & Modify) | 0 | AI-proof | Scheda laboratorio 1; Tracciatore memoria chiave-valore |
| 3 (1h) | Iterazione su dizionari (`.keys()`, `.values()`, `.items()`): calcolo del valore inventariale e filtro sottoscorta con supporto socratico | 1 | AI-powered (tutor) | Esercizio guidato; Gem S1 Tutor socratico |
| 4 (1h) | Strutture dati combinate: lista di transazioni/scontrini rappresentati come dizionari. Debugging di errori di accesso | 1 | AI-powered (tutor) | Esercizio PRIMM 2; Gem S3 Traduttore di errori |
| 5 (1h) | "Trova l'errore dell'IA": analisi critica di script generati da LLM contenenti allucinazioni, `KeyError` e cancellazioni in ciclo | 3 | AI-powered (oggetto di studio) | `verifiche/ai-powered/trova-errore-dizionari/` |
| 6 (1h) | Verifica sommativa individuale in laboratorio (su carta o ambiente privo di accesso web/IA) | 0 | AI-proof | `verifiche/ai-proof/verifica-dizionari-sia.md` |
| 7-8 (2h) | Mini-progetto a coppie: "Gestione cassa e inventario per una PMI" con documentazione prompt/changelog e colloquio orale di difesa del codice | 4 | AI-powered, con evidenze | `verifiche/ai-powered/progetto-inventario-pmi.md`; Gem S9 Allenatore di prompt |

## Agenti per gli studenti

Istruzioni e collaudo nella cartella [`agenti/`](agenti/). Si creano come Gem in Gemini (account della scuola) e si condividono con la classe tramite Classroom.

## Codice e test

- `scontrini.py`: funzioni di riferimento (totale con IVA e sconto, massimo, conteggio, media), scritte solo con i costrutti visti in classe.
- `verifiche/test/test_scontrini.py`: test della specifica, eseguiti da GitHub Actions a ogni push (`.github/workflows/test.yml`).
- `tre_versioni.py`: le tre consegne "di studenti" dell'Incontro 1.

## Machine learning (Incontro 3)

La cartella [`ml/`](ml/) contiene quattro notebook PRIMM (pandas con i funghi, sei modelli con lo stesso schema, baseline su German Credit, sei errori ML) da aprire in Colab direttamente da GitHub. La consegna AI-powered in versione ML è in `verifiche/ai-powered/notebook-ml.md`.

## Sperimentazione

[`SPERIMENTAZIONE.md`](SPERIMENTAZIONE.md): piano per la prima settimana in classe.

## Uso dell'IA nella preparazione di questo kit

Vedi [`DIARIO_DI_BORDO.md`](DIARIO_DI_BORDO.md): cosa è stato generato con Gemini e Antigravity, cosa è stato verificato e corretto a mano. Tutto il codice è stato eseguito e i test passano.

## Patto d'aula

[`PATTO_IA.md`](PATTO_IA.md)

## Limiti noti

- Il tracciatore simula solo i due programmi previsti (versione A corretta, versione B con l'accumulatore dentro il ciclo).
- I Gem orientano il comportamento dell'IA ma non lo garantiscono: la tenuta sta nella progettazione delle attività e nell'orale.

## Licenze

Codice: MIT (file `LICENSE`). Materiali didattici (testi, esercizi, rubriche): CC BY 4.0.
