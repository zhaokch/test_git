from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

class Baidu(unittest.TestCase):
    def setUp(self):
        '''测试准备工作'''
        # ChromeServerDriver = '../driver/chromedriver'
        self.driver = webdriver.Chrome()#初始化浏览器，注意要配置Chromedriver路径，比如：将chrome.exe放在C:\Program Files (x86)\Google\Chrome\Application路径下
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)#隐形等待，隐形等待时我们不会感觉到真的过了10秒，它会等到当前页面元素加载完毕。
        self.base_url = 'https://www.baidu.com/'

    def test_baidu_search(self):
        '''测试百度搜索'''
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('测试工程师')
        self.driver.find_element_by_id('su').click()
        time.sleep(1)# 显性等待，会明显感觉到程序等待的时间长度，比如:time.sleep(2)，会明显感觉程序等待了2秒钟。

    def tearDown(self):
        '''资源释放'''
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()#初始化测试用例集合对象，构建测试套件
    testunit.addTest(Baidu("test_baidu_search"))#把测试用例加入到测试用力集合中去，将用例加入到检测套件中
    fp = open('./result.html','wb')#定义测试报告存放路径
    runner = HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况')#定义测试报告
    runner.run(testunit)#执行测试用例
    fp.close()