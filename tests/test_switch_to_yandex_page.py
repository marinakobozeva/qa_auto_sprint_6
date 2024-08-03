
from pages.switch_to_yandex_page import SwitchToYandexPage


class TestSwitchToYandex:
    def test_switch_to_yandex(self, driver):
        page = SwitchToYandexPage(driver)
        page.switch_to_yandex_page()
        page.wait_for_page("https://dzen.ru/?yredirect=true")
        url = driver.current_url
        assert url == "https://dzen.ru/?yredirect=true"
