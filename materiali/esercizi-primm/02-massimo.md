# Esercizio PRIMM 2 — Il prezzo più alto

## PREDICT
Senza eseguirlo, cosa stampa questo programma?

```python
prezzi = [12, 45, 7, 30]
massimo = prezzi[0]
for prezzo in prezzi:
    if prezzo > massimo:
        massimo = prezzo
print(massimo)
```

Scrivi qui la tua previsione: ______

## RUN
Esegui e confronta. Completa questa tabella con il valore di `massimo` alla fine di ogni giro:

| Giro | prezzo | massimo |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

## INVESTIGATE
1. Perché `massimo` parte da `prezzi[0]` e non da `0`? Trova una lista con cui partire da `0` darebbe un risultato sbagliato.
2. Cosa succede se la lista è vuota? Quale riga dà errore, e che errore?
3. Cosa cambia se al posto di `>` scrivi `>=`? Il risultato stampato cambia?

## MODIFY
Modifica il programma perché stampi il prezzo **più basso**.

## MAKE
Scrivi una funzione `scontrino_piu_alto(totali)` che, data la lista dei totali degli scontrini di una giornata, restituisca il più alto; se la lista è vuota deve restituire `None`.

---

### Soluzione per il docente
- PREDICT: `45`. Tabella: (12, 12), (45, 45), (7, 45), (30, 45).
- INVESTIGATE: 1) con prezzi tutti negativi, es. `[-3, -1, -2]`, partire da 0 darebbe 0 invece di -1 (resi); 2) la riga 2, `IndexError: list index out of range`; 3) il valore stampato non cambia.
- MODIFY: `if prezzo < minimo:` con `minimo = prezzi[0]` → `7`.
- MAKE: controllo `if len(totali) == 0: return None` prima dello stesso schema.
