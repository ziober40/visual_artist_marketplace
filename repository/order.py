from typing import Dict, Any
from sqlalchemy.orm import Session
from models.models import Order
from sqlalchemy import desc


class OrderRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_order(self, order: Order) -> bool: 
        try:
            self.sess.add(order)
            self.sess.commit()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    def cancel_order(self, order_id:int) -> bool: 
       try:
            order = self.sess.query(Order).get(order_id)
            if(order):
                order.is_canceled = True

            self.sess.commit() 
       except Exception as e: 
            print(e) 
            return False 
       return True

    def update_order(self, order_id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Order).filter(Order.order_id == order_id).update(details)     
             self.sess.commit() 
       except Exception as e: 
            print(e) 
            return False 
       return True
   
    def delete_order(self, order_id:int) -> bool: 
        try:
           signup = self.sess.query(Order).filter(Order.order_id == order_id).delete()
           self.sess.commit()
          
        except Exception as e: 
            print(e)
            return False 
        return True
    
    def get_all_orders(self):
        return self.sess.query(Order).all() 
    
    def get_order(self, order_id:int): 
        return self.sess.query(Order).filter(Order.order_id == order_id).one_or_none()