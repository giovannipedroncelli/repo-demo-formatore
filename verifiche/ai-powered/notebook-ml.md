# Consegna AI-powered, variante ML — "Il mio primo classificatore" (quinta, livello 4)

**IA:** consentita per generare il codice del notebook (in Colab solo per maggiorenni; altrimenti il Gem della classe in una finestra separata). **Tempo:** una settimana, con due ore di laboratorio.

## Il problema

Scegli uno dei dataset di esercizio della classe (funghi, German Credit, clienti inventati) e costruisci un notebook che risponda a una domanda precisa, scritta da te nella prima cella.

## Cosa consegni

1. **La specifica** (prima cella markdown): domanda, colonna da prevedere, metrica scelta **e perché**, cosa conterà come "risultato buono".
2. **La cella "Da dove vengono questi dati e cosa non possiamo farci".**
3. **Il notebook commentato cella per cella**: sotto ogni cella di codice una cella markdown che dice *cosa fa* e *perché serve*, con parole tue.
4. **Baseline e divisione dei dati motivate**: `DummyClassifier` (o `DummyRegressor`) e `train_test_split` **prima** di qualunque trasformazione appresa dai dati.
5. **Il prompt log** e almeno 3 commit.

## In classe (orale, 5 minuti, senza IA)

Tre domande tra queste:
- Rispetto a quale baseline hai misurato il tuo risultato?
- Su quali dati hai calcolato l'accuratezza? Cosa succederebbe se la calcolassi sul training?
- Cosa succede se togli la colonna che il modello usa di più?
- Spiegami questa riga (il docente ne indica una).
- Cambia il modello con un altro dei sei e dimmi prima cosa ti aspetti.

## Rubrica

| Criterio | Peso | Da … a … |
|---|---|---|
| Specifica e scelta della metrica | 20% | "accuratezza perché sì" → "metrica motivata dal problema (es. recall sui cattivi pagatori)" |
| Baseline e divisione dei dati | 20% | "assenti" → "presenti, prima di ogni trasformazione, motivate" |
| Commenti e scheda dei dati | 20% | "assenti o copiati dall'IA" → "con parole proprie, con i limiti dei dati" |
| Orale | 40% | "non sa spiegare il notebook" → "prevede, spiega e modifica con sicurezza" |
| Il notebook gira dall'inizio alla fine | requisito | se non gira se ne discute il perché all'orale |
