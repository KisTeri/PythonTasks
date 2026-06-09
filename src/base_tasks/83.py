n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))


def find_sequence_positive_sum(n: int, list_n: list):
    min_length = n + 1
    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += list_n[j]

            if summ > 0:
                length = j - i + 1
                if length < min_length:
                    min_length = length
                break
    if min_length == n + 1:
        print("no")
    else:
        print(min_length)


find_sequence_positive_sum(n, list_n)