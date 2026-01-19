from pydantic import BaseModel

class Teacher(BaseModel):
  teacher_name: str
  subject: str
  
  
  comments: list[str] = []



  class Assignment(Assignments):
    id: int
