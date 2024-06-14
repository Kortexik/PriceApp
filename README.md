
# Python Web Scraping Script For Analyzing And Being Informed Of Item Price Drops.

## A functional script featuring BeautifulSoup for obtaining ceneo.pl pricing data that stores it on local mysql database. Also featuring plotly graphs.

This project was built to help me save some money with online shopping. It is setup to run on my local machine every 2 hours with task scheduler (although it could be run from cloud 24/7), storing the data, and notifing the user if the price dropped by 10% or more. This parameter can be changed in const.py file. It also features a plotly graphing tool to let you see patterns in price. 


**How it works:**

1. Scrapes the name, price and link of an object from all URLs given and saves it to a database with current datetime.
2. For each new insertion it compares the prices of an item with its last price in database
3. It checks if the prices is lower or equal to the price drop parameter (by default 10%). If it is, sends a notification with Telegram bot.

Also has function to check it the price is lowest in a month.

**How the notification looks:**

![image](https://github.com/Kortexik/PriceApp/assets/137905044/2d769b73-16d8-470a-9490-23eadc15a993)

Graphing tool (run separetly from the script):

This tool uses plotly module and reads whole database for choosen product. There is a simple GUI written using Pyside6 (run window.py) and clicking an item creates an interactive graph in your browser.

**How the GUI looks:**

![image](https://github.com/Kortexik/PriceApp/assets/137905044/9e5ffcde-f023-444f-97e0-ba3e982056b0)

The GUI has a clean look and an option to filter it using search bar.

**How the graphs look:**

![image](https://github.com/Kortexik/PriceApp/assets/137905044/ce27381f-041e-4de1-adf1-c26ed3d5db71)

**How to setup:**

1. Pull this repo to choosen directory on your PC.
2. Install required modules (run in terminal: pip install -r requirments.txt).
3. Create MySql database with a table that uses table_structure.sql.
4. Fill in the config.json file.
5. Run main.py 2 times so there arer at least 2 records for each product
6. Run window.py for graphing tool if you want, you might need more records of data for them to look meaningful.
