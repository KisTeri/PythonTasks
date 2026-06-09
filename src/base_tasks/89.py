n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_sequence(n: int, list_n: list):
    second_elements = set()
    for i in range(n - 2):
        triple = [list_n[i], list_n[i + 1], list_n[i + 2]]
        triple.sort()
        second_elements.add(triple[1])
    print(len(second_elements))


find_sequence(n, list_n)