# В подъезде № 1 пятиэтажного жилого дома 20 квартир. Определить: 1)на каком этаже этого подъезда находится квартира с заданным номером; 2) какой по счету является эта квартира, если квартира с минимальным номером является первой на этаже.

import math
from math import floor

flat_num = int(input("Введите номер квартиры: "))

def flat_location(flat_num: int):
    floor = math.ceil((flat_num / 20) * 5)
    number = (flat_num - 1) % 4 + 1
    return floor, number

print(f"Квартира находится на {flat_location(flat_num)[0]} этаже и является {flat_location(flat_num)[1]} по счету")