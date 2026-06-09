from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    SURNAME = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    METRO = (By.XPATH, "//input[contains(@placeholder, 'етро')]")
    METRO_STATION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//*[contains(text(), 'Сокольники')]")
    PHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")

    NEXT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_NextButton')]/button")

    DATE = (By.XPATH, "//input[contains(@placeholder, 'Когда привезти самокат')]")
    RENT_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_ONE_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")

    BLACK_COLOR = (By.ID, "black")
    COMMENT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий')]")

    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Да']")
    SUCCESS_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Text')]")
    
    @staticmethod
    def metro_station(station_name):
        return (By.XPATH, f"//li//div[contains(text(), '{station_name}')]")