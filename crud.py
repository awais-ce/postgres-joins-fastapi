from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemes import *
from models import Teacher
from models import Student


def create_teacher(db  : Session  , teacherssdd : UpdateTeacher):
    db_teacherssdd = Teacher(name = teacherssdd.name , email = teacherssdd.email , phone = teacherssdd.phone , address = teacherssdd.address ,
                                qualification = teacherssdd.qualification , experience = teacherssdd.experience , subjects = teacherssdd.subjects , 
                                date_of_joining = teacherssdd.date_of_joining , designation = teacherssdd.designation ,
                                department = teacherssdd.department , salary = teacherssdd.salary , age = teacherssdd.age )
    db.add(db_teacherssdd)
    db.commit()
    db.refresh(db_teacherssdd)
    return db_teacherssdd

def get_teacher(db  :Session , teacher_id : int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

def update_teacher(db: Session, teacher_id: int, teacherssdd: UpdateTeacher):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if db_teacher is None:
        return None  
    
    db_teacher.name = teacherssdd.name
    db_teacher.email = teacherssdd.email
    db_teacher.phone = teacherssdd.phone
    db_teacher.address = teacherssdd.address
    db_teacher.qualification = teacherssdd.qualification
    db_teacher.experience = teacherssdd.experience
    db_teacher.subjects = teacherssdd.subjects
    db_teacher.date_of_joining = teacherssdd.date_of_joining
    db_teacher.designation = teacherssdd.designation
    db_teacher.department = teacherssdd.department
    db_teacher.salary = teacherssdd.salary
    db_teacher.age = teacherssdd.age
    
    db.commit()
    db.refresh(db_teacher)
    
    return db_teacher


def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404 , detail="Data Does Not Found")
    db.delete(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher





def create_student(db  : Session  , studentsss : UpdateStudent):
    db_student = Student(name = studentsss.name , 
                         email = studentsss.email , 
                         phone = studentsss.phone , 
                         address = studentsss.address ,
                         date_of_birth = studentsss.date_of_birth,
                         department = studentsss.department , 
                         age = studentsss.age ,
                         cnic = studentsss.cnic,
                         city = studentsss.city
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db  :Session , student_id : int):
    return db.query(Student).filter(Student.id == student_id).first()

def update_student(db: Session, teacher_id: int, studentsss: UpdateStudent):
    db_student = db.query(Student).filter(Student.id == teacher_id).first()
    
    if db_student is None:
        return None  
    db_student.name = studentsss.name
    db_student.email = studentsss.email
    db_student.phone = studentsss.phone
    db_student.address = studentsss.address
    db_student.department = studentsss.department
    db_student.age = studentsss.age
    db_student.date_of_birth = studentsss.date_of_birth
    db_student.city = studentsss.city
    db_student.cnic = studentsss.cnic
    db.commit()
    db.refresh(db_student)
    
    return db_student


def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404 , detail="Data Does Not Found")
    db.delete(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student




    

