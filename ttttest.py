from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import threading
import time
import random

op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values.geolocation" :2}
op.add_experimental_option("prefs",prefs)
# ایجاد صفحه مورد نظر توسط بات
chrome=webdriver.Chrome(options=op)
chrome.get('https://www.youtube.com/watch?v=UackUFgscHY')
chrome.find_element(By.XPATH,'//*[@id="dismiss-button"]').click()
chrome.find_element(By.XPATH,'//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]').click()
