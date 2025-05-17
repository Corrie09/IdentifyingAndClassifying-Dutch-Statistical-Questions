# thesis-question-classification-KU-LEUVEN

# Statistical Question Classification in Flemish Parliamentary Data

This repository supports the master's thesis project on classifying and identifying statistical questions in Flemish parliamentary documents. The aim is to build and compare traditional machine learning models and transformer-based models (BERT) for short-text classification, with a focus on identifying questions that can be answered using structured data.

## 📁 Repository Structure

- `BERT_Classifiers/` — Fine-tuned BERT models (GroNLP, RobBERT, mBERT) for classification and identification tasks.
- `Baseline_Classifiers/` — Traditional models (Logistic Regression, SVM, Naive Bayes, Random Forest, XGBoost).
- `Data/` — Contains training, test, and evaluation datasets.
- `EDA/` — Exploratory data analysis and visualizations.
- `EvaluateModels/` — Statistical tests (Wilcoxon, McNemar, Nemenyi), classification reports, and evaluation logic.
- `Extractor/` — Raw PDF-to-text extraction and question/context parsing, including transshap logic.
- `Identifier/` — Binary identifier model (statistical vs non-statistical) with grid search and evaluation.
- `OUD/` — Legacy scripts retained for reference.
- `Preprocessing/` — TF-IDF filtering, stopword removal, context building, and other cleaning steps.
- `Scraper/` — Scripts for scraping PDFs and metadata from Flemish Parliament sources.

## ⚙️ How to Run

1. **Preprocess the data:**
   - Run scripts in `Scraper/` and `Preprocessing/` to extract and clean raw question data.

2. **Train models:**
   - Use `Baseline_Classifiers/` and `BERT_Classifiers/` to train different models.
   - `Identifier/` includes code for training the binary statistical question identifier.

3. **Evaluate:**
   - `EvaluateModels/` contains scripts to compute performance metrics and statistical comparisons between models.

## 📊 Thesis Focus

- Comparative performance of traditional vs transformer-based models.
- Addressing short-text challenges via context injection and active learning.
- Statistical evaluation using Wilcoxon, McNemar, and Nemenyi tests.
- Domain-specific optimization with Dutch-language models.

## 📄 Notes

- Dutch stopwords and TF-IDF are adapted for domain specificity.
- Context windows are used to enhance classification accuracy for short or ambiguous questions.

## 📚 Citation

If you use this code or dataset for academic purposes, please cite the thesis or contact the author.


🛠 Maintained by [Jef Van Kerckhoven, KU Leuven and Corneel Moons, KU Leuven]
