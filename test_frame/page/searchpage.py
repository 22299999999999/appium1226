from appium.webdriver.common.mobileby import MobileBy

from test_frame.page.prepage import PrePage


class SearchPage(PrePage):
    def search(self):
        # self.find_sendkeys(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", "xxxx")
        self.basepage.load('../page/searchpage.yaml')
        # self.stop_video()
        return True
