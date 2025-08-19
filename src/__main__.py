import uvicorn

def run():
    uvicorn.run("app:app", reload=True)

if __name__ == "__main__":
    run()