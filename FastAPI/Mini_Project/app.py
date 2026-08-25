from fastapi import FastAPI, HTTPException,UploadFile,File
from pydantic import BaseModel, Field
from fastapi.responses import StreamingResponse
import joblib
import pandas as pd
import io

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

@app.post("/predict_file")
async def predict_file(file: UploadFile = File(...)): # Upload file is an object, async means python can work on something else while it waits
    if file.filename.endswith(".csv"):
        contents = await file.read() 
        df = pd.read_csv(io.BytesIO(contents)) # bytes io is used to read the binary content of the file into pandas read_csv
        required_features = features
        missing_feature = [
            feature for feature in required_features if feature not in df.columns # Columns which are required by model but not in the input file
        ]
        extra_feature = [
            feature for feature in df.columns if feature not in required_features # Extra features present in the input file which are not required by model
        ]
        if missing_feature:
            raise HTTPException(
                status_code=400,
                detail=f"Missing features: {', '.join(missing_feature)} not in input file"
            )
        if extra_feature:
            raise HTTPException(   
                status_code=400,
                detail=f"Extra features: {', '.join(extra_feature)}"
            )
        if len(df) == 0:
            raise HTTPException(
                status_code=400,
                detail="Input file is empty"
            )
        try:
            prediction = house_model.predict(df[features])
            df["Predicted Price"] = (prediction * 100000)
            df["Predicted Price"] = df["Predicted Price"].apply(lambda x : f"${x:,.0f}")
            output = df.to_csv(index = False)
            return StreamingResponse(
                io.StringIO(output),
                media_type = "text/csv",
                headers= {"Content-Disposition": "attachment; filename=predictions.csv"}
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Prediction Failed Due To : {str(e)}"
            )
    else:
        raise HTTPException(
            status_code=400,
            detail="Input file must be a CSV file"
        )

