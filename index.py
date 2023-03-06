from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def load_search_results(driver, search_query):
    driver.get("https://opensea.io/assets?search[query]=" + search_query)

def scrape_page(driver):
    # Loading Source Code
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    search_results = soup.findAll("div", {"class":"Asset--loaded"})
    
    # Extracting Codes
    codes = []
    for result in search_results:
        link = result.article.a['href']
        code = link.rfind("/")
        codes.append(link[code+1:])
    return codes

def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


query = input("Enter the search query :")
num_of_results = int(input("Enter the number of results :"))

# Setup
driver = webdriver.Chrome()    
load_search_results(driver, query)

while True:
    results = scrape_page(driver)
    print("results loaded")
    print(results)
    print(len(results))
    if len(results) > num_of_results:
        break
    scroll_down(driver)

print(results)

