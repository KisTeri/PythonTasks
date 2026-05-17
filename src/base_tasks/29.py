n = int(input("Введите число: "))

def summ(n:int):
    s = 0
    for i in range(1, n+1):
        s += i
    print(f"Сумма чисел от 1 до n: {s}")

summ(n)