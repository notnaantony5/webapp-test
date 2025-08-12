from fastapi import FastAPI, Request
import json

app = FastAPI()

def get_usernames():
    with open("users.json", "r", encoding="utf-8") as f:
        l = json.load(f)
        return set(x["username"] for x in l)

def write_new_user(user_data: tuple[str, str, int]):
    with open("users.json", "r", encoding="utf-8") as f:
        data: list = json.load(f)
    username, fullname, age = user_data
    data.append({"username": username, "fullname": fullname, "age": age})
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

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
    write_new_user((username, fullname, age))
    return {"username": username, "fullname": fullname, "age": age}
    

    
    
    