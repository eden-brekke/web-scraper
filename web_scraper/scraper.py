import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Chernobyl_disaster'

def get_citations_needed_count(url):
  """
    A function that will take a URL and scrape through the page to find any "citation needed" clauses within
  """
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  results = soup.find_all(title='Wikipedia:Citation needed')