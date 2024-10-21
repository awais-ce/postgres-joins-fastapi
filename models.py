from sqlalchemy import String , Integer , Column , Date
from database import *

class Teacher(Base):
    __tablename__ = "teacherssdd"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    qualification = Column(String)
    experience = Column(String)
    subjects  = Column(String)
    date_of_joining = Column(Date)
    designation = Column(String)
    department = Column(String)
    salary = Column(Integer)
    age = Column(Integer)
    

class Student(Base):

    __tablename__ = "studentsss"
    id = Column(Integer  , primary_key = True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    age = Column(Integer)
    address = Column(String)
    cnic = Column(Integer)
    city = Column(String)
    date_of_birth = Column(Date)
    department = Column(String)
    
    





