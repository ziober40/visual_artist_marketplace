import typing
from enum import Enum
from pydantic import BaseModel

ArtworkId = typing.NewType("ArtworkId", int)
UserId = typing.NewType("UserId", int)
OrderId = typing.NewType("OrderId", str)
TransactionId = typing.NewType("TransactionId", str)

class Direction(str, Enum):
    buy = "buy"
    sell = "sell"

class OrderView(BaseModel):
    order_id: OrderId
    user_id: UserId
    artwork_id: ArtworkId
    price: float
    direction: Direction
    is_canceled: bool


class Transaction(BaseModel):
    transaction_id: TransactionId
    artwork_id: ArtworkId
    price: float
    buy_order_id: OrderId
    sell_order_id: OrderId

class OrderRequest(BaseModel):
    user_id: UserId
    artwork_id: ArtworkId
    price: float
    direction: Direction

class OrderResponse(BaseModel):
    order_id: OrderId

class CancelOrderRequest(BaseModel):
    order_id: OrderId

class CancelOrderResponse(BaseModel):
    is_canceled: bool

class OrderViewRequest(BaseModel):
    user_id: typing.Optional[UserId]

class OrderViewResponse(BaseModel):
    orders: typing.List[OrderView]

class TransactionViewRequest(BaseModel):
    user_id: UserId

class TransactionViewResponse(BaseModel):
    transactions: typing.List[Transaction]