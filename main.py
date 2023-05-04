from fastapi import FastAPI

from api import artworks, orders, transactions, users

app = FastAPI()

app.include_router(artworks.router, prefix='/vam')
app.include_router(orders.router, prefix='/vam')
app.include_router(transactions.router, prefix='/vam')
app.include_router(users.router, prefix='/vam')