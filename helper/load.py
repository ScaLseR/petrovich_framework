"""Модуль для работы с файлами"""
from importlib import import_module


def load_json_schema(path: str, json_schema: str = 'schema'):
    """Подгрузка json схемы из файла"""
    module = import_module(f"schema.{path}")
    return getattr(module, json_schema)


def load_data(path: str, test_data: str = 'data'):
    """Подгрузка из файла тестовых данных для параметризации тестов"""
    module = import_module(f"data.{path}")
    return getattr(module, test_data)
