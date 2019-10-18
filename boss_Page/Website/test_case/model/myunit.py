# -*- coding:utf-8 -*-
from boss_Page.driver.driver import browser
import unittest

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()