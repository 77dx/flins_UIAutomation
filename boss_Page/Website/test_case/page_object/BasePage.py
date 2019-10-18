# -*- coding:utf-8 -*-
from time import sleep

class Page():
    def __init__(self,driver):
        self.driver = driver
        self.base_url = 'http://mp.flins.com.cn/bmspage/#'
        self.timeout = 10


    def _open(self,url):
        url_ = self.base_url+url
        print("Test page is %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_,'Did not land on %s' %url_

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)