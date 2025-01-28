import math

# Данные
x = 16.55 * 10**-3  # x = 16.55 * 10^(-3)
y = -2.75
z = 0.15

# Вычисления
try:
    # Первая часть под корнем
    term1 = math.pow(x, 1/3) + x**(y + 2)
    sqrt_term = math.sqrt(10 * term1)  # Вычисляем корень

    # Вторая часть после корня
    term2 = math.asin(z)**2 - abs(x - y)

    # Итоговое значение
    s = sqrt_term * term2
    print(f"Результат: s = {s:.4f}")
except ValueError as e:
    print(f"Ошибка: {e}")
