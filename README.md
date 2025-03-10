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
git clone https://github.com/7ami/self-service-knowledge-base.git
cd self-service-knowledge-base


Backend Setup:
**Flask API**
>cd C:\codes\Wl
>python app.py


Frontend Setup:
>cd frontend
>npm start


How the Model Works:
Retrieval-Augmented Generation (RAG):
1.Retrieval: FAISS indexes past cases and retrieves the most relevant solutions.
2.Encoding: BERT converts queries into embeddings to find similar cases.
3️.Generation: T5 uses retrieved documents to generate a response.


Usage:
Enter a query (e.g., "What should I do if my internet speed is lower than expected?")
The system retrieves relevant documents using BERT + FAISS
The T5 model generates a human-like response.


Future Improvements:
1.Enhance Data Quality: Include more structured and verified support tickets.
2.Fine-Tune T5 Model: Improve response generation quality.
