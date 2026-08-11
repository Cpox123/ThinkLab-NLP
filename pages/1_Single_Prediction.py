import streamlit as st

st.title("Single Review Prediction")

st.write("Enter a product review to predict its sentiment.")

review = st.text_area(
    "Product Review",
    placeholder="Example: The dress is beautiful and comfortable."
)

if st.button("Predict Sentiment"):
    if not review.strip():
        st.warning("Please enter a review.")
    else:
        st.info("The prediction model will be connected after the backend is ready.")
