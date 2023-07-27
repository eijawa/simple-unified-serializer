from pathlib import Path
from typing import List, Union, Type

from src.serialization import ISerializable


def save(obj: ISerializable, path: Union[str, Path] = "src/data/output.txt"):
    with open(str(path), mode="a+", encoding="utf-8") as f:
        f.write(obj.serialize() + "\n")


def load(cls_: Type[ISerializable], path: Union[str, Path] = "src/data/output.txt") -> List[ISerializable]:
    res = []

    with open(str(path), mode="r", encoding="utf-8") as f:
        for l in f:
            res.append(cls_.unserialize(l.strip()))

    return res