# وارد کردن کتابخانه های سلنیوم
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# وارد کردن ماژول تایم
import time
# وارد کردن ماژول رندوم
import random
# وارد کردن ماژول رشته
import string
# غیر فعال کردن دسترسی وب سایت به ادرس شما

# تابع ایجاد نام کاربری و رمز عبور
def ir_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(10,size))

options = webdriver.ChromeOptions()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument("--disable-notifications")
options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
prefs = {"profile.default_content_setting_values.geolocation" :2}
options.add_experimental_option("prefs",prefs)

while 1==1:
    # ایجاد یک درایور مجازی از مرورگر کروم
    myChrome=webdriver.Chrome(options=options)
    myChrome.get("https://digiato.com/wp-login.php?action=register")
    #myChrome.set_page_load_timeout(3)
    myChrome.maximize_window()
    #myChrome.find_element_by_xpath("//*[@id='login-modal']/i").click()
    #myChrome.switch_to.frame(myChrome.find_element_by_id("login-modal-form"))
    #myChrome.find_element_by_partial_link_text("register-modal").click()
    #myChrome.find_element_by_xpath("//*[@id='quickLoginRegisterIFrameParent']/div/div/div[2]/div[2]").click()
    #myChrome.find_element_by_xpath("//*[@id='Username']").click()
    #myChrome.implicitly_wait()
    username=myChrome.find_element_by_id("user_login")
    username.send_keys(ir_generator())
    email=myChrome.find_element_by_id("user_email")
    email.send_keys(ir_generator()+"@gmail.com")
    #password=myChrome.find_element_by_id("Password")
    #passs=int(''.join(random.choice(string.digits) for _ in range(10,20)))
    #print(passs)
    #password.send_keys(passs)
    #print(passs)
    #cpassword=myChrome.find_element_by_id("ConfirmPassword")
    #print(passs)
    #cpassword.send_keys(passs)
    WebDriverWait(myChrome,10).until(EC.frame_to_be_available_and_switch_to_it(myChrome.find_element_by_css_selector("iframe")))
    WebDriverWait(myChrome,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
    #myChrome.find_element_by_id("recaptcha-checkbox").click()
    myChrome.find_element_by_id("wp-submit").click()
    time.sleep(3)
    myChrome.close()
