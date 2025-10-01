from fastapi import APIRouter
from pydantic import BaseModel

todo_router = APIRouter()

class TodoItem(BaseModel):
    task: str 