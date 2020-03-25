import pymysql
import requests
import time
from db import Database
# from meituan.db import Database

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import pymsyql
from selenium.webdriver.common.proxy import Proxy,ProxyType
import  re
import json

from meituan.taiyandaili import Daili_ip



# proxy = Proxy(
#     {
# 'proxyType':ProxyType.MANUAL,
# # 'httpProxy': ‘ip:port’ # 代理ip和端口
# 'httpProxy': ip[2]# 代理ip和端口
#     }
# )
# mimvp_proxy = {
#
#     'ip': list[0],
#
#     'port_https': list[1],
#
# }
#
# print(mimvp_proxy)




ins = Database()


class Meituan():

    def __init__(self,url_index):
        self.url_index = url_index
        # # 以下代码自动输入账号密码登录！
        # 代理ip
        proxy_ip = Daili_ip()
        proxy = webdriver.Proxy()
        proxy.http_proxy = proxy_ip.get_ip()
        proxy.proxy_type = ProxyType.MANUAL
        # 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
        proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
        # browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)

        self.driver = webdriver.PhantomJS(executable_path=r"D:\python\phantomjs-2.1.1-windows\bin\phantomjs.exe")
        self.driver.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
        # self.driver = webdriver.Firefox(options=options,executable_path="E:\geckodriver-v0.26.0-win64\geckodriver.exe")



    # def login(self):
    #
    #     self.driver.set_window_size(1200, 1200)
    #     # 登录帐号
    #     url_log = "https://passport.meituan.com/account/unitivelogin?service=www&continue=https%3A%2F%2Fwww.meituan.com%2Faccount%2Fsettoken%3Fcontinue%3Dhttps%253A%252F%252Fwww.meituan.com%252Fmeishi%252F42998199%252F"
    #     self.driver.get(url_log)
    #     # 输入账户名
    #     self.driver.find_element_by_css_selector("input[type='text']").send_keys('XXXX')  # 自己美团账号
    #     # 输入密码
    #     self.driver.find_element_by_css_selector("input[type='password']").send_keys('XXXX')  # 自己美团密码
    #     element = self.driver.find_element_by_css_selector("input[data-mtevent='login.normal.submit']")
    #     element.click()


    def index(self):
        try:
            self.driver.get(self.url_index)
        except:
            self.driver.close()
        page_source = self.driver.page_source

        #"poiLists":
        print(page_source)
        time.sleep(5)
        product = re.findall(r'\"poiLists\"\:(.*?)\"comHeader\"',page_source,re.S)[0]


        data = re.match(r'.*\"poiInfos\"\:(.*)},',product).group(1)
        # print(data)
        lists = json.loads(data)
        content =  []
        # print(lists)
        for list in lists:
            data = {}
            data['title']= list['title'] if list['title'] else ''
            data['avgScore'] = list['avgScore'] if list['avgScore'] else ''
            data['commit'] = list['allCommentNum'] if list['allCommentNum'] else ''
            data['price']  = str(list['avgPrice']) if list['avgPrice'] else ''
            data["address"] = list["address"] if list["address"] else ''
            href = list["poiId"]
            url = "https://www.meituan.com/meishi/{}/".format(href)

            phone = self.get_phone(url)
            data['phone'] = phone
            print(data)
            time.sleep(5)

            ins.insert_db(data)

        self.driver.close()
        self.driver.quit()




    def get_phone(self,href):
        self.driver.get(url=href)
        #对弹窗的处理
        # self.driver.switch_to.alert.accept()
        # WebDriverWait(self.driver,5)
        time.sleep(5)
        response = self.driver.page_source
        phone = re.findall(r'\"phone\":\"(.*?)\"',response)[0] if re.findall(r'\"phone\":\"(.*?)\"',response) else ''
        return phone


    # def get_phone2(self,href):
    #     response = requests.get(url=href,headers=self.headers)
    #     html = response.text
    #     print(html)
    #     phone = re.findall(r'\"phone\":\"(.*?)\"', response)[0]
    #     print(phone)
    #     return phone

        # for list in tree.xpath('//div[@class="list"]/ul[@class="list-ul"]/li'):
        #     print("hello")
        #     print(list)
        #     dict ={}
        #     dict["href"] = "https://" + list.xpath('./div[@class="info"]/a/@href')
        #     dict["title"] = list.xpath('./div[@class="info"]/a/h4/text()')
        #     dict["addr"] = list.xpath('./div[@class="info]/a/p/text()')
        #     dict["score"] = list.xpath('./div[@class="info"]/a/div/p/text()')
        #     dict["commit"] = list.xpath('./div[@class="info"]/a/div/p/span/text()')
        #     # self.driver.get(url=dict["href"])
        #     # dict["phone"] = self.driver.find_element_by_xpath('//div[@class="address"]/p[2]')
        #     print(dict)
        # self.detail_xpath(page_source)

    # def detail_xpath(self):
        # for list in self.driver.find_element_by_xpath('//div[@class="list"]/ul[@class="list-ul"]/li'):
        #     print(list)
        #     dict =  {}
        #     dict["href"]  = "https://"+list.xpath('./div[@class="info"]/a/@href')
        #     dict["title"] = list.xpath('./div[@class="info"]/a/h4')
        #     dict["addr"] = list.xpath('./div[@class="info]/a/p')
        #     dict["score"] = list.xpath('./div[@class="info"]/a/div/p')
        #     dict["commit"] = list.xpath('./div[@class="info"]/a/div/p/span')
        #     self.driver.get(url=dict["href"])
        #     dict["phone"] = self.driver.find_element_by_xpath('//div[@class="address"]/p[2]')
        #     print(dict)


    def run(self):
        pass
        # options = webdriver.PhantomJS()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        # # 加代理
        # proxy_https_argument= self.get_ip()
        # options.add_argument(proxy_https_argument)



if __name__ == '__main__':
    url_index = "https://chs.meituan.com/meishi/pn{}/"
    for i in range(72,226):
        url = url_index.format(i)
        meituan = Meituan(url)
        meituan.index()







    # ip = dail_ip()
    # print(ip)
