from pydantic import BaseModel, ConfigDict
from datetime import datetime

class BaseSchema(BaseModel):
    ...

class PostCreateSchema(BaseSchema):
    title: str
    content: str

class PostSchema(PostCreateSchema):
    id: int
    created_at: datetime