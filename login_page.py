# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.WeComPO.register_page import RegisterPage


class LoginPage:

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def scan(self):
        print("扫描二维码")
        pass

    def goto_register(self):
        """
        跳转到注册页面
        :return:
        """
        #点击注册按钮
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        #跳转到注册页面
        return RegisterPage(self.driver)

