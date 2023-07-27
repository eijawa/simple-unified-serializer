"""
RTTI - https://en.wikipedia.org/wiki/Run-time_type_information
"""

import abc
from typing import Any, Generic, Type, TypeVar

from typing_extensions import Protocol

T = TypeVar("T", contravariant=True)


class IRTTI(Generic[T], Protocol):
    @classmethod
    @abc.abstractmethod
    def cast(cls, annot: Type, value: T) -> Any:
        ...

    @classmethod
    @abc.abstractmethod
    def type(cls, value: T) -> Type:
        ...


class AbstractRTTI(Generic[T], abc.ABC):
    """
    Абстрактный класс динамической идентификации типа данных и преобразования в тип.
    """

    @classmethod
    def cast(cls, annot: Type, value: T) -> Any:
        """
        Метод преобразования значения в определённый тип данных
        """

        if value == "None":
            return None

        return annot(value)

    @classmethod
    @abc.abstractmethod
    def type(cls, value: T) -> Type:
        """
        Метод получения типа данных на основе значения
        """

        ...


class StrRTTI(AbstractRTTI[str]):
    """
    Класс динамической идентификации типа данных и преобразования в тип
    
    **На основе строкового значения**
    """

    @classmethod
    def cast(cls, annot: Type, value: str) -> Any:
        if annot is bool:
            return False if value.lower() == "false" else True

        return super().cast(annot, value)

    @classmethod
    def type(cls, value: str) -> Type:
        if value.isdigit():
            return int

        if value.isdecimal():
            return float

        if value.lower() in ("true", "false"):
            return bool

        return str
