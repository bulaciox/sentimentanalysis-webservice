from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from afinn import Afinn

# import spacy
# from spacytextblob.spacytextblob import SpacyTextBlob

app = FastAPI()
afinn = Afinn()

# initialize spacy and add the spacytextblob component for english sentiment analysis
# nlp_en = spacy.load("en_core_web_sm")
# nlp_en.add_pipe('spacytextblob')

print(afinn.score('horrible'))
# Disable v3 because of docker size
# @app.post("/v3/sentiment")
# def analyze_sentiment_v3(text: TextInput):
#     doc = nlp_en(text.text)
#     sentiment = doc._.blob.polarity
#     return {"score": sentiment}

    
