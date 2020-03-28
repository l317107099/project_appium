import json
from db import Database
import time
import random
import re

# random.random()*2

db = Database()
def response(flow):
    url = flow.request.url
    # print("start"*20)
    # print(url)
    # print("end"*20)

    if "http://apihotel.meituan.com/coresearch/HotelSearch?q=&" in url:
    # if "http://apihotel.meituan.com/coresearch/HotelSearch?q=&cateId=20" in url:
    #     print("酒店列表数据{}".format(flow.response.text))
        # print(flow.response.text)
        for user in json.loads(flow.response.text)["data"]["searchresult"]:
            meituan_list = {}
            #地址
            meituan_list["addr"] = user["addr"] if user["addr"] else ''
            #城市
            meituan_list["area"] = user["cityName"] if user["cityName"] else ''
            #hotel id
            meituan_list["poiid"] = user["poiid"] if user["poiid"] else ''
            #酒店名
            meituan_list["name"] = user["name"] if user["name"] else ''
            #评论数
            #价格
            meituan_list["price"] = user["lowestPrice"] if user["lowestPrice"] else ''
            meituan_list["comment_num"] = user["commentsCountDesc"] if user["commentsCountDesc"] else ''
            # #特性
            meituan_list["evalu"] = user["recommedReason"] if user["recommedReason"] else ''
            #图片地址 w.h = 440.267
            meituan_list["href"] = "http://www.meituan.com/shop/{}.html".format(meituan_list["poiid"]) if "http://www.meituan.com/shop/{}.html".format(meituan_list["poiid"]) else ''


                # user["frontImg"].replace("w.h","440.267") if user["frontImg"] else ''

            db.insert_db(meituan_list)
            # print(meituan_list)

    # if "https://apihotel.meituan.com/group/v1/poi/" in url:
    # if "group/v1/poi/" in url:
    #     print("详情数据{}".format(flow.response.text))
    #     for user in json.loads(flow.response.text)["data"]:
    #
    #         meituan = {}
    #         #酒店id
    #         meituan["poiid"]=user["poiid"]
    #         #地址
    #         # meituan["addr"] = user["addr"]
    #         # 酒店名
    #         # meituan["name"] = user["name"]
    #         #电话
    #         meituan["phone"] = user["phone"]
    #         #评分
    #         # meituan["avgScore"] = user["avgScore"]
    #         #特性
    #         # meituan["evalu"] = user["praiseText"]
    #         #评论数
    #         # meituan["markNumbers"] = user["markNumbers"]
    #         db.update_db(meituan)
    #     print(meituan)

        # if "share?utm_source" in url:
        #     meituan={}
        #     meituan["href"] = json.loads(flow.response.text)["data"]["shareUrl"]
        #     meituan["poiid"] = re.match(r".*?(\d+)",meituan["href"]).group(1)
        #     db.share_db(meituan)
        # print(meituan)







#https://apihotel.meituan.com/detailapi/v1/questionnaire/list
#https://apihotel.meituan.com/group/v2/poi/detail
#https://apihotel.meituan.com/group/v1/deal/poi/








        # with open("meituan2.txt","wb") as f:
        #     f.write(flow.request.content)