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

2. Run the server:
```bash
uv run uvicorn main:app --reload
```
The server will be available at http://localhost:8000. You can access the Swagger UI at http://localhost:8000/docs.

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
	- [ ] The Python library spaCy would also be possible.
	- [ ] LLM API.
- [ ] fastapi
- [ ] swagger
- [ ] docker
- [ ] test
