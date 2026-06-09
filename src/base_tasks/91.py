n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_max_first_element(n: int, list_n: list):
    max_cnt = 0
    element = list_n[0]
    for i in range(n):
        cnt = 0
        for j in range(n):
            if list_n[j] == list_n[i]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            element = list_n[i]
    print(element, max_cnt)


find_max_first_element(n, list_n)