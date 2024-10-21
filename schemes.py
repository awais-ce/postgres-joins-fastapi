from pydantic import BaseModel 
from datetime import datetime

class UpdateTeacher(BaseModel):
    name : str
    email : str
    phone : str
    address : str
    qualification : str
    experience : str
    subjects : str
    date_of_joining : datetime
    designation : str
    department : str
    salary : int
    age : int
    


class UpdateStudent(BaseModel):
    name : str
    email : str
    phone : str
    age : int
    address : str
    cnic : int
    city : str
    date_of_birth : datetime
    department : str
    
    

