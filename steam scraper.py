from typing import Text
from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = 'https://store.steampowered.com/search/?specials=1&filter=topsellers'

request_page = urlopen(my_url)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

steam_items = html_soup.find_all('div', class_="responsive_search_name_combined")

filename = 'products.csv'
f = open(filename, 'w')

string = ''
for sales in steam_items:
    price = sales.find('div', class_='col search_price discounted responsive_secondrow').text
    title = sales.find('span', class_='title').text
    x = len(price)
    if x == 42:
        string = ('\nOriginal: ' + price[:12] + " \nSale: \n" + price[12:])
    if x == 41:
        string = ('\nOriginal: ' + price[:11] + " \nSale: \n" + price[11:])
    if x == 40:
        string = ('\nOriginal: ' + price[:10] + " \nSale: \n" + price[10:])
  
    f.write('\n' + title + string + '\n')

f.close

