from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.database import engine, Base
from app.models.task import Task
from app.models.user import User
from app.routes import tasks, auth

load_dotenv()

# CREATE app FIRST
app = FastAPI(title=os.getenv("APP_NAME", "Task Management System"))

#  Create tables
Base.metadata.create_all(bind=engine)

# Register routers AFTER app is defined
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])


@app.get("/")
def root():
    return {"message": "Backend is running"}
