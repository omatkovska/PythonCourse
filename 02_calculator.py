print('''
Виберіть потрібну операцію
1. Сума
2. Різниця
3. Добуток
4. Ділення
5. Піднесення в степінь
6. Синус
7. Косинус
8. Тангенс
''')
operation_number = int(input("Введіть номер операції: "))

import math

if 0 < operation_number <= 5:
    a, b = input("Введіть два числа для виконання операції").split(" ")
    a = int(a)
    b = int(b)
    if operation_number == 1:
        result = a + b
    elif operation_number == 2:
        result = a - b
    elif operation_number == 3:
        result = a * b
    elif operation_number == 4:
        result = a / b
    elif operation_number == 5:
        result = a ** b
elif 5 < operation_number < 9:
    c = int(input("Введіть число для виконання операції"))
    if operation_number == 6:
        result = math.sin(c)
    elif operation_number == 7:
        result = math.cos(c)
    elif operation_number == 8:
        result = math.tan(c)

print(result)
