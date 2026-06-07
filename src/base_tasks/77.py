n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_even_sequence(n: int, list_n: list):
    max_len = 0
    for i in range(n):
        len = 0
        for j in range(i, n):
            even = False
            if list_n[j] % 2 == 0:
                even = True
                len += 1

            if not even:
                break

        if len > max_len:
            max_len = len

    print(f"Максимальная длина: {max_len}")


find_even_sequence(n, list_n)