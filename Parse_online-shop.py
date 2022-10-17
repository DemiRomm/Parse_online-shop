import requests
from bs4 import BeautifulSoup as bs

page_temp = 1
page_all = 5  #количество страниц, указать перед процессом парсинга
n = 0  #счетчик количества объектов


while True:
    req = requests.get('https://www.lamoda.by/c/151/shoes-muzhskie-botinki/?sitelink=topmenuM&l=2&property_season_wear=5593&page=' + str(page_temp))
    html = bs(req.content, 'html.parser')

    if page_temp <= page_all:
        brand = html.find_all('div', class_='x-product-card-description__brand-name')  #поиск объектов по тегу и классу тега
        item = html.find_all('div', class_='x-product-card-description__product-name')
        price = html.find_all('span', class_=['x-product-card-description__price-single x-product-card-description__price-WEB8507_price_no_bold', 'x-product-card-description__price-new x-product-card-description__price-WEB8507_price_no_bold'])
        for b, i, p in zip(brand, item, price):
            print(f'Товар: {b.text}, {i.text}, - {p.text}')
            n += 1

        page_temp += 1

    else:
        break
print(n, 'товар проверен')

