import requests
import urllib.request
import json
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time 

"""
URL = "http://draftkings.com/lobby#/featured"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())"""

# this is a comment
# this is another comment

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
# for mac
# driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)
# for windows
driver = webdriver.Chrome("C:/Windows/chromedriver", chrome_options=options)

driver.get("https://pa.sportsbook.fanduel.com/sports/navigation/6227.1/13348.3")

# get ids of all games
more_buttons = driver.find_elements_by_class_name("event")
all_ids = []
for i in range(len(more_buttons)):
	current = more_buttons[i].get_attribute("innerHTML")[:200]
	index = current.index("idfoevent")
	index2 = current.index('"',index+1)
	index3 = current.index('"',index2+1)
	all_ids.append(cur rent[index2+1:index3])

for id in all_ids:
	print(id)

base = "https://pa.sportsbook.fanduel.com/sports/event/"
all_urls = []
for x in all_ids:
	all_urls.append(base + x)

for i in range(1):
	cur_url = all_urls[i]
	page = requests.get(cur_url)
	soup = BeautifulSoup(page.content, 'lxml')
	lines = []


# print(len(more_buttons))
# print(more_buttons[0].get_attribute('innerHTML'))

"""
jason's old code below

# for x in range(len(more_buttons)):
#   if more_buttons[x].is_displayed():
#       driver.execute_script("arguments[0].click();", more_buttons[x])
#       time.sleep(1)
# page_source = driver.page_source

# soup = BeautifulSoup(page_source, 'lxml')
# lines = []
# lines_selector = soup.find_all('div', class_='event')

# for line in lines_selector:
# 	print(line.get_text())
# 	#break

"""
