from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from datetime import datetime

engine = create_engine("sqlite:///db.sqlite3")
session_maker = sessionmaker(engine)

class Base(DeclarativeBase):
    ...

class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)
    content: Mapped[str]
    created_at: Mapped[datetime]

def create_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()