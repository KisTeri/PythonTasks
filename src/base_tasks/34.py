n = int(input("Введите число: "))

def square(n:int):
    for i in range(1, n+1):
        print(f"Число и его квадрат: {i, i*i}")

square(n)