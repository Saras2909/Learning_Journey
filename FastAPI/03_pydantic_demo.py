from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()
 
class Application(BaseModel): #Form
    name:str
    age:int
    dob:str
    salary:float
    occupation:str
    
@app.post("/home") #To post data to the server
def General_Application(application:Application):
    return application

