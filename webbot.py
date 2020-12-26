# وارد کردن کتابخانه های سلنیوم
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# وارد کردن ماژول تایم
import time
# وارد کردن ماژول رندوم
import random
# غیر فعال کردن دسترسی وب سایت به ادرس شما
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values.geolocation" :2}
options.add_experimental_option("prefs",prefs)
# ایجاد یک درایور مجازی از مرورگر کروم
myChrome=webdriver.Chrome(chrome_options=options)
myChrome.get("https://www.zoomit.ir")
myChrome.maximize_window()
myChrome.find_element_by_xpath("//*[@id='mainMenu']/div[2]/a[1]/i").click()
myChrome.find_element_by_xpath("//*[@id='quickLoginRegisterIFrameParent']/div/div/div[2]/ul/li[2]/a").click()
name=
time.sleep(3)
