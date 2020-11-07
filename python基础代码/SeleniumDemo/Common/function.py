'''
获取测试系统URL方法
'''

import configparser
import os

# 获取项目路径
def project_path():
    return os.path.split(os.path.relpath(__file__))[0].split('C')[0]

# 返回config.ini文件中的testUrl
def config_url():
    config = configparser.ConfigParser()
    config.read('../config.ini')
    return config.get('testUrl', 'url')

if __name__ == '__main__':
    print('被测系统URL为: ' + config_url())