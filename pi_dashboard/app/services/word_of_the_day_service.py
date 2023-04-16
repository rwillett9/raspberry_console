import requests
from bs4 import BeautifulSoup
from service import Service

class WordOfTheDayService(Service):
  def get_word_of_the_day_data(self):
    page = requests.get(url='https://www.transparent.com/word-of-the-day/today/japanese.html')
    soup = BeautifulSoup(page.content, 'html-parser')

    return soup
