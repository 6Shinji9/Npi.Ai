from functools import reduce

# Пример списка чисел
numbers = [1, 2, 3, 4, 5, 6]

# Умножаем только четные числа на 2
filtered = filter(lambda x: x % 2 == 0, numbers)
mapped = map(lambda x: x * 2, filtered)

# Суммируем результат
total = reduce(lambda x, y: x + y, mapped)

print(total)
