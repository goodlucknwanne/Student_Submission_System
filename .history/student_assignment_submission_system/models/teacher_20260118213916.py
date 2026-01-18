from pydantic import BaseModel

class Teachers(BaseModel):
  teacher_name: str
  email:str
  
  
class Teacher(Teachers):
    id:int  
