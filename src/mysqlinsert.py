from datetime import datetime
import mysql.connector

# Function to create a MySQL connection
def create_mysql_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='priceappdata'
    )

def convert_datetime_format(path):
    try:
        original_datetime_str = path[5:-4]
        original_datetime_obj = datetime.strptime(original_datetime_str, '%d.%m.%Y %H-%M-%S')
        formatted_datetime_str = original_datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime_str
    except ValueError:
        print(f"Error converting datetime in path: {path}")
        return None

def writeToDB(listOfObjects, path, connection):
    try:
        if not connection.is_connected():
            connection = create_mysql_connection()

        cursor = connection.cursor()

        for obj in listOfObjects:
            query = "INSERT INTO data(datetime, name, price, link) VALUES(%s, %s, %s, %s)"
            values = (convert_datetime_format(path), obj.name, obj.price, obj.link)
            
            if values[0] is not None:
                cursor.execute(query, values)

        connection.commit()
        cursor.close()

    except Exception as e:
        print(f"Error: {e}")
    


