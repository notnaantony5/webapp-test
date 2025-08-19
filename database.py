from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped
from datetime import datetime

engine = create_engine("sqlite3://db.sqlite3")
session_maker = sessionmaker(engine)

class PostModel(DeclarativeBase):
    __tablename__ = "posts"

    id: Mapped[int]
    title: Mapped[str]
    content: Mapped[str]
    created_at: Mapped[datetime]
