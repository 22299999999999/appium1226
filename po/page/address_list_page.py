from appium.webdriver.common.mobileby import MobileBy

from po.page.basepage import BasePage
from po.page.member_invite_menu_page import InviteMenu


class ConTact(BasePage):
    def goto_invite_page(self):
        """点击添加成员进入手动添加成员页
        :return:
        """
        # # 滚动查找元素
        # self.find_click(MobileBy.
        #                          ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                               'scrollable(true).instance(0)).'
        #                                               'scrollIntoView(new UiSelector().'
        #                                               'text("添加成员").instance(0));')
        self.swip_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return InviteMenu(self.driver)
