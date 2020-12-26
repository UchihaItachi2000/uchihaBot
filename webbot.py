# وارد کردن کتابخانه های سلنیوم
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# وارد کردن ماژول تایم
import time
# وارد کردن ماژول رندوم
import random
# وارد کردن ماژول رشته
import string
# غیر فعال کردن دسترسی وب سایت به ادرس شما

# تابع ایجاد نام کاربری و رمز عبور
def ir_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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
username=myChrome.find_element_by_xpath("/html/body/form/div[2]")
username.send_keys(ir_generator())
time.sleep(3)
