n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))


def find_sequence(n: int, list_n: list):
    cnt = 0
    for i in range(n - 2):
        if list_n[i + 1] > list_n[i] and list_n[i + 1] > list_n[i + 2]:
            cnt += 1

    print(cnt)


find_sequence(n, list_n)