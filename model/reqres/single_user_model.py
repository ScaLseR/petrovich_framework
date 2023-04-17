"""Модель respons-а для single user"""
from dataclasses import dataclass


@dataclass
class ResponseSingleUserModel:
    """Класс для параметров response"""
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
    url: str
    text: str
