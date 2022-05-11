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
  
def get_citations_needed_report(url):
  """ 
  Function that will report the text in which the citation is needed for! 
  """
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  results = soup.find_all(title="Wikipedia:Citation needed")
  text_cites_needed_for = []
  # so many parents!
  for result in results:
    text_cites_needed_for.append(result.parent.parent.parent.text)
    
  print("The follow text needs citation verification")
  for item in text_cites_needed_for:
    print(item)
  
  
get_citations_needed_count(url)
get_citations_needed_report(url)