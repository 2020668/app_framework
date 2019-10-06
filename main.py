# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

import os
import pytest

if __name__ == '__main__':
    pytest.main(["-s", "-v", "--html=output/reports/report.html", "--alluredir=output/allure"])
    os.system("allure serve output/allure")
