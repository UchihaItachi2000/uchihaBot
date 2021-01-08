from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome=webdriver.Chrome()
chrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")
chrome.maximize_window()

chrome.find_element(By.ID,"upload").send_keys("E://Telegram Desktop/Yalda.jpg")
