# View assignments from a specific student
from fastapi import APIRouter, HTTPException
from schemas.db import assignments_by_id, students_by_name

assignment_router = APIRouter()


@assignment_router.get("/students/{name}/assignments/")
def get_student_assignment(name: str):
    if name not in students_by_name:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student_assignment = [
        assignment for assignment in assignments_by_id.values() 
        if assignment.student_name == name
        ]
    
    return student_assignment
