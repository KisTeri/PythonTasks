n = int(input("Введите число: "))

def reverse(n:int):
    m = []
    while n > 0:
        last_digit = n % 10
        m.append(last_digit)
        n //= 10
    print(f"Число в обратном порядке: {"".join(map(str, m))}")

reverse(n)