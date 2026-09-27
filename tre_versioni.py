"""Incontro 1, blocco 2: tre versioni dello stesso compito.

Consegna originale (volutamente ambigua):
  Scrivi una funzione totale_scontrino(prezzi) che riceve la lista dei prezzi
  degli articoli (senza IVA) e restituisce il totale da pagare: aggiungi l'IVA
  al 22% e, se il totale supera 50 euro, applica uno sconto del 10%.

Eseguire con:  python tre_versioni.py
"""


# Studente A: scritto a mano, con un errore di uno
def totale_studente_a(prezzi):
    totale = 0
    for i in range(1, len(prezzi)):
        totale = totale + prezzi[i]
    totale = totale * 1.22
    if totale > 50:
        totale = totale - totale * 0.1
    return totale


# Studente B: generato con un'IA, corretto ma con costrutti mai visti in classe
IVA = 0.22
SOGLIA_SCONTO = 50
SCONTO = 0.10


def totale_studente_b(prezzi: list[float]) -> float:
    """Restituisce il totale ivato, scontato del 10% se supera 50 €."""
    lordo = sum(prezzi) * (1 + IVA)
    if lordo > SOGLIA_SCONTO:
        lordo *= (1 - SCONTO)
    return round(lordo, 2)


# Studente C: generato con un'IA; la spiegazione allegata parla di un ciclo for che non c'è
def totale_studente_c(prezzi):
    totale = sum(prezzi)
    if totale > 50:
        totale = totale * 0.9
    return round(totale * 1.22, 2)


if __name__ == "__main__":
    for scontrino in ([10, 20, 15], [30, 30], [5], [], [40, 2]):
        print(
            f"{str(scontrino):<14}",
            f"A = {totale_studente_a(scontrino)!s:<22}",
            f"B = {totale_studente_b(scontrino)!s:<8}",
            f"C = {totale_studente_c(scontrino)}",
        )
