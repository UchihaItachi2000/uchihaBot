from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.geolocation" :2}
options.add_experimental_option("prefs",prefs)
options.add_argument("--disable-notifications")

chrome=webdriver.Chrome(options=options)
chrome.get("https://www.zoomit.ir/")
chrome.maximize_window()
time.sleep(2)
chrome.find_element(By.XPATH,"//*[@id='mainMenu']/div[2]/a[1]/i").click()
time.sleep(2)
chrome.find_element(By.XPATH,"//*[@id='quickLoginRegisterIFrameParent']/div/div/div[2]/ul/li[2]/a").click()
time.sleep(2)
chrome.switch_to.frame("quickRegisterIframe")
time.sleep(2)
chrome.find_element(By.XPATH,"//*[@id='Username']").send_keys("username1")
