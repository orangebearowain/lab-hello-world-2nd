from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GreetRequest(BaseModel):
    name: str

@app.get("/hello")
def hello():
    return { "message": "Hello, world!" }

@app.post("/greet")
def greet(data: GreetRequest):
    return { "message": f"Hello, {data.name}!" }