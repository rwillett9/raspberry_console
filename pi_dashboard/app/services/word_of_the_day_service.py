import requests
from bs4 import BeautifulSoup

class WordOfTheDayService():
  def get_word_of_the_day_data(self):
    page = requests.get(url='https://www.transparent.com/word-of-the-day/today/japanese.html')
    soup = BeautifulSoup(page.content, 'html-parser')

    return soup
