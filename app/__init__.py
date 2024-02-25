from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: int
    title: str
    Description: str

class Task_up(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    Description: Optional[str] = None

app = FastAPI()