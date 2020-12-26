# وارد کردن کتابخانه های سلنیوم
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ورود کتابخانه زمان
import time

# غیر فعال کردن نوتیفیکیشن و دسترسی به مکان کاربری
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values.geolocation" :2}
options.add_experimental_option("prefs",prefs)

# ایجاد یک درایور مجازی از مرورگر کروم
myChrome=webdriver.Chrome(chrome_options=options)
#myChrome=webdriver.Chrome()
#myChrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")
myChrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")
myChrome.implicitly_wait(5)
myChrome.maximize_window()
username=myChrome.find_element_by_name("text1")
password=myChrome.find_element_by_name("text2")
username.send_keys("user1")
password.send_keys("123")
myChrome.find_element_by_name("login").click()
