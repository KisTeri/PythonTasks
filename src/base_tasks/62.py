n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))
def find_unique_elements(n: int, list_n: list):
    unique_elements = []
    for i in range(1, n - 1):
        if list_n[i] != list_n[i + 1]:
            unique_elements.append(list_n[i])


    if len(unique_elements) == 0:
        print("no")
    else:
        print(f"Элементы, которые встречаются в списке ровно один раз: {unique_elements}")


find_unique_elements(n, list_n)