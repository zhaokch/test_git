import unittest
from selenium import webdriver
import time

class TestFuwenben(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.wangeditor.com/')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_fuwenben(self):
        time.sleep(5)
        self.driver.find_element_by_class_name('w-e-icon-image').click()
        time.sleep(3)
        self.driver.find_element_by_class_name('w-e-icon-upload2').send_keys('/Users/carina/Desktop/教学材料/selenium.docx')
        time.sleep(3)