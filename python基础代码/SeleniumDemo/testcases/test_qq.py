import unittest
from selenium import webdriver
import time

class TestQQ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://mail.qq.com/cgi-bin/loginpage')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_qq(self):
        # 先切换到iframe
        self.driver.switch_to.frame(1)

        self.driver.find_element_by_id('u').send_keys('1222222')
        self.driver.find_element_by_id('p').send_keys('111111')
        self.driver.find_element_by_id('login_button').click()

        time.sleep(3)