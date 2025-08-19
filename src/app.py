from fastapi import FastAPI, HTTPException, status
from schemas import PostCreateSchema, PostSchema
from database import session_maker, PostModel
from sqlalchemy.exc import IntegrityError

app = FastAPI()

@app.get("/posts")
def get_all_posts() -> list[PostSchema]:
    with session_maker() as session:
        posts = session.query(PostModel).all()
        print(posts[0].__dict__)
        return [PostSchema(**post.__dict__) for post in posts]

@app.get("/posts/{post_id}")
def get_post_by_id(post_id: int) -> PostSchema:
    with session_maker() as session:
        post = session.query(PostModel
            ).filter(PostModel.id == post_id).first()
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
        return PostSchema(**post.__dict__)
    
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_new_post(post_data: PostCreateSchema) -> PostSchema:
    with session_maker() as session:
        try:
            post = PostModel(**post_data.model_dump())
            session.add(post)
            session.flush()
            result = PostSchema(**post.__dict__)
            session.commit()
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="title is taken")
        return result