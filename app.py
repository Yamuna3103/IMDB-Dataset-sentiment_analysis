import streamlit as st
import pickle
import re

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="🎬",
    layout="centered"
)

# Load model
model = pickle.load(open("sentiment_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Clean text
def clean_text(text):

    text = text.lower()
    text = re.sub(r"<.*?>"," ",text)
    text = re.sub(r"[^a-zA-Z]"," ",text)
    text = re.sub(r"\s+"," ",text)

    return text

# Prediction function
def predict_sentiment(review):

    review = clean_text(review)
    vector = tfidf.transform([review])

    prediction = model.predict(vector)[0]
    probability = model.predict_proba(vector)[0]

    return prediction, probability


# Title
st.title("🎬 Movie Review Sentiment Analysis")

st.write("Analyze whether a movie review is **Positive or Negative** using NLP.")

# Input box
review = st.text_area(
    "✍️ Enter your movie review:",
    height=150
)

# Predict button
if st.button("🔍 Analyze Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:

        prediction, probability = predict_sentiment(review)

        st.subheader("Result")

        if prediction == 1:
            st.success("😊 Positive Review")
            st.progress(float(probability[1]))

        else:
            st.error("😡 Negative Review")
            st.progress(float(probability[0]))

        st.write("### Confidence Score")

        st.write({
            "Positive Probability": float(probability[1]),
            "Negative Probability": float(probability[0])
        })