import streamlit as st
import os
import sys


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(BASE_DIR)

from db.database import initialize_database
initialize_database()

st.set_page_config(page_title="Document Manager", layout="wide")
st.title("🗂️ Document Manager")
st.divider()

tab = st.tabs(["upload", "Search", "Analytics"])

#   Upload Tab
with tab[0]:
    st.header("Upload Document")
    st.file_uploader("Choose a document to upload", type=["pdf", "docx", "txt"])
    pass
#   Search Tab
with tab[1]:
    st.header("Search Documents")
    st.text_input("Enter search query")
    pass
#   Analytics Tab
with tab[2]:
    st.header("Analytics")
    st.write("Document analytics will be displayed here.")
    pass
