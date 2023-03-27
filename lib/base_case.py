from .assertions import Assertions
from requests import Response


class BaseCase:
    @staticmethod
    def check_name_and_job_values(response: Response, expected_name, expected_job):
        # Compare sent 'name' with 'name' in response
        Assertions.assert_json_value_for_key(response, 'name', expected_name)
        # Compare sent 'job' with 'job' in response
        Assertions.assert_json_value_for_key(response, 'job', expected_job)
