from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.database import engine, Base
from app.models.task import Task


load_dotenv()
Base.metadata.create_all(bind=engine)
app=FastAPI(title=os.getenv("APP_NAME"))

@app.get("/")
def root():
    return{"message":"Backend is running"}