import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

from api.led_matrix import Max7219


app = FastAPI()
my_led_matrix = Max7219(4)


class Matrix(BaseModel):
    matrix: List[List[int]] = []


@app.get("/")
def root_handler():
    return {"message": "Hello World"}


@app.post("/matrix")
def get_matrix(data: Matrix):
    my_led_matrix.set_matrix(data.matrix)
    return {
        "status": "SUCCESS",
        "data": data
    }


@app.get("/matrix")
def get_string(message: str, scroll_speed: float = 0):
    my_led_matrix.print(message, scroll_speed)
    return {
        "status": "SUCCESS",
        "data": {
            "message": message,
            "scroll": scroll_speed
        }
    }


if __name__ == "__main__":
    uvicorn.run("api:app", host='127.0.0.1', port=5000, log_level="info")
