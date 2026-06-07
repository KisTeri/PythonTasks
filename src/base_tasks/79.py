n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_sum_sequence(n: int, list_n: list):
    summ = list_n[0]
    for i in range(1, n):
        if list_n[i] == summ:
            print("Да")
            return

        summ += list_n[i]
    print("Нет")


find_sum_sequence(n, list_n)