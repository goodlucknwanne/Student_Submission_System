from pydantic import BaseModel
from datetime import datetime

class Comment(BaseModel):
    id: int                  
    comment: str            
    created_at: datetime    