# مشخص کردن ماژول های مورد نیاز
from xl import XL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

# مشخص کردن ویژگی های مورد نیاز
op = webdriver.ChromeOptions()
#op.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values.geolocation" :2}
op.add_experimental_option("prefs",prefs)

# ایجاد صفحه مورد نظر توسط بات
chrome=webdriver.Chrome(options=op)
chrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")
# chrome.maximize_window()

# به دست اوردن و ارسال داده ها از فایل اکسل
path="C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.xlsx"
x=XL(path)

chrome.find_element(By.NAME,"un").send_keys(x.readData(2,1))
chrome.find_element(By.NAME,"pw").send_keys(x.readData(2,2))
time.sleep(5)
chrome.find_element(By.ID,"send").click()
if chrome.title=="Result":
    print("OK")
