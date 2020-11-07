import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestHighSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # 1. 打开百度首页
        cls.driver.get('https://www.baidu.com/')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 2.将鼠标悬停在'设置'元素上并点击'搜索设置'链接
    # 3.遍历点击'搜索语言范围'三个单选按钮
    # 4.只点击'搜索语言范围'的某一个单选按钮
    def test_high_search(self):
        # 将鼠标移动到设置元素上
        setting_element = self.driver.find_element_by_id('s-usersetting-top')
        ActionChains(self.driver).move_to_element(setting_element).perform()
        # 点击搜索设置链接
        self.driver.find_element_by_link_text('搜索设置').click()
        time.sleep(2)
        # 找到name='SL'的所有元素
        elements = self.driver.find_elements_by_name('SL')
        print(elements)

        # 将获取的元素遍历点击
        for element in elements:
            element.click()
            time.sleep(2)

        # 只想点击某个元素
        elements[1].click()
        time.sleep(2)