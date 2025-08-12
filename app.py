from fastapi import FastAPI, Request
from pydantic import BaseModel
import json

class User(BaseModel):
    username: str
    fullname: str
    age: int

app = FastAPI()

def get_usernames():
    with open("users.json", "r", encoding="utf-8") as f:
        l = json.load(f)
        return set(x["username"] for x in l)

def write_new_user(u: User):
    with open("users.json", "r", encoding="utf-8") as f:
        data: list = json.load(f)
    data.append(u.model_dump())
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

@app.post("/users")
async def create_user(user_data: User):
    usernames = get_usernames()
    if user_data.username in usernames:
        return {"error": "Username is taken"}
    write_new_user(user_data)
    return user_data
    

    
    
    