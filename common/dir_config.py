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

test_data_dir = os.path.join(base_dir, "data")

test_cases_dir = os.path.join(base_dir, "test_cases")

htmlreport_dir = os.path.join(base_dir, "output/reports")

logs_dir = os.path.join(base_dir, "output/logs")

# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir, "output/screenshots")

caps_dir = os.path.join(base_dir, "caps")
