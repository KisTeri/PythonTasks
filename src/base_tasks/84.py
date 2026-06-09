n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_sequence(n: int, list_n: list):
    maxim = list_n[0]
    for i in range(1, n):
        if list_n[i] > maxim:
            maxim = list_n[i]
    first_el = 0
    for i in range(n):
        if list_n[i] == maxim:
            first_el = i
            break

    last_el = 0
    for i in range(n):
        if list_n[i] == maxim:
            last_el = i

    cnt = 0
    for i in range(first_el + 1, last_el):
        unique = True
        for j in range(first_el + 1, i):
            if list_n[i] == list_n[j]:
                unique = False
                break

        if unique:
            cnt += 1
    print(cnt)


find_sequence(n, list_n)