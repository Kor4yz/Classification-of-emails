import streamlit as st
from emailclf.preprocess import clean_text
from emailclf.models import load_best, predict_proba

st.title("📧 Email Classifier (Spam / Not spam)")
text = st.text_area("Paste email text")
if st.button("Classify"):
    model, vectorizer = load_best("artifacts")
    p = predict_proba(model, vectorizer, clean_text(text))
    st.metric("Spam probability", f"{p:.2%}")
