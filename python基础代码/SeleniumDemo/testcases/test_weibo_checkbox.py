import unittest
from selenium import webdriver
import time

class TestWeiboCheckbox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://weibo.com/login.php')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_weibo_checkbox(self):
        selected = self.driver.find_element_by_id('login_form_savestate').is_selected()
        print('selected01:', selected)
        self.driver.find_element_by_id('login_form_savestate').click()
        selected = self.driver.find_element_by_id('login_form_savestate').is_selected()
        print('selected02:', selected)

        time.sleep(5)
