from model.exchange import Exchange
from util.process_order import process_order
import json

def test_setup(test_name: str) -> Exchange:
    exchange = Exchange() 
    orders_file = open(f'resources/{test_name}_orders.json')
    orders = json.load(orders_file)
    
    for raw_order in orders:
        order = process_order(raw_order)
        exchange.orders.append(order)    
    
    orders_file.close()