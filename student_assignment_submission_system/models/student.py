from pydantic import BaseModel

class Students(BaseModel):
    name: str
    email: str

class Student(Students):
    id: int
