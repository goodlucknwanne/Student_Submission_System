from fastapi import APIRouter, status
from models.db import teachers_by_name
from models.teacher import Teachers, Teacher

teacher_router = APIRouter()

# register a teacher 
@teacher_router.post("/", status_code=status.HTTP_CREATED_201)
def create_teacher(teacher_data: Teacher):
    teacher_dict: dict = teacher_data.model_dump()
    new_teacher: Teacher = Teacher(
        name = teacher_dict["name"],
        email = teacher_dict["email"]
    )
    teachers_by_name[teacher_dict["name"]] = new_teacher
    
    return {"message": "Teacher registered successfully", "data": new_teacher}
    
