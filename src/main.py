from app import *
from const import SORTED_BY_PRICE, TWO_HOURS, connection
import time
from dbanalyzer import check_products, lowest_in_month


def main():
    path = getPath()
    executeMultiple(SORTED_BY_PRICE, path)
    check_products()
    lowest_in_month()
    
if __name__ == "__main__":
    try:
        while True:
            main()
            time.sleep(TWO_HOURS)
        
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Closing the program.")
        connection.close()
        print("Connection closed")



