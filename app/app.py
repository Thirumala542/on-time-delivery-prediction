# app.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model and encoders
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

# Define input schema
class ShipmentFeatures(BaseModel):
    Warehouse_block: str
    Mode_of_Shipment: str
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: float
    Prior_purchases: int
    Product_importance: str
    Gender: str
    Discount_offered: float
    Weight_in_gms: float

@app.post("/predict")
def predict_delivery(data: ShipmentFeatures):
    # Convert input to DataFrame
    input_data = data.dict()
    
    # Apply label encoding
    for col in ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']:
        input_data[col] = encoders[col].transform([input_data[col]])[0]
    
    # Feature order
    features = [
        "Warehouse_block", "Mode_of_Shipment", "Customer_care_calls", "Customer_rating",
        "Cost_of_the_Product", "Prior_purchases", "Product_importance", "Gender",
        "Discount_offered", "Weight_in_gms"
    ]
    
    # Prediction
    X_input = np.array([input_data[feature] for feature in features]).reshape(1, -1)
    prediction = model.predict(X_input)[0]
    
    return {"Reached_on_Time": bool(prediction)}
