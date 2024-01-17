from const import connection
from datetime import datetime
from notification import send_notification, change_params


def get_names(connection):
#gets a list of names in a database
    query = "SELECT DISTINCT name FROM data"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    names = [name[0] for name in data]
    cursor.close()
    return names

def get_link(connection, name):
    query = "SELECT DISTINCT link FROM data WHERE name=%s"
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    link = [item[0] for item in cursor.fetchall()]
    return link[0]


def get_newest_datetimes(connection):
    query = "SELECT DISTINCT datetime FROM data ORDER BY datetime DESC LIMIT 2"
    cursor = connection.cursor()
    cursor.execute(query)
    dts = [dates[0] for dates in cursor.fetchall()]
    cursor.close()
    return dts



def get_prices(connection, dts, name):
    query = "SELECT price FROM data WHERE name = %s AND datetime IN (%s, %s) ORDER BY datetime DESC"

    cursor = connection.cursor()
    cursor.execute(query, (name, dts[0], dts[1]))
    prices = [price_tuple[0] for price_tuple in cursor.fetchall()]

    cursor.close()
    return prices


def new_price_lower(prices):
    new_price = float(prices[0])
    last_price = float(prices[1])
    if new_price < last_price:
        return True
    return False



def check_products():
    names = get_names(connection)
    datetimes = get_newest_datetimes(connection)   
    for name in names:
        link = get_link(connection, name)
        prices = get_prices(connection, datetimes, name)

        if len(prices) < 2:
            print(f"Not enough prices available for {name}")
            continue

        new_price = float(prices[0])
        last_price = float(prices[1])
        new_date = datetimes[0]
        last_date = datetimes[1]

        if new_price_lower(prices):
            send_notification(change_params(name, last_price, new_price, last_date, new_date, link))
            print("name = ", name)
            print("last price = ", last_price)
            print("new_price = ", new_price)
            

    connection.close()






