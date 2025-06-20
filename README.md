
# 🤖 arXiv Chatbot - Computer Science Expert

This chatbot is trained on the arXiv Computer Science subset to:
- Answer advanced CS queries
- Summarize research papers
- Explain complex concepts
- Handle follow-up questions

## 🔧 Features
- NLP-based semantic search using FAISS
- Paper summarization using `T5-small`
- Concept explanation via `Mistral-7B`
- Streamlit UI for user-friendly interactions
- LangChain-powered memory for contextual follow-ups

## 📦 Dataset
- Kaggle Link: https://www.kaggle.com/datasets/Cornell-University/arxiv
- Place `arxiv-metadata-oai-snapshot.csv` inside the `data/` folder before training.

## 🚀 Setup
```bash
git clone https://github.com/your-username/arxiv-chatbot.git
cd arxiv-chatbot
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

## 🧪 Evaluation
Run `evaluation/evaluate_metrics.py` to test semantic retrieval performance.

## 📁 Structure
- `notebooks/train_model.ipynb`: Model training
- `streamlit_app/app.py`: UI logic
- `evaluation/`: Model evaluation script
- `saved_model/`: Embeddings and index files
- `data/`: Dataset file
