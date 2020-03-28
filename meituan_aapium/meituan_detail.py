from db import Database
import random
import requests
import re
import time

db = Database()
class Meituan_detail():
    def __init__(self):
        user_agent = [
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
            "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        ]
        self.headers = {
            'User-Agent': random.choice(user_agent)
        }

    def request_url(self):
        href = db.get_phone()
        # href = (('http://www.meituan.com/shop/194939104.html'),)
        for url in href:
            data = {}
            print(url)
            try:
                # response = requests.get(url=url[0],headers= self.headers,verify=False).text
                response = requests.get(url=url[0], headers=self.headers).text
            except Exception as e:
                print(e)
            # response = requests.get(url=url, headers=self.headers).text
            data["phone"] = re.findall(r'"phone":"(.*?)"',response)[0].replace('\\u002F','/') if re.findall(r'"phone":"(.*?)"',response)[0] else ''
            data["poiid"] = re.findall(r'"poiInfo":{"id":(\d+),',response)[0] if re.findall(r'"poiInfo":{"id":(\d+),',response)[0] else ''
            db.update_db(data)
            time.sleep(3)


if __name__ == '__main__':
    detail = Meituan_detail()
    detail.request_url()


