# Esercizio PRIMM 1 — L'accumulatore

## PREDICT
Senza eseguirlo, cosa stampa questo programma?

```python
prezzi = [4, 6, 10]
totale = 0
for prezzo in prezzi:
    totale = totale + prezzo
print(totale)
```

Scrivi qui la tua previsione: ______

## RUN
Esegui il programma (in Thonny o in Colab) e confronta il risultato con la tua previsione. Se sono diversi, prima di andare avanti scrivi in una riga dove pensi di aver sbagliato.

## INVESTIGATE
1. Quante volte viene eseguita la riga 4? Da cosa dipende?
2. Cosa stamperebbe il programma se la lista fosse `[4, 6, 10, 5]`? E se fosse vuota?
3. Perché `totale = 0` è scritto **prima** del `for` e non dentro?

## MODIFY
Modifica il programma perché stampi il totale con l'IVA al 22% (arrotondato ai centesimi).

## MAKE
Scrivi da zero un programma che, data la lista delle quantità vendute in una giornata `quantita = [3, 1, 4, 2]`, stampi il numero totale di pezzi venduti.

---

### Soluzione per il docente
- PREDICT: `20`.
- INVESTIGATE: 1) tre volte, una per ogni elemento della lista; 2) `25`; con la lista vuota `0`; 3) dentro il ciclo il totale verrebbe azzerato a ogni giro e alla fine varrebbe solo l'ultimo prezzo (misconcezione bersaglio).
- MODIFY: dopo il ciclo `totale = round(totale * 1.22, 2)` → stampa `24.4`.
- MAKE: stesso schema con `pezzi = 0` e `pezzi = pezzi + q` → `10`.
