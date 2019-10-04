# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

from appium.webdriver.common.mobileby import MobileBy


class IndexPageLocator(object):

    # 导航栏  首页、服务、我的  id相同
    nav_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_tab_icon"

    # 账单
    order_nav_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("账单")'
