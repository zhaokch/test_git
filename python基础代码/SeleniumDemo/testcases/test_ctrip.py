import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestCNBlog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://passport.ctrip.com/user/reg/home')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_ctrip_login(self):
        # 点击同意协议按钮
        self.driver.find_element_by_link_text('同意并继续').click()

        # 获取滑块元素
        slider = self.driver.find_element_by_class_name('cpt-drop-btn')
        print(slider.size['width'])
        print(slider.size['height'])
        slideCode = self.driver.find_element_by_id('slideCode')
        print(slideCode.size['width'])
        print(slideCode.size['height'])

        # 鼠标左键按下不放
        ActionChains(self.driver).click_and_hold(slider).perform()
        # 平行移动滑块到滑块区域到最右端,slideCode.size['width']:滑块移动的长度，0：滑块移动的宽度
        ActionChains(self.driver).drag_and_drop_by_offset(slider, slideCode.size['width'], 0).perform()
        time.sleep(5)


