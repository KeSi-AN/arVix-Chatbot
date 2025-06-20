
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

df = pd.read_csv("../saved_model/paper_metadata.csv")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
index = faiss.read_index("../saved_model/faiss_index_cs.idx")

mock_queries = {
    "transformer architecture in NLP": "Attention Is All You Need",
    "image classification with CNN": "Deep Residual Learning for Image Recognition",
    "neural networks optimization": "Adam: A Method for Stochastic Optimization"
}

top_k = 3
correct = 0

for query, expected_title in mock_queries.items():
    query_vec = model.encode(query, convert_to_numpy=True)
    D, I = index.search(np.array([query_vec]), top_k)
    hits = df.iloc[I[0]]["title"].tolist()

    print(f"\nQuery: {query}")
    print("Top matches:")
    for hit in hits:
        print(f"  - {hit}")
    if expected_title in hits:
        correct += 1

accuracy = (correct / len(mock_queries)) * 100
print(f"\nPrecision@{top_k}: {accuracy:.2f}%")
