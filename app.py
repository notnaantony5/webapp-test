from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import json

class User(BaseModel):
    username: str
    fullname: str
    age: int

app = FastAPI()


def _get_users() -> list[dict]:
    with open("users.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_pydantic_users() -> list[User]:
    users = _get_users()
    return [
        User(**user)
        for user in users
    ]
def get_usernames():
    users = _get_users()
    return set(user["username"] for user in users)

def write_new_user(u: User):
    data = _get_users()
    data.append(u.model_dump())
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

@app.delete("/users/{username}")
async def delete_user(username: str):
    return {"message": f"Получено значение из части ендпоинта: {username}" }


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: User) -> User:
    usernames = get_usernames()
    if user_data.username in usernames:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail={"error": "Username is taken"}
            )
    write_new_user(user_data)
    return user_data
    
@app.get("/users", status_code=status.HTTP_200_OK)
async def get_all_users() -> list[User]:
    return get_pydantic_users()

    
    
    