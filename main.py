from bs4 import BeautifulSoup
import requests

request_limit_per_minute = 200

response = requests.get('https://www.jumia.co.ke/office-furniture-lighting/')

soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select('.name')
links = soup.select('.core')
# print(links[0].get('href'))
prices = soup.select('.prc')
ratings = soup.select('.stars')

def get_data(titles, links, prices, ratings, limit):
    products = []

    pass