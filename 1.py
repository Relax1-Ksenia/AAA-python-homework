"""Анализ сотрудников: иерархия команд, сводка по департаментам, экспорт в CSV."""

import csv
import itertools
from collections import defaultdict


def read_file_csv(path: str) -> list[list[str]]:
    """Читает CSV с разделителем ';' и пропускает заголовок."""
    with open(path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        return list(reader)


def choose(input_number: int, corp_summary: list) -> dict:
    """Запускает нужную операцию по номеру 1–3."""
    if input_number == 1:
        return first_func(corp_summary)
    elif input_number == 2:
        return second_func(corp_summary)
    elif input_number == 3:
        return third_func(corp_summary)


def first_func(corp_summary_list: list) -> dict:
    """Собирает иерархию: департамент → отделы."""
    department_otdel = [row[1:3] for row in sorted(corp_summary_list, key=lambda e: (e[1], e[2]))]
    result = defaultdict(list)
    for (department, otdel), _ in itertools.groupby(department_otdel, key=lambda s: (s[0], s[1])):
        result[department].append(otdel)
    return dict(result)


def second_func(corp_summary_list: list) -> dict:
    """Считает по департаментам численность и зарплаты: макс, мин, средняя."""
    ordered = sorted(corp_summary_list, key=lambda e: e[1])
    result = defaultdict(list)
    for department, group in itertools.groupby(ordered, key=lambda e: e[1]):
        rows = list(group)
        salaries = [int(r[5]) for r in rows]
        result[department] = [
            len(rows),
            int(max(rows, key=lambda s: int(s[5]))[5]),
            int(min(rows, key=lambda s: int(s[5]))[5]),
            round(sum(salaries) / len(rows), 2),
        ]
    return dict(result)


def third_func(corp_summary_list: list) -> dict:
    """Пишет сводку в output.csv и возвращает её."""
    summary = second_func(corp_summary_list)
    with open('output.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Департамент', 'Кол-во сотрудников', 'Макс. зарплата', 'Мин. зарплата', 'Средняя зарплата'])
        for department, stats in summary.items():
            writer.writerow([department] + stats)
    print("Данные успешно сохранены в файл 'output.csv'")
    return summary


if __name__ == "__main__":
    # Точка входа: простое меню
    corp_summary = read_file_csv('Corp_Summary.csv')
    flag = True
    while flag:
        print(
            "Введите число от 1 до 3, номер функции которую хотите вызвать\n"
            "  1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него\n"
            "  2. Вывести сводный отчёт по департаментам: название, численность, "
            "\"вилка\" зарплат в виде мин – макс, среднюю зп\n"
            "  3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла."
        )
        input_number = input()
        if input_number.isdigit() and (1 <= int(input_number) <= 3):
            flag = False
            print(choose(int(input_number), corp_summary))
        else:
            print('не балуйтесь!')