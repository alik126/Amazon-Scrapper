import time
import requests
import random
from random import randint
from product import Product
from datetime import datetime
from bs4 import BeautifulSoup
from data_saver import DataSaver

HEADERS = [{
    'authority': 'www.amazon.com',
    'method': 'GET',
    'scheme': 'https',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'accept': '/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-user': '?1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/'
}, {
    'authority': 'www.amazon.com',
    'method': 'GET',
    'scheme': 'https',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'accept': '/',
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-user': '?1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.google.com/'
}, {
    'authority': 'www.amazon.com',
    'method': 'GET',
    'scheme': 'https',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'accept': '/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-user': '?1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/'
}, {
    'authority': 'www.amazon.com',
    'method': 'GET',
    'scheme': 'https',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'accept': '/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-user': '?1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.google.com/'
}, {
    'authority': 'www.amazon.com',
    'method': 'GET',
    'scheme': 'https',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'accept': '/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-user': '?1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.google.com/'
}]
proxies = [
    {'HTTP': 'HTTP://185.181.166.209:8080'},
    {'HTTPS': 'HTTPS://181.129.43.3:8080'},
    {'HTTP': 'HTTP://45.70.198.195:999'},
    {'HTTP': 'HTTP://103.101.17.170:8080'},
    {'HTTP': 'HTTP://181.10.171.234:8080'},
    {'HTTP': 'HTTP://92.60.26.58:8089'},
    {'HTTPS': 'HTTPS://92.249.122.108:61778'},
    {'HTTPS': 'HTTPS://91.92.94.69:41890'},
    {'HTTPS': 'HTTPS://85.234.126.107:55555'},
    {'HTTPS': 'HTTPS://116.105.87.134:3128'},
    {'HTTP': 'HTTP://190.103.74.236:999'},
    {'HTTPS': 'HTTPS://46.35.249.189:41419'},
    {'HTTP': 'HTTP://45.116.229.183:8080'},
    {'HTTP': 'HTTP://46.147.110.7:8080'},
    {'HTTP': 'HTTP://98.154.21.253:3128'},
    {'HTTP': 'HTTP://170.254.230.201:999'},
    {'HTTPS': 'HTTPS://177.136.84.164:999'},
    {'HTTP': 'HTTP://34.208.39.27:3128'},
    {'HTTP': 'HTTP://195.97.124.164:8080'},
    {'HTTP': 'HTTP://80.66.81.35:53281'},
    {'HTTP': 'HTTP://170.79.235.3:999'},
    {'HTTP': 'HTTP://82.114.97.157:1256'},
    {'HTTPS': 'HTTPS://178.151.205.154:45099'},
    {'HTTPS': 'HTTPS://125.25.206.28:8080'},
    {'HTTPS': 'HTTPS://203.150.113.190:57322'},
    {'HTTP': 'HTTP://77.70.35.87:37475'},
    {'HTTPS': 'HTTPS://187.189.132.173:999'},
]


class Scraper:
    def __init__(self, extracted_query):
        self.queries = extracted_query.query
        self.session = requests.Session()
        self.session.proxies.update(random.choice(proxies))
        self.session.headers.update(random.choice(HEADERS))
        self.data_saver = DataSaver()

    def prepare_url(self, query):
        return "https://www.amazon.com/s?k=" + query

    def perform_scrapping(self):
        for query in self.queries:
            url = self.prepare_url(query)
            print("Currently Scraping:", query)
            for i in range(1, 21):
                print('Processing {0}'.format(url + '&page={0}'.format(i)))
                time.sleep(randint(1, 10))
                response = self.session.get(url + '&page={0}'.format(i), stream=True)
                if response.status_code == 200:
                    products = []  # List to store product instances
                    soup = BeautifulSoup(response.content, 'html.parser')
                    titles = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
                    for title in titles:
                        try:
                            product_title = title.find('span', {
                                'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()
                            rating = title.find('i', {'class': 'a-icon-star-small'}).text.strip()
                            rating_count = title.find('span', {'class': 'a-size-base s-underline-text'}).text.strip()
                            dollars = title.find('span', {'class': 'a-price-whole'}).text.strip().replace(',', '')
                            cents = title.find('span', {'class': 'a-price-fraction'}).text.strip()
                            price = float(dollars + cents)
                            image_url = title.find('a', {'class': 'a-link-normal s-no-outline'}).img['src']
                            updated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            item = Product(product_title, rating, rating_count, price, image_url, updated_time)
                            products.append(item)
                        except AttributeError:
                            continue
                    self.data_saver.save_data_to_json(products, query)
                else:
                    print(response.status_code)
        return products  # Return list of Product instances
