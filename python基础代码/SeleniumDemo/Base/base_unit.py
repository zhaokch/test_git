'''
抽离单元测试中的setup与tearDown
'''

import unittest
from Common.function import config_url
from selenium import webdriver

class UnitBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ChromeDriverServer = '../driver/chromedriver'
        cls.driver = webdriver.Chrome(ChromeDriverServer)
        cls.driver.get(config_url())
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()