def product_scraper(titles, links, prices, limit, default_link):
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

    return products