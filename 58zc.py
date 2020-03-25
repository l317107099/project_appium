import requests
import json


headers = {
    "user-Agent":"AiMeiTuan /OPPO-5.1.1-OPPO R11-1920x1080-320-5.5.4-254-863064010380022-qqcpd"
}



class MeiTuan:
    def __init__(self):

        url = "https://chs.meituan.com/meishi/api/poi/getPoiList?cityName=%E9%95%BF%E6%B2%99&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=2&userId=&uuid=a9354521a57747bcb9b1.1584422994.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fchs.meituan.com%2Fmeishi%2Fpn2%2F&riskLevel=1&optimusCode=10&_token=eJyFj0GTojAQhf9LrlISksCINxRmog4iDiIwNQdEagFBEBJAp%2Fa%2Fb6bKPexpT%2B%2Fr169edX%2BDdnUGcwVCHUIJ9GkL5kCZwqkGJMA6sVFnhCCMFJ0QXQLJv56KVAmcWt8E80%2BFQFVCBH79OHthfCoq1qSZRr6kJyKBiEg%2FAk4rEQEZY003l%2BUk66ZVmjMeX6dJXcmCuyyXmyuSxSH%2FSQFRV3miTujlqfFT2d%2FZFo%2BJqi7%2FdRWUrofy4SnO6Bnuwlm%2B9PampHtOrY3L4Ia71gLSZP1eRodgVsuHOA%2B3bmJAPrwhlxuHo7%2Bz%2FVotvdB44LdhvJnhu7yi5Yu5oJkq43Yib81T5H7MigqvaZJjs7u9ajTUirJf0sit0nKphZcdsvxN7%2FkVjrnzsV0vYcWdpu15ZDX3feMPbmDox13NjzRl94xenMC2bmpxuw%2FOhLDXsz3w2u9pz8wgXtljUI%2BTs5nacHIsoxJXI6oJxkWHH4p62qVFphtdWsCLBn7%2FAY8xmfM%3D"

        self.headers = headers


    def run(self):
        response = requests.get(url=self.url,headers=self.headers)
        response = json.dumps(response.text)
        print(response)
        data = {}
        #主页
        for content in response["data"]:
            for list in content["deals"]:
                #评分
                data["rating"] = content["rating"]
                # 范围
                data["range"] = content["range"]
                # 标题
                data["mname"] = content["mname"]
                # 活动
                data["title"] = content["title"]
                # 价格
                data["price"] = content["price"]
                #评论数
                data["rate-count"] = content["rate-count"]
                # 下一页地址？
                data["squareimgurl"] = content["squareimgurl"]
                with open('meituai.txt','w') as f:
                    f.write(data)


# response = requests.get(url=url, headers=headers)

# #详细页
# url = "/group/v1/deal/list/id/633916552?fields=ktvplan%2Cmealcount%2Cdeposit%2Ctag%2Cterms%2ChotelExt%2Csolds%2Cnewrating%2Cdtype%2Cvalue%2Crate-count%2Cimgurl%2Cpricecalendar%2Coptionalattrs%2Cstatus%2Cmenu%2Cbookinginfo%2Ccampaigns%2Cfakerefund%2Cannouncementtitle%2Cprice%2Cstart%2Csatisfaction%2Cslug%2Crecreason%2Csecurityinfo%2Ccate%2Cvoice%2Crange%2Ctodayavaliable%2Csquareimgurl%2Cmlls%2Crdploc%2Cid%2Ctitle%2Crefund%2Ccoupontitle%2Cmurl%2Cend%2Ccampaignprice%2Cmname%2Crdcount%2Cbrandname%2Cctype%2Cshowtype%2Csubcate%2Csevenrefund%2CattrJson%2Chowuse%2Crating%2Cnobooking%2Cisappointonline%2Ccanbuyprice%2Cbookingphone&mpt_dealid=633916552&utm_source=qqcpd&utm_medium=android&utm_term=254&version_name=5.5.4&utm_content=863064010380022&utm_campaign=AgroupBgroupC210836729717185737472271486710922675481_a162807973_c0_d4_e9360358161026910304_f162807973E0Ghomepage_category1_1__a1&ci=70&uuid=E0950FB5296BFAEC18D8310611AB53A46C0CBFACD1AEE3242DF52DE2CFF0FCAA&msid=8630640103800221584411125884&__skck=09474a920b2f4c8092f3aaed9cf3d218&__skts=1584417019475&__skua=8c2c6f7e38010ad25a937d9c9d235536&__skno=f5a3396d-8933-4142-bc2d-c97a37f960c3&__skcy=9y5%2Fs6aM7MBhCzUhe2O2vT18mp0%3D HTTP/1.1"
# #地址


if __name__ == '__main__':
    meituan = MeiTuan()
    meituan.run()

