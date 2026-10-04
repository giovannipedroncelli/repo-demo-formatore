# Rubrica di leggibilità del codice (classe terza)

Usata dal docente e, in forma di istruzioni, dal Gem "Revisore formativo" (S7). Serve per il feedback formativo, non per il voto. I criteri riprendono, in linguaggio da studente, le operazioni di refactoring più comuni (nomi chiari, estrarre una funzione, semplificare le condizioni, togliere il codice che non serve).

| Criterio | Da migliorare | Buono | Ottimo |
|---|---|---|---|
| **A. Nomi** | `a`, `x`, `lista2`: non si capisce cosa contengono | la maggior parte dei nomi dice cosa contiene | ogni variabile e funzione si capisce senza leggere il resto del codice |
| **B. Struttura** | tutto in un blocco unico; pezzi ripetuti | funzioni separate, qualche ripetizione | ogni funzione fa una cosa sola; nessun pezzo ripetuto |
| **C. Casi limite** | lista vuota o valori negativi mandano in errore il programma | alcuni casi limite gestiti | lista vuota, un solo elemento, negativi e soglia esatta gestiti e provati |
| **D. Chiarezza** | nessun commento, oppure commenti che ripetono il codice | un commento per funzione | commenti brevi che dicono *cosa restituisce* e *perché* una scelta è stata fatta |
| **E. Codice che non serve** | variabili mai usate, righe commentate lasciate lì | poco codice inutile | nessun codice inutile |
