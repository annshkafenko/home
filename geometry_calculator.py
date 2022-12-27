Pi = 3.14

input_str = str(input(('Введіть сторони фігури: ')))
values = input_str.split(' ')
count = len(values)

if count == 3:
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
    if a == 0 or b == 0 or c == 0:
        print('Такого трикутника не існує')
    else:
        P = a+b+c
        p = (a+b+c)/2
        if p == a:
            s = round(((p * (p - b) * (p - c)) ** 0.5), 2)
            result = f'Трикутник: сторона а = {a}, сторона b = {b}, сторона c = {c}\nПериметр = {P}, Площа = {s}'
            print(result)
        elif p == b:
            s = round(((p * (p - a) * (p - c)) ** 0.5), 2)
            result = f'Трикутник: сторона а = {a}, сторона b = {b}, сторона c = {c}\nПериметр = {P}, Площа = {s}'
            print(result)
        elif p == c:
            s = round(((p * (p - a) * (p - b)) ** 0.5), 2)
            result = f'Трикутник: сторона а = {a}, сторона b = {b}, сторона c = {c}\nПериметр = {P}, Площа = {s}'
            print(result)
        else:
            s = round(((p * (p - a) * (p - b) * (p - c)) ** 0.5), 2)
            result = f'Трикутник: сторона а = {a}, сторона b = {b}, сторона c = {c}\nПериметр = {P}, Площа = {s}'
            print(result)
elif count == 2:
    a, b = values
    a = int(a)
    b = int(b)
    P = (a+b)*2
    s = a*b
    if a == 0 or b == 0:
        print('Такої фігури не існує')
    else:
        if a == b:
            result = f'Квадрат: сторона = {a}, Перемитер = {P}, Площа = {s}'
            print(result)
        else:
            result = f'Прямокутник: сторона a = {a}, сторона b = {b}, Перемитер = {P}, Площа = {s}'
            print(result)
elif count == 1:
    a = int(values[0])
    if a == 0:
        print('Такої фігури не існує')
    else:
        P = round((2 * Pi * a), 2)
        s = round((Pi * (a**2)), 2)
        result = f'Круг: радіус = {a}, Перемитер = {P}, Площа = {s}'
        print(result)
