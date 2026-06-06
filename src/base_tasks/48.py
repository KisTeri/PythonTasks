n = int(input("Введите число: "))

def find_max_length(n: int):
    last_digit = n % 10
    current_length = 1
    max_length = 1
    n = n // 10

    while n > 0:
        digit = n % 10
        if digit == last_digit:
            current_length += 1
        else:
            current_length = 1

        if current_length > max_length:
            max_length = current_length

        last_digit = digit
        n = n // 10
    print(max_length)


find_max_length(n)