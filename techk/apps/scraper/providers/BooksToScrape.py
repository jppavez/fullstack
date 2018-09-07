import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class BooksToScrape():

    def __init__(self):
        self.MAIN_URL = "http://books.toscrape.com/"

    def getSoup(self, url):
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        return soup

    def cleanUrl(self, url):
        parsed_url = urlparse(url)

        if url.endswith('.html'):

            path_url = parsed_url.path
            clean_path = path_url.rpartition('/')[0]

            return parsed_url.scheme + '://' + parsed_url.netloc + clean_path + '/'

        return url

    def getCategories(self):
        CATEGORIES_RESULT = []

        soup = self.getSoup(self.MAIN_URL)

        categories = soup.find('div', attrs={'class': 'side_categories'}).find_all('li')

        for category in categories:
            category_a_element = category.find('a')
            name = category_a_element.text.strip()
            url = self.MAIN_URL + category_a_element['href']

            CATEGORIES_RESULT.append((name, url))

        return CATEGORIES_RESULT

    def getBookFromCategory(self, category_url):
        CATEGORY_URL = category_url
        BOOKS_RESULTS = []
        soup = self.getSoup(CATEGORY_URL)

        HAS_NEXT_PAGE = soup.find('li', attrs={'class': 'next'})

        books = soup.find_all('article')

        for book in books:
            a_element = book.find('h3').find('a')

            url = a_element['href']
            title = a_element['title']

            BOOKS_RESULTS.append((title,  self.cleanUrl(CATEGORY_URL) + url))

        if HAS_NEXT_PAGE:
            next_page_url = HAS_NEXT_PAGE.find('a')['href']
            BOOKS_RESULTS += self.getBookFromCategory(
                self.cleanUrl(CATEGORY_URL) + next_page_url)

        return BOOKS_RESULTS

    def _getBookInformation(self, book_url):
        BOOK_URL = book_url
        soup = self.getSoup(BOOK_URL)

        title = self._parseTitle(soup)
        upc = self._parseUPC(soup)
        price = self._parsePrice(soup)
        thumbnail = self._parseThumbail(soup)
        stock, stock_quantity = self._parseStock(soup)
        description = self._parseProductDescription(soup)

        print(title)
        print(price)
        print(description)
        print(upc)
        print(thumbnail)
        print(stock, stock_quantity)

    def _parseTitle(self, soup_book_info):
        product_main = soup_book_info.find('div', {'class': 'product_main'})

        title = product_main.find('h1').text.strip()

        return title

    def _parseUPC(self, soup_book_info):
        upc = soup_book_info.find('th', text="UPC").find_next_siblings('td')

        return upc[0].text.strip()

    def _parsePrice(self, soup_book_info):
        product_main = soup_book_info.find('div', {'class': 'product_main'})

        price = product_main.find('p', {'class': 'price_color'}).text.strip()

        return price

    def _parseThumbail(self, soup_book_info):
        thumbnail = soup_book_info.find('div', {'id': 'product_gallery'}).find('img')['src']

        return thumbnail

    def _parseStock(self, soup_book_info):
        stock = soup_book_info.find('th', text='Availability').find_next_siblings('td')

        if not stock:
            return False, 0

        stock_text = stock[0].text.strip()

        if 'In stock' in stock_text:
            m = re.search("(\d+) available", stock_text)
            if m:
                return True, m[1]

        return False, 0

    def _parseProductDescription(self, soup_book_info):
        product_description = soup_book_info.find(
            'div', {'id': 'product_description'}).find_next_siblings('p')

        return product_description[0].text.strip()
