from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import MAIN_PAGE_URL


class MainPage(BasePage):

    def open(self):
        self.driver.get(MAIN_PAGE_URL)

    def click_cookie_button(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)

    def click_question(self, question_locator):
        self.click_on_element(question_locator)

    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    def click_order_button_top(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        element = self.wait_for_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

