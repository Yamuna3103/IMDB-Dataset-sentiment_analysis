# 🎬 Movie Review Sentiment Analysis

A **Natural Language Processing (NLP)** project that predicts whether a movie review is **Positive or Negative** using Machine Learning and TF-IDF vectorization.

This project uses **Python, Scikit-learn, and Streamlit** to build an interactive web application where users can enter a movie review and instantly see the sentiment prediction.

---

## 🚀 Project Overview

Sentiment Analysis is a common **NLP technique** used to determine the emotional tone of text data.

In this project:

* Movie reviews are **cleaned and preprocessed**
* Text is converted into numerical features using **TF-IDF**
* A **Machine Learning model** predicts the sentiment
* A **Streamlit web application** provides an interactive interface

---

## 🛠️ Technologies Used

* Python
* Natural Language Processing (NLP)
* Scikit-learn
* TF-IDF Vectorizer
* Streamlit
* Pickle
* Regular Expressions

---

## 📂 Project Structure

```
IMDB-Dataset-sentiment_analysis
│
├── sentiment_model.pkl        # Trained machine learning model
├── tfidf_vectorizer.pkl       # TF-IDF vectorizer
├── app.py                     # Streamlit application
├── requirements.txt           # Required libraries
└── README.md                  # Project documentation
```

---

## ⚙️ How It Works

1. User enters a **movie review**
2. The text is **cleaned using preprocessing techniques**
3. The review is converted into numerical form using **TF-IDF**
4. The trained **machine learning model predicts the sentiment**
5. The application displays:

* Positive 😊 or Negative 😡 result
* Confidence score

---

## ▶️ Running the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/IMDB-Dataset-sentiment_analysis.git
```

### 2️⃣ Navigate to the Project Folder

```
cd IMDB-Dataset-sentiment_analysis
```

### 3️⃣ Install Required Libraries

```
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App

```
streamlit run app.py
```

---

## 📊 Example

**Input Review**

```
This movie was amazing with great acting and storyline.
```

**Output**

```
Positive Review 😊
Confidence: 92%
```

---

## 🎯 Key Features

* Text preprocessing using regex
* TF-IDF feature extraction

