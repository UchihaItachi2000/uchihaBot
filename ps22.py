# مشخص کردن ماژول های مورد نیاز
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# مشخص کردن ویژگی های مورد نیاز و غیر فعال کردن دسترسی به مکان و ایجاد نوتیفیکیشن
op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications")
prefs = {"profile.default_content_setting_values.geolocation" :2}
op.add_experimental_option("prefs",prefs)

# ایجاد وب درایور
chrome=webdriver.Chrome(options=op)
chrome.get("https://developers.google.com/web/tools/chrome-devtools/storage/cookies")
chrome.minimize_window()

# دسترسی به کوکی ها
cook=chrome.get_cookies()
print(len(cook))
for items in cook:
    print(items)
print()

# # اضافه کردن کوکی
# cook={'name':'mycook','value':'10241024'}
# chrome.add_cookie(cook)

# # دسترسی به کوکی ها
# cook=chrome.get_cookies()
# print(len(cook))
# for items in cook:
#     print(items)

# حذف کوکی
# chrome.delete_cookie('mycook')
# time.sleep(3)
#
# # دسترسی به کوکی ها
# cook=chrome.get_cookies()
# print(len(cook))
# for items in cook:
#     print(items)
#
# # حذف تمام کوکی ها
# chrome.delete_all_cookies()
#
# # دسترسی به کوکی ها
# cook=chrome.get_cookies()
# print(len(cook))
# for items in cook:
#     print(items)
