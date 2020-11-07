from selenium import webdriver
import unittest
import time

class TestSearchBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # 1. 打开百度首页
        cls.driver.get('https://www.baidu.com')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_search_baidu(self):
        # 通过tag_name来定位元素
        self.driver.find_element_by_xpath('//*[@id="form"]/span[1]').find_element_by_tag_name('input').send_keys('新闻')
        self.driver.find_element_by_xpath('//*[@id="form"]/span[2]').find_element_by_tag_name('input').click()

    def test_search_by_js(self):
        js = "document.getElementById('kw').value='新闻'"
        self.driver.execute_script(js)
        js = "document.getElementById('su').click()"
        self.driver.execute_script(js)
        time.sleep(3)
        js = "window.scrollTo(0, 300)"
        self.driver.execute_script(js)
        time.sleep(5)
