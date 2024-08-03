import allure
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Клик на вопрос и получение ответа для него")
    def click_on_question_and_get_answer(self, question_locator, answer_locator, question_number):
        method, locator = question_locator
        locator = locator.format(question_number)
        self.click_on_element((method, locator))
        method, locator = answer_locator
        locator = locator.format(question_number)
        return self.get_text_from_element((method, locator))

    @allure.step("Проверка соответствия результата")
    def check_answer(self, r, e):
        return r == e

