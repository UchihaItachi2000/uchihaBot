# مشخص کردن ماژول های مورد نیاز
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# مشخص کردن ویژگی های مورد نیاز
op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values.geolocation" :2}
op.add_experimental_option("prefs",prefs)

# ایجاد صفحه مورد نظر توسط بات
chrome=webdriver.Chrome(options=op)
chrome.get('https://nl.pinterest.com/')
chrome.save_screenshot('C:\\Users\\mphpamatrasu2000\\Desktop\\pic1.png')
chrome.get_screenshot_as_file('C:\\Users\\mphpamatrasu2000\\Desktop\\pic2.jpg')
chrome.close()
