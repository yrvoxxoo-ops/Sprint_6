from pages.main_page import MainPage
from urls import MAIN_PAGE_URL
from selenium.webdriver.support.ui import WebDriverWait

def test_scooter_logo_redirect(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_scooter_logo()

    assert driver.current_url == MAIN_PAGE_URL


def test_yandex_logo_redirect(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_yandex_logo()

    WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])

    WebDriverWait(driver, 15).until(lambda driver: "dzen.ru" in driver.current_url)

    assert "dzen.ru" in driver.current_url