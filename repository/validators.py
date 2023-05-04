from models.models import Transaction


class TransactionValidator:
    
    def validate (self, transaction: Transaction) -> bool:

        if (transaction.buy_order.artwork_id != transaction.sell_order.artwork_id):
            raise Exception("Transaction attempts to trade two different artwork")


        return True

