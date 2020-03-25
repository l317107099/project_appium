import requests
import re


# url = "http://http.tiqu.qingjuhe.cn/getip?num=10&type=1&pack=47589&port=1&lb=1&pb=4&regions="

def dail_ip():
    list = """
           58.218.214.147:12868
           58.218.214.140:15659
           58.218.92.69:18320
           58.218.214.148:14596
           221.203.191.82:4312
           114.99.20.81:4375
           223.214.204.123:4304
           58.218.214.132:16688
           58.218.214.138:13322
           58.218.214.151:12180
           """
    ip = list.split("\n")[1:-1]
    list = []
    for i in ip:
        data = re.search(r'\d+.*',i).group()

        list.append(data)

    return list



if __name__ == '__main__':
    ip = dail_ip()
    print(ip)
