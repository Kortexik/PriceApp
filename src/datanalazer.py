import pandas as pd
import os
from const import folder_path
from datetime import datetime
from notification import change_params, send_notification
from product import Produkt
from typing import List

def are_these_words_in_name(words, sentence): 
    words_list = words.split()  # Split the words string into a list of words
    for word in words_list:
        if word.lower() not in sentence.lower():  # Compare case-insensitively
            return False
    return True


def getAllFileNames(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def find_closest_file(target_file, file_list):
    print("target file ," , target_file)
    target_time = datetime.strptime(target_file[:-4], '%d.%m.%Y %H-%M-%S')

    closest_file = None
    min_time_difference = float('inf')

    for file in file_list:

        current_time = datetime.strptime(file[:-4], '%d.%m.%Y %H-%M-%S')


        time_difference = abs((current_time - target_time).total_seconds())


        if time_difference < min_time_difference and file != target_file:
            min_time_difference = time_difference
            closest_file = file

    return closest_file

def days_ago(input_date_str):
    input_date = datetime.strptime(input_date_str, "%d.%m.%Y")
    current_date = datetime.now()


    days_difference = (current_date - input_date).days

    return days_difference

def read_data(file, name_of_product) -> List[Produkt]:
    li = []
    df = pd.read_csv("..\\Data\\{}".format(file), sep=':')
    for index, j in df.iterrows():
        name = j['name']
        price = j['price']
        link = j['link']
        if are_these_words_in_name(name_of_product, name):
            li.append(Produkt(name, price, link))
    return li

def compare_prices(current_file, name_of_product):
    closest_file = find_closest_file(current_file, getAllFileNames(folder_path))
    li1 = read_data(current_file, name_of_product)
    li2 = read_data(closest_file, name_of_product)

    for product1 in li1:
        name1 = product1.name
        price1 = product1.price
        link1 = product1.link

        matching_products = [product for product in li2 if product.name.lower() == name1.lower()]

        if matching_products:
            product2 = matching_products[0]
            if price1 < product2.price:
                print(f"Price for '{name1}' is lower in {current_file} compared to {closest_file}")
                send_notification(change_params(name1, product2.price, price1, closest_file, current_file, link1)) 
            elif price1 > product2.price:
                print(f"Price for '{name1}' is higher in {current_file} compared to {closest_file}")
            else:
                print(f"Prices for '{name1}' are equal in both files")
        else:
            print(f"No matching product found for '{name1}' in {closest_file}")
