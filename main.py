from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from afinn import Afinn

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

app = FastAPI()
afinn = Afinn()

# initialize spacy and add the spacytextblob component for english sentiment analysis
nlp_en = spacy.load("en_core_web_sm")

nlp_en.add_pipe('spacytextblob')

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

@app.post("/v3/sentiment")
def analyze_sentiment_v3(text: TextInput):
    doc = nlp_en(text.text)
    sentiment = doc._.blob.polarity
    return {"score": sentiment}

    
