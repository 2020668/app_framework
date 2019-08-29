# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/29
E-mail:keen2020@outlook.com
=================================

"""

import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir, "TestDatas")

testcases_dir = os.path.join(base_dir, "TestCases")

htmlreport_dir = os.path.join(base_dir, "Outputs/reports")

logs_dir = os.path.join(base_dir, "Outputs/logs")

# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir, "Outputs/imgs")
print(screenshot_dir)
