n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))


def find_inversions(n: int, list_n: list):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if list_n[i] > list_n[j]:
                cnt += 1

    print(cnt)


find_inversions(n, list_n)