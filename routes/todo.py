from fastapi import APIRouter, HTTPException
from models.todo import TodoUpdate, TodoItem
from storage.storage import todo_list

todo_router = APIRouter()




@todo_router.post("/todo", response_model=TodoItem)
async def add_todo(todo: TodoItem):
    # Проверяем уникальность id
    if any(t.id == todo.id for t in todo_list):
        raise HTTPException(status_code=400, detail="Task ID already exists")
    todo_list.append(todo)
    return todo

@todo_router.get("/todo/{task_id}", response_model=TodoItem)
async def get_todo(task_id: int):
    for t in todo_list:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")



@todo_router.put("/todo/{task_id}", response_model=TodoItem)
async def update_todo(task_id: int, todo: TodoUpdate):
    for t in todo_list:
        if t.id == task_id:
            if todo.task is not None:
                t.task = todo.task
            if todo.completed is not None:
                t.completed = todo.completed
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@todo_router.delete("/todo/{task_id}")
async def delete_todo(task_id: int):
    for i, t in enumerate(todo_list):
        if t.id == task_id:
            todo_list.pop(i)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
