"""Дата файл для тестирования api reqres, single user"""
from model.single_user_model import ResponseSingleUserModel


# эталонные модели данных для проверки в тестах
# user_id = 2
user_id_2 = ResponseSingleUserModel(id=2, email='janet.weaver@reqres.in', first_name='Janet',
                                    last_name='Weaver', avatar='https://reqres.in/img/faces/2-image.jpg',
                                    url='https://reqres.in/#support-heading',
                                    text='To keep ReqRes free, contributions towards server costs are appreciated!')

# user_id = 3
user_id_3 = ResponseSingleUserModel(id=3, email='emma.wong@reqres.in', first_name='Emma',
                                    last_name='Wong', avatar='https://reqres.in/img/faces/3-image.jpg',
                                    url='https://reqres.in/#support-heading',
                                    text='To keep ReqRes free, contributions towards server costs are appreciated!')

# Валидные данные для тестов ('user_id', 'expected_data')
data = ((2, user_id_2), (3, user_id_3))

# пустое тело ответа
empty_data = {}

# Не валидные данные для тестов ('user_id', 'expected_data')
not_valid_data = ((129398274923874, empty_data),
                  ('test', empty_data),
                  ('роывора', empty_data))
