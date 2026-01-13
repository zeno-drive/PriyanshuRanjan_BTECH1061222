from fastapi import APIRouter
from app.schemas.task import TaskCreate, TaskResponse

router=APIRouter()

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    return{
        "id":1,
        "title": task.title,
        "status": task.status
    }
