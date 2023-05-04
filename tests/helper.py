base_url = "http://127.0.0.1:8000/vam/"

import requests
import string
import random

def cancel_order(id, base_url="http://127.0.0.1:8000/vam/"):

    url = base_url + "order/cancel/{id}?order_id="+str(id)
    response = requests.patch(url)
    
    if response.status_code != 201:
        print(response.json())
    return response.json()

def generate_string(length = 20):
    return ''.join([random.choice(string.ascii_letters) for n in range(length)])

def get_random_side():
    return random.choice(['buy','sell'])

def add_random_artwork(n=1,base_url="http://127.0.0.1:8000/vam/"):
    for i in range(n):
        data = {
            "description_id": random.randint(100,1500),
        }
        url = base_url + "artwork/add"
        response = requests.post(url, json=data)
        # Handle the response
        if response.status_code != 200:
            print(response.json())
    return

def add_random_user(n=1,base_url="http://127.0.0.1:8000/vam/"):
    for i in range(n):
        data = {
            "firstname": generate_string(12),
            "lastname": generate_string(20),
        }
        url = base_url + "user/add"
        response = requests.post(url, json=data)
        # Handle the response
        if response.status_code != 200:
            print(response.json())
    return

def add_transaction(price, buy_order_id, sell_order_id, base_url="http://127.0.0.1:8000/vam/"):
    data = {
        "price": int(price),
        "buy_order_id": int(buy_order_id),
        "sell_order_id": int(sell_order_id)
    }
    
    url = base_url + "transaction/add"
    
    response = requests.post(url, json=data)
    # Handle the response
    if response.status_code != 200:
        print(response.json())
    
    return response.json()

def add_artwork(description_id,base_url="http://127.0.0.1:8000/vam/"):
    data = {
        "description_id": description_id,
    }
    url = base_url + "artwork/add"
    response = requests.post(url, json=data)
    # Handle the response
    if response.status_code != 200:
        print(response.json())
    return response.json()


def add_user(firstname, lastname, base_url="http://127.0.0.1:8000/vam/"):
    data = {
        "firstname": firstname,
        "lastname": lastname,
    }
    url = base_url + "user/add"
    response = requests.post(url, json=data)
    
    if response.status_code != 200:
        print(response.json())
    return response.json()


def add_order(user_id,artwork_id, price, direction, base_url="http://127.0.0.1:8000/vam/"):
    data = {
        "user_id": int(user_id),
        "artwork_id": int(artwork_id),
        "price": int(price),
        "direction": direction
    }
    
    url = base_url + "order/add"
    
    response = requests.post(url, json=data)
    # Handle the response
    if response.status_code != 200:
        print(response.json())
    
    return response.json()
