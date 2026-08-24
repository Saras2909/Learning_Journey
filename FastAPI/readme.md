# FastAPI Learning Journey 🚀

Welcome to my FastAPI learning journey repository! In this collection of scripts, I explored the fundamentals of building fast, modern, and asynchronous web APIs in Python using **FastAPI**, **Pydantic**, and **Uvicorn**.

---

## 💡 What I Learned

1. **FastAPI Framework Basics**:
   - Setting up a FastAPI application instance (`FastAPI()`).
   - Defining route operations using HTTP methods (`@app.get()`, `@app.post()`).
   - Running local development servers using Uvicorn (`uvicorn filename:app --reload`).

2. **Routing & Parameters**:
   - **Path Parameters**: Extracting dynamic variables directly from the URL path.
   - **Query Parameters**: Handling optional or required search/filtering arguments in the URL query string.
   - Combining path and query parameters in a single endpoint.

3. **Data Validation with Pydantic**:
   - Defining structured request payloads using Pydantic's `BaseModel`.
   - Automatic type checking, payload validation, and request parsing for POST endpoints.

4. **Business Logic & Input Validation**:
   - Validating user input values (ranges, allowed categories like gender, region, severity).
   - Implementing custom evaluation rules (e.g., loan approval, health insurance premium calculation).

---

## 📁 File Implementations & Code Breakdown

Here is a breakdown of what I built and implemented in each file across this repository:

### 1. `API.py`
- **What I Implemented**:
  - Created a basic `@app.get("/home")` endpoint returning a JSON greeting.
  - Implemented a `@app.post("/predict")` endpoint accepting a `LoanApplication` Pydantic model (`age`, `income`, `loan_amount`, `credit_score`).
  - Added simple rule-based decision logic to approve or reject loan applications based on credit score, income, and loan amount limits.

### 2. `path_parameter.py`
- **What I Implemented**:
  - Implemented dynamic path parameter routes like `@app.get("/product/{category}")` to query nested product catalogs (Electronics, Clothing, Books, etc.).
  - Combined path parameters and query parameters to look up specific product prices dynamically.
  - Created a `@app.get("/users")` endpoint using query parameters (`city`, `min_score`) to filter a list of user profiles.
  - Handled optional query parameters with default values (`name: str | None = None`).

### 3. `pydantic_demo.py`
- **What I Implemented**:
  - Focused on understanding Pydantic `BaseModel` for structured data models (`Application` class with `name`, `age`, `dob`, `salary`, `occupation`).
  - Created a `@app.post("/home")` endpoint demonstrating how FastAPI automatically parses, validates, and echoes back Pydantic JSON bodies.

### 4. `health_insurance.py`
- **What I Implemented**:
  - Built a comprehensive health insurance calculator endpoint `@app.post("/form")`.
  - Created a `Person` Pydantic model (`age`, `gender`, `bmi`, `children`, `smoker`, `region`, `severity`).
  - Added manual validation logic to check valid ranges for age, BMI, children count, and specific categorical values (gender, region, severity).
  - Implemented initial premium evaluation logic based on applicant attributes.

### 5. `error_handling.py`
- **What I Plan to Implement**:
  - Reserved for exploring custom HTTP exceptions (`HTTPException`), status codes (`400`, `404`, `500`), and custom error responses in FastAPI.

---
