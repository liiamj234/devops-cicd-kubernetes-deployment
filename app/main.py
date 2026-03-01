import os
from fastapi import FastAPI

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.get("/")
def root():
    return {
        "message": "CI/CD Kubernetes Deployment",
        "version": APP_VERSION
    }

@app.get("/health")
def health():
    return {"status": "ok"}