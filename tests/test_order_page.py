import pytest
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from constants import Constants

class TestOrderPage:
    @pytest.mark.parametrize("button_locator", [OrderPageLocators.HEADER_ORDER_BUTTON, OrderPageLocators.BODY_ORDER_BUTTON])
    def test_switch_to_the_order_page(self, driver, button_locator):
        order_page = OrderPage(driver)
        order_page.close_cookies(OrderPageLocators.COOKIES_BUTTON)
        order_page.click_on_element(button_locator)
        assert driver.current_url == Constants.ORDER_PAGE_URL

    def test_order_form_1(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.HEADER_ORDER_BUTTON)
        order_page.fill_order_form_1()
        flag = order_page.get_text_from_element(OrderPageLocators.ORDER_PAGE_TITLE)
        assert "Про аренду" in flag

    def test_order_form_2(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.HEADER_ORDER_BUTTON)
        order_page.fill_order_form_1()
        order_page.fill_order_form_2()
        flag = order_page.get_text_from_element(OrderPageLocators.POPUP_TITLE)
        assert 'Хотите оформить заказ?' in flag

    def test_popup_confirm(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.HEADER_ORDER_BUTTON)
        order_page.fill_order_form_1()
        order_page.fill_order_form_2()
        order_page.confirm_order_popup()
        flag = order_page.get_text_from_element(OrderPageLocators.POPUP_STATUS_TITLE)
        assert "Заказ оформлен" in flag
