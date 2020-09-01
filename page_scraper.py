from product_scraper import product_scraper
from bs4 import BeautifulSoup
from link_recursor import link_recursor

default_link = 'https://www.jumia.co.ke'

def page_scraper(page, pages):
    '''
        Scrapes multiple products from the page that is passed in.
    '''
    products = []

    response = link_recursor(page)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('.name')
    links = soup.select('.core')
    prices = soup.select('.prc')

    products = products + product_scraper(titles, links, prices, default_link)
    print(f'Scraped page {page} of {pages}')
    
    return products