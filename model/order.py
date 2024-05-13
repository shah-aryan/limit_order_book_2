class Order:
    def __init__(self, 
                 order_id: int, 
                 customer_id: int, 
                 order_volume: int, 
                 ticker: str, 
                 price: int, 
                 time_of_order: int, 
                 order_type: str,
                 buy_or_sell: str):
        
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_volume = order_volume
        self.ticker = ticker
        self.price = price
        self.time_of_order = time_of_order
        self.order_type = order_type
        self.buy_or_sell = buy_or_sell

    def __lt__ (self, other):
        if self.price == other.price:
            return self.time_of_order < other.time_of_order
        
        if self.buy_or_sell == "buy":
            return self.price > other.price
        elif self.buy_or_sell == "sell":
            return self.price < other.price
        else:
            print("Invalid")
            exit(1)


