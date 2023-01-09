from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
website = "https://www.dawn.com/"
s = Service('/Users/Asif Butt/Documents/chromedriver_win32 (1)')
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


for dates in dates:
   print(dates.text)

for red in red:
   print(red.text)
   print(red.get_attribute("href"))

for para in paragraphs:
   print(para.text)

for Link in Links:
   print(Link.get_attribute("href"))

for head in headings:
   print(head.text)


for charact in charact:
   print(charact.text)
   print(charact.get_attribute("href"))


time.sleep(5)




