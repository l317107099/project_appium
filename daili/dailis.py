import requests
from lxml import etree



class Ip():
    def __init__(self):
        self.url = "https://www.kuaidaili.com/free/inha/{}/"


        # self.headers = {
        #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        # }

    def kuaidaili_ip(self,page):
        # for i in range(1,4):
        print(self.url.format(page))
        response = requests.get(url = self.url.format(page))
        html = response.text

        return html
        # self.parse_item(html)

    def parse_item(self,response):
        data = []
        content = etree.HTML(response)
        lists = content.xpath("//table/tbody/tr")
        for list in lists:
            ip = list.xpath("./td[position()<3]/text()")
            data.append(ip)
        print(data)
        return data


    # def save_ip(self,data):
    #     list.append(data)

    def run(self):
        list = []
        for i in range(2,4):
            html = self.kuaidaili_ip(i)
            data = self.parse_item(html)
            list.append(data)
        print(list)

if __name__ == '__main__':
    ip = Ip()
    ip.run()