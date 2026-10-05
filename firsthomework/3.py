orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

sum_amount = sum(x["amount"] for x in orders if x["status"] == "returned")

print(sum_amount)  # - на какую сумму оформили возвраты

returned_buyer = set([x["buyer"] for x in orders if x["status"] == "returned"])

print(returned_buyer)  # - кто хотя бы раз вернул заказ

delivered_orders = len([x["buyer"] for x in orders if x["status"] == "delivered"])

print(delivered_orders)  # - сколько заказов доставлено покупателю

avg_delivered_orders_amount = sum([x["amount"] for x in orders if x["status"] == "delivered"])\
    / delivered_orders

print(avg_delivered_orders_amount)  # - средний чек доставленных заказов
