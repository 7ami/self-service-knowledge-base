from flask import Flask, request, jsonify
from flask_cors import CORS
import faiss
import numpy as np
import pandas as pd
import torch
import re
from transformers import BertModel, BertTokenizer, T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)
CORS(app)

data = pd.read_csv("cleaned_data.csv")

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

t5_tokenizer = T5Tokenizer.from_pretrained("t5-base")
t5_model = T5ForConditionalGeneration.from_pretrained("t5-base")

embeddings = np.load("embeddings.npy").astype(np.float32)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def clean_generated_answer(text):
    text = re.sub(r'[^a-zA-Z0-9.,!?\'"() ]+', '', text)
    text = text.replace("..", ".").replace(" .", ".")
    return text.strip()

@app.route("/query", methods=["POST"])
def query():
    user_query = request.json.get("query")

    query_inputs = tokenizer(user_query, padding=True, truncation=True, return_tensors='pt', max_length=128)
    with torch.no_grad():
        query_outputs = model(**query_inputs)

    query_embedding = query_outputs.last_hidden_state[:, 0, :].detach().cpu().numpy().astype(np.float32)

    D, I = index.search(query_embedding, k=5)

    if len(I[0]) == 0 or I[0][0] == -1:
        return jsonify({"response": "No relevant answer found."})

    retrieved_docs = [data['cleaned_combined_text'].iloc[i] for i in I[0] if i < len(data)]
    retrieved_docs = [doc.strip() for doc in retrieved_docs if doc.strip() and len(doc.split()) > 5]

    retrieved_text = " ".join(retrieved_docs)
    if not retrieved_text:
        return jsonify({"response": "No relevant answer found."})

    input_text = f"answer: {retrieved_docs} context: {user_query}"

    input_ids = t5_tokenizer.encode(input_text, return_tensors='pt')

    with torch.no_grad():
        generated_ids = t5_model.generate(
            input_ids, 
            max_length=150,  
            min_length=50,  
            num_beams=7,  
            no_repeat_ngram_size=3,  
            repetition_penalty=1.8,  
            temperature=0.7,  
            top_k=50,  
            top_p=0.9,  
            early_stopping=True
        )

    response = clean_generated_answer(t5_tokenizer.decode(generated_ids[0], skip_special_tokens=True))

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
