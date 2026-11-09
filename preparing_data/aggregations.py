# aggregations.py - функции расчёта метрик по списку словарей
import statistics
from typing import Any, Callable


def get_values(records: list[dict], field: str) -> list[Any]:
    """Достаёт значения поля из записей, пропуски (None) я выбрасываю.

    Принимает: records - список словарей, field - название поля.
    Возвращает: список значений без None.
    """
    values = []
    for record in records:
        value = record.get(field)
        if value is not None:
            values.append(value)
    return values


def count_records(records: list[dict]) -> int:
    """Возвращает количество записей."""
    return len(records)


def mean_value(records: list[dict], field: str) -> float | None:
    """Среднее значение поля; если значений нет, возвращает None."""
    values = get_values(records, field)
    if not values:
        return None
    return statistics.mean(values)


def median_value(records: list[dict], field: str) -> float | None:
    """Медиана поля; если значений нет, возвращает None."""
    values = get_values(records, field)
    if not values:
        return None
    return statistics.median(values)


def max_value(records: list[dict], field: str) -> Any | None:
    """Максимум поля; если значений нет, возвращает None."""
    values = get_values(records, field)
    if not values:
        return None
    return max(values)


def min_value(records: list[dict], field: str) -> Any | None:
    """Минимум поля; если значений нет, возвращает None."""
    values = get_values(records, field)
    if not values:
        return None
    return min(values)


def make_aggregation(func: Callable[[list[dict], str], Any],
                     field: str) -> Callable[[list[dict]], Any]:
    """Фиксирует поле в функции метрики, чтобы передать её в apply_aggregation.

    Принимает: func - например mean_value, field - поле для расчёта.
    Возвращает: функцию, которая принимает только список записей.
    """
    def aggregation(records: list[dict]) -> Any:
        return func(records, field)
    return aggregation


def top_n(metric_by_group: dict, n: int = 5, reverse: bool = True) -> list[tuple]:
    """Выводит топ-N групп по значению метрики.

    Принимает: metric_by_group - словарь {ключ_группы: число}, n - сколько взять,
    reverse - True для самых больших значений, False для самых маленьких.
    Возвращает: список пар (ключ_группы, значение), отсортированный по значению.
    """
    items = [(key, value) for key, value in metric_by_group.items() if value is not None]
    items.sort(key=lambda pair: pair[1], reverse=reverse)
    return items[:n]