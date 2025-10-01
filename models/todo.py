from pydantic import BaseModel
from typing import Optional



class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool = False

class TodoUpdate(BaseModel):
    task: Optional[str] = None
    completed: Optional[bool] = None