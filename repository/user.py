from typing import Dict, Any
from sqlalchemy.orm import Session
from models.models import User
from sqlalchemy import desc


class UserRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_user(self, user: User) -> bool: 
        try:
            self.sess.add(user)
            self.sess.commit()
        except: 
            return False 
        return True
    
    def update_user(self, user_id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(User).filter(User.user_id == user_id).update(details)     
             self.sess.commit() 
       except: 
           return False 
       return True
   
    def delete_user(self, user_id:int) -> bool: 
        try:
           signup = self.sess.query(User).filter(User.user_id == user_id).delete()
           self.sess.commit()
          
        except: 
            return False 
        return True
    
    def get_all_users(self):
        return self.sess.query(User).all() 
    
    def get_user(self, user_id:int): 
        return self.sess.query(User).filter(User.user_id == user_id).one_or_none()