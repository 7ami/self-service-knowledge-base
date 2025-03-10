Self-Service Knowledge Base Based on Support Solutions & Field Visits

Project Overview:
This project implements an AI-powered knowledge base that auto-generates solutions based on past customer support interactions and field technician visits. Using Retrieval-Augmented Generation (RAG), we retrieve relevant past cases and generate informative responses.

Features:
-Retrieval-Augmented Generation (RAG) Model using BERT + T5.
-FAISS-based Similarity Search to retrieve past cases efficiently.
-Flask API to serve the AI model.
-React.js Frontend for an interactive search experience.

Tech Stack:
Backend: Python, Flask, FAISS, Hugging Face Transformers, Pandas, Numpy, Torch
Frontend: React.js, Styled-Components, Axios, Bootstrap,Bulma
Database: Processed CSV Data

Installation & Setup:
Prerequisites:
Python 3.8+
Node.js 16+
pip, virtualenv (recommended)

Clone the Repository:
Backend Setup:
Frontend Setup:


How the Model Works:
Retrieval-Augmented Generation (RAG):
1.Retrieval: FAISS indexes past cases and retrieves the most relevant solutions.
2.Encoding: BERT converts queries into embeddings to find similar cases.
3️.Generation: T5 uses retrieved documents to generate a response.

Future Improvements:
1.Enhance Data Quality: Include more structured and verified support tickets.
2.Fine-Tune T5 Model: Improve response generation quality.