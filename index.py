from fastapi import FastAPI
from routes.students import student_router

app=FastAPI()
app.include_router(student_router)
