# وارد کردن کتابخانه های سلنیوم
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import Select

# وارد کردن ماژول تایم
import time
# وارد کردن ماژول رندوم
import random
# وارد کردن ماژول رشته
import string
# غیر فعال کردن دسترسی وب سایت به ادرس شما
options = webdriver.ChromeOptions()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument("--disable-notifications")
options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
prefs = {"profile.default_content_setting_values.geolocation" :2}
options.add_experimental_option("prefs",prefs)

tel=webdriver.Chrome(options=options)
tel.get("https://web.telegram.org/#/login")
tel.maximize_window()
tel.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[2]/div/div[1]/form/div[2]/div[1]/input").clear()
tel.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[2]/div/div[1]/form/div[2]/div[1]/input").send_keys("46")
tel.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[2]/div/div[1]/form/div[2]/div[2]/input").send_keys("727753065")
tel.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[1]/div/div/div/ul/li[1]/a/my-i18n").click()
tel.find_element_by_xpath("//*[@id='ng-app']/body/div[5]/div[2]/div/div/div[2]/button[2]/span").click()
x=input()
tel.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[2]/div/div[1]/form/div[4]/input").send_keys(x)
tel.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[2]/div/div[1]/div[2]/ul/li[1]/a/div[3]/div[2]").click()
