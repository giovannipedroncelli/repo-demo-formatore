from programma_1 import prezzo_massimo


def test_prezzi_positivi():
    assert prezzo_massimo([12, 45, 7, 30]) == 45


def test_solo_resi():
    assert prezzo_massimo([-3, -1, -2]) == -1
