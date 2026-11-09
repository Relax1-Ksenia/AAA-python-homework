# dataset_helpers.py - фильтрация и группировка списка словарей (как where и group by в SQL)
from typing import Any, Callable


def filter_records(records: list[dict], conditions: dict[str, Any]) -> list[dict]:
    """Оставляет только записи, подходящие под все условия (аналог where).

    Принимает: records - список плоских словарей;
    conditions - словарь {поле: значение} или {поле: функция_проверки}.
    Возвращает: новый список подходящих записей.
    """
    result = []
    for record in records:
        suits = True
        for field, condition in conditions.items():
            value = record.get(field)
            # если условие - функция, вызываю её, иначе сравниваю значения
            if callable(condition):
                if not condition(value):
                    suits = False
                    break
            elif value != condition:
                suits = False
                break
        if suits:
            result.append(record)
    return result


def group_by_attributes(records: list[dict], attributes: list[str]) -> dict[tuple, list[dict]]:
    """Группирует записи по значениям полей (аналог group by).

    Принимает: records - список словарей, attributes - список названий полей.
    Возвращает: словарь {кортеж_значений: список_записей_группы}.
    """
    groups = {}
    for record in records:
        # ключ группы - кортеж, потому что список не может быть ключом словаря
        key = tuple(record.get(attribute) for attribute in attributes)
        if key not in groups:
            groups[key] = []
        groups[key].append(record)
    return groups


def apply_aggregation(groups: dict[tuple, list[dict]],
                      aggregation: Callable[[list[dict]], Any]) -> dict[tuple, Any]:
    """Применяет агрегацию к каждой группе.

    Принимает: groups - результат group_by_attributes,
    aggregation - функция, которая берёт список записей и возвращает одно значение.
    Возвращает: словарь {ключ_группы: результат_агрегации}.
    """
    result = {}
    for key, group_records in groups.items():
        result[key] = aggregation(group_records)
    return result