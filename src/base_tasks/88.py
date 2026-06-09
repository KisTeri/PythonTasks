n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Введите числа через пробел: ").split()))


def find_sequence(n: int, list_n: list):
    min_length = n
    for left in range(n):
        for right in range(left, n):
            ok = True
            previous = None
            for i in range(n):
                if left <= i <= right:
                    continue
                if previous is not None and previous > list_n[i]:
                    ok = False
                    break

                previous = list_n[i]

            if ok:
                length = right - left + 1
                if length < min_length:
                    min_length = length

    print(min_length)


find_sequence(n, list_n)