import requests

def link_recursor(page):
    url = f'https://www.jumia.co.ke/office-furniture-lighting/?page={page}'

    response = requests.get(url)

    return response