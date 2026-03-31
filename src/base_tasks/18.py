# Даны вещественные положительные числа a, b, c. Выяснить, существует ли треугольник со сторонами a, b, c

a, b, c = map(float, input("Введите стороны треугольника(3 значения): ").split())


def triangle(a: float, b: float, c: float):
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
    else:
        print("Треугольник не существует")


triangle(a, b, c)