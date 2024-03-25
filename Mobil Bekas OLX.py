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
driver.get('https://www.olx.co.id/mobil-bekas_c198')
soup = BeautifulSoup(driver.page_source,'lxml')

judul_list = []
harga_list = []
lokasi_list = []
detail_list = []

for i in range(2):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main_content > div > div > section > div > div > div:nth-child(7) > div._2CyHG > div > div:nth-child(2) > ul > li._2xGb5 > div > button'))).click()
    time.sleep(2)

for item in soup.findAll('div', class_='_2v8Tq'):
    judul = item.find('div', class_='_2Gr10').text
    harga = item.find('span', class_='_1zgtX').text
    lokasi = item.find('div', class_='_3VRSm').text
    detail = item.find('div', class_='_21gnE').text

    judul_list.append(judul)
    harga_list.append(harga)
    lokasi_list.append(lokasi)
    detail_list.append(detail)


driver.close()

df = pd.DataFrame({
    'Judul': judul_list,
    'Harga': harga_list,
    'Lokasi': lokasi_list,
    'Detail': detail_list
})

df.to_csv('df_OLX.csv')