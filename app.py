# Importing necessary libraries
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()  # Creating an instance of the FastAPI class
model = joblib.load('models/xgb_tuned_model.pkl')
scaler = joblib.load('models/scaler.pkl')


class Transactions(BaseModel):
    features: list[float]  # Defining the expected input features for the model


@app.get("/")  # Defining a GET endpoint for the root URL
def root():
    # Returning a welcome message
    return {"message": "Fraud detection API is up"}


@app.post("/predict")  # Defining a POST endpoint for making predictions
def predict(transactions: Transactions):
    # Reshaping the input features for prediction
    data = np.array(transactions.features).reshape(1, -1)
    # Scaling the input features using the loaded scaler
    data_scaled = scaler.transform(data)
    # Making a prediction using the loaded model
    prediction = model.predict(data_scaled)[0]
    # Getting the probability of the positive class
    probability = model.predict_proba(data_scaled)[0][1]
    return {
        # Returning whether the transaction is predicted as fraud or not
        "fraud": bool(prediction),
        # Returning the probability of the transaction being fraud
        "probability": float(probability)
    }
