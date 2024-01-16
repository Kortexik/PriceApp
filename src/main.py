
from app import *
from const import SORTED_BY_PRICE, THREE_HOURS
import time
from datanalazer import compare_prices



items_to_check= ["szczoteczka smilesonic", "iphone 14", 'chromecast', 'playstation 5', 'lego lamborghini', 'lego orchidea', 'lego bonsai']


def main():
    path = getPath()
    file = executeMultiple(SORTED_BY_PRICE, path)

    for item in items_to_check:
       compare_prices(file[8:], item)
    


if __name__ == "__main__":
        main()





