"""
Тесты Support страницы - 6 шт:

3 теста по проверке текста и работы 3 кнопок-ссылок в футере страницы

3 теста по проверке 3 сообщений о неверно введенных данных оплаты
"""

from pages.support_page import SupportPage
import pytest
from lib.test_data import TestData
from lib.base_case import BaseCase


@pytest.fixture()
def open_support_page(get_browser, get_base_url):
    page = SupportPage(get_browser, get_base_url)
    page.open()
    page.go_to_full_screen()
    page.scroll_to_support_field()
    page.open_support_page()
    yield page


@pytest.mark.flaky(reruns=3)
class TestSupportPageElements:
    @pytest.mark.parametrize('test_dict', TestData.list_for_footer_links,
                             ids=['Powered by', 'Terms', 'Privacy'])
    def test_support_page_footer_link(self, open_support_page, test_dict):
        page = open_support_page
        # Check link button presence
        assert page.element_is_presented(test_dict['how_link'], test_dict['what_link']),\
            f'"{test_dict["expected_text"]}" button is not presented on support page'
        # Check text in link buttons
        page.compare_text_of_link_button(test_dict['how_link'], test_dict['what_link'], test_dict['expected_text'])

        page.scroll_down(400)
        page.wait_element_is_presented(test_dict['how_link'], test_dict['what_link'])
        # open link
        page.go_to_link(test_dict['how_link'], test_dict['what_link'])
        # check page is opened
        page.wait_element_is_presented(test_dict['opened_how'], test_dict['opened_what'])
        page.switch_to_first_tab()


@pytest.mark.flaky(reruns=3)
class TestSupportPagePaymentNegative(BaseCase):
    @pytest.mark.parametrize('condition', TestData.list_of_conditions_for_wrong_card_data)
    def test_support_page_wrong_card_info(self, open_support_page, condition):
        page = open_support_page

# При вводе почты изначально выходло окно верификации, затем перестало,
# на всякий случай, решил оставить данные, для этого окна -
# закомменчено в locators, support_page, test_support_page:

        # page.send_email(test_dict['email'])
        # page.email_verification_should_appear()
        # page.close_email_verification()

        test_dict = self.prepare_invalid_card_data(condition)
        # Fill payment data
        page.send_payment_data(test_dict['email'], test_dict['card_number'], test_dict['card_expiry'],
                               test_dict['card_cvc'], test_dict['card_name'])
        page.choose_country(test_dict['country'])
        page.scroll_down(400)
        page.press_pay()
        page.scroll_down(-400)
        # Compare messages about wrong card info
        page.check_wrong_card_info_message(test_dict['expected_message'])
        page.go_back_to_main_page()
