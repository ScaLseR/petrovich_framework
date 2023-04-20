"""Тест кейс для api reqres, delete user"""
import allure
import pytest
from helper.load import load_data

pytest_plugins = ["fixture.reqres_api"]
pytestmark = [allure.parent_suite("reqres"),
              allure.suite("delete_user")]


@allure.title('Удаление пользователя')
@pytest.mark.parametrize('user_id', load_data('delete_user_data'))
def test_delete_user(reqres_api, user_id):
    reqres_api.reqres_delete(user_id).status_code_should_be(204)
