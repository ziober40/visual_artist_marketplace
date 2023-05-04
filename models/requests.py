import string
import typing
from typing import Any

from pydantic import BaseModel, validator
from models.models import Direction

# TODO: implement this:
# ArtworkId = typing.NewType("ArtworkId", int)
# UserId = typing.NewType("UserId", int)
# OrderId = typing.NewType("OrderId", int)
# TransactionId = typing.NewType("TransactionId", int)
# class TransactionRequest(BaseModel):
#     user_id: UserId
# class OrderRequest(BaseModel):
#     user_id: UserId
#     artwork_id: ArtworkId
#     price: float
#     direction: Direction
# class CancelOrderRequest(BaseModel):
#     order_id: OrderId


class OrderRequest(BaseModel):
    user_id: Any
    artwork_id: Any
    price: float
    direction: Direction

    class Config:
        orm_mode = True


class TransactionRequest(BaseModel):
    price: float
    buy_order_id: Any
    sell_order_id: Any

    class Config:
        orm_mode = True
        
class UserRequest(BaseModel):
    firstname: str
    lastname: str

    class Config:
        orm_mode = True

class ArtworkRequest(BaseModel):
    description_id: int

    class Config:
        orm_mode = True