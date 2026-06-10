import pytest
import allure 
from pages.main_page import MainPage
from pages.order_page import OrderPage


test_data = [
    ("Анна", "Иванова", "Ленина 1", "Комсомольская", "89991234567", "10.06.2026", "Позвоните заранее"),
    ("Иван", "Петров", "Мира 10", "Сокольники", "89998887766", "15.06.2026", "Не звонить"),
]


class TestOrder:

    @allure.title("Оформление заказа через верхнюю кнопку")
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, comment", test_data)
    def test_order_with_top_button(self, driver, name, surname, address, metro, phone, date, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_button_top()

        order_page.fill_first_page(name, surname, address, metro, phone)
        order_page.click_next()
        order_page.fill_second_page(date, comment)
        order_page.click_order()
        order_page.confirm_order()

        assert order_page.check_success_order()
        
    @allure.title("Оформление заказа через нижнюю кнопку")
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, comment", test_data)
    def test_order_with_bottom_button(self, driver, name, surname, address, metro, phone, date, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_cookie_button()
        main_page.click_order_button_bottom()

        order_page.fill_first_page(name, surname, address, metro, phone)
        order_page.click_next()
        order_page.fill_second_page(date, comment)
        order_page.click_order()
        order_page.confirm_order()

        assert order_page.check_success_order()