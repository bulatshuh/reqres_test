from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from .locators import MainPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_full_screen(self):
        self.browser.maximize_window()

    def element_is_presented(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def wait_element_is_presented(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def scroll_down(self, height):
        self.browser.execute_script(f"window.scrollTo(0, {height})")

    def scroll_to_support_field(self):
        support_button = self.browser.find_element(*MainPageLocators.G0_TO_SUPPORT_BUTTON)
        support_button.click()

    def open_support_page(self):
        support_button = self.browser.find_element(*MainPageLocators.SUPPORT_BUTTON)
        support_button.click()

    def switch_to_first_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[0])
