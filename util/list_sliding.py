# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/9/1

E-mail:keen2020@outlook.com

=================================


"""


from appium import webdriver

desired_caps = {}

desired_caps["platformName"] = "Android"  # 平台名称
desired_caps["platformVersion"] = "5.1"  # 平台版本,雷电模拟器的安卓版本是5.1
desired_caps["deviceName"] = "mi8_lite"  # 设备名称，可以随便写
desired_caps["appPackage"] = 'com.cashier.jiutongshanghu'  # 应用包名 com.cashier.jiutongshanghu
desired_caps["appActivity"] = 'com.cashier.jiutongshanghu.home.home_main.activity.StartActivity'  # 应用入口页面
desired_caps["noReset"] = True  # 不重置应用的状态

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 判断当前页面有无要找的元素,find_element, page_source

# 如果没有,就向下滑动, 内容至少更新80%

# 滑动之后, 执行前两步

# 如找到元素, 或滑动到底部, 则不再滑动
