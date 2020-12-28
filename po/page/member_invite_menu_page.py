from appium.webdriver.common.mobileby import MobileBy

from po.page.basepage import BasePage
from po.page.contact_add import AddMember


class InviteMenu(BasePage):
    def goto_add_member(self):
        """点击手动添加成员，进入添加成员页
        :return:
        """
        self.find_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return AddMember(self.driver)
