from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

chrome=webdriver.Chrome()
chrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\one.html")
hand=chrome.window_handles
print("\n\n",hand)

chrome.find_element(By.XPATH,"/html/body/a").click()
hands=chrome.window_handles
print(hands)
for fingers in hands:
    chrome.switch_to.window(fingers)
    print("\n\n",chrome.title)
