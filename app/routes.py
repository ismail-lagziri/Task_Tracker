from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

Tasks = {
    1: {
        "id": 1,
        "title": "Task_1",
        "Description": "Task_1 things",
    },
    2: {
        "id": 2,
        "title": "Task_2",
        "Description": "Task_2 things",
    }
}

class Task(BaseModel):
    id: int
    title: str
    Description: str

class Task_up(BaseModel):
    id: Optional[int]
    title: Optional[str]
    Description: Optional[str]

task = FastAPI()

@task.get("/")
def get_root():
    return {"Tasks_API":"Welcome"}

@task.post("/tasks/{task_id}")
def create_task(task_id: int, task: Task):
    if task_id in Tasks:
        return {"Error": "Task already exists"}
    Tasks[task_id] = task
    return task

@task.get("/tasks/{task_id}")
def read_task(task_id: int):
    if task_id in Tasks:
        return Tasks[task_id]
    return {"Error": "Not found"}

@task.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task_up):
    if task_id not in Tasks:
        return {"Error": "Not found"}
    if Tasks[task_id].id != None:
        Tasks[task_id].id = task.id
    if Tasks[task_id].title != None:
        Tasks[task_id].title = task.title
    if Tasks[task_id].Description != None:
        Tasks[task_id].Description = task.Description
    return task

@task.delete("/task/{task_id}")
def delete_task(task_id: int):
    if Tasks[task_id] not in Tasks:
        return {"Error": "Not found"}
    del(Tasks[task_id])
    return {"Message": "Task deleted successfully"}
    
