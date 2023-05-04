from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db_config.connect import SessionFactory
from models.requests import TransactionRequest
from models.models import Transaction
from models.views import TransactionView
from repository.transaction import TransactionRepository
from typing import List


router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/transaction/add")
def add_transaction(req: TransactionRequest, sess:Session = Depends(sess_db)):
    repo:TransactionRepository = TransactionRepository(sess)

    transaction = Transaction(
        price = req.price, 
        buy_order_id = req.buy_order_id, 
        sell_order_id = req.sell_order_id, 
        )

    #TODO:
    # - check if order_ids exist
    # - check if any of the orders hasn't been cancelled
    # - check if price is between the range

    result = repo.insert_transaction(transaction)
    if result == True:
        return transaction
    else: 
        return JSONResponse(content={'message':'create transaction problem encountered'}, status_code=500)



@router.get("/transaction/list", response_model=List[TransactionView])
def list_transactions(sess:Session = Depends(sess_db)):
    repo:TransactionRepository = TransactionRepository(sess)
    result = repo.get_all_transactions()
    return result


@router.patch("/transaction/update") 
async def update_transaction(transaction_id:int, req:TransactionRequest, sess:Session = Depends(sess_db)): 
    transaction_dict = req.dict(exclude_unset=True)
    repo:TransactionRepository = TransactionRepository(sess)
    result = repo.update_transaction(transaction_id, transaction_dict )
    if result: 
        return JSONResponse(content={'message':'Transaction updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update transaction error'}, status_code=500)

@router.delete("/transaction/delete/{id}") 
async def delete_transaction(transaction_id:int, sess:Session = Depends(sess_db)): 
    repo:TransactionRepository = TransactionRepository(sess)
    result = repo.delete_transaction(transaction_id)
    if result: 
        return JSONResponse(content={'message':'transaction deleted successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete transaction error'}, status_code=500)

@router.get("/transaction/get/{id}")
async def get_transaction(id:int, sess:Session = Depends(sess_db)): 
    repo:TransactionRepository = TransactionRepository(sess)
    result = repo.get_transaction(id)
    return result