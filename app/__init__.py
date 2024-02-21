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
    id: Optional[int] = None
    title: Optional[str] = None
    Description: Optional[str] = None

app = FastAPI()