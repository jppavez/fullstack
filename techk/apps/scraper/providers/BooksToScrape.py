import requests
from bs4 import BeautifulSoup


class BooksToScrape():

    def getSoup(self, url):
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        return soup

    def getCategories(self):
        MAIN_URL = "http://books.toscrape.com/"
        CATEGORIES_RESULT = {}

        soup = self.getSoup(MAIN_URL)

        categories = soup.find('div', attrs={'class': 'side_categories'}).find_all('li')

        for category in categories:
            name = category.find('a').text.strip()
            url = category.find('a')['href']

            CATEGORIES_RESULT[name] = url

        return CATEGORIES_RESULT
