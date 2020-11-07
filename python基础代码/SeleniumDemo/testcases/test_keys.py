import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestKeys(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.baidu.com/')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_keys(self):
        self.driver.find_element_by_id('kw').send_keys('seleniumtest')
        time.sleep(3)
        self.driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
        time.sleep(3)