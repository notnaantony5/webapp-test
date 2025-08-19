from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, func
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
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self):
        return f"<PostModel id={self.id}, title={self.title}>"

def create_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()