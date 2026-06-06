n = int(input("Введите число: "))

def find_ascending_sequence(n: int):
    ascending_sequence = True
    last_digit = n % 10
    n = n // 10

    while n > 0:
        digit = n % 10
        if digit < last_digit:
            ascending_sequence = True
        else:
            ascending_sequence = False
            break

        last_digit = digit
        n = n // 10
    print(ascending_sequence)


find_ascending_sequence(n)