[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# Унифицированный механизм сериализации и десериализации
> **Пакет typing_extensions**<br>Для удобства написания кода используются расширенные типы данные, такие как Protocol и Self.

## Запуск
Если вы знаете, как запускать код Python в виртуальном окружении и устанавливать зависимости - можете смело пропускать этот раздел.

<hr/>
Для всех остальных.

Создание виртуального окружения:
```bash
python3 -m venv venv
```

Запуск виртуального окружения:

*UNIX-система*
```bash
source venv/bin/activate
```

*Windows*
> Не забудьте активировать выполнение скриптов!
```bash
venv/Scripts/Activate
```

Установка зависимостей:
```bash
pip install -r requirements.txt
```

## Тесты
Для тестирования используется фреймворк `PyTest`. Во всех тестах использовался базовый пример (`src/example/default.py`).

Запуск тестов:
```bash
pytest
```

### Рассматриваемые сценарии

#### Сценарий 1 - Добавление поля
В этом тесте симулируется ситуация, когда объект изначально имел МЕНЬШЕ полей (устаревшая версия кода), чем новый вид объекта (новая версия кода).

Ожидаемый результат:

Все поля, которые присутствовали в прошлом - будут заполнены корректно, а в новых поля будут установлены значения по-умолчанию.

#### Сценарий 2 - Удаление поля
В этом тесте симулируется ситуация, когда объект изначально имел МЕНЬШЕ полей (устаревшая версия кода), чем новый вид объекта (новая версия кода).

Ожидаемый результат:

Все поля, которые присутствовали в прошлом - будут заполнены корректно, а в новых полях будут установлены значения по-умолчанию.

#### (Не рассмотрен!) Сценарий 3 - Переименование поля
> [См. статью на Life]()

## Подготовленные примеры
> Все примеры находятся по пути `src/example`.

- [x] Базовый пример
- [x] Усложнённый пример (С вложенным объектом)
- [x] 'Реальный' пример

## [Документация по модификации](./docs/Modification.md)
