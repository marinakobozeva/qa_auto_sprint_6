
from pages.switch_to_yandex_page import SwitchToYandexPage
from constants.constants_url import Constants_Url

class TestSwitchToYandex:
    def test_switch_to_yandex(self, driver):
        page = SwitchToYandexPage(driver)
        page.switch_to_yandex_page()
        page.wait_for_page(Constants_Url.DZEN_URL)
        url = driver.current_url
        assert url == Constants_Url.DZEN_URL
