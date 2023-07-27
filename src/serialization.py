import abc
import inspect
from functools import lru_cache
from typing import Any, Dict, List

from typing_extensions import Protocol, Self

from .rtti import IRTTI, StrRTTI
from .utils import isattribute

DELIMITER: str = "\1"


class ISerializable(Protocol):
    @abc.abstractmethod
    def serialize(self) -> str:
        ...

    @classmethod
    @abc.abstractmethod
    def unserialize(cls, data: str) -> Self:
        ...


class SerializationMixin:
    _RTTI: IRTTI[str] = StrRTTI

    _filter_fields: List[str] = list()

    def serialize(self) -> str:
        return DELIMITER.join(
            [f"{k}={self._unpack_value(v)}" for k, v in self.fields().items()]
        )

    @classmethod
    def unserialize(cls, data: str) -> Self:
        unserialized_fields_ = cls.get_unserialized_fields(data)

        instance_ = cls()

        for fieldname, fieldvalue in unserialized_fields_.items():
            if hasattr(instance_, fieldname):
                annot = cls.__annotations__.get(fieldname, None)

                if annot is None:
                    annot = cls._RTTI.type(fieldvalue)

                fieldvalue = cls._RTTI.cast(annot, fieldvalue)

                setattr(instance_, fieldname, fieldvalue)

        return instance_

    @lru_cache(maxsize=None)
    def fields(self) -> Dict[str, Any]:
        """
        Получение входящих в объект полей,
        за исключением системных и отфильтрованных
        """

        fields_ = {}

        for fieldname, fieldvalue in inspect.getmembers(self):
            if isattribute(fieldname, fieldvalue) and fieldname not in [
                "_RTTI",
                "_filter_fields",
                *self._filter_fields,
            ]:
                fields_[fieldname] = fieldvalue

        return fields_

    @classmethod
    def get_unserialized_fields(cls, data: str) -> Dict[str, str]:
        return {
            n: "=".join(v)
            for n, *v in map(lambda s: s.split("="), data.split(DELIMITER))
        }

    def _unpack_value(self, value: Any) -> Any:
        """
        Метод для 'доставания' значения.

        Требует переопределения при работе с комплексными объектами.
        """

        return value
