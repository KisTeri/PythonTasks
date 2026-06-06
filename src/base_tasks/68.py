n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_max_sum(n: int, list_n: list):
    max_sum = list_n[0]
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += list_n[j]
            if sum > max_sum:
                max_sum = sum

    print(max_sum)


find_max_sum(n, list_n)