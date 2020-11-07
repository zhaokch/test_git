'''
火车票搜索页面
'''

from Base.base import Base
from selenium.webdriver.common.by import By
import time

class SearchPage(Base):
    def search_leave(self):
        return self.findele(By.ID, 'departCityName')

    def search_arrive(self):
        return self.findele(By.ID, 'arriveCityName')

    def search_date(self):
        return self.findele(By.ID, 'departDate')

    def search_date_by_js(self, value):
        jsvalue = "document.getElementById('departDate').value='%s'" %(value)
        self.js(jsvalue)

    def search_btn(self):
        return self.findele(By.CLASS_NAME, 'searchbtn')

    def oneWay(self):
        return self.findele(By.XPATH, "//*[text='单程']")

    def returnTicket(self):
        return self.findele(By.XPATH, "//*[text='往返']")

    def transit(self):
        return self.findele(By.XPATH, "//*[text='中转']")

    def search_high_speed_train_checkbox(self):
        return self.findele(By.CLASS_NAME, 'checkbox')

    def search_train(self, leave, arrive, leave_date):
        self.search_leave().send_keys(leave)
        time.sleep(2)
        self.search_arrive().send_keys(arrive)
        self.search_date().send_keys(leave_date)
        self.search_btn().click()
        time.sleep(3)
        return self.url()