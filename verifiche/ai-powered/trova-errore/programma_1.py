"""Calcola il prezzo più alto di uno scontrino.

Scritto da un'IA. Contiene un errore: trovalo, scrivi l'input che lo dimostra,
correggilo e spiega perché l'IA potrebbe averlo commesso.
"""


def prezzo_massimo(prezzi):
    """Restituisce il prezzo più alto dello scontrino."""
    massimo = 0
    for prezzo in prezzi:
        if prezzo > massimo:
            massimo = prezzo
    return massimo


if __name__ == "__main__":
    print(prezzo_massimo([12, 45, 7, 30]))
