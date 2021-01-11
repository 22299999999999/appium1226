import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_frame.black_handle import black_wrapper


class BasePage():
    FIND = 'find'
    ACTION = 'action'
    CONTENT = 'content'
    FIND_CLICK = "find_click"
    FIND_SENDKEYS = "find_sendkeys"

    def __init__(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
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

    def load(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            cfg = yaml.load(f)
        for data in cfg:
            elements = data.get(self.FIND)
            ways = data.get(self.ACTION)
            content = data.get(self.CONTENT)
            if ways == self.FIND_CLICK:
                self.find_click(MobileBy.XPATH, elements)

            elif ways == self.FIND_SENDKEYS:
                self.find_sendkeys(MobileBy.XPATH, elements, content)

    def screenshot(self, photopath):
        self.driver.save_screenshot(photopath)

    def start_video(self):
        self.driver.start_recording_screen()

    def stop_video(self):
        self.driver.stop_recording_screen()
