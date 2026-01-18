from fastapi import APIRouter, status
from models.db import teachers_by_name
from models.models import Teacher

teacher_router = APIRouter()

# register a teacher 
@teacher_router.post("/", status_code=status.HTTP_CREATED_201)
def create_teacher(teacher_data: Teacher):
    teacher: dict = teacher_data.model_dump()
    new_teacher: Teacher = Teacher(
        name = teacher.name,
        email = teacher.email
    )
    teachers_by_name[teacher.name] = new_teacher
    
    return {"message": "Teacher registered successfully", "data": new_teacher}
    