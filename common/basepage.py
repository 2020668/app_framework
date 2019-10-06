# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/29
E-mail:keen2020@outlook.com
=================================

"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from appium.webdriver.common.mobileby import MobileBy
from common.dir_config import screenshot_dir
import logging
import time
import datetime
import os


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, loc, img_desc, timeout=30, frequency=0.5):
        start = datetime.datetime.now()  # 用datetime模块获取时间
        try:
            WebDriverWait(self.driver, timeout, frequency).until(ec.visibility_of_element_located(loc))
        except:
            # 日志
            logging.exception("等待元素 {} 可见 失败！".format(loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            end = datetime.datetime.now()  # 用datetime模块获取当前时间
            logging.info("等待 {}  元素  {} 可见成功。耗时：{}".format(img_desc, loc, end - start))

    # 等待元素存在
    def wait_ele_exists(self, loc, img_desc, timeout=30, frequency=0.5):
        start = datetime.datetime.now()  # 用datetime模块获取时间
        try:
            WebDriverWait(self.driver, timeout, frequency).until(ec.presence_of_element_located(loc))
        except:
            # 日志
            logging.exception("等待元素 {} 存在 失败！".format(loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            end = datetime.datetime.now()  # 用datetime模块获取当前时间
            logging.info("等待 {}  元素  {} 存在成功。耗时：{}".format(img_desc, loc, end - start))

    # 查找元素
    def get_element(self, loc, img_desc, find_all=False):
        """
        :param loc: 元组类型。元素定位表达式: (定位类型,定位表达式)
        :param img_desc: 截图命名
        :param find_all: 是否查找所有匹配的元素。为False表示只匹配一个。为True表示获取匹配所有。
        :return: Webelement对象。当find_all为True时，返回的是列表。
        """
        try:
            if find_all is True:
                ele = self.driver.find_elements(*loc)
            else:
                ele = self.driver.find_element(*loc)
        except:
            # 日志
            logging.exception("查找  {} 元素 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            logging.info("查找  {} 元素 {} 成功！".format(img_desc, loc))
            return ele

    # 元素可以是通过元素定位查找，也可以是直接是webElement对象。
    def _deal_element(self, loc, img_desc, timeout=30, frequency=0.5, wait_type="visible"):
        # 先等待可见,再查找元素
        if isinstance(loc, tuple):  # 元素定位表达式类型
            if wait_type == "visible":  # 等待元素可见
                self.wait_ele_visible(loc, img_desc, timeout, frequency)
            else:  # 等待元素存在
                self.wait_ele_exists(loc, img_desc, timeout, frequency)
            return self.get_element(loc, img_desc)
        elif isinstance(loc, WebElement):  # WebElement对象
            return loc
        else:
            logging.error("参数loc: {} 即不是元组，也不是WebElement对象，无法根据此参数找到元素。".format(loc))
            raise

    # 点击元素
    def click_element(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        # 操作
        try:
            ele.click()        # 点击操作
            logging.info("点击  {} 元素 {} 成功！".format(img_desc, loc))
        except:
            # 日志
            logging.exception("点击  {} 元素 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    def input_text(self, loc, value, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        # 操作
        try:
            ele.send_keys(value)  # 点击操作
            logging.info("在 {} 元素 {} 上输入文本值：{} 成功！".format(img_desc, loc, value))
        except:
            # 日志
            logging.exception("在 {} 元素 {} 上输入文本值：{} 失败！".format(img_desc, loc, value))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    # 获取元素的属性值
    def get_element_attribute(self, loc, attr_name, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency,wait_type="precence")
        # 获取属性
        try:
            attr_value = ele.get_attribute(attr_name)
        except:
            # 日志
            logging.exception("获取 {} 元素 {} 的属性 {} 失败！".format(img_desc, loc, attr_name))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.info("获取 {} 元素 {} 的属性 {} 值为:{}".format(img_desc, loc, attr_name, attr_value))
            return attr_value

    # 获取元素的文本值。
    def get_text(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type="precence")
        # 获取属性
        try:
            text = ele.text
        except:
            # 日志
            logging.exception("获取 {} 元素 {} 的文本失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.info("获取 {} 元素 {} 的文本值为:{}".format(img_desc, loc, text))
            return text

    def save_img(self, img_description):
        """
        :param img_description: 图片的描述 。格式为 页面名称_功能名
        :return:
        """
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 时间戳 time模块  不要有:
        filepath = "{}_{}.png".format(img_description, now)
        img_path = os.path.join(screenshot_dir, filepath)
        try:
            self.driver.save_screenshot(img_path)
        except:
            logging.exception("网页截图失败！")
        else:
            logging.info("截图成功，截图存放在：{}".format(img_path))

    # toast获取
    def get_toast_msg(self, part_str, model_name="model"):
        xpath = '//*[contains(@text,"{}")]'.format(part_str)
        logging.info("获取toast信息，toast表达式为：{}".format(xpath))
        try:
            WebDriverWait(self.driver, 10, 0.01).until(ec.presence_of_element_located((MobileBy.XPATH, xpath)))
            return self.driver.find_element(MobileBy.XPATH, xpath)
        except:
            logging.exception("获取toast信息失败！！")
            raise

    # 获取设备的大小
    def get_device_size(self):
        try:
            size = self.driver.get_window_size()
            logging.info("当前设备的大小为：{}".format(size))
            return size
        except:
            logging.exception("获取设备大小失败。")
            raise

    # 左右滑
    def swipe_left_right(self, start_percent=0.9, end_percent=0.1):
        size = self.get_device_size()
        try:
            logging.info("页面左右滑动，页面从坐标：{} 滑动到坐标：{}".format(size["width"] * start_percent, size["width"] * end_percent))
            self.driver.swipe(size["width"] * start_percent, size["height"] * 0.5, size["width"] * end_percent,
                              size["height"] * 0.5, 200)
            time.sleep(1)
        except:
            logging.exception("页面左右滑动失败！！")
            self.save_img("页面左右滑动失败")
            raise

    # 上下滑
    def swipe_up_down(self, start_percent=0.9, end_percent=0.1):
        size = self.get_device_size()
        try:
            self.driver.swipe(size["width"] * 0.5, size["height"] * start_percent, size["width"] * 0.5,
                              size["height"] * end_percent, 200)
            logging.info(
                "页面上下滑动，页面从坐标：{} 滑动到坐标：{}".format(size["height"] * start_percent, size["height"] * end_percent))
            time.sleep(1)
        except:
            logging.exception("页面上下滑动失败！！")
            self.save_img("页面上下滑动失败")
            raise

    # 上下左右滑动 up down left right
    def swipe_by_direction(self, direct, duration=200):
        """
        :param direct: up - 向上滑 down - 向下滑  left - 向左滑  right - 向右滑
        :return: None
        """
        size = self.get_device_size()
        if direct.lower() == "up": # 向上滑动
            self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.1, duration)
        elif direct.lower() == "down": # 向下滑动
            self.driver.swipe(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5, size["height"] * 0.9, duration)
        elif direct.lower() == "left":  # 向左滑动
            self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5, duration)
        elif direct.lower() == "right": # 向右滑动
            self.driver.swipe(size["width"] * 0.1, size["height"] * 0.5, size["width"] * 0.9, size["height"] * 0.5, duration)

    # 获取当前页面源码
    def get_page_source(self):
        logging.info("获取当前页面源码。")
        try:
            return self.driver.page_source
        except:
            logging.exception("获取页面源码失败！")
            self.save_img("获取页面源码失败")
            raise
