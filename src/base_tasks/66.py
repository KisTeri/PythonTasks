n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_zero_sum(n: int, list_n: list):
    max_len = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += list_n[j]
            if sum == 0:
                length = j - i + 1
                if length > max_len:
                    max_len = length

    print(max_len)


find_zero_sum(n, list_n)