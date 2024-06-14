import json
from mysqlinsert import create_mysql_connection

connection = create_mysql_connection()


with open("config.json") as config_file:
    config_data =  json.load(config_file)
    config_file.close()


CHAT_ID = config_data.get('CHAT_ID', '')
TOKEN = config_data.get('TOKEN', '')
URLS = config_data.get('URLS', '')


URL = f"https://api.telegram.org/bot{TOKEN}"


sort_price_desc = ";0112-0.htm" #used to sort the page by lowest price
SORTED_BY_PRICE = [url + sort_price_desc for url in URLS]   #shows results based on lowest price if sort_price_desc added to url


TWO_HOURS = 3600 * 2
PRICE_DROP_PERCENTAGE = config_data.get('PRICE_DROP_PERCENTAGE', '') #It will notify you about prices that are at least 10% cheaper than the old price




