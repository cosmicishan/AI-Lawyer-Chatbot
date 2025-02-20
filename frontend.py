import streamlit as st
from rag_pipeline import answer_query, retrieve_docs, llm_model
from vector_database import create_faiss_database, upload_pdf
import tempfile

# Custom CSS for styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f0f2f6;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .stFileUploader {
        margin-bottom: 20px;
    }
    .stTextInput input {
        border-radius: 12px;
        padding: 10px;
        font-size: 16px;
    }
    .stMarkdown {
        color: #333;
    }
    .header {
        font-size: 32px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 18px;
        color: #666;
        text-align: center;
        margin-bottom: 30px;
    }
    .upload-box {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        color: #666;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="header">AI Lawyer Chatbot</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subheader">Upload a PDF and ask your legal questions!</div>',
    unsafe_allow_html=True,
)

# File uploader inside a styled box
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
st.markdown('</div>', unsafe_allow_html=True)

# Disable the "Ask AI Lawyer" button if no PDF is uploaded
if uploaded_file is not None:
    st.success("PDF uploaded successfully! You can now ask your questions.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name  

    #upload_pdf(uploaded_file)

    with st.spinner("Storing file into vector database"):
        faiss_db = create_faiss_database(temp_file_path)

    user_query = st.text_input("Ask your legal question here:", key="input")

    if st.button("Ask AI Lawyer"):

        with st.spinner("Generating a Response"):

            retrieved_docs=retrieve_docs(user_query, faiss_db)
            response=answer_query(documents=retrieved_docs, model=llm_model, query=user_query)

            st.write(response.content[response.content.find('</think>')+10:])  # Placeholder for response
else:
    st.warning("Please upload a PDF file to proceed.")
    st.button("Ask AI Lawyer", disabled=True)  # Disabled button

# Footer
st.markdown(
    """
    <div class="footer">
        Made with ❤️ by Ishan Purohit
    </div>
    """,
    unsafe_allow_html=True,
)