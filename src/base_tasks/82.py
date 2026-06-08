n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def divide_list(n: int, list_n: list):
    possible = False
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            left_sum = 0
            middle_sum = 0
            right_sum = 0
            for k in range(i):
                left_sum += list_n[k]
            for k in range(i, j):
                middle_sum += list_n[k]
            for k in range(j, n):
                right_sum += list_n[k]

            if left_sum == middle_sum and right_sum == middle_sum:
                possible = True
                break
        if possible:
            break

    if possible:
        print("Да")
    else:
        print("Нет")


divide_list(n, list_n)