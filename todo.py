from fastapi import APIRouter

todo_router = APIRouter()

# Хранилище задач (пока в памяти)
todo_list = []

@todo_router.post("/todo")  # Добавление задачи
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@todo_router.get("/todo")  # Получение всех задач
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
