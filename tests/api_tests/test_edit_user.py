"""
13 тестов по изменению юзеров:
    1 тест - создание юзера
    8 тестов - изменеие юзера:
        4 через - put
        4 через - patch
    4 теста - удаление юзера
"""

import pytest
import requests
from lib.test_data import TestData
from lib.assertions import Assertions
from lib.base_case import BaseCase


class TestCreateUser:
    def test_create_user(self, get_base_url):
        response = requests.post(f'{get_base_url}api/users',
                                 data=TestData.create_user_data
                                 )

        assert response.status_code == 201, 'Wrong status code, expected - 201'
        # Compare sent and name and job values with values in response
        BaseCase.check_name_and_job_values(response, TestData.create_user_data['name'],
                                           TestData.create_user_data['job'])

        # Check that response has keys: 'id', 'createAt'
        Assertions.assert_json_has_keys(response, ['id', 'createdAt'])


class TestUpdateUser:
    @pytest.mark.parametrize('user_id', TestData.list_of_correct_ids)
    def test_update_user_put(self, get_base_url, user_id):
        response = requests.put(f'{get_base_url}api/users/{user_id}',
                                data=TestData.update_user_data
                                )

        assert response.status_code == 200, 'Wrong status code, expected - 200'
        # Compare sent and name and job values with values in response
        BaseCase.check_name_and_job_values(response, TestData.update_user_data['name'],
                                           TestData.update_user_data['job'])
        # Check that response has key 'createAt'
        Assertions.assert_json_has_key(response, 'updatedAt')
        # Check that response doesn't have key 'id'
        Assertions.assert_json_has_no_key(response, 'id')

    @pytest.mark.parametrize('user_id', TestData.list_of_correct_ids)
    def test_update_user_patch(self, get_base_url, user_id):
        response = requests.patch(f'{get_base_url}api/users/{user_id}',
                                  data=TestData.update_user_data
                                  )

        assert response.status_code == 200, 'Wrong status code, expected - 200'
        # Compare sent and name and job values with values in response
        BaseCase.check_name_and_job_values(response, TestData.update_user_data['name'],
                                           TestData.update_user_data['job'])
        # Check that response has key 'createAt'
        Assertions.assert_json_has_key(response, 'updatedAt')
        # Check that response doesn't have key 'id'
        Assertions.assert_json_has_no_key(response, 'id')


class TestDeleteUser:
    @pytest.mark.parametrize('number', TestData.list_of_correct_ids)
    def test_delete_single_user(self, get_base_url, number):
        response = requests.delete(f'{get_base_url}api/users/{number}')

        assert response.status_code == 204, 'Wrong status code, expected - 204'
        # Check that response doesn't have body
        Assertions.assert_no_response_body(response)
