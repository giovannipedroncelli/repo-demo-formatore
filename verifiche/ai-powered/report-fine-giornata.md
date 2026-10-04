# Consegna AI-powered — Mini-progetto "Report di fine giornata" (livello 4)

**Classe:** terza. **Tempo:** due settimane, con due ore di laboratorio. **IA:** consentita per generare il codice, con le regole sotto.

## Il problema

Il negozio registra ogni scontrino della giornata come lista di prezzi netti. A fine giornata la titolare vuole sapere:
- quanti scontrini sono stati fatti;
- l'incasso totale della giornata (IVA 22% inclusa, con lo sconto del 10% sugli scontrini che superano 50 € con IVA);
- lo scontrino più alto;
- quanti articoli sono costati più di 20 € (prezzo netto).

Un reso è registrato come prezzo negativo.

## Cosa consegni

1. **La specifica**, controllata con l'allenatore di prompt della classe (Gem "Allenatore di specifiche"): scopo, input, output, vincoli, almeno due casi limite, come verifichi che funziona.
2. **Almeno 5 test** scritti **prima** di generare il codice (file `test_report.py`).
3. **Il prompt log** (`PROMPT_LOG.md`): per ogni richiesta all'IA, cosa hai chiesto, cosa hai accettato, cosa hai cambiato e perché.
4. **Il repository** con almeno 4 commit significativi; i test devono passare su GitHub Actions.
5. **La dichiarazione d'uso dell'IA** (modello nel patto d'aula).

## In classe (5 minuti per studente)

- Spieghi il tuo codice: il docente sceglie due righe e tu dici cosa fanno.
- Prevedi l'output su uno scontrino che ti dà il docente.
- Fai una piccola modifica dal vivo, **senza IA** (per esempio: lo sconto scatta da 60 € invece che da 50 €).

## Rubrica

| Criterio | Peso | Insufficiente | Sufficiente | Buono | Ottimo |
|---|---|---|---|---|---|
| Specifica | 20% | vaga, mancano input o output | input e output chiari, casi limite assenti | casi limite presenti | un'altra persona la implementerebbe senza chiedere nulla |
| Test prima del codice | 20% | assenti o scritti dopo il codice | 5 test solo su casi normali | anche casi limite | coprono tutti i casi limite della specifica, con nomi chiari |
| Spiegazione orale e modifica dal vivo | 40% | non sa spiegare il codice consegnato | spiega con incertezza, modifica con aiuto | spiega e modifica | spiega, prevede e modifica con sicurezza, motiva le scelte |
| Processo: prompt log, commit, PR | 20% | unico commit finale, log assente | log sommario, pochi commit | log completo, commit regolari | percorso leggibile con correzioni motivate |
| Il programma funziona | requisito | se non funziona, all'orale si discute il perché invece di azzerare il punteggio | | | |
