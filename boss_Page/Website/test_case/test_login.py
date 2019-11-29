# -*- coding:utf-8 -*-

import os,sys
# 将 项目的根目录添加到sys.path中
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from .page_object.LoginPage import *
from .model import myunit,function
from .page_object.OcrPage import *
from .page_object.ManualPage import *
from .page_object.UserPage import *
from .page_object.RolePage import *
from time import sleep
from util.loggers import Logger




logger = Logger(logger="LoginTest").getlog()

class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        logger.info('test start ...')
        #首页-登录
        po = LoginPage(self.driver)
        po.Login_action('jane','123456')
        sleep(2)
        self.assertEqual(po.type_loginPass_hint(),'小简')
        function.insert_img(self.driver, "index.png")

        #ocr确认
        # po2 = OcrPage(self.driver)
        # po2.Ocr_action()
        # sleep(2)
        # self.assertEqual(po2.type_ocrPass_hint(),'待处理')
        # function.insert_img(self.driver, "ocr.png")

        #人工确认
        # po3 = ManualPage(self.driver)
        # po3.Manual_action()
        # sleep(2)
        # self.assertEqual(po3.type_manualPass_hint(),'待处理')
        # function.insert_img(self.driver, "manual.png")

        #添加用户
        # po4 = UserPage(self.driver)
        # po4.user_action('test4','黎明','123456')
        # function.insert_img(self.driver, "user_add.png")

        #添加角色
        # po5 = RolePage(self.driver)
        # po5.role_action('测试角色4','test1',2)
        # function.insert_img(self.driver, "role_add.png")

        logger.info('test end ...')


if __name__ == '__main__':
    unittest.main()
