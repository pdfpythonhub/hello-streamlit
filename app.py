import streamlit as st


# Display the app title and introduction
st.title("📄 PDF Inspector")
st.write(
    "Upload a PDF to count its pages, inspect its metadata, "
    "and download a JSON report."
)

# Upload a PDF file
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
)


