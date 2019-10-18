# -*- coding:utf-8 -*-
import unittest
from .model import myunit,function
from .page_object.LoginPage import *
from .page_object.OcrPage import *
from .page_object.ManualPage import *
from time import sleep

class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        print('test start...')
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
        po3 = ManualPage(self.driver)
        po3.Manual_action()
        sleep(2)
        self.assertEqual(po3.type_manualPass_hint(),'待处理')
        function.insert_img(self.driver, "manual.png")

        print('test end')


if __name__ == '__main__':
    unittest.main()