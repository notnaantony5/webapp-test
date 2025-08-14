from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from sqlite3 import connect, IntegrityError

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
    try:
        cur.execute("""INSERT INTO posts (title, content, created_at)
            VALUES (?, ?, ?)
        """, (post_data.title, post_data.content, datetime.now().isoformat()))
    except IntegrityError:
        raise HTTPException(status_code=400, detail="title already taken")
    conn.commit()
    cur.execute("""SELECT id, title, content, created_at FROM posts
    WHERE title = ?""", (post_data.title,))
    id_, title, content, created_at = cur.fetchone()
    return PostSchema(id=id_, title=title, content=content, created_at=datetime.fromisoformat(created_at)) 