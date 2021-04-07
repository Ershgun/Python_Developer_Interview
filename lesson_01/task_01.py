# Написать функцию (несколько функций), реализующую вывод таблицы умножения размерностью AｘB.
# Первый и второй множитель должны задаваться в виде аргументов функции.


a = int(input('Введите число A: '))
b = int(input('Введите число B: '))


def multiplication_table(a, b):
    c = 0
    while (c := c + 1) <= a:
        x = 0
        print()
        while (x := x + 1) <= b:
            result = c * x
            print(f'{c} * {x} = {result}')


# Вариант 2

# def multiplication_table(a, b):
# c = a + 1
# while (c := c - 1) > 0:
#     x = b + 1
#     print()
#     while (x := x - 1) > 0:
#         result = c * x
#         print(f'{c} * {x} = {result}')

# Вариант 3

# def multiplication_table(x, y):
#     for a in range(1, x + 1):
#         for b in range(1, y + 1):
#             print(f'{a} * {b} = {a * b}')


print(f'multiplication_table({a}, {b})')
multiplication_table(a, b)
