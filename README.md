# 🧠 **Cleaning House Price Data in PySpark**

This project focuses on cleaning large quantities of data using **PySpark** to partition it. This is an essential task in every Data Science project as it not only improves the model performance, but it also helps on understanding variables and their reliability.

- Calcular precios de casas
- Tengo mucha información, como el número de garajes, si tiene piscina y juraría que hasta si tiene chimenea
- Problema:
  - muchos NAs que imputar -> imputar con criterio
  - Muchas categorías -> PCA
  - Muchos casos -> particionar
- Medimos en Kaggle el rendimiento para comparar
---

## 📂 Dataset

The dataset belongs to [this Kaggle competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), and showcase house prices and several other characteristics, such as:
- 🏡**House measurements** (e.g., garage area, distance from the door to the street).
- ✨**Quality** (e.g., fireplace quality, garage quality).
- 🧰**Technical information** (e.g., access to gas, type of heating).
- 💰**Sale information** (e.g., year sold, sal type).

<!--
Data preprocessing involves:
- Tokenization
- Lemmatization
- Stop-word removal

---

## 🎯 Objective

To classify user input into predefined intent categories with high accuracy. Key goals include:
- Building and evaluating **machine learning models** for classification.
- Analyzing the impact of **text preprocessing** techniques on performance.
- Comparing the results of various **algorithms** like SVM, Naive Bayes, and Neural Networks.

---

## ⚙️ Approach

### 🔄 Data Preparation
1. **Preprocessing Steps:**
   - Removed noise, punctuation, and stop-words.
   - Applied stemming/lemmatization for word normalization.

2. **Feature Extraction:**
   - Used **TF-IDF vectors** to represent text numerically.
   - Experimented with **word embeddings** for semantic representation.

### 🛠️ Models
- **Baseline Model:** Random classifier.
- Naive Bayes classifier with bag-of-words.
- **Models to compare:**
  - TF-IDF Classifier.  
  - Naive Bayes Classifier.
 
---

## 🌟 Results

### Performance Insights
- **Baseline Model (Random Classifier):** As it was expected, increasing the number of categories decreases it's accuracy.
- **TF-IDF Classifier:** Reached a decent accuracy, although it requires a long time to train.
- ⭐ **Naive Bayes:** Best accuracy of the three with a short training time.

---

## 🔮 Future Improvements

- **Expanded Dataset:** Incorporate more diverse and multilingual queries.
- **Context Awareness:** Leverage sequence models like LSTMs or Transformers.
- **Real-Time Deployment:** Implement in a live environment for continuous learning and feedback.
-->

