from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def op():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    prefs = {"profile.default_content_setting_values.geolocation" :2}
    options.add_experimental_option("prefs",prefs)
    return options

chrome=webdriver.Chrome(options=op())
chrome.get("https://ir.sputniknews.com/")

chrome.maximize_window()

# for t in range(0,61):
#     time.sleep(1)
#     chrome.execute_script("window.scrollBy(0,100)","")

# el=chrome.find_element(By.XPATH,"//*[@id='adfox_1479114591']")
# chrome.execute_script("arguments[0].scrollIntoView();",el)

chrome.execute_script("window.scrollBy(0,document.body.scrollHeight)")
