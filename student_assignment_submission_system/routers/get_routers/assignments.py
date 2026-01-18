from fastapi import APIRouter
from typing import List
from core.db import assignments_by_id

router = APIRouter()


@router.get("/assignments")
async def get_assignments():
        return list(assignments_by_id.values())