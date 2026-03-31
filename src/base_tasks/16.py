# Даны два прямоугольника, стороны которых параллельны или перпендикулярны осям координат. Известны координаты левого нижнего угла каждого из них и длины их сторон. Один из прямоугольников назовем первым, другой – вторым. Определить: а) принадлежат ли все точки первого прямоугольника второму; б)принадлежат ли все точки одного из прямоугольников другому; в) пересекаются ли эти прямоугольники.


x1, y1, a, b = map(float, input("Введите координаты левого нижнего угла x, y, длину и ширину первого прямоугольника: ").split())
x2, y2, c, d = map(float, input("Введите координаты левого нижнего угла x2, y2, длину и ширину второго прямоугольника: ").split())


def rectangle(x1: float, y1: float, x2: float, y2: float, a: float, b: float, c: float, d: float):
    left1 = x1
    right1 = x1 + a
    bottom1 = y1
    top1 = y1 + b

    left2 = x2
    right2 = x2 + c
    bottom2 = y2
    top2 = y2 + d

    if (left1 >= left2 and right1 <= right2 and bottom1 >= bottom2 and top1 <= top2):
        print("Все точки первого прямоугольника принадлежат второму")
    else:
        print("Условие не выполняется")

    if (left1 >= left2 and right1 <= right2 and bottom1 >= bottom2 and top1 <= top2) or (left2 >= left1 and right2 <= right1 and bottom2 >= bottom1 and top2 <= top1) :
        print("Все точки одного из прямоугольников принадлежат другому")
    else:
        print("Условие не выполняется")

    if not (right1 <= left2 or right2 <= left1 or top1 <= bottom2 or top2 <= bottom1):
        print("Прямоугольники пересекаются")
    else:
        print("Условие не выполняется")


rectangle(x1, y1, x2, y2, a, b, c, d)


