"""
22 теста по просмотру информации юзеров:
    16 - позитивных
    6 - негативных
"""

import pytest
import requests
from lib.test_data import TestData
from lib.assertions import Assertions


class TestUserInfoPositive:

    @pytest.mark.parametrize('number', TestData.number_of_users)
    def test_list_user(self, number, get_base_url):
        response = requests.get(f'{get_base_url}api/users',
                                params={'page': number}
                                )

        assert response.status_code == 200, 'Wrong status code, expected - 200'
        # Compare sent number with number in response
        Assertions.assert_json_value_for_key(response, 'page', number)
        # Check that per_page number is 6
        Assertions.assert_json_value_for_key(response, 'per_page', 6)

    @pytest.mark.parametrize('user_id', TestData.list_of_correct_ids)
    def test_single_user(self, user_id, get_base_url):
        response = requests.get(f'{get_base_url}api/users/{user_id}')

        assert response.status_code == 200, 'Wrong status code, expected - 200'
        # Compare sent user_id with user_id in response
        Assertions.assert_json_deep_value_for_key(response, 'data', 'id', user_id)

    def test_unknown_list_user(self, get_base_url):
        response = requests.get(f'{get_base_url}api/unknown')

        assert response.status_code == 200, 'Wrong status code, expected - 200'
        # Check that response has keys: 'page', 'per_page', 'total', 'data'
        Assertions.assert_json_has_keys(response, ['page', 'per_page', 'total', 'data'])

    @pytest.mark.parametrize('user_id', TestData.list_of_correct_ids)
    def test_unknown_single_user(self, user_id, get_base_url):
        response = requests.get(f'{get_base_url}api/users/{user_id}')

        assert response.status_code == 200, 'Wrong status code, expected - 200'
        # Check that response has key 'data'
        Assertions.assert_json_has_key(response, 'data')
        # Compare sent user_id with user_id in response[data][id]
        Assertions.assert_json_deep_value_for_key(response, 'data', 'id', user_id)

    @pytest.mark.parametrize('number', TestData.number_of_delays)
    def test_list_users_delayed(self, get_base_url, number):
        response = requests.get(f'{get_base_url}api/users',
                                params={
                                    'delay': number
                                }
                                )
        assert response.status_code == 200, 'Wrong status code, expected - 200'
        # Check that response has keys: 'page', 'per_page', 'total', 'total_pages', 'data'
        Assertions.assert_json_has_keys(response, ['page', 'per_page', 'total', 'total_pages', 'data'])


class TestUserInfoNegative:

    @pytest.mark.parametrize('user_id', TestData.list_of_incorrect_ids)
    def test_single_user_not_found(self, get_base_url, user_id):
        response = requests.get(f'{get_base_url}api/users/{user_id}')

        assert response.status_code == 404, 'Wrong status code, expected - 404'
        # Check that response is empty
        Assertions.assert_empty_json(response)

    @pytest.mark.parametrize('user_id', TestData.list_of_incorrect_ids)
    def test_unknown_single_user_not_found(self, user_id, get_base_url):
        response = requests.get(f'{get_base_url}api/users/{user_id}')

        assert response.status_code == 404, 'Wrong status code, expected - 404'
        # Check that response is empty
        Assertions.assert_empty_json(response)
