import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
import google.generativeai as genai
from pydantic import BaseModel






load_dotenv()
origins = [
    "http://localhost:5173",
]

app=FastAPI()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # List of allowed origins
    allow_credentials=True,     # Allow cookies and auth headers
    allow_methods=["*"],         # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],         # Allow all headers
)


# midleware
class validPrompt(BaseModel):
    prompt: str


@app.get('/')
def home():
    return "welcome to home page."


@app.post('/generate')
async  def generate_content(request: validPrompt):
    # model=genai.GenerativeModel('gemini-2.5-flash')
    # result=model.generate_content(request.prompt)
    # return {"response": result.text}
    result="Nicola Tesla was a great Scientist..."  # dummy response
    return {"response": result}