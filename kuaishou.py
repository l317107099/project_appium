import multiprocessing
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random

# cap = {
#   "platformName": "Android",
#   "deviceName": "127.0.0.1:62001",
#   "appPackage": "com.smile.gifmaker",
#   "appActivity": "com.yxcorp.gifshow.HomeActivity",
#   "platformVersion": "5.1.1",
#   "noRest": True
# }

#多模拟器的抓取
def handle_appium(info):
    cap = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": info['deviceName'],
        "udid": info['device'],
        "appPackage": info['appPackage'],
        "appActivity": info['appActivity'],
        "noRest": True,
        "unicodekeyboard": True,
        "resetkeyboard": True

    }
    # #快手
    # cap = {
    #   "platformName": "Android",
    #     #夜神的ip地址
    #   "deviceName": device,
    #     # 夜神的ip地址
    #   "udid":device,
    #   "appPackage": "com.smile.gifmaker",
    #   "appActivity": "com.yxcorp.gifshow.HomeActivity",
    #     #安卓版本或夜神版本
    #   "platformVersion": "6.5.0.0",
    #   "noRest": True
    # }
    # #酷狗
    # cap = {
    #     "platformName": "Android",
    #     # 夜神的ip地址
    #     "deviceName": device,
    #     # 夜神的ip地址
    #     "udid": device,
    #     "appPackage": "com.kugou.android",
    #     "appActivity": "com.kugou.android.app.splash.SplashActivity",
    #     # 安卓版本或夜神版本
    #     "platformVersion": "6.5.0.0",
    #     "noRest": True
    # }
    #
    # #抖音
    # cap = {
    #     "platformName": "Android",
    #     # 夜神的ip地址
    #     "deviceName": device,
    #     # 夜神的ip地址
    #     "udid": device,
    #     "appPackage": "com.ss.android.ugc.aweme",
    #     "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    #     # 安卓版本或夜神版本
    #     "platformVersion": "6.5.0.0",
    #     "noRest": True
    # }


    # driver = webdriver.Remote('http://192.168.2.154:'+str(info['port'])+'/wd/hub',cap)
    driver = webdriver.Remote('http://127.0.0.1:'+str(info['port'])+'/wd/hub',cap)
# driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.smile.gifmaker:id/wechat_login_text']").click()
    l = get_locatin(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)

    wait = WebDriverWait(driver,5)
    # 抖音
    a = 0

    if  info["appActivity"] == "com.ss.android.ugc.aweme.main.MainActivity":

        while True:
            a+=1
            print("start抖音{}".format(a))
             # 个人信息
            try:
                if wait.until(EC.presence_of_element_located((By.ID,'com.ss.android.ugc.aweme:id/a91'))):
                    print("个人信息保护指引")
                    driver.find_element_by_id("com.ss.android.ugc.aweme:id/a91").click()
                else:
                    pass
            except:
                pass

            # 获取手机权限
            try:
                print("获取手机权限")
                if wait.until(EC.presence_of_element_located((By.ID,'android:id/button2'))):
                    print("个人信息保护指引")
                    driver.find_element_by_id("android:id/button2").click()
                else:
                    pass

            except:
                pass

            #获取打电话是否询问
            try:

                if wait.until(EC.presence_of_element_located((By.ID,'com.android.packageinstaller:id/do_not_ask_checkbox'))):
                    print("不再询问")
                    driver.find_element_by_id("com.android.packageinstaller:id/do_not_ask_checkbox").click()
                else:
                    pass

            except:
                pass
                # 获取打电话确定按钮
            try:

                if wait.until(EC.presence_of_element_located(
                        (By.ID, 'com.android.packageinstaller:id/permission_deny_button'))):
                    print("不再询问")
                    driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button").click()
                else:
                    pass

            except:
                pass

            #获取设备位置信息 是否询问
            try:

                if wait.until(EC.presence_of_element_located((By.ID,'com.android.packageinstaller:id/do_not_ask_checkbox'))):
                    print("获取设备位置信息")
                    driver.find_element_by_id("com.android.packageinstaller:id/do_not_ask_checkbox").click()
                else:
                    pass

            except:
                pass
            # 获取设备位置信息确定按钮
            try:

                if wait.until(EC.presence_of_element_located((By.ID,'com.android.packageinstaller:id/permission_deny_button'))):
                    print("获取设备位置信息")
                    driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button").click()
                else:
                    pass

            except:
                pass

            # try:
            #
            #     if wait.until(EC.presence_of_element_located((By.ID,'com.ss.android.ugc.aweme:id/a2p'))):
            #         print("个人信息保护指引")
            #         driver.find_element_by_id("com.ss.android.ugc.aweme:id/a2p").click()
            #     else:
            #         pass
            #
            # except:
            #     pass
            time.sleep(random.randint(2,5))
            #进入评论
            try:
                if wait.until(lambda x: x.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a5i')):
                    driver.find_element_by_id("com.ss.android.ugc.aweme:id/a5i").click()
                    time.sleep(random.randint(1, 3))
                    # driver.scroll()
                    driver.swipe(200, 700, 200, 500)
            except:
                pass

            # try:
            #     if wait.until(lambda x: x.driver.find_element_by_id( 'com.ss.android.ugc.aweme:id/dnh')):
            #
            #         driver.find_element_by_id("com.ss.android.ugc.aweme:id/dnh").click()
            #         time.sleep(random.randint(1,3))
            #         # driver.scroll()
            #         driver.swipe(200, 700, 200, 500)
            # except:
            #     pass
            # try:
            #     if wait.until(lambda x: x.driver.find_element_by_id( 'com.ss.android.ugc.aweme:id/zn')):
            #         driver.find_element_by_id(( 'com.ss.android.ugc.aweme:id/zn')).click()
            # except:
            #     pass

            #进入评论
            # try:
            #     if wait.until(lambda x: x.driver.find_element_by_id( 'com.ss.android.ugc.aweme:id/e_6')):
            #         driver.find_element_by_id(( 'com.ss.android.ugc.aweme:id/e_6')).click()
            #         while True:
            #             driver.swipe(453, 1517, 519, 1121)
            #             time.sleep(random.randint(1, 3))
            # except:
            #     pass

            driver.swipe(x1, y1, x1, y2)

            time.sleep(random.randint(3, 7))

    #快手
    # elif info['appActivity']=='com.yxcorp.gifshow.HomeActivity':
    #     while True:
    #         a += 1
    #         print("start快手{}".format(a))
    #         try:
    #             if wait.until(lambda x:x.driver.find_element_by_id("com.smile.gifmaker:id/positive")):
    #                 if driver.find_element_by_id("com.smile.gifmaker:id/positive"):
    #                     driver.find_element_by_id("com.smile.gifmaker:id/positive").click()
    #         except:
    #             pass
    #         try:
    #             if wait.until(lambda x:x.driver.find_element_by_id("com.smile.gifmaker:id/other_login_view")):
    #                 driver.find_element_by_id("com.smile.gifmaker:id/close_btn").click()
    #         except:
    #             pass
    #
    #
    #         driver.swipe(x1, y1, x1, y2)
    #         time.sleep(5)

    # elif info['appPackage'] == 'com.kugou.android':
    #     pass
    # # run(driver)

def get_locatin(driver):
    x =driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print(x,y)
    return (x,y)

if __name__ == '__main__':
    m_list = []
    devices_list = [
        # {
    #     "device":"192.168.2.175:5555",
    #     "port":4725,
    #     "appPackage": "com.smile.gifmaker",
    #     "appActivity": "com.yxcorp.gifshow.HomeActivity",
    #     "key":'快手'
    #
    # },

        {
            # "device": "192.168.2.193:5555",
            # "deviceName": "DRA-AL00",
            # "deviceName": "OPPO_R11st",
            "device": "127.0.0.1:62001",
            "port": 4723,
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
            "key": '抖音'
        },

        # {
        #   "device": "192.168.2.222",
        #   "port": 4725,
        #    "appPackage": "com.kugou.android",
        #   "appActivity": "com.kugou.android.app.splash.SplashActivity",
        #   "key": '酷狗'
        # },

    ]
    # devices_list=['192.168.2.204:5555','192.168.2.244:5555']
    # for i in range(len(devices_list)):
    # #     port = 4723+2*i
    #     m_list.append(multiprocessing.Process(target=handle_appium,args=(devices_list[i],port)))f

    for devices in devices_list:
        m_list.append(multiprocessing.Process(target=handle_appium,args=(devices,)))
    for m1 in m_list:
        m1.start()
    for m2 in m_list:
        m2.join()
    # for i in range(len(devices_list)):
    # 	handle_appium(devices_list[0], 4723)


