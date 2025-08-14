from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from sqlite3 import connect

class CreatePostSchema(BaseModel):
    title: str
    content: str

class PostSchema(CreatePostSchema):
    id: int
    created_at: datetime

app = FastAPI()

@app.post("/posts")
async def create_post(post_data: CreatePostSchema) -> PostSchema:
    conn = connect("test.sqlite3")
    cur = conn.cursor()
    cur.execute("""INSERT INTO posts (title, content, created_at)
    VALUES (?, ?, ?)
    """, (post_data.title, post_data.content, datetime.now().isoformat()))
    conn.commit()
    return PostSchema(**post_data.model_dump(), created_at=datetime.now(), id=1)