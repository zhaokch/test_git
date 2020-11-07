import unittest
from selenium import webdriver
import time


class TestScreenShot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://user.qunar.com/passport/login.jsp')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_screenshot_element(self):
        # 点击'密码登录'链接
        self.driver.find_element_by_class_name('pwd-login').click()
        # 整个页面截图
        self.driver.save_screenshot('../img/qunar_login.png')
        # 获取验证码元素
        vcodeImg = self.driver.find_element_by_id('vcodeImg')
        # 获取验证码对坐标
        left = vcodeImg.location['x']
        top = vcodeImg.location['y']
        right = left + vcodeImg.size['width']
        bottom = top + vcodeImg.size['height']

        from PIL import Image
        # 打开刚才保存对页面截图
        im = Image.open('../img/qunar_login.png')
        # 使用获取到的位置剪切图片
        im = im.crop((left * 2, top * 2, right * 2, bottom * 2))
        # im = im.crop((left, top, right, bottom))
        im.save('../img/im.png')


