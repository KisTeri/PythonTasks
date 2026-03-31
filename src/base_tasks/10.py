# В подъезде № 1 пятиэтажного жилого дома 15 квартир. Определить, на каком этаже этого подъезда находится квартира с заданным номером
import math

flat_num = int(input("Введите номер квартиры: "))

def flat_location(flat_num: int):
    return math.ceil((flat_num / 15) * 5)

print(f"Квартира находится на {flat_location(flat_num)} этаже")