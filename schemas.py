from typing import List, Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    content: str

class Task(TaskBase):
    user_id: int

    class Config:
        from_attributes = True

class TaskSimple(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    tasks: List[TaskSimple] = []

    class Config:
        from_attributes = True

class ShowTask(BaseModel):
    title: str
    content: str
    creator: Optional[ShowUser]

    class Config:
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username:Optional[str]= None