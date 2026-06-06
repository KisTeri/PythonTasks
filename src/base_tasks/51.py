n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Теперь введите числа через пробел: ").split()))
def find_list_elements(n: int, list_n: list):
    cnt = 0
    for i in range(1, n - 1):
        if list_n[i] > list_n[i - 1] and list_n[i] > list_n[i + 1]:
            cnt += 1

    print(cnt)


find_list_elements(n, list_n)
