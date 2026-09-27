"""Funzioni sugli scontrini del negozio (UdA demo Lab6: liste e cicli in Python).

Specifica chiarita nell'Incontro 1:
- i prezzi degli articoli sono al netto dell'IVA;
- l'IVA è del 22%;
- se il totale con IVA supera 50 euro si applica uno sconto del 10% sul totale con IVA;
- il risultato è arrotondato ai centesimi.

Il codice usa solo i costrutti visti in classe: variabili, liste, cicli for,
if, funzioni con return. Niente sum(), max(), list comprehension.
"""

IVA = 0.22
SOGLIA_SCONTO = 50
SCONTO = 0.10


def totale_scontrino(prezzi):
    """Restituisce il totale da pagare (IVA inclusa, eventuale sconto), arrotondato ai centesimi."""
    totale = 0
    for prezzo in prezzi:
        totale = totale + prezzo
    totale = totale * (1 + IVA)
    if totale > SOGLIA_SCONTO:
        totale = totale - totale * SCONTO
    return round(totale, 2)


def prezzo_massimo(prezzi):
    """Restituisce il prezzo più alto della lista, oppure None se la lista è vuota."""
    if len(prezzi) == 0:
        return None
    massimo = prezzi[0]
    for prezzo in prezzi:
        if prezzo > massimo:
            massimo = prezzo
    return massimo


def conta_sopra_soglia(prezzi, soglia=20):
    """Restituisce quanti articoli costano più di soglia (esclusa)."""
    conteggio = 0
    for prezzo in prezzi:
        if prezzo > soglia:
            conteggio = conteggio + 1
    return conteggio


def media_prezzi(prezzi):
    """Restituisce la media dei prezzi, arrotondata ai centesimi, oppure None se la lista è vuota."""
    if len(prezzi) == 0:
        return None
    totale = 0
    for prezzo in prezzi:
        totale = totale + prezzo
    return round(totale / len(prezzi), 2)


if __name__ == "__main__":
    scontrino = [10, 20, 15]
    print("Totale da pagare:", totale_scontrino(scontrino))
    print("Prezzo più alto:", prezzo_massimo(scontrino))
    print("Articoli sopra 20 euro:", conta_sopra_soglia(scontrino))
    print("Prezzo medio:", media_prezzi(scontrino))
