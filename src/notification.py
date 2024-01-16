from const import URL, CHAT_ID
import requests


def change_params(name, oldPrice, newPrice, date1, date2, link):
    params = {"chat_id": CHAT_ID,
              "text": f"The price of {name} has changed from {oldPrice}zl ({date1}) to {newPrice}zl ({date2})!!!\nLink: ceneo.pl{link}"}
    return params



def send_notification(params):
    r = requests.get(URL + "/sendMessage", params=params)