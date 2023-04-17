"""Фикстуры reqres api"""
import pytest
from api.reqres.reqres_api import ReqresApi


@pytest.fixture(scope="function")
def reqres_api() -> ReqresApi:
    """Коннект к api reqres"""
    return ReqresApi()
