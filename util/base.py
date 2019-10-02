# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/8/29

E-mail:keen2020@outlook.com

=================================


"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# desired_caps["automationName"] = "UiAutomator2"

desired_caps = {}

desired_caps["platformName"] = "Android"  # 平台名称
desired_caps["platformVersion"] = "9"  # 平台版本,雷电模拟器的安卓版本是5.1,真机以实际版本为准
desired_caps["deviceName"] = "mi8_lite"  # 设备名称，可以随便写
desired_caps["appPackage"] = 'com.cashier.jiutongshanghu'  # 应用包名 com.cashier.jiutongshanghu
desired_caps["appActivity"] = 'com.cashier.jiutongshanghu.home.home_main.activity.StartActivity'  # 应用入口页面
desired_caps["noReset"] = True  # 不重置应用的状态

# desired_caps["chromedriverExecutable"] = 'D:\\ChromeDrivers\\chrome39-42\\chromedriver.exe'

# 2、连接appium desktop，向appium发送请求。在哪个设备打开哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ed_login_phone"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("13072721092")

driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/ed_login_password")').send_keys("123456")

# driver.find_element_by_android_uiautomator(
#     'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/iv_login_jizhu")').click()

driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/but_login")').click()

# loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("账单")'
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# # 所有页面
# loc = (MobileBy.ID, 'com.cashier.jiutongshanghu:id/tv_status')
# WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
# time.sleep(1)
#
# size = driver.get_window_size()
# # 滑动之前的页面
# old = ""
# # 当前的页面
# new = driver.page_source
#
# while old != new:
#     try:
#         driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("15:40:48")')
#         print("找到 指定订单 元素了")
#     except:
#         old = new  # 滑动之前,将当前的页面赋值给old
#         driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5, 200)
#         loc = MobileBy.ID, 'com.cashier.jiutongshanghu:id/tv_status'
#         WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
#         time.sleep(1)
#         # 重新获取当前页面
#         new = driver.page_source
#     else:
#         print("找到 指定订单 元素了")
#         break

time.sleep(3)
p = driver.page_source
print(p)

# 点击 我的
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的")')
# loc1 = MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout" \
#                       "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout" \
#                       "/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout" \
#                       "/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.TextView"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

p1 = driver.page_source
print(p1)

loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/tv_setting")')
# driver.find_element_by_android_uiautomator(
#     'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/tv_setting")').click()
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击 退出登录
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("退出登录")')
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击确定
loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/dialog_normal_rightbtn"

# 点击取消
# loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/dialog_normal_leftbtn"

WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
driver.find_element(*loc).click()

# # 等待webview元素出现
# loc = (MobileBy.CLASS_NAME, 'android.webkit.WebView')
# WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
# time.sleep(2)

# # 获取当前所有的contexts
# cons = driver.contexts
# print(cons)

# # 切换到 webview --- 切换到html页面
# driver.switch_to.context(cons[1])
# time.sleep(2)
# print("当前的context: ", driver.current_context)

# print("=======================进入web自动化======================")
# 怎么得到html页面，并进行元素定位？？
# 1、 工具 - uc devtools
# 2、 chrome://inspect
# 3、 driver.page_source得到html页面。保存在一个文件中用chrome访问。
# 4、 直接找开发获取内嵌的html

# 注意chromedriver的版本 要与  安卓 系统的webview版本匹配
# 可以通过desired_caps["chromedriverExecutable"] 来指定 chromedriver的路径 。

# //button[text()="立即购买"]
# loc = (MobileBy.XPATH, '//button[text()="立即购买"]')
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()

# 步骤： 识别、开启调试模式、得到所有上下文、切换到webview、定位元素并操作(chromedriver的版本匹配)
