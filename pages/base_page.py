from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def fill_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def fill_text_and_press_enter(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def get_text(self, locator):
        return self.wait_for_element(locator).text
