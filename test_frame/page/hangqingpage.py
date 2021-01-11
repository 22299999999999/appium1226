from appium.webdriver.common.mobileby import MobileBy

from test_frame.basepage import BasePage
from test_frame.page.searchpage import SearchPage


class HangQing(BasePage):
    def goto_search(self):
        # self.find_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.load('../page/hangqingpage.yaml')

        return SearchPage(self.driver)
