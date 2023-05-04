from typing import Dict, Any
from sqlalchemy.orm import Session
from models.models import Transaction
from sqlalchemy import desc


class TransactionRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_transaction(self, transaction: Transaction) -> bool: 
        try:
            self.sess.add(transaction)
            self.sess.commit()
            print(transaction.transaction_id)
        except Exception as e:
            print(e) 
            return False 
        return True
    
    def update_transaction(self, transaction_id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Transaction).filter(Transaction.transaction_id == transaction_id).update(details)     
             self.sess.commit() 
       except Exception as e:
           print(e) 
           return False 
       return True
   
    def delete_transaction(self, transaction_id:int) -> bool: 
        try:
           signup = self.sess.query(Transaction).filter(Transaction.transaction_id == transaction_id).delete()
           self.sess.commit()
          
        except Exception as e: 
            print(e)
            return False 
        return True
    
    def get_all_transactions(self):
        return self.sess.query(Transaction).all() 
    
    def get_transaction(self, transaction_id:int): 
        return self.sess.query(Transaction).filter(Transaction.transaction_id == transaction_id).one_or_none()