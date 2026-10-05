days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]


sum_revenue = sum(x["revenue"] for x in days)

print(sum_revenue)  # - выручку за всю неделю

ordered_days_by_revenue = sorted(days, key=lambda s: s["revenue"], reverse=True)

print(ordered_days_by_revenue[0])  # - день с самой большой выручкой

avg_revenue_by_orders = {x["day"]: x["revenue"]/x["orders"] for x in days}

print(avg_revenue_by_orders)  # - среднюю выручку на один заказ в каждый день

days_with_large_returns = [x["day"] for x in days if x["returns"] > 0.2*x["orders"]]

print(days_with_large_returns)  # - дни, где возвратов больше 20% заказов
