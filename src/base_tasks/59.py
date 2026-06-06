list_n = list(map(int, input("Введите числа через пробел: ").split()))
def find_max_element_index(list_n: list):
    index = 0
    for i in range(1, len(list_n)):
        if list_n[i] > list_n[index]:
            index = i

    print(f"Индекс максимального элемента: {index}")


find_max_element_index(list_n)