from queue import PriorityQueue
from queue import Queue
from model.order import Order

class Exchange: 
    def __init__(self, ticker):
        self.buys = PriorityQueue()
        self.sells = PriorityQueue()
        self.ticker = ticker
    
    def add_order(self, order: Order):
        if order.buy_or_sell == "buy":
            self.buys.put(order)
        elif order.buy_or_sell == "sell":
            self.sells.put(order)
        else:          
            print("Invalid buy_or_sell type")
            exit(1)
        

    def handle_order(self):
        while 1:
            if self.buys.empty():
                return
            highest_buy = self.buys.queue[0]

            if self.sells.empty():
                return
            lowest_sell = self.sells.queue[0]

            if highest_buy.price < lowest_sell.price:
                return
            
            print("NEW TRANSACTION")
            print("Highest buy: ")
            print(highest_buy)
            print("Lowest sell: ")
            print(lowest_sell)
            print("\n")
            if highest_buy.order_volume > lowest_sell.order_volume:
                print("Filled order: " + str(lowest_sell.order_id) + " with " + str(highest_buy.order_id))
                highest_buy.order_volume -= lowest_sell.order_volume
                self.sells.get()
            elif highest_buy.order_volume < lowest_sell.order_volume:
                print("Filled order: " + str(highest_buy.order_id) + " with " + str(lowest_sell.order_id))
                lowest_sell.order_volume -= highest_buy.order_volume
                self.buys.get()
            else:
                self.buys.get()
                self.sells.get()
                print("Filled both orders: " + str(highest_buy.order_id) + " and " + str(lowest_sell.order_id))
            
            print("\n\n")




    