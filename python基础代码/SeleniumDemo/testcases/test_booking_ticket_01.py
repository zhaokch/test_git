import unittest
from selenium import webdriver
import time


class TestBookingTicket01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://trains.ctrip.com/')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_01_search_ticket(self):
        # 以下变量为定义搜索火车票的出发站,到达站和出发时间
        from_station = '北京'
        to_station = '杭州'
        depart_date = '2020-11-11'

        # 以下是输入出发城市，到达城市，出发时间
        self.driver.find_element_by_id('departCityName').send_keys(from_station)
        time.sleep(3)
        self.driver.find_element_by_id('arriveCityName').send_keys(to_station)
        time.sleep(3)
        self.driver.execute_script("document.getElementById('departDate').removeAttribute('readonly')")
        # 需要在输入日期前先情况日期控件里的数据，要不然输入的数据就会追加到后面
        self.driver.find_element_by_id('departDate').clear()
        self.driver.find_element_by_id('departDate').send_keys(depart_date)
        time.sleep(3)

        from selenium.webdriver.common.action_chains import ActionChains
        # 将鼠标移动到空白处后点击，时间控件就会消失
        ActionChains(self.driver).move_by_offset(0,0).click().perform()
        # 点击'开始搜索'按钮
        self.driver.find_element_by_class_name('searchbtn').click()

        time.sleep(3)

    def test_02_booking_ticket(self):
        self.driver.find_element_by_xpath("//div[@trainname='G57']/div[6]/div[1]/a").click()


    def test__03_write_people_info(self):
        time.sleep(3)
        # 输入乘客信息
        self.driver.find_element_by_class_name('input-name').send_keys('小赵')
        self.driver.find_element_by_xpath("//input[@placeholder='证件号码']").send_keys('341203198909224897')
        self.driver.find_element_by_xpath("//input[@placeholder='请输入乘客本人手机号']").send_keys('15678654345')

        # 选择座位
        self.driver.find_element_by_xpath("//li[text()='A']").click()
        time.sleep(3)
        # 输入联系人手机号
        self.driver.find_element_by_id('contact-mobile').send_keys('15678654345')
        time.sleep(3)
        # 点击'优享预定'按钮
        self.driver.find_element_by_xpath("//div[@id='bookButtonVue']/button[1]").click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()