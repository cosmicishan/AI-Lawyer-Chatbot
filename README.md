# 🏡 AI Lawyer Chatbot

## 📌 Overview
AI Lawyer Chatbot is a **legal document Q&A system** that allows users to upload PDFs containing legal texts and ask questions related to them. It leverages **Retrieval-Augmented Generation (RAG)** and advanced **LLM models** to provide context-aware responses.

## 🚀 Features
- 🐂 **PDF Upload**: Users can upload legal documents for analysis.
- 🔍 **Context-Aware Retrieval**: Uses FAISS vector database for document search.
- 🤖 **AI-Powered Answers**: Uses **DeepSeek R1 LLM** to generate responses.
- 🎨 **Streamlit UI**: User-friendly interface for seamless interactions.

## 🛠️ Tech Stack
- **Frontend**: Streamlit (`frontend.py`)
- **Vector Database**: FAISS, LangChain (`vector_database.py`)
- **AI Model**: DeepSeek R1 + Groq (`rag_pipeline.py`)
- **Embedding Model**: Ollama Embeddings

## 💂 Project Structure
```
📎 ai-lawyer-chatbot
├── 💜 frontend.py            # Streamlit frontend for UI interaction
├── 💜 vector_database.py     # FAISS database for document search
├── 💜 rag_pipeline.py        # RAG pipeline for query answering
├── 📂 PDFs/                  # Directory for uploaded PDF files
└── 💜 README.md              # Project documentation
```

## ⚙️ Installation & Usage

### 🔧 Prerequisites
- Python 3.8+
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### ▶️ Run the Chatbot
```sh
streamlit run frontend.py
```

## 🏡 How It Works
1. **Upload a legal PDF** via the web interface.
2. **Vectorize and store** in FAISS using `vector_database.py`.
3. **Ask a legal question** in the chatbox.
4. **Retrieve relevant document chunks** via similarity search.
5. **Generate an AI-powered response** using DeepSeek R1.

## 🤝 Contribution
Contributions are welcome! Feel free to open an issue or PR.

## ❤️ Credits
Developed by **Ishan Purohit**.

