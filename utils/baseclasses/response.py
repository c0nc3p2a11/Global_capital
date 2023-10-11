import allure
from pydantic.error_wrappers import ValidationError
from utils.enums.general_enums import GeneralErrors


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        with allure.step("Validating the schema"):
            try:
                if isinstance(self.response_json, list):
                    for item in self.response_json:
                        parsed_object = schema.parse_obj(item)
                        self.parsed_object = parsed_object
                else:
                    schema.parse_obj(self.response_json)
            except ValidationError:
                raise AssertionError("Could not map received object to pydantic schema")

    def assert_status_code(self, status_code):
        with allure.step("Checking status code"):
            if isinstance(status_code, list):
                assert self.response_status in status_code, GeneralErrors.WRONG_STATUS_CODE.value
            else:
                assert self.response_status == status_code, GeneralErrors.WRONG_STATUS_CODE.value

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        return (
            f"\nStatus code: {self.response_status} \n"
            f"Requested url: {self.response.url} \n"
            f"Response body: {self.response_json}"
        )
