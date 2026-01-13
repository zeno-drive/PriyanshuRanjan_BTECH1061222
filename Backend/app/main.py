from fastapi import FastAPI
app=FastAPI(title="Task Management System")

@app.get("/")
def root():
    return{"message":"Backend is running"}