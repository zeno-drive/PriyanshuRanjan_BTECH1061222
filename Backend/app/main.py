from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.database import engine, Base
load_dotenv()

app=FastAPI(title=os.getenv("APP_NAME"))

@app.get("/")
def root():
    return{"message":"Backend is running"}