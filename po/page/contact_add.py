from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.webdriver import WebDriver

from po.page.basepage import BasePage


class AddMember(BasePage):
    def add_member(self, username, phone):
        """添加成员
        :return:
        """
        self.find_sendkeys(MobileBy.XPATH, "//*[@text='姓名　']/..//*[@text='必填']", username)
        self.find_click(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']")

        def wait_ele_for(driver: WebDriver):
            eles = self.finds(MobileBy.XPATH, "//*[@text='女']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)
        self.find_click(MobileBy.XPATH, f"//*[@text='男']")
        self.find_sendkeys(MobileBy.XPATH,
                           "//*[contains(@text,'手机')]/..//*[@text='手机号']", phone)
        self.find_click(MobileBy.XPATH, "//*[@text='保存']")
