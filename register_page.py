# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def register(self):
        """
        注册内容填写
        :return:
        """
        #输入企业名称
        self.driver.find_element(By.ID, "corp_name").send_keys("紫光华智")
        #输入管理员信息
        self.driver.find_element(By.ID, "manager_name").send_keys("zhangshuyi")
        #点击同意
        self.driver.find_element(By.ID, "iagree").click()

        #点击注册
        self.driver.find_element(By.ID, "submit_btn").click()

        return True
