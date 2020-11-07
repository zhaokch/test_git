'''
乘客信息页面
'''
from Base.base import Base
from selenium.webdriver.common.by import By

class PassengerInfo(Base):
    # 乘客姓名
    def passenger_name(self):
        return self.findele(By.CLASS_NAME, 'input-name')

    # 乘客身份证
    def passenger_card(self):
        return self.findele(By.XPATH, '//*[@id="inputPassengerVue"]/div[1]/ul/li[3]/input')

    # 乘客手机号
    def passenger_phone(self):
        return self.findele(By.XPATH, '//*[@id="inputPassengerVue"]/div[1]/ul/li[6]/input')

    # 座位
    def seat(self):
        return self.findele(By.XPATH, '//*[text="A"]')

    # 联系人
    def contact_phone(self):
        return self.findele(By.ID, 'contact-mobile')

    # 预定按钮
    def book_btn(self):
        return self.findele(By.CLASS_NAME, 'btn-putong')

