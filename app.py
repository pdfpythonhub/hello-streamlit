import streamlit as st

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide",  # Options: "centered" or "wide"
    initial_sidebar_state="expanded",  # Options: "auto", "expanded", "collapsed"
    menu_items={
        "Get Help": "https://google.com",
        "Report a bug": "https://google.com",
        "About": "This is a custom Streamlit app.",
    },
)

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


