from pages.base_page import BasePage
from locators.switch_to_yandex_page_locators import SwitchToYandexPageLocators
import allure

class SwitchToYandexPage(BasePage):
    @allure.step("Проверка перехода на страницу Дзена")
    def switch_to_yandex_page(self):
        self.click_on_element(SwitchToYandexPageLocators.YANDEX_LOGO)
        self.switch_to(1, "about:blank")

