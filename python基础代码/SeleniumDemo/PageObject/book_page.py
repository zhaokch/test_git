'''
预定火车票页面
'''

from Base.base import Base
from selenium.webdriver.common.by import By
import time

class BookPage(Base):
    # 预定车票按钮
    def book(self):
        return self.findele(By.XPATH, "//*[class='List-Box']/div/div/div[5]/div/a")

    # 高铁
    def book_high_speed_train(self):
        return self.findele(By.XPATH, "//*[@id='search_cate_vue']/dl[1]/dd[2]/label/i")

    # 二等座
    def book_second_class(self):
        return self.findele(By.XPATH, "//*[@id='search_cate_vue']/dl[2]/dd[4]/label/i")

    def book_btn(self):
        try:
            self.book_high_speed_train().click()
            self.book_second_class().click()
            self.book().click()
        except:
            self.log.error('车次查询失败')

        return self.url()
