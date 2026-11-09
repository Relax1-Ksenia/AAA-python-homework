# attribute_manager.py - добавление и удаление полей у списка словарей
from typing import Any, Callable


def add_attribute(records: list[dict], name: str,
                  func: Callable[[dict], Any]) -> list[dict]:
    """Добавляет новое поле в каждую запись (меняет записи на месте).

    Принимает: records - список словарей, name - название нового поля,
    func - функция, которая берёт одну запись и возвращает значение поля.
    Возвращает: тот же список records.
    """
    for record in records:
        record[name] = func(record)
    return records


def remove_attribute(records: list[dict], name: str) -> list[dict]:
    """Удаляет поле из каждой записи, если оно там есть.

    Принимает: records - список словарей, name - название поля.
    Возвращает: тот же список records.
    """
    for record in records:
        record.pop(name, None)
    return records