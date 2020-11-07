#encoding=utf-8
from selenium import webdriver
import unittest
import HTMLTestRunner
import time

class TestSuite(unittest.TestCase):
    def setUp(self):
        ChromeServerDriver = '../driver/chromedriver'
        self.driver = webdriver.Chrome(ChromeServerDriver)

    def tearDown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id('kw').send_keys('python')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)

        assert u'python' in self.driver.page_source, '页面中不存在要搜索的关键字'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
    # 设置生成报告HTML文件地址
    file_name = '../report/report.html'
    fp = open(file_name, 'wb')
    # 设置报表页面的title和报表总结描述内容
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='test_baidu_report', description='Report_Description')
    runner.run(suite)
    fp.close()
    print('测试完成')