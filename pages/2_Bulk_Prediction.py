import streamlit as st
import pandas as pd

st.title("Bulk CSV Prediction")

st.write("Upload a CSV file containing product reviews.")

uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Preview")
    st.dataframe(df.head())

    if "Review Text" not in df.columns:
        st.error("The CSV must contain a 'Review Text' column.")
    else:
        st.success(f"{len(df)} reviews loaded successfully.")

        if st.button("Predict All"):
            st.info(
                "The prediction model will be connected after "
                "the backend is ready."
            )
