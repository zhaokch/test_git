import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class TestSelect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://weibo.com/signup/signup.php')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_select_by_index(self):
        element = self.driver.find_element_by_class_name('year')
        # index索引是从0开始,选择1则表示选择第二个选项
        Select(element).select_by_index(1)
        time.sleep(3)

    def test_select_by_value(self):
        element = self.driver.find_element_by_class_name('year')
        # index索引是从0开始,选择1则表示选择第二个选项
        Select(element).select_by_value('2018')
        time.sleep(3)

    def test_select_by_visible_text(self):
        element = self.driver.find_element_by_class_name('year')
        # 通过页面显示的文本进行选择
        Select(element).select_by_visible_text('2014')
        time.sleep(3)

    def test_all_selected_options(self):
        element = self.driver.find_element_by_class_name('year')
        ops = Select(element).all_selected_options
        for i in ops:
            print(i.text)

    def test_first_selected_option(self):
        element = self.driver.find_element_by_class_name('year')
        option = Select(element).first_selected_option

        print(option.text)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()