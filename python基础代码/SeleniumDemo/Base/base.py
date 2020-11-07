'''
对元素操作进行封装
'''

from Common.log import FrameLog
from selenium import webdriver

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.log = FrameLog().log()

    # 单星号参数代表此处接收任意多个非关键字参数
    def findele(self, *args):
        try:
            print(args)
            self.log.info('通过' + args[0] + '定位元素是' + args[1])
            return self.driver.find_element(*args)
        except:
            # 在页面上没有定位到页面元素
            self.log.error('定位元素失败')

    def click(self, *args):
        self.findele(args).click()

    def sendkey(self, *args, value):
        self.findele(args).send_keys(value)

    def js(self, str):
        self.driver.excute_script(str)

    def url(self):
        return self.driver.current_url

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def quit(self):
        self.driver.quit()