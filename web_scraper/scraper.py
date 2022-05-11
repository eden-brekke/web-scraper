from functools import total_ordering
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
  counter = 0
  
  for cites_needed in results:
    counter +=1
    
  print(f"The Wikipedia page at url: {url} needs {counter} citations!")
  

  
  
get_citations_needed_count(url)