from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from db.models.task import Task, UpdateTask
from db.schemas.task import task_schema, tasks_schema
from datetime import datetime
from bson import ObjectId
import logging

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/")
async def getTasks():
    return tasks_schema(db_client.local.tasks.find())

@router.get("/{id}")
async def getTask(id: str):
    return search_task("_id", ObjectId(id))

@router.get("/filter/{status}")
async def getFilteredTasks(status: str):
    return tasks_schema(db_client.local.tasks.find({"status": status}))

@router.post("/")
async def addTask(task: Task):
    task_dict = dict(task)
    del task_dict["id"]
    task_dict["createdAt"] = datetime.now()
    task_dict["updatedAt"] = datetime.now()

    id = db_client.local.tasks.insert_one(task_dict).inserted_id

    new_task = task_schema(db_client.local.tasks.find_one({"_id":id}))

    return Task(**new_task)

@router.put("/{id}")
async def updateTask(id: str, updateTask: UpdateTask):
    modificaciones = {"updatedAt": datetime.now()}
    if updateTask.name is not None:
        modificaciones["name"] = updateTask.name
    if updateTask.description is not None:
        modificaciones["description"] = updateTask.description
    if updateTask.status is not None:
        modificaciones["status"] = updateTask.status
    try:
        db_client.local.tasks.find_one_and_update({"_id": ObjectId(id)}, {"$set":modificaciones})
        return search_task("_id", ObjectId(id))
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")


def search_task(field: str, value):
    try:
        task = db_client.local.tasks.find_one({field: value})
        return Task(**task_schema(task))
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")