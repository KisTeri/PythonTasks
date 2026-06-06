n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def divide_list(n: int, list_n: list):
    for i in range(1, n):
        left_sum = 0
        right_sum = 0
        for j in range(i):
            left_sum += list_n[j]
        for j in range(i, n):
            right_sum += list_n[j]

        if left_sum == right_sum:
            print("Да")
            break
    else:
        print("Нет")


divide_list(n, list_n)