import string
import typing
from typing import Any
from enum import Enum
from pydantic import BaseModel
from models.models import Direction

class ArtworkView(BaseModel):
    artwork_id: Any
    description_id: int

    class Config:
        orm_mode = True

class TransactionView(BaseModel):
    transaction_id: Any
    price: float
    buy_order_id: Any
    sell_order_id: Any

    class Config:
        orm_mode = True

class UserView(BaseModel):
    user_id: Any
    firstname: str
    lastname: str

    class Config:
        orm_mode = True


class OrderView(BaseModel):
    order_id: Any
    user_id: Any
    artwork_id: Any
    price: float
    direction: Direction
    is_canceled: bool