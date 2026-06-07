n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))


def find_unique_sublist(n: int, list_n: list):
    max_len = 0
    for i in range(n):
        len = 0
        for j in range(i, n):
            repeat = False
            for k in range(i, j):
                if list_n[i] == list_n[j]:
                    repeat = True
                    break

            if repeat:
                break

            len += 1

        if len > max_len:
            max_len = len

    print(f"Максимальная длина: {max_len}")


find_unique_sublist(n, list_n)