import streamlit as st



uploaded_file = st.file_uploader(
  label =  "Choose a PDF file",
    type=["pdf"],
)


