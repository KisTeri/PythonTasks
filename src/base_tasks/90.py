n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))

def find_elements_distances(n: int, list_n: list):
    result = []
    for i in range(n):
        distance = 0
        for j in range(i + 1, n):
            if list_n[j] == list_n[i]:
                distance = j - i
                break
        result.append(distance)
    print(*result)


find_elements_distances(n, list_n)