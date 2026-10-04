# Verifica AI-proof — Liste e cicli (classe terza)

**Modalità:** in classe, senza IA. Su carta, oppure al computer con un editor senza completamento automatico (Thonny o IDLE, estensioni IA disattivate).
**Tempo:** 50 minuti. **Materiale ammesso:** nessuno.

---

## Esercizio 1 — Tracing (10 punti)

```python
prezzi = [8, 25, 12, 30]
totale = 0
cari = 0
for prezzo in prezzi:
    totale = totale + prezzo
    if prezzo > 20:
        cari = cari + 1
print(totale, cari)
```

Completa la tabella con i valori **alla fine** di ogni giro del ciclo, poi scrivi cosa stampa il programma.

| Giro | prezzo | totale | cari |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

Il programma stampa: ______________

---

## Esercizio 2 — Parsons (8 punti)

Riordina le righe (e scegli l'indentazione giusta) per scrivere la funzione `conta_cari(prezzi)` che restituisce quanti prezzi superano i 20 euro. **Attenzione: una riga non serve e va scartata.**

```
return conteggio
if prezzo > 20:
conteggio = 0
def conta_cari(prezzi):
conteggio = conteggio + 1
conteggio = 0
for prezzo in prezzi:
```

Scrivi qui la funzione riordinata:

```




```

Quale riga hai scartato, e cosa succederebbe se la mettessi dentro il ciclo?

---

## Esercizio 3 — Trova e spiega (8 punti)

Uno studente ha scritto questa funzione per il totale di uno scontrino (prezzi netti, IVA 22%, sconto 10% se il totale con IVA supera 50 €):

```python
def totale_scontrino(prezzi):
    totale = 0
    for i in range(1, len(prezzi)):
        totale = totale + prezzi[i]
    totale = totale * 1.22
    if totale > 50:
        totale = totale - totale * 0.1
    return totale
```

a) Qual è l'errore? Indica la riga.
b) Scrivi uno scontrino (una lista di prezzi) con cui l'errore si vede, il risultato che dà la funzione e quello corretto.
c) Correggi la riga sbagliata.

---

## Esercizio 4 — Spiega una riga (4 punti)

Nella versione corretta della funzione dell'esercizio 3, cosa succede se la lista `prezzi` è vuota? Cosa restituisce la funzione, e perché?

---

## Chiave per il docente

**Es. 1:** giri: (8, 8, 0), (25, 33, 1), (12, 45, 1), (30, 75, 2). Stampa `75 2`.
**Es. 2:**
```python
def conta_cari(prezzi):
    conteggio = 0
    for prezzo in prezzi:
        if prezzo > 20:
            conteggio = conteggio + 1
    return conteggio
```
Riga scartata: il secondo `conteggio = 0`. Dentro il ciclo azzererebbe il conteggio a ogni giro: la funzione restituirebbe al massimo 1.
**Es. 3:** a) `range(1, len(prezzi))` salta il primo elemento (indice 0). b) Con `[10, 20, 15]` la funzione restituisce circa 42,70 (arrotondato); il valore corretto è 49,41. Qualunque lista in cui il primo prezzo non sia zero va bene. c) `for i in range(len(prezzi)):` oppure `for prezzo in prezzi:` con `totale = totale + prezzo`.
**Es. 4:** il ciclo non viene eseguito, `totale` resta 0, `0 * 1.22` fa 0, la condizione `0 > 50` è falsa: restituisce 0.

**Punteggio:** 30 punti. Nell'esercizio 3 conta più la spiegazione (b) della correzione (c).
