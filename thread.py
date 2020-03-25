'''
多线程爬取一部小说
'''

# 导入第三方库
import os
import time
import requests
import threading
from lxml import etree
from queue import Queue
# from fake_useragent import UserAgent
# ua = UserAgent()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}

# 定义生产者类
class Product(threading.Thread):
    # 初始化对象
    def __init__(self, url, content_queue, content):
        # 调用父类
        super(Product, self).__init__()
        self.page_queue = url
        self.content_queue = content_queue
        self.content = content

    # 定义运行方法
    def run(self):
        # 循环
        # while True:
        #     # 判断page_queue是否为空，如果为空则退出循环
        #     if self.page_queue.empty():
        #         print("product_break{}".format(self.name))
        #         break

            # 从page_queue中获取每一页的url
        url = self.page_queue
        print(url)
        # 解析每一页的html并提取图片的地址
        self.paser_html(url)

    # 定义解析html文本的方法
    def paser_html(self, url):
        time.sleep(0.5)
        print("parse_html  {}".format(url))
        html = requests.get(url, headers=headers).content.decode("utf-8")
        # html = requests.get(url,headers=headers).text
        # print(html)
        e = etree.HTML(html)
        # print(e)
        # 提取图片的地址
        href = e.xpath('//dd/a/@href')
        href = ["https://www.17k.com" + i for i in href][5:]
        # print(href)
        # 遍历循环图片地址
        for href in href:
            print("product_href {}".format(href))
            self.content_queue.put(href)


# 定义消费者类
class Consunmer(threading.Thread):

    # 初始化对象
    def __init__(self, content_queue, content):
        # 调用父类
        super(Consunmer, self).__init__()

        self.content_queue = content_queue
        self.content = content

    # 定义运行函数
    def run(self):
        # 创建文件夹
        print("product {}".format("start"))
        if not os.path.exists('盗墓笔记续十年之后'):
            os.mkdir('盗墓笔记续十年之后')
        # 循环
        while True:
            # 判断img_queue和page_queue是否为空，如果为空，退出循环
            time.sleep(2)
            if self.content_queue.empty():
                print("break{}".format(self.name))
                break
            else:
                time.sleep(0.5)
                # title, content = self.content
                self.paser_noverl()
            while True:
                if self.content.empty():
                    time.sleep(2)
                    print("content{}".format("aaa"))
                    break
                else:
                    print("self.content{}".format("start"))
                    title,content = self.content.get()
                    # print("content{}".format(content))
                    with open('盗墓笔记续十年之后' + '/' + title[0]+'.txt', 'w+', encoding='utf-8') as f:
                        print("正在下载:{}".format(title[0]))
                        for line in content:
                            f.write(line)


    def paser_noverl(self):
        print("paser_noverl{}".format("a"))
        href = self.content_queue.get()
        r = requests.get(href, headers=headers)
        if r.status_code == 200:
            html = r.content.decode()
            e = etree.HTML(html)
            title = e.xpath('//div[@class="readAreaBox content"]/h1/text()')
            content = e.xpath('//div[@class="p"]/p/text()')
            # print("title{}content{}".format(title,content))
            self.content.put((title, content))
        else:
            print("请求失败:" + href)



# 定义主函数
def main():
    # 创建每一页url的队列
    # page_queue = Queue(2)
    # 创建图片地址的队列
    content_queue = Queue(200)
    content = Queue(200)
    url = "https://www.17k.com/list/2886125.html"
    # 将url加入到page_queue队列中
    # page_queue.put(url)
    # 创建五个生产者线程

    # for x in range(5):
    t1 = Product(url, content_queue, content)


    # 创建五个消费者线程
    list_consumer=[]
    list_consumer.append(t1)
    for x in range(5):
        t = Consunmer(content_queue, content)
        list_consumer.append(t)

    for list in list_consumer:
        list.start()
    for list in list_consumer:
        list.join()

if __name__ == '__main__':
    main()
