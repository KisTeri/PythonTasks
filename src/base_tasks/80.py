n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))


def find_sequence(n: int, list_n: list):
    cnt = 0
    for i in range(n):
        len = 0
        summ = 0
        for j in range(i, n):
            len += 1
            summ += list_n[j]

            if len == 2 and summ % 2 == 0:
                cnt += 1
                break
    print(cnt)


find_sequence(n, list_n)

