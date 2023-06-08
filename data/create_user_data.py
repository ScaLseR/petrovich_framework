"""Дата файл для тестирования api reqres, create user"""
from model.create_model import RequestCreateUserModel

# данные для тестов ('request_parameters')
data = (RequestCreateUserModel(name='test', job='bobr'),
        RequestCreateUserModel(name='123', job=''),
        RequestCreateUserModel(name='Бобр Добр', job='#@^&T'))
