from const import URL, CHAT_ID
import requests


def change_params(name, oldPrice, newPrice, date1, date2, link):
    text = f"CHEAPER BY {round((oldPrice - newPrice), 2):.2f}zl!!!\nThe price of {name} has changed from {oldPrice}zl ({date1}) to {newPrice}zl ({date2})!!!\nLink: ceneo.pl{link}"
    params = {"chat_id": CHAT_ID,
              "text": text}
    return params

def lowest_in_month_params(name, price, link):
    text = f"The product: {name} currently has the lowest price in month: {price}.\nCheck it out: {link}"
    params = {"chat_id": CHAT_ID,
              "text": text}
    return params

def send_notification(params):
    r = requests.get(URL + "/sendMessage", params=params) 