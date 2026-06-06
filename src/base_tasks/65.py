n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def make_new_list(n: int, list_n: list):
    for i in range(n):
        cnt = 0

        for j in range(n):
            if list_n[i] == list_n[j]:
                cnt += 1

        if cnt == 1:
            print(list_n[i], end=" ")

    for i in range(n):
        cnt = 0

        for j in range(n):
            if list_n[i] == list_n[j]:
                cnt += 1

        if cnt > 1:
            first = True

            for k in range(i):
                if list_n[k] == list_n[i]:
                    first = False
                    break

            if first:
                print(list_n[i], end=" ")


make_new_list(n, list_n)