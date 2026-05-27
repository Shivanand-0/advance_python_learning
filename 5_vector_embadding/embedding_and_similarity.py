from sentence_transformers import SentenceTransformer, util

sentences = [
    'I love AI', 
    'Artificial Intelligence is changing the world.', 
    'The weather is good.'
]

# 1. Load the embedding model (384-dimensional vectors)
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Convert text into numerical embeddings
embeddings = model.encode(sentences)

# 3. Calculate cosine similarity
# We compare the first sentence (index 0) with the second sentence (index 1)
similarity = util.cos_sim(embeddings[0], embeddings[1])

print(f"Similarity score: {similarity.item():.4f}")
