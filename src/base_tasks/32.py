n = int(input("Введите число: "))

def summ(n:int):
    s = 0
    while n > 0:
        last_digit = n % 10
        s += last_digit
        n //= 10
    print(f"Сумма цифр числа n: {s}")

summ(n)