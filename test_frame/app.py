# from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
#
# from test_frame.basepage import BasePage
# from test_frame.page.main import MainPage
#
#
# class App(BasePage):
#     def start(self):
#         if self.driver is None:
#             caps = {}
#             caps["platformName"] = "Android"
#             caps["deviceName"] = "127.0.0.1:7555"
#             caps["appPackage"] = "com.xueqiu.android"
#             caps["appActivity"] = ".view.WelcomeActivityAlias"
#             caps["noReset"] = "true"
#             self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#         else:
#             self.driver.launch_app()
#         self.driver.implicitly_wait(10)
#
#     def goto_main(self):
#         """进入首页
#         :return:
#         """
#         return MainPage(self.driver)
