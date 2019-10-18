# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep,ctime
from util.logger import Loggers
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BossUITest(unittest.TestCase):
    def setUp(self):
        self.log = Loggers(level='info')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                               #浏览器窗口最大化
        self.driver.get("http://mp.flins.com.cn/bmspage/#/")
        self.driver.implicitly_wait(10)                             #全局隐式等待10s

    #boss流程
    def test_login(self):
        driver = self.driver
        try:
            #登录
            self.login(driver)
            #ocr待领取
            self.ocr_pending(driver)
            #ocr指派
            self.ocr_assign(driver)
            #ocr处理
            self.ocr_process(driver)

            #切换人工处理
            driver.find_element_by_xpath('//*[@id="menuLeft"]/ul/li[1]/ul/li[2]/ul/a/li').click()
            self.log.logger.info('进入人工处理')
            sleep(5)
            #人工-待领取
            self.people_pending(driver)

            #人工-指派
            self.people_assign(driver)

            #人工-处理
            # 点击处理
            driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[1]').click()
            sleep(5)
            self.log.logger.info('人工待处理列表第一条数据')
            self.people_process(driver)
        except NoSuchElementException as e:
            self.log.logger.error(e)


    #登录
    def login(self,driver):
        #显示等待
        # log = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_box"]/div/form/div[3]/div/button/span')))
        sleep(2)
        # 输入账号
        driver.find_element_by_xpath('//*[@id="login_box"]/div/form/div[1]/div/div/input').send_keys('admin')
        self.log.logger.info('账号：admin')
        # 输入密码
        driver.find_element_by_xpath('//*[@id="login_box"]/div/form/div[2]/div/div/input').send_keys('123456')
        self.log.logger.info('密码：******')
        # 点击登录
        driver.find_element_by_xpath('//*[@id="login_box"]/div/form/div[3]/div/button').click()
        self.log.logger.info('登录成功')
        sleep(5)

    #ocr待领取
    def ocr_pending(self,driver):
        # 切换到ocr待领取列表
        driver.find_element_by_xpath('//div[@id="box"]/div[2]/div/div[3]/div/a').click()
        sleep(3)
        self.log.logger.info('切换到ocr待领取列表')
        try:
            driver.find_element_by_xpath('//div[@id="box"]/div[2]/div/div[3]/div/label').click()
            sleep(2)
            self.log.logger.info('点击批量领取')
            driver.find_element_by_xpath('//span[contains(.,"确定")]').click()
            self.log.logger.info('批量领取确认')
            sleep(2)
        except Exception as e:
            self.log.logger.error('ocr无可领取数据')
            sleep(2)

    #ocr待处理
    def ocr_process(self,driver):
        # 处理列表第一条数据
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[1]').click()
        self.log.logger.info('进入ocr待处理列表第一条数据')
        sleep(2)
        # 确认
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[4]/a[2]').click()
        self.log.logger.info('ocr确认')
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        self.log.logger.info('ocr确认弹框确认')
        sleep(3)

    #ocr指派
    def ocr_assign(self,driver):
        #切换到ocr待处理列表
        driver.find_element_by_xpath('//div[@id="box"]/div[2]/div/div[3]/div/a[2]').click()
        sleep(2)
        self.log.logger.info("切换ocr待处理列表")
        driver.find_element_by_xpath('//span[contains(.,"指派")]').click()
        sleep(1)
        self.log.logger.info("点击ocr指派")
        driver.find_element_by_xpath('(//input[@type="text"])[2]').click()
        sleep(1)
        self.log.logger.info("点击指派下拉框")
        driver.find_element_by_xpath('//li[contains(.,"党旭")]').click()
        sleep(1)
        self.log.logger.info("选择被指派人dx")
        driver.find_element_by_xpath('//a[contains(.,"确定")]').click()
        sleep(2)
        self.log.logger.info("点击确定")

    #人工-指派
    def people_assign(self,driver):
        #点击指派
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[2]').click()
        sleep(1)
        self.log.logger.info('点击人工指派')
        #点击下拉菜单
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[4]/div[2]/div[1]/div/div[1]/input').click()
        sleep(1)
        self.log.logger.info('点击下拉菜单')
        driver.find_element_by_xpath('//li[contains(.,"党旭")]').click()
        sleep(1)
        self.log.logger.info('选择被指派人')
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[4]/div[2]/a').click()
        sleep(3)
        self.log.logger.info('确认')


    #人工待领取
    def people_pending(self,driver):
        #切换到待领取列表
        driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[1]/a[2]').click()
        sleep(3)
        self.log.logger.info('切换到待领取列表')
        try:
            driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[3]/div[1]/label').click()
            sleep(2)
            self.log.logger.info('点击批量领取')
            driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
            self.log.logger.info('批量领取确认')
            sleep(2)
        except Exception as e:
            self.log.logger.error('无可领取数据')
            sleep(2)


    #人工处理数据
    def people_process(self,driver):
        try:
            #位置
            driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input').click()
            sleep(1)
            driver.find_element_by_xpath('//body/div[2]/div/div/ul/li/span').click()
            sleep(1)
            self.log.logger.info("位置已选择")

            #方位
            driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/div/div[1]/input').click()
            sleep(1)
            driver.find_element_by_xpath('//body/div[3]/div/div/ul/li/span').click()
            sleep(1)
            self.log.logger.info("方位已选择")

            #成分
            driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/div/div[1]/input').click()
            sleep(1)
            driver.find_element_by_xpath('//div[4]/div/div/ul/li[2]/span').click()
            sleep(1)
            self.log.logger.info("成分已选择")

            #回声
            driver.find_element_by_xpath('//div[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr/td[5]/div/div/div/input').click()
            sleep(1)
            driver.find_element_by_xpath('//div[5]/div/div/ul/li[3]/span').click()
            sleep(1)
            self.log.logger.info("回声已选择")

            #形态
            driver.find_element_by_xpath('(//input[@type="text"])[5]').click()
            sleep(1)
            driver.find_element_by_xpath('//div[6]/div/div/ul/li[2]/span').click()
            sleep(1)
            self.log.logger.info("形态已选择")

            #边缘
            driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/div/div').click()
            sleep(1)
            driver.find_element_by_xpath('//div[7]/div/div/ul/li[2]/span').click()
            sleep(1)
            self.log.logger.info("边缘已选择")

            #强回声
            driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div/div[2]').click()
            sleep(1)
            driver.find_element_by_xpath('//div[8]/div/div/ul/li/span').click()
            sleep(1)
            self.log.logger.info("强回声已选择")

            # 评分
            driver.find_element_by_xpath('//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[12]/div/span[1]').click()
            self.log.logger.info('已评分')
            sleep(2)
            # 确认
            driver.find_element_by_xpath('//a[contains(text(),"确认")]').click()
            self.log.logger.info('确认')
            sleep(1)
            driver.find_element_by_xpath('//span[contains(.,"狠心提交")]').click()
            self.log.logger.info('狠心提交')
            sleep(2)
            driver.find_element_by_xpath('//button[contains(.,"确定")]').click()
        except Exception as e:
            self.log.logger.info("没有可处理数据或特征选择异常了")






    def tearDown(self):
        sleep(5)
        self.driver.close()
        self.log.logger.info('关闭浏览器')






if __name__ == '__main__':
    unittest.main()