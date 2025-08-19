from pydantic import BaseModel
from datetime import datetime

class PostCreateSchema(BaseModel):
    title: str
    content: str

class PosSchema(PostCreateSchema):
    id: int
    created_at: datetime