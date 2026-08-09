import streamlit as st

st.set_page_config(
    page_title="ThinkLab Sentiment Analyzer",
    page_icon="💬",
    layout="wide"
)

st.title("ThinkLab NLP Sentiment Analyzer")
st.write("Product Review Sentiment Classification System")

st.subheader("Single Review Prediction")

review = st.text_area(
    "Enter a product review:",
    placeholder="Example: The dress is beautiful and comfortable."
)

if st.button("Predict Sentiment"):
    if review.strip():
        st.info("Prediction service will be connected next.")
    else:
        st.warning("Please enter a review.")
