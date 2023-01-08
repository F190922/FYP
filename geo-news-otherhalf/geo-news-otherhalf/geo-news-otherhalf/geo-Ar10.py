from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By

website = "https://www.geo.tv/category/pakistan"
s = Service('/Users/Asif Butt/Documents/chromedriver_win32 (1)')
driver = webdriver.Chrome(service=s)
driver.get(website)


#pagination
pages = driver.find_element(By.XPATH, '//div[@class="video-list laodMoreCatNews"]/div/div[@class="list"]/ul/li/a[@title="Is winter vacation extended for Islamabad schools?"]')
heads = []
href = pages.get_attribute("href")
driver.get(href)
heads.append(driver.find_element(By.XPATH, '//section/div/div/div[1]/div[@class="story-area"]/h1').text)
paras = driver.find_elements(By.XPATH, '//section/div/div/div[1]/div/div[@class="content-area"]/p')
pr = []
for parass in range(len(paras)):
	pr.append(paras[parass].text)
driver.back()

df_books = pd.DataFrame({"heads":[heads],"paras": [pr]})
df_books.to_csv('geo_10.cvs', index=False, encoding='utf-8')

dat = pd.read_csv('geo_10.cvs')
client = MongoClient("mongodb://localhost:27017/")
db = client['jwt']
collection = db['goe']
data_dict = dat.to_dict("records")
collection.insert_many(data_dict)




