Take Home Assignment

You are tasked with the creation of an online art platform. This will be the latest and greatest virtual marketplace for visual artists to gain exposure and sell their work directly to customers and art collectors. For creators, it offers a place to put their inventory up for sale, and for customers, a place to browse and place orders for artwork.

The platform should expose an API through which customers will be able to participate in a two-way market: artists can offer items for sale, and customers can place orders to buy them. For simplicity's sake, we will refer to both of these actions as an order.

Participants from either side of the market need to be able to accomplish four main tasks:

 - Place an order
 - Cancel an order
 - View open orders
 - View completed orders

Additionally, there needs to be a way for a user to request all items available to be able to browse inventory.

In addition to exposing these APIs, the backend will be responsible for matching sell and buy orders to determine when they can be completed and for recording the transactions.

The Python code below contains the interfaces required to interact with the platform (does not necessarily have to be the entire solution; you can view this as the set of minimum requirements and expand upon them if needed).

```python
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


class Order(BaseModel):

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

    orders: typing.List[Order]


class TransactionViewRequest(BaseModel):

    user_id: UserId


class TransactionViewResponse(BaseModel):

    transactions: typing.List[Transaction]


async def send_order(order_request: OrderRequest) -> OrderResponse:
    pass


async def cancel_order(cancel_order_request: CancelOrderRequest) -> CancelOrderRequest:
    pass


async def view_orders(order_view_request: OrderViewRequest) -> OrderViewResponse:
    pass


async def view_transactions(transaction_view_request: TransactionViewRequest) -> TransactionViewResponse:
    pass
```

Your primary task is to write a backend service that implements these interfaces and be able to demonstrate how a client can use it. At minimum, you should be able to run the service locally and interact with it via HTTP requests. If you can demonstrate the functionality with a simple script, that's fine, or you may choose to implement a client that offers a lightweight GUI to a user.

Solution assumptions:
 - We do not care a lot about performance; focus on reliably and cleanly fulfilling the requirements described above.
 - We are not concerned with authentication; you may assume that a user who is able to make a given request is permissioned to do so.
 - Set up a database to persist orders and transactions data (Postgres, MySQL or similar).
 - State is kept in memory and built from the database.
 - Rely on existing Python frameworks to the extent possible: FastAPI (or similar) for the server side, httpx (or similar) for making requests, Django (or similar) if you choose a graphical client.

 Please ask as many clarifying questions as you like before starting your implementation. Have fun!
