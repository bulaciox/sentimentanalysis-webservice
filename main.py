from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from afinn import Afinn

app = FastAPI()
afinn = Afinn()

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health_check():
    return {"status": "ok"}

class TextInput(BaseModel):
    text: str

@app.post("/v1/sentiment")
def analyze_sentiment(text: TextInput):
    lowered_text = text.text.lower()

    if 'god' in lowered_text or 'good' in lowered_text:
        return {"score": 3}
    elif 'dårlig' in lowered_text or 'bad' in lowered_text:
        return {"score": -3}
    else:
        return {"score": 0}

@app.post("/v2/sentiment")
def analyze_sentiment_v2(text: TextInput):
    return {"score": afinn.score(text.text)}
    
