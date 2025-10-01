from fastapi import APIRouter

todo_router = APIRouter()


todo_list: list[TodoItem] = []

@todo_router.post("/todo")
async def add_todo(todo: TodoItem) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": [t.model_dump() for t in todo_list]}