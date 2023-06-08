"""Дата файл для тестирования api reqres, update user"""
from model.update_model import RequestUpdateUserModel

# данные для тестов ('user_id', 'request_parameters')
data = ((100, RequestUpdateUserModel(name='test', job='bobr')),
        ('test', RequestUpdateUserModel(name='123', job='')),
        (1212121212, RequestUpdateUserModel(name='Бобр Добр', job='#@^&T')))
