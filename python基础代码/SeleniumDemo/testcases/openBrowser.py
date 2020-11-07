# 打开浏览器

from selenium import webdriver
import os

def open_chrome():
    # 将chromedriver驱动器放到/usr/local/bin目录下面，chmod +7 chromedriver
    # driver = webdriver.Chrome()
    # driver.get('https://www.baidu.com')

    ChromeDriverServer = '../driver/chromedriver'
    driver = webdriver.Chrome(ChromeDriverServer)
    # driver.get('https://www.baidu.com')
    return driver

def open_ie():
    IEDriverServer = '../driver/IEDriverServer.exe'
    os.environ['webdriver.ie.driver'] = IEDriverServer
    driver = webdriver.Ie(IEDriverServer)
    driver.get('https://www.baidu.com')

def open_firefox():
    driver = webdriver.Firefox(executable_path='../driver/geckodriver')
    driver.get('https://www.baidu.com')

if __name__ == '__main__':
    open_firefox()
