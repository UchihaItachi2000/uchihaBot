from selenium import webdriver
from selenium.webdriver.common.by import By

import time

chrome=webdriver.Chrome()
chrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")
time.sleep(3)
chrome.find_element(By.ID,"upload").send_keys("E://Telegram Desktop/Yalda.jpg")
