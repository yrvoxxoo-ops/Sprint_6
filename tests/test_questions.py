import pytest

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestQuestions:

    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text",
        [
            (MainPageLocators.QUESTION_0, MainPageLocators.ANSWER_0, MainPageLocators.ANSWER_0_TEXT
            ),
            (
                MainPageLocators.QUESTION_1,
                MainPageLocators.ANSWER_1,
                MainPageLocators.ANSWER_1_TEXT
            ),
            (
                MainPageLocators.QUESTION_2,
                MainPageLocators.ANSWER_2,
                MainPageLocators.ANSWER_2_TEXT
            ),
            (
                MainPageLocators.QUESTION_3,
                MainPageLocators.ANSWER_3,
                MainPageLocators.ANSWER_3_TEXT
            ),
            (
                MainPageLocators.QUESTION_4,
                MainPageLocators.ANSWER_4,
                MainPageLocators.ANSWER_4_TEXT
            ),
            (
                MainPageLocators.QUESTION_5,
                MainPageLocators.ANSWER_5,
                MainPageLocators.ANSWER_5_TEXT
            ),
            (
                MainPageLocators.QUESTION_6,
                MainPageLocators.ANSWER_6,
                MainPageLocators.ANSWER_6_TEXT
            ),
            (
                MainPageLocators.QUESTION_7,
                MainPageLocators.ANSWER_7,
                MainPageLocators.ANSWER_7_TEXT
            ),
        ]
    )
    def test_question_opens_answer(self, driver, question_locator, answer_locator, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_cookie_button()
        main_page.click_question(question_locator)
        actual_text = main_page.get_answer_text(answer_locator)
        assert actual_text == expected_text