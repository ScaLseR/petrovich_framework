"""Модели для update user"""
from dataclasses import dataclass, asdict


@dataclass
class RequestUpdateUserModel:
    """Класс для параметров rquest"""
    name: str
    job: str

    def to_dict(self):
        """преобразование в dict для отправки body"""
        return asdict(self)


@dataclass
class ResponseUpdateUserModel:
    """Класс для параметров response"""
    name: str
    job: str
    updated_at: str
