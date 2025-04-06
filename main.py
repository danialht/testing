r"""Dump Your Thoughts using Fast API"""
from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

all_messages = []

class Message(BaseModel):
    user: Annotated[str, Query(min_length = 5, max_length = 20, regex="^[a-z0-9]+$")]
    message: Annotated[str, Query(min_length=1)]

@app.get('/messages/')
async def read_messages():
    return all_messages

@app.post('/messages/')
async def send_message(message: Message):
    all_messages.append({"user": message.user, "message": message.message})
    return {"status": "success"}
