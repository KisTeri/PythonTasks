n = int(input("Введите число: "))

def simple_number(n:int):
    simple = True
    if n < 2:
        simple = False
    else:
        for i in range(2, n):
            if n % i == 0:
                simple = False
                break
    if simple:
        print("Да")
    else:
        print("Нет")

simple_number(n)
