from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
    "1":{"name":"John","age":20,"subject":{"math":100,"science":90,"english":80,"history":70,"geography":60}},
    "2":{"name":"Jane","age":21,"subject":{"math":50,"science":80,"english":70,"history":70,"geography":50}},
    "3":{"name":"Bob","age":22,"subject":{"math":70,"science":50,"english":60,"history":90,"geography":50}},
    "4":{"name":"Alice","age":23,"subject":{"math":40,"science":60,"english":70,"history":80,"geography":50}},
    "5":{"name":"Charlie","age":24,"subject":{"math":80,"science":50,"english":70,"history":50,"geography":50}}
}

@app.get("/student/{student_id}")
def get_std(student_id:str):
    if student_id not in students:
        raise HTTPException(
            status_code=404, 
            detail=f"Student with ID {student_id} not found"
            )
    return students[student_id] #If a student id is not present we will need to handle the error
    
class subject_Mark(BaseModel):
    student_id:str
    name:str
    subject:str
    marks:int



@app.post("/subject-marks")
def post_marks(Marks:subject_Mark):
    if Marks.marks > 100 or Marks.marks < 0:
        raise HTTPException(
            status_code=400,
            detail=f"Marks should be between 0 and 100"
        )
    if Marks.student_id not in students:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {Marks.student_id} not found"
        )
    if Marks.subject not in students["subject"]:
        raise HTTPException(
            status_code=400,
            detail=f"Subject {Marks.subject} not found"
        )
    try:
        students[Marks.student_id]["subject"][Marks.subject] = Marks.marks
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error from server side: {e}"
        )
    return {"message":"Marks updated successfully"}
