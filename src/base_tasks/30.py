n = int(input("Введите число: "))

def even(n:int):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=" ")

even(n)