"""
Пример стандартной сериализации и десериализации базового объекта
"""


from typing import Union

from src.serialization import SerializationMixin


class Article(SerializationMixin):
    title: str = "Default Title of\tNew York Times"

    published: bool = False

    views = 1145

    _prv = "Some private field"

    def __init__(self, title: Union[str, None] = None):
        if title is not None:
            self.title = title
