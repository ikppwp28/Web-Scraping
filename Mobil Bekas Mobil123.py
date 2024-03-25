import time
import lxml
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://www.mobil123.com/mobil-dijual/indonesia')
soup = BeautifulSoup(driver.page_source,'lxml')

judul_list = []
harga_list = []

for item in soup.findAll('div', class_='grid  grid--full  cf'):
    judul = item.find('a', class_='ellipsize  js-ellipsize-text').text
    harga = item.find('div', class_='listing__price  delta  weight--bold').text

    judul_list.append(judul)
    harga_list.append(harga)

driver.close()

df = pd.DataFrame({
    'Judul': judul_list,
    'Harga': harga_list
})

df.to_csv('df_mobil123.csv')