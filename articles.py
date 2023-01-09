from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By

website = "https://www.dawn.com/"
s = Service('/Users/Asif Butt/Documents/chromedriver_win32 (1)')
driver = webdriver.Chrome(service=s)
driver.get(website)

container = driver.find_element(By.XPATH, '//div[contains(@class,"w-full sm:w-3/10 sm:pr-0.5")]')
header = container.find_elements(By.XPATH, './article[@data-layout="story"]')

news_heading = []
para_lines = []

for sss in header:
   para_lines.append(sss.find_element(By.XPATH, './/div[@dir="auto"]').text)


for header in header:
   news_heading.append(header.find_element(By.XPATH, './/h2/a').text)


df_books = pd.DataFrame({'head':news_heading, 'para' :para_lines})
df_books.to_csv('news.cvs', index=False)

