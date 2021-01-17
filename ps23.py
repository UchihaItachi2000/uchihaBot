# مشخص کردن ماژول های مورد نیاز
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# مشخص کردن ویژگی های مورد نیاز
op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values.geolocation" :2}
op.add_experimental_option("prefs",prefs)

# ایجاد صفحه مورد نظر توسط بات
chrome=webdriver.Chrome(options=op)
chrome.get('https://www.youtube.com/watch?v=qnfYo7RFER0')
chrome.find_element(By.XPATH,'//*[@id="dismiss-button"]').click()
chrome.find_element(By.XPATH,'//*[@id="movie_player"]/div[28]/div[2]/div[2]/button[8]').click()

t=0
while t<300:
    #chrome.save_screenshot('C:\\Users\\mphpamatrasu2000\\Desktop\\pics\\pic'+str(t)+'.png')
    chrome.get_screenshot_as_file('C:\\Users\\mphpamatrasu2000\\Desktop\\pics\\pic'+str(t)+'.png')
    chrome.minimize_window()
    t=t+1
    time.sleep(1)

chrome.close()
