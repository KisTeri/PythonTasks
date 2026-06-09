n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))


def find_ascending_sequence(n: int, list_n: list):
    possible = False
    for i in range(n - 2):
        if list_n[i + 1] < list_n[i] and list_n[i + 1] < list_n[i + 2]:
            possible = True

    if possible:
        print("Да")
    else:
        print("Нет")


find_ascending_sequence(n, list_n)