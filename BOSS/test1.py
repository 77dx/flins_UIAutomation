# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep

class BossUITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://mp.flins.com.cn/bmspage/#/")

    #boss流程
    def test_login(self):
        driver = self.driver
        sleep(2)
        #登录
        self.login(driver)
        #ocr指派
        # self.ocr_assign(driver)
        #ocr处理
        # self.ocr_process(driver)

        #切换人工处理
        driver.find_element_by_xpath('//*[@id="menuLeft"]/ul/li[1]/ul/li[2]/ul/a/li').click()
        sleep(3)
        #人工-处理
        self.people_process(driver)




    #登录
    def login(self,driver):
        # 输入账号
        driver.find_element_by_xpath('//*[@id="login_box"]/div/form/div[1]/div/div/input').send_keys('admin')
        # 输入密码
        driver.find_element_by_xpath('//*[@id="login_box"]/div/form/div[2]/div/div/input').send_keys('123456')
        # 点击登录
        driver.find_element_by_xpath('//*[@id="login_box"]/div/form/div[3]/div/button').click()
        sleep(3)

    #ocr待领取
    def ocr_pending(self,driver):
        pass

    #ocr处理数据
    def ocr_process(self,driver):
        # 处理列表第一条数据
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[1]').click()
        sleep(3)
        # 确认
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[4]/a[2]').click()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

    #ocr指派
    def ocr_assign(self,driver):
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[2]').click()
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[4]/div[2]/div[1]/div/div/input').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[7]/span').click()
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[4]/div[2]/a').click()
        sleep(3)

    #人工待领取
    def people_pending(self,driver):
        pass

    #人工处理数据
    def people_process(self,driver):
        #点击处理
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[1]').click()
        sleep(2)
        #位置
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span').click()
        sleep(1)
        #方位
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/div/div[1]/input').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span').click()
        sleep(1)
        #成分
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/div/div[1]/input').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span').click()
        sleep(1)

        #回声
        # driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/div/div[1]').click()
        # sleep(1)
        # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[3]/span').click()
        # sleep(1)

        #形态
        # driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/div/div[1]').click()
        # sleep(1)
        # driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span').click()
        # sleep(1)

        #边缘
        # driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/div/div').click()
        # sleep(1)
        # driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[4]/span').click()
        # sleep(1)

        #强回声
        # driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div/div[2]').click()
        # sleep(1)
        # driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[3]/span').click()
        # sleep(1)

        #评分
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[12]/div/span[1]').click()
        sleep(2)

        #确认
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[6]/a[2]').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/button[2]/span').click()



    def tearDown(self):
        sleep(5)
        self.driver.close()






if __name__ == '__main__':
    unittest.main()