from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure 


class OrderPage(BasePage):

    allure.step("Выбор станции метро")
    def choose_metro(self, metro):
        self.click_on_element(OrderPageLocators.METRO)
        self.click_on_element(OrderPageLocators.metro_station(metro))

    @allure.step("Заполнение первой страницы заказа")
    def fill_first_page(self, name, surname, address, metro, phone):
        self.fill_text(OrderPageLocators.NAME, name)
        self.fill_text(OrderPageLocators.SURNAME, surname)
        self.fill_text(OrderPageLocators.ADDRESS, address)
        self.choose_metro(metro)
        self.fill_text(OrderPageLocators.PHONE, phone)

    @allure.step("Нажать кнопку Далее")
    def click_next(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение второй страницы заказа")
    def fill_second_page(self, date, comment):
        self.fill_text_and_press_enter(OrderPageLocators.DATE, date)
        self.click_on_element(OrderPageLocators.RENT_PERIOD)
        self.click_on_element(OrderPageLocators.RENT_ONE_DAY)
        self.click_on_element(OrderPageLocators.BLACK_COLOR)
        self.fill_text(OrderPageLocators.COMMENT, comment)

    @allure.step("Нажать кнопку Заказать")
    def click_order(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON)
        
    @allure.step("Проверить успешное оформление заказа")
    def check_success_order(self):
        return self.wait_for_element(OrderPageLocators.SUCCESS_ORDER).is_displayed()
