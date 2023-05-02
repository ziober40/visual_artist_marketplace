from sqlalchemy import create_engine, Column, Integer, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base


# DB part
engine = create_engine("sqlite:///vam.db")
Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    artwork_id = Column(Integer)
    price = Column(Float)
    direction = Column(Boolean)
    is_canceled = Column(Boolean)
    


