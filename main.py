import sys
from test.run_all_tests import run_all_tests
from model.exchange import Exchange
from controller.run_exchange import run_exchange
import json

def read_orders(inputFile, dict):
    #REQUIRED: input file is json
    with open(inputFile, "r") as json_file:
        data = json.load(json_file)
    #data is a dictionary with one key ("orders") that maps to a list of smaller order dictionaries
    orders = data["orders"]

    for order in orders:
        #creates exchange if one doesn't exist for the ticker
        #if one does exist it adds the order to the exchange
        exchange = order["ticker"]
        
        if exchange in dict:
            e = Exchange(exchange)
            e.add_order(order)
        else:
            dict["exchange"].add_order(order)


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
        
    
    
    read_orders(args[0], my_dict)

    # exchange = Exchange()
    # run_exchange(exchange)
    
if __name__ == "__main__":
    main()