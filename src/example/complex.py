"""
Пример сериализации и десериализации более объекта, 
содержащего в себе другой объект
"""


from typing import Any

from src.serialization import SerializationMixin


class Typography:
    def __init__(self, name: str):
        self.name = name


class Article(SerializationMixin):
    title: str = "Article====Title Default Value"

    typography: Typography = Typography("default")

    def _unpack_value(self, value: Any) -> Any:
        if isinstance(value, Typography):
            return value.name

        return super()._unpack_value(value)

    def __setattr__(self, __name: str, __value: Any):
        if __name == "typography":
            self.typography.name = __value
            return

        return super().__setattr__(__name, __value)
