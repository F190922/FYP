from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['cnn_data']
collection = db['articles']

website = "https://edition.cnn.com/world"
s = Service('/Users/Asif Butt/Documents/chromedriver_win32 (1)')
driver = webdriver.Chrome(service=s)
driver.get(website)

for i in range(5):
	pages = driver.find_elements(By.XPATH, './/div/a[@class="container__link container_lead-plus-headlines__link"]')
	click = pages[i].get_attribute("href")
	driver.get(click)
	cont = driver.find_element(By.XPATH, '//div[@class="article__content-container"]')
	paras = cont.find_elements(By.XPATH, '//div[@class="article__content"]/p')
	text = ""
	for p in paras:
		text += p.text + "\n"
	data = {
		"title": driver.title,
		"url": click,
		"text": text
	}
	# Insert data into MongoDB
	collection.insert_one(data)
	driver.back()

# Close the browser and MongoDB client
driver.quit()
client.close()