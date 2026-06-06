n = int(input("Введите число: "))

def count_digits(n):
    for i in range(10):
        cnt = 0
        num = n
        while num > 0:
            digit = num % 10
            if digit == i:
                cnt += 1
            num //= 10

        print(f"Столько раз {cnt} встречается число {i}")


count_digits(n)
