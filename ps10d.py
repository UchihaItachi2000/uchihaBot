from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

chrome=webdriver.Chrome()
chrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")
chrome.maximize_window()
chrome.switch_to.frame("three")
chrome.find_element(By.ID,"se").send_keys("I am three")
chrome.switch_to.default_content()
chrome.switch_to.frame("two")
chrome.find_element(By.XPATH,"//*[@id='do']").send_keys("I am two")
chrome.switch_to.default_content()
chrome.switch_to.frame("one")
chrome.find_element(By.XPATH,"//*[@id='yek']").send_keys("I am one")
