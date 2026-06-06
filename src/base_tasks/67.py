n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_zero_sum(n: int, list_n: list):
    exist = False
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += list_n[j]
            if sum == 0 and (j - i + 1) >= 2:
                exist = True
                break
        if exist:
            break

    if exist:
        print("Да")
    else:
        print("Нет")


find_zero_sum(n, list_n)