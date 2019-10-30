# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from .BasePage import *
from util.decorators import Decorators
from util.loggers import Logger

logger = Logger(logger="UserPage").getlog()

class UserPage(Page):
    url = '/userList'

    user_manage_1 = (By.XPATH,'//*[@id="menuLeft"]/ul/li[2]/div/span')  #左侧展开菜单
    user_manage_2 = (By.XPATH,'//*[@id="menuLeft"]/ul/li[2]/ul/li[1]/ul/a/li')              #左侧-用户管理
    add_user = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[3]/button[3]/span')        #新增用户
    add_user_account = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[1]/div/div/input')  #用户账号
    add_user_name = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[2]/div/div/input')     #姓名
    add_user_password = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[5]/div/div/input')  #密码
    add_user_permission = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[6]/div/div[2]/label[13]/span[2]')   #全权限的选择框
    add_user_comfirm = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[3]/span/button[2]/span')   #确认

    user_account_filter = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[1]/div/input')    #账号筛选框
    filter_inquire = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[3]/button[1]/span')    #确认搜索

    result = (By.XPATH,'//*[@id="box"]/div[2]/div/div[4]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div')   #搜索结果



    def add_users(self,account,name,password):
        #点击创建用户
        self.find_element(*self.add_user).click()
        sleep(3)
        #输入账号
        self.find_element(*self.add_user_account).send_keys(account)
        #输入姓名
        self.find_element(*self.add_user_name).send_keys(name)
        #输入密码
        self.find_element(*self.add_user_password).send_keys(password)
        #选择权限
        self.find_element(*self.add_user_permission).click()
        #确定
        self.find_element(*self.add_user_comfirm).click()
        sleep(2)

    def search_user(self,account):
        #账号筛选
        self.find_element(*self.user_account_filter).send_keys(account)
        #确认搜索
        self.find_element(*self.filter_inquire).click()
        sleep(2)
        user = self.find_elements(*self.result)
        if len(user) >0 :
            logger.info('用户添加成功:'+account)
        else:
            logger.error('用户添加失败')

    @Decorators.retry(3)
    def user_action(self,account,name,password):
        self.open()
        self.driver.refresh()
        sleep(1)
        self.find_element(*self.user_manage_1).click()
        self.find_element(*self.user_manage_2).click()
        sleep(1)
        self.add_users(account,name,password)
        self.search_user(account)








