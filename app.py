from fastapi import FastAPI 
import joblib
from schema import CustomerData
import pandas as pd

app = FastAPI()

pipeline = joblib.load("churn_pipeline.pkl")
threshold = joblib.load("threshold.pkl")


@app.post("/predict")
def predict(data: CustomerData):
    df = data.model_dump()

    # convert to DataFrame
    df = pd.DataFrame([df])

    probability = pipeline.predict_proba(df)[0][1]

    prediction = int(probability >= threshold)

    return {
        "prediction": prediction,
        "probability": round(probability, 4)
    }