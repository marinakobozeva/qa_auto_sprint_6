import pytest
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from constants.constants_url import Constants_Url

class TestOrderPage:
    @pytest.mark.parametrize("button_locator", [OrderPageLocators.HEADER_ORDER_BUTTON, OrderPageLocators.BODY_ORDER_BUTTON])
    def test_switch_to_the_order_page(self, driver, button_locator):
        order_page = OrderPage(driver)
        order_page.close_cookies(OrderPageLocators.COOKIES_BUTTON)
        order_page.click_on_element(button_locator)
        assert driver.current_url == Constants_Url.ORDER_PAGE_URL

    def test_order_form_1(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.HEADER_ORDER_BUTTON)
        order_page.fill_order_form_1()
        result = order_page.find_element_with_wait(OrderPageLocators.ORDER_PAGE_TITLE)
        assert result

    def test_order_form_2(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.HEADER_ORDER_BUTTON)
        order_page.fill_order_form_1()
        order_page.fill_order_form_2()
        result = order_page.find_element_with_wait(OrderPageLocators.POPUP_TITLE)
        assert result

    def test_popup_confirm(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.HEADER_ORDER_BUTTON)
        order_page.fill_order_form_1()
        order_page.fill_order_form_2()
        order_page.confirm_order_popup()
        result = order_page.find_element_with_wait(OrderPageLocators.POPUP_STATUS_TITLE)
        assert result
