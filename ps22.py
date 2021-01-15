# مشخص کردن ماژول های مورد نیاز
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class chef:
    def __init__(self):
        op=""
        prefs=""
        myoptions=""
        myaddress=""
        cook=""
        chrome=""
        mycook=""
        delcook=""
    def chromeoptios(self):
        # مشخص کردن ویژگی های مورد نیاز و غیر فعال کردن دسترسی به مکان و ایجاد نوتیفیکیشن
        self.op = webdriver.ChromeOptions()
        self.op.add_argument("--disable-notifications")
        self.prefs = {"profile.default_content_setting_values.geolocation" :2}
        self.op.add_experimental_option("prefs",self.prefs)
        return self.op
    def chromer(self,myop,addr):
        # ایجاد وب درایور
        self.myoptions=myop
        self.myaddress=addr
        self.chrome=webdriver.Chrome(options=self.myoptions)
        self.chrome.get(self.myaddress)
        self.chrome.minimize_window()
    def accesscookies(self):
        # دسترسی به کوکی ها
        self.cook=self.chrome.get_cookies()
        # تعداد کوکی ها
        print(len(self.cook))
        # چاپ کوکی ها
        for items in self.cook:
            print(items)
        print()
    def addcookies(self,incook):
        # اضافه کردن کوکی
        self.mycook=incook
        self.chrome.add_cookie(self.mycook)
    def deletecookies(self,namecook):
        #حذف کوکی
        self.delcook=namecook
        self.chrome.delete_cookie(namecook)
        time.sleep(3)
    def deleteallcookies(self):
        # حذف تمام کوکی ها
        self.chrome.delete_all_cookies()

chef1=chef()
chef1.chromer(chef1.chromeoptios(), addr="https://developers.google.com/web/tools/chrome-devtools/storage/cookies")
chef1.accesscookies()
dic={'name':'dj','value':'1234566'}
chef1.addcookies(dic)
chef1.accesscookies()
chef1.deletecookies('dj')
chef1.accesscookies()
chef1.deleteallcookies()
chef1.accesscookies()

# varcook=chrome.get_cookies()
# print(varcook)
# # لیستی از دیکشنری ها
# cook1={'name':'abc','value':'3214jhnkn'}
# chrome.add_cookie(cook1)
# chrome.delete('abc')
# chrome.deleteallcookies()
