# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from web.WeComPO.login_page import LoginPage
from web.WeComPO.register_page import RegisterPage


class IndexPage:

    def __init__(self):
        """
        初始化driver
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        """
        跳转到登录页面
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        #跳转到登录PO
        return LoginPage(self.driver)

    def goto_register(self):
        """
        跳转到注册页面
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        #跳转到注册PO
        return RegisterPage(self.driver)