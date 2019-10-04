# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

import pytest
from page_ojbects.login_page import LoginPage
from page_ojbects.index_page import IndexPage
from common.tools import uninstall_appium_settings, uninstall_uiautomator2


@pytest.mark.usefixtures("start_app")
class TestLogin(object):

    def test_login_success(self, start_app):
        # 执行登录
        LoginPage(start_app).login_action("13072721092", "123456")
        # 获取登录状态
        assert IndexPage(start_app).get_login_status() is True

        # uninstall_appium_settings()
        # uninstall_uiautomator2()
