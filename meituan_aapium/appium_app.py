import multiprocessing
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random


#多模拟器的抓取
def handle_appium(info):
    cap = {
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": info['deviceName'],
        "udid": info['device'],
        "appPackage": info['appPackage'],
        "appActivity": info['appActivity'],
        "noRest": True,
        # "unicodekeyboard": True,
        # "resetkeyboard": True

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


    # driver = webdriver.Remote('http://192.168.2.154:'+str(info['port'])+'/wd/hub',cap)
    driver = webdriver.Remote('http://127.0.0.1:'+str(info['port'])+'/wd/hub',cap)
    l = get_locatin(driver)
    #随机获取数
    x1 = int(l[0] * round(random.uniform(0.35,0.7),2))
    y1 = int(l[1] * round(random.uniform(0.5,0.52),2))
    y2 = int(l[1] * round(random.uniform(0.32,0.34),2))

    wait = WebDriverWait(driver,5)
    # 美团
    a = 0
    #美团1
    # if info["device"] == "192.168.0.190:5555":
    if info["device"] == "192.168.2.245:5555":
        # 设置地理位置
        driver.set_location(28.0794753600,112.9962330200)  # 中信广场


        # elementId = 1
        # "platformName": "Android",
        # "deviceName": "MI_4LTE",
        # "appPackage": "com.sankuai.meituan.takeoutnew",
        # "appActivity": "com.sankuai.meituan.takeoutnew.ui.page.boot.WelcomeActivity",
        # "platformVersion": "6.0.1"
        # "platformName": "Android",
        # "deviceName": "MI_4LTE",
        # "appPackage": "com.sankuai.meituan.takeoutnew",
        # "appActivity": "com.sankuai.meituan.takeoutnew.ui.page.boot.WelcomeActivity",
        # "platformVersion": "6.0.1"

        while True:
            a += 1
            print("start美团1-{}".format(a))
            # 同意并使用
            # try:
            #     if wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[2]'))):
            #         print("同意并使用")
            #         driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[2]").click()
            #     else:
            #         pass
            # except:
            #     pass

            #获取文本
            # el = self.driver.find_element_by_accessibility_id('SomeAccessibilityID')
            # text = el.text
            #设置地理位置
            # self.driver.set_location(49, 123, 10)
            #获取当前url地址
            # url = self.driver.current_url()
            #切换位置服务
            #self.driver.toggle_location_services();
            #刷新
            # self.driver.refresh()
            #返回
            # self.driver.back()
            #截图
            # screenshotBase64 = self.driver.get_screenshot_as_base64()
            #名称
            # self.driver.find_element_by_accessibility_id('SomeAccessibilityID').tag_name
            #属性
            # tagName = self.driver.find_element_by_accessibility_id('SomeAccessibilityID').get_attribute('content-desc')
            #所有上下文
            # contexts = driver.contexts
            #当前上下文
            context = driver.context

            # 获取手机权限
            try:

                if wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'))):
                    print("获取设备信息")
                    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]").click()
                else:
                    pass

            except:
                pass

            # 获取手机号码IMEI权限
            try:

                if wait.until(
                        EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'))):
                        print("不再询问")
                        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]").click()
                else:
                    pass

            except:
                pass
                # 获取打电话确定按钮

            #删除新人广告
            try:
                # ????????????
                if wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//android.widget.Image[@content-desc="8HP3u6fvxcwMoAAAAASUVORK5CYII="]'))):
                    print("删除新人广告")
                    driver.find_element_by_xpath("//android.widget.Image[@content-desc='8HP3u6fvxcwMoAAAAASUVORK5CYII=']").click()
                else:
                    pass

            except:
                pass

            #进入酒店住宿
            try:
                #    ??????
                if wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//android.view.View[@content-desc="酒店住宿"]'))):
                    print("不再询问")
                    driver.find_element_by_xpath("//android.view.View[@content-desc='酒店住宿']").click()
                else:
                    pass
            except:
                pass

            # 安心住广告
            try:

                if wait.until(EC.presence_of_element_located(
                        (By.XPATH, '(//android.widget.ImageView[@content-desc="51DC84F29657039D"])[2]'))):
                    print("安心住广告")
                    driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=‘51DC84F29657039D’])[2]").click()
                else:
                    pass


            except:
                pass

            # 定位失败
            try:
                if wait.until(EC.presence_of_element_located((By.XPATH,
                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout'))):
                    print("定位页")
                    # time.sleep(2)
                    driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout').click()
                else:
                    pass

            except:
                pass


            #查找页
            try:
                if wait.until(EC.presence_of_element_located((By.XPATH,'//android.view.ViewGroup[@content-desc="B17ACBA417195CB3"]/android.view.View'))):
                    print("查找页")
                    # time.sleep(2.5)
                    driver.find_element_by_xpath(
                        '//android.view.ViewGroup[@content-desc="B17ACBA417195CB3"]/android.view.View').click()
                else:
                    pass

            except:
                pass

            #进入详情页

            try:
                # time.sleep(1)
                if wait.until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup'))):
                    print("详情页")
                    driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup').click()
                    #返回列表页
                    while True:
                        # time.sleep(4)
                        try:
                            driver.swipe(x1, y1, x1, y2)
                        except:
                            pass
                        driver.press_keycode(4)
                        if wait.until(EC.presence_of_element_located((By.XPATH,
                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup'))):
                            print("返回成功")
                            break
                        else:
                            print("返回失败")


            except:
                pass
            # 滑动
            print("滑动x1{} y1{} y2{}".format(x1,y1,y2))
            try:
                driver.swipe(x1, y1, x1, y2)
            except:
                pass


    #美团2
    # if info["device"] == "192.168.0.171:5555":
    if info["device"] == "192.168.2.101:5555":
        # 设置地理位置
        # driver.set_location(28.235, 112.93) #雨花区
        # driver.set_location(28.19799, 113.0353)  # 芙蓉区
        # driver.set_location(28, 112)   宁乡
        # print(driver.set_location(49, 123, 10)) 内蒙古
        # driver.set_location(28.14753269, 113.062601)
        # driver.set_location(28.14118, 113.09377)
        # driver.set_location(28.0883384400,112.9958994000)#大托
        driver.set_location(28.1050021500,112.9949747500)  # 桂花坪
        # elementId = 1
        # "platformName": "Android",
        # "deviceName": "MI_4LTE",
        # "appPackage": "com.sankuai.meituan.takeoutnew",
        # "appActivity": "com.sankuai.meituan.takeoutnew.ui.page.boot.WelcomeActivity",
        # "platformVersion": "6.0.1"
        # "platformName": "Android",
        # "deviceName": "MI_4LTE",
        # "appPackage": "com.sankuai.meituan.takeoutnew",
        # "appActivity": "com.sankuai.meituan.takeoutnew.ui.page.boot.WelcomeActivity",
        # "platformVersion": "6.0.1"

        while True:
            a += 1
            print("start美团2-{}".format(a))
            # 同意并使用
            # try:
            #     if wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[2]'))):
            #         print("同意并使用")
            #         driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[2]").click()
            #     else:
            #         pass
            # except:
            #     pass

            # 获取文本
            # el = self.driver.find_element_by_accessibility_id('SomeAccessibilityID')
            # text = el.text
            # 设置地理位置
            # self.driver.set_location(49, 123, 10)
            # 获取当前url地址
            # url = self.driver.current_url()
            # 切换位置服务
            # self.driver.toggle_location_services();
            # 刷新
            # self.driver.refresh()
            # 返回
            # self.driver.back()
            # 截图
            # screenshotBase64 = self.driver.get_screenshot_as_base64()
            # 名称
            # self.driver.find_element_by_accessibility_id('SomeAccessibilityID').tag_name
            # 属性
            # tagName = self.driver.find_element_by_accessibility_id('SomeAccessibilityID').get_attribute('content-desc')
            # 所有上下文
            # contexts = driver.contexts
            # 当前上下文
            context = driver.context

            # 获取手机权限
            try:

                if wait.until(EC.presence_of_element_located((By.XPATH,
                                                              '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'))):
                    print("获取设备信息")
                    driver.find_element_by_xpath(
                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]").click()
                else:
                    pass

            except:
                pass

            # 获取手机号码IMEI权限
            try:

                if wait.until(
                        EC.presence_of_element_located((By.XPATH,
                                                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'))):
                    print("不再询问")
                    driver.find_element_by_xpath(
                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]").click()
                else:
                    pass

            except:
                pass
                # 获取打电话确定按钮

            # 删除新人广告
            try:
                # ????????????
                if wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//android.widget.Image[@content-desc="8HP3u6fvxcwMoAAAAASUVORK5CYII="]'))):
                    print("删除新人广告")
                    driver.find_element_by_xpath(
                        "//android.widget.Image[@content-desc='8HP3u6fvxcwMoAAAAASUVORK5CYII=']").click()
                else:
                    pass

            except:
                pass

            # 进入酒店住宿
            try:
                #    ??????
                if wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//android.view.View[@content-desc="酒店住宿"]'))):
                    print("不再询问")
                    driver.find_element_by_xpath("//android.view.View[@content-desc='酒店住宿']").click()
                else:
                    pass
            except:
                pass

            # 安心住广告
            try:

                if wait.until(EC.presence_of_element_located(
                        (By.XPATH, '(//android.widget.ImageView[@content-desc="51DC84F29657039D"])[2]'))):
                    print("安心住广告")
                    driver.find_element_by_xpath(
                        "(//android.widget.ImageView[@content-desc=‘51DC84F29657039D’])[2]").click()
                else:
                    pass


            except:
                pass

            # 定位失败
            try:
                if wait.until(EC.presence_of_element_located((By.XPATH,
                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout'))):
                    print("定位页")
                    # time.sleep(2)
                    driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout').click()
                else:
                    pass

            except:
                pass

            # 查找页
            try:
                if wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//android.view.ViewGroup[@content-desc="B17ACBA417195CB3"]/android.view.View'))):
                    print("查找页")
                    # time.sleep(2.5)
                    driver.find_element_by_xpath(
                        '//android.view.ViewGroup[@content-desc="B17ACBA417195CB3"]/android.view.View').click()
                else:
                    pass

            except:
                pass

            # 进入详情页

            try:
                if wait.until(EC.presence_of_element_located((By.XPATH,
                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup'))):
                    print("详情页")
                    driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup').click()
                    # 返回列表页
                    while True:
                        # time.sleep(4)
                        try:
                            driver.swipe(x1, y1, x1, y2)
                        except:
                            pass
                        driver.press_keycode(4)
                        if wait.until(EC.presence_of_element_located((By.XPATH,
                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup'))):
                            print("返回成功")
                            break
                        else:
                            print("返回失败")


            except:
                pass
            # 滑动
            print("滑动x1{} y1{} y2{}".format(x1, y1, y2))
            try:
                driver.swipe(x1, y1, x1, y2)
            except:
                pass
def get_locatin(driver):
    x =driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    # print(x,y)
    return (x,y)

if __name__ == '__main__':
    m_list = []
    devices_list = [
        {
            "device": "192.168.2.245:5555",
            # "device": "192.168.0.190:5555",
            "deviceName": "MI_4LTE",
            # "deviceName": "OPPO_R11st",
            # "device": "127.0.0.1:62001",
            "port": 4725,
            "appPackage": "com.sankuai.meituan",
            "appActivity": "com.meituan.android.pt.homepage.activity.Welcome",
            "key": '美团2'
        },

        # {
        #     # "device": "192.168.2.193:5555",
        #     # "deviceName": "DRA-AL00",
        #     # "deviceName": "OPPO_R11st",
        #     "device": "127.0.0.1:62001",
        #     "port": 4723,
        #     "appPackage": "com.ss.android.ugc.aweme",
        #     "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
        #     "key": '抖音'
        # },
        {
            "device": "192.168.2.101:5555",
            # "device": "192.168.0.171:5555",
            "deviceName": "MI_4LTE",
            # "deviceName": "OPPO_R11st",
            # "device": "127.0.0.1:62001",
            "port": 4723,
            "appPackage": "com.sankuai.meituan",
            "appActivity": "com.meituan.android.pt.homepage.activity.Welcome",
            "key": '美团1'
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


