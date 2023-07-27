from pathlib import Path
from typing import List

from src.example.default import Article
from src.example.utils import load, save

TEST_DIR = Path(__file__).parent
TEST_DATA_DIR = TEST_DIR / "data"

DEFAULT_FILEPATH = TEST_DATA_DIR / "default.txt"


def test_serialization_of_v1():
    """
    Базовый тест сериализации и десериализации.

    Ожидаемый результат:
    Значения класса после десериализации будут идентичны значениям класса до.
    """

    a = Article()
    save(a, path=DEFAULT_FILEPATH)

    b: List[Article] = load(Article, path=DEFAULT_FILEPATH)  # type: ignore

    assert b.pop().title == a.title


def test_serialization_with_new_field():
    """
    В этом тесте симулируется ситуация,
    когда объект изначально имел МЕНЬШЕ полей (устаревшая версия кода),
    чем новый вид объекта (новая версия кода).

    Ожидаемый результат:
    Все поля, которые присутствовали в прошлом - будут заполнены корректно,
    а в новых полях будут установлены значения по-умолчанию.
    """
    buff = Article.views
    delattr(Article, "views")

    a = Article()
    save(a, path=DEFAULT_FILEPATH)

    setattr(Article, "views", buff)

    b: List[Article] = load(Article, path=DEFAULT_FILEPATH)  # type: ignore

    assert hasattr(b.pop(), "views")


def test_serialization_with_removed_field():
    """
    В этом тесте симулируется ситуация,
    когда объект изначально имел БОЛЬШЕ полей (устаревшая версия кода),
    чем новый вид объекта (новая версия кода).

    Ожидаемый результат:
    Поля, которые отсутствовали в прошлом, 
    не буду учитываться при текущем заполнении полей.
    """

    a = Article()
    save(a, path=DEFAULT_FILEPATH)

    buff = Article.views
    delattr(Article, "views")

    b: List[Article] = load(Article, path=DEFAULT_FILEPATH)  # type: ignore

    assert not hasattr(b.pop(), "views")

    setattr(Article, "views", buff)
