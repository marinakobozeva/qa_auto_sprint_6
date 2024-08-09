import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from constants.constants_answers import Constants_Answers
from constants.constants_url import Constants_Url
class TestMainPage:
    @pytest.mark.parametrize(
        "question_number,answer", [
            (0, Constants_Answers.ANSWER_0),
            (1, Constants_Answers.ANSWER_1),
            (2, Constants_Answers.ANSWER_2),
            (3, Constants_Answers.ANSWER_3),
            (4, Constants_Answers.ANSWER_4),
            (5, Constants_Answers.ANSWER_5),
            (6, Constants_Answers.ANSWER_6),
            (7, Constants_Answers.ANSWER_7),
        ]
    )
    def test_questions(self, driver, question_number, answer):
        main_page = MainPage(driver)
        main_page.go_to_url(Constants_Url.URL)
        main_page.close_cookies(MainPageLocators.COOKIES_BUTTON)
        main_page.scroll_page_to_the_bottom()
        result = main_page.click_on_question_and_get_answer(MainPageLocators.QUESTION_LOCATOR, MainPageLocators.ANSWER_LOCATOR, question_number)
        assert main_page.check_answer(result, answer)

