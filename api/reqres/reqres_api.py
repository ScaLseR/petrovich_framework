"""Модуль для работы с api https://reqres.in/
методы: post, get, put, delete
"""

# -*- coding: utf-8 -*-
import allure
from api.api import Api
from model.reqres.create_model import RequestCreateUserModel, ResponseCreateUserModel
from model.reqres.single_user_model import ResponseSingleUserModel
from model.reqres.update_model import RequestUpdateUserModel, ResponseUpdateUserModel


class ReqresApi(Api):

    """URl"""
    _URL = 'ws_site_paid_order'

    """Endpoint"""
    _ENDPOINT = '/api/users/'

    @allure.step('Обращение к single user')
    def reqres_single_user(self, user_id: int):
        return self.get(service_name=self._URL,
                        endpoint=self._ENDPOINT + str(user_id),
                        headers=self._HEADERS)

    @allure.step('Обращение к create')
    def reqres_create(self, param_request_body: RequestCreateUserModel):
        return self.post(service_name=self._URL,
                         endpoint=self._ENDPOINT,
                         headers=self._HEADERS,
                         json_body=param_request_body.to_dict())

    @allure.step('Обращение к update')
    def reqres_update(self, user_id: int, param_request_body: RequestUpdateUserModel):
        return self.put(service_name=self._URL,
                        endpoint=self._ENDPOINT + str(user_id),
                        headers=self._HEADERS,
                        json_body=param_request_body.to_dict())

    @allure.step('Обращение к delete')
    def reqres_delete(self, user_id: int):
        return self.delete(service_name=self._URL,
                           endpoint=self._ENDPOINT + str(user_id),
                           headers=self._HEADERS)
