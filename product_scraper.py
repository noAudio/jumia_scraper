def product_scraper(titles, links, prices, default_link):
    '''
    Scrapes information of each product within a page and returns a list.
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

    return products