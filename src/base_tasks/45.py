n = int(input("Введите число: "))

def find_min_digit(n):
    numbers = []
    while n > 0:
        last_digit = n % 10
        numbers.append(last_digit)
        n //= 10
    numbers.sort()
    if numbers[0] != numbers[1]:
        print(f"Единственная наименьшая цифра в числе: {numbers[0]}")
    else:
        print("Нет")


find_min_digit(n)