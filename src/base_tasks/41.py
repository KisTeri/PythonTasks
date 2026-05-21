n = int(input("Введите число: "))

def find_max_num(n):
    numbers = []
    while n > 0:
        last_digit = n % 10
        numbers.append(last_digit)
        n //= 10
    numbers.sort(reverse=True)
    print(f"Самая большая цифра в числе: {numbers[0]}")


find_max_num(n)