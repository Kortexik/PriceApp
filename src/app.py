from product import Produkt
import os
import requests as re
from bs4 import BeautifulSoup 
from datetime import datetime



def get_datetime():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H-%M-%S")
    formatted_date = current_time.strftime("%d.%m.%Y")

    return formatted_date + " " + formatted_time



#only ceneo
def connect_and_get_offers(url):
    div_to_skip = 'highlighted-offers js_category-list-body js_highlighted-offers js_highlighted-offers-container'
    html = re.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    offers = soup.find_all('div', class_='cat-prod-row__body')

    # Filter out divs with parent div having class 'x'
    filtered_offers = []
    for offer in offers:
        parent_div = offer.find_parent('div', class_=div_to_skip)
        if parent_div is None:
            filtered_offers.append(offer)

    return filtered_offers

def parse_currency_string(zl_str, gr_str):
    if " " in zl_str:
        new_zl = zl_str.replace(" ", "")
    else:
        new_zl = zl_str

    zl = float(new_zl.strip())
    gr = float(gr_str.replace(',', '.'))
    return zl + gr

def makeObjects(offers):
    newL = []
    for product in offers:
        nazwa = product.find('span', class_=lambda x: x != 'recommended-label' and x != 'new-label').text
        link = product.find('div', class_='cat-prod-row__foto').a['href']
        zlotowki = product.find('span', class_='value').text
        grosze = product.find('span', class_='penny').text
        pr = Produkt(nazwa, parse_currency_string(zlotowki, grosze), link)
        newL.append(pr)
    return newL

def getPath():
    return os.path.join("Data", f'{get_datetime()}.csv')


def writeToFile(listOfObjects, path):
    with open(path, 'a', encoding="utf-8") as file:
        for object in listOfObjects:
            file.write(f'{object.name}:{object.price}:{object.link}\n')

        file.close()



def executeDataMininig(url, path):
    offs = connect_and_get_offers(url)
    list_of_objects = makeObjects(offs)
    writeToFile(sorted(list_of_objects, key=lambda x: x.price, reverse=True), path)
    


def executeMultiple(urls, path):
    for url in urls:
        executeDataMininig(url, path)
    addHeader(path)
    return path


def addHeader(path):
    with open(path, 'r') as data:
        content = data.read()
        data.close()
    with open(path, 'w') as data:
        data.write("name:price:link\n")
        data.write(content)
        data.close()
