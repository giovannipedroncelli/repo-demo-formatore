# Chiave — programma_1.py (per il docente)

- **Riga dell'errore:** `massimo = 0`.
- **Misconcezione:** inizializzare il massimo a zero invece che al primo elemento.
- **Input che lo rivela:** uno scontrino di soli resi, per esempio `[-3, -1, -2]`.
- **Output atteso:** `-1`. **Output effettivo:** `0`.
- **Correzione:** `massimo = prezzi[0]` (con un controllo per la lista vuota).
- **Perché un'IA potrebbe commetterlo:** è lo schema più frequente negli esempi con prezzi positivi; funziona su quasi tutti gli input "normali", quindi passa i test più ovvi.
- **Test che lo dimostra:** `test_programma_1.py` fallisce su questo programma e passa sulla versione corretta.
