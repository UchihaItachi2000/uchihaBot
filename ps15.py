from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

import time

chrome=webdriver.Chrome()
chrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")

text=chrome.find_element(By.XPATH,"//*[@id='pasid']")
send=chrome.find_element(By.XPATH,"//*[@id='sendid']")

act=ActionChains(chrome)
#act.move_to_element(title).move_to_element(subtitle).click().perform()
act.context_click(text).perform()
time.sleep(3)
chrome.find_element(By.XPATH,"//*[@id='pasid']").send_keys("mypass")
time.sleep(3)
act.double_click(send).perform()
