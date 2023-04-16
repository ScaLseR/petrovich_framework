"""Модуль для работы с api, отправка http запросов и получение ответов"""
# -*- coding: utf-8 -*-

import allure
import requests
from helper.logger import log


class Api:
    """Основной класс для работы с Api"""
    _HEADERS = {'Content-Type': 'application/json; charset=utf-8'}
    _TIMEOUT = 10
    base_url = {}

    def __init__(self):
        self.response = None

    @allure.step("Отправить POST запрос")
    def post(self, url: str, endpoint: str, params: dict = None,
             json_body: dict = None):
        with allure.step(f"POST запрос на url: {url}{endpoint}"
                         f"\n тело запроса: \n {json_body}"):
            self.response = requests.post(url=f"{url}{endpoint}",
                                          headers=self._HEADERS,
                                          params=params,
                                          json=json_body,
                                          timeout=self._TIMEOUT)
        log(response=self.response, request_body=json_body)
        return self

    @allure.step("Отправить PUT запрос")
    def put(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(f"PUT запрос на url: {url}{endpoint}"
                         f"\n тело запроса: \n {json_body}"):
            self.response = requests.put(url=f"{url}{endpoint}",
                                         headers=self._HEADERS,
                                         params=params,
                                         json=json_body,
                                         timeout=self._TIMEOUT)
        log(response=self.response, request_body=json_body)
        return self

    @allure.step("Отправить GET запрос")
    def get(self, url: str, endpoint: str):
        with allure.step(f"GET запрос на url: {url}{endpoint}"):
            self.response = requests.get(url=f"{url}{endpoint}",
                                         headers=self._HEADERS,
                                         timeout=self._TIMEOUT)
        log(response=self.response)
        return self

    @allure.step("Отправить DELETE запрос")
    def delete(self, url: str, endpoint: str):
        with allure.step(f"DELETE запрос на url: {url}{endpoint}"):
            self.response = requests.get(url=f"{url}{endpoint}",
                                         headers=self._HEADERS,
                                         timeout=self._TIMEOUT)
        log(response=self.response)
        return self
