n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))
def find_ubiquitous_element(n: int, list_n: list):
    max_cnt = 0
    ubiquitous_elements = list_n[0]
    for i in range(n):
        cnt = 0
        for j in range(n):
            if list_n[i] == list_n[j]:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt
            ubiquitous_elements = list_n[i]

    print(ubiquitous_elements)


find_ubiquitous_element(n, list_n)