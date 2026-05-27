from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="AI Model Serving API")

# Enable CORS for the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Hugging Face Pipelines (loaded once at startup)
print("Loading models... (This may take a moment on first run)")
sentiment_analyzer = pipeline("sentiment-analysis")
text_generator = pipeline("text-generation", model="distilgpt2")
print("Models loaded successfully!")

# Pydantic models for request validation
class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "FastAPI AI Backend is running."}

@app.post("/api/sentiment")
def analyze_sentiment(request: TextRequest):
    try:
        result = sentiment_analyzer(request.text)[0]
        return {"label": result["label"], "score": result["score"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate")
def generate_text(request: TextRequest):
    try:
        # Generate text with a max length of 50 tokens
        result = text_generator(request.text, max_length=50, num_return_sequences=1)[0]
        return {"generated_text": result["generated_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)