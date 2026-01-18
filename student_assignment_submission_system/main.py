from fastapi import FastAPI
# Importing Post routers
from routers.post_routers.teacher import teacher_router
from routers.post_routers.student import student_router
from routers.post_routers.assignments import assignment_router
from routers.post_routers.assignments_id_comment import assingment_comment_router
# Importing Get routers
from routers.get_routers.student_name_assignments import assignment_student_router
from routers.get_routers.assignments import get_assignment_router


app = FastAPI()


@app.include_router(teacher_router, prefix="/teacher", tags=["Teacher Register"])
@app.include_router(student_router, prefix="/student", tags=["Student Register"])
@app.include_router(assignment_router, prefix="/assignment", tags=["Assignment Create"])
@app.include_router(assingment_comment_router, prefix="/assignment/comment", tags=["Comment on Assignments"])
@app.include_router(assingment_student_router, tags=["Get Specific Student Assignments"])
@app.include_router(get_assignment_router, prefix="/assignments", tags=["Get All Submitted Assignments"])
