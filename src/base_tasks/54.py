n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Теперь введите числа через пробел: ").split()))
def find_descending_sequence(n: int, list_n: list):
    max_len = 1
    current_len = 1
    for i in range(1, n):
        if list_n[i] < list_n[i - 1]:
            current_len += 1
        else:
            current_len = 1
        if current_len > max_len:
            max_len = current_len

    print(max_len)


find_descending_sequence(n, list_n)