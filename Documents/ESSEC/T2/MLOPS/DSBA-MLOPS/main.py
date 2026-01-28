from typing import Union

from fastapi import FastAPI
from BusinessLogic import return_logic_one as logic_return_one, return_logic_item as logic_return_item

app = FastAPI()


@app.get("/")
def read_root():
    return logic_return_one()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return logic_return_item(item_id, q)