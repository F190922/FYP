from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By

website = "https://www.geo.tv/"
s = Service('/Users/Asif Butt/Documents/chromedriver_win32 (1)')
driver = webdriver.Chrome(service=s)
driver.get(website)


#pagination
pages = driver.find_element(By.XPATH, '//ul/li/div[@class="heading"]/a[@data-article_name="PM Shehbaz leaves for Geneva to co-host climate conference"]')
heads = []
href = pages.get_attribute("href")
driver.get(href)
heads.append(driver.find_element(By.XPATH, '//section/div/div/div[1]/div[@class="story-area"]/h1').text)
paras = driver.find_elements(By.XPATH, '//section/div/div/div[1]/div/div[@class="content-area"]/p')
for parass in paras:
   print(parass.text)


driver.back()

df_books = pd.DataFrame({'heads':heads})
df_books.to_csv('qasim.cvs', index=False)




