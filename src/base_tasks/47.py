n = int(input("Введите число: "))

def simple_number(n:int):
    for number in range(2, n+1):
        simple = True
        for i in range(2, number):
            if number % i == 0:
                simple = False
                break
        if simple:
            print(number)

simple_number(n)