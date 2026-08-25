from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI()
house_model = joblib.load("house_model.pkl")
features = joblib.load("house_features.pkl")

# Schema for the input
class Housefeatures(BaseModel):
    MedInc : float  = Field(gt=0 , description="Median income in block group")
    HouseAge : float = Field(gt=0, description="Median age of houses in block group")
    AveRooms : float = Field(gt=0, description="Average number of rooms in block group")
    AveBedrms : float = Field(gt=0, description="Average number of bedrooms in block group")
    Population : float = Field(gt=0, description="Population in block group")
    AveOccup : float = Field(gt=0, description="Average number of people per household")
    Latitude : float = Field(description="Latitude of block group")
    Longitude : float = Field(description="Longitude of block group")
     
# home
@app.get("/")
def home():
    return {
        "message" : "House Price Prediction is working.",
        "status" : "Running",
        "predict" : "to predict got to /predict",
        "docs" : "/docs"
    }

# model info
@app.get("/model")
def get_model_info():
    return {
        "status": "running",
        "model": "random forest regressor",
        "features": features,
        "avg_error": "25000"
    }

# predict    
 
@app.post("/predict")
def predict(Features: Housefeatures):
    try:
        house_data = Features.model_dump()
        input_data = pd.DataFrame([house_data])
        
        predicted = house_model.predict(input_data)
        price = float(predicted[0] * 100000)
        return {
            "Price in usd" : f"${price:,.0f}",
            "Confidence in range" : f"${(price - 25000):,.0f} to ${(price + 25000):,.0f}"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction Failed Due To : {str(e)}"
        )



