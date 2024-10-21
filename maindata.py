from fastapi import FastAPI , Depends ,HTTPException
from schemes import UpdateTeacher
from sqlalchemy.orm import Session
from database import *
from crud import *


app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)



@app.post("/teacherssdd/create")
async def create_teacher_api(teacherssdd : UpdateTeacher , db : Session = Depends(get_db)):
    return create_teacher(db ,teacherssdd)


@app.get("/teacherssdd/{teacher_id}")
async def get_teacher_api(teacher_id : int , db  :Session = Depends(get_db)):
    db_teacher =  get_teacher(db , teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404 , detail="Teacher Data Not Found")
    
    return db_teacher

@app.post("/teacherssdd/update")
async def update_teacher_api(teacher_id  : int , teacherssdd : UpdateTeacher , db  :Session = Depends(get_db)):
    db_teacher = update_teacher(db, teacher_id, teacherssdd)
    if db_teacher is None:
        raise HTTPException(status_code=404 , detail = "Teacher Data Not Found")
    
    return db_teacher

@app.post("/teacherssdd/delete")
async def delete_teacher_api(teacher_id  : int , db  :Session = Depends(get_db)):
    db_teacher = delete_teacher(db, teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404 , detail = "Teacher Data Not Found")
    
    return db_teacher



@app.post("/studentsss/create")
async def create_student_api(studentsss : UpdateStudent , db : Session = Depends(get_db)):
    return create_student(db ,studentsss)


@app.get("/studentsss/{student_id}")
async def get_student_api(student_id : int , db  :Session = Depends(get_db)):
    db_student =  get_student(db , student_id)
    if db_student is None:
        raise HTTPException(status_code=404 , detail="Student Data Not Found")
    
    return db_student

@app.post("/studentsss/update")
async def update_student_api(student_id  : int , studentsss : UpdateStudent , db  :Session = Depends(get_db)):
    db_student = update_student(db, student_id, studentsss)
    if db_student is None:
        raise HTTPException(status_code=404 , detail = "Student Data Not Found")
    
    return db_student

@app.post("/studentsss/delete")
async def delete_student_api(student_id  : int , db  :Session = Depends(get_db)):
    db_student = delete_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404 , detail = "Student Data Not Found")
    
    return db_student



