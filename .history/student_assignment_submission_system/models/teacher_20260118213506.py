from pydantic import BaseModel

class Teachers(BaseModel):
  teacher_name: str
  subject: str
  email:str
  
  
class Teacher(Teachers):
    id:  
