from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_BUTTON_TOP = (By.XPATH,".//button[text()='Заказать']")

    ORDER_BUTTON_BOTTOM = (By.XPATH,".//div[contains(@class,'Home_FinishButton')]//button")

    SCOOTER_LOGO = (By.CLASS_NAME,"Header_LogoScooter__3lsAR")

    YANDEX_LOGO = (By.CLASS_NAME,"Header_LogoYandex__3TSOI")

    QUESTION_0 = (By.ID, "accordion__heading-0")
    ANSWER_0 = (By.ID, "accordion__panel-0")

    QUESTION_1 = (By.ID, "accordion__heading-1")
    ANSWER_1 = (By.ID, "accordion__panel-1")

    QUESTION_2 = (By.ID, "accordion__heading-2")
    ANSWER_2 = (By.ID, "accordion__panel-2")

    QUESTION_3 = (By.ID, "accordion__heading-3")
    ANSWER_3 = (By.ID, "accordion__panel-3")

    QUESTION_4 = (By.ID, "accordion__heading-4")
    ANSWER_4 = (By.ID, "accordion__panel-4")

    QUESTION_5 = (By.ID, "accordion__heading-5")
    ANSWER_5 = (By.ID, "accordion__panel-5")

    QUESTION_6 = (By.ID, "accordion__heading-6")
    ANSWER_6 = (By.ID, "accordion__panel-6")

    QUESTION_7 = (By.ID, "accordion__heading-7")
    ANSWER_7 = (By.ID, "accordion__panel-7")

    COOKIE_BUTTON = (By.XPATH,".//button[text()='да все привыкли']")

    ANSWER_0_TEXT = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    ANSWER_1_TEXT = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    ANSWER_2_TEXT = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    ANSWER_3_TEXT = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    ANSWER_4_TEXT = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    ANSWER_5_TEXT = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    ANSWER_6_TEXT = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    ANSWER_7_TEXT = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
