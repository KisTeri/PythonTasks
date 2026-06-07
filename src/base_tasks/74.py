n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def rearrange_list_elements(n: int, list_n: list):
    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if list_n[i] == list_n[j]:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt

    if max_cnt <= (n + 1) // 2:
        print("Да")
    else:
        print("Нет")


rearrange_list_elements(n, list_n)