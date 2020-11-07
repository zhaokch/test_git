import unittest
from selenium import webdriver
import time


class TestCNBlog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.cnblogs.com/')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_cnblog(self):
        # 获取cnblogs的所有cookie
        for cookie in self.driver.get_cookies():
            print(cookie)

        print('--------------------------')

        # 登录用户
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('mat-input-0').send_keys('zhaokch')
        self.driver.find_element_by_id('mat-input-1').send_keys('qwe123456')
        self.driver.find_element_by_xpath("//span[text()=' 登录 ']").click()
        time.sleep(10)

        print('after login:')
        # 打印登录后的全部cookie
        for cookie in self.driver.get_cookies():
            print(cookie)

    def test_add_cookie_for_login(self):
        time.sleep(3)
        cookie = {'domain': '.cnblogs.com', 'expiry': 1605525851, 'httpOnly': True, 'name': '.CNBlogsCookie',
                  'path': '/', 'secure': False,
                  'value': '6D1D31B792734ED142FC5779E2B61AA0503A707144ED951CA0AF4E6610F9EB5B3D7BE481586755EFDC5C4478F89996ED97D9DC6E55A5D9BA0337EE751E90AE3D17C68540F6931E56DA3E467F962AAC0CA0A37A59'}
        self.driver.add_cookie(cookie)
        cookie = {'domain': '.cnblogs.com', 'expiry': 1605525851, 'httpOnly': True,
                  'name': '.Cnblogs.AspNetCore.Cookies', 'path': '/', 'secure': False,
                  'value': 'CfDJ8AHUmC2ZwXVKl7whpe9_latfRJrvz8Jfc2UgHB2smF-rXK-a_F1_SJyllqyCjKVstIfxJ9rXFCQkqqb7JNmLM3FQoc8nvlf7a4a0W3jmbii7euSDIHFCAlxPTc0oyKVm6B0gZsfHgNVKd1gDeTCBsDYUn_mKSRz-_DyU3DC5P1JuNQ4TMzqBKa3XPRSubheksj9ywtfVuCr0Frq0A4ouHiu-xHQEk0wLiZPcGwKB7_KuwCE4zA2WB8gUMZss8nVcNgcKFX9TTrQv_hnoIhWEk5qUUS8f46wQ-aediP5kMcKYj7qepSYo5jV_SL7pWEVC8mUpSsLi7cEO9HPdzpNjhmzpdWZmxEgZAF1zyhWRsgc7-yEbqTz6ohPH9tPVt1j7nocI1BMX4fWQ_sFFmZwk0ui27lpeO4C9VC2aSSsLDuran3qtDRxWBjiSM8mK-1FzS1lmaVXeYuiVa0-sUHcUItvtL5uDFy8e0hwZYz0yciLn2vr-Z_v4-ZmsignYB4QUvj4wspmmMnDIcJGHQGSZnugJDrH_7ah8J1Y8Enaksa8E824LrQYX1ssva-4LV-g9Xw'}
        self.driver.add_cookie(cookie)
        self.driver.refresh()
        time.sleep(5)
