import inspect


def isattribute(fieldname: str, fieldvalue: object) -> bool:
    """
    Метод проверки, что поле является аттрибутом
    """

    if fieldname.startswith("__") and fieldname.endswith("__"):
        return False

    return not any(
        (
            inspect.isfunction(fieldvalue),
            inspect.isbuiltin(fieldvalue),
            inspect.ismethod(fieldvalue),
            inspect.isroutine(fieldvalue),
            inspect.ismodule(fieldvalue),
        )
    )
