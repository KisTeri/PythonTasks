n = int(input("Введите число: "))

def check_palindrome(n):
    input_num = n
    backwards = 0
    while n > 0:
        num = n % 10
        backwards = backwards * 10 + num
        n //= 10

    if input_num == backwards:
        print("Палиндром")
    else:
        print("Не палиндром")


check_palindrome(n)