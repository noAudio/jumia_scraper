from random import randint
import time

from page_scraper import page_scraper
from workbook_writer import write_to_workbook

pages = 50
products = []
file_name = 'jumia_products.xlsx'
row = 1

if __name__ == '__main__':
    # Scrape products from multiple pages
    for page in range(pages):
        products = products + page_scraper(page)

        sleep_time = randint(5, 10)
        print(f'Sleeping for {sleep_time} seconds...')
        time.sleep(sleep_time)

    # Write scraped products into Excel workbook
    for dictionary in products:
        write_to_workbook(row, file_name, dictionary)
        row += 1