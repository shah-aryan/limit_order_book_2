from model.order import Order
import json

def process_order(order) -> Order:
    data = json.loads(order)
    o = Order(order_id=data["order_id"], 
              customer_id=data["customer_id"],
              order_volume=data["order_volume"],
              ticker=data["ticker"],
              price=data["price"],
              time_of_order=data["time_of_order"],
              order_type=data["order_type"])
          
    return o