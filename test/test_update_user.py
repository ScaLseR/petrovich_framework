"""Тест кейс для api reqres, update user"""
import allure
import pytest
from helper.worker import load_data

pytest_plugins = ["fixture.reqres_api"]
pytestmark = [allure.parent_suite("reqres"),
              allure.suite("update_user")]


@allure.title('Запрос на обновление данных пользователя')
@pytest.mark.parametrize(('user_id', 'request_parameters'),
                         load_data('update_user_data', 'data'))
def test_single_user_wo_parameters(reqres_api, user_id, request_parameters):
    reqres_api.reqres_update(user_id, request_parameters).status_code_should_be(200).\
        have_value_in_response_parameter(['name'], request_parameters.name).\
        have_value_in_response_parameter(['job'], request_parameters.job)
