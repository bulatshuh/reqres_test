"""
8 тестов по регистрации юзеров:
    2 - позитивных
    6 - негативных:
        3 - без пароля
        3 - без почты
"""

import pytest
import requests
from lib.assertions import Assertions
from lib.test_data import TestData


class TestRegisterUserPositive:
    @pytest.mark.parametrize('data', TestData.list_login_user_correct_data,
                             ids=['pistol', 'cityslicka'])
    def test_positive_register_user(self, get_base_url, data):
        response = requests.post(f'{get_base_url}api/register',
                                 data=data
                                 )

        assert response.status_code == 200, 'Wrong status code, expected - 200'
        # Check keys id and token in response
        Assertions.assert_json_has_keys(response, ['id', 'token'])


class TestRegisterUserNegative:
    @pytest.mark.parametrize('data', TestData.list_login_user_without_password_data)
    def test_negative_register_user_without_password(self, get_base_url, data):
        response = requests.post(f'{get_base_url}api/register',
                                 data=data
                                 )

        assert response.status_code == 400, 'Wrong status code, expected - 400'
        # Check error key value in response
        Assertions.assert_json_value_for_key(response, 'error', 'Missing password')

    @pytest.mark.parametrize('data', TestData.list_login_user_without_email_data,
                             ids=['only password', 'name and job', 'empty'])
    def test_negative_register_user_without_email(self, get_base_url, data):
        response = requests.post(f'{get_base_url}api/register',
                                 data=data
                                 )

        assert response.status_code == 400, 'Wrong status code, expected - 400'
        # Check error key value in response
        Assertions.assert_json_value_for_key(response, 'error', 'Missing email or username')
