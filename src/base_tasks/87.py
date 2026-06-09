n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))


def find_ascending_sequence(n: int, list_n: list):
    possible = False
    for i in range(n):
        for j in range(i+1, n):
            list_n[i], list_n[j] = list_n[j], list_n[i]
            ascending = True
            for k in range(n - 1):
                if list_n[k] >= list_n[k + 1]:
                    ascending = False
                    break
            if ascending:
                possible = True

            list_n[i], list_n[j] = list_n[j], list_n[i]

            if possible:
                break

    if possible:
        print("Да")
    else:
        print("Нет")


find_ascending_sequence(n, list_n)