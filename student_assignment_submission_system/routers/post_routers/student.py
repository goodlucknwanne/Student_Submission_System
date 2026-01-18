from fastapi import APIRouter
from schemas.models import Students, Student
from schemas.db import students_by_name


student_router = APIRouter()


# Create student
@student_router.post("/")
def create_student(student: Students):
    student_id = len(students_by_name) + 1

    student_dict: dict = student.model_dump()
    new_student: Student = Student(
        id=student_id,
        **student_dict
    )

    students_by_name[new_student.name] = new_student

    return new_student
