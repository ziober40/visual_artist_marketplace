from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db_config.connect import SessionFactory
from models.requests import Direction, OrderRequest
from models.models import Order
from models.views import OrderView
from repository.order import OrderRepository
from typing import List


router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/order/add")
def add_signup(req: OrderRequest, sess:Session = Depends(sess_db)):
    repo:OrderRepository = OrderRepository(sess)

    order = Order(
        user_id = req.user_id, 
        artwork_id = req.artwork_id,
        price = req.price,
        direction = req.direction==Direction.buy,
        is_canceled =  False
        )
    
    result = repo.insert_order(order)
    if result == True:
        return order
    else: 
        return JSONResponse(content={'message':'create signup problem encountered'}, status_code=500)

def _parse_order_view(orders: List[Order]) -> List[OrderRequest]:
    return [OrderView(
        order_id=o.order_id,
        user_id=o.user_id,
        artwork_id=o.artwork_id,
        price=o.price,
        direction=Direction.buy if o.direction else  Direction.sell,
        is_canceled=o.is_canceled
    ) for o in orders]

@router.get("/order/list", response_model=List[OrderView])
def list_orders(sess:Session = Depends(sess_db)):
    repo:OrderRepository = OrderRepository(sess)
    result = repo.get_all_orders()

    return _parse_order_view(result)

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