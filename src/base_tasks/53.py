n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Теперь введите числа через пробел: ").split()))
def print_list(n: int, list_n: list):
    for element in list_n:
        print(element)


print_list(n, list_n)