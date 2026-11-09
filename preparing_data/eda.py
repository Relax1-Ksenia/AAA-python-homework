# eda.py - функции для первичного анализа данных о лауреатах
from typing import Any


def count_missing(records: list[dict]) -> dict[str, int]:
    """Считает пропуски в каждом поле.

    Принимает: records - список словарей с данными о лауреатах.
    Возвращает: словарь {название_поля: число_пропусков}.
    """
    # сначала я собрала названия всех полей, которые вообще встречаются
    all_fields = set()
    for record in records:
        for field in record:
            all_fields.add(field)

    missing = {}
    for field in all_fields:
        missing[field] = 0

    for record in records:
        for field in all_fields:
            value = record.get(field)
            # пропуском я решила считать None, пустую строку и пустой список
            if value is None or value == '' or value == []:
                missing[field] += 1

    return missing


def get_missing_share(missing: dict[str, int], total: int) -> dict[str, float]:
    """Переводит число пропусков в долю от общего числа записей.

    Принимает: missing - словарь {поле: число_пропусков}, total - общее число записей (int).
    Возвращает: словарь {поле: доля_пропусков}, доля округлена до 3 знаков.
    """
    share = {}
    for field, count in missing.items():
        share[field] = round(count / total, 3)
    return share


def get_award_years(record: dict) -> list[int | None]:
    """Возвращает годы награждения одного лауреата.

    Принимает: record - словарь с данными одного лауреата.
    Возвращает: список годов (int); если года нет в призе, на его месте будет None.
    """
    years = []
    prizes = record.get('prizes_relevant')
    if prizes is None:
        return years
    for prize in prizes:
        years.append(prize.get('award_year'))
    return years


def get_all_ids(records: list[dict]) -> list[int]:
    """Собирает все id в список, записи без id я пропускаю.

    Принимает: records - список словарей с данными о лауреатах.
    Возвращает: список id (int) в том же порядке, что и записи.
    """
    ids = []
    for record in records:
        if record.get('id') is not None:
            ids.append(record['id'])
    return ids


def find_min_max_id(records: list[dict]) -> dict[str, Any]:
    """Находит записи с минимальным и максимальным id и их годы награждения.

    Принимает: records - список словарей с данными о лауреатах.
    Возвращает: словарь с ключами 'min_id' (int), 'min_id_years' (list),
    'max_id' (int), 'max_id_years' (list).
    """
    min_record = None
    max_record = None

    for record in records:
        current_id = record.get('id')
        if current_id is None:
            continue
        if min_record is None or current_id < min_record['id']:
            min_record = record
        if max_record is None or current_id > max_record['id']:
            max_record = record

    return {
        'min_id': min_record['id'],
        'min_id_years': get_award_years(min_record),
        'max_id': max_record['id'],
        'max_id_years': get_award_years(max_record),
    }


def find_duplicate_ids(records: list[dict]) -> list[int]:
    """Ищет повторяющиеся id.

    Принимает: records - список словарей с данными о лауреатах.
    Возвращает: отсортированный список id (int), которые встретились больше одного раза.
    """
    seen = set()
    duplicates = set()

    for current_id in get_all_ids(records):
        if current_id in seen:
            duplicates.add(current_id)
        else:
            seen.add(current_id)

    return sorted(duplicates)


def find_id_gaps(records: list[dict]) -> list[tuple[int, int]]:
    """Ищет соседние id (после сортировки), которые различаются больше чем на 1.

    Принимает: records - список словарей с данными о лауреатах.
    Возвращает: список пар (меньший_id, больший_id), между которыми есть разрыв.
    """
    sorted_ids = sorted(set(get_all_ids(records)))

    gaps = []
    for i in range(len(sorted_ids) - 1):
        left = sorted_ids[i]
        right = sorted_ids[i + 1]
        if right - left > 1:
            gaps.append((left, right))

    return gaps