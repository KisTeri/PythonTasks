# С начала суток часовая стрелка повернулась на y градусов (0 ≤ y < 360, y– вещественное число). Определить число полных часов и число полных минут, прошедших с начала суток.
import math

degree = int(input("Введите градус поворота стрелки: "))


def hours_and_minutes(degree: int):
    if degree >= 0 and degree < 360:
        h = degree // 30
        m = math.ceil((degree % 30) // 0.5)
        return h, m
    else:
        print("Невозможно вычислить час и минуты!")


print(f"Прошло {hours_and_minutes(degree)[0]} час(а/ов) и {hours_and_minutes(degree)[1]} минут")