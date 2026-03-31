# Выпуклый четырехугольник задан координатами своих вершин. Найти площадь этого четырехугольника как сумму площадей треугольников.

a = tuple(map(float, input("Введите x1 y1: ").split()))
b = tuple(map(float, input("Введите x2 y2: ").split()))
c = tuple(map(float, input("Введите x3 y3: ").split()))
d = tuple(map(float, input("Введите x4 y4: ").split()))


def triangle_square(x1, y1, x2, y2, x3, y3):
    return abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) / 2


def quadrangle(a: float, b: float, c: float, d: float):
    triangle1 = triangle_square(*a, *b, *c)
    triangle2 = triangle_square(*a, *c, *d)
    return triangle1 + triangle2


print("Площадь четырехугольника: ", quadrangle(a, b, c, d))