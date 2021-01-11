from test_frame.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy
import yaml

from test_frame.page.hangqingpage import HangQing


class MainPage(BasePage):
    def goto_hangqing(self):
        # self.find_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_click(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
        # self.start_video()
        self.load('../page/main.yaml')
        return HangQing(self.driver)
