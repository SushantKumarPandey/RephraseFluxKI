import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

API_KEY = "-"
BASE_URL = "https://chat-default.models.th-luebeck.dev/v1/chat/completions"

@app.get("/")
async def root():
    return {"message": "Welcome to RephraseFluxKI!"}

class ParaphraseRequest(BaseModel):
    text: str

@app.post("/paraphrase/")
async def paraphrase(request: ParaphraseRequest):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    data = {
        "model": "tgi",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Paraphrase the following text: {request.text}"}
        ],
        "stream": False,
        "max_tokens": 1024
    }
    
    try:
        response = requests.post(BASE_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        paraphrased_text = result["choices"][0]["message"]["content"].strip()
        return {"paraphrased_text": paraphrased_text}
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
