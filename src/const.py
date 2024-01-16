import json

with open("config.json") as config_file:
    config_data =  json.load(config_file)

CHAT_ID = config_data.get('CHAT_ID', '')
TOKEN = config_data.get('TOKEN', '')
URL = f"https://api.telegram.org/bot{TOKEN}"


sort_price_desc = ";0112-0.htm"
URLS = ['https://www.ceneo.pl/;szukaj-szczoteczka+elektryczna+smilesonic+ex', 'https://www.ceneo.pl/Smartfony;szukaj-iphone+15', 
        'https://www.ceneo.pl/Sprzet_RTV;szukaj-google+chromecast+4k', 'https://www.ceneo.pl/Smartfony;szukaj-iphone+14',
        'https://www.ceneo.pl/Konsole_do_gier;szukaj-playstation+5', 'https://www.ceneo.pl/Konsole_do_gier;szukaj-xbox+series+s'
        'https://www.ceneo.pl/;szukaj-szczoteczka+elektryczna+seysso+gold?', 'https://www.ceneo.pl/;szukaj-lego+bonsai', 'https://www.ceneo.pl/;szukaj-lego+orchidea', 
        'https://www.ceneo.pl/;szukaj-lego+lamborghini']

SORTED_BY_PRICE = [url + sort_price_desc for url in URLS]   #shows results based on lowest price if added to url
THREE_HOURS = 3600 * 3
HOUR = 3600

folder_path = '..\\Data'





