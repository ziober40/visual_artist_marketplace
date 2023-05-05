from helper import *

def test_successfull_transaction():
   test_artwork = add_artwork(0)

   buy_price = 50
   sell_price = 100
   transact_price = 50

   test_user = add_user('test','test')
   test_buy_order = add_order(test_user['user_id'], test_artwork['artwork_id'], buy_price, "buy")
   test_sell_order = add_order(test_user['user_id'], test_artwork['artwork_id'], sell_price, "sell")
   test_transaction = add_transaction(transact_price, test_buy_order['order_id'], test_sell_order['order_id'])

   assert(isinstance(test_transaction['transaction_id'],int))


def test_transaction_two_different_artwork_ids():
    
    buy_price = 50
    sell_price = 100
    transact_price = 50
    
    test_artwork_1 = add_artwork(1)
    test_artwork_2 = add_artwork(2)
    test_user = add_user('test','test')
    test_buy_order = add_order(test_user['user_id'], test_artwork_1['artwork_id'], buy_price, "buy")
    test_sell_order = add_order(test_user['user_id'], test_artwork_2['artwork_id'], sell_price, "sell")
    test_transaction = add_transaction(transact_price, test_buy_order['order_id'], test_sell_order['order_id'])

    assert(test_transaction['message']=="create transaction problem encountered")


def test_one_side_only_transaction_error():
    test_artwork = add_artwork(0)
    
    buy_price = 50
    sell_price = 100
    transact_price = 50
    
    test_user = add_user('test','test')
    test_buy_order = add_order(test_user['user_id'], test_artwork['artwork_id'], buy_price, "buy")
    test_sell_order = add_order(test_user['user_id'], test_artwork['artwork_id'], sell_price, "buy")
    test_transaction = add_transaction(transact_price, test_buy_order['order_id'], test_sell_order['order_id'])
    
    assert(test_transaction['message']=="create transaction problem encountered")

def test_mixed_buy_side_error():
    test_artwork = add_artwork(0)
    
    buy_price = 50
    sell_price = 100
    transact_price = 50
    
    test_user = add_user('test','test')
    test_buy_order = add_order(test_user['user_id'], test_artwork['artwork_id'], 50, "sell")
    test_sell_order = add_order(test_user['user_id'], test_artwork['artwork_id'], 100, "buy")
    test_transaction = add_transaction(transact_price, test_buy_order['order_id'], test_sell_order['order_id'])
    
    assert(test_transaction['message']=="create transaction problem encountered")


def test_execute_same_order_twice_error():
    test_artwork = add_artwork(0)
    
    buy_price = 50
    sell_price = 100
    transact_price = 75
    
    test_user = add_user('test','test')
    test_buy_order = add_order(test_user['user_id'], test_artwork['artwork_id'], buy_price, "buy")
    test_sell_order = add_order(test_user['user_id'], test_artwork['artwork_id'], sell_price, "sell")
    test_transaction = add_transaction(transact_price, test_buy_order['order_id'], test_sell_order['order_id'])
    test_transaction_2 = add_transaction(transact_price, test_buy_order['order_id'], test_sell_order['order_id'])
    
    assert(test_transaction_2['message']=="create transaction problem encountered")

def test_order_is_cancelled_already():
    test_artwork = add_artwork(0)
    
    buy_price = 50
    sell_price = 100
    transact_price = 50
    
    test_user = add_user('test','test')
    
    
    
    test_buy_order = add_order(test_user['user_id'], test_artwork['artwork_id'], buy_price, "buy")
    test_sell_order = add_order(test_user['user_id'], test_artwork['artwork_id'], sell_price, "sell")
    
    cancel_order(test_buy_order['order_id'])
    
    test_transaction = add_transaction(transact_price, test_buy_order['order_id'], test_sell_order['order_id'])
    
    assert(test_transaction['message']=="create transaction problem encountered")