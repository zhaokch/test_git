import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestFeifei(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.qunar.com/')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_feifei(self):
        # 点击登录链接
        self.driver.find_element_by_link_text('登录').click()
        # 点击密码登录链接
        self.driver.find_element_by_class_name('pwd-login').click()

        # 将登录界面截图
        self.driver.save_screenshot('../img/login.png')
        # 获取验证码元素
        vcodeImg = self.driver.find_element_by_id('vcodeImg')
        # 获取验证码坐标
        left = vcodeImg.location['x']
        top = vcodeImg.location['y']
        right = left + vcodeImg.size['width']
        bottom = top + vcodeImg.size['height']

        from PIL import Image
        # 打开登录界面的截图
        img = Image.open('../img/login.png')
        # 将验证码图片截切出来
        img = img.crop((left*2, top*2, right*2, bottom*2))
        # 保存验证码图片
        img.save('../img/vcodeImg.png')
        time.sleep(3)

        from utils.fateadm_api import TestFunc
        # 获取验证码
        # vcode = TestFunc('125278', 'wOhJQYcoTCYPa0q3Sme0WKC4Z4kXS2ZP', '../img/vcodeImg.png')
        vcode = TestFunc()
        print('vcode: ', vcode)
        # 登录用户
        self.driver.find_element_by_name('username').send_keys('15010369878')
        self.driver.find_element_by_name('password').send_keys('qwe123456')
        self.driver.find_element_by_name('vcode').send_keys(vcode)
        # 如果用户名密码正确话点击登录按钮就能正常登录
        time.sleep(5)
        self.driver.find_element_by_id('submit').click()

        time.sleep(3)


