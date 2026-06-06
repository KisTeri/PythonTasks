n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_max_sum_elements(n: int, list_n: list):
    max_sum = list_n[0]
    first_element = 0
    last_element = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += list_n[j]
            if sum > max_sum:
                max_sum = sum
                first_element = i
                last_element = j

    print(first_element, last_element)


find_max_sum_elements(n, list_n)