from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure 

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание элемента")
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step("Заполнение поля")
    def fill_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)
    
    @allure.step("Заполнение поля и нажатие Enter")
    def fill_text_and_press_enter(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    @allure.step("Получение текста")
    def get_text(self, locator):
        return self.wait_for_element(locator).text
    
    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Ожидание нового окна")
    def wait_for_new_window(self):
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
    
    @allure.step("Переключение на новое окно")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидание URL")
    def wait_url_contains(self, text):
        WebDriverWait(self.driver, 15).until(lambda driver: text in driver.current_url)