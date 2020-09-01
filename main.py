from bs4 import BeautifulSoup
import requests
import time
from random import randint

def get_data(titles, links, prices, limit, default_link):
    '''
    This Function will scrape the webpage for specified data and append to a dictionary in a list.
    Accepted parameters must be lists, except for limit which accepts an int.
    Limit is the number of requests the scraper makes before sleeping.
    '''
    products = []

    for index, item in enumerate(titles):
        title = titles[index].getText()
        link = str(links[index].get('href'))
        price = prices[index].getText()

        if title:
            products.append({
                'title': title,
                'link': default_link + link,
                'price': price,
            })

            print(title + '\n')
            print(default_link + link + '\n')
            print(price + '\n')
            print('-' * 30)

    return products

request_limit_per_minute = 200
default_link = 'https://www.jumia.co.ke'
pages = 50
# pages = 5
products = []

def setup(page):
    url = f'https://www.jumia.co.ke/office-furniture-lighting/?page={page}'

    response = requests.get(url)

    return response

for page in range(1):
    response = setup(page)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('.name')
    links = soup.select('.core')
    prices = soup.select('.prc')

    products = products + get_data(titles, links, prices, request_limit_per_minute, default_link)
    print(f'Scraped page {page} of {pages}')
    sleep_time = randint(5, 10)
    print(f'Sleeping for {sleep_time} seconds...')
    time.sleep(sleep_time)

# print(products)
import xlsxwriter
workbook = xlsxwriter.Workbook('jumia_products.xlsx')
worksheet = workbook.add_worksheet()

row = 0
for dictionary in products:
    title = dictionary['title']
    link = dictionary['link']
    price = dictionary['price']
    worksheet.write(f'A{row}', dictionary['title'])
    worksheet.write(f'B{row}', dictionary['link'])
    worksheet.write(f'C{row}', dictionary['price'])
    row += 1
workbook.close()
