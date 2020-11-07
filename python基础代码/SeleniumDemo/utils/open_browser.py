# -*- coding:utf-8 -*-
from selenium import webdriver

class OpenBrowser():

    def open_chrome(url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()

        return driver


if __name__ == '__main__':
    OpenBrowser.open_chrome()