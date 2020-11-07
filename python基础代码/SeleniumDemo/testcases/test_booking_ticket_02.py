'''
代码封装
'''

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import time

class TestBookingTicket01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = cls.open_browser('https://trains.ctrip.com/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 将浏览器操作进行封装
    def open_browser(url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()

        return driver

    # 将操作元素进行封装
    def find_element(self, driver, **kwargs):
        key = kwargs['key']
        value = kwargs['value']

        if key.upper() == 'ID':
            locator = (By.ID, value)
        elif key.upper() == 'CLASS_NAME':
            locator = (By.CLASS_NAME, value)
        elif key.upper() == 'XPATH':
            locator = (By.XPATH, value)
        elif key.upper() == 'CSS':
            locator = (By.CSS_SELECTOR, value)
        elif key.upper() == 'LINK_TEXT':
            locator = (By.LINK_TEXT, value)
        elif key.upper() == 'NAME':
            locator = (By.NAME, value)
        elif key.upper() == 'PARTIAL_LINK_TEXT':
            locator = (By.PARTIAL_LINK_TEXT, value)
        elif key.upper() == 'TAG_NAME':
            locator = (By.TAG_NAME, value)

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
            if key.upper() == 'ID':
                element = driver.find_element_by_id(value)
            elif key.upper() == 'CLASS_NAME':
                element = driver.find_element_by_class_name(value)
            elif key.upper() == 'XPATH':
                element = driver.find_element_by_xpath(value)
            elif key.upper() == 'CSS':
                element = driver.find_element_by_css_selector(value)
            elif key.upper() == 'LINK_TEXT':
                element = driver.find_element_by_link_text(value)
            elif key.upper() == 'NAME':
                element = driver.find_element_by_name(value)
            elif key.upper() == 'PARTIAL_LINK_TEXT':
                element = driver.find_element_by_partial_link_text(value)
            elif key.upper() == 'TAG_NAME':
                element = driver.find_element_by_tag_name(value)
            else:
                print(key + ' 类型错误没有找到!')
                raise Exception(key + ' 类型错误没有找到!')
            return element

        except WebDriverException:
            print(value + ' 元素没有找到!')
            raise WebDriverException(value + ' 元素没有找到!')

    def test_01_search_ticket(self):
        # 以下变量为定义搜索火车票的出发站,到达站和出发时间
        from_station = '北京'
        to_station = '杭州'
        depart_date = '2020-11-11'

        # 以下是输入出发城市，到达城市，出发时间
        self.find_element(self.driver, **{'key':'id', 'value':'departCityName'}).send_keys(from_station)
        time.sleep(3)
        self.find_element(self.driver, **{'key':'id', 'value':'arriveCityName'}).send_keys(to_station)
        time.sleep(3)
        self.driver.execute_script("document.getElementById('departDate').removeAttribute('readonly')")
        # 需要在输入日期前先情况日期控件里的数据，要不然输入的数据就会追加到后面
        self.find_element(self.driver, **{'key':'id', 'value':'departDate'}).clear()
        self.find_element(self.driver, **{'key': 'id', 'value': 'departDate'}).send_keys(depart_date)
        time.sleep(3)

        from selenium.webdriver.common.action_chains import ActionChains
        # 将鼠标移动到空白处后点击，时间控件就会消失
        ActionChains(self.driver).move_by_offset(0,0).click().perform()
        # 点击'开始搜索'按钮
        self.find_element(self.driver, **{'key': 'class_name', 'value': 'searchbtn'}).click()

        time.sleep(3)

    def test_02_booking_ticket(self):
        self.find_element(self.driver, **{'key': 'xpath', 'value': "//div[@trainname='G57']/div[6]/div[1]/a"}).click()


    def test__03_write_people_info(self):
        time.sleep(3)
        # 输入乘客信息
        self.find_element(self.driver, **{'key': 'class_name', 'value': 'input-name'}).send_keys('小赵')
        self.find_element(self.driver, **{'key': 'xpath', 'value': "//input[@placeholder='证件号码']"}).send_keys('341203198909224897')
        self.find_element(self.driver, **{'key': 'xpath', 'value': "//input[@placeholder='请输入乘客本人手机号']"}).send_keys(
            '15678654345')

        # 选择座位
        self.find_element(self.driver, **{'key': 'xpath', 'value': "//li[text()='A']"}).click()
        time.sleep(3)
        # 输入联系人手机号
        self.find_element(self.driver, **{'key': 'id', 'value': 'contact-mobile'}).send_keys('15678654345')
        time.sleep(3)
        # 点击'优享预定'按钮
        self.find_element(self.driver, **{'key': 'xpath', 'value': "//div[@id='bookButtonVue']/button[1]"}).click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()