"""Тест кейс для api reqres, single user"""
import allure
import pytest
from helper.worker import load_tests

pytest_plugins = ["fixture.reqres.reqres_api_fixture"]
pytestmark = [allure.parent_suite("reqres"),
              allure.suite("single_user")]


@allure.title('Запрос с невалидным или отсутствующим параметром')
@pytest.mark.parametrize(('user_id', 'expected_data'),
                         load_tests('reqres.single_user_data', 'not_valid_data'))
def test_single_user_wo_parameters(reqres_api, expected_data, user_id):
    reqres_api.reqres_single_user(user_id).status_code_should_be(404).\
        have_value_in_response_parameter([], expected_data)


@allure.title('Запрос c валидными параметрами')
@pytest.mark.parametrize(('user_id', 'expected_data'),
                         load_tests('reqres.single_user_data', 'data'))
def test_single_user_valid_parameters(reqres_api, expected_data, user_id):
    reqres_api.reqres_single_user(user_id).status_code_should_be(200).\
        json_schema_should_be_valid('reqres.single_user_schema').\
        objects_should_be(expected_data, reqres_api.deserialize_register_payment())
