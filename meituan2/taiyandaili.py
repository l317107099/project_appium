import requests
import re

import time


class Daili_ip():
    """
    获取ip
    """
    def __init__(self):
        # self.url_index = "https://chs.meituan.com/meishi/pn1"
        # self.url_index = "https://chs.meituan.com/meishi"
        self.url_index = "https://www.baidu.com/"
        self.url_ip = "http://http.tiqu.qingjuhe.cn/getip?num=20&type=1&pack=47626&port=1&lb=1&pb=4&regions="
        self.headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }

    def dail(self):
        ip_list = requests.get(url=self.url_ip).text
        ip = ip_list.split("\r\n")[1:-2]
        list = []
        for i in ip:
            data = re.search(r'\d+.*',i).group()

            list.append(data)
        # print(list)
        return list


    def get_ip(self):
        ip = self.dail()
        a = 0
        iplist = ''
        while a<len(ip):
            # ip = dail_ip()
            time.sleep(1)
            proxy={

                "http":"http://{}".format(ip[a]),
                "https":"https://{}".format(ip[a])
               # "https": "https://103.133.177.83:25"
            }
            # print(proxy["http"])
            print("开始测试url{}第{}个ip {}".format(self.url_index,a+1,ip[a]))
            try:
                response = requests.get(url=self.url_index,headers = self.headers,proxies=proxy)
                if response.status_code in [200, 301]:
                    print(response.status_code)
                    print("获取代理成功")
                    iplist = ip[a]
                    break
            except Exception as e:
                a += 1
                print(e)
        print(iplist)
        if iplist == '':
            print("没有代理")
        proxy_ip = iplist
        # print(proxy_https_argument)
        return proxy_ip


    def run(self):
        self.get_ip()


if __name__ == '__main__':
    ip = Daili_ip()
    daip = ip.get_ip()
