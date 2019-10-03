# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

import os


def uninstall_uiautomator2():
    os.system("adb uninstall io.appium.uiautomator2.server")
    print("uninstall uiautomator2.server successfully")

    os.system("adb uninstall io.appium.uiautomator2.server.test")
    print("uninstall uiautomator2.server.test successfully")


def uninstall_appium_settings():
    os.system("adb uninstall io.appium.settings")
    print("uninstall appium.settings successfully")


if __name__ == '__main__':
    uninstall_uiautomator2()
    uninstall_appium_settings()
