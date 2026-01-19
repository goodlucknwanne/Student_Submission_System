


class Teacher(BaseModel):
  student_name: str
  subject: str
  description: str
  filename: str
  comments: list[str] = []



  class Assignment(Assignments):
    id: int
