import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime as dt


def apple_stock_price():
    url = "https://api.nasdaq.com/api/quote/AAPL/info?assetclass=stocks"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:

        response = requests.get(url, headers=headers)
        print(response.ok, response.status_code)

        data = response.json()['data']['primaryData']

        item = {
            'price': data['lastSalePrice'],
            'net_change': data['netChange'],
            'percent_change': data['percentageChange'],
            'time_stamp': dt.now().strftime("%d-%m-%Y %H:%M:%S")}

        print(item)
        return item


    except Exception as e:
        print('An error occurred:', e)
