"""Модуль для работы с api https://reqres.in/
методы: post, get, put, delete
"""

# -*- coding: utf-8 -*-
import allure
from api.api import Api
from model.create_model import RequestCreateUserModel
from model.single_user_model import ResponseSingleUserModel
from model.update_model import RequestUpdateUserModel


class ReqresApi(Api):

    """URl"""
    _URL = 'https://reqres.in'

    """Endpoint"""
    _ENDPOINT = '/api/users/'

    @allure.step('Обращение к single user')
    def reqres_single_user(self, user_id: int):
        return self.get(url=self._URL,
                        endpoint=self._ENDPOINT + str(user_id))

    @allure.step('Обращение к create')
    def reqres_create(self, param_request_body: RequestCreateUserModel):
        return self.post(url=self._URL,
                         endpoint=self._ENDPOINT,
                         json_body=param_request_body.to_dict())

    @allure.step('Обращение к update')
    def reqres_update(self, user_id: int, param_request_body: RequestUpdateUserModel):
        return self.put(url=self._URL,
                        endpoint=self._ENDPOINT + str(user_id),
                        json_body=param_request_body.to_dict())

    @allure.step('Обращение к delete')
    def reqres_delete(self, user_id: int):
        return self.delete(url=self._URL,
                           endpoint=self._ENDPOINT + str(user_id))

    """Собираем респонс в обьект для последующего использования"""
    def deserialize_single_user(self):
        """для метода get (single user)"""
        payload = self.get_payload([])
        return ResponseSingleUserModel(id=payload['data']['id'],
                                       email=payload['data']['email'],
                                       first_name=payload['data']['first_name'],
                                       last_name=payload['data']['last_name'],
                                       avatar=payload['data']['avatar'],
                                       url=payload['support']['url'],
                                       text=payload['support']['text'])

