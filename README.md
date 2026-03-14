🎬 Movie Review Sentiment Analysis

A Natural Language Processing (NLP) project that predicts whether a movie review is Positive or Negative using Machine Learning and TF-IDF vectorization.

This project is built with Python, Scikit-learn, and Streamlit, and allows users to input a movie review and instantly analyze the sentiment.

🚀 Project Overview

Sentiment Analysis is a common NLP task used to understand opinions in text data.

In this project:

Text reviews are cleaned and preprocessed

Converted into numerical features using TF-IDF

A Machine Learning model predicts the sentiment

A Streamlit web application allows users to interact with the model.

🛠️ Technologies Used

Python

Natural Language Processing (NLP)

Scikit-learn

TF-IDF Vectorizer

Streamlit

Pickle

Regular Expressions

📂 Project Structure
IMDB-Dataset-sentiment_analysis
│
├── sentiment_model.pkl        # Trained ML model
├── tfidf_vectorizer.pkl       # TF-IDF vectorizer
├── app.py                     # Streamlit application
├── requirements.txt           # Required libraries
└── README.md                  # Project documentation
⚙️ How It Works

User enters a movie review

The text is cleaned and preprocessed

The review is transformed using TF-IDF vectorization

The trained Machine Learning model predicts the sentiment

The app displays:

Positive 😊 or Negative 😡 result

Confidence score
