from random import randint
import allure
from pages.base_page import BasePage
from faker import Faker
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    fake = Faker(["ru_RU"])
    @allure.step("Заполнение данными в форме номер 1")
    def fill_order_form_1(self):
        self.set_text_to_element(OrderPageLocators.INPUT_NAME, self.fake.first_name())
        self.set_text_to_element(OrderPageLocators.INPUT_SURNAME, self.fake.last_name())
        self.set_text_to_element(OrderPageLocators.INPUT_ADDRESS, f"{self.fake.street_name()}, {self.fake.building_number().replace('/', '')}")
        self.click_on_element(OrderPageLocators.INPUT_METRO_STATION)
        self.click_on_element(OrderPageLocators.STATION_SELECT_BUTTON)
        self.set_text_to_element(OrderPageLocators.INPUT_TELEPHONE_NUMBER, f"+7{randint(10**9, 10**10 - 1)}")
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение данными в форме номер 2")
    def fill_order_form_2(self):
        self.set_text_to_element(OrderPageLocators.INPUT_DELIVERY_DATE, self.fake.date(pattern="%d.%m.%Y"))
        self.click_on_element(OrderPageLocators.ORDER_PAGE_TITLE)
        self.click_on_element(OrderPageLocators.INPUT_RENT_PERIOD)
        self.click_on_element(OrderPageLocators.RENT_PERIOD_ELEMENT)
        self.click_on_element(OrderPageLocators.INPUT_COLOR)
        self.click_on_element(OrderPageLocators.FORM_ORDER_BUTTON)

    @allure.step("Клик на подтверждение заказа самоката во всплывающем окне")
    def confirm_order_popup(self):
        self.click_on_element(OrderPageLocators.POPUP_CONFIRM_BUTTON)









