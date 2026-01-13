from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app=FastAPI(title=os.getenv("APP_NAME","FastAPI APP"))

@app.get("/")
def root():
    return{"message":"Backend is running"}