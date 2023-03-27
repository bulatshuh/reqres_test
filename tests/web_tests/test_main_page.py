"""
Тетсы главной страницы - 16 шт:

15 тестов по отправке web запросов с проверкой с api запросами:
    7 тестов - на get запросы
    5 тестов - на post запросы
    1 тест - put запрос
    1 тест - patch запрос
    1 тест - delete запрос

1 тест по проверке наличия элементов на главной странице:
    Проверка main logo, кнопки swagger, поля для ввода суммы в support field
"""

from pages.locators import MainPageLocators
from lib.test_data import TestData
from pages.main_page import MainPage
import json
import requests
import pytest


@pytest.fixture()
def open_main_page(get_browser, get_base_url):
    page = MainPage(get_browser, get_base_url)
    page.open()
    page.go_to_full_screen()
    yield page


@pytest.mark.flaky(reruns=3)
class TestSendWebRequests:
    @pytest.mark.parametrize('test_dict', TestData.list_of_web_request_type_get,
                             ids=['list users', 'single user', 'single user not found',
                                  'list resource', 'single resource', 'single resource not found',
                                  'delayed response'])
    def test_send_request_get(self, get_base_url, open_main_page, test_dict):
        response = requests.get(f'{get_base_url}{test_dict["url_for_api"]}')
        # print(f'api code - {response.status_code}')

        page = open_main_page
        page.send_request(test_dict['request_name'])
        # Compare status codes form web and api
        page.wait_for_response_and_check_status_code(response)

        web_response_text = json.loads(page.get_response_text_from_field())
        api_response_text = json.loads(response.text)

        # print(f'web text - {web_response_text}')
        # print(f'api text - {api_response_text}')

        # Compare response from web with response from api
        assert web_response_text == api_response_text, \
            f'Responses from web and from api are not equal' \
            f'\nweb - {page.get_response_text()}' \
            f'\napi - {api_response_text}'

    @pytest.mark.parametrize('test_dict', TestData.list_of_web_request_type_post,
                             ids=['create', 'register successful', 'register unsuccessful',
                                  'login successful', 'login unsuccessful'])
    def test_send_request_post(self, get_base_url, open_main_page, test_dict):
        response = requests.post(f'{get_base_url}{test_dict["url_for_api"]}',
                                 data=test_dict['data'])
        # print(f'api code - {response.status_code}')

        page = open_main_page
        page.send_request(test_dict['request_name'])
        # Compare status codes form web and api
        page.wait_for_response_and_check_status_code(response)

        web_response_text = json.loads(page.get_response_text_from_field())
        api_response_text = json.loads(response.text)

        # print(f'web text - {web_response_text}')
        # print(f'api text - {api_response_text}')

        # In create responses "time" will be different, so will compare "name" and "job" values
        if test_dict['request_name'] == 'create':
            # Compare "name" and "job" values in responses
            assert web_response_text['name'] == api_response_text['name'], \
                f'Names from web and from api are not equal' \
                f'\nweb - {web_response_text["name"]}' \
                f'\napi - {api_response_text["name"]}'
            assert web_response_text['job'] == api_response_text['job'], \
                f'Jobs from web and from api are not equal' \
                f'\nweb - {web_response_text["job"]}' \
                f'\napi - {api_response_text["job"]}'
        # For other post requests hole responses can be compared
        else:
            # Compare response from web with response from api
            assert web_response_text == api_response_text, \
                f'Responses from web and from api are not equal'\
                f'\nweb - {page.get_response_text()}'\
                f'\napi - {api_response_text}'

    @pytest.mark.parametrize('test_dict', TestData.list_of_web_request_type_put,
                             ids=['update'])
    def test_send_request_put(self, get_base_url, open_main_page, test_dict):
        response = requests.put(f'{get_base_url}{test_dict["url_for_api"]}',
                                data=test_dict['data'])
        # print(f'api code - {response.status_code}')

        page = open_main_page
        page.send_request(test_dict['request_name'])
        # Compare status codes form web and api
        page.wait_for_response_and_check_status_code(response)

        web_response_text = json.loads(page.get_response_text_from_field())
        api_response_text = json.loads(response.text)

        # print(f'web text - {web_response_text}')
        # print(f'api text - {api_response_text}')

        # Compare "name" and "job" values in responses
        assert web_response_text['name'] == api_response_text['name'], \
            f'Names from web and from api are not equal'\
            f'\nweb - {web_response_text["name"]}'\
            f'\napi - {api_response_text["name"]}'
        assert web_response_text['job'] == api_response_text['job'], \
            f'Jobs from web and from api are not equal'\
            f'\nweb - {web_response_text["job"]}'\
            f'\napi - {api_response_text["job"]}'

    @pytest.mark.parametrize('test_dict', TestData.list_of_web_request_type_patch,
                             ids=['update'])
    def test_send_request_patch(self, get_base_url, open_main_page, test_dict):
        response = requests.patch(f'{get_base_url}{test_dict["url_for_api"]}',
                                  data=test_dict['data'])
        # print(f'api code - {response.status_code}')

        page = open_main_page
        page.send_request(test_dict['request_name'])
        # Compare status codes form web and api
        page.wait_for_response_and_check_status_code(response)

        web_response_text = json.loads(page.get_response_text_from_field())
        api_response_text = json.loads(response.text)

        # print(f'web text - {web_response_text}')
        # print(f'api text - {api_response_text}')

        # Compare "name" and "job" values in responses
        assert web_response_text['name'] == api_response_text['name'], \
            f'Names from web and from api are not equal'\
            f'\nweb - {web_response_text["name"]}'\
            f'\napi - {api_response_text["name"]}'
        assert web_response_text['job'] == api_response_text['job'], \
            f'Jobs from web and from api are not equal'\
            f'\nweb - {web_response_text["job"]}'\
            f'\napi - {api_response_text["job"]}'

    @pytest.mark.parametrize('test_dict', TestData.list_of_web_request_type_delete,
                             ids=['delete'])
    def test_send_request_delete(self, get_base_url, open_main_page, test_dict):
        response = requests.delete(f'{get_base_url}{test_dict["url_for_api"]}')
        # print(f'api code - {response.status_code}')

        page = open_main_page
        page.send_request(test_dict['request_name'])
        # Compare status codes form web and api
        page.wait_for_response_and_check_status_code(response)

        web_response_text = json.dumps(page.get_response_text_from_field())
        api_response_text = json.dumps(response.text)

        # print(f'web text - {web_response_text}')
        # print(f'api text - {api_response_text}')

        # Compare response from web with response from api
        assert web_response_text == api_response_text, \
            f'Responses from web and from api are not equal'\
            f'\nweb - {web_response_text}'\
            f'\napi - {api_response_text}'


@pytest.mark.flaky(reruns=3)
class TestMainPage:
    def test_main_page_main_elements(self, open_main_page):
        page = open_main_page
        # Check main page elements presence
        assert page.element_is_presented(*MainPageLocators.MAIN_LOGO_BUTTON),\
            'Can\'t find main logo button'
        assert page.element_is_presented(*MainPageLocators.SWAGGER_BUTTON),\
            'Can\'t find swagger button'
        assert page.element_is_presented(*MainPageLocators.G0_TO_SUPPORT_BUTTON),\
            'Can\'t find support button'
        page.scroll_to_support_field()
        assert page.element_is_presented(*MainPageLocators.MONEY_AMOUNT_FIELD),\
            'Can\'t find money amount field'
