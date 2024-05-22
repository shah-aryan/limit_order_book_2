import sys
from test.run_all_tests import run_all_tests
from model.exchange import Exchange
from controller.run_exchange import run_exchange
import json
from util.process_order import process_order

def read_orders(inputFile, my_dict):
    #REQUIRED: input file is json
    with open(inputFile, "r") as json_file:
        data = json.load(json_file)
    #data is a dictionary with one key ("orders") that maps to a list of smaller order dictionaries
    orders = data["orders"]

    for order in orders:
        #creates exchange if one doesn't exist for the ticker
        #if one does exist it adds the order to the exchange
        exchange = order["ticker"]
        
        if exchange not in my_dict:
            e = Exchange(exchange)
            my_dict[exchange] = e
        
        o = process_order(order)
        my_dict[exchange].add_order(o)
        my_dict[exchange].handle_order()
        


def main():
    args = sys.argv[1:]

    my_dict = {}

    if len(args) == 1 and (args[0] == "--test" or args[0] == "-t"):  
        run_all_tests()
    
    if len(args) == 1 and (args[0] == "--help" or args[0] == "-h"):
        print("Usage: python main.py [options]")
        print("Options:")
        print("  -t, --test    Run all tests")
        print("  -h, --help    Show this help message and exit")
        return

    if len(args) > 2:
        print ("too many arguments")
        
    
    #testing read_orders and Exchange print
    read_orders(args[0], my_dict)

    for ticker in my_dict:
        e = my_dict[ticker]
        print(ticker)
        print("buys")
        while not e.buys.empty():
            print(e.buys.get())
        print("\n\nsells")
        while not e.sells.empty():
            print(e.sells.get())
        print("\n\n")

    # exchange = Exchange()
    # run_exchange(exchange)
    
if __name__ == "__main__":
    main()