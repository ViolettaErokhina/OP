def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Пример использования:
n = int(input("Введите натуральное число n: "))
print(f"Факториал числа {n} равен {factorial(n)}")
