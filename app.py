from fastapi import FastAPI, Request
import json

app = FastAPI()

def get_usernames():
    with open("users.json", "r", encoding="utf-8") as f:
        l = json.load(f)
        return set(x["username"] for x in l)

@app.post("/users")
async def create_user(request: Request):
    user_data = await request.json()
    username = user_data.get("username")
    if not username:
        return {"error": "Username is required"}
    fullname = user_data.get("fullname")
    if not fullname:
        return {"error": "Fullname is required"}
    age = user_data.get("age")
    if not age or not isinstance(age, int):
        return {"error": "Age is required as int"}
    usernames = get_usernames()
    if username in usernames:
        return {"error": "Username is taken"}

    
    
    