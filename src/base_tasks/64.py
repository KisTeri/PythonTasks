list_n = list(map(int, input("Введите числа через пробел: ").split()))
def make_unique_list(list_n: list):
    new_list = []
    for i in list_n:
        if i not in new_list:
            new_list.append(i)

    print(*new_list)


make_unique_list(list_n)