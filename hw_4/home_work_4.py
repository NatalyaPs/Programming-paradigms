# Корреляция
# Контекст: Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
# Ваша задача: Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). Можете использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере она значительно упростит вам жизнь.
# r = (Σ[(x — x̄)(y — ȳ)]) / √[(Σ(x — x̄)²)(Σ(y — ȳ)²)]


import statistics

arr1 = [1,5,7,9,4,3,9]
arr2 = [2,8,6,2,3,4,5]

print(statistics.correlation(arr1, arr2))
print(statistics.correlation(arr1, arr1))
print(statistics.correlation(arr2, arr2))