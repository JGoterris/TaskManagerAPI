from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    status: str = "todo"
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class UpdateTask(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None