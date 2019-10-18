# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from .BasePage import *

class OcrPage(Page):
    url = '/ocrConfirm'

    unmanage_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[1]/a[2]')   #待处理
    unmanage_list_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[1]')   #待处理列表第一条数据
    unmanage_detail_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[2]/div[4]/a[2]')  #ocr详情页确定
    unmanage_detail_confirm_loc = (By.XPATH,'/html/body/div[2]/div/div[3]/button/span')  #确认弹框

    unmanage_assign_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[2]')   #待处理列表第一条指派
    unmanage_assign_list_loc = (By.XPATH,'(//input[@type="text"])[2]')         #指派弹框列表
    unmanage_assign_aim_loc = (By.XPATH,'//li[contains(.,"党旭")]')             #被指派人
    unmanage_assign_confirm_loc = (By.XPATH,'//a[contains(.,"确定")]')          #指派确认

    receive_loc = (By.XPATH,'//div[@id="box"]/div[2]/div/div[3]/div/a')        #待领取
    receive_batch_loc = (By.XPATH,'//div[@id="box"]/div[2]/div/div[3]/div/label')   #批量领取
    receive_batch_confirm_loc = (By.XPATH,'//span[contains(.,"确定")]')           #领取确认

    def type_unmanage_detail(self):
        self.find_element(*self.unmanage_loc).click()
        sleep(1)
        self.find_element(*self.unmanage_list_loc).click()
        sleep(2)
        self.find_element(*self.unmanage_detail_loc).click()
        sleep(1)
        self.find_element(*self.unmanage_detail_confirm_loc).click()
        sleep(3)

    def type_unmanage_assign(self):
        self.find_element(*self.unmanage_assign_loc).click()
        sleep(1)
        self.find_element(*self.unmanage_assign_list_loc).click()
        sleep(1)
        self.find_element(*self.unmanage_assign_aim_loc).click()
        sleep(1)
        self.find_element(*self.unmanage_assign_confirm_loc).click()
        sleep(3)

    def type_receive(self):
        try:
            self.find_element(*self.receive_loc).click()
            sleep(1)
            self.find_element(*self.receive_batch_loc).click()
            sleep(1)
            self.find_element(*self.receive_batch_confirm_loc).click()
            sleep(2)
        except Exception as e:
            print('无待领取数据 :%s' %e)



    def Ocr_action(self):
        self.open()
        self.type_receive()
        # self.type_unmanage_assign()
        # self.type_unmanage_detail()

    ocrPass_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[1]/a[2]')
    # loginFail_loc = (By.XPATH,'//*[@id="login_box"]/div/form/div[3]/div/button')

    def type_ocrPass_hint(self):
        return self.find_element(*self.ocrPass_loc).text

    # def type_ocrFail_hint(self):
    #     return self.find_element(*self.loginFail_loc).text

