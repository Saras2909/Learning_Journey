# 🎓 Learning Journey

Welcome to the **Learning Journey** repository! This repository represents my learning journey in Data Science and Machine Learning, documenting my hands-on practice, code experiments, and practical implementations.

---

## 🌟 Table of Contents

- [Overview](#-overview)
- [📁 Repository Structure](#-repository-structure)
- [🚀 Key Modules & Topics Covered](#-key-modules--topics-covered)
  - [1. FastAPI Foundations](#1-fastapi-foundations)
  - [2. California House Price Prediction (Mini Project)](#2-california-house-price-prediction-mini-project)
- [🛠️ Tech Stack & Tools](#%EF%B8%8F-tech-stack--tools)
- [⚙️ How to Run](#%EF%B8%8F-how-to-run)

---

## 🎯 Overview

This repository serves as a structured collection of code, notes, and projects tracking progressive milestones in Data Science and Machine Learning, from API development to model deployment.

---

## 📁 Repository Structure

```text
Learning_Journey/
├── FastAPI/
│   ├── 01_API.py                # Fundamentals: GET routes & rule-based POST predictions
│   ├── 02_path_parameter.py     # Path & Query parameter handling & combination
│   ├── 03_pydantic_demo.py      # Pydantic BaseModel request parsing & validation
│   ├── 04_health_insurance.py   # Business logic & complex input validation
│   ├── 05_error_handling.py     # HTTP exceptions & status codes (400, 404, 500)
│   ├── readme.md                # FastAPI module documentation
│   └── Mini_Project/            # End-to-End ML API Project
│       ├── app.py               # Production FastAPI service with single & CSV batch prediction
│       ├── train.py             # Random Forest model training on California Housing dataset
│       ├── analyze.py           # Exploratory dataset analysis
│       ├── house_model.pkl      # Serialized ML model artifact
│       ├── house_features.pkl   # Serialized feature set metadata
│       └── readme.md            # Mini Project documentation
└── readme.md                    # Root repository documentation
```

---

## 🚀 Key Modules & Topics Covered

### 1. FastAPI Foundations

Hands-on implementations mastering key backend and API development concepts in Python:

- **Routing & HTTP Methods**: Configured `@app.get()` and `@app.post()` endpoints running on Uvicorn.
- **Path & Query Parameters**: Extracted dynamic URL parameters (e.g., `/product/{category}`) and optional query parameters (e.g., `city`, `min_score`).
- **Data Validation (Pydantic)**: Defined strict request payloads using `BaseModel` for automatic type checking and response schema generation.
- **Domain Logic Implementations**:
  - *Loan Approval Engine*: Rule-based credit checking and loan approval logic (`01_API.py`).
  - *Health Insurance Calculator*: Multi-field validation for applicant demographics and health parameters (`04_health_insurance.py`).
- **Error Handling & Status Codes**: Leveraged `HTTPException` to return standard status codes (`400 Bad Request`, `404 Not Found`, `500 Internal Server Error`) with descriptive error messages (`05_error_handling.py`).

---

### 2. California House Price Prediction (Mini Project)

An end-to-end Machine Learning API serving housing price estimates.

- **Model Training**: Trained a `RandomForestRegressor` on the California Housing dataset using `scikit-learn` (`train.py`) and saved model artifacts (`.pkl`).
- **Single & Batch Predictions**:
  - `POST /predict`: Evaluates a single property feature vector (`MedInc`, `HouseAge`, `AveRooms`, `Latitude`, `Longitude`, etc.) to predict USD value with confidence intervals.
  - `POST /predict_file`: Processes `.csv` file uploads in bulk, validates column requirements, and returns a CSV download stream with predictions.
- **Model Metadata & Documentation**:
  - `GET /model`: Returns active feature dependencies, metrics, and model information.
  - OpenAPI / Swagger interactive documentation available live at `/docs`.

---

## 🛠️ Tech Stack & Tools

- **Language**: Python 3.x
- **Framework**: FastAPI, Uvicorn
- **Machine Learning & Data**: Scikit-Learn, Pandas, Joblib
- **Data Validation**: Pydantic
- **Documentation**: Markdown, OpenAPI / Swagger UI

---

## ⚙️ How to Run

### 1. Install Dependencies
```bash
pip install fastapi uvicorn pandas scikit-learn joblib pydantic
```

### 2. Run Learning Scripts
Navigate to the `FastAPI` directory and start any script with Uvicorn:
```bash
cd FastAPI
uvicorn 01_API:app --reload
```

### 3. Run the Mini Project API
```bash
cd FastAPI/Mini_Project
uvicorn app:app --reload
```

### 4. Interactive API Documentation
Access auto-generated interactive documentation in your browser at:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`
