# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from .BasePage import *

class LoginPage(Page):
    url = '/'

    username_loc = (By.XPATH,'//*[@id="login_box"]/div/form/div[1]/div/div/input')
    password_loc = (By.XPATH,'//*[@id="login_box"]/div/form/div[2]/div/div/input')
    submit_loc = (By.XPATH,'//*[@id="login_box"]/div/form/div[3]/div/button')

    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def Login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    loginPass_loc = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/label')   #登录正常，页面出现管理员
    loginFail_loc = (By.XPATH,'//*[@id="login_box"]/div/form/div[3]/div/button')  #登录失败，页面还在登录页

    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc).text