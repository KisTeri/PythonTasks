n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Теперь введите числа через пробел: ").split()))
def find_even_numbers(n: int, list_n: list):
    cnt = 0
    for i in range(1, n):
        if list_n[i] % 2 == 0:
            cnt += 1

    print(cnt)


find_even_numbers(n, list_n)