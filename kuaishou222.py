import requests
from requests.cookies import RequestsCookieJar


class weChat():

    def __init__(self):
        self.session = requests.session()
        self.url_first = "https://live.kuaishou.com/"
        self.url = "https://open.weixin.qq.com/connect/qrconnect?appid=wx10b8eeb25dbe601f&redirect_uri=http%3A%2F%2Flive.kuaishou.com%2FthirdPartLogin%2Fwechat%2F&response_type=code&scope=snsapi_login&state=ks_live_wechat"

        self.before_url = "http://live.kuaishou.com/thirdPartLogin/wechat/?code=021XHkTJ0Msdfa2zvFSJ0m7qTJ0XHkTq&state=ks_live_wechat"
        self.kuaishou_redrect_url = "https://live.kuaishou.com/thirdPartLogin/wechat/?code=021XHkTJ0Msdfa2zvFSJ0m7qTJ0XHkTq&state=ks_live_wechat"


        self.tree_authod_token = "https://id.kuaishou.com/pass/kuaishou/login/sns/code?code=021XHkTJ0Msdfa2zvFSJ0m7qTJ0XHkTq&state=ks_live_wechat"
        # self.url_
        self.headers = {
            # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        }


    def get_code(self):

        cookie_jar = RequestsCookieJar()
        response1=requests.get(url=self.url_first,headers = self.headers)
        resd = requests.utils.dict_from_cookiejar(response1.cookies)
        print(requests.utils.dict_from_cookiejar(response1.cookies))
        cookie_jar.set([key for key in resd][0],resd[[key for key in resd][0]])
       # response2 =self.session.get(self.url,headers = self.headers)
        response3 =self.session.get(self.before_url,headers = self.headers,cookies=cookie_jar)
        response4 =self.session.get(self.kuaishou_redrect_url, headers = self.headers)
        response5 = self.session.get(self.tree_authod_token,headers = self.headers)

        return response3,response4,response5
        # return requests.utils.dict_from_cookiejar(response.cookies)
        # requests.utils.add_dict_to_cookiejar(response.cookies,{})
        # return response.cookies


if __name__ == '__main__':
    wechat = weChat()
    response3,response4,response5 = wechat.get_code()
    print("\n\nresponse3{}\nresponse4{}\nresponse5{}".format(response3,response4,response5))



# clientid=3;
# did=web_26362ebdbf35b0baeff4209b2452d838;
# client_key=65890b29;
# infra_kuaishou_oauth_state="
# 3a526d16e504b0f2a4cf2a50eb10cfb2_{\"sid\":\"kuaishou.live.web\",\"callback\":\"\",\"appId\":\"ks_live_wechat\",
# \"htmlJump\":\"https://live.kuaishou.com/thirdPart/wechat/\",
# \"htmlJumpCallback\":\"\",\"issueTime\":1582776405}"

# https://live.kuaishou.com/thirdPart/wechat/?data={"result":1,
# "authToken":"ChRrdWFpc2hvdS5saXZlLndlYi5hdBKwAV13lRkV2pqGqvuykiYRa0TwghMkQWIgNavIImgsNQIZmKNHxRPoDU_XjhMEEJ8vBvkt3t0NtU176Yyw0RFFhRYR5rBCujP2H38qTXk0GRlrs2ohvyTqmufCHjchu108KGjF9t7NH_kAUJDhx8Rxeh9BJ3PDP-8ZsGBYYFlPlZBQ3k2tTIOp6138Ie3xxdFxikvU3GtYsUpT8Oid4L99MWiIHv-0fXLfa3YfjkcaDwdkGhJcMNBiujhBzJleIsQ7Ls4f8fAiIBQT6cS3t72jVVvN-j-KiS8x_K8Hcz6fz57ZUYrDzGJVKAUwAQ",
# "sid":"kuaishou.live.web"}