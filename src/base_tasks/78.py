n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_alternating_sequence(n: int, list_n: list):
    max_len = 1
    len = 1
    for i in range(1, n):
            if (list_n[i] > 0 and list_n[i - 1] < 0) or (list_n[i] < 0 and list_n[i - 1] > 0):
                len += 1
            else:
                len = 1

            if len > max_len:
                max_len = len

    print(f"Максимальная длина: {max_len}")


find_alternating_sequence(n, list_n)