"""
Приближённый к текущей реальности пример сериализации и десериализации
"""


from typing import Any, Dict, Generic, List, TypeVar, Union

from src.serialization import SerializationMixin
from src.utils import isattribute

T = TypeVar("T")


class UIElement(Generic[T]):
    def __init__(self, default: Union[T, None] = None):
        self.value = default


class UITextField(UIElement[str]):
    ...


class UINumberField(UIElement[int]):
    ...


class UISerializationMixin(SerializationMixin):
    _ui_fieldsnames: List[str]

    _filter_fields = ["_ui_fieldsnames"]

    def _unpack_value(self, value: Any) -> Any:
        if isinstance(value, UIElement):
            return value.value

        return super()._unpack_value(value)

    def __setattr__(self, __name: str, __value: Any):
        if __name in self._ui_fieldsnames:
            getattr(self, __name).value = __value
            return

        return super().__setattr__(__name, __value)


class UIPage(type):
    _ui_fieldsnames: List[str]

    def __new__(cls, name, bases, dct: Dict[str, Any]):
        instance_ = super().__new__(cls, name, bases, dct)

        instance_._ui_fieldsnames = []
        for k, v in dct.items():
            if isattribute(k, v) and isinstance(v, UIElement):
                instance_._ui_fieldsnames.append(k)

        return instance_


class SomePage(UISerializationMixin, metaclass=UIPage):
    ipaddr = UITextField("")

    port = UINumberField()
