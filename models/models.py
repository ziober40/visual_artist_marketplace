from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, Boolean
from sqlalchemy.orm import relationship
from db_config.connect import Base
from enum import Enum

class Direction(str, Enum):
    buy = "buy"
    sell = "sell"


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    artwork_id = Column(Integer, ForeignKey('artworks.artwork_id'))
    price = Column(Float)
    direction = Column(Boolean)
    is_canceled = Column(Boolean)

    users = relationship('User', back_populates="orders")
    artworks =  relationship('Artwork', back_populates="orders")
    
class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    price = Column(Float)
    buy_order_id = Column(Integer, ForeignKey('orders.order_id'))
    sell_order_id = Column(Integer, ForeignKey('orders.order_id'))

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    orders = relationship('Order', back_populates="users")
    
class Artwork(Base):
    __tablename__ = 'artworks'

    artwork_id = Column(Integer, primary_key=True)
    description_id = Column(Integer)

    orders = relationship('Order', back_populates='artworks')