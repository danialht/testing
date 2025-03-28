r"""Dump Your Thoughts using Fast API"""
from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

all_messages = []

@app.get('/messages/')
async def read_messages():
    return all_messages

@app.post('/messages/')
async def send_message(user: Annotated[str, Query(min_length = 5, max_length = 20, regex="^[a-z0-9]+$")] = "notgiven",
                       message: Annotated[str, Query(min_length=1)] = "notgiven"):
    all_messages.append({"user": user, "message": message})
    return {"status": "success"}
