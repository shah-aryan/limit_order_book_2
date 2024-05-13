from queue import PriorityQueue
from queue import Queue
from order import Order

class Exchange: 
    def __init__(self, ticker):
        self.buys = PriorityQueue()
        self.sells = PriorityQueue()
        self.order_queue = Queue()
        self.ticker = ticker
        self.start_price = 75
    
    def add_order(self, order: Order):
        self.order_queue.append(Order)
        if Order.buy_or_sell == "buy":
            self.buys.append(Order)
        elif Order.buy_or_sell == "sell":
            self.sells.append(Order)
        else:          
            print("Invalid buy_or_sell type")
            exit(1)
    



    