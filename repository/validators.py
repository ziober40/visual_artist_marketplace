from models.models import Transaction


class TransactionValidator:
    
    def validate (self, transaction: Transaction) -> bool:

        if (transaction.buy_order.artwork_id != transaction.sell_order.artwork_id):
            print("Transaction attempts to trade two different artwork")
            return False

        if (transaction.buy_order.direction == transaction.sell_order.direction):
            print("Transaction attempts to trade same side orders")
            return False

        if (transaction.buy_order.direction == False) or (transaction.sell_order.direction == True):
            print("Buy order is not buy or sell order is not sell")
            return False

        if (transaction.buy_order.is_canceled) or (transaction.sell_order.is_canceled):
            print("One of the orders is cancelled already")
            return False

        if (transaction.buy_order.is_executed) or (transaction.sell_order.is_executed):
            print("One of the orders is executed already")
            return False

        return True

