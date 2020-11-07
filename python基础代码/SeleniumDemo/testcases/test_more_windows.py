import unittest
from selenium import webdriver
import time


class TestMoreWindows(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.baidu.com/')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_more_windows(self):
        # 点击新闻链接
        self.driver.find_element_by_link_text('新闻').click()
        # 获取所有窗口的handles
        handles = self.driver.window_handles
        # 切换到新窗口,窗口的序号是从0开始的
        self.driver.switch_to.window(handles[1])
        self.driver.find_element_by_id('ww').send_keys('python')
        self.driver.find_element_by_id('s_btn_wr').click()

        time.sleep(3)



