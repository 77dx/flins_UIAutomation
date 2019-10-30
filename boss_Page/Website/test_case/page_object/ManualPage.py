# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from .BasePage import *
from util.decorators import Decorators
from util.loggers import Logger

logger = Logger(logger="ManualPage").getlog()

class ManualPage(Page):
    url = '/manualEvaluation'
    #人工处理的页面
    unmanage_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[1]/a[2]')   #待处理
    unmanage_list_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[1]')   #待处理列表第一条数据
    position_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/input')  #位置
    position_aim_loc = (By.XPATH,'//body/div[2]/div/div/ul/li/span')   #左叶
    direction_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/div/div[1]/input')  #方位
    direction_aim_loc = (By.XPATH,'//body/div[3]/div/div/ul/li/span')  #
    ingredient_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/div/div[1]/input')  #成分
    ingredient_aim_loc = (By.XPATH,'//div[4]/div/div/ul/li[2]/span')
    echo_loc = (By.XPATH,'//div[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr/td[5]/div/div/div/input')  #回声
    echo_aim_loc = (By.XPATH,'//div[5]/div/div/ul/li[3]/span')
    form_loc = (By.XPATH,'(//input[@type="text"])[5]')   #形态
    form_aim_loc = (By.XPATH,'//div[6]/div/div/ul/li[2]/span')
    edge_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/div/div') #边缘
    edge_aim_loc = (By.XPATH,'//div[7]/div/div/ul/li[2]/span')
    secho_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div/div[2]')  #强回声
    secho_aim_loc = (By.XPATH,'//div[8]/div/div/ul/li/span')
    score_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[2]/div[5]/div[2]/div[3]/table/tbody/tr[1]/td[12]/div/span[1]')  #评分
    unmanage_detail_confirm_loc = (By.XPATH,'//a[contains(text(),"确认")]')  #确认
    unmanage_detail_confirm2_loc = (By.XPATH, '//span[contains(.,"狠心提交")]')
    unmanage_detail_confirm3_loc = (By.XPATH, '//button[contains(.,"确定")]')
    #人工指派
    unmanage_assign_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span[2]')   #待处理列表第一条指派
    unmanage_assign_list_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[4]/div[2]/div[1]/div/div[1]/input')         #指派弹框列表
    unmanage_assign_aim_loc = (By.XPATH,'//li[contains(.,"党旭")]')             #被指派人
    unmanage_assign_confirm_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[4]/div[2]/a')          #指派确认
    #人工待领取
    receive_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[1]/a[1]')        #待领取
    receive_batch_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[1]/label')   #批量领取
    receive_batch_confirm_loc = (By.XPATH,'/html/body/div[2]/div/div[3]/button/span')           #领取确认

    #处理出现的个数
    manage_number_loc = (By.XPATH,'//span[contains(.,"处理")]')

    #人工处理
    def type_unmanage_detail(self):
        try:
            self.find_element(*self.unmanage_loc).click()
            sleep(1)
            self.find_element(*self.unmanage_list_loc).click()
            sleep(3)
            self.find_element(*self.position_loc).click()
            sleep(3)
            self.find_element(*self.position_aim_loc).click()
            sleep(1)
            self.find_element(*self.direction_loc).click()
            sleep(1)
            self.find_element(*self.direction_aim_loc).click()
            sleep(1)
            self.find_element(*self.ingredient_loc).click()
            sleep(1)
            self.find_element(*self.ingredient_aim_loc).click()
            sleep(1)
            self.find_element(*self.echo_loc).click()
            sleep(1)
            self.find_element(*self.echo_aim_loc).click()
            sleep(1)
            self.find_element(*self.form_loc).click()
            sleep(1)
            self.find_element(*self.form_aim_loc).click()
            sleep(1)
            self.find_element(*self.edge_loc).click()
            sleep(1)
            self.find_element(*self.edge_aim_loc).click()
            sleep(1)
            self.find_element(*self.secho_loc).click()
            sleep(1)
            self.find_element(*self.secho_aim_loc).click()
            sleep(1)
            self.find_element(*self.score_loc).click()
            sleep(2)
            self.find_element(*self.unmanage_detail_confirm_loc).click()
            sleep(1)
            self.find_element(*self.unmanage_detail_confirm2_loc).click()
            sleep(1)
            self.find_element(*self.unmanage_detail_confirm3_loc).click()
            sleep(1)
            logger.info('人工-处理完成')
        except Exception as e:
            logger.error("某一特征无法定位 %s" %e)

    def type_unmanage_assign(self):
        self.find_element(*self.unmanage_assign_loc).click()
        sleep(1)
        self.find_element(*self.unmanage_assign_list_loc).click()
        sleep(1)
        self.find_element(*self.unmanage_assign_aim_loc).click()
        sleep(1)
        self.find_element(*self.unmanage_assign_confirm_loc).click()
        sleep(3)
        logger.info('人工-指派完成')

    def type_receive(self):
        try:
            self.find_element(*self.receive_loc).click()
            sleep(1)
            s = self.find_elements(*self.receive_batch_loc)
            if len(s) >0 :
                self.find_element(*self.receive_batch_loc).click()
                sleep(1)
                self.find_element(*self.receive_batch_confirm_loc).click()
                sleep(1)
                logger.info('批量已领取')
            else:
                logger.warning('人工-无可领取数据')
        except Exception as e:
            logger.warning('无数据可领取 :%s' %e)

    @Decorators.retry(3)
    def Manual_action(self):
        self.open()
        sleep(1)
        self.type_receive()
        self.find_element(*self.unmanage_loc).click()
        sleep(2)
        result = self.find_elements(*self.manage_number_loc)
        if len(result) >= 2:
            self.type_unmanage_assign()
            self.type_unmanage_detail()
        elif len(result) == 1:
            self.type_unmanage_detail()
        else:
            logger.warning('人工-无可处理数据')

    manualPass_loc = (By.XPATH,'//*[@id="box"]/div[2]/div/div[3]/div[1]/a[2]')
    # loginFail_loc = (By.XPATH,'//*[@id="login_box"]/div/form/div[3]/div/button')

    def type_manualPass_hint(self):
        return self.find_element(*self.manualPass_loc).text

    # def type_ocrFail_hint(self):
    #     return self.find_element(*self.loginFail_loc).text



