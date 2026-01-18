from fastapi import APIRouter, HTTPException, status
from models.database import assignments_by_id, teachers_by_name
from models.models import Assignment
from schemas.assignment import AssignmentCreate, AssignmentResponse

assignment_router = APIRouter()

#post an assignment
@assignment_router.post("/assignments", response_model=AssignmentResponse, status_code=status.HTTP_201_CREATED)

def create_assignment(assignment: AssignmentCreate):
    # Checking if teacher exists
    if assignment.teacher_name not in teachers_by_name:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    # Generate assignment ID
    assignment_id = len(assignments_by_id) + 1

    # Create assignment instance
    new_assignment = Assignment(
        id=assignment_id,
        title=assignment.title,
        description=assignment.description,
        teacher_name=assignment.teacher_name
    )

    # Save to DB
    assignments_by_id[assignment_id] = new_assignment

    return {"message": "Assignment created successfully", "data":new_assignment}
    