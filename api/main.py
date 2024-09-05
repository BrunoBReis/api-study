from fastapi import FastAPI

app = FastAPI()

@app.get("/get-message")
async def get_message():
    content = {
        "message": "Hello, World!"
    }
    return content

@app.get("/get-message/{message}")
async def get_message(message: str):
    content = {
        "message": message
    }
    return content