import unittest
from selenium import webdriver
from time import sleep

class TestWeiboLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # 1. 打开微博首页
        cls.driver.get('https://weibo.com/login.php')
        sleep(3)


    @classmethod
    def tearDownClass(cls):
        pass

    def test_weibo_login(self):
        # 2.在用户名输入框输入用户名
        # 3.在密码输入框输入密码
        # 4.点击'登录'按钮
        # 通过xpath绝对路径来定位元素
        self.driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@node-type="password"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@node-type="submitBtn"]').click()