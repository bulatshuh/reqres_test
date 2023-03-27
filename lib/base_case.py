from .assertions import Assertions
from requests import Response
from datetime import datetime


class BaseCase:
    @staticmethod
    def check_name_and_job_values(response: Response, expected_name, expected_job):
        # Compare sent 'name' with 'name' in response
        Assertions.assert_json_value_for_key(response, 'name', expected_name)
        # Compare sent 'job' with 'job' in response
        Assertions.assert_json_value_for_key(response, 'job', expected_job)

    def prepare_invalid_card_data(self, condition):
        if condition == 'invalid number':
            base_part = 'qwerty'
            random_part = datetime.now().strftime('%m%d%Y%H%M%S')
            domain = '@example.com'
            email = f'{base_part}{random_part}{domain}'

            return {
                'email': email,
                'card_number': '1234123412341234',
                'card_expiry': '0825',
                'card_cvc': '111',
                'card_name': 'QWERTY ASDFG',
                'country': 'russia',
                'expected_message': 'Your card number is invalid.'
            }

        if condition == 'past expiry':
            base_part = 'qwerty'
            random_part = datetime.now().strftime('%m%d%Y%H%M%S')
            domain = '@example.com'
            email = f'{base_part}{random_part}{domain}'

            return {
                'email': email,
                'card_number': '',
                'card_expiry': '0822',
                'card_cvc': '',
                'card_name': '',
                'country': 'cyprus',
                'expected_message': 'Your card\'s expiration year is in the past.'
            }

        if condition == 'incomplete number':
            base_part = 'qwerty'
            random_part = datetime.now().strftime('%m%d%Y%H%M%S')
            domain = '@example.com'
            email = f'{base_part}{random_part}{domain}'

            return {
                'email': email,
                'card_number': '123412341234',
                'card_expiry': '0825',
                'card_cvc': '111',
                'card_name': 'QWERTY ASDFG',
                'country': 'russia',
                'expected_message': 'Your card number is incomplete.'
            }
