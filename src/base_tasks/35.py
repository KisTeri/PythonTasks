n = int(input("Введите число: "))

def divider_of_n(n:int):
    for i in range(1, n+1):
        if n % i == 0:
            print(f"Делитель числа N: {i}")

divider_of_n(n)