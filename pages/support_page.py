from .base_page import BasePage
from .locators import SupportPageLocators
import time


class SupportPage(BasePage):
    def send_payment_data(self, email, card_number, card_expiry, card_cvc, card_name):
        email_field = self.browser.find_element(*SupportPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        time.sleep(1)
        card_number_field = self.browser.find_element(*SupportPageLocators.CARD_NUMBER_FIELD)
        time.sleep(1)
        card_number_field.send_keys(card_number)
        time.sleep(1)
        card_expiry_field = self.browser.find_element(*SupportPageLocators.CARD_EXPIRY_FIELD)
        time.sleep(1)
        card_expiry_field.send_keys(card_expiry)
        time.sleep(1)
        card_cvc_field = self.browser.find_element(*SupportPageLocators.CARD_CVC_FIELD)
        card_cvc_field.send_keys(card_cvc)
        time.sleep(1)
        card_name_field = self.browser.find_element(*SupportPageLocators.CARD_NAME_FIELD)
        card_name_field.send_keys(card_name)
        time.sleep(1)

    def choose_country(self, country):
        country_field = self.browser.find_element(*SupportPageLocators.COUNTRY_FIELD)
        country_field.click()
        if country == 'russia':
            country_russia = self.browser.find_element(*SupportPageLocators.COUNTRY_RUSSIA)
            country_russia.click()
        elif country == 'cyprus':
            country_russia = self.browser.find_element(*SupportPageLocators.COUNTRY_CYPRUS)
            country_russia.click()

    def check_wrong_card_info_message(self, expected_message):
        web_message = self.browser.find_element(*SupportPageLocators.WRONG_CARD_INFO_MESSAGE).text
        assert web_message == expected_message, f'Message is not as expected,' \
                                                f'\nactual - {web_message}' \
                                                f'\nexpected - {expected_message}'

    def press_pay(self):
        pay_button = self.browser.find_element(*SupportPageLocators.PAY_BUTTON)
        pay_button.click()
        time.sleep(1)

    def compare_text_of_link_button(self, how, what, expected_text):
        web_text = self.browser.find_element(how, what).text
        assert web_text == expected_text, f'Wrong text in link button' \
                                          f'\nactual - {web_text}' \
                                          f'\nexpected - {expected_text}'

    def go_to_link(self, how, what):
        link_button = self.browser.find_element(how, what)
        link_button.click()

    def go_back_to_main_page(self):
        back_button = self.browser.find_element(*SupportPageLocators.BACK_BUTTON)
        back_button.click()
        alert = self.browser.switch_to.alert
        alert.accept()

# При вводе почты изначально выходло окно верификации, затем перестало,
# на всякий случай, решил оставить данные, для этого окна -
# закомменчено в locators, support_page, test_support_page:

    # def email_verification_should_appear(self):
        # assert self.wait_element_is_presented(*SupportPageLocators.EMAIL_VERIFICATION),\
            # 'Can\'t find email verification window'

    # def close_email_verification(self):
        # email_verification = self.browser.find_element(
            # *SupportPageLocators.EMAIL_VERIFICATION_CANCEL_BUTTON)
        # email_verification.click()
