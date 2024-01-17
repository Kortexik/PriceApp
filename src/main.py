
from app import *
from const import SORTED_BY_PRICE, THREE_HOURS
import time
from dbanalyzer import check_products



items_to_check= ["szczoteczka smilesonic", "iphone 14", 'chromecast', 'playstation 5', 'lego lamborghini', 'lego orchidea', 'lego bonsai']


def main():
    path = getPath()
    executeMultiple(SORTED_BY_PRICE, path)
    check_products()
    


if __name__ == "__main__":
        main()
        #time.sleep(THREE_HOURS)





