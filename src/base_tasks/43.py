n = int(input("Введите число: "))

def find_second_max_num(n):
    max_num1 = -1
    max_num2 = -1
    while n > 0:
        digit = n % 10
        if digit > max_num1:
            max_num2 = max_num1
            max_num1 = digit
        elif digit != max_num1 and digit > max_num2:
            max_num2 = digit
        n //= 10
    if max_num2 == -1:
        print("no")
    else:
        print(max_num2)

find_second_max_num(n)