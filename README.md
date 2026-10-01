# Liste e cicli in Python: gli scontrini del negozio

Kit didattico dimostrativo del laboratorio **Lab6 — Programmazione e coding guidate dalla AI, approccio responsabile**. È il repository che il formatore costruisce davanti ai corsisti, incontro dopo incontro, con la stessa struttura del loro kit.

**Classe:** terza SIA (o AFM con informatica) · **Durata:** 8 ore · **Prerequisiti:** variabili, `input` e `print`, `if`, funzioni con `return`.

## Obiettivi di apprendimento (osservabili)

Alla fine dell'UdA lo studente sa:
1. prevedere il valore di un accumulatore a ogni giro di un ciclo `for` su una lista;
2. scrivere funzioni che scorrono una lista per calcolare totale, massimo, conteggio e media;
3. individuare e correggere l'errore di uno, l'accumulatore nel posto sbagliato, `print` al posto di `return`;
4. scrivere test che descrivono una specifica, compresi i casi limite (lista vuota, resi negativi, soglia esatta);
5. usare un assistente IA secondo le regole del patto d'aula e spiegare il codice che consegna.

## Misconcezioni affrontate

- accumulatore non inizializzato o reinizializzato dentro il ciclo;
- confusione tra indice ed elemento;
- errore di uno (`range(1, len(prezzi))`);
- `print` al posto di `return`;
- modificare una lista mentre la si scorre;
- ordine delle operazioni tra IVA e sconto (specifica ambigua).

## Sequenza delle lezioni

| Lezione | Attività | Livello IA (0-4) | AI-proof / AI-powered | Materiali e agenti |
|---|---|---|---|---|
| 1 (1h) | Il ciclo `for` sugli scontrini: spiegazione e tracing alla lavagna | 0 | AI-proof | Esercizio PRIMM 1 |
| 2 (1h) | Il tracciatore interattivo, alla LIM e poi individuale | 0 | AI-proof | [Tracciatore del ciclo](artefatti/tracciatore-ciclo.html) |
| 3 (1h) | Studio dei concetti con il tutor | 1 | AI-powered (tutor) | Gem S1 Tutor socratico |
| 4 (1h) | Massimo e conteggio; errori nel proprio codice | 1 | AI-powered (tutor) | Esercizio PRIMM 2; Gem S3 Traduttore di errori |
| 5 (1h) | Trova l'errore dell'IA | 3 | AI-powered (oggetto di studio) | `verifiche/ai-powered/trova-errore/` |
| 6 (1h) | Verifica in classe | 0 | AI-proof | `verifiche/ai-proof/verifica-liste-cicli.md` |
| 7-8 (2h) | Mini-progetto "Report di fine giornata" e orale | 4 | AI-powered, con evidenze | `verifiche/ai-powered/report-fine-giornata.md`; Gem S9 Allenatore di prompt |

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
