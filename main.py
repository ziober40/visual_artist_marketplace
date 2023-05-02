
from fastapi import FastAPI, status, HTTPException

from repository.schemas import Base, engine, Order
from sqlalchemy.orm import Session

from models import *

Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Visual Artist Marketplace"}

@app.post("/order", status_code=status.HTTP_201_CREATED)
async def send_order(order_request: OrderRequest) -> OrderResponse:

    session = Session(bind=engine, expire_on_commit=False)
    order = Order(user_id=order_request.user_id, artwork_id = order_request.artwork_id, price = order_request.price, direction = order_request.direction==Direction.buy, is_canceled=False)
    session.add(order)
    session.commit()

    response = OrderResponse(order_id = order.order_id)
    return response

@app.delete("/order/{order_id}")
async def cancel_order(cancel_order_request: CancelOrderRequest) -> CancelOrderRequest:
    session = Session(bind=engine, expire_on_commit=False)

    order = session.query(Order).get(cancel_order_request.order_id)

    if(order):
        order.is_canceled = True
        session.commit()

    session.close()

    if not order:
        raise HTTPException(status_code=404, detail=f"orders under user {cancel_order_request.order_id} not found")
    
    return cancel_order_request


def parse_order_view(orders: typing.List[Order]) -> typing.List[OrderView]:
    return [OrderView(
        order_id=o.order_id,
        user_id=o.user_id,
        artwork_id=o.artwork_id,
        price=o.price,
        direction=Direction.buy if o.direction else  Direction.sell,
        is_canceled=o.is_canceled
    ) for o in orders]

#async def view_orders(order_view_request: OrderViewRequest) -> OrderViewResponse:
@app.get("/order/{user_id}")
async def view_orders(user_id: int) -> OrderViewResponse:

    session = Session(bind=engine, expire_on_commit=False)
    orders = session.query(Order).filter(Order.user_id == user_id)
    orders_view = parse_order_view(orders)

    if len(orders_view) == 0:
        raise HTTPException(status_code=404, detail=f"orders under user {id} not found")

    session.close()

    return OrderViewResponse(orders=orders_view)

@app.get("/transactions/")
async def view_transactions(transaction_view_request: TransactionViewRequest) -> TransactionViewResponse:
    pass
