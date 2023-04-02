from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from rank_bm25 import BM25Okapi
import numpy as np
from pymongo import MongoClient

# MongoDB connection parameters
client = MongoClient('localhost', 27017)
db= client['Search_Engine']
collection = db['articles']

# Scraping the CNN news articles
website = "https://edition.cnn.com/world"
s = Service('/Users/Asif Butt/Documents/chromedriver_win32 (1)')
driver = webdriver.Chrome(service=s)
driver.get(website)

articles = []
for i in range(5):
    pages = driver.find_elements(By.XPATH, './/div/a[@class="container__link container_lead-plus-headlines__link"]')
    click = pages[i].get_attribute("href")
    driver.get(click)
    cont = driver.find_element(By.XPATH, '//div[@class="article__content-container"]')
    paras = cont.find_elements(By.XPATH,'//div[@class="article__content"]/p')
    article_text = ""
    for p in paras:
        article_text += p.text
    articles.append(article_text)
    driver.back()

    # Storing the article in MongoDB
    doc = {"article_text": article_text}
    collection.insert_one(doc)

# Creating the BM25 index
tokenized_articles = [article.split() for article in articles]
bm25 = BM25Okapi(tokenized_articles)

# Querying the BM25 index
query = "China’s new defense minister"
tokenized_query = query.split()
doc_scores = bm25.get_scores(tokenized_query)

# Displaying the top 3 articles based on the query
top_k = 3
top_doc_indices = np.argsort(-doc_scores)[:top_k]
for i, doc_idx in enumerate(top_doc_indices):
    print(f"Rank {i+1}: {articles[doc_idx]}")
