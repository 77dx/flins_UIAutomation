# -*- coding:utf-8 -*-
from selenium import webdriver


def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.PhantomJS()

    return driver


if __name__ == '__main__':
    browser()