from requests import Response
import json.decoder


class Assertions:
    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response is "{response.text}"'

        assert name in response_dict, f'Can\'t find "{name}" in JSON response'

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response is "{response.text}"'

        for name in names:
            assert name in response_dict, f'Can\'t find "{name}" in JSON response'

    @staticmethod
    def assert_json_has_no_key(response: Response, name):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response is "{response.text}"'

        assert name not in response_dict, f'Find "{name}" in JSON response'

    @staticmethod
    def assert_json_value_for_key(response: Response, name, expected_value):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response is "{response.text}"'

        assert name in response_dict, f'Can\'t find {name} in JSON response'
        assert response_dict[name] == expected_value, f'"{name}" value is not equal ' \
                                                      f'\n actual - "{response_dict[name]}"' \
                                                      f'\nexpected - "{expected_value}"'

    @staticmethod
    def assert_json_deep_value_for_key(response: Response, name1, name2, expected_value):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response is "{response.text}"'

        assert name1 in response_dict, f'Can\'t find "{name1}" in JSON response'
        assert name2 in response_dict[name1], f'Can\'t find "{name2}" in JSON response'
        assert response_dict[name1][name2] == expected_value, f'"{name2}" value is not equal ' \
                                                              f'\n actual - {response_dict[name1][name2]}' \
                                                              f'\n expected - "{expected_value}"'

    @staticmethod
    def assert_empty_json(response: Response):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response is "{response.text}"'

        assert response_dict == {}, 'Response is not empty, but should be'

    @staticmethod
    def assert_no_response_body(response: Response):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert True, f'Response is in JSON format'

        assert response.text == '', 'Response is not empty, but should be'
