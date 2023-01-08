from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = "https://www.dawn.com/"
s = Service('/Users/Asif Butt/Documents/chromedriver_win32 (1)')
driver = webdriver.Chrome(service=s)
driver.get(website)


#pagination

pages = driver.find_element(By.XPATH, '//article[@data-id="1730529"]/h2/a')
heads = []
href = pages.get_attribute("href")
driver.get(href)
cont = driver.find_element(By.XPATH, '//article[@data-id="1730529"]')
heads.append(cont.find_element(By.XPATH, './/div/h2/a').text)
paras = cont.find_elements(By.XPATH, '//div[@class="story__content  overflow-hidden    text-4  sm:text-4.5        pt-1  mt-1"]/.//p')
pr =[]
for parass in range(len(paras)):
	pr.append(paras[parass].text)
driver.back()

df_books = pd.DataFrame({"heads":[heads],"paras": [pr]})
df_books.to_csv('art_2.cvs', index=False, encoding='utf-8')

dat = pd.read_csv('art_2.cvs')
client = MongoClient("mongodb://localhost:27017/")
db = client['jwt']
collection = db['mycol']
data_dict = dat.to_dict("records")
collection.insert_many(data_dict)




