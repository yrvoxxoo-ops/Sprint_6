from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import MAIN_PAGE_URL
import allure 

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(MAIN_PAGE_URL)

    @allure.step("Нажать кнопку принятия cookies")
    def click_cookie_button(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Открыть вопрос FAQ")
    def click_question(self, question_locator):
        self.click_on_element(question_locator)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)
    
    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_order_button_top(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

