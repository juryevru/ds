# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
a = float(input('Введите первое число координаты 1'))
b = float(input('Введите второе число координаты 1'))
c = float(input('Введите первое число координаты 2'))
d = float(input('Введите второе число координаты 2'))
k = (b - d) / (a - c)
e = d - k * c
print(f'y = {k}x + {e}')
