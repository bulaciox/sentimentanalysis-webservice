# Sentiment Analysis - Web service

A simple web service for sentiment analysis built with FastAPI. It currently uses a basic keyword-based approach to determine sentiment scores.

## Local Development

### Prerequisites

- [uv](https://github.com/astral-sh/uv) installed.

### Run locally

1. Install dependencies:
```bash
uv sync
```

2. Run the main sentiment analysis service (backend):
```bash
uv run uvicorn main:app --reload --port 8000
```
The server will be available at http://localhost:8000. You can access the Swagger UI at http://localhost:8000/docs.

3. Run the demo frontend app:
```bash
uv run uvicorn app:app --reload --port 8001
```
The frontend UI will be available at http://localhost:8001.

## Sentiment Analysis Versions

This project implements different versions of sentiment analysis:

- **v1**: Basic keyword-based approach (hardcoded).
- **v2**: Uses the [AFINN](https://github.com/fnielsen/afinn) lexicon for sentiment scoring.
- **v3 (spaCy)**: An advanced NLP approach using [spaCy](https://spacy.io/) was implemented but is currently **disabled** to keep the Docker image size small. 

### Enabling spaCy (v3)

If you want to use the spaCy implementation locally (v3 endpoint), you need to reinstall the dependencies:

```bash
uv add spacy spacytextblob https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl
```

Then uncomment the relevant lines in `main.py`.

## Docker

### Build the image

```bash
docker build -t sentiment-analysis .
```

### Run the container

```bash
docker run -p 8000:8000 sentiment-analysis
```

## TASKs

- [x] git repo
- [x] uv
- [ ] sentiment analysis
    - [x] hardcoded s.a.
	- [ ] Training a machine learning classifier would also be possible.
	- [x] The Python library spaCy would also be possible.
	- [ ] LLM API.
- [x] fastapi
- [x] swagger
- [x] docker
- [x] test
