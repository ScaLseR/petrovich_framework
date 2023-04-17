"""Тест кейс для api reqres, single user"""
import allure
import pytest
from helper.worker import load_tests

pytest_plugins = ["fixture.reqres.reqres_api_fixture"]
pytestmark = [allure.parent_suite("reqres"),
              allure.suite("single_user")]


@allure.title('Запрос с невалидным или отсутствующим параметром')
@pytest.mark.parametrize(('id', 'expected_data'),
                         load_tests('ws_terminal.register_payment_data', 'wo_parameters_test_data_err'))
def test_single_user_wo_parameters(reqres_api, expected_data, id):
    reqres_api.reqres_single_user(id).status_code_should_be(404)


@allure.title('Запрос c валидными параметрами')
@pytest.mark.parametrize(('id', 'expected_data'),
                         load_tests('ws_terminal.register_payment_data', 'wo_parameters_test_data'))
def test_single_user_valid_parameters(reqres_api, expected_data, id):
    reqres_api.reqres_single_user(id).status_code_should_be(200).\
        json_schema_should_be_valid('reqres.single_user_schema').\
        objects_should_be(expected_data, reqres_api.deserialize_register_payment())
