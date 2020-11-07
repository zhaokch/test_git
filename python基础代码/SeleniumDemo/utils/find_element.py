from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

class FindElement():

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