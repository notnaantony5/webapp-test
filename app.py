from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class CreatePostSchema(BaseModel):
    title: str
    content: str

class PostSchema(CreatePostSchema):
    id: int
    create_at: datetime

app = FastAPI()

@app.post("/posts")
async def create_post(post_data: CreatePostSchema) -> PostSchema:
    now = datetime.now()
    id_ = 1
    return PostSchema(**post_data.model_dump(), create_at=now, id=id_)