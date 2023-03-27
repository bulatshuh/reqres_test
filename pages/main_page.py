from .base_page import *
from .locators import MainPageLocators
from requests import Response


class MainPage(BasePage):
    def send_request(self, request_name):
        if request_name == 'list users':
            button = self.browser.find_element(*MainPageLocators.LIST_USER_REQUEST_BUTTON)
            button.click()
        elif request_name == 'single user':
            button = self.browser.find_element(*MainPageLocators.SINGLE_USER_REQUEST_BUTTON)
            button.click()
        elif request_name == 'single user not found':
            button = self.browser.find_element(*MainPageLocators.SINGLE_USER_NOT_FOUND_REQUEST_BUTTON)
            button.click()
        elif request_name == 'list resource':
            button = self.browser.find_element(*MainPageLocators.LIST_RESOURCE_REQUEST_BUTTON)
            button.click()
        elif request_name == 'single resource':
            button = self.browser.find_element(*MainPageLocators.SINGLE_RESOURCE_REQUEST_BUTTON)
            button.click()
        elif request_name == 'single resource not found':
            button = self.browser.find_element(*MainPageLocators.SINGLE_RESOURCE_NOT_FOUND_REQUEST_BUTTON)
            button.click()
        elif request_name == 'create':
            button = self.browser.find_element(*MainPageLocators.CREATE_REQUEST_BUTTON)
            button.click()
        elif request_name == 'update put':
            button = self.browser.find_element(*MainPageLocators.UPDATE_PUT_REQUEST_BUTTON)
            button.click()
        elif request_name == 'update patch':
            button = self.browser.find_element(*MainPageLocators.UPDATE_PATCH_REQUEST_BUTTON)
            button.click()
        elif request_name == 'delete':
            button = self.browser.find_element(*MainPageLocators.DELETE_REQUEST_BUTTON)
            button.click()
        elif request_name == 'register_successful':
            button = self.browser.find_element(*MainPageLocators.REGISTER_SUCCESSFUL_REQUEST_BUTTON)
            button.click()
        elif request_name == 'register_unsuccessful':
            button = self.browser.find_element(*MainPageLocators.REGISTER_UNSUCCESSFUL_REQUEST_BUTTON)
            button.click()
        elif request_name == 'login_successful':
            button = self.browser.find_element(*MainPageLocators.LOGIN_SUCCESSFUL_REQUEST_BUTTON)
            button.click()
        elif request_name == 'login_unsuccessful':
            button = self.browser.find_element(*MainPageLocators.LOGIN_UNSUCCESSFUL_REQUEST_BUTTON)
            button.click()
        elif request_name == 'delayed_response':
            button = self.browser.find_element(*MainPageLocators.DELAYED_RESPONSE_REQUEST_BUTTON)
            button.click()
        else:
            print('Wrong request type asked')

    def get_response_status_code(self):
        status_code = self.browser.find_element(*MainPageLocators.RESPONSE_STATUS_CODE_FIELD).text
        # print(f'web code - {status_code}')
        return int(status_code)

    def get_response_text_from_field(self):
        data = self.browser.find_element(*MainPageLocators.RESPONSE_DATA_FIELD).text
        return data

    def wait_for_response_and_check_status_code(self, response: Response):
        # Check that loading spinner disappeared
        assert self.element_is_presented(*MainPageLocators.SPINNER_IS_HIDDEN), \
            'Loading spinner is still visible'
        # Check that response data field appear
        assert self.element_is_presented(*MainPageLocators.RESPONSE_DATA_FIELD), \
            'Can\'t find Response data field on page'
        # Compare status code from web with status code from api
        assert self.get_response_status_code() == response.status_code, 'Status codes are different'
