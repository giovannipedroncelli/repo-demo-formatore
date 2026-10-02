# Machine learning con Python — materiali dell'Incontro 3

| Notebook | Durata in classe | Livello IA | Contenuto |
|---|---|---|---|
| `01_pandas_funghi.ipynb` | 1 h | 0-1 | PRIMM su pandas: shape, value_counts, mancanti nascosti, crosstab, one-hot |
| `02_sei_modelli.ipynb` | 2 h | 1 | regressione lineare, logistica, kNN, albero, SVM, k-means con lo stesso schema fit/predict |
| `02b_baseline_credito.ipynb` | 45 min | 1 | German Credit: accuratezza contro baseline e recall; discussione su bias e proxy |
| `03_errori_ml.ipynb` | 1 h | 3 | sei errori di metodo in codice "scritto dall'IA" |
| `04_riserva_knn_da_zero.ipynb` | 20-30 min | 0 | kNN scritto a mano e confrontato con scikit-learn: parità di voti e unità di misura (riserva) |
| `05_riserva_svm.ipynb` | 15-20 min | 1 | SVM: iperpiano, margine, parametro C, kernel lineare e `rbf` (riserva) |

- `dati/`: i CSV. `mushrooms.csv` (UCI Mushroom); `german_credit.csv` (UCI Statlog German Credit, CC BY 4.0, con le etichette testuali della versione OpenML `credit-g`).
- `docente/`: versioni eseguite con gli output e `chiave-notebook.md` con i numeri reali. **Da non pubblicare** nel repository degli studenti: basta cancellare la cartella dal fork della classe, oppure tenere il repository del docente privato.

## Come aprirli

- **Colab (consigliato)**: `https://colab.research.google.com/github/giovannipedroncelli/repo-demo-formatore/blob/main/ml/01_pandas_funghi.ipynb`. Chi copia i notebook in un proprio repository deve cambiare utente e nome del repository nel link e nella variabile `URL_BASE` della prima cella di codice: in Colab il CSV si legge da GitHub.
- **In locale** (Jupyter, VS Code): i notebook trovano il file in `dati/` senza bisogno di internet.
- **Antigravity**: i notebook si scrivono e si modificano come file, ma si eseguono in Colab (Antigravity non ha un'esecuzione nativa dei notebook affidabile).

## Vincoli d'età

Colab è un servizio aggiuntivo di Google Workspace for Education: per gli studenti minorenni serve che la scuola l'abbia abilitato e che ci sia il consenso dei genitori. Le funzioni IA integrate in Colab (Gemini) sono riservate ai maggiorenni. Per i minorenni i notebook si usano quindi senza IA: livello 0-1 con il Gem tutor in una finestra separata.
