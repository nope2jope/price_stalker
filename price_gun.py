import requests
from bs4 import BeautifulSoup

# function issues request, formats html
# and returns product current price

def pricecheck(url, request_header):
    try:
        # issue request
        response = requests.get(url=url, headers=request_header)
        response.raise_for_status()

        data = response.text

        # scrape data with bs4
        scraped_data = BeautifulSoup(data, 'html.parser')

        raw_price = scraped_data.find(id='priceblock_ourprice')
        current_price = round(float(raw_price.getText().split('$')[1]))

        return current_price
    except:
        print('pricecheck failed!')
