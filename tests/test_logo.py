from pages.main_page import MainPage
from urls import MAIN_PAGE_URL
import allure 

class TestLogo:

    @allure.title("Переход по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == MAIN_PAGE_URL
        
    @allure.title("Переход по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        main_page.wait_for_new_window()
        main_page.switch_to_last_window()
        main_page.wait_url_contains("dzen.ru")
        assert "dzen.ru" in main_page.get_current_url()