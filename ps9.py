from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome=webdriver.Chrome()
chrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")
chrome.switch_to_alert().accept()
chrome.find_element(By.ID,"esm").send_keys("hello")
