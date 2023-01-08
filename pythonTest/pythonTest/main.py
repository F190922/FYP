import driver as driver
import pandas as pd
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pymongo

from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.devtools.v106 import browser

website = "https://www.dawn.com/"
s = Service('/Users/Asif Butt/Documents/chromedriver_win32 (1)')

# fname="ETF.csv"
# f = open(fname, "a", encoding="utf-8")
# f.write("dates,red,paragraphs,Links,headings,charact")

driver = webdriver.Chrome(service=s)
driver.get(website)
driver.find_element(By.XPATH, '//article[@data-layout="story"]')
headings = driver.find_elements(By.TAG_NAME, 'h2')
paragraphs = driver.find_elements(By.XPATH, '//article/div')
red = driver.find_elements(By.XPATH, '//div[@class="w-full"]/a')

driver.find_element(By.XPATH, '//article/h2')
Links = driver.find_elements(By.TAG_NAME, 'a')
charact = driver.find_elements(By.XPATH, '//div[@class="flex-col"]/div/a')
dates = driver.find_elements(By.XPATH, '//article[@data-layout="story"]/span/span[2]')
date = []
r = []
pr = []
h = []
L = []
ch = []
for p in range(len(dates)):
	date.append(dates[p].text)

for p in range(len(red)):
	r.append(red[p].text)

for p in range(len(paragraphs)):
	pr.append(paragraphs[p].text)

for p in range(len(Links)):
	L.append(Links[p].text)

for p in range(len(headings)):
	h.append(headings[p].text)

for p in range(len(charact)):
	ch.append(charact[p].text)

time.sleep(5)

df = pd.DataFrame({"Dates": [date], "Red": [r], "Paragraphs": [pr], "Headings": [h], "Links": [L], "Chararcteristics": [ch]})

df.to_csv('products.csv', index=False, encoding='utf-8')
dat = pd.read_csv('products.csv')
client = MongoClient("mongodb://localhost:27017/")
db = client['jwt']
collection = db['mycol']
data_dict = dat.to_dict("records")
collection.insert_many(data_dict)