n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Теперь введите числа через пробел: ").split()))
def find_min_element_index(n: int, list_n: list):
    index = -1
    for i in range(1, n - 1):
        if list_n[i] < list_n[i - 1] and list_n[i] < list_n[i + 1]:
            index = i

    if index == -1:
        print("no")
    else:
        print(f"Индекс локального минимума: {index}")


find_min_element_index(n, list_n)