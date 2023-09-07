from fastapi import APIRouter
from models.students import Student
from config.database import connection
from schemas.students import listOfstudents, studentEntity
from bson import ObjectId

student_router = APIRouter()


@student_router.get('/students')
async def find_all_student():
    return listOfstudents(connection.local.student.find())

@student_router.get('/students/{student_id}')
async def find_student_id(student_id):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(student_id)}))

@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfstudents(connection.local.student.find())


@student_router.put('/students/{student_id}')
async def update_student(student_id, student: Student):
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(student_id)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(student_id)}))

@student_router.delete('/students/{student_id}')
async def delete_student(student_id):
    return studentEntity(connection.local.student.find_one_and_delete(
        {"_id": ObjectId(student_id)}
    ))
