n = int(input("Введите количество элементов обоих списков: "))
list_a = list(map(int, input("Введите числа через пробел для первого списка: ").split()))
list_b = list(map(int, input("Введите числа через пробел для второго списка: ").split()))

def make_list_b(n:int, list_a: list, list_b: list):
    possible = False
    for change in range(n):
        ok = True
        for i in range(n):
            if list_a[(i + change) % n] != list_b[i]:
                ok = False
                break
        if ok:
            possible = True
            break
    if possible:
        print("Да")
    else:
        print("Нет")


make_list_b(n, list_a, list_b)