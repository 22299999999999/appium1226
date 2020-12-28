from appium.webdriver.common.mobileby import MobileBy

from po.page.address_list_page import ConTact
from po.page.basepage import BasePage


class MainPage(BasePage):

    def goto_con(self):
        """进入通讯录页
        :return:
        """
        self.find_click(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id ='com.tencent.wework:id/elq']")
        return ConTact(self.driver)
