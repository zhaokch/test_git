import unittest
import HTMLTestRunner
from Common.function import project_path
import time

if __name__ == '__main__':
    test_dir = project_path() + 'testcases'
    tests = unittest.defaultTestLoader.discover(test_dir, pattern='train_*.py', top_level_dir=None)
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    filepath = project_path() + '/Reports/' + now + '.html'
    fp = open(filepath, 'wb')
    # 定义测试报告都标题和描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试报告')
    runner.run(tests)
    fp.close()