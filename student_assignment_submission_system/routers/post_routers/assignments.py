from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException,
    status
)
from core.db import assignments_by_id
from models.comment import Comment
from models.assignment import Assignments
from pydantic import BaseModel
import os

assignment_router = APIRouter()


class CommentCreate(BaseModel):
    comment: str
    
ALLOWED_EXTENSIONS = {"pdf", "docx", "doc"}

@assignment_router.post(
    "/assignments",
    response_model=Assignment,
    status_code=status.HTTP_201_CREATED
)
def submit_assignment(
    student_name: str = Form(...),
    subject: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...)
):
    # Validate file extension
    file_extension = file.filename.split(".")[-1].lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Only PDF and Word documents are allowed."
        )

    assignment_id = len(assignments_by_id) + 1

   
    os.makedirs("uploads", exist_ok=True)

    file_path = f"media/uploads/{assignment_id}_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    new_assignment = Assignment(
        id=assignment_id,
        student_name=student_name,
        subject=subject,
        description=description,
        filename=file.filename,
        comments=[]
    )

    assignments_by_id[assignment_id] = new_assignment

    return {"message": "Assignment successfully uploaded", "data": new_assignment}
