# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from .BasePage import *
from util.loggers import Logger

logger = Logger(logger="RolePage").getlog()

class RolePage(Page):
    url = '/roleList'    #页面地址

    #页面各个元素的定位
    role_manage_loc = (By.XPATH,'//*[@id="menuLeft"]/ul/li[2]/ul/li[2]/ul/a/li')    #左侧角色管理
    add_role_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[2]/button[3]/span')    #添加角色
    add_role_name_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[1]/div/div[1]/input')    #角色名称
    add_role_serialNumber_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[2]/div/div/input')   #编码
    add_role_sort_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[3]/div/div[1]/input')    #排序号
    add_role_permission_1_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[5]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]/span[2]/span') #选择ocr权限
    add_role_permission_2_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[5]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[2]/span')
    add_role_permission_3_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[5]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]/span')
    add_role_permission_4_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[2]/form/div[5]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/span[2]/span')
    add_role_confirm_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[5]/div/div[3]/span/button[2]/span')   #确认

    search_role_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[1]/div/input')           #搜索角色
    search_confirm_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[2]/button[1]/span')           #搜索确认

    result_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[4]/div/div[3]/table/tbody/tr/td[2]/div')   #搜索结果

    #添加角色
    def add_role(self,roleName,serialNumber,sort):
        self.find_element(*self.add_role_loc).click()   #点击添加角色
        sleep(3)
        self.find_element(*self.add_role_name_loc).send_keys(roleName)      #角色名称
        self.find_element(*self.add_role_serialNumber_loc).send_keys(serialNumber)    #编码
        self.find_element(*self.add_role_sort_loc).send_keys(sort)   #排序号
        self.find_element(*self.add_role_permission_1_loc).click()    #权限1
        self.find_element(*self.add_role_permission_2_loc).click()
        self.find_element(*self.add_role_permission_3_loc).click()
        self.find_element(*self.add_role_permission_4_loc).click()
        sleep(1)
        self.find_element(*self.add_role_confirm_loc).click()      #提交3
        sleep(3)

    #搜索角色
    def search_role(self,roleName):
        self.find_element(*self.search_role_loc).send_keys(roleName)     #输入角色名
        self.find_element(*self.search_confirm_loc).click()            #点击搜索
        sleep(3)
        s = self.find_elements(*self.result_loc)
        if len(s) >0 :
            logger.info('角色添加成功：'+roleName)
        else:
            logger.error('角色添加失败')

    def role_action(self,roleName,serialNumber,sort):
        self.open()
        #点击左侧角色管理
        self.find_element(*self.role_manage_loc).click()
        sleep(1)
        self.add_role(roleName,serialNumber,sort)
        self.search_role(roleName)



