from selenium.webdriver.common.by import By

class OrderPageLocators:
    INPUT_NAME = (By.XPATH, '//input[contains(@placeholder,"Имя")]')  # Поле ввода имени
    INPUT_SURNAME = (By.XPATH, '//input[contains(@placeholder,"Фамилия")]')  # Поле ввода фамилии
    INPUT_ADDRESS = (By.XPATH, '//input[contains(@placeholder,"Адрес")]')  # Поле ввода адреса
    INPUT_METRO_STATION = (By.XPATH, '//input[contains(@placeholder,"Станция метро")]')  # Поле ввода станции метро
    INPUT_TELEPHONE_NUMBER = (By.XPATH, '//input[contains(@placeholder,"Телефон")]')  # Поле ввода адреса
    STATION_SELECT_BUTTON = (By.XPATH, '//div[text()="Бульвар Рокоссовского"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    HEADER_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Header_Header")]//button[text()="Заказать"]')
    BODY_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_ThirdPart")]//button[text()="Заказать"]')
    COOKIES_BUTTON = (By.XPATH, '//button[text()="да все привыкли"]')
    ORDER_PAGE_TITLE = (By.XPATH, '//div[text()="Про аренду"]')
    INPUT_DELIVERY_DATE = (By.XPATH, '//input[contains(@placeholder,"Когда привезти")]')
    INPUT_RENT_PERIOD = (By.XPATH, '//div[text()="* Срок аренды"]')
    RENT_PERIOD_ELEMENT = (By.XPATH, '//div[text()="сутки"]')
    INPUT_COLOR = (By.XPATH, '//label[text()="чёрный жемчуг"]')
    FORM_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Content")]//button[text()="Заказать"]')
    POPUP_TITLE = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    POPUP_CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')
    POPUP_STATUS_TITLE = (By.XPATH, '//div[text()="Заказ оформлен"]')

