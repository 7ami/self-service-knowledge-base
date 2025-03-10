from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import faiss
import numpy as np
import pandas as pd
import torch
from transformers import BertModel, BertTokenizer, T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend to access API

# Load dataset
data = pd.read_csv("cleaned_data.csv")  # Ensure this CSV contains 'cleaned_combined_text'

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Load T5 tokenizer and model
t5_tokenizer = T5Tokenizer.from_pretrained("t5-base")
t5_model = T5ForConditionalGeneration.from_pretrained("t5-base")

# Load FAISS index
embeddings = np.load("embeddings.npy").astype(np.float32)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

@app.route("/query", methods=["POST"])
def query():
    user_query = request.json.get("query")

    print(f"\n🔹 Received Query: {user_query}")

    # Convert query to BERT embedding
    query_inputs = tokenizer(user_query, padding=True, truncation=True, return_tensors='pt', max_length=128)
    with torch.no_grad():
        query_outputs = model(**query_inputs)

    query_embedding = query_outputs.last_hidden_state[:, 0, :].detach().cpu().numpy().astype(np.float32)

    # Perform FAISS search
    D, I = index.search(query_embedding, k=5)

    print(f"\n🔹 FAISS Search Results (Top 5 IDs): {I[0]}")

    # Handle case where FAISS returns no relevant results
    if len(I[0]) == 0 or I[0][0] == -1:
        return jsonify({"response": "No relevant answer found."})

    # Retrieve top 5 documents
    retrieved_docs = " ".join([data['cleaned_combined_text'].iloc[i] for i in I[0] if i < len(data)])

    print("\n🔹 Retrieved Documents:")
    print(retrieved_docs)  # Debugging print

    # If no meaningful documents are retrieved, return a default response
    if not retrieved_docs.strip():
        return jsonify({"response": "No relevant answer found."})

    # Prepare input for T5
    input_text = f"answer: {retrieved_docs} context: {user_query}"
    input_ids = t5_tokenizer.encode(input_text, return_tensors='pt')

    # Generate response
    with torch.no_grad():
        generated_ids = t5_model.generate(input_ids, max_length=150, num_beams=5, early_stopping=True)

    response = t5_tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    print(f"\n✅ Generated Response: {response}")

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
