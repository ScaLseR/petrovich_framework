"""Модуль для работы с файлами"""
from importlib import import_module


def load_json_schema(path: str, json_schema: str):
    """Подгрузка json схемы из файла"""
    module = import_module(f"schema.{path}")
    return getattr(module, json_schema)
