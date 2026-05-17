n = int(input("Введите число: "))

def count(n:int):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    print("Количество цифр в числе:", count)

count(n)