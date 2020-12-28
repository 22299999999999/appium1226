from appium.webdriver.webdriver import WebDriver


class BasePage():
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

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
