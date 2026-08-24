from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class Person(BaseModel):
    age:int
    gender:str
    bmi:float
    children:int
    smoker:str
    region:str
    severity:str
    
@app.post('/form')
def Health_Insurance(insurance:Person):
    gender = ["male","female"]
    region = ["southwest","southeast","northwest","northeast"]
    severity = ["minimal","moderate","severe","high"]
    
    if insurance.gender not in gender:
        return {"message":"Enter correct gender"}

    elif insurance.region not in region:
        return {"message":"Enter correct region"}

    elif insurance.severity not in severity:
        return {"message":"Enter correct severity"}

    if(insurance.age < 0 and insurance.age > 150):
        return {"message":"Enter the correct age"}

    elif(insurance.children < 0):
        return {"message":"Children cannot be negative"}

    elif(insurance.bmi < 0 and insurance.bmi > 100):
        return {"message":"Enter Correct BMI"}

    elif(insurance.age <= 25 and insurance.children==0 and insurance.smoker=="no" and insurance.severity=="minimal" and insurance.gender=="female"):
        return {"premium":12500}




