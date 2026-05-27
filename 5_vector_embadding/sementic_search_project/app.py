# !pip install sentence-transformers
# !pip install sklearn


import numpy as np
import gradio as gr
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load model and define documents
model = SentenceTransformer('all-MiniLM-L6-v2')
documents = [
    "Python is used for AI and Machine Learning",
    "Cars require regular maintainence.",
    "Neural Network is part of Deep Learning"
]

# Precompute document embeddings so it doesn't recalculate on every query
doc_embeddings = model.encode(documents)

# 2. Define the matching function
def find_best_match(query):
    query_embedding = model.encode([query])
    similarity = cosine_similarity(query_embedding, doc_embeddings)
    best_match_idx = np.argmax(similarity[0])
    
    matched_doc = documents[best_match_idx]
    score = similarity[0][best_match_idx]
    
    return matched_doc, round(score, 4)

# 3. Create the Gradio UI
with gr.Blocks(title="Semantic Search Engine") as demo:
    gr.Markdown("# 🔍 Semantic Search & Sentence Similarity")
    gr.Markdown("Enter a query to find the most semantically similar document in our predefined database.")
    
    with gr.Row():
        user_query = gr.Textbox(label="Enter your Query", placeholder="e.g., Artificial intelligence using python")
    
    search_btn = gr.Button("Search")
    
    with gr.Row():
        output_doc = gr.Textbox(label="Best Match Document")
        output_score = gr.Number(label="Cosine Similarity Score")
        
    search_btn.click(find_best_match, inputs=user_query, outputs=[output_doc, output_score])

# Run the app
if __name__ == "__main__":
    demo.launch()



