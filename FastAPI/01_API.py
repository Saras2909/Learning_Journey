from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
#TO run use uvicorn filename:app --reload

@app.get("/home")#Used to retrieve data from the server and travels thorugh URL
def root():
    return {"message": "Hello World"} 

class LoanApplication(BaseModel):
    age:int
    income:float
    loan_amount:float
    credit_score:int
    
@app.post("/predict")
def predict(application:LoanApplication):
    if application.credit_score>=750 and application.income>=30000 and application.loan_amount<=100000 and application.age<=65:
        decision = "Approved"
    else:
        decision = "Rejected"
    return {"decision":decision}
