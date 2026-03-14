from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(
    title="Strettch Cloud FastAPI Demo",
    description="A production-ready FastAPI service deployed on Strettch Cloud",
    version="1.0.0",
)

class PredictionRequest(BaseModel):
    input: float

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(request: PredictionRequest):
    """
    Simulates an ML inference request.
    """
    time.sleep(0.2) #simulate processing delay
    result = request.input * 1.5

    return {
        "input": request.input,
        "prediction": result,
        "model": "demo-linear-model",
    }