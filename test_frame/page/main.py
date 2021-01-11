from test_frame.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy
import yaml

from test_frame.page.hangqingpage import HangQing
from test_frame.page.prepage import PrePage


class MainPage(PrePage):
    def goto_hangqing(self):
        # self.find_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_click(MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
        # self.start_video()
        self.basepage.load('../page/main.yaml')
        return HangQing(self.basepage)
