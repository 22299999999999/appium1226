from appium.webdriver.common.mobileby import MobileBy

from test_frame.basepage import BasePage


class SearchPage(BasePage):
    def search(self):
        # self.find_sendkeys(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", "xxxx")
        self.load('../page/searchpage.yaml')
        # self.stop_video()
        return True
