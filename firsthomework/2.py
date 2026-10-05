from collections import Counter

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

print(f'всего поисковых запросов в ленте: len(queries)')  # - сколько всего поисковых запросов в ленте
print()
counts = Counter(queries)

counts_most_common = counts.most_common()

for query, count in counts_most_common:
    print(f'запрос {query} ввели: {count} раз')  # - сколько раз ввели каждый запрос

print()
print(f'запрос вводили чаще всего: {counts_most_common[0]}')  # - какой запрос вводили чаще всего
print()

print(f'долю всех поисков занимает iphone: \
{round(counts_most_common[0][1]/len(queries)*100, 2)}%')  # - какую долю всех поисков он занимает

print()
only_one = {query1: count1 for query1, count1 in counts_most_common if count1 == 1}\
    # - какие запросы встретились один раз
print(f'встретились один раз: {only_one}')
