from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_frame.black_handle import black_wrapper


class BasePage():
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    # def find(self, by, locator):
    #     try:
    #         return self.driver.find_element(by, locator)
    #     except Exception as e:
    #         for black in self.black_list:
    #             elements = self.finds(*black)
    #             if len(elements) > 0:
    #                 elements[0].click()
    #                 return self.driver.find_element(by, locator)
    #     raise e

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def find_sendkeys(self, by, locator, neirong):
        self.find(by, locator).send_keys(neirong)

    def swip(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        while len(elements) == 0:
            self.driver.swipe(0, 600, 0, 200)
            elements = self.driver.find_elements(by, locator)
        return elements[0]

    def swip_click(self, by, locator):
        self.swip(by, locator).click()
