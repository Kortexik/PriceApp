from const import connection
from datetime import datetime, timedelta
from notification import send_notification, change_params, lowest_in_month_params

def get_names():
#gets a list of names in a database
    query = "SELECT DISTINCT name FROM data"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    names = [name[0] for name in data]
    cursor.close()
    return names

def get_link(name):
    query = "SELECT DISTINCT link FROM data WHERE name=%s"
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    link = [item[0] for item in cursor.fetchall()]
    return link[0]


def get_newest_datetimes():
    query = "SELECT DISTINCT datetime FROM data ORDER BY datetime DESC LIMIT 2"
    cursor = connection.cursor()
    cursor.execute(query)
    dts = [dates[0] for dates in cursor.fetchall()]
    cursor.close()
    return dts



def get_prices(dts, name):
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
    names = get_names()
    datetimes = get_newest_datetimes()  
    for name in names:
        link = get_link(name)
        prices = get_prices(datetimes, name)

        if len(prices) < 2:
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
            

def get_dates_month_behind():
    now = datetime.now()
    thirty_days_ago = now - timedelta(days=30)
    query = "SELECT datetime FROM data WHERE datetime BETWEEN %s AND %s ORDER BY datetime DESC"
    cursor = connection.cursor()
    cursor.execute(query, (thirty_days_ago, now))
    result = cursor.fetchall()
    datetimes_list = [row[0] for row in result if row[0]]
    cursor.close()
    return datetimes_list



def get_prices_from_30days(name):
    dts = get_dates_month_behind()  
    query = "SELECT price FROM data WHERE datetime BETWEEN %s AND %s AND name = %s"
    cursor = connection.cursor()
    cursor.execute(query, (min(dts), max(dts), name))
    result = cursor.fetchall()
    prices = [float(row[0]) for row in result if row[0]]
    cursor.close()
    return prices

def newest_datetime():
    query = "SELECT datetime from data ORDER BY datetime DESC LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    dt = [row[0] for row in result if row[0]]
    cursor.close()
    return dt[0]


def get_price_on_dt(dtime, name):
    query = "SELECT price FROM data WHERE datetime = %s AND name = %s"
    cursor = connection.cursor()
    cursor.execute(query, (dtime, name))
    result = cursor.fetchall()
    cursor.close()
    if result:
        return float(result[0][0])
    else:
        return None


def lowest_in_month():
    names = get_names()
    new_dt = newest_datetime()
    for product in names:
        link = get_link(product)
        listOfPrices = get_prices_from_30days(product)
        new_price = get_price_on_dt(new_dt, product)

        if (new_price is not None):
            if (new_price < min(listOfPrices)):
                print("Lowest price in month")
                send_notification(lowest_in_month_params(product, new_price, link))
