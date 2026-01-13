from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate, TaskResponse
from app.models.task import Task
from app.dependencies import get_db

router=APIRouter()

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db:Session= Depends(get_db)):
    new_task=Task(
        title=task.title,
        status=task.status
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
    
@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks