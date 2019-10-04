# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

from common.basepage import BasePage
from page_locators.login_page_locator import LoginPageLocator as Loc
from common.tools import uninstall_appium_settings, uninstall_uiautomator2


class LoginPage(BasePage):

    # 登录操作
    def login_action(self, username, pwd):
        self.wait_ele_visible(Loc.user_loc, "登录页_等待用户名元素可见")
        self.input_text(Loc.user_loc, value=username, img_desc="登录页_输入用户名")
        self.input_text(Loc.pwd_loc, value=pwd, img_desc="登录页_输入密码")
        self.click_element(Loc.login_button_loc, img_desc="登录页_点击登录按钮")
        return self


if __name__ == '__main__':
    lg = LoginPage(BasePage)
    lg.login_action('13072721092', '123456')
    uninstall_appium_settings()
    uninstall_uiautomator2()
