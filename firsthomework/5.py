import itertools

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

for x in reviews:
    x["product"] = x["product"].capitalize()  # приводим продукт к одному формату

reviews_sorted = sorted(reviews, key=lambda s: s["product"])

# Делала групп бай по продукту если бы у нас были бы одинаковые продукты,
# но с разными айдишниками то делала бы групп бай по айди
worst_avg_star = 10**10
worst_product = ''
print('средняя оценка каждого товара:')
for product, group in itertools.groupby(reviews_sorted, key=lambda s: s["product"]):
    stars = [s["stars"] for s in group]
    count_stars = len(stars)
    avg_star = sum(stars)/count_stars
    print(f"{product}: {avg_star} stars")  # - средняя оценка каждого товара

    if count_stars >= 2:
        if avg_star < worst_avg_star:
            worst_product = product
            worst_avg_star = avg_star
print()
print(f"худший товар {worst_product}: {worst_avg_star} средняя оценка") \
    # - худший товар по средней оценке среди тех, у кого хотя бы два отзыва
print()

reviews_1_or_2_star = len([x for x in reviews_sorted if x["stars"] < 3])

print(f'сколько отзывов на 1 или 2 звезды: {reviews_1_or_2_star}')  # - сколько отзывов на 1 или 2 звезды
print()

print(f'доля отзывов с оценкой 1 или 2 звезды: {reviews_1_or_2_star/len(reviews_sorted)*100} %')  \
    # - какую долю всех отзывов они составляют
