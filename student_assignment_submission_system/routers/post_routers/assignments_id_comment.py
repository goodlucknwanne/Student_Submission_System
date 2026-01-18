# Teacher adds a comment
from fastapi import APIRouter, HTTPException, status
from core.db import assignments_by_id
from models.comment import Comment
from models.assignment import Assignments

assignment_comment_router = APIRouter()

@assignment_comment_router.post(
    "/assignments/{assignment_id}/comments",
    response_model=Assignments,
    status_code=status.HTTP_201_CREATED
)
def add_comment(
    assignment_id: int,
    comment_data: CommentCreate
):

    assignment = assignments_by_id.get(assignment_id)

    if not assignment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assignment not found"
        )

    assignment.comments.append(comment_data.comment)

    return assignment
