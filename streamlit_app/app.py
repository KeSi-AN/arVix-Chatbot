
import streamlit as st
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.llms import HuggingFacePipeline
import torch

@st.cache_resource
def load_resources():
    data = pd.read_csv("../saved_model/paper_metadata.csv")
    index = faiss.read_index("../saved_model/faiss_index_cs.idx")
    embed_model = SentenceTransformer("../saved_model/sbert_model")
    summarizer = pipeline("summarization", model="t5-small")
    explainer_pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", torch_dtype=torch.float16, device_map="auto")
    llm = HuggingFacePipeline(pipeline=explainer_pipeline)
    memory = ConversationBufferMemory()
    chat = ConversationChain(llm=llm, memory=memory)
    return data, index, embed_model, summarizer, chat

papers, index, embed_model, summarizer, chat = load_resources()

st.title("📚 arXiv Chatbot - Computer Science Expert")

query = st.text_input("Ask your research question or type keywords:")

if query:
    q_embed = embed_model.encode([query])
    D, I = index.search(np.array(q_embed).astype('float32'), 3)
    top_papers = papers.iloc[I[0]]

    for idx, row in top_papers.iterrows():
        st.subheader(row['title'])
        st.write(row['abstract'])

        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Summarize #{idx}"):
                summary = summarizer(row['abstract'], max_length=150, min_length=40, do_sample=False)[0]['summary_text']
                st.info(summary)
        with col2:
            if st.button(f"Explain #{idx}"):
                explanation = chat.run(f"Explain the topic: {row['abstract']}")
                st.success(explanation)
