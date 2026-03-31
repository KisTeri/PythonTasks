# Даны три вещественных числа. Вывести на экран те из них, которые принадлежат интервалу [1.6, 3.8]

a, b, c = map(float, input("Введите 3 числа: ").split())


def range(a: float, b: float, c: float):
    if a >= 1.6 and a <= 3.8:
        print(a)
    if b >= 1.6 and b <= 3.8:
        print(b)
    if c >= 1.6 and c <= 3.8:
        print(c)


range(a, b, c)