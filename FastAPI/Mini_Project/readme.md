# California House Price Prediction API 🏡

A lightweight FastAPI service to predict house prices using a trained **Random Forest Regressor** model on the California Housing dataset.

## Project Structure

```text
Mini_Project/
├── app.py              # FastAPI application & endpoints
├── train.py            # Model training script
├── analyze.py          # Exploratory data analysis
├── house_model.pkl     # Saved Random Forest model
├── house_features.pkl  # Saved feature names list
└── readme.md           # Project documentation
```

## Features
- **Single Prediction (`POST /predict`)**: Validates input features via Pydantic schema and returns estimated USD price with confidence range.
- **Batch CSV Prediction (`POST /predict_file`)**: Accepts `.csv` file uploads, validates required columns, and streams back a CSV download with predicted prices.
- **Model Info (`GET /model`)**: Displays model metadata, active feature names, and error metrics.
- **Interactive Docs (`GET /docs`)**: Auto-generated Swagger UI for testing endpoints.

## Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | API status & health check |
| `GET` | `/model` | Model metadata & required features |
| `POST` | `/predict` | Predict single sample (JSON body) |
| `POST` | `/predict_file` | Predict batch samples (CSV upload) |

## Input Features
`MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`, `Population`, `AveOccup`, `Latitude`, `Longitude`

## How to Run

```bash
# 1. Install dependencies
pip install fastapi uvicorn pandas scikit-learn joblib pydantic

# 2. Start API server
uvicorn app:app --reload
```
Access interactive documentation at `http://127.0.0.1:8000/docs`.
