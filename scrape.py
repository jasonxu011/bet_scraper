import requests
import urllib.request
import json
import re
from bs4 import BeautifulSoup
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

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)

driver.get("https://sportsbook.fanduel.com/sports?utm_source=homepage")

more_buttons = driver.find_elements_by_class_name("btn__content")
for x in range(len(more_buttons)):
  if more_buttons[x].is_displayed():
      driver.execute_script("arguments[0].click();", more_buttons[x])
      time.sleep(1)
page_source = driver.page_source
print(page_source)