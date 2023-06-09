from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db_config.connect import SessionFactory
from models.requests import Direction, OrderRequest
from models.models import Order,Transaction
from models.views import OrderView
from repository.order import OrderRepository
from repository.transaction import TransactionRepository

from typing import List

import pandas as pd

router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/order/add")
def add_order(req: OrderRequest, sess:Session = Depends(sess_db)) -> OrderView:
    repo:OrderRepository = OrderRepository(sess)

    order = Order(
        user_id = req.user_id, 
        artwork_id = req.artwork_id,
        price = req.price,
        direction = req.direction==Direction.buy,
        is_canceled =  False,
        is_executed = False
        )
    
    result = repo.insert_order(order)
    if(result):
        matching_orders = repo.get_matching_orders(order)
        
        if(len(matching_orders)>0):

            transaction_candidate = matching_orders[-1] if order.direction else matching_orders[0]

            if(order.direction) and (order.price >= transaction_candidate.price):
                t_repo = TransactionRepository(sess)
                transaction = Transaction(
                    price = order.price, 
                    buy_order_id = order.order_id, 
                    sell_order_id = transaction_candidate.order_id, 
                    )
                t_repo.insert_transaction(transaction)

            if(not order.direction) and (order.price <= transaction_candidate.price):
                t_repo = TransactionRepository(sess)
                transaction = Transaction(
                    price = order.price, 
                    buy_order_id = transaction_candidate.order_id,
                    sell_order_id = order.order_id
                    )
                t_repo.insert_transaction(transaction)


    if result == True:
        return _parse_order_view(order)
    else: 
        return JSONResponse(content={'message':'create signup problem encountered'}, status_code=500)

def _parse_order_view(o: Order) -> OrderView:
    return OrderView(
        order_id=o.order_id,
        user_id=o.user_id,
        artwork_id=o.artwork_id,
        price=o.price,
        direction=Direction.buy if o.direction else  Direction.sell,
        is_canceled=o.is_canceled,
        is_executed=o.is_executed
    )

def _parse_order_views(orders: List[Order]) -> List[OrderView]:
    return [OrderView(
        order_id=o.order_id,
        user_id=o.user_id,
        artwork_id=o.artwork_id,
        price=o.price,
        direction=Direction.buy if o.direction else  Direction.sell,
        is_canceled=o.is_canceled,
        is_executed=o.is_executed
    ) for o in orders]

@router.get("/order/list", response_model=List[OrderView])
def list_orders(sess:Session = Depends(sess_db)):
    repo:OrderRepository = OrderRepository(sess)
    result = repo.get_all_orders()

    return _parse_order_views(result)

@router.get("/order/open", response_model=List[OrderView])
def open_orders(sess:Session = Depends(sess_db)):
    repo:OrderRepository = OrderRepository(sess)
    result = repo.get_open_orders()

    return _parse_order_views(result)

@router.get("/order/executed", response_model=List[OrderView])
def executed_orders(sess:Session = Depends(sess_db)):
    repo:OrderRepository = OrderRepository(sess)
    result = repo.get_executed_orders()

    return _parse_order_views(result)

@router.patch("/order/cancel/{id}")
async def cancel_order(order_id:int, sess:Session = Depends(sess_db)): 
    repo:OrderRepository = OrderRepository(sess)

    result = repo.cancel_order(order_id)
    
    if result: 
        return JSONResponse(content={'message':'order cancelled successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete order error'}, status_code=500)


@router.patch("/order/update") 
async def update_order(order_id:int, req:OrderRequest, sess:Session = Depends(sess_db)): 
    order_dict = req.dict(exclude_unset=True)

    print(order_dict)
    order_dict["direction"] = order_dict["direction"] == "sell" 

    repo:OrderRepository = OrderRepository(sess)
    result = repo.update_order(order_id, order_dict )
    if result: 
        return JSONResponse(content={'message':'Order updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update order error'}, status_code=500)

@router.delete("/order/delete/{id}") 
async def delete_order(order_id:int, sess:Session = Depends(sess_db)): 
    repo:OrderRepository = OrderRepository(sess)
    result = repo.delete_order(order_id)
    if result: 
        return JSONResponse(content={'message':'order deleted successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete order error'}, status_code=500)

@router.get("/order/get/{id}")
async def get_order(id:int, sess:Session = Depends(sess_db)): 
    repo:OrderRepository = OrderRepository(sess)
    result = repo.get_order(id)
    return result