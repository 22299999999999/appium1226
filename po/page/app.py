from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from po.page.basepage import BasePage
from po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = "true"
            # 执行程序时不会重新启动app
            caps["dontStopAppOnReset"] = "true"
            # 跳过一些安装和权限的设置
            caps["skipDeviceInitialization"] = "true"

            caps["ensureWebviewsHavePages"] = True
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def goto_main(self):
        """进入首页
        :return:
        """
        return MainPage(self.driver)
