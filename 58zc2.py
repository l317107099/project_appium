import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Meituan():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url_index = "https://chs.meituan.com/meishi/"
        # # 以下代码自动输入账号密码登录！
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument(
            "user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'")
        self.driver = webdriver.Chrome(options=options)

    def login(self):

        self.driver.set_window_size(1200, 1200)
        # 登录帐号
        url_log = "https://passport.meituan.com/account/unitivelogin?service=www&continue=https%3A%2F%2Fwww.meituan.com%2Faccount%2Fsettoken%3Fcontinue%3Dhttps%253A%252F%252Fwww.meituan.com%252Fmeishi%252F42998199%252F"
        self.driver.get(url_log)
        # 输入账户名
        self.driver.find_element_by_css_selector("input[type='text']").send_keys('XXXX')  # 自己美团账号
        # 输入密码
        self.driver.find_element_by_css_selector("input[type='password']").send_keys('XXXX')  # 自己美团密码
        element = self.driver.find_element_by_css_selector("input[data-mtevent='login.normal.submit']")
        element.click()


    def index(self):
        self.driver.get(self.url_index)
        page_source = self.driver.page_source
        print(page_source)
    #     for data in response:
    #         pass
    # def detail(self,response):
    #
    #     pass

if __name__ == '__main__':
    meituan = Meituan()
    meituan.index()

